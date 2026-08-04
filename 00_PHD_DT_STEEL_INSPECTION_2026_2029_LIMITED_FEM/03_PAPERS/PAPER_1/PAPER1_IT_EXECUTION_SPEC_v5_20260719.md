# PAPER 1 — ĐẶC TẢ THỰC THI CHO SV IT
## Hướng dẫn chạy kết quả, hoàn thiện bảng và hình từ tập dữ liệu đã có

**Phiên bản:** v5 — IT Execution Specification (biên tập theo thống nhất của The Council)
**Ngày:** 19/07/2026
**Tài liệu học thuật gốc:** `PAPER1_Q2_INTEGRATED_OUTLINE_v4`
**Mục đích tài liệu này:** cho SV IT biết **chính xác phải sản xuất gì**, theo **thứ tự nào**, với **định dạng nào**, để thay thế toàn bộ số liệu single-split sơ bộ bằng kết quả run-aware cuối cùng.

---

## ⚠️ ĐỌC TRƯỚC — HAI NGUYÊN TẮC KHÔNG ĐƯỢC VI PHẠM

**Nguyên tắc 1 — VIỆC SỐ MỘT LÀ CHẠY LORO 6-FOLD, KHÔNG PHẢI SINGLE-SPLIT.**
Toàn bộ số liệu hiện có trong outline v4 (Bảng 8–11, macro-F1 = 0,869 / 0,841 / 0,862 …) đến từ **một** phép chia `train R1–R4 / val R5 / test R6`. Đây chỉ là **giàn giáo phát triển**, KHÔNG phải bằng chứng. Bài báo có luận điểm trung tâm là "single-split gây rò rỉ dữ liệu" — nên **không thể kết luận bằng single-split**. Pipeline đã chạy được R6 nghĩa là nó chạy được cả 6 fold. Nhiệm vụ đầu tiên và quan trọng nhất: chạy Leave-One-Replicate-Group-Out cho cả 6 nhóm.

**Nguyên tắc 2 — KHÔNG THAY ĐỔI QUY TRÌNH XỬ LÝ ĐỂ "CỨU" KẾT QUẢ CŨ.**
Nếu kết quả LORO yếu hơn single-split, đó là kết quả đúng — báo cáo trung thực. Không được đổi window size, overlap, feature list, hay seed chỉ để phục hồi con số 0,86x. Mọi thay đổi pipeline phải được ghi log và báo cáo cho NCS trước.

---

## 0. BIẾN CHẶN — PHẢI KHÓA TRƯỚC TIÊN

Trước khi chạy bất kỳ thứ gì, xác nhận **cấu trúc nhóm độc lập** từ run registry. Đây là biến quyết định mọi phần còn lại.

| Câu hỏi phải trả lời | Ai trả lời | Ảnh hưởng nếu sai |
|---|---|---|
| Đơn vị độc lập là `Recording_ID` hay `Replicate_Group_ID`? | NCS + hồ sơ thí nghiệm | Sai đơn vị → toàn bộ split sai → mọi kết quả vô hiệu |
| Mỗi nhóm R1…R6 có chứa đủ 4 states × 3 excitations = 12 recordings không? | Run registry | Nếu không đủ 4 class/nhóm → không dùng được LORO chuẩn, phải đổi thiết kế |
| Tổng số recordings có đúng 72 không? | Manifest | Lệch số → kiểm kê lại trước khi chạy |
| Có nhóm nào bị cờ chất lượng cần loại không? | Data-quality audit | Ảnh hưởng sensitivity analysis |

> **SV IT không tự quyết biến này.** Nếu run registry chưa rõ, DỪNG và hỏi NCS. Không giả định.

**Giả định làm việc hiện tại (cần NCS xác nhận):** mỗi `Replicate_Group_ID` chứa 12 recordings (4 states × 3 excitations) → dùng **Leave-One-Replicate-Group-Out (LOGO)**, 6 fold.

---

## 1. QUY TRÌNH CHẠY LORO/LOGO — THỨ TỰ BẮT BUỘC

Chạy đúng thứ tự này cho **từng fold** (giữ R_k làm test, train trên 5 nhóm còn lại), lặp cho k = 1…6:

```text
[1] Khóa registry: xác nhận R_k gồm những recording nào
[2] Hold out TOÀN BỘ nhóm R_k TRƯỚC khi cắt window
[3] Cắt window CHỈ trên 5 nhóm training + nhóm test riêng biệt
       (KHÔNG cắt window trên toàn bộ dữ liệu rồi mới chia)
[4] Fit preprocessing (scaler, feature normalization) CHỈ trên training windows
[5] Train model với cùng seed, cùng tuning budget cho mọi cấu hình
[6] Transform test windows bằng preprocessing đã fit ở bước [4]
[7] Dự đoán từng window của nhóm test
[8] Gộp window → recording-level bằng majority vote
[9] Tính metric ở cấp nhóm test (macro-F1, balanced accuracy, per-class F1)
[10] Lưu: predictions, confusion matrix, metrics, seed, config, code version
```

Lặp toàn bộ [1]–[10] cho **mỗi tổ hợp**: 3 cấu hình cảm biến (S1, S2, S1+S2) × 4 model (LR, SVM, RF, 1D-CNN) × 6 fold = **72 lần chạy**. ResNet1D chạy riêng (xem §5).

**Điểm kiểm tra chống rò rỉ (bắt buộc log lại):**
- [ ] Không có window nào của R_k xuất hiện trong training của fold k
- [ ] Scaler/feature-normalizer fit KHÔNG chạm vào dữ liệu test
- [ ] Early stopping (nếu có) dùng validation TÁCH từ training groups, KHÔNG dùng nhóm test
- [ ] Cùng một danh sách fold dùng chung cho mọi cấu hình và mọi model

---

## 2. BẢNG PHẢI SẢN XUẤT — ĐẶC TẢ ĐẦU VÀO/ĐẦU RA

Mỗi bảng dưới đây ghi rõ: bảng này thay bảng nào trong v4, dữ liệu lấy từ đâu, định dạng ra sao. **Tất cả macro-F1 báo cáo ở cấp recording sau majority vote, KHÔNG ở cấp window.**

### Bảng A — Kiểm kê nhóm độc lập *(thay Bảng 4+5 của v4)*
- **Input:** run registry đã khóa.
- **Nội dung mỗi hàng:** `Replicate_Group_ID` | số recordings | states có mặt | excitations có mặt | có đủ 4 class? | cờ chất lượng.
- **Mục đích:** chứng minh cấu trúc dữ liệu hợp lệ cho LOGO trước khi trình bày kết quả.

### Bảng B — Macro-F1 theo từng held-out group *(thay Bảng 12 rỗng của v4 — BẢNG QUAN TRỌNG NHẤT)*
- **Input:** metric cấp nhóm từ bước [9], mọi fold.
- **Cấu trúc cột:** `Held-out group (R1…R6)` × `Model` × `S1 macro-F1` × `S2 macro-F1` × `S1+S2 macro-F1` × `Balanced accuracy`.
- **Hai hàng tổng hợp cuối bảng:** `Median` và `Range/IQR` cho mỗi cột.
- **QUY TẮC:** báo cáo **cả 6 giá trị từng nhóm**, không chỉ trung bình. Nhóm khó (nếu có) phải hiện rõ, không được giấu sau một mean.

### Bảng C — Chênh lệch cấu hình cảm biến theo cặp *(thay Bảng 9 single-split của v4)*
- **Input:** so sánh **theo cặp trong cùng nhóm** (paired), không phải chênh lệch của một test group.
- **Cấu trúc:** `Model` × `So sánh (S1+S2−S1 / S1+S2−S2 / S1−S2)` × `Median paired difference` × `Range/IQR` × `Số nhóm cùng chiều (x/6)`.
- **LƯU Ý:** ở single-split, RF cho S1+S2−S1 = −0,007 (âm). Nếu LOGO xác nhận, đây là bằng chứng cho "interaction, không phải dual-sensor luôn thắng" — báo cáo trung thực, đừng làm tròn về 0.

### Bảng D — So sánh model theo từng cấu hình *(thay phần 9.3 của v4)*
- **Input:** median macro-F1 mỗi model trong mỗi cấu hình, kèm range.
- **Cấu trúc:** `Sensor config` × `Model` × `Median macro-F1` × `Range/IQR`.
- **Ghi chú bắt buộc:** nếu dùng bất kỳ test so sánh nào (Wilcoxon…) trên các fold chồng lấn, đánh dấu là **exploratory** vì fold không độc lập hoàn toàn.

