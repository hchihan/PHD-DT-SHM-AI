# MASTER INDEX - CURRENT

**Version:** v2.4
**Effective date / Updated:** 13/09/2026
**Status:** CURRENT REPOSITORY NAVIGATION | **Source-of-truth level:** 5
**Supersedes:** v2.3 index (retained at `../90_ARCHIVE/01_SUPERSEDED_VERSIONS/PRE_SYNC_20260913/01_CURRENT_CONTROL/`). | **Superseded by:** None.
**Changes in this version:**
- Replaces paths to folders that no longer exist (`00_GOVERNANCE/`, `02_EVIDENCE_BASE/`, `03_PAPERS/`, `05_DATA_CODE_AND_EXPERIMENTS/`) with locations verified on 13/09/2026.
- Adds the Paper 1 science-lock set and the G1 evidence locations.
- Lists files that are referenced but missing.

No authority order is changed.

**Rule:**
- This index lists current governing and working files only.
- Paths are relative to `01_LITERATURE_REVIEW/01_CURRENT_CONTROL/`; `../../` is the project root.
- Historical, superseded, backup and audit files are excluded, except where the archive holds the only surviving copy of a control record (marked ARCHIVE LOCATION).

## 1. Entry And Authority

| File | Status | Role |
|---|---|---|
| `../README.md` | CURRENT_ENTRY | Literature Review and project navigation. The root `00_README_START_HERE.md` survives only under `../../90_ARCHIVE/` |
| `../../90_ARCHIVE/HISTORICAL_UNIQUE_FILES/BACKUP_BEFORE_WRITEBACK_20260718/MASTER_RESEARCH_CHARTER_v1.1_LIMITED_FEM_20260717.md` | CONTROL_BASELINE — ARCHIVE LOCATION | Locked 17/07 Charter (level 2), read-only. The concise 17/07 `MASTER_RESEARCH_CHARTER.md` is in the same folder |
| `08-RESEARCH_ARCHITECTURE_DECISION_RECORD_20260717.md` | CONTROL_BASELINE | ADR-2026-001 |
| `../../90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/00_GOVERNANCE/THE_COUNCIL_REVIEW_FEM_OR_NO_FEM_17.07.2026.md` | DECISION_AUTHORITY — ARCHIVE LOCATION | Unchanged Council Review (a copy also exists under `../../90_ARCHIVE/SNAPSHOTS_20260718/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/`) |
| `SOURCE_OF_TRUTH_HIERARCHY_v2.1.md` | CURRENT_AUTHORITY_ORDER | Conflict resolution and evidence order. Its internal paths are stale (sync report C-09) |
| `CURRENT_DIRECTION_LOCK_20260804.md` | CURRENT_DIRECTION_LOCK | Execution direction and non-negotiable boundaries |
| `CURRENT_STATUS_AND_NEXT_DIRECTION.md` | CURRENT_STATUS (v2.4) | Gate and Paper status; P1–P3 priorities; WP1 → WP2 handover |
| `PAPER1_SCIENCE_LOCK_PROJECT_SYNC_REPORT_20260913.md` | CURRENT_SYNC_RECORD | Paper 1 science-lock synchronization, G1 gap, conflicts and decisions required |

## 2. Approved Governance (this folder)

| File | Role |
|---|---|
| `MASTER_RESEARCH_CHARTER_CURRENT_20260812.md` | Consolidated Charter v2.1.2 (level 3), subordinate to the 17/07 baseline. Carries the title "v2.1 TRACEABILITY-CORE" |
| `RQ_WP_CHAPTER_PAPER_GATE_MATRIX_v2.1.md` | RQ-WP-Chapter-Paper-Gate mapping; §5A Paper 1 claim status |
| `EVIDENCE_GATES_v2.1.md` | Gate definitions and acceptance requirements; G1/M1 evidence sync |
| `TERMINOLOGY_CONTROL_CURRENT.md` | Controlled terminology |
| `AGENT_RULES.md` | Agent scope and evidence rules |
| `RESEARCH_DIRECTION_AND_SCOPE.md` | Supporting research boundary |
| `RESEARCH_ARCHITECTURE.md` | Supporting four-layer architecture |

## 3. Paper 1 / G1 Set

