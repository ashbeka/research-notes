# Drafts Digest (atomic bullets, no info loss)

## [PROB] Problem & Scope
- Disasters (natural/man-made) require rapid post-event damage and land-use mapping to support resilience.
- Current deep learning pipelines are compute-heavy, limiting use in resource-constrained deployments.

## [OBJ] Objectives
- Build a computationally efficient hybrid (subspace + DL) that yields rapid, actionable insights.
- Perform ordinal damage assessment as the primary task, with land-use analysis as a contextual layer for an integrated operating picture.

## [DATA] Data
- Sentinel-2 multispectral for land-use/land-cover (urban/rural/vegetation).
- xBD pre/post annotated data for building damage classification.
- xView2 to enhance damage-class granularity.
- UAV imagery for localized, high-resolution details.
- Optional real-time feeds from UAVs/IoT sensors (e.g., structural integrity, environmental conditions)
  to improve adaptability.
- Optional auxiliary LULC datasets for pretraining/evaluation: EuroSAT, MiniFrance, Urban Atlas; Planet Labs for high-cadence updates where available.
- MultiSenGE Sentinel-2 (13-band, multi-temporal patches) as an unlabeled development testbed for DS behaviour and visualizations (not a primary labeled damage benchmark; details TBD; to-verify).
- Onera Satellite Change Detection (OSCD) as the main labeled 13-band Sentinel-2 benchmark for DS change-detection evaluation (F1/IoU/Precision/Recall + runtime; license and preprocessing to-verify).
- Optional future datasets: SpaceNet and DeepGlobe for urban structures/LULC; Landsat for additional multi-temporal optical context; SAR context (e.g., ALOS PALSAR); OSM roads/buildings as vector overlays (details TBD; to-verify).
- Optional elevation datasets (DSM/DTM/LiDAR) or height proxies aligned with Sentinel-2/xBD/xView2 AOIs to enable height-aware geodesic damage mapping (building collapse and new vertical structures; availability and alignment to-verify).

## [PRE] Preprocessing
- Noise removal, resolution alignment, multispectral band merging across datasets.
- Augmentation to improve generalization: rotations/flips; small scale/translation; brightness/contrast/gamma jitter; light Gaussian noise/blur (low magnitude). For temporal pairs, apply the same transform to pre/post imagery.

## [METH-SSC] Subspace / Representation
- Sparse Subspace Clustering (SSC) to produce compact, structure-preserving representations for downstream segmentation.
- On-device SSC preprocessing (UAV/edge) to compress before transmission.
- Rationale and analysis: reduce VRAM/bandwidth, preserve manifold structure for noise-robust features, and enable interpretability via coefficients/clusters (to be evaluated with ablations).
- Geodesic-weighted temporal SSC (future): regularize SSC codes across time using geodesic affinities (e.g., w_ij = exp(-d_G(i,j)^2/σ^2)) so divergence among geodesic-near neighbors becomes a change cue; objective/hyperparameters TBD.

