# 09_DATASET_VALIDATION_REPORT

**Scope:** RQ1 -> WP1 -> Chapter 4 -> Paper 1 -> Evidence Gate 1. This report
concerns **dataset preparation readiness only**. It is not a model result, not
a macro-F1 figure, and not a Gate 1 closure -- those require a separate,
future modelling pass on top of this dataset.

## Status: **READY_FOR_IT_TRAINING**

**Claim.** All 10 acceptance conditions from the task brief (Section 16) are met.

**Evidence**, condition by condition:

1. **Inventory complete for 216 files.** `01_RAW_FILE_INVENTORY.csv`, 216/216 rows, 0 parse errors, 0 duplicate SHA256 (Test T01/T02).
2. **Sensor mapping for Campaign 1/2 corrected per file.** `02_PHYSICAL_SENSOR_MAPPING_REGISTRY.csv`, 576 blocks (216 files x 2 or 3 deployed sensors), assigned via static-gravity-fingerprint clustering + per-file Hungarian assignment -- not by CSV column position.
3. **No unresolved mapping remains.** 576/576 blocks `RESOLVED_HIGH_CONFIDENCE`; 0 `UNRESOLVED` (Test T03).
4. **Every analysis set has a fixed input shape.** Set A: [4000,2] for all 216 recordings (Test T06). Set B: [4000,9] for all 144 Campaign2+3 recordings (Test T07). Set C: same [4000,9] scope as Set B plus metadata-only quality mask.
5. **No hidden exclusion.** `05_EXCLUSION_AND_WARNING_REGISTRY.csv` logs every (recording, analysis set) decision explicitly; 0 of 504 evaluated pairs were excluded in this pass, and the one provenance-flagged file (`BS1B1L1R12`) is visibly kept with a `PROVENANCE_WARNING` note plus a separate sensitivity manifest that excludes it.
6. **Registry and hashes complete.** `06_MASTER_RUN_REGISTRY.csv` carries SHA256 and both raw and effective duration for all 216 recordings.
7. **Trailing NaN handled correctly.** Every recording's valid segment stops at the last sample where all deployed Ax/Ay/Az channels are simultaneously non-NaN; 0 mid-recording gaps found; all 216 valid segments are >=41.5 s (comfortably above the 40 s requirement).
8. **Quality taxonomy distinguishes dead from low-dynamic.** `04_CHANNEL_QUALITY_REGISTRY.csv`: 36 `DEAD_CONSTANT` (all in one specific channel: Campaign 1 BeamColumn_Ay, in exactly half of Campaign 1's 72 files), 622 `LOW_DYNAMIC_QUANTIZED` (kept, flagged, not treated as dead), 1,070 `VALID_DYNAMIC`, 0 spikes, 0 genuine clipping (an initial naive "20 consecutive samples at local max/min" heuristic produced 416 false positives on near-flat/low-dynamic channels and was corrected to also require the extreme value to be a real outlier vs. the channel's own distribution -- see `03_CHANNEL_QUALITY_RULES.md`).
9. **Leakage-safe fold manifests exist.** `FOLD_MANIFESTS/06_WITHIN_CAMPAIGN_LORO_MANIFEST.csv` (42 rows) and `07_CROSS_CAMPAIGN_LOCO_MANIFEST.csv` (3 rows), both verified programmatically to have disjoint train/test run sets (Test T10) and empirically re-verified via a smoke-tested window generation on one LORO and one LOCO fold (Test T11, 0 overlapping recordings).
10. **Automated tests pass.** `08_AUTOMATED_VALIDATION_RESULTS.csv`: **12/12 PASS**.
11. **Reproducible with one command.** `run_pipeline.sh` (copy in `PIPELINE_CODE/`) runs Stages 1 through 10 in order against the untouched raw CSVs (Test T12).

**Limitation.** "READY_FOR_IT_TRAINING" describes **data preparation** readiness
only. It does not mean: the data is free of every quality issue (622
recordings still carry at least one LOW_DYNAMIC_QUANTIZED channel, by design
kept rather than removed), the sensor configuration is optimal, cross-campaign
generalisation will succeed, or that any Gate 1 evidence item is closed --
closing Gate 1 requires actually running LORO/LOCO evaluation on this
corrected dataset and reporting macro-F1 with permutation controls, which is
explicitly out of scope for this pass (no model was trained here). The
DEAD_CONSTANT finding is narrow and specific (one physical channel, one
campaign) rather than the broad, scattered pattern reported by a prior,
cruder `std<0.1` heuristic -- this is a byproduct of fingerprint-correcting
sensor identity before judging channel quality, not a claim that the earlier
finding was fabricated.

**Next action.** Hand this dataset to the IT team per
`11_DATASET_HANDOFF_FOR_IT.md`. The next evidentiary step for Gate 1 is a
fresh LORO/LOCO modelling pass (feature baselines + compact 1D-CNN, >=3 seeds,
permutation control) run against this corrected canonical dataset, to see
whether the earlier cross-campaign collapse finding changes once Campaign 1/2
sensor identities are no longer column-position-dependent.
