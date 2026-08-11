# ROADMAP G2–G3 VÀ PAPER 2 — BẢN HIỆU CHỈNH THEO THE COUNCIL
## Verifiable Component-Level Traceability: Vibration Evidence → BIM Component → Inspection Record → Action Status

**Tên tệp:** `G2_G3_PAPER2_REVISED_ROADMAP_v1.1.md`  
**Phiên bản:** v1.1 — Major Revision theo góp ý The Council  
**Ngày:** 03/08/2026  
**Luận án:** Phát triển khung Digital Twin dựa trên dữ liệu phục vụ giám sát trạng thái và hỗ trợ kiểm tra, bảo trì nhà công nghiệp khung thép ven biển  
**Lĩnh vực:** Quản lý xây dựng / Quản lý tài sản  
**RQ/WP:** RQ2 / WP2  
**Chương/Paper:** Chương 5 / Paper 2  
**Evidence Gates:** Gate 2 – Traceability Design Readiness; Gate 3 – End-to-End Laboratory Traceability  
**Kiến trúc:** Limited-FEM  
**Mốc kỹ thuật hiện tại:** `READY TO FREEZE PSET EXPORT SETUP`  
**Trạng thái:** Gate 2 đang mở; Gate 3 chưa mở  

---

# 0. QUYẾT ĐỊNH CHIẾN LƯỢC SAU PHẢN BIỆN

## 0.1. Phán quyết

The Council đánh giá:

```text
ACCEPT WITH MAJOR REVISION
```

Điều này được hiểu là:

- hướng RQ2/Paper 2 vẫn đúng;
- kiến trúc G2–G3 không phải thiết kế lại;
- phải sửa trình tự phương pháp luận;
- phải bổ sung các quy tắc còn thiếu;
- phải tăng tính quản lý tài sản và tính học thuật của Paper 2;
- chưa được tiếp tục Graph 02 write hoặc mở Gate 3.

## 0.2. Các sửa đổi bắt buộc đã tiếp nhận

| Council Issue | Quyết định |
|---|---|
| CQ được đặt sau schema draft | Đưa CQ derivation và pre-registration lên trước **schema v1 lock** |
| Thiếu rule conflicting binding | Bổ sung `IR-21 — Conflicting Asset–BIM Binding` |
| Finding → Action chưa rõ | Xây **permitted transition rules**, không tự động ra quyết định |
| Chưa phân Required/Supporting CQ | Khóa phân loại trước Gate 3 |
| 17 `REVIT_ONLY` | Chỉ là blocker nếu nằm trong Core Scope |
| 1.002 phần tử không Tag | Không phải blocker nếu không phải inspection unit |
| Novelty chưa nổi bật | Đặt **vibration evidence-to-inspection traceability** làm đóng góp trung tâm |
| Thiếu management usefulness | Bổ sung review ngữ nghĩa nhẹ với 2–3 chuyên gia; Supporting Evidence |
| Outline FEM cũ | Đánh dấu superseded theo Charter v1.1 và ADR Limited-FEM |

## 0.3. Nguyên tắc không được vi phạm

```text
CQ phải xuất phát từ RQ2 và nhu cầu quản lý,
không được “may đo” sau khi biết schema hoặc kết quả test.

Schema hiện tại chỉ là concept draft.
Schema v1 chỉ được khóa sau CQ pre-registration.

Gate 2 đóng trước khi Gate 3 mở.

Gate 3 phải có:
forward trace
+ reverse trace
+ invalid-data tests
+ reproducibility.

Revit, IFC, Dynamo, SQLite là research instruments,
không phải đóng góp học thuật chính.
```

---

# 1. ĐỊNH VỊ NGHIÊN CỨU

## 1.1. RQ2

> Bằng chứng trạng thái từ dữ liệu cảm biến được tổ chức và liên kết với cấu kiện BIM và hồ sơ kiểm tra như thế nào để bảo đảm khả năng truy vết ở cấp cấu kiện?

## 1.2. WP2

```text
BIM–Sensor–Inspection traceability
```

## 1.3. Chương và Paper

| Thành phần | Nội dung |
|---|---|
| Chương 5 | Traceability framework |
| Paper 2 | Verifiable component-level traceability |
| Gate 2 | Data model, requirements, CQ, criteria, scope |
| Gate 3 | End-to-end laboratory validation |
| Validation level | V2 — Traceability validity |

## 1.4. Chuỗi nghiên cứu

```text
Vibration data
→ condition/state-change evidence
→ BIM-linked component
→ inspection record
→ inspection-maintenance action support
```

## 1.5. Chuỗi định danh

```text
Sensor_ID
→ BIM_GUID
→ Condition_Evidence_ID
→ Inspection_Record_ID
→ Action_Status
```

Định danh hỗ trợ:

```text
Asset_ID
Model_Version_ID
Run_ID
Source_Data_ID
Revit_UniqueId
Revit_ElementId
Action_Record_ID
```

## 1.6. FEM firewall

FEM chỉ được mô tả:

> nominal, uncalibrated, reference-only, not used for damage diagnosis.

`FEM_Node_ID` chỉ là metadata tùy chọn.

Không có FEM Gate, FEM Paper hoặc FEM contribution trong RQ2.

---

# 2. ĐÓNG GÓP PAPER 2 ĐÃ HIỆU CHỈNH

## Contribution 1 — Evidence-to-inspection traceability

Một mô hình truy vết hình thức liên kết:

```text
vibration-based condition evidence
→ BIM-linked component
→ inspection record
→ action status
```

với provenance từ dữ liệu nguồn, Run_ID, Sensor_ID và model/evaluation version.

## Contribution 2 — Versioned identity governance

Một kiến trúc phân biệt rõ:

```text
Asset_ID
BIM_GUID
Model_Version_ID
Revit_UniqueId
Revit_ElementId
```

và duy trì lịch sử binding qua các phiên bản IFC.

## Contribution 3 — Pre-registered validation

Một phương pháp kiểm chứng gồm:

- competency questions có nguồn gốc từ RQ2/use case;
- tiêu chí chấp nhận khóa trước;
- forward trace;
- reverse trace;
- duplicate/orphan/conflict detection;
- invalid-data fixtures;
- reproducibility manifest.

## Contribution 4 — Inspection-oriented information semantics

Một cấu trúc tách biệt:

```text
condition evidence
≠ inspection finding
≠ recommended action
≠ authorized decision
```

và giữ lịch sử trạng thái có con người rà soát.

## Không được coi là contribution

- xây Revit model;
- xuất IFC;
- dùng Dynamo;
- tạo SQLite;
- làm website/dashboard;
- gắn sensor icon;
- tạo hyperlink;
- chạy demo một chiều.

---

# 3. PHẠM VI G2–G3

## Core Scope

- condition evidence provenance;
- Asset_ID và BIM_GUID governance;
- Model_Version_ID;
- component-level binding;
- competency questions;
- traceability schema;
- Inspection_Record;
- Action_Status history;
- integrity rules;
- forward/reverse traceability;
- invalid-data tests;
- laboratory end-to-end validation.

## Supporting Scope

- Revit 2027.1;
- Dynamo 4.0;
- IFC4X3;
- Shared Parameters;
- `Pset_DT_AssetIdentity`;
- IfcOpenShell;
- IfcTester/IDS;
- SQLite;
- Excel/CSV;
- Git;
- ISO 19650 và TCVN 14177 framing;
- management semantic review.

## Future Work

- ontology/knowledge graph quy mô lớn;
- bolt-level asset management;
- multi-building AIM;
- live Digital Twin;
- production CDE;
- commercial platform.

## Out of Scope

- field damage diagnosis;
- calibrated FEM;
- stiffness degradation;
- RUL;
- predictive maintenance;
- complex Health Index;
- autonomous maintenance;
- optimal sensor placement;
- direct lab-to-field classifier transfer.

---

# 4. HIỆN TRẠNG BẰNG CHỨNG

## 4.1. BIM Information Readiness đã có

- Model Version Registry;
- Component Registry;
- BIM Binding Registry;
- geometry readiness;
- Coordinate_Quality;
- IDS baseline;
- link audit;
- no auto-verified mapping.

## 4.2. Revit–IFC pipeline

Môi trường:

```text
Revit 2027.1
Dynamo 4.0
IFC4X3_ADD2
IfcOpenShell
```

Kết quả chính:

| Chỉ số | Giá trị |
|---|---:|
| Structural crosswalk | 718 |
| IFC sync IfcElement | 3.468 |
| Structural elements | 1.703 |
| GUID unique | 3.468/3.468 |
| Geometry usable | 1.703/1.703 |
| `MATCH_TAG_AND_GUID` | 685/718 |
| IFC counterpart duy nhất | 701/718 |
| `REVIT_ONLY` | 17 |
| Plate/fastener không Tag | 1.002 |

## 4.3. Pset validation

```text
Pset_DT_AssetIdentity
```

Bảy trường:

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

```text
41/41 PASS
14/14 values match
0 data spread
0 verified
0 identifier change
0 geometry change
```

## 4.4. Ý nghĩa đúng

Đã chứng minh:

> Đường trao đổi thông tin Revit → IFC hoạt động trên IfcColumn và IfcBeam.

Chưa chứng minh:

- Asset_ID thật đúng;
- toàn bộ model sẵn sàng AIM;
- traceability end-to-end;
- Inspection_Record hoạt động;
- Gate 2 đóng;
- Gate 3 đạt.

---

# 5. ĐỊNH NGHĨA GATE

## 5.1. Gate 2 — Traceability Design Readiness

Gate 2 xác nhận rằng:

- câu hỏi nghiên cứu đã được chuyển thành câu hỏi kiểm chứng;
- tiêu chí chấp nhận được khóa trước;
- phạm vi asset/inspection unit rõ;
- identifier governance rõ;
- schema và integrity rules khóa;
- Inspection_Record và Action_Status rõ;
- Revit–IFC exchange được chấp nhận;
- pilot official binding hoạt động;
- Gate 3 có thể bắt đầu mà không cần thay đổi thiết kế lớn.

Gate 2 không xác nhận traceability validity.

## 5.2. Gate 3 — End-to-End Laboratory Traceability

Gate 3 xác nhận rằng:

- chain chạy hai chiều;
- CQs bắt buộc được trả lời đúng;
- invalid records bị phát hiện;
- valid records không bị loại sai;
- version ambiguity được xử lý;
- provenance đầy đủ;
- implementation tái lập được;
- claim chỉ giới hạn laboratory traceability.

---

# 6. TRÌNH TỰ PHƯƠNG PHÁP ĐÃ SỬA

## Trình tự cũ cần thay

```text
Scope
→ Asset_ID
→ Schema
→ Integrity
→ Inspection/Action
→ CQ
```

## Trình tự mới

```text
PHASE A — Freeze technical evidence
A1 Freeze Pset ACCEPTED_V1
A2 Create clean working model
A3 Lock manifests and provenance

PHASE B — Derive evaluation from RQ2
B1 Define management use cases
B2 Draft competency questions
B3 Create CQ source/rationale matrix
B4 Classify Required/Supporting
B5 Freeze acceptance criteria
B6 Pre-register before schema v1 lock

PHASE C — Finalize design
C1 Define sensor/asset target scope
C2 Lock Asset_ID convention
C3 Finalize schema v1 to answer pre-registered CQ
C4 Add integrity rules including IR-21
C5 Lock Inspection_Record semantics
C6 Lock permitted action transitions

PHASE D — Controlled implementation
D1 Approve Asset_ID pilot
D2 Graph 02 dry-run
D3 Pilot write
D4 Export official enriched IFC
D5 Full audit

PHASE E — Close Gate 2
E1 Closure review
E2 Freeze schema/CQ/criteria
E3 Open Gate 3 only after approval

PHASE F — Gate 3 validation
F1 Immutable valid/invalid fixtures
F2 Load real laboratory condition evidence
F3 Build deterministic database/query layer
F4 Forward trace
F5 Reverse trace
F6 Invalid-data tests
F7 End-to-end scenarios
F8 CQ evaluation
F9 Management semantic review
F10 Reproducibility and closure

PHASE G — Paper 2
G1 Freeze evidence package
G2 Tables/figures
G3 Draft manuscript
G4 Internal review
G5 Submission readiness
```

