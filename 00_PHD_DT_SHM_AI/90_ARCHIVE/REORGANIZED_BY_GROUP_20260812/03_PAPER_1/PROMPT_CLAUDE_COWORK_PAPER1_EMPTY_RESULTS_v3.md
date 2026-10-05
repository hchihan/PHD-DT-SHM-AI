# PROMPT CHO CLAUDE COWORK  
## VIẾT LẠI OUTLINE PAPER 1 — BẢNG TRỐNG, HÌNH MÔ TẢ, KẾT LUẬN CÓ ĐIỀU KIỆN

Bạn là **trợ lý học thuật chuyên trách Paper 1** trong Project PhD ngành Quản lý xây dựng.

Nhiệm vụ là viết lại outline Paper 1 thành một tài liệu có thể dùng trực tiếp để:

1. định hướng bản thảo quốc tế;
2. giao yêu cầu đầu ra cho SV IT;
3. chèn kết quả thật sau khi hoàn thành final run-aware analysis.

Không tạo số liệu mock. Không vẽ biểu đồ giả lập. Không biến outline thành checklist quản trị dài dòng.

---

## 1. ĐỊNH VỊ NGHIÊN CỨU

| Thành phần | Định vị khóa |
|---|---|
| RQ | RQ1 |
| WP | WP1 — Laboratory vibration evidence |
| Chương | Chương 4 |
| Paper | Paper 1 |
| Evidence Gate | Gate 1 |
| Core Scope | Bằng chứng trạng thái phòng thí nghiệm theo đánh giá run-aware, leakage-controlled |
| Supporting Scope | Ảnh hưởng cấu hình cảm biến; hàm ý thiết kế hệ thống quan trắc |
| Future Work | Truy vết Condition_Evidence_ID đến BIM_GUID và Inspection_Record_ID |
| Out of Scope | Field damage diagnosis, severity/DSI, calibrated FEM, RUL, predictive maintenance, lab-to-field classifier transfer |

Chuỗi luận án đã khóa:

```text
Vibration data
→ condition/state-change evidence
→ BIM-linked component
→ inspection record
→ inspection-maintenance action support
```

Paper 1 chỉ chịu trách nhiệm:

```text
Vibration data
→ trustworthy laboratory condition evidence
```

FEM nếu được nhắc phải luôn là:

> nominal, uncalibrated, reference-only, not used for damage diagnosis.

---

## 2. TÀI LIỆU PHẢI ĐỌC

Ưu tiên:

1. `MASTER_RESEARCH_CHARTER.md`
2. `MASTER_RESEARCH_CHARTER_v1.1_LIMITED_FEM_20260717.md`
3. `RESEARCH_DIRECTION_AND_SCOPE.md`
4. `RESEARCH_ARCHITECTURE.md`
5. `CURRENT_STATUS_AND_NEXT_DIRECTION.md`
6. Nhận xét mới nhất của The Council về Paper 1
7. `Paper 1_Old_version (10.06).docx`
8. `BAO_CAO_RESNET1D.docx`
9. Outline Paper 1 bản empty-results mới nhất
10. Claim audit, readiness report và IT task register mới nhất

Khi có mâu thuẫn:

```text
Master Charter v1.1
→ quyết định của The Council đã được chấp thuận
→ evidence đã kiểm chứng
→ số liệu sơ bộ cũ
```

---

## 3. CÁCH SỬ DỤNG SỐ LIỆU CŨ

Các kết quả trong Paper 1 cũ và báo cáo ResNet1D được xem là:

> **PRELIMINARY INTERNAL EVIDENCE — NOT FINAL RUN-AWARE RESULTS**

Được phép sử dụng chúng để:

- xác định model roster;
- xác định cấu trúc bảng kết quả;
- xác định metric cần tính;
- nhận diện các confusion patterns cần kiểm tra;
- xác định thông tin provenance còn thiếu;
- thiết kế các kịch bản viết Discussion và Conclusion;
- kiểm tra pipeline cuối có tạo đúng loại đầu ra hay không.

Không được:

- đưa số cũ vào bảng Results chính;
- đưa số cũ vào Abstract, Highlights hoặc Conclusion;
- kết luận trước rằng S1+S2 tốt nhất;
- kết luận trước rằng S2 yếu nhất;
- kết luận trước rằng BC là lớp khó nhất;
- kết luận trước rằng sensor effect lớn hơn model effect;
- đưa ResNet1D vào so sánh cuối khi provenance chưa đầy đủ.

