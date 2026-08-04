# HỒ SƠ TÓM TẮT ĐỂ NOTEBOOKLM ĐÁNH GIÁ PAPER 1/GATE 1 SO VỚI AVCI ET AL. (2021)

**Phiên bản:** 2026-07-27  
**Mục đích:** Cung cấp một hồ sơ tự chứa để NotebookLM đối chiếu hướng nghiên cứu hiện tại với bài tổng quan của Avci et al. (2021), nhận diện phần đã được literature hỗ trợ, khoảng trống có thể bảo vệ, rủi ro overclaim và các việc còn thiếu trước khi đóng G1/nộp Paper 1.

---

## 1. Tài liệu cần dùng trong NotebookLM

1. `Avci et al. - 2021 - A review of vibration-based damage detection in civil structures From traditional methods to Machine Learning and Deep Learning Applications.pdf`
2. `CAMPAIGN_AND_SENSOR_PAIR_REPORT.md`
3. `00_README_START_HERE_v2.2_UPDATED_20260720.md`
4. Các file governance, run registry, fold manifest, model results và Paper 1 outline nếu có.

### Thứ tự nguồn nội bộ ưu tiên

1. `MASTER_RESEARCH_CHARTER_v2.1_TRACEABILITY_CORE_20260719.md` hoặc Charter hiện hành tương đương;
2. `00_README_START_HERE_v2.2_UPDATED_20260720.md`;
3. `RQ_WP_CHAPTER_PAPER_GATE_MATRIX_v2.1.md`;
4. `EVIDENCE_GATES_v2.1.md`;
5. `RESEARCH_DIRECTION_AND_SCOPE.md`;
6. `RESEARCH_ARCHITECTURE.md`;
7. `CURRENT_STATUS_AND_NEXT_DIRECTION.md`;
8. Báo cáo và artefact riêng của Paper 1.

**Lưu ý quản trị:** README v2.2 là tài liệu vận hành cập nhật nhất, nhưng bộ governance chưa được đồng bộ hoàn toàn sang v2.2. Khi có mâu thuẫn, cần nêu rõ nguồn được ưu tiên và nội dung phải đồng bộ.

---

## 2. Định vị luận án hiện hành

### 2.1. Lĩnh vực và vấn đề nghiên cứu

Luận án thuộc **Quản lý xây dựng/Quản lý tài sản công trình**, phát triển một **data-informed Digital Twin framework** để tổ chức, truy vết và giới hạn cách sử dụng bằng chứng trạng thái từ dữ liệu rung đến cấu kiện BIM, hồ sơ kiểm tra và hành động quản lý có thể giải trình.

### 2.2. Chuỗi nghiên cứu đã khóa

```text
Vibration data
→ condition/state-change evidence + CEI
→ BIM-linked component
→ inspection record
→ justified and accountable inspection action
```

### 2.3. Chuỗi định danh hiện hành

```text
Sensor_ID
→ BIM_GUID
→ Condition_Evidence_ID
→ Inspection_Record_ID
→ Action_Record_ID
```

`Action_Status` là thuộc tính của `Action_Record_ID`, không phải một định danh độc lập.

### 2.4. CEI được hiểu thế nào

CEI là **confidence/evidence indicator** dưới dạng metadata của `Condition_Evidence_ID`, tối thiểu gồm:

- evidence validity status;
- model confidence;
- run/fold variability;
- sensor configuration;
- data-quality status;
- provenance;
- timestamp và version.

CEI **không phải** severity, Health Index, damage score hay ngưỡng tự động ra quyết định.

### 2.5. FEM

FEM chỉ được dùng ở mức:

> nominal, uncalibrated, reference-only, not used for damage diagnosis.

FEM không có RQ, WP, Paper hoặc Evidence Gate riêng.

---

## 3. RQ-WP-Chapter-Paper-Gate liên quan

| Thành phần | Nội dung |
|---|---|
| **RQ1** | Dữ liệu rung từ các cấu hình cảm biến khác nhau có thể tạo laboratory condition evidence đáng tin cậy đến đâu dưới giao thức run-aware và leakage-controlled? Hiệu ứng cấu hình cảm biến có giữ qua các model family hay không? |
| **WP1** | Laboratory evidence generation and validation |
| **Chương** | Chương 4 |
| **Paper** | Paper 1 - Sensors / laboratory condition evidence |
| **Gate** | G1 - Dataset integrity and run-aware evaluation |
| **Core Scope** | Run registry, sensor configuration, LORO, uncertainty, model provenance |
| **Supporting Scope** | So sánh traditional ML, compact 1D-CNN và ResNet1D trên cùng fold |
| **Ngoài phạm vi** | Field damage diagnosis, severity, RUL, predictive maintenance, calibrated FEM, lab-to-field classifier transfer |

