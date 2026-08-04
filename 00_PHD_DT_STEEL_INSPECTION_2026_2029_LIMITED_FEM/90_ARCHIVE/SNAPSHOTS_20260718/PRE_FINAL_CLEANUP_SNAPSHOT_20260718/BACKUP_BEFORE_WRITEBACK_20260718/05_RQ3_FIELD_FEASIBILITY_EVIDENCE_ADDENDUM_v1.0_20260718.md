# RQ3 / WP3 / Paper 3 / Gate 4 Field-Feasibility Evidence Addendum
**Version:** v1.0 | **Date:** 2026-07-18

## Scope Boundary

Field feasibility means deployment, data return, operational baseline, component mapping, traceability scenarios, and human-reviewed inspection workflow. It does not mean field damage diagnosis or transfer of the laboratory classifier.

## Claim Register

| Claim ID | Claim | Evidence | Limitation | Next action |
|---|---|---|---|---|
| C3-05 | Long-term field baselines should be location-specific and account for environmental effects. | `TRZY4P6X`, `GE3XSAYV`, `9823WXJZ` | Bridge/building contexts differ; no universal duration. | Predefine environmental metadata and baseline-coverage criteria. |
| C3-06 | Low-cost vibration nodes require field-relevant qualification for noise, timing, sampling, storage, and ambient signal level. | `LZPF7ILT`, PDF pp. 2-15 | Laboratory slab only. | Run a pre-deployment qualification and acceptance log. |
| C3-07 | Missing data, freezing, wind, activity, and excitation amplitude can mimic or dominate state changes. | `D3TGCKXW`, `GE3XSAYV`, `9823WXJZ` | Sources do not provide one transferable correction model. | Record missingness/fault/environment metadata and keep alerts as evidence pending inspection. |
| C3-08 | Continuous vibration monitoring is feasible in a real steel-frame building. | `9823WXJZ`, pp. 715-735 | Occupied institutional building, not coastal industrial asset; no BIM mapping. | Use as deployment precedent only. |
| C3-09 | A field alert must lead to inspection, not a damage conclusion. | Limitation convergence across all sources | Inspection records are absent or weakly documented. | Predefine alert-to-`Inspection_Record_ID` and human disposition workflow. |

## Source Boundaries

### `TRZY4P6X`

**Claim ->** Practical multi-year baseline acquisition is feasible on an operational steel bridge.  
**Evidence ->** Three-minute sampling, dense temperature/strain/displacement network, and three-year surfaces, pp. 161-167.  
**Limitation ->** Scenario sensitivity is numerical and not field-confirmed damage.  
**Next action ->** Transfer only installation, placement, and environmental-QC lessons.

### `GE3XSAYV`

**Claim ->** Temperature adjustment can materially change threshold behavior.  
**Evidence ->** One year of hourly GNSS and static/dynamic comparison, pp. 10-21.  
**Limitation ->** Missingness rate and manual-inspection provenance are not auditable.  
**Next action ->** Link each project alert timestamp prospectively to a human inspection record.

### `LZPF7ILT`

**Claim ->** Low-cost nodes may work for controlled impulse input yet fail under ambient vibration.  
**Evidence ->** Side-by-side tests, sampling drops, and ambient failure, pp. 8-15.  
**Limitation ->** Laboratory-only evidence.  
**Next action ->** Qualify noise floor, synchronization, data loss, and drift before field use.

### `D3TGCKXW`

**Claim ->** Environmental effects and mode-dependent missingness can dominate field-derived features.  
**Evidence ->** Z24 and KW51 datasets, pp. 6-13.  
**Limitation ->** Secondary datasets omit sensor/component provenance and use intervention labels.  
**Next action ->** Define prospective completeness and environmental-coverage rules; do not transfer the classifier.

### `9823WXJZ`

**Claim ->** Continuous monitoring in an occupied steel-frame building captures operational and wind-dependent baseline variation.  
**Evidence ->** 72-channel installation, ambient/wind/earthquake observations, pp. 715-735.  
**Limitation ->** No component mapping, inspection confirmation, or coastal industrial context.  
**Next action ->** Map every field channel to `Sensor_ID` and `BIM_GUID` before acquisition.

## Gate Position

**ALLOWED CLAIM:** The new corpus strengthens practical field requirements for sensing, baselines, environmental context, missing data, and human confirmation.  
**PROHIBITED INFERENCE:** Field anomaly equals damage; temporary frequency change proves damage; a fixed minimum baseline duration applies universally; lab classifier transfers to field.  
**EVIDENCE SUFFICIENCY:** Evidence is currently insufficient to close Gate 4 because no source or project result yet demonstrates the complete field identifier-to-inspection chain.
