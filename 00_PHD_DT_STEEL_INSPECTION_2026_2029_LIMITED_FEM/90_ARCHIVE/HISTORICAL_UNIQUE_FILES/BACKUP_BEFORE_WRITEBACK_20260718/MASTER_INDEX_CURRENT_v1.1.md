# MASTER INDEX — CURRENT
**Version:** v1.1 — LIMITED-FEM | **Last modified:** 2026-07-17 | **Next review:** before chuyên đề tổng quan submission (T7/2026 deadline); at latest 2026-08-17.
This file is the single entry point. If a file is not listed as CURRENT here, do not treat it as source of truth.

## 1. Current source-of-truth files

| File | Location | Owns |
|---|---|---|
| MASTER_RESEARCH_CHARTER_v1.1_LIMITED_FEM_20260717.md | 01_CORE_REPORTS | Scope, RQs, WPs, chapters, papers, claims, FEM role |
| RESEARCH_ARCHITECTURE_DECISION_RECORD_20260717.md | 01_CORE_REPORTS | Architecture decision (Verdict B) |
| RQ_WP_CHAPTER_PAPER_GATE_MATRIX_v1.1.md | 02_GATE_MATRICES | RQ/WP/chapter/paper/gate mapping and status |
| EVIDENCE_GATES_v1.1_LIMITED_FEM.md | 02_GATE_MATRICES | Gate definitions G1–G7 |
| PAPER1_SCOPE_REVIEW_v1.1_LIMITED_FEM_20260717.md + Paper1_Literature_Addendum_Note.md | 03_PAPER_SPECIFIC/Paper1_Gate1 | Paper 1 (RQ1/WP1) |
| PAPER2_CONCEPT_NOTE_TRACEABILITY_v1.0_20260717.md | 03_PAPER_SPECIFIC/Paper2_Gate3 | Paper 2 (RQ2/WP2) |
| PAPER3_CONCEPT_UPDATE_v1.1_LIMITED_FEM_20260717.md | 03_PAPER_SPECIFIC/Paper3_Gate4 | Paper 3 (RQ3/WP3) |
| PX_RQ1_Lab_Leakage_Evidence.md | 04_RQ_EVIDENCE_ADDENDA | RQ1 evidence addendum |
| RQ2_TRACEABILITY_EVIDENCE_ADDENDUM_v1.0.md | 04_RQ_EVIDENCE_ADDENDA | RQ2 evidence addendum (claims C2-01…C2-11) |
| PX_RQ4_Inspection_Workflow_Evidence.md | 04_RQ_EVIDENCE_ADDENDA | WP4 evidence addendum |
| LIVING_EVIDENCE_BASE_v1.1_LIMITED_FEM.md | 06_LIVING_EVIDENCE_BASE | Evidence classification and claim tagging |
| Literature_Review_Master_Index_Current.md | 05_MASTER_INDEX_CONTROL | Duplicate control and per-key status (control function only; RQ/Paper tags read through the v1.1 remapping below) |
| Literature_Evidence_Cowork_Ready.md + _Addendum.md | 01_CORE_REPORTS | Canonical evidence record content (tags read through v1.1 remapping) |
| TERMINOLOGY_CONTROL_v1.1.md | 05_MASTER_INDEX_CONTROL | Terminology rules |
| MIGRATION_INVENTORY_20260717.md; CHANGE_LOG_LIMITED_FEM_MIGRATION_20260717.md | 05_MASTER_INDEX_CONTROL | Migration record |
| UNRESOLVED_ITEMS_AFTER_LIMITED_FEM_MIGRATION.md | 99_REVIEW_NEEDED | Open items |
| FINAL_CONSISTENCY_AUDIT_v1.1.md | 05_MASTER_INDEX_CONTROL | Consistency status |
| THE_COUNCIL_REVIEW_FEM_OR_NO_FEM_17.07.2026.md | project root | Decision authority record |

## 2. RQ/Paper tag remapping (applies when reading pre-migration files)

| Old tag | Read as (v1.1) |
|---|---|
| RQ2 / Paper 2 (FEM interpretation) | SUPPORTING_REFERENCE or POST_PHD per Living v1.1 §7 |
| RQ3 / Paper 3 (BIM–FEM–Sensor traceability) | RQ2 / Paper 2 (traceability) for schema/identifier content; RQ3 / Paper 3 for field workflow content |
| RQ4 / Optional Paper 4 | WP4 / Gate 5 (unchanged optionality) |
| Gate 3 (FEM) | Removed; see EVIDENCE_GATES_v1.1 |
| Sensor_ID → FEM_Node_ID → BIM_GUID | Sensor_ID → BIM_GUID → Condition_Evidence_ID → Inspection_Record_ID → Action_Status |

## 3. Superseded files and archive locations

| Superseded file | Archive | Note |
|---|---|---|
| 00_SYSTEM/MASTER_CHARTER.md | 92/MASTER_RESEARCH_CHARTER_v1.0_SUPERSEDED_20260717.md (verbatim copy) | Original left in place pending user decision on replacing it in 00_SYSTEM |
| 02_GATE_MATRICES/Updated_RQ_Evidence_Gate_Matrix.csv | 92/Updated_RQ_Evidence_Gate_Matrix_SUPERSEDED_20260717.csv (verbatim copy) | Original preserved |
| 06_LIVING_EVIDENCE_BASE/Literature_Evidence_Living.md | In place (historical record); see 92/ARCHIVE_NOTE_LIMITED_FEM_MIGRATION_20260717.md | Referenced by Living v1.1 for extraction detail |
| 01_CORE_REPORTS/Unified_Literature_Evidence_Gate_Update_20260710.md | In place; see ARCHIVE_NOTE | — |
| 01_CORE_REPORTS/Research_Direction_Evidence_Justification_Report_20260710.md | In place; see ARCHIVE_NOTE | — |
| 03_PAPER_SPECIFIC/Paper2_Gate3/Paper2_Literature_Boundary_Table.md | In place; see ARCHIVE_NOTE | Retained as SUPPORTING_REFERENCE table |
| 04_RQ_EVIDENCE_ADDENDA/PX_RQ2_FEM_Loosening_Evidence.md | In place; see ARCHIVE_NOTE | Retained as SUPPORTING_REFERENCE |
| 03_PAPER_SPECIFIC/Paper3_Gate4/Paper3_Traceability_Gap_Table.md | In place (UPDATE_REQUIRED, content split between Papers 2 and 3) | See PAPER3_CONCEPT_UPDATE |

## 4. RQ/Paper ownership

RQ1/WP1/C4/Paper 1 — Gate 1. RQ2/WP2/C5/Paper 2 — Gates 2, 3, 6. RQ3/WP3/C6/Paper 3 — Gates 4, 7. WP4/C7/optional Paper 4 — Gate 5.

## 5. Unresolved items

See 99_REVIEW_NEEDED/UNRESOLVED_ITEMS_AFTER_LIMITED_FEM_MIGRATION.md (8 items: ResNet1D sensor mode; LORO status; run count; field-access agreement; Inspection_Record structure; CQ approval; DT maturity definition source; program regulations). Plus: AGENT_RULES.md and 04_AI_SYSTEM/RESEARCH_CHARTER.md require user-approved revision; 00_README_INDEX navigation files point to superseded matrix; YTH389L4/BERUCUIC duplicate suspicion.
