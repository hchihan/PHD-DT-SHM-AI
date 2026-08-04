# KIẾN TRÚC NGHIÊN CỨU TỔNG THỂ
**Ngày:** 17/07/2026 | Cấp chiến lược; không chi tiết hóa Paper, phương pháp hay lịch thực hiện.

## Bốn lớp kiến trúc

```text
Laboratory evidence
→ Information traceability
→ Field feasibility
→ Inspection-maintenance support
```

### Lớp 1 — Laboratory evidence

Mô hình khung thép 1:10 tạo bằng chứng dao động có nhãn, có kiểm soát cho các trạng thái liên kết (healthy, apex, beam–column, brace). Nguyên tắc bất di bất dịch: run registry đầy đủ, đánh giá run-aware chống rò rỉ dữ liệu. Đầu ra của lớp: condition evidence đáng tin cậy trong điều kiện kiểm soát — không phải chẩn đoán.

### Lớp 2 — Information traceability

Mô hình dữ liệu hình thức hóa liên kết evidence với cấu kiện và hồ sơ: `Sensor_ID → BIM_GUID → Condition_Evidence_ID → Inspection_Record_ID → Action_Status`. Kiểm chứng bằng competency questions và tiêu chí công bố trước (toàn vẹn định danh, truy vết hai chiều, đầy đủ chuỗi). Đây là lớp mang tính mới chính của luận án.

### Lớp 3 — Field feasibility

Áp khung vào một công trình thực: bố trí cảm biến có tham chiếu mô hình thiết kế danh nghĩa, baseline vận hành, ánh xạ Sensor_ID → BIM_GUID, kịch bản truy vết chạy end-to-end. Chứng minh *khả thi triển khai*, không chứng minh phát hiện hư hỏng.

### Lớp 4 — Inspection-maintenance support

Chuyển evidence thành bốn mức hành động minh bạch: `Normal → Watch → Inspect → Priority Inspection`, có con người rà soát, kiểm chứng qua kịch bản với người quản lý cơ sở. Không Health Index trọng số, không tự động hóa.

## Nguyên tắc kiến trúc

1. Mỗi lớp chỉ tuyên bố những gì lớp đó kiểm chứng được; không lớp nào "mượn" bằng chứng của lớp khác.
2. Trục duy nhất: evidence → traceability → decision. Không có nhánh FEM; mô hình thiết kế danh nghĩa chỉ phục vụ Lớp 3 (vị trí cảm biến) và phần Limitation.
3. Dòng chảy giá trị: Lớp 1 cấp evidence cho Lớp 2; Lớp 2 cấp cơ chế truy vết cho Lớp 3; Lớp 3 cấp bối cảnh vận hành cho Lớp 4; Lớp 4 quay lại xác nhận ý nghĩa quản lý của toàn chuỗi.
4. Digital Twin trong luận án là **data-informed Digital Twin ở cấp quản lý thông tin**; mức trưởng thành sẽ được tự định nghĩa tường minh trong chương khung nghiên cứu, không tuyên bố predictive.

## Ánh xạ sang cấu trúc luận án (tham chiếu, không chi tiết hóa ở đây)

Lớp 1 → RQ1/WP1; Lớp 2 → RQ2/WP2; Lớp 3 → RQ3/WP3; Lớp 4 → WP4 (synthesis). Chi tiết chương, paper và evidence gates: `05_OUTPUT/Zotero_MCP/02_GATE_MATRICES/`.
