# CANONICAL_THREE_CAMPAIGN_DATASET

**Scope classification:** RQ1 -> WP1 -> Chapter 4 -> Paper 1 -> Evidence Gate 1.

**What this is:** a canonical, analysis-ready, audit-ready re-derivation of the
three vibration-testing campaigns (216 raw PASCO CSV recordings), built to hand
off to the IT team for 1D-CNN training. **No model was trained. No accuracy or
macro-F1 was computed. No hyperparameter tuning occurred. No raw source CSV was
modified, renamed, moved, or overwritten.**

## Read this first

1. `11_DATASET_HANDOFF_FOR_IT.md` -- plain-language handoff notes for the IT team (read before touching any file).
2. `09_DATASET_VALIDATION_REPORT.md` -- whether this dataset is READY_FOR_IT_TRAINING and why.
3. `07_DATA_DICTIONARY.md` -- every field in every registry.
4. `08_DATASET_VARIANTS.md` -- what Analysis Set A/B/C are for and how they differ.

## Where the full dataset (NPZ files + code) is

This workspace copy contains all documentation and registries. The full
216-recording NPZ layers, the three Analysis Sets, fold manifests, window
generator, pipeline code, and automated-test artifacts are packaged as
`CANONICAL_THREE_CAMPAIGN_DATASET.zip`, delivered alongside this folder via
the chat file cards (also copyable here on request).

## What changed relative to the raw CSVs

Nothing in the raw CSVs changed. What this pass adds, on top of read-only raw
data, is:

- a corrected **physical-sensor identity** per file (via static gravity
  fingerprint clustering, not CSV column position) -- see
  `02_PHYSICAL_SENSOR_MAPPING_REGISTRY.csv` (in the zip);
- a **channel quality taxonomy** that distinguishes truly dead channels from
  merely low-dynamic-but-real channels -- see `03_CHANNEL_QUALITY_RULES.md` /
  `04_CHANNEL_QUALITY_REGISTRY.csv`;
- two data layers (full raw-valid recordings, and a fixed-shape 40-second
  analysis-ready layer) and three analysis sets with fixed input shapes;
- leakage-safe fold manifests for within-campaign LORO and cross-campaign LOCO;
- a window-generation script that fits any scaler on training windows only;
- an automated test suite, all 12 checks passing at the time this package was built.

## Directory map (inside the zip)

```
00_README.md
01_RAW_FILE_INVENTORY.csv
02_PHYSICAL_SENSOR_MAPPING_REGISTRY.csv
03_CHANNEL_QUALITY_RULES.md
04_CHANNEL_QUALITY_REGISTRY.csv
05_EXCLUSION_AND_WARNING_REGISTRY.csv
06_MASTER_RUN_REGISTRY.csv
07_DATA_DICTIONARY.md
08_DATASET_VARIANTS.md
08_AUTOMATED_VALIDATION_RESULTS.csv
CANONICAL_FULL_RECORDINGS/         (Layer A: 216 NPZ, full valid-segment, raw units, unscaled)
ANALYSIS_SET_A_CORE_3CAMPAIGN_S1S2_AX/     (216 recordings, shape [4000,2])
ANALYSIS_SET_B_SUPPORT_2CAMPAIGN_3SENSOR_XYZ/  (144 recordings, shape [4000,9])
ANALYSIS_SET_C_INCLUSIVE_SENSITIVITY/      (144 recordings, shape [4000,9] + quality mask)
FOLD_MANIFESTS/                    (06_WITHIN_CAMPAIGN_LORO_MANIFEST.csv, 07_CROSS_CAMPAIGN_LOCO_MANIFEST.csv)
WINDOW_GENERATOR/                  (generate_windows_from_fold.py)
AUTOMATED_TESTS/                   (test script + smoke-test provenance + results copy)
PIPELINE_CODE/                     (verbatim copies of every stage script + run_pipeline.sh)
09_DATASET_VALIDATION_REPORT.md
10_REPRODUCIBILITY_MANIFEST.md
11_DATASET_HANDOFF_FOR_IT.md
```

## What this dataset is NOT

Per the task brief's explicit limitation list (also in
`11_DATASET_HANDOFF_FOR_IT.md`): this is not a claim of a perfectly clean
dataset, not sufficient for damage diagnosis, not an optimal sensor
configuration, not a trained/best AI, not a Gate 1 closure, not evidence of
cross-campaign generalisation, and not directly applicable to real-world
structures. The only permitted conclusion is:

> The dataset has been canonically mapped, quality-audited, provenance-locked,
> and prepared for leakage-safe run-aware and campaign-aware evaluation.
