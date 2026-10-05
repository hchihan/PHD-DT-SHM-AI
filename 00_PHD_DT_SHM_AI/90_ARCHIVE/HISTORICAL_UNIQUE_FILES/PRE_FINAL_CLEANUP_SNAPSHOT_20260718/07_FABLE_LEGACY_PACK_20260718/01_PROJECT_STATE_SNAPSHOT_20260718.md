# PROJECT STATE SNAPSHOT
**Ngày:** 2026-07-18 | **Căn cứ:** 6 file định hướng đọc ngày 18/07/2026 (Charter, Charter v1.1, Direction & Scope, Architecture, Current Status, ADR-2026-001). Không phải Source of Truth.

## 1. Định danh dự án

- Đề tài (EN): Developing a Data-informed Digital Twin Framework for Condition Monitoring and Inspection–Maintenance Support of Coastal Industrial Steel Buildings.
- Ngành: Construction Management / Asset Management. Cảm biến, AI, BIM, FEM là công cụ, không phải đối tượng nghiên cứu.
- Kiến trúc: Limited-FEM (ADR-2026-001, Verdict B, hai thầy hướng dẫn chấp thuận 17/07/2026).

## 2. Chuỗi đã khóa (không thay đổi)

```text
Vibration data → condition/state-change evidence → BIM-linked component
→ inspection record → inspection-maintenance action support

Sensor_ID → BIM_GUID → Condition_Evidence_ID → Inspection_Record_ID → Action_Status
```

`FEM_Node_ID` chỉ là metadata tùy chọn. FEM: nominal, uncalibrated, reference-only, not used for damage diagnosis.

## 3. Hiện trạng theo bốn loại bằng chứng

### 3.1 Laboratory evidence (Lớp 1 — RQ1/WP1, Paper 1, Gate 1)

- Claim: Đã có mô hình khung thép 1:10 với dữ liệu dao động có nhãn cho các trạng thái liên kết (healthy, apex, beam–column, brace) và kết quả phân loại ban đầu kèm đề xuất CEI (confidence/evidence indicator).
- Evidence: CURRENT_STATUS_AND_NEXT_DIRECTION.md §1; Charter v1.1 §5.
- Limitation: Số run báo cáo là 6 nhưng chưa khóa trong run registry; LORO chưa chạy; sensor mode của ResNet1D chưa xác nhận. Kết quả phân loại hiện tại chưa đủ điều kiện trích dẫn như kết quả cuối. Evidence is currently insufficient (cho mọi tuyên bố định lượng về hiệu năng phân loại).
- Next action: Thực thi checklist Gate 1 (`02_GATE1_EXECUTION_CHECKLIST_20260718.md`).

### 3.2 Information traceability (Lớp 2 — RQ2/WP2, Paper 2, Gates 2–3, 6)

- Claim: Paper 2 đã đổi trục sang traceability framework; concept note và addendum RQ2 đã lập (PAPER2_CONCEPT_NOTE_TRACEABILITY_v1.0_20260717.md; RQ2_TRACEABILITY_EVIDENCE_ADDENDUM_v1.0.md).
- Evidence: CURRENT_STATUS_AND_NEXT_DIRECTION.md §1–2; ADR-2026-001.
- Limitation: Competency questions CQ1–CQ8 chưa được phê duyệt và chưa pre-register; cấu trúc Inspection_Record chưa được định nghĩa/phê duyệt; nguồn văn liệu cho phương pháp competency questions còn thiếu. Không được xây schema/demo trước khi CQ được duyệt.
- Next action: Trình hai thầy phê duyệt CQ + tiêu chí đánh giá truy vết; pre-register trước khi triển khai (Gate 2).

### 3.3 Field feasibility (Lớp 3 — RQ3/WP3, Paper 3, Gates 4–5, 7)

- Claim: Đã có mô hình BIM cho công trình thực (kho khung thép 25×80 m), asset register, shop drawings; kế hoạch bố trí cảm biến theo reference-informed sensor placement (dựa mô hình thiết kế danh nghĩa).
- Evidence: CURRENT_STATUS_AND_NEXT_DIRECTION.md §1, §3.
- Limitation: Thỏa thuận tiếp cận công trình thực chưa xác nhận đã ký — điều kiện tiên quyết cứng trước mọi việc lắp cảm biến. Không chuyển kết luận định lượng 1:10 → công trình thực. Evidence is currently insufficient (về trạng thái chữ ký thỏa thuận).
- Next action: Xác nhận văn bản ký với chủ/đơn vị vận hành công trình trước khi mở Gate 4.

### 3.4 Management decision support (Lớp 4 — WP4, Paper 4/stretch, Gate 5)

- Claim: Logic bốn mức Normal → Watch → Inspect → Priority Inspection đã thống nhất về nguyên tắc: minh bạch, có con người rà soát, không Health Index trọng số, không tự động hóa.
- Evidence: Charter v1.1 §8 (WP4), §12 (V4); RESEARCH_ARCHITECTURE.md Lớp 4.
- Limitation: Chưa có kịch bản đánh giá với người quản lý cơ sở; phụ thuộc đầu ra các lớp trước. Evidence is currently insufficient (về tính hợp lý của khuyến nghị theo đánh giá facility management).
- Next action: Chỉ triển khai sau khi Gate 1–2 có tiến triển; thiết kế kịch bản rà soát chuyên gia ở giai đoạn WP4.

## 4. Ưu tiên đã thống nhất (thứ tự từ CURRENT_STATUS §5)

1. Xác nhận bằng văn bản của hai thầy về bộ khung Limited-FEM trước hạn chuyên đề tổng quan T7/2026.
2. Khóa Gate 1: run registry → LORO → xác nhận ResNet1D (nút chặn kỹ thuật số 1).
3. Phê duyệt + pre-register competency questions và tiêu chí đánh giá truy vết (Gate 2).
4. Ký thỏa thuận tiếp cận công trình thực (mở Gate 4).
5. Bổ sung văn liệu thiếu (DT maturity, CQ methodology, provenance) qua phiên OpenCode/Zotero.
6. Đồng bộ tài liệu vận hành cũ (AGENT_RULES, navigation) về Limited-FEM sau khi có phê duyệt.

## 5. Kết luận trạng thái

- Claim: Bộ khung quản trị v1.1 hoàn chỉnh và vận hành được; Project chưa sẵn sàng đầy đủ ở cấp kỹ thuật/field vì Gate 1 chưa khóa và tiền đề Gate 4 chưa xác nhận.
- Evidence: Mục 3–4 ở trên.
- Limitation: Snapshot phản ánh nội dung file tại 18/07/2026; không xác minh độc lập ngoài file text.
- Next action: Mọi phiên sau bắt đầu từ ưu tiên 1–2 trừ khi người dùng chỉ đạo khác.
