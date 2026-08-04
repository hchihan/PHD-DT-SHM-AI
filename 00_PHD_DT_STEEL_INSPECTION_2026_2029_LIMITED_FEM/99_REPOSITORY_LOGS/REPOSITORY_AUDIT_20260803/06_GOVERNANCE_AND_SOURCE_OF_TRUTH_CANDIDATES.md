# 06 — GOVERNANCE AND SOURCE-OF-TRUTH CANDIDATES

**Audit ID:** REPOSITORY_AUDIT_20260803 · Read-only
**Rule applied:** where more than one file could hold a role, **all candidates are listed and none is selected.** Selection is the user's decision.

---

## Role 1 — Charter (highest academic source of truth)

| Candidate | Path | Size | Modified | Identifying evidence |
|---|---|---:|---|---|
| **C1.1** | `00_GOVERNANCE/MASTER_RESEARCH_CHARTER_v2.1_TRACEABILITY_CORE_20260719.md` | 16.4 KB | 2026-07-19 | `SOURCE_OF_TRUTH_HIERARCHY_v2.1.md` §2 table: **"SOURCE OF TRUTH — Hiện hành cao nhất"**. `V2.1_CORE_EVIDENCE_INDEX.md` header: "Current source of truth". Ranked #2 in the hierarchy (below only the supervisors' 17/07 verdict) |
| **C1.2** | `00_GOVERNANCE/MASTER_RESEARCH_CHARTER_v2_20260719.docx` | 29.3 KB | 2026-07-19 | Hierarchy §2: **"HISTORICAL DECISION SOURCE"** — v2.0 reframe, for context lookup only |
| **C1.3** | `00_GOVERNANCE/MASTER_RESEARCH_CHARTER.md` | 7.2 KB | 2026-07-19 | Hierarchy §2: **"CURRENT NAVIGATION"** — concise entry point that redirects to v2.1 |
| **C1.4** | `90_BACKUP/…/MASTER_RESEARCH_CHARTER_v1.1_LIMITED_FEM_20260717.md` (3 copies) | 11.1 KB | 2026-07-17 | Hierarchy §2: **"SUPERSEDED — ARCHIVED"**. But the hierarchy places it at `99_ARCHIVE_PRE_V2_SYSTEM_20260719/LEGACY_CHARTERS/`, **which does not exist**. It survives only in `90_BACKUP/` |
| **C1.5** | `90_BACKUP/…/92_ARCHIVE_SUPERSEDED_FILES/MASTER_RESEARCH_CHARTER_v1.0_SUPERSEDED_20260717.md` | 8.3 KB | 2026-07-17 | Filename self-declares SUPERSEDED |
| **C1.6** | `90_BACKUP/…/MASTER_RESEARCH_CHARTER.md` (3 copies) | 6.2 KB | 2026-07-17 | Earlier content of C1.3 — differs in bytes, same name |

**Status:** the role is **explicitly assigned** by two governance files that agree with each other. C1.1 is the documented answer.
**Open issue:** the archive path for C1.4 is broken; a reader following the hierarchy's own instruction cannot reach the superseded charter. Three byte-identical copies of C1.4 exist in `90_BACKUP/`. No supersede header check was performed on the file bodies.

---

## Role 2 — Root README / start-here

| Candidate | Path | Size | Modified | Identifying evidence |
|---|---|---:|---|---|
| **C2.1** | `00_README_START_HERE.md` | 3.4 KB | 2026-07-19 | Named by `V2.1_CORE_EVIDENCE_INDEX.md` as the current "Điểm vào / thứ tự đọc", status "CURRENT v2.1". Named by `SOURCE_OF_TRUTH_HIERARCHY_v2.1.md` §1 item 5 |
| **C2.2** | `00_README_START_HERE_v2.1_UPDATED_20260719.md` | 5.9 KB | 2026-07-19 | Filename claims v2.1 + UPDATED. Longer than C2.1, same date. **Not referenced by any other document in the repository** |
| **C2.3** | `00_README_START_HERE_v2.2_UPDATED_20260720.md` | 14.3 KB | 2026-07-20 | **Newest.** Self-declares "Phiên bản vận hành: **v2.2**". Contains a governance note stating Charter v2.1 remains the highest academic source "until the whole governance set is synchronised to v2.2". Announces eight `v0.1` G2 artifacts (none of which exist). **Not referenced by `V2.1_CORE_EVIDENCE_INDEX.md` or by the source-of-truth hierarchy** |
| **C2.4** | `90_BACKUP/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/00_README_START_HERE.md` | 2.1 KB | 2026-07-17 | Backup snapshot of an earlier C2.1 |