---

# 7. PHASE A — FREEZE TECHNICAL EVIDENCE

## A1. Khóa Pset ACCEPTED_V1

### Output

```text
IFC4X3_DT_ASSET_IDENTITY_ACCEPTED_V1
DT_UserDefinedPropertySets_ACCEPTED_V1.txt
PSET_EXPORT_ACCEPTANCE_RECORD.md
```

### Acceptance record bắt buộc

```text
Acceptance_ID
Revit_Version
Dynamo_Version
IFC_Exporter_Version
IFC_Schema
Setup_Name
Mapping_SHA256
Pset_Name
Property_Count
Data_Type
Test_Classes
Audit_Result
Limitations
Accepted_By
Acceptance_Date
Change_Control
```

### PASS

- 7/7 property;
- `IFCTEXT`;
- 41/41 PASS được dẫn chiếu;
- mapping file immutable;
- hash khóa;
- test files archive;
- không sửa ACCEPTED_V1.

## A2. Working model sạch

### File

```text
model_revit2027_asset_working_v1.rvt
```

### Quét marker

```text
TEST-
test_only
EXPORT-TEST
EXPORT_VALIDATION_TEST
```

### Output

```text
WORKING_MODEL_CLEANLINESS_AUDIT.csv
WORKING_MODEL_BASELINE_MANIFEST.csv
```

### PASS

- 0 test marker;
- 0 verified thiếu evidence;
- model/version/hash ghi lại.

## A3. Governance snapshot

### Output

```text
G2_CURRENT_INPUT_MANIFEST.csv
G2_CURRENT_STATUS_SNAPSHOT.md
G2_DECISION_LOG.md
```

### PASS

- mọi file quan trọng có SHA-256;
- runtime/canonical phân biệt rõ;
- no overwrite;
- source Revit ↔ IFC relationship rõ.

---

# 8. PHASE B — COMPETENCY QUESTIONS TRƯỚC SCHEMA LOCK

## B1. Management use cases

Tạo:

```text
GATE2_MANAGEMENT_USE_CASES_v1.0.md
```

Use cases tối thiểu:

1. tìm component từ Sensor_ID;
2. tìm Asset_ID từ BIM object;
3. truy condition evidence đến source run;
4. tạo Inspection_Record từ evidence;
5. truy ngược Action_Status đến evidence;
6. phát hiện orphan/duplicate/conflict;
7. xử lý IFC version update;
8. kiểm tra record có đủ reviewer/provenance.

## B2. CQ source and rationale matrix

Tạo:

```text
GATE2_CQ_SOURCE_AND_RATIONALE_MATRIX.csv
```

Trường:

```text
CQ_ID
Management_Question
RQ2_Link
Use_Case_ID
Independent_Source
Why_Needed
Required_Output
Candidate_Schema_Element
Required_or_Supporting
Approval_Status
Reviewer
Review_Date
```

Mục tiêu:

> Chứng minh CQ xuất phát từ RQ2 và nhu cầu quản lý, không phải từ database đã thiết kế.

## B3. Bộ competency questions

### Identity

- CQ01: Sensor_ID liên kết BIM_GUID nào trong Model_Version_ID nào?
- CQ02: BIM_GUID tương ứng Asset_ID nào?
- CQ03: Có mapping nhiều–một/một–nhiều ngoài rule không?

### Evidence provenance

- CQ04: Condition_Evidence_ID bắt nguồn Run_ID, Sensor_ID, Source_Data_ID nào?
- CQ05: Evidence được tạo bởi model/config/evaluation protocol nào?
- CQ06: Những evidence nào liên quan component này?

### Inspection

- CQ07: Evidence nào kích hoạt Inspection_Record_ID?
- CQ08: Inspection_Record chứa finding và tài liệu nào?
- CQ09: Từ Inspection_Record có truy đúng source run/file không?

### Action

- CQ10: Action_Status hiện tại là gì?
- CQ11: Ai thay đổi status, khi nào, dựa trên evidence nào?

### Integrity

- CQ12: Có orphan record không?
- CQ13: Có duplicate/conflicting binding không?
- CQ14: Có verified record thiếu evidence/reviewer không?

### Versioning

- CQ15: BIM_GUID thuộc model version nào?
- CQ16: Binding thay đổi thế nào giữa hai IFC version?

### Bidirectional traceability

- CQ17: Evidence → component → inspection → action có chạy không?
- CQ18: Action → inspection → evidence → run → sensor có chạy không?

### Reproducibility

- CQ19: Có tái lập từ manifest và code version không?
- CQ20: Hai lần chạy cùng fixture có kết quả giống nhau không?

## B4. Phân Required/Supporting

### Đề xuất Required

```text
CQ01–CQ05
CQ07
CQ09–CQ15
CQ17–CQ20
```

### Đề xuất Supporting

```text
CQ06
CQ08
CQ16
```

Danh sách cuối phải được người nghiên cứu và người hướng dẫn phê duyệt trước Gate 3.

## B5. Acceptance criteria

Tạo:

```text
GATE2_CQ_ACCEPTANCE_CRITERIA_v1.0.csv
```

Trường:

```text
CQ_ID
Fixture_ID
Required_Inputs
Query_or_Test
Expected_Output
Required_or_Supporting
Pass_Criterion
Failure_Severity
Evidence_File
Approved_By
Approval_Date
```

## B6. Pre-registration record

```text
GATE2_PRE_REGISTRATION_RECORD.md
```

Phải ghi:

- date;
- RQ2 version;
- use cases;
- CQ version;
- Required/Supporting;
- thresholds;
- amendment rules;
- schema status = concept draft;
- Gate 3 chưa chạy.

## PASS toàn Phase B

- 20/20 CQ có nguồn gốc;
- 20/20 có Required/Supporting;
- 20/20 có expected output;
- thresholds khóa;
- pre-registration trước schema v1 lock;
- chưa xem kết quả Gate 3.

