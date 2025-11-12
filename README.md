# Research Notes Workflow (Disaster Mapping)

This repo contains a living set of research notes, a canonical idea matrix, and concise proposal text for a pipeline that combines temporal change cues with segmentation and decision support.

## Structure
- `drafts_raw/` — Legacy raw drafts (kept for provenance)
- `master/` — Outline (Option B, concept-only), proposal, skeleton, and LaTeX appendices
  - `master/master_outline.md`
  - `master/master_proposal.md`
  - `master/master_skeleton.md`
  - `master/slides_equations.tex`, `master/appendix_ds_math.tex`
- `coverage_matrix.csv` — Canonical mapping (ideas ↔ sections; status placed/planned; provenance in notes)
- `Drafts_digest.md` — Draft-agnostic digest (human-readable)
- `decisions_log.md`, `gaps_towatch.md`, `glossary.md` — Support docs
- `docs/spec_snippets.md`, `scripts/` — Quick figures (temporal deltas, MCDA demo, payload chart)
- `Per Chat Distillation.md` — Prompt to extract deltas per online chat
- `validate_references.md` — Deduplicated references list for later verification

## Current Workflow (delta-only)
1. If new input exists, add raw text to `drafts_raw/` (optional, for provenance).
2. Extract delta-only ideas; update `coverage_matrix.csv` (status: placed/planned; add provenance notes).
3. Update `master/master_proposal.md` concisely; keep `master/master_outline.md` concept-only (no draft IDs).
4. Update `gaps_towatch.md` with concrete gaps; append a short ADR in `decisions_log.md`.
5. For external/web ideas, run the per-chat prompt and save JSONL (see below), then map into the matrix.

## Conventions
- One idea per bullet; traceability lives in the matrix (idea_id, status, notes).
- Outline remains concept-only; IDs live in the CSV.
- Prefer revising existing sentences over duplicating content.

## Using the Per-Chat Distillation Prompt
- In ChatGPT Web, paste a Baseline dump of this repo and one chat under markers from `Per Chat Distillation.md`.
- Save outputs per chat under `external/web/`:
  - `<label>_updates.jsonl` (update/conflict)
  - `<label>_new.jsonl` (new)
- Concatenate across chats, then map into `coverage_matrix.csv` (we can help ingest these).

## Quick Figures
- See `docs/spec_snippets.md` and run:
  - `python scripts/render_deltas.py --save outputs/figs/deltas_grid.png`
  - `python scripts/render_mcda_demo.py --save outputs/figs/mcda_heatmap.png`
  - `python scripts/render_payload_chart.py --save outputs/figs/payload_vs_m.png`

## What’s Implemented (spec)
- Appendix A (math): notation; temporal deltas; DS sketch; SSC objective; segmentation loss; MCDA; metrics
- Appendix B (implementation): tiling/normalization; deterministic augmentation; baseline training; edge/server payload; ablations; checkpoints

## Next Steps (Plan)
- DS exporter & calibration
  - Implement sliding-window DS exporter (see `coverage_matrix.csv:D11-PLAN-003`).
  - Calibrate DS thresholds (projection vs geodesic); report AUROC; add ROC plotting.
- Damage head (ordinal)
  - Add Siamese/change-aware U-Net with optional DS prior; configure ordinal smoothing + focal/IoU; report quadratic-weighted kappa.
- Compute budget & deployment
  - Profile latency/VRAM/MACs; add Makefile/tasks for quick figs, train, eval.
  - Prototype quantized U-Net (TFLite) for edge (`D11-PLAN-002`).
- External deltas ingestion
  - Run per-chat prompt; save JSONL; ingest into matrix with baseline_refs + provenance.
- Gaps closure
  - Specify AOI/time windows; finalize MCDA weights; complete ontology mapping (xBD/xView2 -> final).