### Working RQ nên giữ

> **Các cấu hình cảm biến khác nhau tạo laboratory condition evidence đáng tin cậy đến đâu dưới đánh giá theo run và kiểm soát rò rỉ dữ liệu; kết luận đó có ổn định qua campaign, session và model family hay không?**

Không nên ép Paper 1 phải chứng minh một mệnh đề tuyệt đối rằng “sensor configuration quan trọng hơn model architecture”. Model-family comparison nên là kiểm tra độ bền của kết luận, không phải cuộc thi tìm mô hình tốt nhất.

---

## 4. Thiết kế thí nghiệm và dữ liệu hiện có

### 4.1. Mô hình thí nghiệm

- Khung thép bu lông tỷ lệ 1:10.
- Bốn trạng thái liên kết có kiểm soát:
  - Healthy: tất cả liên kết được siết chặt;
  - B1: lỏng liên kết tại đỉnh;
  - B2: lỏng liên kết nút cột-dầm;
  - B3: lỏng liên kết giằng.
- Ba dạng kích động:
  - Beat L1;
  - Beat L2;
  - White Noise.
- Tần số lấy mẫu: 100 Hz cho dữ liệu PASCO được dùng trong báo cáo hiện tại.

B1/B2/B3 là **controlled connection states**, không phải các mức severity.

### 4.2. Hai campaign hiện có

| Nội dung | Campaign cũ | Campaign mới |
|---|---:|---:|
| File hợp lệ | 72/72 | 71/72 |
| Run | R1-R6 | R7-R12 |
| Số cảm biến | 2 | 3 |
| Vị trí | Apex, BeamColumn | Apex, BeamColumn, Brace |
| Median duration | khoảng 50,9 s | khoảng 70,9 s; White Noise khoảng 121 s |
| File thiếu | 0 | B1/Beat L1/R12 |
| File có dead channel | 36 | 0 |
| Trailing-gap files | 46 | 44 |
| Block permutations | 2/2 | 6/6 |
| Quantisation | 0,1 m/s² | 0,1 m/s² |

### 4.3. Sensor mapping

Người thực hiện thí nghiệm đã xác nhận:

- `U_AP` = Apex;
- `U_BC` = BeamColumn;
- `U_BR` = Brace.

Cần chính thức hóa trong registry:

```text
mapping_status = USER_CONFIRMED
mapping_evidence = experimenter confirmation
```

Nếu instrumentation log gốc không còn, phải ghi rõ đây là **retrospective reconstruction**, bổ sung ảnh bố trí, serial, hướng trục và ngày xác nhận.

---

## 5. Chất lượng dữ liệu và các vấn đề đã phát hiện

### 5.1. Dead channel ở campaign cũ

- Trục Y của cảm biến BeamColumn bị giữ ở giá trị không đổi trong 36/72 file.
- Đây nhiều khả năng là lỗi acquisition/kết nối/export hoặc channel freeze, không phải phản ứng kết cấu bằng 0.
- Cần audit theo `State × Run_ID × Excitation × Recording_Order × Block_Order`.
- Cần chạy sensitivity:
  1. giữ dữ liệu gốc;
  2. loại BeamColumn-Y khỏi toàn bộ campaign cũ;
  3. chỉ dùng common valid axes.

### 5.2. B3/session confounding ở campaign mới

- B3 chỉ được ghi trong session/ngày 21.07, còn Healthy/B1/B2 chủ yếu ở 22.07.
- B3 gần như hoàn hảo trong campaign mới nhưng không dễ ở campaign cũ.
- Vì vậy, B3 performance của campaign mới không thể quy hoàn toàn cho connection state.
- Phân tích bốn trạng thái ở campaign mới chỉ nên là exploratory.
- Phân tích same-session Healthy-B1-B2 là control bắt buộc.

### 5.3. Campaign shift

- Điểm số tuyệt đối và confusion pattern thay đổi giữa hai campaign.
- Prior audit ghi nhận khoảng 30% RMS shift và khoảng 1° fingerprint rotation sau remounting.
- Hai campaign không được pool để tăng số window.
- Chỉ rank-level và direction-level findings được xem là replicated.

