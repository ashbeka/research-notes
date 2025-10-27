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
**Temporal change.** First/second-difference subspaces encode abrupt and gradual spectral shifts.  
**Segmentation.** U-Net consumes subspace outputs to produce pixel-wise damage/land-use maps. If UAV is used in deployment, we operate an **edge/server split** with DR (Dimensionality Reduction) on device and U-Net on server.  
**Decision.** Geospatial heatmaps (damage, land-use, and temporal trends) feed an MCDA module to rank reconstruction priorities. Criteria may include **damage severity, land-use context**, accessibility, and resource availability.


## 5. Experiments
Evaluate on Japan’s disaster-prone regions and conflict-affected areas; report IoU/F1/Precision/Recall. Baselines and ablations will compare U-Net vs SSC+U-Net, with/without temporal deltas, and with/without augmentation.

## 6. Contributions
A scalable, deployable mapping framework for agencies/NGOs; design patterns generalize to **disaster preparedness**, infrastructure planning, smart cities, and climate monitoring.





