# CURRENT DIRECTION LOCK 20260804

**Version:** v1.2 administrative alignment
**Effective date / Updated:** 11/08/2026
**Status:** CURRENT AND BINDING FOR EXECUTION | **Source-of-truth level:** 4
**Authority:** Subordinate to the 17/07 Limited-FEM Charter, ADR-2026-001 and Council Review.
**Supersedes:** v1.1 administrative alignment. | **Superseded by:** None.
**Changes in this version:** Restores the canonical 17/07 chains and records evidence status through 11/08/2026; no Gate is closed.

## 1. Locked Research Direction

```text
Vibration data
-> condition/state-change evidence
-> BIM-linked component
-> inspection record
-> inspection-maintenance action support
```

```text
Sensor_ID
-> BIM_GUID
-> Condition_Evidence_ID
-> Inspection_Record_ID
-> Action_Status
```

`Action_Status` is the canonical endpoint. `Asset_ID`, `Model_Version_ID`, `Action_Record_ID`, `Workflow_Status` and `Status_Event` are noncanonical implementation proposals unless separately approved. They do not replace or extend the locked chain.

## 2. Locked States

| Item | State |
|---|---|
| G1 | `OPEN — PARTIAL EVIDENCE` |
| G2 | `OPEN — LITERATURE BOUNDARY CLOSED, SPECIFICATION NOT YET FROZEN` |
| G3 | `OPEN — NOT IMPLEMENTED, NOT VALIDATED, NOT OFFICIALLY PASSED`; execution `NOT OPEN` |
| G4 | `READINESS/PREPARATION ONLY — FIELD ACCESS UNCONFIRMED` |
| Paper 2 | `DESIGN AND EVIDENCE DEVELOPMENT` |

No existing aggregate result, schema draft, literature review, software prototype, or repository reset closes a gate.

`CLOSE_SEARCH` is corpus-bounded. It is not universal absence, does not support a "first" claim, and does not constitute G2 PASS.

## 3. Paper 2 Lock

- There is one current Paper 2.
- Its first evidence phase is G2 specification and preregistration.
- Its second evidence phase is G3 executed validation, which may begin only after an explicit G2 readiness decision.
- Paper 2A, Paper 2B, split-paper, and dual-paper roadmap commitments are superseded.
- G2 and G3 remain separate evidence gates even though they are reported in one paper.

## 4. CEI Lock

CEI is a mandatory structured metadata record attached to each `Condition_Evidence_ID`. It records evidence validity, confidence basis, run/fold variability, sensor configuration, data quality, provenance, timestamp, and version. CEI is not:

- a universal scalar;
- a Health Index;
- damage severity;
- damage probability;
- maintenance priority; or
- an authorization to inspect or act.

## 5. Instrument Lock

Revit, IFC, Dynamo, Pset, IDS, SQLite, viewers, and validation languages are supporting instruments. They may instantiate or test the specification but are not the central novelty. The contribution is the governed, verifiable evidence-to-record-to-action traceability contract and its validation.

**Do not run Graph 02.** No graph execution is authorized as G3 evidence while G3 is `NOT OPEN`.

## 6. Scope Guardrails

FEM is **nominal, uncalibrated, reference-only, not used for damage diagnosis**.

The current direction does not include calibrated FEM, EMA/MAC acceptance, stiffness-degradation inference, field damage diagnosis, RUL, predictive maintenance, weighted Health Index, autonomous maintenance, or automatic authorization of inspection or maintenance actions.

## 7. Change Control

Any proposed change to the locked chain, identifier chain, CEI meaning, gate order, or single-Paper-2 structure requires:

1. a written change request with evidence and impact;
2. comparison against the 17/07 Limited-FEM Charter, ADR-2026-001 and Council Review;
3. supervisor review where the proposal affects an approved research commitment; and
4. synchronized updates to this lock, the source-of-truth hierarchy, current status, roadmap, Paper 2 direction, and master index.

Absent that process, this document controls execution.
