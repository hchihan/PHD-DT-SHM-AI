# 00 — EXECUTIVE SUMMARY

**Audit ID:** REPOSITORY_AUDIT_20260803
**Date:** 2026-08-03
**Repository:** `00_PHD_DT_STEEL_INSPECTION_2026_2029_LIMITED_FEM`
**Absolute path scanned:** `H:\My Drive\03_RESEARCH\01_PHD_DT_AI_AM\00_PHD_DT_STEEL_INSPECTION_2026_2029_LIMITED_FEM`
**Mode:** READ-ONLY inventory. No file was deleted, moved, renamed, merged, or edited. The only write was the creation of this report folder.

> **Path note.** The task specified drive `G:\`. On this machine the Google Drive mount is `H:\`; the folder path below `03_RESEARCH\01_PHD_DT_AI_AM\` is otherwise identical. All paths in this audit are recorded as `H:\...`.

---

## 1. Scale

| Metric | Value |
|---|---|
| Sub-directories (excluding this report folder) | 61 |
| Empty directories | 6 |
| Files | 301 |
| Total size | 192,395,087 bytes ≈ **183.5 MiB** |
| Files hashed (SHA-256) | **301 / 301 (100%)** |
| Deepest path level | 5 (`90_BACKUP\PRE_FINAL_CLEANUP_SNAPSHOT_20260718\Perplexity_Pro\References\<file>`) |

## 2. Files by extension

| Extension | Count | Share |
|---|---|---|
| `.md` | 192 | 63.8% |
| `.pdf` | 52 | 17.3% |
| `.csv` | 39 | 13.0% |
| `.docx` | 13 | 4.3% |
| `.py` | 3 | 1.0% |
| `.json` | 1 | 0.3% |
| `.jpg` | 1 | 0.3% |

The repository is **document-dominated**. There is no raw measurement data file (`.npz`, campaign `.csv` recordings), and the only three `.py` files are cleanup helper scripts inside a 2026-07-18 backup snapshot — not analysis code. See §6.

## 3. Files by preliminary category

| Category | Count | Category | Count |
|---|---|---|---|
| BACKUP | 127 | SPECIAL_TOPIC | 4 |
| LITERATURE_EVIDENCE | 37 | IT_HANDOFF | 3 |
| ZOTERO_OUTPUT | 31 | REPORT | 3 |
| PAPER_DRAFT | 23 | REPRODUCIBILITY_PACKAGE | 2 |
| GOVERNANCE | 19 | RUN_REGISTRY | 1 |
| PROMPT | 18 | DEMO_PROTOTYPE | 1 |
| CURRENT_CONTROL | 15 | TEMPORARY_OUTPUT | 1 |
| MODEL_OUTPUT | 11 | ANALYSIS_CODE | 0 |
| LAB_PROCESSED_DATA | 5 | LAB_RAW_DATA | 0 |

**42% of all files (127 of 301) sit inside `90_BACKUP/`.** Only 174 files live in active locations.

## 4. Files by research strand

Counts are of *active-location* files; a file may map to more than one strand.

| Strand | Active files | Principal locations |
|---|---|---|
| G1 / RQ1 / WP1 — laboratory vibration evidence | ~63 | `05_DATA_CODE_AND_EXPERIMENTS/`, `03_PAPERS/PAPER_1/`, `02_EVIDENCE_BASE/RQ1_GATE1/` |
| G2–G3 / RQ2 / WP2 — traceability & schema | ~16 | `02_EVIDENCE_BASE/RQ2_GATES2_3/`, `03_PAPERS/PAPER_2/`, `06_LITERATURE_AND_ZOTERO/` |
| G4 / RQ3 / WP3 — field feasibility | ~3 | `02_EVIDENCE_BASE/RQ3_GATE4/`, `03_PAPERS/PAPER_3/` |
| G5 / WP4 — decision support | ~2 | `02_EVIDENCE_BASE/WP4_GATE5/` |
| Governance / control (strand-independent) | 34 | `00_GOVERNANCE/`, `01_CURRENT_CONTROL/`, root |
| Prompts / tooling | 25 | `07_PROMPTS_AND_HANDOFFS/`, `PROMPT_CONTROL_CENTER_PROJECT/`, root |

The distribution is **heavily front-loaded on G1 and governance**. G4 and G5 exist only as one evidence addendum and one direction note each.

## 5. Access and Google Drive status

**No access problem was found.**

- 301 / 301 files reported `FileAttributes = Normal (128)`. No file carried `Offline (0x1000)`, `RecallOnOpen (0x40000)`, or `RecallOnDataAccess (0x400000)` — i.e. **no Google Drive cloud-only placeholder exists** in this tree.
- 301 / 301 files were opened and fully read to compute SHA-256. Zero `ACCESS_ERROR`, zero `LOCKED`, zero `UNKNOWN`.
- No hash was skipped for size; the largest file is 15.8 MB, far under the 200 MB skip threshold.

**The inventory is therefore complete.** Nothing in this audit is limited by cloud-only availability. (See `09_ACCESS_AND_GOOGLE_DRIVE_ISSUES.csv`.)

## 6. Principal findings

### 6.1 The G1 evidence chain is documented but its data, code, and registry are not in this repository — **highest-impact finding**

`05_DATA_CODE_AND_EXPERIMENTS/` contains 23 files: reports, result CSVs, and dataset documentation. It contains **no raw data, no pipeline code, and no run registry.** Specifically, the following artifacts are named as evidence by files that *are* present, but do not exist anywhere in the repository:

- Raw campaign folders `Campaign1_25.04.2026/`, `Campaign2_22.07.2026/`, `Campaign3_29.07.2026/` (stated as 72 CSVs each, 216 total).
- `02_MASTER_RUN_REGISTRY.csv` (216 rows) and `06_MASTER_RUN_REGISTRY.csv` — cited as the evidence for the completeness claim in `THREE_CAMPAIGN_REANALYSIS/00_EXECUTIVE_REPORT.md` §1.
- `RUN_REGISTRY_LOCKED.csv` — referenced by **six** separate active documents including `EVIDENCE_GATES_v2.1.md`. This is blocking item #1 in `UNRESOLVED_ITEMS_TRACKER_v2.1.md`.
- All 20 pipeline scripts (`build_registry.py`, `pipeline_lib.py`, `run_cnn.py`, `canon_lib.py`, `stage1_inventory.py` … ), whose SHA-256 values are published in `01_ENVIRONMENT_PROVENANCE.md` and `10_REPRODUCIBILITY_MANIFEST.md`.
- `CANONICAL_THREE_CAMPAIGN_DATASET.zip`, which `CANONICAL_THREE_CAMPAIGN_DATASET/00_README.md` states holds all 216 NPZ layers, analysis sets, fold manifests, and pipeline code, and which was "delivered alongside this folder via the chat file cards".
- Intermediate result files cited in `00_EXECUTIVE_REPORT.md`: `04_ANALYSIS_SET_MANIFEST.csv`, `10_PER_CLASS_RESULTS.csv`, `14_PREDICTIONS_WITH_PROVENANCE.csv`, `sensor_fingerprint_check.csv`, `sensor_block_permutation_flags.csv`.

Present result files are numbered `00,01,03,05,06,07,08,09,11,12,13,15` — the gaps at 02, 04, 10, 14 correspond exactly to the missing registry/manifest/per-class/prediction files.

`10_REPRODUCIBILITY_MANIFEST.md` also discloses that `canon_lib.py` hard-codes a session-sandbox path (`/sessions/affectionate-adoring-galileo/mnt/DATA_ALL_3_CAMPAIGN`), so even the packaged code is not directly runnable from this repository.

**Consequence to review:** the G1 result CSVs currently present cannot be independently regenerated or verified from anything inside this repository. This is a statement of what the audit could and could not find; it is not a judgement about whether the results are correct, and it is not a claim that the data is lost — it may exist outside this folder or in the delivered zip.

### 6.2 Governance points to three folders that do not exist

`SOURCE_OF_TRUTH_HIERARCHY_v2.1.md` — the file whose stated purpose is "one and only one priority order when documents conflict" — routes readers to:

| Referenced target | Status |
|---|---|
| `99_ARCHIVE_PRE_V2_SYSTEM_20260719/` (+ `LEGACY_CHARTERS/`, `LEGACY_NAVIGATION/`) | **does not exist** |
| `92_ARCHIVE_MINIMAL/` | **does not exist** |
| `ARCHIVE_MANIFEST.md` | **does not exist** |
| `UNRESOLVED_ITEMS_CURRENT.md` | **does not exist** |
| `05_DATA_CODE_AND_EXPERIMENTS/G1_EXECUTION_PACK/` (12 templates, tracker item #17) | **does not exist** |

`00_README_START_HERE.md` and `MASTER_INDEX_CURRENT.md` repeat the same dangling pointers. The v1.1 charter and pre-v2 ADR that the hierarchy says were "archived into `99_ARCHIVE_PRE_V2_SYSTEM_20260719/`" are in fact only present inside `90_BACKUP/` — a location the same document declares "never a source of truth".

A total of **119 distinct referenced artifacts** cited in active markdown were not found in the repository. Full list in `07_LEGACY_DIRECTION_SCAN.md` §4 and `10_MANUAL_REVIEW_PRIORITY.md`.

### 6.3 Version conflict at the top of the governance stack

Three `00_README_START_HERE*` files sit at the repository root:

| File | Modified | Self-declared status |
|---|---|---|
| `00_README_START_HERE.md` | 2026-07-19 | "Kiến trúc hiện hành: Traceability-Core v2.1" |
| `00_README_START_HERE_v2.1_UPDATED_20260719.md` | 2026-07-19 | v2.1 |
| `00_README_START_HERE_v2.2_UPDATED_20260720.md` | 2026-07-20 | **"Phiên bản vận hành: v2.2"** |

The v2.2 README explicitly states that the governance set has *not yet* been synchronised to v2.2 and that Charter v2.1 remains the highest academic source. Meanwhile `V2.1_CORE_EVIDENCE_INDEX.md` names the unsuffixed `00_README_START_HERE.md` as the current entry point and does not mention v2.2 at all. **No single file is unambiguously the current root README.** This audit does not resolve which one wins.

### 6.4 Duplication

| Measure | Value |
|---|---|
| Exact (byte-identical) duplicate groups | **61** |
| Files inside an exact duplicate group | **150** (49.8% of all files) |
| Redundant bytes | 39,736,267 ≈ **37.9 MiB** (20.7% of repository) |
| Duplicate pair rows reported | 89 exact + 64 near/version = **153** |
| Version-series / likely-duplicate / possible-superseded pairs | 40 / 15 / 9 |
| Files carrying a version token in the filename | 161 |

Structure of the duplication:

- **46 of 61** exact groups are an active file mirrored in `90_BACKUP/` — expected for a snapshot, low risk.
- **14 of 61** are duplicated *within* `90_BACKUP/` itself: `PRE_FINAL_CLEANUP_SNAPSHOT_20260718/` contains a nested copy of `BACKUP_BEFORE_WRITEBACK_20260718/` (23 files), a `Zotero MCP/` copy of the same evidence pack (10 files), and a `Perplexity_Pro/` copy (26 files). The backup tree stores the same evidence pack **three times**.
- **2 groups duplicate inside active locations** and deserve a decision:
  - `kim2018.pdf` — three active copies: `02_EVIDENCE_BASE/RQ2_GATES2_3/kim2018.pdf`, `.../DEEP_READ_20.07.2026/kim2018.pdf`, `06_LITERATURE_AND_ZOTERO/PERPLEXITY_PRO/References/Gate 2.1 kim2018.pdf`.
  - `phd-scope.md` — identical file under both `phd-prompt-compressor/references/` and `phd-prompt-router/references/`.

### 6.5 Suspected governance conflicts (preliminary — 4 items)

| # | Conflict | Evidence |
|---|---|---|
| 1 | Root README version (v2.1 vs v2.2) | §6.3 |
| 2 | `Skill.md` (root) uses the **pre-v2.1 identifier chain** — `… → Inspection_Record_ID → Action_Status` and `FEM_Node_ID = optional metadata`. Charter v2.1 / README v2.2 lock the chain as `… → Inspection_Record_ID → Action_Record_ID`, with `Action_Status` demoted to an attribute. `Skill.md` is an unversioned, active root file with no supersede header. | `Skill.md` §2 vs `V2.1_CORE_EVIDENCE_INDEX.md`, `00_README_START_HERE_v2.2_UPDATED_20260720.md` §2.2 |
| 3 | Two files both act as "master index": `01_CURRENT_CONTROL/PROJECT_CLEANUP_20260718/MASTER_INDEX_CURRENT.md` (named current by the hierarchy, but stored inside a dated cleanup subfolder) and `90_BACKUP/.../MASTER_INDEX_CURRENT_v1.1.md`. | `SOURCE_OF_TRUTH_HIERARCHY_v2.1.md` §1 item 5 |
| 4 | Three "Living Evidence Base" documents in `02_EVIDENCE_BASE/CURRENT/` (v1.1, v1.2, v2.1) plus a pointer file. The pointer resolves this correctly; noted only because the folder is named `CURRENT`. | `LIVING_EVIDENCE_BASE_CURRENT.md` |

Item 4 is **already resolved by an explicit pointer file** and is listed for completeness, not as an unresolved conflict.

### 6.6 Legacy-direction keywords

129 files (57 of them in active locations) contain at least one keyword from the legacy-direction list (calibrated FEM, EMA, MAC, stiffness degradation, RUL, predictive maintenance, Health Index, autonomous maintenance, FEM_Node_ID, commercial platform).

**The large majority are guardrails, not legacy direction.** 278 of 516 keyword occurrences sit inside an explicit negation/exclusion phrase ("không mở rộng sang…", "REMOVE from claims", "Prohibited:", "out of scope"). The terminology-control and charter files necessarily *name* the excluded concepts in order to exclude them. Flagging these as legacy content would be a false positive.

Items that genuinely warrant a read: `Skill.md` (§6.5 #2), `THE_COUNCIL_REVIEW_FEM_OR_NO_FEM_17.07.2026.md` (decision-authority document that discusses FEM/EMA/MAC at length — historical by role, but ranked #1 in the source-of-truth hierarchy), and the v1.1 evidence base. Detail in `07_LEGACY_DIRECTION_SCAN.md`.

## 7. Most complex areas of the repository

Ranked by review burden, not by size:

1. **`90_BACKUP/` (127 files, 33.9 MB, 100 files in exact duplicate groups)** — three-deep nested snapshots of the same content; contains the only surviving copies of the v1.1 charter and pre-v2 ADR that governance believes live elsewhere.
2. **`05_DATA_CODE_AND_EXPERIMENTS/` (23 files)** — smallest by size, largest by consequence. Two parallel G1 packages (`CANONICAL_THREE_CAMPAIGN_DATASET` and `THREE_CAMPAIGN_REANALYSIS`) with overlapping but non-identical registries, both missing their data and code.
3. **Repository root (10 loose files + 2 loose folders)** — three READMEs, an unversioned `Skill.md` carrying a stale identifier chain, a duplicated prompt-control-centre (folder *and* standalone instructions file), an empty `New folder`, and an untracked JPG.
4. **`00_GOVERNANCE/` + `01_CURRENT_CONTROL/` (30 files)** — internally consistent in content, but the navigation layer points at five non-existent targets.
5. **`06_LITERATURE_AND_ZOTERO/PERPLEXITY_PRO/` (25 files, 24 in duplicate groups)** — near-total mirror of `90_BACKUP/.../Perplexity_Pro/`.

## 8. Risks requiring manual review

| # | Risk | Why it matters |
|---|---|---|
| R1 | G1 raw data, pipeline code, and run registry are not in the repository | Gate 1 cannot be closed or independently verified from this repository; blocking tracker items #1–#3 depend on artifacts that are absent |
| R2 | Source-of-truth hierarchy points to non-existent archive folders | Any agent or reader following the documented navigation path hits a dead end; "archived" v1.1 files actually survive only in `90_BACKUP/` |
| R3 | No unambiguous current root README (v2.1 vs v2.2) | Two different operating versions are simultaneously live at the entry point |
| R4 | `Skill.md` propagates the superseded `Action_Status` identifier chain | It is a prompt-generation skill; a stale chain here re-injects the old model into every downstream prompt |
| R5 | `90_BACKUP/` holds unique content, not just copies | It cannot be treated as safe-to-discard until the unique files are identified |
| R6 | Sensor column-position instability in Campaigns 1 and 2 | Self-reported in `00_EXECUTIVE_REPORT.md` §1 as the single most important open analysis item; affects every single/paired-sensor result from those campaigns |
| R7 | 6 empty directories, incl. `New folder` and `02_EVIDENCE_BASE/02.08.2026 Q2-Q3` | Intent unknown; the dated one suggests an in-progress but unstarted work phase |
| R8 | 119 dangling artifact references across active documents | Indicates documentation written against a workspace larger than this repository |

## 9. Recommended order for the next audit stage

No move, merge, archive, or deletion is recommended by this report. The proposed *reading* order is:

1. **Confirm the source of truth.** Resolve README v2.1 vs v2.2; decide the status of `Skill.md`; decide whether `99_ARCHIVE_PRE_V2_SYSTEM_20260719/` and `92_ARCHIVE_MINIMAL/` were never created, were created elsewhere, or should be created. (`06_GOVERNANCE_AND_SOURCE_OF_TRUTH_CANDIDATES.md`)
2. **Locate the G1 data, code, and run registry** — establish whether they exist outside this repository, inside the delivered zip, or not at all. Nothing in G1 can be judged before this. (`03_RESEARCH_CAMPAIGN_AND_PHASE_MAP.md`)
3. **Separate current from superseded** across the 25 document families with more than one member. (`04_DOCUMENT_VERSION_MAP.csv`)
4. **Identify unique content inside `90_BACKUP/`** before that tree is treated as redundant. (`05_DUPLICATE_AND_NEAR_DUPLICATE_REPORT.csv`)
5. **Review the loose root items** and the two-folder prompt-control-centre split. (`08_LOOSE_ROOT_ITEMS_REPORT.md`)
6. Only then define a target structure and a move/archive plan, for user approval. (`11_NEXT_AUDIT_PLAN.md`)

---

## 10. Read-only compliance verification

After the reports were written, the entire repository was re-enumerated and every file re-hashed, then diffed against the pre-audit inventory.

| Check | Result |
|---|---|
| Original files with changed content | **1** — see note below |
| Original files deleted | **0** |
| Original files moved or renamed | **0** |
| Files added | **12** — all inside `99_REPOSITORY_LOGS/REPOSITORY_AUDIT_20260803/` |
| Directories created | **2** — `99_REPOSITORY_LOGS/` and `REPOSITORY_AUDIT_20260803/` |

**The one changed file: `.claude/settings.local.json`** (719 bytes → modified 2026-08-03). This is the Claude Code tool-permission file, rewritten by the agent harness when tool permissions were granted during this session. It is IDE configuration, not research content. It was **not** opened or edited by any audit step. No governance, evidence, paper, data, code, or literature file was altered in any way.

**Every one of the 300 research files carries the same SHA-256 after the audit as before it.**

---

## Claim → Evidence → Limitation → Next action

**Claim.** The repository contains 301 files (183.5 MiB) across 61 directories, all locally available and fully hashed. It is a document-and-governance repository: 42% of files are backup copies, 50% participate in an exact-duplicate group, and it contains no raw laboratory data and no analysis code. Its governance layer is internally coherent in content but points at five targets that do not exist, and two active files (root README, `Skill.md`) carry version/identifier statements that conflict with the declared v2.1/v2.2 architecture.

**Evidence.** Full enumeration via `Get-ChildItem -Recurse -Force` (301 files, 61 directories); SHA-256 computed for 301/301 files; `FileAttributes` inspected for cloud-only bits on every file; 61 exact-duplicate groups identified by hash collision across differing paths; 119 dangling artifact references extracted from backtick-quoted tokens in 174 active-location markdown files and checked against the file table; direct reading of `SOURCE_OF_TRUTH_HIERARCHY_v2.1.md`, `V2.1_CORE_EVIDENCE_INDEX.md`, `UNRESOLVED_ITEMS_TRACKER_v2.1.md`, `CURRENT_STATUS_AND_NEXT_DIRECTION.md`, the three root READMEs, `Skill.md`, `THREE_CAMPAIGN_REANALYSIS/00_EXECUTIVE_REPORT.md`, `01_ENVIRONMENT_PROVENANCE.md`, `15_NEXT_ANALYSIS_RECOMMENDATION.md`, and `CANONICAL_THREE_CAMPAIGN_DATASET/00_README.md` + `10_REPRODUCIBILITY_MANIFEST.md`.

**Limitation.**
- Categories, RQ/WP/Gate tags, campaign tags, and duplicate-risk levels in the CSVs are assigned by **path-and-filename rule plus targeted reading**, not by full reading of all 301 files. They are descriptive, provisional, and must be confirmed by a human.
- Near-duplicate detection compares normalised filenames and sizes, not document content. Two files with unrelated names but overlapping content would not be detected.
- The 13 `.docx` and 52 `.pdf` files were inventoried and hashed but **not** read for content; their classification rests on filename and location only.
- "Missing" means *not present under this repository root*. Files may exist in sibling folders (`01_KNOWLEDGE/`, `04_AI_SYSTEM/`, `05_MASTER_INDEX_CONTROL/`), in the delivered zip, or on another machine. This audit did not scan outside the specified root.
- No canonical file has been selected for any conflicting family. All duplicate, legacy, and conflict findings are **preliminary**.

**Next action.** User reviews reports 02–11, then decides the three questions that gate everything else: (a) which README and which charter are current; (b) where the G1 data, code, and run registry live; (c) whether `90_BACKUP/` may be consolidated. No reorganisation is to be performed before that decision.

**Status of this run: the repository has been inventoried only. No file has been moved, renamed, or deleted; all 300 research files verify byte-identical after the audit (§10). No canonical source of truth has been confirmed. All duplicate, legacy, and conflict findings are preliminary and require user review before any reorganisation.**

---

## Report index

| File | Contents |
|---|---|
| `00_EXECUTIVE_SUMMARY.md` | This document |
| `01_FULL_REPOSITORY_INVENTORY.csv` | 301 rows — every file with SHA-256, category, RQ/WP/Gate/Paper, campaign, version, duplicate and legacy flags |
| `02_FOLDER_TREE_AND_STATISTICS.md` | 5-level tree, per-folder statistics, duplication hot-spots, unique content inside `90_BACKUP/` |
| `03_RESEARCH_CAMPAIGN_AND_PHASE_MAP.md` | G1 campaigns, G2–G3, RQ3/G4–G5, sub-topics — what exists and what is missing per strand |
| `04_DOCUMENT_VERSION_MAP.csv` | 139 rows — 25 document families with more than one member, with conflict risk |
| `05_DUPLICATE_AND_NEAR_DUPLICATE_REPORT.csv` | 153 pairs — 89 exact, 40 version-series, 15 likely-duplicate, 9 possible-superseded |
| `06_GOVERNANCE_AND_SOURCE_OF_TRUTH_CANDIDATES.md` | 12 governance roles, 41 candidates, no canonical selected |
| `07_LEGACY_DIRECTION_SCAN.md` | 14 keyword families, 516 occurrences, exclusion-context separation, 119 dangling references |
| `08_LOOSE_ROOT_ITEMS_REPORT.md` | 8 loose root files, 13 root folders, the four-location prompt-tooling cluster, 6 empty directories |
| `09_ACCESS_AND_GOOGLE_DRIVE_ISSUES.csv` | Nil return — no cloud-only, locked, or unreadable file |
| `10_MANUAL_REVIEW_PRIORITY.md` | Five priority tiers with dependency order and effort estimate |
| `11_NEXT_AUDIT_PLAN.md` | Six-stage forward plan; stages 4–6 gated on user approval |
