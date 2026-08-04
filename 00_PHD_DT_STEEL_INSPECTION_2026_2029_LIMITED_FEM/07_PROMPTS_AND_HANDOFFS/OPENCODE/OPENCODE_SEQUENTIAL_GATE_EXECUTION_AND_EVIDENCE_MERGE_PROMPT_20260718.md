# PROMPT ĐIỀU PHỐI OPENCODE + ZOTERO MCP
## Thực hiện tuần tự Gate 1 → Gate 5 và hợp nhất nguồn mới vào hệ thống dữ liệu hiện hành

**Ngày:** 2026-07-18  
**Chế độ:** Sequential execution — non-destructive — evidence-controlled  
**Ngôn ngữ báo cáo:** Tiếng Việt  
**Mục tiêu:** Hoàn tất writeback Zotero, hợp nhất 19 nguồn deep-read mới vào nguồn dữ liệu hiện hành, sau đó triển khai lần lượt Gate 1 → Gate 5 mà không mở rộng phạm vi nghiên cứu.

---

## 0. KIẾN TRÚC NGHIÊN CỨU KHÓA

### RQ/WP/Paper/Gate

| Trục | Nội dung |
|---|---|
| RQ1 / WP1 / Paper 1 | Laboratory vibration evidence |
| Gate 1 | Run registry, leakage-safe evaluation, LORO, ResNet1D provenance |
| RQ2 / WP2 / Paper 2 | Evidence-to-inspection traceability |
| Gate 2 | Competency questions, schema requirements, constraints |
| Gate 3 | End-to-end laboratory traceability implementation |
| RQ3 / WP3 / Paper 3 | Field feasibility |
| Gate 4 | Sensor mapping, operational baseline, field traceability |
| WP4 / Paper 4-support | Human-reviewed decision support |
| Gate 5 | Scenario validation for four-level action workflow |

**Không có RQ4.**

### Chuỗi nghiên cứu khóa

```text
Vibration data
→ condition/state-change evidence
→ BIM-linked component
→ inspection record
→ inspection-maintenance action support
```

### Chuỗi định danh khóa

```text
Sensor_ID
→ BIM_GUID
→ Condition_Evidence_ID
→ Inspection_Record_ID
→ Action_Status
```

### Vai trò FEM

FEM chỉ được mô tả là:

> nominal, uncalibrated, reference-only, not used for damage diagnosis.

Không được tạo RQ, WP, chương, Paper hoặc Evidence Gate cho FEM.

### Ngoài phạm vi

Không mở rộng sang:

- calibrated FEM;
- stiffness-degradation inference;
- bolt-preload inference;
- field damage diagnosis;
- direct lab-to-field classifier transfer;
- RUL;
- predictive maintenance;
- Edge AI;
- Smart City;
- weighted Health Index;
- autonomous maintenance;
- commercial software development;
- optimal sensor placement.

---

## 1. SOURCE OF TRUTH PHẢI ĐỌC TRƯỚC

Đọc theo thứ tự:

1. `MASTER_RESEARCH_CHARTER.md`
2. `MASTER_RESEARCH_CHARTER_v1.1_LIMITED_FEM_20260717.md`
3. `RESEARCH_DIRECTION_AND_SCOPE.md`
4. `RESEARCH_ARCHITECTURE.md`
5. `CURRENT_STATUS_AND_NEXT_DIRECTION.md`
6. `RESEARCH_ARCHITECTURE_DECISION_RECORD_20260717.md`
7. `LIVING_EVIDENCE_BASE_v1.1_LIMITED_FEM.md`
8. `01_LIVING_EVIDENCE_BASE_v1.2_LIMITED_FEM_20260718.md`
9. `02_NEW_DEEP_READ_EVIDENCE_MATRIX_20260718.csv`
10. `03_RQ1_GATE1_METHOD_EVIDENCE_ADDENDUM_v1.0_20260718.md`
11. `04_RQ2_TRACEABILITY_EVIDENCE_ADDENDUM_v1.2_20260718.md`
12. `05_RQ3_FIELD_FEASIBILITY_EVIDENCE_ADDENDUM_v1.0_20260718.md`
13. `06_WP4_DECISION_SUPPORT_EVIDENCE_ADDENDUM_v1.0_20260718.md`
14. `07_CLOSEST_COMPETITOR_MATRIX_PAPER2_20260718.csv`
15. `08_DUPLICATE_AND_METADATA_CORRECTION_LOG_20260718.csv`
16. `09_ZOTERO_DEEP_READ_COMPLETION_REPORT_20260718.md`
17. `10_ZOTERO_WRITEBACK_QUEUE_20260718.md`
18. `MASTER_INDEX_CURRENT_v1.1.md`
19. `TERMINOLOGY_CONTROL_v1.1.md`

