# KẾ HOẠCH TÌM KIẾM VÀ SÀNG LỌC TÀI LIỆU PHỤC VỤ GATE 1 VÀ GATE 2–3

**Ngày:** 11/08/2026  
**Kiến trúc kiểm soát:** Limited-FEM, ADR-2026-001  
**Chuỗi đã khóa:** `Vibration data → condition/state-change evidence → BIM-linked component → inspection record → inspection-maintenance action support`  
**Chuỗi định danh:** `Sensor_ID → BIM_GUID → Condition_Evidence_ID → Inspection_Record_ID → Action_Status`

## 1. Định tuyến và phán quyết

| Gói tìm kiếm | Định tuyến | Evidence type | Mục đích |
|---|---|---|---|
| LS-G1 | RQ1 → WP1 → Chương 4 → Paper 1 → Gate 1 → Core Scope | Laboratory evidence | Bảo vệ giao thức, diễn giải LORO–LOCO/campaign effect, xác định ranh giới claim |
| LS-G23 | RQ2 → WP2 → Chương 5 → Paper 2 → Gate 2–3 → Core Scope | Information traceability | Thiết kế mô hình dữ liệu, competency questions, ràng buộc định danh và tiêu chí kiểm chứng |
| LS-STD | Cross-cutting → Chương 2–3 → Supporting Scope | Standards/method context | Chuẩn hóa provenance, BIM/IFC, quản lý thông tin và hồ sơ tài sản |

**Phán quyết:** Không làm lại một systematic review rộng về “AI–BIM–Digital Twin”. Thực hiện **targeted evidence search + backward/forward snowballing**, bắt đầu từ kho 108 bản ghi/33 bài đã deep-read và 7 DOI đã kiểm chứng trong `CITATION_AUDIT_GATE1_TO_GATE23_20260811.md`.

Tài liệu không tự khóa Gate 1. Gate 1 chỉ đóng bằng evidence pack thực nghiệm; văn liệu chỉ bảo vệ thiết kế, cách diễn giải và giới hạn suy rộng. Với Gate 2–3, văn liệu phải được hoàn thành **trước** khi khóa competency questions và schema.

## 2. Câu hỏi bằng chứng cần trả lời

### 2.1. Gate 1

| ID | Câu hỏi tìm kiếm | Dùng ở Paper 1 |
|---|---|---|
| G1-L1 | Đơn vị chia dữ liệu nào ngăn leakage khi một run được chia thành nhiều window? | Phương pháp LORO; split trước windowing; train-only preprocessing |
| G1-L2 | Độ lặp lại và biến thiên giữa các measurement campaign của kết cấu/liên kết bu lông được báo cáo thế nào? | Giải thích `C2 > C1 > C3`; campaign effect |
| G1-L3 | LORO cao nhưng LOCO thấp được diễn giải dưới domain shift/generalization như thế nào? | Generalization boundary; không chuyển classifier lab → field |
| G1-L4 | Thứ tự thu nhận, tháo–lắp, mounting, excitation và sensor configuration có thể tạo confounding nào? | Threats to validity; protocol registry; Campaign 4 nếu cần |
| G1-L5 | Bất định phải báo cáo ở cấp run/campaign bằng metric và phép kiểm nào? | Macro-F1, balanced accuracy, fold-level results, cluster bootstrap/permutation |
| G1-L6 | Baseline-referenced representation có cơ sở và nghĩa vụ kiểm chứng nào? | Thí nghiệm phương pháp bổ sung; không biến thành claim field diagnosis |

### 2.2. Gate 2–3

