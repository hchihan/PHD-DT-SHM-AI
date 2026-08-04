# G2-G3 PAPER 2 CURRENT ROADMAP v2.1

**Date:** 2026-08-04
**Status:** CURRENT ROADMAP
**Mapping:** RQ2 -> WP2 -> Chapter 5 -> Paper 2 -> G2, G3, G6

## 1. Objective

Develop and validate one implementation-neutral traceability specification that connects bounded condition/state-change evidence to a BIM-linked component, inspection record, accountable action record, and status-event history for human-reviewed inspection-maintenance action support.

This roadmap does not close G1, G2, or G3. Current states are:

| Item | State |
|---|---|
| G1 | `OPEN / NOT READY` |
| G2 | `OPEN / SPECIFICATION DEVELOPMENT` |
| G3 | `NOT OPEN` |
| Paper 2 | `DESIGN AND EVIDENCE DEVELOPMENT` |

## 2. Scope Classification

| Class | Included work |
|---|---|
| Core | Traceability requirements; entity and relationship model; identifier integrity; CEI metadata; competency questions; acceptance criteria; review/accountability; positive and negative validation; bidirectional traceability |
| Supporting | Revit/IFC mapping, Pset/IDS representation, SQLite reference instance, Dynamo or scripts, viewer demonstrations, legal/management-obligation references pending official-source verification |
| Future Work | Field deployment, field baseline validation, broader asset classes, production integration |
| Out of Scope | Field damage diagnosis, calibrated FEM, RUL, predictive maintenance, weighted Health Index, autonomous decision or action, commercial product development |

FEM is **nominal, uncalibrated, reference-only, not used for damage diagnosis**.

## 3. Phase A - G2 Specification Development

G2 remains open until every required item is reviewed against explicit acceptance criteria.

| Workstream | Required output | Minimum acceptance basis | Current state |
|---|---|---|---|
| G1-to-G2 contract | `04_SCHEMA_RULES/G1_TO_G2_CONDITION_EVIDENCE_INTERFACE_v1.0.md` | Required fields, provenance, granularity, review, supersession, candidate/verified binding, prohibited interpretations | WORKING SPECIFICATION |
| Open decisions | `../01_CURRENT_CONTROL/G1_G2_INTERFACE_DECISION_REGISTER.csv` | Every unresolved normative choice has owner, evidence requirement, reviewer, and due-before state | OPEN |
| Competency questions | Versioned SCQ/VCQ/RCQ register | Questions preregistered before implementation; each maps to a testable criterion | NOT YET ACCEPTED |
| Entity and relationship model | Versioned model for evidence, component, inspection, action, status event, actors, and provenance | Cardinality, identity, lifecycle, and orphan rules explicit | NOT YET ACCEPTED |
| Identifier rules | Versioned identifier and mapping specification | Uniqueness, non-reuse, foreign-key integrity, model-version context, and ambiguity handling | NOT YET ACCEPTED |
| CEI metadata | Versioned CEI dictionary/schema | Structured dimensions and provenance; no scalar/severity/priority semantics | NOT YET ACCEPTED |
| `Inspection_Record` | Minimum schema and lifecycle | Observation/finding separation, actor, time, version, approval, evidence links | NOT YET ACCEPTED |
| `Action_Record` | Minimum schema and lifecycle | Accountable rationale, evidence and inspection links, role, approval, status projection | NOT YET ACCEPTED |
| `Status_Event` | Event schema and transition rules | Append-only history, legal transitions, actor/time/reason/version | NOT YET ACCEPTED |
| Validation plan | Positive, negative, integrity, and round-trip fixtures | Expected results and pass/fail rules fixed before execution | NOT YET ACCEPTED |

### G2 readiness decision

G2 may move to ready-for-review only when the complete specification package is internally consistent, all mandatory decisions are resolved or explicitly deferred without blocking validation, every competency question has an acceptance criterion, and the validation fixtures are preregistered.

Only an explicit reviewer decision may open G3. A draft schema, functioning database, IFC export, or successful graph run is insufficient.

## 4. Phase B - G3 Executed Validation

**Current state: NOT OPEN.** Do not implement this phase as claimed gate evidence until the G2 readiness decision authorizes it.

When opened, G3 must use the smallest implementation capable of testing the specification rather than optimizing a software platform.

Required evidence classes:

1. versioned reference dataset or fixtures with provenance;
2. full forward trace from evidence to component, inspection, action, and status event;
3. reverse trace from action or component to source evidence and CEI;
4. orphan and missing-reference rejection;
5. duplicate-identifier rejection;
6. missing-CEI and malformed-CEI rejection;
7. invalid status-transition rejection;
8. candidate-versus-verified BIM-binding tests;
9. unauthorized review/approval transition rejection;
10. version/supersession and stale-model-binding tests;
11. round-trip integrity evidence; and
12. reproducible execution log with input, implementation, environment, and output versions.

The implementation technology may include JSON Schema, SQL constraints, SHACL, ShEx, SPARQL, IDS, or equivalent mechanisms. Tool choice must follow the approved competency questions and cannot redefine the research contribution.

**Do not run Graph 02.** Revit, IFC, Dynamo, Pset, IDS, SQLite, and viewers remain supporting instruments.

## 5. Phase C - Paper 2 Evidence Assembly

Paper 2 is one paper. It may be assembled progressively but cannot claim G3 validation before execution evidence exists.

| Paper section | Required evidence |
|---|---|
| Problem and gap | Verified literature and competitor boundary |
| Requirements | Governance, stakeholder/accountability needs, competency questions |
| Specification | Entity/relationship, identifier, CEI, lifecycle, and validation rules |
| Method | Preregistered validation design and fixtures |
| Results | Executed G3 test outcomes only; no planned result presented as observed |
| Discussion | Contribution boundary, implementation neutrality, limitations, transferability |
| Conclusion | Claims bounded to accepted G2 and executed G3 evidence |

G6 remains open until the paper is submitted and the submission record exists.

## 6. Immediate Sequence

1. Review and resolve the G1-to-G2 decision register.
2. Preregister SCQ, VCQ, RCQ, and acceptance criteria.
3. Finalize the minimum entity, identifier, CEI, record, lifecycle, and accountability specifications.
4. Preregister validation fixtures and expected outcomes.
5. Conduct the G2 readiness review.
6. Open G3 only through an explicit acceptance decision.
7. Execute the minimal reference implementation and retain reproducible validation evidence.
8. Complete Paper 2 results and claims from accepted evidence.

## 7. Stop Conditions

Stop and return to G2 if implementation requires an undefined identifier, cardinality, lifecycle transition, approval role, CEI field, ambiguity policy, or acceptance rule. Stop if a tool-specific design begins to drive the research question. Stop if any output is interpreted as damage diagnosis, severity, maintenance priority, or automatic authorization.
