# ROADMAP THỰC THI LUẬN ÁN PhD
## Data-informed Digital Twin phục vụ giám sát trạng thái và hỗ trợ kiểm tra – bảo trì nhà công nghiệp khung thép ven biển

**Lĩnh vực:** Quản lý xây dựng / Quản lý tài sản  
**Kiến trúc nghiên cứu:** Limited-FEM  
**Giai đoạn:** 2026–2029  
**Trạng thái:** Roadmap điều hành theo Evidence Gate  
**Ngày cập nhật:** 03/08/2026  

---

# 1. KHỐI ĐỊNH VỊ

| Thành phần | Nội dung |
|---|---|
| Chuỗi nghiên cứu | Dữ liệu dao động → bằng chứng trạng thái → cấu kiện BIM → hồ sơ kiểm tra → hỗ trợ hành động |
| Chuỗi định danh | `Sensor_ID → BIM_GUID → Condition_Evidence_ID → Inspection_Record_ID → Action_Status` |
| Đóng góp trung tâm | Mô hình truy vết component-level có thể kiểm chứng |
| FEM | Nominal, uncalibrated, reference-only, not used for damage diagnosis |
| Gate hiện tại | G1 chưa đóng; G2 chưa đóng |
| Mốc BIM hiện tại | `READY TO FREEZE PSET EXPORT SETUP` |
| Ưu tiên số 1 | Run registry → LORO → xác nhận sensor mode ResNet1D |
| Ưu tiên song song | Pre-register competency questions và khóa schema RQ2 |

Luận án không tuyên bố predictive maintenance, RUL, field damage diagnosis, calibrated FEM, stiffness-degradation inference, optimal sensor placement hoặc autonomous maintenance.

---

# 2. RQ – WP – CHƯƠNG – PAPER – GATE

| RQ | WP | Chương | Paper | Gate | Evidence |
|---|---|---|---|---|---|
| RQ1 | WP1 | Chương 4 | Paper 1 | G1 | Laboratory evidence |
| RQ2 | WP2 | Chương 5 | Paper 2 | G2–G3 | Information traceability |
| RQ3 | WP3 | Chương 6 | Paper 3 | G4 | Field feasibility |
| Tổng hợp | WP4 | Chương 7 | Paper 4 hoặc tích hợp Paper 3 | G5 | Decision support |
| Toàn luận án | Tổng hợp | Chương 8 | Thesis synthesis | G6–G7 | Evidence chain hoàn chỉnh |

## RQ1

Dữ liệu dao động từ khung thép 1:10 và các cấu hình cảm biến khác nhau có thể tạo bằng chứng phân biệt các trạng thái liên kết kiểm soát đáng tin cậy đến mức nào dưới giao thức run-aware, chống rò rỉ?

## RQ2

Bằng chứng trạng thái được tổ chức và liên kết với cấu kiện BIM và hồ sơ kiểm tra như thế nào để bảo đảm truy vết cấp cấu kiện?

## RQ3

Khung Digital Twin dựa trên dữ liệu có thể hỗ trợ lựa chọn và ghi nhận hành động kiểm tra tại công trình thực như thế nào khi dữ liệu hư hỏng hiện trường còn hạn chế?

---

# 3. PHẠM VI

## Core Scope

- dữ liệu rung phòng thí nghiệm;
- run-aware/LORO;
- condition evidence;
- component-level BIM traceability;
- Inspection_Record;
- field feasibility;
- logic `Normal → Watch → Inspect → Priority Inspection`;
- human-in-the-loop review.

## Supporting Scope

- Revit;
- IFC4X3;
- Shared Parameters;
- Dynamo;
- IfcOpenShell;
- IDS/IfcTester;
- AIM information semantics;
- ISO 19650 và TCVN 14177;
- nominal FEM tham chiếu vị trí cảm biến.

## Future Work

- calibrated FEM;
- ontology/knowledge graph quy mô lớn;
- bolt-level asset management;
- multi-building AIM;
- RUL;
- predictive maintenance;
- Edge AI;
- commercial platform.

## Out of Scope

- CFD;
- Smart City;
- direct lab-to-field classifier transfer;
- field damage diagnosis;
- weighted Health Index;
- autonomous maintenance.

---

# 4. KIẾN TRÚC BẰNG CHỨNG

