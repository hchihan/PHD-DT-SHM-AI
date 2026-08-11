# CURRENT RESEARCH CONTEXT — 2026-08-04

## Thesis identity

**Field:** Construction Management / Asset Management.

**Core problem:** condition evidence from vibration data is often disconnected from component identity, inspection records and accountable action history. The thesis develops and validates a transparent information-management chain rather than a new damage-diagnosis algorithm.

## Locked research chain

```text
Vibration data
→ condition/state-change evidence
→ BIM-linked component
→ inspection record
→ inspection-maintenance action support
```

## RQ–WP–Chapter–Paper mapping

| RQ | WP | Chapter | Paper | Gate | Main evidence |
|---|---|---|---|---|---|
| RQ1 | WP1 | C4 | Paper 1 | G1 | Leakage-safe, run-aware laboratory evidence |
| RQ2 | WP2 | C5 | Paper 2 | G2–G3 | Formal evidence-to-action traceability |
| RQ3 | WP3 | C6 | Paper 3 | G4 | Field feasibility, not field diagnosis |
| Synthesis | WP4 | C7 or merge C6 | Paper 4 optional | G5 | Human-reviewed inspection-action support |

## Paper 2 current direction

```text
Condition_Evidence
→ BIM-linked component
→ Inspection_Record
→ Action_Record
→ Status_Event
→ accountable authorization/review
→ post-action verification
→ guarded closure/reopen
```

This is the design boundary for G2. It is not an implemented result.

## Current novelty boundary

### Established prior art

Sensor-to-BIM, BIM-linked inspection records, IFC GlobalId, BIM–CMMS integration, action information, competency questions, provenance, SHACL, generic fixtures, direct/inverse navigation, and generic human review.

### Narrowed or supporting gaps

- stable Inspection_Record–Action_Record relation;
- evidence-basis preservation;
- chain-specific integrity mutations;
- paired forward/reverse queries;
- query-answer parity;
- declared transformation equivalence and permitted loss.

### Strong core candidates

- immutable/queryable maintenance Status_Event history;
- accountable approval/rejection/rework;
- actor-bound authorization;
- formal post-action verification;
- guarded closure/reopen;
- complete identity-governed evidence-to-action record–event chain.

The integrated chain is the defensible unit of contribution. Individual techniques are not.

## Search decision

`CLOSE_SEARCH`

Remaining uncertainty is transferred to:

- governance decisions;
- expert review;
- G1 payload;
- later executable validation.

## Current priority

1. G1 run registry;
2. leakage-safe LORO;
3. ResNet1D provenance decision;
4. G1 acceptance;
5. ADR Action–Status–Event;
6. G2 Decision Register;
7. ER model;
8. CQ Registry;
9. Constraint Catalogue;
10. Fixture/Oracle Manifest;
11. expert review;
12. G2 freeze;
13. bounded G3 prototype.
