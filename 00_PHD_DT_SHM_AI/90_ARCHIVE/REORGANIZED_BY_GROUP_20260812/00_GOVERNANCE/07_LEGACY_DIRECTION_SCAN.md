# 07 — LEGACY DIRECTION SCAN

**Audit ID:** REPOSITORY_AUDIT_20260803 · Read-only · **report only, no action taken**

**Method.** Full-text regex scan of all 232 locally readable text files (`.md`, `.csv`, `.txt`, `.json`, `.py`) for 14 legacy-direction keyword families, plus filename matching on all 301 files. 516 keyword occurrences were found across **129 files** (57 of them in active, non-backup locations).

> **Critical methodological caveat.** The current architecture defines itself largely by *exclusion*. Charter v2.1, `TERMINOLOGY_CONTROL_CURRENT.md`, `AGENT_RULES.md`, and the READMEs must **name** calibrated FEM, EMA, MAC, RUL, predictive maintenance, Health Index, and autonomous maintenance in order to prohibit them. **278 of 516 occurrences (54%) sit inside an explicit negation or prohibition phrase** ("không mở rộng sang…", "REMOVE from claims", "**Prohibited:**", "out of scope", "Excluded alternatives:"). Treating keyword presence as evidence of legacy direction would produce a majority-false-positive list. This report separates the two.

---

## 1. Keyword frequency

| Keyword family | Occurrences | Files | Predominant context |
|---|---:|---:|---|
| digital twin (broad) | 78 | 56 | **Current thesis subject** — "data-informed Digital Twin". Not a legacy term; scanned for completeness |
| RUL | 64 | 41 | Exclusion lists |
| Health Index | 62 | 40 | Exclusion lists ("weighted/complex Health Index") |
| predictive maintenance | 54 | 38 | Exclusion lists |
| calibrated FEM | 45 | 30 | Exclusion lists + Council review discussion |
| FEM_Node_ID | 43 | 24 | Mixed — see §3 |
| field damage diagnosis | 41 | 31 | Exclusion lists |
| autonomous maintenance | 37 | 27 | Exclusion lists |
| MAC | 24 | 17 | Council review + literature descriptions |
| stiffness degradation | 22 | 16 | Exclusion lists |
| EMA | 19 | 14 | Council review + post-PhD extension sections |
| FEM-core | 12 | 9 | Migration/cleanup notes referring to the abandoned architecture |
| equivalent stiffness | 11 | 9 | Terminology-control removal rules |
| commercial platform | 4 | 4 | Exclusion lists |

---

## 2. Findings table — items that warrant a read

Only files where a keyword appears **outside** a prohibition/exclusion frame, or where the file's own status is ambiguous.

