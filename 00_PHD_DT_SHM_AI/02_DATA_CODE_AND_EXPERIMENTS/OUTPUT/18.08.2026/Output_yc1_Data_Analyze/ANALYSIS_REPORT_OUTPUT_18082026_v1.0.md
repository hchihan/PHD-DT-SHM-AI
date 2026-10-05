# BÁO CÁO PHÂN TÍCH BỘ KẾT QUẢ `OUTPUT_18.08.2026`

**Phiên bản:** v1.0 | **Ngày lập:** 18/08/2026
**Loại tài liệu:** Báo cáo phân tích thực nghiệm để thảo luận với thầy hướng dẫn. Không phải bản thảo bài báo, không phải hồ sơ đóng Gate.
**Người lập:** NCS, hỗ trợ phân tích read-only trên artefact gốc.

## Routing block

```text
RQ:             RQ1
WP:             WP1 — Laboratory vibration evidence
Chương:         Chapter 4
Paper:          Paper 1
Evidence Gate:  Gate 1 — OPEN — PARTIAL EVIDENCE
Scope:          Core — qualification of vibration-derived condition evidence
Evidence type:  Laboratory evidence
```

---

## 1. Vì sao báo cáo này quan trọng

Các phiên rà soát trước ghi nhận rằng toàn bộ file kết quả mô hình của Paper 1 không tồn tại trong repository, và rằng ResNet1D chưa từng được chạy. Bộ `OUTPUT_18.08.2026` bác bỏ cả hai nhận định đó.

Thư mục chứa 7 bảng kết quả CSV, 3 confusion matrix, 8 lần chạy deep learning có đầy đủ `scores.json`, `predictions.json`, `history.json`, checkpoint `.pt` và confusion matrix ảnh, cùng toàn bộ mã nguồn `sensor_signal_analyzer` kèm test suite. Đây là artefact cấp một, không phải báo cáo tường thuật.

Báo cáo này tính lại mọi con số từ file gốc, không trích dẫn lại bản tường thuật nào.

## 2. Artefact đã phân tích

| Nhóm | File | Nội dung xác minh được |
|---|---|---|
| Chất lượng dữ liệu | `03_DATA_QUALITY_AND_PROVENANCE_LOG.csv` | 66 dòng cờ chất lượng và provenance |
| LORO trong campaign | `05_WITHIN_CAMPAIGN_LORO_RESULTS.csv` | 238 dòng: 4 model × 8 sensor config × 6 fold |
| LOCO liên campaign | `06_CROSS_CAMPAIGN_RESULTS.csv` | 36 dòng: 4 model × 3 config × 3 fold |
| Tổng hợp model | `07_BASELINE_MODEL_COMPARISON.csv` | 36 dòng thống kê |
| Permutation | `08_PERMUTATION_RESULTS.csv` | 300 dòng: 3 cấu hình × 100 hoán vị |
| Cấu hình cảm biến | `09_SENSOR_CONFIGURATION_RESULTS.csv` | 11 dòng |
| Sensitivity | `11_SENSITIVITY_RESULTS.csv` | 10 dòng, 4 phép kiểm |
| Confusion matrix | `12_CONFUSION_MATRICES/*.csv` | 3 ma trận cấp window |
| Deep learning | `cp{1,2_21,2_2122,3}_{1dcnn,resnet1d}_v5/ddp_seed42/` | 8 lần chạy, mỗi lần có scores, predictions, history, checkpoint |
| Mã nguồn | `sensor_signal_analyzer/` | 6 kiến trúc, engine, dataloader, 11 file test |

Toàn bộ 8 lần chạy deep learning dùng `seed42` và nhánh `ddp` (distributed data parallel).

## 3. Phương pháp của báo cáo này

Bốn thao tác được thực hiện trên artefact gốc, không sửa file nguồn:

1. Đọc lại và tổng hợp các bảng CSV theo campaign, model và sensor configuration.
2. Tính lại empirical p-value từ 300 dòng permutation, đối chiếu với giá trị thực đọc trực tiếp từ `05_` và `06_`.
3. Tính khoảng tin cậy Wilson và kiểm định McNemar chính xác trên `predictions.json` của 8 lần chạy deep learning.
4. Tái dựng phân bố lớp dự đoán từ confusion matrix LOCO để xác định cơ chế của thất bại chuyển giao.

Empirical p-value dùng dạng bảo thủ `(k+1)/(n+1)` theo khuyến nghị của Combrisson và Jerbi về ngưỡng ngẫu nhiên ở cỡ mẫu nhỏ [1] và khung permutation của Ojala và Garriga [2].

---

## 4. Kết quả

### 4.1 Chất lượng dữ liệu và tính ổn định định danh cảm biến

`03_DATA_QUALITY_AND_PROVENANCE_LOG.csv` ghi nhận trực tiếp trạng thái ổn định vị trí cột.

**Bảng 1. Cờ chất lượng và provenance theo campaign.**

| Campaign | `sensor_column_position_stability` | Dead channel (số recording) | Provenance warning |
|---|---|---:|---:|
| Campaign 1 | `UNSTABLE` | 36 | 0 |
| Campaign 2 | `UNSTABLE` | 12 | 1 |
| Campaign 3 | `STABLE` | 14 | 0 |

**Bảng 2. Phân bố dead channel theo vị trí cột, trước khi sửa định danh.**

| Campaign | S1_Ax | S1_Ay | S2_Ax | S2_Ay | S3_Ax | Tổng |
|---|---:|---:|---:|---:|---:|---:|
| Campaign 1 | 0 | 19 | 0 | 17 | 0 | 36 |
| Campaign 2 | 3 | 0 | 5 | 0 | 4 | 12 |
| Campaign 3 | 0 | 0 | 0 | 0 | 14 | 14 |
| Tổng | 3 | 19 | 5 | 17 | 18 | 62 |

