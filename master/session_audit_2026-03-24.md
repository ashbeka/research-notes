# Session Audit - 2026-03-24

This file captures the main decisions and technical conclusions from the March 2026 thesis-reset discussion. It is meant to preserve the reasoning, not just the final scope outcome.

## 1. Repo-State Audit

The implementation repo was audited end-to-end before any scope decision.

Key findings:
- The runnable work is a two-phase Sentinel-2 pipeline, not a completed damage-mapping system.
- Phase 1 is a real DS/classical-prior pipeline on OSCD and MultiSenGE.
- Phase 2 is a real OSCD binary change-segmentation pipeline using raw Sentinel-2 inputs with optional prior channels.
- Phase 3 damage work is still scaffolding, not a complete implementation.

Important implementation caveats preserved from the audit:
- `pca_diff` is the strongest standalone unsupervised OSCD method in the saved Phase 1 test summary.
- `ds_projection` is the most useful current prior for downstream OSCD segmentation.
- The latest strong Phase 2 result is from the 2025-12-15 GPU run.
- The main DS-vs-raw segmentation evidence is still effectively single-seed.
- Phase 1 runtime reporting is not true per-method runtime isolation; timing is measured around the combined tile processing path and then attached back to each method.
- The damage dataset adapter exists as a placeholder, but the training/evaluation path is still OSCD-specific and binary-oriented.

## 2. Research Judgment

The broad historical proposal and the implemented repo had drifted into two different theses.

The discussion concluded that the most defensible current thesis is:
- interpretable unsupervised multispectral priors for Sentinel-2 change segmentation

This was chosen because:
- it matches the implemented code
- it already has real empirical support
- it is narrow enough to finish cleanly
- it still leaves a stronger disaster-damage extension open

The old broad plan was not discarded. It was re-bucketed:
- Active thesis scope:
  - DS-first Sentinel-2 priors and OSCD change segmentation
- Warm extension:
  - xBD-S12 medium-resolution disaster damage mapping
- Cold archive:
  - SSC-heavy pipeline, UAV/edge, MCDA, land-use as a co-equal primary task, DMaaS, IoT, and similar broad system ideas

## 3. Main Scientific Angle

The most promising thesis angle identified in the discussion is:

- the best standalone unsupervised detector is not necessarily the best downstream segmentation prior

Why this matters:
- In Phase 1, `pca_diff` is strongest by AUROC on OSCD.
- In Phase 2, `ds_projection` is the best current prior for improving mean IoU/F1.
- This is more scientifically interesting and more defensible than claiming DS is the strongest unsupervised OSCD detector overall.

## 4. Novelty, Validity, And Applicability Guardrails

The discussion explicitly rejected several overclaims.

Valid claim:
- DS projection is a useful and interpretable prior for supervised OSCD segmentation in the current implementation.

Claims to avoid:
- DS is state of the art for unsupervised OSCD.
- The repo already demonstrates disaster damage mapping.
- The thesis is currently a complete SSC + UAV + MCDA + land-use framework.

Applicability judgment:
- OSCD is still a change benchmark, not a disaster damage benchmark.
- Therefore OSCD alone is not enough for a strong disaster-damage claim.
- xBD-S12 was identified as the best nearby bridge because it keeps the work in the Sentinel/Copernicus regime while making the disaster-damage connection real.

## 5. External Benchmark Discussion

The discussion compared the repo against newer external work.

Most important external comparison:
- Bandara and Patel, WACV 2025, Metric-CD

Conclusion from the discussion:
- Their OSCD comparison is meaningful but not protocol-identical.
- It is the same benchmark family, but not the same evaluation setup as the current repo.
- AUC is the safer cross-paper comparison.
- F1 is only semi-fair because thresholding and averaging details matter.
- Compute-efficiency comparison is not fair unless rerun under controlled conditions.

This point matters because the thesis should not be framed around absolute unsupervised leaderboard claims.

## 6. Why xBD-S12 Was Marked As Warm

xBD-S12 was identified as the strongest nearby extension for three reasons:
- it keeps the work in medium-resolution Sentinel-1/2 space
- it gives the thesis a real disaster-damage bridge
- recent evidence suggests that more complex architectures do not necessarily generalize better on that problem

Implication:
- if there is time after stabilizing the active thesis, xBD-S12 is the best extension candidate
- if there is not time, the thesis remains coherent without it

## 7. Notes-Repo Workflow Decision

The notes-repo duplication problem was also resolved in this discussion.

Operational rule:
- keep one live editable `research-notes` repo only
- use the nested repo inside `DS_damage_segmentation` as the canonical working copy
- do not maintain multiple editable copies in different filesystem locations
- outer repo and inner notes repo remain separate Git repos

This was treated as important because research drift can also happen through file-management drift.

## 8. Planning Anchors Carried Forward

The next planning step should turn the active scope into concrete tasks under three headings:

- Strengthen the active claim
  - multi-seed confirmation
  - cleaner ablations
  - clearer write-up of limitations
- Align notes and implementation
  - keep current thesis docs synchronized with the code and outputs
- Define the warm-extension gate
  - state exactly what must be true before starting xBD-S12 work

## 9. Linked Support Files

- `master/current_scope.md`
- `master/master_outline.md`
- `paths_menu.md`
- `refs_links/benchmark_watchlist.md`