**Status:** **UNRESOLVED — POSSIBLE_CONFLICT.** Three READMEs sit in the active root. The index files point at C2.1; the newest and most detailed is C2.3, which declares a *later* operating version than the governance set it sits above. C2.2 is referenced by nothing.
**This is the single most consequential governance ambiguity found.** It is the first file any reader or agent opens.

---

## Role 3 — RQ–WP–Chapter–Paper–Gate matrix

| Candidate | Path | Size | Modified | Identifying evidence |
|---|---|---:|---|---|
| **C3.1** | `00_GOVERNANCE/RQ_WP_CHAPTER_PAPER_GATE_MATRIX_v2.1.md` | 6.4 KB | 2026-07-19 | Hierarchy §1 item 3: part of the "bộ file cấu trúc v2.1 đồng cấp dưới Charter v2.1". `V2.1_CORE_EVIDENCE_INDEX.md`: "CURRENT v2.1" |
| **C3.2** | `04_PHD_SPECIAL_TOPICS/CHUYEN_DE_TONG_QUAN/MATRIX_CHUYEN_DE_RQ_WP_PAPER_GATE_v1.md` | 4.3 KB | 2026-07-18 | Coursework-scoped matrix, `v1`. Duplicated in `90_BACKUP/` |
| **C3.3** | `90_BACKUP/…/92_ARCHIVE_SUPERSEDED_FILES/Updated_RQ_Evidence_Gate_Matrix_SUPERSEDED_20260717.csv` | 2.5 KB | 2026-07-17 | Filename self-declares SUPERSEDED |
| *(missing)* | `RQ_WP_CHAPTER_PAPER_GATE_MATRIX_v1.1.md` | — | — | Listed in `MISSING_CURRENT_FILES_REGISTER_20260718.md` as referenced but never found |

**Status:** C3.1 is unambiguously assigned. C3.2 is a different scope (chuyên đề), not a competitor.

---

## Role 4 — Evidence Gates

| Candidate | Path | Size | Modified | Identifying evidence |
|---|---|---:|---|---|
| **C4.1** | `00_GOVERNANCE/EVIDENCE_GATES_v2.1.md` | 9.8 KB | 2026-07-19 | Hierarchy §1 item 3. `V2.1_CORE_EVIDENCE_INDEX.md`: "CURRENT v2.1 — Bảng execution-gate 7 cột; G1 chi tiết 15 artifact". Open issue recorded in that same index: **"Artifacts G1 chưa tạo/điền"** |
| **C4.2** | `90_BACKUP/…/07_FABLE_LEGACY_PACK_20260718/02_GATE1_EXECUTION_CHECKLIST_20260718.md` | 3.2 KB | 2026-07-18 | Legacy pack, Gate-1 checklist |
| *(missing)* | `EVIDENCE_GATES_v1.1_LIMITED_FEM.md` | — | — | Listed in `MISSING_CURRENT_FILES_REGISTER_20260718.md` |

**Status:** C4.1 assigned. **But** C4.1 names 10+ G1 artifacts (`RUN_REGISTRY_LOCKED.csv`, `DATASET_MANIFEST.csv`, `LORO_PROTOCOL_PREREGISTERED.md`, `G1_ACCEPTANCE_MATRIX.md`, `MODEL_CONFIGURATION_REGISTER.csv`, `RESNET1D_PROVENANCE_AUDIT.md`, `PAPER1_CLAIM_STATUS_TABLE.md`, `SENSOR_METADATA_REGISTER.csv`, `FILE_PROVENANCE_REGISTER.csv`, `RUN_REGISTRY_DATA_DICTIONARY.md`) and a container folder `05_DATA_CODE_AND_EXPERIMENTS/G1_EXECUTION_PACK/` — **none of which exist.** The gate definition is live; the gate's artifact set is empty.