Bảng 2 chứa một dấu hiệu nội tại đáng chú ý. Ở Campaign 1, kênh chết phân bố 19 ở `S1_Ay` và 17 ở `S2_Ay`, tổng 36. Báo cáo kiểm định dataset sau khi sửa định danh bằng vân tay trọng trường ghi nhận đúng 36 kênh `DEAD_CONSTANT`, toàn bộ thuộc một kênh vật lý duy nhất là `BeamColumn_Ay`, xuất hiện ở đúng một nửa trong 72 file của campaign đó.

Hai con số 19 + 17 = 36 hội tụ về một kênh vật lý sau khi sửa. Đây là bằng chứng nội tại rằng hoán vị khối cột là có thật và phép sửa đã gom đúng: cùng 36 lần xuất hiện của một kênh vật lý đã bị gán cho hai vị trí cột khác nhau trong file xuất. Không cần giả thiết bổ sung nào để giải thích quan hệ số học này.

Campaign 3 là campaign duy nhất mang cờ `STABLE`, và đó là cơ sở để coi kết quả Campaign 3 là kết quả duy nhất diễn giải được ở cấp vị trí vật lý mà không cần dè dặt.

### 4.2 Hiệu năng trong từng campaign

**Bảng 3. Macro-F1 trung vị theo campaign và model, gộp toàn bộ sensor configuration và fold. Nguồn: `05_WITHIN_CAMPAIGN_LORO_RESULTS.csv`.**

| Campaign | LogReg | SVM | RF | CNN | Số fold (RF) |
|---|---:|---:|---:|---:|---:|
| Campaign 1 | 0.460 | 0.483 | **0.683** | 0.100 | 18 |
| Campaign 2 | 0.702 | 0.706 | **0.878** | không chạy | 30 |
| Campaign 3 | 0.410 | 0.433 | **0.609** | không chạy | 30 |

Mức ngẫu nhiên bốn lớp cân bằng là 0.25.

Random forest vượt trội ở cả ba campaign. Khoảng cách so với LogReg và SVM là 0.18 đến 0.22, tức không nhỏ. Điều này nhất quán với nhận định rằng đặc trưng miền thời gian và miền tần số thủ công đủ mạnh cho bài toán này ở cỡ mẫu hiện có, và mô hình phi tuyến dạng ensemble khai thác được chúng tốt hơn mô hình tuyến tính.

**Bảng 4. Macro-F1 trung vị của RF theo sensor configuration.**

| Sensor config | Campaign 1 | Campaign 2 | Campaign 3 |
|---|---:|---:|---:|
| `S1_Ax` | 0.645 | – | – |
| `S2_Ax` | 0.683 | – | – |
| `S1S2_Ax` | 0.760 | – | – |
| `S1_xyz` | – | 0.878 | 0.628 |
| `S2_xyz` | – | 0.755 | 0.542 |
| `S3_xyz` | – | **0.911** | 0.580 |
| `S1S2_xyz` | – | 0.888 | 0.650 |
| `S1S2S3_xyz` | – | 0.907 | **0.678** |

Ba quan sát.

Gộp cảm biến luôn tốt hơn cảm biến đơn, ở cả ba campaign. Ở Campaign 1, `S1S2_Ax` đạt 0.760 so với 0.683 và 0.645 của hai cảm biến đơn.

Ở Campaign 2, cấu hình tốt nhất là `S3_xyz` (0.911), tức một cảm biến đơn tại vị trí brace, cao hơn cả cấu hình ba cảm biến (0.907). Chênh lệch 0.004 nằm trong nhiễu, nhưng nó cho thấy Campaign 2 đã chạm trần từ một cảm biến và vì thế không phân giải được câu hỏi về số lượng cảm biến.

Ở Campaign 3, thứ tự đơn cảm biến là `S1_xyz` 0.628 > `S3_xyz` 0.580 > `S2_xyz` 0.542, và cấu hình đầy đủ 0.678 là tốt nhất. Campaign 3 là campaign duy nhất mà phép so sánh cấu hình cảm biến có sức phân giải, vì nó không chạm trần và không mang cờ `UNSTABLE`.

**Bảng 5. F1 trung vị từng lớp, RF, theo campaign.**

| Campaign | Healthy | B1 | B2 | B3 |
|---|---:|---:|---:|---:|
| Campaign 1 | 0.669 | 0.678 | 0.706 | 0.700 |
| Campaign 2 | 0.935 | 0.813 | 0.801 | **0.965** |
| Campaign 3 | 0.640 | 0.659 | 0.626 | 0.673 |

Ở Campaign 1 và Campaign 3, bốn lớp có độ khó tương đương, chênh lệch dưới 0.05. Ở Campaign 2, B3 và Healthy tách rõ hơn B1 và B2 khoảng 0.13 đến 0.16. Mục 4.6 kiểm tra xem chênh lệch này có phải hệ quả của cấu trúc buổi đo hay không.

### 4.3 Chuyển giao giữa các campaign

**Bảng 6. Kết quả LOCO, 36 dòng, Analysis Set A. Nguồn: `06_CROSS_CAMPAIGN_RESULTS.csv`.**

