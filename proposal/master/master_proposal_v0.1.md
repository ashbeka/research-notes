# Disaster Resilience: Temporal Damage Analysis and Land-Use Classification Using Subspace Methods and U-Net

## Abstract
We propose a computationally efficient hybrid for post-disaster mapping that couples subspace methods with deep learning. Sparse Subspace Clustering (SSC) compacts high-dimensional imagery while preserving structure; U-Net performs pixel-wise segmentation for damage and land-use. Temporal difference subspaces capture progression vs. recovery, and a decision layer (MCDA) turns maps into prioritized actions. The goal is rapid, actionable insights in resource-constrained settings.

## 1. Problem & Gap
Accurate post-disaster assessment is essential for resilience planning, yet prevailing deep models are compute-intensive and slow to deploy where bandwidth/VRAM are scarce. We target a pipeline that maintains segmentation quality while minimizing computational cost.

## 2. Objectives
(i) Jointly segment damage and land-use; (ii) model temporal change via first/second-order subspace deltas; (iii) deliver decision-ready heatmaps with an MCDA layer for triage and resource allocation.

## 3. Data & Preprocessing
We use Sentinel-2 for land-use/land-cover, xBD/xView2 for building damage, and UAV imagery for local detail. Preprocessing includes noise removal, resolution alignment, and multispectral band merging. Optional real-time UAV/IoT streams may enrich situational awareness.

## 4. Methods
**Subspace layer.** SSC produces compact, structure-aware representations.  
**Temporal change.** First/second-difference subspaces encode abrupt and gradual spectral shifts.  
**Segmentation.** U-Net consumes subspace outputs to produce pixel-wise damage/land-use maps.  
**Decision.** Geospatial heatmaps feed an MCDA module to rank reconstruction priorities.

## 5. Experiments
Evaluate on Japan’s disaster-prone regions and conflict-affected areas; report IoU/F1/Precision/Recall. Baselines and ablations will compare U-Net vs SSC+U-Net and with/without temporal deltas.

## 6. Contributions
A scalable, deployable mapping framework for agencies/NGOs; design patterns generalize to infrastructure planning, smart cities, and climate monitoring.
