# Current Thesis Scope

Status date: 2026-03-24

This file is the active source of truth for the master's-thesis direction. It translates the implementation state into a clean research scope and keeps preserved alternatives from muddying the active work.

## Current Implemented State

The implementation repo currently supports a two-phase Sentinel-2 pipeline:

- Phase 1:
  - Unsupervised change priors on OSCD and MultiSenGE using Difference Subspace (DS) and classical baselines.
- Phase 2:
  - Supervised binary OSCD change segmentation using raw Sentinel-2 bands with optional prior channels from Phase 1.

Latest substantial completed run:
- Phase 2 GPU run dated 2025-12-15.

What is not yet implemented in substance:
- A real damage-segmentation pipeline on xBD, xView2, or xBD-S12.
- Multi-class damage losses, metrics, and training/evaluation integration.

## Locked Thesis Direction

The active thesis is:

- Mainline claim:
  - Interpretable unsupervised multispectral change priors, especially DS projection, can improve supervised Sentinel-2 change segmentation on OSCD.
- Mainline question:
  - Which prior characteristics make a change score useful downstream as a segmentation prior, even when that prior is not the strongest standalone unsupervised detector?

This means the thesis is currently about:
- DS-first Sentinel-2 change understanding
- Prior-assisted OSCD change segmentation
- A clean bridge toward later damage work

This means the thesis is not currently claiming:
- state-of-the-art unsupervised OSCD change detection
- a finished disaster damage-mapping system
- a full SSC + UAV + MCDA + land-use platform

## Why This Direction Was Chosen

This direction is the most mature and defensible because:

- it matches the implemented code and saved outputs
- it already has a real empirical result
- it can be completed as a coherent master's-thesis core
- it still leaves a scientifically stronger extension path open

The broader historical proposal was intentionally not chosen as the active thesis because it mixes too many tasks and weakens execution.

## Evidence To Carry Forward

Current implementation evidence that should anchor the thesis narrative:

- Phase 1:
  - `pca_diff` is the strongest standalone unsupervised OSCD method in the saved test summary by AUROC (`0.813`).
  - `ds_projection` is lower as a standalone detector (`0.755` AUROC) but remains competitive with simple classical baselines.
- Phase 2:
  - Raw-only U-Net mean IoU/F1: `0.223 / 0.343`
  - Raw + DS projection prior mean IoU/F1: `0.273 / 0.401`
  - DS prior improves IoU on 8 of 10 held-out OSCD test cities in the latest main run.

The most interesting scientific tension in the repo is:

- the best standalone unsupervised detector is not the best downstream prior

That is currently more promising as a thesis contribution than claiming absolute unsupervised change-detection novelty.

## Validity And Novelty Guardrails

Use these guardrails when writing or presenting:

- Do say:
  - DS projection is a useful and interpretable prior for supervised OSCD segmentation in the current implementation.
- Do not say:
  - DS is the strongest unsupervised OSCD detector overall.
- Do not say:
  - the project already demonstrates disaster damage mapping.

External comparison note:
- Recent unsupervised OSCD work reports much stronger AUC/F1 under different, more complex protocols. Use that to avoid overclaiming, not to dismiss the current result.
- See `refs_links/benchmark_watchlist.md` for the paper/repo list and the protocol caveats behind that statement.

## Benchmark Comparison Discipline

- Same dataset family does not automatically mean same benchmark protocol.
- For external OSCD comparisons, AUC is the safer first comparison.
- F1 comparisons require thresholding and averaging details to be checked.
- Compute comparisons are not fair unless methods are rerun under aligned conditions.

## Main Limitations

- The main DS-vs-raw segmentation result is still effectively single-seed.
- OSCD is a binary urban change dataset, not a disaster damage dataset.
- The damage adapter and template are not integrated into a runnable pipeline.
- Some older notes and proposal text still reflect a broader pre-lock vision and should be treated as historical unless updated.

## Three Buckets

### 1. Active Thesis Scope

This bucket is allowed to drive current implementation, writing, and experiment planning.

- Phase 1 priors on OSCD and MultiSenGE
- Phase 2 OSCD change segmentation with priors
- Thesis framing around interpretable priors for Sentinel-2 change segmentation
- Validation and ablation work that strengthens the DS-prior claim

### 2. Warm Extension

This bucket contains one nearby path that may be activated if time permits.

- xBD-S12 medium-resolution disaster damage mapping

Why this extension is warm:
- it is close to the current Sentinel-2 change pipeline
- it is more thesis-relevant to disaster damage than OSCD alone
- recent xBD-S12 work suggests medium-resolution damage mapping is viable and that more complex models do not necessarily generalize better

Warm-extension rule:
- Do not let this bucket redirect the main thesis until the active scope is stabilized or an explicit decision is taken.

### 3. Cold Archive

These ideas are preserved, but they are not allowed to compete with the active thesis.

- SSC-heavy core pipeline
- UAV / edge deployment
- MCDA decision layer
- land-use as a co-equal primary task
- DMaaS framing
- IoT integration
- graph-based decision layers
- broad pre-disaster early-warning work

Archive rule:
- Keep them visible for future papers or post-master work, but do not let them expand the current scope.

## Promotion Rules

- Active -> remains active until explicitly replaced by an ADR.
- Warm -> active only if:
  - the active thesis core is stable, and
  - time/resources are explicitly committed, and
  - the change is recorded in `decisions_log.md`.
- Cold archive -> warm or active only through a deliberate ADR, never through drift.

## Planning Anchors For The Next Step

The next planning pass should build tasks under three headings:

- Strengthen the active claim
  - multi-seed confirmation, better ablation discipline, clearer limitations
- Align notes and implementation
  - update historical wording so the current thesis is easy to recover
- Define the warm-extension gate
  - decide what must be true before xBD-S12 work is allowed to start
- External benchmark preparation
  - collect protocol details and runnable external baselines before making strong comparative claims