| ID | Câu hỏi tìm kiếm | Đầu ra Gate 2–3 |
|---|---|---|
| G23-L1 | Provenance/lineage của condition evidence nên được biểu diễn bằng thực thể, quan hệ và metadata nào? | Data model và provenance requirements |
| G23-L2 | Competency questions được hình thành, pre-register và dùng để kiểm chứng ontology/schema ra sao? | CQ set và protocol đánh giá |
| G23-L3 | IFC GlobalId/BIM_GUID có giới hạn gì qua export, import và round-trip? | Identity constraints và conflict tests |
| G23-L4 | Sensor evidence được liên kết tới BIM object, inspection record và action status như thế nào? | Evidence-to-inspection model; không dừng ở visualization |
| G23-L5 | Completeness, uniqueness, consistency, orphan, conflict và bidirectional traceability được đo thế nào? | Tiêu chí chấp nhận Gate 2 và test suite Gate 3 |
| G23-L6 | Các chuẩn chính thức nào chỉ cung cấp framing, và chuẩn nào tạo ràng buộc dữ liệu kiểm chứng được? | Standards map; tránh tuyên bố “tuân thủ” quá mức |

## 3. Nguồn tìm kiếm

### 3.1. Nguồn chính

- Scopus và Web of Science Core Collection: truy vấn chính, xuất metadata và loại trùng.
- Engineering Village/Compendex, IEEE Xplore và ASCE Library: bổ sung kỹ thuật cảm biến, ontology, interoperability và asset information.
- ScienceDirect, SpringerLink, SAGE, Taylor & Francis và ITcon: lấy toàn văn từ publisher.
- Google Scholar: chỉ dùng cho backward/forward snowballing và tìm bản manuscript hợp lệ; không dùng số citation làm thước đo chất lượng.
- Crossref/publisher page: xác minh DOI, năm, volume/issue và phiên bản xuất bản.
- Nguồn chính thức: W3C cho provenance; buildingSMART cho IFC/IDS; ISO và nguồn TCVN chính thức cho quản lý thông tin/tài sản. Dùng phiên bản hiện hành tại ngày khóa evidence pack.

### 3.2. Khoảng thời gian

- Vòng hiện đại: 2018–11/08/2026.
- Vòng nền tảng: không giới hạn năm, chỉ qua citation chaining từ các bài lõi hoặc tiêu chuẩn chính thức.
- Ưu tiên tiếng Anh; tiếng Việt chỉ cho TCVN, quy định và bối cảnh quản lý trong nước.

## 4. Chuỗi truy vấn khởi đầu

Các chuỗi dưới đây viết theo cú pháp Scopus `TITLE-ABS-KEY`; khi chuyển sang WoS dùng `TS=` và hiệu chỉnh sau pilot search.

### 4.1. Gate 1

**G1-Q1 — Leakage và group-aware validation**

```text
TITLE-ABS-KEY(
  (vibration OR "structural health monitoring") AND
  ("data leakage" OR "grouped cross-validation" OR "group-aware validation"
   OR "leave-one-run-out" OR "event-wise split" OR "record-wise split")
)
```

**G1-Q2 — Repeatability, campaign và assembly variability**

```text
TITLE-ABS-KEY(
  (vibration OR modal OR "acoustic emission") AND
  ("bolted joint*" OR "steel frame*" OR "jointed structure*") AND
  (repeatab* OR reproducib* OR variability OR "measurement campaign*" OR reassembl*)
)
```

**G1-Q3 — Cross-campaign/domain generalization**

```text
TITLE-ABS-KEY(
  ("structural health monitoring" OR "condition monitoring") AND
  ("cross-campaign" OR "domain shift" OR "domain generalization" OR "domain adaptation") AND
  (vibration OR "bolted joint*")
)
```

**G1-Q4 — Sensor configuration và acquisition protocol**

```text
TITLE-ABS-KEY(
  (accelerometer* OR "sensor configuration*" OR "low-cost sensor*") AND
  vibration AND ("steel frame*" OR "bolted joint*") AND
  (classification OR discrimination OR repeatab*)
)
```

**G1-Q5 — Healthy-baseline-referenced representation**

```text
TITLE-ABS-KEY(
  (vibration AND "healthy baseline") AND
  ("baseline-referenced" OR normalization OR standardization) AND
  ("domain shift" OR variability OR generalization)
)
```

### 4.2. Gate 2–3

**G23-Q1 — BIM/IFC provenance và traceability**

```text
TITLE-ABS-KEY(
  (BIM OR IFC OR "digital twin") AND
  (provenance OR traceab* OR lineage) AND
  (sensor* OR "condition monitoring" OR inspection)
)
```

**G23-Q2 — Competency questions và schema/ontology validation**

