# 02 — FOLDER TREE AND STATISTICS

**Audit ID:** REPOSITORY_AUDIT_20260803 · Read-only · 301 files · 61 directories · 183.5 MiB

`n` = files at or below this node. `size` = cumulative bytes. `dup` = files at or below this node that are byte-identical to a file elsewhere. `ver` = files whose name carries a version/date token.

---

## 1. Directory tree (5 levels)

```
00_PHD_DT_STEEL_INSPECTION_2026_2029_LIMITED_FEM/          n=301  183.5 MiB  dup=150  ver=161
│
├── .claude/                                                n=1      1 KB   — agent settings
│
├── 00_GOVERNANCE/                                          n=15   139 KB   dup=1   ver=9
│       Charter v2.1 (.md) + v2.0 (.docx), Evidence Gates v2.1, RQ/WP/Paper/Gate
│       matrix v2.1, Source-of-Truth hierarchy, 2 ADRs, terminology control,
│       AGENT_RULES, CLAUDE.md, Council review 17.07, V2.1 core evidence index
│
├── 01_CURRENT_CONTROL/                                     n=15   120 KB   dup=1   ver=12
│   └── PROJECT_CLEANUP_20260718/                           n=6     89 KB   dup=1   ver=6
│           MASTER_INDEX_CURRENT.md, cleanup final report, pre-cleanup inventory
│           CSV, migration manifest CSV, deleted-superseded manifest, broken-link audit
│
├── 02_EVIDENCE_BASE/                                       n=41  115.3 MiB dup=11  ver=17
│   ├── 02.08.2026 Q2-Q3/                                   n=0        —    ** EMPTY **
│   ├── CURRENT/                                            n=5     50 KB   dup=1   ver=5
│   │       Living Evidence Base v1.1, v1.2, v2.1 + CURRENT pointer + migration report
│   ├── RQ1_GATE1/                                          n=17    78.1 MiB dup=1   ver=3
│   │   └── RQ1_UPDATED_DEEP_READ_10.07/                    n=16    78.1 MiB dup=0   ver=2
│   │           16 literature PDFs (Avci 2021, Abdeljaber 2018, SHMnet, …)
│   ├── RQ2_GATES2_3/                                       n=12    37.1 MiB dup=4   ver=2
│   │   └── DEEP_READ_20.07.2026/                           n=5     11.8 MiB dup=1   ver=0
│   │           5 traceability/provenance PDFs (Antunes 2024, Çelik 2023, Lee 2021, …)
│   ├── RQ3_GATE4/                                          n=1      4 KB   dup=1   ver=1
│   ├── WP4_GATE5/                                          n=1      3 KB   dup=1   ver=1
│   └── ZOTERO_AUDIT/                                       n=5     48 KB   dup=3   ver=5
│
├── 03_PAPERS/                                              n=26   801 KB   dup=4   ver=23
│   ├── PAPER_1/                                            n=23   781 KB   dup=4   ver=21
│   │   ├── ARCHIVE_MINIMAL/OUTLINE_VERSION_REVIEW/         n=4    416 KB   dup=3   ver=3
│   │   ├── CURRENT_MANUSCRIPT/                             n=1     39 KB   dup=0   ver=1
│   │   ├── GATE1_EVIDENCE/                                 n=2      9 KB   dup=0   ver=2
│   │   ├── IT_REQUESTS/                                    n=1      6 KB   dup=0   ver=1
│   │   ├── REFERENCE_AUDIT/                                n=1      7 KB   dup=1   ver=1
│   │   └── REVISION_HISTORY/                               n=1      7 KB   dup=0   ver=1
│   ├── PAPER_2/                                            n=1      5 KB   — direction note only
│   ├── PAPER_3/                                            n=1      3 KB   — direction note only
│   └── PAPER_4_OPTIONAL/                                   n=0        —    ** EMPTY **
│
├── 04_PHD_SPECIAL_TOPICS/                                  n=4     30 KB   dup=4   ver=4
│   ├── CHUYEN_DE_1/                                        n=0        —    ** EMPTY **
│   ├── CHUYEN_DE_2/                                        n=0        —    ** EMPTY **
│   └── CHUYEN_DE_TONG_QUAN/                                n=4     30 KB   dup=4   ver=4
│
├── 05_DATA_CODE_AND_EXPERIMENTS/                           n=23   169 KB   dup=0   ver=0
│   ├── CANONICAL_THREE_CAMPAIGN_DATASET/                   n=8     29 KB   dup=0   ver=0
│   │       README, channel-quality rules, data dictionary, dataset variants,
│   │       validation report, reproducibility manifest, IT handoff, automated
│   │       validation results CSV      ** no NPZ, no code, no registry **
│   ├── THREE_CAMPAIGN_REANALYSIS/                          n=14   103 KB   dup=0   ver=0
│   │   ├── 12_CONFUSION_MATRICES/                          n=3    <1 KB
│   │   └── 13_TRAINING_CURVES/                             n=1      1 KB   (README: curves not retained)
│   └── Checklist_Campaign_3_Gate1.docx                     n=1     37 KB
│
├── 06_LITERATURE_AND_ZOTERO/                               n=26    32.7 MiB dup=24  ver=1
│   ├── PERPLEXITY_PRO/                                     n=25    32.7 MiB dup=24  ver=1
│   │   └── References/                                     n=13    32.6 MiB dup=13  ver=1
│   ├── REFERENCE_EXPORTS/                                  n=0        —    ** EMPTY **
│   └── ZOTERO_MCP/                                         n=1     <1 KB   (README only)
│
├── 07_PROMPTS_AND_HANDOFFS/                                n=8     54 KB   dup=5   ver=3
│   ├── OPENCODE/                                           n=3     45 KB   dup=3   ver=3
│   │   └── PAPER1/                                         n=1     16 KB   dup=1   ver=1
│   ├── phd-prompt-compressor/references/                   n=2      4 KB   dup=1
│   └── phd-prompt-router/references/                       n=3      5 KB   dup=1
│
├── 90_BACKUP/                                              n=127   33.9 MiB dup=100 ver=89
│   ├── BACKUP_BEFORE_WRITEBACK_20260718/                   n=23   150 KB   dup=23  ver=20
│   └── PRE_FINAL_CLEANUP_SNAPSHOT_20260718/                n=104   33.7 MiB dup=77  ver=69
│       ├── 01_CURRENT_CONTROL/PROJECT_CLEANUP_20260718/    n=8    103 KB   dup=1   ver=6
│       │       (contains the only 3 .py files in the repository)
│       ├── 07_FABLE_LEGACY_PACK_20260718/                  n=5     18 KB   dup=0   ver=5
│       ├── 92_ARCHIVE_SUPERSEDED_FILES/                    n=3     12 KB   dup=0   ver=3
│       ├── BACKUP_BEFORE_WRITEBACK_20260718/               n=23   150 KB   dup=23  ver=20   ← nested re-copy
│       ├── Paper 1/                                        n=10   497 KB   dup=5   ver=10
│       ├── Perplexity_Pro/                                 n=26    32.8 MiB dup=25  ver=3
│       │   └── References/                                 n=13    32.6 MiB dup=13  ver=1
│       └── Zotero MCP/                                     n=10    70 KB   dup=10  ver=10   ← 3rd copy of evidence pack
│
├── New folder/                                             n=0        —    ** EMPTY **
├── PROMPT_CONTROL_CENTER_PROJECT/                          n=7     11 KB   dup=0   ver=0
│
└── (8 loose files at root — see 08_LOOSE_ROOT_ITEMS_REPORT.md)
        00_README_START_HERE.md
        00_README_START_HERE_v2.1_UPDATED_20260719.md
        00_README_START_HERE_v2.2_UPDATED_20260720.md
        BIM-AEC-CLAUDE.jpg
        NOTEBOOKLM_BRIEF_G1_PAPER1_VS_AVCI_2021.md
        PROMPT_CONTROL_CENTER_PROJECT_INSTRUCTIONS.md
        Skill.md
        YEU_CAU_CAP_NHAT_WEBSITE_BIM_VIEWER_DIGITAL_TWIN_DEMO_20260727.md
```

