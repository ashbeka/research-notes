# Spec Snippets and Quick Figures

Purpose
- Provide small, self‑contained examples (code + figures) tied to Appendix A/B so you can generate slides and sanity‑check behavior quickly.
- Figures are lightweight (synthetic by default) and CPU‑friendly.

Outputs
- `outputs/figs/deltas_grid.png` — temporal deltas (Delta1/Delta2) visualization
- `outputs/figs/feature_stack.png` — static diagram (placeholder note)
- `outputs/figs/mcda_heatmap.png` — toy MCDA score heatmap
- `outputs/figs/payload_vs_m.png` — embedded vs raw uplink bytes chart

Run Commands
- Python v3.9+ with numpy and matplotlib
- Generate deltas figure:
  - `python scripts/render_deltas.py --save outputs/figs/deltas_grid.png`
- Generate MCDA heatmap:
  - `python scripts/render_mcda_demo.py --save outputs/figs/mcda_heatmap.png`
- Generate payload chart:
  - `python scripts/render_payload_chart.py --save outputs/figs/payload_vs_m.png`

Notes
- All scripts create parent directories if missing.
- Replace synthetic inputs with real tiles later by pointing to image arrays where noted.

Sections

## Temporal Deltas (Appendix A — A.2)
The scripts compute first‑ and second‑order differences
- Delta1 = x_t2 - x_t1
- Delta2 = x_t3 - 2*x_t2 + x_t1
and render a grid: pre/mid/post plus Delta1 and Delta2 with colorbars.

## SSC Features (Appendix A — A.3)
SSC objective:
`min_C  0.5*||X - X*C||_F^2 + lambda*||C||_1 + (beta/2)*||C||_F^2,  s.t. diag(C)=0`
This doc does not fit a model; it explains where to splice SSC‑derived features (residuals, cluster one‑hots) into the feature stack (Appendix A — A.4).

## Feature Stack (Appendix A — A.4)
Diagram placeholder: render a simple pipeline (e.g., draw.io) showing channels [x_t2, Delta1, Delta2, residual, cluster_onehot] flowing into U‑Net.

## MCDA (Appendix A — A.6)
We normalize simple criteria per region, apply weights `w`, and compute `s_j = w^T q_j`. The script renders both normalized criteria and final scores as a heatmap.

## Payload (Appendix B — B.4)
Embedded uplink estimate: `uplink_bytes_per_sec ~= T*(H*W*m*4)` vs raw 16‑bit uplink `T*(H*W*d*2)`. The chart shows savings vs embedding dim `m`.

