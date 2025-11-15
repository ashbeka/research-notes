# Master Skeleton (rolling bullets)

- Problem: compute-heavy DL limits field deployment → need fast, deployable triage.
- Objective (master-phase): change-detection–centric ordinal damage-level segmentation (none/minor/major/destroyed) as the core task, with land-use as contextual support; temporal deltas and MCDA connect maps to triage decisions.
- Data: Sentinel-2, xBD, xView2, UAV (+ optional IoT); MultiSenGE S2 (unlabeled DS dev testbed) and OSCD (13-band S2 change-detection benchmark) for the DS-only phase; preprocess: noise/resolution/band merge (+ augmentation: geom + radiometric; paired for temporal; light noise/blur).
- Methods: SSC representation; 1st/2nd difference subspaces for damage progression (incl. sliding-window DS change maps); U-Net segmentation; MCDA ranking.
- Experiments: DS-only phase on MultiSenGE/OSCD with pixel-diff, CVA, PCA-diff, IR-MAD baselines; segmentation phase in Japan + conflict-affected contexts; metrics: IoU/F1/Prec/Rec; quadratic-weighted kappa; AUROC for DS maps; latency/VRAM TBD.
- Contributions: scalable + deployable change-detection and damage-mapping core; reusable later for land-use, infra planning, smart cities, climate monitoring.
- Open: compute budget, AOI/time window, MCDA criteria, ontology mapping, ablations, DS sliding-window design, DS-only vs hybrid scope (to be fixed in a later ADR).
