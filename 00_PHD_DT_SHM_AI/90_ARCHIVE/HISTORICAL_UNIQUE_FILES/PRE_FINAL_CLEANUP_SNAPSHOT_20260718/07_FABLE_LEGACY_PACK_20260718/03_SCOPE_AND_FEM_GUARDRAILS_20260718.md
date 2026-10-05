# SCOPE & FEM GUARDRAILS — BẢN RÚT GỌN CHO PHIÊN LÀM VIỆC
**Ngày:** 2026-07-18 | **Nguồn:** MASTER_RESEARCH_CHARTER_v1.1 §13–16; ADR-2026-001; CLAUDE.md. Bản rút gọn tra cứu nhanh — khi nghi ngờ, đọc bản gốc.

## 1. Vai trò FEM

Mọi lần nhắc FEM bắt buộc kèm: **"nominal, uncalibrated, reference-only, not used for damage diagnosis."**

Được phép: reference-informed sensor placement (biện minh sơ bộ vị trí cảm biến field); minh họa vị trí cấu kiện; giả thuyết cơ học định tính cho các anomaly của Paper 1 (BCJ collapse dưới S2; nhầm lẫn Apex↔BCJ) trong Discussion/Limitation, nhãn "hypothesis, not confirmed"; FEM_Node_ID như metadata tùy chọn.

Bị cấm: hiệu chuẩn hoặc mô tả như đã hiệu chuẩn; chẩn đoán hư hỏng; suy luận suy giảm độ cứng/lực siết bu lông; chuyển định lượng 1:10 → công trình thực; có RQ/WP/chương/paper/gate riêng hoặc xuất hiện trong tên các thành phần đó; là mắt xích bắt buộc trong chuỗi định danh; neo cho "physics-informed condition evidence" hay "optimal sensor placement".

Rủi ro "zombie FEM": mọi nhắc FEM mời gọi câu hỏi "đã hiệu chuẩn chưa? MAC bao nhiêu?" — kiểm soát bằng kỷ luật ngôn ngữ tuyệt đối, FEM chỉ nằm ở một tiểu mục C3 và các mục Limitation.

## 2. Out of Scope (từ chối hoặc gắn nhãn Future Work, kể cả khi được diễn đạt hấp dẫn)

Calibrated FEM / MAC / EMA / model updating; RUL, predictive maintenance, dự báo thời điểm hư hỏng; chẩn đoán hư hỏng hiện trường; Health Index trọng số phức tạp; Edge AI; CFD; Smart City; nền tảng/phần mềm thương mại; bảo trì tự động; chuyển classifier lab → field; severity/DSI.

## 3. Tuyên bố được phép

Bằng chứng lab phân biệt trạng thái liên kết có kiểm soát dưới đánh giá chống rò rỉ; cấu hình cảm biến ảnh hưởng mạnh hơn lựa chọn kiến trúc mô hình; khung truy vết liên kết cảnh báo ↔ cấu kiện ↔ hồ sơ kiểm tra qua kịch bản định trước; khung khả thi triển khai tại công trình thực; FEM danh nghĩa cung cấp tham chiếu bố trí cảm biến; CEI là confidence/evidence indicator.

## 4. Tuyên bố bị cấm

Chẩn đoán hư hỏng hiện trường khi chưa có kiểm tra xác nhận; mọi tuyên bố dựa FEM hiệu chuẩn; chuyển định lượng 1:10 → thực; RUL/predictive maintenance; severity/DSI hoặc CEI là mức hư hỏng vật lý; "AI tốt nhất"/ưu việt tổng quát; Health Index trọng số; "optimal sensor placement"; quyết định bảo trì tự động; Digital Twin thương mại hoàn thiện; áp dụng phổ quát.

## 5. Thuật ngữ

Dùng: data-informed Digital Twin; condition evidence; state-change evidence; BIM-linked component traceability; component-level traceability; field feasibility; inspection-maintenance support; nominal reference model; reference-informed sensor placement; CEI = confidence/evidence indicator.

Cấm trong kiến trúc lõi: calibrated FEM; physics-informed condition evidence; equivalent stiffness degradation; mechanical damage interpretation; optimal sensor placement; FEM-based diagnosis; damage severity; RUL; predictive maintenance; autonomous maintenance decision.

## 6. Kỷ luật bằng chứng

- Bốn loại bằng chứng không trộn lẫn: laboratory evidence / information traceability / field feasibility / management decision support. Mọi bất thường hiện trường dẫn đến *kiểm tra*, không dẫn đến *kết luận hư hỏng*.
- Không bịa citation, DOI, Zotero key, metric, tiêu chuẩn, kết quả. Thiếu bằng chứng: ghi đúng "Evidence is currently insufficient."
- Mọi phân tích theo Claim → Evidence → Limitation → Next action; không bỏ Limitation; không tự đánh dấu COMPLETE.
