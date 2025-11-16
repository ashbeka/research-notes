# Placement Plan

## 1. Abstract
- Problem, objectives, and key contribution summary.

## 2. Problem & Gap
- Compute-heavy DL limits field deployment; need fast, deployable triage.

## 3. Objectives & Hypotheses
- Joint damage + land-use; temporal deltas; decision-ready outputs.

## 4. Data & Preprocessing
- Sentinel-2, xBD, xView2, UAV (+ optional IoT); preprocess: noise/resolution/band merge; augmentation; optional auxiliary datasets (MultiSenGE, EuroSAT, MiniFrance, Urban Atlas; Planet Labs if available).
- [OPEN anchors] AOI window specifics; ontology mapping to final labels.

## 5. Methods
### 5.1 Subspace Family (Representation)
- Compact, structure-aware representation via subspace methods; on-device preprocessing at edge when applicable.

### 5.2 Temporal Change Theory
- First/second-order temporal deltas; theory for abrupt vs gradual change.
- Geodesic change detection (optional): manifold-based change indices using Grassmann distances between local PCA subspaces and SPD distances between covariance descriptors, complementing DS projection/cross-residual scores.

### 5.3 Temporal Change Integration in Pipeline
- Where deltas are computed (pre/post U-Net), fusion with representation, and hand-off to segmentation; edge/server split (preprocess on device, segmentation on server) where appropriate.

### 5.4 Segmentation (U-Net)
- U-Net segmentation leveraging compact features.

### 5.5 Decision Layer (MCDA) & Map Products
- Geospatial heatmaps; MCDA criteria and ranking for reconstruction/resource allocation.
- [OPEN anchor] MCDA criteria/weights choice.

## 6. Experiments
- Evaluate in Japan and conflict-affected contexts; include baselines/ablations (with/without temporal deltas; with/without augmentation; S2 only vs +UAV).

## 7. Metrics & Analysis
- IoU/F1/Precision/Recall; add latency/compute once defined.

## 8. Expected Contributions
- Scalable, deployable mapping framework; reusable for preparedness, infra planning, smart cities, climate, with potential service framing (DMaaS dashboard/API/offline edge) and additional triage layers (DS/uncertainty maps) as future extensions.

## 9. Risks, Ethics, Governance
- To populate (ethics, privacy, licenses).

## 10. Timeline & Resources (draft)

- Phase 1 — Literature & DS/subspace grounding (1–2 months)
- Phase 2 — Data selection & preprocessing (AOI, xBD/xView2/Sentinel-2; optional Landsat audit) (1 month)
- Phase 3 — Implementation (3a: DS-only pipeline on MultiSenGE/OSCD with pixel-diff/CVA/PCA-diff/IR-MAD baselines; 3b: SSC + U-Net damage segmentation prototypes) (2–3 months)
- Phase 4 — Validation & ablations (DS vs pixel diff; DS-only vs deep-only; temporal on/off; compute profiling on OSCD and xBD/xView2) (2 months)
- Phase 5 — Writing & presentation prep (1–2 months)

## 11. References
- (placeholder)

## 12. Glossary & Acronyms
- SSC, U-Net, MCDA, xBD, xView2, Sentinel-2, UAV, IoU/F1, etc.
