# DANH MỤC BÀI HỘI THẢO HỖ TRỢ SC-1 ĐẾN SC-5

**Phiên bản:** v1.2  
**Ngày cập nhật:** 07/08/2026  
**Trạng thái:** TÀI LIỆU KIỂM SOÁT NỘI BỘ — SẴN SÀNG TRÌNH THẦY, CHƯA PHẢI PHÊ DUYỆT NỘP BÀI  
**Quan hệ với bản trước:** Tổng hợp SC-1–SC-3 từ kế hoạch v1.1 và bổ sung SC-4–SC-5.  
**Mục đích:** Lưu giữ các ý tưởng bài hội thảo hỗ trợ, tên bài đề xuất, mục tiêu, dữ liệu, phương pháp, điều kiện Go/No-Go và ma trận bảo vệ đóng góp lõi của luận án.

---

## 1. Vị trí trong kiến trúc luận án

Chuỗi nghiên cứu lõi đã khóa:

```text
Dữ liệu dao động
→ bằng chứng trạng thái/biến đổi trạng thái
→ cấu kiện liên kết BIM
→ hồ sơ kiểm tra
→ hỗ trợ hành động kiểm tra – bảo trì
```

Chuỗi định danh lõi:

```text
Sensor_ID → BIM_GUID → Condition_Evidence_ID → Inspection_Record_ID → Action_Status
```

Các bài SC-1–SC-5 đều thuộc **Supporting Scope**. Không bài nào:

- mở RQ, WP, chương, Paper lõi hoặc Evidence Gate riêng;
- được dùng để tuyên bố đã đóng G1, G2, G3 hoặc G4;
- được ưu tiên cao hơn việc khóa Gate 1;
- được thay đổi kiến trúc Limited-FEM đã được chấp thuận.

**Evidence Gate hiện tại:** Gate 1.  
**Nút chặn bắt buộc:** khóa run registry → đánh giá run-aware/LORO chống rò rỉ → xác nhận sensor mode của ResNet1D → khóa Paper 1.

---

## 2. Danh mục tổng hợp

| Mã | Tên bài đề xuất | Mục tiêu chính | Dữ liệu | Quan hệ với luận án | Trạng thái |
|---|---|---|---|---|---|
| **SC-1** | **Đánh giá sự tương hợp và chất lượng dữ liệu của phép đo PASCO–ADXL đồng bộ trên mô hình khung thép tỷ lệ** | Định lượng mức tương hợp giữa hai hệ đo trong miền thời gian và tần số | 36 cặp PASCO–ADXL đồng bộ; các file khỏe bổ sung chỉ dùng phân tích nhạy nếu điều kiện khác được tách riêng | Tiếp giáp RQ1/WP1/C4/Paper 1/G1 | **GO có điều kiện** |
| **SC-2** | **Tối ưu siêu tham số 1D-CNN có kiểm soát ngân sách tính toán cho phân loại dao động kết cấu** | So sánh hiệu năng–chi phí của các chiến lược HPO dưới cùng ngân sách | Benchmark công khai hoặc bộ dữ liệu đề tài phụ, tuyệt đối không dùng Campaign 1–3 | Nghiên cứu phương pháp AI độc lập; không ánh xạ RQ/WP/Gate | **GO có điều kiện; firewall sạch nhất** |
| **SC-3** | **Ánh xạ yêu cầu quản lý thông tin BIM phục vụ vận hành và bảo trì từ TCVN 14177 và ISO 19650 sang IFC** | Chuyển yêu cầu thông tin tài sản tĩnh đã kiểm chứng thành trường IFC/hồ sơ ngoài IFC và quy tắc kiểm tra | Văn bản tiêu chuẩn chính thức + mô hình Revit/IFC + tập cấu kiện pilot | Tiếp giáp RQ2/WP2/C5/Paper 2/G2 | **GO có điều kiện** |
| **SC-4** | **Từ đầu ra AI/SHM đến hồ sơ kiểm tra liên kết BIM: nghiên cứu ánh xạ hệ thống về chuyển giao thông tin** | Lập bản đồ bằng chứng và taxonomy về information handover từ đầu ra SHM/AI đến BIM, hồ sơ kiểm tra và bảo trì | Corpus văn liệu tái lập được; Scopus/WoS và snowballing | Cầu nối học thuật giữa WP1 và WP2; hỗ trợ C2/C5 | **DỰ PHÒNG — GO chỉ sau pilot search** |
| **SC-5** | **Đánh giá độ lặp lại theo run và độ ổn định giữa các campaign của dữ liệu dao động trạng thái khỏe trên mô hình khung thép 1:10** | Định lượng biến thiên tự nhiên của phép đo S0 giữa run và campaign trước khi diễn giải kết quả AI | PASCO, S0–Healthy, Campaign 1–3; tối đa 54 recording nếu registry xác nhận | Tiếp giáp RQ1/WP1/C4/Paper 1/G1 | **GO có điều kiện; rủi ro xâm phạm Paper 1 cao nhất** |

