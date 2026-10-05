# RQ1 / WP1 / Paper 1 / Gate 1 Method Evidence Addendum
**Version:** v1.0 | **Date:** 2026-07-18

## Scope

This addendum covers laboratory condition evidence only. It does not support field diagnosis, direct lab-to-field transfer, general AI superiority, or physical damage severity.

## Claim Register

| Claim ID | Claim | Evidence | Limitation | Next action |
|---|---|---|---|---|
| C1-12 | The independent run/group is the effective split and inference unit. | `L97BIAI3`, `XE9XS6BQ`, `M8LMWFQH`, `RG9FMT8Y` | Domains differ; exact steel-frame design not validated. | Lock `Run_ID`; keep all windows from each run in one fold. |
| C1-13 | Windowing must follow group assignment, or at minimum preserve whole source groups across partitions. | Direct vibration leakage in `M8LMWFQH`; grouped windows in `RG9FMT8Y`; subject hierarchy in `XE9XS6BQ` | Some sources generate windows before assignment but preserve groups. | Implement and audit split-before-windowing; retain non-overlap sensitivity analysis. |
| C1-14 | Learned preprocessing must be fitted on training groups only. | Fold-contained pipeline in `XE9XS6BQ`; held-out-group exclusion in `RG9FMT8Y` | Exact scaler implementation is not always reported. | Fit scaling, selection, reduction, calibration, and tuning only inside training folds. |
| C1-15 | Small independent-group counts require explicit uncertainty and empirical chance analysis. | `L97BIAI3`, `PZ937I73`, `ZLFATP2Z` | No source proves adequacy at approximately six runs/class. | Report run outcomes, intervals, group-preserving permutations, and sensitivity analyses. |
| C1-16 | Wilcoxon/Friedman logic requires defensible independent paired units. | `9XNSNIPX` | LORO folds overlap in training data and are not independent datasets. | Treat six-fold Wilcoxon as exploratory at most; prioritize group-level predictions/permutations. |
| C1-17 | Sensor configuration may materially alter apparent performance. | Two-location comparison in `RG9FMT8Y` | Bearing sensors do not establish the best steel-frame configuration. | Compare sensor modes on identical folds, seeds, preprocessing, and budgets. |
| C1-18 | Existing literature cannot verify the project's ResNet1D sensor mode. | No reviewed source reports the project experiment. | Missing project provenance cannot be repaired by literature. | Verify channels, mode, folds, seeds, preprocessing, and artifacts before inclusion. |

## Per-Source Controls

### `L97BIAI3`

**Claim ->** Derived observations do not increase the number of independent experimental units.  
**Evidence ->** Patient/batch-level validation and uncertainty calculations, PDF pp. 1-10.  
**Limitation ->** Raman spectroscopy, not vibration.  
**Next action ->** Report `n` as independent runs, not windows.

### `PZ937I73`

**Claim ->** Theoretical chance is unsafe for small samples.  
**Evidence ->** Noise classifications, binomial and permutation thresholds, PDF pp. 3-10.  
**Limitation ->** No correlated-window group model.  
**Next action ->** Permute labels at run level through the complete pipeline.

### `9XNSNIPX`

**Claim ->** Statistical comparisons need independent paired units and multiplicity control.  
**Evidence ->** Wilcoxon/Friedman analysis, JMLR pp. 1-15.  
**Limitation ->** Independent datasets are not equivalent to overlapping LORO folds.  
**Next action ->** Keep model-comparison claims bounded and pre-specified.

### `ZLFATP2Z`

**Claim ->** A full-pipeline permutation test can assess an empirical null.  
**Evidence ->** Corrected empirical p-values and repeated classifier procedures, JMLR pp. 1836-1843.  
**Limitation ->** Parent metadata is the 2009 conference paper, while the PDF is the 2010 expanded journal version; row exchangeability is not run exchangeability.  
**Next action ->** Resolve the version link and preserve complete runs during permutation.

### `XE9XS6BQ`

**Claim ->** Group-wise CV better estimates unseen-source performance than record-wise CV.  
**Evidence ->** Subject-wise holdout, grouped 10-fold and LOGO, journal pp. 190-198.  
**Limitation ->** Healthcare audio with hundreds of subjects.  
**Next action ->** Implement LORO with all preprocessing inside each fold.

### `M8LMWFQH`

**Claim ->** Source-group separation must precede segmentation.  
**Evidence ->** Segment/record/fault-shape split comparison on two vibration datasets, PDF pp. 1-5.  
**Limitation ->** Bearing diagnosis and limited uncertainty reporting.  
**Next action ->** Use it for split design only, not field diagnosis or RUL/severity claims.

### `RG9FMT8Y`

**Claim ->** Run, day, part, and sensor position can dominate apparent vibration-classification performance.  
**Evidence ->** Leave-one-run/day/part-out and two accelerometer positions, IEEE pp. 169883-169892.  
**Limitation ->** Bearing rigs and no ResNet1D.  
**Next action ->** Compare project sensor configurations under common LORO folds and equal budgets.

## Gate 1 Position

**ALLOWED CLAIM:** The reviewed evidence supports run-aware, leakage-controlled evaluation and fair sensor-configuration comparison.  
**PROHIBITED INFERENCE:** Random-window results, approximately six runs/class, or one model result establish general superiority or field diagnosis.  
**EVIDENCE SUFFICIENCY:** Evidence is currently insufficient to close Gate 1 without the project's run registry, LORO execution, train-only preprocessing audit, ResNet1D provenance, and run-level uncertainty results.
