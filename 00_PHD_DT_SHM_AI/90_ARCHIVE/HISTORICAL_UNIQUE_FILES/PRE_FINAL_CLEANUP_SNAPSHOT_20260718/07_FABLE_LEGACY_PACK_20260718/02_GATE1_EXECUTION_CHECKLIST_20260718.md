# GATE 1 EXECUTION CHECKLIST — DATASET INTEGRITY & RUN-AWARE EVALUATION
**Ngày:** 2026-07-18 | **Phạm vi:** RQ1 / WP1 / Paper 1 / Gate 1 — Core Scope | **Loại bằng chứng:** laboratory evidence (không phải field diagnosis).
**Nguyên tắc:** không mục nào được đánh dấu DONE khi chưa có bằng chứng được ghi nhận (file, bảng, kết quả cụ thể). Không bịa metric.

## Bước 1 — Khóa run registry

| # | Việc | Bằng chứng yêu cầu | Trạng thái 18/07/2026 |
|---|---|---|---|
| 1.1 | Kiểm kê toàn bộ run thí nghiệm (số run, ngày đo, trạng thái liên kết, cấu hình cảm biến, thông số thu) | File run registry có version/ngày, liệt kê từng run | OPEN — "6 runs" chỉ là số báo cáo, chưa xác nhận |
| 1.2 | Đối chiếu run registry với dữ liệu thô trên đĩa (khớp số file, thời lượng, kênh) | Bảng đối chiếu registry ↔ dữ liệu thô | OPEN |
| 1.3 | Khóa registry (đánh dấu LOCKED, có ngày) và ghi change log | Registry LOCKED + change log | OPEN |

## Bước 2 — Đánh giá run-aware / LORO

| # | Việc | Bằng chứng yêu cầu | Trạng thái 18/07/2026 |
|---|---|---|---|
| 2.1 | Định nghĩa giao thức chia dữ liệu run-aware (mọi split theo run, không trộn segment cùng run giữa train/test) | Văn bản giao thức, công bố trước khi chạy | OPEN |
| 2.2 | Chạy LORO (leave-one-run-out) trên các run đã đăng ký | Kết quả LORO ghi nhận theo từng fold/run | OPEN — LORO chưa chạy |
| 2.3 | Ghi nhận độ ổn định kết quả giữa các fold; nếu số run ít, ghi rõ hạn chế thống kê | Bảng kết quả + mục Limitation | OPEN — Evidence is currently insufficient |

## Bước 3 — Xác nhận sensor mode của ResNet1D

| # | Việc | Bằng chứng yêu cầu | Trạng thái 18/07/2026 |
|---|---|---|---|
| 3.1 | Truy vết input pipeline của ResNet1D: single-sensor hay multi-sensor, kênh nào, tiền xử lý gì | Ghi chú kỹ thuật đối chiếu code/config với run registry | OPEN — chưa xác nhận |
| 3.2 | Quyết định giữ/loại ResNet1D khỏi bảng so sánh Paper 1 dựa trên kết quả 3.1 | Quyết định ghi văn bản | OPEN — cho đến khi xác nhận, ResNet1D không đưa vào manuscript (UNRESOLVED #1) |

## Điều kiện khóa Gate 1

Cả ba bước hoàn tất với bằng chứng ghi nhận; không suy diễn từ trí nhớ hay báo cáo cũ. Sau khi khóa: cập nhật `EVIDENCE_GATES_v1.1_LIMITED_FEM.md` phía Zotero_MCP (qua quy trình được phép) và báo hai thầy.

## Ranh giới

- Kết quả Gate 1 chỉ chứng minh khả năng phân biệt trạng thái trong điều kiện lab có kiểm soát — không phải chẩn đoán hư hỏng hiện trường.
- Không dùng FEM trong bất kỳ bước nào của Gate 1; nếu nhắc đến FEM trong Discussion, phải kèm "nominal, uncalibrated, reference-only, not used for damage diagnosis" và nhãn "hypothesis, not confirmed".
- CEI nếu xuất hiện: confidence/evidence indicator, không phải mức độ hư hỏng.
