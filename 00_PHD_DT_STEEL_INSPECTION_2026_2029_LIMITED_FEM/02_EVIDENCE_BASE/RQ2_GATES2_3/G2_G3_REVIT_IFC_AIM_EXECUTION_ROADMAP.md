# ROADMAP THỰC THI RIÊNG GATE 2 – GATE 3
## Từ mô hình Revit ban đầu đến khóa truy vết end-to-end trong phòng thí nghiệm

**Tên tệp:** `G2_G3_REVIT_IFC_AIM_EXECUTION_ROADMAP.md`  
**Luận án:** Data-informed Digital Twin phục vụ giám sát trạng thái và hỗ trợ kiểm tra – bảo trì nhà công nghiệp khung thép ven biển  
**Lĩnh vực:** Quản lý xây dựng / Quản lý thông tin tài sản  
**RQ/WP:** RQ2 / WP2  
**Chương/Paper:** Chương 5 / Paper 2  
**Evidence Gates:** G2 – Traceability Design Readiness; G3 – End-to-End Laboratory Traceability  
**Kiến trúc:** Limited-FEM  
**Ngày lập:** 03/08/2026  
**Trạng thái hiện tại:** `READY TO FREEZE PSET EXPORT SETUP`  
**Trạng thái Gate:** G2 đang mở; G3 chưa mở  

---

# 0. MỤC ĐÍCH CỦA ROADMAP

Roadmap này hướng dẫn toàn bộ quá trình từ mô hình Revit ban đầu đến khi:

```text
Gate 2 được đóng:
mô hình dữ liệu truy vết + chuỗi định danh + cấu trúc hồ sơ
+ competency questions + tiêu chí đánh giá được khóa trước;

sau đó Gate 3 được đóng:
một case laboratory traceability chạy end-to-end,
truy vấn được hai chiều,
phát hiện được dữ liệu thiếu/trùng/mồ côi,
và đạt toàn bộ tiêu chí đã pre-register ở Gate 2.
```

Roadmap không hướng dẫn:

- chẩn đoán hư hỏng hiện trường;
- hiệu chỉnh FEM;
- suy luận lực siết bu lông;
- đánh giá suy giảm độ cứng;
- chuyển classifier 1:10 sang công trình thực;
- RUL hoặc predictive maintenance;
- tự động ra quyết định bảo trì;
- phát triển phần mềm thương mại.

---

# 1. ĐỊNH VỊ HỌC THUẬT

| Thành phần | Nội dung đã khóa |
|---|---|
| RQ2 | Tổ chức và liên kết bằng chứng trạng thái với cấu kiện BIM và hồ sơ kiểm tra để bảo đảm truy vết cấp cấu kiện |
| WP2 | BIM–Sensor–Inspection traceability |
| Chương | Chương 5 – Traceability framework |
| Paper | Paper 2 |
| G2 | Traceability data model and competency questions |
| G3 | End-to-end laboratory traceability |
| Evidence type | Information traceability |
| Validation level | V2 – Traceability validity |
| Core chain | `Sensor_ID → BIM_GUID → Condition_Evidence_ID → Inspection_Record_ID → Action_Status` |

## Tên Paper 2 đề xuất

**A Verifiable Component-Level Traceability Framework Linking Vibration-Based Condition Evidence to BIM Objects and Inspection Records for Industrial Steel Buildings**

## Đóng góp Paper 2 phải là

1. mô hình dữ liệu truy vết hình thức;
2. kiến trúc định danh có phiên bản;
3. competency questions được công bố trước;
4. tiêu chí đánh giá có thể đo;
5. kiểm chứng hai chiều;
6. invalid-data tests;
7. liên kết BIM object với Inspection_Record;
8. bằng chứng Revit–IFC có thể tái lập.

## Đóng góp Paper 2 không phải là

- dựng Revit;
- xuất IFC;
- làm dashboard;
- tạo website;
- gắn một vài hyperlink;
- hiển thị sensor trên mô hình;
- tạo demo trực quan nhưng không có tiêu chí kiểm chứng.

---

# 2. CHUỖI NGHIÊN CỨU VÀ FIREWALL PHẠM VI

## 2.1. Chuỗi khóa

```text
Vibration data
→ condition/state-change evidence
→ BIM-linked component
→ inspection record
→ inspection-maintenance action support
```

## 2.2. Chuỗi định danh khóa

```text
Sensor_ID
→ BIM_GUID
→ Condition_Evidence_ID
→ Inspection_Record_ID
→ Action_Status
```

## 2.3. Định danh hỗ trợ

```text
Asset_ID
Model_Version_ID
Revit_UniqueId
Revit_ElementId
Run_ID
Action_Record_ID
```

## 2.4. FEM

FEM chỉ được mô tả:

> nominal, uncalibrated, reference-only, not used for damage diagnosis.

`FEM_Node_ID` chỉ là metadata tùy chọn, không được trở thành mắt xích bắt buộc.

---

# 3. PHÂN LOẠI PHẠM VI G2–G3

## Core Scope

- mô hình dữ liệu truy vết;
- BIM object identity;
- Asset_ID governance;
- Model_Version_ID;
- Sensor_ID;
- Condition_Evidence_ID;
- Inspection_Record_ID;
- Action_Status;
- Revit–IFC information exchange;
- competency questions;
- integrity rules;
- bidirectional queries;
- invalid-data fixtures;
- end-to-end lab case.

## Supporting Scope

- Revit 2027.1;
- Dynamo 4.0 / PythonNet3;
- IFC4X3;
- `Pset_DT_AssetIdentity`;
- IfcOpenShell;
- IfcTester/IDS;
- SQLite hoặc PostgreSQL;
- Excel/CSV;
- Git;
- CDE-style provenance;
- ISO 19650 và TCVN 14177 như định hướng quản lý thông tin.

## Future Work

- ontology đầy đủ;
- knowledge graph lớn;
- multi-building AIM;
- bolt-level asset management;
- live streaming Digital Twin;
- production-grade CDE;
- commercial platform.

## Out of Scope

- calibrated FEM;
- field damage diagnosis;
- stiffness degradation;
- RUL;
- predictive maintenance;
- weighted Health Index;
- autonomous maintenance;
- Smart City;
- Edge AI.

---

# 4. ĐIỂM XUẤT PHÁT HIỆN TẠI

## 4.1. IFC baseline ban đầu

```text
model.ifc
```

| Trường | Giá trị |
|---|---|
| Schema | IFC4X3_ADD2 |
| SHA-256 | `814baf3ac26432d2b689c1013406cbea57678e9cb602290f40cf239b302bb7f7` |
| Model_Version_ID | `MV-20260313-814baf3a` |
| Revit nguồn | 25.4.0.32 |
| ODA SDAI | 24.12 |
| Tổng IfcElement | 4.013 |
| Cấu kiện kết cấu | 1.813 |

## 4.2. Phase 1 – BIM Information Readiness

Đã tạo và kiểm tra:

- Model Version Registry;
- Component Registry;
- BIM Binding Registry;
- geometry readiness;
- Coordinate_Quality;
- IDS baseline;
- link audit.

Kết quả đáng chú ý:

| Chỉ số | Giá trị |
|---|---:|
| Asset_ID duy nhất dùng được | 24 |
| Asset_ID bị chặn do trùng | 2 |
| Không có nguồn Asset_ID | 1.787 |
| Geometry usable | 1.812/1.813 |
| Placement suy biến được geometry khôi phục | 607/607 |
| Link audit | 8/8 PASS |

## 4.3. Revit 2027 structural crosswalk

Môi trường:

```text
Revit 2027.1
Dynamo 4.0.2.3852
PythonNet3
```

Graph:

```text
01_export_revit_crosswalk_structural_Dynamo4.dyn
```

Thiết lập:

```text
INCLUDE_STEEL_CONNECTIONS = False
```

Kết quả:

| Category | Số lượng |
|---|---:|
| Structural Framing | 596 |
| Structural Columns | 56 |
| Generic Models | 41 |
| Structural Foundations | 24 |
| Floors | 1 |
| Tổng | 718 |

## 4.4. IFC sync từ Revit 2027

```text
model_revit2027_sync_v1.ifc
```

| Chỉ số | Giá trị |
|---|---:|
| Model_Version_ID | `MV-20260803-fc94ef3c` |
| Parent | `MV-20260313-814baf3a` |
| IfcElement | 3.468 |
| Structural | 1.703 |
| GUID unique | 3.468/3.468 |
| Geometry usable | 1.703/1.703 |
| IFC Tag | 714 |

Round-trip:

| Chỉ số | Giá trị |
|---|---:|
| `MATCH_TAG_AND_GUID` | 685/718 |
| Có IFC counterpart duy nhất | 701/718 |
| Conflict | 0 |
| Duplicate Tag | 0 |
| REVIT_ONLY | 17 |
| GUID persistence trên tập chung | 90/90 |

## 4.5. Pset export validation

Property set:

```text
Pset_DT_AssetIdentity
```

Bảy property:

```text
Asset_ID
Asset_Name
Asset_Type
Location_Mark
Asset_ID_Source
Verification_Status
Traceability_Scope
```

Kết quả v2:

```text
41/41 PASS
0 PASS_WITH_LIMITATION
0 FAIL
```

Đã chứng minh:

- 14/14 giá trị đúng;
- đúng một IfcColumn và một IfcBeam;
- toàn bộ là `IfcText`;
- tiếng Việt không lỗi;
- không lan sang phần tử thứ ba;
- Tag, GlobalId, class và geometry không đổi;
- không có `verified`;
- input khóa bằng SHA-256.

## 4.6. Kết luận hiện tại

```text
READY TO FREEZE PSET EXPORT SETUP
```

Nhưng:

```text
Gate 2 chưa đóng.
Gate 3 chưa bắt đầu.
```

---

# 5. ĐỊNH NGHĨA CHÍNH XÁC GATE 2 VÀ GATE 3

## Gate 2 — Traceability Design Readiness

Gate 2 đóng khi:

1. traceability schema v1 được khóa;
2. identifier chain được định nghĩa;
3. Asset_ID/BIM_GUID/Model_Version rules được khóa;
4. Inspection_Record structure được khóa;
5. Action_Status model được khóa;
6. competency questions được phê duyệt và pre-register;
7. acceptance criteria được khóa trước kiểm chứng;
8. sensor/asset scope được xác định;
9. Revit–IFC setup được chấp nhận;
10. integrity rules và invalid-data plan được khóa;
11. human verification workflow được xác định;
12. G2 closure review được phê duyệt.

Gate 2 là **design readiness**, chưa phải end-to-end validation.

## Gate 3 — End-to-End Laboratory Traceability

Gate 3 đóng khi:

1. một lab case thực chạy hết chuỗi;
2. truy vấn forward đạt;
3. truy vấn reverse đạt;
4. competency questions bắt buộc được trả lời đúng;
5. không còn orphan hoặc duplicate ngoài fixture chủ ý;
6. invalid fixtures bị phát hiện đúng;
7. Model_Version ambiguity được xử lý;
8. provenance đầy đủ;
9. input/output/code/hash tái lập được;
10. G3 closure review được phê duyệt.

---

# 6. ROADMAP TỔNG THỂ

```text
R0  Khóa governance và lưu bằng chứng hiện tại
R1  Freeze Pset export setup
R2  Tách test model khỏi working model
R3  Xác định asset/sensor target scope
R4  Khóa Asset_ID convention và review workflow
R5  Xây Traceability Schema v1
R6  Xây Inspection_Record và Action_Status schema
R7  Pre-register competency questions và acceptance criteria
R8  Phê duyệt Asset_ID pilot
R9  Graph 02 dry-run và pilot import
R10 Xuất official enriched IFC và audit
R11 Gate 2 closure review
R12 Chuẩn bị laboratory traceability fixtures
R13 Nạp condition evidence từ Gate 1
R14 Triển khai database và query layer
R15 Chạy forward/reverse traceability
R16 Chạy invalid-data tests
R17 Chạy end-to-end scenarios
R18 Đánh giá theo tiêu chí pre-register
R19 Gate 3 closure review
R20 Freeze Paper 2 evidence package
```

---

# 7. R0 — KHÓA GOVERNANCE VÀ BẰNG CHỨNG HIỆN TẠI

## Mục tiêu

Ngăn mất provenance trước khi tiếp tục.

## Input

- IFC baseline;
- IFC sync;
- test IFC v1/v2;
- crosswalk;
- binding audit;
- Pset audit;
- source Revit models;
- Dynamo graphs;
- mapping files.

## Thực hiện

1. Tạo thư mục:

```text
05_GATE2/
├── 00_GOVERNANCE/
├── 01_REVIT_IFC_BASELINE/
├── 02_PSET_ACCEPTANCE/
├── 03_SCOPE/
├── 04_SCHEMA/
├── 05_PRE_REGISTRATION/
├── 06_ASSET_ID_PILOT/
├── 07_OFFICIAL_IFC/
├── 08_GATE2_CLOSURE/
└── 99_ARCHIVE/
```

2. Sao chép output hiện tại vào thư mục immutable.
3. Tạo `G2_CURRENT_INPUT_MANIFEST.csv`.
4. Tính SHA-256.
5. Không dựa vào mtime.
6. Ghi rõ runtime file và canonical file.
7. Đánh dấu file bị ghi đè trước đây là không dùng.

## Output

```text
G2_CURRENT_INPUT_MANIFEST.csv
G2_CURRENT_STATUS_SNAPSHOT.md
G2_DECISION_LOG.md
```

## Công cụ

- Python;
- SHA-256;
- Git;
- file system.

## PASS khi

- mọi file quan trọng có hash;
- không ghi đè;
- test model và source model tách biệt;
- source-of-truth rõ.

## Stop condition

Dừng nếu không xác định được file Revit nào tạo IFC nào.

---

# 8. R1 — FREEZE PSET EXPORT SETUP

## Mục tiêu

Khóa đường truyền Revit Shared Parameters → IFC Pset đã đạt 41/41 PASS.

## Thực hiện

1. Trong Revit IFC Exporter, lưu setup:

```text
IFC4X3_DT_ASSET_IDENTITY_ACCEPTED_V1
```

2. Xuất mapping:

```text
DT_UserDefinedPropertySets_ACCEPTED_V1.txt
```

3. Lưu:

```text
revit_integration/ifc_export/accepted/
```

4. Tính SHA-256.
5. Tạo acceptance record.

## Acceptance record

```text
PSET_EXPORT_ACCEPTANCE_RECORD.md
```

Phải có:

```text
Acceptance_ID
Revit_Version
Dynamo_Version
IFC_Exporter_Version
IFC_Schema
Setup_Name
Mapping_File
Mapping_SHA256
Pset_Name
Property_Count
Data_Type
Test_IFC_Classes
Test_Result
Known_Limitations
Accepted_By
Acceptance_Date
Change_Control
```

## Known limitations phải ghi

- mới thử IfcColumn và IfcBeam;
- 2/1.703 elements;
- chưa thử một số special characters;
- plate/fastener không Tag;
- test data chưa phải Asset_ID thật.

## PASS khi

- accepted setup có tên;
- mapping file immutable;
- 7/7 property;
- datatype `IFCTEXT`;
- hash lưu;
- 41/41 audit dẫn chiếu;
- test files archive.

## Không được làm

- sửa `ACCEPTED_V1`;
- dùng test values trong model chính thức;
- chạy Graph 02.

---

# 9. R2 — TÁCH TEST MODEL VÀ WORKING MODEL

## Mục tiêu

Không để dữ liệu `TEST-*` lẫn vào production pipeline.

## File đề xuất

```text
model_revit2027_pset_test_v2.rvt     → archive test evidence
model_revit2027_pset_test_v2.ifc     → archive test evidence
model_revit2027_asset_working_v1.rvt → working copy
```

## Thực hiện

1. Mở một bản sạch không có test values.
2. Kiểm tra bằng Revit Schedule.
3. Chạy Graph 01.
4. Quét:

```text
TEST-
test_only
EXPORT-TEST
EXPORT_VALIDATION_TEST
```

5. Kết quả phải bằng 0 trong working model/crosswalk.

## Output

```text
WORKING_MODEL_CLEANLINESS_AUDIT.csv
WORKING_MODEL_BASELINE_MANIFEST.csv
```

## PASS khi

- 0 test marker;
- 0 `verified` không có evidence;
- model có backup;
- model hash/version ghi lại.

---

# 10. R3 — XÁC ĐỊNH ASSET/SENSOR TARGET SCOPE

## Mục tiêu

Chỉ chọn cấu kiện thực sự phục vụ traceability case.

## File

```text
sensor_target_scope.csv
```

## Trường bắt buộc

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

## Đơn vị quản lý đề xuất

### Core unit

- cột;
- dầm;
- giằng;
- parent connection/component;
- vị trí kiểm tra.

### Supporting/Future

- plate;
- bolt;
- anchor;
- chi tiết fabrication.

## Quy trình chọn

1. Lọc 718 structural elements.
2. Xác định vị trí sensor của mô hình 1:10.
3. Xác định component thật cần Inspection_Record.
4. Chọn parent component thay vì từng bolt.
5. Ghi lý do.
6. Review thủ công.
7. Khóa scope.

## 17 REVIT_ONLY

| Trường hợp | Hành động |
|---|---|
| Trong Core Scope | Phải điều tra và xử lý trước G2 closure |
| Ngoài Core Scope | Ghi limitation |
| Chưa rõ | `REVIEW_REQUIRED` |

## 1.002 phần tử không Tag

| Trường hợp | Hành động |
|---|---|
| Không phải inspection unit | Không chặn Core |
| Thuộc connection assembly | Gắn parent component |
| Cần quản lý riêng | Future Work hoặc ID mechanism khác |

## PASS khi

- scope có giới hạn;
- mọi dòng có lý do;
- mọi dòng có reviewer;
- inspection granularity rõ;
- không chọn toàn bộ model.

---

# 11. R4 — KHÓA ASSET_ID CONVENTION VÀ REVIEW WORKFLOW

## Mục tiêu

Phân biệt Asset_ID nghiệp vụ với khóa kỹ thuật.

## Không dùng làm Asset_ID

```text
IFC GlobalId
Revit ElementId
Revit UniqueId
IFC row number
tọa độ
mã tự sinh không có phê duyệt
```

## Asset_ID phải

- duy nhất;
- bền vững;
- có source;
- có reviewer;
- không phụ thuộc model version;
- có lifecycle status;
- có superseded rule.

## File

```text
ASSET_ID_CONVENTION_v1.0.md
ASSET_ID_REVIEW_WORKFLOW_v1.0.md
ASSET_ID_CONTROLLED_VOCABULARY.csv
```

## Trạng thái

```text
candidate
pending_human_verification
verified
rejected
superseded
retired
```

## Review workflow

```text
Candidate generated
→ Evidence attached
→ Reviewer checks element
→ Uniqueness check
→ Approve/Reject
→ Import_Approved
```

## PASS khi

- rule rõ;
- uniqueness scope rõ;
- reviewer role rõ;
- không có auto-verified;
- lifecycle rule rõ.

---

# 12. R5 — TRACEABILITY SCHEMA v1

## Mục tiêu

Khóa mô hình dữ liệu trước khi xây demo.

## Entity bắt buộc

```text
Model_Version
Asset_Component
BIM_Binding
Sensor
Run
Source_Data
Condition_Evidence
Inspection_Record
Inspection_Finding
Action_Record
Action_Status_Event
Document
Actor
```

## 12.1 Model_Version

```text
Model_Version_ID
File_Name
SHA256
IFC_Schema
Exporter
Exported_At
Parent_Model_Version_ID
Container_Status
Purpose
```

## 12.2 Asset_Component

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

## 12.3 BIM_Binding

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

## 12.4 Sensor

```text
Sensor_ID
Sensor_Type
Sensor_Model
Channel
Axis
Sampling_Rate
Installed_Asset_ID
Installed_BIM_GUID
Model_Version_ID
Installation_Context
Calibration_Status
Sensor_Status
```

## 12.5 Run

```text
Run_ID
Campaign_ID
Acquisition_Session
State_Label
Excitation
Start_Time
Duration
Sensor_Mode
Source_File_Count
Quality_Status
```

## 12.6 Source_Data

```text
Source_Data_ID
Run_ID
Sensor_ID
File_Path
File_Name
SHA256
Sampling_Rate
Channel_Schema
Preprocessing_Version
Include_Exclude
Exclusion_Reason
```

## 12.7 Condition_Evidence

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

Lưu ý:

- CEI là confidence/evidence indicator.
- CEI không phải mức hư hỏng vật lý.

## 12.8 Inspection_Record

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

## 12.9 Action_Record

```text
Action_Record_ID
Inspection_Record_ID
Action_Type
Assigned_To
Decision_By
Decision_Date
Due_Date
Completion_Date
Current_Action_Status
Evidence_Reference
Comment
```

## 12.10 Action_Status_Event

```text
Action_Status_Event_ID
Action_Record_ID
Previous_Status
New_Status
Changed_By
Changed_At
Change_Reason
Evidence_Reference
```

## Output