---

## 2. Top-level folder statistics

| Folder | Files | Size | % of bytes | Exact-dup files | Versioned files | Dominant content |
|---|---:|---:|---:|---:|---:|---|
| `02_EVIDENCE_BASE` | 41 | 115.3 MiB | 62.9% | 11 | 17 | Literature PDFs + evidence addenda |
| `90_BACKUP` | 127 | 33.9 MiB | 18.5% | 100 | 89 | Snapshot copies |
| `06_LITERATURE_AND_ZOTERO` | 26 | 32.7 MiB | 17.8% | 24 | 1 | Perplexity outputs + reference PDFs |
| `03_PAPERS` | 26 | 801 KB | 0.4% | 4 | 23 | Paper 1 package |
| `05_DATA_CODE_AND_EXPERIMENTS` | 23 | 169 KB | 0.1% | 0 | 0 | G1 reports + result CSVs |
| `00_GOVERNANCE` | 15 | 139 KB | 0.1% | 1 | 9 | Charter / gates / ADR |
| `01_CURRENT_CONTROL` | 15 | 120 KB | 0.1% | 1 | 12 | Status, trackers, cleanup logs |
| `07_PROMPTS_AND_HANDOFFS` | 8 | 54 KB | <0.1% | 5 | 3 | Prompts + 2 skills |
| `PROMPT_CONTROL_CENTER_PROJECT` | 7 | 11 KB | <0.1% | 0 | 0 | Prompt-system docs |
| `04_PHD_SPECIAL_TOPICS` | 4 | 30 KB | <0.1% | 4 | 4 | Chuyên đề tổng quan |
| *(root loose files)* | 8 | 296 KB | 0.2% | 0 | 2 | READMEs, skill, briefs, image |
| `.claude` | 1 | 1 KB | <0.1% | 0 | 0 | Settings |