| Model | Trung vị | Trung bình | Độ lệch chuẩn | Nhỏ nhất | Lớn nhất |
|---|---:|---:|---:|---:|---:|
| LogReg | 0.186 | 0.189 | 0.032 | 0.153 | 0.259 |
| SVM | 0.195 | 0.193 | 0.039 | 0.120 | 0.230 |
| RF | 0.166 | 0.160 | 0.024 | 0.129 | 0.202 |
| CNN | 0.152 | 0.157 | 0.050 | 0.100 | 0.250 |

Ba con số quyết định:

- **35 trên 36 dòng dưới mức ngẫu nhiên 0.25.** Giá trị lớn nhất trong toàn bộ 36 dòng là 0.259, thuộc LogReg với `S2_Ax`, giữ lại Campaign 3.
- **31 trên 36 dòng dưới trung vị của phân phối null** (0.2243).
- **6 trên 36 dòng dưới cả giá trị nhỏ nhất của 100 lần hoán vị** (0.1339).

Trong 144 ô F1 từng lớp của bảng LOCO, có 18 ô bằng đúng 0.000: Healthy 6 ô, B1 5 ô, B2 4 ô, B3 3 ô. Một mô hình không dự đoán lớp nào đó dù chỉ một lần đúng, trên 360 window của lớp đó, không phải là mô hình yếu. Đó là mô hình sụp về một tập con của không gian lớp.

**Cơ chế.** Confusion matrix LOCO giữ lại Campaign 1, RF, `S1S2_Ax`, 1.440 window:

| true \ predicted | Healthy | B1 | B2 | B3 |
|---|---:|---:|---:|---:|
| Healthy | 3 | 45 | 18 | **294** |
| B1 | 7 | 42 | 24 | **287** |
| B2 | 3 | 33 | 20 | **304** |
| B3 | 11 | 128 | 24 | 197 |

Phân bố lớp dự đoán: Healthy 1.7 %, B1 17.2 %, B2 6.0 %, **B3 75.1 %**, so với sự thật cân bằng 25 % mỗi lớp. Recall từng lớp: Healthy 0.008, B1 0.117, B2 0.056, B3 0.547.

Mô hình huấn luyện trên Campaign 2 và Campaign 3 gán ba phần tư số window của Campaign 1 vào một lớp duy nhất. Đây là sụp đổ suy biến, không phải suy giảm hiệu năng. Nó giải thích trực tiếp vì sao p thực nghiệm bằng 1.000 ở mục 4.4: nhãn thật của hai campaign nguồn dạy cho mô hình một ranh giới mà khi áp lên campaign đích, nó phản tương quan với nhãn đích.

Kết quả này nhất quán với văn liệu về domain shift trong kết cấu liên kết bu lông, nơi việc tháo lắp lại giữa các campaign được xác định là cơ chế phá vỡ khả năng lặp lại [3], và với quan sát rằng biến thiên do lắp đặt, bề mặt và hình học giao diện trong kết cấu có liên kết có thể lớn hơn chính hiệu ứng cần đo [4]. Khi phân bố nguồn và đích khác nhau, mô hình chỉ huấn luyện trên nguồn có thể thất bại hoàn toàn [5].

### 4.4 Permutation control

Giá trị thực được đọc trực tiếp từ file kết quả, không lấy từ báo cáo tường thuật.

**Bảng 7. Permutation control, 100 hoán vị mỗi cấu hình, giữ nguyên cấu trúc nhóm run.**

| Cấu hình | Thực đo | Null trung vị | Null nhỏ nhất | Null lớn nhất | k = #(null ≥ thực) | p = (k+1)/101 |
|---|---:|---:|---:|---:|---:|---:|
| Trong Campaign 2, `S1S2S3_xyz`, giữ lại R7 | 0.9624 | 0.2225 | 0.0000 | 0.4887 | 0 | **0.0099** |
| Trong Campaign 1, `S1S2_Ax`, giữ lại R1 | 0.6473 | 0.2286 | 0.0773 | 0.3994 | 0 | **0.0099** |
| LOCO `S1S2_Ax`, giữ lại Campaign 1 | 0.1292 | 0.2243 | 0.1339 | 0.3237 | 100 | **1.0000** |

Phân phối null của cả ba cấu hình tập trung quanh 0.222 đến 0.229, tức quanh mức ngẫu nhiên. Đây là phép kiểm chính pipeline chứ không phải kết quả về kết cấu: nếu pipeline rò rỉ, phân phối null sẽ bị đẩy lên trên mức ngẫu nhiên.

Hai dòng đầu nằm trên toàn bộ 100 hoán vị. Dòng thứ ba nằm dưới toàn bộ 100 hoán vị, và dưới cả giá trị nhỏ nhất trong 100 lần (0.1292 so với 0.1339).

Giới hạn: với 100 hoán vị, p nhỏ nhất đạt được là 0.0099. Mọi fold dùng làm bằng chứng chính cần nâng lên tối thiểu 1.000 hoán vị trước khi nộp.

### 4.5 Deep learning, gồm cả ResNet1D

Tám lần chạy tồn tại đầy đủ artefact. Cấu trúc tập kiểm tra được tái dựng từ `predictions.json`: mỗi lần chạy giữ lại **toàn bộ 12 recording của một run duy nhất** (R6 cho Campaign 1, R12 cho Campaign 2, R18 cho Campaign 3). Định danh recording mang tiền tố run, xác nhận phép chia là run-aware.

**Bảng 8. Kết quả deep learning, cấp recording, n = 12 recording mỗi lần chạy.**

