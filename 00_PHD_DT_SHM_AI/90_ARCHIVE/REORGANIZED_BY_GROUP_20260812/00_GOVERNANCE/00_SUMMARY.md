# 00 — REORGANIZATION PLAN SUMMARY

**Plan ID:** REORGANIZATION_PLAN_20260803
**Date:** 2026-08-03
**Repository:** `H:\My Drive\03_RESEARCH\01_PHD_DT_AI_AM\00_PHD_DT_STEEL_INSPECTION_2026_2029_LIMITED_FEM`
**Status:** **PLAN ONLY — NOTHING HAS BEEN MOVED.** Awaiting the command `APPROVE REORGANIZATION`.

---

## 0. Scope and boundaries

- Only this repository folder was read. **Nothing outside it was accessed, scanned, copied, moved, or changed.**
- Raw experimental data is stored by the user on separate storage outside this repository. It is **out of scope**, treated as external-by-design, and **not** treated as missing. This plan makes no reference to, and takes no action on, any external location.
- The only write performed in this session was the creation of this plan folder and its 7 files.
- No `DELETE` action appears anywhere in this plan.

## 1. Current state

| Metric | Value |
|---|---|
| Files | 313 (301 research files + 12 audit reports from 2026-08-03) |
| Directories | 63 |
| Total size | ~183.9 MiB |
| Loose files at root | 8 |
| Empty directories | 6 |
| Files inside `90_BACKUP/` | 127 (40.6%) |

## 2. Proposed action summary

| Action | Rows | Meaning |
|---|---:|---|
| `KEEP` | 109 | Stays exactly where it is |
| `ARCHIVE` | 144 | Moves under `90_ARCHIVE/` — preserved, never deleted |
| `RENAME` | 28 | Folder renamed; file keeps its name (`ZOTERO_AUDIT`→`ZOTERO_DEEP_READ`, `PERPLEXITY_PRO`→`PERPLEXITY_DISCOVERY`) |
| `MOVE` | 17 | Relocated to the correct functional group |
| `MOVE_TO_REVIEW` | 9 | Role undetermined → `91_REVIEW_REQUIRED/`, decision left to the user |
| `NO_ACTION` | 12 | Audit reports already in `99_REPOSITORY_LOGS/` |
| **Total** | **319** | 313 files + 6 directory rows |

## 3. What changes at root

**Before:** 8 loose files + 13 folders (2 outside the numbered scheme).
**After:** 1 loose file + 12 top-level folders + `.claude/` (hidden IDE config).

| Root item | Action | Destination |
|---|---|---|
| `00_README_START_HERE.md` | **KEEP** | the single entry point |
| `00_README_START_HERE_v2.1_UPDATED_20260719.md` | ARCHIVE | `90_ARCHIVE/README_HISTORY/` |
| `00_README_START_HERE_v2.2_UPDATED_20260720.md` | ARCHIVE | `90_ARCHIVE/README_HISTORY/` |
| `Skill.md` | MOVE_TO_REVIEW | `91_REVIEW_REQUIRED/STALE_AGENT_RULES/` |
| `PROMPT_CONTROL_CENTER_PROJECT_INSTRUCTIONS.md` | MOVE | `07_PROMPTS_AND_HANDOFFS/PROMPT_CONTROL_CENTER/` |
| `PROMPT_CONTROL_CENTER_PROJECT/` (7 files) | MOVE | `07_PROMPTS_AND_HANDOFFS/PROMPT_CONTROL_CENTER/` |
| `NOTEBOOKLM_BRIEF_G1_PAPER1_VS_AVCI_2021.md` | MOVE | `07_PROMPTS_AND_HANDOFFS/NOTEBOOKLM/` |
| `YEU_CAU_CAP_NHAT_WEBSITE_BIM_VIEWER_DIGITAL_TWIN_DEMO_20260727.md` | MOVE | `08_DEMO_AND_PROTOTYPES/IT_HANDOFFS/` |
| `BIM-AEC-CLAUDE.jpg` | MOVE | `07_PROMPTS_AND_HANDOFFS/ASSETS/` |
| `New folder/` (empty) | MOVE_TO_REVIEW | `91_REVIEW_REQUIRED/EMPTY_FOLDERS/` |