---

## 3. Largest folders

**By bytes:**

| Rank | Folder | Size | Driver |
|---|---|---:|---|
| 1 | `02_EVIDENCE_BASE/RQ1_GATE1/RQ1_UPDATED_DEEP_READ_10.07` | 78.1 MiB | 16 literature PDFs; largest single file `yang2014.pdf` (15.1 MiB) |
| 2 | `06_LITERATURE_AND_ZOTERO/PERPLEXITY_PRO/References` | 32.6 MiB | 13 reference PDFs |
| 3 | `90_BACKUP/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/Perplexity_Pro/References` | 32.6 MiB | byte-identical mirror of rank 2 |
| 4 | `02_EVIDENCE_BASE/RQ2_GATES2_3` | 37.1 MiB | 12 PDFs incl. a 9.4 MiB Automation-in-Construction paper |

**By file count:**

| Rank | Folder | Files |
|---|---|---:|
| 1 | `90_BACKUP/PRE_FINAL_CLEANUP_SNAPSHOT_20260718` | 104 |
| 2 | `02_EVIDENCE_BASE` | 41 |
| 3 | `06_LITERATURE_AND_ZOTERO/PERPLEXITY_PRO` | 25 |
| 4 | `03_PAPERS/PAPER_1` | 23 |
| 5 | `90_BACKUP/BACKUP_BEFORE_WRITEBACK_20260718` | 23 |

---

## 4. Folders with the most versioning / duplication