---

## Role 5 — Living Evidence Base

| Candidate | Path | Size | Modified | Identifying evidence |
|---|---|---:|---|---|
| **C5.0** | `02_EVIDENCE_BASE/CURRENT/LIVING_EVIDENCE_BASE_CURRENT.md` | 0.8 KB | 2026-07-19 | **Pointer file.** States: current source of truth = C5.1; C5.2/C5.3 are historical, not current. Explicitly resolves the ambiguity |
| **C5.1** | `02_EVIDENCE_BASE/CURRENT/LIVING_EVIDENCE_BASE_v2.1_TRACEABILITY_CORE.md` | 29.3 KB | 2026-07-19 | Named CURRENT by C5.0; consolidates v1.1 + v1.2 into groups A–J with a 13-field schema |
| **C5.2** | `02_EVIDENCE_BASE/CURRENT/01_LIVING_EVIDENCE_BASE_v1.2_LIMITED_FEM_20260718.md` | 8.5 KB | 2026-07-18 | Historical — 19 new deep reads. Duplicated 3× in `90_BACKUP/` |
| **C5.3** | `02_EVIDENCE_BASE/CURRENT/LIVING_EVIDENCE_BASE_v1.1_LIMITED_FEM.md` | 9.9 KB | 2026-07-17 | Historical — 33 canonical records. Duplicated 3× in `90_BACKUP/`. **Uses the superseded identifier chain** ending in `Action_Status`, with `FEM_Node_ID = optional metadata only` |
| *(supporting)* | `02_EVIDENCE_BASE/CURRENT/EVIDENCE_MIGRATION_REPORT_v2.1.md` | 2.7 KB | 2026-07-19 | Documents the v1.1/v1.2 → v2.1 migration |

**Status:** **RESOLVED by design.** This is the one document family in the repository with an explicit, in-folder pointer file. It is a good model for the others. Listed here only because three versioned files sit in a folder literally named `CURRENT`.

---

## Role 6 — Current status

| Candidate | Path | Size | Modified | Identifying evidence |
|---|---|---:|---|---|
| **C6.1** | `01_CURRENT_CONTROL/CURRENT_STATUS_AND_NEXT_DIRECTION.md` | 4.1 KB | 2026-07-19 | Hierarchy §1 item 6. `V2.1_CORE_EVIDENCE_INDEX.md`: "CURRENT v2.1 — Current gate G1" |
| **C6.2** | `90_BACKUP/…/CURRENT_STATUS_AND_NEXT_DIRECTION.md` (3 copies) | 3.4 KB | 2026-07-17 | Earlier content, same name |
| **C6.3** | `90_BACKUP/…/07_FABLE_LEGACY_PACK_20260718/01_PROJECT_STATE_SNAPSHOT_20260718.md` | 5.6 KB | 2026-07-18 | Parallel state snapshot from the legacy pack |

**Status:** C6.1 assigned.
**Content issue for review:** C6.1 §4 states *"LORO chưa chạy … run registry chưa khóa"* (LORO not run, run registry not locked), while `05_DATA_CODE_AND_EXPERIMENTS/THREE_CAMPAIGN_REANALYSIS/` (modified 2026-07-29, ten days later) reports a completed LORO matrix. C6.1 may be stale.

---

## Role 7 — Unresolved-items tracker

| Candidate | Path | Size | Modified | Identifying evidence |
|---|---|---:|---|---|
| **C7.1** | `01_CURRENT_CONTROL/UNRESOLVED_ITEMS_TRACKER_v2.1.md` | 4.5 KB | 2026-07-19 | Self-declares: "Kế thừa `UNRESOLVED_ITEMS_CURRENT.md` (v1.1); file này là bản hiện hành v2.1". 19 open items in 3 groups |
| **C7.2** | `90_BACKUP/…/07_FABLE_LEGACY_PACK_20260718/04_UNRESOLVED_ITEMS_TRACKER_20260718.md` | 3.3 KB | 2026-07-18 | Legacy pack version |
| **C7.3** | `90_BACKUP/…/UNRESOLVED_ITEMS_AFTER_LIMITED_FEM_MIGRATION.md` | 2.8 KB | 2026-07-17 | Migration-era tracker |
| *(missing)* | `UNRESOLVED_ITEMS_CURRENT.md` | — | — | Referenced by C7.1, by C6.1 §4, and by `SOURCE_OF_TRUTH_HIERARCHY_v2.1.md` §1 item 6 — **does not exist anywhere.** The hierarchy lists it as a current-tier file |

