# Active Thesis Outline

## 1. Thesis Claim

- Interpretable unsupervised multispectral change priors, especially DS projection, can improve supervised Sentinel-2 change segmentation on OSCD.

## 2. Problem And Scope

- The project currently has strong implementation support for Sentinel-2 change priors and OSCD change segmentation.
- The thesis should be written around what is implemented and evidenced now, not around the broader historical disaster-mapping wish list.

## 3. Research Question

- Which unsupervised change priors are most useful downstream for supervised change segmentation?
- Why can a prior help segmentation even when it is not the best standalone unsupervised detector?

## 4. Datasets

- OSCD:
  - labeled benchmark for binary change segmentation and prior evaluation
- MultiSenGE:
  - unlabeled Sentinel-2 development set for qualitative DS behavior and temporal analysis
- xBD-S12:
  - optional warm extension if time permits, not part of the locked thesis core

## 5. Methods

### 5.1 Phase 1: Prior Generation

- DS projection
- DS cross-residual
- PCA-diff
- pixel differencing / CVA
- Celik local PCA + k-means
- IR-MAD

### 5.2 Phase 2: Prior-Assisted Segmentation

- raw Sentinel-2 pre/post stacks as baseline input
- prior channels added to supervised OSCD segmentation models
- comparison of raw-only vs raw + priors

### 5.3 Interpretation Focus

- compare standalone prior quality to downstream usefulness
- treat interpretability and transfer potential as supporting themes, not inflated claims

## 6. Results To Date

- Phase 1:
  - `pca_diff` is the best standalone unsupervised method in the saved OSCD test summary
  - `ds_projection` is weaker as a detector but remains competitive
- Phase 2:
  - raw + DS projection is the best current mean IoU/F1 U-Net result in the completed 150-epoch run
- Main scientific tension:
  - best standalone detector is not the best downstream prior

## 7. Limitations

- main segmentation comparison is effectively single-seed
- OSCD is not a disaster damage benchmark
- current code does not yet implement a real damage-segmentation pipeline

## 8. Optional Extension

- If time permits, test the same DS-first prior logic on xBD-S12 as a medium-resolution disaster damage extension.

## 9. Contributions

- a coherent DS-first Sentinel-2 change-prior pipeline
- empirical evidence that DS projection can help supervised segmentation
- a clean bridge to future medium-resolution damage mapping
