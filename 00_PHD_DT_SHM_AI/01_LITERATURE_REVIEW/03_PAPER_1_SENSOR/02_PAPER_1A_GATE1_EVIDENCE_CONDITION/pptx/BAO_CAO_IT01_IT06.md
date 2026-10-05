# Báo cáo kiểm tra IT-01 đến IT-06

Báo cáo trình bày kết quả đối chiếu PAPER1 v7 với dữ liệu nguồn, registry, code và artifact Kaggle. Phạm vi gồm CP1, CP2, CP3; bốn model trong bài và hai model ML bổ sung ở Table A4. Việc kiểm tra sử dụng kết quả đã lưu, không huấn luyện lại hoặc thay đổi lựa chọn model, candidate hay checkpoint.

## IT-01 — Đúng bộ dữ liệu nguồn

### Yêu cầu

Đối chiếu nguồn dữ liệu của từng campaign với registry, cấu hình và artifact đã chạy. Xác định recording bổ sung của CP2 và kiểm tra có trùng nguồn với CP3 hay không.

### Kết luận

**Chưa xác minh được đầy đủ rằng đây chính xác là các file đã được load tại thời điểm training. Phần kiểm tra dữ liệu hiện có đã đạt.**

- **Đã được:** đủ 216 recording, ID toàn cục duy nhất, không trùng đường dẫn/hash nguồn; xác định rõ recording bổ sung CP2 và không thấy trùng nguyên nguồn với CP3. Chuỗi nguồn → canonical → NPZ hiện có khớp; 102 NPZ tải từ Kaggle cũng khớp registry.
- **Chưa được:** xác nhận byte của các file tại thời điểm training. **Vì** artifact không ghi hash từng NPZ lúc load; hash của bản tải hiện tại không bổ sung được bằng chứng lịch sử đó.
- **Cần xử lý:** §4.1 có thể ghi kết quả đối chiếu hiện tại, nhưng phải giữ giới hạn trên. Muốn xác minh thêm cần bản input đã khóa phiên bản hoặc bằng chứng hash gắn với phiên training.

### Chi tiết kiểm tra

**Vị trí trong bài:** §3.4–3.5 và §4.1.

- Registry có **216 recording**, mỗi campaign 72 recording. ID toàn cục được biểu diễn bằng tổ hợp campaign/run/recording vì tên `REC0001` đến `REC0012` được dùng lại trong từng run.
- Có **216 đường dẫn nguồn và 216 SHA-256 nguồn khác nhau**. Hash tính lại của file nguồn và canonical đều khớp registry.
- Dựng lại các window từ CSV canonical cho đủ 216 recording cho kết quả khớp tensor NPZ local. Tổng cộng có **6.899 window**; 951 mẫu cuối không hợp lệ bị cắt ở 149 recording.
- Cả **102 NPZ tải từ Kaggle** khớp hash của bản local và index. Số 102 bao gồm các cấu hình cảm biến khác nhau, không phải 102 recording.
- Recording bổ sung là **CP2/RUN012/REC0004**, trạng thái B1, kích thích BEAT_L1, nguồn `raw/BS1B1L1R12_bo_sung_file_thieu_dot_2.csv`. Đây là recording thay thế trong tổng số 72 của CP2, không phải recording thứ 73.
- Recording bổ sung không trùng nguyên file hoặc toàn bộ mảng gia tốc với CP3. So sánh với 72 recording CP3 không tìm thấy đoạn liên tục 400 mẫu giống hệt; đoạn giống hệt dài nhất là 22 mẫu.

**File bàn giao:** [DATASET_REGISTRY_FINAL.csv](DATASET_REGISTRY_FINAL.csv).

**Bằng chứng:** [Tổng hợp kiểm tra dữ liệu](evidence/DATASET_AUDIT.json), [đối chiếu hash NPZ](evidence/NPZ_HASH_CHECK.csv), [kiểm tra recording bổ sung với CP3](evidence/CP2_SUPPLEMENT_CP3_OVERLAP_CHECK.csv).

## IT-02 — Ánh xạ cảm biến và kênh

### Yêu cầu

Xác định thứ tự kênh, cột dữ liệu, thiết bị và input shape của từng campaign/model từ code/config. Không suy đoán vị trí vật lý cảm biến.

### Kết luận