```text
Lớp 1 — Laboratory evidence
Vibration data → controlled-state evidence → run-aware validity

Lớp 2 — Information traceability
Evidence → Sensor_ID → BIM_GUID → Inspection_Record → Action_Status

Lớp 3 — Field feasibility
Field sensor → baseline → traceability scenario → inspection workflow

Lớp 4 — Decision support
Evidence + context + human review → action level
```

Nguyên tắc:

1. Lab evidence không thay field evidence.
2. IFC readiness không thay traceability validity.
3. Field deployment không đồng nghĩa damage diagnosis.
4. Decision support không đồng nghĩa autonomous maintenance.

---

# 5. ROADMAP 2026–2029

| Pha | Thời gian đề xuất | Mục tiêu | Gate |
|---|---|---|---|
| P0 | 08–10/2026 | Khóa G1, pre-register G2 | G1 + thiết kế G2 |
| P1 | 10/2026–03/2027 | Khóa traceability model và BIM identity | G2 |
| P2 | 03–08/2027 | End-to-end lab traceability | G3 |
| P3 | 2027–2028 | Field deployment và baseline | G4 |
| P4 | 2028 | Decision-support review | G5 |
| P5 | 2028–2029 | Papers, synthesis, defense | G6–G7 |

Thời gian là kế hoạch điều hành; Evidence Gate mới là điều kiện chuyển pha.

---

# 6. GATE 1 — LABORATORY EVIDENCE

## Định vị

- RQ1 / WP1 / Chương 4 / Paper 1.
- Trạng thái: chưa đóng.
- Mức ưu tiên: cao nhất.

## Mục tiêu

Chứng minh các trạng thái liên kết kiểm soát có thể được phân biệt dưới đánh giá run-aware, leakage-controlled.

## Nhiệm vụ

### G1.1 Dataset inventory

Tạo:

```text
Dataset_ID
Campaign_ID
Acquisition_Session
Date
State
Excitation
Run_ID
Sensor_Mode
Sensor_ID
Sampling_Rate
Duration
File_Path
File_Hash
Quality_Flag
Include_Exclude
Exclusion_Reason
```

### G1.2 Run registry

Khóa cấu trúc:

```text
Campaign → Session → Run → File → Window
```

Không để window cùng run xuất hiện ở train và test.

### G1.3 Sensor provenance

Xác nhận:

- S1 = Apex;
- S2 = Beam–Column;
- S3 = Brace–Column;
- axis/channel order;
- sensor mode của 1D-CNN;
- sensor mode của ResNet1D.

Nếu ResNet1D không chứng minh được provenance, loại chính thức khỏi Paper 1.

### G1.4 Leakage-safe pipeline

```text
split runs
→ fit preprocessing on train only
→ window train/validation/test riêng
```

Không random split toàn bộ windows.

### G1.5 Common folds

Mọi model và sensor configuration dùng cùng held-out runs.

### G1.6 Model comparison

Core:

- Logistic Regression;
- SVM;
- Random Forest;
- 1D-CNN;
- ResNet1D nếu provenance đạt.

Autoencoder không thuộc Paper 1 core.

### G1.7 Metrics

- macro-F1;
- balanced accuracy;
- per-class metrics;
- confusion matrix;
- per-run results;
- uncertainty across runs;
- per-recording aggregation;
- empirical null;
- seed sensitivity;
- overlap sensitivity;
- sensor configuration comparison.

## Đầu ra

```text
GATE1/
├── DATASET_MANIFEST.csv
├── RUN_REGISTRY.csv
├── SENSOR_PROVENANCE.csv
├── EXCLUSION_LOG.csv
├── SPLIT_REGISTRY.csv
├── PREPROCESSING_SPEC.md
├── MODEL_CONFIG_REGISTRY.csv
├── PER_RECORDING_PREDICTIONS.csv
├── PER_RUN_RESULTS.csv
├── LORO_SUMMARY.csv
├── CONFUSION_MATRICES/
├── SENSITIVITY_REPORT.md
├── EMPIRICAL_NULL_REPORT.md
├── REPRODUCIBILITY_MANIFEST.csv
└── GATE1_CLOSURE_REVIEW.md
```

## Tiêu chí đóng

- run registry khóa;
- independent unit rõ;
- split-before-windowing;
- train-only preprocessing;
- LORO hoàn tất;
- common folds;
- per-recording predictions;
- uncertainty qua runs;
- ResNet1D xác nhận hoặc loại;
- code/environment/hash khóa;
- không dùng single split làm claim chính.