| Lần chạy | Đúng | Accuracy | KTC Wilson 95 % | Balanced acc | Macro-F1 | ROC-AUC | Epoch | Train acc cuối | Val loss cuối |
|---|---:|---:|---|---:|---:|---:|---:|---:|---:|
| C1 · 1D-CNN | 9/12 | 0.750 | [0.468, 0.911] | 0.750 | 0.727 | 0.926 | 33 | 0.983 | 1.626 |
| C1 · ResNet1D | 11/12 | 0.917 | [0.646, 0.985] | 0.917 | **0.914** | 1.000 | 69 | 0.997 | 0.396 |
| C2 (21/07) · 1D-CNN | 7/12 | 0.583 | [0.320, 0.807] | 0.583 | 0.581 | 0.870 | 27 | 0.996 | 2.077 |
| C2 (21/07) · ResNet1D | 11/12 | 0.917 | [0.646, 0.985] | 0.917 | **0.914** | 1.000 | 58 | 1.000 | 0.322 |
| C2 (21+22/07) · 1D-CNN | 7/12 | 0.583 | [0.320, 0.807] | 0.583 | 0.586 | 0.870 | 26 | 1.000 | 1.464 |
| C2 (21+22/07) · ResNet1D | 11/12 | 0.917 | [0.646, 0.985] | 0.917 | **0.914** | 0.972 | 36 | 1.000 | 0.442 |
| C3 · 1D-CNN | 4/12 | 0.333 | [0.138, 0.609] | 0.333 | 0.250 | 0.769 | 23 | 0.874 | 3.325 |
| C3 · ResNet1D | 5/12 | 0.417 | [0.193, 0.680] | 0.417 | 0.345 | 0.676 | 24 | 0.881 | 1.506 |

**Bảng 9. Kiểm định McNemar chính xác, ghép cặp trên cùng một run giữ lại.**

| Campaign | 1D-CNN | ResNet1D | Chỉ ResNet đúng | Chỉ CNN đúng | p chính xác |
|---|---:|---:|---:|---:|---:|
| C1 | 9/12 | 11/12 | 2 | 0 | 0.5000 |
| C2 (21/07) | 7/12 | 11/12 | 5 | 1 | 0.2188 |
| C2 (21+22/07) | 7/12 | 11/12 | 4 | 0 | 0.1250 |
| C3 | 4/12 | 5/12 | 4 | 3 | 1.0000 |

Bốn nhận định, xếp theo mức chắc chắn giảm dần.

**ResNet1D tốt hơn 1D-CNN ở cả bốn so sánh, và không so sánh nào đạt ý nghĩa thống kê.** p nhỏ nhất là 0.1250. Với n = 12 và một fold duy nhất, ngay cả chênh lệch 4 recording cũng không vượt ngưỡng 0.05. Nếu dùng phép kiểm dấu trên bốn campaign, bốn trên bốn cùng chiều cho p = 0.125 hai phía, cũng không đạt ý nghĩa. Đây là điểm mà một phản biện ML sẽ nhắm vào trước tiên.

**Chênh lệch nằm ở khả năng khái quát, không ở khả năng khớp.** Cả hai kiến trúc đều đạt train accuracy từ 0.983 đến 1.000 ở Campaign 1 và Campaign 2. Khác biệt nằm ở val loss: ResNet1D 0.322 đến 0.442, còn 1D-CNN 1.464 đến 2.077. Mô hình nông khớp dữ liệu huấn luyện hoàn hảo rồi mất khả năng khái quát; mô hình sâu có residual connection giữ được val loss thấp hơn từ 3 đến 6 lần. Đây là mẫu hình overfitting kinh điển ở cỡ mẫu nhỏ.

**Campaign 3 khó ở phía dữ liệu, không ở phía dung lượng mô hình.** Ở C1 và C2, cả hai mô hình khớp gần như hoàn hảo tập huấn luyện. Ở C3, train accuracy chỉ đạt 0.874 và 0.881, và val balanced accuracy dừng ở 0.333. Cả hai kiến trúc đều không khớp nổi tập huấn luyện của C3. Tăng độ sâu kiến trúc từ 1D-CNN lên ResNet1D chỉ cải thiện macro-F1 từ 0.250 lên 0.345, vẫn quanh mức ngẫu nhiên. Kết luận: độ khó của C3 không phải do mô hình thiếu dung lượng.

**ROC-AUC không đồng hành với macro-F1 ở C3.** C3 · 1D-CNN có macro-F1 đúng bằng mức ngẫu nhiên 0.250 nhưng ROC-AUC 0.769. Nghĩa là mô hình có xếp hạng xác suất mang chút thông tin, nhưng ngưỡng quyết định argmax sụp về một lớp: nó dự đoán B3 cho 8 trên 12 recording. ResNet1D ở C3 dự đoán B2 cho 6 trên 12. Cả hai đều là sụp đổ về lớp trội, giống hệt mẫu hình LOCO ở mục 4.3, chỉ khác quy mô.

### 4.6 Kiểm chứng nhiễu loạn buổi đo của Campaign 2

Cặp `cp2_21` và `cp2_2122` là một phép kiểm có chủ đích, và nó trả lời trực tiếp câu hỏi đã treo từ các phiên trước.

**Bảng 10. Cấu trúc buổi đo trong run giữ lại R12.**

| Lần chạy | Recording từ 21/07 | Recording từ 22/07 | Lớp có trong 21/07 | Lớp có trong 22/07 |
|---|---|---|---|---|
| C2 (21/07 only) · 1D-CNN | 7/12 đúng | không có | B1, B2, B3, Healthy | – |
| C2 (21/07 only) · ResNet1D | 11/12 đúng | không có | B1, B2, B3, Healthy | – |
| C2 (21+22/07) · 1D-CNN | 3/3 đúng | 4/9 đúng | chỉ B3 | B1, B2, Healthy |
| C2 (21+22/07) · ResNet1D | 3/3 đúng | 8/9 đúng | chỉ B3 | B1, B2, Healthy |