**Lưu ý chiến lược:** Danh mục này là kho ý tưởng có kiểm soát, không phải cam kết nộp đủ năm bài. SC-4 và SC-5 chỉ được kích hoạt nếu pilot tạo đóng góp độc lập và không làm chậm Paper 1/Paper 2.

---

## 3. SC-1 — Tương hợp phép đo PASCO–ADXL

### 3.1 Tên đề xuất

**Tiếng Việt:** Đánh giá sự tương hợp và chất lượng dữ liệu của phép đo PASCO–ADXL đồng bộ trên mô hình khung thép tỷ lệ.  
**Tiếng Anh:** *Cross-Sensor Agreement and Data-Quality Assessment of Synchronized PASCO and ADXL Measurements on a Scaled Steel Frame.*

### 3.2 Mục tiêu

Định lượng mức tương hợp giữa hai hệ đo trong dải tần chung hợp lệ; nhận diện sai khác có hệ thống do tần số lấy mẫu, độ trễ, giá trị thiếu, kênh phẳng, bão hòa và chất lượng phổ.

### 3.3 Định vị

| Hạng mục | Quyết định |
|---|---|
| RQ liên quan | Tiếp giáp RQ1; không trả lời khả năng phân loại trạng thái |
| WP/Chương/Paper | WP1/C4/Paper 1 — Supporting Scope |
| Gate | Tiếp giáp G1; không phải điều kiện đóng G1 |
| Đơn vị phân tích | Một cặp PASCO–ADXL đo đồng bộ, cùng vị trí/trục và đoạn thời gian hợp lệ |

### 3.4 Claim → Evidence → Limitation → Next action

**Claim.** Trong cùng khoảng thời gian và dải tần hợp lệ, PASCO và ADXL có mức tương hợp đo được; khác biệt giữa hai hệ có thể được định lượng bằng chỉ số chất lượng tín hiệu và phổ.

**Evidence.** Hồ sơ hiện có nêu 36 cặp đo đồng bộ: 4 trạng thái × 3 kích thích × 3 run. Con số và tính đồng bộ chỉ được công bố sau khi paired-file registry xác nhận file, timestamp, vị trí, trục, sampling rate và valid interval. Các cặp Healthy thu khác ngày/vị trí không được gộp vào phân tích chính; chỉ được dùng như phân tích nhạy tách biệt nếu metadata đủ.

**Limitation.** Kết quả chỉ áp dụng cho thiết bị, cách gá, khung, kích thích và dải tần đã thử; không chứng minh hai hệ thay thế nhau phổ quát, không chứng minh hiệu quả hiện trường hoặc khả năng chẩn đoán.

**Next action.** Khóa `PASCO_ADXL_PAIR_REGISTRY` trước phân tích cuối.

### 3.5 Dữ liệu và phương pháp tối thiểu

- Cắt đoạn hợp lệ chung; NaN cuối file PASCO được xem là giới hạn xuất dữ liệu, không tự động coi là lỗi đo.
- Ước lượng độ trễ và báo cáo rõ cách căn chỉnh.
- Lọc chống aliasing trước khi đưa về dải tần chung.
- Chỉ số chính: valid duration, missing/flat/clipping; cross-correlation lag; normalized waveform agreement; dominant-frequency difference; PSD similarity; coherence trong điều kiện phù hợp.
- Báo cáo theo cặp/run và độ biến thiên; nhãn S0/B1/B2/B3 chỉ dùng phân tầng mô tả, không dùng làm biến đích.

### 3.6 Firewall

Không phân loại S0/B1/B2/B3; không LORO/LOCO/random split; không RF/SVM/1D-CNN/ResNet1D; không xếp hạng vị trí/cấu hình cảm biến; không CEI; không Autoencoder hiện trường.

### 3.7 Go / No-Go

**GO:** cặp đo, vị trí, trục, sampling rate và valid interval được xác nhận; Paper 1 đã khóa bảng–hình và phạm vi kết quả.  
**NO-GO:** không khôi phục được tính đồng bộ/đồng vị trí, hoặc đóng góp chính chỉ xuất hiện khi đưa bài toán phân loại vào.

