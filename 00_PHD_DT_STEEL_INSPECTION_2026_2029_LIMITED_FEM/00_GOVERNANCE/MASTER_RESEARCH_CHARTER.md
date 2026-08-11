# MASTER RESEARCH CHARTER (CONCISE — NAVIGATION ENTRY)
**Version:** v2.2 concise pointer | **Updated:** 2026-08-04
**Status:** CURRENT SUPPORTING NAVIGATION | **Source-of-truth level:** 7
**Supersedes:** v2.1 concise pointer. | **Superseded by:** None.
**Change summary:** Aligns current entry, identifier/event boundary and gate status; the full Charter remains authoritative.

> **SOURCE OF TRUTH cao nhất là `MASTER_RESEARCH_CHARTER_v2.1_TRACEABILITY_CORE_20260719.md`** (cùng thư mục). File concise này chỉ tóm tắt. Trật tự ưu tiên: `SOURCE_OF_TRUTH_HIERARCHY_v2.1.md`. Evidence entry: `../02_EVIDENCE_BASE/CURRENT/00_MASTER_INDEX_CURRENT_20260804.md`.

## 1. Tên đề tài

Tiếng Việt: **Phát triển khung Digital Twin dựa trên dữ liệu phục vụ giám sát trạng thái và hỗ trợ kiểm tra, bảo trì nhà công nghiệp khung thép ven biển.**
Tiếng Anh: **Developing a Data-informed Digital Twin Framework for Condition Monitoring and Inspection–Maintenance Support of Coastal Industrial Steel Buildings.**

## 2. Lĩnh vực nghiên cứu

Quản lý xây dựng / Quản lý tài sản công trình (Construction Management / Asset Management). Cảm biến, AI, BIM và FEM là công cụ hỗ trợ, không phải đối tượng nghiên cứu.

## 3. Đối tượng nghiên cứu

Nhà công nghiệp khung thép ven biển; trọng tâm là liên kết khung thép, phản ứng dao động, giám sát trạng thái, truy vết thông tin cấp cấu kiện và hỗ trợ kiểm tra – bảo trì theo điều kiện.

## 4. Vấn đề nghiên cứu trung tâm

Hồ sơ giám sát – kiểm tra – bảo trì hiện nay phân tán và không truy vết được: cảnh báo từ cảm biến không gắn được một cách kiểm chứng với cấu kiện cụ thể và hồ sơ kiểm tra tương ứng, nên không hỗ trợ minh bạch cho quyết định kiểm tra – bảo trì.

## 5. Mục tiêu tổng quát

Phát triển và kiểm chứng một khung data-informed Digital Twin tổ chức, liên kết và truy vết condition evidence từ dữ liệu dao động đến cấu kiện BIM và hồ sơ kiểm tra, nhằm hỗ trợ lựa chọn hành động kiểm tra – bảo trì minh bạch, kiểm chứng được, ngay cả khi dữ liệu hư hỏng hiện trường hạn chế.

## 6. Chuỗi nghiên cứu (đã khóa)

```text
Dữ liệu dao động
→ condition/state-change evidence (+ CEI)
→ BIM-linked component
→ inspection record
→ justified, accountable inspection–maintenance action
```

Chuỗi định danh: `Sensor_ID → BIM_GUID / Asset_ID @ Model_Version_ID → Condition_Evidence_ID → Inspection_Record_ID → Action_Record_ID`. CEI là first-class attribute. `Action_Status`/`Workflow_Status` là current projection, không phải identifier. Candidate `Status_Event_ID` và exact lifecycle/verification/closure rules là `PROPOSED — NOT YET ACCEPTED`. Không tự thêm `Component_ID`; database surrogate key chỉ là technical key.

## 7. Phạm vi

Trong phạm vi: bằng chứng dao động phòng thí nghiệm (mô hình khung thép 1:10, giao thức run-aware chống rò rỉ dữ liệu); mô hình dữ liệu truy vết cấp cấu kiện (BIM-linked component traceability); tính khả thi hiện trường (field feasibility) tại một công trình thực; logic hỗ trợ quyết định bốn mức Normal → Watch → Inspect → Priority Inspection (đơn giản, có con người rà soát).

Ngoài phạm vi (không bắt đầu): CFD; Smart City; Edge AI; RUL / dự báo thời điểm hư hỏng; predictive maintenance; chẩn đoán hư hỏng hiện trường; Health Index trọng số phức tạp; phần mềm thương mại; bảo trì tự động; hiệu chuẩn FEM; chuyển trực tiếp classifier từ lab sang field.