Hai kết luận, và chúng đi ngược nhau ở mức độ đáng chú ý.

**Nhiễu loạn buổi đo tồn tại trong cấu trúc dữ liệu.** Ở biến thể gộp hai buổi, cả ba recording từ 21/07 trong run giữ lại đều thuộc lớp B3, và cả hai mô hình phân loại đúng 3 trên 3. Toàn bộ lỗi nằm ở 9 recording của 22/07. Điều này khớp với hệ số Cramér's V bằng 1.00 giữa State và Acquisition_Date đã ghi nhận trước đây.

**Nhưng nhiễu loạn đó không thổi phồng con số công bố.** Biến thể chỉ dùng buổi 21/07, trong đó cả bốn lớp cùng một buổi và vì thế không thể có nhiễu loạn ngày đo, cho macro-F1 **0.914 với ResNet1D**, đúng bằng biến thể gộp hai buổi. Với 1D-CNN, 0.581 so với 0.586, chênh lệch 0.005.

Đây là một kết quả tích cực và nó sửa lại nhận định trước đó. Hai phiên rà soát trước, dựa trên tài liệu tường thuật chưa có artefact, đã đề nghị loại Campaign 2 khỏi bằng chứng chính vì nghi ngờ nhiễu loạn buổi đo. Artefact `cp2_21` cho thấy nghi ngờ đó không được xác nhận: khi loại bỏ hoàn toàn khả năng nhiễu loạn bằng cách chỉ dùng một buổi, hiệu năng không đổi.

Cần ghi rõ giới hạn: phép kiểm này chạy trên một fold, n = 12, một seed. Nó làm giảm mạnh xác suất rằng con số Campaign 2 là artefact buổi đo, nhưng không loại trừ được ở mức thống kê.

### 4.7 Sensitivity

**Bảng 11. Bốn phép kiểm độ nhạy, một fold đại diện, RF. Nguồn: `11_SENSITIVITY_RESULTS.csv`.**

| Phép kiểm | Biến thể | Macro-F1 | Chênh lệch |
|---|---|---:|---:|
| A. File provenance `BS1B1L1R12` | có | 0.9708 | – |
| | không | 0.9750 | +0.004 |
| B. Độ dài cửa sổ | giữa 40 s | 0.9708 | – |
| | toàn bộ bản ghi | 0.8589 | −0.112 |
| C. Chuẩn hóa | giữ biên độ | 0.9708 | – |
| | chuẩn hóa RMS từng bản ghi | 0.8412 | −0.130 |
| D. Chọn trục, Campaign 2 | chỉ Ax | 0.7698 | – |
| | xyz | 0.9192 | +0.149 |
| D. Chọn trục, Campaign 3 | chỉ Ax | 0.6599 | – |
| | xyz | 0.6903 | +0.030 |

File provenance có ảnh hưởng không đáng kể, xác nhận rằng vấn đề `BS1B1L1R12` là vấn đề tài liệu chứ không phải vấn đề số liệu.

Chuẩn hóa RMS làm giảm 0.130. Thông tin biên độ mang nội dung phân biệt trạng thái trong bộ dữ liệu này, và quyết định giữ biên độ trong pipeline chính là đúng.

Ràng buộc kênh chung để so sánh liên campaign khiến Campaign 2 mất 0.149. Kết hợp với mục 4.3, ràng buộc này trả giá bằng hiệu năng nội campaign mà không mua được khả năng chuyển giao.

### 4.8 Kiểm toán cấp báo cáo metric

Một phát hiện phương pháp cần xử lý trước khi so sánh hai họ mô hình.

Các bảng CSV ghi `n_test_windows = 240` cho LORO nội campaign và `n_test_windows = 1440` cho LOCO. Ma trận confusion nội campaign có tổng 240 và ma trận LOCO có tổng 1.440. Với 12 recording mỗi run và 20 window mỗi recording, 240 = 12 × 20. Do đó **metric của họ mô hình đặc trưng được tính ở cấp window**.

Ngược lại, `predictions.json` của tám lần chạy deep learning chứa đúng 12 mục, tức **metric của họ deep learning được tính ở cấp recording**.

Phép chia dữ liệu của cả hai họ đều là run-aware và hợp lệ. Nhưng cấp tổng hợp báo cáo khác nhau. Macro-F1 cấp window và macro-F1 cấp recording không phải cùng một đại lượng: tổng hợp 20 window về một recording trước khi tính metric thường làm tăng giá trị vì nó khử nhiễu cấp window. **Không được đặt hai họ mô hình cạnh nhau trong một bảng cho tới khi cả hai được báo cáo ở cùng một cấp.**

Đây là hạng mục bắt buộc phải sửa, và nó rẻ: chỉ cần tổng hợp lại dự đoán cấp window của họ đặc trưng về cấp recording rồi tính lại metric.

---

## 5. Hình

**Hình 1** (`FIG1_within_vs_cross_vs_null.png`). Phân bố macro-F1 nội campaign của ba campaign, phân bố LOCO, và hai phân phối null, trên cùng một trục. Đường ngang 0.25 là mức ngẫu nhiên.

**Hình 2** (`FIG2_resnet_vs_cnn_wilson.png`). Accuracy cấp recording của 1D-CNN và ResNet1D theo bốn cấu hình campaign, kèm khoảng tin cậy Wilson 95 %. Độ rộng khoảng tin cậy là thông điệp chính của hình này.