### Bảng E — Per-class precision/recall/F1 *(thay Bảng 10+11 của v4)*
- **Input:** metric từng class, tổng hợp qua các nhóm.
- **Cấu trúc:** `Model` × `Sensor config` × `State (H/A/BC/BR)` × `Precision` × `Recall` × `F1` × `Support`.
- **Mục đích:** cho thấy evidence quality phụ thuộc trạng thái (BC yếu dưới S2 ở single-split — kiểm chứng có lặp lại không).

### Bảng F — Empirical-null và sensitivity *(thay Bảng 13 rỗng của v4)*
- **Input:** kết quả permutation block-preserving + 3 sensitivity analyses.
- **Phần null:** đơn vị hoán vị (recording) | blocking (replicate × excitation) | statistic (median held-out macro-F1) | số permutation B (499 hoặc 999) | observed | null mean | empirical p = (b+1)/(B+1).
- **Phần sensitivity:** 3 hàng — non-overlapping windows | seed sensitivity | loại nhóm bị cờ chất lượng — mỗi hàng ghi observed / alternative / có đảo chiều kết luận không.

### Bảng G — Metadata cố định *(thay Bảng 1,2,3 của v4)*
- Trạng thái liên kết, thông số kích động, metadata cảm biến. **Phần lớn là data-independent** — SV IT điền từ hồ sơ thí nghiệm/config, KHÔNG chờ LORO. Ô nào NCS phải xác nhận thì để `[AUTHOR CONFIRMATION REQUIRED]`.

---

## 3. HÌNH PHẢI SẢN XUẤT — ĐẶC TẢ KỸ THUẬT

Mọi hình phải có nhãn nguồn dữ liệu. Khi còn dùng số single-split, gắn watermark `PRELIMINARY SINGLE-SPLIT`. Khi có LOGO, gỡ watermark và **đổi kiểu biểu đồ** theo yêu cầu dưới.

### Hình 1 — Specimen và vị trí cảm biến
- **Loại:** ảnh/bản vẽ kỹ thuật, không phải biểu đồ.
- **Yêu cầu:** kích thước chính, ký hiệu S1 (apex), S2 (beam–column joint), vị trí 3 liên kết (apex/BC/brace), chiều & phương đo.
- **Không** hiển thị giá trị chưa xác minh.

### Hình 2 — Sơ đồ pipeline run-aware
- **Loại:** flowchart.
- **Nội dung:** đúng chuỗi 10 bước ở §1 (registry → hold out group → window → fit preprocessing on train → train → transform test → aggregate → group metric → repeat).
- **Mục đích:** cho reviewer thấy split-before-windowing và train-only preprocessing.

### Hình 3 → chuyển thành Hình per-group *(thay bar chart single-split)*
- **Single-split (tạm):** grouped bar chart macro-F1, trục X = model, màu = S1/S2/S1+S2.
- **FINAL (bắt buộc đổi):** **dot plot / connected-points plot** hiển thị **từng nhóm R1…R6**. Mỗi điểm = một held-out group. KHÔNG dùng bar chart của mean — nó che nhóm khó.
- **Trục Y đồng nhất** giữa các panel để so sánh.

### Hình 4 — Hiệu ứng cảm biến theo cặp
- **Loại:** paired/slope plot — nối điểm cùng một nhóm giữa hai cấu hình.
- **Nội dung:** cho thấy nhóm nào cải thiện, nhóm nào không, khi thêm cảm biến. Phân panel theo model nếu hiệu ứng phụ thuộc model.

### Hình 5 — Per-class F1
- **Loại:** grouped bars theo H/A/BC/BR × 3 cấu hình.
- **FINAL:** thêm thanh biểu diễn range/IQR qua các nhóm (uncertainty).

### Hình 6 — Confusion matrices
- **Loại:** heatmap.
- **Yêu cầu:** một matrix cho mỗi (cấu hình × model được chọn); **class order cố định H–A–BC–BR**; cung cấp **cả count và row-normalized**; cùng scale màu.
- **KHÔNG hard-code cặp A↔BC.** Vẽ theo predictions thật; nếu cặp nhầm chính khác, vẽ theo dữ liệu.
- Per-group matrices → Supplementary.

### Hình 7 — Phân bố empirical-null
- **Loại:** histogram của null statistic + đường thẳng đứng cho observed.
- **Caption ghi rõ:** đơn vị hoán vị, blocking, số permutation, việc chạy lại full pipeline, empirical p-value.

---

## 4. QUY TẮC GỘP WINDOW → RECORDING (đọc kỹ, dễ sai)

