# EVIDENCE GATES — v2.1 (EXECUTION GATES)
**Version:** v2.1 | **Date:** 2026-07-19 | **Status:** CURRENT (dưới Charter v2.1)
**Rule:** Mỗi Gate item là một **execution gate** với artifact bắt buộc + acceptance criterion + evidence path + owner + reviewer/sign-off + status. **Không đánh dấu PASS chỉ vì code chạy thành công.** Không đóng gate bằng giả định. Không tồn tại gate FEM-calibration/MAC/EMA/stiffness/OSP.

**Current gate: G1** — materially strengthened nhưng experimentally OPEN (LORO + ResNet1D provenance pending).
**Status legend:** OPEN · IN-PROGRESS · READY-FOR-REVIEW · PASS (signed) · N/A.

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

---

## G2 — Traceability model & competency questions

| Gate item | Required artifact | Acceptance criterion | Evidence path | Owner | Reviewer/sign-off | Status |
|---|---|---|---|---|---|---|
| Identifier schema | schema doc | `Sensor_ID → BIM_GUID → Condition_Evidence_ID → Inspection_Record_ID → Action_Record_ID` | 02_EVIDENCE_BASE/RQ2_GATES2_3/ | PhD | Supervisor | OPEN |
| CEI attribute structure | CEI spec | Metadata fields (validity, model confidence, run/fold variability, sensor config, data-quality, provenance, timestamp/version); không scalar | 02_EVIDENCE_BASE/RQ2_GATES2_3/ | PhD | Supervisor | OPEN |
| Action_Record schema | schema doc | `Action_Record_ID` truy được evidence, CEI, component, inspection record, role, timestamp, version, approval status, management/legal ref | 02_EVIDENCE_BASE/RQ2_GATES2_3/ | PhD | Supervisor | OPEN |
| SCQ/VCQ/RCQ | pre-registration doc | Pre-registered TRƯỚC khi build schema/demo | 02_EVIDENCE_BASE/RQ2_GATES2_3/ | PhD | Supervisor | OPEN |
| Acceptance criteria | criteria doc | Tiêu chí chấp nhận cho từng CQ | 02_EVIDENCE_BASE/RQ2_GATES2_3/ | PhD | Supervisor | OPEN |
| Inspection_Record schema | minimum schema | Trường tối thiểu + role + approval status | 02_EVIDENCE_BASE/RQ2_GATES2_3/ | PhD | Supervisor | OPEN |

## G3 — End-to-end laboratory traceability-to-decision demo

| Gate item | Required artifact | Acceptance criterion | Evidence path | Owner | Reviewer/sign-off | Status |
|---|---|---|---|---|---|---|
| Chain demo | demo | evidence → CEI → BIM component → inspection record → Action_Record | lab demo repo | PhD | Supervisor | OPEN |
| Round-trip | test log | Truy vết hai chiều đầy đủ | lab demo repo | PhD | — | OPEN |
| Orphan-ID test | test log | Phát hiện id mồ côi | lab demo repo | PhD | — | OPEN |
| Duplicate-ID test | test log | Phát hiện id trùng | lab demo repo | PhD | — | OPEN |
| Missing-CEI test | test log | Phát hiện evidence thiếu CEI | lab demo repo | PhD | — | OPEN |
| Invalid-data validation | SHACL-or-equivalent report | Ràng buộc validation chạy, bắt lỗi | lab demo repo | PhD | Supervisor | OPEN |

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
- **Evidence:** File này; Charter v2.1; matrix v2.1; ADR Action_ID.
- **Limitation:** G1 chưa PASS (LORO, ResNet1D provenance); G2 cần pre-register CQ; G3–G7 mở; artifacts G1 chưa khởi tạo.
- **Next action:** khởi tạo `G1_EXECUTION_PACK/`; khóa run registry → LORO → ResNet1D provenance → run-level uncertainty; ký G1_ACCEPTANCE_MATRIX; song song pre-register SCQ/VCQ/RCQ + CEI/Action_Record schema.
