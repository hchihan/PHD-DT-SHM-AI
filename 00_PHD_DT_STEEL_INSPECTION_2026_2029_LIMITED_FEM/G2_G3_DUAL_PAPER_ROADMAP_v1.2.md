# ROADMAP G2–G3 VÀ KIẾN TRÚC HAI BÀI BÁO — v1.2
## Gate 2: AIM Information Readiness & Versioned Identity Governance  
## Gate 3: Pre-registered Bidirectional Evidence-to-Inspection Traceability

**Tên tệp:** `G2_G3_DUAL_PAPER_ROADMAP_v1.2.md`  
**Phiên bản:** v1.2 — phát triển từ v1.1 và góp ý The Council  
**Ngày:** 03/08/2026  
**Luận án:** Data-informed Digital Twin phục vụ giám sát trạng thái và hỗ trợ kiểm tra – bảo trì nhà công nghiệp khung thép ven biển  
**Lĩnh vực:** Quản lý xây dựng / Quản lý tài sản  
**RQ/WP:** RQ2 / WP2  
**Chương luận án:** Chương 5  
**Gate:** G2 – Traceability Design Readiness; G3 – End-to-End Laboratory Traceability  
**Kiến trúc:** Limited-FEM  
**Mốc hiện tại:** `READY TO FREEZE PSET EXPORT SETUP`  
**Trạng thái:** G2 đang mở; G3 chưa mở  

---

# 0. QUYẾT ĐỊNH CHIẾN LƯỢC CỦA v1.2

## 0.1. Phán quyết

Mỗi Gate được phát triển thành một gói bằng chứng đủ độc lập để hướng tới một bài báo Q2/Q3:

```text
Gate 2
→ Supporting Paper G2
→ BIM/AIM information readiness và versioned identity governance

Gate 3
→ Core Paper 2 / Paper G3
→ Pre-registered bidirectional evidence-to-inspection traceability
```

## 0.2. Cấu trúc công bố được khuyến nghị

| Gate | Tên quản trị bài | Vai trò trong luận án | Mức mục tiêu thực tế |
|---|---|---|---|
| G2 | **Supporting Paper G2** hoặc **Paper 2A** | Bài hỗ trợ RQ2; cung cấp hạ tầng phương pháp và bằng chứng trao đổi thông tin | Q3 mục tiêu chính; Q2 chỉ khi tăng độ khái quát và so sánh |
| G3 | **Core Paper 2** hoặc **Paper 2B** | Bài cốt lõi trả lời RQ2 | Q2 mục tiêu; Q3 dự phòng |

## 0.3. Lý do không gọi cả hai là “Paper 2” chính thức

Charter hiện tại gắn RQ2/WP2/Chương 5 với Paper 2 và G2–G3. Để không âm thầm thay đổi kiến trúc đã khóa:

- Paper G3 giữ vai trò **Paper 2 cốt lõi**;
- Paper G2 là **supporting paper** của RQ2;
- có thể dùng ký hiệu nội bộ `Paper 2A` và `Paper 2B`;
- nếu muốn công nhận cả hai là paper cốt lõi, phải có quyết định cập nhật Charter/ADR riêng.

## 0.4. Cảnh báo về quartile

Không được mặc định một bài sẽ đạt Q2 chỉ vì có nhiều kiểm tra kỹ thuật.

Với evidence hiện tại:

```text
Paper G2:
Q3 khả thi hơn.
Evidence is currently insufficient để bảo đảm Q2.

Paper G3:
có tiềm năng Q2 nếu hoàn tất:
pre-registration
+ real laboratory evidence
+ forward/reverse validation
+ invalid-data testing
+ reproducibility
+ management relevance.
```

Quartile phải được kiểm tra lại tại thời điểm chọn tạp chí và nộp bài.

---

# 1. ĐỊNH VỊ RQ2/WP2

## 1.1. RQ2 của luận án

> Bằng chứng trạng thái từ dữ liệu cảm biến được tổ chức và liên kết với cấu kiện BIM và hồ sơ kiểm tra như thế nào để bảo đảm khả năng truy vết ở cấp cấu kiện?

## 1.2. WP2

```text
BIM–Sensor–Inspection traceability
```

## 1.3. Chuỗi nghiên cứu khóa

```text
Vibration data
→ condition/state-change evidence
→ BIM-linked component
→ inspection record
→ inspection-maintenance action support
```

## 1.4. Chuỗi định danh khóa

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

## 1.5. FEM firewall

FEM chỉ là:

> nominal, uncalibrated, reference-only, not used for damage diagnosis.

Không có:

- FEM RQ;
- FEM Gate;
- FEM Paper trong WP2;
- calibrated FEM;
- stiffness-degradation inference;
- lab-to-field classifier transfer.

---

# 2. KIẾN TRÚC HAI BÀI BÁO

## 2.1. Paper G2 — Supporting Paper

### Working title

**A Version-Aware BIM–IFC Information Readiness and Asset-Identity Governance Workflow for Inspection-Oriented Asset Information Models**

### Paper-specific research question

> How can persistent asset identity, model-version provenance and controlled Revit–IFC information exchange be operationalized and verified to prepare an inspection-oriented AIM for component-level traceability?

### Mục tiêu

Xây dựng và kiểm chứng quy trình:

```text
Revit authoring information
→ controlled IFC exchange
→ versioned BIM binding
→ verified Asset_ID pilot
→ AIM information readiness
```

### Trả lời phần nào của RQ2?

Paper G2 không trả lời toàn bộ RQ2.

Nó trả lời điều kiện nền:

> Cấu kiện và thông tin định danh phải được chuẩn bị, trao đổi và quản trị phiên bản như thế nào trước khi condition evidence có thể liên kết đáng tin cậy với BIM object và Inspection_Record?

### Loại bằng chứng

```text
BIM/AIM information readiness
+ controlled information exchange
+ identity governance
```

### Gate

```text
Gate 2
```

---

## 2.2. Paper G3 — Core Paper 2

### Working title

**A Pre-registered Bidirectional Traceability Framework Linking Vibration-Based Condition Evidence to BIM Components and Inspection Records**

### Paper-specific research question

> To what extent can a pre-registered, version-aware traceability framework reliably link vibration-based condition evidence to BIM components, inspection records and action-status histories while detecting identifier, relationship and provenance failures?

### Mục tiêu

Kiểm chứng:

```text
Condition_Evidence_ID
↔ BIM-linked component
↔ Inspection_Record_ID
↔ Action_Record
```

theo hai chiều, trên valid và invalid fixtures.

### Trả lời RQ2

Paper G3 trực tiếp trả lời RQ2 và là Paper 2 cốt lõi.

### Loại bằng chứng

```text
Traceability validity
```

### Gate

```text
Gate 3
```

---

# 3. MA TRẬN KHÔNG TRÙNG LẶP GIỮA HAI BÀI

| Thành phần | Paper G2 | Paper G3 |
|---|---|---|
| Câu hỏi chính | AIM có đủ định danh, version và exchange readiness chưa? | Chuỗi evidence–component–inspection có chạy và phát hiện lỗi không? |
| Gate | G2 | G3 |
| Unit of analysis | IFC container, BIM object, Asset_ID–BIM binding | Một traceability chain |
| Input chính | Revit, IFC, crosswalk, Pset, Asset_ID pilot | Condition evidence, sensor, BIM binding, inspection/action records |
| Kết quả chính | Information readiness và exchange acceptance | Forward/reverse traceability validity |
| Baseline | Không quản trị identity/version; Pset không kiểm soát | One-way demo; no invalid-data test |
| Metrics | completeness, uniqueness, persistence, exchange correctness | CQ pass, forward/reverse success, invalid detection |
| Management link | Inspection-oriented AIM readiness | Inspection_Record và Action_Status semantics |
| Condition evidence | Chỉ là use-case requirement, không dùng làm result chính | Là input chính |
| Invalid-data fixtures | Chỉ identity/exchange cases giới hạn | Bộ valid/invalid fixtures đầy đủ |
| Revit/Dynamo | Công cụ nghiên cứu trọng yếu | Chỉ cung cấp accepted BIM binding |
| Novelty | Version-aware identity governance và controlled exchange | Pre-registered evidence-to-inspection traceability |
| Kết luận | Sẵn sàng cho traceability implementation | Traceability framework đã được kiểm chứng trong lab scope |

## Quy tắc chống “salami slicing”

Paper G2 không được:

- báo cáo forward/reverse trace results;
- dùng Condition_Evidence_ID như kết quả chính;
- tuyên bố traceability framework validated;
- trình bày toàn bộ Inspection_Action chain.

Paper G3 không được:

- lặp lại chi tiết từng thao tác Revit/Dynamo;
- tái báo cáo đầy đủ 41/41 Pset test;
- coi Revit–IFC exchange là novelty;
- lặp lại toàn bộ Phase 1 tables.

Paper G3 chỉ tóm tắt Paper G2 như một prerequisite:

> The accepted version-aware BIM/IFC identity layer was used as the component-binding substrate for Gate 3 validation.

---

# 4. HIỆN TRẠNG BẰNG CHỨNG

## 4.1. Phase 1

Đã có:

- Model Version Registry;
- Component Registry;
- BIM Binding Registry;
- Geometry readiness;
- Coordinate_Quality;
- IDS baseline;
- link audit;
- no auto-verified mapping.

## 4.2. Revit–IFC evidence

Môi trường:

```text
Revit 2027.1
Dynamo 4.0
PythonNet3
IFC4X3_ADD2
IfcOpenShell
```

Kết quả:

| Chỉ số | Giá trị |
|---|---:|
| Structural crosswalk | 718 |
| Sync IFC IfcElement | 3.468 |
| Structural elements | 1.703 |
| GUID unique | 3.468/3.468 |
| Geometry usable | 1.703/1.703 |
| `MATCH_TAG_AND_GUID` | 685/718 |
| IFC counterpart duy nhất | 701/718 |
| `REVIT_ONLY` | 17 |
| Plate/fastener không Tag | 1.002 |

## 4.3. Pset acceptance evidence

```text
Pset_DT_AssetIdentity
```