---

# 9. PHASE C — FINALIZE DESIGN

## C1. Sensor/asset target scope

### File

```text
sensor_target_scope.csv
```

### Trường

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

### Core Scope

- cột đặt sensor;
- dầm/giằng liên quan;
- parent connection;
- component cần Inspection_Record;
- component lân cận có lý do quản lý.

### 17 REVIT_ONLY

PASS khi:

```text
0 unresolved REVIT_ONLY trong Core Scope
```

Ngoài Core:

```text
declared limitation
```

### 1.002 phần tử không Tag

Không là blocker nếu:

- không phải inspection unit;
- được quản lý qua parent component;
- ghi rõ Future/Supporting Scope.

## C2. Asset_ID convention

### Output

```text
ASSET_ID_CONVENTION_v1.0.md
ASSET_ID_REVIEW_WORKFLOW_v1.0.md
ASSET_ID_CONTROLLED_VOCABULARY.csv
```

### Không dùng làm Asset_ID

- BIM_GUID;
- Revit ElementId;
- Revit UniqueId;
- IFC row number;
- coordinate;
- auto-generated code chưa review.

### Trạng thái

```text
candidate
pending_human_verification
verified
rejected
superseded
retired
```

### PASS

- uniqueness scope rõ;
- source rõ;
- reviewer rõ;
- lifecycle rule rõ;
- no auto-verified.

## C3. Traceability schema v1

