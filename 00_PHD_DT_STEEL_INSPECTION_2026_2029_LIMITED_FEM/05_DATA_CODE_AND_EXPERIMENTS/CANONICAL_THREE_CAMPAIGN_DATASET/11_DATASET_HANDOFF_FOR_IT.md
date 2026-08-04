# 11_DATASET_HANDOFF_FOR_IT

Plain-language handoff for the team that will train the 1D-CNN. Scope: RQ1 ->
WP1 -> Chapter 4 -> Paper 1 -> Evidence Gate 1. This dataset has been prepared,
not modelled -- no accuracy or macro-F1 exists yet.

## 1. Where the three campaigns come from
A 1:10-scale steel-frame lab specimen was instrumented with 2 (Campaign 1) or
3 (Campaign 2/3) PASCO accelerometers and shaken under 4 damage states
(Healthy, B1, B2, B3) x 3 excitations (Beat_L1, Beat_L2, White_Noise) x 6
repeat runs, recorded as 100 Hz CSV exports. Campaign 1 = global runs R1-R6,
Campaign 2 = R7-R12, Campaign 3 = R13-R18. 216 recordings total, all present
and hashed (`01_RAW_FILE_INVENTORY.csv`).

## 2. How sensor mapping was fixed
The raw CSV column order does **not** reliably indicate which physical sensor
(Apex / BeamColumn / BraceColumn) it belongs to in Campaign 1 and Campaign 2 --
the two units get swapped between recording sessions. This was fixed by
computing each column-block's static gravity fingerprint (mean Ax/Ay/Az over
its own valid segment), clustering those fingerprints per campaign, and
matching clusters to physical locations using the confirmed priors (Apex:
Ax<~-1.0; BeamColumn: Ax>~+1.0; BraceColumn: Ay<~-0.30). Every one of the 576
file-blocks resolved with high confidence -- see
`02_PHYSICAL_SENSOR_MAPPING_REGISTRY.csv`. **Always read channel identity from
this registry (or from an NPZ's own `channel_names` array), never assume
"first block = Apex."**

## 3. Which analysis set to use for which question
- **Cross-campaign comparison (all 3 campaigns, same sensors):** `ANALYSIS_SET_A_CORE_3CAMPAIGN_S1S2_AX`.
- **Does the 3rd sensor (BraceColumn) add value, in Campaign 2/3 only:** `ANALYSIS_SET_B_SUPPORT_2CAMPAIGN_3SENSOR_XYZ`.
- **Sensitivity check on whether flagged channels change a result:** `ANALYSIS_SET_C_INCLUSIVE_SENSITIVITY` (same data as Set B plus a quality mask). Never use Set C as your primary/reported configuration.

## 4. Input shape of each set
- Set A: **[4000, 2]** = 40 s @ 100 Hz x (Apex_Ax, BeamColumn_Ax).
- Set B / Set C: **[4000, 9]** = 40 s @ 100 Hz x (Apex, BeamColumn, BraceColumn) x (Ax, Ay, Az).
- These shapes are fixed for every recording in the set -- confirmed by automated tests T06/T07.

## 5. Which channels carry a warning
See `04_CHANNEL_QUALITY_REGISTRY.csv`, column `Quality_Label`. In this pass:
Campaign 1's BeamColumn_Ay is `DEAD_CONSTANT` in exactly 36 of its 72
recordings (kept in the data, not deleted -- if your architecture requires a
non-dead channel, check this column per recording). 622 channel-recordings
are `LOW_DYNAMIC_QUANTIZED` (real signal, just small/quantised -- do not treat
as dead). Campaign 2's `BS1B1L1R12` also carries a `PROVENANCE_WARNING`
(missing its date-prefix, unlike its 71 siblings) -- it stays in the primary
data; a duplicate manifest excluding it is provided
(`SENSITIVITY_MANIFEST_SET_A/B_EXCLUDING_R12.csv`) for a sensitivity run.

## 6. Which recordings were excluded, and why
None. `05_EXCLUSION_AND_WARNING_REGISTRY.csv` shows 0 of 504 (recording,
analysis-set) evaluations excluded in this pass. If you (IT) later find a
reason to exclude something, log it in the same registry format with an
approved `Reason_Code` -- never drop a recording silently, and never for
"the model does badly on it."

## 7. How to generate LORO / LOCO windows
Use `WINDOW_GENERATOR/generate_windows_from_fold.py`:
```
python3 generate_windows_from_fold.py \
  --dataset-root CANONICAL_THREE_CAMPAIGN_DATASET \
  --analysis-set A \
  --fold-manifest CANONICAL_THREE_CAMPAIGN_DATASET/FOLD_MANIFESTS/06_WITHIN_CAMPAIGN_LORO_MANIFEST.csv \
  --fold-id LORO_Campaign2_holdout_R7_A \
  --window-seconds 2.0 --overlap 0.0 \
  --out-dir /your/output/path
```
Pick `Fold_ID` values from `06_WITHIN_CAMPAIGN_LORO_MANIFEST.csv` (42 folds)
or `07_CROSS_CAMPAIGN_LOCO_MANIFEST.csv` (3 folds). Default window is 2 s /
200 samples / 0% overlap; change via `--window-seconds`/`--overlap` if a
future stage calls for it, but keep it fixed within any one comparison.

## 8. How to fit the scaler
The generator fits mean/std **only on that fold's training windows**, then
applies the same fitted values to validation/test windows -- never refit on
held-out data. This is already implemented; do not add your own
`fit_transform` on the full dataset upstream of this step. Layer B / Analysis
Set arrays you load are already per-recording mean-removed (not scaled) --
that removal happened before the fold split and is harmless because it only
uses each recording's own mean, not any cross-recording statistic.

## 9. What IT must not do
- **Do not** randomly split windows into train/val/test -- always split at Run or Campaign level first, using the provided fold manifests, before any windowing.
- **Do not** apply a global scaler fit across the whole dataset -- fit per fold, on training windows only (the provided script already does this).
- **Do not** delete or downweight "hard" recordings/windows to improve a metric.
- **Do not** change the sensor mapping in `02_PHYSICAL_SENSOR_MAPPING_REGISTRY.csv` -- if you believe a mapping is wrong, report it, do not silently reassign it.
- **Do not** use a test run or test campaign to choose hyperparameters, channels, or preprocessing.
- **Do not** pool all three campaigns and report one "overall accuracy" figure -- report per-fold, per-campaign metrics; pooling erases exactly the cross-campaign question this dataset exists to test.
