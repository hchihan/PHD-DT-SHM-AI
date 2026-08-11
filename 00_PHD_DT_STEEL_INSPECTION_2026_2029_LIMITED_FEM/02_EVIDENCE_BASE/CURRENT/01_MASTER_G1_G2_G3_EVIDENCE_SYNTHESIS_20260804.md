# MASTER G1-G2-G3 EVIDENCE SYNTHESIS 20260804

**Version:** v1.0
**Date / Updated:** 2026-08-04
**Status:** CURRENT OFFICIAL SYNTHESIS — NO GATE PASS DECLARED
**Source-of-truth level:** 5 (current synthesis; subordinate to Charter and ACCEPTED ADRs)
**Supersedes:** `reportG2-G3.md`, `PHD_G1_G2_G3_EVIDENCE_GAP_AND_THESIS_DIRECTION_REPORT_VI.md`, and the current-purpose use of `PAPER2_DIRECTION_AND_GATE_v2.1_20260719.md`.
**Superseded by:** None.
**Change summary:** Integrates G1 status and immutable Round 1-3B evidence into one corpus-bounded research direction, G2 Decision Register, conflict log and next-action plan.

## A. Executive Decision

**Claim:** The single thesis direction is:

```text
Vibration data
-> credible condition evidence
-> identity-governed BIM-linked component
-> accountable inspection record
-> event-aware action lifecycle
-> verified inspection-maintenance support
```

**Evidence:** Current Charter and ACCEPTED Action-ID ADR; G1 method evidence; Round 1-3B; current G1-G2 interface.

**Limitation:** G1 lacks accepted provenance-complete payload/sign-off; G2 is not frozen; G3 is not implemented or validated; exact event/authorization/verification rules remain proposed.

**Next action:** Close G1; govern and baseline G2; only then authorize a bounded G3 prototype.

Official search decision: **`CLOSE_SEARCH`**, bounded to the screened/deep-read corpus. It is not universal absence, does not support “first” or “no study worldwide”, and does not close G2.

## B. RQ-WP-Chapter-Paper-Gate Mapping

| RQ | WP | Chapter | Paper | Gate | Boundary |
|---|---|---|---|---|---|
| RQ1 | WP1 | C4 | Paper 1 | G1 | Laboratory condition/state-change evidence under run-aware leakage control |
| RQ2 | WP2 | C5 | Paper 2 | G2, G3, G6 | Identity-governed, event-aware, verification-controlled traceability specification and later bounded validation |
| RQ3 | WP3 | C6 | Paper 3 optional | G4, G5 | Field feasibility; minimum thesis evidence mandatory, no diagnosis |
| None | WP4 merged into WP2/WP3 | C7 optional/merge | Paper 4 optional | G5 | Human-reviewed management decision support; no autonomous action |

No RQ, WP, chapter, Paper or Gate belongs to FEM.

## C. Current Research Chain

Research chain:

```text
Vibration data
-> condition/state-change evidence
-> BIM-linked component
-> Inspection_Record
-> Action_Record
-> Status_Event
-> accountable authorization/review
-> post-action verification
-> guarded closure/reopen
-> inspection-maintenance action support
```

Identifier context:

```text
Sensor_ID
-> BIM_GUID / Asset_ID @ Model_Version_ID
-> Condition_Evidence_ID
-> Inspection_Record_ID
-> Action_Record_ID
-> Status_Event_ID  [PROPOSED; NOT ACCEPTED]
```

`Action_Status`/`Workflow_Status` is a current-state projection, not an identifier. Recommendation is not automatically an `Action_Record`; `completed` is not verified closure; defect severity is not `Action_Level`. `Verification_Record` versus `Inspection_Record` subtype remains **GOVERNANCE_DECISION_REQUIRED**.

## D. G1 Evidence, Status And Gap

**Claim:** G1 is `OPEN — PARTIAL EVIDENCE`.

**Evidence:** RQ1 addendum supports run-aware grouping, split-before-windowing, train-only preprocessing, run-level uncertainty and sensor-configuration comparison. Existing dataset/reanalysis artifacts are supporting/provisional.

**Limitation:** No accepted canonical run registry, complete sensor identity/provenance, accepted leakage-safe LORO/multi-seed package, ResNet1D provenance decision, run/fold uncertainty package or signed acceptance matrix.

**Next action:** Canonical run registry -> sensor provenance -> split audit -> leakage-safe LORO/multi-seed -> ResNet1D confirm/remove -> uncertainty -> acceptance/sign-off.

## E. G2 Prior Art, Novelty And Search Closure

### Established prior art — no independent novelty claim

Sensor-to-BIM integration; BIM-linked condition/inspection records; IFC GlobalId; BIM-CMMS integration; maintenance/action information; generic inspection-to-repair workflow; competency questions; provenance; SHACL/SPARQL/MVD/IDS/database validation; generic valid/invalid fixtures; direct/inverse navigation; generic human-in-the-loop; current status/repaired/unrepaired/completed flags; BIM viewer/dashboard/website.

### Central Paper 2 direction