---

## 4. SC-2 — HPO theo ngân sách tính toán trên dữ liệu độc lập

### 4.1 Tên đề xuất

**Tiếng Việt:** Tối ưu siêu tham số 1D-CNN có kiểm soát ngân sách tính toán cho phân loại dao động kết cấu: nghiên cứu so sánh công bằng.  
**Tiếng Anh:** *Compute-Budget-Aware Hyperparameter Optimization for 1D-CNN-Based Structural Vibration Classification: A Fair Comparative Study.*

### 4.2 Mục tiêu

So sánh các chiến lược HPO, dự kiến gồm Random Search, GWO và SAFCA, dưới cùng số lần đánh giá hàm mục tiêu; đánh giá đồng thời macro-F1, độ ổn định, tốc độ hội tụ và chi phí tính toán.

### 4.3 Định vị

| Hạng mục | Quyết định |
|---|---|
| RQ/WP/Chương/Gate | Không có; nghiên cứu phương pháp AI độc lập |
| Paper lõi | Không tạo evidence cho Paper 1 |
| Đơn vị phân tích | Một lần HPO hoàn chỉnh trong một outer fold và một seed |
| Dữ liệu | Benchmark công khai hoặc dữ liệu của hướng phụ, có quyền sử dụng và cấu trúc nhóm rõ |

### 4.4 Claim → Evidence → Limitation → Next action

**Claim.** Dưới cùng ngân sách tìm kiếm, các chiến lược HPO khác nhau về hiệu năng ngoài mẫu, độ ổn định, đường hội tụ và chi phí.

**Evidence.** Nested group-aware evaluation, nhiều seed, cùng preprocessing, mô hình, early stopping, search space và số lần đánh giá hàm mục tiêu.

**Limitation.** Kết luận phụ thuộc dataset, search space, budget, protocol và phần cứng; không chứng minh một HPO vượt trội phổ quát và không chuyển kết quả sang dữ liệu luận án.

**Next action.** Chọn dataset độc lập và lập phiếu provenance/quyền sử dụng/đơn vị nhóm trước khi chạy.

### 4.5 Dữ liệu và phương pháp tối thiểu

- Khóa dataset, nhãn, đơn vị nhóm, search space và compute budget.
- Dùng nested group-aware evaluation khi có run/specimen/subject tự nhiên.
- Metric chính: macro-F1 outer test; metric phụ: độ biến thiên, convergence, failed trials, wall-clock/accelerator time.
- Lặp nhiều seed; lưu trial log và cấu hình cuối.
- Phân biệt rõ LORO và LOCO nếu dataset có cả run và campaign; không dùng hai thuật ngữ thay thế nhau.

### 4.6 Firewall

Tuyệt đối không dùng Campaign 1–3, window dẫn xuất, run registry, cấu hình cảm biến, LORO, CEI hoặc metric Paper 1. Không gắn claim BIM, Digital Twin hay Quản lý xây dựng nếu dữ liệu và câu hỏi không liên quan.

### 4.7 Go / No-Go

**GO:** dataset độc lập, quyền sử dụng rõ, nhóm dữ liệu đủ cho đánh giá hợp lệ, budget chung đã khóa.  
**NO-GO:** phải dùng dữ liệu luận án; các HPO không cùng ngân sách; kết quả dựa vào seed tốt nhất hoặc metadata nhóm không rõ.

---

## 5. SC-3 — TCVN 14177, ISO 19650 và IFC

### 5.1 Tên đề xuất

**Tiếng Việt:** Ánh xạ yêu cầu quản lý thông tin BIM phục vụ vận hành và bảo trì công trình: từ TCVN 14177 và ISO 19650 đến thuộc tính IFC.  
**Tiếng Anh:** *From BIM Information-Management Requirements to IFC Properties for Building Operation and Maintenance: A Validation-Oriented Mapping.*

Tên ngắn cho hội thảo trong nước:

> **Khung ánh xạ yêu cầu thông tin tài sản phục vụ bảo trì công trình theo TCVN 14177 và ISO 19650.**

### 5.2 Mục tiêu

Chuyển một tập yêu cầu thông tin tài sản tĩnh đã kiểm chứng đến cấp điều khoản thành ma trận `Requirement → IFC field/external record → validation rule`, sau đó pilot vòng Revit–IFC trên tập cấu kiện cố định.

### 5.3 Định vị