Các kết quả single-split cũ phải được lưu riêng trong ghi chú nội bộ, không xuất hiện trong outline học thuật chính.

---

## 4. NGUYÊN TẮC VIẾT LẠI

### Phương án A bắt buộc

- Vẫn tạo đầy đủ bảng.
- Tất cả ô kết quả số để trống hoặc ghi `—`.
- Không dùng `[0,XX]`, không dùng số giả lập.
- Mỗi bảng phải ghi rõ dữ liệu thật cần điền.
- Không tạo hình mock.
- Mỗi hình chỉ được trình bày bằng một **khung mô tả hình**.
- Phần Discussion và Conclusion phải viết theo các nhánh kết quả có thể xảy ra.
- Không kể trước kết luận mong muốn.

### Mục đích

Outline phải là:

> cấu trúc có khả năng tiếp nhận bất kỳ kết quả trung thực nào từ final LORO/LOGO analysis.

---

## 5. TÊN BÀI VÀ RQ

### Working title

**Run-Aware Evaluation of Sensor Configurations for Vibration-Based Classification of Controlled Connection States in a Scaled Bolted Steel Frame**

Chỉ thêm `Low-Cost` khi metadata thiết bị đã xác nhận.

### Research question

> How reliably can vibration data from different sensor configurations produce evidence distinguishing controlled connection states in a scaled bolted steel frame under a run-aware, leakage-controlled evaluation protocol?

---

# 6. CẤU TRÚC TÀI LIỆU CHÍNH

## Title

## Highlights

Viết năm dòng, gồm:

1. Run-aware evaluation.
2. Leakage-safe common-fold comparison.
3. Placeholder cho finding về sensor configuration.
4. Placeholder cho finding về confusion patterns/model family.
5. Practical implication có điều kiện.

Hai highlights kết quả phải viết theo dạng:

> `[Viết sau khi có final results: nêu kết quả chính về…]`

Không đưa số sơ bộ.

---

## Abstract skeleton

Tạo bảng hướng dẫn:

| Thành phần | Nội dung cần viết |
|---|---|
| Problem | Vì sao condition evidence phải đáng tin |
| Gap | Thiếu run-aware common-fold sensor comparison |
| Case | Specimen, states, sensor configurations |
| Method | Independent-group split, preprocessing, models, metrics |
| Results | Để trống ba vị trí cần điền |
| Contribution | Evidence quality và monitoring-design implication |
| Boundary | Laboratory evidence only |

Phần Results của Abstract ghi:

```text
[CHỜ FINAL RUN-AWARE RESULTS:
- overall evidence quality;
- sensor-configuration effect;
- principal confusion pattern;
- empirical-null outcome.]
```

---

# 7. INTRODUCTION

Xây dựng theo bảy nhịp:

1. Nhu cầu chuyển vibration data thành condition evidence.
2. Windows cùng nguồn không phải independent experiments.
3. Random-window split có nguy cơ leakage.
4. Sensor configuration đặt giới hạn thông tin cho model.
5. Văn liệu thường tập trung model hơn sensing design.
6. Research gap.
7. RQ và contributions.

Đóng góp phải gồm cặp method + result:

| Đóng góp phương pháp | Đóng góp kết quả cần kiểm chứng |
|---|---|
| Run-aware evaluation | Độ ổn định giữa independent groups |
| Leakage-safe processing | Hiệu năng trên unseen source groups |
| Common-fold sensor comparison | Mức ảnh hưởng của S1, S2, S1+S2 |
| Fair model comparison | Vai trò model family dưới từng sensor configuration |
| Group-level uncertainty | Kết quả có vượt empirical null hay không |
| Confusion analysis | Trạng thái và cặp trạng thái khó phân biệt |

Không viết kết quả như đã xảy ra.

---

# 8. RELATED WORK

Giữ bốn nhóm:

1. Controlled connection-state classification.
2. Leakage và group-aware evaluation.
3. Sensor-configuration và model-family comparison.
4. Small-group uncertainty và empirical-null analysis.

Tạo literature-gap matrix:

