# 03 — RESEARCH CAMPAIGN AND PHASE MAP

**Audit ID:** REPOSITORY_AUDIT_20260803 · Read-only · descriptive only

Locked research chain: `vibration data → condition/state-change evidence → BIM-linked component → inspection record → inspection–maintenance action support`. FEM: nominal, uncalibrated, reference-only, not used for damage diagnosis.

> This map records what the repository **contains** and what its own documents **say**. It does not assess whether any dataset, result, or claim is valid.

---

## 1. Master table

| Campaign / Phase | Folder | Data | Code | Registry | Reports | Current understanding | Missing / unclear items |
|---|---|---|---|---|---|---|---|
| **G1 — Three-campaign reanalysis** (Campaigns 1+2+3) | `05_DATA_CODE_AND_EXPERIMENTS/THREE_CAMPAIGN_REANALYSIS/` (14 files, 103 KB) | **None present.** Result CSVs only: `05_WITHIN_CAMPAIGN_LORO_RESULTS.csv` (39 KB), `06_CROSS_CAMPAIGN_RESULTS.csv`, `07_BASELINE_MODEL_COMPARISON.csv`, `08_PERMUTATION_RESULTS.csv`, `09_SENSOR_CONFIGURATION_RESULTS.csv`, `11_SENSITIVITY_RESULTS.csv`, `03_DATA_QUALITY_AND_PROVENANCE_LOG.csv`, 3 confusion matrices | **None present.** 8 scripts named + SHA-256 published in `01_ENVIRONMENT_PROVENANCE.md`; none in repo | **Absent.** `02_MASTER_RUN_REGISTRY.csv` (216 rows) cited as evidence but not present | `00_EXECUTIVE_REPORT.md` (20 KB), `01_ENVIRONMENT_PROVENANCE.md`, `15_NEXT_ANALYSIS_RECOMMENDATION.md`, `13_TRAINING_CURVES/README.md` | Independent pipeline built from raw data; full feature-baseline (LR/SVM/RF) matrix complete for within-campaign LORO (234 fits) and cross-campaign LOCO (27 fits); CNN complete for LOCO only, partial for LORO (Campaign 1 / S1_Ax, 4 of 6 folds). Report states explicitly: **"This document does not close Gate 1."** All figures are candidate claims | Numbering gaps 02, 04, 10, 14 = exactly the missing registry, analysis-set manifest, per-class results, and per-window predictions. Also missing: `sensor_fingerprint_check.csv`, `sensor_block_permutation_flags.csv`, `pipeline_lib.py` and 7 sibling scripts. Training curves explicitly not retained. Seeds 123 and 2026 not run |
| **G1 — Canonical dataset package** | `05_DATA_CODE_AND_EXPERIMENTS/CANONICAL_THREE_CAMPAIGN_DATASET/` (8 files, 29 KB) | **None present.** Documentation states 216 NPZ layers + 3 analysis sets live in `CANONICAL_THREE_CAMPAIGN_DATASET.zip`, delivered via chat file cards — zip not in repo | **None present.** 12 scripts named + SHA-256 in `10_REPRODUCIBILITY_MANIFEST.md` | **Absent.** `06_MASTER_RUN_REGISTRY.csv`, `02_PHYSICAL_SENSOR_MAPPING_REGISTRY.csv`, `04_CHANNEL_QUALITY_REGISTRY.csv`, `05_EXCLUSION_AND_WARNING_REGISTRY.csv`, `01_RAW_FILE_INVENTORY.csv`, fold manifests — all named, none present | `00_README.md`, `03_CHANNEL_QUALITY_RULES.md`, `07_DATA_DICTIONARY.md`, `08_DATASET_VARIANTS.md`, `09_DATASET_VALIDATION_REPORT.md`, `10_REPRODUCIBILITY_MANIFEST.md`, `11_DATASET_HANDOFF_FOR_IT.md`, `08_AUTOMATED_VALIDATION_RESULTS.csv` | Later, cleaner re-derivation: corrects physical-sensor identity via gravity-fingerprint clustering rather than column position; adds channel-quality taxonomy, two data layers, three analysis sets, leakage-safe fold manifests, 12 passing automated tests. States **no model trained, no accuracy computed, not a Gate 1 closure** | Relationship to `THREE_CAMPAIGN_REANALYSIS` is **not stated in either folder** — supersession vs complement is unresolved. `canon_lib.py` hard-codes a session sandbox path (`/sessions/…/DATA_ALL_3_CAMPAIGN`), disclosed as requiring manual edit to reproduce elsewhere |
| **Campaign 1** (25.04.2026) | referenced as `Campaign1_25.04.2026/` | **Not in repo** (72 CSVs stated) | — | — | Described in `00_EXECUTIVE_REPORT.md` §1 | 72 recordings; Ax-only in the core set; 36/72 files carry dead-channel flags (`S1_Ay` in 19, `S2_Ay` in 17) | **Sensor column position unstable** — bimodal gravity fingerprint on both S1 and S2; `Sensor_Mapping_Status = SENSOR_SET_CONFIRMED_COLUMN_POSITION_UNSTABLE`. Single/paired-sensor results must be read as "column position", not physical sensor identity |
| **Campaign 2** (22.07.2026) | referenced as `Campaign2_22.07.2026/` | **Not in repo** (72 CSVs stated) | — | — | Described in `00_EXECUTIVE_REPORT.md` §1 | 72 recordings; S1/S2/S3 × Ax/Ay/Az; 12/72 dead-channel flags (Ax only) | **3-modal fingerprint on all three column positions** — same instability, worse. One file `BS1B1L1R12.csv` lacks the date prefix its 71 siblings carry → flagged `PROVENANCE_WARNING`, deliberately not auto-excluded |
| **Campaign 3** (29.07.2026) | referenced as `Campaign3_29.07.2026/` | **Not in repo** (72 CSVs stated) | — | — | Described in `00_EXECUTIVE_REPORT.md` §1; `Checklist_Campaign_3_Gate1.docx` (37 KB) present at `05_DATA_CODE_AND_EXPERIMENTS/` root | 72 recordings; **column position is a reliable physical-sensor proxy here** — the only clean campaign; 14/72 dead-channel flags (`S3_Ax`) | Within-campaign RF macro-F1 varies 0.218–0.954 (std 0.184) — flagged as needing per-run/per-state breakdown before any fold is treated as representative |
| **Experiment protocol / run design (VI)** | `03_PAPERS/PAPER_1/` | — | — | — | `KICH_BAN_THI_NGHIEM_PAPER1_VA_TIEN_KIEM_CHUNG_CAM_BIEN_CO_DAY_20260721.docx` (53 KB), `KICH_BAN_THI_NGHIEM_RUT_GON_20260721.docx` (43 KB), `Kich_ban_thi_nghiem_21.07.2026.docx` (20 KB) | Three Vietnamese experiment-scenario documents, all dated 21/07/2026, three different sizes | Three near-identical names, no `_FINAL`/`_CURRENT` marker, no README stating which governs. **`.docx` content not read in this audit** |
| **PASCO sensors** | — | — | — | — | `03_PAPERS/Yêu cầu phân tích PASCO–ADXL cho Paper S1.docx` (12 KB) | Raw recordings described as "216 raw PASCO CSV recordings" in `CANONICAL_.../00_README.md` | The only PASCO/ADXL-specific document sits loose at `03_PAPERS/` root, not inside any paper folder. Refers to a "Paper S1" that has no folder |
| **ADXL / custom sensor** | — | — | — | — | same file as above | Named only in that one filename | No ADXL dataset, comparison, or report present. Whether the simultaneous PASCO/ADXL comparison was executed is not determinable from this repository |
| **Baseline ML (LR / SVM / RF)** | `THREE_CAMPAIGN_REANALYSIS/` | — | — | — | `07_BASELINE_MODEL_COMPARISON.csv` (5 KB) | Complete across both matrices, single seed 42, no tuning, fixed 9-feature set per channel | — |
| **1D-CNN** | `THREE_CAMPAIGN_REANALYSIS/` | — | — | — | rows inside `05_…LORO_RESULTS.csv` / `06_CROSS_CAMPAIGN_RESULTS.csv` | TensorFlow/Keras 2.21.0 CPU; complete for cross-campaign LOCO (9/9), partial for LORO | Several folds stopped at epoch ~11 with macro-F1 ≈ 0.10 (near single-class collapse); `patience=10` ablation recommended but not run |
| **ResNet1D** | — | — | — | — | referenced in `PAPER1_INTERNAL_PRELIMINARY_EVIDENCE_NOTE_v3.md`, `PAPER1_Q2_INTEGRATED_OUTLINE_…_v4`, `PROMPT_CLAUDE_COWORK_PAPER1_EMPTY_RESULTS_v3.md` | **No ResNet1D result file present.** Source document `BAO_CAO_RESNET1D.docx` referenced 3× — **not in repo** | Blocking tracker item #2: "sensor mode & provenance not confirmed"; no ResNet1D number may enter Paper 1 until resolved | Both the report and its provenance audit (`RESNET1D_PROVENANCE_v1.md`, `RESNET1D_PROVENANCE_AUDIT.md`) are absent |
| **LORO (leave-one-run-out)** | `THREE_CAMPAIGN_REANALYSIS/` | — | — | — | `05_WITHIN_CAMPAIGN_LORO_RESULTS.csv` | Feature-baseline LORO matrix complete: 13 sensor configs × 6 folds × 3 models | `CURRENT_STATUS_AND_NEXT_DIRECTION.md` and `UNRESOLVED_ITEMS_TRACKER_v2.1.md` (item #1, #3) still state **"LORO chưa chạy"** (LORO not yet run). Whether the reanalysis satisfies that item, or whether the item predates it, is **unresolved** — a governance/evidence timing conflict worth explicit review |
| **LOCO (leave-one-campaign-out)** | `THREE_CAMPAIGN_REANALYSIS/` | — | — | — | `06_CROSS_CAMPAIGN_RESULTS.csv` | 3 configs × 3 folds × 3 models complete + full CNN matrix | — |
| **Permutation tests** | `THREE_CAMPAIGN_REANALYSIS/` | — | — | — | `08_PERMUTATION_RESULTS.csv` (16 KB) | Three independent 100-permutation negative controls | — |
| **Run registry / manifest / corrected mapping** | — | — | — | **Absent** | — | `RUN_REGISTRY_LOCKED.csv` referenced by 6 active documents incl. `EVIDENCE_GATES_v2.1.md`; `DATASET_FILE_MANIFEST.csv` by 5 | **This is blocking item #1 for Gate 1 and it does not exist in the repository.** Corrected sensor mapping exists only as a *described* registry inside the undelivered zip |

---

## 2. G2–G3 / RQ2 / WP2 — traceability, schema, competency questions

| Element | Present? | Location / evidence |
|---|---|---|
| Traceability evidence addendum | **Yes** | `02_EVIDENCE_BASE/RQ2_GATES2_3/04_RQ2_TRACEABILITY_EVIDENCE_ADDENDUM_v1.2_20260718.md` (4 KB) |
| Closest-competitor matrix (Paper 2) | **Yes** | `02_EVIDENCE_BASE/RQ2_GATES2_3/07_CLOSEST_COMPETITOR_MATRIX_PAPER2_20260718.csv` (1.4 KB) |
| Paper 2 planning / direction | **Yes** | `03_PAPERS/PAPER_2/PAPER2_DIRECTION_AND_GATE_v2.1_20260719.md` — the *only* file in `PAPER_2/`. Defines CEI metadata, accountability, Action_Record schema intent, RCQ, legal mapping |
| Zotero deep-read (G2–G3) | **Yes** | `02_EVIDENCE_BASE/RQ2_GATES2_3/DEEP_READ_20.07.2026/` — 5 PDFs (Antunes 2024 ontology-based BIM-AMS; Çelik 2023 BIM data provenance; Lee 2021 provenance & accountability; Johannes 2021 smart-maintenance maturity; kim2018) + 5 further PDFs at folder root |
| Competency questions (SCQ / VCQ / RCQ) | **No** | Named in Charter v2.1, `PAPER2_DIRECTION…`, tracker item #5. `G2_COMPETENCY_QUESTION_REGISTER_v0.1.md` referenced by README v2.2 — **not in repo**. Tracker: "chưa pre-register/duyệt" |
| Formal schema | **No** | `RQ2_ENTITY_RELATIONSHIP_MODEL_v0.1.md`, `CONTEXT_MAPPING_RULES_v0.1.md`, `IDENTIFIER_AND_SENSOR_ASSIGNMENT_SCHEMA_v0.1.csv`, `CEI_METADATA_DICTIONARY_v0.1.csv`, `INSPECTION_RECORD_SCHEMA_v0.1.csv`, `ACTION_RECORD_ACCOUNTABILITY_SCHEMA_v0.1.csv` — all referenced by `00_README_START_HERE_v2.2_UPDATED_20260720.md`, **none present** |
| `Condition_Evidence` / `Inspection_Record` / `Action_Record` / `Status_Event` | **Concept only** | Defined narratively in Charter v2.1, README v2.2 §2.2, `PAPER2_DIRECTION…`. No schema file, no fixture, no instance data. Tracker items #9, #15, #16 open |
| `BIM_GUID` / `Asset_ID` | **Concept only** | Identifier chain stated in governance. No BIM model, IFC file, or asset register in the repository |
| SHACL / SQL / JSON validation | **No** | No `.ttl`, `.shacl`, `.sql`, or schema `.json` anywhere. The single `.json` file is `.claude/settings.local.json` |
| Demo / prototype | **No** | Only a request document: `YEU_CAU_CAP_NHAT_WEBSITE_BIM_VIEWER_DIGITAL_TWIN_DEMO_20260727.md` (12 KB, root) |
| Test fixtures | **No** | None |
| G2/G3 acceptance criteria | **No** | `G2_ACCEPTANCE_CRITERIA_v0.1.md` referenced by README v2.2 — not present |

**Summary.** G2–G3 exists as *literature evidence plus direction documents*. The eight `v0.1` schema and CQ artifacts that README v2.2 announces as the G2 work package are all absent. Gate 2 is pre-artifact.

---

## 3. RQ3 / G4–G5 — field feasibility and decision support

| Element | Present? | Location / evidence |
|---|---|---|
| RQ3 evidence addendum | **Yes** | `02_EVIDENCE_BASE/RQ3_GATE4/05_RQ3_FIELD_FEASIBILITY_EVIDENCE_ADDENDUM_v1.0_20260718.md` (4 KB) — the only file in that folder |
| WP4 evidence addendum | **Yes** | `02_EVIDENCE_BASE/WP4_GATE5/06_WP4_DECISION_SUPPORT_EVIDENCE_ADDENDUM_v1.0_20260718.md` (3 KB) — the only file in that folder |
| Paper 3 direction | **Yes** | `03_PAPERS/PAPER_3/PAPER3_FIELD_FEASIBILITY_DIRECTION_v2.1_20260719.md` — the only file in `PAPER_3/` |
| Field literature | **Yes** | `06_LITERATURE_AND_ZOTERO/PERPLEXITY_PRO/7. Peer-Reviewed Field Studies — Vibration Monitoring, Operational Baselines, and Low-Cost Sensor Deployment in Steel Structures.md` (21 KB) + `References/Gate 4*.pdf` (5 PDFs) |
| **Field access agreement (Rapexco)** | **No** | Named in `UNRESOLVED_ITEMS_TRACKER_v2.1.md` item #7 as a **hard prerequisite for G4**, status "chưa xác nhận ký" (signature not confirmed). No agreement document, correspondence, or site record in the repository |
| Real structure / case data | **No** | `CURRENT_STATUS_AND_NEXT_DIRECTION.md` §1 states a BIM model exists for a real 25×80 m steel-frame warehouse, plus asset register and shop drawings. **None of these are in this repository** |
| BIM / IFC model | **No** | No `.ifc`, `.rvt`, `.nwd`, `.bcf` file anywhere |
| Asset register | **No** | None |
| Sensor_ID ↔ BIM_GUID mapping | **No** | Protocol described in Charter §6.1 as field-prep work permitted to run early; no mapping file present |
| Operational baseline | **No** | None |
| Field data | **No** | None |
| Inspection workflow / decision-support scenarios | **No** | "2–3 scenarios" listed as field-prep deliverables in `CURRENT_STATUS_AND_NEXT_DIRECTION.md` §5.4; not present |
| Paper 4 | **Empty folder** | `03_PAPERS/PAPER_4_OPTIONAL/` contains no files |

**Summary.** RQ3/G4–G5 is at direction-and-literature stage only. Two 3–4 KB addenda and two direction notes constitute the entire strand. Every field artifact named by the governance documents is outside this repository or not yet created.

---

## 4. Sub-topics and side threads

| Thread | Folder | Files | Status |
|---|---|---:|---|
| **Chuyên đề tổng quan** (comprehensive review topic) | `04_PHD_SPECIAL_TOPICS/CHUYEN_DE_TONG_QUAN/` | 4 | Complete small package: detailed outline, RQ–WP–Paper–Gate matrix, evidence-gap note, evidence matrix CSV. All four also exist byte-identically in `90_BACKUP/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/` |
| **Chuyên đề 1 / Chuyên đề 2** | `04_PHD_SPECIAL_TOPICS/CHUYEN_DE_1/`, `CHUYEN_DE_2/` | 0 | **Both empty.** Placeholders |
| **Zotero audit & writeback** | `02_EVIDENCE_BASE/ZOTERO_AUDIT/` | 5 | Deep-read evidence matrix (19 KB CSV), duplicate/metadata correction log, completion report, writeback queue (15 KB), phase-0 safety/dry-run report. Tracker item #14: **writeback pending, Zotero must not be modified without user approval** |
| **Perplexity Pro discovery** | `06_LITERATURE_AND_ZOTERO/PERPLEXITY_PRO/` | 25 | 10 numbered query outputs + 13 reference PDFs + README. Governance ranks this tier 8 — **not citable as evidence** |
| **Zotero MCP** | `06_LITERATURE_AND_ZOTERO/ZOTERO_MCP/` | 1 | README only (215 bytes). The 10-file evidence pack that once lived here now exists only in `90_BACKUP/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/Zotero MCP/` |
| **NotebookLM brief** | root | 1 | `NOTEBOOKLM_BRIEF_G1_PAPER1_VS_AVCI_2021.md` (28 KB) — G1 positioning against Avci et al. 2021 |
| **BIM viewer / Digital Twin demo request** | root | 1 | `YEU_CAU_CAP_NHAT_WEBSITE_BIM_VIEWER_DIGITAL_TWIN_DEMO_20260727.md` (12 KB). Nearest thing to a G2/G3 demo artifact; it is a request, not a deliverable |
| **Prompt tooling** | `07_PROMPTS_AND_HANDOFFS/` + `PROMPT_CONTROL_CENTER_PROJECT/` + root `Skill.md`, `PROMPT_CONTROL_CENTER_PROJECT_INSTRUCTIONS.md` | 17 | Two skills (`phd-prompt-compressor`, `phd-prompt-router`) sharing a byte-identical `references/phd-scope.md`; a 7-file prompt-control-centre folder; a near-duplicate standalone instructions file at root; and `Skill.md`. See report 08 |
| **Repository cleanup 2026-07-18** | `01_CURRENT_CONTROL/PROJECT_CLEANUP_20260718/` + `90_BACKUP/` | 6 + 127 | A prior full cleanup with inventory, migration manifest, deletion manifest, broken-link audit, and two backup snapshots. The current audit is effectively the second such pass |

---

## 5. Cross-cutting observations

1. **Documentation outruns artifacts.** Every strand has direction documents and evidence addenda; only G1 has result files, and even G1 lacks its data, code, and registry.
2. **Two G1 packages, no stated relationship.** `THREE_CAMPAIGN_REANALYSIS` (analysis, has results) and `CANONICAL_THREE_CAMPAIGN_DATASET` (dataset prep, explicitly no results) were produced by different passes. The canonical package's fingerprint-based sensor correction appears to *answer* the reanalysis package's #1 open item — but neither folder says so.
3. **A possible timing conflict on LORO.** Control documents dated 2026-07-19 state LORO has not been run; the reanalysis package (undated in-folder, files modified 2026-07-29) contains a completed LORO matrix. Either the tracker is stale or the reanalysis does not satisfy the tracker's definition. **Not resolved here.**
4. **The `02.08.2026 Q2-Q3` empty folder** under `02_EVIDENCE_BASE/` is dated one day before this audit and suggests a just-started, not-yet-populated work phase.

---

## Claim → Evidence → Limitation → Next action

**Claim.** G1 is the only strand with produced results, and those results are documented but not reproducible from this repository: raw data (216 CSVs across three campaigns), all 20 pipeline scripts, and every run/mapping registry are absent. G2–G3 exists as literature plus direction documents with zero schema or CQ artifacts. G4–G5 exists as two short addenda plus two direction notes, with no field agreement, BIM model, asset register, or field data present.

**Evidence.** Full file enumeration of `05_DATA_CODE_AND_EXPERIMENTS/` (23 files, no `.py`, no `.npz`, no campaign CSV); direct reading of `THREE_CAMPAIGN_REANALYSIS/00_EXECUTIVE_REPORT.md`, `01_ENVIRONMENT_PROVENANCE.md`, `15_NEXT_ANALYSIS_RECOMMENDATION.md`, `13_TRAINING_CURVES/README.md`, `CANONICAL_THREE_CAMPAIGN_DATASET/00_README.md` and `10_REPRODUCIBILITY_MANIFEST.md`; cross-check of 119 backtick-quoted artifact references against the 301-file table; direct reading of `UNRESOLVED_ITEMS_TRACKER_v2.1.md` and `CURRENT_STATUS_AND_NEXT_DIRECTION.md`.

**Limitation.** `Evidence is currently insufficient` to determine (a) whether the missing G1 data and code exist outside this repository root, (b) whether `CANONICAL_THREE_CAMPAIGN_DATASET` supersedes `THREE_CAMPAIGN_REANALYSIS`, and (c) whether the completed LORO matrix satisfies blocking tracker item #1. The 13 `.docx` files — including the three Vietnamese experiment protocols and `Checklist_Campaign_3_Gate1.docx` — were inventoried and hashed but **not read**; campaign metadata that may be recorded only in those files is therefore not reflected here. No judgement is offered on the validity of any dataset or result.

**Next action.** Ask the user for the location of `DATA_ALL_3_CAMPAIGN/` (or the three campaign folders) and of `CANONICAL_THREE_CAMPAIGN_DATASET.zip`; establish the intended relationship between the two G1 packages; and reconcile the LORO status between the 2026-07-19 trackers and the 2026-07-29 reanalysis outputs. Read the four `.docx` files in `03_PAPERS/PAPER_1/` and `05_DATA_CODE_AND_EXPERIMENTS/` before treating the campaign record as complete.