### 5.4. Duration mismatch

White Noise ở campaign mới dài hơn Beat, nên có nhiều window hơn. Nếu chấm theo pooled windows, recording dài có trọng số lớn hơn.

Cần bổ sung:

- equal recording weighting;
- recording-level majority vote;
- mean probability/decision score theo recording;
- same-duration analysis, ví dụ central 50 s.

### 5.5. Quantisation

- Bước lượng tử 0,1 m/s² tương đối lớn so với RMS động của một số kênh.
- Đây là instrumentation limit có thể làm giảm khả năng phân biệt B1-B2.
- Không được đổ toàn bộ lỗi phân biệt cho mô hình.

### 5.6. File thiếu

- File B1/Beat L1/R12 vẫn để missing.
- Không nội suy, sao chép hoặc thu mới rồi gán lại là R12.
- Có thể thu campaign mới với Run_ID mới, nhưng không “bù” vào provenance cũ.

---

## 6. Pipeline phân tích hiện tại

1. Numeric coercion.
2. Loại trailing non-finite block; không impute.
3. Reorder sensor blocks theo canonical unit identity.
4. Per-recording, per-channel mean removal.
5. Không filtering trong main analysis.
6. Window 2 s, không overlap.
7. Split theo Run_ID trước windowing.
8. Z-score fit trên training windows của từng fold.
9. XYZ giữ nguyên theo sensor.
10. Input có dạng `batch × channels × time`; không nối sensor theo chiều thời gian.
11. Sáu fold Leave-One-Run-Out cho mỗi campaign.
12. Cùng fold manifest cho mọi sensor configuration trong cùng campaign.
13. Hai campaign không pool.

### Mô hình hiện tại

Fixed compact 1D-CNN:

```text
Conv1D(32,k7)-BN-ReLU-MaxPool
→ Conv1D(64,k5)-BN-ReLU-MaxPool
→ Conv1D(128,k3)-BN-ReLU
→ GAP
→ Dense(64)-ReLU-Dropout(0.3)
→ Dense(4)
```

Hiện báo cáo chính mới dùng seed 42.

---

## 7. Kết quả chính hiện có

### 7.1. Campaign cũ

| Cấu hình | Median macro-F1 | Worst-run | Std |
|---|---:|---:|---:|
| Apex + BeamColumn | 0,914 | 0,862 | 0,027 |
| Apex | 0,871 | 0,794 | 0,037 |
| BeamColumn | 0,695 | 0,643 | 0,039 |

### 7.2. Campaign mới

| Cấu hình | Median macro-F1 | Worst-run | Std |
|---|---:|---:|---:|
| Apex + BeamColumn + Brace | 0,923 | 0,895 | 0,015 |
| Apex + BeamColumn | 0,892 | 0,785 | 0,058 |
| Apex + Brace | 0,888 | 0,832 | 0,048 |
| Brace | 0,849 | 0,722 | 0,061 |
| BeamColumn + Brace | 0,829 | 0,667 | 0,078 |
| Apex | 0,817 | 0,786 | 0,031 |
| BeamColumn | 0,734 | 0,682 | 0,044 |

### 7.3. Cross-campaign replication

Ba cấu hình chung giữ cùng thứ hạng:

```text
Apex + BeamColumn > Apex > BeamColumn
```

Nhưng:

- điểm số tuyệt đối thay đổi;
- dominant confusion không tái lập;
- excitation tốt nhất không tái lập;
- B3 mới bị session-confounded.

### 7.4. Negative control

Label-shuffle control giảm về gần chance, hỗ trợ kết luận rằng pipeline LORO/split/windowing không có label leakage rõ ràng.

### 7.5. Cách diễn giải đúng

Kết quả hiện tại cho thấy:

> Trong điều kiện phòng thí nghiệm được kiểm soát, dữ liệu rung có thể tạo bằng chứng phân biệt trạng thái trên held-out runs; cấu hình cảm biến ảnh hưởng cả discriminability và run-level stability.

Không được diễn giải thành:

- chẩn đoán hư hỏng công trình thật;
- severity classification;
- optimal sensor placement;
- best model in general;
- field-ready classifier.

---

## 8. Đóng góp hiện tại của dữ liệu đối với Paper 1

### 8.1. Đóng góp phương pháp - chính