| File | Keyword / direction | Context | Appears historical / active / unclear | Review priority |
|---|---|---|---|---|
| `Skill.md` (root) | `FEM_Node_ID`; identifier chain ending in `Action_Status` | §2 "Phạm vi nghiên cứu cố định" states the chain as `Sensor_ID → BIM_GUID → Condition_Evidence_ID → Inspection_Record_ID → Action_Status` and `FEM_Node_ID chỉ là metadata tùy chọn`. Charter v2.1 (19/07) and README v2.2 (20/07) replaced this with `→ Action_Record_ID`, `Action_Status` demoted to an attribute. File modified **2026-07-28** — after both | **ACTIVE — and carrying a superseded chain.** No version suffix, no supersede header. Its output is prompts for other models, so the stale chain propagates | **P1 — highest** |
| `00_GOVERNANCE/THE_COUNCIL_REVIEW_FEM_OR_NO_FEM_17.07.2026.md` | calibrated FEM, EMA, MAC, similitude, stiffness, `FEM_Node_ID` | 35 KB deliberation on whether to keep FEM at the core; concludes Verdict B (drop it). Records the chain as ending in `Action_Status` (correct for its 17/07 date). Also states "Chuỗi định danh lõi bỏ FEM_Node_ID" | **HISTORICAL by content, but ranked #1 in the source-of-truth hierarchy** — a decision record, above the Charter. Its FEM discussion is the *record of rejecting* FEM, not guidance to use it | **P2** — confirm its rank-1 status is intended to cover the decision only, not its technical content |
| `02_EVIDENCE_BASE/CURRENT/LIVING_EVIDENCE_BASE_v1.1_LIMITED_FEM.md` | `FEM_Node_ID`, MAC | States "chain: … → Inspection_Record_ID → Action_Status. FEM_Node_ID = optional metadata only". Lists MAC/frequency-matching sources as SUPPORTING_REFERENCE | **HISTORICAL — correctly labelled.** `LIVING_EVIDENCE_BASE_CURRENT.md` explicitly demotes it to "historical base, do not use as current". Sits in a folder named `CURRENT`, which is the only source of confusion | **P4** — no conflict; naming only |
| `00_GOVERNANCE/MASTER_RESEARCH_CHARTER.md` | EMA, calibrated FEM, RUL, predictive maintenance, Health Index | §12 "Hướng mở rộng sau PhD": FEM calibration with EMA and model updating; similitude laws; predictive maintenance and RUL; Health Index | **ACTIVE and correct.** These are explicitly framed as post-PhD extensions, which the terminology control permits ("Only in Post-PhD/limitations as explicitly deferred work") | **P5 — no action** |
| `00_GOVERNANCE/TERMINOLOGY_CONTROL_CURRENT.md` | all 14 families | The control table itself: "calibrated FEM — REMOVE from all core text"; "equivalent stiffness degradation — REMOVE from claims"; "MAC (as thesis acceptance criterion) — REMOVE as criterion"; "FEM_Node_ID (as chain link) — …" | **ACTIVE guardrail.** Highest keyword density in the repository *because* it is the prohibition list | **P5 — no action** |
| `00_GOVERNANCE/AGENT_RULES.md` | calibrated FEM, MAC, EMA, stiffness degradation, RUL, predictive maintenance, field damage diagnosis, Health Index, autonomous maintenance | Single out-of-scope trigger list: "out of scope — dừng và cảnh báo" | **ACTIVE guardrail** | **P5 — no action** |
| `00_GOVERNANCE/SOURCE_OF_TRUTH_HIERARCHY_v2.1.md` | FEM-core | "File FEM-core cũ đã nằm sẵn trong `90_BACKUP/` và `92_ARCHIVE_MINIMAL` — giữ nguyên" | **ACTIVE.** Confirms FEM-core files are expected in `90_BACKUP/`. But `92_ARCHIVE_MINIMAL/` does not exist | **P2** — resolves as a broken-path issue, not a legacy-content issue |
| `01_CURRENT_CONTROL/SYSTEM_UPDATE_REPORT_v2.1_20260719.md` | FEM-core | "File FEM-core cũ đã nằm sẵn trong `90_BACKUP/.../92_ARCHIVE_SUPERSEDED_FILES` và `92_ARCHIVE_MINIMAL`" | **ACTIVE report.** Points at a real path *and* a non-existent one in the same sentence | **P2** |
| `01_CURRENT_CONTROL/KEYWORD_AND_CONFLICT_CHECK_REPORT.md` | all families | A **prior keyword scan** with the same purpose as this section: "FEM calibration / calibrated FEM — ✅ chỉ trong prohibited/exclusion"; "RUL — ✅ chỉ trong prohibited" | **ACTIVE.** Independently corroborates this audit's §1 conclusion. Undated in filename | **P3** — read to compare scope and date |
| `04_PHD_SPECIAL_TOPICS/CHUYEN_DE_TONG_QUAN/*` (4 files) | Health Index, autonomous maintenance, calibrated FEM, stiffness degradation, DT maturity | "**Out of scope** \| Field damage diagnosis; calibrated FEM trong core; stiffness degradation; weighted Health Index; Edge AI; Smart City; autonomous maintenance" | **ACTIVE coursework, correctly scoped.** Dated 18/07, so predates the `Action_Record_ID` ADR of 19/07 — tracker item #18 already flags coursework as still using `Action_Status`-in-chain notation and says **do not revise the evidence now** | **P4** — already tracked |
| `02_EVIDENCE_BASE/WP4_GATE5/06_WP4_DECISION_SUPPORT_EVIDENCE_ADDENDUM_v1.0_20260718.md` | predictive maintenance, autonomous action, DT maturity | Frames AHP / weighted condition index / Markov deterioration / PdM / autonomous action as **SUPPORTING_REFERENCE** literature that does *not* constitute the thesis four-level logic | **ACTIVE and correctly framed** — literature context, not thesis method | **P5 — no action** |
| `06_LITERATURE_AND_ZOTERO/PERPLEXITY_PRO/*` (10 files) | DT maturity, PdM, RUL, MAC | Literature discovery outputs; keywords appear because the surveyed papers use them | **ACTIVE but tier-8** — governance ranks discovery outputs as "không citable làm evidence" | **P5 — no action** |
| `02_EVIDENCE_BASE/ZOTERO_AUDIT/10_ZOTERO_WRITEBACK_QUEUE_20260718.md` | RUL, autonomous maintenance | Each entry records a "Prohibited inference" field, e.g. "bearing results prove steel-frame field diagnosis, RUL, or severity" | **ACTIVE guardrail metadata** | **P5 — no action** |
| `90_BACKUP/…/07_FABLE_LEGACY_PACK_20260718/03_SCOPE_AND_FEM_GUARDRAILS_20260718.md` | FEM guardrails | Legacy pack, 4 KB. Filename declares "legacy" | **HISTORICAL.** Not referenced by any active document | **P5** |
| `90_BACKUP/…/92_ARCHIVE_SUPERSEDED_FILES/ARCHIVE_NOTE_LIMITED_FEM_MIGRATION_20260717.md` | Limited-FEM migration | Archive note for the FEM-core → Limited-FEM migration | **HISTORICAL, correctly labelled** | **P5** |
| `90_BACKUP/…/MASTER_RESEARCH_CHARTER_v1.0_SUPERSEDED_20260717.md` | FEM-core era charter | Self-declares SUPERSEDED in the filename | **HISTORICAL, correctly labelled.** Only copy in the repository | **P5** — preserve, do not delete |

