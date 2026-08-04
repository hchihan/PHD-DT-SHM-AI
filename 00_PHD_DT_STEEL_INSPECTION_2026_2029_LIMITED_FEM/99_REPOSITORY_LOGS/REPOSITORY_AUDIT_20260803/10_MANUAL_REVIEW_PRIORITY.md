# 10 — MANUAL REVIEW PRIORITY

**Audit ID:** REPOSITORY_AUDIT_20260803 · Read-only

Reading order for the human review pass. Priority reflects **how much downstream work is blocked**, not folder size. Nothing below is a move or delete instruction.

---

## PRIORITY 1 — Governance / source of truth

**Why first:** every other decision inherits from this. Until it is known which README, which charter, and which identifier chain govern, any judgement about whether a paper draft or evidence file is "current" is unanchored. This is also the smallest tier — 6 files, ~50 KB, perhaps one hour of reading.

| Order | File | Question to answer |
|---|---|---|
| 1.1 | `00_README_START_HERE.md`, `00_README_START_HERE_v2.1_UPDATED_20260719.md`, `00_README_START_HERE_v2.2_UPDATED_20260720.md` | **Which is current?** The v2.1 index names the first; the third is newest, declares operating version v2.2, and is cited as a priority source by `NOTEBOOKLM_BRIEF_…` (27/07). The second is referenced by nothing |
| 1.2 | `Skill.md` (root) | **Is the `Action_Status` chain deliberate or stale?** Modified 28/07, nine days after the `Action_Record_ID` ADR. It generates prompts for other models, so the answer propagates |
| 1.3 | `00_GOVERNANCE/SOURCE_OF_TRUTH_HIERARCHY_v2.1.md` | **Where is the archive tier?** It routes to `99_ARCHIVE_PRE_V2_SYSTEM_20260719/`, `92_ARCHIVE_MINIMAL/`, `ARCHIVE_MANIFEST.md`, and `UNRESOLVED_ITEMS_CURRENT.md` — none exist. Were they never created, created elsewhere, or removed by the 2026-07-18 cleanup? |
| 1.4 | `01_CURRENT_CONTROL/CURRENT_STATUS_AND_NEXT_DIRECTION.md` §4 | **Is the LORO statement stale?** It says "LORO chưa chạy" (19/07); `THREE_CAMPAIGN_REANALYSIS/` contains a completed LORO matrix (files modified 29/07) |
| 1.5 | `00_GOVERNANCE/EVIDENCE_GATES_v2.1.md` | **Do the 10+ named G1 artifacts and `G1_EXECUTION_PACK/` exist anywhere?** The gate definition is live; its artifact set is empty |
| 1.6 | `01_CURRENT_CONTROL/PROJECT_CLEANUP_20260718/MASTER_INDEX_CURRENT.md` | **Should the current master index live inside a dated cleanup subfolder?** Also: reconcile against `90_BACKUP/…/Literature_Review_Master_Index_Current.md` (23 KB, no active twin) |

**Deliverable of this tier:** a single decision record naming the canonical file for each of the 12 governance roles in `06_GOVERNANCE_AND_SOURCE_OF_TRUTH_CANDIDATES.md`.

---

## PRIORITY 2 — Raw data / run registry / code

**Why second:** Gate 1 is the current gate, and blocking tracker items #1–#3 all depend on artifacts this audit could not find. This tier is not a reading task — it is a **location task**. Until it is answered, no G1 result in the repository can be verified or regenerated.

| Order | Target | Question to answer |
|---|---|---|
| 2.1 | `Campaign1_25.04.2026/`, `Campaign2_22.07.2026/`, `Campaign3_29.07.2026/` (216 CSVs) | **Where are they?** Not under this repository root. Sibling folders `01_KNOWLEDGE/`, `02_PROJECTS/`, `03_RESEARCH_ASSETS/` were not scanned |
| 2.2 | `CANONICAL_THREE_CAMPAIGN_DATASET.zip` | **Was it retained?** `00_README.md` says it holds all 216 NPZ layers, 3 analysis sets, fold manifests, window generator, automated tests, and all 12 pipeline scripts, and was "delivered via the chat file cards" |
| 2.3 | `RUN_REGISTRY_LOCKED.csv` | **Does it exist?** Cited by 6 active documents including `EVIDENCE_GATES_v2.1.md`. This is blocking tracker item #1 |
| 2.4 | `02_MASTER_RUN_REGISTRY.csv` / `06_MASTER_RUN_REGISTRY.csv` | Two differently-numbered registries named by the two G1 packages. **Same file, or two generations?** |
| 2.5 | The 20 pipeline scripts | SHA-256 published for all of them in `01_ENVIRONMENT_PROVENANCE.md` and `10_REPRODUCIBILITY_MANIFEST.md`. **Do the files matching those hashes still exist?** |
| 2.6 | `05_DATA_CODE_AND_EXPERIMENTS/CANONICAL_THREE_CAMPAIGN_DATASET/` vs `THREE_CAMPAIGN_REANALYSIS/` | **What is the intended relationship?** Neither folder says. The canonical package's fingerprint-based sensor correction appears to answer the reanalysis package's #1 open item |
| 2.7 | `05_DATA_CODE_AND_EXPERIMENTS/Checklist_Campaign_3_Gate1.docx` (37 KB) | Not read in this audit. May hold campaign metadata not recorded elsewhere |
| 2.8 | `BAO_CAO_RESNET1D.docx` | Cited 3× by Paper 1 documents; not in repository. Blocking tracker item #2 (ResNet1D sensor mode) depends on it |

