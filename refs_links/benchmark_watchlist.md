# Benchmark Watchlist

Status date: 2026-03-24

This file tracks the external papers, datasets, and codebases discussed during the March 2026 reset. It exists to keep benchmark comparisons technically honest and to make follow-up implementation/reproduction work easier.

## 1. Comparison Discipline

General rule:
- do not compare numbers across papers as if they were directly equivalent unless the dataset, masking, thresholding, averaging, and compute protocol are aligned

Working rule for the current thesis:
- cross-paper AUC comparisons are usually safer than F1 comparisons
- thresholded metrics require protocol checks
- compute-efficiency claims require controlled reruns

## 2. Core References

### OSCD dataset paper

- Paper:
  - Rodrigo Caye Daudt, Bertrand Le Saux, Alexandre Boulch, Yann Gousseau, "Urban Change Detection for Multispectral Earth Observation Using Convolutional Neural Networks," IGARSS 2018
  - https://arxiv.org/abs/1810.08468
- Dataset/code references:
  - OSCD dataset repo: https://github.com/daudt1995/oscd_dataset
  - FCNN baseline repo: https://github.com/rcdaudt/fully_convolutional_change_detection
- Why it matters:
  - this is the benchmark family used by the current implementation

### Metric-CD / Bandara and Patel

- Paper:
  - Wele Gedara Chaminda Bandara, Vishal M. Patel, "Deep Metric Learning for Unsupervised Remote Sensing Change Detection," WACV 2025
  - Open-access paper: https://openaccess.thecvf.com/content/WACV2025/papers/Bandara_Deep_Metric_Learning_for_Unsupervised_Remote_Sensing_Change_Detection_WACV_2025_paper.pdf
  - arXiv page: https://arxiv.org/abs/2303.09536
- Code:
  - https://github.com/wgcban/Metric-CD
- Key protocol note:
  - same OSCD benchmark family, but not the same end-to-end protocol as the current repo
  - the paper states that it optimizes network parameters for each image separately and saves the change map after 80 iterations, then thresholds it at 0.5
- How to use this reference:
  - use it as evidence that stronger unsupervised OSCD results exist
  - do not use it as a perfectly apples-to-apples claim against the current repo without rerunning under aligned conditions

### xBD dataset

- Paper:
  - Ritwik Gupta et al., "xBD: A Dataset for Assessing Building Damage from Satellite Imagery," CVPRW 2019
  - https://arxiv.org/abs/1911.09296
- Code / baseline references:
  - xView2 baseline: https://github.com/DIUx-xView/xView2_baseline
  - Microsoft Siamese baseline: https://github.com/microsoft/building-damage-assessment-cnn-siamese
- Why it matters:
  - this is the canonical VHR damage benchmark family if the research later moves beyond OSCD

### xBD-S12

- Paper:
  - Olivier Dietrich et al., "The Potential of Copernicus Satellites for Disaster Response: Retrieving Building Damage from Sentinel-1 and Sentinel-2"
  - https://arxiv.org/abs/2511.05461
- Important abstract claims:
  - introduces xBD-S12 with 10,315 aligned pre/post image pairs from Sentinel-1 and Sentinel-2
  - medium-resolution damage mapping is viable in many scenarios
  - more complex architectures do not necessarily generalize better to unseen disasters
  - paper states that dataset, code, and trained models are released
- Current tracking note:
  - as of this reset, the paper is identified and logged, but the exact official release repo link still needs to be captured before implementation begins
- Why it matters:
  - this is the warm-extension path because it bridges the current Sentinel-scale work to true disaster damage mapping

### Emergency-context transfer learning

- Paper:
  - Isabelle Bouchard et al., "On Transfer Learning for Building Damage Assessment from Satellite Imagery in Emergency Contexts," Remote Sensing 2022
  - https://www.mdpi.com/2072-4292/14/11/2532
- Why it matters:
  - useful for thesis realism
  - emphasizes cross-disaster generalization and emergency-consistent evaluation rather than random-split optimism
- Current note:
  - use this as conceptual support when framing disaster relevance and evaluation realism

### Prior-guided / semantic-guided change detection

- Representative paper:
  - Maximilian Bernhard, Niklas Strauss, Matthias Schubert, "MapFormer: Boosting Change Detection by Using Pre-change Information," ICCV 2023
  - https://arxiv.org/abs/2303.17859
- Code:
  - https://github.com/mxbh/mapformer
- Why it matters:
  - supports the caution that "using extra prior information to help change detection" is not, by itself, a strong novelty claim

## 3. Practical Benchmark Implications

For the current thesis:
- strongest internal benchmark story:
  - raw-only vs raw + DS prior on OSCD
- strongest external caution:
  - newer unsupervised OSCD methods can reach higher headline metrics under different protocols
- strongest future bridge:
  - xBD-S12

## 4. Reproduction / Comparison To-Do

Before making strong benchmark claims, verify:
- exact split compatibility
- valid-pixel masking policy
- threshold selection policy
- averaging convention across cities/tiles/pixels
- band usage and normalization
- compute budget and runtime protocol

If we later benchmark against Metric-CD or another external method, the first deliverable should be:
- a protocol-alignment note
- not just a table of scores
