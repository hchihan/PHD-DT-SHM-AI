# 08 — LOOSE ROOT ITEMS REPORT

**Audit ID:** REPOSITORY_AUDIT_20260803 · Read-only · **description only, no move proposed**

The repository root holds **8 loose files** and **13 folders**, of which 2 folders sit outside the numbered `00_`–`90_` scheme. Everything at root is listed below.

---

## 1. Loose files at root

| # | File | Size | Modified | Apparent role | Status / observation |
|---|---|---:|---|---|---|
| 1 | `00_README_START_HERE.md` | 3,397 B | 2026-07-19 | Entry point / reading order | **One of three competing READMEs.** Named as CURRENT by `V2.1_CORE_EVIDENCE_INDEX.md` and by `SOURCE_OF_TRUTH_HIERARCHY_v2.1.md` §1 item 5. Shortest of the three. Points to `99_ARCHIVE_PRE_V2_SYSTEM_20260719/` and `ARCHIVE_MANIFEST.md`, **neither of which exists** |
| 2 | `00_README_START_HERE_v2.1_UPDATED_20260719.md` | 5,865 B | 2026-07-19 | Entry point, v2.1 | **Referenced by no other file in the repository.** Same date as #1, 73% larger. Relationship to #1 undocumented — expansion, draft, or superseded twin is not determinable |
| 3 | `00_README_START_HERE_v2.2_UPDATED_20260720.md` | 14,309 B | 2026-07-20 | Entry point, **v2.2** | **Newest and most detailed (4× #1).** Self-declares "Phiên bản vận hành: v2.2" and states the governance set is not yet synchronised to v2.2. Announces eight `v0.1` G2 schema/CQ artifacts, **none of which exist**. Not mentioned by the v2.1 index or hierarchy — **but is cited as a priority internal source by `NOTEBOOKLM_BRIEF_…` (27/07)**, i.e. later work treats it as operative |
| 4 | `Skill.md` | 6,487 B | 2026-07-28 | PhD prompt-architect skill definition | **Highest-priority conflict in the repository.** Unversioned, no supersede header, at root rather than in `07_PROMPTS_AND_HANDOFFS/`. Modified 9 days after the v2.1 governance set, yet §2 states the identifier chain as `… → Inspection_Record_ID → **Action_Status**` and `FEM_Node_ID chỉ là metadata tùy chọn` — the **pre-v2.1** model. Charter v2.1 and README v2.2 both use `→ Action_Record_ID` with `Action_Status` as an attribute. Because this file generates prompts for other models, the stale chain propagates downstream. See `07_LEGACY_DIRECTION_SCAN.md` §2 |
| 5 | `PROMPT_CONTROL_CENTER_PROJECT_INSTRUCTIONS.md` | 10,377 B | 2026-07-28 | Prompt-control-centre project instructions | **Near-duplicate purpose with `PROMPT_CONTROL_CENTER_PROJECT/00_PROJECT_INSTRUCTIONS.md`** (4,077 B, same folder name minus the suffix). Not byte-identical — this root file is 2.5× larger and differently structured ("HƯỚNG DẪN DỰ ÁN" vs "PROJECT INSTRUCTIONS"), so it is a **VERSION_SERIES / POSSIBLE_SUPERSEDED** pair, not a copy. Which one governs the project is not stated in either |
| 6 | `NOTEBOOKLM_BRIEF_G1_PAPER1_VS_AVCI_2021.md` | 28,206 B | 2026-07-27 | Self-contained brief for NotebookLM to compare Paper 1 / G1 against Avci et al. 2021 | **Largest loose root file.** Legitimate, current, well-scoped G1 work product. Belongs conceptually with `03_PAPERS/PAPER_1/` or `07_PROMPTS_AND_HANDOFFS/`. References `CAMPAIGN_AND_SENSOR_PAIR_REPORT.md` — **not in the repository** — and names README v2.2 as a priority source |
| 7 | `YEU_CAU_CAP_NHAT_WEBSITE_BIM_VIEWER_DIGITAL_TWIN_DEMO_20260727.md` | 11,905 B | 2026-07-27 | IT request: convert `bim.aac79.com.vn` from a commercial SaaS BIM/IFC viewer landing page to an academic Digital Twin demo | **The only demo/prototype-related artifact in the repository**, and it is a request, not a deliverable. Explicitly written to enforce Charter scope on the website (remove pricing tiers, login, commercial framing; keep the 3D/IFC viewer core; add the traceability chain). Correctly aligned with current direction. No corresponding IT-handoff folder exists at root level; `03_PAPERS/PAPER_1/IT_REQUESTS/` exists but is Paper-1 scoped |
| 8 | `BIM-AEC-CLAUDE.jpg` | 228,069 B | 2026-07-31 | Image | **Role unknown.** Newest file in the repository apart from `.claude/settings.local.json`. Not referenced by any document. No caption, figure number, or accompanying note. Only image file in the repository |

---

## 2. Folders at root

| # | Folder | Files | Size | Role | Observation |
|---|---|---:|---:|---|---|
| 1 | `.claude/` | 1 | 719 B | Claude Code tool-permission settings | `settings.local.json`, modified 2026-08-03 (today). Infrastructure, not research content |
| 2 | `00_GOVERNANCE/` | 15 | 139 KB | Charter, gates, ADR, terminology, agent rules | Numbered scheme, clear role |
| 3 | `01_CURRENT_CONTROL/` | 15 | 120 KB | Status, trackers, cleanup logs | Numbered scheme, clear role |
| 4 | `02_EVIDENCE_BASE/` | 41 | 115.3 MiB | Evidence addenda + literature PDFs by RQ/Gate | Contains one **empty** dated subfolder, `02.08.2026 Q2-Q3` |
| 5 | `03_PAPERS/` | 26 | 801 KB | Paper 1–4 packages | `PAPER_4_OPTIONAL/` **empty**. One file sits loose at `03_PAPERS/` root: `Yêu cầu phân tích PASCO–ADXL cho Paper S1.docx` — refers to a "Paper S1" with no folder |
| 6 | `04_PHD_SPECIAL_TOPICS/` | 4 | 30 KB | Chuyên đề | `CHUYEN_DE_1/` and `CHUYEN_DE_2/` both **empty** |
| 7 | `05_DATA_CODE_AND_EXPERIMENTS/` | 23 | 169 KB | G1 data/code/experiments | Contains no data and no code — see `03_RESEARCH_CAMPAIGN_AND_PHASE_MAP.md`. One file loose at folder root: `Checklist_Campaign_3_Gate1.docx` |
| 8 | `06_LITERATURE_AND_ZOTERO/` | 26 | 32.7 MiB | Discovery + Zotero | `REFERENCE_EXPORTS/` **empty**; `ZOTERO_MCP/` holds only a 215-byte README |
| 9 | `07_PROMPTS_AND_HANDOFFS/` | 8 | 54 KB | Prompts, OpenCode handoffs, 2 skills | Two skills share a byte-identical `references/phd-scope.md`. `Skill.md` at root is **not** here |
| 10 | `90_BACKUP/` | 127 | 33.9 MiB | Two 2026-07-18 snapshots | 42% of all files. 63 files have no active-location twin |
| 11 | `99_REPOSITORY_LOGS/` | 12 | — | **Created by this audit** | Contains only `REPOSITORY_AUDIT_20260803/` |
| 12 | `New folder` | 0 | 0 B | — | **Empty, default Windows name, created 2026-07-28.** Same date as `Skill.md` and `PROMPT_CONTROL_CENTER_PROJECT_INSTRUCTIONS.md`, suggesting an abandoned action during that session |
| 13 | `PROMPT_CONTROL_CENTER_PROJECT/` | 7 | 11 KB | Prompt-control-centre package | Outside the numbered scheme. Contents: `00_PROJECT_INSTRUCTIONS.md`, `01_PROMPT_REQUEST_TEMPLATE.md`, `02_PROMPT_CATALOG.md`, `03_MODEL_ROUTING_GUIDE.md`, `04_PROMPT_QUALITY_CHECKLIST.md`, `05_DOMAIN_PROFILE_PHD.md`, `README.md`. Overlaps in purpose with root file #5, with root `Skill.md`, and with `07_PROMPTS_AND_HANDOFFS/phd-prompt-router|compressor/` |

---

## 3. The prompt-tooling cluster — four overlapping locations

The single most tangled area at root level. Four distinct locations hold prompt-architecture material with overlapping scope:

| Location | Files | Purpose as stated in the files |
|---|---:|---|
| `Skill.md` (root) | 1 | "SKILL — PHD PROMPT ARCHITECT": turns a short user request into one prompt targeted at the right model and Evidence Gate. Contains a mode→RQ/WP/Gate map and a fixed scope statement |
| `PROMPT_CONTROL_CENTER_PROJECT_INSTRUCTIONS.md` (root) | 1 | "HƯỚNG DẪN DỰ ÁN — PROMPT CONTROL CENTER": prompt creation, compression, checking, and management across models; separates PhD context from other work |
| `PROMPT_CONTROL_CENTER_PROJECT/` | 7 | "PROJECT INSTRUCTIONS — PROMPT CONTROL CENTER" + request template, catalog, model-routing guide, quality checklist, PhD domain profile |
| `07_PROMPTS_AND_HANDOFFS/phd-prompt-router/` + `phd-prompt-compressor/` | 5 | Two packaged skills (`SKILL.md` + `references/`), sharing a **byte-identical** `references/phd-scope.md` (1,811 B) |

All four define overlapping responsibilities (routing to the right model, compressing prompts, holding PhD scope). No file states the relationship between them. Three of the four contain their own copy of the PhD scope statement, and — as noted in §1 #4 — the copy in `Skill.md` is the one carrying the superseded identifier chain.

---

## 4. Empty directories

| Directory | Created | Interpretation |
|---|---|---|
| `New folder` | 2026-07-28 | Accidental / abandoned. Default Windows name |
| `02_EVIDENCE_BASE/02.08.2026 Q2-Q3` | 2026-08-02 | Dated one day before this audit — a work phase just opened but not populated. Space in the name and a date-first format inconsistent with the repository's `YYYYMMDD` convention |
| `03_PAPERS/PAPER_4_OPTIONAL/` | 2026-07-18 | Deliberate placeholder — Paper 4 is described as optional/bonus in the gate matrix |
| `04_PHD_SPECIAL_TOPICS/CHUYEN_DE_1/` | 2026-07-18 | Deliberate placeholder |
| `04_PHD_SPECIAL_TOPICS/CHUYEN_DE_2/` | 2026-07-18 | Deliberate placeholder |
| `06_LITERATURE_AND_ZOTERO/REFERENCE_EXPORTS/` | 2026-07-18 | Deliberate placeholder — Zotero exports expected but not yet produced |

Four of the six are consistent with intentional placeholders created during the 2026-07-18 restructure. Two (`New folder`, `02.08.2026 Q2-Q3`) are recent and unexplained.

---

## 5. Naming-convention deviations at root

| Item | Convention in this repository | Deviation |
|---|---|---|
| `New folder` | `NN_UPPER_SNAKE_CASE` | Default Windows name |
| `PROMPT_CONTROL_CENTER_PROJECT/` | numbered `NN_` prefix | No number prefix |
| `Skill.md` | `UPPER_SNAKE_CASE.md` for governance | Mixed case, no version, no date |
| `BIM-AEC-CLAUDE.jpg` | underscores | Hyphens |
| `02_EVIDENCE_BASE/02.08.2026 Q2-Q3` | `YYYYMMDD` suffix | `DD.MM.YYYY` prefix + space in name |
| `03_PAPERS/Yêu cầu phân tích PASCO–ADXL cho Paper S1.docx` | ASCII, no spaces | Vietnamese diacritics, spaces, en-dash |

These are observations, not defects. Vietnamese filenames are used throughout `03_PAPERS/` and `02_EVIDENCE_BASE/RQ2_GATES2_3/DEEP_READ_20.07.2026/` and all read correctly — no encoding damage was found in any filename.

---

## Claim → Evidence → Limitation → Next action

**Claim.** The repository root holds 8 loose files and 13 folders. Six of the eight loose files have a clear and current purpose; two carry unresolved problems — `Skill.md` (superseded identifier chain, no version marker) and the three-way README split. A fourth-order problem is the prompt-tooling cluster, which is spread across four locations with overlapping scope and three separate copies of the PhD scope statement. Two empty directories (`New folder`, `02.08.2026 Q2-Q3`) are recent and unexplained; four others are consistent with deliberate placeholders from the 2026-07-18 restructure.

**Evidence.** Full root enumeration with size, creation, and modification timestamps; direct reading of all 8 loose root files plus `PROMPT_CONTROL_CENTER_PROJECT/00_PROJECT_INSTRUCTIONS.md` and `README.md`; SHA-256 comparison establishing that root file #5 and the folder's `00_PROJECT_INSTRUCTIONS.md` are **not** byte-identical; existence check confirming `99_ARCHIVE_PRE_V2_SYSTEM_20260719/`, `ARCHIVE_MANIFEST.md`, `CAMPAIGN_AND_SENSOR_PAIR_REPORT.md`, and the eight README-v2.2 `v0.1` artifacts are absent.

**Limitation.** `BIM-AEC-CLAUDE.jpg` was **not opened**; its role is inferred solely from the absence of any referencing document. The relationship between the three READMEs, and between root file #5 and the `PROMPT_CONTROL_CENTER_PROJECT/` folder, is not stated anywhere in the repository and cannot be resolved from file metadata. Creation timestamps on a Google Drive mount may reflect sync time rather than authoring time. **No move, rename, or consolidation is proposed by this report.**

**Next action.** The user answers four questions: (1) which README is current, and what happens to the other two; (2) is `Skill.md` current, superseded, or in need of a chain update to `Action_Record_ID`; (3) which of the four prompt-tooling locations is authoritative; (4) what is `BIM-AEC-CLAUDE.jpg` and should `New folder` and `02.08.2026 Q2-Q3` be kept. Only after those answers should any root reorganisation be designed.
