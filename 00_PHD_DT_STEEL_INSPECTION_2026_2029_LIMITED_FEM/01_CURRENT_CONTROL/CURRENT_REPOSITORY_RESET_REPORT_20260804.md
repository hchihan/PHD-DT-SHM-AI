# CURRENT REPOSITORY RESET REPORT 20260804

**Date:** 2026-08-04
**Status:** COMPLETED - GOVERNANCE RESET ONLY
**Project:** `00_PHD_DT_STEEL_INSPECTION_2026_2029_LIMITED_FEM`

## 1. Outcome

The repository now has one current execution direction for RQ2/WP2/Chapter 5/Paper 2:

```text
Vibration data
-> condition/state-change evidence
-> BIM-linked component
-> Inspection_Record
-> Action_Record
-> Status_Event
-> inspection-maintenance action support
```

The current identifier chain is:

```text
Sensor_ID
-> BIM_GUID
-> Condition_Evidence_ID
-> Inspection_Record_ID
-> Action_Record_ID
```

Paper 2 is one paper with G2 specification followed by G3 executed validation. G3 remains `NOT OPEN`.

## 2. Locked States

| Item | State |
|---|---|
| G1 | `OPEN / NOT READY` |
| G2 | `OPEN / SPECIFICATION DEVELOPMENT` |
| G3 | `NOT OPEN` |
| Paper 2 | `DESIGN AND EVIDENCE DEVELOPMENT` |

The reset changes governance and organization only. It does not close a gate or approve a scientific claim.

## 3. Baseline And Backup

- The Git repository had no commits before this reset; all project files were initially untracked.
- Exact pre-update Git output is retained in `PRE_UPDATE_GIT_STATUS_20260804.txt`.
- The pre-reset classification contains 342 rows and 184,991,365 bytes, each with SHA-256.
- The pre-reset action manifest records the intended action and destination for every classified file.
- Twelve change-target files were copied to `../90_ARCHIVE/BACKUP_BEFORE_CURRENT_RESET_20260804/`; all 12 source/copy SHA-256 comparisons passed.
- Commit 1 established the managed project baseline because no tracked baseline previously existed.

## 4. Changes Applied

### Governance and navigation

- Rebuilt the source-of-truth hierarchy around a single authority order and gate-evidence order.
- Rebuilt `MASTER_INDEX_CURRENT.md` to list genuinely current files only.
- Updated the root entry point, current status, core evidence pointer, and agent navigation.
- Added `CURRENT_DIRECTION_LOCK_20260804.md`.

### G2-G3 and Paper 2

- Added `../05_GATE2/G2_G3_PAPER2_CURRENT_ROADMAP_v2.1_20260804.md`.
- Added `../03_PAPERS/PAPER_2/PAPER2_CURRENT_DIRECTION_v2.1_20260804.md`.
- Added `G1_G2_INTERFACE_DECISION_REGISTER.csv` with 20 controlled decisions.
- Moved the G1-to-G2 interface to `../05_GATE2/04_SCHEMA_RULES/` and synchronized it with the current roadmap.
- Locked CEI as structured metadata and retained the human-review/accountability boundary.
- Locked Revit, IFC, Dynamo, Pset, IDS, SQLite, viewers, and validation languages as supporting instruments.
- Prohibited Graph 02 execution while G3 is not open.

### Archive and provenance

- Moved nine superseded/dated control and Paper 2 documents byte-for-byte into `../90_ARCHIVE/CURRENT_RESET_20260804/`.
- Verified all nine destination hashes against their pre-reset hashes.
- Recorded physical, already-archived, quarantined, and non-present logical supersessions in `SUPERSEDED_DOCUMENT_REGISTER_20260804.csv`.
- Performed no hard deletion.

## 5. Integrity Results

| Verification | Result |
|---|---|
| Required current paths | 10/10 present |
| Archive moves | 9/9 source absent and destination hash matched |
| Protected evidence/history scheduled to remain | 214/214 SHA-256 matched |
| Pre-reset path coverage | 342/342 resolved |
| Final managed manifest | 367 rows; 366 post-reset hashes matched; self-hash omitted |
| Decision-register parse | 20/20 rows parsed |
| Hard deletions | 0 |
| Gate closures | 0 |

Full details are in `CROSS_FILE_CONSISTENCY_AUDIT_20260804.md` and `CURRENT_REPOSITORY_RESET_MANIFEST_20260804.csv`.

## 6. Git Commits

| Sequence | Commit | Scope |
|---|---|---|
| 1 | `f48e856` | Baseline, backup, classification, and pre-reset manifests |
| 2 | `324c771` | Governance hierarchy and current indexes |
| 3 | `a4943d4` | Unified G2-G3 roadmap, Paper 2 direction, lock, decision register, and interface relocation |
| 4 | `f2d7bc9` | Byte-identical archive moves and superseded register |
| 5 | This final QA commit | Consistency fixes, QA report, reset report, and final manifest |

## 7. Concurrent Untracked Files

The following root PDFs appeared after the pre-reset inventory and were deliberately left untouched and uncommitted:

- `applsci-16-04642.pdf`
- `buildings-15-01312.pdf`
- `buildings-15-02633.pdf`

They require separate classification and are not evidence of this reset.

## 8. Remaining Work

Six interface decisions remain `BLOCKING_OPEN`. G2 cannot be accepted until competency questions, acceptance criteria, minimum schemas, lifecycle rules, and validation fixtures are reviewed. G3 cannot open until an explicit G2 readiness decision exists.

**Next action:** Resolve the blocking decisions and preregister the complete G2 acceptance package. Do not run Graph 02.