Khi có mâu thuẫn:

```text
Supervisor-approved Charter/ADR
> current Research Direction
> Living Evidence Base
> addenda
> older files
```

---

# PHASE 0 — AN TOÀN, BACKUP VÀ KIỂM TRA MÔI TRƯỜNG

## 0.1. Kiểm tra kết nối

Xác minh:

- Zotero MCP đọc được library;
- `ZOTERO_API_KEY` tồn tại qua environment variable;
- `ZOTERO_LIBRARY_ID` tồn tại qua environment variable;
- quyền ghi được bật;
- không ghi trực tiếp vào Zotero SQLite;
- không in API key vào log hoặc file;
- không commit secrets vào Git.

## 0.2. Backup

Tạo:

```text
BACKUP_BEFORE_WRITEBACK_20260718/
```

Sao lưu:

- current Master Index;
- Living Evidence Base v1.1 và v1.2;
- các addendum;
- metadata export hiện tại;
- danh sách Zotero item keys;
- duplicate log;
- writeback queue.

## 0.3. Dry run

Chọn một item deep-read có metadata ổn định và thử:

- thêm tag;
- thêm child note;
- đọc lại item;
- xác minh note/tag được ghi đúng.

Nếu dry run thất bại:

```text
STOP
→ ghi lỗi
→ không tiếp tục writeback hàng loạt
```

---

# PHASE 1 — ZOTERO WRITEBACK VÀ HỢP NHẤT NGUỒN MỚI

## 1.1. Thực hiện writeback

Dùng `10_ZOTERO_WRITEBACK_QUEUE_20260718.md` để:

- thêm child notes;
- thêm tags;
- sửa metadata;
- đánh dấu duplicate/counterpart;
- không xóa item;
- không gắn `DEEP_READ` cho PDF thiếu, preview hoặc sai file;
- không tạo tag `RQ4`.

## 1.2. Xử lý duplicate và version conflict

Áp dụng:

- canonical: `GE3XSAYV`, `Z4IBWW9Y`, `YGZ32C8M`;
- non-independent counterpart: `2RB2YRBW`, `P674U5V2`, `EN2SIFMC`;
- `ZLFATP2Z`: tách conference parent và journal-extension PDF;
- `43648CQ8`: gỡ PDF sai khỏi claim evidence, giữ trạng thái `FULLTEXT_UNAVAILABLE`;
- không xóa duplicate tự động.

## 1.3. Chuẩn hóa metadata

Chỉ sửa theo:

```text
08_DUPLICATE_AND_METADATA_CORRECTION_LOG_20260718.csv
```

Mỗi chỉnh sửa phải có:

- old value;
- new value;
- source used to verify;
- Zotero key;
- timestamp;
- writeback status.

## 1.4. Hợp nhất 19 nguồn mới vào nguồn dữ liệu hiện hành

Không để 19 nguồn mới chỉ tồn tại trong file addendum.

Tạo mới:

```text
LIVING_EVIDENCE_BASE_v1.3_CONSOLIDATED_20260718.md
```

File này phải hợp nhất:

- 33 substantive/limited records của v1.1;
- 19 complete new deep-read records;
- retained normative/supporting sources;
- duplicate controls;
- metadata corrections;
- claim register cũ và mới;
- RQ/WP/Paper/Gate mapping;
- Evidence Role;
- Evidence Type;
- Allowed Claim;
- Prohibited Inference;
- Relevant Pages;
- status of missing full texts.

Không ghi đè v1.1 hoặc v1.2.

## 1.5. Cập nhật dữ liệu điều hướng hiện hành

Tạo/cập nhật:

```text
MASTER_INDEX_CURRENT_v1.2.md
LITERATURE_REVIEW_MASTER_INDEX_CURRENT_v1.2.md
ZOTERO_CANONICAL_RECORD_REGISTER_v1.2.csv
CLAIM_EVIDENCE_REGISTER_CURRENT_v1.2.csv
```

Master Index mới phải trỏ tới:

- Living Evidence Base v1.3 consolidated;
- current addenda;
- current competitor matrix;
- duplicate log;
- current Gate status;
- missing-full-text tracker.

Đánh dấu:

```text
v1.1 = historical
v1.2 = transitional update
v1.3 = consolidated current candidate
```

Chỉ gắn `CURRENT_APPROVED` sau khi hoàn thành quality review.

## 1.6. Chuẩn hóa evidence matrix

Tạo:

```text
NEW_DEEP_READ_EVIDENCE_MATRIX_v1.1_NORMALIZED_20260718.csv
```

Sửa cấu trúc:

- tách `RQ` và `Synthesis_WP`;
- dùng `Primary_Gate`;
- dùng `Supporting_Gate`;
- tách `PDF_Pages`;
- tách `Published_Pages`;
- thêm `Section_Table_Figure`;
- thêm `Canonical_Status`;
- thêm `Writeback_Status`;
- thêm `Fulltext_Status`.

## 1.7. Báo cáo Phase 1

Tạo:

```text
PHASE1_ZOTERO_WRITEBACK_AND_CONSOLIDATION_REPORT_20260718.md
```

Chỉ chuyển Phase 2 khi:

- writeback hoàn tất hoặc lỗi được xác định rõ;
- 19 nguồn mới đã nằm trong consolidated evidence base;
- Master Index đã trỏ đúng;
- duplicate log đã cập nhật;
- no false `DEEP_READ` tags.

---

# PHASE 2 — ĐÓNG GATE 1

## 2.1. Mục tiêu

Khóa RQ1/WP1/Paper 1 bằng project evidence, không chỉ literature evidence.

## 2.2. Bắt buộc thực hiện theo thứ tự

### Bước 1 — Run registry

Tạo:

```text
RUN_REGISTRY_LOCKED_v1.0.csv
RUN_REGISTRY_AUDIT_REPORT_v1.0.md
```

Tối thiểu có:

- Run_ID;
- State;
- Excitation;
- Sensor_Mode;
- Sensor_ID;
- Date/time;
- Source file;
- sampling rate;
- duration;
- channel count;
- preprocessing status;
- quality flag;
- inclusion/exclusion status;
- reason.

Không tiếp tục nếu số run/class chưa xác minh.

### Bước 2 — Dataset dictionary

Tạo:

```text
DATASET_DICTIONARY_GATE1_v1.0.md
DATASET_FILE_MANIFEST_GATE1_v1.0.csv
```

### Bước 3 — ResNet1D provenance

Xác minh:

- code version;
- sensor mode;
- input channels;
- folds;
- seeds;
- preprocessing;
- checkpoint;
- metric calculation;
- data source.

Tạo:

```text
RESNET1D_PROVENANCE_AUDIT_v1.0.md
```

Nếu không xác minh được:

```text
FORMALLY_EXCLUDE_RESNET1D
```

khỏi fair comparison.

### Bước 4 — Pre-register analysis protocol

Tạo:

```text
GATE1_RUN_AWARE_ANALYSIS_PROTOCOL_v1.0.md
```

Phải khóa:

- split by Run_ID;
- split before windowing;
- train-only normalization;
- identical folds across models/sensors;
- identical seeds/budget;
- primary metrics;
- confusion matrix;
- run-level outputs;
- group-preserving permutation;
- effect-size reporting;
- sensitivity analyses;
- ResNet1D inclusion/exclusion rule.

Không dùng individual windows làm đơn vị inference.

### Bước 5 — Execute LORO

Xuất:

```text
LORO_FOLD_REGISTRY.csv
LORO_PREDICTIONS_BY_RUN.csv
LORO_METRICS_BY_RUN.csv
LORO_CONFUSION_MATRICES/
LORO_MODEL_SENSOR_COMPARISON.csv
LEAKAGE_AUDIT_REPORT.md
```

### Bước 6 — Gate 1 decision

Tạo:

```text
GATE1_CLOSURE_REVIEW_20260718.md
```

Theo cấu trúc:

```text
Claim
→ Evidence
→ Limitation
→ Decision
→ Next action
```

Không tự đóng Gate 1 nếu artifact chưa đầy đủ.

## 2.3. Cập nhật evidence system sau Gate 1

Nếu có project evidence mới:

- cập nhật `LIVING_EVIDENCE_BASE_v1.3_CONSOLIDATED_20260718.md` thành bản mới có version tăng;
- cập nhật `CLAIM_EVIDENCE_REGISTER_CURRENT`;
- cập nhật RQ1 Addendum;
- cập nhật Gate matrix;
- cập nhật Master Index;
- cập nhật Paper 1 evidence package.

Không ghi đè file cũ; tăng version.

---

# PHASE 3 — PRE-REGISTER GATE 2

Chỉ bắt đầu sau khi Phase 2 có trạng thái rõ.

## 3.1. Thu thập bốn full text còn thiếu

Ưu tiên:

- `3II2WKLN`;
- `NUTL57KJ`;
- `Z4IBWW9Y`;
- đúng PDF của `43648CQ8`.

Nếu không có:

```text
Evidence is currently insufficient.
```

Không suy diễn từ abstract.

## 3.2. Mở rộng competitor matrix

Cập nhật:

```text
CLOSEST_COMPETITOR_MATRIX_PAPER2_v1.1.csv
```

Bắt buộc thêm các canonical sources cũ:

- Rio et al. 2013;
- Theiler & Smarsly 2018;
- Valinejadshoubi et al. 2019;
- Heaton & Parlikad 2020;
- Deng et al. 2022;
- Li et al. 2023;
- Chen et al. 2014;
- các nguồn sensor–BIM/inspection/provenance trong v1.1.

Các cột:

```text
Raw sensor data
Derived condition evidence
BIM/IFC identifier
Inspection record
Action status
Status history
Provenance
Bidirectional query
Competency questions
Constraint validation
Invalid-data tests
Study object
Validation type
```

## 3.3. Thiết kế CQ

Tạo:

```text
GATE2_COMPETENCY_QUESTION_REGISTER_v1.0.md
```

Phân loại:

- SCQ;
- VCQ;
- RCQ.

Mỗi CQ phải có:

- CQ_ID;
- business question;
- scope;
- actors;
- required entities;
- relationship;
- direction;
- expected answer;
- failure condition;
- linked Claim ID;
- linked Gate criterion;
- planned executable query.

## 3.4. Constraint tests

Tạo:

```text
GATE2_CONSTRAINT_TEST_REGISTER_v1.0.md
GATE2_INVALID_DATA_FIXTURES_v1.0.csv
```

Bắt buộc có:

- orphan Sensor_ID;
- missing BIM_GUID;
- duplicate Condition_Evidence_ID;
- evidence without source run;
- inspection record without component;
- action status without inspection record;
- status transition without actor/time/reason;
- reverse query mismatch;
- cardinality violation.

## 3.5. Pre-registration decision

Tạo:

```text
GATE2_PREREGISTRATION_PACKAGE_v1.0.md
GATE2_APPROVAL_REQUEST_FOR_SUPERVISORS_v1.0.md
```