```text
Window predictions (nhiều window/recording)
   → majority vote trong mỗi recording
   → recording-level prediction (1 nhãn/recording)
   → gộp các recording trong nhóm test → confusion & metric cấp nhóm
```

- **Primary:** majority vote ở cấp recording.
- **Sensitivity (tuỳ chọn):** mean class-probability nếu model xuất probability hợp lệ.
- **CẤM:** coi 1.149 windows là 1.149 mẫu độc lập. Không bootstrap từng window. Không báo cáo p-value từ window làm bằng chứng chính. `n` hiệu dụng = số nhóm độc lập (≈6), KHÔNG phải số window.

---

## 5. RESNET1D — QUY TẮC RIÊNG (KHÔNG VÀO BẢNG CHÍNH KHI CHƯA ĐỦ ĐIỀU KIỆN)

Báo cáo IT ghi ResNet1D hội tụ/tổng quát hóa tốt hơn 1D-CNN. **Nhưng chưa được đưa vào so sánh số chính** cho đến khi khóa đủ **8 điều kiện provenance:**

- [ ] sensor mode (S1 / S2 / S1+S2 nào?)
- [ ] input channels (C=1 hay 2?)
- [ ] common folds (cùng 6 nhóm với các model khác?)
- [ ] seeds
- [ ] preprocessing (giống pipeline chung?)
- [ ] checkpoint hash
- [ ] code version
- [ ] final per-group macro-F1 (đủ 6 nhóm)

**Cho đến khi đủ 8 mục:** ResNet1D chỉ được mô tả là "candidate model", để ở Supplementary hoặc mục riêng, KHÔNG nằm trong Bảng B/C/D. Nếu chạy được cùng 6 fold như các model khác → đưa vào so sánh chính như model thứ 5.

---

## 6. THAM SỐ PIPELINE HIỆN TẠI (để SV IT tái lập, cần khóa & log)

| Tham số | Giá trị single-split hiện tại | Yêu cầu cho FINAL |
|---|---|---|
| Sampling frequency | 100 Hz | Xác nhận từ acquisition config |
| Window length | 1.024 mẫu (≈10,24 s) | Giữ, nhưng cắt SAU khi split nhóm |
| Overlap / stride | 75% / 256 mẫu | Giữ; thêm biến thể non-overlap cho sensitivity |
| Scaling | chưa audit đầy đủ | Fit train-only, log rõ |
| Traditional features | ~140 features/kênh | Khóa danh sách + code version |
| Dual-sensor features | nối đặc trưng 2 kênh | Giữ nguyên logic |
| Deep input | raw `C × 1024` | Giống nhau giữa các fold |
| 1D-CNN | 4 conv blocks 32→64→128→256, kernel 5, **dropout=0.0, no weight decay** | Giữ nguyên để trung thực; ghi rõ hạn chế regularization |
| ResNet1D | kernel 8/5/3, GAP, ~1.028 classifier params, AdamW wd=1e-3 | Chạy cùng folds trước khi kết luận |
| Seeds | theo bản cũ | Cố định danh sách seed, dùng chung mọi cấu hình |

> **Ghi chú luận điểm (quan trọng, chuyển cho NCS):** việc 1D-CNN cũ có `dropout=0.0` và không weight decay, với classifier ~49.924 params trên số nhóm độc lập rất nhỏ, giải thích **tại sao** RF ổn định hơn trong dữ liệu nhỏ và **tại sao** ResNet1D (có weight decay, classifier nhỏ) là hướng cải thiện hợp lý. SV IT giữ nguyên cấu hình cũ để so sánh trung thực — KHÔNG thêm dropout vào 1D-CNN cũ để "cứu" nó.

---

## 7. THỨ TỰ CÔNG VIỆC CHO SV IT (checklist tuần tự)

