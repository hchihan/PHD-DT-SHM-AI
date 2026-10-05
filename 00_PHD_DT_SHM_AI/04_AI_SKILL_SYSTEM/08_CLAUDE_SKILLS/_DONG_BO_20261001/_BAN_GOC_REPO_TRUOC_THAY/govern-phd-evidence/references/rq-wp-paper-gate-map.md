# Bản đồ RQ ↔ WP ↔ Chương ↔ Paper ↔ Gate — govern-phd-evidence v0.2

Cập nhật 2026-08-09. Trích từ `MASTER_RESEARCH_CHARTER_v1.1_LIMITED_FEM_20260717.md`
(§7–§12), `RESEARCH_ARCHITECTURE_DECISION_RECORD_20260717.md` (ADR-2026-001) và
`RESEARCH_ARCHITECTURE.md`.

**Chỉ là cấu trúc.** Trạng thái tiến độ, metric, kết quả mô hình cố tình không đưa vào đây
— đọc từ `CURRENT_STATUS_AND_NEXT_DIRECTION.md` và evidence pack hiện hành mỗi lần cần
báo cáo tiến độ.

---

## 1. Trục chính

| RQ | WP | Chương | Paper | Evidence Gate | Loại bằng chứng |
|---|---|---|---|---|---|
| **RQ1** — Dữ liệu dao động từ mô hình khung thép 1:10 và các cấu hình cảm biến tạo bằng chứng phân biệt trạng thái liên kết có kiểm soát đáng tin cậy đến mức nào, dưới giao thức đánh giá run-aware chống rò rỉ? | WP1 — Laboratory vibration evidence | C4 | Paper 1 | G1 | Laboratory evidence |
| **RQ2** — Bằng chứng trạng thái từ dữ liệu cảm biến được tổ chức và liên kết với cấu kiện BIM và hồ sơ kiểm tra như thế nào để bảo đảm truy vết cấp cấu kiện? | WP2 — BIM–Sensor–Inspection traceability | C5 | Paper 2 | G2, G3, G6 | Information traceability |
| **RQ3** — Khung data-informed Digital Twin hỗ trợ lựa chọn và ghi nhận hành động kiểm tra tại công trình thực như thế nào trong điều kiện dữ liệu hư hỏng hiện trường hạn chế? | WP3 — Field feasibility and inspection support | C6 | Paper 3 | G4, G5, G7 | Field feasibility |
| — (synthesis bốn mức hành động) | WP4 — Decision-support synthesis | C7 (optional / stretch) | Paper 4 (optional; có thể gộp vào Paper 3) | G5 | Management decision support |

Lớp kiến trúc tương ứng (`RESEARCH_ARCHITECTURE.md`): Lớp 1 → RQ1/WP1; Lớp 2 → RQ2/WP2;
Lớp 3 → RQ3/WP3; Lớp 4 → WP4.

Lớp 2 (Information traceability) là **lớp mang tính mới chính** của luận án.

## 2. Bản đồ chương (Charter v1.1 §9)

| Chương | Nội dung | RQ | Paper |
|---|---|---|---|
| C1 | Mở đầu | — | — |
| C2 | Tổng quan và khoảng trống = thiếu chuỗi truy vết end-to-end evidence-to-action: dao động → bằng chứng → cấu kiện BIM → hồ sơ kiểm tra → hành động | — | — |
| C3 | Khung nghiên cứu và thiết kế kiểm chứng; gồm mục "Định nghĩa và mức trưởng thành Digital Twin trong luận án này" và tiểu mục "Vai trò giới hạn của mô hình FEM danh nghĩa" | — | — |
| C4 | Laboratory evidence | RQ1 | Paper 1 |
| C5 | Traceability framework | RQ2 | Paper 2 |
| C6 | Field feasibility | RQ3 | Paper 3 |
| C7 | Decision-support framework (optional / stretch) | — | Paper 4 |
| C8 | Kết luận | — | — |

**Không có chương FEM.** FEM chỉ nằm trong một tiểu mục phương pháp ở C3 và phần
Limitations.

## 3. Work packages (Charter v1.1 §8)

| WP | Nội dung | Output chính |
|---|---|---|
| WP1 — Laboratory vibration evidence | Labelled dataset, run registry, cấu hình cảm biến, run-aware/LORO evaluation, xác nhận sensor mode (gồm ResNet1D) | Bằng chứng lab tái lập được — không phải field diagnosis |
| WP2 — BIM–Sensor–Inspection traceability | Mô hình dữ liệu truy vết hình thức hóa, identifier schema, competency questions, tiêu chí đánh giá, demo lab end-to-end | Khung truy vết cấp cấu kiện kiểm chứng được |
| WP3 — Field feasibility and inspection support | Bố trí cảm biến field (reference-informed placement), baseline vận hành, kịch bản truy vết field, quy trình hồ sơ kiểm tra | Bằng chứng khả thi hiện trường — không phải field damage diagnosis |
| WP4 — Decision-support synthesis | Logic Normal → Watch → Inspect → Priority Inspection, case scenarios, rà soát bởi chuyên gia/quản lý cơ sở | Logic hỗ trợ quyết định minh bạch; không Health Index trọng số |