An implementation-neutral, identity-governed, event-aware and verification-controlled evidence-to-action traceability specification, evaluated through chain-specific constraints, controlled valid/invalid fixtures, and paired forward/reverse competency queries.

### Core candidate gaps

- Stable Inspection_Record-Action_Record linkage and distinct Action_Record identity.
- Immutable/queryable Status_Event history and current-state reconstruction.
- Actor-bound approval, rejection, rework and authorization rules.
- Post-action verification and guarded closure/reopen.
- Complete identity-governed record-event-authorization-verification chain.

### Supporting candidate gaps

Evidence-basis preservation; chain-specific integrity mutations; exact machine-readable oracle; paired forward/reverse CQs and query-answer parity; separately declared transformation equivalence/permitted loss.

**Limitation:** These are candidate contribution boundaries, not completed contributions. Exact cardinalities, role permissions, lifecycle vocabulary and verification criteria require review.

**Next action:** Freeze the reviewed structural decisions in G2, complete missing specifications, obtain expert review and baseline before G3.

## F. G2 Final Decision Register

| Item | Decision | Basis / condition |
|---|---|---|
| BIM_GUID/Asset_ID/model version context | FREEZE | Stable external/contextual identity; no unnecessary Component_ID |
| Condition_Evidence_ID | FREEZE | Distinct evidence identity with provenance |
| Inspection_Record_ID | FREEZE | Distinct accountable inspection record identity |
| Action_Record_ID | FREEZE | ACCEPTED Action-ID ADR |
| Workflow_Status as current projection | FREEZE | Status is not identity or history |
| Append-only Status_Event | FREEZE | Structural requirement; exact ADR vocabulary still pending |
| Agent_ID structural role | FREEZE | Structural identity only; domain roles need expert review |
| Exact Inspection-Action cardinality | EXPERT_REVIEW_REQUIRED | Do not force 1:1 |
| Action lifecycle vocabulary | EXPERT_REVIEW_REQUIRED | Domain transitions unresolved |
| Role and permission matrix | EXPERT_REVIEW_REQUIRED | Authority and separation of duties unresolved |
| Authorization requirement | FREEZE_PROVISIONALLY | Exact permission rules pending expert review/ADR |
| Verification requirement | FREEZE | Post-action verification is distinct from generic provenance verification |
| Verification entity/subtype | FREEZE_PROVISIONALLY | Separate entity versus Inspection_Record subtype unresolved |
| Closure/reopen requirement | FREEZE_PROVISIONALLY | Exact policy and vocabulary pending review |
| Exact verification criteria | EXPERT_REVIEW_REQUIRED | Facility/domain criteria required |
| G1 evidence payload fields | WAIT_FOR_G1_PAYLOAD | Use real G1 Condition_Evidence only after provenance acceptance |
| Constraint families | FREEZE | Identity, relation, chronology, transition, authorization, evidence, closure |
| Fixture and machine-readable oracle | FREEZE | Exact expected-versus-actual assertion required |
| Paired forward/reverse CQ | FREEZE | Query-answer parity is distinct from round-trip transformation |
| Mandatory blockchain | REMOVE | Generic provenance instrument, not a requirement |
| Mandatory SHACL | REMOVE | Implementation-neutral constraints |
| Mandatory graph database | REMOVE | No technology mandate |
| Website/viewer as contribution | REMOVE | Supporting instrument only |
| Calibrated FEM | REMOVE | Outside thesis core and prohibited by Limited-FEM |

`FREEZE` means a G2 specification-development decision, not G2/G3 PASS.

## G. G3 Prerequisites And Prohibited Claims

**Claim:** G3 is `OPEN — NOT IMPLEMENTED, NOT VALIDATED, NOT OFFICIALLY PASSED`; execution is `NOT OPEN`.

**Evidence:** Current gate controls and roadmap require a reviewed/baselined G2 package before implementation.

**Limitation:** No ER baseline, approved CQ/expected-answer registry, Constraint Catalogue, Fixture/Oracle Manifest, expert review, G2 sign-off or executed validation package exists.

**Next action:** Do not build a website, database or G3 prototype. After G2 acceptance, implement only the smallest bounded, technology-neutral test instance. Use synthetic/controlled payloads until real G1 payload provenance is accepted.

Prohibited claims include G3 validation, field diagnosis, lab-to-field quantitative transfer, autonomous maintenance, calibrated FEM, stiffness degradation, predictive maintenance, RUL, tool novelty and universal literature absence.

## H. RQ3/G4 Boundary

**Claim:** Only G4 readiness/preparation may run in parallel.

**Evidence:** Charter permits low-cost field preparation and requires minimum field-feasibility evidence for the thesis.

**Limitation:** Field access is unconfirmed; no deployment, baseline or field scenario validation is accepted.

**Next action:** Confirm field access; prepare sensor register, BIM/GUID audit, mapping protocol, data governance and inspection templates. Do not claim field validation or diagnosis.

## I. WP4/G5 Boundary

**Claim:** WP4/G5 is human-reviewed management decision support, merged into WP2/WP3 and not a separate RQ.