| Hạng mục | Quyết định |
|---|---|
| RQ liên quan | Tiếp giáp RQ2; không trả lời evidence-to-inspection traceability |
| WP/Chương/Paper | WP2/C5/Paper 2 — Supporting Scope |
| Gate | Tiếp giáp G2; không mở hoặc đóng G2–G3 |
| Đơn vị phân tích | Một yêu cầu thông tin đã kiểm chứng và ánh xạ triển khai tương ứng |

### 5.4 Claim → Evidence → Limitation → Next action

**Claim.** Một tập yêu cầu thông tin tài sản tĩnh có thể được ánh xạ sang IFC hoặc hồ sơ ngoài IFC và kiểm tra bằng quy tắc tái lập được.

**Evidence.** Bảng bằng chứng điều khoản từ văn bản chính thức; ma trận Requirement–Field–Rule; thử nghiệm sự hiện diện, kiểu dữ liệu, tính duy nhất và khả năng giữ giá trị sau vòng Revit–IFC.

**Limitation.** Chỉ chứng minh ánh xạ giới hạn; không chứng minh AIM đầy đủ, tuân thủ toàn bộ tiêu chuẩn, Digital Twin vận hành hoặc truy vết inspection–action.

**Next action.** Thu thập văn bản chính thức của TCVN 14177-1/-2:2024 và phần ISO 19650 được chọn; khóa clause-evidence table trước danh sách trường. **Evidence is currently insufficient** để gọi bất kỳ trường nào là “bắt buộc theo TCVN/ISO” nếu chưa có neo điều khoản.

### 5.5 Ma trận dữ liệu bắt buộc

`Requirement_ID; Source_Clause; Requirement_Text; Required_Optional_Conditional; Asset_Field; IFC_Representation; External_Record; Data_Type; Allowed_Value; Validation_Rule; Pilot_Result`.

### 5.6 Phương pháp tối thiểu

- Phân tích tiêu chuẩn đến cấp điều khoản; không diễn giải từ tài liệu thứ cấp thay cho văn bản chính thức.
- Chọn tập con thông tin tài sản tĩnh có chủ ý.
- Khai báo trước validation rules.
- Pilot trên tập cấu kiện cố định; báo cáo Pass / Limitation / Fail.
- Cách diễn đạt ưu tiên: “phù hợp với tập yêu cầu đã kiểm chứng được lựa chọn cho nghiên cứu”, không dùng “AIM tuân thủ đầy đủ”.

### 5.7 Firewall

Không dùng `Sensor_ID`, `Condition_Evidence_ID`, `Inspection_Record_ID`, `Action_Status`, `Status_Event_ID`; không schema truy vết động; không competency questions; không truy vấn hai chiều; không quyền hạn/xác nhận/đóng hồ sơ; không dữ liệu Rapexco.

### 5.8 Go / No-Go

**GO:** có văn bản nguồn chính thức, neo điều khoản, tập trường tĩnh và pilot tách khỏi Paper 2.  
**NO-GO:** claim phải dựa vào chuỗi truy vết động, competency questions hoặc không kiểm chứng được tiêu chuẩn.

---

## 6. SC-4 — Systematic mapping về information handover

### 6.1 Tên đề xuất

**Tiếng Việt:** Từ đầu ra AI/SHM đến hồ sơ kiểm tra liên kết BIM: nghiên cứu ánh xạ hệ thống về chuyển giao thông tin trong bảo trì công trình.  
**Tiếng Anh:** *From AI/SHM Outputs to BIM-Linked Inspection Records: A Systematic Mapping of Information Handover in Structural Maintenance.*

### 6.2 Mục tiêu

Lập bản đồ có hệ thống về cách đầu ra phân tích SHM/AI được liên kết với đối tượng BIM, hồ sơ kiểm tra, yêu cầu công việc hoặc hành động bảo trì; xác định loại thông tin nguồn gốc và mức truy hồi ngược đã được văn liệu báo cáo.

### 6.3 Định vị

| Hạng mục | Quyết định |
|---|---|
| RQ liên quan | Không có RQ riêng; hỗ trợ lập luận khoảng trống của RQ2 |
| WP/Chương | Cầu nối WP1→WP2; hỗ trợ C2 và nền phương pháp C5 |
| Paper/Gate | Không thay Paper 1/Paper 2; không có Gate riêng |
| Đơn vị phân tích | Một nghiên cứu có mô tả đường chuyển giao từ đầu ra phân tích đến điểm đến nghiệp vụ |