- split-before-windowing;
- LORO theo independent run;
- train-only preprocessing;
- common folds;
- negative control;
- báo cáo median, worst-run và fold variability thay vì chỉ pooled-window accuracy.

### 8.2. Đóng góp thực nghiệm - chính nhưng có điều kiện

- so sánh sensor configurations trên cùng fold;
- kiểm tra khả năng tái lập qua hai campaign;
- chỉ ra campaign/session là nuisance factors quan trọng;
- chỉ ra multi-sensor có thể cải thiện stability nhiều hơn headline accuracy.

### 8.3. Đóng góp thực tiễn - hỗ trợ

- tạo bằng chứng để lựa chọn cấu hình cảm biến tiết kiệm tài nguyên trong thí nghiệm tiếp theo;
- không được gọi một cấu hình là tối ưu tuyệt đối;
- Apex+BeamColumn mạnh hơn về median, trong khi Apex+Brace có thể mạnh hơn về worst-run robustness ở campaign mới.

---

## 9. Đóng góp đối với toàn luận án

Paper 1 không phải toàn bộ luận án. Vai trò của dữ liệu là tạo mắt xích đầu tiên:

```text
Vibration data
→ Condition_Evidence_ID + CEI
```

Sau G1, evidence phải có:

- Campaign_ID;
- Session_ID;
- Run_ID;
- Sensor configuration;
- model family/version;
- fold/seed;
- macro-F1, worst-run và uncertainty;
- data-quality flags;
- confound flags;
- provenance;
- Evidence_Context = LABORATORY_1_10;
- Quantitative_Transfer_Allowed = FALSE.

Paper 2 sau đó mới liên kết evidence với `BIM_GUID`, inspection record và accountable action record. Field feasibility tại Rapexco là một bối cảnh độc lập; không chuyển classifier hoặc threshold từ lab sang field.

---

## 10. Trạng thái Gate 1 hiện tại

### Đã đáp ứng tốt

- split-before-windowing;
- train-only preprocessing;
- LORO sáu fold;
- common folds trong từng campaign;
- run/fold uncertainty cơ bản;
- label-shuffle negative control;
- so sánh sensor configurations;
- hai campaign độc lập.

### Chưa hoàn tất

1. Dead-channel sensitivity.
2. Same-session Healthy-B1-B2 control.
3. Campaign xác nhận cân bằng session.
4. Traditional ML baselines trên cùng folds.
5. Multi-seed cho 1D-CNN.
6. ResNet1D sensor-mode/provenance audit.
7. Recording-level aggregation.
8. Paired run-level comparison và uncertainty.
9. Dataset hashes, locked run registry và acceptance matrix.

### Phán quyết hiện tại

> **G1 OPEN / READY FOR GATE REVIEW AFTER PRE-SUBMISSION ANALYSES; chưa chính thức CLOSED.**

Mọi kết quả định lượng hiện tại nên được gọi là:

> **Candidate claim pending Gate 1 closure.**

---

## 11. Kế hoạch Campaign 3 - confirmatory dataset

### Mục tiêu

Không phải tăng số window, mà:

- phá state-session alias;
- chuẩn hóa acquisition;
- kiểm tra session generalization;
- tạo dataset sạch để khóa G1.

### Thiết kế đề xuất

```text
2 sessions
× 4 states
× 3 excitations
× 3 independent runs
= 72 recordings
```

- Session 1: Healthy → B1 → B2 → B3.
- Session 2: Healthy → B3 → B2 → B1.
- Mỗi session có đủ bốn trạng thái.
- Mọi recording: 60 s, 100 Hz.
- Ba sensor cố định: Apex, BeamColumn, Brace.
- QC ngay sau từng recording.
- Không có trục constant/near-constant.
- Không đo B3 riêng session khác.

### Phân tích confirmatory

- LORO theo run;
- Leave-One-Session-Out;
- same-duration analysis;
- recording-level metrics;
- multi-seed;
- model-family comparison;
- pre-registered criteria.

Sau campaign này, nên dừng mở rộng thí nghiệm nếu QC đạt và chuyển trọng tâm sang đóng Paper 1/G1 và phát triển G2.

---

## 12. Model-family analyses còn phải chạy

Chạy trên cùng raw recordings, cùng window registry và fold manifest:

1. Logistic Regression hoặc SVM.
2. Random Forest.
3. Compact 1D-CNN.
4. ResNet1D, chỉ khi sensor mode và provenance được xác nhận.

