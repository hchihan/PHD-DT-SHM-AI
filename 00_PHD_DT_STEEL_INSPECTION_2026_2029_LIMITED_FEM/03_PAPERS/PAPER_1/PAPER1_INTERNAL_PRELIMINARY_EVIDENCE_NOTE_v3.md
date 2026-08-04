# PAPER 1 — INTERNAL PRELIMINARY EVIDENCE NOTE (v3)
**Date:** 2026-07-18 | **Status:** PRELIMINARY INTERNAL EVIDENCE — NOT FINAL RUN-AWARE RESULTS
**Nguồn:** `Paper 1_Old_version (10.06).docx`, `BAO_CAO_RESNET1D.docx`. Ghi chú nội bộ — KHÔNG đưa vào manuscript học thuật chính.

## 1. Bản chất số liệu
Toàn bộ số dưới đây đến từ **một** lần chia (single-split): train R1–R4, val R5, test R6. Không phải LORO/LOGO. Chỉ dùng để: xác định model roster, cấu trúc bảng, metric, confusion pattern cần kiểm tra, provenance còn thiếu, và thiết kế kịch bản Discussion/Conclusion. **Không** dùng làm bằng chứng cuối; **không** đưa vào Abstract/Highlights/Conclusion.

## 2. Cấu hình thí nghiệm (sơ bộ)
- Sampling 100 Hz; window 1 024 mẫu (≈10,24 s); overlap 0,75 (stride 256).
- 72 recordings = 4 state × 3 excitation × 6 run; tổng 1 149 windows.
- Split: train 765 (R1–R4), val 192 (R5), test 192 (R6).
- Nhãn dataset thô ↔ mã paper: Healthy=H; Đỉnh/Dinh=Apex(A); Nút/Nut=Beam–column(BC); Giằng/Giang=Brace(BR).
- Phân bố lớp train/val/test: Healthy 189/48/48; Apex 192/48/48; Beam–column 192/48/48; Brace 192/48/48.

## 3. Macro-F1 (single-split test R6) — Table 6 bản cũ
| Config | Random Forest | SVM | 1D-CNN | Logistic Reg. |
|---|---:|---:|---:|---:|
| S1 | 0,869 | 0,546 | 0,641 | 0,541 |
| S2 | 0,841 | 0,838 | 0,764 | 0,620 |
| S1+S2 | 0,862 | 0,765 | 0,841 | 0,716 |

## 4. Per-class F1 dưới S1+S2 (single-split) — Table 7 bản cũ
| State | Random Forest | 1D-CNN |
|---|---:|---:|
| Healthy | 0,917 | 0,911 |
| Apex | 0,792 | 0,800 |
| Beam–column | 0,833 | 0,758 |
| Brace | 0,903 | 0,852 |

## 5. Per-class F1 của 1D-CNN theo cấu hình (single-split) — Table 8 bản cũ
| Config | Healthy | Apex | Beam–column | Brace |
|---|---:|---:|---:|---:|
| S1 | 0,753 | 0,632 | 0,700 | 0,753 |
| S2 | 0,733 | 0,685 | 0,475 | 0,708 |
| S1+S2 | 0,911 | 0,800 | 0,758 | 0,852 |

## 6. Confusion (định tính, bản cũ)
Cặp nhầm chính báo cáo: **Apex ↔ Beam–column**. Chưa có ma trận số → không vẽ confusion matrix bằng số. Cần retained per-window predictions từ final analysis.

## 7. ResNet1D — provenance ghi nhận & còn thiếu
**Ghi nhận (định tính, báo cáo SV IT):**
- Residual block = 3× Conv1D liên tiếp + shortcut; kernel 8/5/3.
- Global Average Pooling → 1 lớp Linear; classifier 1.028 tham số (so với 1D-CNN 3 FC = 49.924 tham số).
- Optimizer AdamW, weight_decay = 1e-3 (1D-CNN dùng Adam, không weight decay, dropout = 0.0).
- Nhận xét bản cũ: "ResNet1D tốt hơn 1D-CNN về hội tụ, tổng quát hóa, kết quả test" — **single-split, định tính, KHÔNG có macro-F1 số**.
- Softmax margin (ví dụ minh họa A/B) — chỉ khái niệm, **không** dùng như calibrated probability.

**Còn thiếu để INCLUDE vào main results:** sensor mode; input channels; common folds; seeds; preprocessing; checkpoint hash; code version; và macro-F1 số dưới final common-fold. → Trạng thái: **PENDING PROVENANCE VERIFICATION**. Không viết "ResNet1D tốt hơn" trong Results.

## 8. Loại bỏ dứt khoát
- **DSI / severity** (Table 9 cũ: Pearson R=0.953, RMSE 0.119, MAE 0.051): KHÔNG phục hồi — severity/DSI bị cấm theo Charter §11.
- Confidence score như calibrated probability: không dùng.
- "Softmax preserves severity": không dùng.

## 9. Điều KHÔNG được kết luận trước từ số single-split
Không kết luận trước: S1+S2 tốt nhất; S2 yếu nhất; BC là lớp khó nhất; sensor effect > model effect; RF superiority tổng quát; ResNet1D > 1D-CNN. Mọi kết luận chờ final LORO/LOGO + empirical null.
