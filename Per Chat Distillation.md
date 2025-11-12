# Per-Chat Delta Distillation

**Role:** You are an expert research scribe. Read the **entire chat from first message to last**. Your job is to **COLLECT, not decide**, only the **DELTAS** (new, updated, or conflicting ideas) **relative to the Baseline** I’ll paste. Be neutral; do not infer a preferred approach or add advice.

## Inputs
- **Baseline (canonical)** between markers. Treat it as “what we already have.”
==== BASELINE START ====
[Paste full repo dump here]
==== BASELINE END ====


## Operating Rules
- **Scope:** Collect problem statements; objectives; data sources; preprocessing; modeling approaches (classical/stat/ML/geometry/manifold/harmonic/Lie groups/Fourier/etc.); evaluation setups; metrics; deployment; risks/ethics; gaps; references; reviewer/senpai comments; novelty claims.
- **Delta-only:** Output items **only** if they are **NEW** vs Baseline, **UPDATES** to Baseline, or explicit **CONFLICTS** with Baseline.
- **No bias:** Neutral wording. Do not steer toward any method family.
- **Atomicity + dedup (this chat only):** One idea per unit. Merge true duplicates **inside this chat**; keep alternatives when meaningfully distinct.
- **Specifics:** Include parameters, constraints, examples, citations, reviewer/senpai quotes (short quotes allowed, ≤ ~20 words).
- **Reality checks:** Mark uncertain citations/claims as **to-verify**. If you must infer, label **generated-not-extracted**.
- **Baseline IDs:** If the Baseline has structured IDs (e.g., `D1-TAG-###`), capture them in `baseline_refs`. **Do not invent** new Baseline-style IDs.
- **Chronology first, then thematic grouping.** No advice or recommendations.

## Deliverables (Markdown only, in this order)

### 1) Executive Overview (delta-focused, this chat only)
Write 6–10 lines summarizing what’s **NEW/UPDATED/CONFLICTING** vs Baseline. No decisions or advocacy.

### 2) Chronology Log (delta timeline)
Walk the chat **in order**, listing **only** delta-bearing content. For each relevant turn/block, use bullets:
- **T# – One-line summary**
  - **Delta:** [neutral sentence]
  - **Evidence:** [params/datasets/constraints/short quote ≤20w]
  - **to-verify:** yes/no
  - **baseline_refs:** [IDs/phrases from Baseline, if any]

### 3) Delta Idea Atoms (grouped by discovered themes)
Group atoms under short **Theme** headings. For each atomic delta, render a mini-card like this:

**WEB-<CHAT>-####**  
- **Classification:** new | update | conflict  
- **Idea:** [one neutral sentence]  
- **Evidence:** [1–2 specifics or short quotes]  
- **Alternatives (this chat):** [WEB-<CHAT>-####, …]  
- **Assumptions/Dependencies:** [optional]  
- **Novelty:** yes/no — [1-line rationale]  
- **Gaps:** yes/no — [what’s missing to test/deploy]  
- **baseline_refs:** [matching IDs/phrases/anchors]  
- **difference_summary:** [for update/conflict, 1–2 lines vs Baseline]  
- **Provenance:** [chat title or “Chat-N”; rough date/message indices if visible]  
- **Confidence:** high | medium | low  
- **Status:** open | hypothesis | note | decided

### 4) Alternatives & Conflicts Map (within this chat)
For any cluster with multiple approaches:  
- **Context:** [what need/question]  
- **Alternatives:**  
  - WEB-<CHAT>-#### — [1–2 lines as extracted]  
  - WEB-<CHAT>-#### — [1–2 lines as extracted]  
- **Tradeoffs (as extracted only):** [bullets; no speculation]  
- **Provenance:** [turns/quotes]

### 5) Novelty Board (from this chat)
For each novelty candidate (as claimed in the chat):  
- **Claim:** [neutral]  
- **Why novel:** [1–2 lines]  
- **Closest prior/Baseline:** [item or “none stated”]  
- **To-verify:** yes/no  
- **Provenance:** [turn/quote]

### 6) Gaps & To-Watch (from this chat)
List **concrete** gaps only (compute budgets, AOI/time windows, privacy, metrics definitions, baselines/ablations, dataset coverage, bandwidth/latency, etc.). For each gap:  
- **Gap:** [concise]  
- **Impact:** [why it matters]  
- **Dependency:** [if any]  
- **Provenance:** [turn]  
- **to-verify:** yes/no

### 7) References (deduplicated per chat)
One bullet per citation; **author-year-title-venue** if present; mark incomplete as **to-verify**.

### 8) Machine-Readable Summaries in Markdown Tables (instead of JSONL)
Produce **two Markdown tables** at the end:

**A) Updates & Conflicts (only)**