**Deliverable of this tier:** a location register stating, for each missing G1 artifact, whether it exists elsewhere, is recoverable, or is gone.

---

## PRIORITY 3 — G2 / G3 evidence and demo

**Why third:** Gate 2 is the next gate, and it is currently pre-artifact. Nothing here blocks Gate 1, but the eight `v0.1` artifacts announced by README v2.2 are the declared G2 work package and none exists.

| Order | Target | Question to answer |
|---|---|---|
| 3.1 | The eight `v0.1` schema/CQ artifacts named by README v2.2 | **Were they ever created?** `CONTEXT_MAPPING_RULES`, `RQ2_ENTITY_RELATIONSHIP_MODEL`, `IDENTIFIER_AND_SENSOR_ASSIGNMENT_SCHEMA`, `CEI_METADATA_DICTIONARY`, `INSPECTION_RECORD_SCHEMA`, `ACTION_RECORD_ACCOUNTABILITY_SCHEMA`, `G2_COMPETENCY_QUESTION_REGISTER`, `G2_ACCEPTANCE_CRITERIA`. Their existence or absence determines whether README v2.2 describes reality or intent |
| 3.2 | `03_PAPERS/PAPER_2/PAPER2_DIRECTION_AND_GATE_v2.1_20260719.md` | The only file in `PAPER_2/`. Read against the eight artifacts above and tracker items #4, #5, #15, #16 |
| 3.3 | `02_EVIDENCE_BASE/RQ2_GATES2_3/` (12 files) + `DEEP_READ_20.07.2026/` (5 PDFs) | Confirm the deep-read set is complete. Tracker item #13: three RQ2 full texts still missing (`3II2WKLN`, `NUTL57KJ`, `Z4IBWW9Y`) |
| 3.4 | `YEU_CAU_CAP_NHAT_WEBSITE_BIM_VIEWER_DIGITAL_TWIN_DEMO_20260727.md` | The only demo-related artifact. **Was the IT request acted on?** No response, status note, or deliverable is present |
| 3.5 | `02_EVIDENCE_BASE/ZOTERO_AUDIT/10_ZOTERO_WRITEBACK_QUEUE_20260718.md` | Tracker item #14: **Zotero must not be modified until approved.** Read the queue before any Zotero session |
| 3.6 | `02_EVIDENCE_BASE/02.08.2026 Q2-Q3/` | Empty, created 2026-08-02. **What was it opened for?** |

---

## PRIORITY 4 — Papers / thesis / special topics

**Why fourth:** these are outputs of the tiers above. Reviewing a Paper 1 draft before knowing which results are valid, or a chuyên đề before knowing which charter governs, wastes the pass. This tier has the highest version-token density in the repository (21 of 23 files in `PAPER_1/`).

| Order | Target | Question to answer |
|---|---|---|
| 4.1 | `03_PAPERS/PAPER_1/` (23 files) | **Which outline is current?** `PAPER1_OUTLINE_20260719.md` (37 KB), `PAPER1_Q2_INTEGRATED_OUTLINE_WITH_PRELIMINARY_RESULTS_v4_20260719.md` (48 KB), `PAPER1_JOURNAL_OUTLINE_EMPTY_RESULTS_SOURCE_v2_20260719.md` (7 KB) — all dated 19/07. Plus three `.docx` outlines `v3`/`v4`/`v6` in `ARCHIVE_MINIMAL/OUTLINE_VERSION_REVIEW/`, and `Paper 1_Old_version (10.06).docx` |
| 4.2 | The three Vietnamese experiment protocols in `03_PAPERS/PAPER_1/` | `KICH_BAN_THI_NGHIEM_PAPER1_VA_TIEN_KIEM_CHUNG_CAM_BIEN_CO_DAY_20260721.docx` (53 KB), `KICH_BAN_THI_NGHIEM_RUT_GON_20260721.docx` (43 KB), `Kich_ban_thi_nghiem_21.07.2026.docx` (20 KB). **All three dated 21/07, three sizes, no current marker.** Not read in this audit |
| 4.3 | `03_PAPERS/Yêu cầu phân tích PASCO–ADXL cho Paper S1.docx` | Loose at `03_PAPERS/` root. **What is "Paper S1"?** No folder exists for it. Only PASCO/ADXL-specific document in the repository |
| 4.4 | `03_PAPERS/PAPER_3/PAPER3_FIELD_FEASIBILITY_DIRECTION_v2.1_20260719.md` | Read together with tracker item #7 (field access unsigned) and item #8 (minimum field protocol undefined) |
| 4.5 | `04_PHD_SPECIAL_TOPICS/CHUYEN_DE_TONG_QUAN/` (4 files) | Dated 18/07, so predates the `Action_Record_ID` ADR. Tracker item #18 already says **do not revise now**. Confirm that still holds |
| 4.6 | `NOTEBOOKLM_BRIEF_G1_PAPER1_VS_AVCI_2021.md` (28 KB, root) | Current, well-scoped. References `CAMPAIGN_AND_SENSOR_PAIR_REPORT.md`, which is not in the repository |

