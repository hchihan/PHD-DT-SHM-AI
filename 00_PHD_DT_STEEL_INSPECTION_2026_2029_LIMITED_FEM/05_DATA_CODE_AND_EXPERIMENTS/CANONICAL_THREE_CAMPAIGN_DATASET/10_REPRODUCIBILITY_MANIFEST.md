# 10_REPRODUCIBILITY_MANIFEST

## Environment
- Python 3.10, numpy 2.2.6, pandas 2.3.3, scipy 1.15.3, scikit-learn 1.7.2.
- No GPU, no deep-learning framework used or needed for this pass (no training occurs).

## Raw data (untouched)
- `Campaign1_25.04.2026/` (72 files), `Campaign2_22.07.2026/` (72 files), `Campaign3_29.07.2026/` (72 files), all read-only.
- Raw-file SHA256 values: see `01_RAW_FILE_INVENTORY.csv` (computed before any parsing).

## Pipeline code (verbatim copies in `PIPELINE_CODE/`)

| Script | SHA256 |
|---|---|
| canon_lib.py | f2888382cfce5ed787b08ef5bc52d6f664f28dff40168f7ec616237e9e81dc1c |
| stage1_inventory.py | 4ae58c0946fcacb265ef611f93a4164a3755bfd511cdbce6fdb363d8f2b031c7 |
| stage2_fingerprint_cache.py | 3bc3811323eba6d907191858b8cec0466339e6fa86136f83106febd4785a1fc5 |
| stage2b_sensor_mapping.py | 26cc82b05e3b49dc8f3162163106e0aa37779d8cf6ecc419e418dcd86528878b |
| stage3_4_channel_quality.py | 4adbcf3ed91322120e4d7034e8fa3276534a09aa928bfc873a3d25028d60c406 |
| stage5_layerA_canonical_full.py | 47be3472cdb6aec4c7159f239eb66f9ee8aab7553d2b6f37f44590463b3cb064 |
| stage6_layerB_analysis_sets.py | eb1c7289ad03ccc7ee035a9a4f6b74aff9893443b02fae2658853b5336afd928 |
| stage7_exclusion_balance.py | f4078cfe690a46274d859022e2abc71b94e6c122cc0afa28258a8265e51145f1 |
| stage8_registry_folds.py | bda6eb6f3b486edac85a28fe9bb3ae47db078e7dbe9458ef78ea1e0b29585174 |
| stage10_automated_tests.py | dc7802aa998eea4d35587521769150e958aeb8e86be8193dc24ead684531a288 |
| generate_windows_from_fold.py | bade0b4edcc9d998539cf46308976a27467abbeb65acc03564c8699fa30db681 |
| run_pipeline.sh | 2839bdfefd31b530e6104411aeaceaaa4c2d831bf83f2e327a5b65285f444c4b |

## One-command reproduction

```
bash run_pipeline.sh
```

runs Stage 1 through Stage 10 in order (inventory -> fingerprint parse cache
-> sensor mapping -> channel quality -> Layer A -> Layer B / Analysis Sets ->
exclusion/balance check -> master registry + fold manifests -> automated
tests), regenerating every file in this package deterministically from the
raw CSVs.

**Known portability caveat:** `canon_lib.py` currently hard-codes the raw-data
root path used in this session
(`/sessions/affectionate-adoring-galileo/mnt/DATA_ALL_3_CAMPAIGN`). Running
`run_pipeline.sh` on a different machine requires updating `RAW_ROOT` in
`canon_lib.py` to point at wherever `Campaign1_25.04.2026/`,
`Campaign2_22.07.2026/`, and `Campaign3_29.07.2026/` live there. This is
disclosed rather than hidden: it is the one manual step needed for full
reproduction outside this session.

## Determinism
- `KMeans(random_state=42)` for sensor-fingerprint clustering: deterministic given the same input fingerprints.
- All quality-taxonomy and exclusion logic is rule-based (no randomness).
- `generate_windows_from_fold.py` has no randomness (fixed window/step size, scaler is a closed-form mean/std fit).

## What is NOT included in one-command reproduction
`generate_windows_from_fold.py` is a per-fold, per-analysis-set tool the IT
team invokes explicitly (see `11_DATASET_HANDOFF_FOR_IT.md`); `run_pipeline.sh`
does not run it for every fold automatically, since no model training or
window materialisation for all ~45 folds was requested for this dataset-prep
pass. Two folds (one LORO, one LOCO) were smoke-tested during this pass purely
to validate the generator's correctness (Test T11); their outputs live outside
this package under `/tmp` and are not part of the deliverable.
