

### Working title

**Run-Aware Evaluation of Sensor Configurations for Vibration-Based Classification of Controlled Connection States in a Scaled Bolted Steel Frame**


# 4. ABSTRACT — SƠ BỘ DỰA TRÊN KẾT QUẢ CŨ

> **PRELIMINARY ABSTRACT — phải viết lại sau final run-aware analysis.**


# 1. INTRODUCTION

## 1.1. Bối cảnh quản lý tài sản

Nhà công nghiệp khung thép phụ thuộc nhiều vào sự làm việc ổn định của các liên kết bu lông. Dữ liệu dao động có thể phản ánh sự thay đổi của đáp ứng kết cấu, nhưng bản thân tín hiệu chưa tạo ra thông tin đủ để hỗ trợ kiểm tra hoặc quản lý tài sản. Giá trị của hệ thống giám sát phụ thuộc vào khả năng chuyển dữ liệu đo thành **condition evidence** có thể kiểm tra nguồn gốc, đánh giá độ tin cậy và liên kết với cấu kiện trong các bước nghiên cứu tiếp theo.

Trong bối cảnh này, hiệu năng phân loại không chỉ do thuật toán quyết định. Số lượng cảm biến, vị trí đặt cảm biến, kênh đo và cách tổ chức dữ liệu có thể giới hạn lượng thông tin mà bất kỳ model nào tiếp nhận được. Vì vậy, cấu hình cảm biến phải được xem là một biến thiết kế nghiên cứu thay vì một điều kiện nền cố định.

## 1.2. Vấn đề rò rỉ dữ liệu và đơn vị độc lập

Một recording dao động thường được chia thành nhiều window. Các window từ cùng một recording hoặc cùng một replicate group không phải các thí nghiệm độc lập. Nếu window được chia ngẫu nhiên vào train và test, model có thể tiếp cận các mẫu tín hiệu rất giống nhau từ cùng nguồn đo, dẫn đến performance biểu kiến cao hơn khả năng tổng quát hóa thực tế.

Do đó, đơn vị split phải được xác định ở cấp nguồn tín hiệu độc lập trước khi windowing. Preprocessing có tham số học từ dữ liệu phải được fit trên training groups. Mọi cấu hình cảm biến và model family phải được đánh giá trên cùng các held-out groups.

## 1.3. Khoảng trống nghiên cứu

Nghiên cứu hiện có đã chứng minh khả năng sử dụng vibration data và machine learning cho nhận dạng trạng thái kết cấu. Tuy nhiên, trong phạm vi evidence base đã rà soát, vẫn thiếu nghiên cứu đồng thời kết hợp:

- nhiều trạng thái liên kết có kiểm soát trên khung thép bu lông;
- đánh giá theo nhóm nguồn độc lập;
- split-before-windowing và train-only preprocessing;
- so sánh cấu hình cảm biến trên common folds;
- so sánh traditional ML và deep learning trong cùng protocol;
- báo cáo uncertainty ở cấp held-out group;
- kiểm tra empirical null bằng permutation bảo toàn cấu trúc thí nghiệm.

## 1.4. Mục tiêu

Nghiên cứu nhằm:

1. mô tả và quản trị dữ liệu dao động thí nghiệm theo cấu trúc run/replicate-aware;
2. đánh giá khả năng phân biệt bốn trạng thái liên kết;
3. so sánh S1, S2 và S1+S2 trên cùng các nhóm giữ lại;
4. so sánh Logistic Regression, SVM, Random Forest, 1D-CNN và ResNet1D;
5. đánh giá độ ổn định, confusion patterns và empirical-null;
6. rút ra hàm ý có điều kiện cho thiết kế hệ thống quan trắc.

## 1.5. Đóng góp dự kiến

- Một case study có kiểm soát về ảnh hưởng đồng thời của sensor configuration và model family.
- Một protocol đánh giá chống leakage dựa trên independent groups.
- Một evidence-quality profile gồm khả năng phân biệt, độ ổn định, class-specific performance và robustness.
- Một diễn giải thận trọng về giá trị của kết quả phân loại đối với thiết kế hệ thống quan trắc, không mở rộng sang chẩn đoán hiện trường.

---

# 2. RELATED WORK

## 2.1. Vibration-based classification of controlled connection states

Phần này tổng hợp các nghiên cứu sử dụng dữ liệu dao động để phát hiện hoặc phân loại thay đổi liên kết, ưu tiên các nghiên cứu có specimen thí nghiệm, repeated measurements và trạng thái liên kết bu lông. Cần phân biệt rõ:

- bằng chứng trực tiếp trên steel frames hoặc bolted connections;
- bằng chứng từ bridge, bearing hoặc rotating machinery chỉ dùng cho phương pháp;
- nghiên cứu numerical-only không được dùng để chứng minh tính hợp lệ của kết quả thí nghiệm hiện tại.

Các nguồn dự kiến: Zhang et al.; Eraliev et al.; Valdez-Yepez et al.; Avci et al.

## 2.2. Data leakage và group-aware evaluation

Tổng hợp các lập luận về:

- source-group separation;
- split-before-segmentation;
- train-only normalization;
- grouped cross-validation;
- effective sample size;
- nguy cơ dùng số window như independent sample size.

Các nguồn dự kiến: Matania et al.; Wheat et al.; Tougui et al.; Beleites et al.

## 2.3. Sensor configuration và model-family comparison

Phần này làm rõ rằng sensor placement, sensor count và input-channel structure có thể ảnh hưởng đến classification performance. Đóng góp của Paper 1 không phải optimal sensor placement mà là **fair comparative evaluation of available configurations**.

## 2.4. Small-group uncertainty và empirical null

Với số nhóm độc lập nhỏ, nghiên cứu không nên dựa vào p-value từ các window hoặc coi LORO folds là các dataset độc lập. Nên ưu tiên:

- báo cáo từng held-out group;
- median, range và IQR;
- paired differences;
- full-pipeline block-preserving permutation;
- sensitivity analyses.

Nguồn dự kiến: Combrisson and Jerbi; Ojala and Garriga; Demšar; Beleites.

## 2.5. Literature-gap matrix

| Nghiên cứu | Steel/bolted relevance | Independent grouping | Leakage control | Sensor comparison | Common folds | Group-level uncertainty |
|---|---|---|---|---|---|---|
| Zhang et al. | Direct | Partial | Chưa rõ | Không | Không | Hạn chế |
| Matania et al. | Methodological | Có | Có | Không | Có | Hạn chế |
| Wheat et al. | Methodological | Có | Có | Có | Có | Một phần |
| Tougui et al. | Methodological | Có | Có | Không | Có | Một phần |
| Paper 1 hiện tại | Direct laboratory case | Dự kiến replicate-aware | Split-before-windowing | S1/S2/S1+S2 | Có | Per-group + empirical null |
---

# 3. EXPERIMENTAL PROGRAMME

## 3.1. Mô hình

Mô hình thực nghiệm là khung thép liên kết bu lông thu nhỏ, tỷ lệ danh nghĩa 1:10. Bản thảo cuối phải mô tả:

- hình học tổng thể;
- tiết diện cấu kiện;
- vật liệu;
- điều kiện biên;
- cấu tạo liên kết;
- vị trí cảm biến;
- quy trình tạo và khôi phục trạng thái.

Không tuyên bố dynamic similitude hoặc quantitative transfer sang công trình thực nếu chưa có hồ sơ thiết kế đồng dạng và kiểm chứng riêng.

### Hình 1. Specimen và vị trí cảm biến

**Mô tả hình cần tạo:**

- ảnh hoặc bản vẽ specimen có kích thước chính;
- ký hiệu S1 tại apex;
- ký hiệu S2 tại beam–column joint;
- vị trí apex, beam–column và brace connections;
- chú thích chiều đo và phương cảm biến;
- không thể hiện giá trị hoặc đặc tính chưa xác minh.

## 3.2. Controlled connection states

### Bảng 1. Các trạng thái liên kết có kiểm soát

| Mã | Tên trạng thái | Nhãn dữ liệu thô | Vị trí | Cách tạo trạng thái | Cách xác nhận | Quy trình reset |
|---|---|---|---|---|---|---|
| H | Healthy/reference | Healthy | Toàn khung | `[Thầy sẽ bổ sung]` | `[Thầy sẽ bổ sung]` | `[Thầy sẽ bổ sung]` |
| A | Apex connection state | Đỉnh/Dinh | Apex | `[Thầy sẽ bổ sung]` | `[Thầy sẽ bổ sung]` | `[Thầy sẽ bổ sung]` |
| BC | Beam–column connection state | Nút/Nut | Beam–column joint | `[Thầy sẽ bổ sung]` | `[Thầy sẽ bổ sung]` | `[Thầy sẽ bổ sung]` |
| BR | Brace connection state | Giằng/Giang | Brace connection | `[Thầy sẽ bổ sung]` | `[Thầy sẽ bổ sung]` | `[Thầy sẽ bổ sung]` |

Các state là **categorical controlled conditions**, không phải bốn mức severity.

## 3.3. Excitation protocol

### Bảng 2. Thông số kích động

| Excitation_ID | Loại kích động | Vị trí tác động | Thời lượng | Số lần lặp | Trạng thái xác minh |
|---|---|---|---:|---:|---|
| E1 | `[điền]` | `[điền]` | `[điền]` | 6 sơ bộ | Chưa khóa |
| E2 | `[điền]` | `[điền]` | `[điền]` | 6 sơ bộ | Chưa khóa |
| E3 | `[điền]` | `[điền]` | `[điền]` | 6 sơ bộ | Chưa khóa |

Cấu trúc sơ bộ hiện tại là:

```text
4 states × 3 excitation conditions × 6 replicate groups = 72 recordings
```

Cấu trúc này phải được xác nhận bằng run registry.

## 3.4. Sensors and configurations

### Bảng 3. Metadata cảm biến