| File or location | Status | Role |
|---|---|---|
| `../03_OUTPUTS/03_PAPER_1A_GATE1/Paper 1.md/PAPER1_v8.1_SHM_RISK_REDUCED.docx` | CURRENT_MANUSCRIPT — SCIENCE LOCKED | Final Paper 1 (target: Structural Health Monitoring); not submitted |
| `../03_OUTPUTS/03_PAPER_1A_GATE1/Paper 1.md/PAPER1_v8.1_SHM_PRE_SUBMISSION_AUDIT.md`, `PAPER1_v8.1_SHM_CHANGELOG.md`, `PAPER1_v8.1_NEW_REFERENCE_AUDIT.md` | CURRENT_AUDIT | Verdict: READY AFTER AUTHOR METADATA / FIGURE FIXES |
| `../03_OUTPUTS/03_PAPER_1A_GATE1/BAO_CAO_IT01_IT06.md` | CURRENT_EVIDENCE_AUDIT | IT-01–IT-06 (12/09/2026); overriding evidence for reported numbers |
| `../03_OUTPUTS/03_PAPER_1A_GATE1/Paper 1.md/README.md` | CURRENT_STATUS_RECORD | Paper 1 status record |
| `../03_OUTPUTS/03_PAPER_1A_GATE1/PAPER1_Figure3_A4_Editable.pptx` | AUTHOR_ACTION | Figure 3, pending author approval |
| `../03_OUTPUTS/02_CHUYEN_DE_1/PAPER1_SUPERVISOR_REPORT_DUT_TEMPLATE_v2.pptx`, `PAPER1_GIAI_THICH_NGHIEN_CUU_DE_HIEU_v2.md` | CURRENT_SUPERVISOR_MATERIAL | Supervisor briefing (v1 files superseded) |
| `../../02_DATA_CODE_AND_EXPERIMENTS/OUTPUT/24.08.2026/GATE1_LORO_UPDATED_RESULTS_AUDIT_20260824.md` | SUPPORTING_AUDIT | LORO audit; ResNet1D sensor-mode verification |
| `../../02_DATA_CODE_AND_EXPERIMENTS/OUTPUT/27.08.2026/bao_cao_xac_minh_tinh_hop_le_va_ket_qua_ml.md` | SUPPORTING_AUDIT | CP2 provenance; permutation and aggregation caveats |
| `../../02_DATA_CODE_AND_EXPERIMENTS/OUTPUT/GATE1_INTEGRATED_EVIDENCE_AND_CLOSURE_AUDIT_20260819.md` | HISTORICAL_AUDIT | Superseded as a status source by the 24/08, 07/09 and 12/09 audits |
| `../../02_DATA_CODE_AND_EXPERIMENTS/THREE_CAMPAIGN_REANALYSIS/` | SUPERSEDED_FOR_CLAIMS | 29/07 provisional reanalysis using legacy block-position sensor identity; do not cite as Paper 1 evidence |
| `../../02_DATA_CODE_AND_EXPERIMENTS/CANONICAL_THREE_CAMPAIGN_DATASET/08_AUTOMATED_VALIDATION_RESULTS.csv` | SUPPORTING_PROXY | Early validation assertions |
| `D:\01_RESEARCH\08_Output_07.09\` | OUTSIDE_REPOSITORY_WORKING_EVIDENCE | Four Kaggle output bundles; built NPZ dataset `v1/` (manifest, index, splits, QC); 07/09 audit set (`00`–`07`). Not a G1 execution pack |
| `G1_EXECUTION_PACK/` | NOT CREATED | Required by EVIDENCE_GATES G1. The designated path lies under a non-existent root (sync report C-11) |

No entry in this index implies G1 acceptance.

## 4. Current G2–G3 And Paper 2 Set

| File | Status | Role |
|---|---|---|
| `../03_OUTPUTS/05_PAPER_2_TRACEABILITY/G2_G3_PAPER2_CURRENT_ROADMAP_v2.1_20260804.md` | CURRENT_ROADMAP | G2 specification to G3 validation sequence |
| `../03_OUTPUTS/05_PAPER_2_TRACEABILITY/PAPER2_CURRENT_DIRECTION_v2.1_20260804.md` | CURRENT_PAPER_DIRECTION | Single Paper 2 scope and claim boundary |
| `../03_OUTPUTS/05_PAPER_2_TRACEABILITY/PAPER2_VERIFIABLE_TRACEABILITY_DETAILED_OUTLINE_v0.1_20260812.md` | WORKING_OUTLINE | Paper 2 outline |
| `../02_DEEP_READ_CURRENT_PDF/03_RQ2_GATE2_3/G1_TO_G2_CONDITION_EVIDENCE_INTERFACE_v1.0.md` | CURRENT_WORKING_SPECIFICATION | G1-to-G2 evidence contract; carries a sync note dated 13/09/2026 |
| `G1_G2_INTERFACE_DECISION_REGISTER.csv` | CURRENT_DECISION_REGISTER | Open interface decisions and approval state |

## 5. Current Evidence Bases

| File or location | Role |
|---|---|
| `LIVING_EVIDENCE_BASE_CURRENT_20260812.md` | Current evidence register. Its RQ1 lines predate the Paper 1 science lock; a sync is pending |
| `MASTER_LITERATURE_AND_EVIDENCE_SYNTHESIS_v2_20260828.md` and `REVISION_LOG_MASTER_SYNTHESIS_v2_20260828.md` | Current master synthesis. Its Paper 1 figures predate the science lock |
| `../02_DEEP_READ_CURRENT_PDF/` | Current deep reads by RQ/Gate |
| `../02_DEEP_READ_CURRENT_PDF/03_RQ2_GATE2_3/ROUND4_VERIFIED_EVIDENCE_RECORD_v1.1.md` | Round 4 audit-corrected evidence; provisional in part |
| `../02_DEEP_READ_CURRENT_PDF/03_RQ2_GATE2_3/G2_G3_SCREENING_EVIDENCE_AND_GAP_REPORT.md` and `G2_G3_RECENT_EVIDENCE_SCREENING_2023_2026.md` | Immutable screening evidence |
| `../../90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/02_EVIDENCE/` | IMMUTABLE_EVIDENCE — ARCHIVE LOCATION: Round 1, Round 2, Round 3A, Round 3B and the RQ2 addendum v1.2 |

These reports support design decisions but do not constitute executed gate evidence.

## 6. Literature Review, Paper 1B, Paper 3

| File or location | Status |
|---|---|
| `../03_OUTPUTS/01_TIEU_LUAN_TONG_QUAN/TIEU_LUAN_TONG_QUAN_HOAN_CHINH_v2_13092026.docx` | CURRENT_WORKING (priority P1) |
| `../03_OUTPUTS/04_PAPER_1B_SENSOR_CONFIGURATION/` | SUPPORTING_SCOPE of WP1; no RQ, WP or Gate of its own |
| `../03_OUTPUTS/06_PAPER_3_FIELD_FEASIBILITY/PAPER3_FIELD_FEASIBILITY_DIRECTION_v2.1_20260719.md` | CURRENT_DIRECTION (G4 preparation) |

## 7. Referenced In v2.3 But Not Found In The Current Tree (13/09/2026)

- `00_README_START_HERE.md` (root): archive copies only.
- `../02_EVIDENCE_BASE/06-MASTER_RESEARCH_CHARTER_v1.1_LIMITED_FEM_20260717.md`: archive copy only, without the `06-` prefix (see §1).
- `MASTER_RESEARCH_CHARTER_v2.1_TRACEABILITY_CORE_20260719.md`: apparently continued as `MASTER_RESEARCH_CHARTER_CURRENT_20260812.md` (same title, v2.1.2).
- `LIVING_EVIDENCE_BASE_v2.1_TRACEABILITY_CORE.md` and `PAPER1_DIRECTION_AND_GATE_v2.1_20260719.md`: not found.
- `PAPER1_GATE1_READINESS_REPORT_v2.md`: archive only (pre-18/07 snapshot).
- `THREE_CAMPAIGN_REANALYSIS/00_EXECUTIVE_REPORT.md` and `CANONICAL_THREE_CAMPAIGN_DATASET/00_README.md`: not found; only CSV outputs remain.
- `SUPERSEDED_DOCUMENT_REGISTER_20260804.csv` and the 04/08 reset manifests: not found in current control.
- `EVIDENCE_AND_GOVERNANCE_UPDATE_REPORT_20260811.md`: archive only (`../../90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/02_EVIDENCE/`).
- `CONFERENCE_PAPER_RESEARCH_DIRECTIONS_CURRENT_20260812.md`: archive only (`../90_ARCHIVE/03_AUDIT_CLEANUP_AND_MANIFESTS/01_CORE_SOURCE_OF_TRUTH_REMAINDER/`).
- `EVIDENCE_GATES_v1.1_LIMITED_FEM.md`: never found.

## 8. State Summary

| Item | State |
|---|---|
| Paper 1 | `SCIENCE LOCKED — NOT SUBMISSION-READY — NOT SUBMITTED` |
| G1 | `OPEN — PARTIAL EVIDENCE`; execution pack not materialized; no signed acceptance |
| G2 | `OPEN — LITERATURE BOUNDARY CLOSED, SPECIFICATION NOT YET FROZEN` |
| G3 | `OPEN — NOT IMPLEMENTED, NOT VALIDATED, NOT OFFICIALLY PASSED`; execution `NOT OPEN` |
| G4 | Readiness/preparation only; field access unconfirmed |
| G5 | OPEN; not a current priority |
| Paper 2 | `DESIGN AND EVIDENCE DEVELOPMENT` |
| Priorities | P1 Literature Review → P2 G2–G3 → P3 G4 preparation |

Historical and superseded files are in `../90_ARCHIVE/` and `../../90_ARCHIVE/`, with move history in `../99_INDEX_AND_LOG/CLEANUP_AND_MOVE_LOG.csv`. They are not listed as current here.
