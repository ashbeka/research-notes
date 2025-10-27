# Proposal Repo (Research Notes Workflow)

This repo holds the distillation workflow using Markdown + one CSV matrix.

## Structure
- `drafts_raw/` — Legacy raw drafts (kept for provenance).
- `digests/` — Historical digest of Draft 1 (D1) only.
- `deltas/` — Legacy diff reports (D1 era).
- `master/` — Outline (Option B, concept-only), skeleton, and proposal narratives.
- `matrices/` — `coverage_matrix.csv` is canonical mapping (ideas ↔ sections; status placed/planned).
- `glossary.md`, `phrases.md`, `gaps_towatch.md`, `decisions_log.md` — Support files.

## Current Workflow (delta-only)
1. If new input exists, add raw text to `drafts_raw/` (legacy storage; optional).
2. Extract delta-only ideas; update `matrices/coverage_matrix.csv` (status: placed/planned; preserve provenance in notes).
3. Update `master/master_proposal_v0.1.md` concisely; keep `master/master_outline.md` concept-only (no draft IDs).
4. Update `gaps_towatch.md` with concrete gaps; append a brief ADR in `decisions_log.md`.
5. Commit locally. External/web ideas should first be collected as WEB-#### (JSONL or notes) and then mapped into the matrix.

## Conventions
- One idea per bullet; traceability lives in the matrix (idea_id, status, notes).
- Outline stays concept-only; IDs remain in the CSV.
- Keep sections concise; revise existing sentences rather than duplicating.