### 6.4 Claim → Evidence → Limitation → Next action

**Claim dự kiến.** Văn liệu tích hợp SHM/AI–BIM chưa mô tả nhất quán việc chuyển giao đầu ra phân tích thành thông tin có thể dùng trong hồ sơ kiểm tra–bảo trì.

**Evidence.** Corpus tái lập được từ Scopus/WoS, sàng lọc theo protocol, snowballing và data-extraction matrix. Các bài đã deep-read chỉ là seed corpus.

**Limitation.** Bài chỉ mô tả và phân loại văn liệu; không đề xuất schema mới, không kiểm chứng traceability, không tạo dữ liệu định lượng thí nghiệm và không giải quyết khoảng trống của Paper 2.

**Next action.** Pilot search 30–50 kết quả. **Evidence is currently insufficient** để khẳng định tính mới cho tới khi chứng minh đơn vị phân tích “information handover” khác các tổng quan BIM–SHM/Digital Twin gần đây.

### 6.5 Dữ liệu và phương pháp tối thiểu

- File quản trị: `SC4_SEARCH_LOG`, `SC4_SCREENING_MATRIX`, `SC4_INCLUDED_STUDIES`, `SC4_EXCLUSION_REASONS`, `SC4_DATA_EXTRACTION_MATRIX`.
- Trường mã hóa: Study_ID/DOI/năm/loại công trình; nguồn đầu vào; đầu ra AI/SHM; điểm liên kết BIM; điểm đến nghiệp vụ; timestamp/identifier/model version/user confirmation; mức kiểm chứng; hướng liên kết một chiều/hai chiều.
- Protocol trước tìm kiếm; PRISMA 2020 và nguyên tắc systematic mapping; không meta-analysis.
- Ít nhất 20–25% mẫu được người thứ hai kiểm tra; AI chỉ hỗ trợ, không thay quyết định học thuật.

### 6.6 Firewall

Không dùng dữ liệu/metric/LORO/CEI của Paper 1; không đề xuất chuỗi định danh, schema, competency questions, round-trip test hoặc action lifecycle của Paper 2; không ánh xạ TCVN/ISO sang IFC như SC-3; không dữ liệu Rapexco.

### 6.7 Go / No-Go

**GO:** pilot xác nhận khoảng trống “information handover” riêng biệt, corpus đủ và protocol có thể tái lập.  
**NO-GO:** kết quả chỉ lặp lại tổng quan BIM–SHM/DT chung; cần dùng schema của Paper 2 để tạo tính mới; hoặc khối lượng làm chậm G1/G2.

---

## 7. SC-5 — Độ lặp lại và ổn định của dữ liệu Healthy

### 7.1 Tên đề xuất

**Tiếng Việt:** Đánh giá độ lặp lại theo run và độ ổn định giữa các campaign của dữ liệu dao động trạng thái khỏe trên mô hình khung thép tỷ lệ 1:10.  
**Tiếng Anh:** *Run-Level Repeatability and Between-Campaign Stability of Healthy-State Vibration Measurements on a 1:10 Scaled Steel Frame.*

### 7.2 Mục tiêu

Định lượng biến thiên tự nhiên của dữ liệu S0–Healthy trong cùng campaign và độ dịch chuyển giữa các campaign, từ đó mô tả giới hạn ổn định của phép đo trước khi diễn giải kết quả AI.

### 7.3 Định vị

| Hạng mục | Quyết định |
|---|---|
| RQ liên quan | Tiếp giáp RQ1; không trả lời khả năng phân loại S0/B1/B2/B3 |
| WP/Chương/Paper | WP1/C4/Paper 1 — Supporting Scope |
| Gate | Tiếp giáp G1; không phải điều kiện đóng G1 |
| Đơn vị phân tích | Một run S0 hợp lệ dưới một campaign, kích thích, sensor và trục xác định |

### 7.4 Claim → Evidence → Limitation → Next action

**Claim.** Mức biến thiên trong cùng campaign và mức dịch chuyển giữa campaign của dữ liệu Healthy có thể được định lượng ở cấp run, giúp phân biệt biến thiên phép đo tự nhiên với thay đổi do điều kiện thu nhận.

**Evidence.** Dữ liệu PASCO S0 từ Campaign 1–3, ba kích thích và tối đa sáu run/tổ hợp, tương đương tối đa 54 recording nếu run registry xác nhận đầy đủ và điều kiện lắp đặt tương đương.