| Nghiên cứu | Liên quan khung thép/liên kết | Independent grouping | Leakage control | Sensor comparison | Common folds | Group-level uncertainty |
|---|---:|---:|---:|---:|---:|---:|

Metadata và DOI chưa kiểm chứng phải được đánh dấu:

> `[REFERENCE METADATA CHECK REQUIRED]`

---

# 9. EXPERIMENTAL PROGRAMME

## 9.1. Specimen

Mô tả:

- nominal scale;
- geometry;
- member sections;
- materials;
- boundary conditions;
- connections.

Không tuyên bố quantitative similitude khi chưa có hồ sơ kiểm chứng.

## 9.2. Controlled states

Tạo bảng:

### Bảng 1. Các trạng thái liên kết có kiểm soát

| Mã | Tên trạng thái | Vị trí liên kết | Cách tạo trạng thái | Cách xác nhận | Quy trình reset |
|---|---|---|---|---|---|
| H |  |  |  |  |  |
| A |  |  |  |  |  |
| BC |  |  |  |  |  |
| BR |  |  |  |  |  |

## 9.3. Excitation protocol

### Bảng 2. Thông số kích động và thu nhận

| Excitation_ID | Loại kích động | Vị trí tác động | Thời lượng | Số lần lặp | Ghi chú |
|---|---|---|---:|---:|---|
|  |  |  |  |  |  |

## 9.4. Sensors

### Bảng 3. Metadata cảm biến và kênh đo

| Sensor_ID | Model | Dải đo | Độ nhạy | Trục đo | Vị trí | Lắp đặt | Sampling rate | Đồng bộ |
|---|---|---|---|---|---|---|---:|---|
| S1 |  |  |  |  | Apex |  |  |  |
| S2 |  |  |  |  | Beam–column |  |  |  |

### Mô tả Hình 1 — Specimen và vị trí cảm biến

Không tạo hình.

Ghi rõ hình cuối cần có:

- ảnh hoặc bản vẽ specimen đã kiểm chứng;
- S1, S2;
- Apex, beam–column, brace connections;
- kích thước chính;
- chú thích trạng thái;
- không thể hiện thông tin chưa xác nhận.

---

# 10. RUN-AWARE EVALUATION METHOD

## 10.1. Independent unit

Không dùng cụm mơ hồ `run/replicate group`.

Tạo bảng quyết định:

### Bảng 4. Cấu trúc phân cấp dữ liệu và đơn vị độc lập

| Cấp | Định danh | Định nghĩa | Thành phần | Vai trò |
|---|---|---|---|---|
| File | File_ID |  |  | Lưu trữ |
| Recording | Recording_ID |  |  | Một lần thu tín hiệu |
| Independent group | Replicate_Group_ID hoặc tên đã khóa |  |  | Split và inference |
| Window | Window_ID |  |  | Derived observation |

Phải trả lời:

- một independent group chứa bao nhiêu recording;
- có đủ bốn state trong held-out group hay không;
- LORO hay LOGO;
- effective n là bao nhiêu.

Nếu chưa đủ bằng chứng, ghi:

> **Evidence is currently insufficient to lock the independent experimental unit.**

## 10.2. Windowing và preprocessing

### Bảng 5. Quy trình xử lý tín hiệu

| Bước | Thao tác | Tham số | Fixed hay learned | Fit trên training only? |
|---|---|---|---|---|
| Windowing |  |  | Fixed | N/A |
| Scaling |  |  | Learned |  |
| Feature extraction |  |  |  |  |
| Selection/reduction |  |  | Learned nếu có |  |

## 10.3. Aggregation rule

Tạo subsection bắt buộc:

```text
Window prediction
→ Recording-level prediction
→ Held-out-group evaluation
→ Evidence-quality profile
```

### Bảng 6. Quy tắc tổng hợp dự đoán

| Cấp | Đầu vào | Quy tắc tổng hợp | Đầu ra | Metric tính ở cấp này? |
|---|---|---|---|---|
| Window | Class probabilities |  | Window prediction |  |
| Recording | Nhiều windows |  | Recording prediction |  |
| Independent group | Nhiều recordings |  | Group-level result |  |

Không tự chọn majority vote hoặc mean probability nếu chưa có quyết định phương pháp.

## 10.4. Model roster

### Bảng 7. Cấu hình model

