# Research Notes Workflow

This repo is the planning and reasoning layer for the disaster/change research program. It records the active master's-thesis scope, preserves alternative paths without mixing them into daily work, and tracks design decisions against the implementation repo.

## Current Source Of Truth
- `master/current_scope.md` - active thesis direction, evidence, limitations, and bucket rules
- `master/master_outline.md` - current thesis outline aligned with the implemented work
- `master/session_audit_2026-03-24.md` - end-to-end audit of the March 2026 reset discussion
- `paths_menu.md` - active scope vs warm extension vs cold archive
- `decisions_log.md` - scope-lock ADRs and later promotions

Historical documents are still preserved, but if an older note disagrees with the files above, the files above win.

## Structure
- `master/` - active scope docs, current outline/skeleton, historical proposal text, and LaTeX appendices
- `phases/` - phase summaries and implementation-facing handoff notes
- `refs_links/benchmark_watchlist.md` - external papers, datasets, repos, and benchmark-comparison notes
- `coverage_matrix.csv` - broader idea inventory; useful for preservation, not the first place to infer active thesis scope
- `drafts_digest.md`, `gaps_towatch.md`, `glossary.md` - supporting notes
- `paths_menu.md` - centralized menu of active, warm, and archived paths
- `decisions_log.md` - lightweight ADRs
- `scripts/`, `spec/`, `spec_snippets.md` - support material and quick figures

## Working Model
- `Active thesis scope`
  - The work that is allowed to drive current writing, implementation, and experiment planning.
- `Warm extension`
  - One nearby path that may be activated if time and results justify it.
- `Cold archive`
  - Preserved ideas that remain visible but cannot pull the thesis off course.

Today the buckets are:
- Active thesis scope: DS-first Sentinel-2 change priors and OSCD change segmentation
- Warm extension: xBD-S12 medium-resolution disaster damage mapping
- Cold archive: SSC-heavy, UAV/edge, MCDA, land-use, DMaaS, and other broader future paths

## Update Workflow
1. When implementation results change, update `master/current_scope.md` first.
2. If the change affects thesis wording, update `master/master_outline.md` and `master/master_skeleton.md`.
3. If the change alters scope or promotes a path, add an ADR to `decisions_log.md`.
4. Keep `paths_menu.md` aligned so active work and preserved alternatives stay separated.
5. Only then update broader historical notes if needed.

## Conventions
- Prefer one explicit source-of-truth sentence over duplicate partial notes.
- Preserve old ideas, but label their bucket clearly.
- Promote a warm or archived path into active scope only through an ADR and a concrete time/resource decision.

## Quick Figures
- `python scripts/render_deltas.py --save outputs/figs/deltas_grid.png`
- `python scripts/render_mcda_demo.py --save outputs/figs/mcda_heatmap.png`
- `python scripts/render_payload_chart.py --save outputs/figs/payload_vs_m.png`