```text
TITLE-ABS-KEY(
  (ontology OR "data model" OR schema) AND
  ("competency question*" OR "ontology evaluation") AND
  (BIM OR construction OR "asset management")
)
```

Chạy thêm một truy vấn nền tảng không có `BIM/construction` để không bỏ sót phương pháp CQ gốc.

**G23-Q3 — BIM/IFC identity persistence và round-trip**

```text
TITLE-ABS-KEY(
  (IFC OR BIM) AND
  (GlobalId OR GUID OR "persistent identifier*" OR "round-trip") AND
  (interoperability OR exchange OR traceab*)
)
```

**G23-Q4 — Inspection/maintenance records**

```text
TITLE-ABS-KEY(
  (BIM OR "digital twin") AND
  ("inspection record*" OR "maintenance record*" OR "asset register" OR "work order*") AND
  (link* OR traceab* OR provenance)
)
```

**G23-Q5 — Information quality và constraints**

```text
TITLE-ABS-KEY(
  (BIM OR IFC OR "asset information") AND
  ("information quality" OR completeness OR consistency OR uniqueness OR orphan* OR conflict*) AND
  (validation OR assessment)
)
```

**G23-Q6 — SHM–BIM component-level linkage**

```text
TITLE-ABS-KEY(
  ("structural health monitoring" OR vibration) AND
  (BIM OR IFC) AND
  ("component-level" OR inspection) AND
  (traceab* OR framework OR workflow)
)
```

## 5. Quy trình sàng lọc

### Bước 0 — Audit kho hiện có

1. Hợp nhất 108 bản ghi canonical, 33 bài đã deep-read và 7 DOI đã kiểm chứng.
2. Gắn mỗi bài vào đúng một đích chính: G1, G2–3, G4, Supporting hoặc Out of Scope.
3. Không tìm lại bài đã có; chỉ bổ sung khi một evidence question còn trống.

### Bước 1 — Pilot query

- Chạy từng query trên Scopus; xem 30–50 kết quả đầu.
- Ghi từ khóa nhiễu và thuật ngữ đồng nghĩa.
- Chỉnh query một lần trước khi chạy chính thức; lưu nguyên chuỗi và ngày tìm.

### Bước 2 — Title/abstract screening

**Bao gồm Gate 1 khi:** có dữ liệu vật lý; mô tả đơn vị đo/run/session/campaign; hoặc cung cấp phương pháp rõ cho leakage, generalization, repeatability và uncertainty.

**Loại Gate 1 khi:** chỉ random-window split mà không nhận diện leakage; chỉ mô phỏng; chỉ tối ưu accuracy; hoặc tuyên bố chuyển lab → field không có kiểm chứng độc lập. Bài có lỗi phương pháp đặc biệt rõ có thể giữ làm `AVOID/design warning`, không dùng làm bằng chứng tích cực.

**Bao gồm Gate 2–3 khi:** có mô hình dữ liệu/thực thể–quan hệ/ràng buộc định danh; CQ hoặc yêu cầu định nghĩa trước; kiểm chứng đo được; liên kết tới inspection/maintenance record hoặc action.

**Loại Gate 2–3 khi:** chỉ hiển thị sensor trên BIM; dashboard/demo không có schema và tiêu chí; BIM-to-FEM thuần kỹ thuật; Digital Twin predictive/RUL; hoặc phần mềm thương mại không công bố logic kiểm chứng.

### Bước 3 — Full-text audit

- DOI và version được xác minh từ publisher/Crossref.
- Đọc đầy đủ Method, Results, Discussion, Limitations và phụ lục liên quan.
- Kiểm tra bằng locator trang/bảng/hình; abstract không được dùng làm bằng chứng phương pháp.
- Mỗi bài lập một record theo cấu trúc `Claim → Evidence → Limitation → Next action` và route đầy đủ.

### Bước 4 — Snowballing có kiểm soát

- Backward snowballing từ bài core để tìm nguồn nền tảng.
- Forward snowballing để tìm bài 2023–2026 áp dụng/đối chiếu.
- Chỉ giữ bài mới nếu lấp một evidence question hoặc cung cấp kết quả mâu thuẫn đáng kể.

