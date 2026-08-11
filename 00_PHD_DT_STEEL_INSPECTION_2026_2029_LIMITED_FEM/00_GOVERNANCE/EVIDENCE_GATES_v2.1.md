# EVIDENCE GATES — v2.1 (EXECUTION GATES)
**Version:** v2.2 | **Issued:** 2026-07-19 | **Updated:** 2026-08-04
**Status:** CURRENT | **Source-of-truth level:** 4
**Supersedes:** v2.1 execution-gate wording. | **Superseded by:** None.
**Change summary:** Reconciles gate status with execution authorization, adds the G2 decision/schema/oracle prerequisites and G3 event/authorization/verification tests; no gate is marked PASS.
**Rule:** Mỗi Gate item là một **execution gate** với artifact bắt buộc + acceptance criterion + evidence path + owner + reviewer/sign-off + status. **Không đánh dấu PASS chỉ vì code chạy thành công.** Không đóng gate bằng giả định. Không tồn tại gate FEM-calibration/MAC/EMA/stiffness/OSP.

**Current priority: G1** — `OPEN — PARTIAL EVIDENCE`; canonical registry, leakage-safe LORO/multi-seed evaluation, ResNet1D provenance, uncertainty and sign-off remain missing.
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

---

## G2 — Traceability model & competency questions

**Gate status:** `OPEN — LITERATURE BOUNDARY CLOSED, SPECIFICATION NOT YET FROZEN`. The corpus-bounded `CLOSE_SEARCH` decision is not G2 PASS.

| Gate item | Required artifact | Acceptance criterion | Evidence path | Owner | Reviewer/sign-off | Status |
|---|---|---|---|---|---|---|
| G2 Final Decision Register | reviewed register | Every FREEZE/FREEZE_PROVISIONALLY/EXPERT_REVIEW_REQUIRED/WAIT_FOR_G1_PAYLOAD/REMOVE item has basis, owner and approval state | 02_EVIDENCE_BASE/CURRENT/ | PhD | Supervisor | OPEN |
| Action-Status-Event ADR | accepted ADR or explicit unresolved decision | Proposed ADR reviewed; no proposed rule treated as accepted | 00_GOVERNANCE/ | PhD | Supervisor | OPEN |
| Identifier governance | schema doc | `Sensor_ID → BIM_GUID / Asset_ID @ Model_Version_ID → Condition_Evidence_ID → Inspection_Record_ID → Action_Record_ID`; no `Action_Status` identifier; no unnecessary `Component_ID` | 02_EVIDENCE_BASE/RQ2_GATES2_3/ | PhD | Supervisor | OPEN |
| CEI attribute structure | CEI spec | Metadata fields (validity, model confidence, run/fold variability, sensor config, data-quality, provenance, timestamp/version); không scalar | 02_EVIDENCE_BASE/RQ2_GATES2_3/ | PhD | Supervisor | OPEN |
| Action_Record schema | schema doc | `Action_Record_ID` truy được evidence, CEI, component, inspection record, role, timestamp, version, approval status, management/legal ref | 02_EVIDENCE_BASE/RQ2_GATES2_3/ | PhD | Supervisor | OPEN |
| SCQ/VCQ/RCQ | pre-registration doc | Pre-registered TRƯỚC khi build schema/demo | 02_EVIDENCE_BASE/RQ2_GATES2_3/ | PhD | Supervisor | OPEN |
| Acceptance criteria | criteria doc | Tiêu chí chấp nhận cho từng CQ | 02_EVIDENCE_BASE/RQ2_GATES2_3/ | PhD | Supervisor | OPEN |
| Inspection_Record schema | minimum schema | Trường tối thiểu + role + approval status | 02_EVIDENCE_BASE/RQ2_GATES2_3/ | PhD | Supervisor | OPEN |
| Status_Event schema | minimum event model | Append-only event identity, action relation, prior/new status, actor/role, time, reason, version and authorization context | 02_EVIDENCE_BASE/RQ2_GATES2_3/ | PhD | Supervisor | OPEN |
| Verification and closure rules | specification | Post-action verification required; `completed` alone cannot close; closure/reopen guards explicit | 02_EVIDENCE_BASE/RQ2_GATES2_3/ | PhD | Supervisor/Expert | OPEN |
| CQ Registry and expected answers | preregistration | Paired forward/reverse CQs, exact expected answers and query-answer parity distinguished from transformation round-trip | 02_EVIDENCE_BASE/RQ2_GATES2_3/ | PhD | Supervisor | OPEN |
| Constraint Catalogue | versioned catalogue | Identity, relation, chronology, transition, authorization, evidence and closure families fixed | 02_EVIDENCE_BASE/RQ2_GATES2_3/ | PhD | Supervisor | OPEN |
| Fixture/Oracle Manifest | machine-readable or versioned manifest | Controlled valid/invalid fixtures, isolated mutations, expected focus IDs/codes/counts and exact expected-vs-actual rule | 02_EVIDENCE_BASE/RQ2_GATES2_3/ | PhD | Supervisor | OPEN |
| G2 baseline/sign-off | approval record | Complete internally consistent package reviewed, approved and baselined | 02_EVIDENCE_BASE/RQ2_GATES2_3/ | PhD | Supervisor | OPEN |

## G3 — End-to-end laboratory traceability-to-decision demo

**Gate status:** `OPEN — NOT IMPLEMENTED, NOT VALIDATED, NOT OFFICIALLY PASSED`. **Execution authorization:** `EXECUTION-NOT-OPEN` until the G2 package is approved and baselined. Real G1 `Condition_Evidence` may be used only after provenance-complete G1 payload acceptance.

| Gate item | Required artifact | Acceptance criterion | Evidence path | Owner | Reviewer/sign-off | Status |
|---|---|---|---|---|---|---|
| Chain demo | demo | evidence → CEI → BIM component → inspection record → Action_Record → Status_Event → review/authorization → verification/guarded closure | bounded prototype | PhD | Supervisor | EXECUTION-NOT-OPEN |
| Paired forward/reverse CQ | test log | Exact expected and actual result sets match; reverse lookup is not mislabeled as round-trip parity | bounded prototype | PhD | Supervisor | EXECUTION-NOT-OPEN |
| Identity/relation tests | test log | Orphan, duplicate, stale/reused ID, wrong type and invalid cardinality are rejected | bounded prototype | PhD | — | EXECUTION-NOT-OPEN |
| Evidence tests | test log | Missing/malformed CEI, missing provenance and stale evidence basis are rejected | bounded prototype | PhD | — | EXECUTION-NOT-OPEN |
| Event/chronology tests | test log | Illegal transition, ordering and current-state reconstruction failures are rejected | bounded prototype | PhD | — | EXECUTION-NOT-OPEN |
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
- **Evidence:** File này; Charter v2.1; matrix v2.1; ADR Action_ID.
- **Limitation:** G1 has partial evidence but no signed acceptance; G2 literature boundary is closed but specification is not frozen; G3 is not implemented, validated or passed and execution is not open.
- **Next action:** lock canonical run/sensor provenance → leakage-safe multi-seed LORO → ResNet1D provenance decision → run/fold uncertainty → G1 sign-off; in parallel review the Action-Status-Event ADR and complete the G2 Decision Register, ER model, CQ/expected answers, Constraint Catalogue, Fixture/Oracle Manifest, expert review and baseline.
