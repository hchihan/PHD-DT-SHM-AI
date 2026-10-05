# KIẾN TRÚC NGHIÊN CỨU TỔNG THỂ
**Version:** v2.3 | **Issued:** 2026-07-17 | **Updated:** 11/08/2026
**Status:** CURRENT SUPPORTING | **Source-of-truth level:** 7
**Supersedes:** v2.2 supporting architecture. | **Superseded by:** None.
**Changes in this version:** Restores the canonical identifier chain, constrains schema work behind CQ/verification freeze, and records current evidence limitations.

> Control baseline: Charter v1.1 Limited-FEM and ADR-2026-001 dated 17/07/2026, plus the unchanged Council Review. Later implementation proposals are noncanonical where they conflict with the locked chains.

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

Mô hình dữ liệu hình thức hóa liên kết evidence với cấu kiện và hồ sơ theo chuỗi `Sensor_ID → BIM_GUID → Condition_Evidence_ID → Inspection_Record_ID → Action_Status`. CEI là metadata của condition evidence. Kiểm chứng bằng competency questions và verification criteria được khóa trước; chỉ sau đó mới được xây schema, constraint, fixture/oracle và paired forward/reverse queries. `Action_Record_ID`, `Workflow_Status` và `Status_Event` là noncanonical implementation proposals, không kéo dài chuỗi khóa.

### Lớp 3 — Field feasibility

Áp khung vào một công trình thực: bố trí cảm biến có tham chiếu FEM **nominal, uncalibrated, reference-only, not used for damage diagnosis**, baseline vận hành, ánh xạ Sensor_ID → BIM_GUID, kịch bản truy vết chạy end-to-end. Chứng minh *khả thi triển khai*, không chứng minh phát hiện hư hỏng.

### Lớp 4 — Inspection-maintenance support

Hỗ trợ inspection-maintenance action qua record, authorization/review, post-action verification và guarded closure/reopen có con người rà soát. Exact action vocabulary và role/permission matrix cần expert review. Defect severity không tự động thành `Action_Level`; recommendation không tự động thành `Action_Record`; `completed` không tự động thành verified closure. Không Health Index trọng số, không tự động hóa.

## Nguyên tắc kiến trúc

1. Mỗi lớp chỉ tuyên bố những gì lớp đó kiểm chứng được; không lớp nào "mượn" bằng chứng của lớp khác.
2. Trục duy nhất: evidence → traceability → decision. FEM is **nominal, uncalibrated, reference-only, not used for damage diagnosis** and has no separate RQ, WP, chapter, Paper or Evidence Gate.
3. Dòng chảy giá trị: Lớp 1 cấp evidence cho Lớp 2; Lớp 2 cấp cơ chế truy vết cho Lớp 3; Lớp 3 cấp bối cảnh vận hành cho Lớp 4; Lớp 4 quay lại xác nhận ý nghĩa quản lý của toàn chuỗi.
4. Digital Twin trong luận án là **data-informed Digital Twin ở cấp quản lý thông tin**; mức trưởng thành sẽ được tự định nghĩa tường minh trong chương khung nghiên cứu, không tuyên bố predictive.

## Ánh xạ sang cấu trúc luận án (tham chiếu, không chi tiết hóa ở đây)

Lớp 1 → RQ1/WP1; Lớp 2 → RQ2/WP2; Lớp 3 → RQ3/WP3; Lớp 4 → WP4 (synthesis). Điều hướng chi tiết hiện hành: `../01_CURRENT_CONTROL/MASTER_INDEX_CURRENT.md`; evidence theo Gate: `../02_EVIDENCE_BASE/`.

**Evidence status 11/08/2026:** No Gate is PASS. Evidence is currently insufficient for Gate closure.
