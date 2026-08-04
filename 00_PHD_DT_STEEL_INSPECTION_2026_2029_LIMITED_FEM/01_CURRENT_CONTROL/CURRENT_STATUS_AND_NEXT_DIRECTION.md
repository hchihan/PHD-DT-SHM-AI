# CURRENT STATUS AND NEXT DIRECTION

**Effective date:** 2026-08-04
**Status:** CURRENT
**Scope:** RQ2, WP2, Chapter 5, Paper 2, G2-G3. G1 remains an upstream dependency.

## 1. Locked Status

| Item | Current state | Meaning |
|---|---|---|
| G1 | `OPEN / NOT READY` | No accepted Condition_Evidence payload or signed G1 acceptance matrix exists. Existing aggregate results remain supporting/provisional evidence. |
| G2 | `OPEN / SPECIFICATION DEVELOPMENT` | Define and review the traceability contract, competency questions, acceptance criteria, entity relations, identifiers, CEI metadata, and record schemas. |
| G3 | `NOT OPEN` | No end-to-end implementation or validation execution is authorized as G3 evidence yet. |
| Paper 2 | `DESIGN AND EVIDENCE DEVELOPMENT` | One paper will report the G2 specification and, later, the executed G3 validation. |

No gate is closed by this repository reset.

## 2. Current Direction

```text
Vibration data
-> condition/state-change evidence
-> BIM-linked component
-> Inspection_Record
-> Action_Record
-> Status_Event
-> inspection-maintenance action support
```

```text
Sensor_ID
-> BIM_GUID
-> Condition_Evidence_ID
-> Inspection_Record_ID
-> Action_Record_ID
```

`Action_Status` is attached to `Action_Record`; status changes are represented by `Status_Event`. CEI remains structured evidence metadata and cannot be converted into a scalar, Health Index, severity, damage probability, or priority without new approved evidence and governance.

## 3. Paper 2 Boundary

- Paper 2 is the single current RQ2 publication direction.
- G2 supplies the preregistered specification and acceptance basis.
- G3, when opened, supplies executed end-to-end validation and negative-test evidence.
- Paper 2A, Paper 2B, dual-paper, and split-roadmap commitments are superseded.
- Paper 2 does not claim field damage diagnosis, autonomous action, predictive maintenance, RUL, calibrated FEM, or a universal Health Index.

## 4. Instrument Boundary

Revit, IFC, Dynamo, Pset, IDS, SQLite, and any viewer are supporting implementation instruments. Their presence or execution is not the novelty and cannot substitute for traceability completeness, provenance, integrity validation, human review, or gate acceptance. **Do not run Graph 02.**

FEM is **nominal, uncalibrated, reference-only, not used for damage diagnosis**.

## 5. Immediate Work Order

1. Resolve open G1-to-G2 interface decisions in `G1_G2_INTERFACE_DECISION_REGISTER.csv` without fabricating missing G1 evidence.
2. Lock G2 competency questions and acceptance criteria before implementation.
3. Complete the minimum entity/relationship, identifier, CEI, `Inspection_Record`, `Action_Record`, and `Status_Event` specifications.
4. Define positive, negative, orphan, duplicate, missing-field, status-transition, and round-trip validation cases.
5. Hold a G2 readiness review. Do not open G3 unless the review explicitly accepts the G2 package.
6. After G3 opens, implement the smallest technology-neutral reference instance and retain executed validation evidence.

## 6. Evidence Limitation

The repository contains substantial design evidence and deep-read synthesis but no accepted G1 Condition_Evidence payload, no approved G2 package, and no executed G3 validation package. **Evidence is currently insufficient** to claim G1, G2, or G3 completion.
