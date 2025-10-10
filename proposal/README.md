# Proposal Repo (Distillation Workflow)

This repo holds the distillation workflow using Markdown + one CSV matrix.

## Structure
- `drafts_raw/` — Original drafts as-is.
- `digests/` — One-line bullet digests with stable IDs.
- `deltas/` — Diff reports vs previous drafts.
- `master/` — Outline (Option B), lean outline (alternate), skeleton, and proposal narratives.
- `matrices/` — `coverage_matrix.csv` proving no info loss.
- `glossary.md`, `phrases.md`, `gaps_towatch.md`, `decisions_log.md` — Support files.

## Workflow per draft (Dn)
1. Add raw draft → `drafts_raw/Dn.txt`.  
2. Create digest → `digests/Dn_digest.md` (copy template from D1).  
3. Delta report → `deltas/Dn_vs_D(n-1)_delta.md`.  
4. Update `master/master_outline.md` (Option B) and `master/master_skeleton.md`.  
5. Append rows to `matrices/coverage_matrix.csv` (status: placed/planned).  
6. Update `gaps_towatch.md` and log choices in `decisions_log.md`.  
7. Commit & push.

## Conventions
- One idea per bullet; IDs at start (e.g., `D3-METH-SUB-002`).  
- Keep sections ≤ ~1200 words; split when longer.  
- YAML front matter on digests/deltas for easy parsing.