**Limitation.** Chỉ ba campaign nên phân tích between-campaign mang tính thăm dò; không phải hiệu chuẩn thiết bị, không suy rộng sang công trình thực, không chẩn đoán và không chứng minh độ ổn định dài hạn.

**Next action.** Khóa `SC5_HEALTHY_RUN_REGISTRY` và audit sự tương đương về cảm biến, vị trí, trục, kích thích, valid interval và mounting status.

### 7.5 Dữ liệu và phương pháp tối thiểu

- Chỉ PASCO và S0–Healthy; không gộp ADXL vì thuộc SC-1.
- Registry: `File_ID; Campaign_ID; Run_ID; Excitation; Sensor_ID; Axis; Sampling_Rate; Valid_Interval; Mounting_Status; QC_Flag; File_Hash`.
- Đặc trưng cấp run: valid-sample ratio, flat/clipping, RMS, standard deviation, peak-to-peak, crest factor, dominant frequency, spectral centroid, band energy, PSD similarity/distance.
- Báo cáo median, IQR, robust coefficient of variation, within-cell repeatability spread, between-campaign median shift và hierarchical bootstrap 95% CI theo run.
- Có thể dùng phân rã phương sai hoặc mô hình hỗn hợp như phân tích bổ sung nếu cấu trúc dữ liệu đủ; không dựa kết luận vào p-value khi chỉ có ba campaign.
- Không coi các window chồng lấn là quan sát độc lập; không dùng coherence giữa các run không đồng bộ pha.

### 7.6 Firewall

Không B1/B2/B3; không classification; không random split/LORO/LOCO; không RF/SVM/CNN/ResNet1D; không accuracy/macro-F1/confusion matrix; không xếp hạng cấu hình cảm biến; không CEI/Condition_Evidence_ID; không chuyển thành baseline Rapexco.

### 7.7 Go / No-Go

**GO:** Paper 1 đã khóa kết quả và bảng–hình; ba campaign được xác nhận; có đủ run hợp lệ; điều kiện lắp đặt và kích thích truy vết được.  
**NO-GO:** mapping Campaign 1–2 còn không ổn định; thay đổi gá/hướng trục không kiểm soát; chỉ còn một campaign; hoặc kết quả chỉ có ý nghĩa khi thêm B1–B3/phân loại.

---

## 8. Ma trận sở hữu tài sản nghiên cứu

Ký hiệu: **Lõi** = tài sản dành riêng cho Paper lõi; **Chính** = đóng góp riêng của bài SC; **Có điều kiện** = chỉ dùng theo firewall và khai báo; **Loại trừ** = không được dùng; **Bối cảnh** = chỉ dùng để định vị.

| Tài sản/dữ liệu/phương pháp | Chủ sở hữu ưu tiên | SC-1 | SC-2 | SC-3 | SC-4 | SC-5 |
|---|---|---|---|---|---|---|
| Campaign 1–3 và run registry lõi | Paper 1 | Có điều kiện: paired subset | Loại trừ | Loại trừ | Loại trừ | Có điều kiện: S0 subset |
| Phân loại S0/B1/B2/B3 | Paper 1 | Loại trừ | Loại trừ | Loại trừ | Loại trừ | Loại trừ |
| Random split vs run-aware/LORO | Paper 1 | Loại trừ | Loại trừ | Loại trừ | Loại trừ | Loại trừ |
| So sánh/xếp hạng cấu hình cảm biến | Paper 1 | Loại trừ | Loại trừ | Loại trừ | Loại trừ | Loại trừ |
| RF/CNN/ResNet1D và metric phân loại | Paper 1 | Loại trừ | Loại trừ trên dữ liệu luận án | Loại trừ | Loại trừ | Loại trừ |
| CEI/bằng chứng trạng thái đầu ra | Paper 1 → Paper 2 | Loại trừ | Loại trừ | Loại trừ | Loại trừ | Loại trừ |
| Tương hợp PASCO–ADXL | SC-1 | **Chính** | — | — | — | Loại trừ |
| HPO hiệu năng–chi phí trên dữ liệu độc lập | SC-2 | — | **Chính** | — | — | — |
| Requirement-to-IFC cho thông tin tài sản tĩnh | SC-3 | — | — | **Chính** | Bối cảnh; không tái tạo ma trận | — |
| Taxonomy information handover trong văn liệu | SC-4 | — | — | Bối cảnh | **Chính** | — |
| Độ lặp lại S0 theo run/campaign | SC-5 | Loại trừ | — | — | — | **Chính** |
| Schema `Sensor_ID→…→Action_Status` | Paper 2 | Loại trừ | Loại trừ | Loại trừ | Loại trừ | Loại trừ |
| Competency questions, truy vết hai chiều, round-trip | Paper 2 | Loại trừ | Loại trừ | Loại trừ | Loại trừ | Loại trừ |
| Inspection/action lifecycle và quyền hạn hồ sơ | Paper 2/Paper 3 | Loại trừ | Loại trừ | Loại trừ | Loại trừ | Loại trừ |
| Baseline hiện trường và Rapexco | Paper 3 | Loại trừ | Loại trừ | Loại trừ | Loại trừ | Loại trừ |
| Logic Normal→Watch→Inspect→Priority Inspection | WP4/Paper 3–4 | Loại trừ | Loại trừ | Loại trừ | Loại trừ | Loại trừ |

