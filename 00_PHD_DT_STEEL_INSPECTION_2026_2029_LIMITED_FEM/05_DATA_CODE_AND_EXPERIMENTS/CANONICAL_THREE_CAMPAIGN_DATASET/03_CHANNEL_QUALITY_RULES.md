# 03_CHANNEL_QUALITY_RULES

Scope: RQ1 -> WP1 -> Chapter 4 -> Paper 1 -> Evidence Gate 1. Documentation only,
governs how `04_CHANNEL_QUALITY_REGISTRY.csv` labels were assigned. No training,
no accuracy/macro-F1 computed anywhere in this pipeline pass.

Unit of analysis: **File x Physical Sensor (post fingerprint-correction) x Axis**.
Physical_Sensor_ID here is the corrected identity from
`02_PHYSICAL_SENSOR_MAPPING_REGISTRY.csv`, not the raw CSV block position.

## Labels and definitions

**DEAD_CONSTANT** -- the entire valid segment (not a short window) has exactly
one unique value (rounded to 1e-6), or range < 1e-6 (machine-precision noise
only). This is checked over the full recorded valid segment, so a brief
plateau inside an otherwise-moving signal does NOT qualify -- only a channel
that never leaves a single value for its whole valid duration is DEAD_CONSTANT.

**LOW_DYNAMIC_QUANTIZED** -- more than one unique value is present, but the
full-segment range is <= 2x the estimated quantisation step (nominally 0.1 m/s^2
for this accelerometer, re-estimated per channel from the minimum consecutive
gap between unique values). This channel is NOT called dead; it is kept in the
dataset and flagged so the low-dynamic behaviour is visible to IT and to any
future modelling decision, per Section 5C/6 of the task brief.

**VALID_DYNAMIC** -- full-segment range exceeds 2x quantisation step, no
overriding CLIPPING_WARNING.

**CLIPPING_WARNING** -- >=20 consecutive samples sit at the exact segment
max or min (a real sensor-saturation signature, not just a single repeated
peak). Overrides the base DEAD/LOW/VALID label in the Quality_Label field but
does not imply exclusion by itself.

**SPIKE_WARNING** -- appended to the base label (not exclusive) when >=3
sample-to-sample jumps exceed max(6x local MAD, 2.0 m/s^2). Advisory only.

**MID_RECORDING_GAP** -- recorded at the recording level (from Stage 3 NaN
checks: a NaN block that is *not* purely trailing) and propagated into this
channel's Notes field; recordings with this flag are excluded from primary
analysis sets for the affected configuration (see
`05_EXCLUSION_AND_WARNING_REGISTRY.csv`), not silently repaired.

**EXPECTED_TRAILING_NAN** -- not an axis quality problem. Trailing NaN at the
end of a PASCO export is expected instrument behaviour; the valid segment used
for every statistic in this registry already stops before the trailing NaN
begins (see `valid_segment_end_index` in `canon_lib.py`). Never interpolated,
never zero-filled.

**PROVENANCE_WARNING** -- carried from the raw-file provenance check (Campaign
2's `BS1B1L1R12.csv`, missing the date prefix its 71 siblings carry). Does not
change the channel-level quality label; it is an independent provenance flag,
propagated into Notes and into the exclusion/warning registry.

## Explicit rule NOT used

`std < 0.1` alone is never used to call a channel dead, per the task brief.
The full unique-value-count-over-full-segment + range-vs-quantisation-step
logic above is the sole basis for DEAD_CONSTANT vs LOW_DYNAMIC_QUANTIZED.