---

# 7. GATE 2 — TRACEABILITY MODEL VÀ BIM INFORMATION READINESS

## Định vị

- RQ2 / WP2 / Chương 5 / Paper 2.
- Trạng thái: đang phát triển, chưa đóng.

## Kết quả đã đạt

### Phase 1

- Model Version Registry;
- Component Registry;
- BIM Binding Registry;
- geometry readiness;
- Coordinate_Quality;
- IDS baseline;
- link audit;
- không auto-verified mapping.

### Revit–IFC

- Revit 2027.1;
- Dynamo 4.0;
- 718 structural elements trong crosswalk;
- IFC sync: 3.468 IfcElement;
- 1.703 structural elements;
- 3.468/3.468 GUID unique;
- 1.703/1.703 geometry usable;
- round-trip audit;
- 17 `REVIT_ONLY`;
- 1.002 plate/fastener không Tag.

### Pset validation

`Pset_DT_AssetIdentity` gồm:

```text
Asset_ID
Asset_Name
Asset_Type
Location_Mark
Asset_ID_Source
Verification_Status
Traceability_Scope
```

Kết quả:

- 14/14 values match;
- IfcColumn + IfcBeam;
- tiếng Việt đúng;
- 41/41 PASS;
- không lan dữ liệu;
- không đổi Tag/GUID/class/geometry;
- `READY TO FREEZE PSET EXPORT SETUP`.

## Chưa đạt

- acceptance record chính thức;
- Asset_ID thật;
- sensor target scope;
- competency questions;
- Inspection_Record schema;
- traceability schema v1;
- invalid-data tests;
- end-to-end chain.

## Trình tự G2

```text
G2-A Freeze export setup
G2-B Pre-register competency questions
G2-C Define sensor/asset target scope
G2-D Define identifier and record schema
G2-E Approve real Asset_ID
G2-F Graph 02 dry-run
G2-G Official IFC enrichment
G2-H Gate 2 closure review
```

---

# 8. G2-A — KHÓA REVIT–IFC EXPORT SETUP

## Việc làm

1. Lưu setup:

```text
IFC4X3_DT_ASSET_IDENTITY_ACCEPTED_V1
```

2. Xuất mapping:

```text
DT_UserDefinedPropertySets_ACCEPTED_V1.txt
```

3. Tạo:

```text
PSET_EXPORT_ACCEPTANCE_RECORD.md
```

4. Ghi:

- Revit version;
- exporter;
- IFC schema;
- 7 mappings;
- datatype `IFCTEXT`;
- tested classes;
- audit 41/41;
- limitation;
- reviewer;
- hash.

## PASS khi

- accepted setup có version;
- mapping immutable;
- test RVT/IFC lưu riêng;
- không dùng test values làm official data.

---

# 9. G2-B — PRE-REGISTER COMPETENCY QUESTIONS

## Câu hỏi đề xuất

### Identity

- CQ01: Sensor_ID liên kết với BIM_GUID nào trong Model_Version_ID nào?
- CQ02: BIM_GUID tương ứng Asset_ID nào?
- CQ03: Có mapping nhiều–một hoặc conflict ngoài quy tắc không?

### Evidence

- CQ04: Condition_Evidence_ID bắt nguồn từ run, sensor và model nào?
- CQ05: Những evidence nào liên quan một cấu kiện?

### Inspection

- CQ06: Evidence nào tạo/hỗ trợ Inspection_Record_ID?
- CQ07: Từ inspection record có truy ngược về sensor và run được không?

### Action

- CQ08: Action_Status hiện tại là gì?
- CQ09: Ai thay đổi trạng thái, khi nào và dựa trên bằng chứng nào?

### Integrity

- CQ10: Chuỗi nào thiếu mắt xích?
- CQ11: Có orphan sensor/evidence/BIM/inspection record không?
- CQ12: Có duplicate identifier không?

### Version

- CQ13: BIM_GUID thuộc model version nào?
- CQ14: Khi xuất lại IFC, binding thay đổi thế nào?

### Bidirectional

- CQ15: Có thể truy từ warning đến record và quay lại đúng nguồn không?

## Đầu ra

```text
GATE2_COMPETENCY_QUESTIONS_v1.0.md
GATE2_ACCEPTANCE_CRITERIA_v1.0.csv
GATE2_PRE_REGISTRATION_RECORD.md
```

## PASS khi

