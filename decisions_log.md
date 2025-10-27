# Decisions (Light ADRs)

## 0001 — Source of Truth = Markdown + CSV
Context: Need human+AI friendly workflow.
Decision: Keep repo in Git; Markdown + one CSV matrix.
Consequences: Easy diffs; reproducible; Word only for export.

## 0002 — Idea ID Convention
Format: D{n}-{TAG}-{###}. Tags: PROB, OBJ, DATA, PRE, METH-SSC, METH-SUB, METH-UNET, DEC, EXP, METRIC, RESULT, RISK, ETHICS, PLAN, OPEN, PHRASE.

## 0003 — Methods Split (Option B)
Decision: Use Option B (theory → integration → segmentation → decision) for clearer growth when new methods appear.
Consequence: Stable anchors for future additions (e.g., geodesic change detection).

## 0004 — D2 Integration (UAV emphasis, on-device SSC, edge/server split)
Decision: Prioritize UAV imagery in constrained contexts; allow SSC preprocessing on device; adopt edge/server split (SSC on UAV/edge, U-Net on server); include land-use as an explicit MCDA criterion; extend reuse to disaster preparedness.
Consequences: Outline amended (§5.1, §5.3); proposal text updated (Data/Methods/Decision/Contributions); matrix rows added/updated; new gaps opened for bandwidth, privacy, and feasibility profiling.

## 0005 — D3 Integration (IoT adaptability + temporal trends)
Context: D3 reiterates the core hybrid and clarifies adaptability via UAV+IoT fusion and explicit temporal trend overlays in decision outputs.
Decision: Update proposal wording in Data/Methods/Decision; fix typos; add D3 provenance in matrix for D1-DATA-005; backfill matrix with D2-PLAN-001 referenced in outline.
Consequences: Clearer data integration narrative; consistent matrix/outline; no new method families or IDs introduced for D3; no new gaps.

## 0006 — D4 Integration (training augmentation)
Context: D4 adds explicit data augmentation for xBD/xView2 training to improve generalization.
Decision: Add PRE item D4-PRE-001; update proposal Data & Preprocessing to include augmentation; add outline anchor; append matrix row.
Consequences: Training procedure clarified; outline and matrix aligned; no other changes or new gaps.

## 0007 — D7 Integration (aux datasets + interpretability)
Context: D7 adds auxiliary LULC datasets (EuroSAT, MiniFrance, Urban Atlas, Planet Labs) and requests clearer efficiency rationale and SSC→U‑Net benefits; interpretability needs explicit treatment.
Decision: Add matrix rows D7-DATA-006..009 (planned) and OPEN D7-OPEN-006; update proposal (Problem & Gap efficiency sentence; Data auxiliary datasets; Methods SSC rationale); add outline anchors.
Consequences: Broader dataset options without scope creep; interpretability tracked as an OPEN item; outline/matrix synced; no new method families.

## 0008 — D5 Integration (no new additions)
Context: D5 reiterates existing concepts with no novel datasets, methods, or metrics.
Decision: No changes to proposal/outline/matrix; note provenance only.
Consequences: Repo remains consistent; no new IDs; no gaps added.

## 0009 — D6 Integration (no new additions)
Context: D6 restates established ideas (datasets, SSC+U‑Net, metrics, contexts, deployability).
Decision: No changes to proposal/outline/matrix; note provenance only.
Consequences: No new items; matrix unchanged.

## 0010 — D8 Integration (no new additions)
Context: D8 repeats earlier content alongside reviewer comments already addressed in D7.
Decision: No changes to proposal/outline/matrix; note provenance only.
Consequences: No new items; matrix unchanged.

## 0011 — D9 Integration (no new additions)
Context: D9 repeats existing concepts; no new or conflicting ideas.
Decision: No changes to proposal/outline/matrix; note provenance only.
Consequences: No new items; matrix unchanged.

## 0012 — D10 Integration (no new additions)
Context: D10 restates existing concepts (datasets, SSC+U‑Net, temporal deltas, UAV+IoT, products).
Decision: No changes to proposal/outline/matrix; note provenance only.
Consequences: No new items; matrix unchanged.