```text
TRACEABILITY_SCHEMA_v1.0.md
TRACEABILITY_ER_MODEL_v1.0.md
TRACEABILITY_DATA_DICTIONARY_v1.0.csv
TRACEABILITY_STATUS_DICTIONARY_v1.0.csv
TRACEABILITY_RELATIONSHIP_MATRIX_v1.0.csv
```

## Công cụ

- Markdown;
- Mermaid/PlantUML;
- CSV;
- SQLite;
- JSON Schema nếu cần.

## PASS khi

- entity và relationship đủ;
- required/optional rõ;
- datatype rõ;
- cardinality rõ;
- versioning rõ;
- history không bị ghi đè.

---

# 13. R6 — INTEGRITY RULES

## Mục tiêu

Định nghĩa lỗi trước khi chạy Gate 3.

## Rule bắt buộc

### Identity

```text
IR-01 Asset_ID unique trong phạm vi
IR-02 BIM_GUID unique trong một Model_Version_ID
IR-03 Sensor_ID unique
IR-04 Condition_Evidence_ID unique
IR-05 Inspection_Record_ID unique
IR-06 Action_Record_ID unique
```

### Relationship

```text
IR-07 Evidence phải có Sensor_ID
IR-08 Evidence phải có Run_ID
IR-09 Sensor mapping phải có BIM_GUID + Model_Version_ID
IR-10 Inspection_Record phải có Asset_ID/BIM binding
IR-11 Trigger_Evidence_ID phải tồn tại nếu Trigger_Type = condition_evidence
IR-12 Action_Record phải tham chiếu Inspection_Record
```

### Status

```text
IR-13 verified cần reviewer + evidence
IR-14 rejected không được import
IR-15 superseded không phải current
IR-16 Action_Status thay đổi phải có event
```

### Provenance

```text
IR-17 IFC cần SHA-256 + Model_Version_ID
IR-18 Source data cần SHA-256
IR-19 Model result cần model version/config
IR-20 Audit output cần input manifest
```

## Output

```text
TRACEABILITY_INTEGRITY_RULES_v1.0.csv
TRACEABILITY_VALIDATION_RULES.sql
TRACEABILITY_VALIDATION_SPEC.md
```

## PASS khi

- mỗi rule có:
  - ID;
  - description;
  - severity;
  - query;
  - expected result;
  - failure action.

---

# 14. R7 — INSPECTION_RECORD VÀ ACTION_STATUS MODEL

## Mục tiêu

Đảm bảo traceability không dừng ở BIM object.

## Inspection trigger types

```text
routine
condition_evidence
data_quality_issue
manual_observation
follow_up
```

## Finding status

```text
not_inspected
no_visible_issue
observation_recorded
requires_follow_up
confirmed_issue
inconclusive
closed
```

## Action status

```text
Normal
Watch
Inspect
Priority_Inspection
In_Progress
Completed
Closed
```

Lưu ý:

- Bốn mức đầu là hỗ trợ lựa chọn hành động.
- `confirmed_issue` chỉ do inspection xác nhận.
- Condition evidence không tự tạo `confirmed_issue`.

## Output

```text
INSPECTION_RECORD_SCHEMA_v1.0.md
INSPECTION_FINDING_DICTIONARY_v1.0.csv
ACTION_STATUS_MODEL_v1.0.md
ACTION_STATUS_TRANSITION_RULES_v1.0.csv
```

## PASS khi

- evidence và finding tách biệt;
- recommendation và decision tách biệt;
- human review bắt buộc;
- transition history giữ lại.

---

# 15. R8 — PRE-REGISTER COMPETENCY QUESTIONS

## Mục tiêu

Khóa cách đánh giá trước Gate 3.

## CQ nhóm Identity

**CQ01.** Một Sensor_ID đang liên kết với BIM_GUID nào trong Model_Version_ID nào?

**CQ02.** BIM_GUID đó tương ứng Asset_ID nào?

**CQ03.** Có mapping nhiều–một hoặc một–nhiều ngoài quy tắc cho phép không?

## CQ nhóm Evidence

**CQ04.** Condition_Evidence_ID bắt nguồn từ Run_ID, Sensor_ID và Source_Data_ID nào?

**CQ05.** Evidence được tạo bởi model/config/evaluation protocol nào?

**CQ06.** Những evidence nào liên quan một Asset_ID/BIM_GUID cụ thể?

## CQ nhóm Inspection

**CQ07.** Evidence nào đã kích hoạt Inspection_Record_ID?

**CQ08.** Inspection_Record chứa finding và tài liệu nào?

**CQ09.** Từ Inspection_Record có truy ngược về đúng run và source file không?

## CQ nhóm Action

**CQ10.** Action_Status hiện tại là gì?

**CQ11.** Ai thay đổi trạng thái, khi nào và dựa trên evidence nào?

## CQ nhóm Integrity

**CQ12.** Có orphan Sensor/BIM/Evidence/Inspection/Action không?

**CQ13.** Có duplicate identifier hoặc conflicting binding không?

**CQ14.** Có verified record thiếu evidence/reviewer không?

## CQ nhóm Versioning

**CQ15.** BIM_GUID thuộc model version nào?

**CQ16.** Khi IFC đổi version, Asset_ID/BIM binding thay đổi thế nào?

## CQ nhóm Bidirectional Traceability

**CQ17.** Từ evidence có thể truy tới component → inspection → action không?

**CQ18.** Từ action có thể quay lại inspection → evidence → run → sensor không?

## CQ nhóm Reproducibility

**CQ19.** Một kết quả có thể tái lập từ input manifest và code version không?

**CQ20.** Hai lần chạy cùng fixture có trả kết quả giống nhau không?

## File

```text
GATE2_COMPETENCY_QUESTIONS_v1.0.md
GATE2_CQ_ACCEPTANCE_CRITERIA_v1.0.csv
GATE2_PRE_REGISTRATION_RECORD.md
```

## Trường acceptance criteria

```text
CQ_ID
Question
Required_Inputs
Query_or_Test
Expected_Output
Required_or_Optional
Pass_Criterion
Failure_Severity
Evidence_File
Approved_By
Approval_Date
```

## Ngưỡng vận hành đề xuất

Các ngưỡng này phải được phê duyệt trước Gate 3:

- 100% CQ bắt buộc trả lời đúng;
- 100% forward/reverse chain trên fixture hợp lệ;
- 100% orphan/duplicate fixture bắt buộc bị phát hiện;
- 0 unexpected duplicate trong valid dataset;
- 0 verified record thiếu reviewer/evidence;
- 100% result có provenance bắt buộc.

Không thay đổi ngưỡng sau khi xem kết quả, trừ khi ghi amendment có lý do.

---

# 16. R9 — PHÊ DUYỆT ASSET_ID PILOT

## Mục tiêu

Chuẩn bị 3–5 cấu kiện thật cho pilot import.

## File