### Mục tiêu so sánh

- Sensor-configuration effect có giữ qua model family không?
- Model nào ổn định hơn qua held-out run/session?
- Multi-sensor gain là median gain hay worst-run/stability gain?
- Deep learning có tạo giá trị rõ hơn traditional ML hay không?
- Không tuyên bố “best model” ngoài điều kiện thí nghiệm.

### ResNet1D audit bắt buộc

- input shape;
- sensor mode;
- cách tổ chức XYZ và nhiều sensor;
- split-before-windowing;
- train-only normalization;
- fold/seed/checkpoint provenance;
- không nối sensor theo chiều thời gian;
- không dùng test run để tuning.

Nếu provenance không đạt, loại ResNet1D khỏi primary results và ghi rõ lý do.

---

## 13. Các luận điểm trọng tâm từ Avci et al. (2021) cần NotebookLM kiểm tra

Avci et al. (2021) là bài tổng quan về vibration-based structural damage detection, chuyển từ phương pháp truyền thống sang ML và DL. Các điểm sơ bộ cần đối chiếu trực tiếp với bài gốc:

1. Nhiều phương pháp ML truyền thống phụ thuộc vào hand-crafted features và feature/classifier selection.
2. Không có đảm bảo một feature/classifier combination phù hợp cho mọi cấu trúc và damage scenario.
3. 1D CNN có thể học trực tiếp từ raw acceleration time histories và giảm nhu cầu manual feature extraction.
4. Compact 1D CNN được xem là phù hợp cho dedicated applications có lượng tín hiệu rung 1D hạn chế.
5. Supervised methods cần labeled damaged data, trong khi dữ liệu hư hỏng thực tế của công trình dân dụng rất hiếm.
6. Downscaled laboratory models được đề xuất như một nguồn simulated/experimental damage-scenario data.
7. Environmental/operational variability, generalization và sensor reliability là các thách thức quan trọng.
8. Unsupervised/semi-supervised approaches được đề xuất cho bối cảnh thiếu nhãn hiện trường.

Các điểm trên chủ yếu xuất hiện trong phần thảo luận DL và **Section 6 - Conclusions and recommendations for future work** của Avci et al.; NotebookLM phải trích dẫn đúng trang/đoạn của PDF, không chỉ dựa trên bản tóm tắt này.

### Giới hạn khi dùng Avci để tuyên bố novelty

- Avci là review xuất bản năm 2021 nhưng phạm vi lựa chọn bài ML/DL chủ yếu đến năm 2019.
- Avci có thể hỗ trợ nền tảng lý thuyết và research motivation.
- Avci **không đủ một mình** để chứng minh novelty hiện tại năm 2026.
- Không dùng Avci để viết “first study”, “no prior study” hoặc “literature has not addressed X” nếu chưa cập nhật literature 2020-2026.

---

## 14. Giả thuyết vị trí nghiên cứu so với Avci - cần NotebookLM kiểm chứng

### Phần phù hợp trực tiếp với Avci

- sử dụng raw acceleration time histories;
- compact 1D-CNN trong dedicated laboratory application;
- downscaled physical model để tạo labeled controlled-state data;
- so sánh traditional ML với DL;
- multi-sensor vibration evidence;
- thừa nhận supervised classifier không chuyển trực tiếp ra field.

### Phần có thể là giá trị bổ sung so với trọng tâm review của Avci

Đây chỉ là **candidate contribution**, phải được NotebookLM kiểm tra:

1. Đặt run là experimental unit và split trước windowing.
2. LORO/common-fold comparison giữa sensor configurations và model families.
3. Label-shuffle negative control để kiểm tra leakage.
4. Báo cáo worst-run, fold variability và seed uncertainty thay vì chỉ accuracy.
5. Replication qua independent campaigns và kiểm tra campaign/session confounding.
6. Xem sensor configuration là yếu tố quyết định reliability của evidence.
7. Biến kết quả ML thành `Condition_Evidence_ID` có provenance, CEI và context restriction.
8. Liên kết condition evidence với BIM-inspection-accountable action trong một luận án Quản lý xây dựng.

### Không được nhầm là novelty

- dùng CNN;
- dùng accelerometer;
- phân loại healthy/damaged states;
- dùng laboratory frame;
- dùng multi-sensor data;
- đạt accuracy/macro-F1 cao.

---

## 15. Yêu cầu NotebookLM đánh giá