Gồm:

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
0 spread
0 verified
0 identity change
0 geometry change
```

## 4.4. Phán quyết hiện tại

```text
READY TO FREEZE PSET EXPORT SETUP
```

Chưa đạt:

- Pset Acceptance Record chính thức;
- target scope;
- real Asset_ID pilot;
- schema v1;
- CQ pre-registration;
- Gate 2 closure;
- Gate 3 fixtures;
- traceability validation.

---

# 5. PAPER G2 — CLAIM, NOVELTY VÀ BASELINES

## 5.1. Central claim

> A version-aware, inspection-oriented BIM–IFC information-readiness workflow can establish controlled asset identity and reproducible component bindings without conflating authoring-system identifiers, IFC object identifiers and persistent Asset_IDs.

## 5.2. Đóng góp G2

### G2-C1 — Identity separation

Phân biệt và quản trị:

```text
Asset_ID
BIM_GUID
Model_Version_ID
Revit_UniqueId
Revit_ElementId
```

### G2-C2 — Controlled Revit–IFC exchange

Chứng minh Shared Parameters đi qua accepted Pset đến đúng IFC object mà không làm thay đổi identity/geometry.

### G2-C3 — Version-aware binding

Không sử dụng một BIM_GUID ngoài ngữ cảnh `Model_Version_ID`.

### G2-C4 — Scope-based AIM readiness

Không cấp Asset_ID cho mọi object; chỉ cấp cho inspection-oriented Core Scope.

### G2-C5 — Machine-checkable acceptance

Kết hợp:

- IDS/entity checks;
- custom uniqueness rules;
- binding audit;
- hash/manifest;
- human verification.

## 5.3. Baseline comparisons

### B-G2-1 — IFC without accepted Pset setup

Hiển thị việc property có trong Revit nhưng mất trong IFC.

### B-G2-2 — GUID-only identity

Chứng minh GUID/ElementId không thay thế Asset_ID.

### B-G2-3 — Unversioned binding

Chứng minh BIM_GUID không có Model_Version_ID tạo ambiguity.

### B-G2-4 — Broad category filtering

Đối chiếu bộ lọc 2.160 dòng không liên quan với structural whitelist 718 dòng.

## 5.4. Baseline không cần xây hệ thống mới

Các baseline có thể sử dụng:

- các output đã có;
- controlled failure cases;
- before/after audit;
- không cần xây bốn platform riêng.

---

# 6. PAPER G2 — EVIDENCE CẦN BỔ SUNG

## 6.1. Bắt buộc để đủ một bài độc lập

1. `PSET_EXPORT_ACCEPTANCE_RECORD.md`.
2. Working model sạch.
3. `sensor_target_scope.csv`.
4. Asset_ID convention.
5. Asset_ID pilot 3–5 cấu kiện.
6. Graph 02 dry-run.
7. Pilot write.
8. Official enriched IFC.
9. Round-trip pilot audit.
10. Identity/version integrity rules.
11. Management semantic review nhẹ.
12. Reproducibility manifest.

## 6.2. Để tăng khả năng Q2

Ít nhất một trong các tăng cường sau:

### Option A — Multi-version robustness

Kiểm chứng qua tối thiểu bốn trạng thái container:

```text
baseline IFC
→ sync IFC
→ Pset test IFC
→ official enriched IFC
```

Đo:

- identity persistence;
- binding changes;
- property persistence;
- model-version disambiguation.

### Option B — Broader representative classes

Ngoài IfcColumn và IfcBeam, thêm một class thuộc Core Scope:

- brace/structural member;
- parent connection;
- foundation nếu phục vụ inspection.

Không bắt buộc plate/bolt.

### Option C — Second case/model

Một model thứ hai hoặc subset độc lập.

Đây là tăng cường mạnh nhất cho generalizability nhưng không bắt buộc để đóng G2.

### Option D — Comparative workflow baseline

So sánh có hệ thống:

```text
uncontrolled IFC export
vs
accepted version-aware workflow
```

## 6.3. Phán quyết thực tế

- Không có tăng cường A/B/C/D: Q3 khả thi hơn.
- Có A + B + semantic review: Q2 có thể cân nhắc.
- Có C hoặc một validation case độc lập: hồ sơ Q2 mạnh hơn rõ rệt.

---

# 7. PAPER G2 — METHODS

## 7.1. Research design

```text
Design requirements
→ baseline audit
→ authoring schema
→ controlled exchange
→ pilot enrichment
→ version/binding audit
→ information-readiness assessment
```

## 7.2. Unit of analysis

- IFC container;
- scoped BIM object;
- Asset_ID–BIM_GUID binding;
- one exchange transaction;
- one version transition.

## 7.3. Data sources

- Revit model;
- baseline IFC;
- sync IFC;
- crosswalk;
- Pset test v1/v2;
- official enriched IFC;
- audit CSV;
- manifests.

## 7.4. Validation layers

### Container level

- SHA-256;
- schema;
- exporter;
- element count;
- GUID uniqueness;
- geometry readiness.

### Object level

- IFC class;
- Tag;
- GlobalId;
- Pset;
- property;
- datatype;
- encoding.

### Set level

- Asset_ID uniqueness;
- binding cardinality;
- orphan;
- conflict;
- scope completeness.

### Process level

- reviewer;
- evidence;
- accepted/rejected;
- superseded;
- manifest;
- change log.

---

# 8. PAPER G2 — METRICS

## Core metrics

```text
Scoped_Asset_ID_Completeness
Asset_ID_Uniqueness_Rate
BIM_Binding_Completeness
Binding_Conflict_Count
IFC_Property_Transfer_Accuracy
GUID_Uniqueness_Rate
Geometry_Persistence_Rate
Model_Version_Provenance_Completeness
Round_Trip_Match_Rate
Unexpected_Data_Spread_Count
```

## Supporting metrics

```text
REVIT_ONLY_Core_Count
IFC_ONLY_Core_Count
Pset_Completeness
Encoding_Accuracy
Audit_Reproducibility
Management_Semantic_Clarity
```

## Không dùng

- damage metrics;
- model classification accuracy;
- Health Index;
- field prediction;
- maintenance optimization.

---

# 9. PAPER G2 — GATE 2 ROADMAP

## G2-A — Freeze technical setup

### Output

```text
IFC4X3_DT_ASSET_IDENTITY_ACCEPTED_V1
DT_UserDefinedPropertySets_ACCEPTED_V1.txt
PSET_EXPORT_ACCEPTANCE_RECORD.md
```

### PASS

- 7/7 mapping;
- IFCTEXT;
- 41/41 audit referenced;
- hash;
- immutable setup.

## G2-B — Clean working model

### Output

```text
WORKING_MODEL_CLEANLINESS_AUDIT.csv
WORKING_MODEL_BASELINE_MANIFEST.csv
```

### PASS

- 0 test markers;
- 0 unjustified verified values.

## G2-C — Derive management use cases and CQ

Bước này phải xảy ra trước schema v1 lock.

### Output

```text
GATE2_MANAGEMENT_USE_CASES_v1.0.md
GATE2_CQ_SOURCE_AND_RATIONALE_MATRIX.csv
GATE2_CQ_ACCEPTANCE_CRITERIA_v1.0.csv
GATE2_PRE_REGISTRATION_RECORD.md
```

## G2-D — Target scope

### Output

```text
sensor_target_scope.csv
```

### PASS

```text
0 unresolved REVIT_ONLY in Core Scope
```

Plate/fastener ngoài inspection unit không chặn.

## G2-E — Asset_ID governance

### Output

```text
ASSET_ID_CONVENTION_v1.0.md
ASSET_ID_REVIEW_WORKFLOW_v1.0.md
```

## G2-F — Schema and integrity

### Output

```text
TRACEABILITY_SCHEMA_v1.0.md
TRACEABILITY_ER_MODEL_v1.0.md
TRACEABILITY_DATA_DICTIONARY_v1.0.csv
TRACEABILITY_INTEGRITY_RULES_v1.0.csv
```

Bắt buộc có:

```text
IR-21 — Conflicting Asset–BIM Binding
```

## G2-G — Inspection/action semantics

### Output

```text
INSPECTION_RECORD_SCHEMA_v1.0.md
ACTION_STATUS_PERMITTED_TRANSITIONS_v1.0.csv
```

Không auto-map Finding → Action.

## G2-H — Asset_ID pilot

### Output

```text
revit_asset_import_verified_pilot.csv
```

### PASS

- 3–5 verified assets;
- 0 duplicate/conflict;
- reviewer/evidence;
- approved.

## G2-I — Graph 02 dry-run and write

### Output

```text
GRAPH02_PILOT_DRY_RUN_LOG.csv
GRAPH02_PILOT_WRITE_LOG.csv
REVIT_PILOT_CHANGE_AUDIT.csv
```

## G2-J — Official enriched IFC

### Output

```text
model_revit2027_asset_enriched_pilot_v1.ifc
IFC_ENRICHMENT_ACCEPTANCE_RECORD.md
```

## G2-K — Management semantic review

2–3 người:

- asset/facility manager;
- inspection/maintenance engineer;
- BIM/information manager.

Chỉ đánh giá:

- identity fields;
- inspection unit;
- record clarity;
- workflow usefulness.

## G2-L — Gate 2 closure

### Verdict

```text
CLOSE
CLOSE_WITH_DECLARED_LIMITATIONS
DO_NOT_CLOSE
```

---

# 10. ĐIỀU KIỆN G2 PAPER-READY

Paper G2 chỉ bắt đầu viết Results cuối cùng khi:

- Pset ACCEPTED_V1;
- clean working model;
- target scope locked;
- Asset_ID pilot verified;
- enriched IFC audit PASS;
- IR-21 implemented;
- multi-version analysis completed;
- management semantic review completed;
- Gate 2 closure package approved.

## Minimum submission readiness

| Hạng mục | Yêu cầu |
|---|---|
| Identity | 0 unresolved conflict trong pilot |
| Exchange | 100% scoped pilot properties đúng |
| Versioning | 100% container có Model_Version_ID + hash |
| Geometry | Không suy giảm ngoài dự kiến |
| Scope | 0 unresolved `REVIT_ONLY` trong Core |
| Reproducibility | Rebuild/audit được từ manifest |
| Management | Semantic review được báo cáo |
| Claim boundary | Không tuyên bố full AIM hoặc traceability validity |

---

# 11. PAPER G2 — OUTLINE

## 1. Introduction

- AIM identity problem;
- Revit/IFC identifier confusion;
- inspection-oriented information requirements;
- research question;
- contributions.

## 2. Background

- AIM information readiness;
- persistent identity;
- model versioning;
- IFC exchange;
- ISO 19650/TCVN 14177 positioning.

## 3. Research design

- case;
- baseline;
- validation layers;
- scope;
- claim boundaries.

## 4. Baseline information-readiness audit

- Asset_ID gap;
- geometry;
- IDS;
- model version;
- broad filtering problem.

## 5. Version-aware identity workflow

- Asset_ID;
- BIM_GUID;
- Model_Version_ID;
- binding registry;
- target scope.

## 6. Controlled Revit–IFC exchange

- Shared Parameters;
- crosswalk;
- accepted Pset;
- Graph 02 pilot.

## 7. Validation

- object-level;
- set-level;
- version-level;
- process-level;
- semantic review.

## 8. Results

- transfer accuracy;
- persistence;
- uniqueness;
- conflict;
- multi-version change;
- management review.

## 9. Discussion

- novelty;
- generalizability;
- cost/limitations;
- why not full AIM;
- implication for inspection workflows.

## 10. Conclusion

- Gate 2 result;
- transition to evidence traceability.

---

# 12. PAPER G2 — TABLES VÀ FIGURES

## Tables

1. Identifier semantics.
2. Model versions and provenance.
3. Information-readiness baseline.
4. Structural scope.
5. Pset mapping.
6. Pset validation.
7. Asset_ID pilot.
8. Multi-version binding.
9. Integrity issues.
10. Semantic review.
11. Limitations.

## Figures

1. AIM readiness architecture.
2. Revit–IFC controlled exchange.
3. Identifier separation.
4. Versioned binding lifecycle.
5. Scope decision flow.
6. Before/after IFC information.
7. Acceptance workflow.
8. Gate 2 evidence map.

---

# 13. PAPER G3 — CLAIM, NOVELTY VÀ BASELINES

## 13.1. Central claim

> A pre-registered, version-aware framework can trace vibration-based condition evidence bidirectionally through BIM-linked components, inspection records and action-status histories, while detecting predefined identity, relationship and provenance failures in a controlled laboratory case.

## 13.2. Đóng góp G3

### G3-C1 — Evidence-to-inspection chain

```text
Condition_Evidence_ID
→ BIM component
→ Inspection_Record_ID
→ Action_Record
```

### G3-C2 — Bidirectional validation

Không chỉ:

```text
evidence → component
```

mà còn:

```text
action → inspection → evidence → run → sensor → source file
```

### G3-C3 — Pre-registered CQs

CQs và thresholds khóa trước test.

### G3-C4 — Invalid-data testing

Bao gồm:

- duplicate;
- orphan;
- conflicting binding;
- missing provenance;
- invalid transition;
- wrong model version.

### G3-C5 — Inspection semantics

Tách:

```text
condition evidence
≠ inspection finding
≠ recommended action
≠ authorized decision
```

## 13.3. Baseline comparisons

### B-G3-1 — Forward-only linkage

Chứng minh một chiều không đảm bảo auditability.

### B-G3-2 — No version context

Chứng minh BIM_GUID không kèm Model_Version_ID tạo ambiguity.

### B-G3-3 — Valid-data-only demo

Chứng minh chỉ chạy dữ liệu đẹp không kiểm được integrity.

### B-G3-4 — No provenance chain

Chứng minh prediction không Run_ID/Sensor_ID/model config không thể audit.

---

# 14. PAPER G3 — EVIDENCE BẮT BUỘC

## 14.1. Gate 2 accepted substrate

Paper G3 dùng:

- accepted Asset_ID–BIM binding;
- Model_Version_ID;
- accepted IFC;
- scope;
- data dictionary.

## 14.2. Laboratory condition evidence

Tối thiểu:

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
```

