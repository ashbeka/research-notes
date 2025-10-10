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