---

## 9. Ma trận xâm phạm đối với các Paper lõi

Thang đánh giá: **Thấp** = độc lập rõ; **Trung bình** = tiếp giáp dữ liệu/chủ đề, cần firewall; **Cao** = dùng tài sản cùng nguồn, chỉ được làm sau khi Paper lõi khóa.

| Bài hỗ trợ | Paper 1 / G1 | Paper 2 / G2–G3 | Paper 3 / G4 | Nguyên nhân chính | Kiểm soát bắt buộc |
|---|---:|---:|---:|---|---|
| **SC-1** | **Trung bình** | Thấp | Thấp | Dùng một phần phiên đo liên quan WP1 | Chỉ sensor agreement; không phân loại/LORO; Paper 1 khóa trước |
| **SC-2** | Thấp | Thấp | Thấp | Dữ liệu và câu hỏi độc lập | Cấm Campaign 1–3; khai báo dataset và quyền sử dụng |
| **SC-3** | Thấp | **Trung bình** | Thấp | Tiếp giáp quản lý thông tin và IFC | Chỉ asset information tĩnh; cấm schema/CQ/inspection-action |
| **SC-4** | Thấp | **Trung bình** | Thấp | Có thể công bố trước khoảng trống và taxonomy của Paper 2 | Chỉ mapping văn liệu; không đề xuất giải pháp/schema; pilot novelty trước |
| **SC-5** | **Cao** | Thấp | Thấp | Dùng S0 của Campaign 1–3 và metadata run/campaign | Paper 1 sở hữu ưu tiên; chỉ Healthy repeatability; khóa Paper 1 trước; disclosure đầy đủ |

### 9.1 Ma trận xâm phạm giữa các bài SC

| Cặp bài | Rủi ro | Điểm giao nhau | Firewall |
|---|---:|---|---|
| SC-1 ↔ SC-5 | Trung bình | Cùng bối cảnh lab và có thể cùng file PASCO Healthy | SC-1 sở hữu cross-sensor agreement; SC-5 sở hữu within/between-campaign variability; không dùng lại bảng/hình |
| SC-3 ↔ SC-4 | Trung bình | Cùng bối cảnh chuyển giao thông tin/BIM | SC-3 là clause-to-IFC pilot; SC-4 là taxonomy văn liệu; SC-4 không lập requirement matrix |
| SC-1 ↔ SC-2 | Thấp | Cùng lĩnh vực dao động/AI | SC-2 dùng dữ liệu độc lập và HPO; SC-1 không AI |
| SC-2 ↔ SC-5 | Thấp | Cùng bối cảnh dữ liệu dao động | SC-2 dùng dataset độc lập; SC-5 không HPO/phân loại |
| Các cặp còn lại | Thấp | Chỉ giao nhau ở bối cảnh luận án | Không tái sử dụng claim, kết quả, bảng, hình hoặc văn bản đáng kể |

---

## 10. Thứ tự ưu tiên và thời điểm kích hoạt

| Thứ tự | Công việc | Điều kiện |
|---:|---|---|
| **0** | Hoàn thành Gate 1/Paper 1 | Luôn ưu tiên trước mọi SC |
| **1** | SC-2 | Có dataset độc lập và không lấy nguồn lực của G1 |
| **2** | SC-1 | Paired registry khóa; Paper 1 đã khóa kết quả/bảng–hình, ưu tiên sau khi Paper 1 nộp |
| **3** | Pilot SC-5 | Paper 1 khóa; Healthy registry xác nhận ba campaign và điều kiện tương đương |
| **4** | Chuẩn bị SC-3 | Có thể lập clause-evidence table sớm; chỉ hoàn thiện sau khi ranh giới G2/CQ Paper 2 khóa |
| **5** | Pilot SC-4 | Chỉ sau G1; dừng nếu không chứng minh tính mới hoặc cạnh tranh nguồn lực với G2 |

