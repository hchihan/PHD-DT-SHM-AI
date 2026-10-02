# BẢN GIẢI TRÌNH TIẾP THU GÓP Ý CỦA THẦY HƯỚNG DẪN

**Báo cáo chuyên đề:** Tiểu luận tổng quan – "Tổng quan về hệ thống song sinh kỹ thuật số dựa trên dữ liệu trong giám sát trạng thái và hỗ trợ kiểm tra – bảo trì công trình công nghiệp khung thép"

**Nghiên cứu sinh:** Hồ Chí Hân. **Ngành:** Quản lý xây dựng.

**Bản được giải trình:** bản v2 ngày 02/10/2026 (`xuat_ban/HO_CHI_HAN_TIEU_LUAN_TONG_QUAN_v2_20261002.docx`), so với bản ngày 23/09/2026.

Số mục ghi theo bản v2. Lịch sử sửa từng phiên được lưu trong `revision/changelog.md` và trong nhánh Git `revision-v2`.

## 1. Tiếp thu từng góp ý

| # | Góp ý của thầy | Sửa ở đâu (bản v2) | Sửa như thế nào |
|---|---|---|---|
| G1 | Thiếu lý do chọn nhà công nghiệp khung thép liên kết bu lông | Mục 1.2 (mới), gồm 1.2.1–1.2.4; Dẫn nhập đoạn 5 | Mục 1.2.1 nêu quy mô khu công nghiệp ở Việt Nam theo số liệu Cục Đầu tư nước ngoài (478 khu đã thành lập, 324 khu đang hoạt động, khoảng tháng 11/2025). Nhận định của nghiên cứu sinh về mức phổ biến của nhà khung thép được ghi rõ là nhận định. Mục 1.2.2 nêu ba nhóm yếu tố làm thay đổi trạng thái liên kết bu lông (nới lỏng, ăn mòn trong khí hậu nhiệt đới ẩm, lắp ráp), mỗi nhóm có nguồn. Mục 1.2.3 nêu điều kiện vận hành (cầu trục, máy móc) và chi phí kiểm tra. Mục 1.2.4 xác định khách thể, đối tượng và phạm vi nghiên cứu |
| G2 | Thiếu hạn chế của phương pháp quan trắc hiện tại với công trình công nghiệp | Mục 3.2 (mới), gồm 3.2.1–3.2.3 và 3.2.5 | Mục 3.2.1: kiểm tra trực quan phụ thuộc người kiểm tra (số liệu FHWA: 49 kiểm tra viên; tỷ lệ phát hiện đai ốc hở 24 %). Mục 3.2.2: chi phí và mật độ đo. Mục 3.2.3: biến đổi vận hành – môi trường, gồm rung do cầu trục. Mục 3.2.5 rút hàm ý: cả kết quả kiểm tra của kỹ sư lẫn tín hiệu cảm biến cần được ghi thành bằng chứng có phạm vi hiệu lực |
| G3 | Thiếu kết nối dữ liệu thực nghiệm với thực tế | Mục 3.2.4 (mới); Mục 1.6.3; Mục 5.7.3; Mục 1.2.4 | Mục 3.2.4 tổng hợp bốn nhóm bằng chứng cho thấy bộ phân loại học trong phòng thí nghiệm khó chuyển nguyên sang nhà xưởng. Phần chuyển được là nguyên tắc tổ chức bằng chứng và giao thức đánh giá. Mục 5.7.3 đổi vai công cụ AI ở hiện trường, từ phân loại sang phát hiện bất thường so với đường cơ sở vận hành. Mục 1.2.4 nêu quan hệ giữa khung 1:10, nhà xưởng ở Khánh Hòa (nền đánh giá mô hình thông tin và đối chứng B0) và nhà xưởng ở Đắk Lắk (triển khai thực tế). Theo đúng quyết định của nghiên cứu sinh, tiểu luận chỉ mô tả thiết kế và công cụ, không đưa kết quả thực nghiệm |
| G4 | Chưa rõ "bằng chứng trạng thái" | Mục 1.3 (mới); Bảng 1.1; Mục 3.1.3; Giải thích thuật ngữ | Định nghĩa bằng chứng trạng thái là một nhận định về tình trạng của cấu kiện, kèm nguồn gốc, độ bất định và phạm vi hiệu lực. Mục 1.3 có ví dụ giả định ở cột trục C3. Bảng 1.1 đối chiếu ba khái niệm: kết quả phân loại, bằng chứng trạng thái và chẩn đoán hư hỏng. Thuật ngữ được dùng thống nhất toàn văn |
| G5 | Chuỗi nghiên cứu phức tạp, khó hiểu | Dẫn nhập (viết lại); Mục 1.4 (mới); Mục 5.6.2; Phụ lục A, B | Dẫn nhập mở bằng một kịch bản: bu lông lỏng ở cột C3 và sự cố sáu tháng sau. Mục 1.4 rút ra ba câu hỏi của người quản lý: Cái gì bất thường, ở đâu? Tin được đến mức nào? Ai đã xử lý, dựa vào đâu? Mô hình dữ liệu rút gọn còn sáu thực thể và năm ràng buộc (Mục 5.6.2). Chi tiết định danh, thuộc tính và ràng buộc chuyển sang Phụ lục A, B |
| G6 | Bổ sung công cụ AI dùng cho toàn bộ luận án | Mục 5.7 (mới); Bảng 5.6 | Mục 5.7.1 nêu nguyên tắc "AI tạo bằng chứng, con người quyết định". Ở phòng thí nghiệm có bốn mô hình (RF, SVM-RBF, 1D-CNN, ResNet1D), đánh giá theo nhóm ở hai mức (giữ lại lần chạy, giữ lại đợt), chấm điểm theo bản ghi, kiểm định hoán vị. Ở hiện trường dùng autoencoder kèm bù nhiệt độ và trạng thái cầu trục, cùng vòng lặp kiểm tra tạo nhãn. Phần hồ sơ và hỗ trợ hành động không dùng AI hộp đen. Bảng 5.6 gắn đầu ra của từng công cụ với trường dữ liệu tương ứng |
| G7 | Cần 20–30 tài liệu key, đọc sâu từng tài liệu trước khi chỉ ra khoảng trống | Mục 1.8; Mục 5.1, 5.2; tài liệu làm việc kèm theo | Chốt 30 tài liệu key (12 đọc toàn văn sâu, 18 đọc có trọng tâm); 29 tài liệu đã đọc toàn văn, một tài liệu bỏ. Mỗi tài liệu có ghi chú đọc sâu và một dòng trong ma trận (luận điểm, bằng chứng, giới hạn, tác động tới khoảng trống). Khoảng trống được xác lập bằng phép trừ tiền lệ (Mục 1.8.4, Bảng 5.1), sau khi kiểm các phản chứng gần nhất (BCF 3.0, IFC4, IFC 4.3 theo Bellon và cộng sự, SSN). Kết quả là hai khoảng trống KT1 và KT2 (Mục 5.2), mỗi khoảng trống có từ sáu nhóm căn cứ trở lên |

