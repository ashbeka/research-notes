# Disaster Resilience: Temporal Damage Analysis and Land-Use Classification Using Subspace Methods and U-Net

## Abstract
We propose a computationally efficient hybrid for post-disaster mapping that couples subspace methods with deep learning. Sparse Subspace Clustering (SSC) compacts high-dimensional imagery while preserving structure; U-Net performs pixel-wise segmentation for damage and land-use. Temporal difference subspaces capture progression vs. recovery, and a decision layer (MCDA) turns maps into prioritized actions. The goal is rapid, actionable insights in resource-constrained settings.

## 1. Problem & Gap
Accurate post-disaster assessment is essential for resilience planning, yet prevailing deep models are compute-intensive and slow to deploy where bandwidth/VRAM are scarce. We target a pipeline that maintains segmentation quality while minimizing computational cost. Efficiency matters at the edge and over constrained uplinks: pre-embedding on UAVs or ground stations reduces bandwidth, while surge scenarios still constrain server VRAM/latency.

## 2. Objectives
(i) Jointly segment damage and land-use; (ii) model temporal change via first/second-order subspace deltas; (iii) deliver decision-ready heatmaps with an MCDA layer for triage and resource allocation.

## 3. Data & Preprocessing
We use Sentinel-2 for land-use/land-cover, xBD/xView2 for building damage, and UAV imagery for local detail. Preprocessing includes noise removal, resolution alignment, multispectral band merging, and data augmentation to improve generalization (rotations/flips; small scale/translation; brightness/contrast/gamma jitter; light Gaussian noise/blur at low magnitude). For temporal pairs, the same transform is applied to pre/post imagery. Optional real-time UAV and IoT streams can enrich situational awareness by fusing localized imagery with ground-level signals. Optional auxiliary LULC datasets for pretraining/eval: EuroSAT, MiniFrance, Urban Atlas; Planet Labs for cadence if available.

## 4. Methods
**Subspace layer.** SSC produces compact, structure-aware representations. In case of UAV, SSC (or any other dimensionality reduction method) could be run on-device. SSC reduces VRAM and bandwidth needs, preserves manifold structure for noise-robust features, and yields interpretable coefficients/clusters that can be analyzed; ablations will quantify the trade-offs.
**Temporal change.** First/second-difference subspaces encode abrupt and gradual spectral shifts; practical DS heads include projection-energy and cross-residual maps built from PCA/difference subspaces, with optional Grassmann geodesic index for calibration.  
**Segmentation.** U-Net consumes subspace outputs to produce pixel-wise damage/land-use maps. If UAV is used in deployment, we operate an **edge/server split** with DR (Dimensionality Reduction) on device and U-Net on server.  
**Decision.** Geospatial heatmaps (damage, land-use, and temporal trends) feed an MCDA module to rank reconstruction priorities. Criteria may include **damage severity, land-use context**, accessibility, and resource availability.


## 5. Experiments
Evaluate on Japan’s disaster-prone regions and conflict-affected areas; report IoU/F1/Precision/Recall. Baselines and ablations will compare U-Net vs SSC+U-Net, with/without temporal deltas, and with/without augmentation; include DS-only vs deep-only, geodesic vs projection calibration, and AUROC for DS change-maps.

## 6. Contributions
A scalable, deployable mapping framework for agencies/NGOs; design patterns generalize to **disaster preparedness**, infrastructure planning, smart cities, and climate monitoring.





## Appendix A - Mathematical Specification

### A.1 Notation and data model
- Let x_{i,t} in R^d denote the d-dimensional spectral vector for pixel i at time t. Stack n pixels at time t into X_t in R^{d x n}.
- Per-band z-score normalization: tilde{x}_{i,t} = (x_{i,t} - mu)/sigma, with mu and sigma estimated on the training set (per band).

### A.2 Temporal differences (per-pixel)
- Delta1_i = tilde{x}_{i,t2} - tilde{x}_{i,t1}
- Delta2_i = tilde{x}_{i,t3} - 2*tilde{x}_{i,t2} + tilde{x}_{i,t1}
- Alignment: compute tilde{x}_{i,*} after co-registration/warping of X_t to a common grid. If timestamps vary, select nearest neighbors within a bounded window [t1, t2, t3].
- Optional robust delta (per component): rho(Delta) = 0.5*Delta^2 if |Delta| <= delta; else delta*(|Delta| - 0.5*delta)