| Folder | Files | Exact-dup | Versioned | Observation |
|---|---:|---:|---:|---|
| `90_BACKUP/PRE_FINAL_CLEANUP_SNAPSHOT_20260718` | 104 | 77 (74%) | 69 (66%) | Snapshot of a snapshot: nests a full copy of `BACKUP_BEFORE_WRITEBACK_20260718/` **and** a `Zotero MCP/` copy of the same 10-file evidence pack **and** a `Perplexity_Pro/` copy of the literature set. The same evidence pack exists three times inside this one folder. |
| `06_LITERATURE_AND_ZOTERO/PERPLEXITY_PRO` | 25 | 24 (96%) | 1 | Almost every file has a byte-identical twin in `90_BACKUP`. Highest duplication ratio in the repository. |
| `90_BACKUP/BACKUP_BEFORE_WRITEBACK_20260718` | 23 | 23 (100%) | 20 | Every file duplicated — partly against active locations, partly against its own nested re-copy. |
| `03_PAPERS/PAPER_1` | 23 | 4 | 21 (91%) | Highest *version-token density* in an active folder: `_v1` … `_v6`, plus `_Old_version (10.06)`. Two `.docx` experiment protocols dated `20260721` alongside a third dated `21.07.2026` — three near-identical names, different sizes. |
| `00_GOVERNANCE` + `01_CURRENT_CONTROL` | 30 | 2 | 21 (70%) | Low duplication, high version density: `v2.1` suffixes on 12 files, plus unsuffixed twins (`MASTER_RESEARCH_CHARTER.md` vs `..._v2.1_TRACEABILITY_CORE_20260719.md` vs `..._v2_20260719.docx`). |
| `04_PHD_SPECIAL_TOPICS/CHUYEN_DE_TONG_QUAN` | 4 | 4 (100%) | 4 | All four files also exist in `90_BACKUP/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/`. |

---

## 5. Folders with the most unclear-role files

| Folder | Unclear items | Why unclear |
|---|---|---|
| **Repository root** | 6 of 10 loose files | Three competing READMEs; `Skill.md` unversioned and carrying a superseded identifier chain; `PROMPT_CONTROL_CENTER_PROJECT_INSTRUCTIONS.md` duplicates the purpose of the folder of nearly the same name; `BIM-AEC-CLAUDE.jpg` has no referencing document |
| `05_DATA_CODE_AND_EXPERIMENTS/` | 23 of 23 | Two parallel G1 packages with overlapping registries; both describe data and code that are not present. Whether `CANONICAL_THREE_CAMPAIGN_DATASET` supersedes `THREE_CAMPAIGN_REANALYSIS`, or they are complements, is not stated in either folder |
| `90_BACKUP/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/07_FABLE_LEGACY_PACK_20260718/` | 5 | "Legacy pack" with no supersede header and no reference from any active document |
| `90_BACKUP/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/92_ARCHIVE_SUPERSEDED_FILES/` | 3 | Holds the v1.0 charter and superseded RQ matrix; governance says the archive lives at a top-level `92_ARCHIVE_MINIMAL/` that does not exist |
| Empty directories | 6 | `New folder`, `02_EVIDENCE_BASE/02.08.2026 Q2-Q3`, `03_PAPERS/PAPER_4_OPTIONAL`, `04_PHD_SPECIAL_TOPICS/CHUYEN_DE_1`, `.../CHUYEN_DE_2`, `06_LITERATURE_AND_ZOTERO/REFERENCE_EXPORTS`. Placeholders vs abandoned vs pending — not determinable from the repository |

---

## 6. Depth profile

| Depth | Directories | Files at this depth |
|---|---:|---:|
| 1 (root) | — | 8 |
| 2 | 12 | 34 |
| 3 | 25 | 122 |
| 4 | 21 | 112 |
| 5 | 3 | 25 |
| **Total** | **61** | **301** |

Maximum depth is 5, reached only inside `90_BACKUP/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/` (its `Perplexity_Pro/References/` and the two nested pack copies). The active tree never exceeds depth 4.