## [METH-SUB] Temporal Change (Subspace deltas)
- First-difference subspace to capture abrupt spectral changes post-disaster.
- Second-difference subspace to capture progression/recovery trends across time.
- Difference-Subspace (DS) change maps: projection-energy and illumination-robust cross-residual built from PCA bases and a difference subspace (principal-angle interpretability).
- Multi-date DS: second-order "acceleration" over sliding windows to flag surge/recovery.
- Classical pixel-wise differencing will serve as a baseline for change detection; DS maps are expected to outperform it on robustness to noise/illumination and change localization (to be tested with AUROC/IoU ablations).
- Optional future temporal methods: Singular Spectrum Analysis (SSA) and Slow Feature Analysis (SFA) for trend/seasonal/slow-change characterization if sufficient temporal depth is available (integration with DS/SSC to be decided).
- Classical pixel-wise differencing will serve as a baseline for change detection; DS maps are expected to outperform it on robustness to noise/illumination and change localization (to be tested with AUROC/IoU ablations).
- Sliding-window DS: local subspaces S₁(w), S₂(w) and DS D(w) on spatial windows (e.g., 64×64, stride 16–32), with overlapping scores aggregated into per-pixel DS change maps (window/stride/aggregation TBD).
- Period-subspace DS: when multiple images are available per side, stack spectra into “before” and “after” period subspaces and apply DS between them to reduce single-date noise/cloud sensitivity (period definition and scope TBD).
- Band-level DS interpretability: derive per-band weights from the DS basis (e.g., w_b = Σ_i D_{b,i}²) and approximate per-pixel band contributions; optionally run DS on grouped bands (VIS, red-edge, NIR, SWIR, atmos) to separate atmospheric vs surface-driven changes (design TBD).
- Optional Grassmann geodesic change detection: patch-level PCA subspaces at t1/t2 compared via Grassmann geodesic distance d_G to form a local change map S_G; S_G can be used as an additional channel/prior for segmentation (future extension; configuration and placement TBD).
- Optional SPD geodesic change detection: patch-level SPD covariance matrices per time with Riemannian (affine-invariant or Log-Euclidean) geodesic distance S_SPD as a complementary dispersion/texture-aware change score (future extension).
- Multi-geometry DamageScore (hypothesis): fuse DS residual-based scores, S_G, S_SPD, and encoder-feature differences into a single scalar damage score for triage and MCDA; weights to be calibrated with AUROC/ROC analysis.
- Celik-style unsupervised baseline: local h×h PCA features followed by k-means (k=2) into changed/unchanged as a classical, local-context change-detection method and rapid triage prior (Celik 2009; h≈7–11, S PCs capturing ~90% variance, small-object removal as default heuristics).

## [METH-UNET] Segmentation
- U-Net consumes subspace outputs for pixel-wise damage and land-use segmentation.
- Siamese/change-aware U-Net variant with optional DS prior channel for damage (T1/T2) or concatenated DS prior for change-aware inputs.
- DS-gated compact U-Net (future): use DS-derived unsupervised change masks as ROI gates so a compact U-Net runs only on likely-changed regions, to reduce latency and VRAM; requires ablations vs full-frame segmentation (accuracy vs compute).
- External supervised reference (ChangeOS): deep object-based semantic change-detection framework that jointly localizes buildings and classifies damage from pre/post imagery with object-consistent supervision and end-to-end optimization (ChangeOS; external baseline/design pattern, not in-scope to implement in the master-phase).

## [PLAN] Deployment
- Edge/server split: on-device preprocessing (e.g., SSC) at UAV/edge to reduce uplink; server-side segmentation (e.g., U-Net).
- Quantized U-Net (e.g., TFLite) for edge; sliding-window DS exporter (GeoTIFF) with YAML/CLI.

## [DEC] Decision Layer / Outputs
- Geospatial heatmaps (damage intensity, land-use classes, temporal trends).
- MCDA fuses outputs with criteria (e.g., severity, resource availability) to prioritize recovery.
- Explicit overlays for temporal trends to support triage and recovery planning.
- Export artifacts: weights.json for criteria and priority GeoTIFF + quick-look PNG.

## [EXP] Scope / Evaluation
- Evaluate across Japan’s disaster-prone regions and conflict-affected areas (or other disasters).
- Ablations/baselines: U-Net vs SSC+U-Net; optional SegNet baseline; with/without temporal deltas; with/without augmentation; Sentinel-2 only vs +UAV.
- DS-only vs deep-only baselines; 1st vs 2nd-order DS; geodesic vs projection calibration; report MACs/peak RAM.
- Advanced geodesic ablations (optional): on DS datasets (MultiSenGE, OSCD) and segmentation datasets (xBD/xView2), compare Euclidean vs Grassmann vs SPD geodesic metrics and fused DamageScore, including variants with/without geodesic priors, SSC coupling, and GFK; report AUROC, F1, IoU, and runtime.
- DS-only phase: develop and evaluate DS change detection on MultiSenGE (unlabeled visual assessment) and OSCD (labeled benchmark) with baselines pixel differencing, CVA, PCA-diff, IR-MAD, and a Celik-style local PCA + k-means baseline (Celik 2009); report AUROC, F1, IoU, and runtime per tile.