| id | classification | theme | idea | evidence | alternatives | assumptions | novelty | gaps | baseline_refs | difference_summary | provenance | confidence | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

(Fill one row per `update` or `conflict` atom.)

**B) New Ideas (only)**

| id | classification | theme | idea | evidence | alternatives | assumptions | novelty | gaps | provenance | confidence | status |
|---|---|---|---|---|---|---|---|---|---|---|---|

(Fill one row per `new` atom.)

> Keep cell content concise. Use semicolons for multiple items. Include the chat label in `id` (e.g., `WEB-OLAP-0001`). Do **not** invent Baseline IDs.

## Formatting Constraints
- Use clear Markdown headings and compact bullets.
- Keep quotes under ~20 words.
- **Chronology first**, then thematic grouping.
- If output would exceed limits, end with `CONTINUE: <section>` markers and resume there.

## Execution
1) Read Baseline.  
2) Read the **entire** chat from the very beginning till the end.  
3) Emit only **deltas** vs Baseline, following the deliverables above.  
4) Ask for **RESOURCES** only if the chat explicitly references missing items needed to interpret deltas.
# Per-Chat Delta Distillation

Role
- You are an expert research scribe. Read the entire chat from first to last message. Your job is to COLLECT, not decide, only the DELTAS (new, updated, or conflicting ideas) relative to the Baseline I paste. Be neutral; do not add advice.

Inputs
- Baseline (canonical) between markers. Treat it as "what we already have."
==== BASELINE START ====
[Paste full repo dump here]
==== BASELINE END ====
- One chat transcript between markers. Put a short label on the first line, e.g., "Chat: Geometry Brainstorm, 2025-02-03"
==== CHAT START ====
[Paste the single chat transcript here]
==== CHAT END ====
- Optional resources (paste only if needed to interpret deltas)
==== RESOURCES START ====
[Papers/code/data/meta]
==== RESOURCES END ====
- If the Baseline or chat is missing or incomplete, STOP and ask me to paste them.

Operating rules
- Scope: Collect problem statements; objectives; data; preprocessing; modeling (classical/stat/ML/geometry/manifold/harmonic/Lie groups/Fourier/etc.); evaluation setups; metrics; deployment; risks/ethics; gaps; references; reviewer/senpai comments; novelty claims.
- Delta-only: Emit items only if NEW vs Baseline, UPDATES to Baseline, or explicit CONFLICTS with Baseline.
- No bias: Use neutral wording; do not steer toward any method family.
- Atomicity + dedup (this chat only): One idea per unit. Merge true duplicates inside this chat; keep alternatives when meaningfully distinct.
- Specifics: Include parameters, constraints, examples, citations, short quotes (<= 20 words).
- Reality checks: Mark uncertain citations/claims as to-verify. If you must infer, label generated-not-extracted.
- Baseline IDs: If Baseline has structured IDs (e.g., Dn-TAG-###), capture them in baseline_refs. Do not invent new Baseline-style IDs.
- IDs for this chat: Use WEB-<CHAT>-#### where <CHAT> is a short label (e.g., WEB-GEO-0001).

Deliverables (in this order)
1) Executive Overview (delta-focused)
- 6-10 lines summarizing what is NEW/UPDATED/CONFLICTING vs Baseline (for this chat only). No decisions or advocacy.

