# REPOSITORY BASELINE — RETROSPECTIVE APPROVAL RECORD

**Version:** v1.0
**Date / Updated:** 2026-08-04
**Status:** `ACCEPTED AS WORKING REPOSITORY BASELINE — RETROSPECTIVE GOVERNANCE APPROVAL`
**Source-of-truth level:** 7 (governance/change provenance)
**Approving authority:** PhD candidate (repository owner), acting on a post-execution independent audit.
**Supervisor approval:** **NOT PRESENT.** No supervisor review or sign-off evidence exists for either operation or for this record.
**Supersedes:** None.
**Superseded by:** None.
**Change summary:** Records retrospective acceptance of the 2026-08-04 repository state as the working baseline, the absence of a prior approval record, and the binding pre-approval requirement for all future repository-wide operations.

---

## 1. Operations Executed On 2026-08-04

Two separate repository operations were executed on 2026-08-04:

| # | Operation | Scope | Change control produced |
|---|---|---|---|
| 1 | **CURRENT_CONTROL reset** | Governance hierarchy and navigation rebuilt; 9 documents archived to `90_ARCHIVE/CURRENT_RESET_20260804/`; 5 Git commits created | `CURRENT_REPOSITORY_RESET_REPORT_20260804.md`, `CROSS_FILE_CONSISTENCY_AUDIT_20260804.md` (both since archived) |
| 2 | **Evidence Base consolidation** | 30 files modified, 6 created, 6 archived to `02_EVIDENCE_BASE/90_ARCHIVE_SUPERSEDED/20260804/`; **no Git commit created** | `02_EVIDENCE_BASE/CURRENT/REPOSITORY_UPDATE_REPORT_20260804.md`, `03_REPOSITORY_UPDATE_CHANGELOG_20260804.md`, `ARCHIVE_MANIFEST_20260804.csv` |

Operation 2 superseded and archived Operation 1's two reports, because Operation 1's path and status wording ceased to describe the worktree after Operation 2 relocated key G2 files into the Evidence Base.

The authoritative account of the current worktree is:

```text
02_EVIDENCE_BASE/CURRENT/REPOSITORY_UPDATE_REPORT_20260804.md
```

## 2. Approval Sequence — As It Actually Occurred

**Both operations were executed before any documented prior approval record was created.** No written update plan was approved in advance of execution, and no approval artifact exists in the repository predating either operation.

A post-execution independent audit was performed afterwards, on 2026-08-04, and is recorded in `../CLAUDE_COWORK_PHD_PROJECT_SETUP_20260804/08_AUDIT_AND_UPDATE_PLAN_20260804.md` (marked `SUPERSEDED — FACTUAL FINDINGS D.1 RETRACTED`; read its correction notice before use).

This record is therefore **retrospective**. It does not claim that prior approval existed.

## 3. Post-Execution Review Findings

| # | Finding |
|---|---|
| 1 | The scientific direction is consistent across the Charter, source-of-truth hierarchy, gates, current-direction lock, status, roadmap and Paper 2 direction. |
| 2 | Gate statuses remain conservative and are stated identically wherever they appear. |
| 3 | **No Gate is marked PASS.** G1 `OPEN — PARTIAL EVIDENCE`; G2 `OPEN — LITERATURE BOUNDARY CLOSED, SPECIFICATION NOT YET FROZEN`; G3 `OPEN — NOT IMPLEMENTED, NOT VALIDATED, NOT OFFICIALLY PASSED`, execution `NOT OPEN`; G4/G5 `OPEN`. |
| 4 | Archived records preserve historical provenance. Superseded documents were moved byte-identical with SHA-256 recorded in `SUPERSEDED_DOCUMENT_REGISTER_20260804.csv` and `ARCHIVE_MANIFEST_20260804.csv`. No hard deletion was performed. |
| 5 | The two reporting errors initially suspected by the audit — a decision-register row-count discrepancy and a reference to a `05_GATE2/` path — **were retracted** after Operation 2 was discovered. The register grew from `D001-D020` to `D001-D026` during Operation 2, and the `05_GATE2/` layout existed at the time Operation 1 reported it. Both archived reports were accurate as at their own execution time. |
| 6 | **No outstanding factual reporting error is currently established** in the current governance or change-control set. |

## 4. Acceptance

The current repository state is **retrospectively accepted as the working baseline from 2026-08-04**.

## 5. Explicit Limits Of This Acceptance

This acceptance does **not**:

- pass G1, G2 or G3, or alter any Gate status;
- accept `00_GOVERNANCE/ADR_ACTION_STATUS_EVENT_20260804_DRAFT.md` as an approved ADR — it remains `PROPOSED — NOT YET ACCEPTED`;
- authorize G3 implementation, any bounded prototype, or execution of Graph 02;
- change, revalidate or reinterpret any immutable evidence, including the Round 1–3B deep-read reports and `EVIDENCE_MIGRATION_REPORT_v2.1.md`;
- approve any scientific claim beyond the current evidence boundary;
- constitute supervisor approval, expert review, or resolution of any item marked `BLOCKING_OPEN`, `EXPERT_REVIEW_REQUIRED`, `FREEZE_PROVISIONALLY` or `WAIT_FOR_G1_PAYLOAD` in `G1_G2_INTERFACE_DECISION_REGISTER.csv`.

Acceptance is administrative and governance-level only. It fixes a baseline for further work; it does not advance the evidence position.

## 6. Binding Requirement For Future Operations

Every future repository-wide reset, archive move, Git commit or push requires, **in this order**:

1. a **written update plan** identifying target files, action, reason, governing authority and risk;
2. **explicit approval before execution**, recorded in `01_CURRENT_CONTROL/` before any file is changed;
3. a **post-execution changelog and verification report**, including hashes for every moved file and an explicit statement of what did and did not change.

An operation executed without step 2 is a governance exception and must be recorded as such, as this record does.

## 7. Residual Governance Items

| Item | Status |
|---|---|
| Supervisor review of the 2026-08-04 baseline | Not obtained |
| `ADR_ACTION_STATUS_EVENT_20260804_DRAFT` acceptance | Pending supervisor decision |
| 6 `BLOCKING_OPEN` interface decisions (D004, D005, D007, D013, D014, D016) | Unresolved; block G2 readiness |
| `LIVING_EVIDENCE_BASE_v2.2` successor | Not yet created; deliberately deferred |
| Round 3B external hash drift during Operation 2 QC | Recorded as a residual provenance limitation in `REPOSITORY_UPDATE_REPORT_20260804.md` §5 |
| Three unclassified root PDFs (`applsci-16-04642`, `buildings-15-01312`, `buildings-15-02633`) | Outside the managed baseline; require separate classification |