## 4. Bản đồ Evidence Gate (Charter v1.1 §11)

| Gate | RQ/WP | Nội dung tóm tắt | Loại bằng chứng |
|---|---|---|---|
| G1 | RQ1 / WP1 | Dataset integrity và run-aware evaluation | Laboratory evidence |
| G2 | RQ2 / WP2 | Traceability data model và competency questions | Information traceability |
| G3 | RQ2 / WP2 | End-to-end laboratory traceability | Information traceability |
| G4 | RQ3 / WP3 | Field mapping và baseline feasibility | Field feasibility |
| G5 | WP4 (+WP3) | Inspection-action scenario review | Management decision support |
| G6 | RQ2 / WP2 | Paper 2 submission | Information traceability |
| G7 | RQ3 / WP3 | Paper 3 submission và thesis synthesis | Tổng hợp bốn lớp, giữ tách biệt |

**Tiêu chí nghiệm thu chi tiết của từng Gate:** Charter v1.1 §11 viện dẫn
`EVIDENCE_GATES_v1.1_LIMITED_FEM.md`; ma trận chi tiết viện dẫn
`RQ_WP_CHAPTER_PAPER_GATE_MATRIX_v1.1.md`. Cả hai file **không tìm thấy trong repo**
(kiểm tra 2026-08-09). Ngoài phần tóm tắt trên: `Evidence is currently insufficient.`
Không tự chế tiêu chí nghiệm thu thay thế.

**Gate không tồn tại (bị cấm):** calibrated FEM · MAC · equivalent stiffness · FEM sensor
sensitivity · FEM calibration baseline.

## 5. Gate 1 — ưu tiên hiện tại

Theo `CURRENT_STATUS_AND_NEXT_DIRECTION.md` §5.2, ba hạng mục chặn:

1. khóa run registry;
2. leakage-safe run-aware/LORO evaluation;
3. xác nhận sensor mode của ResNet1D.

Số run, kết quả LORO, metric mô hình và trạng thái từng hạng mục: đọc từ evidence pack
hiện hành, không lấy từ file này.

## 6. Validation ladder (Charter v1.1 §12)

| Mức | Ý nghĩa |
|---|---|
| V1 — Laboratory validity | Trạng thái liên kết có kiểm soát phân biệt được và lặp lại được dưới đánh giá run-aware/LORO |
| V2 — Traceability validity | Chuỗi định danh chạy hai chiều (cảnh báo ↔ cấu kiện ↔ hồ sơ), đo bằng competency questions và tiêu chí công bố trước |
| V3 — Field feasibility | Khung triển khai được tại công trình thực; dữ liệu về; kịch bản truy vết chạy |
| V4 — Decision validity | Khuyến nghị minh bạch, giải thích được, được quản lý cơ sở đánh giá là hợp lý |

## 7. Paper portfolio (Charter v1.1 §10)

| Paper | Nội dung lõi |
|---|---|
| Paper 1 | Dataset integrity, run registry, run-aware/LORO evaluation, ảnh hưởng của cấu hình cảm biến, CEI như confidence/evidence indicator |
| Paper 2 | Mô hình dữ liệu truy vết hình thức hóa, identifier schema, competency questions pre-registered, kiểm chứng theo kịch bản |
| Paper 3 | Triển khai field, baseline vận hành, kịch bản truy vết field, quy trình hồ sơ kiểm tra |
| Paper 4 (optional; có thể gộp vào Paper 3) | Logic bốn mức, rà soát kịch bản |

Tên đầy đủ của từng Paper nằm ở Charter v1.1 §10 — trích nguyên văn khi cần, không diễn
đạt lại.

## 8. Bất biến

1. Không tạo thêm RQ, WP, chương, Paper hay Evidence Gate.
2. Không có thành phần FEM ở bất kỳ cấp nào của bản đồ này.
3. Chuỗi định danh: `Sensor_ID → BIM_GUID → Condition_Evidence_ID → Inspection_Record_ID
   → Action_Status`. `FEM_Node_ID` chỉ metadata tùy chọn.
4. CEI là confidence/evidence indicator, không phải severity, không phải Health Index.
5. Bốn lớp bằng chứng tách biệt; không mượn chéo.
6. Không hard-code trạng thái, metric hay kết quả vào file này.