**Status:** C7.1 assigned, but the hierarchy simultaneously names a non-existent file at the same tier.

---

## Role 8 — Master index

| Candidate | Path | Size | Modified | Identifying evidence |
|---|---|---:|---|---|
| **C8.1** | `01_CURRENT_CONTROL/PROJECT_CLEANUP_20260718/MASTER_INDEX_CURRENT.md` | 8.2 KB | 2026-07-19 | Hierarchy §1 item 5 and `V2.1_CORE_EVIDENCE_INDEX.md`: "Master index điều hướng — CURRENT v2.1". **Stored inside a dated cleanup subfolder**, which is an odd location for a current navigation file |
| **C8.2** | `90_BACKUP/…/01_CURRENT_CONTROL/PROJECT_CLEANUP_20260718/MASTER_INDEX_CURRENT.md` | 5.5 KB | 2026-07-18 | Earlier content of C8.1 |
| **C8.3** | `90_BACKUP/…/MASTER_INDEX_CURRENT_v1.1.md` (2 copies) | 4.9 KB | 2026-07-17 | v1.1 lineage; **no active-location twin** |
| **C8.4** | `90_BACKUP/…/Literature_Review_Master_Index_Current.md` (2 copies) | 23.1 KB | 2026-07-07 | Largest index in the repository; literature-scoped; **no active-location twin** |

**Status:** C8.1 assigned by governance, but its location inside `PROJECT_CLEANUP_20260718/` conflicts with its stated current-navigation role. C8.4 (23 KB) has no active counterpart and may contain literature-index content not carried forward.

---

## Role 9 — ADR (architecture decision records)

| Candidate | Path | Size | Modified | Identifying evidence |
|---|---|---:|---|---|
| **C9.1** | `00_GOVERNANCE/RESEARCH_ARCHITECTURE_DECISION_RECORD_20260719.md` | 2.5 KB | 2026-07-19 | Hierarchy §1 item 3; index: "CURRENT v2.1 — Traceability-core" |
| **C9.2** | `00_GOVERNANCE/RESEARCH_ARCHITECTURE_DECISION_RECORD_ACTION_ID_20260719.md` | 2.9 KB | 2026-07-19 | Hierarchy §1 item 3; index: "CURRENT v2.1 — data-model Action_Record_ID" |
| **C9.3** | `90_BACKUP/…/RESEARCH_ARCHITECTURE_DECISION_RECORD_20260717.md` (3 copies) | 5.7 KB | 2026-07-17 | Hierarchy §1 item 9: SUPERSEDED, said to be archived at `99_ARCHIVE_PRE_V2_SYSTEM_20260719/LEGACY_CHARTERS/` — **that folder does not exist**; the file survives only in `90_BACKUP/` |

**Status:** C9.1 + C9.2 are co-current by design (two ADRs, different subjects). C9.3's stated archive location is broken. Note that C9.3 (5.7 KB) is larger than C9.1 and C9.2 combined.

---

## Role 10 — Agent rules / CLAUDE.md

| Candidate | Path | Size | Modified | Identifying evidence |
|---|---|---:|---|---|
| **C10.1** | `00_GOVERNANCE/AGENT_RULES.md` | 4.0 KB | 2026-07-19 | Hierarchy §1 item 3; index: "CURRENT v2.1". Tracker item #12: this file "tuyên bố thay vai trò" of older agent rules elsewhere |
| **C10.2** | `00_GOVERNANCE/CLAUDE.md` | 4.5 KB | 2026-07-19 | Named in `00_README_START_HERE.md` reading order item 5 |
| **C10.3** | `90_BACKUP/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/CLAUDE.md` | 3.8 KB | 2026-07-17 | Earlier content; **no active-location twin** |
| **C10.4** | `Skill.md` (repository root) | 6.5 KB | 2026-07-28 | **Newest governance-adjacent file in the repository.** Defines the PhD prompt-architect skill, including a fixed scope statement and mode→RQ/WP/Gate map. **Carries the superseded identifier chain** `… → Inspection_Record_ID → Action_Status` and `FEM_Node_ID chỉ là metadata tùy chọn` |
| **C10.5** | `.claude/settings.local.json` | 0.7 KB | 2026-08-03 | Tool-permission settings, not research governance |
| *(missing)* | `RESEARCH_CHARTER.md`, `04_AI_SYSTEM/AGENTS/RESEARCH_CHARTER.md`, `00_SYSTEM/MASTER_CHARTER.md` | — | — | Referenced by C10.1 and by `SYSTEM_GUIDANCE_AUDIT_v2.1_20260719.md`; outside this repository root |

