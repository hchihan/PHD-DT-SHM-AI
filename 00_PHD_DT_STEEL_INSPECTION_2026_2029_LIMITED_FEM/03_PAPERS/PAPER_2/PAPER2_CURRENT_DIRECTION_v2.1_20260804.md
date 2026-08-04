# PAPER 2 CURRENT DIRECTION v2.1

**Date:** 2026-08-04
**Status:** DESIGN AND EVIDENCE DEVELOPMENT
**Mapping:** RQ2 -> WP2 -> Chapter 5 -> Paper 2 -> G2, G3, G6

## 1. Paper Direction

Paper 2 develops and validates a governed, implementation-neutral traceability specification for connecting condition/state-change evidence and its CEI metadata to BIM-linked components, inspection records, accountable action records, and status-event histories.

Research question:

> How can condition evidence and its confidence be organised and linked to BIM components and inspection records to enable verifiable justification and accountability of inspection decisions under limited field damage data?

The paper is positioned in construction information management and asset/inspection management. Its novelty is not a software stack, BIM viewer, database, ontology in isolation, or automatic maintenance decision.

## 2. Single-Paper Structure

Paper 2 contains two sequential evidence phases:

1. **G2 specification:** preregistered competency questions and acceptance criteria; entity, identifier, CEI, record, lifecycle, provenance, and accountability rules.
2. **G3 validation:** executed positive, negative, integrity, authorization, versioning, and round-trip tests after G2 readiness is accepted.

G2 and G3 remain separate gates. Combining their evidence in one paper does not permit implementation before specification readiness. Paper 2A, Paper 2B, and dual-paper commitments are superseded.

## 3. Core Contribution

The intended contribution is a verifiable contract in which:

```text
Vibration data
-> condition/state-change evidence
-> BIM-linked component
-> Inspection_Record
-> Action_Record
-> Status_Event
-> inspection-maintenance action support
```

and:

```text
Sensor_ID
-> BIM_GUID
-> Condition_Evidence_ID
-> Inspection_Record_ID
-> Action_Record_ID
```

can be traversed, validated, reviewed, versioned, and audited without converting laboratory evidence into a field diagnosis or automated action.

## 4. Claim Boundary

### Claims allowed only after supporting evidence exists

- the specification defines explicit identity, provenance, cardinality, lifecycle, and accountability rules;
- competency questions are mapped to executable acceptance tests;
- valid records support complete forward and reverse traceability;
- invalid records are rejected by preregistered negative and integrity tests;
- review, approval, status change, versioning, and supersession remain auditable; and
- the reference implementation demonstrates implementation feasibility without making the tools the novelty.

### Claims prohibited

- condition evidence diagnoses field damage;
- CEI is a scalar Health Index, severity, damage probability, or priority;
- the framework authorizes inspection or maintenance automatically;
- laboratory model confidence transfers directly to field performance;
- calibrated FEM, stiffness degradation, RUL, or predictive maintenance is demonstrated; or
- Revit, IFC, Dynamo, Pset, IDS, SQLite, or a viewer is itself the scientific contribution.

FEM is **nominal, uncalibrated, reference-only, not used for damage diagnosis**.

## 5. CEI Position

CEI is a mandatory structured metadata record associated with `Condition_Evidence_ID`. At minimum it retains evidence-validity status, confidence basis and scale, run/fold variability, sensor configuration, data-quality status, provenance, timestamp, and version. It supports interpretation and review; it does not prescribe an action.

## 6. Accountability Position

Accountability means the ability to trace roles, evidence sources, record creators and reviewers, timestamps, versions, approval states, rationales, and applicable management obligations. It does not assign personal legal liability.

`Action_Record_ID` is the stable action-record identity. `Action_Status` is its current-state attribute or projection. Each change is retained as a `Status_Event` rather than overwriting history without trace.

## 7. Method And Validation

The method must proceed in this order:

1. evidence and competitor review;
2. requirements and competency-question preregistration;
3. specification and expected validation outcomes;
4. G2 readiness review;
5. minimal reference implementation;
6. executed positive and negative validation;
7. cross-file and claim-evidence audit; and
8. paper assembly and G6 submission record.

The validation must include complete-chain, reverse-trace, orphan, duplicate, missing-CEI, invalid-transition, authorization, candidate/verified binding, version/supersession, stale-binding, and round-trip cases.

## 8. Tool Boundary

Revit, IFC, Dynamo, Pset, IDS, SQLite, semantic validation languages, and viewers may be selected only to instantiate or test approved requirements. **Do not run Graph 02.** G3 is `NOT OPEN` until G2 readiness is explicitly accepted.

## 9. Current Evidence State

The current deep-read reports and interface specification support the design boundary. They do not provide an accepted G2 package or executed G3 validation. G1 also remains `OPEN / NOT READY`, so no accepted upstream `Condition_Evidence` payload is available.

**Evidence is currently insufficient** to claim G2 completion, G3 validation, or Paper 2 submission readiness.

## 10. Next Action

Resolve the interface decision register, preregister competency questions and acceptance criteria, complete the minimum schemas and lifecycle rules, and conduct a G2 readiness review before implementation.