## 14.3. Valid fixtures

```text
VF-01 Normal
VF-02 Watch
VF-03 Inspect
VF-04 Priority Inspection with review
VF-05 Data-quality issue
VF-06 BIM version update
```

## 14.4. Invalid fixtures

```text
IF-01 Duplicate Sensor_ID
IF-02 Duplicate Asset_ID
IF-03 Duplicate BIM_GUID/version
IF-04 Missing Model_Version_ID
IF-05 Orphan Condition_Evidence
IF-06 Missing Run_ID
IF-07 Missing Source_Data
IF-08 Orphan Inspection_Record
IF-09 Inspection missing Asset/BIM
IF-10 Action missing Inspection_Record
IF-11 verified missing reviewer
IF-12 invalid Action_Status transition
IF-13 conflicting Asset–BIM binding
IF-14 superseded model used as current
IF-15 broken document link
IF-16 missing model/evaluation provenance
```

## 14.5. Real evidence requirement

Controlled synthetic fixtures được phép để kiểm:

- schema;
- constraints;
- query;
- invalid detection.

Nhưng để Paper G3 trả lời RQ2 đầy đủ, phải có ít nhất một chuỗi từ laboratory condition evidence thật.

Nếu chỉ có synthetic fixtures:

> Evidence is currently insufficient để tuyên bố vibration-based laboratory traceability validity.

