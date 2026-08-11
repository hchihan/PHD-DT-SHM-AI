# ADR ACTION-STATUS-EVENT 20260804 — DRAFT

**Version:** v0.1
**Date / Updated:** 2026-08-04
**Status:** **PROPOSED — NOT YET ACCEPTED**
**Source-of-truth level:** Decision input only; below all ACCEPTED ADRs
**Supersedes:** None.
**Superseded by:** None.
**Change summary:** Records the unresolved Action-Status-Event, authorization, verification and closure decisions exposed by Round 1-3B. It does not amend the Charter or the accepted Action-ID ADR.

## Context

The ACCEPTED `RESEARCH_ARCHITECTURE_DECISION_RECORD_ACTION_ID_20260719.md` establishes `Action_Record_ID`, removes `Action_Status` from the identifier chain and refers historically to `Action_Status_Event_ID`. Round 3A-3B supports separating stable action identity, current-state projection and append-only event history, but does not supply authority to accept exact lifecycle vocabulary, role permissions, verification criteria or closure/reopen policy.

## Proposed Decision

Subject to supervisor approval and expert review:

1. Keep the canonical identifier chain ending at `Action_Record_ID`.
2. Treat `Action_Status`/`Workflow_Status` as a current-state projection or attribute, never an identifier.
3. Use `Status_Event_ID` as the candidate stable identity for an append-only event linked to one `Action_Record_ID`.
4. Require at least prior state, new state, actor/role, occurred-at, reason, record version, authorization context and source reference.
5. Distinguish recommendation, authorized action, execution, post-action verification and closure.
6. Prohibit `completed` from implying verified closure.
7. Require accepted post-action verification and an authorized closer before closure; preserve prior closure when reopening.
8. Permit `Verification_Record` as either a separate entity or an `Inspection_Record` subtype only after an explicit reviewed choice.
9. Keep exact Inspection_Record-Action_Record cardinality, lifecycle vocabulary, role/permission matrix, verification criteria and exceptional override rules open for expert review.

## Identifier Context

```text
Sensor_ID
-> BIM_GUID / Asset_ID @ Model_Version_ID
-> Condition_Evidence_ID
-> Inspection_Record_ID
-> Action_Record_ID
-> Status_Event_ID  [PROPOSED; NOT ACCEPTED]
```

Do not add `Component_ID` when `Asset_ID + BIM_GUID + Model_Version_ID` is sufficient. A database surrogate key, if used, is a technical implementation key and not part of the research identifier chain.

## Consequences If Accepted

- G2 must baseline the event envelope, legal transitions, current-state reconstruction, authorization and verification/closure guards.
- G3 fixtures must include illegal transition, chronology, unauthorized decision, closure-without-verification and reopen-history cases.
- Current governance and paper files must be synchronized through controlled updates.
- Historical and immutable evidence remains unchanged.

## Decisions Still Required

| Item | Required authority |
|---|---|
| Accept `Status_Event_ID` naming and append-only source-of-history role | Supervisor governance decision |
| Exact Inspection_Record-Action_Record cardinality | Expert review |
| Action lifecycle vocabulary and transitions | Expert review + supervisor acceptance |
| Role/permission matrix and separation of duties | Expert review |
| Verification entity versus Inspection_Record subtype | Expert review + supervisor acceptance |
| Exact verification and closure/reopen criteria | Expert review |
| G1 payload binding fields | Accepted G1 payload |

## Files Affected After Acceptance

`MASTER_RESEARCH_CHARTER_v2.1_TRACEABILITY_CORE_20260719.md`; `SOURCE_OF_TRUTH_HIERARCHY_v2.1.md`; `RQ_WP_CHAPTER_PAPER_GATE_MATRIX_v2.1.md`; `EVIDENCE_GATES_v2.1.md`; `TERMINOLOGY_CONTROL_CURRENT.md`; `CURRENT_DIRECTION_LOCK_20260804.md`; `CURRENT_STATUS_AND_NEXT_DIRECTION.md`; Paper 2 direction; G2 roadmap; G1-G2 interface; CQ/constraint/fixture specifications.

Until acceptance, all exact event/lifecycle/verification/closure choices above remain **GOVERNANCE_DECISION_REQUIRED**.
