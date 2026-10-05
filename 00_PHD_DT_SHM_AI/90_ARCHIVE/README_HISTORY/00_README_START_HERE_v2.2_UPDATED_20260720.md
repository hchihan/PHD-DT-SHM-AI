# BẮT ĐẦU TẠI ĐÂY

**Ngày lập:** 17/07/2026  
**Cập nhật mới nhất:** 20/07/2026  
**Phiên bản vận hành:** **v2.2**  
**Kiến trúc hiện hành:** **Traceability-Core · Limited-FEM**  
**Lĩnh vực:** Quản lý xây dựng / Quản lý tài sản công trình

> **Lưu ý quản trị:** README v2.2 này cập nhật trục thực thi đã thống nhất.  
> `00_GOVERNANCE/MASTER_RESEARCH_CHARTER_v2.1_TRACEABILITY_CORE_20260719.md` vẫn là nguồn học thuật cao nhất cho đến khi toàn bộ bộ governance được đồng bộ sang v2.2. Khi có mâu thuẫn chưa được xử lý, áp dụng `00_GOVERNANCE/SOURCE_OF_TRUTH_HIERARCHY_v2.1.md` và ghi rõ nội dung cần đồng bộ.

---

## 1. Luận án giải quyết vấn đề gì

Luận án phát triển một **data-informed Digital Twin framework** để tổ chức và truy vết bằng chứng trạng thái từ dữ liệu dao động đến cấu kiện BIM, hồ sơ kiểm tra và hành động quản lý có thể giải trình.

Đóng góp cốt lõi thuộc **Quản lý xây dựng**:

> hỗ trợ biện minh và truy vết trách nhiệm của quyết định kiểm tra trong điều kiện dữ liệu hư hỏng hiện trường hạn chế.

Luận án **không** nhằm:

- chẩn đoán hư hỏng hiện trường;
- dự báo RUL hoặc predictive maintenance;
- phát triển thuật toán AI mới;
- hiệu chuẩn FEM hoặc suy luận suy giảm độ cứng;
- xây dựng Health Index phức tạp;
- tự động ra quyết định bảo trì;
- phát triển phần mềm Digital Twin thương mại.

---

## 2. Trục nghiên cứu đã khóa

### 2.1. Chuỗi bằng chứng

```text
Vibration data
→ condition/state-change evidence (+ CEI)
→ BIM-linked component
→ inspection record
→ justified, accountable inspection action
```

### 2.2. Chuỗi định danh

```text
Sensor_ID
→ BIM_GUID
→ Condition_Evidence_ID (+ CEI)
→ Inspection_Record_ID
→ Action_Record_ID
```

`Action_Status` là **thuộc tính của `Action_Record_ID`**, không phải một định danh độc lập.

`CEI` là **confidence/evidence indicator** dưới dạng cấu trúc metadata của `Condition_Evidence_ID`, tối thiểu gồm:

- evidence validity status;
- model confidence;
- run/fold variability;
- sensor configuration;
- data-quality status;
- provenance;
- timestamp và version.

CEI **không phải** severity, Health Index hoặc một điểm tổng hợp phổ quát.

`FEM_Node_ID` chỉ là metadata tùy chọn. FEM luôn được mô tả:

> **nominal, uncalibrated, reference-only, not used for damage diagnosis.**

---

## 3. Ba bối cảnh nghiên cứu phải tách biệt

| Bối cảnh | Vai trò | Bằng chứng được phép | Không được tuyên bố |
|---|---|---|---|
| **Khung thép vật lý 1:10** | Nguồn tạo dữ liệu dao động và controlled connection-state evidence | Laboratory evidence; `Condition_Evidence_ID`; CEI sau G1 | Hư hỏng hoặc trạng thái thật của công trình Cam Ranh/Rapexco |
| **Revit LOD 400 tỷ lệ 1:1 của công trình Cam Ranh** | Information anchor cho cấu kiện, `BIM_GUID` và workflow truy vết | Component correspondence; BIM-linked records; case G2–G3 | Chuyển kết quả định lượng 1:10 thành kết luận hiện trường |
| **Rapexco** | Công trình thật độc lập cho field feasibility | Field sensor register; data return; baseline; traceability scenarios | Chuyển classifier/CEI/ngưỡng từ lab sang chẩn đoán Rapexco |