### Entity bắt buộc

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
Validation_Issue
```

### Output

```text
TRACEABILITY_SCHEMA_v1.0.md
TRACEABILITY_ER_MODEL_v1.0.md
TRACEABILITY_DATA_DICTIONARY_v1.0.csv
TRACEABILITY_RELATIONSHIP_MATRIX_v1.0.csv
TRACEABILITY_STATUS_DICTIONARY_v1.0.csv
```

### Quy tắc thiết kế

Mỗi entity/field phải trả lời ít nhất một CQ hoặc integrity rule.

Trường không phục vụ CQ/use case phải:

- loại;
- hoặc đánh dấu Supporting/Future.

## C4. Integrity rules

### Identity

```text
IR-01 Asset_ID unique
IR-02 BIM_GUID unique trong Model_Version_ID
IR-03 Sensor_ID unique
IR-04 Condition_Evidence_ID unique
IR-05 Inspection_Record_ID unique
IR-06 Action_Record_ID unique
```

### Relationships

```text
IR-07 Evidence có Sensor_ID
IR-08 Evidence có Run_ID
IR-09 Sensor mapping có BIM_GUID + Model_Version_ID
IR-10 Inspection có Asset_ID/BIM binding
IR-11 Trigger evidence tồn tại
IR-12 Action tham chiếu Inspection_Record
```

### Status

```text
IR-13 verified có reviewer + evidence
IR-14 rejected không được import
IR-15 superseded không phải current
IR-16 Action_Status change có event
```

### Provenance

```text
IR-17 IFC có SHA-256 + Model_Version_ID
IR-18 Source data có SHA-256
IR-19 Model result có model/config version
IR-20 Audit có input manifest
```

### Bổ sung theo The Council

```text
IR-21 Conflicting Asset–BIM Binding
```

#### IR-21 thất bại khi

- một Asset_ID có nhiều BIM_GUID current trong cùng version ngoài cardinality cho phép;
- một BIM_GUID có nhiều Asset_ID current;
- hai verified bindings mâu thuẫn;
- binding mới không supersede binding cũ đúng quy trình.

#### IR-21 fields

```text
Rule_ID = IR-21
Severity = CRITICAL
Expected_Result = 0 unresolved conflict
Failure_Action = block verification/import
Linked_Fixture = IF-13
```

### Output

```text
TRACEABILITY_INTEGRITY_RULES_v1.0.csv
TRACEABILITY_VALIDATION_SPEC.md
TRACEABILITY_VALIDATION_RULES.sql
```

## C5. Inspection_Record semantics

### Trigger types

```text
routine
condition_evidence
data_quality_issue
manual_observation
follow_up
```

### Finding status

```text
not_inspected
no_visible_issue
observation_recorded
requires_follow_up
confirmed_issue
inconclusive
closed
```

### Rule cốt lõi

```text
Condition_Evidence ≠ Inspection_Finding
```

Evidence không được tự tạo `confirmed_issue`.

## C6. Permitted action transitions

### Output

```text
ACTION_STATUS_PERMITTED_TRANSITIONS_v1.0.csv
```

### Action status

```text
Normal
Watch
Inspect
Priority_Inspection
In_Progress
Completed
Closed
```

### Ma trận sơ bộ

| Finding_Status | Action status được phép | Điều kiện |
|---|---|---|
| `not_inspected` | Watch / Inspect | Reviewer quyết định |
| `no_visible_issue` | Normal / Watch | Inspection_Record xác nhận |
| `observation_recorded` | Watch / Inspect | Có finding note |
| `requires_follow_up` | Inspect | Phải có kế hoạch kiểm tra |
| `inconclusive` | Watch / Inspect | Dựa trên quality/context |
| `confirmed_issue` | Inspect / Priority_Inspection | Inspection xác nhận + reviewer |
| `closed` | Completed / Closed | Có completion evidence |

### Không được làm

```text
Finding A → auto Action B
```

Thiết kế đúng:

```text
Finding
+ evidence quality
+ component context
+ human review
→ permitted action
```

## PASS toàn Phase C

- scope khóa;
- 0 unresolved Core REVIT_ONLY;
- Asset_ID convention khóa;
- schema trả lời Required CQ;
- IR-01…IR-21 khóa;
- Inspection/Action semantics rõ;
- no auto decision;
- versioning và history rõ.

---

# 10. PHASE D — CONTROLLED IMPLEMENTATION

## D1. Asset_ID pilot

### File

```text
revit_asset_import_verified_pilot.csv
```

### Pilot

3–5 assets:

- một cột;
- một dầm;
- một giằng hoặc parent connection;
- chỉ component trong Core Scope.

### PASS

- 0 duplicate;
- 0 conflict;
- mọi dòng có reviewer/evidence;
- `Verification_Status = verified`;
- `Import_Approved = TRUE`;
- hash khóa.

## D2. Graph 02 dry-run

### Graph

```text
02_import_verified_asset_data.dyn
```

### Thiết lập

```text
DRY_RUN = TRUE
```

### Kiểm tra

- header;
- Revit_UniqueId;
- ElementId;
- parameter;
- writable;
- uniqueness;
- approved status;
- old/new value;
- issue list.

### Output

```text
GRAPH02_PILOT_DRY_RUN_LOG.csv
GRAPH02_PILOT_DRY_RUN_SUMMARY.md
GRAPH02_PILOT_INPUT_MANIFEST.csv
```

### NO-GO khi

- duplicate;
- missing element;
- unapproved row;
- read-only parameter;
- conflict IR-21.

## D3. Pilot write

Chỉ chạy khi:

- dry-run PASS;
- backup RVT;
- reviewer approval;
- rollback plan;
- input hash khóa.

### Output

```text
GRAPH02_PILOT_WRITE_LOG.csv
REVIT_PILOT_POST_IMPORT_CROSSWALK.csv
REVIT_PILOT_CHANGE_AUDIT.csv
```

### PASS

- đúng element;
- đúng số dòng;
- no spread;
- no Type write;
- no unapproved change.

## D4. Official enriched IFC

### File

```text
model_revit2027_asset_enriched_pilot_v1.ifc
```

### Setup

```text
IFC4X3_DT_ASSET_IDENTITY_ACCEPTED_V1
```

### Audit

- hash;
- Model_Version_ID;
- parent;
- GUID uniqueness;
- geometry;
- Pset completeness;
- Asset_ID uniqueness;
- binding;
- IDS;
- no test marker;
- IR-21 conflict check.

### Output

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

### PASS

- all pilot assets đúng;
- 0 duplicate/conflict;
- 0 spread;
- no test values;
- no verified without evidence;
- geometry/identity stable.

---

# 11. PHASE E — GATE 2 CLOSURE

## 11.1. Gate 2 closure package

```text
05_GATE2/08_GATE2_CLOSURE/
├── GATE2_CLOSURE_REVIEW.md
├── GATE2_EVIDENCE_MATRIX.csv
├── GATE2_REQUIREMENT_TRACEABILITY_MATRIX.csv
├── GATE2_CQ_SOURCE_AND_RATIONALE_MATRIX.csv
├── GATE2_CQ_ACCEPTANCE_CRITERIA_v1.0.csv
├── GATE2_PRE_REGISTRATION_RECORD.md
├── GATE2_OPEN_ISSUES.csv
├── GATE2_DECISION_LOG.md
└── GATE2_CLOSURE_MANIFEST.csv
```

## 11.2. Điều kiện bắt buộc đóng G2

| Nhóm | Điều kiện |
|---|---|
| CQ | Có nguồn RQ2/use case; Required/Supporting khóa |
| Pre-registration | Criteria khóa trước G3 |
| Scope | Core component và inspection unit khóa |
| Identity | Asset_ID convention + pilot verified |
| Schema | ER + dictionary review xong |
| Integrity | IR-01…IR-21 khóa |
| Inspection | Record semantics khóa |
| Action | Permitted transitions khóa |
| Revit–IFC | ACCEPTED_V1 + enriched pilot PASS |
| Governance | Hash, manifest, reviewer, decision log |
| Closure | Verdict được phê duyệt |

## 11.3. Supporting evidence không phải blocker

- review ISO/TCVN chi tiết;
- management semantic review;
- toàn bộ 1.703 cấu kiện có Asset_ID;
- plate/bolt identity;
- website/dashboard;
- field deployment.

## 11.4. Verdict

```text
CLOSE
CLOSE_WITH_DECLARED_LIMITATIONS
DO_NOT_CLOSE
```

## 11.5. Claim được phép

> Mô hình dữ liệu, yêu cầu, chuỗi định danh, quy tắc toàn vẹn và tiêu chí đánh giá truy vết đã được khóa trước khi kiểm chứng end-to-end.

Không được nói:

> Framework đã được kiểm chứng đầy đủ.

---

# 12. PHASE F — GATE 3 VALIDATION

## F1. Điều kiện mở Gate 3

- Gate 2 closed;
- schema/CQ/criteria frozen;
- no major redesign;
- real laboratory evidence có provenance hoặc được ghi rõ là controlled fixture;
- BIM pilot binding hoạt động;
- fixture plan approved.

### Quy tắc về Gate 1

Controlled fixture có thể dùng để:

- test schema;
- test query;
- test integrity rule.

Để đóng G3 và dùng cho Paper 2, cần ít nhất một chuỗi condition evidence từ dữ liệu lab thật có:

```text
Run_ID
Sensor_ID
Source_Data_ID
Model_Name
Model_Version
Evaluation_Protocol
Quality_Flag
```

Nếu G1 chưa đủ:

> Evidence is currently insufficient để claim laboratory state validity.

## F2. Valid fixtures

```text
VF-01 Normal chain
VF-02 Watch chain
VF-03 Inspect chain
VF-04 Priority Inspection chain có review
VF-05 Data quality issue
VF-06 BIM version update
```

## F3. Invalid fixtures

```text
IF-01 Duplicate Sensor_ID
IF-02 Duplicate Asset_ID
IF-03 Duplicate BIM_GUID/version
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
IF-14 superseded model used as current
IF-15 broken document/photo link
IF-16 evidence thiếu model/evaluation provenance
```

### Output

```text
GATE3_FIXTURE_REGISTER.csv
GATE3_EXPECTED_RESULTS.csv
GATE3_VALID_FIXTURES/
GATE3_INVALID_FIXTURES/
```

### PASS

- mỗi fixture immutable;
- expected result khóa;
- CQ/IR mapping rõ;
- IF-13 liên kết IR-21.

## F4. Condition evidence import

### File

```text
CONDITION_EVIDENCE_REGISTER.csv
```

### Required fields

```text
Condition_Evidence_ID
Run_ID
Sensor_ID
Source_Data_ID
Model_Name
Model_Version
Evaluation_Protocol
Predicted_State
Confidence_or_CEI
Quality_Flag
Created_At
Evidence_Status
```

### PASS

- 100% có run/sensor/source;
- no orphan;
- model provenance đầy đủ;
- CEI không gọi là physical severity.

## F5. Database/query layer

### Công cụ

```text
SQLite
Python
SQL
IfcOpenShell
```

### Tables

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

### Views

```text
vw_sensor_to_component
vw_evidence_to_component
vw_evidence_to_inspection
vw_inspection_to_action
vw_forward_trace
vw_reverse_trace
vw_orphans
vw_duplicates
vw_conflicting_bindings
vw_provenance_completeness
```

### PASS

- database rebuild từ script;
- deterministic import;
- no hidden manual edit;
- constraints hoạt động.

## F6. Forward trace

```text
Condition_Evidence_ID
→ Sensor_ID
→ BIM_GUID + Model_Version_ID
→ Asset_ID
→ Inspection_Record_ID
→ Action_Record_ID
→ Action_Status
```

### PASS

- 100% Required valid fixture thành công;
- 0 wrong component;
- 0 wrong version;
- 0 hidden manual join.

## F7. Reverse trace

```text
Action_Status
→ Action_Record
→ Inspection_Record
→ Condition_Evidence_ID
→ Run_ID
→ Sensor_ID
→ Source_Data_ID
```

### PASS

- 100% Required valid fixture về đúng source;
- đúng run;
- đúng sensor;
- đúng model/evaluation provenance;
- 0 ambiguity.

## F8. Invalid-data tests

### PASS

- 100% mandatory invalid fixtures detected;
- correct issue code;
- correct severity;
- 0 valid fixture false reject;
- IR-21 phát hiện IF-13.

## F9. CQ evaluation

### File

```text
GATE3_CQ_RESULTS.csv
```

### Trường

```text
CQ_ID
Fixture_ID
Query_Version
Expected_Output
Actual_Output
Pass_Fail
Evidence_File
Issue_Code
Reviewer
Review_Note
```

### Gate-blocking threshold

- 100% Required CQ PASS;
- Supporting CQ báo cáo riêng;
- không đổi threshold sau khi xem kết quả.

## F10. Reproducibility

### Output

```text
GATE3_REPRODUCIBILITY_MANIFEST.csv
environment.yml
requirements.txt
code_commit.txt
query_hashes.csv
fixture_hashes.csv
```

### PASS

- database rebuild;
- two-run identical outputs;
- fixture hashes stable;
- query version locked;
- code commit recorded.

## F11. Management semantic review — Supporting Evidence

### Người review

- 1 facility/asset manager;
- 1 inspection/maintenance engineer;
- 1 BIM/information manager nếu có.

### Chỉ đánh giá

- Inspection_Record có dễ hiểu không;
- Action_Status có rõ trách nhiệm không;
- query có hữu ích không;
- field nào thiếu;
- workflow có phản ánh thực tế không.

### Không đánh giá

- damage diagnosis accuracy;
- technical threshold;
- optimal maintenance action.

### Output

```text
MANAGEMENT_SEMANTIC_REVIEW_FORM.csv
MANAGEMENT_SEMANTIC_REVIEW_SUMMARY.md
```

### Vai trò

Supporting Evidence cho management relevance; không thay Gate 5 decision validity.

---

# 13. GATE 3 CLOSURE

## 13.1. Closure package

```text
06_GATE3/08_GATE3_CLOSURE/
├── GATE3_CLOSURE_REVIEW.md
├── GATE3_EVIDENCE_MATRIX.csv
├── GATE3_CQ_RESULTS.csv
├── FORWARD_TRACE_RESULTS.csv
├── REVERSE_TRACE_RESULTS.csv
├── INVALID_DATA_TEST_RESULTS.csv
├── GATE3_REQUIREMENT_TRACEABILITY_MATRIX.csv
├── GATE3_OPEN_ISSUES.csv
├── GATE3_REPRODUCIBILITY_MANIFEST.csv
└── GATE3_DECISION_LOG.md
```

## 13.2. Điều kiện bắt buộc

| Nhóm | Điều kiện |
|---|---|
| Fixtures | Valid/invalid immutable |
| Evidence | Run/Sensor/Model provenance |
| Forward | 100% Required PASS |
| Reverse | 100% Required PASS |
| Integrity | 100% mandatory invalid detected |
| False rejection | 0 valid fixture rejected |
| CQ | 100% Required PASS |
| Versioning | 0 unresolved ambiguity |
| Reproducibility | rebuild + commit + hash |
| Scope | laboratory traceability only |
| Closure | verdict approved |

## 13.3. Verdict

```text
CLOSE
CLOSE_WITH_DECLARED_LIMITATIONS
DO_NOT_CLOSE
```

## 13.4. Claim được phép

> Chuỗi truy vết component-level đã chạy hai chiều trong case phòng thí nghiệm, trả lời đúng các competency questions được công bố trước và phát hiện được các lỗi định danh, quan hệ và provenance đã thiết kế.

## 13.5. Claim cấm

- field damage diagnosis;
- predictive maintenance;
- damage severity;
- calibrated FEM;
- general AI superiority;
- autonomous maintenance.

---

# 14. PAPER 2 — RESEARCH DESIGN

## 14.1. Working title

**A Verifiable Component-Level Traceability Framework Linking Vibration-Based Condition Evidence to BIM Objects and Inspection Records for Industrial Steel Buildings**

## 14.2. Central research claim

> A pre-registered, version-aware traceability framework can link vibration-based condition evidence to BIM components, inspection records and action-status histories, and its information integrity can be verified through bidirectional queries and adversarial invalid-data fixtures.

## 14.3. Research design

```text
Design specification
→ pre-registration
→ controlled Revit–IFC implementation
→ laboratory valid/invalid fixtures
→ bidirectional query validation
→ management semantic review
```

## 14.4. Unit of analysis

Không phải toàn bộ công trình.

Unit of analysis chính:

```text
one traceability chain
Condition_Evidence_ID
↔ BIM-linked component
↔ Inspection_Record_ID
↔ Action_Record
```

Unit hỗ trợ:

- identifier;
- binding;
- query result;
- invalid fixture;
- model version.

## 14.5. Baselines cần có

### Baseline B1 — No formal identity governance

Chứng minh lỗi khi chỉ dùng GUID/ElementId.

### Baseline B2 — One-way linkage

So sánh với forward-only demo, không reverse/provenance.

### Baseline B3 — No invalid-data testing

Làm rõ vì sao demo dữ liệu đẹp không đủ.

Không cần xây ba hệ thống đầy đủ. Có thể trình bày bằng controlled fixtures và failure demonstration.

---

# 15. PAPER 2 — OUTLINE

## 1. Introduction

- vấn đề evidence-to-action;
- hạn chế sensor-to-BIM demo;
- RQ2;
- objectives;
- contributions.

## 2. Literature and research gap

Bốn cụm:

1. condition-monitoring evidence;
2. BIM/AIM identity and information management;
3. component-level traceability;
4. inspection-record/action linkage.

Gap:

> Thiếu một framework được kiểm chứng hình thức, có phiên bản và truy vấn hai chiều từ condition evidence đến BIM component, inspection record và action status.

## 3. Research design and scope

- Gate 2/Gate 3;
- pre-registration;
- validation ladder;
- Limited-FEM firewall;
- claim boundaries.

## 4. Information-management requirements

- management use cases;
- CQ derivation;
- Required/Supporting classification;
- acceptance criteria;
- ISO 19650/TCVN 14177 positioning.

## 5. BIM information readiness and Revit–IFC exchange

- baseline model;
- model version;
- identity gap;
- geometry;
- IDS;
- Revit crosswalk;
- round-trip audit;
- Pset validation;
- 41/41 PASS.

## 6. Identifier governance and target scope

- Asset_ID;
- BIM_GUID;
- Model_Version_ID;
- Revit keys;
- inspection unit;
- 17 REVIT_ONLY;
- plate/fastener boundary.

## 7. Traceability data model

- entities;
- ER model;
- cardinality;
- integrity rules;
- IR-21;
- provenance.

## 8. Inspection and action semantics

- evidence vs finding;
- Inspection_Record;
- Action_Record;
- permitted transitions;
- human review.

## 9. Laboratory implementation

- condition evidence records;
- valid fixtures;
- invalid fixtures;
- database/query layer.

## 10. Validation methods

- forward trace;
- reverse trace;
- CQ evaluation;
- invalid-data detection;
- reproducibility.

## 11. Results

- Revit–IFC readiness;
- Required CQ pass;
- forward/reverse success;
- duplicate/orphan/conflict detection;
- false reject;
- provenance completeness;
- management semantic review.

## 12. Discussion

- novelty;
- management relevance;
- generalizability;
- why not software demo;
- AIM implications;
- limitations.

## 13. Conclusion

- answer RQ2;
- Gate 3 conclusion;
- transition to field feasibility.

---

# 16. PAPER 2 — BẢNG VÀ HÌNH

## Tables

1. RQ2 use cases and competency questions.
2. Required/Supporting CQ classification.
3. Identifier dictionary.
4. Revit–IFC readiness results.
5. Pset validation results.
6. Traceability entities and relationships.
7. Integrity rules including IR-21.
8. Inspection finding and permitted action transitions.
9. Valid and invalid fixtures.
10. Forward/reverse results.
11. Invalid-data detection matrix.
12. Management semantic review.
13. Scope and limitations.

## Figures

1. Evidence-to-action architecture.
2. Gate 2–Gate 3 research design.
3. CQ derivation before schema lock.
4. Revit–IFC–AIM information flow.
5. Identifier architecture.
6. ER diagram.
7. Forward trace.
8. Reverse trace.
9. Invalid-data architecture.
10. BIM-linked Inspection_Record example.
11. Versioned binding history.
12. Paper 2 contribution boundary.

---

# 17. PAPER 2 — METRICS

## Core metrics

```text
Required_CQ_Pass_Rate
Forward_Trace_Success_Rate
Reverse_Trace_Success_Rate
Mandatory_Invalid_Fixture_Detection_Rate
Valid_Fixture_False_Rejection_Rate
Provenance_Completeness_Rate
Query_Reproducibility_Rate
Unresolved_Conflict_Count
Unexpected_Orphan_Count
```

## Supporting metrics

```text
Supporting_CQ_Pass_Rate
Management_Clarity_Rating
Management_Usefulness_Rating
Missing_Field_Count
```

## Không dùng

- Health Index;
- damage severity score;
- predictive accuracy cho field;
- RUL;
- maintenance optimization score.

---

# 18. PAPER 2 — CLAIM BOUNDARY

## Allowed

- formal traceability model;
- version-aware identity;
- bidirectional queries;
- invalid-data detection;
- reproducible Revit–IFC exchange;
- laboratory traceability validity;
- inspection-oriented information support.

## Không được viết

- system diagnoses field damage;
- framework predicts maintenance;
- BIM proves structural damage;
- FEM validates classifier;
- evidence equals confirmed defect;
- framework automatically chooses maintenance;
- ISO 19650 certified/compliant in full.

## Cách viết ISO/TCVN

> The workflow was structured to support information-requirement definition, container versioning, controlled exchange, verification and traceability in alignment with the principles of ISO 19650 and TCVN 14177.

---

# 19. PUBLICATION READINESS

Paper 2 chỉ sẵn sàng nộp khi:

- Gate 2 closed;
- Gate 3 closed;
- Required CQ = 100% PASS;
- forward/reverse = 100% Required fixture;
- mandatory invalid detection = 100%;
- false rejection = 0;
- Paper 2 evidence package immutable;
- limitation/claim audit hoàn tất;
- internal review xong.

## Paper 2 evidence package

```text
10_PAPERS/PAPER2/
├── 00_CONCEPT/
├── 01_PRE_REGISTRATION/
├── 02_G2_EVIDENCE/
├── 03_G3_EVIDENCE/
├── 04_TABLES/
├── 05_FIGURES/
├── 06_RESULTS/
├── 07_MANAGEMENT_REVIEW/
├── 08_LIMITATIONS/
├── 09_REPRODUCIBILITY/
└── 10_SUBMISSION/
```

---

# 20. KẾ HOẠCH THỰC THI 14 TUẦN

> Evidence Gate quan trọng hơn lịch.

| Tuần | Công việc | Output chính |
|---|---|---|
| 1 | Freeze Pset, clean working model | Acceptance record, clean audit |
| 2 | Management use cases + CQ source matrix | Use cases, CQ rationale |
| 3 | Required/Supporting + acceptance criteria | Pre-registration |
| 4 | Sensor target scope | `sensor_target_scope.csv` |
| 5 | Asset_ID convention | Convention + workflow |
| 6 | Schema v1 + ER | Schema/dictionary |
| 7 | IR-01…21 + Inspection/Action | Rules and transitions |
| 8 | Asset_ID pilot + Graph 02 dry-run | Pilot input/dry-run |
| 9 | Pilot write + enriched IFC audit | Official pilot IFC |
| 10 | Gate 2 closure | G2 package |
| 11 | Fixtures + condition evidence + database | Gate 3 inputs |
| 12 | Forward/reverse tests | Trace results |
| 13 | Invalid tests + CQ evaluation | Validation results |
| 14 | Reproducibility + management review + G3 closure | G3 package |
| 15–16 | Paper 2 draft | Manuscript package |

---

# 21. GO / NO-GO

| Hành động | Quyết định hiện tại | Điều kiện |
|---|---|---|
| Freeze Pset ACCEPTED_V1 | GO | Acceptance record + hash |
| Tạo CQ source matrix | GO | Dựa RQ2/use cases |
| Tạo `sensor_target_scope.csv` | GO | Không chọn toàn model |
| Chuẩn bị Asset_ID pilot | CONDITIONAL GO | Scope + convention khóa |
| Graph 02 dry-run | NO-GO hiện tại | Pilot approved |
| Graph 02 write | NO-GO | Dry-run PASS |
| Close Gate 2 | NO-GO | Hoàn tất Phase B–D |
| Open Gate 3 | NO-GO | Gate 2 closed |
| Submit Paper 2 | NO-GO | Gate 3 closed |

---

# 22. RISK REGISTER HIỆU CHỈNH

| Rủi ro | Kiểm soát |
|---|---|
| CQ may đo theo schema | CQ source matrix + pre-registration trước schema lock |
| Missing conflicting-binding rule | IR-21 + IF-13 |
| Action bị tự động hóa | Permitted transitions + human review |
| Software-demo perception | Formal CQ, baselines, invalid tests, management semantics |
| Management relevance yếu | 2–3 expert semantic review |
| GUID/Asset_ID confusion | Versioned identity governance |
| Pset mất khi export | ACCEPTED_V1 |
| Test data lẫn production | Clean working model audit |
| REVIT_ONLY kéo dài | Scope-based blocker |
| Plate/bolt scope creep | Parent inspection unit |
| Gate 1 chưa đủ | Tách state validity khỏi traceability validity |
| ISO overclaim | aligned, not certified |
| FEM quay lại | Limited-FEM firewall |

---

# 23. EVIDENCE MATRIX

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

# 24. CLAIM → EVIDENCE → LIMITATION → NEXT ACTION

## Claim

Revit–IFC exchange cho lớp thông tin định danh đã đủ điều kiện khóa kỹ thuật; hướng Paper 2 có khả năng tạo đóng góp học thuật nếu chuyển trọng tâm sang pre-registered evidence-to-inspection traceability.

## Evidence

- 41/41 Pset tests PASS;
- 14/14 values;
- identity/geometry stable;
- Charter khóa G2/G3 theo traceability validity;
- The Council xác nhận kiến trúc tổng thể chặt nhưng yêu cầu major revision về phương pháp.

## Limitation

- CQ chưa pre-register;
- scope chưa khóa;
- Asset_ID thật chưa duyệt;
- IR-21 chưa tạo;
- permitted transitions chưa khóa;
- G2/G3 chưa đóng;
- Evidence is currently insufficient để claim framework đã được kiểm chứng.

## Next action duy nhất

```text
Freeze Pset ACCEPTED_V1
→ lập GATE2_CQ_SOURCE_AND_RATIONALE_MATRIX.csv
→ phân Required/Supporting
→ khóa acceptance criteria
```

Chỉ sau đó mới khóa schema v1 và chuẩn bị Asset_ID pilot.

---

# 25. ROADMAP LOCK

Bản v1.1 này khóa:

```text
CQ before schema v1 lock
Required/Supporting classification
IR-21 conflicting binding
Human-controlled permitted transitions
Scope-based REVIT_ONLY handling
Management semantic review as Supporting Evidence
Paper 2 novelty = vibration evidence-to-inspection traceability
Gate 2 before Gate 3
Forward + reverse + invalid-data validation
```

Mọi thay đổi tiếp theo phải ghi:

```text
Version
Date
Change
Reason
Affected_CQ
Affected_Rule
Affected_Gate
Approved_By
```

Không sửa pre-registration hoặc fixture sau khi đã xem kết quả nếu không có amendment record.

---

# 26. SOURCE BASIS

Nguồn điều hành:

1. `MASTER_RESEARCH_CHARTER_v1.1_LIMITED_FEM_20260717.md`
2. `RESEARCH_ARCHITECTURE_DECISION_RECORD_20260717.md`
3. `G2_G3_REVIT_IFC_AIM_EXECUTION_ROADMAP.md`
4. `PSET_7_PARAMETER_QUICK_REVIEW.md`
5. `Revit-IFCGuide.md`
6. Góp ý The Council về G2–G3 và Paper 2 ngày 03/08/2026

Khi có mâu thuẫn:

```text
Charter v1.1
→ ADR Limited-FEM
→ pre-registration được phê duyệt
→ Gate evidence
→ roadmap
```