| Model | Input | Feature representation | Hyperparameters | Tuning budget | Seeds | Inclusion status |
|---|---|---|---|---|---|---|
| Logistic Regression |  |  |  |  |  |  |
| SVM |  |  |  |  |  |  |
| Random Forest |  |  |  |  |  |  |
| 1D-CNN |  |  |  |  |  |  |
| ResNet1D |  |  |  |  |  | PENDING / INCLUDE / EXCLUDE |

### ResNet1D

Sử dụng báo cáo SV IT để ghi nhận sơ bộ:

- residual blocks;
- Global Average Pooling;
- classifier ít tham số hơn 1D-CNN;
- AdamW và weight decay;
- nhận xét về overfitting;
- softmax và margin.

Nhưng chỉ INCLUDE khi xác minh:

- sensor mode;
- input channels;
- common folds;
- seeds;
- preprocessing;
- checkpoint hash;
- code version.

Không đưa nhận xét “ResNet tốt hơn CNN” vào Results trước final common-fold comparison.

## 10.5. Small independent n

Thêm subsection ngắn:

- báo cáo từng held-out group;
- ưu tiên median, range/IQR;
- không coi windows là independent n;
- không bootstrap individual windows;
- không dùng Wilcoxon/Friedman làm bằng chứng chính trên overlapping folds;
- statistical power thấp là limitation cấu trúc;
- empirical-null analysis không làm tăng số independent groups.

## 10.6. Permutation scheme

Không mặc định:

> permutation unit = complete group.

Tạo bảng:

### Bảng 8. Đặc tả empirical-null analysis

| Thành phần | Quyết định cuối |
|---|---|
| Đơn vị mang nhãn |  |
| Blocking factors |  |
| Hoán vị được phép |  |
| Statistic |  |
| Số permutations |  |
| Công thức empirical p-value |  |
| Có chạy lại full pipeline? |  |

Nếu independent group chứa nhiều state, phải dùng block-preserving permutation phù hợp.

### Mô tả Hình 2 — Run-aware evaluation pipeline

Chỉ mô tả hình:

```text
Locked independent-group registry
→ hold out complete group
→ segment training recordings
→ fit preprocessing on training groups
→ train/tune models
→ transform held-out group
→ aggregate recording-level predictions
→ calculate group-level evidence
```

---

# 11. RESULTS — GIỮ BẢNG TRỐNG

Không viết số liệu sơ bộ vào phần này.

## 11.1. Dataset summary

### Bảng 9. Tổng hợp dữ liệu cuối

| Chỉ tiêu | Giá trị cuối |
|---|---:|
| Số independent groups |  |
| Số recordings |  |
| Số state |  |
| Số excitation conditions |  |
| Số channels |  |
| Số groups bị loại |  |
| Window length |  |
| Overlap |  |
| Số windows |  |

## 11.2. Overall evidence quality

### Bảng 10. Hiệu năng theo held-out group

| Held-out group | Model | S1 macro-F1 | S2 macro-F1 | S1+S2 macro-F1 | Balanced accuracy | Ghi chú |
|---|---|---:|---:|---:|---:|---|
|  |  |  |  |  |  |  |
| Median |  |  |  |  |  |  |
| Range/IQR |  |  |  |  |  |  |

### Mô tả Hình 3 — Phân bố hiệu năng theo held-out group

Hình cuối nên:

- dùng dot plot hoặc connected-points plot;
- trục X là held-out group;
- trục Y là macro-F1;
- phân nhóm theo sensor configuration;
- chia panel theo model;
- không dùng bar chart làm hình chính.

## 11.3. Sensor-configuration effect

### Bảng 11. So sánh cấu hình cảm biến theo cặp

| Model | So sánh | Median difference | IQR/range | Số group cùng chiều | Effect-size description |
|---|---|---:|---|---:|---|
|  | S1+S2 − S1 |  |  |  |  |
|  | S1+S2 − S2 |  |  |  |  |
|  | S1 − S2 |  |  |  |  |

### Mô tả Hình 4 — Paired sensor-effect plot

- mỗi đường là một held-out group;
- ba điểm S1, S2, S1+S2;
- chia panel theo model;
- không đánh dấu trước cấu hình tốt nhất.

## 11.4. Model-family effect

### Bảng 12. So sánh model family