---

## 3. `FEM_Node_ID` — the one keyword with a genuine split

`FEM_Node_ID` (43 occurrences, 24 files) is the only family where active files disagree:

| Position | Stated in | Date |
|---|---|---|
| Removed from the core identifier chain | `THE_COUNCIL_REVIEW_FEM_OR_NO_FEM_17.07.2026.md` | 17/07 |
| "optional metadata only" | `LIVING_EVIDENCE_BASE_v1.1_LIMITED_FEM.md` (historical) | 17/07 |
| Controlled term — "FEM_Node_ID (as chain link)" listed in the removal table | `TERMINOLOGY_CONTROL_CURRENT.md` | 19/07 |
| **"`FEM_Node_ID` chỉ là metadata tùy chọn"** — restated as current scope | **`Skill.md` (root)** | **28/07** |

The first three are consistent (removed from the chain; may persist as optional metadata; not a chain link). `Skill.md` restates the position but pairs it with the **superseded `Action_Status` chain**, which is the actual conflict — see §2 row 1.

**No file in the repository advocates calibrated FEM, EMA-based model updating, MAC as an acceptance criterion, stiffness-degradation inference, RUL, predictive maintenance, a weighted Health Index, autonomous maintenance, or a commercial platform as current thesis direction.** Every occurrence is a prohibition, a post-PhD deferral, a literature description, a decision record of rejection, or a file explicitly labelled historical.

---

## 4. Dangling references (related finding)

119 distinct artifacts are cited in backticks by active markdown but do not exist under this repository root. This is not a legacy-direction problem, but it is the same class of drift and is recorded here for the same review pass.

**Governance / navigation (5)** — `99_ARCHIVE_PRE_V2_SYSTEM_20260719/`, `92_ARCHIVE_MINIMAL/`, `ARCHIVE_MANIFEST.md`, `UNRESOLVED_ITEMS_CURRENT.md`, `05_DATA_CODE_AND_EXPERIMENTS/G1_EXECUTION_PACK/`

**G1 evidence artifacts (≈45)** — `RUN_REGISTRY_LOCKED.csv` (cited by 6 files), `DATASET_FILE_MANIFEST.csv` (5), `02_MASTER_RUN_REGISTRY.csv`, `06_MASTER_RUN_REGISTRY.csv`, `02_PHYSICAL_SENSOR_MAPPING_REGISTRY.csv` (4), `04_CHANNEL_QUALITY_REGISTRY.csv` (5), `05_EXCLUSION_AND_WARNING_REGISTRY.csv` (4), `01_RAW_FILE_INVENTORY.csv`, `04_ANALYSIS_SET_MANIFEST.csv`, `10_PER_CLASS_RESULTS.csv`, `14_PREDICTIONS_WITH_PROVENANCE.csv`, `sensor_fingerprint_check.csv`, `sensor_block_permutation_flags.csv`, the fold manifests, plus the 10 Evidence-Gates G1 artifacts (`DATASET_MANIFEST.csv`, `RUN_REGISTRY_DATA_DICTIONARY.md`, `FILE_PROVENANCE_REGISTER.csv`, `SENSOR_METADATA_REGISTER.csv`, `LORO_PROTOCOL_PREREGISTERED.md`, `MODEL_CONFIGURATION_REGISTER.csv`, `RESNET1D_PROVENANCE_AUDIT.md`, `G1_ACCEPTANCE_MATRIX.md`, `PAPER1_CLAIM_STATUS_TABLE.md`)

**Code (≈20)** — `canon_lib.py`, `stage1_inventory.py` … `stage10_automated_tests.py`, `generate_windows_from_fold.py`, `run_pipeline.sh`, `build_registry.py`, `build_data_cache.py`, `pipeline_lib.py`, `run_cnn.py`, `run_feature_baselines.py`, `run_permutation_control.py`, `run_sensitivity.py`, `assemble_outputs.py`, `make_figs.py`

