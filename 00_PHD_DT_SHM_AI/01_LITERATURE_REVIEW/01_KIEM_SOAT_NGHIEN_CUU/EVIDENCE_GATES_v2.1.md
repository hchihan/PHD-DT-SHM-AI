# EVIDENCE GATES — v2.1 (EXECUTION GATES)
**Version:** v2.4 | **Issued:** 2026-07-19 | **Updated:** 13/09/2026
**Status:** CURRENT | **Source-of-truth level:** 4
**Supersedes:** v2.3 execution-gate wording (retained at `../90_ARCHIVE/01_SUPERSEDED_VERSIONS/PRE_SYNC_20260913/01_CURRENT_CONTROL/`). | **Superseded by:** None.
**Changes in this version:** Adds the "G1 / M1 evidence sync (13/09/2026)" subsection and updates the current-priority line after the Paper 1 science lock. Acceptance criteria and item statuses are unchanged; no Gate is closed. (v2.3 restored the canonical 17/07 identifier chain, made approved CQs and verification criteria prerequisites to G2–3 schema work, and recorded evidence status through 11/08/2026.)
**Rule:** Mỗi Gate item là một **execution gate** với artifact bắt buộc + acceptance criterion + evidence path + owner + reviewer/sign-off + status. **Không đánh dấu PASS chỉ vì code chạy thành công.** Không đóng gate bằng giả định. Không tồn tại gate FEM-calibration/MAC/EMA/stiffness/OSP.

**Current priority (13/09/2026):** the earliest open gate remains **G1** — `OPEN — PARTIAL EVIDENCE`. The scientific evidence behind Paper 1 is executed and audited, but the repository-resident execution pack and the signed acceptance are missing (see "G1 / M1 evidence sync" below). Execution priorities from 13/09/2026 (P1 literature review, P2 G2–G3, P3 G4 preparation) are set in `CURRENT_STATUS_AND_NEXT_DIRECTION.md` v2.4 §7.
**Status legend:** OPEN · PARTIAL EVIDENCE · IN-PROGRESS · READY-FOR-REVIEW · EXECUTION-NOT-OPEN · PASS (signed) · N/A.

---

## G1 — Dataset integrity & run-aware evaluation
Execution pack: `05_DATA_CODE_AND_EXPERIMENTS/G1_EXECUTION_PACK/` (khi khởi tạo).

| Gate item | Required artifact | Acceptance criterion | Evidence path | Owner | Reviewer/sign-off | Status |
|---|---|---|---|---|---|---|
| Dataset version | `DATASET_MANIFEST.csv` | Dataset có version-tag cố định + hash; mọi run trỏ về đúng version | G1_EXECUTION_PACK/ | PhD | Supervisor | OPEN |
| Run registry | `RUN_REGISTRY_LOCKED.csv` + `RUN_REGISTRY_DATA_DICTIONARY.md` | Mọi run có id, date, config, sensor set; count khóa (xác nhận "6" hay khác) | G1_EXECUTION_PACK/ | PhD | Supervisor | OPEN |
| Input manifest | `FILE_PROVENANCE_REGISTER.csv` | Mỗi file thô ↔ run ↔ hash ↔ nguồn | G1_EXECUTION_PACK/ | PhD | — | OPEN |
| Sensor metadata | `SENSOR_METADATA_REGISTER.csv` | Mỗi sensor: vị trí, kênh, trục, đơn vị, sampling | G1_EXECUTION_PACK/ | PhD | — | OPEN |
| Script/repo/version | commit hash / repo tag | Code chạy được từ commit cố định; không sửa sau khi khóa | repo | PhD | — | OPEN |
| Fold definition | `LORO_PROTOCOL_PREREGISTERED.md` | LORO fold = leave-one-run-out; định nghĩa trước khi chạy | G1_EXECUTION_PACK/ | PhD | Supervisor | OPEN |
| Split-before-windowing | evidence log | Split ở cấp run TRƯỚC khi windowing (chống rò rỉ) | G1_EXECUTION_PACK/ | PhD | — | OPEN |
| Train-only preprocessing | evidence log | Scaler/normalisation fit chỉ trên train fold | G1_EXECUTION_PACK/ | PhD | — | OPEN |
| Common seeds | config | Seed chung, ghi lại, tái lập được | G1_EXECUTION_PACK/ | PhD | — | OPEN |
| Model configuration | `MODEL_CONFIGURATION_REGISTER.csv` | Config từng model (RF, 1D-CNN, ResNet1D) khóa | G1_EXECUTION_PACK/ | PhD | — | OPEN |
| Output metrics | metrics table | Macro-F1 + per-class, per-fold | G1_EXECUTION_PACK/ | PhD | Supervisor | OPEN |
| Run/fold uncertainty | uncertainty table | Mean ± sd across folds/runs; không chỉ 1 con số | G1_EXECUTION_PACK/ | PhD | Supervisor | OPEN |
| ResNet1D provenance | `RESNET1D_PROVENANCE_AUDIT.md` | Sensor mode & input provenance xác nhận; nếu không → loại khỏi Paper 1 | G1_EXECUTION_PACK/ | PhD | Supervisor | OPEN |
| Rerun conditions | rerun note | Điều kiện tái chạy được ghi để reproduce | G1_EXECUTION_PACK/ | PhD | — | OPEN |
| Gate sign-off | `G1_ACCEPTANCE_MATRIX.md` | Người xác nhận Gate ký; mọi item PASS | G1_EXECUTION_PACK/ | PhD | Supervisor | OPEN |