| Sensor configuration | Model | Median macro-F1 | Range/IQR | Stability rank | Ghi chú |
|---|---|---:|---|---|---|
|  |  |  |  |  |  |

Không kết luận model complexity bù được hay không trước khi có dữ liệu.

### Mô tả Hình 5 — Sensor effect và model effect

Dùng heatmap hoặc dot-range plot.

Không dùng line chart nối các model như một biến liên tục.

## 11.5. Per-class performance và confusion patterns

### Bảng 13. Chỉ tiêu theo từng trạng thái

| Model | Sensor config | State | Precision | Recall | F1 | Support |
|---|---|---|---:|---:|---:|---:|
|  |  | H |  |  |  |  |
|  |  | A |  |  |  |  |
|  |  | BC |  |  |  |  |
|  |  | BR |  |  |  |  |

### Bảng 14. Cặp nhầm lẫn chính

| Model | Sensor config | True state | Predicted state | Tỷ lệ/số lượng | Có lặp lại giữa groups? |
|---|---|---|---|---:|---|
|  |  |  |  |  |  |

### Mô tả Hình 6 — Confusion matrices

- cùng class order;
- cùng scale;
- báo cáo counts và row-normalized matrices;
- không cố định trước BC ↔ A;
- Supplementary chứa per-group matrices.

Mọi diễn giải cơ học:

> hypothesis, not confirmed.

## 11.6. Empirical-null và sensitivity

### Bảng 15. Empirical-null results

| Sensor/model analysis | Observed statistic | Null summary | Số permutations | Empirical p-value | Kết luận |
|---|---:|---:|---:|---:|---|
|  |  |  |  |  |  |

### Bảng 16. Sensitivity analyses

| Phân tích | Kết quả chính | Kết quả thay thế | Mức thay đổi | Kết luận có đổi không? |
|---|---:|---:|---:|---|
| Window overlap |  |  |  |  |
| Seed sensitivity |  |  |  |  |
| Exclusion of quality-flagged groups |  |  |  |  |

### Mô tả Hình 7 — Empirical-null distribution

- histogram/density của null statistics;
- đường observed statistic;
- số permutations;
- empirical p-value;
- ghi rõ permutation design.

---

# 12. DISCUSSION — VIẾT THEO NHÁNH KẾT QUẢ

## 12.1. Sensor configuration

Tạo bảng hướng dẫn:

| Kết quả cuối | Hướng viết |
|---|---|
| Dual sensor cải thiện rõ và nhất quán | Nêu marginal information gain có điều kiện |
| Dual sensor chỉ cải thiện một số state | Nhấn mạnh class-specific sensing benefit |
| Dual sensor không cải thiện đáng kể | Nêu redundancy hoặc insufficient added information |
| Một sensor đơn tốt hơn | Thảo luận vị trí đo và giới hạn specimen |
| Ranking thay đổi giữa groups | Nhấn mạnh uncertainty và không khuyến nghị phổ quát |

## 12.2. Model family

| Kết quả cuối | Hướng viết |
|---|---|
| RF tốt hơn deep models | Gắn với small-data regime, không khái quát |
| ResNet1D tốt hơn 1D-CNN | Thảo luận residual blocks, GAP, regularization; chỉ khi provenance đủ |
| Deep model tốt nhất | Chỉ kết luận trong protocol hiện tại |
| Ranking không ổn định | Nhấn mạnh group variability |
| Model effect nhỏ hơn sensor effect | Định lượng bằng estimand đã định nghĩa |
| Model effect lớn hơn sensor effect | Sửa narrative; không giữ claim cũ |

## 12.3. Confusion patterns

| Kết quả cuối | Hướng viết |
|---|---|
| A ↔ BC là cặp nhầm chính | Nêu open mechanical hypothesis |
| Cặp khác là chính | Viết theo dữ liệu thật |
| Confusion giảm khi thêm sensor | Nêu added spatial information |
| Confusion không giảm | Không khuyến nghị dual sensing |
| Pattern khác nhau giữa model | Không nói sensor effect độc lập model |

## 12.4. Practical implication

Chỉ viết khuyến nghị khi:

- effect đủ lớn;
- nhất quán giữa groups;
- state quan trọng được cải thiện;
- sensitivity analysis không đảo chiều.

Không dùng `optimal`.

---

# 13. LIMITATIONS

Giữ ngắn:

- one specimen;
- controlled categorical states;
- small independent n;
- excitation dependence;
- sensor hardware and mounting dependence;
- derived windows;
- no severity;
- no field diagnosis;
- no quantitative lab-to-field transfer;
- no calibrated FEM;
- external validity limited.

---

# 14. CONCLUSION — ĐỊNH HƯỚNG CÁCH VIẾT, KHÔNG ĐIỀN SỐ

Tạo một khung kết luận gồm sáu câu:

1. **Evidence quality:**  
   `[Nêu khả năng phân biệt và độ ổn định qua independent groups.]`

2. **Sensor configuration:**  
   `[Nêu cấu hình ảnh hưởng thế nào; tránh khuyến nghị phổ quát.]`

3. **Model family:**  
   `[Nêu model effect và mức ổn định của ranking.]`

4. **Confusion patterns:**  
   `[Nêu state/cặp state khó nhất theo dữ liệu thật.]`

5. **Empirical-null và robustness:**  
   `[Nêu kết quả có vượt empirical null và bền vững không.]`

6. **Practical implication và boundary:**  
   `[Nêu hàm ý cho monitoring design; laboratory evidence only.]`

Tạo thêm ma trận:

| Kịch bản kết quả | Câu kết luận phù hợp |
|---|---|
| Sensor effect rõ hơn model effect | “Under the present specimen and protocol…” |
| Sensor và model effect tương đương | Nhấn mạnh joint sensing–model design |
| Model effect rõ hơn sensor effect | Không giữ claim cũ về sensor dominance |
| Không có khác biệt ổn định | Định vị bài thành methodological case study |
| Performance không vượt empirical null | Không tuyên bố condition evidence đáng tin; thảo luận giới hạn dữ liệu |
| Một số state tốt, một số state yếu | Kết luận evidence có tính state-dependent |

Không đưa câu:

> Gate 1 is not yet closed

vào manuscript gửi tạp chí. Câu này chỉ nằm trong internal QA checklist.

---

# 15. OUTPUT PHẢI TẠO

1. `PAPER1_JOURNAL_OUTLINE_EMPTY_RESULTS_v3.docx`
2. `PAPER1_JOURNAL_OUTLINE_EMPTY_RESULTS_SOURCE_v3.md`
3. `PAPER1_INTERNAL_PRELIMINARY_EVIDENCE_NOTE_v3.md`
4. `PAPER1_TABLE_AND_FIGURE_SPECIFICATION_v3.docx`
5. `PAPER1_CONDITIONAL_DISCUSSION_AND_CONCLUSION_MATRIX_v3.docx`

Yêu cầu định dạng:

- tiếng Việt là ngôn ngữ chính;
- thuật ngữ chuyên môn có thể giữ tiếng Anh;
- bảng đánh số tuần tự theo thứ tự xuất hiện;
- hình đánh số tuần tự;
- không có số mock;
- không tạo ảnh giả;
- không ghi đè phiên bản cũ.

---

# 16. PHẢN HỒI ĐẦU TIÊN

Trong phản hồi đầu:

1. Xác nhận RQ1/WP1/Chương 4/Paper 1/Gate 1.
2. Xác nhận sử dụng Phương án A.
3. Xác nhận số liệu cũ và ResNet1D chỉ là preliminary internal evidence.
4. Liệt kê các bảng trống và hình mô tả sẽ tạo.
5. Không hỏi lại thông tin đã có.
6. Bắt đầu viết và xuất file ngay.

---

# 17. NGUYÊN TẮC CUỐI

- Dữ liệu thật dẫn dắt narrative.
- Không ép kết quả thật theo Paper 1 cũ.
- Không bịa metric, p-value hoặc effect size.
- Không dùng window count làm effective sample size.
- Không tuyên bố leakage inflation nếu chưa chạy contrast.
- Không đưa ResNet1D vào main results khi provenance chưa đủ.
- Không dùng softmax như calibrated probability.
- Không phục hồi DSI/severity.
- Không mở rộng Paper 1 sang FEM, field diagnosis hoặc Paper 2.
- Nếu kết quả cuối yếu, điều chỉnh claim thay vì che giấu.

Mọi phần Results và Discussion phải tuân theo:

```text
Final result
→ Evidence
→ Limitation
→ Conditional interpretation
→ Practical implication
```