---

## PRIORITY 5 — Prompts / backups / external projects

**Why last:** none of it blocks research progress, and `90_BACKUP/` must not be touched until Priorities 1–2 have established what is unique in it.

| Order | Target | Question to answer |
|---|---|---|
| 5.1 | The 63 files in `90_BACKUP/` with **no active-location twin** (41 distinct filenames) | **Which are worth preserving as history?** Includes the only copies of `MASTER_RESEARCH_CHARTER_v1.0_SUPERSEDED`, `MASTER_RESEARCH_CHARTER_v1.1_LIMITED_FEM`, `RESEARCH_ARCHITECTURE_DECISION_RECORD_20260717`, `Literature_Review_Master_Index_Current.md`, `MASTER_INDEX_CURRENT_v1.1.md`, `TERMINOLOGY_CONTROL_v1.1.md`, the 5-file Fable legacy pack, the 2026-07-18 cleanup provenance manifests, and the repository's **only three `.py` files** |
| 5.2 | Triple nesting inside `90_BACKUP/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/` | The same evidence pack exists three times (`BACKUP_BEFORE_WRITEBACK_20260718/`, `Zotero MCP/`, plus the top-level `90_BACKUP/BACKUP_BEFORE_WRITEBACK_20260718/`). ~38 MiB of the repository is redundant |
| 5.3 | The four-location prompt-tooling cluster | `Skill.md`, `PROMPT_CONTROL_CENTER_PROJECT_INSTRUCTIONS.md`, `PROMPT_CONTROL_CENTER_PROJECT/`, `07_PROMPTS_AND_HANDOFFS/phd-prompt-{router,compressor}/`. **Which is authoritative?** Three hold separate copies of the PhD scope statement |
| 5.4 | `06_LITERATURE_AND_ZOTERO/PERPLEXITY_PRO/` (25 files, 24 duplicated in backup) | Governance tier 8 — not citable as evidence. Confirm whether the active copy or the backup copy is intended to be kept |
| 5.5 | `BIM-AEC-CLAUDE.jpg`, `New folder` | Unexplained. Lowest consequence |
| 5.6 | `03_PAPERS/PAPER_1/ARCHIVE_MINIMAL/` | Local archive folder. Governance names a repository-level `92_ARCHIVE_MINIMAL/` that does not exist — **are these related?** |

---

## Effort estimate

| Tier | Files to read | Approx. size | Nature of work |
|---|---:|---:|---|
| P1 | 6 | ~50 KB | Reading + decision |
| P2 | 8 | mostly external | **Locating**, not reading |
| P3 | ~20 | ~80 KB | Reading + existence check |
| P4 | ~30 (incl. 6 `.docx`) | ~800 KB | Reading + version resolution |
| P5 | ~70 | ~34 MiB | Comparison + retention decision |

P1 and P2 together are a few hours and unblock everything else. P5 is the largest by volume and the least urgent.

---

## Claim → Evidence → Limitation → Next action

**Claim.** The review work divides into five tiers with a strict dependency order. Priorities 1 and 2 — six governance files and eight missing-artifact locations — block essentially all other judgements about what in this repository is current, valid, or reproducible. Priority 5 is the largest by volume (34 MiB, ~70 files) and the least urgent, but must not be actioned before Priority 1–2 establish what is unique inside `90_BACKUP/`.

**Evidence.** Dependency ordering derives from the blocking structure recorded in `UNRESOLVED_ITEMS_TRACKER_v2.1.md` (items #1–#8 blocking, #9–#14 inherited, #15–#19 phase-2); the role assignments and conflicts in `06_GOVERNANCE_AND_SOURCE_OF_TRUTH_CANDIDATES.md`; the 119 dangling references in `07_LEGACY_DIRECTION_SCAN.md` §4; and the 63 unique-content backup files identified by SHA-256 comparison.

**Limitation.** Priorities are the auditor's judgement based on stated blocking relationships, not on the user's own schedule, supervisor deadlines, or the July 2026 chuyên đề tổng quan milestone referenced in `CURRENT_STATUS_AND_NEXT_DIRECTION.md` §5.1. The effort estimates are rough and assume the `.docx` files are of ordinary length. **This report assigns no action beyond reading.**

**Next action.** Begin with P1.1 (which README) and P1.2 (`Skill.md`), then move straight to P2.1–P2.3 (locate the campaign data, the zip, and the run registry). Those five answers determine the shape of everything that follows.