2) Chronology Log (delta timeline)
- Walk the chat in order. List only turns that carry deltas.
- T<index> — one-line summary (use visible message index if present)
  - Delta: [neutral sentence]
  - Evidence: [params/datasets/constraints/short quote <= 20w]
  - to-verify: yes/no
  - baseline_refs: [IDs/phrases from Baseline, if any]

3) Delta Idea Atoms (grouped by discovered themes)
- Group under short Theme headings. For each atom:
  - id: WEB-<CHAT>-#### (sequential)
  - classification: new | update | conflict
  - theme: short freeform label
  - idea: one neutral sentence
  - evidence: 1-2 specifics or short quotes
  - alternatives (this chat): [WEB-<CHAT>-####, ...] (if any)
  - assumptions/dependencies: [optional]
  - novelty: yes/no — [1-line rationale]
  - gaps: yes/no — [what is missing to test/deploy]
  - baseline_refs: [matching Baseline IDs/phrases/anchors]
  - difference_summary: [for update/conflict, 1-2 lines vs Baseline]
  - provenance: [chat label + rough date/message indices if visible]
  - confidence: high | medium | low
  - status: open | hypothesis | note | decided

4) Alternatives & Conflicts Map (this chat)
- Context: [what need/question]
- Alternatives:
  - WEB-<CHAT>-#### — [1-2 lines as extracted]
  - WEB-<CHAT>-#### — [1-2 lines as extracted]
- Tradeoffs (as extracted only): [bullets]
- Provenance: [turns/quotes]

5) Novelty Board (this chat)
- For each novelty candidate:
  - Claim: [neutral]
  - Why novel: [1-2 lines]
  - Closest prior/Baseline: [item or "none stated"]
  - to-verify: yes/no
  - Provenance: [turn/quote]

6) Gaps & To-Watch (this chat)
- Concrete gaps only (compute budgets, AOI/time windows, privacy, metrics definitions, baselines/ablations, dataset coverage, bandwidth/latency, etc.). For each:
  - Gap: [concise]
  - Impact: [why it matters]
  - Dependency: [if any]
  - Provenance: [turn]
  - to-verify: yes/no

7) References (deduplicated per chat)
- One bullet per citation; author-year-title-venue if present; mark incomplete as to-verify.

8) Machine-Readable Exports
- A) Updates & Conflicts (Markdown table)

| id | classification | theme | idea | evidence | alternatives | assumptions | novelty | gaps | baseline_refs | difference_summary | provenance | confidence | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

- B) New Ideas (Markdown table)

| id | classification | theme | idea | evidence | alternatives | assumptions | novelty | gaps | provenance | confidence | status |
|---|---|---|---|---|---|---|---|---|---|---|---|

- C) JSONL code blocks (also output these for programmatic merging)
  - updates.jsonl objects: id, classification, theme, idea, evidence, alternatives, assumptions, novelty, gaps, baseline_refs, difference_summary, provenance, confidence, status
  - new.jsonl objects: id, classification, theme, idea, evidence, alternatives, assumptions, novelty, gaps, provenance, confidence, status
- Keep strings concise. Include the chat label in id. Do not invent Baseline IDs.

Formatting & continuations
- Use clear headings and compact bullets.
- Keep quotes under ~20 words.
- If output would exceed limits, end with CONTINUE: <section> markers and resume there.
- Prefer ASCII punctuation (dashes/arrows) to avoid display issues.

Execution
1) Read Baseline.
2) Read the entire chat.
3) Emit only deltas vs Baseline, following deliverables.
4) Ask for RESOURCES only if the chat references missing items needed to interpret deltas.

note: provide a title for the ditilled chat