**Evidence:** Current matrix and G5 addendum support transparent, traceable and accountable review.

**Limitation:** Exact action vocabulary, role matrix, verification criteria and facility-manager review are missing. Four-level labels are not evidence of validated decision logic.

**Next action:** Resolve expert-dependent vocabulary/permissions and retain scenario review evidence. No automated decision.

## J. Evidence Firewall

| Layer | May establish | Must not establish |
|---|---|---|
| Laboratory evidence | Controlled state discrimination and uncertainty | Field damage diagnosis or maintenance priority |
| Information traceability | Identity, records, provenance, events, constraints and query results | Detection accuracy, field feasibility or decision effectiveness |
| Field feasibility | Deployment/data return/baseline/workflow feasibility | Confirmed damage or lab classifier transfer |
| Management decision support | Human-reviewed action support and accountability | Autonomous action or engineering diagnosis |

FEM is **nominal, uncalibrated, reference-only, not used for damage diagnosis**. It has no RQ, WP, chapter, Paper or Gate and cannot support stiffness-degradation inference or quantitative lab-to-field transfer.

## K. Repository Conflicts Resolved

| OLD POSITION | NEW EVIDENCE | AUTHORITY | DECISION | FILES AFFECTED |
|---|---|---|---|---|
| Chain ends at Action_Status | ACCEPTED Action-ID ADR; Round 3A-3B scalar/event distinction | ACCEPTED ADR | End identity chain at Action_Record_ID; status is projection | Governance, status, roadmap, Paper 2, indexes |
| Current status equals history | Round 3A-3B | Current synthesis below ADR | Append-only Status_Event is structural; exact schema pending ADR | G2 files |
| Provenance verification equals post-action verification | Round 3B | Corpus-bounded evidence | Keep concepts distinct | Paper 2/G2 claims |
| Reverse lookup equals parity/round trip | Round 3A-3B | Corpus-bounded evidence | Separate navigation, paired query-answer parity and transformation round trip | CQ/validation language |
| CLOSE_SEARCH implies G2 PASS | Round 3B | Gate governance | Search closure is corpus-bounded only; G2 remains open | Status/index/roadmap |
| G2 specification and G3 implementation can overlap | Current gate order | Charter/gates | Baseline G2 before claimed G3 execution | Roadmap/status |
| G1 blocks all G2 work | Interface evidence | Current control | G1 closure and G2 specification governance run in parallel; real payload waits for G1 | Status/roadmap |
| FEM may support diagnosis/calibration | Limited-FEM decision | Supervisor/ACCEPTED ADR | Reference-only, uncalibrated, no diagnosis | All current controls |

## L. Remaining Governance Decisions

| Decision | Dependency |
|---|---|
| Accept/reject Action-Status-Event ADR and `Status_Event_ID` naming | Supervisor decision |
| Exact Inspection-Action cardinality | Expert review |
| Lifecycle vocabulary, role/permission matrix and authorization rules | Expert review + supervisor acceptance |
| Verification entity/subtype and exact criteria | Expert review + supervisor acceptance |
| Closure/reopen/override policy | Expert review |
| Real Condition_Evidence binding fields and eligibility | Accepted G1 payload |
| G4 deployment window | Field-access confirmation |

## M. Next-Action Plan

1. G1 canonical run registry.
2. Sensor identity/provenance and split-before-windowing audit.
3. Leakage-safe multi-seed LORO.
4. ResNet1D provenance decision.
5. Run/fold uncertainty and G1 acceptance.
6. Review ADR Action-Status-Event.
7. Complete G2 Decision Register and ER model.
8. Complete CQ Registry with expected answers.
9. Complete Constraint Catalogue.
10. Complete Fixture/Oracle Manifest.
11. Conduct expert review and supervisor approval.
12. Freeze/baseline G2.
13. Only then authorize a bounded G3 prototype.

## N. Source Inventory

### CURRENT_SOURCE_OF_TRUTH

This synthesis; current status; current governance set; Evidence Gates; Matrix.

### CURRENT_SUPPORTING

Living evidence base/pointer/migration report; RQ1/RQ2/RQ3/WP4 addenda; RQ2 README; G1-G2 interface; G2-G3 roadmap; Paper 1/2/3 directions; G1-G2 decision register.

### IMMUTABLE_EVIDENCE

Initial G2-G3 screening; Round 1; Round 2; recent screening 2023-2026; Round 3A; Round 3B; Zotero Phase 0/completion reports and deep-read matrix; all source PDFs/corpus files. Scientific content retained unchanged.

### SUPERSEDED

`PAPER2_DIRECTION_AND_GATE_v2.1_20260719.md`; `reportG2-G3.md`; `PHD_G1_G2_G3_EVIDENCE_GAP_AND_THESIS_DIRECTION_REPORT_VI.md`; early competitor matrix. See archive manifest.

### REVIEW_REQUIRED

Zotero writeback queue and duplicate/metadata correction log; proposed Action-Status-Event ADR; unresolved G1 payload and expert-dependent G2 decisions.