- mỗi CQ có fixture;
- expected answer;
- query;
- PASS/FAIL;
- required/optional rules;
- phê duyệt trước demo.

---

# 10. G2-C — SENSOR TARGET SCOPE

## File

```text
sensor_target_scope.csv
```

## Trường

```text
Scope_ID
Revit_UniqueId
Revit_ElementId
BIM_GUID
Model_Version_ID
Category
Family
Type
Location_Mark
Component_Role
Inspection_Unit
Proposed_Sensor_ID
Traceability_Reason
Include_In_Core_Scope
Scope_Status
Review_Evidence
Reviewer
Review_Date
Review_Note
```

## Core Scope

- cột đặt sensor;
- dầm/giằng liên quan;
- cấu kiện chủ tại connection;
- cấu kiện cần Inspection_Record;
- cấu kiện lân cận có lý do quản lý.

## Không mặc định đưa vào Core

- từng plate;
- từng bolt;
- từng anchor;
- fabrication detail không phải inspection unit.

## 17 REVIT_ONLY

- nằm trong scope → phải giải thích;
- ngoài scope → limitation;
- chưa rõ → `REVIEW_REQUIRED`.

## 1.002 phần tử không Tag

- không phải inspection unit → không chặn Core;
- thuộc connection assembly → liên kết parent;
- cần quản lý riêng → Supporting/Future Work.

---

# 11. G2-D — DATA DICTIONARY VÀ TRACEABILITY SCHEMA

## Entity tối thiểu

```text
Model_Version
Asset_Component
BIM_Binding
Sensor
Run
Condition_Evidence
Inspection_Record
Inspection_Finding
Action_Record
Action_Status_Event
Document
Actor
```

## Chuỗi khóa

```text
Sensor_ID
→ BIM_GUID + Model_Version_ID
→ Condition_Evidence_ID
→ Inspection_Record_ID
→ Action_Record_ID
→ Action_Status_Event_ID
```

## Asset component

```text
Asset_ID
Asset_Name
Asset_Type
Location_Mark
Inspection_Unit
Lifecycle_Status
Asset_ID_Source
Verification_Status
```

## BIM binding

```text
Binding_ID
Asset_ID
BIM_GUID
Model_Version_ID
IFC_Class
Revit_UniqueId
Revit_ElementId
Binding_Status
Binding_Evidence
Reviewer
Valid_From
Valid_To
```

## Condition evidence

```text
Condition_Evidence_ID
Source_Data_ID
Run_ID
Sensor_ID
Evidence_Type
Model_Name
Model_Version
Evaluation_Protocol
Predicted_State
Confidence_or_CEI
Quality_Flag
Created_At
Evidence_Status
```

CEI không phải physical severity.

## Inspection record

```text
Inspection_Record_ID
Asset_ID
BIM_GUID
Model_Version_ID
Trigger_Type
Trigger_Evidence_ID
Inspection_Type
Inspector
Inspection_Date
Finding
Finding_Status
Photo_Link
Document_Link
Recommended_Action
Review_Status
```

## Action record

```text
Action_Record_ID
Inspection_Record_ID
Action_Type
Action_Status
Assigned_To
Decision_By
Decision_Date
Due_Date
Completion_Date
Evidence_Reference
Comment
```

## Integrity rules

- Asset_ID unique;
- BIM_GUID unique trong Model_Version_ID;
- không evidence thiếu Sensor_ID;
- không inspection record thiếu Asset/BIM;
- Action_Status có event history;
- không ghi đè lịch sử;
- không auto-verified.

## Đầu ra

```text
TRACEABILITY_SCHEMA_v1.0.md
TRACEABILITY_ER_MODEL_v1.0.md
TRACEABILITY_DATA_DICTIONARY_v1.0.csv
TRACEABILITY_INTEGRITY_RULES_v1.0.csv
TRACEABILITY_STATUS_DICTIONARY_v1.0.csv
```

---

# 12. G2-E — ASSET_ID THẬT

## Không được dùng làm Asset_ID

- IFC GlobalId;
- Revit ElementId;
- Revit UniqueId;
- số thứ tự IFC;
- tọa độ;
- mã tự sinh chưa phê duyệt.

## File duyệt

```text
revit_asset_import_verified.csv
```

## Trường

