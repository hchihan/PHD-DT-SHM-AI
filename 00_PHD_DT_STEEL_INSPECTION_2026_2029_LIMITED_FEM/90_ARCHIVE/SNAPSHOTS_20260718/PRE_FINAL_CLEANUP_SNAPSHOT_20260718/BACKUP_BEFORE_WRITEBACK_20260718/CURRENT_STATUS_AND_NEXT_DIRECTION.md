# HIỆN TRẠNG VÀ HƯỚNG VIỆC TIẾP THEO
**Ngày:** 17/07/2026 | Cấp tổng quát; chi tiết gate/paper xem `05_OUTPUT/Zotero_MCP/`.

## 1. Những gì đã có

- Mô hình thí nghiệm khung thép 1:10 với dữ liệu dao động có nhãn cho các trạng thái liên kết (số run báo cáo: 6 — chưa khóa trong run registry).
- Mô hình BIM cho mô hình 1:10 và công trình thực (kho khung thép 25×80 m), asset register, shop drawings.
- Evidence base văn liệu đã kiểm soát trùng lặp: 108 bản ghi canonical, trong đó 33 bản ghi substantive/limited đã deep-read; đã di trú sang kiến trúc Limited-FEM (`LIVING_EVIDENCE_BASE_v1.1_LIMITED_FEM.md`).
- Bộ file quản trị v1.1 hoàn chỉnh: Charter, ADR, gate matrix, evidence gates, concept note Paper 2 (traceability), addendum RQ2, terminology control, master index, change log.
- Kết quả phân loại lab ban đầu và đề xuất CEI (confidence/evidence indicator).

## 2. Những gì đã thống nhất

- Verdict B (17/07/2026, hai thầy hướng dẫn chấp thuận): FEM chỉ là mô hình tham chiếu danh nghĩa; kiến trúc bốn lớp evidence → traceability → field feasibility → decision support.
- Chuỗi nghiên cứu và chuỗi định danh đã khóa (Charter §6).
- Ba RQ theo ba lớp đầu; WP4 synthesis bốn mức hành động; không Health Index phức tạp.
- Paper 2 đổi trục sang traceability framework với competency questions công bố trước.

## 3. Nguồn dữ liệu hiện có

Dữ liệu dao động lab 1:10 (nhiều run, nhiều cấu hình cảm biến); mô hình BIM lab + field; hồ sơ thiết kế công trình thực; văn liệu Zotero đã kiểm soát; chuẩn tham chiếu ISO 19650, TCVN 14177:2024 và quy định bảo trì hiện hành.

## 4. Các vấn đề chưa khóa

(Chi tiết: `05_OUTPUT/Zotero_MCP/99_REVIEW_NEEDED/UNRESOLVED_ITEMS_AFTER_LIMITED_FEM_MIGRATION.md`)

- LORO chưa chạy; sensor mode của ResNet1D chưa xác nhận; run registry chưa khóa.
- Thỏa thuận tiếp cận công trình thực chưa xác nhận ký — điều kiện tiên quyết của mọi việc field.
- Cấu trúc Inspection_Record và competency questions chưa được phê duyệt.
- Nguồn văn liệu cho định nghĩa mức trưởng thành Digital Twin và phương pháp competency questions còn thiếu.
- AGENT_RULES.md và RESEARCH_CHARTER.md cũ (04_AI_SYSTEM) chưa cập nhật theo Limited-FEM; yêu cầu chính thức của chương trình đào tạo chưa có.

## 5. Hướng việc lớn tiếp theo (theo thứ tự ưu tiên)

1. Xin xác nhận bằng văn bản của hai thầy về bộ khung này trước hạn chuyên đề tổng quan T7/2026.
2. Khóa Gate 1: run registry → LORO → xác nhận ResNet1D; đây là nút chặn kỹ thuật số 1.
3. Phê duyệt và pre-register competency questions + tiêu chí đánh giá truy vết (Gate 2) trước khi xây bất kỳ schema/demo nào.
4. Ký thỏa thuận tiếp cận công trình thực trước khi lắp cảm biến (mở Gate 4).
5. Bổ sung văn liệu còn thiếu (DT maturity, CQ methodology, provenance) qua phiên OpenCode/Zotero.
6. Đồng bộ các tài liệu vận hành cũ (AGENT_RULES, navigation files) về Limited-FEM sau khi có phê duyệt.
