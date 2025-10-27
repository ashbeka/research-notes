# Drafts Digest (atomic bullets, no info loss)

## [PROB] Problem & Scope
- Disasters (natural/man-made) require rapid post-event damage and land-use mapping to support resilience.
- Current deep learning pipelines are compute-heavy, limiting use in resource-constrained deployments.

## [OBJ] Objectives
- Build a computationally efficient hybrid (subspace + DL) that yields rapid, actionable insights.
- Jointly perform damage assessment + land-use analysis for an integrated operating picture.

## [DATA] Data
- Sentinel-2 multispectral for land-use/land-cover (urban/rural/vegetation).
- xBD pre/post annotated data for building damage classification.
- xView2 to enhance damage-class granularity.
- UAV imagery for localized, high-resolution details.
- Optional real-time feeds from UAVs/IoT sensors to improve adaptability.
- Optional auxiliary LULC datasets for pretraining/evaluation: EuroSAT, MiniFrance, Urban Atlas; Planet Labs for high-cadence updates where available.

## [PRE] Preprocessing
- Noise removal, resolution alignment, multispectral band merging across datasets.
- Augmentation to improve generalization: rotations/flips; small scale/translation; brightness/contrast/gamma jitter; light Gaussian noise/blur (low magnitude). For temporal pairs, apply the same transform to pre/post imagery.

## [METH-SSC] Subspace / Representation
- Sparse Subspace Clustering (SSC) to produce compact, structure-preserving representations for downstream segmentation.
- On-device SSC preprocessing (UAV/edge) to compress before transmission.
- Rationale and analysis: reduce VRAM/bandwidth, preserve manifold structure for noise-robust features, and enable interpretability via coefficients/clusters (to be evaluated with ablations).

## [METH-SUB] Temporal Change (Subspace deltas)
- First-difference subspace to capture abrupt spectral changes post-disaster.
- Second-difference subspace to capture progression/recovery trends across time.

## [METH-UNET] Segmentation
- U-Net consumes subspace outputs for pixel-wise damage and land-use segmentation.

## [PLAN] Deployment
- Edge/server split: on-device preprocessing (e.g., SSC) at UAV/edge to reduce uplink; server-side segmentation (e.g., U-Net).

## [DEC] Decision Layer / Outputs
- Geospatial heatmaps (damage intensity, land-use classes, temporal trends).
- MCDA fuses outputs with criteria (e.g., severity, resource availability) to prioritize recovery.
- Explicit overlays for temporal trends to support triage and recovery planning.

## [EXP] Scope / Evaluation
- Evaluate across Japan’s disaster-prone regions and conflict-affected areas.
- Ablations/baselines: U-Net vs SSC+U-Net; with/without temporal deltas; with/without augmentation; Sentinel-2 only vs +UAV.

## [METRIC] Metrics
- Precision, Recall, F1, IoU (segmentation). (Latency/compute TBD)

## [RESULT] Impact
- Scalable, deployable framework for agencies/NGOs to improve disaster resilience.
- Transferable to infrastructure planning, smart cities, climate monitoring.

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