Không xây schema/demo trước khi CQ và constraints được phê duyệt.

## 3.6. Cập nhật evidence system

Sau khi pre-register:

- cập nhật RQ2 Addendum;
- cập nhật Gate matrix;
- cập nhật Master Index;
- cập nhật consolidated Living Evidence Base;
- ghi rõ literature evidence khác project design evidence.

---

# PHASE 4 — GATE 3: END-TO-END LAB TRACEABILITY

Chỉ bắt đầu khi Gate 2 đã được phê duyệt.

## 4.1. Formal schema

Tạo:

```text
TRACEABILITY_SCHEMA_v1.0.md
TRACEABILITY_ENTITY_RELATIONSHIP_MODEL_v1.0.md
TRACEABILITY_IDENTIFIER_DICTIONARY_v1.0.csv
```

Bắt buộc có:

- Sensor_ID;
- Run_ID;
- BIM_GUID;
- Condition_Evidence_ID;
- Inspection_Record_ID;
- Action_Status_Event_ID;
- Action_Status;
- source/provenance fields;
- cardinality;
- required/optional attributes.

## 4.2. Lab implementation

Tạo lab case fixtures và chạy:

- forward query;
- reverse query;
- invalid-data test;
- status-history test;
- provenance test;
- competency-question test.

Xuất:

```text
GATE3_LAB_TRACEABILITY_TEST_RESULTS.csv
GATE3_QUERY_RESULTS/
GATE3_INVALID_DATA_TEST_REPORT.md
GATE3_BIDIRECTIONAL_TRACEABILITY_REPORT.md
```

## 4.3. Gate 3 review

Tạo:

```text
GATE3_CLOSURE_REVIEW.md
```

Không tuyên bố Paper 2 hoàn chỉnh nếu test chưa tái lập được.

---

# PHASE 5 — GATE 4: FIELD FEASIBILITY

Chỉ bắt đầu khi:

- thỏa thuận field được xác nhận;
- Gate 2 schema đã khóa;
- Gate 3 lab traceability hoạt động.

## 5.1. Field readiness

Tạo:

```text
FIELD_ACCESS_CONFIRMATION_REGISTER.md
FIELD_SENSOR_REGISTER_v1.0.csv
FIELD_SENSOR_TO_BIM_MAPPING_v1.0.csv
FIELD_DEPLOYMENT_PROTOCOL_v1.0.md
FIELD_DATA_QUALITY_PLAN_v1.0.md
```

## 5.2. Sensor qualification

Kiểm tra:

- noise floor;
- sampling stability;
- timing synchronization;
- missing data;
- storage;
- drift;
- channel identity;
- ambient-signal adequacy.

## 5.3. Operational baseline

Không đặt một thời gian baseline cố định trước.

Định nghĩa:

- completeness criteria;
- environmental metadata;
- operational metadata;
- exclusion rules;
- drift/fault rules;
- baseline coverage;
- alert policy.

## 5.4. Alert-to-inspection workflow

Tạo:

```text
FIELD_ALERT_TO_INSPECTION_PROTOCOL_v1.0.md
FIELD_TRACEABILITY_SCENARIO_REGISTER_v1.0.csv
```

Mọi anomaly:

```text
→ evidence
→ human review
→ inspection request
```

Không được:

```text
anomaly → damage diagnosis
```

## 5.5. Gate 4 review

Tạo:

```text
GATE4_FIELD_FEASIBILITY_REVIEW.md
```

---

# PHASE 6 — GATE 5: WP4 DECISION-SUPPORT VALIDATION

Chỉ bắt đầu khi đã có traceability chain hoạt động.

## 6.1. Four-level logic

Thiết kế:

```text
Normal
→ Watch
→ Inspect
→ Priority Inspection
```

Đây là thiết kế của luận án, không phải thang đã được literature xác nhận.

Không dùng:

- weighted Health Index;
- AHP;
- Markov deterioration;
- automated optimization;
- RUL;
- predictive maintenance.