---

## 7. `90_BACKUP/` is not purely redundant

**63 of the 127 files in `90_BACKUP/` (spanning 41 distinct filenames) have no byte-identical twin anywhere outside `90_BACKUP/`.** They cannot be recovered from the active tree. This is the single most important reason not to treat the backup tree as disposable. Unique content includes:

- `MASTER_RESEARCH_CHARTER_v1.0_SUPERSEDED_20260717.md` and `MASTER_RESEARCH_CHARTER_v1.1_LIMITED_FEM_20260717.md` — the two legacy charters that `SOURCE_OF_TRUTH_HIERARCHY_v2.1.md` says live in the (non-existent) `99_ARCHIVE_PRE_V2_SYSTEM_20260719/LEGACY_CHARTERS/`.
- `RESEARCH_ARCHITECTURE_DECISION_RECORD_20260717.md` — the pre-v2 ADR, likewise "archived" to a folder that does not exist.
- `Literature_Review_Master_Index_Current.md` (23 KB) and `MASTER_INDEX_CURRENT_v1.1.md` — earlier master-index lineage.
- `TERMINOLOGY_CONTROL_v1.1.md`, `UNRESOLVED_ITEMS_AFTER_LIMITED_FEM_MIGRATION.md`, `Updated_RQ_Evidence_Gate_Matrix_SUPERSEDED_20260717.csv`.
- The full `07_FABLE_LEGACY_PACK_20260718/` (5 files) and `92_ARCHIVE_SUPERSEDED_FILES/` (3 files).
- `SNAPSHOT_CHECKSUM_MANIFEST_20260718.csv`, `VERIFIED_DUPLICATE_DELETION_MANIFEST_20260718.csv`, `PROJECT_FILE_MIGRATION_MANIFEST_20260718.csv`, `ZOTERO_ITEM_KEY_INVENTORY_20260718.csv`, `ZOTERO_METADATA_EXPORT_CURRENT_20260718.csv` — the provenance record of the 2026-07-18 cleanup.
- `_create_pre_final_snapshot.py`, `_generate_dry_run_inventory.py`, `_inspect_docx_versions.py` — **the only three `.py` files in the entire repository.**
- Earlier-dated variants of active files (`CLAUDE.md`, `RESEARCH_ARCHITECTURE.md`, `RESEARCH_DIRECTION_AND_SCOPE.md`, `MASTER_RESEARCH_CHARTER.md`, `CURRENT_STATUS_AND_NEXT_DIRECTION.md`, `00_README_START_HERE.md`) that differ in content from their active namesakes — these are version-series members, not copies.

---

## Claim → Evidence → Limitation → Next action

**Claim.** The repository is shallow (max depth 5) and small in file count but concentrated: 63% of its bytes are literature PDFs in `02_EVIDENCE_BASE`, and 42% of its files are backup copies. Duplication is structural rather than accidental — it comes from three nested snapshot layers inside `90_BACKUP/`, not from scattered stray copies. Version-token density is highest in `03_PAPERS/PAPER_1` and the governance folders, which is where naming ambiguity is concentrated.

**Evidence.** Recursive enumeration of 301 files and 61 directories; per-node cumulative counts, byte totals, exact-duplicate counts, and version-token counts computed from the SHA-256 table and filename tokens in `01_FULL_REPOSITORY_INVENTORY.csv`.

**Limitation.** Statistics are computed from file metadata and names only. "Dominant content" labels per folder derive from the preliminary category rule, not from reading every file. The six empty directories cannot be interpreted from the filesystem alone.

**Next action.** Use §4, §5, and §7 to prioritise reading: `03_PAPERS/PAPER_1` and the governance folders for version resolution; `05_DATA_CODE_AND_EXPERIMENTS/` for the missing-artifact question; and the 63 files in `90_BACKUP/` that have no active-location twin (41 distinct filenames, §7) before that tree is treated as redundant.