Đối với case Cam Ranh, mọi evidence phải giữ rõ bối cảnh:

```text
Evidence_Context = LABORATORY_1_10
Source_Asset_ID = CAMRANH_SCALED_FRAME
Reference_Asset_ID = CAMRANH_REVIT_1_1
Mapping_Type = COMPONENT_CORRESPONDENCE
Quantitative_Transfer_Allowed = FALSE
Field_Condition_Claim = NOT_PERMITTED
```

---

## 4. Cấu trúc RQ – WP – Chapter – Paper – Gate

| Trục | Nội dung | Gate | Vai trò |
|---|---|---|---|
| **RQ1 / WP1 / C4 / Paper 1** | Lab evidence; run registry; leakage-safe LORO; sensor configuration; CEI by-product | **G1** | Bằng chứng trạng thái có kiểm soát |
| **RQ2 / WP2 / C5 / Paper 2** | Evidence-aware traceability; CEI; BIM; inspection/action records; provenance; accountability | **G2, G3, G6** | **Trụ cột nhận diện ngành QLXD** |
| **RQ3 / WP3 / C6 / Paper 3 (bonus)** | Field feasibility tại Rapexco | **G4** | Bằng chứng khả thi hiện trường bắt buộc cho luận án |
| **WP4 / C7 tùy chọn** | Logic Normal → Watch → Inspect → Priority; expert/facility-manager review | **G5** | Hỗ trợ quyết định minh bạch, human-reviewed |
| **Thesis synthesis** | Tổng hợp đóng góp; Paper 3 khi site window cho phép | **G7** | Hoàn thiện luận án |

**Paper 3 có thể là bonus về công bố, nhưng minimum field-feasibility evidence tại Rapexco là bắt buộc.**

---

## 5. Evidence Gates v2.2 — cách hiểu và thực thi

### G1 — Dataset integrity and run-aware evaluation

Điều kiện chính:

1. khóa run registry;
2. hoàn thiện sensor metadata và file provenance;
3. split-before-windowing;
4. train-only preprocessing;
5. LORO với common seeds;
6. run/fold-level metrics và uncertainty;
7. xác nhận sensor mode và provenance của ResNet1D.

Cho tới khi G1 đóng, mọi kết quả định lượng phải ghi:

> **Candidate claim pending Gate 1 closure.**

### G2 — Traceability model and competency questions

G2 là **gate thiết kế**, chưa phải demo hoàn chỉnh. Cần khóa:

- identifier và assignment schema;
- context-mapping rules;
- CEI metadata dictionary;
- Inspection_Record schema;
- Action_Record và accountability schema;
- SCQ / VCQ / RCQ pre-registration;
- acceptance criteria.

### G3 — End-to-end traceability and integrity validation

G3 dùng case Cam Ranh để kiểm chứng:

```text
Laboratory evidence + CEI
→ component correspondence
→ Cam Ranh BIM_GUID
→ inspection record
→ human-authorized action record
```

Bằng chứng cần có:

- forward query;
- reverse query;
- competency-question results;
- orphan-ID test;
- duplicate-ID test;
- missing-CEI test;
- invalid-data / SHACL-or-equivalent validation.

G3 **không** chứng minh logic quyết định hiện trường và không chuyển lab evidence thành field diagnosis.

### G4 — Minimum field mapping and baseline feasibility tại Rapexco

G4 phải có:

- field-access basis được xác nhận;
- field sensor register;
- sensor assignment và component register;
- mapping tới `BIM_GUID` hoặc định danh tài sản tương đương được quản trị chính thức;
- data return;
- completeness, missingness và drift/stability checks;
- operational baseline;
- tối thiểu 2–3 field traceability scenarios.

Nếu Rapexco chưa có BIM hoàn chỉnh, có thể dùng `Asset_Component_ID` như định danh trung gian trong giai đoạn chuẩn bị; việc đóng G4 phải tuân theo tiêu chí mapping đã được governance phê duyệt.

### G5 — Inspection-action scenario review