---

# 15. PAPER G3 — PRE-REGISTERED COMPETENCY QUESTIONS

## Required CQ đề xuất

```text
CQ01 Sensor → BIM/version
CQ02 BIM → Asset_ID
CQ03 binding cardinality/conflict
CQ04 evidence provenance
CQ05 model/evaluation provenance
CQ07 evidence → inspection
CQ09 inspection → source
CQ10 current action status
CQ11 action history
CQ12 orphan detection
CQ13 duplicate/conflict detection
CQ14 verified-evidence rule
CQ15 model version
CQ17 forward trace
CQ18 reverse trace
CQ19 reproducibility from manifest
CQ20 deterministic repeat
```

## Supporting CQ

```text
CQ06 list all evidence for component
CQ08 inspection documents/findings
CQ16 binding history across versions
```

## Thresholds đề xuất

- 100% Required CQ PASS;
- 100% valid forward chain;
- 100% valid reverse chain;
- 100% mandatory invalid fixtures detected;
- 0 valid fixture false rejected;
- 0 unresolved unexpected orphan;
- 0 unresolved binding conflict;
- 100% required provenance present.

Thresholds phải được phê duyệt trước Gate 3.

---

# 16. PAPER G3 — METHODS

## 16.1. Research design

```text
Pre-registration
→ immutable fixtures
→ laboratory evidence import
→ deterministic implementation
→ forward/reverse tests
→ invalid-data tests
→ CQ evaluation
→ reproducibility
```