## 2. Tiếp thu góp ý về mật độ câu giới hạn

Thầy nhận xét các câu giới hạn ("không chứng minh", "không phải", "không thay thế"…) quá dày, khiến văn bản nặng nề. Nghiên cứu sinh đã rà toàn văn theo danh sách câu giới hạn (52 câu, bản v2) và xử lý theo ba loại:
- Câu phân định khái niệm được viết lại theo hướng khẳng định, mỗi chương còn tối đa ba đến bốn câu.
- Câu tự hạ đóng góp được viết lại thành câu kế thừa có dẫn nguồn.
- Câu giới hạn kết luận được gom về Mục 5.9 (Phạm vi, giới hạn và điều kiện diễn giải kết quả).

Sau bước biên tập văn phong, Chương 2–5 hầu như không còn câu thuộc nhóm này ngoài Mục 5.9.

## 3. Các thay đổi khác so với bản 23/09/2026

- **Khoảng trống:** chốt hai khoảng trống (trước đây ba). KT1 là bằng chứng trạng thái có phạm vi hiệu lực, gồm vế đánh giá A1 và vế khai báo A2. KT2 là đường từ bằng chứng đến hành động có trách nhiệm. Yêu cầu về khoảng hiệu lực của ánh xạ cảm biến – cấu kiện chuyển thành ràng buộc C3 của mô hình dữ liệu.
- **Mục tiêu và câu hỏi:** ba mục tiêu ứng một – một với ba câu hỏi nghiên cứu và hai bài báo (Mục 5.3–5.5). Mục tiêu 1 cho Bài báo 1, Mục tiêu 2 cho Bài báo 2. Mục tiêu 3 là chương luận án hoặc phần hiện trường của Bài báo 2.
- **Phương pháp:** bổ sung Bảng 5.4 (câu hỏi – phương pháp – dữ liệu – chỉ số – đối chứng – kế thừa – khác tiền lệ). Mô hình thông tin được đánh giá với hai đối chứng: B0 là hồ sơ kiểm định hiện hành, B1 là IFC 4.3 theo Bellon và cộng sự cùng BCF 3.0. Chỉ số chính là tỉ lệ phát hiện lỗi chèn mù.
- **Đóng góp:** Bảng 5.7 tách đóng góp khoa học (so với mốc cùng lần chạy và với B1) và đóng góp thực tiễn (so với B0 và khả thi trên nhà xưởng thật).
- **Mức tích hợp:** khai báo ở mức bóng số theo phân loại của Kritzinger và cộng sự (Mục 1.1.3). Tên đề tài giữ cụm "song sinh số dựa trên dữ liệu" theo hướng kiến trúc.
- **Bổ sung chuẩn:** ISO 55000:2024 (Mục 2.1.1) và chuẩn biểu diễn vấn đề – hành động (BCF 3.0, IFC4, IFC 4.3) ở Mục 2.2.3.
- **Khai báo sử dụng trí tuệ nhân tạo tạo sinh** đặt ở phần đầu tiểu luận.
- **Danh mục tài liệu** đánh số lại theo chuẩn IEEE, theo thứ tự xuất hiện lần đầu, gồm 114 tài liệu.

## 4. Nội dung chuyển sang giai đoạn luận án

Danh sách các nội dung chưa giải quyết trong phạm vi tiểu luận, kèm lý do và nơi xử lý, xem `revision/chuyen_sang_luan_an.md`.