**Status:** **POSSIBLE_CONFLICT.** C10.4 (`Skill.md`) is dated nine days after the v2.1 governance set and eight days after README v2.2, yet encodes the **pre-v2.1** identifier chain that Charter v2.1 and README v2.2 both replaced with `Action_Record_ID`. It has no version suffix and no supersede header. Because its function is to generate prompts for other models, a stale chain here propagates into downstream work.

---

## Role 11 — Terminology control

| Candidate | Path | Size | Modified |
|---|---|---:|---|
| **C11.1** | `00_GOVERNANCE/TERMINOLOGY_CONTROL_CURRENT.md` | 5.9 KB | 2026-07-19 |
| **C11.2** | `90_BACKUP/…/TERMINOLOGY_CONTROL_v1.1.md` (2 copies) | 3.3 KB | 2026-07-17 |

**Status:** C11.1 assigned (index: "CURRENT (v1.1 lineage + §5 v2.1)"). No conflict.

---

## Role 12 — Decision authority

| Candidate | Path | Size | Modified | Identifying evidence |
|---|---|---:|---|---|
| **C12.1** | `00_GOVERNANCE/THE_COUNCIL_REVIEW_FEM_OR_NO_FEM_17.07.2026.md` | 35.2 KB | 2026-07-17 | **Ranked #1 in `SOURCE_OF_TRUTH_HIERARCHY_v2.1.md`** — above the Charter. Records Verdict B and the supervisors' decision of 17/07/2026. Largest governance file in the repository |
| **C12.2** | `90_BACKUP/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/THE_COUNCIL_REVIEW_FEM_OR_NO_FEM_17.07.2026.md` | 35.2 KB | 2026-07-17 | Byte-identical copy |

**Status:** assigned and unambiguous. Note for report 07: this file necessarily discusses calibrated FEM, EMA, MAC, similitude, and `FEM_Node_ID` at length — that is its subject matter, not a legacy-direction leak. It also records the chain as ending in `Action_Status`, consistent with its 17/07 date and predating the `Action_Record_ID` ADR of 19/07.

> **Date convention in this report.** `Modified` is the file's own last-write time, i.e. when its content was authored. Files inside `90_BACKUP/` were *copied* on 2026-07-18 (creation time) but retain 2026-07-07/17 write times from when they were written. Both timestamps are in `01_FULL_REPOSITORY_INVENTORY.csv`.

---

## Summary table

| Role | Candidates | Assigned by governance? | Verdict for this audit |
|---|---:|---|---|
| Charter | 6 | Yes — C1.1 | **NO_ISSUE** (broken archive path noted) |
| Root README | 4 | Partially — index says C2.1, newest is C2.3 | **POSSIBLE_CONFLICT** |
| RQ/WP/Paper/Gate matrix | 3 | Yes — C3.1 | **NO_ISSUE** |
| Evidence Gates | 2 | Yes — C4.1 | **NO_ISSUE** (all named G1 artifacts absent) |
| Living Evidence Base | 4 + pointer | Yes — C5.1 via explicit pointer | **NO_ISSUE** (model practice) |
| Current status | 3 | Yes — C6.1 | **POSSIBLE_SUPERSEDED** (LORO statement may be stale) |
| Unresolved-items tracker | 3 | Yes — C7.1 | **NO_ISSUE** (hierarchy also names a missing file) |
| Master index | 4 | Yes — C8.1 | **UNKNOWN** (location conflicts with role; C8.4 has no active twin) |
| ADR | 3 | Yes — C9.1 + C9.2 | **NO_ISSUE** (broken archive path noted) |
| Agent rules / skill | 5 | Partially | **POSSIBLE_CONFLICT** (`Skill.md`) |
| Terminology control | 2 | Yes — C11.1 | **NO_ISSUE** |
| Decision authority | 2 | Yes — C12.1 | **NO_ISSUE** |

