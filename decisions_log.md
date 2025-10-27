# Decisions (Light ADRs)

## 0001 — Source of Truth = Markdown + CSV
Context: Need human+AI friendly workflow.  
Decision: Keep repo in Git; Markdown + one CSV matrix.  
Consequences: Easy diffs; reproducible; Word only for export.

## 0002 — Idea ID Convention
Format: D{n}-{TAG}-{###}. Tags: PROB, OBJ, DATA, PRE, METH-SSC, METH-SUB, METH-UNET, DEC, EXP, METRIC, RESULT, RISK, ETHICS, PLAN, OPEN, PHRASE.

## 0003 — Methods Split (Option B)
Decision: Use Option B (theory → integration → segmentation → decision) for clearer growth when new methods appear.  
Consequence: Stable anchors for future D2+ additions (e.g., geodesic CD).

## 0004 — D2 Integration (UAV emphasis, on-device SSC, edge/server split)
Decision: Prioritize UAV imagery in constrained contexts; allow SSC preprocessing on device; adopt edge/server split (SSC on UAV/edge, U-Net on server); include land-use as an explicit MCDA criterion; extend reuse to disaster preparedness.
Consequences: Outline amended (§5.1, §5.3); proposal text updated (Data/Methods/Decision/Contributions); matrix rows added/updated; new gaps opened for bandwidth, privacy, and feasibility profiling.

## 0006  ED4 Integration (training augmentation)
Context: D4 adds explicit data augmentation for xBD/xView2 training to improve generalization.  
Decision: Add PRE item D4-PRE-001; update proposal Data & Preprocessing to include augmentation; add outline anchor; append matrix row.  
Consequences: Training procedure clarified; outline and matrix aligned; no other changes or new gaps.
## 0005 ?ED3 Integration (IoT adaptability + temporal trends)
Context: D3 reiterates the core hybrid and clarifies adaptability via UAV+IoT fusion and explicit temporal trend overlays in decision outputs.  
Decision: Update proposal wording in Data/Methods/Decision; fix typos; add D3 provenance in matrix for D1-DATA-005; backfill matrix with D2-PLAN-001 referenced in outline.  
Consequences: Clearer data integration narrative; consistent matrix/outline; no new method families or IDs introduced for D3; no new gaps.

## 0007 ?ED7 Integration (aux datasets + interpretability)
Context: D7 adds auxiliary LULC datasets (EuroSAT, MiniFrance, Urban Atlas, Planet Labs) and requests clearer efficiency rationale and SSC��U?Net benefits; interpretability needs explicit treatment.
Decision: Add matrix rows D7-DATA-006..009 (planned) and OPEN D7-OPEN-006; update proposal (Problem & Gap efficiency sentence; Data auxiliary datasets; Methods SSC rationale); add outline anchors.
Consequences: Broader dataset options without scope creep; interpretability tracked as an OPEN item; outline/matrix synced; no new method families.