## 4. Governance — one active file per role

Seventeen roles are registered in `03_CANONICAL_FILE_REGISTER.csv`. Active set retained in `00_GOVERNANCE/`:

`MASTER_RESEARCH_CHARTER_v2.1_TRACEABILITY_CORE_20260719.md` · `RQ_WP_CHAPTER_PAPER_GATE_MATRIX_v2.1.md` · `EVIDENCE_GATES_v2.1.md` · `RESEARCH_ARCHITECTURE_DECISION_RECORD_20260719.md` · `RESEARCH_ARCHITECTURE_DECISION_RECORD_ACTION_ID_20260719.md` · `TERMINOLOGY_CONTROL_CURRENT.md` · `SOURCE_OF_TRUTH_HIERARCHY_v2.1.md` · `THE_COUNCIL_REVIEW_FEM_OR_NO_FEM_17.07.2026.md` · `V2.1_CORE_EVIDENCE_INDEX.md` · `RESEARCH_ARCHITECTURE.md` · `RESEARCH_DIRECTION_AND_SCOPE.md` · `AGENT_RULES.md` · `CLAUDE.md` · `MASTER_RESEARCH_CHARTER.md` (navigation pointer only)

Archived from governance:

| File | To | Why |
|---|---|---|
| `MASTER_RESEARCH_CHARTER_v2_20260719.docx` | `90_ARCHIVE/GOVERNANCE_HISTORY/CHARTERS/` | Charter v2.0, superseded by v2.1 |
| `LIVING_EVIDENCE_BASE_v1.1_LIMITED_FEM.md` | `90_ARCHIVE/GOVERNANCE_HISTORY/EVIDENCE_BASE/` | Historical base; the v2.1 pointer already demotes it |
| `01_LIVING_EVIDENCE_BASE_v1.2_LIMITED_FEM_20260718.md` | `90_ARCHIVE/GOVERNANCE_HISTORY/EVIDENCE_BASE/` | Same |
| 5 files in `01_CURRENT_CONTROL/PROJECT_CLEANUP_20260718/` | `90_ARCHIVE/CLEANUP_PROVENANCE_20260718/` | Provenance of the 2026-07-18 cleanup |

`MASTER_INDEX_CURRENT.md` is promoted out of the dated cleanup subfolder to `01_CURRENT_CONTROL/MASTER_INDEX_CURRENT.md` — **the highest-risk single move** (22 outbound relative links inside it must be re-based).

## 5. `90_BACKUP/` → `90_ARCHIVE/`

All 127 files move; none is deleted. They are split by content uniqueness:

| Destination | Files | Classification |
|---|---:|---|
| `90_ARCHIVE/HISTORICAL_UNIQUE_FILES/` | 41 | **No copy exists anywhere else in the repository.** One representative per unique hash |
| `90_ARCHIVE/SNAPSHOTS_20260718/` | 86 | Exact duplicate of an active file, or a 2nd/3rd copy of a preserved unique file |

The 41 unique files include the only surviving copies of `MASTER_RESEARCH_CHARTER_v1.0_SUPERSEDED_20260717.md`, `MASTER_RESEARCH_CHARTER_v1.1_LIMITED_FEM_20260717.md`, `RESEARCH_ARCHITECTURE_DECISION_RECORD_20260717.md`, `Literature_Review_Master_Index_Current.md`, `MASTER_INDEX_CURRENT_v1.1.md`, `TERMINOLOGY_CONTROL_v1.1.md`, the 5-file Fable legacy pack, the cleanup provenance manifests, and the repository's only three `.py` helper scripts.

Relative sub-paths are preserved under both destinations, so the snapshot's internal shape stays legible.

## 6. Literature separation

