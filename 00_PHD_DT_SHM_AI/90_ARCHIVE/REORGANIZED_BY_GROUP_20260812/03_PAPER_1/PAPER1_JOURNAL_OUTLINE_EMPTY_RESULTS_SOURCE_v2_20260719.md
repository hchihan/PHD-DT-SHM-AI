# ĐỀ CƯƠNG BÀI BÁO QUỐC TẾ — PAPER 1

## Run-Aware Evaluation of Sensor Configurations for Vibration-Based Classification of Controlled Connection States in a Scaled Bolted Steel Frame

**Phiên bản v2 — Phương án A:** bảng kết quả để trống; hình chỉ mô tả yêu cầu; narrative được viết theo dữ liệu cuối.

> Tài liệu này không chứa số liệu giả lập. Mọi bảng kết quả chỉ được điền bằng kết quả cuối đã kiểm toán theo giao thức run-aware.

## 0. Định vị

- RQ1 → WP1 → Chương 4 → Paper 1 → Gate 1.
- Core Scope: chất lượng bằng chứng trạng thái phòng thí nghiệm dưới đánh giá run-aware, leakage-controlled.
- Chuỗi trách nhiệm: `Vibration data → trustworthy laboratory condition evidence`.
- Out of Scope: field diagnosis, severity/DSI, calibrated FEM, RUL, predictive maintenance, lab-to-field classifier transfer.

## Research question

> How reliably can vibration data from different sensor configurations produce evidence distinguishing controlled connection states in a scaled bolted steel frame under a run-aware, leakage-controlled evaluation protocol?

## Đóng góp dự kiến

| Đóng góp phương pháp | Đóng góp kết quả phải được xác nhận bằng dữ liệu cuối |
|---|---|
| Run-aware evaluation với independent-group splitting | Định lượng mức phân biệt trạng thái và độ ổn định giữa các held-out groups |
| Split-before-windowing và train-only preprocessing | Ước lượng hiệu năng trên nguồn chưa xuất hiện trong training và tránh leakage do chia window |
| Common-fold sensor comparison | Định lượng ảnh hưởng của S1, S2, S1+S2 dưới cùng held-out groups |
| Fair model-family comparison | Xác định mức ảnh hưởng của model so với sensor configuration |
| Group-level uncertainty và empirical-null analysis | Đánh giá kết quả có vượt empirical chance và ổn định đến mức nào |
| Confusion-pattern analysis | Xác định lớp/cặp lớp khó phân biệt; mọi diễn giải cơ học là hypothesis, not confirmed |

# 1. Introduction

1. Nhu cầu chuyển vibration data thành condition evidence có thể kiểm toán.
2. Windows cùng nguồn không phải independent experiments.
3. Random-window split có nguy cơ data leakage.
4. Sensor configuration quyết định lượng thông tin trước khi model được áp dụng.
5. Khoảng trống: thiếu common-fold sensor/model comparison + group-level uncertainty trên bolted steel frame.
6. RQ, phạm vi và đóng góp.

# 2. Related Work

- Controlled connection-state classification.
- Data leakage và group-aware evaluation.
- Sensor configuration và model-family comparison.
- Small-group uncertainty và empirical-null analysis.
- Kết thúc bằng literature-gap matrix; dùng “Within the reviewed evidence base…”.

# 3. Experimental Programme

## 3.1. Trạng thái liên kết

| Mã | Tên trạng thái | Mô tả vật lý | Xác nhận/reset |
|---|---|---|---|
| H | Healthy/reference | [Bổ sung] | [Bổ sung] |
| A | Apex connection state | [Bổ sung] | [Bổ sung] |
| BC | Beam–column connection state | [Bổ sung] | [Bổ sung] |
| BR | Brace connection state | [Bổ sung] | [Bổ sung] |

## 3.2. Thu nhận dữ liệu