**Khuyến nghị danh mục thực dụng:** SC-2, SC-1 và SC-3 là ba hướng chính; SC-5 là bài định lượng bổ sung nếu pilot mạnh; SC-4 giữ làm phương án dự phòng hoặc nền tổng quan, không bắt buộc xuất bản.

---

## 11. Quy tắc Go / No-Go chung

### GO khi

- Câu hỏi, dữ liệu, đơn vị phân tích và kết quả chính khác Paper lõi.
- Protocol, metric và nội dung loại trừ được khóa trước phân tích cuối.
- Có provenance, quyền sử dụng dữ liệu và chính sách proceedings/tạp chí rõ.
- Không tái sử dụng bảng, hình, kết quả hoặc văn bản đáng kể.
- Cả hai thầy xem ma trận chồng lấn và đồng ý nộp.

### NO-GO khi

- Bài chỉ là phiên bản thu nhỏ của Paper 1 hoặc Paper 2.
- Tính mới chỉ xuất hiện khi dùng LORO, xếp hạng cảm biến, CEI, schema truy vết, competency questions hoặc dữ liệu Rapexco.
- Cần công bố trước một claim/kết quả mà Paper lõi chưa khóa.
- Chính sách prior publication/copyright không rõ.
- Công việc làm chậm Evidence Gate kế tiếp.

---

## 12. Checklist trước mỗi lần nộp

- [ ] Xác nhận mã SC và phiên bản protocol.
- [ ] Khóa câu hỏi, dataset, đơn vị nhóm, metric chính và bảng–hình dự kiến.
- [ ] Cập nhật ma trận xâm phạm với Papers 1–3 và các SC đã nộp.
- [ ] Kiểm tra proceedings, indexing, copyright, prior publication và quyền mở rộng thành bài tạp chí.
- [ ] Khai báo đầy đủ dataset/phiên đo/bài liên quan trong manuscript và cover letter.
- [ ] Không có bản thảo chồng lấn đáng kể đang được xét đồng thời.
- [ ] Authorship và đóng góp được thống nhất trước khi nộp.
- [ ] Cả hai thầy phê duyệt Go/No-Go bằng văn bản.
- [ ] Nếu bằng chứng chưa đủ, ghi rõ: **Evidence is currently insufficient.**

---

## 13. Đoạn trình thầy

> Em tổng hợp năm ý tưởng bài hội thảo thuộc Supporting Scope. SC-1 đánh giá tương hợp PASCO–ADXL; SC-2 so sánh HPO trên dữ liệu độc lập; SC-3 ánh xạ yêu cầu thông tin tĩnh theo TCVN 14177/ISO 19650 sang IFC; SC-4 là systematic mapping về chuyển giao đầu ra AI/SHM sang hồ sơ kiểm tra; SC-5 định lượng độ lặp lại dữ liệu Healthy giữa run và campaign. Không bài nào sử dụng kết quả LORO, xếp hạng cấu hình cảm biến, CEI, schema truy vết, competency questions hoặc dữ liệu Rapexco để công bố trước. Gate 1 và Paper 1 vẫn là ưu tiên; SC-5 chỉ thực hiện sau khi Paper 1 khóa vì có rủi ro chồng lấn cao nhất. Trước mỗi lần nộp, em sẽ kiểm tra chính sách venue, cập nhật ma trận chồng lấn và xin thầy quyết định Go/No-Go.

---

## 14. Source of truth

Tài liệu này được đối chiếu với:

1. `MASTER_RESEARCH_CHARTER.md`;
2. `MASTER_RESEARCH_CHARTER_v1.1_LIMITED_FEM_20260717.md`;
3. `RESEARCH_DIRECTION_AND_SCOPE.md`;
4. `RESEARCH_ARCHITECTURE.md`;
5. `CURRENT_STATUS_AND_NEXT_DIRECTION.md`;
6. `00_README_START_HERE.md`;
7. `THE_COUNCIL_REVIEW_FEM_OR_NO_FEM_17.07.2026.md`;
8. `RESEARCH_ARCHITECTURE_DECISION_RECORD_20260717.md`.

Nếu có quyết định mới được hai thầy chấp thuận, quyết định đó có ưu tiên cao hơn tài liệu này và bản v1.2 phải được cập nhật trước khi sử dụng tiếp.
