# START HERE

**Current navigation date:** 2026-08-04
**Architecture:** Limited-FEM, Traceability-Core v2.1
**Current work:** G2 specification development for one unified Paper 2; G3 is not open.

The academic source of truth remains `00_GOVERNANCE/MASTER_RESEARCH_CHARTER_v2.1_TRACEABILITY_CORE_20260719.md`. For conflicts, use `00_GOVERNANCE/SOURCE_OF_TRUTH_HIERARCHY_v2.1.md`.

## Locked Research Chain

```text
Vibration data
-> condition/state-change evidence
-> BIM-linked component
-> Inspection_Record
-> Action_Record
-> Status_Event
-> inspection-maintenance action support
```

Identifier chain:

```text
Sensor_ID -> BIM_GUID -> Condition_Evidence_ID -> Inspection_Record_ID -> Action_Record_ID
```

`Action_Status` belongs to `Action_Record`. CEI is mandatory structured metadata, not a scalar, Health Index, severity, damage probability, or priority. FEM is **nominal, uncalibrated, reference-only, not used for damage diagnosis**.

## Current States

| Item | State |
|---|---|
| G1 | `OPEN / NOT READY` |
| G2 | `OPEN / SPECIFICATION DEVELOPMENT` |
| G3 | `NOT OPEN` |
| Paper 2 | `DESIGN AND EVIDENCE DEVELOPMENT` |

Paper 2 combines G2 specification and later G3 executed validation. There is no current Paper 2A, Paper 2B, or dual-paper commitment.

## Read In This Order

1. `00_GOVERNANCE/MASTER_RESEARCH_CHARTER_v2.1_TRACEABILITY_CORE_20260719.md`
2. `00_GOVERNANCE/SOURCE_OF_TRUTH_HIERARCHY_v2.1.md`
3. `01_CURRENT_CONTROL/CURRENT_DIRECTION_LOCK_20260804.md`
4. `01_CURRENT_CONTROL/CURRENT_STATUS_AND_NEXT_DIRECTION.md`
5. `05_GATE2/G2_G3_PAPER2_CURRENT_ROADMAP_v2.1_20260804.md`
6. `03_PAPERS/PAPER_2/PAPER2_CURRENT_DIRECTION_v2.1_20260804.md`
7. `05_GATE2/04_SCHEMA_RULES/G1_TO_G2_CONDITION_EVIDENCE_INTERFACE_v1.0.md`
8. `01_CURRENT_CONTROL/MASTER_INDEX_CURRENT.md`

## Execution Boundary

- Current work is specification, evidence mapping, competency questions, acceptance criteria, and schema rules.
- Do not begin G3 implementation until G2 readiness is reviewed and explicitly accepted.
- Do not run Graph 02.
- Revit, IFC, Dynamo, Pset, IDS, and SQLite are supporting instruments, not the thesis novelty.
- No tool output, demo, or planned artifact closes a gate without the required validation and sign-off evidence.

Deep-read reports, empirical evidence, result CSVs, models, and prior archives are preserved as evidence or provenance. They are not current navigation authority unless explicitly listed in `01_CURRENT_CONTROL/MASTER_INDEX_CURRENT.md`.