**Hình 3** (`FIG3_loco_collapse.png`). Ma trận confusion chuẩn hóa theo hàng và phân bố lớp dự đoán của LOCO giữ lại Campaign 1. Cột phải cho thấy 75.1 % dự đoán rơi vào một lớp.

---

## 6. Thảo luận về mức đóng góp

### 6.1 Đóng góp của bộ dữ liệu

**Cao, và không nằm ở chỗ thường được kỳ vọng.**

Giá trị của bộ dữ liệu này không phải ở 216 recording cân bằng bốn lớp. Bộ dữ liệu như vậy đã có trong văn liệu, ví dụ tập bolt-loosening có metadata cảm biến và run lặp lại. Giá trị nằm ở ba đặc điểm hiếm.

**Thứ nhất, bộ dữ liệu mang theo chính lỗi provenance của nó và phép sửa.** Cờ `sensor_column_position_stability` với giá trị `UNSTABLE` cho hai campaign và `STABLE` cho campaign thứ ba, cùng quan hệ số học 19 + 17 = 36 hội tụ về một kênh vật lý sau khi sửa, tạo thành một ca nghiên cứu hoàn chỉnh về một dạng lỗi mà không nguồn nào trong corpus đã rà soát đề cập. Phần lớn dataset công bố không giữ lại dấu vết này.

**Thứ hai, cặp `cp2_21` và `cp2_2122` là một control có thiết kế.** Một biến thể chỉ dùng một buổi đo, một biến thể gộp hai buổi với cấu trúc lớp lệch hoàn toàn theo buổi. Đây đúng là phép kiểm mà văn liệu về nhiễu loạn thu nhận đòi hỏi và hiếm khi có. Nó cho phép trả lời câu hỏi "kết quả này là về kết cấu hay về buổi đo" bằng số chứ không bằng lập luận.

**Thứ ba, ba campaign có tháo lắp lại giữa các đợt tạo thành một benchmark domain shift tự nhiên cho liên kết bu lông.** Văn liệu ghi nhận rằng dữ liệu loại này khan hiếm, và rằng tháo lắp lại là cơ chế phá vỡ khả năng lặp lại giữa campaign [3], [4]. Bộ dữ liệu này cung cấp đúng điều kiện đó với nhãn có kiểm soát.

### 6.2 Đóng góp của kết quả

**Trung bình đến cao, phân bố rất không đều giữa các kết quả.**

**Kết quả mạnh nhất là thất bại LOCO cùng cơ chế của nó.** Không phải vì nó âm tính, mà vì nó được định lượng ở ba mức: 35 trên 36 dòng dưới mức ngẫu nhiên; p thực nghiệm bằng 1.000, tức dưới toàn bộ 100 hoán vị; và cơ chế cụ thể là 75.1 % dự đoán dồn vào một lớp với recall của lớp Healthy chỉ 0.008. Ba mức này biến một câu "mô hình không khái quát được" thành một phát biểu kiểm chứng được về sụp đổ suy biến. Đây là kết quả dễ trích dẫn nhất của cả bộ.

**Kết quả có giá trị bất ngờ là control buổi đo.** Nó cho ra kết quả ngược với giả thuyết ban đầu: nhiễu loạn tồn tại trong cấu trúc dữ liệu nhưng không làm thay đổi con số. Một kết quả control cho ra câu trả lời "không, mối lo này không được xác nhận" có giá trị học thuật ngang với một kết quả xác nhận, và nó chứng minh rằng quy trình kiểm chứng của đề tài thực sự có thể trả lời cả hai chiều.

**Kết quả có giá trị vừa là so sánh ResNet1D với 1D-CNN.** Chiều hiệu ứng nhất quán 4 trên 4 và biên độ lớn ở C1 và C2. Nhưng không so sánh nào đạt ý nghĩa thống kê ở n = 12, một fold, một seed. Ở dạng hiện tại đây là quan sát, chưa phải bằng chứng. Điểm thực sự có giá trị lại là điều phái sinh: cả hai kiến trúc đều không khớp nổi tập huấn luyện của Campaign 3, nên độ khó của C3 là ở phía dữ liệu chứ không phải ở phía dung lượng mô hình. Phát biểu đó không cần ý nghĩa thống kê để đứng vững, vì nó dựa trên train accuracy chứ không dựa trên hiệu số test.

**Kết quả yếu nhất là hiệu năng nội campaign.** RF đạt 0.683, 0.878 và 0.609. Ba con số này tự thân không đóng góp gì cho văn liệu. Chúng chỉ có giá trị khi đặt cạnh phần còn lại, để cho thấy rằng một kết quả nội campaign trên mức ngẫu nhiên rõ rệt vẫn không chuyển giao được.

### 6.3 Vì sao điều này phục vụ mục tiêu luận án

Mục tiêu Paper 1 đã khóa là mắt xích `Vibration data → qualified condition evidence`, thuộc trục Quản lý xây dựng chứ không phải trục thuật toán.

Bộ kết quả này phục vụ đúng mục tiêu đó, và phục vụ theo cách mà một bộ kết quả hiệu năng cao sẽ không làm được. Nó cung cấp:

- một điều kiện provenance có thể vi phạm và đã bị vi phạm, kèm cách phát hiện (mục 4.1);
- một phép kiểm nhiễu loạn thu nhận có thể chạy và cho ra câu trả lời hai chiều (mục 4.6);
- một ranh giới phạm vi hiệu lực đo được, ở đây là biên giới campaign (mục 4.3, 4.4);
- một tập trường metadata bắt buộc suy ra từ chính những gì đã hỏng, chứ không từ một bài tập thiết kế schema.