```text
Import_Row_ID
Revit_UniqueId
Revit_ElementId
Current_BIM_GUID
Model_Version_ID
Asset_ID
Asset_Name
Asset_Type
Location_Mark
Asset_ID_Source
Verification_Status
Review_Evidence
Reviewer
Review_Date
Import_Approved
```

## PASS khi

- 0 duplicate;
- 0 missing element;
- 0 conflict;
- mọi dòng có evidence;
- mọi dòng có reviewer;
- hash được khóa.

---

# 13. G2-F — DYNAMO GRAPH 02

## Lần đầu

```text
DRY_RUN = TRUE
```

## Dry-run kiểm tra

- file và header;
- Revit_UniqueId;
- ElementId đối chứng;
- parameter tồn tại;
- writable;
- Asset_ID unique;
- approved status;
- old/new value;
- error list.

## Output

```text
GRAPH02_DRY_RUN_LOG.csv
GRAPH02_DRY_RUN_SUMMARY.md
```

## Pilot

3–5 cấu kiện verified:

- một cột;
- một dầm;
- một giằng hoặc parent component.

## Sau pilot

```text
Revit Schedule review
→ Graph 01 export lại
→ crosswalk comparison
→ IFC export
→ full audit
```

Không chạy write khi dry-run chưa PASS.

---

# 14. G2-G — IFC ENRICHED CHÍNH THỨC

## File đề xuất

```text
model_revit2027_asset_enriched_v1.ifc
```

## Audit

- Model_Version_ID;
- parent version;
- SHA-256;
- GUID uniqueness;
- geometry;
- Asset_ID uniqueness;
- Pset;
- Revit–IFC binding;
- IDS;
- no test values;
- no unexpected spread.

## Đầu ra

```text
MODEL_VERSION_REGISTRY.csv
ASSET_ID_UNIQUENESS_AUDIT.csv
REVIT_IFC_BINDING_AUDIT.csv
PSET_EXPORT_AUDIT.csv
GEOMETRY_PERSISTENCE_AUDIT.csv
IDS_REPORT.html
IFC_ENRICHMENT_ACCEPTANCE_RECORD.md
```

---

# 15. ĐÓNG GATE 2

Gate 2 chỉ đóng khi có:

1. competency questions;
2. acceptance criteria;
3. identifier dictionary;
4. data dictionary;
5. Inspection_Record schema;
6. Action_Status model;
7. sensor/asset scope;
8. real Asset_ID governance;
9. accepted Revit–IFC setup;
10. official BIM binding;
11. integrity rules;
12. provenance rules;
13. human verification workflow;
14. closure review.

Kết luận cho phép:

> Mô hình dữ liệu và tiêu chí đánh giá truy vết đã được khóa và sẵn sàng kiểm chứng end-to-end.

Chưa được nói framework đã được kiểm chứng hoàn toàn.

---

# 16. GATE 3 — END-TO-END LAB TRACEABILITY

## Điều kiện bắt đầu

Gate 2 được phê duyệt.

## Chuỗi kiểm thử

```text
Run
→ Sensor_ID
→ Condition_Evidence_ID
→ BIM_GUID
→ Asset_ID
→ Inspection_Record_ID
→ Action_Record
→ Action_Status
```

## Test fixtures

- valid cases;
- duplicate Sensor_ID;
- missing BIM_GUID;
- orphan evidence;
- missing Inspection_Record;
- invalid Action_Status;
- superseded model;
- changed GUID;
- conflicting Asset_ID;
- missing provenance.

## Truy vấn

### Forward

```text
Evidence → component → inspection → action
```

### Reverse

```text
Action → inspection → evidence → run → sensor
```

## Metrics

- CQ pass rate;
- forward trace success;
- reverse trace success;
- orphan detection;
- duplicate detection;
- missing-link detection;
- query reproducibility;
- provenance completeness.

## Output

```text
GATE3/
├── LAB_TRACEABILITY_FIXTURES/
├── QUERY_IMPLEMENTATION/
├── CQ_RESULTS.csv
├── FORWARD_TRACE_RESULTS.csv
├── REVERSE_TRACE_RESULTS.csv
├── INVALID_DATA_TEST_RESULTS.csv
├── ORPHAN_DUPLICATE_REPORT.csv
├── PROVENANCE_COMPLETENESS_REPORT.csv
├── BIDIRECTIONAL_TRACEABILITY_REPORT.md
└── GATE3_CLOSURE_REVIEW.md
```

## Đóng G3 khi