```text
revit_asset_import_verified_pilot.csv
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

## Pilot đề xuất

- một cột;
- một dầm;
- một giằng hoặc parent connection;
- tối đa 3–5 assets.

## PASS khi

- 0 duplicate Asset_ID;
- 0 missing Revit element;
- 0 conflict;
- mọi dòng có reviewer;
- mọi dòng có evidence;
- `Import_Approved = TRUE`;
- file hash khóa.

---

# 17. R10 — GRAPH 02 DRY-RUN VÀ PILOT IMPORT

## Mục tiêu

Nhập Asset_ID thật vào Revit có kiểm soát.

## Graph

```text
02_import_verified_asset_data.dyn
```

## Lần đầu

```text
DRY_RUN = TRUE
```

## Dry-run kiểm tra

- CSV tồn tại;
- header đúng;
- Revit_UniqueId tồn tại;
- ElementId đối chứng;
- parameter tồn tại;
- parameter writable;
- Asset_ID unique;
- verification approved;
- old/new value;
- error list;
- số dòng dự kiến.

## Output

```text
GRAPH02_PILOT_DRY_RUN_LOG.csv
GRAPH02_PILOT_DRY_RUN_SUMMARY.md
GRAPH02_PILOT_INPUT_MANIFEST.csv
```

## Chỉ chạy write khi

- dry-run PASS;
- backup RVT;
- reviewer xác nhận;
- input hash khóa;
- rollback plan có sẵn.

## Sau write

1. Revit Schedule review.
2. Graph 01 export lại.
3. Compare pre/post crosswalk.
4. Kiểm tra chỉ đúng pilot assets được thay đổi.

## Output

```text
GRAPH02_PILOT_WRITE_LOG.csv
REVIT_PILOT_POST_IMPORT_CROSSWALK.csv
REVIT_PILOT_CHANGE_AUDIT.csv
```

## PASS khi

- đúng số dòng;
- đúng element;
- không unexpected spread;
- không thay Type;
- không ghi vào unapproved rows.

---

# 18. R11 — XUẤT OFFICIAL ENRICHED IFC

## File đề xuất

```text
model_revit2027_asset_enriched_pilot_v1.ifc
```

## Thiết lập

```text
IFC4X3_DT_ASSET_IDENTITY_ACCEPTED_V1
```

## Audit bắt buộc

### Container

- SHA-256;
- Model_Version_ID;
- parent version;
- schema;
- exporter;
- element count;
- GUID uniqueness;
- geometry readiness.

### Pset

- scoped Asset_ID count;
- property completeness;
- datatype;
- no test values;
- no spread.

### Binding

- ElementId ↔ Tag;
- BIM_GUID;
- Asset_ID;
- Model_Version_ID;
- conflict;
- orphan.

### IDS/script

- required properties;
- IFCTEXT;
- uniqueness script;
- provenance check.

## Output

```text
OFFICIAL_IFC_INPUT_MANIFEST.csv
MODEL_VERSION_REGISTRY.csv
ASSET_ID_UNIQUENESS_AUDIT.csv
REVIT_IFC_BINDING_AUDIT.csv
PSET_EXPORT_AUDIT.csv
GEOMETRY_PERSISTENCE_AUDIT.csv
IDS_REPORT.html
IFC_ENRICHMENT_ACCEPTANCE_RECORD.md
```

## PASS khi

- all pilot assets đúng;
- 0 duplicate;
- 0 unexpected spread;
- 0 verified thiếu evidence;
- geometry/identifier không suy giảm;
- no test marker.

---

# 19. R12 — GATE 2 CLOSURE REVIEW

## Hồ sơ bắt buộc

```text
05_GATE2/08_GATE2_CLOSURE/
├── GATE2_CLOSURE_REVIEW.md
├── GATE2_EVIDENCE_MATRIX.csv
├── GATE2_REQUIREMENT_TRACEABILITY_MATRIX.csv
├── GATE2_OPEN_ISSUES.csv
├── GATE2_DECISION_LOG.md
└── GATE2_CLOSURE_MANIFEST.csv
```

## Checklist

### Design

- [ ] Schema v1 khóa.
- [ ] Identifier chain khóa.
- [ ] Asset_ID convention khóa.
- [ ] Inspection_Record khóa.
- [ ] Action_Status khóa.
- [ ] Integrity rules khóa.

### Evaluation

- [ ] CQs pre-register.
- [ ] Acceptance criteria pre-register.
- [ ] Invalid-data plan khóa.
- [ ] Required/optional CQs rõ.

### BIM/AIM

- [ ] Pset ACCEPTED_V1.
- [ ] Pilot real Asset_ID.
- [ ] Official pilot enriched IFC.
- [ ] Round-trip audit.
- [ ] Scope review.
- [ ] 17 REVIT_ONLY được phân loại theo scope.
- [ ] Plate/fastener scope được chốt.

### Governance

- [ ] Human verification workflow.
- [ ] Input manifests.
- [ ] Hash.
- [ ] Versioning.
- [ ] Open issues rõ.

## Gate 2 verdict

```text
CLOSE
CLOSE_WITH_DECLARED_LIMITATIONS
DO_NOT_CLOSE
```

## Allowed conclusion khi đóng G2

> Mô hình dữ liệu, yêu cầu thông tin, chuỗi định danh và tiêu chí đánh giá truy vết đã được khóa trước khi thực hiện kiểm chứng end-to-end.

## Không được kết luận

> Traceability framework đã được kiểm chứng đầy đủ.

Đó là G3.

---

# 20. ĐIỀU KIỆN MỞ GATE 3

G3 chỉ mở khi:

1. G2 closure được phê duyệt;
2. CQs đã pre-register;
3. schema không còn thay đổi lớn;
4. lab evidence input từ G1 có provenance;
5. BIM pilot binding hoạt động;
6. Inspection_Record và Action_Status tạo được;
7. database/query layer sẵn sàng;
8. fixture plan khóa.

Nếu Gate 1 chưa đóng, G3 có thể dùng **controlled evidence fixture** để kiểm thử phần mềm/schema, nhưng không dùng để kết luận về laboratory state validity. Kết luận Paper 2 về traceability chỉ được gắn với evidence có provenance rõ.

---

# 21. R13 — CHUẨN BỊ LABORATORY TRACEABILITY FIXTURES

## Mục tiêu

Tạo dữ liệu kiểm thử có expected result.

## Nhóm valid fixtures

### VF-01 Normal chain

```text
Run
→ Sensor
→ Healthy/condition evidence
→ BIM component
→ routine inspection
→ Normal
```

### VF-02 Watch chain

```text
Run
→ state-change evidence
→ BIM component
→ review
→ Watch
```

### VF-03 Inspect chain

```text
Evidence
→ component
→ inspection request
→ finding pending
→ Inspect
```

### VF-04 Priority Inspection chain

Chỉ dùng khi context và review rule cho phép; không gọi damage.

## Nhóm invalid fixtures

```text
IF-01 Duplicate Sensor_ID
IF-02 Duplicate Asset_ID
IF-03 Duplicate BIM_GUID trong cùng model version
IF-04 Missing Model_Version_ID
IF-05 Orphan Condition_Evidence
IF-06 Missing Run_ID
IF-07 Missing Source_Data
IF-08 Orphan Inspection_Record
IF-09 Inspection thiếu Asset/BIM
IF-10 Action thiếu Inspection_Record
IF-11 verified thiếu reviewer
IF-12 invalid Action_Status transition
IF-13 conflicting Asset_ID–BIM binding
IF-14 superseded model được dùng như current
IF-15 broken document/photo link
IF-16 evidence thiếu model/evaluation provenance
```

## File

```text
GATE3_FIXTURE_REGISTER.csv
GATE3_VALID_FIXTURES/
GATE3_INVALID_FIXTURES/
GATE3_EXPECTED_RESULTS.csv
```

## PASS khi

- mỗi fixture có ID;
- input rõ;
- expected result rõ;
- CQ liên quan rõ;
- không sửa fixture sau test.

---

# 22. R14 — NẠP CONDITION EVIDENCE TỪ GATE 1

## Mục tiêu

Chuyển kết quả lab thành Condition_Evidence records có provenance.

## Input tối thiểu

```text
Run_ID
Sensor_ID
Source_Data_ID
Model_Name
Model_Version
Evaluation_Protocol
Held_Out_Run
Predicted_State
Confidence_or_CEI
Quality_Flag
Prediction_Timestamp
```

## Quy tắc

- evidence không được tách khỏi Run_ID;
- evidence không được tách khỏi Sensor_ID;
- model version bắt buộc;
- evaluation protocol bắt buộc;
- không gọi predicted state là damage diagnosis;
- CEI không phải severity.

## File

```text
CONDITION_EVIDENCE_REGISTER.csv
CONDITION_EVIDENCE_INPUT_MANIFEST.csv
CONDITION_EVIDENCE_IMPORT_LOG.csv
```

## PASS khi

- 100% evidence có run/sensor/source;
- no orphan;
- model provenance đầy đủ;
- quality flag rõ.

---

# 23. R15 — TRIỂN KHAI DATABASE VÀ QUERY LAYER

## Mục tiêu

Tạo implementation tối thiểu để kiểm chứng, không phát triển commercial platform.

## Công cụ đề xuất

```text
SQLite
Python
SQL
IfcOpenShell
CSV import/export
```

PostgreSQL chỉ dùng nếu có nhu cầu multi-user thực.

## Tables

```text
model_version
asset_component
bim_binding
sensor
run
source_data
condition_evidence
inspection_record
inspection_finding
action_record
action_status_event
document
actor
validation_issue
```

## View/query đề xuất

```text
vw_sensor_to_component
vw_evidence_to_component
vw_evidence_to_inspection
vw_inspection_to_action
vw_forward_trace
vw_reverse_trace
vw_orphans
vw_duplicates
vw_provenance_completeness
```

## Output

```text
traceability_lab_v1.sqlite
schema.sql
constraints.sql
views.sql
seed_valid_fixtures.sql
seed_invalid_fixtures.sql
```

## PASS khi

- constraints chạy;
- imports deterministic;
- database rebuild từ script;
- không manual edit bí mật.

---

# 24. R16 — FORWARD TRACEABILITY TEST

## Chuỗi

```text
Condition_Evidence_ID
→ Sensor_ID
→ BIM_GUID + Model_Version_ID
→ Asset_ID
→ Inspection_Record_ID
→ Action_Record_ID
→ Action_Status
```

## Output

```text
FORWARD_TRACE_RESULTS.csv
FORWARD_TRACE_QUERY_LOG.sql
FORWARD_TRACE_REVIEW.md
```

## Kiểm tra

- correct component;
- correct model version;
- correct inspection;
- correct action;
- no missing link;
- deterministic output.

## PASS đề xuất

- 100% valid fixture bắt buộc trace thành công;
- 0 unexpected component;
- 0 wrong version;
- 0 hidden manual join.

---

# 25. R17 — REVERSE TRACEABILITY TEST

## Chuỗi

```text
Action_Status
→ Action_Record
→ Inspection_Record
→ Condition_Evidence_ID
→ Run_ID
→ Sensor_ID
→ Source_Data_ID
```

## Output

```text
REVERSE_TRACE_RESULTS.csv
REVERSE_TRACE_QUERY_LOG.sql
REVERSE_TRACE_REVIEW.md
```

## PASS đề xuất

- 100% required valid fixture quay về đúng source;
- đúng run;
- đúng sensor;
- đúng model/evaluation provenance;
- không ambiguity.

---

# 26. R18 — INVALID-DATA TESTS

## Mục tiêu

Chứng minh framework phát hiện lỗi, không chỉ chạy dữ liệu đẹp.

## Test groups

### Duplicate

- Asset_ID;
- Sensor_ID;
- BIM_GUID/version;
- evidence ID;
- inspection ID.

### Orphan

- sensor không BIM;
- evidence không run;
- inspection không component;
- action không inspection.

### Provenance

- missing hash;
- missing model version;
- missing evaluation protocol;
- missing reviewer.

### Status

- auto-verified;
- invalid transition;
- superseded used as current.

### Version

- GUID reused in wrong version;
- conflicting binding;
- parent version missing.

## Output

```text
INVALID_DATA_TEST_RESULTS.csv
INVALID_FIXTURE_DETECTION_MATRIX.csv
ORPHAN_DUPLICATE_REPORT.csv
PROVENANCE_FAILURE_REPORT.csv
STATUS_TRANSITION_FAILURE_REPORT.csv
```

## PASS đề xuất

- 100% mandatory invalid fixtures bị phát hiện;
- issue code đúng;
- severity đúng;
- valid fixtures không bị false reject.

---

# 27. R19 — END-TO-END LAB SCENARIOS

## Scenario S1 — Normal

```text
Valid run
→ sensor
→ evidence within accepted condition
→ component
→ inspection record
→ Normal
```

## Scenario S2 — Watch

```text
State-change evidence
→ component
→ review
→ Watch
→ follow-up schedule
```

## Scenario S3 — Inspect

```text
Evidence + review
→ inspection request
→ inspector record
→ finding inconclusive/observation
→ Inspect
```

## Scenario S4 — Data quality issue

```text
Sensor quality failure
→ quality flag
→ sensor inspection record
→ no structural diagnosis
```

## Scenario S5 — BIM version update

```text
Old BIM_GUID/version
→ new IFC version
→ Asset_ID persistent
→ binding history retained
```

## Scenario S6 — Invalid chain

```text
orphan/conflict
→ validation failure
→ no action recommendation
```

## Output

```text
GATE3_SCENARIO_REGISTER.csv
GATE3_SCENARIO_RESULTS.csv
GATE3_SCENARIO_EVIDENCE/
```

---

# 28. R20 — ĐÁNH GIÁ COMPETENCY QUESTIONS

## File

```text
GATE3_CQ_RESULTS.csv
```

## Trường

```text
CQ_ID
Fixture_ID
Query_Version
Expected_Output
Actual_Output
Pass_Fail
Execution_Time
Evidence_File
Issue_Code
Reviewer
Review_Note
```

## Metrics

```text
CQ_Pass_Rate
Forward_Trace_Success_Rate
Reverse_Trace_Success_Rate
Orphan_Detection_Rate
Duplicate_Detection_Rate
Missing_Link_Detection_Rate
Provenance_Completeness
Query_Reproducibility
```

## Cảnh báo

Không dùng các metric trên như Health Index hoặc damage severity.

---

# 29. R21 — GATE 3 CLOSURE REVIEW

## Hồ sơ

```text
06_GATE3/
├── 00_GOVERNANCE/
├── 01_FIXTURES/
├── 02_DATABASE/
├── 03_FORWARD_TRACE/
├── 04_REVERSE_TRACE/
├── 05_INVALID_DATA_TESTS/
├── 06_SCENARIOS/
├── 07_CQ_RESULTS/
├── 08_GATE3_CLOSURE/
└── 99_ARCHIVE/
```

## Closure package

```text
GATE3_CLOSURE_REVIEW.md
GATE3_EVIDENCE_MATRIX.csv
GATE3_CQ_RESULTS.csv
GATE3_REQUIREMENT_TRACEABILITY_MATRIX.csv
GATE3_OPEN_ISSUES.csv
GATE3_REPRODUCIBILITY_MANIFEST.csv
GATE3_DECISION_LOG.md
```

## Checklist

### Chain validity

- [ ] Forward trace đạt.
- [ ] Reverse trace đạt.
- [ ] Correct model version.
- [ ] Correct asset/component.
- [ ] Correct inspection.
- [ ] Correct action.

### Integrity

- [ ] No unexpected duplicate.
- [ ] No unexpected orphan.
- [ ] Invalid fixtures detected.
- [ ] Status transitions valid.
- [ ] Verified records có evidence.

### Reproducibility

- [ ] Database rebuild được.
- [ ] Fixtures immutable.
- [ ] Query version khóa.
- [ ] Input/output hash.
- [ ] Code commit.
- [ ] Environment record.

### Academic

- [ ] CQs pre-register trước test.
- [ ] Không thay ngưỡng sau kết quả.
- [ ] Claim audit hoàn tất.
- [ ] Limitations rõ.
- [ ] No field diagnosis claim.
- [ ] No FEM-core claim.

## Gate verdict

```text
CLOSE
CLOSE_WITH_DECLARED_LIMITATIONS
DO_NOT_CLOSE
```

## Allowed claim khi đóng G3

> Chuỗi truy vết component-level đã chạy hai chiều trong case phòng thí nghiệm, trả lời đúng các competency questions được công bố trước, đồng thời phát hiện được các lỗi định danh và quan hệ đã thiết kế.

## Prohibited claim

> Framework đã chẩn đoán hư hỏng công trình thực hoặc chứng minh bảo trì dự báo.

---

# 30. PAPER 2 EVIDENCE PACKAGE

## Folder

```text
10_PAPERS/PAPER2/
├── 00_CONCEPT/
├── 01_METHOD/
├── 02_G2_EVIDENCE/
├── 03_G3_EVIDENCE/
├── 04_TABLES/
├── 05_FIGURES/
├── 06_RESULTS/
├── 07_LIMITATIONS/
├── 08_REPRODUCIBILITY/
└── 09_SUBMISSION/
```

## Tables đề xuất

1. Entity and identifier dictionary.
2. Revit–IFC information readiness.
3. Pset validation.
4. Competency questions.
5. Integrity rules.
6. Forward/reverse query results.
7. Invalid-data detection.
8. Scenario results.
9. Limitations and scope.

## Figures đề xuất

1. Evidence-to-action architecture.
2. Identifier chain.
3. Revit–IFC–AIM information flow.
4. ER diagram.
5. Gate 2–Gate 3 validation design.
6. Forward trace example.
7. Reverse trace example.
8. Invalid-data test architecture.
9. BIM-linked inspection record example.

---

# 31. CHƯƠNG 5 — CẤU TRÚC THỰC THI

## 5.1 Introduction

- evidence-to-action gap;
- RQ2;
- objectives;
- chapter structure.

## 5.2 Information management positioning

- AIM semantics;
- Revit authoring;
- IFC exchange;
- Asset_ID;
- BIM_GUID;
- Model_Version_ID;
- ISO 19650/TCVN 14177 alignment.

## 5.3 BIM Information Readiness

- baseline IFC;
- model version;
- identity gap;
- geometry;
- IDS;
- link audit.

## 5.4 Revit–IFC controlled exchange

- Shared Parameters;
- Dynamo crosswalk;
- structural whitelist;
- sync IFC;
- round-trip audit;
- Pset acceptance.

## 5.5 Scope and identifier governance

- sensor target scope;
- inspection unit;
- Asset_ID;
- versioning.

## 5.6 Traceability schema

- entities;
- relationships;
- data dictionary;
- integrity rules.

## 5.7 Inspection and action records

- trigger;
- finding;
- action;
- status history.

## 5.8 Competency questions

- pre-registration;
- expected outputs;
- acceptance.

## 5.9 End-to-end lab implementation

- fixtures;
- database;
- forward/reverse queries.

## 5.10 Invalid-data tests

- duplicate;
- orphan;
- provenance;
- version conflict.

## 5.11 Results

- CQ pass;
- trace success;
- detection rates;
- reproducibility.

## 5.12 Discussion

- contribution;
- management significance;
- AIM implications;
- limits.

## 5.13 Conclusion

- answer RQ2;
- transition to field feasibility.

---

# 32. QUAN HỆ VỚI ISO 19650 VÀ TCVN 14177

Roadmap áp dụng theo hướng:

- yêu cầu thông tin được xác định trước;
- container có phiên bản và trạng thái;
- trao đổi có tiêu chí chấp nhận;
- Revit là authoring tool;
- IFC là exchange container;
- Asset_ID là định danh nghiệp vụ;
- BIM_GUID là object identifier;
- Model_Version_ID tạo ngữ cảnh;
- AIM là tập hợp thông tin phục vụ vận hành;
- audit và human approval được tách.

Không tuyên bố:

> hệ thống được chứng nhận hoặc hoàn toàn phù hợp ISO 19650/TCVN 14177.

Cách viết:

> Quy trình được tổ chức theo hướng hỗ trợ quản lý yêu cầu thông tin, định danh, phiên bản, trao đổi, kiểm tra và truy vết phù hợp với định hướng ISO 19650 và TCVN 14177.

---

# 33. CÔNG CỤ VÀ TRÁCH NHIỆM

| Công cụ | Vai trò |
|---|---|
| Revit | Tạo lập/duy trì property |
| Shared Parameters | Định nghĩa trường |
| Revit Schedule | QA trước xuất |
| Dynamo Graph 01 | Crosswalk chỉ đọc |
| Dynamo Graph 02 | Import dữ liệu đã duyệt |
| IFC Exporter | Tạo exchange container |
| IfcOpenShell | Audit IFC, geometry, Pset, GUID |
| IfcTester/IDS | Entity-level validation |
| Python | Hash, manifests, validation, reports |
| SQLite | Gate 3 implementation |
| Excel/CSV | Review, scope, approval |
| Git | Code/version control |
| Claude Code | Hỗ trợ code/audit, không quyết định verified |
| Con người | Asset_ID, scope, review, acceptance |

---

# 34. KẾ HOẠCH THỜI GIAN THAM KHẢO

> Thời gian không thay Evidence Gate.

| Tuần | Công việc |
|---|---|
| 1 | R0–R2: governance, freeze Pset, clean working model |
| 2–3 | R3–R4: target scope, Asset_ID convention |
| 3–5 | R5–R7: schema, integrity, inspection/action model |
| 5–6 | R8: competency questions và pre-registration |
| 6–7 | R9–R10: Asset_ID pilot, Graph 02 dry-run/import |
| 7–8 | R11: official enriched IFC audit |
| 8 | R12: Gate 2 closure |
| 9–10 | R13–R15: fixtures, condition evidence, database |
| 11 | R16–R17: forward/reverse tests |
| 12 | R18: invalid-data tests |
| 13 | R19–R20: scenarios và CQ evaluation |
| 14 | R21: Gate 3 closure |
| 15–16 | Paper 2 tables, figures, manuscript |

Điều kiện:

- G3 không kết luận state validity nếu G1 evidence chưa đủ.
- G2 có thể triển khai song song với G1.
- G3 chỉ mở chính thức sau G2 closure.

---

# 35. STOP/GO DECISION TABLE

| Mốc | GO khi | STOP khi |
|---|---|---|
| Freeze Pset | 41/41 PASS + mapping hash | mapping chưa xác định |
| Scope | component/inspection unit rõ | chọn toàn bộ model |
| Asset_ID | reviewer + evidence + unique | auto-generated chưa duyệt |
| Graph 02 | dry-run PASS | duplicate/missing element |
| Official IFC | no test value + audit PASS | Pset mất hoặc lan dữ liệu |
| Close G2 | CQs/schema/pre-registration đủ | acceptance criteria chưa khóa |
| Open G3 | G2 closed | schema còn đổi lớn |
| Forward/reverse | deterministic | hidden manual step |
| Invalid tests | fixtures immutable | sửa fixture sau khi xem kết quả |
| Close G3 | all mandatory criteria đạt | orphan/duplicate chưa xử lý |

---

# 36. RISK REGISTER G2–G3

| Rủi ro | Ảnh hưởng | Kiểm soát |
|---|---|---|
| Asset_ID tự sinh sai | Mất validity | human verification |
| GUID thay đổi | Binding sai | Asset_ID + Model_Version_ID |
| IFC mất Pset | Exchange failure | accepted setup |
| Runtime file bị ghi đè | Không tái lập | immutable + hash |
| CQs viết sau demo | confirmation bias | pre-register |
| Demo chỉ chạy valid data | Paper yếu | invalid-data tests |
| Plate/bolt kéo scope | scope creep | parent inspection unit |
| 17 REVIT_ONLY | orphan | scope-based resolution |
| Website mở rộng | mất thời gian | SQLite/query first |
| Gate 1 chưa đủ | evidence claim yếu | separate traceability from state validity |
| AI auto-verified | governance breach | prohibit |
| ISO overclaim | phản biện | aligned, not certified |

---

# 37. EVIDENCE MATRIX G2–G3

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

Mỗi bảng/hình Paper 2 phải truy về Evidence_ID.

---

# 38. CLAIM → EVIDENCE → LIMITATION → NEXT ACTION

## Claim hiện tại

Đường truyền 7 Shared Parameters từ Revit sang `Pset_DT_AssetIdentity` đã được kiểm chứng trên IfcColumn và IfcBeam mà không làm thay đổi identity hoặc geometry.

## Evidence

- 41/41 PASS;
- 14/14 values;
- 0 spread;
- 0 verified;
- GUID/class/geometry stable;
- manifests và hashes.

## Limitation

- test data;
- 2/1.703 elements;
- chưa có Asset_ID thật;
- G2 schema/CQs chưa khóa;
- G3 chưa chạy;
- 17 REVIT_ONLY;
- plate/fastener scope chưa chốt.

## Next action duy nhất

```text
Freeze Pset ACCEPTED_V1
→ clean working model
→ create and review sensor_target_scope.csv
```

Chưa chạy Graph 02 write cho đến khi Asset_ID pilot được phê duyệt.

---

# 39. GATE 2 CLOSURE STATEMENT MẪU

> Gate 2 được đóng sau khi mô hình dữ liệu truy vết v1, chuỗi định danh, cấu trúc Inspection_Record và Action_Status, competency questions, tiêu chí đánh giá, quy tắc integrity, phạm vi asset/sensor và quy trình Revit–IFC được phê duyệt và khóa trước kiểm chứng. Gate 2 xác nhận mức sẵn sàng thiết kế, không xác nhận end-to-end traceability validity.

---

# 40. GATE 3 CLOSURE STATEMENT MẪU

> Gate 3 được đóng sau khi case phòng thí nghiệm thực hiện thành công truy vết hai chiều từ condition evidence đến BIM-linked component, inspection record và action status; trả lời đúng các competency questions bắt buộc; phát hiện các fixture mồ côi, trùng và thiếu provenance; đồng thời cung cấp đầy đủ manifest, code version và bằng chứng tái lập. Kết quả chứng minh traceability validity trong phạm vi laboratory case, không chứng minh field damage diagnosis hoặc predictive maintenance.

---

# 41. ROADMAP LOCK

Roadmap này khóa:

```text
RQ2 / WP2 / Chương 5 / Paper 2
Revit → IFC → AIM identity pipeline
Gate 2 design readiness
Gate 3 end-to-end lab validation
Limited-FEM firewall
Pre-registration requirement
Invalid-data testing requirement
Bidirectional traceability requirement
```

Mọi nhiệm vụ mới phải trả lời:

1. Nó phục vụ CQ hoặc integrity rule nào?
2. Nó đóng G2 hay G3?
3. Evidence file nào được tạo?
4. Tiêu chí PASS là gì?
5. Có làm thay đổi pre-registration không?
6. Thuộc Core, Supporting, Future hay Out of Scope?

Không trả lời được sáu câu này thì không đưa vào G2–G3.

---

# 42. NGUỒN NỘI BỘ PHẢI ĐỌC KÈM

1. `MASTER_RESEARCH_CHARTER_v1.1_LIMITED_FEM_20260717.md`
2. `RESEARCH_DIRECTION_AND_SCOPE.md`
3. `RESEARCH_ARCHITECTURE.md`
4. `CURRENT_STATUS_AND_NEXT_DIRECTION.md`
5. `RESEARCH_ARCHITECTURE_DECISION_RECORD_20260717.md`
6. `THE_COUNCIL_REVIEW_FEM_OR_NO_FEM_17.07.2026.md`
7. `PHASE1_RESEARCH_WALKTHROUGH.md`
8. `PSET_7_PARAMETER_QUICK_REVIEW.md`
9. `Revit-IFCGuide.md`
10. `roadmap.md`
11. `PHD_BIM_AIM_IMPLEMENTATION_ROADMAP.md`

---

# 43. PHÁN QUYẾT ĐIỀU HÀNH

1. Công việc Revit–IFC hiện tại đủ để khóa exchange setup, chưa đủ đóng G2.
2. Bước tiếp theo không phải mở rộng dashboard; phải khóa scope, schema và CQs.
3. Graph 02 chỉ chạy dry-run sau khi Asset_ID pilot được phê duyệt.
4. G2 đóng trước khi xây case G3 chính thức.
5. G3 bắt buộc có forward, reverse và invalid-data tests.
6. Paper 2 chỉ mạnh khi chứng minh được traceability validity, không phải vì có BIM model.
7. Kết quả G3 chỉ có giá trị laboratory traceability; field feasibility thuộc G4.