- `PERPLEXITY_PRO/` → `06_LITERATURE_AND_ZOTERO/PERPLEXITY_DISCOVERY/` — discovery-tier, explicitly **not** peer-reviewed evidence, and no longer sharing a parent with curated evidence.
- `ISO-IEC-30173-2023.pdf` → `06_LITERATURE_AND_ZOTERO/STANDARDS/`.
- `06_LITERATURE_AND_ZOTERO/MISSING_FULLTEXT/` created with a README placeholder (tracker item #13 lists 3 missing RQ2 full texts). **No content is fabricated.**
- Curated per-gate deep-read PDF sets stay inside `02_EVIDENCE_BASE/RQ*_GATE*/` — they are the evidence for those gates, and moving them would break gate-scoped organisation for no gain.

**`kim2018.pdf` duplicates (3 active copies, byte-identical):**

| Path | Action |
|---|---|
| `02_EVIDENCE_BASE/RQ2_GATES2_3/DEEP_READ_20.07.2026/kim2018.pdf` | **KEEP — canonical** (member of the curated 20.07 deep-read set) |
| `02_EVIDENCE_BASE/RQ2_GATES2_3/kim2018.pdf` | ARCHIVE → `90_ARCHIVE/DUPLICATE_LITERATURE/` |
| `06_LITERATURE_AND_ZOTERO/PERPLEXITY_PRO/References/Gate 2.1 kim2018.pdf` | ARCHIVE → `90_ARCHIVE/DUPLICATE_LITERATURE/` |

SHA-256 recorded for all three in `04_ARCHIVE_PLAN.csv` (`2251629` bytes each).

## 7. Papers

`03_PAPERS/PAPER_1/` keeps its working subfolders (`CURRENT_MANUSCRIPT`, `GATE1_EVIDENCE`, `IT_REQUESTS`, `REFERENCE_AUDIT`, `REVISION_HISTORY`).

Two different fates, deliberately distinguished:

| Category | Files | Destination | Rationale |
|---|---:|---|---|
| **Known-superseded** — self-labelled old or already in a local archive folder | 5 | `90_ARCHIVE/PAPER_VERSION_HISTORY/PAPER_1/` | `Paper 1_Old_version (10.06).docx` + the v3/v4/v6 outlines already sitting in `ARCHIVE_MINIMAL/` |
| **Undetermined currency** — competing same-date versions | 6 | `91_REVIEW_REQUIRED/PAPER1_VERSION_REVIEW/` | 3 competing `.md` outlines all dated 19/07; 3 experiment protocols all dated 21/07 |

**This split is an interpretation and you may override it.** The instruction said versioned outlines with undetermined currency go to archive; the instruction also said undetermined-role files go to review. I applied *archive* only where the file itself declares it is old, and *review* where currency is genuinely unknown — because archiving all six would leave Paper 1 with no active outline. See `05_REVIEW_REQUIRED.md` item **R1**.

New: `03_PAPERS/PAPER_S1_SENSOR_COMPARISON_CANDIDATE/` receives `Yêu cầu phân tích PASCO–ADXL cho Paper S1.docx`, marked `CANDIDATE_SUPPORTING_PAPER_NOT_YET_GOVERNED`. **Not added to the RQ–WP–Gate matrix.**

## 8. G1 packages kept separate

`CANONICAL_THREE_CAMPAIGN_DATASET/` (dataset standardisation) and `THREE_CAMPAIGN_REANALYSIS/` (analysis results) both stay in place, unmerged. **No supersession claim is made in either direction** — neither package's own documentation states the relationship. `Checklist_Campaign_3_Gate1.docx` moves out of the folder root into `05_DATA_CODE_AND_EXPERIMENTS/CAMPAIGN_DOCUMENTATION/`.

## 9. Link risk

596 references from markdown to files that move were found. Scoped by whether repair is actually needed:

| Scope | Rows | Repair |
|---|---:|---|
| `ACTIVE_NAVIGATION` — **HIGH** (contains a path) | **79** | **Must be re-based** |
| `ACTIVE_NAVIGATION` — LOW (bare filename in prose) | 98 | Verify context only; no path to fix |
| `ARCHIVE_INTERNAL` | 223 | None — snapshot moves as a block; links already described a pre-2026-07-18 layout |
| `HISTORICAL_RECORD` | 155 | None — audit reports are a dated record of the pre-reorganisation state |
| `ARCHIVED_REFERRER` | 41 | None — the referring file is itself being archived |

The 79 HIGH-risk repairs concentrate in 21 files, led by `MASTER_INDEX_CURRENT.md` (22), `09_ZOTERO_DEEP_READ_COMPLETION_REPORT_20260718.md` (8), `SYSTEM_UPDATE_REPORT_v2.1_20260719.md` (7), and `PAPER1_GATE1_READINESS_REPORT_v2.md` (7). Full list in `06_BROKEN_LINK_RISK.csv`.

**Note:** the repository already contains 119 dangling references that predate this plan (recorded in the 2026-08-03 audit). Those are **not** caused by this reorganisation and are **not** repaired by it.

## 10. Legacy-direction guard

No file whose content advocates calibrated FEM, FEM-based diagnosis, EMA/MAC gating, stiffness degradation, predictive maintenance, RUL, field damage diagnosis, direct lab-to-field transfer, autonomous maintenance, or a commercial Digital Twin platform is moved **into** an ACTIVE folder by this plan. The pre-v2 FEM-core material in `90_BACKUP/` moves only deeper into `90_ARCHIVE/`. `Skill.md` — the one active file carrying a superseded identifier chain — moves **out** of ACTIVE into `91_REVIEW_REQUIRED/`, with its content untouched.

## 11. Post-approval execution order

1. Create the new folder skeleton (27 directories).
2. Batch A — root files (10 items), verify hashes.
3. Batch B — governance + current control (10 items), verify.
4. Batch C — evidence + literature (34 items), verify.
5. Batch D — papers + data (14 items), verify.
6. Batch E — `90_BACKUP` → `90_ARCHIVE` (127 items), verify.
7. Repair the 79 HIGH-risk links.
8. Re-hash all 313 files and diff against `02_MOVE_PLAN.csv`.
9. Emit the execution report set.

---

## Claim → Evidence → Limitation → Next action

**Claim.** A complete, reversible reorganisation plan covering all 313 files and 6 empty directories is ready. It yields a root containing one README plus twelve top-level folders; exactly one active file per governance role; G1, G2–G3, and RQ3 material separated; papers, evidence, literature, prompts, and demo unmixed; and every superseded or duplicate file preserved under `90_ARCHIVE/`. Nine files whose role could not be determined from metadata go to `91_REVIEW_REQUIRED/` rather than being decided unilaterally.

**Evidence.** Verified SHA-256 for all 313 files (301 carried forward from the 2026-08-03 audit, 12 newly hashed); 61 exact-duplicate groups; 63 backup files with no active-location twin, reduced to 41 unique hashes; role assignments taken from `SOURCE_OF_TRUTH_HIERARCHY_v2.1.md`, `V2.1_CORE_EVIDENCE_INDEX.md`, and `LIVING_EVIDENCE_BASE_CURRENT.md`; 596 markdown references classified into four repair scopes.

**Limitation.** Classification uses filename, path, hash, and the governance documents' own role statements. **The 13 `.docx` and 52 `.pdf` files were not read** — including the three competing experiment protocols and the v2.0 charter. For the six Paper 1 files with competing same-date versions, `Evidence is currently insufficient` to name the current one, which is why they go to review rather than archive. The archive-versus-review split in §7 is an interpretation open to override. Link risk is computed from backtick and markdown-link tokens; references in `.docx`/`.pdf` are not covered.

**No Gate is claimed to be closed, opened, or passed by this plan. No academic claim, metric, or citation is altered.**

**Next action.** Review `05_REVIEW_REQUIRED.md` (7 decisions), skim `02_MOVE_PLAN.csv`, then reply **`APPROVE REORGANIZATION`** — with any overrides — to execute. Until then the repository is untouched.
