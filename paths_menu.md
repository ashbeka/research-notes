# Paths Menu

This file keeps the research options visible without letting them blur together. The rule is simple: only one path is active, one path stays warm, and the rest are archived until deliberately revived.

## Active Thesis Scope

This is the current master's-thesis lane.

- Core problem:
  - Can interpretable unsupervised multispectral priors improve supervised Sentinel-2 change segmentation?
- Implemented basis:
  - Phase 1 DS and classical priors on OSCD and MultiSenGE
  - Phase 2 OSCD segmentation with raw bands and optional prior channels
- Current contribution focus:
  - DS projection as an interpretable prior for OSCD segmentation
  - understanding why a good downstream prior may differ from the best standalone unsupervised detector
- Allowed work:
  - ablations
  - multi-seed validation
  - result cleanup
  - thesis writing aligned to this claim

## Warm Extension

This is the only extension path currently allowed to stay close to the mainline.

- xBD-S12 medium-resolution disaster damage mapping

Why this path is warm:
- it is close to the Sentinel-2 change pipeline already implemented
- it connects the thesis to real disaster damage rather than generic urban change
- it is narrower and more realistic than the older broad damage/edge/decision-stack vision

Warm-path rule:
- do not start implementation here until the active thesis core is stabilized or an explicit scope promotion is recorded

## Cold Archive

These paths are preserved for future work, follow-up papers, or post-master research. They are not allowed to redirect the active thesis.

1. SSC-heavy core pipelines and unsupervised clustering as the main backbone
2. UAV / edge deployment, payload optimization, and quantized field inference
3. MCDA decision layers and DMaaS packaging
4. Land-use as a co-equal primary task
5. IoT integration and multimodal operational systems
6. Broad pre-disaster early-warning and vulnerability trajectories
7. Graph-based post-segmentation decision systems

## Promotion Rules

- Active scope changes only through an ADR.
- Warm extension can become active only if time/resources are explicitly committed.
- Cold archive ideas must be promoted deliberately; they should never return through note drift.

## Reading Order

If you need the current state fast, read in this order:

1. `master/current_scope.md`
2. `master/master_outline.md`
3. `decisions_log.md`
