---
draft_id: D1
date: 2025-10-10
source: ../drafts_raw/D1.txt
---

# Draft 1 — Digest (atomic bullets, no info loss)

## [PROB] Problem & Scope
- D1-PROB-001: Disasters (natural/man-made) require rapid post-event **damage** and **land-use** mapping to support resilience.
- D1-PROB-002: Current deep learning pipelines are **compute-heavy**, limiting use in resource-constrained deployments.

## [OBJ] Objectives
- D1-OBJ-001: Build a **computationally efficient hybrid** (subspace + DL) that yields **rapid, actionable insights**.
- D1-OBJ-002: Jointly perform **damage assessment** + **land-use analysis** for an integrated operating picture.

## [DATA] Data
- D1-DATA-001: **Sentinel-2** multispectral for land-use/land-cover (urban/rural/vegetation).
- D1-DATA-002: **xBD** pre/post annotated data for building damage classification.
- D1-DATA-3: **xView2** to enhance **damage-class granularity**.
- D1-DATA-004: **UAV imagery** for localized, high-resolution details.
- D1-DATA-005: Optional **real-time feeds** from UAVs/**IoT sensors** to improve adaptability.

## [PRE] Preprocessing
- D1-PRE-001: **Noise removal**, **resolution alignment**, **multispectral band merging** across datasets.

## [METH-SSC] Subspace / Representation
- D1-METH-SSC-001: **Sparse Subspace Clustering (SSC)** to produce compact, structure-preserving representations for downstream segmentation.

## [METH-SUB] Temporal Change (Subspace deltas)
- D1-METH-SUB-001: **First-difference subspace** to capture abrupt spectral changes post-disaster.
- D1-METH-SUB-002: **Second-difference subspace** to capture progression/recovery trends across time.

## [METH-UNET] Segmentation
- D1-METH-UNET-001: **U-Net** consumes SSC outputs for pixel-wise **damage** and **land-use** segmentation.

## [DEC] Decision Layer / Outputs
- D1-DEC-001: Output **geospatial heatmaps** (damage intensity, land-use classes, temporal trends).
- D1-DEC-002: **MCDA** fuses outputs with criteria (e.g., severity, resource availability) to **prioritize recovery**.

## [EXP] Scope / Evaluation
- D1-EXP-001: Test across **Japan’s disaster-prone regions** and **war-torn areas** with decimated infrastructure.

## [METRIC] Metrics
- D1-METRIC-001: **Precision**, **Recall**, **F1**, **IoU** (segmentation). *(Latency/compute not specified in D1)*

## [RESULT] Impact
- D1-RESULT-001: **Scalable, deployable** framework for agencies/NGOs to improve disaster resilience.
- D1-RESULT-002: Transferable to **infrastructure planning**, **smart cities**, **climate monitoring**.

## [OPEN] Gaps surfaced by D1
- D1-OPEN-001: **Compute budget** targets (latency/VRAM/GPU-hours).
- D1-OPEN-002: **AOI** + **temporal window** specifics (timestamps, revisit).
- D1-OPEN-003: **MCDA** criteria/weights (AHP/TOPSIS/custom).
- D1-OPEN-004: **Label ontology** mapping (xBD/xView2 → final classes).
- D1-OPEN-005: **Baselines/ablations** list (e.g., U-Net vs SSC+U-Net; with/without temporal).

## [PHRASE] Voice to preserve
- D1-PHRASE-001: “rapid, actionable insights”
- D1-PHRASE-002: “computationally efficient hybrid framework”