**Chưa đạt đầy đủ: đã biết từng kênh lấy từ cột nào, nhưng chưa xác nhận được thiết bị vật lý tương ứng.**

- **Đã được:** xác định thứ tự kênh, cột và khối cảm biến trong từng CSV; giải thích được CP1 dùng 8 kênh, CP2/CP3 dùng 12 kênh và input shape của từng model.
- **Chưa được:** serial/device ID và vị trí lắp thực tế. **Vì** tên `apex`, `beam_column`, `brace_column` được code gán bằng gravity fingerprint; chưa có hồ sơ nối khối CSV với thiết bị và vị trí lắp.
- **Cần xử lý:** bổ sung hồ sơ thiết bị nếu muốn xác nhận ánh xạ vật lý; không suy đoán để điền. §3.3/Table 1 cũng cần sửa nguồn gốc resultant: kênh này đã có trong CSV PASCO, không được tính mới bởi dataset builder.

### Chi tiết kiểm tra

**Vị trí trong bài:** §3.3, §4.1 và Figure 1.

Mỗi khối cảm biến cung cấp bốn kênh gia tốc theo thứ tự **x, y, z, resultant**. Cột force có trong CSV nhưng không được đưa vào tensor gia tốc này.

| Campaign | Cấu hình | Số kênh | Input DL | Input RF/SVM sau trích feature |
| --- | --- | ---: | --- | --- |
| CP1 | S12 | 8 | N × 8 × 400 | N × 228 |
| CP2 | S123 | 12 | N × 12 × 400 | N × 366 |
| CP3 | S123 | 12 | N × 12 × 400 | N × 366 |

Trong bảng, N là số window. File ánh xạ có một dòng cho mỗi recording/model/kênh, chỉ rõ cột canonical, cột và khối cảm biến trong CSV nguồn. Cần giữ chi tiết theo recording vì thứ tự khối cảm biến trong file nguồn có thể thay đổi.

Kênh **resultant đã tồn tại trong CSV PASCO nguồn**. Code canonical chép kênh này sang dữ liệu chuẩn hóa cấu trúc; NPZ builder không tính mới resultant từ x, y, z.

**File bàn giao:** [SENSOR_CHANNEL_MAP.csv](SENSOR_CHANNEL_MAP.csv).

**Bằng chứng:** [Báo cáo mapping nguồn](evidence/source_repository/datasets/built/reports/preprocessing/07_sensor_mapping_report.csv), [code gán nhãn bằng gravity fingerprint](evidence/source_repository/datasets/preprocessing_scripts/07_map_sensor_blocks.py).

## IT-03 — Số chiều và định nghĩa đặc trưng

### Yêu cầu

Kiểm tra feature extractor thực tế của RF/SVM, xác định tên, tham số, số feature trên mỗi kênh và tổng số chiều đưa vào model.

### Kết luận

**Được. Đã xác minh định nghĩa feature và số chiều đầu vào thực tế.**

- **Kết quả:** 228 feature cho 8 kênh ở CP1; 366 feature cho 12 kênh ở CP2/CP3. Mỗi kênh có 25 feature, cộng thêm 28 hoặc 66 feature giữa các cặp kênh.
- **Vì sao có thể kết luận:** đã thực thi extractor trên dữ liệu thật và đối chiếu tên/số feature với cấu hình của 360 fit ML; kết quả khớp, không chỉ suy ra từ công thức.
- **Còn cần làm trong bài:** điền 366 chiều vào §3.6/Table A2 thay phần đang để mở. Không còn vướng mắc về số chiều trong phạm vi kiểm tra này.

### Chi tiết kiểm tra

**Vị trí trong bài:** §3.6 và Table A2.

Extractor thực hiện chuẩn hóa z-score riêng cho từng window/kênh, sau đó tính:

| Nhóm | Feature | Số lượng trên mỗi kênh |
| --- | --- | ---: |
| Thời gian | Skewness, excess kurtosis, max absolute value, peak-to-peak, mean absolute difference, zero-crossing rate, q10, q25, q75, q90 | 10 |
| Công suất dải | Công suất tương đối trong 12 nhóm FFT bin sau Hanning window và đặt DC bằng 0 | 12 |
| Phổ | Spectral centroid, spectral entropy, dominant frequency | 3 |
| Tổng theo kênh | Ba nhóm trên | **25** |

