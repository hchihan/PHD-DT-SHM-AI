# START HERE

**Version:** v2.2
**Current navigation date / Updated:** 2026-08-04
**Status:** CURRENT SUPPORTING NAVIGATION | **Source-of-truth level:** 7
**Supersedes:** Initial 2026-08-04 G2 navigation. | **Superseded by:** None.
**Change summary:** Fixes moved paths, includes Round 3A-3B and routes readers through the single Evidence Base master index.
**Architecture:** Limited-FEM, Traceability-Core
**Current work:** G2 specification governance for one Paper 2; G3 execution is not open.

The academic source of truth remains `../../00_GOVERNANCE/MASTER_RESEARCH_CHARTER_v2.1_TRACEABILITY_CORE_20260719.md`. For conflicts, use `../../00_GOVERNANCE/SOURCE_OF_TRUTH_HIERARCHY_v2.1.md`. Evidence Base entry: `../CURRENT/00_MASTER_INDEX_CURRENT_20260804.md`.

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
Sensor_ID -> BIM_GUID / Asset_ID @ Model_Version_ID -> Condition_Evidence_ID -> Inspection_Record_ID -> Action_Record_ID
```

`Action_Status`/`Workflow_Status` is a current-state projection of `Action_Record`, never an identifier. Candidate `Status_Event` history is pending the proposed ADR. Recommendation is not an Action_Record and `completed` is not verified closure. CEI is mandatory structured metadata, not a scalar, Health Index, severity, damage probability, or priority. FEM is **nominal, uncalibrated, reference-only, not used for damage diagnosis**.

## Current States

| Item | State |
|---|---|
| G1 | `OPEN — PARTIAL EVIDENCE` |
| G2 | `OPEN — LITERATURE BOUNDARY CLOSED, SPECIFICATION NOT YET FROZEN` |
| G3 | `OPEN — NOT IMPLEMENTED, NOT VALIDATED, NOT OFFICIALLY PASSED`; execution `NOT OPEN` |
| Paper 2 | `DESIGN AND EVIDENCE DEVELOPMENT` |

Paper 2 combines G2 specification and later G3 executed validation. There is no current Paper 2A, Paper 2B, or dual-paper commitment.

## Read In This Order

1. `../CURRENT/00_MASTER_INDEX_CURRENT_20260804.md`
2. `../../00_GOVERNANCE/MASTER_RESEARCH_CHARTER_v2.1_TRACEABILITY_CORE_20260719.md`
3. `../../00_GOVERNANCE/SOURCE_OF_TRUTH_HIERARCHY_v2.1.md`
4. `../CURRENT/01_MASTER_G1_G2_G3_EVIDENCE_SYNTHESIS_20260804.md`
5. `../../01_CURRENT_CONTROL/CURRENT_STATUS_AND_NEXT_DIRECTION.md`
6. `G2_G3_ROUND1_DEEP_READ_AND_NOVELTY_BOUNDARY.md` through `G2_G3_ROUND3B_HISTORY_ACCOUNTABILITY_AND_SEARCH_CLOSURE.md` as immutable evidence
7. `G2_G3_PAPER2_CURRENT_ROADMAP_v2.1_20260804.md`
8. `G1_TO_G2_CONDITION_EVIDENCE_INTERFACE_v1.0.md`
9. `../../03_PAPERS/PAPER_2/PAPER2_CURRENT_DIRECTION_v2.1_20260804.md`

## Execution Boundary

- Current work is specification, evidence mapping, competency questions, acceptance criteria, and schema rules.
- Do not begin G3 implementation until G2 readiness is reviewed and explicitly accepted.
- Do not run Graph 02.
- Revit, IFC, Dynamo, Pset, IDS, and SQLite are supporting instruments, not the thesis novelty.
- No tool output, demo, or planned artifact closes a gate without the required validation and sign-off evidence.

Deep-read reports, empirical evidence, result CSVs, models, and prior archives are preserved as evidence or provenance. `CLOSE_SEARCH` is corpus-bounded and not a gate decision. They are not current navigation authority unless listed in the master index.