## 16.2. Unit of analysis

```text
one traceability chain
```

gồm:

```text
Condition_Evidence_ID
↔ BIM-linked component
↔ Inspection_Record_ID
↔ Action_Record
```

## 16.3. Implementation

Công cụ tối thiểu:

```text
SQLite
Python
SQL
IfcOpenShell
```

Không cần production website.

## 16.4. Tables

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

## 16.5. Queries

```text
vw_forward_trace
vw_reverse_trace
vw_orphans
vw_duplicates
vw_conflicting_bindings
vw_provenance_completeness
```

---

# 17. PAPER G3 — METRICS

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
Query_Execution_Time
Management_Clarity_Rating
Management_Usefulness_Rating
```

## Không dùng

- Health Index;
- field classification accuracy;
- damage severity;
- RUL;
- maintenance optimization.

---

# 18. GATE 3 ROADMAP

## G3-A — Freeze fixtures

### Output

```text
GATE3_FIXTURE_REGISTER.csv
GATE3_EXPECTED_RESULTS.csv
fixture_hashes.csv
```

## G3-B — Import condition evidence

### Output

```text
CONDITION_EVIDENCE_REGISTER.csv
CONDITION_EVIDENCE_INPUT_MANIFEST.csv
```

## G3-C — Build database/query layer

### Output

```text
traceability_lab_v1.sqlite
schema.sql
constraints.sql
views.sql
```

## G3-D — Forward trace test

### Output

```text
FORWARD_TRACE_RESULTS.csv
FORWARD_TRACE_QUERY_LOG.sql
```

## G3-E — Reverse trace test

### Output

```text
REVERSE_TRACE_RESULTS.csv
REVERSE_TRACE_QUERY_LOG.sql
```

## G3-F — Invalid-data tests

### Output

```text
INVALID_DATA_TEST_RESULTS.csv
INVALID_FIXTURE_DETECTION_MATRIX.csv
```

## G3-G — CQ evaluation

### Output

```text
GATE3_CQ_RESULTS.csv
```

## G3-H — Reproducibility

### Output

```text
GATE3_REPRODUCIBILITY_MANIFEST.csv
environment.yml
requirements.txt
code_commit.txt
query_hashes.csv
```

## G3-I — Management semantic review

Supporting Evidence, không thay Gate 5.

## G3-J — Gate 3 closure

### Verdict

```text
CLOSE
CLOSE_WITH_DECLARED_LIMITATIONS
DO_NOT_CLOSE
```

---

# 19. ĐIỀU KIỆN G3 PAPER-READY

| Hạng mục | Yêu cầu |
|---|---|
| Gate substrate | Gate 2 closed |
| Pre-registration | Approved before test |
| Real lab evidence | Ít nhất một complete chain |
| Forward | 100% Required valid fixture |
| Reverse | 100% Required valid fixture |
| Invalid tests | 100% mandatory detected |
| False rejection | 0 |
| CQ | 100% Required PASS |
| Provenance | 100% required fields |
| Reproducibility | Rebuild + identical repeat |
| Claim boundary | Laboratory traceability only |
| Closure | Gate 3 approved |

---

# 20. PAPER G3 — OUTLINE

## 1. Introduction

- evidence-to-action gap;
- limitations of one-way sensor-to-BIM demos;
- research question;
- contributions.

## 2. Background and gap

- vibration condition evidence;
- BIM/AIM traceability;
- inspection records;
- bidirectional provenance;
- invalid-data testing.

## 3. Pre-registered research design

- Gate 2 substrate;
- CQ derivation;
- Required/Supporting;
- thresholds;
- scope.

## 4. Traceability framework

- entities;
- identifier chain;
- versioning;
- integrity rules;
- Inspection/Action semantics.

## 5. Laboratory implementation

- condition evidence;
- BIM component binding;
- fixtures;
- database/query layer.

## 6. Validation methods

- forward;
- reverse;
- invalid;
- reproducibility;
- management review.

## 7. Results

- CQ;
- trace success;
- invalid detection;
- provenance;
- reproducibility.

## 8. Discussion

- novelty;
- why not software demo;
- management relevance;
- generalizability;
- limitations.

## 9. Conclusion

- answer RQ2;
- transition to G4 field feasibility.

---

# 21. PAPER G3 — TABLES VÀ FIGURES

## Tables

1. Competency questions.
2. Required/Supporting classification.
3. Entity dictionary.
4. Integrity rules.
5. Valid fixtures.
6. Invalid fixtures.
7. Forward results.
8. Reverse results.
9. Invalid detection.
10. CQ evaluation.
11. Reproducibility.
12. Limitations.

## Figures

1. Evidence-to-inspection architecture.
2. Pre-registration flow.
3. Identifier chain.
4. ER model.
5. Forward trace.
6. Reverse trace.
7. Invalid-data test architecture.
8. BIM-linked Inspection_Record.
9. Version transition.
10. Gate 3 evidence map.

---

# 22. QUAN HỆ HAI BÀI VỚI CHƯƠNG 5

## Chương 5.1–5.6 — Paper G2

```text
5.1 RQ2 and management requirements
5.2 AIM/Revit/IFC semantics
5.3 BIM information readiness
5.4 Versioned identity governance
5.5 Controlled Revit–IFC exchange
5.6 Gate 2 evidence and limitations
```

## Chương 5.7–5.12 — Paper G3

```text
5.7 Traceability schema
5.8 Inspection and action semantics
5.9 Pre-registered competency questions
5.10 End-to-end laboratory implementation
5.11 Validation results
5.12 Discussion and RQ2 answer
```

## Không lặp

Chương luận án có thể chứa chi tiết đầy đủ hơn, nhưng hai bài phải dẫn chiếu nhau thay vì lặp toàn bộ.

---

# 23. KẾ HOẠCH THỰC THI TÍCH HỢP

## Pha 1 — 0–4 tuần: hoàn tất nền G2

| Tuần | Công việc | Output |
|---|---|---|
| 1 | Freeze Pset + clean model | Acceptance record |
| 2 | Use cases + CQ source matrix | Pre-registration draft |
| 3 | Scope + Asset_ID convention | Target scope |
| 4 | Schema + IR-21 + Action transitions | Design package |

## Pha 2 — 5–8 tuần: pilot và đóng G2

| Tuần | Công việc | Output |
|---|---|---|
| 5 | Asset_ID pilot | Verified import CSV |
| 6 | Graph 02 dry-run/write | Change logs |
| 7 | Enriched IFC + audits | Accepted IFC |
| 8 | Semantic review + G2 closure | Closure package |

## Pha 3 — 9–12 tuần: Paper G2

| Tuần | Công việc | Output |
|---|---|---|
| 9 | Multi-version analysis | Results tables |
| 10 | Baseline comparisons | Figures |
| 11 | Draft Paper G2 | Manuscript v0.1 |
| 12 | Internal review | Submission-ready draft |

Paper G2 có thể được viết trong khi G3 bắt đầu, nhưng không dùng kết quả G3.

## Pha 4 — 9–14 tuần: Gate 3

| Tuần | Công việc | Output |
|---|---|---|
| 9 | Freeze fixtures | Fixture register |
| 10 | Import lab evidence + database | SQLite package |
| 11 | Forward/reverse tests | Trace results |
| 12 | Invalid tests | Detection matrix |
| 13 | CQ + reproducibility | G3 results |
| 14 | G3 closure | Closure package |

## Pha 5 — 15–18 tuần: Paper G3/Core Paper 2

| Tuần | Công việc | Output |
|---|---|---|
| 15 | Freeze evidence package | Tables/figures |
| 16 | Draft Methods/Results | Manuscript |
| 17 | Discussion + claim audit | v0.2 |
| 18 | Internal review | Submission-ready draft |

---

# 24. PUBLICATION DECISION GATES

## Paper G2 submit/no-submit

### SUBMIT khi

- Gate 2 closed;
- multi-version evidence đủ;
- paper có baseline comparison;
- management review có kết quả;
- novelty không chỉ là “Revit export”.

### HOLD khi

- chỉ có 2-element Pset test;
- chưa có real Asset_ID pilot;
- chưa có enriched IFC;
- chưa có multi-version analysis;
- chưa có independent claim.

## Paper G3 submit/no-submit

### SUBMIT khi

- Gate 3 closed;
- real laboratory evidence chain;
- all Required CQ PASS;
- invalid detection complete;
- reproducibility complete;
- claim audit complete.

### HOLD khi

- chỉ synthetic fixtures;
- chỉ forward trace;
- thresholds chưa pre-register;
- manual joins còn tồn tại;
- Gate 1 evidence provenance chưa đủ.

---

# 25. RỦI RO CÔNG BỐ

| Rủi ro | Paper | Kiểm soát |
|---|---|---|
| G2 bị coi là technical note | G2 | Multi-version comparison + identity governance + semantic review |
| G2 thiếu generalizability | G2 | Thêm class/case hoặc tuyên bố limitation |
| G3 bị coi là software demo | G3 | Pre-registration + invalid-data tests + formal CQs |
| Hai bài trùng nội dung | Cả hai | Anti-overlap matrix |
| G3 phụ thuộc G1 chưa đủ | G3 | Chỉ dùng evidence có provenance; tách validity levels |
| Management relevance yếu | Cả hai | Expert semantic review |
| ISO overclaim | G2 | Aligned, not certified |
| Automated decision creep | G3 | Permitted transitions + human review |
| FEM creep | Cả hai | Limited-FEM firewall |
| Journal quartile thay đổi | Cả hai | Kiểm tra tại thời điểm nộp |

---

# 26. CẤU TRÚC FOLDER

```text
05_GATE2/
├── 00_GOVERNANCE/
├── 01_PSET_ACCEPTANCE/
├── 02_CQ_PRE_REGISTRATION/
├── 03_SCOPE_IDENTITY/
├── 04_SCHEMA_RULES/
├── 05_ASSET_ID_PILOT/
├── 06_ENRICHED_IFC/
├── 07_MANAGEMENT_REVIEW/
├── 08_GATE2_CLOSURE/
└── 09_PAPER_G2/