Sau các feature theo kênh, code thêm một feature cho mỗi cặp kênh: trung bình tích của hai tín hiệu đã chuẩn hóa.

| Đầu vào | Feature theo kênh | Feature giữa các cặp kênh | Tổng xác nhận |
| --- | ---: | ---: | ---: |
| 8 kênh | 200 | 28 | **228** |
| 12 kênh | 300 | 66 | **366** |

Các tổng này được xác nhận bằng cách thực thi extractor trên dữ liệu thật và đối chiếu tên/số feature trong cấu hình của **360 fit ML** đã lưu. Không chỉ suy ra từ công thức. Centroid và dominant frequency được biểu diễn theo tần số chuẩn hóa với Nyquist, không trực tiếp bằng Hz.

**File bàn giao:** [FEATURE_DEFINITION.csv](FEATURE_DEFINITION.csv).

**Bằng chứng:** [Kết quả thực thi extractor](evidence/FEATURE_SHAPE_CHECK.json), [đối chiếu feature với artifact đã chạy](evidence/SAVED_FEATURE_CHECK.csv), [code extractor](evidence/source_repository/src/lib/ml/features.py).

## IT-04 — Ghép và đồng bộ dữ liệu cảm biến

### Yêu cầu

Xác định pipeline ghép các kênh theo timestamp, sample index, nội suy hay cắt về cùng độ dài; mô tả đúng cách triển khai.

### Kết luận

**Được đối với yêu cầu xác định cách ghép trong code: các kênh được ghép theo hàng/sample index của CSV.**

- **Đã được:** chỉ ra được code đổi thứ tự cột, giữ phần hàng hợp lệ chung và cắt window cùng offset. Không có bước join timestamp, nội suy hoặc hiệu chỉnh trễ giữa cảm biến trong pipeline này.
- **Chưa xác nhận:** PASCO có đồng bộ các thiết bị trước khi xuất CSV như thế nào. **Vì** chưa có hồ sơ thu đo xác nhận bước đó. Đây là giới hạn của kết luận về đồng bộ vật lý, không phải phần còn thiếu trong việc xác định cách ghép của code.
- **Cần xử lý:** §3.6 ghi đúng là ghép theo hàng/index; không gọi bước này là đồng bộ thời gian giữa cảm biến.

### Chi tiết kiểm tra

**Vị trí trong bài:** §3.6.

CSV PASCO nguồn đã chứa các khối cảm biến trên cùng hàng. Code canonical đổi thứ tự cột nhưng giữ quan hệ giữa các giá trị trên hàng đó. NPZ builder lấy các cột gia tốc theo thứ tự header, giữ tiền tố hàng hợp lệ chung cho mọi kênh và cắt window 400 mẫu với bước 200 mẫu trong từng recording.

**Việc ghép diễn ra theo hàng/sample index của CSV.** Không có bước join theo timestamp, nội suy, resample hoặc hiệu chỉnh độ trễ giữa cảm biến trong pipeline đã kiểm tra. Timestamp đầu window được lưu làm metadata, không được dùng để quyết định phép cắt.

Với RUN012, timestamp được tạo tổng hợp liên tục ở 100 Hz; timestamp nguồn được giữ trong `timestamp_original`. Cách tạo timestamp này không căn lại tín hiệu gia tốc và không chứng minh sự đồng bộ vật lý giữa các cảm biến.

**File bàn giao:** [CHANNEL_SYNCHRONISATION_NOTE.md](CHANNEL_SYNCHRONISATION_NOTE.md), có sẵn đoạn tiếng Anh đề xuất cho Methods.

**Bằng chứng:** [Code canonical](evidence/source_repository/datasets/build_canonical.py), [code tạo NPZ](evidence/source_repository/datasets/preprocessing_scripts/15_build_npz.py).

## IT-05 — Đầu ra và cách lựa chọn mô hình

### Yêu cầu

Xác định loại đầu ra của RF/SVM, calibration, random state, metric và cấp dữ liệu dùng chọn DL candidate/checkpoint. Kiểm tra test không tham gia lựa chọn trong từng fit; không chọn lại model.

### Kết luận

**Phần kiểm tra code đã được; chưa đạt tiêu chí “Methods khớp code” vì bản thảo còn mô tả thiếu hoặc chưa đúng.**

