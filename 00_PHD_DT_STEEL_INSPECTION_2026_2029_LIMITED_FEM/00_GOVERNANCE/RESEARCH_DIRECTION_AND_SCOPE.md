# ĐỊNH HƯỚNG VÀ PHẠM VI NGHIÊN CỨU
**Ngày:** 17/07/2026 | **Cập nhật v2.1:** 19/07/2026 | Đọc sau `MASTER_RESEARCH_CHARTER_v2.1_TRACEABILITY_CORE_20260719.md`; file này giải thích "vì sao", không lặp lại Charter.

> **Cập nhật v2.1:** (1) CEI là first-class attribute của chuỗi (metadata, không scalar/Health Index); (2) mục đích cuối = justification & accountability của quyết định kiểm tra; (3) RQ2 câu gốc đã khóa (xem Charter v2.1 §3); (4) field feasibility — Paper 3 publication optional nhưng **minimum field evidence bắt buộc**.

## 1. Luận án giải quyết vấn đề gì

Chủ công trình nhà công nghiệp khung thép hiện không có cách kiểm chứng được để trả lời: cảnh báo này đến từ cảm biến nào, thuộc cấu kiện nào, lần kiểm tra gần nhất khi nào, hành động đang ở trạng thái gì. Luận án xây dựng và kiểm chứng chuỗi thông tin truy vết từ dữ liệu dao động đến hành động kiểm tra – bảo trì, kèm bằng chứng lab về độ tin cậy của lớp evidence và bằng chứng field về tính khả thi triển khai.

## 2. Vì sao thuộc ngành Quản lý xây dựng

Đóng góp nằm ở **quy trình quản lý thông tin và hỗ trợ quyết định kiểm tra**, không nằm ở mô hình cơ học hay thuật toán mới. Câu hỏi trung tâm là câu hỏi quản lý tài sản (tổ chức, liên kết, truy vết, hỗ trợ quyết định), gắn với chuẩn quản lý thông tin công trình (ISO 19650, TCVN 14177:2024) và yêu cầu hồ sơ bảo trì – quan trắc trong quy định hiện hành. Hội đồng trước đây đã yêu cầu làm nổi bật định vị ngành QLXD; kiến trúc Limited-FEM là kết quả trực tiếp của yêu cầu đó.

## 3. Vai trò của từng thành phần

| Thành phần | Vai trò | Không phải |
|---|---|---|
| Dữ liệu dao động | Nguồn tạo condition evidence có kiểm soát (lab) và baseline vận hành (field) | Công cụ chẩn đoán hư hỏng hiện trường |
| AI/ML | Công cụ phân loại trạng thái trong điều kiện lab, đánh giá run-aware chống rò rỉ | Đóng góp thuật toán; "AI tốt nhất" |
| BIM | Nguồn định danh cấu kiện bền vững (BIM_GUID/IFC GlobalId) làm neo truy vết | Digital Twin "thông minh" tự thân |
| Công trình thực | Nơi kiểm chứng field feasibility: triển khai, baseline, kịch bản truy vết, hồ sơ kiểm tra | Nơi kiểm chứng chẩn đoán hay chuyển giao classifier |
| FEM | Mô hình thiết kế tham chiếu danh nghĩa (nominal, không hiệu chuẩn): tham khảo vị trí cảm biến, minh họa cấu kiện, giả thuyết định tính | Trục nghiên cứu; nguồn chẩn đoán; căn cứ suy luận suy giảm kết cấu |

## 4. Ranh giới ba loại bằng chứng

1. **Bằng chứng thí nghiệm (laboratory evidence):** trạng thái liên kết có kiểm soát trên mô hình 1:10; chỉ chứng minh khả năng phân biệt trạng thái trong điều kiện kiểm soát.
2. **Tính khả thi hiện trường (field feasibility):** khung triển khai được, dữ liệu về, truy vết chạy tại công trình thực; không chứng minh phát hiện hư hỏng thực. **Lưu ý v2.1:** Paper 3 (công bố) là optional/bonus, nhưng **minimum field feasibility evidence là bắt buộc đối với luận án** (field sensor register; Sensor_ID→BIM_GUID; data return & completeness; operational baseline; inspection-record workflow; 2–3 traceability scenarios). **Field preparation** (agreement, BIM/GUID audit, register/mapping/template) được phép làm sớm song song Paper 1–2; **field deployment** (lắp cảm biến, baseline dài hạn, validation) chỉ sau khi G4 mở (Charter §6.1).
3. **Hỗ trợ quyết định (decision support):** logic bốn mức minh bạch, con người rà soát; không phải quyết định tự động và không thay thế đánh giá kỹ thuật.

Ba loại này không được trộn lẫn trong bất kỳ tuyên bố nào. Mọi bất thường hiện trường dẫn đến *kiểm tra*, không dẫn đến *kết luận hư hỏng*.

## 5. Trong và ngoài phạm vi

Trong phạm vi: dataset dao động lab có nhãn + run registry; mô hình dữ liệu truy vết + competency questions + tiêu chí đánh giá; ánh xạ Sensor_ID → BIM_GUID tại field; baseline vận hành; kịch bản truy vết field; hồ sơ kiểm tra và bốn mức hành động.

Ngoài phạm vi: danh mục tại Charter §7 (CFD, Smart City, Edge AI, RUL, predictive maintenance, chẩn đoán hiện trường, Health Index phức tạp, phần mềm thương mại, bảo trì tự động, hiệu chuẩn FEM, chuyển classifier lab→field). Mọi yêu cầu chạm vào danh mục này phải bị từ chối hoặc gắn nhãn Future Work.