Nói cách khác, bộ dữ liệu và bộ kết quả này đủ để xây dựng CEI-Lab profile như một cấu trúc có nội dung thực nghiệm, chứ không phải như một khai báo.

Bốn lớp bằng chứng của luận án được giữ tách biệt: toàn bộ nội dung báo cáo này là **laboratory evidence**. Không có phát biểu nào về chẩn đoán hiện trường, mức độ hư hỏng, tuổi thọ còn lại, bảo trì dự báo, vị trí cảm biến tối ưu, hay chuyển giao bộ phân lớp từ phòng thí nghiệm ra công trình. Mọi mô hình phần tử hữu hạn được nhắc tới trong chương trình nghiên cứu này là **nominal, uncalibrated, reference-only, and not used for damage diagnosis**, và không mô hình nào như vậy tham gia vào bất kỳ kết quả nào ở đây.

---

## 7. Giới hạn

**Cỡ mẫu kiểm tra của họ deep learning.** 12 recording, một run, một fold. Khoảng tin cậy Wilson 95 % cho 11/12 là [0.646, 0.985]. Không phát biểu so sánh nào giữa hai kiến trúc đứng vững ở cỡ mẫu này. Kích thước tập kiểm tra độc lập quyết định độ chính xác của ước lượng hiệu năng [6].

**Một seed duy nhất.** Toàn bộ 8 lần chạy dùng `seed42`. Không tách được biến thiên giữa các run khỏi biến thiên do khởi tạo.

**Không có LORO đầy đủ cho họ deep learning.** Chỉ một fold mỗi cấu hình, không phải 6 fold.

**Cấp báo cáo metric không đồng nhất giữa hai họ mô hình** (mục 4.8). Đây là hạng mục chặn việc so sánh.

**Coverage của CNN trong bảng CSV bị hỏng.** Bốn dòng duy nhất, Campaign 1, `S1_Ax`, macro-F1 đúng bằng 0.100 và balanced accuracy đúng bằng 0.250 ở cả bốn fold, dừng ở epoch 11. Đây là sụp về một lớp do dừng sớm, không phải kết quả học. Bốn dòng này phải bị loại khỏi mọi tổng hợp.

**Permutation mới ở 100 hoán vị và 3 cấu hình.** p nhỏ nhất đạt được là 0.0099.

**Ánh xạ nhãn sang liên kết vật lý vẫn chưa có.** `B1`, `B2`, `B3` được giải mã tất định từ tên file, nhưng không tài liệu nào ghi mỗi nhãn ứng với liên kết nào. **Evidence is currently insufficient.** Vì vậy không phát biểu nào trong báo cáo này gán ý nghĩa cơ học cho một lớp cụ thể, và không phát biểu nào nói một trạng thái gần Healthy hơn trạng thái khác.

**Kết quả cấp cột, không cấp vị trí vật lý, cho Campaign 1 và Campaign 2.** Cờ `UNSTABLE` áp cho toàn bộ hai campaign này. Mọi thứ hạng cảm biến đơn ở Bảng 4 cho hai campaign đó là thứ hạng giữa các vị trí cột.

**Chưa có so sánh window-random với run-aware trên chính bộ dữ liệu này.** Lập luận về thổi phồng do chia ngẫu nhiên cấp window hiện dựa vào văn liệu [7], [8], chưa dựa vào số của đề tài.

---

## 8. Điều này thay đổi gì trong Paper 1

Năm thay đổi, xếp theo mức tác động.

**ResNet1D chuyển từ "chưa có bằng chứng" sang "có bằng chứng, chưa đủ mạnh".** Câu `ResNet1D remains pending verification and is excluded from the main comparative claim` không còn đúng về phần verification. Artefact tồn tại đầy đủ. Nhưng vì n = 12 và một seed, ResNet1D vào Paper 1 như một quan sát nhất quán về chiều, không như một so sánh có ý nghĩa thống kê. Hạng mục Gate 1 về ResNet1D provenance chuyển từ `OPEN` sang có thể đóng khi bổ sung xác nhận sensor mode.

**Campaign 2 được phục hồi một phần.** Đề xuất trước đó loại Campaign 2 khỏi bằng chứng chính không còn cơ sở, vì `cp2_21` cho kết quả bằng `cp2_2122`. Campaign 2 vẫn mang cờ `UNSTABLE` về định danh cột, nên nó vẫn không diễn giải được ở cấp vị trí vật lý, nhưng nó không còn bị nghi ngờ về nhiễu loạn buổi đo.

**Thất bại LOCO có thêm cơ chế.** Trước đây chỉ có con số. Nay có phân bố dự đoán 75.1 % dồn vào một lớp và recall Healthy 0.008. Phần Discussion viết được chặt hơn nhiều.

**Xuất hiện một hạng mục chặn mới: cấp báo cáo metric.** Hạng mục này chưa từng được nêu trong bất kỳ tài liệu nào trước đó của đề tài.

**Bốn dòng CNN trong bảng CSV phải bị đánh dấu loại.** Chúng là artefact dừng sớm và hiện đang nằm trong bảng tổng hợp.

---

## 9. Claim → Evidence → Limitation → Next action

**Claim.** Bộ `OUTPUT_18.08.2026` là bộ artefact cấp một đầu tiên của Paper 1 có thể kiểm chứng tại nguồn. Nó nâng mức đóng góp của đề tài từ "một giao thức được đặc tả" lên "một giao thức đã được thực thi và đã phát hiện được lỗi trên chính dữ liệu của mình", đồng thời sửa lại hai nhận định sai của các phiên rà soát trước.