## 6. Chấm chất lượng

Điểm chỉ dùng để ưu tiên deep-read; không thay thế phán đoán học thuật.

### 6.1. Gate 1 — 10 điểm

| Tiêu chí | Điểm |
|---|---:|
| Dữ liệu thực nghiệm vật lý và đơn vị phân tích rõ | 0–2 |
| Split/grouping logic rõ | 0–2 |
| Kiểm soát leakage và train-only preprocessing | 0–2 |
| Có independent run/campaign/domain validation | 0–2 |
| Báo cáo bất định/error pattern | 0–1 |
| Có đủ thông tin tái lập | 0–1 |

`Core G1`: từ 7/10 và không FAIL ở split/leakage. Bài dưới ngưỡng chỉ dùng Supporting/AVOID.

### 6.2. Gate 2–3 — 10 điểm

| Tiêu chí | Điểm |
|---|---:|
| Mô hình thực thể–quan hệ/schema hình thức | 0–2 |
| Quy tắc định danh/provenance rõ | 0–2 |
| CQ/yêu cầu nghiệp vụ định nghĩa trước | 0–2 |
| Kiểm chứng có metric/test/scenario đo được | 0–2 |
| Liên kết đến inspection/action | 0–1 |
| Có artifact/standard/reproducibility support | 0–1 |

`Core G2–3`: từ 7/10, bắt buộc có mô hình hình thức và kiểm chứng đo được. “BIM + sensor visualization” không đạt Core dù điểm tổng cao.

## 7. Cấu trúc evidence matrix

Mỗi bản ghi phải có tối thiểu:

`Record_ID; Title; DOI; Year; Venue; Query_Block; Evidence_Question; RQ; WP; Chapter; Paper; Gate; Scope; Evidence_Type; Unit_of_Analysis; Data/Case; Split_or_CQ_Logic; Validation; Metrics; Author_Claim; Claim_Boundary; Limitations; Thesis_Use; CITE/ADAPT/BENCHMARK/AVOID; Locator; Decision`.

Riêng G1 bổ sung: `Run/Session/Campaign_Unit; Windowing_Order; Leakage_Control; Train_Only_Preprocessing; Cross_Campaign_Test; Uncertainty`.

Riêng G2–3 bổ sung: `Entities; Relationships; Identifier_Rules; Provenance; CQ; Completeness; Uniqueness; Orphan_Test; Conflict_Test; Bidirectional_Test; Inspection_Link; Action_Link`.

## 8. Đầu ra bắt buộc

### Gate 1 literature support pack

1. `G1_SEARCH_LOG.csv`
2. `G1_SCREENING_MATRIX.csv`
3. `G1_CORE_DEEP_READ_MANIFEST.csv`
4. `G1_METHOD_AND_CLAIM_JUSTIFICATION.md`
5. `G1_LORO_LOCO_CAMPAIGN_SYNTHESIS.md`
6. `G1_PAPER1_CITATION_MAP.csv`
7. `G1_LITERATURE_QC_REPORT.md`

Mục tiêu tìm mới: khoảng 6–10 bài core ngoài 7 bài seed, cộng các bài supporting cần thiết. Con số không phải tiêu chí đạt; độ phủ evidence questions mới là tiêu chí.

### Gate 2–3 evidence pack

1. `G23_SEARCH_LOG.csv`
2. `G23_SCREENING_MATRIX.csv`
3. `G23_CORE_DEEP_READ_MANIFEST.csv`
4. `G23_PROVENANCE_CQ_IFC_IDENTITY_SYNTHESIS.md`
5. `G23_CQ_SOURCE_AND_PROOF_MAP.csv`
6. `G23_SCHEMA_CONSTRAINT_CATALOG.md`
7. `G23_GAP_STATEMENT_v0.9.md`
8. `G2_PREREGISTRATION_PACK_v0.9.md`
9. `G23_LITERATURE_QC_REPORT.md`

Mục tiêu deep-read: khoảng 12–18 bài core và các tiêu chuẩn/đặc tả chính thức. Không khóa schema chỉ vì đủ số bài.

