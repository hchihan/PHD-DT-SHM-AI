# 08_DATASET_VARIANTS

## CANONICAL_FULL_RECORDINGS/ (Layer A)
216 NPZ files, one per recording. Channels reordered to canonical physical
identity (Apex, BeamColumn, [BraceColumn]), trailing NaN cut at the valid
segment boundary, **all axes kept (Ax/Ay/Az per sensor)**, raw physical units,
no mean removal, no scaling, no windowing. This is the layer to go back to if
a future pass needs the full recording rather than the middle 40 seconds.
Shape: Campaign 1 = [N,6] (2 sensors x 3 axes), Campaign 2/3 = [N,9] (3
sensors x 3 axes), where N is the file's own valid-sample count (varies by
recording, see `06_MASTER_RUN_REGISTRY.csv` -> `Effective_Duration_s`).

## Analysis-ready layer (Layer B) and the three Analysis Sets
Every Analysis Set is built from the middle 4,000 samples (40 s @ 100 Hz) of
Layer A, with **per-recording, per-channel mean removal only** (no z-score, no
RMS-normalisation, no windowing yet). Scaling is deliberately deferred to
`generate_windows_from_fold.py`, which fits any scaler on the training fold's
windows only -- never on the whole dataset.

### ANALYSIS_SET_A_CORE_3CAMPAIGN_S1S2_AX
- **Question it answers:** cross-campaign comparison using the one sensor
  configuration common to all three campaigns.
- Channels: `Apex_Ax`, `BeamColumn_Ax`. Shape **[4000, 2]** for all 216 recordings (Campaigns 1+2+3).
- This is the only set used for the cross-campaign LOCO fold manifest, because it is the only set with all three campaigns represented.

### ANALYSIS_SET_B_SUPPORT_2CAMPAIGN_3SENSOR_XYZ
- **Question it answers:** value of the full 3-sensor / 3-axis configuration, where available (Campaign 2 + 3 only -- Campaign 1 never had a BraceColumn sensor deployed).
- Channels: `Apex_Ax/Ay/Az`, `BeamColumn_Ax/Ay/Az`, `BraceColumn_Ax/Ay/Az`. Shape **[4000, 9]** for all 144 Campaign 2+3 recordings.
- S3 (BraceColumn) axes are **not** dropped for being low-dynamic under White Noise; per the task brief, BraceColumn's structurally meaningful axis may be Ay rather than Ax, so all three BraceColumn axes are retained and only flagged (see `04_CHANNEL_QUALITY_REGISTRY.csv`), never silently removed.

### ANALYSIS_SET_C_INCLUSIVE_SENSITIVITY
- **Question it answers:** sensitivity checks that need visibility into channels Set B's own inclusion rules would otherwise let through unflagged, e.g. whether a DEAD_CONSTANT channel is materially changing a result.
- Same recordings and same [4000, 9] channel scope as Set B (144 Campaign 2+3 recordings) -- in this pass, no recording was excluded from either set on quality grounds, so Set B and Set C have identical membership. What differs is metadata: every Set C NPZ additionally carries `quality_label_per_channel` (9-length string array) and `quality_mask_dead_constant` (9-length 0/1 array).
- **The quality mask is metadata only.** It must never be concatenated into the model input tensor, and Set C must never replace Set B as the primary configuration -- it exists solely to support sensitivity analyses that ask "does removing/downweighting the flagged channels change the picture."

## Why Set B and Set C have the same membership in this pass
This is not an oversight: per Section 9 of the task brief, a recording is only
excluded from an analysis set for unresolved mapping, a missing required
physical sensor, a too-short valid segment, a mid-recording NaN gap, a
protocol-mandated channel being DEAD_CONSTANT, or invalid timestamps/sampling
rate -- never merely for being low-dynamic or having one dead channel among
nine. Because none of Campaign 2/3's 144 recordings triggered any of those
hard-exclusion conditions, Set B's membership is already maximally inclusive,
and Set C's only additional value in this pass is exposing the quality mask
as metadata rather than changing which recordings are present.