| Sensor_ID | Model | Dải đo | Độ nhạy | Trục đo | Vị trí | Sampling rate | Đồng bộ |
|---|---|---|---|---|---|---:|---|
| S1 | `[điền]` | `[điền]` | `[điền]` | `[điền]` | Apex | 100 Hz sơ bộ | `[điền]` |
| S2 | `[điền]` | `[điền]` | `[điền]` | `[điền]` | Beam–column joint | 100 Hz sơ bộ | `[điền]` |

Ba cấu hình:

- **S1:** chỉ sử dụng kênh S1;
- **S2:** chỉ sử dụng kênh S2;
- **S1+S2:** sử dụng đồng thời hai kênh.

Chỉ sử dụng cụm từ **Low-Cost** trong title nếu model và phân khúc thiết bị được xác minh.

## 3.5. Preliminary dataset summary

### Bảng 4. Tóm tắt dữ liệu sơ bộ

| Chỉ tiêu | Giá trị sơ bộ |
|---|---:|
| Sampling frequency | 100 Hz |
| Số recordings | 72 |
| Số states | 4 |
| Số excitation conditions | 3 |
| Số replicate groups | 6 |
| Window length | 1.024 mẫu |
| Window duration | ≈10,24 s |
| Overlap | 75% |
| Stride | 256 mẫu |
| Tổng windows | 1.149 |
| Train windows R1–R4 | 765 |
| Validation windows R5 | 192 |
| Test windows R6 | 192 |

Phân bố class sơ bộ:

| State | Train | Validation | Test | Tổng |
|---|---:|---:|---:|---:|
| Healthy | 189 | 48 | 48 | 285 |
| Apex | 192 | 48 | 48 | 288 |
| Beam–column | 192 | 48 | 48 | 288 |
| Brace | 192 | 48 | 48 | 288 |

---

# 4. METHODS

## 4.1. Data hierarchy và independent unit

### Bảng 5. Cấu trúc phân cấp dữ liệu

| Cấp | Định danh | Định nghĩa làm việc | Vai trò |
|---|---|---|---|
| File | `File_ID` | File tín hiệu vật lý | Lưu trữ và checksum |
| Recording | `Recording_ID` | Một lần thu tín hiệu cho một state–excitation–replicate | Đơn vị đo |
| Replicate group | `Replicate_Group_ID` | Nhóm R1…R6, dự kiến chứa đủ 4 states × 3 excitations | Đơn vị split và inference |
| Window | `Window_ID` | Đoạn cắt từ recording | Derived observation |

**Giả định làm việc cần xác minh:**  
Mỗi `Replicate_Group_ID` chứa 12 recordings, gồm 4 states × 3 excitation conditions. Nếu run registry xác nhận cấu trúc này, final evaluation sử dụng Leave-One-Replicate-Group-Out.

## 4.2. Preliminary split và final evaluation

### Preliminary single split

```text
Train: R1–R4
Validation: R5
Test: R6
```

Kết quả hiện có trong Section 9 đến từ split này.

### Final protocol

```text
6 common held-out replicate groups
→ split group before windowing
→ train-only preprocessing
→ identical folds across sensor configurations and models
→ per-group predictions and metrics
→ paired sensor/model contrasts
```

## 4.3. Windowing và preprocessing

### Bảng 6. Quy trình xử lý

| Bước | Preliminary setting | Final requirement |
|---|---|---|
| Windowing | 1.024 samples; 75% overlap | Thực hiện sau group split |
| Scaling | Chưa audit đầy đủ | Fit trên training groups only |
| Traditional feature extraction | Khoảng 140 features/kênh | Khóa feature list và code version |
| Dual-sensor features | Nối đặc trưng hai kênh | Giữ cùng feature logic |
| Deep-model input | Raw `C × 1024` | Giống nhau giữa common folds |
| Hyperparameter tuning | Theo bản cũ | Chung budget và training-data only |
| Early stopping | Validation macro-F1 | Không sử dụng held-out group |

## 4.4. Aggregation từ window đến recording

Để condition evidence có ý nghĩa ở cấp nguồn đo, final analysis nên sử dụng:

```text
Window predictions
→ recording-level majority vote
→ held-out-group confusion and metrics
```

**Primary final result:** recording-level prediction bằng majority vote.  
**Sensitivity analysis:** mean class probability khi model hỗ trợ probability output phù hợp.

Window-level metrics có thể báo cáo ở Supplementary Material nhưng không được dùng để phóng đại effective sample size.

## 4.5. Traditional machine-learning models

- Logistic Regression: linear baseline.
- SVM with RBF kernel: nonlinear margin-based baseline.
- Random Forest: ensemble model sử dụng hand-crafted features.

Final comparison phải khóa:

- hyperparameter space;
- tuning budget;
- random seeds;
- class weighting;
- probability settings nếu có;
- code/library versions.

## 4.6. 1D-CNN

Kiến trúc sơ bộ:

| Thành phần | Cấu hình sơ bộ |
|---|---|
| Input | `C × 1024`, C = 1 hoặc 2 |
| Conv blocks | 4 blocks |
| Filters | 32 → 64 → 128 → 256 |
| Kernel | 5 trong bản paper cũ |
| Pooling | Max pooling + adaptive average pooling |
| Classifier | Dense layers, khoảng 49.924 classifier parameters theo báo cáo IT |
| Optimizer | Adam |
| Weight decay | Không |
| Dropout | Báo cáo IT cho biết dropout thực tế = 0.0 |
| Loss | Cross-entropy |
| Early stopping | Validation macro-F1 |