## 6.2. Scenario protocol

Tạo:

```text
GATE5_SCENARIO_REGISTER_v1.0.csv
GATE5_FACILITY_MANAGER_REVIEW_FORM_v1.0.md
GATE5_ACTION_STATUS_STATE_MACHINE_v1.0.md
```

Mỗi scenario phải lưu:

- input evidence;
- baseline/context;
- rule version;
- expected action;
- actual action;
- reviewer;
- comments;
- prior/new status;
- reason;
- timestamp;
- discrepancy.

## 6.3. Gate 5 review

Tạo:

```text
GATE5_DECISION_VALIDITY_REVIEW.md
```

Không đóng Gate nếu chưa có human review.

---

# PHASE 7 — HỢP NHẤT CUỐI VÀ QUẢN TRỊ NGUỒN DỮ LIỆU

Sau mỗi Phase, phải cập nhật hệ thống hiện hành, không tạo silo.

## 7.1. Các nguồn dữ liệu phải cập nhật

- Living Evidence Base current version;
- Claim–Evidence Register;
- Zotero notes/tags;
- Master Index;
- Literature Review Master Index;
- RQ/WP/Paper/Gate matrix;
- Evidence Gates status;
- duplicate log;
- unresolved-item tracker;
- Paper-specific evidence package;
- current status and next direction.

## 7.2. Quy tắc versioning

Không ghi đè file đã phát hành.

Dùng:

```text
v1.1 → v1.2 → v1.3
```

Mỗi file mới phải có:

- previous version;
- change summary;
- reason;
- files superseded;
- current status;
- approval status.

## 7.3. Trạng thái source of truth

Chỉ gắn:

```text
CURRENT_APPROVED
```

khi:

- nội dung đã hợp nhất;
- metadata đúng;
- duplicate đã xử lý;
- links hoạt động;
- supervisor approval được ghi nhận nếu cần.

Nếu chưa:

```text
CURRENT_CANDIDATE
```

---

# BÁO CÁO SAU MỖI PHASE

Mỗi báo cáo phải dùng:

```text
Claim
→ Evidence
→ Limitation
→ Next action
```

Và có bảng:

| Mục | Trạng thái |
|---|---|
| Completed | |
| Partial | |
| Blocked | |
| Evidence insufficient | |
| Files created | |
| Existing files updated | |
| Zotero writeback | |
| Gate effect | |
| Next authorized phase | |

Không tự chuyển sang Phase kế tiếp nếu completion criteria chưa đạt.

---

# STOP RULES

Dừng ngay khi:

- source of truth mâu thuẫn;
- API writeback lỗi;
- metadata không xác minh được;
- full text thiếu nhưng task yêu cầu claim chi tiết;
- Gate trước chưa đạt;
- yêu cầu chạm Out of Scope;
- project evidence chưa có nhưng được yêu cầu đánh dấu COMPLETE.

Không được tự bịa citation, DOI, page, metric, result hoặc Gate status.

---

# FINAL DELIVERABLES

Sau toàn bộ chuỗi, tạo:

```text
FINAL_RESEARCH_EVIDENCE_AND_GATE_STATUS_REPORT.md
FINAL_MASTER_INDEX_CURRENT.md
FINAL_LIVING_EVIDENCE_BASE_CURRENT.md
FINAL_CLAIM_EVIDENCE_REGISTER.csv
FINAL_ZOTERO_CANONICAL_REGISTER.csv
FINAL_UNRESOLVED_ITEMS_TRACKER.md
```

Báo cáo cuối phải nêu:

1. Số nguồn canonical;
2. Số deep-read;
3. Số duplicate;
4. Số metadata sửa;
5. Gate đã đóng;
6. Gate còn mở;
7. Evidence còn thiếu;
8. Các claim được phép;
9. Các claim bị cấm;
10. Ba hành động tiếp theo.

Không thay đổi Charter hoặc định hướng Limited-FEM.
