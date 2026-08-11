# CURRENT STATUS AND NEXT DIRECTION

**Version:** v2.2
**Effective date / Updated:** 2026-08-04
**Status:** CURRENT SOURCE OF EXECUTION STATUS | **Source-of-truth level:** 5
**Scope:** Entire thesis execution state, with G1 closure, G2 specification governance and G4 readiness as parallel streams.
**Supersedes:** v2.1 status wording. | **Superseded by:** None.
**Change summary:** Incorporates Round 1-3B, corpus-bounded `CLOSE_SEARCH`, exact G1/G2/G3 status, proposed Action-Status-Event ADR, and the three permitted parallel workstreams.

## 1. Locked Status

| Item | Current state | Meaning |
|---|---|---|
| G1 | `OPEN — PARTIAL EVIDENCE` | Supporting dataset/reanalysis documentation exists, but no accepted Condition_Evidence payload or signed G1 acceptance matrix exists. |
| G2 | `OPEN — LITERATURE BOUNDARY CLOSED, SPECIFICATION NOT YET FROZEN` | Round 1-3B closes the corpus-bounded structural search; required specification artifacts, review and baseline are missing. |
| G3 | `OPEN — NOT IMPLEMENTED, NOT VALIDATED, NOT OFFICIALLY PASSED` | The gate remains unresolved; execution authorization is `NOT OPEN` until G2 is baselined and explicitly accepted. |
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
-> BIM_GUID / Asset_ID @ Model_Version_ID
-> Condition_Evidence_ID
-> Inspection_Record_ID
-> Action_Record_ID
```

`Action_Status`/`Workflow_Status` is the current-state projection of `Action_Record`; it is not an identifier. Candidate append-only history is represented by `Status_Event`, subject to `../00_GOVERNANCE/ADR_ACTION_STATUS_EVENT_20260804_DRAFT.md` (`PROPOSED — NOT YET ACCEPTED`). Recommendation is not automatically an `Action_Record`; `completed` is not verified closure; defect severity is not `Action_Level`. Do not add `Component_ID` to the canonical chain when `Asset_ID + BIM_GUID + Model_Version_ID` is sufficient. A database surrogate key is technical only. CEI remains structured evidence metadata and cannot be converted into a scalar, Health Index, severity, damage probability, or priority without new approved evidence and governance.

## 3. Paper 2 Boundary

- Paper 2 is the single current RQ2 publication direction.
- G2 supplies the preregistered specification and acceptance basis.
- G3, when opened, supplies executed end-to-end validation and negative-test evidence.
- Paper 2A, Paper 2B, dual-paper, and split-roadmap commitments are superseded.
- Paper 2 does not claim field damage diagnosis, autonomous action, predictive maintenance, RUL, calibrated FEM, or a universal Health Index.

**Literature decision:** `CLOSE_SEARCH`. This is bounded to the screened/deep-read corpus, is not universal absence, does not authorize a "first" claim, and does not close G2. Reopen broad search only if a new question is likely to change the structural novelty boundary.

## 4. Instrument Boundary

Revit, IFC, Dynamo, Pset, IDS, SQLite, and any viewer are supporting implementation instruments. Their presence or execution is not the novelty and cannot substitute for traceability completeness, provenance, integrity validation, human review, or gate acceptance. **Do not run Graph 02.**

FEM is **nominal, uncalibrated, reference-only, not used for damage diagnosis**.

## 5. Three Parallel Workstreams

### Stream A — G1 closure

1. Lock the canonical run registry and sensor identity/provenance.
2. Audit split-before-windowing and train-only preprocessing.
3. Execute leakage-safe run-aware/LORO evaluation with multiple seeds.
4. Confirm or remove ResNet1D based on provenance.
5. Report run/fold uncertainty and complete the acceptance matrix/sign-off.

### Stream B — G2 specification governance

1. Review the proposed Action-Status-Event ADR; do not treat it as accepted.
2. Complete the G2 Final Decision Register, ER model and identifier governance.
3. Preregister CQ Registry plus expected answers.
4. Complete Constraint Catalogue and Fixture/Oracle Manifest.
5. Conduct expert review, approval and baseline. Do not start claimed G3 execution before this.

### Stream C — G4 readiness only

1. Confirm field-access basis.
2. Prepare the field sensor register, BIM/GUID stability audit, mapping protocol and inspection templates.
3. Do not deploy, claim field validation or use G4 evidence to close G1/G2/G3.

## 6. Evidence Limitation

The repository contains substantial design evidence and immutable Round 1-3B deep-read synthesis but no accepted G1 Condition_Evidence payload, no approved/baselined G2 package, and no executed G3 validation package. **Evidence is currently insufficient** to claim G1, G2, or G3 completion.

Legal and management-obligation references remain pending official-source verification. Field-access evidence remains unresolved for G4 but does not authorize or block the current G2 specification work. Historical `Action_Status`-as-chain notation remains in protected evidence and archives; it is not current and must not be propagated.