**Cho tới khi G1 PASS:** mọi Paper 1 metric/claim ghi "Candidate claim pending Gate 1 closure."

### Milestone M1 — Paper 1 Submission Readiness (KHÔNG phải Gate mới)
Milestone công bố nằm **dưới** G1; không tạo Evidence Gate mới.

| M1 item | Acceptance criterion | Status |
|---|---|---|
| G1 closed | G1_ACCEPTANCE_MATRIX ký PASS | OPEN |
| Final claim table locked | `PAPER1_CLAIM_STATUS_TABLE.md` khóa | OPEN |
| Candidate claims resolved | mỗi candidate được accepted/rejected/revised | OPEN |
| Reproducibility package | dataset+registry+script+seeds+config đầy đủ | OPEN |
| Limitations updated | limitations phản ánh kết quả LORO | OPEN |
| Figures/tables from LORO | mọi hình/bảng dùng kết quả LORO (không preliminary) | OPEN |
| Submission-ready | Paper 1 sẵn sàng nộp | OPEN |

### G1 / M1 evidence sync (13/09/2026): statuses above unchanged

Recorded after the Paper 1 science lock. This subsection describes evidence locations and gaps only. It does not change any item status, and no reviewer sign-off exists. Details: `PAPER1_SCIENCE_LOCK_PROJECT_SYNC_REPORT_20260913.md` §3.

