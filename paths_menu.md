# Paths Menu (Research Roadmap)

This file summarizes the main methodological paths captured in the notes repo and how they relate to the locked-in master-phase path.

## Core Master-Phase Path (Locked-In via ADR 0017)

- **Task focus:** Change-detection–centric ordinal building-damage mapping (none/minor/major/destroyed) with land-use as contextual support.
- **Phase 1 — DS-only change detection (Sentinel-2):**
  - Datasets: MultiSenGE (unlabeled dev), OSCD (labeled benchmark).
  - Methods: first/second-order Difference Subspace (projection-energy and cross-residual change maps) on 13-band S2 tiles; optional sliding-window DS and second-order temporal “acceleration”.
  - Baselines: pixel differencing, CVA, PCA-diff, IR-MAD, optional Celik local PCA+k-means.
  - Metrics: AUROC, F1, IoU, runtime per tile.
- **Phase 2 — DS-aware ordinal damage segmentation (VHR + optional medium-res):**
  - Datasets: xBD / xView2 VHR building-damage; xBD-S12 optional Sentinel-1/2 bridge.
  - Methods: U-Net (or similar) for ordinal damage segmentation, consuming S2/VHR imagery with DS/delta channels or DS-gated ROIs; SSC used as unsupervised change-type clustering and baseline on DS/delta features.
  - Metrics: IoU/F1, precision/recall, quadratic-weighted kappa for ordinal labels, plus latency/VRAM once defined.
- **Phase 3+ — Decision layer and products (lightweight in master-phase):**
  - Simple MCDA on top of damage maps (and later land-use) for triage; full DMaaS framing kept as future work.

## Future Paths (Phase-2+ / Additional Papers)

These are derived from `Drafts_digest.md`, `gaps_towatch.md`, `my_notes.md`, `old_notes.md`, and remain valid but out-of-scope for the core master-phase.

1. **Pre-Disaster Temporal / Early-Warning Analysis**
   - Use F-DS/S-DS, DMD, SSA/SFA, RTW, and Fourier-style temporal analysis on long pre-event S1/S2 sequences to detect vulnerability trends, precursors, and repeated-strike patterns.

2. **Medium-Resolution Damage Mapping at Scale (xBD-S12)**
   - Focus on Sentinel-1/2 (~10 m) damage mapping using xBD-S12, with DS and DS-aware networks as candidates for rapid, large-scale disaster mapping.

3. **UAV / Edge Deployment and DS-Gated Segmentation**
   - Quantized, DS-gated U-Net variants running partially on UAV/edge, with subspace/SSC embeddings for uplink reduction; relates to payload charts and edge/server split in `spec_snippets.md` and Appendix B.

4. **Land-Use / Land-Cover and Geodesic Drift**
   - Dedicated land-use segmentation experiments (EuroSAT, MiniFrance, Urban Atlas) and geodesic drift of class-level subspaces/SPD prototypes to quantify land-use transitions and environmental impact.

5. **Building-Level Descriptors and Graph-Based Decision Layers**
   - Per-building descriptor stacks (geometry, spectral indices, DS/deep features, temporal change descriptors) and building-graph models (GCN/BP) for USAR and reconstruction decision-support.

6. **Unsupervised Dataset Construction via DS + SSC**
   - Use first/second-order DS features and SSC clustering on large unlabeled satellite collections (S2, Planet, etc.) to automatically derive granular damage/change-type datasets for pretraining and future models.

> The goal of this file is not to commit to all paths, but to keep a clear, centralized menu of options so future ADRs can promote specific paths into core scope.