- **Đã được:** RF/SVM dùng `predict_proba`, DL dùng softmax; xác định được seed và calibration. Tái hiện đúng 192 candidate đã lưu và 612 checkpoint DL; test metric không tham gia khóa lựa chọn trong từng fit.
- **Chưa đúng trong Methods:** thiếu điều kiện checkpoint chỉ được lưu khi validation loss giảm **và recording-level validation BA > 0.25**; chưa phân biệt loss ở cấp window với BA ở cấp recording. Câu nói test chỉ được đọc sau khi khôi phục checkpoint cũng chưa đúng: code load test trước training, còn test inference diễn ra sau khi khôi phục checkpoint.
- **Vì sao chưa hoàn tất:** các khác biệt trên đã được xác nhận từ code nhưng chưa được sửa trong DOCX. Cần cập nhật §3.7–3.8 và ghi đúng `split_id` làm tie-break cuối. Không cần huấn luyện hoặc chọn lại model.

Kiểm tra này không xóa sự phụ thuộc vào phát triển hyperparameter đã nêu ở §3.9. Phạm vi 192 candidate không bao gồm notebook sensor-subset, nên chưa xác nhận lại con số 294 của kho rộng hơn tại §4.1.

### Chi tiết kiểm tra

**Vị trí trong bài:** §3.7–3.9 và Table A2.

| Model | Đầu ra dùng để tổng hợp recording | Seed và calibration |
| --- | --- | --- |
| RF | `predict_proba` theo window | `random_state=42`; không thêm calibration ngoài estimator |
| SVM-RBF | `predict_proba` từ Pipeline StandardScaler + SVC | `probability=True`, `random_state=42`; probability estimation nội bộ SVC/libsvm |
| 1D-CNN | Softmax của logits theo window | Seed 42, 43, 44 |
| ResNet1D | Softmax của logits theo window | Seed 42, 43, 44 |

Tất cả model lấy trung bình xác suất window trong recording rồi argmax. RF/SVM không tổng hợp decision score hoặc bỏ phiếu trên nhãn window.

Checkpoint DL được lưu khi **window-level validation loss giảm và recording-level validation balanced accuracy > 0.25**. Early stopping dùng patience 10 sau khi đã có checkpoint hợp lệ; số epoch tối đa là 80. Kiểm tra lại history tái hiện đúng metadata checkpoint của **612 fit DL**.

Candidate giữa các split được chọn theo validation BA giảm dần, validation loss tăng dần, rồi chuỗi `split_id` tăng dần khi hòa. Bộ kiểm tra giữ nguyên candidate đã lưu trên Kaggle và tái hiện đúng **192 lựa chọn**. Test metric không nằm trong khóa lựa chọn; các tập run train/validation/test đều tách rời trong **972 fit** được kiểm tra.

**File bàn giao:** [MODEL_OUTPUT_AND_SELECTION.md](MODEL_OUTPUT_AND_SELECTION.md).

**Bằng chứng:** [Kiểm tra từng fit](evidence/RUN_ARTIFACT_CHECK.csv), [đối chiếu candidate](evidence/SELECTION_REPLAY_CHECK.csv), [đối chiếu checkpoint](evidence/CHECKPOINT_REPLAY_CHECK.csv), [cấu hình thực thi](evidence/EXECUTED_CONFIGS.json).

## IT-06 — Tổng hợp prediction và tính thống kê

### Yêu cầu

Kiểm tra window prediction → recording prediction; tính lại pooled Macro-F1, SD_seed, SD_fold và mẫu số `ddof`; đối chiếu bảng trong bài và bổ sung SD còn thiếu khi dữ liệu cho phép.

### Kết luận

**Chưa đạt đầy đủ: đã tính lại được thống kê recording, nhưng còn ba ô số không khớp bản thảo và hai giới hạn bằng chứng.**

