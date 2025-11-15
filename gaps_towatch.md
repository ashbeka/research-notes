# Gaps & To-Watch

- [OPEN] Compute targets (latency/image, VRAM, GPU-hours) -> influences 7 and model sizing.
- [OPEN] AOI + temporal window (timestamps, revisit cadence) -> finalize 4 and temporal design.
- [OPEN] SSC details (coefficients vs reconstructions; cluster count) (see Appendix A) -> 5.1.
- [OPEN] Temporal deltas (exact formulation, alignment, fusion location) (see Appendix A) -> 5.2 & 5.3.
- [OPEN] MCDA criteria/weights (AHP/TOPSIS/custom) -> 5.5.
- [OPEN] Damage ontology mapping (xBD/xView2 -> final labels) -> 4.
- [OPEN] Baselines & ablations (U-Net vs SSC+U-Net; +/- temporal; S2 only vs +UAV) -> 6.
- [OPEN] Ethics/governance (conflict-zone imagery, privacy, licenses) -> 9.
- [OPEN] Clarify MCDA criteria weights with explicit land-use sensitivity and accessibility constraints -> 5.5.
- [OPEN] IoT sensor catalog and fusion specification (structural/environmental signals; where to fuse in pipeline) -> 4 & 5.
- [OPEN] Novelty verification vs literature (SSC + U-Net hybrid for joint damage+LULC in constrained deployments) -> 2 & 8.
- [RESERVED] Geodesic change detection (if added later) — anchor in 5.2 (theory) and 5.3 (integration).
 - [OPEN] DS thresholds & calibration (projection vs geodesic) -> 5.2; report AUROC for change-maps.
 - [OPEN] Ordinal loss/smoothing setting for damage head -> 5.4; confirm metrics include quadratic-weighted kappa.