06_GATE3/
├── 00_GOVERNANCE/
├── 01_FIXTURES/
├── 02_CONDITION_EVIDENCE/
├── 03_DATABASE/
├── 04_FORWARD_TRACE/
├── 05_REVERSE_TRACE/
├── 06_INVALID_TESTS/
├── 07_CQ_REPRODUCIBILITY/
├── 08_GATE3_CLOSURE/
└── 09_PAPER_G3_CORE_PAPER2/
```

---

# 27. EVIDENCE MATRIX

```text
Evidence_ID
RQ
WP
Chapter
Paper_ID
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

`Paper_ID` chỉ nhận:

```text
G2_SUPPORTING_PAPER
G3_CORE_PAPER2
THESIS_ONLY
```

---

# 28. GO / NO-GO HIỆN TẠI

| Hành động | Quyết định | Lý do |
|---|---|---|
| Freeze Pset ACCEPTED_V1 | GO | 41/41 PASS |
| Tạo CQ source matrix | GO | Phải trước schema lock |
| Tạo target scope | GO | Đang chặn pilot |
| Viết Paper G2 Results | NO-GO | Chưa có enriched pilot/multi-version analysis |
| Chuẩn bị Asset_ID pilot | CONDITIONAL GO | Sau scope + convention |
| Graph 02 dry-run | NO-GO hiện tại | Pilot chưa approved |
| Close G2 | NO-GO | Chưa hoàn tất design/pilot |
| Mở G3 | NO-GO | G2 chưa đóng |
| Draft Introduction Paper G2 | GO | Có thể viết framing, chưa viết Results cuối |
| Draft Introduction Paper G3 | CONDITIONAL GO | Chỉ concept, không khóa claim kết quả |