| Thông số | Giá trị cuối | Nguồn xác minh |
|---|---|---|
| Excitation | [Bổ sung] | Nhật ký thí nghiệm |
| Sampling frequency | [Bổ sung] | Acquisition config |
| Window length | [Bổ sung] | Pipeline code |
| Overlap/stride | [Bổ sung] | Pipeline code |
| Số recordings/files | [Bổ sung] | Manifest |
| Số independent groups | [Bổ sung] | Independent-unit decision |

## 3.3. Independent unit

Phải khóa Recording_ID hay Replicate_Group_ID; thành phần mỗi group; mỗi held-out group có đủ bốn class hay không; LORO hay LOGO; effective n.

# 4. Run-Aware Evaluation Method

1. Split-before-windowing.
2. Train-only preprocessing.
3. Common folds, seeds, tuning budget và metric implementation.
4. Model roster: LR, SVM, RF, 1D-CNN; ResNet1D chỉ include sau khi xác minh provenance.
5. Aggregation: Window probabilities → Recording-level prediction → Held-out-group metrics.
6. Primary metric: macro-F1 ở cấp hợp lệ; secondary: balanced accuracy, precision, recall, per-class F1, confusion matrices.
7. Small-n strategy: report all groups, median, range/IQR; không coi windows là independent n.
8. Empirical-null analysis chỉ chạy sau khi khóa exchangeability/blocking.
9. Sensitivity chính: overlap, seed, exclusion of quality-flagged group.

# 5. Results

Không viết sẵn cấu hình tốt nhất, model tốt nhất, lớp khó nhất hoặc confusion pair.

## 5.1. Dataset summary

Bảng trống: số groups ban đầu/phân tích, groups loại, recordings, states, excitations, sensor configurations, windows.

## 5.2. Group-level evidence quality

Bảng trống theo Held-out group × Sensor config × Model × Macro-F1 × Balanced accuracy.

Hình mô tả: dot plot/connected-points plot; không dùng mean duy nhất để che group khó.

## 5.3. Sensor configuration effect

Bảng trống: model × S1/S2/S1+S2, median[IQR].

Bảng paired effects: S1+S2−S1; S1+S2−S2; S1−S2; median difference; số groups cùng chiều.

## 5.4. Model-family effect

Bảng trống theo sensor config × model × median macro-F1 × range/IQR.

Sensor effect và model effect phải được định nghĩa bằng estimand trước khi so sánh.

## 5.5. Per-class and confusion patterns

Bảng trống: Model × Sensor × State × Precision × Recall × F1 × Support.

Confusion matrices: counts + row-normalized; cùng class order; không hard-code BC↔A.

## 5.6. Empirical null and sensitivity

Bảng trống: permutation unit/block, statistic, B, observed, null summary, empirical p-value.

Bảng sensitivity: overlap, seed, quality-group exclusion.

# 6. Discussion

Viết theo dữ liệu thực:

- Nếu một sensor config tốt hơn nhất quán: nêu magnitude, consistency, class-specific benefit; không gọi optimal.
- Nếu gần tương đương: nêu không có lợi ích ổn định từ sensor addition.
- Nếu model effect lớn hơn: đổi substantive finding theo dữ liệu.
- Nếu sensor effect lớn hơn: chỉ kết luận khi paired estimand xác nhận.
- Nếu confusion pattern ổn định: thảo luận như open hypothesis; không suy luận stiffness loss/preload/severity.
- Nếu biến thiên lớn: nhấn mạnh small-n uncertainty.
- Nếu không vượt empirical chance: định vị thành methodological case study.

# 7. Limitations

One specimen; controlled categorical states; small independent n; excitation/hardware/mounting dependence; windows are derived observations; no severity; no field diagnosis; no quantitative lab-to-field transfer; no calibrated FEM.

# 8. Conclusions

Điền sau final analysis:

1. RQ1: mức phân biệt và ổn định.
2. Sensor configuration effect.
3. Model-family effect.
4. Confusion patterns.
5. Empirical chance.
6. Practical implication có điều kiện.
7. Scope boundary.
8. Một câu nối sang traceability framework của Paper 2.

Không sử dụng số liệu single-split cũ hoặc số liệu chưa audit trong Conclusion.