## 4.7. ResNet1D

Báo cáo SV IT ghi nhận:

- mỗi residual block gồm 3 lớp Conv1D và shortcut;
- kernel sizes 8/5/3;
- Global Average Pooling;
- một lớp Linear cuối;
- classifier khoảng 1.028 parameters;
- AdamW với `weight_decay = 1e-3`.

Về mặt kiến trúc, ResNet1D có cơ sở để giảm overfitting so với 1D-CNN cũ. Tuy nhiên, ResNet1D chỉ được đưa vào main Results khi có đủ:

- sensor mode;
- input channels;
- common folds;
- seeds;
- preprocessing;
- checkpoint hash;
- code version;
- final per-group macro-F1.

Trạng thái hiện tại:

> **PENDING PROVENANCE VERIFICATION**

## 4.8. Metrics và Evidence Quality Profile

### Primary metrics

- recording-level macro-F1 theo held-out replicate group;
- balanced accuracy;
- per-class precision, recall và F1.

### Evidence Quality Profile

| Chiều đánh giá | Chỉ báo |
|---|---|
| Khả năng phân biệt | Macro-F1, balanced accuracy |
| Chất lượng từng state | Precision, recall, F1 |
| Độ ổn định | Median, range/IQR qua held-out groups |
| Ảnh hưởng cảm biến | Paired per-group differences |
| Ảnh hưởng model | Common-fold model contrasts |
| Vượt mức ngẫu nhiên | Empirical-null analysis |
| Độ bền | Overlap, seed và exclusion sensitivity |
| Provenance | Group, seed, model config, code version |

Không tạo một chỉ số tổng hợp dạng Health Index hoặc DSI.

## 4.9. Small independent n

Với sáu replicate groups:

- báo cáo toàn bộ kết quả của từng held-out group;
- ưu tiên median, range và IQR;
- không coi 1.149 windows là independent sample size;
- không bootstrap individual windows;
- không dùng Wilcoxon/Friedman trên overlapping LORO folds làm bằng chứng chính;
- statistical power thấp phải được nêu trong Limitations.

## 4.10. Empirical-null analysis

Nếu run registry xác nhận mỗi `Replicate_Group_ID` chứa đủ bốn states dưới từng excitation, đề xuất:

```text
Giữ nguyên replicate và excitation blocks
→ hoán vị State_Code giữa bốn recordings trong mỗi replicate × excitation block
→ chạy lại full preprocessing–training–evaluation pipeline
→ thu null statistic
```

### Bảng 7. Đặc tả permutation

| Thành phần | Quyết định đề xuất |
|---|---|
| Đơn vị mang nhãn | Recording |
| Blocking factors | Replicate group × excitation |
| Hoán vị | State labels trong từng block |
| Statistic | Median held-out-group macro-F1 |
| Số permutations | 499 hoặc 999 |
| Empirical p-value | `(b + 1) / (B + 1)` |
| Full pipeline rerun | Có |

Thiết kế cuối phải được phê duyệt sau khi khóa registry.

### Hình 2. Run-aware evaluation pipeline

**Mô tả hình cần tạo:**

```text
Locked replicate-group registry
→ hold out one complete replicate group
→ segment training recordings
→ fit preprocessing on training groups
→ tune/train models
→ transform held-out recordings
→ aggregate window predictions to recording level
→ calculate held-out-group metrics
→ repeat across all groups
```

---

# 5. RESULTS (theo số liệu cũ)

## 5.1. Overall model × sensor-configuration performance

### Bảng 8. Macro-F1 trên test group R6 (bổ sung Resnet1D)

| Sensor configuration | Random Forest | SVM | 1D-CNN | Logistic Regression |
|---|---:|---:|---:|---:|
| S1 | 0,869 | 0,546 | 0,641 | 0,541 |
| S2 | 0,841 | 0,838 | 0,764 | 0,620 |
| S1+S2 | 0,862 | 0,765 | 0,841 | 0,716 |

### Nhận xét sơ bộ

Kết quả cho thấy ảnh hưởng của sensor configuration phụ thuộc vào model family:

- Random Forest tương đối ổn định giữa các cấu hình, với macro-F1 dao động từ 0,841 đến 0,869.
- 1D-CNN nhạy với cấu hình đầu vào, tăng từ 0,641 ở S1 lên 0,841 ở S1+S2.
- SVM đạt kết quả cao nhất ở S2, không phải S1+S2.
- Logistic Regression cải thiện dần từ S1 đến S1+S2 nhưng vẫn là model yếu nhất.

Do đó, số liệu sơ bộ không ủng hộ một cấu hình cảm biến tốt nhất cho mọi model. Phát hiện quan trọng hơn là **sensor–model interaction**.

### Hình 3. Macro-F1 của bốn model dưới ba cấu hình

**Mô tả hình hiện tại:**