**Two roles carry an unresolved conflict (Root README, Agent rules/skill); one is unknown (Master index); one may be stale (Current status). Eight are cleanly assigned.**

---

## Structural observation

The governance layer of this repository is **unusually well specified in content and unusually broken in navigation.** `SOURCE_OF_TRUTH_HIERARCHY_v2.1.md` does exactly what a source-of-truth document should — it states a single total order, names the winner per role, and forbids multiple files claiming the same role. Its weakness is that four of the paths it routes to do not exist:

| Target named as current or archival | Exists? |
|---|---|
| `99_ARCHIVE_PRE_V2_SYSTEM_20260719/` (+ `LEGACY_CHARTERS/`, `LEGACY_NAVIGATION/`) | **No** |
| `92_ARCHIVE_MINIMAL/` | **No** |
| `ARCHIVE_MANIFEST.md` | **No** |
| `UNRESOLVED_ITEMS_CURRENT.md` | **No** |

Consequently the files the hierarchy declares "SUPERSEDED — ARCHIVED" (v1.1 charter, pre-v2 ADR) are physically located in `90_BACKUP/` — a tree the same document declares "không bao giờ là source of truth" (never a source of truth). The archive tier described in governance was either never created, was created outside this repository root, or was removed by the 2026-07-18 cleanup without updating the hierarchy.

---

## Claim → Evidence → Limitation → Next action

**Claim.** Twelve governance roles were identified with 41 candidate files between them. Eight roles are cleanly and consistently assigned by two mutually agreeing governance documents. Two roles carry an active conflict — the root README (v2.1 vs v2.2) and the agent-rules/skill layer (`Skill.md` encoding a superseded identifier chain). One is unknown (master index). One may be stale (current status). Separately, the source-of-truth hierarchy routes to four targets that do not exist.

**Evidence.** Direct reading of `SOURCE_OF_TRUTH_HIERARCHY_v2.1.md`, `V2.1_CORE_EVIDENCE_INDEX.md`, `00_README_START_HERE.md`, `00_README_START_HERE_v2.2_UPDATED_20260720.md`, `CURRENT_STATUS_AND_NEXT_DIRECTION.md`, `UNRESOLVED_ITEMS_TRACKER_v2.1.md`, `MISSING_CURRENT_FILES_REGISTER_20260718.md`, `LIVING_EVIDENCE_BASE_CURRENT.md`, and `Skill.md`; filename, size, modified-time, and SHA-256 comparison across all 301 files; existence check of every backtick-quoted path in active markdown.

**Limitation.** Candidate identification rests on filename, location, and the explicit role statements in the two index documents. **File bodies were read for 15 governance files; the remaining candidates — including `MASTER_RESEARCH_CHARTER_v2_20260719.docx` (the v2.0 charter) — were not read.** No supersede-header verification was performed on backup-tree files. `Evidence is currently insufficient` to determine whether `99_ARCHIVE_PRE_V2_SYSTEM_20260719/` and `92_ARCHIVE_MINIMAL/` were never created, were created outside this root, or were deleted. **No canonical file has been selected for any conflicting role.**

**Next action.** The user decides, in this order: (1) which root README is current and what happens to the other two; (2) whether `Skill.md` is superseded, should be updated to `Action_Record_ID`, or is deliberately scoped to the older chain; (3) whether the archive tier should be created inside this repository or the hierarchy corrected to point at `90_BACKUP/`; (4) whether `MASTER_INDEX_CURRENT.md` belongs in `01_CURRENT_CONTROL/` root rather than inside `PROJECT_CLEANUP_20260718/`; (5) whether `CURRENT_STATUS_AND_NEXT_DIRECTION.md` §4 needs updating against the 2026-07-29 reanalysis outputs.