---

# 29. CLAIM → EVIDENCE → LIMITATION → NEXT ACTION

## Claim

Việc tách Gate 2 và Gate 3 thành hai bài báo là khả thi về học thuật nếu hai bài có câu hỏi, unit of analysis, evidence và claim khác nhau.

## Evidence

- G2 đã có nền kỹ thuật mạnh: model/version registry, crosswalk, round-trip audit và 41/41 Pset validation.
- G3 có thiết kế phương pháp mạnh: pre-registration, forward/reverse queries, invalid fixtures và reproducibility.
- The Council xác nhận kiến trúc tổng thể có giá trị nhưng yêu cầu tăng novelty và management relevance.

## Limitation

- Paper G2 hiện chưa đủ kết quả độc lập để bảo đảm Q2.
- Asset_ID thật và official enriched IFC chưa có.
- G2 chưa đóng.
- G3 chưa có real condition evidence chain.
- Evidence is currently insufficient để tuyên bố hai paper đã sẵn sàng nộp.

## Next action

```text
1. Freeze Pset ACCEPTED_V1.
2. Lập CQ source/rationale matrix.
3. Khóa sensor_target_scope.csv.
4. Khóa Asset_ID convention.
5. Chỉ sau đó chuẩn bị Asset_ID pilot.
```

---

# 30. ROADMAP LOCK v1.2

Bản v1.2 khóa:

```text
Gate 2 → Supporting Paper G2
Gate 3 → Core Paper 2 / Paper G3
No overlap between the two papers
CQ before schema v1 lock
IR-21 conflicting binding
Human-controlled action transitions
Multi-version evidence for Paper G2
Real laboratory evidence for Paper G3
Forward + reverse + invalid-data validation
```

Mọi thay đổi phải ghi:

```text
Version
Date
Change
Reason
Affected_Gate
Affected_Paper
Affected_CQ
Affected_Rule
Approved_By
```

Không được:

- đổi Required CQ sau khi xem kết quả;
- đổi fixture không có amendment;
- dùng G3 results để “cứu” novelty Paper G2;
- lặp cùng bảng/kết quả ở hai bài;
- tuyên bố quartile khi chưa kiểm tra tại thời điểm nộp.

---

# 31. SOURCE BASIS

Nguồn điều hành:

1. `MASTER_RESEARCH_CHARTER_v1.1_LIMITED_FEM_20260717.md`
2. `RESEARCH_ARCHITECTURE_DECISION_RECORD_20260717.md`
3. `G2_G3_PAPER2_REVISED_ROADMAP_v1.1.md`
4. `G2_G3_REVIT_IFC_AIM_EXECUTION_ROADMAP.md`
5. `PSET_7_PARAMETER_QUICK_REVIEW.md`
6. `Revit-IFCGuide.md`
7. Phản biện The Council ngày 03/08/2026

Thứ tự ưu tiên khi có mâu thuẫn:

```text
Charter v1.1
→ ADR Limited-FEM
→ approved pre-registration
→ Gate evidence
→ Roadmap v1.2
→ paper drafts
```