## 8. Đóng góp dự kiến

1. Bằng chứng phòng thí nghiệm có kiểm soát về phân biệt trạng thái liên kết dưới giao thức đánh giá run-aware, chống rò rỉ.
2. Mô hình dữ liệu truy vết hình thức hóa + bộ tiêu chí đánh giá tái lập được cho lớp bài toán evidence-to-inspection trong quản lý tài sản nhà công nghiệp thép.
3. Bằng chứng khả thi hiện trường của khung truy vết tại công trình thực.
4. Candidate event-aware, accountable and verification-controlled inspection-maintenance support; chưa phải contribution hoàn thành trước G2/G3 validation.

## 8.1 Trạng thái gate ngày 2026-08-04

G1 = `OPEN — PARTIAL EVIDENCE`; G2 = `OPEN — LITERATURE BOUNDARY CLOSED, SPECIFICATION NOT YET FROZEN`; G3 = `OPEN — NOT IMPLEMENTED, NOT VALIDATED, NOT OFFICIALLY PASSED`, execution `NOT OPEN`. `CLOSE_SEARCH` là corpus-bounded, không phải universal absence hoặc G2 PASS.

## 9. Vai trò giới hạn của FEM

FEM tồn tại duy nhất như **mô hình thiết kế tham chiếu danh nghĩa: nominal, không hiệu chuẩn, chỉ tham chiếu, không dùng để chẩn đoán hư hỏng**. Được phép: tham khảo vị trí đặt cảm biến (reference-informed sensor placement); minh họa vị trí/thông tin cấu kiện; nêu giả thuyết cơ học định tính trong Discussion/Limitation với nhãn "hypothesis, not confirmed". Không được: có mục tiêu/RQ/chương/Paper/Evidence Gate riêng; hiệu chuẩn; suy luận mức suy giảm kết cấu hoặc lực siết bu lông; chuyển kết luận định lượng 1:10 → công trình thực; xuất hiện trong tên bất kỳ thành phần cấu trúc nào của luận án.

## 10. Tuyên bố được phép

- Bằng chứng lab phân biệt được các trạng thái liên kết có kiểm soát dưới đánh giá chống rò rỉ. *(kết luận định lượng: candidate pending Gate 1)*
- Khung truy vết liên kết evidence + CEI với cấu kiện và hồ sơ kiểm tra, kiểm chứng qua SCQ/VCQ/RCQ định trước.
- Một quyết định kiểm tra có thể được biện minh và truy trách nhiệm về evidence, confidence, cấu kiện, nghĩa vụ quản lý.
- Khung khả thi khi triển khai tại công trình thực (feasibility, không phải diagnosis).
- FEM danh nghĩa cung cấp tham chiếu bố trí cảm biến.
- CEI là confidence/evidence indicator (cấu trúc metadata, không phải severity).

**Candidate claims (BẮT BUỘC ghi nhãn "Candidate claim pending Gate 1 closure" cho tới khi G1 đóng):**
- "Cấu hình cảm biến ảnh hưởng mạnh hơn lựa chọn kiến trúc mô hình AI."
- RF/1D-CNN/ResNet1D macro-F1 (RF ~0.862; 1D-CNN S12 ~0.841; ResNet1D ~0.828); "ResNet1D corroborates".

**Field: publication (Paper 3) optional; minimum field feasibility evidence BẮT BUỘC** (field sensor register; Sensor_ID→BIM_GUID; data return & completeness; operational baseline; inspection-record workflow; 2–3 traceability scenarios).

## 11. Tuyên bố không được phép

- Chẩn đoán hư hỏng hiện trường khi chưa có kiểm tra xác nhận.
- Mọi tuyên bố dựa trên FEM đã hiệu chuẩn; suy luận suy giảm độ cứng/lực siết từ FEM.
- Chuyển kết luận định lượng từ mô hình 1:10 sang công trình thực.
- RUL, predictive maintenance, dự báo thời điểm hư hỏng.
- Mức độ hư hỏng (severity/DSI); CEI là mức độ hư hỏng vật lý.
- "AI tốt nhất" hoặc ưu việt tổng quát; Health Index trọng số; "optimal sensor placement"; bảo trì tự động; hoàn thiện Digital Twin thương mại; áp dụng phổ quát.

## 12. Hướng mở rộng sau PhD

FEM hiệu chuẩn với EMA và model updating; luật đồng dạng lab → field; predictive maintenance và RUL; Health Index trọng số; triển khai đa công trình; nền tảng thương mại; Edge AI; Smart City.