- grouped bar chart;
- trục X: model;
- trục Y: macro-F1;
- ba nhóm màu: S1, S2, S1+S2;
- gắn nhãn `PRELIMINARY SINGLE-SPLIT`.

**Hình final:** thay bằng dot/connected-points plot theo held-out group.

## 5.2. Preliminary sensor-configuration contrasts

### Bảng 9. Chênh lệch single-split (bổ sung Resnet)

| Model | So sánh | Chênh lệch macro-F1 |
|---|---|---:|
| Random Forest | S1+S2 − S1 | −0,007 |
| Random Forest | S1+S2 − S2 | +0,021 |
| SVM | S1+S2 − S1 | +0,219 |
| SVM | S1+S2 − S2 | −0,073 |
| 1D-CNN | S1+S2 − S1 | +0,200 |
| 1D-CNN | S1+S2 − S2 | +0,077 |
| Logistic Regression | S1+S2 − S1 | +0,175 |
| Logistic Regression | S1+S2 − S2 | +0,096 |

Các giá trị này là chênh lệch của một test group, không phải paired effect qua các groups. Final Results phải bổ sung:

- median paired difference;
- range/IQR;
- số held-out groups cùng chiều;
- effect-size description;
- sensitivity analysis.

## 5.3. Model-family comparison (bổ sung resnet)

Trên cấu hình S1+S2, thứ tự sơ bộ là:

```text
Random Forest 0,862
> 1D-CNN 0,841
> SVM 0,765
> Logistic Regression 0,716
```

Khoảng cách RF–1D-CNN chỉ là 0,021 dưới S1+S2, trong khi khoảng cách này lớn hơn ở S1. Điều đó cho thấy dual-channel input có thể giúp deep model khai thác thêm thông tin. Tuy nhiên, RF đạt mức cao tương đối ổn định ngay cả với một sensor, trong khi 1D-CNN thể hiện độ nhạy lớn hơn với cấu hình.

## 5.4. Per-class performance dưới S1+S2

### Bảng 10. Per-class F1 dưới S1+S2

| State | Random Forest | 1D-CNN |
|---|---:|---:|
| Healthy | 0,917 | 0,911 |
| Apex | 0,792 | 0,800 |
| Beam–column | 0,833 | 0,758 |
| Brace | 0,903 | 0,852 |

Healthy và Brace có F1 cao hơn Apex và Beam–column ở cả hai model. 1D-CNN nhỉnh hơn RF ở Apex nhưng thấp hơn ở Beam–column và Brace. Đây là bằng chứng sơ bộ rằng model ranking có thể thay đổi theo class.

## 5.5. Per-class sensitivity của 1D-CNN theo sensor configuration

### Bảng 11. Per-class F1 của 1D-CNN

| Configuration | Healthy | Apex | Beam–column | Brace |
|---|---:|---:|---:|---:|
| S1 | 0,753 | 0,632 | 0,700 | 0,753 |
| S2 | 0,733 | 0,685 | 0,475 | 0,708 |
| S1+S2 | 0,911 | 0,800 | 0,758 | 0,852 |

Kết quả sơ bộ cho thấy:

- S1+S2 cải thiện cả bốn class so với S1;
- Beam–column giảm mạnh dưới S2, với F1 = 0,475;
- Healthy đạt F1 cao nhất dưới S1+S2;
- các state phản ứng khác nhau trước thay đổi cấu hình cảm biến.

### Hình 4. Per-class F1 của 1D-CNN

**Mô tả hình:**

- grouped bars theo H, A, BC và BR;
- ba cấu hình S1, S2 và S1+S2;
- nhãn `PRELIMINARY SINGLE-SPLIT`;
- final version phải thể hiện uncertainty qua held-out groups.

## 5.6. Confusion patterns

Bản paper cũ báo cáo định tính rằng cặp nhầm chính là:

```text
Apex ↔ Beam–column
```

Chưa có retained prediction matrix nên chưa thể xác minh số lượng hoặc tỷ lệ nhầm.

### Hình 5. Confusion matrices

**Mô tả hình final:**

- một matrix cho mỗi sensor configuration và model được chọn;
- class order cố định H–A–BC–BR;
- cung cấp cả count và row-normalized version;
- cùng scale;
- per-group matrices đưa vào Supplementary Material;
- không cố định trước A↔BC nếu final predictions cho kết quả khác.

Mọi giải thích cơ học chỉ được ghi:

> **hypothesis, not confirmed.**

## 5.7. ResNet1D

Báo cáo SV IT nhận xét ResNet1D có convergence và generalization tốt hơn 1D-CNN trong thử nghiệm hiện tại. Các nguyên nhân kiến trúc được đề xuất gồm:

- shortcut connections;
- Global Average Pooling;
- classifier nhỏ hơn;
- AdamW và weight decay;
- kernel sizes phù hợp hơn với dataset nhỏ.

Tuy nhiên, chưa có bảng macro-F1 đầy đủ, sensor mode và common-fold provenance. Vì vậy:

- không đưa ResNet1D vào bảng so sánh số chính;
- chỉ mô tả như candidate model;
- chỉ kết luận sau khi chạy cùng folds, seeds và preprocessing.