## 9. Lịch thực hiện 14 ngày làm việc

| Ngày | Việc chính | Đầu ra |
|---|---|---|
| 1–2 | Audit kho cũ, loại trùng, lập evidence-gap matrix | Danh mục seed + khoảng trống thật |
| 3 | Pilot và khóa query Gate 1 | Search protocol G1 |
| 4–5 | Search, screening và lấy full text G1 | Screening matrix + manifest |
| 6–7 | Deep-read bài G1 ưu tiên | Evidence records |
| 8 | Cross-paper synthesis G1, map vào kết quả thực nghiệm | G1 literature support pack |
| 9 | Pilot và khóa query Gate 2–3 | Search protocol G23 |
| 10–11 | Search, screening, full text G23 | Screening matrix + manifest |
| 12–13 | Deep-read provenance/CQ/IFC identity/inspection | Evidence records + constraint catalog |
| 14 | Tổng hợp gap, CQ-source map và pre-registration v0.9 | G23 evidence pack |

Nếu nhân lực hạn chế, hoàn thành ngày 1–8 trước; không để Gate 2–3 làm chậm việc khóa Paper 1.

## 10. Điều kiện dừng tìm kiếm

### Gate 1

- Sáu câu hỏi G1-L1…L6 đều có bằng chứng trực tiếp hoặc được ghi `Evidence is currently insufficient.`
- Mỗi claim quan trọng có ít nhất hai nguồn độc lập hoặc một nguồn nền tảng + một nghiên cứu thực nghiệm gần đây.
- Hai vòng citation chaining liên tiếp không tạo thêm method/criterion mới.
- Văn liệu đã đủ để bảo vệ split, campaign effect, generalization boundary và uncertainty; không tiếp tục tìm chỉ để tăng số tài liệu.

### Gate 2–3

- Sáu câu hỏi G23-L1…L6 được phủ.
- Mỗi CQ ứng viên có nguồn lý luận hoặc yêu cầu quản lý rõ và proof/test tương ứng.
- Mỗi quan hệ lõi trong chuỗi định danh có ràng buộc completeness, uniqueness, orphan/conflict và round-trip.
- Khoảng trống `evidence-to-inspection/action traceability` được hỗ trợ bởi ít nhất hai nhóm văn liệu độc lập; không suy ra gap chỉ từ nhóm bài đã xem.
- Hai vòng citation chaining liên tiếp không tạo thêm loại thực thể, constraint hoặc validation criterion mới.

## 11. Ranh giới phạm vi

- **Core:** run-aware/campaign-aware laboratory evidence; provenance; BIM/IFC component identity; competency questions; inspection-record traceability.
- **Supporting:** DT maturity definition; ISO/TCVN framing; nominal FEM reference; graph database như implementation instrument.
- **Future Work:** domain adaptation lab → field, multi-building transfer, calibrated FEM, RUL/predictive maintenance.
- **Out of Scope:** AI-superiority benchmarking, field damage diagnosis, complex Health Index, autonomous maintenance, thương mại hóa phần mềm.

## 12. Claim → Evidence → Limitation → Next action

- **Claim:** Kế hoạch tìm kiếm có thể đồng thời bảo vệ Paper 1 và tạo nền khoa học cho Paper 2 mà không làm lệch kiến trúc Limited-FEM.
- **Evidence:** Charter xác định G1 là laboratory validity và G2–3 là formal traceability + end-to-end lab validation; audit 7 bài hiện tại đã chứng minh nhu cầu provenance nhưng chưa đủ cho CQ/schema/IFC identity/inspection records.
- **Limitation:** Kết quả thực nghiệm và evidence pack Gate 1 mới nhất chưa được cung cấp trong phiên này; vì vậy chưa thể kết luận Gate 1 đã đóng. `Evidence is currently insufficient.`
- **Next action:** Giao OpenCode thực hiện **Ngày 1–8 trước**, đầu vào bắt buộc gồm evidence pack thực nghiệm mới nhất, kho Zotero canonical, 7 bài seed và toàn bộ source-of-truth; chỉ sau QC G1 mới chuyển sang Ngày 9–14.