| G1 item | Evidence now available | Location | Gap |
|---|---|---|---|
| Dataset version | Built-dataset `manifest.json` (216 recordings, 6,899 windows, canonical-manifest SHA-256) and `index.csv` (102 NPZ SHA-256). NPZ files reconciled with the Kaggle copies (IT-01) | `D:\01_RESEARCH\08_Output_07.09\v1\` (outside repository) | Not in pack. The manifest records 18 selected splits, whereas 30 ordered combinations per case were executed |
| Run registry | Canonical campaigns/runs/recordings registry; IT `DATASET_REGISTRY_FINAL.csv` | Kaggle bundles (outside repository); IT deliverable not in project | Not locked; no data dictionary |
| Input manifest | 216 source paths and SHA-256 values; recomputed hashes match (IT-01) | IT evidence folder (not in project) | Training-time byte identity cannot be verified (no load-time hashes) |
| Sensor metadata | Channel map x, y, z, resultant; 8 or 12 channels (IT-02) | IT deliverable (not in project) | Device serial, mounting position and pre-export synchronisation undocumented |
| Script/repo/version | Commit `360c79f`, `git_dirty = false` on all runs | Kaggle bundles | No repository tag; repository is private |
| Fold definition | Whole-run 4/1/1 partitioning; 30 ordered validation–test combinations per case (v8.1 §3.8) | Manuscript | **Not preregistered** (decision C-05) |
| Split-before-windowing | Windows cut within recordings before partitioning; whole runs assigned; 0 test-run leakage violations | v8.1 §3.5; 07/09 protocol audit (outside repository) | Literal wording not met; functionally equivalent (decision C-05) |
| Train-only preprocessing | Per-window standardisation (no cross-recording information); SVM StandardScaler fitted on training data only | v8.1 §3.6; IT-05 | Wording (decision C-05) |
| Common seeds | Deep models 42/43/44; RF/SVM `random_state` 42 | v8.1 Table A2 | RF/SVM single seed |
| Model configuration | Parameters for six models; hyperparameter-development record | v8.1 Table A2; `../03_OUTPUTS/03_PAPER_1A_GATE1/bao_cao_lua_chon_hyperparameter.pdf` | `MODEL_CONFIGURATION_REGISTER.csv` not created |
| Output metrics | Recording-level Tables 4–7 and A3–A7; 469 of 472 values matched, 3 corrected | v8.1; IT-06 | Per-window probabilities not archived |
| Run/fold uncertainty | SD_fold and SD_seed (ddof = 1); per-fold balanced accuracy | v8.1 §3.10, Table 6 | No within-campaign permutation |
| ResNet1D provenance | Sensor/input mode verified; 612 deep-model checkpoints reproduced | `../../02_DATA_CODE_AND_EXPERIMENTS/OUTPUT/24.08.2026/GATE1_LORO_UPDATED_RESULTS_AUDIT_20260824.md`; IT-05 | Standalone `RESNET1D_PROVENANCE_AUDIT.md` absent; ResNet1D retained in Paper 1 |
| Rerun conditions | Notebooks, configs, output bundles | Outside repository | Rerun note absent |
| Gate sign-off | None | — | **`G1_ACCEPTANCE_MATRIX.md` absent — blocking** |

| M1 item | Evidence now available | Gap |
|---|---|---|
| G1 closed | — | G1 not signed |
| Final claim table locked | Claims locked in manuscript v8.1; matrix §5A | `PAPER1_CLAIM_STATUS_TABLE.md` not created |
| Candidate claims resolved | Matrix §5A (not claimed / superseded / locked in manuscript) | Supervisor decisions C-02 and C-03 |
| Reproducibility package | Output bundles, NPZ dataset and code, all outside the repository | No public DOI; IT deliverables not in project |
| Limitations updated | v8.1 §4.1, §5.6 | — |
| Figures/tables from LORO | All v8.1 tables and figures use LORO results | Figure 3 pending author approval |
| Submission-ready | Pre-submission audit: READY AFTER AUTHOR METADATA / FIGURE FIXES | Author items; G1 sign-off or approved exception (C-04) |

The execution-pack path `05_DATA_CODE_AND_EXPERIMENTS/G1_EXECUTION_PACK/` lies under a root folder that no longer exists. The current data root is `02_DATA_CODE_AND_EXPERIMENTS/` (decision C-11).

---

## G2 — Traceability model & competency questions

**Gate status:** `OPEN — LITERATURE BOUNDARY CLOSED, SPECIFICATION NOT YET FROZEN`. The corpus-bounded `CLOSE_SEARCH` decision is not G2 PASS.

| Gate item | Required artifact | Acceptance criterion | Evidence path | Owner | Reviewer/sign-off | Status |
|---|---|---|---|---|---|---|
| G2 Final Decision Register | reviewed register | Every FREEZE/FREEZE_PROVISIONALLY/EXPERT_REVIEW_REQUIRED/WAIT_FOR_G1_PAYLOAD/REMOVE item has basis, owner and approval state | 02_EVIDENCE_BASE/CURRENT/ | PhD | Supervisor | OPEN |
| Action-Status-Event ADR | accepted ADR or explicit unresolved decision | Proposed ADR reviewed; no proposed rule treated as accepted | 00_GOVERNANCE/ | PhD | Supervisor | OPEN |
| Identifier governance | control doc | `Sensor_ID → BIM_GUID → Condition_Evidence_ID → Inspection_Record_ID → Action_Status`; proposed implementation IDs do not replace/extend the chain | 02_EVIDENCE_BASE/RQ2_GATES2_3/ | PhD | Supervisor | OPEN |
| CEI attribute structure | CEI spec | Metadata fields (validity, model confidence, run/fold variability, sensor config, data-quality, provenance, timestamp/version); không scalar | 02_EVIDENCE_BASE/RQ2_GATES2_3/ | PhD | Supervisor | OPEN |
| Competency questions | approved preregistration | Domain CQs, expected-answer form and scope approved **before any schema build/freeze** | 02_EVIDENCE_BASE/RQ2_GATES2_3/ | PhD | Supervisor | OPEN |
| Verification criteria | approved criteria doc | Pass/fail criteria, forward/reverse expectations and evidence requirements approved **before any schema build/freeze** | 02_EVIDENCE_BASE/RQ2_GATES2_3/ | PhD | Supervisor | OPEN |
| Inspection_Record/Action_Status schema | minimum schema | Built only after the two prerequisites above; preserves the canonical chain | 02_EVIDENCE_BASE/RQ2_GATES2_3/ | PhD | Supervisor | EXECUTION-NOT-OPEN |
| Verification and closure semantics | specification | Exact semantics approved; proposed Action_Record/Status_Event constructs remain noncanonical unless separately accepted | 02_EVIDENCE_BASE/RQ2_GATES2_3/ | PhD | Supervisor/Expert | OPEN |
| Constraint Catalogue | versioned catalogue | Identity, relation, chronology, transition, authorization, evidence and closure families fixed | 02_EVIDENCE_BASE/RQ2_GATES2_3/ | PhD | Supervisor | OPEN |
| Fixture/Oracle Manifest | machine-readable or versioned manifest | Controlled valid/invalid fixtures, isolated mutations, expected focus IDs/codes/counts and exact expected-vs-actual rule | 02_EVIDENCE_BASE/RQ2_GATES2_3/ | PhD | Supervisor | OPEN |
| G2 baseline/sign-off | approval record | Complete internally consistent package reviewed, approved and baselined | 02_EVIDENCE_BASE/RQ2_GATES2_3/ | PhD | Supervisor | OPEN |

## G3 — End-to-end laboratory traceability-to-decision demo

**Gate status:** `OPEN — NOT IMPLEMENTED, NOT VALIDATED, NOT OFFICIALLY PASSED`. **Execution authorization:** `EXECUTION-NOT-OPEN` until the G2 package is approved and baselined. Real G1 `Condition_Evidence` may be used only after provenance-complete G1 payload acceptance.

| Gate item | Required artifact | Acceptance criterion | Evidence path | Owner | Reviewer/sign-off | Status |
|---|---|---|---|---|---|---|
| Chain demo | demo | vibration evidence → condition/state-change evidence → BIM-linked component → inspection record → Action_Status → inspection-maintenance action support | bounded prototype | PhD | Supervisor | EXECUTION-NOT-OPEN |
| Paired forward/reverse CQ | test log | Exact expected and actual result sets match; reverse lookup is not mislabeled as round-trip parity | bounded prototype | PhD | Supervisor | EXECUTION-NOT-OPEN |
| Identity/relation tests | test log | Orphan, duplicate, stale/reused ID, wrong type and invalid cardinality are rejected | bounded prototype | PhD | — | EXECUTION-NOT-OPEN |
| Evidence tests | test log | Missing/malformed CEI, missing provenance and stale evidence basis are rejected | bounded prototype | PhD | — | EXECUTION-NOT-OPEN |
| Status/chronology tests | test log | Illegal `Action_Status` transitions and chronology failures are rejected under the approved specification | bounded prototype | PhD | — | EXECUTION-NOT-OPEN |
| Authorization tests | test log | Unauthorized approval/rejection/rework and prohibited self-approval are rejected per approved role matrix | bounded prototype | PhD | Expert/Supervisor | EXECUTION-NOT-OPEN |
| Verification/closure tests | test log | Closure without accepted verification is blocked; valid reopen preserves prior history | bounded prototype | PhD | Expert/Supervisor | EXECUTION-NOT-OPEN |
| Exact oracle validation | implementation-neutral report | Actual violations/results equal preregistered focus IDs, codes and counts | bounded prototype | PhD | Supervisor | EXECUTION-NOT-OPEN |

## G4 — Minimum field mapping & baseline feasibility (Rapexco)

| Gate item | Required artifact | Acceptance criterion | Evidence path | Owner | Reviewer/sign-off | Status |
|---|---|---|---|---|---|---|
| Field-access basis | signed/confirmed agreement | Cơ sở tiếp cận hợp lệ (hard prerequisite) | 02_EVIDENCE_BASE/RQ3_GATE4/ | PhD | Owner/Operator | OPEN |
| Field sensor register | register | Mọi sensor field ghi nhận | 02_EVIDENCE_BASE/RQ3_GATE4/ | PhD | — | OPEN |
| Sensor→BIM mapping | mapping table | `Sensor_ID → BIM_GUID` đầy đủ | 02_EVIDENCE_BASE/RQ3_GATE4/ | PhD | — | OPEN |
| Data return | data log | Dữ liệu về, đo được completeness | 02_EVIDENCE_BASE/RQ3_GATE4/ | PhD | — | OPEN |
| Completeness & drift | QC report | Kiểm tra completeness + drift | 02_EVIDENCE_BASE/RQ3_GATE4/ | PhD | — | OPEN |
| Operational baseline | baseline doc | Baseline vận hành (không áp thời lượng phổ quát) | 02_EVIDENCE_BASE/RQ3_GATE4/ | PhD | — | OPEN |
| Traceability scenarios | 2–3 scenarios | Chạy end-to-end tại field | 02_EVIDENCE_BASE/RQ3_GATE4/ | PhD | Supervisor | OPEN |

**Đây là minimum field feasibility evidence — BẮT BUỘC cho luận án** (kể cả khi Paper 3 không công bố). Không yêu cầu field damage diagnosis.

## G5 — Inspection-action scenario review

| Gate item | Required artifact | Acceptance criterion | Evidence path | Owner | Reviewer/sign-off | Status |
|---|---|---|---|---|---|---|
| 4-level logic | logic doc | Normal→Watch→Inspect→Priority minh bạch, không trọng số | 02_EVIDENCE_BASE/WP4_GATE5/ | PhD | — | OPEN |
| Expert review | review record | Facility-manager/expert rà soát | 02_EVIDENCE_BASE/WP4_GATE5/ | PhD | Expert | OPEN |
| No automated decision | design note | Không quyết định tự động | 02_EVIDENCE_BASE/WP4_GATE5/ | PhD | — | OPEN |
| No field damage conclusion | design note | Không kết luận hư hỏng khi chưa kiểm tra | 02_EVIDENCE_BASE/WP4_GATE5/ | PhD | — | OPEN |

## G6 — Paper 2 submission
| Gate item | Required artifact | Acceptance criterion | Owner | Reviewer | Status |
|---|---|---|---|---|---|
| Paper 2 submitted | submission record | Paper 2 (RQ2, QLXD core) nộp | PhD | Supervisor | OPEN |

## G7 — Thesis synthesis & (when feasible) Paper 3 submission
| Gate item | Required artifact | Acceptance criterion | Owner | Reviewer | Status |
|---|---|---|---|---|---|
| Thesis synthesis | synthesis draft | Tổng hợp 4 lớp bằng chứng | PhD | Supervisor | OPEN |
| Paper 3 (bonus) | submission record | Nộp nếu site window cho phép | PhD | Supervisor | N/A-until-G4 |

---

## Gates KHÔNG tồn tại (prohibited)
calibrated FEM · MAC · EMA · equivalent stiffness · stiffness degradation · FEM sensitivity · optimal sensor placement.

## Trạng thái hiện tại (Claim → Evidence → Limitation → Next action)
- **Claim:** Hệ gate đã chuyển sang execution-gate với artifact + acceptance + sign-off; M1 milestone gắn dưới G1.
- **Evidence:** File này; 17/07 Limited-FEM Charter; ADR-2026-001; Council Review; evidence audits through 11/08/2026.
- **Limitation:** G1 has partial evidence but no signed acceptance; G2 literature boundary is closed but specification is not frozen; G3 is not implemented, validated or passed and execution is not open.
- **Next action:** Materialize and lock the repository-resident `G1_EXECUTION_PACK` from the corrected 216-record canonical dataset, including physical run/sensor registry, hashes and provenance. In parallel, approve G2 competency questions and verification criteria; do not build the schema first.
- **Sync 13/09/2026:**
  - Paper 1 is `SCIENCE LOCKED`; G1 remains `OPEN — PARTIAL EVIDENCE`.
  - The next G1 action is administrative: materialize the pack from existing artefacts without new analysis, obtain decisions C-04 to C-06, and sign `G1_ACCEPTANCE_MATRIX.md`.
  - Research priority moves to P1–P3 (`CURRENT_STATUS_AND_NEXT_DIRECTION.md` v2.4 §7).