Hãy dùng Avci et al. (2021) và toàn bộ hồ sơ nghiên cứu được cung cấp để trả lời các câu hỏi dưới đây. Mọi nhận định về Avci phải có trích dẫn trang/đoạn cụ thể.

### 15.1. Alignment với Avci

1. Hướng Paper 1 phù hợp với những kết luận và khuyến nghị nào của Avci?
2. Việc dùng compact 1D-CNN trên raw acceleration và khung laboratory 1:10 được Avci hỗ trợ đến đâu?
3. Việc thêm traditional ML baselines có cần thiết theo logic của Avci không?
4. Avci mô tả những hạn chế nào của supervised ML/DL mà nghiên cứu hiện tại phải thừa nhận?

### 15.2. Research gap và novelty

5. Avci có thảo luận rõ về run-aware splitting, window leakage, common folds, held-out-run uncertainty hoặc session confounding không?
6. Avci có đánh giá sensor configuration theo run-level reliability qua independent campaigns không?
7. Các mục sau là established knowledge, incremental contribution hay defensible methodological novelty?
   - split-before-windowing;
   - LORO;
   - label-shuffle control;
   - sensor-configuration comparison trên common folds;
   - campaign/session confound analysis;
   - recording/run-level evidence;
   - CEI-bearing traceability.
8. Research gap nào có thể bảo vệ chỉ từ Avci, và gap nào cần literature 2020-2026?
9. Paper 1 có đủ khác biệt với các nghiên cứu 1D-CNN được Avci review hay chỉ là một application mới?

### 15.3. Data and experiment quality

10. Hai campaign hiện tại cung cấp bằng chứng nào đủ mạnh và bằng chứng nào còn confounded?
11. Campaign 3 gồm hai session cân bằng có giải quyết đúng hạn chế mà Avci nêu về variability/generalization không?
12. Dead channel, quantisation, duration mismatch và remounting shift ảnh hưởng thế nào đến internal validity?
13. Cần giữ bốn trạng thái hay nên lấy same-session Healthy-B1-B2 làm primary analysis?
14. Các điều kiện tối thiểu để có thể gọi kết quả là replicated laboratory evidence là gì?

### 15.4. Model comparison

15. Traditional ML features nên được chọn thế nào để có comparison công bằng với compact 1D-CNN?
16. ResNet1D có cần thiết cho research question hay chỉ là supporting benchmark?
17. Cách trình bày model-family results nào tránh biến Paper 1 thành “best model competition”? 
18. Những metrics nào nên ưu tiên: median macro-F1, worst-run, balanced accuracy, recording-level metrics, seed variance hay confidence interval?

### 15.5. Scope and thesis contribution

19. Cách gọi `controlled connection-state evidence` có phù hợp và thận trọng hơn `damage diagnosis` không?
20. Avci có hỗ trợ hoặc mâu thuẫn với quyết định không chuyển classifier từ laboratory sang Rapexco?
21. Việc đưa provenance, CEI, BIM linkage và accountable inspection action có tạo khác biệt ngành Quản lý xây dựng rõ ràng không?
22. Paper 1 nên đóng góp gì để làm đầu vào đáng tin cậy cho Paper 2 mà không overclaim?

### 15.6. Publication readiness

23. Claim nào hiện đã đủ bằng chứng để đưa vào abstract?
24. Claim nào chỉ nên để trong Discussion hoặc Supplementary Materials?
25. Những phản biện lớn nhất một reviewer dựa trên Avci có thể đưa ra là gì?
26. Các phân tích bắt buộc trước khi nộp và các phân tích chỉ “nice to have” là gì?
27. Gate 1 hiện nên được đánh giá là `NOT READY`, `READY FOR GATE REVIEW`, `CONDITIONALLY CLOSED` hay `CLOSED`?

---

## 16. Định dạng đầu ra yêu cầu từ NotebookLM

### A. Executive verdict

Tối đa 300 từ, trả lời:

- Paper 1 có được Avci hỗ trợ về rationale không?
- Contribution hiện tại có vượt mức “application of 1D-CNN” không?
- Điều gì còn thiếu trước khi đóng G1?

### B. Ma trận so sánh

| Nội dung nghiên cứu hiện tại | Avci evidence/page | Mức phù hợp | Established / Incremental / Candidate novelty | Limitation | Next action |
|---|---|---|---|---|---|

### C. Claim audit

