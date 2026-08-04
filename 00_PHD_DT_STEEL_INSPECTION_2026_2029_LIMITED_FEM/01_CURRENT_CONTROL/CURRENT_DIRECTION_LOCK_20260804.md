# CURRENT DIRECTION LOCK 20260804

**Effective date:** 2026-08-04
**Status:** CURRENT AND BINDING FOR EXECUTION
**Authority:** Subordinate to the v2.1 Charter and approved governance set; controlling over lower-ranked working plans and paper notes.

## 1. Locked Research Direction

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

`Action_Status` is an attribute or current-state projection of `Action_Record`. A change in state is represented by a `Status_Event` with accountable actor, timestamp, reason, and version context.

## 2. Locked States

| Item | State |
|---|---|
| G1 | `OPEN / NOT READY` |
| G2 | `OPEN / SPECIFICATION DEVELOPMENT` |
| G3 | `NOT OPEN` |
| Paper 2 | `DESIGN AND EVIDENCE DEVELOPMENT` |

No existing aggregate result, schema draft, literature review, software prototype, or repository reset closes a gate.

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
2. comparison against the v2.1 Charter and structural set;
3. supervisor review where the proposal affects an approved research commitment; and
4. synchronized updates to this lock, the source-of-truth hierarchy, current status, roadmap, Paper 2 direction, and master index.

Absent that process, this document controls execution.