## 5.8. Kết quả còn thiếu

### Bảng 12. Final held-out-group results

| Held-out group | Model | S1 macro-F1 | S2 macro-F1 | S1+S2 macro-F1 | Balanced accuracy |
|---|---|---:|---:|---:|---:|
| R1 |  |  |  |  |  |
| R2 |  |  |  |  |  |
| R3 |  |  |  |  |  |
| R4 |  |  |  |  |  |
| R5 |  |  |  |  |  |
| R6 |  |  |  |  |  |
| Median |  |  |  |  |  |
| Range/IQR |  |  |  |  |  |

### Bảng 13. Empirical-null và sensitivity

| Analysis | Observed result | Alternative/null result | Effect on conclusion |
|---|---:|---:|---|
| Block-preserving permutation |  |  |  |
| Non-overlapping windows |  |  |  |
| Seed sensitivity |  |  |  |
| Exclusion of quality-flagged group |  |  |  |

---

# 6. DISCUSSION — DỰ THẢO HOÀN CHỈNH THEO KẾT QUẢ CŨ

## 6.1. Sensor configuration và model family tương tác với nhau

Kết quả sơ bộ cho thấy ảnh hưởng của cấu hình cảm biến không đồng nhất giữa các model. Random Forest duy trì macro-F1 trong khoảng hẹp 0,841–0,869 và đạt giá trị cao nhất với S1. Ngược lại, 1D-CNN tăng từ 0,641 với S1 lên 0,841 với S1+S2. SVM lại đạt mức cao nhất với S2 và giảm khi sử dụng S1+S2. Logistic Regression cải thiện khi bổ sung kênh thứ hai nhưng vẫn thấp hơn các model phi tuyến.

Mẫu kết quả này cho thấy không nên tách riêng quyết định lựa chọn cảm biến khỏi lựa chọn model. Một cấu hình giàu thông tin đối với một kiến trúc chưa chắc tạo cùng mức cải thiện đối với kiến trúc khác. Do đó, đóng góp trung tâm của Paper 1 nên được định vị là **joint evaluation of sensor configuration and model family**, thay vì cố chứng minh dual sensing luôn tốt hơn hoặc một model luôn vượt trội.

Giới hạn quan trọng là kết quả hiện tại chỉ đến từ test group R6. Final LORO/LOGO có thể thay đổi ranking. Vì vậy, claim cuối phải dựa trên median paired differences và số held-out groups có cùng xu hướng.

## 6.2. Random Forest là baseline mạnh trong điều kiện dữ liệu nhỏ

Random Forest đạt macro-F1 cao nhất hoặc gần cao nhất trong cả ba cấu hình sơ bộ. Kết quả này phù hợp với đặc tính của ensemble tree models trong bối cảnh feature engineering có cấu trúc và số nguồn đo độc lập nhỏ. Random Forest có khả năng giảm variance thông qua bagging và không phụ thuộc vào một classifier nhiều tham số.

Ngược lại, 1D-CNN cũ có khoảng 49.924 parameters ở classifier, trong khi số independent replicate groups rất nhỏ. Mặc dù có 765 training windows, các window này bắt nguồn từ số recording và replicate hữu hạn, nên không thể được xem là 765 thí nghiệm độc lập. Báo cáo SV IT cũng cho thấy dropout của 1D-CNN bằng 0.0 và optimizer không sử dụng weight decay, làm tăng nguy cơ overfitting.

Tuy nhiên, kết quả không chứng minh RF luôn tốt hơn deep learning. Khoảng cách RF–1D-CNN giảm còn 0,021 dưới S1+S2. Điều này cho thấy deep model có thể khai thác hiệu quả hơn khi input chứa đủ thông tin không gian. Claim phù hợp là:

## 6.3. ResNet1D là hướng cải thiện hợp lý nhưng chưa phải kết quả chính

ResNet1D sử dụng residual connections, Global Average Pooling, classifier nhỏ và AdamW với weight decay. Các lựa chọn này có cơ sở để cải thiện convergence và giảm overfitting so với 1D-CNN cũ. Báo cáo SV IT nhận định ResNet1D tốt hơn 1D-CNN về hội tụ và tổng quát hóa trong thử nghiệm hiện tại.

Tuy nhiên, chưa có đủ provenance để biến nhận xét này thành claim học thuật. Sensor mode, input channels, folds, seeds, preprocessing và checkpoint phải được khóa. Nếu ResNet1D đạt kết quả tốt hơn dưới final common folds, Discussion có thể giải thích sự cải thiện bằng:

- residual feature reuse;
- reduced classifier complexity;
- Global Average Pooling;
- weight regularization.

Nếu kết quả không ổn định, ResNet1D nên được đưa vào Supplementary Material hoặc formally excluded.

## 6.4. Chất lượng dữ liệu có tính phụ thuộc trạng thái

Per-class F1 dưới S1+S2 cho thấy Healthy và Brace được phân biệt tốt hơn Apex và Beam–column. Với 1D-CNN, Beam–column giảm xuống 0,475 dưới S2 và tăng lên 0,758 dưới S1+S2. Apex cũng cải thiện từ 0,632 dưới S1 lên 0,800 dưới S1+S2.

