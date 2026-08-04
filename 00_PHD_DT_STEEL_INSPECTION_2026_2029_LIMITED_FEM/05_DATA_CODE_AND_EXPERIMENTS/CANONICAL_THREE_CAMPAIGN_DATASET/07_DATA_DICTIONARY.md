# 07_DATA_DICTIONARY

## 01_RAW_FILE_INVENTORY.csv (216 rows)
- `Campaign_ID`, `File_Name`, `File_Path`, `SHA256` -- raw file identity, computed before any processing.
- `Filename_Decoded` -- whether the filename matched the known PASCO naming grammar.
- `State` -- Healthy / B1 / B2 / B3 (decoded from filename, e.g. `S0`->Healthy, `S1B2`->B2).
- `Excitation` -- Beat_L1 / Beat_L2 / White_Noise.
- `Run_Num`, `Date_Prefix` -- decoded run number (global, 1-18) and, for Campaign 2, the export date prefix.
- `Expected_N_Sensor_Blocks` / `Parsed_N_Sensor_Blocks` -- 2 for Campaign 1, 3 for Campaign 2/3.
- `Parse_Error`, `Duplicate_Of` -- must both be empty for a clean file.

## 02_PHYSICAL_SENSOR_MAPPING_REGISTRY.csv (576 rows = one per file x deployed block)
- `Original_Block_Position` -- the raw CSV column-block index (1-based); **never used as sensor identity**.
- `Physical_Sensor_ID` / `Physical_Location` -- the corrected identity (Apex / BeamColumn / BraceColumn), assigned from the static-gravity fingerprint, independent of block position.
- `Fingerprint_Ax/Ay/Az` -- mean acceleration per axis over the file's valid segment, pre-mean-removal.
- `Assigned_Centroid` -- the [Ax,Ay] cluster centroid this block was matched to.
- `Distance_To_Centroid` / `Second_Nearest_Distance` -- Euclidean distance (m/s^2) to the assigned vs. next-nearest cluster.
- `Mapping_Confidence` -- normalised margin = (second_nearest - distance_to_assigned) / (smallest inter-centroid distance in that campaign). Higher is more confident.
- `Mapping_Status` -- RESOLVED_HIGH_CONFIDENCE / RESOLVED_MEDIUM_CONFIDENCE / RESOLVED_LOW_CONFIDENCE / UNRESOLVED. All 576 blocks in this pass resolved HIGH_CONFIDENCE.
- `Mapping_Method` -- `static_gravity_fingerprint_kmeans_hungarian_v1`.

## 04_CHANNEL_QUALITY_REGISTRY.csv (1,728 rows = 216 files x up to 3 sensors x 3 axes)
See `03_CHANNEL_QUALITY_RULES.md` for the full label definitions. Key fields:
`Unique_Value_Count`, `Range`, `Quantisation_Step` (drive the DEAD_CONSTANT vs
LOW_DYNAMIC_QUANTIZED vs VALID_DYNAMIC decision), `Spike_Count`,
`Clipping_Status`, `Quality_Label` (final label, may append `+SPIKE_WARNING`),
`Eligibility_By_Analysis_Set` (advisory only -- the binding decision is in
`05_EXCLUSION_AND_WARNING_REGISTRY.csv`).

## 05_EXCLUSION_AND_WARNING_REGISTRY.csv
One row per (Recording_ID, Analysis_Set) pair actually evaluated (504 rows:
216 for Set A + 144 for Set B + 144 for Set C). `Included=False` rows carry a
`Reason_Code` that must be one of the approved exclusion reasons (never "low
macro-F1" or similar). In this pass, 0 of 504 rows were excluded.

## 06_MASTER_RUN_REGISTRY.csv (216 rows, one per recording)
Full per-recording metadata: `Physical_Sensors` (which locations were
identified in this file), `Available_Channels`, `SHA256`, `Raw_Duration_s`
(from the original file, including its trailing NaN), `Effective_Duration_s`
(after truncating trailing NaN), `Canonical_Dataset_Path` (Layer A NPZ),
per-set eligibility, `Quality_Status` (worst channel label observed in the
recording), `Provenance_Status`.

## FOLD_MANIFESTS/06_WITHIN_CAMPAIGN_LORO_MANIFEST.csv (42 rows)
One row per (Campaign, Held_Out_Run, Analysis_Set). `Train_Runs` are the other
5 runs of that campaign. Campaign 1 only appears under Analysis Set A (it has
no BraceColumn sensor, so it is out of scope for Set B/C).

## FOLD_MANIFESTS/07_CROSS_CAMPAIGN_LOCO_MANIFEST.csv (3 rows)
One row per Leave-One-Campaign-Out configuration, Analysis Set A only (the
only set spanning all three campaigns). `Train_Runs` / `Test_Runs` are the
global run IDs (1-18) belonging to the training vs. test campaigns.

## 08_AUTOMATED_VALIDATION_RESULTS.csv
12 rows, one per required automated check (Section 13 of the task brief),
each PASS/FAIL with a `Detail` field showing the underlying evidence.