### A.2a Difference-Subspace change detection (sketch)
- Compute PCA bases Phi (t1) and Psi (t2) from X_{t1}, X_{t2}. Let their principal angles be given by the SVD of Phi^T Psi.
- Define a difference subspace D from the orthogonal complement of the common subspace; a simple change score per pixel is p_i = || D^T (x_{i,t2} - x_{i,t1}) ||_2.
- Illumination-robust variant uses cross-residual terms instead of plain differencing.
- Optional Grassmann geodesic distance between subspaces: d_G(Phi, Psi) = sqrt( sum_k theta_k^2 ), used as a scale-free change index.

### A.3 Sparse Subspace Clustering (SSC)
- Data matrix X in R^{d x n} stacks the input vectors (choose X = X_{t2}, or [X_{t2}; Delta1; Delta2] if fusing deltas before SSC).
- Elastic-net SSC objective (columnwise self-representation):
  minimize_C  0.5*||X - X*C||_F^2 + lambda*||C||_1 + (beta/2)*||C||_F^2,  subject to diag(C) = 0
- Affinity and clustering: W = abs(C) + abs(C)^T; run spectral clustering on W to obtain K subspaces/clusters.
- Derived features per column i:
  - Coefficients c_i (i-th column of C)
  - Reconstruction residual r_i = ||x_i - X*c_i||_2
  - Cluster label k_i (from spectral clustering), and optional one-hot embedding
  - Local affinity stats (e.g., sum of top-p affinities)
- Edge variants: approximate c_i via Lasso/OMP; select K via silhouette or eigengap.

### A.4 Feature stack for segmentation
- Base: f_i(base) = tilde{x}_{i,t2}
- Temporal fusion options:
  - Pre-SSC: f_i = [tilde{x}_{i,t2}; Delta1_i; Delta2_i; g_i], where g_i are SSC-derived features (e.g., r_i, cluster one-hot)
  - Post-SSC: f_i = [tilde{x}_{i,t2}; Delta1_i; Delta2_i], with SSC-derived g_i concatenated to encoder features
- Optional dimensionality reduction: PCA to m <= d' dims if memory/compute constrained.

### A.5 Segmentation and loss
- Input to U-Net: tensor of shape B x C x H x W with C matching channel count of the feature stack.
- Composite loss:
  L = alpha*L_CE + (1 - alpha)*L_Dice
  where the multi-class Dice term is
  L_Dice = 1 - (1/K) * sum_k ( 2*sum_p yhat_{k,p}*y_{k,p} + epsilon ) / ( sum_p yhat_{k,p} + sum_p y_{k,p} + epsilon )
  and L_CE is the standard multi-class cross-entropy.

### A.6 Decision scoring (MCDA)
- For region R_j, normalized criteria q_j in R^m (e.g., damage severity, land-use sensitivity, accessibility) and weights w in R^m, sum_k w_k = 1, w_k >= 0.
- Region score and ranking: s_j = w^T * q_j.

### A.7 Metrics and system measures
- Per class k: IoU_k = TP_k/(TP_k + FP_k + FN_k), mIoU = average over classes. Report Precision, Recall, F1.
- System measures: latency/image (ms), throughput (imgs/s), peak VRAM (GB), uplink bytes/tile (see B.4).
- For temporal methods, include change-detection accuracy in ablations (+/-Delta1/Delta2).

## Appendix B - Implementation Specification

### B.1 Co-registration, tiling, normalization
- Tile size 512 x 512, stride 256; bilinear resampling to a common grid; mask NODATA; per-band z-score normalization.

### B.2 Augmentation (deterministic seeds)
- Rotations {0, 90, 180, 270}, horizontal/vertical flips; scale 0.9-1.1; translate <= 5% of image; brightness/contrast +/-10-15%; gamma 0.9-1.1; Gaussian noise sigma in [0, 0.01]; Gaussian blur sigma in [0.5, 1.0].
- Temporal pairing: apply the same sampled transform to both pre and post images (and masks).

### B.3 Baseline training config (CPU-friendly defaults)
- Optimizer: Adam (lr=1e-3, betas=(0.9, 0.999)); epochs=10 (dev), 50 (full); batch=4 (increase if memory allows).
- Checkpoint best mIoU; early stop on validation plateau; log loss/mIoU per epoch.

### B.4 Edge/server split and payload
- If pre-embedding to m dims is used for T tiles/s at resolution H x W with 32-bit floats, uplink ~= T*(H*W*m*4) bytes/s.
- Raw uplink for 16-bit imagery would be T*(H*W*d*2) bytes/s. Target >= 5-10x reduction to justify edge preprocessing.

### B.5 Experiments and ablations (toggles)
- +/- temporal deltas (Delta1/Delta2); +/- augmentation; Sentinel-2 only vs +UAV; SSC features on/off; pre- vs post-SSC fusion.

### B.6 Compute budget checkpoints
- Record latency/image, VRAM peak, and wall-clock/epoch; enforce caps to keep runs feasible within a week.