Kết quả này cho thấy một macro-F1 tổng hợp không đủ để mô tả condition evidence. Một cấu hình có thể đạt mức tổng thể chấp nhận được nhưng vẫn thất bại đối với một state cụ thể. Do đó, evidence quality phải được trình bày dưới dạng profile gồm:

- overall macro-F1;
- per-class precision, recall và F1;
- confusion pairs;
- consistency across held-out groups.

Quan sát Apex↔Beam–column có thể liên quan đến sự tương đồng của đáp ứng tại các vị trí liên kết lân cận hoặc độ nhạy của vị trí đo. Đây chỉ là **open mechanical hypothesis**, không phải bằng chứng về stiffness loss hay cơ chế hư hỏng.

## 6.5. Hàm ý cho thiết kế hệ thống quan trắc

Kết quả sơ bộ không cho phép tuyên bố S1+S2 là cấu hình tối ưu. RF đạt kết quả cao nhất với S1, SVM đạt cao nhất với S2, trong khi 1D-CNN và Logistic Regression đạt cao nhất với S1+S2. Điều có thể rút ra là:

> Sensor configuration should be evaluated together with the intended analytical model and the connection states that the monitoring system is expected to distinguish.

Việc bổ sung cảm biến chỉ nên được khuyến nghị khi:

- mức cải thiện xuất hiện nhất quán qua replicate groups;
- state khó phân biệt được cải thiện;
- sensitivity analysis không đảo chiều;
- lợi ích thông tin bổ sung tương xứng với yêu cầu acquisition và processing.

Đây là **resource–information trade-off**, không phải optimal sensor placement.

## 6.6. Đóng góp đối với quản lý tài sản

Paper 1 không tạo ra quyết định kiểm tra hoặc bảo trì. Giá trị quản lý nằm ở việc tạo một lớp condition evidence có:

- provenance dữ liệu;
- cấu hình cảm biến xác định;
- protocol đánh giá rõ;
- chỉ tiêu chất lượng;
- giới hạn diễn giải.

Sau khi final analysis hoàn thành, mỗi output có thể được gán `Condition_Evidence_ID` để Paper 2 liên kết với `BIM_GUID` và `Inspection_Record_ID`. Paper 1 không triển khai chuỗi truy vết đó.

## 6.7. So sánh

So với các nghiên cứu chỉ báo cáo model accuracy trên một sensor layout cố định, Paper 1 làm nổi bật tương tác giữa sensing configuration và model family. So với nghiên cứu dùng random-window split, thiết kế final dự kiến đánh giá theo replicate groups và báo cáo per-group uncertainty. So với nghiên cứu binary damage detection, case study hiện tại sử dụng bốn trạng thái liên kết có kiểm soát.

Không nên so sánh trực tiếp các giá trị F1 với nghiên cứu sử dụng dataset, state definition hoặc split protocol khác. Đóng góp nằm ở cấu trúc đánh giá và insight về sensor–model interaction trong một controlled laboratory case.

## 6.8. Điều final LORO/LOGO có thể làm thay đổi

Final results có thể dẫn đến các kịch bản:

| Kịch bản cuối | Cách điều chỉnh Discussion |
|---|---|
| S1+S2 cải thiện nhất quán | Nhấn mạnh marginal spatial information |
| S1+S2 chỉ cải thiện một số class | Nhấn mạnh class-specific benefit |
| S1 hoặc S2 tốt hơn | Không giữ narrative dual-sensor advantage |
| RF ổn định nhất | Giữ small-data baseline argument |
| ResNet1D vượt RF | Thảo luận architecture và regularization, giới hạn trong protocol |
| Ranking thay đổi giữa groups | Nhấn mạnh uncertainty và không khuyến nghị phổ quát |
| Không vượt empirical null | Định vị bài thành methodological case study và giảm claim |
| Confusion pair khác A↔BC | Viết theo final predictions, bỏ giả thuyết cũ |

---

# 7. LIMITATIONS

1. Kết quả số hiện tại chỉ dựa trên một run-separated single split.
2. Independent unit và run registry chưa được khóa chính thức.
3. Dataset xuất phát từ một specimen phòng thí nghiệm.
4. Sáu replicate groups tạo small independent n.
5. Các window chồng lấn không phải independent observations.
6. Các state là controlled categorical conditions, không phải severity levels.
7. Kết quả có thể phụ thuộc excitation protocol, sensor hardware, mounting và orientation.
8. ResNet1D chưa có đủ provenance để đưa vào primary comparison.
9. Chưa có empirical-null và sensitivity results.
10. Không có field damage validation.
11. Không có quantitative transfer từ mô hình 1:10 sang công trình thực.
12. FEM không được hiệu chuẩn và không dùng để chẩn đoán.
13. External validity hiện còn hạn chế.

---

# 8. CONCLUSIONS — DỰ THẢO ĐẦY ĐỦ THEO KẾT QUẢ CŨ