- CQ bắt buộc đạt;
- forward/reverse reproducible;
- invalid fixtures bị phát hiện;
- không có hidden manual step;
- input/output/code/hash lưu đầy đủ.

---

# 17. PAPER 2 VÀ CHƯƠNG 5

## Tên Paper 2

**A Verifiable Component-Level Traceability Framework Linking Vibration-Based Condition Evidence to BIM Objects and Inspection Records for Industrial Steel Buildings**

## Cấu trúc Paper 2

1. Introduction.
2. Evidence-to-action gap.
3. Research framework.
4. Information requirements.
5. Identifier architecture.
6. BIM information readiness.
7. Revit–IFC exchange validation.
8. Traceability schema.
9. Competency questions.
10. Laboratory case.
11. Invalid-data tests.
12. Results.
13. Management implications.
14. Limitations.
15. Conclusion.

## Đóng góp thật

- formal identifier chain;
- verifiable data model;
- pre-registered CQs;
- bidirectional validation;
- integrity tests;
- reproducible Revit–IFC exchange;
- inspection record linkage.

Không lấy “tạo mô hình Revit” hoặc “làm website” làm contribution chính.

---

# 18. GATE 4 — FIELD FEASIBILITY

## Điều kiện tiên quyết

- field access;
- Gate 2 schema khóa;
- Gate 3 hoạt động;
- sensor plan;
- safety/data ownership rõ.

## Hồ sơ

```text
FIELD_ACCESS_CONFIRMATION_REGISTER.md
FIELD_ASSET_REGISTER.csv
FIELD_SENSOR_REGISTER.csv
FIELD_SENSOR_TO_BIM_MAPPING.csv
FIELD_DEPLOYMENT_PROTOCOL.md
FIELD_DATA_QUALITY_PLAN.md
```

## Sensor register

```text
Sensor_ID
Hardware_ID
Sensor_Type
Axis
Sampling_Rate
Installed_Asset_ID
Installed_BIM_GUID
Model_Version_ID
Installation_Date
Mounting_Method
Calibration_Status
Network_Status
Storage_Status
Maintainer
```

## Field data quality

- noise floor;
- clipping;
- sampling stability;
- timestamp;
- missing data;
- channel swap;
- power/network loss;
- drift;
- mounting change;
- environment;
- operation.

## Operational baseline

Mô tả:

- availability;
- operating conditions;
- environment;
- expected variation;
- sensor health;
- exclusion rules.

Không đặt ngưỡng damage diagnosis.

## Tối thiểu ba scenarios

### F1 Routine

```text
baseline → component → inspection record → Normal
```

### F2 Data quality issue

```text
sensor anomaly → quality flag → sensor inspection
```

### F3 Condition warning

```text
state-change evidence → component → human review → inspection request
```

## Đóng G4 khi

- hệ thống triển khai được;
- dữ liệu trả về;
- sensor identity ổn định;
- BIM mapping hoạt động;
- ít nhất ba scenarios chạy;
- inspection record tạo được;
- không field diagnosis claim.

---

# 19. GATE 5 — DECISION SUPPORT

## Logic

```text
Normal
Watch
Inspect
Priority Inspection
```

## Rulebook

```text
Rule_ID
Input
Precondition
Data_Quality_Requirement
Evidence_Requirement
Context
Recommended_Status
Human_Review_Required
Override_Rule
Audit_Field
```

## Reviewers

- facility manager;
- maintenance engineer;
- inspection engineer;
- BIM/information manager;
- researcher.

## Đánh giá

- clarity;
- explainability;
- consistency;
- usefulness;
- auditability;
- false escalation;
- missing information;
- override needs.

## Output

```text
DECISION_RULEBOOK_v1.0.md
ACTION_SCENARIO_REGISTER.csv
EXPERT_REVIEW_FORM.csv
REVIEW_RESULTS.csv
RULE_REVISION_LOG.csv
GATE5_DECISION_VALIDITY_REVIEW.md
```

Không dùng weighted Health Index và không tự động hóa quyết định.

---

# 20. KẾ HOẠCH CHƯƠNG

## Chương 1

- bối cảnh;
- vấn đề;
- mục tiêu;
- RQ;
- phạm vi;
- đóng góp;
- cấu trúc.

## Chương 2

Bốn cụm:

1. vibration evidence;
2. BIM/DT traceability;
3. field feasibility;
4. inspection-maintenance support.

Khoảng trống:

> Thiếu chuỗi có thể kiểm chứng từ dữ liệu dao động đến bằng chứng, cấu kiện BIM, hồ sơ kiểm tra và trạng thái hành động.

## Chương 3

- DT definition;
- maturity boundary;
- evidence architecture;
- validation ladder;
- cases;
- data governance;
- reproducibility;
- ethics;
- Limited FEM subsection;
- ISO 19650/TCVN 14177 positioning.

## Chương 4

Gate 1 / Paper 1.

## Chương 5

Gate 2–3 / Paper 2.

## Chương 6

Gate 4 / Paper 3.

## Chương 7

Gate 5 / synthesis.

## Chương 8

- trả lời từng RQ;
- contribution theo evidence level;
- limitations;
- implications;
- future work.

---

# 21. PUBLICATION PLAN

| Paper | Điều kiện nộp |
|---|---|
| Paper 1 | G1 đóng |
| Paper 2 | G2 + G3 đóng |
| Paper 3 | G4 đóng |
| Paper 4 optional | G5 đủ evidence |

Paper 1 không chờ BIM.  
Paper 2 không chờ field.  
Paper 3 không dùng classifier lab để chẩn đoán field.  
Paper 4 có thể tích hợp Paper 3 nếu evidence chuyên gia chưa đủ.

---

# 22. CÔNG CỤ

| Workstream | Công cụ |
|---|---|
| WP1 | Python, scikit-learn, PyTorch, Git |
| WP2 | Revit, Dynamo, IFC Exporter, IfcOpenShell, IfcTester, SQL |
| WP3 | Sensors, field log, storage, BIM/IFC viewer |
| WP4 | Rulebook, scenario matrix, expert review |

AI hỗ trợ code, audit và draft. AI không tự tạo evidence, Asset_ID, verified status, Gate status hoặc damage claim.

---

# 23. QUẢN TRỊ FILE

## Folder đề xuất

```text
00_GOVERNANCE/
01_LITERATURE/
02_DATA_LAB/
03_GATE1/
04_BIM_AIM/
05_GATE2/
06_GATE3/
07_FIELD/
08_GATE4/
09_GATE5/
10_PAPERS/
11_THESIS/
12_REPRODUCIBILITY/
99_ARCHIVE/
```

## Quy tắc

- không ghi đè raw data;
- không ghi đè accepted model;
- hash input quan trọng;
- mỗi audit có manifest;
- append-only decision log;
- canonical + runtime file;
- mỗi result gắn code commit.

---

# 24. EVIDENCE MATRIX

```text
Evidence_ID
RQ
WP
Chapter
Paper
Gate
Evidence_Type
Claim
Source
Method
Result
Metric
Limitation
Allowed_Use
Prohibited_Inference
File_Path
File_Hash
Review_Status
Reviewer
```

Mọi bảng/hình trong luận án phải truy về Evidence_ID.

---

# 25. RISK REGISTER

| Rủi ro | Kiểm soát |
|---|---|
| Data leakage | LORO, split-before-windowing |
| Sensor provenance sai | Sensor registry và channel audit |
| BIM thiếu Asset_ID | Scope nhỏ + human verification |
| GUID thay đổi | Asset_ID + Model_Version_ID |
| IFC mất property | Accepted Pset setup |
| REVIT_ONLY | Xử lý khi thuộc Core Scope |
| Field access chậm | Thỏa thuận sớm |
| Sensor field không ổn định | Qualification + quality plan |
| FEM mở rộng | Limited-FEM firewall |
| Website phát triển quá mức | Chỉ phục vụ CQ/scenarios |
| File bị ghi đè | Immutable outputs + hash |
| Overclaim ISO/TCVN | Nói aligned, không nói certified |

---

# 26. DASHBOARD GATE

| Gate | Status | Blocker |
|---|---|---|
| G1 | OPEN | run registry, LORO, ResNet1D mode |
| G2 | OPEN | CQ, schema, scope, real Asset_ID |
| G3 | NOT STARTED | G2 chưa đóng |
| G4 | BLOCKED/NOT STARTED | field access + G3 |
| G5 | NOT STARTED | traceability chain |
| G6 | NOT STARTED | Paper 2 |
| G7 | NOT STARTED | field + thesis synthesis |

---

# 27. KẾ HOẠCH 30–60–90 NGÀY

## 0–30 ngày

### G1