## [METRIC] Metrics
- Precision, Recall, F1, IoU (segmentation). (Latency/compute TBD)
- Quadratic-weighted kappa for ordinal damage; AUROC for DS change-map evaluation.
- Operational KPIs (hypotheses): time-to-map per tile and end-to-end latency; IoU on changed tiles (e.g., restricted to DS/ROI-positive areas); precision/recall of prioritized regions within a 24–72 hour response window; and aggregate false-alarm reduction / analyst-time savings vs simple baselines (e.g., CVA or pixel differencing) — all to be framed cautiously and backed by experiments where possible.


## [RESULT] Impact
- Scalable, deployable framework for agencies/NGOs to improve disaster resilience.
- Transferable to infrastructure planning, smart cities, climate monitoring,
  and related environmental applications (e.g., deforestation and reforestation analysis).
- Longer-term avenues: few-shot/domain-adapted mapping; GAN-based reconstruction visualization (including view-conditioned city perspectives from satellite imagery); evacuation-route and infrastructure-route analysis built on segmentation outputs; urgent facility placement optimization; LLM-based decision-support summaries for planners; MCDA-based evaluation of reconstruction strategies (e.g., rebuild/upgrade/relocate) as future extensions.
- DS maps as label-free triage products (heatmaps/masks/polygons) usable in GIS workflows for disaster response, with agriculture/infrastructure/environment/insurance applications logged as future evaluation.
- Land-use geodesic drift (Phase-2): track geodesic drift of class-level subspace/SPD prototypes over time as a land-use transition metric feeding into MCDA once land-use segmentation is available.
- Geodesic post-processing (optional): use image-space geodesic distances/shortest paths as an edge-aware prior so change masks respect strong boundaries (e.g., roads, rivers), as an alternative to CRF/morphology.
- PCA/DS-based building reconstruction (future): learn pre-disaster PCA (or geodesic PCA) manifolds for buildings and, post-disaster, reconstruct their likely original structures by projection, using reconstruction residuals as building-level damage maps (lighter-weight alternative or complement to GAN-based reconstructions).
- Graph-based USAR decision layer (future): building-graph models with belief propagation and uncertainty-aware GCNs over multimodal data (e.g., Selvakumaran et al. 2025) as a richer, post-segmentation alternative to the current MCDA decision layer.
- Disaster Damage Mapping as a Service (DMaaS, future framing): package the DS + SSC + U-Net pipeline as a service with a web dashboard, API, and optional offline edge mode for agencies/NGOs, built on the same core methods and map products.
- Uncertainty layers (optional): use lightweight Bayesian deep learning approximations (e.g., MC dropout à la Kendall & Gal 2017) to output epistemic/aleatoric uncertainty maps alongside damage/land-use predictions for risk-aware triage.
- Multi-expert co-design (governance): explicitly involve remote-sensing scientists, ML engineers, civil engineers/emergency managers, GIS analysts, and policy/ethics advisors, with clear responsibilities for AOI/ontology choices, model design, MCDA criteria, and governance.

## [OPEN] Gaps
- Compute budget targets (latency/VRAM/GPU-hours).
- AOI + temporal window specifics (timestamps, revisit cadence).
- MCDA criteria/weights (AHP/TOPSIS/custom).
- Label ontology mapping (xBD/xView2 -> final classes).
- Baselines/ablations list (e.g., U-Net vs SSC+U-Net; with/without temporal).
- Interpretability plan for SSC coefficients/clusters (define analyses and success criteria).
- Uplink/bandwidth budget for edge/server split and real-time feeds.

## [PHRASE] Voice to preserve
- "rapid, actionable insights"
- "computationally efficient hybrid framework"