| Proposed claim | Evidence hiện có | Avci support | Risk of overclaim | Allowed wording | Prohibited wording |
|---|---|---|---|---|---|

### D. Gap assessment

Phân loại từng gap:

- Supported by Avci;
- Partially supported;
- Not addressed by Avci;
- Requires 2020-2026 literature search;
- Evidence is currently insufficient.

### E. Paper 1 contribution hierarchy

Xếp hạng:

1. Primary methodological contribution;
2. Primary empirical contribution;
3. Supporting practical contribution;
4. Không nên dùng làm contribution.

### F. Gate 1 verdict

Đánh giá từng tiêu chí:

- dataset integrity;
- run registry/provenance;
- leakage control;
- sensor configuration evidence;
- model-family robustness;
- multi-seed uncertainty;
- session/campaign generalization;
- recording-level evidence;
- claim discipline.

### G. Reading list từ Avci

Chọn tối đa 10 nghiên cứu gốc được Avci trích dẫn cần đọc kỹ nhất cho Paper 1, nêu:

- lý do chọn;
- liên quan tới sensor configuration/1D-CNN/multi-sensor/generalization;
- nghiên cứu hiện tại kế thừa gì;
- khác biệt gì;
- cần kiểm tra thêm gì trong bài gốc.

Không chỉ dựa vào cách Avci tóm tắt; ghi rõ cần đọc bài gốc trước khi dùng làm citation trực tiếp.

---

## 17. Allowed claims hiện tại

- Controlled laboratory connection states show separable vibration patterns on held-out runs under a leakage-controlled protocol.
- Sensor configuration affects both discriminability and run-level stability.
- The rank `Apex+BeamColumn > Apex > BeamColumn` reproduced across two campaigns under a fixed compact 1D-CNN.
- Multi-sensor inputs may improve worst-run reliability more consistently than headline median performance.
- Campaign and session effects can remain important even after window leakage is controlled.
- Laboratory evidence must carry provenance, uncertainty, data-quality and context-use restrictions before BIM/inspection linkage.

Mọi claim trên vẫn là **candidate claim pending Gate 1 closure**.

---

## 18. Prohibited claims

- Damage diagnosis in real structures.
- B1/B2/B3 as severity levels.
- Softmax score as damage probability or severity.
- Optimal sensor placement.
- Best model in general.
- Direct transfer of classifier/threshold to Cam Ranh or Rapexco.
- Calibrated FEM or stiffness-degradation inference.
- Predictive maintenance, RUL or autonomous maintenance.
- “First study” hoặc “no previous study” chỉ dựa trên Avci.
- Four-state replication in the new campaign without acknowledging B3/session alias.

---

## 19. Câu hỏi quyết định cuối cùng cho NotebookLM

> Dựa trên Avci et al. (2021) và bằng chứng hiện có, Paper 1 nên được định vị là một nghiên cứu application của compact 1D-CNN, một nghiên cứu về sensor-configuration reliability, hay một methodological study về leakage-safe run-aware laboratory condition evidence? Hãy chọn một định vị chính, giải thích bằng trích dẫn và đề xuất title/RQ/contribution phù hợp nhất nhưng không overclaim.

---

## 20. Phán quyết nội bộ trước khi NotebookLM đánh giá

### Claim

Hai campaign hiện tại đã cung cấp bằng chứng khá mạnh cho laboratory feasibility và sensor-configuration effect dưới LORO.

### Evidence

- kết quả trên held-out runs cao hơn chance;
- label-shuffle control đạt;
- thứ hạng ba cấu hình chung tái lập;
- multi-sensor nhìn chung cải thiện hiệu suất hoặc stability.

### Limitation

- B3/session alias;
- dead BeamColumn-Y ở campaign cũ;
- duration mismatch;
- quantisation;
- single seed;
- thiếu traditional ML và ResNet1D audit;
- chưa có confirmatory balanced-session dataset.

### Next action

1. Thực hiện Campaign 3 cân bằng hai session.
2. Chạy dead-channel và same-session sensitivity.
3. Chạy traditional ML, compact 1D-CNN và ResNet1D trên common folds.
4. Chạy multi-seed và recording/session-level evaluation.
5. Khóa registry, manifest, hashes, provenance và G1 acceptance matrix.
6. Sau đó tổ chức vòng đánh giá Gate 1 chính thức.

**Trạng thái hiện tại:** `G1 OPEN - strong candidate evidence, not formally closed.`