```text
[ ] B0. Cùng NCS khóa run registry & xác nhận đơn vị độc lập (§0) ← CHẶN, làm trước
[ ] B1. Điền Bảng G (metadata) từ hồ sơ — không chờ LORO
[ ] B2. Viết/kiểm tra pipeline LOGO theo đúng 10 bước §1
[ ] B3. Chạy 4 checkpoint chống rò rỉ (§1) trên 1 fold thử → xác nhận sạch
[ ] B4. Chạy đủ 72 lần (3 sensor × 4 model × 6 fold), lưu mọi output
[ ] B5. Sinh Bảng A (kiểm kê) và Bảng B (per-group macro-F1)
[ ] B6. Sinh Bảng C (paired sensor), Bảng D (model), Bảng E (per-class)
[ ] B7. Sinh Hình 3–5 dạng per-group (dot/paired plot), Hình 6 confusion
[ ] B8. Chạy empirical-null block-preserving → Bảng F + Hình 7
[ ] B9. Chạy 3 sensitivity (overlap, seed, exclusion) → phần dưới Bảng F
[ ] B10. (Nếu đủ 8 provenance) chạy ResNet1D cùng 6 fold → đưa vào so sánh
[ ] B11. Đóng gói: predictions, configs, seeds, code version, checksums cho reproducibility
[ ] B12. Bàn giao NCS: mọi bảng/hình + log, KHÔNG tự viết kết luận học thuật
```

---

## 8. RANH GIỚI SV IT KHÔNG ĐƯỢC VƯỢT (bảo vệ tính toàn vẹn bài báo)

- SV IT sản xuất **số liệu, bảng, hình, log** — KHÔNG viết claim học thuật, KHÔNG quyết cấu hình "tốt nhất".
- KHÔNG dùng từ "optimal" trong bất kỳ nhãn biểu đồ nào.
- KHÔNG suy diễn severity, độ cứng, lực siết bu-lông từ kết quả phân loại.
- KHÔNG gán ý nghĩa vật lý cho softmax (softmax = đầu ra phân loại chưa hiệu chuẩn, không phải xác suất hư hỏng).
- KHÔNG chuyển số từ mô hình 1:10 sang công trình thực.
- Mọi diễn giải cặp nhầm lẫn (vd A↔BC) chỉ ghi **"hypothesis, not confirmed"** — không giải thích cơ chế.
- Nếu phát hiện kết quả LOGO mâu thuẫn narrative cũ → báo NCS, KHÔNG tự điều chỉnh pipeline.

---

## 9. BẢNG ÁNH XẠ: SỐ SƠ BỘ v4 → SỐ CUỐI CÙNG (để không bỏ sót chỗ nào)

| Vị trí trong v4 | Số sơ bộ (single-split) | Thay bằng | Trạng thái |
|---|---|---|---|
| Abstract, Highlights | 0,869 / 0,841 / 0,862; 0,641→0,841 | **Xóa mọi con số**, chỉ giữ mô tả cấu trúc phát hiện | ⚠️ Rút số |
| Bảng 8 (macro-F1) | có | Bảng B (per-group, 6 nhóm) | Chờ LOGO |
| Bảng 9 (contrasts) | có (gồm RF −0,007) | Bảng C (paired, median+range) | Chờ LOGO |
| Bảng 10,11 (per-class) | có | Bảng E | Chờ LOGO |
| Bảng 12,13 | rỗng | Bảng B, F | Chờ LOGO |
| Hình 3 (bar chart) | có | Hình 3 dạng dot/per-group | Chờ LOGO |
| Discussion §10 | viết theo single-split | Giữ giọng điều kiện, cập nhật theo per-group | Chờ LOGO |
| Conclusion §12 | có số | **Xóa số**, cập nhật theo final | ⚠️ Rút số |
| ResNet1D §8.7,9.7 | định tính | Bảng số nếu đủ provenance | Chờ 8 điều kiện |

---

## 10. NGUYÊN TẮC VÀNG KHI THAY SỐ

```text
Final result → Evidence → Limitation → Conditional interpretation → Practical implication
```

- **Abstract / Highlights / Conclusion: KHÔNG chứa con số single-split.** Chỉ mô tả cấu trúc ("sensor configuration interacts with model family"), không nêu giá trị.
- **Results / Discussion:** được giữ số sơ bộ **chỉ khi** đóng khung rõ "preliminary, single held-out group, not the basis for any claim" — và thay ngay khi có LOGO.
- Nếu LOGO yếu hơn single-split: **giảm claim, định vị methodological case study, báo cáo trung thực** — không giấu nhóm khó, không sửa pipeline để phục hồi số cũ.

---

*Tài liệu này là đặc tả thực thi. Nội dung học thuật đầy đủ (câu chữ Introduction, Related Work, Discussion) nằm ở `PAPER1_Q2_INTEGRATED_OUTLINE_v4`. Ranh giới claim tối cao theo `MASTER_RESEARCH_CHARTER_v1.1_LIMITED_FEM`.*
