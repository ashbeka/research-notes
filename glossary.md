# Glossary & Acronyms

## Data & Datasets
**Sentinel-2** - Multispectral satellite imagery (13 bands) for land-use/land-cover tasks.

**xBD / xView2** - Large-scale building-damage datasets with pre/post imagery and damage labels.

**EuroSAT** - Sentinel-2 based labeled LULC dataset (patch-based), useful for pretraining/evaluation.

**MiniFrance** - High-resolution LULC dataset covering urban and rural scenes.

**Urban Atlas** - Copernicus standardized urban land-use/land-cover layers for Europe.

**Planet Labs** - Commercial provider of high-cadence Earth imagery (daily coverage) for selected regions.

**Multispectral imagery** - Imagery captured in multiple spectral bands (e.g., visible and infrared), enabling richer analysis of land cover, vegetation, water, and urban surfaces.

**MultiSenGE** - Remote sensing dataset mentioned for potential disaster mapping evaluation; exact specification to be verified (to-verify).

## Methods & Models
**SSC (Sparse Subspace Clustering)** - Unsupervised method modeling data as a union of low-dimensional subspaces; yields compact, structure-aware features.

**U-Net** - Encoder-decoder CNN with skip connections for pixel-wise segmentation.

**Subspace coefficients** - Weights from SSC that express a sample as a combination of others within its subspace; useful for clustering and interpretability analyses.

## Geometry & Geodesics
**Geodesic (on a manifold)** - The straightest possible path between two points on a curved space: locally distance-minimizing in the intrinsic metric (free-fall trajectories in General Relativity follow geodesics of spacetime).

**Geodesic change detection** - Family of methods that quantify change by measuring geodesic distances on appropriate manifolds (e.g., Grassmann for local PCA subspaces; SPD for covariance descriptors) between pre- and post-disaster representations, then turning these distances into patch- or pixel-level change maps, optionally fused with Difference-Subspace scores.

## Temporal & Change
**Temporal pair** - Co-registered pre- and post-disaster images for the same AOI and timestamps; used for change detection and temporal deltas.

**Temporal difference subspace** - First-order difference highlights abrupt change; second-order difference emphasizes progression or recovery patterns in spectral space.

## Deployment
**UAV** - Unmanned Aerial Vehicle; provides high-resolution local imagery.

**Edge/server split** - Deployment pattern where lightweight preprocessing (e.g., SSC) runs on UAV/edge devices to reduce bandwidth, while heavier segmentation (e.g., U-Net) runs on a server.

## Products & Decision
**Geospatial heatmap** - A spatial raster summarizing pixel-wise outputs (e.g., damage intensity, land-use categories, temporal trends) for decision support.

**MCDA (Multi-Criteria Decision Analysis)** - Family of methods (e.g., AHP, TOPSIS) for combining multiple criteria into a ranked set of options.

## Metrics & Evaluation
**IoU / F1 / Precision / Recall** - Standard segmentation metrics.

## Concepts & Taxonomy
**Disaster resilience** - Ability of a city/system to analyze, respond to, and recover from disasters; requires precise land-use and structural-damage insights for efficient recovery.

**AOI (Area of Interest)** - The geographic footprint under analysis; defines tiling, retrieval, and evaluation extents.

**Urban resilience** - In this project, the ability of cities to respond to and recover from disasters using data-driven land-use and damage insights derived from satellite imagery and hybrid ML models.

**Damage classes** - Typical label schema for building-damage segmentation/classification; often four levels (none, minor, major, destroyed) as in xView2; xBD and others use similar ordinal tiers.

**Damage ontology** - A cross-dataset mapping that reconciles differing label sets (e.g., xBD vs xView2) into a unified schema for training/evaluation.

**rapid, actionable insights, computationally efficient hybrid framework**

**Bi-temporal (two time dimensions)**
