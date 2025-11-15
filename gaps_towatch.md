# Gaps & To-Watch

- [OPEN] Compute targets (latency/image, VRAM, GPU-hours) -> influences 7 and model sizing.
- [OPEN] AOI + temporal window (timestamps, revisit cadence) -> finalize 4 and temporal design.
- [OPEN] SSC details (coefficients vs reconstructions; cluster count) (see Appendix A) -> 5.1.
- [OPEN] Temporal deltas (exact formulation, alignment, fusion location) (see Appendix A) -> 5.2 & 5.3.
- [OPEN] MCDA criteria/weights (AHP/TOPSIS/custom) -> 5.5.
- [OPEN] Damage ontology mapping (xBD/xView2 -> final labels) -> 4.
- [OPEN] Baselines & ablations (U-Net vs SSC+U-Net; optional SegNet baseline; +/- temporal; S2 only vs +UAV) -> 6.
- [OPEN] Ethics/governance (conflict-zone imagery, privacy, licenses) -> 9.
- [OPEN] Clarify MCDA criteria weights with explicit land-use sensitivity and accessibility constraints -> 5.5.
- [OPEN] IoT sensor catalog and fusion specification (structural/environmental signals; where to fuse in pipeline) -> 4 & 5.
- [OPEN] Novelty verification vs literature (SSC + U-Net hybrid for joint damage+LULC in constrained deployments) -> 2 & 8.
- [OPEN] Dataset prioritization under constraints (xBD-first vs multi-dataset framing; role of Sentinel-2-only scenarios) -> 4 & 6.
- [OPEN] Clarify whether deforestation / reforestation is an evaluated task or an illustrative extension
  (affects datasets, experiments, and Expected Contributions) -> 6 & 8.
- [OPEN] Ingest and triage the curated web reference pack (dedup vs existing refs; map key papers to
  Data/Methods/Result and novelty verification) -> 2, 4, 5, 8.
- [OPEN] Master-phase scope vs full pipeline (disaster damage-level classification with land-use as context vs joint damage+land-use classification vs infrastructure-planning/urgent-facilities framing; long-term DS+MCDA pipeline) -> 1, 3, 5, 8.
- [OPEN] Auxiliary datasets (SpaceNet, DeepGlobe, ALOS PALSAR, OSM overlays) — clarify which are core vs future extensions -> 4 & 6.
- [OPEN] Future directions (few-shot, domain adaptation, GAN reconstruction, evacuation-route mapping, LLM-based decision-support) — track as post-master roadmap, not core scope -> 2, 5, 8.
- [OPEN] Infrastructure planning tasks (urgent facility placement, infrastructure-route design) — keep as Phase-2/future extension unless scope is formally pivoted -> 5, 6, 8.
- [OPEN] Segmentation-to-decision narrative ("what then?" from SSC+U-Net outputs to prioritized reconstruction actions) -> 5.5, 6, 8.
- [OPEN] Difference-Subspace vs pixel-wise differencing baseline (define classical pixel-difference change maps and compare against DS using AUROC/IoU) -> 5.2, 6.
- [OPEN] DS task taxonomy and metrics (treat DS as unsupervised change detection/subspace learning evaluated separately from supervised segmentation) -> 5.2, 6, 7.
- [OPEN] Optional temporal methods (SSA, SFA) — decide if/when to add them as future extensions and how they integrate with DS+SSC pipeline -> 5.2, 6.
- [OPEN] Temporal depth vs advanced temporal methods (SSA/SFA) — audit number of time steps per dataset/AOI to see if these methods are practical -> 4, 5.
- [OPEN] Title naming (generic subspace methods vs SSC-specific wording in the title) -> 1 & 6.
- [OPEN] SSC deployment location profiling (on-UAV vs ground-station vs central server; payload/latency tradeoffs) -> 4, 5, 7.
- [RESERVED] Geodesic change detection (if added later) — anchor in 5.2 (theory) and 5.3 (integration).
 - [OPEN] DS thresholds & calibration (projection vs geodesic) -> 5.2; report AUROC for change-maps.
 - [OPEN] Ordinal loss/smoothing setting for damage head -> 5.4; confirm metrics include quadratic-weighted kappa.
