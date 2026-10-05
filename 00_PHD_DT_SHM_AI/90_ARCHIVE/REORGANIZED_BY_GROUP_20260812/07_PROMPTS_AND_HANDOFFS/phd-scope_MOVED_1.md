# PhD scope reference

## Research identity

Field: Construction Management / Asset Management.

Locked evidence chain:

`Vibration data → condition/state-change evidence → BIM-linked component → inspection record → inspection-maintenance action support`

Locked identifier chain:

`Sensor_ID → BIM_GUID → Condition_Evidence_ID → Inspection_Record_ID → Action_Status`

`FEM_Node_ID` is optional metadata only.

## Research map

| Mode | RQ/WP | Chapter/Paper | Gate |
|---|---|---|---|
| G1_LAB | RQ1/WP1 | Chapter 4/Paper 1 | Gate 1 |
| G2_TRACEABILITY | RQ2/WP2 | Chapter 5/Paper 2 | Gate 2–3 |
| G3_FIELD | RQ3/WP3 | Chapter 6/Paper 3 | Gate 4 |
| G4_DECISION | WP4 | Chapter 7/Paper 3 or 4 | Gate 5 |

Current priority: Gate 1 — run registry, leakage-safe run-aware/LORO evaluation, and verification of the ResNet1D sensor mode.

## Scope control

Core scope:
- laboratory vibration evidence;
- component-level information traceability;
- field feasibility;
- transparent inspection-maintenance support.

Supporting scope:
- BIM/IFC semantics;
- nominal FEM reference for field sensor placement;
- qualitative mechanical hypotheses clearly labelled as unconfirmed.

Future work:
- calibrated FEM and model updating;
- similitude-based lab-to-field transfer;
- RUL and predictive maintenance;
- weighted Health Index;
- multi-building deployment.

Out of scope:
- CFD;
- Smart City;
- Edge AI;
- field damage diagnosis;
- calibrated FEM used for diagnosis;
- stiffness-degradation or bolt-preload inference;
- direct lab classifier transfer to field;
- autonomous maintenance;
- commercial software development.

Every analytical prompt should require:

`Claim → Evidence → Limitation → Next action`

When evidence is inadequate, use exactly:

`Evidence is currently insufficient.`