This study examined how sensor configuration and model family jointly influenced vibration-based classification of four controlled connection states in a nominally scaled bolted steel frame. Under the preliminary run-separated single-split evaluation, the available vibration data produced meaningful but model- and state-dependent laboratory condition evidence. Random Forest yielded comparatively stable macro-F1 values across S1, S2 and S1+S2, ranging from 0.841 to 0.869, while the 1D-CNN was substantially more sensitive to sensing configuration, improving from 0.641 under S1 to 0.841 under S1+S2. The SVM achieved its highest preliminary result under S2 rather than the dual-sensor configuration, indicating that no sensor configuration can yet be considered universally preferable.

Class-level analysis further showed that the quality of condition evidence varied across controlled states. Healthy and Brace achieved the strongest preliminary F1 scores under S1+S2, whereas the Beam–column state was difficult for the 1D-CNN under S2 and improved when both sensor channels were used. The reported Apex–Beam–column confusion remains an observation requiring confirmation from retained final predictions and should be interpreted only as an open mechanical hypothesis.

The preliminary findings support two practical conclusions. First, sensing configuration should be evaluated together with the selected analytical model rather than treated as a fixed background condition. Second, increasing model complexity cannot be assumed to compensate for limited or poorly positioned sensing information. Random Forest currently provides a strong small-data baseline, while ResNet1D remains a promising candidate whose inclusion depends on complete provenance and common-fold evaluation.

These results remain preliminary because they are based on a single held-out replicate group. Final claims must be based on split-before-windowing LORO/LOGO evaluation, recording-level aggregation, common folds, group-level uncertainty, block-preserving permutation and sensitivity analyses. The contribution of Paper 1 is therefore bounded to controlled laboratory condition evidence and does not constitute field damage diagnosis, physical severity estimation, calibrated-FEM interpretation or quantitative lab-to-field transfer.

---

# PHỤ LỤC. DANH MỤC BẢNG VÀ HÌNH CHO BẢN THẢO CUỐI

## 1. Bảng chính

| Số | Nội dung | Trạng thái |
|---:|---|---|
| Table 1 | Controlled connection states | Thầy sẽ bổ sung sau |
| Table 2 | Excitation protocol | Thầy sẽ bổ sung sau |
| Table 3 | Sensor metadata | Thầy sẽ bổ sung sau |
| Table 4 | Dataset summary | Thầy sẽ bổ sung sau |
| Table 5 | Data hierarchy | Cần bổ sung run registry |
| Table 6 | Preprocessing protocol | Cần em audit |
| Table 7 | Model configurations | Chờ hyperparameter/provenance |
| Table 8 | Preliminary macro-F1 | Có kết quả cũ |
| Table 9 | Preliminary sensor contrasts | Có kết quả cũ |
| Table 10 | Per-class F1 under S1+S2 | Có kết quả cũ |
| Table 11 | 1D-CNN per-class F1 by configuration | Có kết quả cũ |
| Table 12 | Final per-held-out-group metrics | Cần em bổ sung |
| Table 13 | Empirical-null and sensitivity | Cần em bổ sung |

## 2. Hình chính

| Số | Nội dung | Yêu cầu |
|---:|---|---|
| Figure 1 | Specimen and sensor locations | Thầy sẽ bổ sung |
| Figure 2 | Run-aware evaluation pipeline | Cần em bổ sung |
| Figure 3 | Preliminary model × sensor macro-F1 | Cần em cập nhật |
| Figure 4 | Final per-group performance | Cần cập nhật |
| Figure 5 | Paired sensor contrasts | Paired plot theo group (cần em cập nhật) |
| Figure 6 | Model × sensor interaction | Heatmap hoặc dot-range (cần cập nhật) |
| Figure 7 | Confusion matrices | Counts + row-normalized (cần cập nhật)|
| Figure 8 | Empirical-null distribution | Null histogram + observed statistic (Cần cập nhật)|

---

# 3. CHECKLIST THAY KẾT QUẢ SƠ BỘ BẰNG FINAL RESULTS

| Nội dung | Hiện tại | Việc phải làm |
|---|---|---|
| Independent unit | Giả định R1…R6 | Khóa run registry |
| Split | R1–R4 / R5 / R6 | Thay bằng common LORO/LOGO folds |
| Windowing | 1024, overlap 0.75 | Audit split-before-windowing |
| Preprocessing | Chưa khóa | Train-only audit |
| Aggregation | Window-level | Chạy recording-level majority vote |
| RF/SVM/LR/CNN config | Một phần | Khóa hyperparameters, seeds |
| ResNet1D | Định tính | Khóa provenance và final metrics |
| Per-group results | Chưa có | Xuất R1…R6 metrics |
| Confusion | Định tính | Xuất retained predictions |
| Empirical null | Chưa có | Block-preserving full-pipeline permutation |
| Sensitivity | Chưa có | Overlap, seed, quality-flagged groups |
| Abstract | Số sơ bộ | Viết lại hoàn toàn |
| Discussion | Theo số sơ bộ | Cập nhật theo per-group evidence |
| Conclusion | Theo số sơ bộ | Cập nhật và giảm/tăng claim theo final results |