G5 mới là nơi đánh giá:

```text
Normal → Watch → Inspect → Priority
```

Nguyên tắc:

```text
Evidence + CEI
→ recommendation
→ human review
→ Action_Record
→ Action_Status
```

Không cho phép `CEI score → tự động Priority`.

### G6 — Paper 2 submission

- Paper 2 chỉ nộp khi gap, contribution, G2 artifacts và G3 validation đã đủ bằng chứng.

### G7 — Thesis synthesis and Paper 3 when feasible

- tổng hợp luận án;
- nộp Paper 3 nếu field window và bằng chứng cho phép.

---

## 6. Candidate gap và đóng góp của Paper 2

### Candidate research gap

> Trong nhóm nghiên cứu gần nhất đã được deep-read, chưa ghi nhận một framework đồng thời tổ chức sensor-derived condition evidence cùng confidence, provenance và evidence context; liên kết hai chiều với BIM component, inspection record và accountable action record; đồng thời kiểm chứng bằng competency questions và explicit integrity-failure tests.

Đây là **candidate gap**, chưa phải tuyên bố novelty cuối cùng. Khi bằng chứng chưa đủ, ghi:

> **Evidence is currently insufficient.**

### Ba đóng góp dự kiến

1. **Context-preserving CEI-bearing evidence model**  
   Tổ chức condition evidence cùng validity, confidence, variability, data quality, provenance và bối cảnh sử dụng; ngăn lab evidence bị hiểu thành field evidence.

2. **Formally constrained bidirectional traceability model**  
   Định nghĩa thực thể, cardinality, forward/reverse relationships và referential-integrity rules từ evidence đến action.

3. **Pre-registered accountability and integrity-validation protocol**  
   Kiểm chứng bằng SCQ/VCQ/RCQ, expected answers, pass/fail criteria, invalid-data cases và actor/role/version/verification/approval metadata.

Ontology, SPARQL, blockchain, API và giao diện màu chỉ là **công cụ triển khai tùy chọn**, không phải novelty tự thân.

---

## 7. Ba track triển khai song song

### Track A — G1 / Paper 1

- run registry;
- ResNet1D provenance;
- leakage-safe LORO;
- run/fold uncertainty;
- khóa candidate claims.

### Track B — G2 → G3 / Paper 2 / Chương 5

Có thể thực hiện ngay khi G1 còn mở:

1. khóa candidate gap;
2. định nghĩa `Traceability_Instance`;
3. xây context-mapping rules;
4. thiết kế ER model và cardinality;
5. hoàn thiện CEI dictionary;
6. thiết kế Inspection_Record và Action_Record;
7. pre-register SCQ/VCQ/RCQ;
8. đặt acceptance criteria;
9. sau đó mới dựng database/knowledge graph và chạy G3.

Trong giai đoạn đầu có thể dùng evidence giả lập có cấu trúc. Khi G1 đóng, thay bằng evidence chính thức.

### Track C — Chuẩn bị G4 / Rapexco / Chương 6

Có thể thực hiện song song:

- xác nhận field access;
- lập asset/component register;
- tạo field sensor register;
- định nghĩa `Sensor_Assignment_ID`;
- chuẩn hóa file naming và data-return protocol;
- thiết kế completeness, missingness và drift checks;
- chuẩn bị 2–3 field traceability scenarios.

Repository của Rapexco phải tách khỏi lab:

```text
Evidence_Context = FIELD_RAPEXCO
```

---

## 8. Artifact tối thiểu

### Đóng G2

1. `CONTEXT_MAPPING_RULES_v0.1.md`
2. `RQ2_ENTITY_RELATIONSHIP_MODEL_v0.1.md`
3. `IDENTIFIER_AND_SENSOR_ASSIGNMENT_SCHEMA_v0.1.csv`
4. `CEI_METADATA_DICTIONARY_v0.1.csv`
5. `INSPECTION_RECORD_SCHEMA_v0.1.csv`
6. `ACTION_RECORD_ACCOUNTABILITY_SCHEMA_v0.1.csv`
7. `G2_COMPETENCY_QUESTION_REGISTER_v0.1.md`
8. `G2_ACCEPTANCE_CRITERIA_v0.1.md`