- hợp nhất dataset inventory;
- khóa campaign/run registry;
- xác nhận sensor mode;
- positive control;
- LORO common folds;
- per-recording predictions.

### G2 song song

- freeze Pset ACCEPTED_V1;
- acceptance record;
- competency questions v1;
- acceptance criteria;
- sensor target scope candidate;
- inspection unit.

### Không làm

- Graph 02 write;
- field classifier;
- FEM calibration;
- website feature expansion.

## 31–60 ngày

- G1 sensitivity;
- G1 closure review;
- Paper 1 tables;
- pre-register G2;
- data dictionary;
- ER model;
- Inspection_Record schema;
- Asset_ID convention.

## 61–90 ngày

- approve target scope;
- approve pilot Asset_ID;
- Graph 02 dry-run;
- pilot import;
- official enriched IFC;
- full audit;
- freeze schema;
- Gate 3 fixtures.

---

# 28. CLAIM → EVIDENCE → LIMITATION → NEXT ACTION

## Claim

Luận án có kiến trúc bảo vệ được trong ngành Quản lý xây dựng: laboratory evidence tạo đầu vào; BIM/AIM cung cấp định danh và truy vết; field case kiểm chứng khả thi; rulebook hỗ trợ quyết định có con người rà soát.

## Evidence

- RQ/WP/chương/Paper/Gate đã khóa;
- Phase 1 BIM Information Readiness đã chạy;
- Pset test đạt 41/41 PASS;
- dữ liệu lab và BIM case đã có.

## Limitation

- G1 chưa đóng;
- CQ chưa pre-register;
- Asset_ID thật chưa duyệt;
- G3–G5 chưa có evidence;
- field access chưa đủ;
- Evidence is currently insufficient để tuyên bố framework đã được kiểm chứng toàn bộ.

## Next action

```text
Ưu tiên tuyệt đối:
Khóa Gate 1.

Song song:
Freeze Pset
→ pre-register competency questions
→ define sensor target scope
→ approve traceability schema
```

Chưa chạy Graph 02 write.

---

# 29. PHÁN QUYẾT CHIẾN LƯỢC

1. Revit–IFC hiện tại là infrastructure evidence, chưa phải toàn bộ contribution Paper 2.
2. Contribution Paper 2 xuất hiện khi có CQs, formal identifier model, invalid-data tests, bidirectional traceability và Inspection_Record.
3. G1 vẫn là đường găng số một.
4. G2 có thể làm song song; G3 chỉ bắt đầu sau khi G2 khóa.
5. Field case chứng minh feasibility, không damage diagnosis.
6. FEM phải tiếp tục giới hạn.
7. Website là phương tiện truy vấn, không phải sản phẩm khoa học chính.

---

# 30. ĐIỀU KIỆN TRƯỚC BẢO VỆ

## RQ1

Bằng chứng lab chống rò rỉ, tái lập được và có uncertainty theo run.

## RQ2

Mô hình truy vết được pre-register, triển khai, kiểm chứng hai chiều và phát hiện lỗi.

## RQ3

Case hiện trường chứng minh triển khai và inspection workflow.

## WP4

Rulebook bốn mức được người quản lý/chuyên gia rà soát.

## Logic bảo vệ

```text
Evidence validity
→ Traceability validity
→ Field feasibility
→ Decision validity
```

---

# 31. ISO 19650 VÀ TCVN 14177

Trong luận án:

- Revit là authoring tool;
- IFC là container trao đổi;
- CDE quản lý container và phiên bản;
- Asset_ID là định danh nghiệp vụ;
- BIM_GUID là định danh object IFC;
- Model_Version_ID tạo ngữ cảnh;
- AIM phục vụ vận hành;
- không tuyên bố chứng nhận ISO 19650.

Cách diễn đạt:

> Khung được tổ chức theo hướng hỗ trợ quản lý yêu cầu thông tin, container, phiên bản, trao đổi, kiểm tra và truy vết phù hợp với định hướng ISO 19650 và TCVN 14177.

---

# 32. ROADMAP LOCK

Mọi nhiệm vụ mới phải trả lời:

1. Phục vụ RQ nào?
2. Thuộc WP nào?
3. Viết vào chương/Paper nào?
4. Đóng Gate nào?
5. Evidence tạo ra là gì?
6. Thuộc Core, Supporting, Future hay Out of Scope?

Không trả lời được sáu câu này thì không đưa vào luận án.