- **Đã được:** metric tính từ prediction recording khớp artifact gốc; 469/472 ô đối chiếu với bản thảo khớp trong sai số làm tròn. Đã tính thêm SD còn thiếu khi có đủ dữ liệu seed.
- **Ba ô chưa được:** Table 5 — CP1/RUN006/1D-CNN mean Macro-F1 cần đổi **0.640 → 0.639**; Table A3 — CP1/ResNet1D/B3 F1 đổi **0.871 → 0.870**; Table A3 — CP3/ResNet1D/B3 SD_seed đổi **0.115 → 0.114**. **Vì** tính từ prediction chưa làm tròn cho ra các giá trị bên phải; đã kiểm tra thêm bằng phân số chính xác. Chưa xác minh nguyên nhân tạo ra ba số cũ.
- **Chưa xác nhận từ code xuất cũ:** mẫu số SD_fold. `ddof=1` tái tạo các số trong Tables 4/A4, nhưng chưa tìm thấy script xuất riêng SD_fold của bản thảo. Với SD_seed, `ddof=1` đã được xác nhận từ code báo cáo.
- **Chưa thể tính lại bước mean window từ artifact:** chỉ có xác suất đã tổng hợp ở cấp recording, không có toàn bộ xác suất từng window. Cách mean đã được xác nhận từ code tại commit đã chạy, nhưng thiếu dữ liệu để kiểm tra số học riêng bước đó.

**Cần xử lý:** sửa ba ô số và chỗ nhắc lại F1 0.871 ở §4.5; giữ rõ hai giới hạn bằng chứng trên. Không cần chạy lại model để sửa các thống kê đã tính được.

### Chi tiết kiểm tra

**Vị trí trong bài:** §3.10 và Tables 4–6/A3.

| Đại lượng | Cách tính được kiểm tra |
| --- | --- |
| Recording prediction | Lấy trung bình xác suất các window trong recording, sau đó argmax |
| Pooled Macro-F1 | Tính trên 72 recording gộp từ sáu outer fold trong từng seed, rồi lấy trung bình qua seed |
| SD_seed | Sample SD của metric pooled giữa ba seed, `ddof=1` |
| SD_fold | Sample SD của sáu fold Macro-F1 trong từng seed, rồi lấy trung bình qua seed; `ddof=1` tái tạo các số trong Tables 4/A4 |

Metric tính lại từ prediction recording khớp `scores.json` của các fit đã kiểm tra. Trong **472 ô số đối chiếu với bản thảo**, 469 ô khớp trong sai số làm tròn; ba ô cần sửa:

| Vị trí | Nội dung | Trong bài | Giá trị tính lại | Đúng ở 3 chữ số |
| --- | --- | ---: | ---: | ---: |
| Table 5 | CP1, RUN006, 1D-CNN, mean Macro-F1 | 0.640 | 0.6394841269841269 | **0.639** |
| Table A3 | CP1, ResNet1D, B3 F1 | 0.871 | 0.8704984333374743 | **0.870** |
| Table A3 | CP3, ResNet1D, B3 F1 SD_seed | 0.115 | 0.11448313030084885 | **0.114** |

Các giá trị gần ngưỡng làm tròn này đã được kiểm tra thêm bằng phân số chính xác từ số đếm prediction. Chỗ nhắc lại CP1 ResNet1D B3 F1 ở §4.5 cũng cần đổi từ 0.871 thành 0.870. Chưa xác minh nguyên nhân hình thành ba số cũ.

Phạm vi 472 ô gồm các bảng yêu cầu và phần đối chiếu mở rộng: Table A4, các ô confusion của A7, accuracy/F1 cùng SD của Table 7. Không kiểm tra lại p-value hoặc chạy lại permutation test. Những SD chưa hiển thị nhưng có đủ dữ liệu seed đã được tính và đánh dấu `COMPUTED_NOT_REPORTED` trong bảng bàn giao; các dòng chẩn đoán `ddof=0` cũng được tách riêng.

**File bàn giao:** [METRIC_AGGREGATION_CHECK.csv](METRIC_AGGREGATION_CHECK.csv).

**Bằng chứng:** [Tổng hợp đối chiếu metric](evidence/METRIC_AUDIT.json), [prediction được chọn](evidence/SELECTED_RECORDING_PREDICTIONS.csv), [metric pooled theo seed](evidence/POOLED_METRICS_BY_SEED.csv), [metric theo fold/seed](evidence/FOLD_METRICS_BY_SEED.csv), [metric từng lớp](evidence/CLASS_METRICS_BY_SEED.csv), [kiểm tra làm tròn chính xác](evidence/EXACT_ROUNDING_CHECK.csv).