**Evidence.** 238 dòng LORO, 36 dòng LOCO, 300 dòng permutation, 66 dòng cờ chất lượng, 3 confusion matrix, 8 lần chạy deep learning có predictions và history đầy đủ, toàn bộ mã nguồn. Mọi con số trong báo cáo này được tính lại từ những file đó, không lấy từ bản tường thuật nào.

**Limitation.** Họ deep learning chỉ có 12 recording kiểm tra, một fold, một seed, nên không so sánh kiến trúc nào đạt ý nghĩa thống kê. Hai họ mô hình đang được báo cáo ở hai cấp tổng hợp khác nhau. Ánh xạ nhãn sang liên kết vật lý vẫn chưa có. Kết quả Campaign 1 và Campaign 2 vẫn ở cấp vị trí cột.

**Next action.** Theo thứ tự chi phí tăng dần:

1. Tổng hợp lại dự đoán cấp window của họ đặc trưng về cấp recording, rồi tính lại metric. Rẻ, và mở khóa mọi so sánh giữa hai họ.
2. Đánh dấu loại bốn dòng CNN dừng sớm trong `05_WITHIN_CAMPAIGN_LORO_RESULTS.csv`.
3. Tra nhật ký thí nghiệm để chốt ánh xạ `B1`, `B2`, `B3`.
4. Xác nhận sensor mode cho ResNet1D và 1D-CNN, đóng hạng mục Gate 1 tương ứng.
5. Chạy ResNet1D và 1D-CNN đủ 6 fold LORO mỗi campaign với ít nhất ba seed. Đây là việc duy nhất tốn tài nguyên tính toán, và nó biến quan sát ở Bảng 9 thành bằng chứng.
6. Nâng permutation lên tối thiểu 1.000 hoán vị cho các fold dùng làm bằng chứng chính.

**Evidence Gate kế tiếp có gần hơn không.** Có, và gần hơn đáng kể. Trước phiên này, ba trong năm điều kiện Gate 1 không có artefact nào. Nay điều kiện leakage-safe run-aware evaluation có artefact đầy đủ, điều kiện ResNet1D provenance có artefact và chỉ còn chờ xác nhận sensor mode, và điều kiện run/fold uncertainty có dữ liệu để tính. Hai điều kiện còn thiếu là canonical run registry đã khóa với chữ ký nghiệm thu, và multi-seed. Gate 1 vẫn `OPEN — PARTIAL EVIDENCE`.

---

## 10. Tài liệu tham khảo

[1] E. Combrisson and K. Jerbi, "Exceeding chance level by chance: the caveat of theoretical chance levels in brain signal classification and statistical assessment of decoding accuracy," *Journal of Neuroscience Methods*, 2015. doi: 10.1016/j.jneumeth.2015.01.010.

[2] M. Ojala and G. C. Garriga, "Permutation tests for studying classifier performance," 2009/2010. *Ghi chú kiểm soát: bản hội thảo 2009 và bản tạp chí 2010 đang có xung đột phiên bản trong evidence register và phải tách trước khi trích dẫn chính thức.*

[3] E. Ramasso, R. de Oliveira Teloli, and R. Marcel, "On the condition monitoring of bolted joints through acoustic emission and deep transfer learning: generalization, ordinal loss, and super-convergence," *Structural Health Monitoring*, vol. 24, no. 4, pp. 2536–2558, 2025. doi: 10.1177/14759217241259668.

[4] M. R. W. Brake, C. W. Schwingshackl, and P. Reuß, "Observations of variability and repeatability in jointed structures," *Mechanical Systems and Signal Processing*, vol. 129, pp. 282–307, 2019. doi: 10.1016/j.ymssp.2019.04.020.

[5] A. I. Ozdagli and X. Koutsoukos, "Domain adaptation for structural health monitoring," in *Annual Conference of the PHM Society*, vol. 12, no. 1, art. 9, 2020. doi: 10.36001/phmconf.2020.v12i1.1184.

[6] C. Beleites, U. Neugebauer, T. Bocklitz, C. Krafft, and J. Popp, "Sample size planning for classification models," *Analytica Chimica Acta*, 2013. doi: 10.1016/j.aca.2012.11.007.

[7] D. R. Roberts et al., "Cross-validation strategies for data with temporal, spatial, hierarchical, or phylogenetic structure," *Ecography*, vol. 40, no. 8, pp. 913–929, 2017. doi: 10.1111/ecog.02881.

[8] J. P. Vieira, V. A. Bauler, R. K. Rosa, and D. Silva, "Towards a more realistic evaluation of machine learning models for bearing fault diagnosis," *Mechanical Systems and Signal Processing*, vol. 258, art. 114640, 2026. doi: 10.1016/j.ymssp.2026.114640.

[9] S. Kapoor and A. Narayanan, "Leakage and the reproducibility crisis in machine-learning-based science," *Patterns*, vol. 4, no. 9, art. 100804, 2023. doi: 10.1016/j.patter.2023.100804.

[10] C. Guo, G. Pleiss, Y. Sun, and K. Q. Weinberger, "On calibration of modern neural networks," in *Proc. 34th International Conference on Machine Learning*, PMLR 70, pp. 1321–1330, 2017. *Trích dẫn cho lý do vì sao ROC-AUC và macro-F1 tách rời nhau ở Campaign 3, và vì sao đầu ra mô hình được gọi là model score chứ không phải confidence.*

---

**Hết báo cáo.** Mọi con số trong tài liệu này truy được về một file cụ thể trong `OUTPUT_18.08.2026`. Không con số nào được suy diễn, làm tròn có lợi, hay lấy từ tài liệu tường thuật.