### Đóng G3

1. database/knowledge graph mẫu;
2. end-to-end traceability instances;
3. forward/reverse query report;
4. invalid-data fixtures;
5. integrity-validation report.

### Chuẩn bị và đóng G4

1. field-access evidence;
2. Rapexco asset/component register;
3. field sensor register;
4. sensor-assignment and mapping file;
5. data-return and QC report;
6. operational baseline;
7. 2–3 traceability scenarios.

---

## 9. Nguyên tắc bắt buộc

Mọi phân tích dùng cấu trúc:

```text
Claim → Evidence → Limitation → Next action
```

Phải tách biệt:

1. laboratory evidence;
2. information traceability;
3. field feasibility;
4. management decision support.

Không dùng bằng chứng của lớp này để tuyên bố kết quả của lớp khác.

Legal mapping chỉ dùng để neo nghĩa vụ quản lý và khả năng giải trình; không dùng để tạo ngưỡng hư hỏng hoặc chẩn đoán kỹ thuật.

Không được:

- chuyển kết quả định lượng hoặc classifier từ khung 1:10 sang Cam Ranh/Rapexco;
- gọi controlled connection states là field damage ground truth;
- biến CEI thành severity hoặc Health Index;
- dùng risk score 1–5 như CEI;
- tự động sinh `Action_Status` từ CEI;
- mặc định ontology, SPARQL hoặc blockchain là bắt buộc;
- mặc định Rapexco đã có `BIM_GUID` nếu chưa được xác nhận;
- mở rộng sang calibrated FEM, RUL, predictive maintenance hoặc autonomous maintenance.

---

## 10. Các file cần đọc và duy trì

1. `00_GOVERNANCE/MASTER_RESEARCH_CHARTER_v2.1_TRACEABILITY_CORE_20260719.md`
2. `00_GOVERNANCE/RQ_WP_CHAPTER_PAPER_GATE_MATRIX_v2.1.md`
3. `00_GOVERNANCE/EVIDENCE_GATES_v2.1.md`
4. `00_GOVERNANCE/SOURCE_OF_TRUTH_HIERARCHY_v2.1.md`
5. `00_GOVERNANCE/RESEARCH_DIRECTION_AND_SCOPE.md`
6. `00_GOVERNANCE/RESEARCH_ARCHITECTURE.md`
7. `01_CURRENT_CONTROL/CURRENT_STATUS_AND_NEXT_DIRECTION.md`
8. `LIVING_EVIDENCE_BASE_v2.1_TRACEABILITY_CORE.md`
9. README v2.2 này.

### Các nội dung cần đồng bộ vào governance v2.2

- chuỗi định danh kết thúc bằng `Action_Record_ID`;
- `Action_Status` là thuộc tính;
- tách rõ Cam Ranh 1:10, Revit Cam Ranh 1:1 và Rapexco;
- G3 là end-to-end traceability validation;
- G5 là management decision-support review;
- cho phép G1, G2 và G4-readiness triển khai song song;
- ontology/blockchain chỉ là công cụ tùy chọn.

---

## 11. Ưu tiên vận hành hiện tại

Không tiếp tục mở rộng governance ngoài các điều chỉnh cần đồng bộ. Tập trung ba việc song song:

1. **G1:** run registry → LORO → ResNet1D provenance → run/fold uncertainty.
2. **G2:** context rules → ER model → CEI/records → CQ và acceptance criteria.
3. **G4 readiness:** field access → asset/sensor register → data-return protocol tại Rapexco.

Trục thực thi hiện hành:

> **G1 tạo evidence → G2 định nghĩa cách quản lý evidence → G3 kiểm chứng truy vết trên case Cam Ranh → G4 kiểm tra khả thi độc lập tại Rapexco → G5 đánh giá logic hỗ trợ quyết định bởi con người.**

---

**Trạng thái v2.2:** sẵn sàng dùng làm README vận hành; các thay đổi định danh và Gate cần được đồng bộ vào Charter, Matrix, Evidence Gates và Current Status trước khi coi toàn bộ governance là v2.2 hoàn chỉnh.