**Raw data (4)** — `Campaign1_25.04.2026/`, `Campaign2_22.07.2026/`, `Campaign3_29.07.2026/`, `DATA_ALL_3_CAMPAIGN/`, plus `CANONICAL_THREE_CAMPAIGN_DATASET.zip`

**G2 schema / CQ `v0.1` set (8)** — announced by README v2.2: `CONTEXT_MAPPING_RULES_v0.1.md`, `RQ2_ENTITY_RELATIONSHIP_MODEL_v0.1.md`, `IDENTIFIER_AND_SENSOR_ASSIGNMENT_SCHEMA_v0.1.csv`, `CEI_METADATA_DICTIONARY_v0.1.csv`, `INSPECTION_RECORD_SCHEMA_v0.1.csv`, `ACTION_RECORD_ACCOUNTABILITY_SCHEMA_v0.1.csv`, `G2_COMPETENCY_QUESTION_REGISTER_v0.1.md`, `G2_ACCEPTANCE_CRITERIA_v0.1.md`

**Paper 1 outputs (≈20)** — `BAO_CAO_RESNET1D.docx` (cited 3×), `PAPER1_JOURNAL_OUTLINE_EMPTY_RESULTS_v3.docx`, `PAPER1_TABLE_AND_FIGURE_SPECIFICATION_v3.docx`, `PAPER1_CONDITIONAL_DISCUSSION_AND_CONCLUSION_MATRIX_v3.docx`, `PAPER1_GATE1_Q2_VERIFIED_EVIDENCE_REVISED_v2.docx`, and the 9 `_vX` control-room templates

**Pre-existing known-missing (10)** — already registered in `MISSING_CURRENT_FILES_REGISTER_20260718.md`; that file states they were not deleted by the 2026-07-18 cleanup and were not reconstructed

**Outside this root (3)** — `../05_MASTER_INDEX_CONTROL/FINAL_CONSISTENCY_AUDIT_v1.1.md`, `04_AI_SYSTEM/AGENTS/RESEARCH_CHARTER.md`, `00_SYSTEM/MASTER_CHARTER.md`. These are expected to be outside; sibling folders `01_KNOWLEDGE/`, `04_AI_SYSTEM/`, `05_MASTER_INDEX_CONTROL/` exist one level up but were **not scanned** (outside the specified audit root)

---

## Claim → Evidence → Limitation → Next action

**Claim.** The repository shows **no active advocacy of any legacy research direction.** 54% of the 516 legacy-keyword occurrences sit inside explicit prohibition or exclusion statements, and the remainder are post-PhD deferrals, literature descriptions, decision records of rejection, or files correctly labelled historical. One genuine conflict exists: `Skill.md` at the repository root, modified 2026-07-28, encodes the pre-v2.1 identifier chain ending in `Action_Status`, contradicting Charter v2.1 (19/07) and README v2.2 (20/07). Separately, 119 referenced artifacts do not exist under this root.

**Evidence.** Regex scan of 14 keyword families across 232 readable text files, 516 occurrences with ±90-character context captured for each; negation-frame classification of every occurrence; direct reading of `Skill.md`, `TERMINOLOGY_CONTROL_CURRENT.md`, `AGENT_RULES.md`, `THE_COUNCIL_REVIEW_FEM_OR_NO_FEM_17.07.2026.md`, `LIVING_EVIDENCE_BASE_v1.1_LIMITED_FEM.md`, `LIVING_EVIDENCE_BASE_CURRENT.md`, `MASTER_RESEARCH_CHARTER.md`, and `UNRESOLVED_ITEMS_TRACKER_v2.1.md` (item #18 confirms the coursework `Action_Status` notation is known and deliberately not being revised yet).

**Limitation.** The scan covers text formats only. **The 52 `.pdf` and 13 `.docx` files were not text-extracted** — a legacy-direction statement inside `MASTER_RESEARCH_CHARTER_v2_20260719.docx` (the v2.0 charter), the three Vietnamese experiment protocols, or the Paper 1 outline `.docx` files would not appear here. Negation-frame classification is a ±90-character heuristic and can misjudge long sentences or table rows. Priority labels are the auditor's provisional judgement. **No file has been reclassified, moved, or marked superseded by this audit.**

**Next action.** Decide the status of `Skill.md` (P1). Then resolve the four broken archive paths (P2), which would also close the `92_ARCHIVE_MINIMAL` references in §2. Compare this scan against the existing `KEYWORD_AND_CONFLICT_CHECK_REPORT.md` (P3) to see whether it covers the same families. Text-extract the 13 `.docx` files before treating the legacy scan as complete.
