# THUẬT NGỮ VÀ CHỮ VIẾT TẮT

<!-- Bản rút gọn 02/10/2026: gộp sáu bảng (bản v2) thành một bảng các thuật ngữ dùng trong thân bài. -->

| Thuật ngữ, viết tắt | Tiếng Anh | Giải thích |
|:---|:---|:---|
| Bằng chứng trạng thái | condition evidence | Một nhận định về tình trạng của một cấu kiện, kèm nguồn gốc, độ bất định và phạm vi hiệu lực (Mục 1.3) |
| Kết quả phân loại | classification result | Giá trị mô hình học máy gán cho một mẫu tín hiệu: nhãn, xác suất hoặc điểm số |
| Chẩn đoán hư hỏng | damage diagnosis | Kết luận của kỹ sư sau kiểm tra về hư hỏng, vị trí, nguyên nhân và mức độ |
| Bản ghi kiểm tra | inspection record | Bản ghi kết quả một lần kiểm tra của kỹ sư trong mô hình dữ liệu (thực thể `INSPECTION_RECORD`); "hồ sơ kiểm tra" chỉ hồ sơ kiểm tra – kiểm định nói chung |
| Nguồn gốc | provenance | Dữ liệu, quy trình và tác nhân đã tạo ra một bản ghi |
| Phạm vi hiệu lực | validity scope | Các điều kiện mà bằng chứng đã được đánh giá (đơn vị suy luận, cách chia dữ liệu, đợt lắp đặt, cấu hình cảm biến, điều kiện vận hành) và giới hạn sử dụng rút ra từ đó; không bảo đảm từng nhận định đúng (Mục 1.3, 3.3) |
| Đường cơ sở vận hành | operational baseline | Trạng thái tham chiếu của chính công trình khi vận hành bình thường, ghi kèm nhiệt độ và trạng thái cầu trục |
| Vòng lặp kiểm tra tạo nhãn | inspection-labelling loop | Kết quả kiểm tra của kỹ sư được ghi thành bản ghi kiểm tra và dùng làm nhãn hiện trường |
| KT1, KT2, KT3 | – | Ba khoảng trống: bằng chứng có phạm vi hiệu lực (vế A1 đánh giá, A2 khai báo và kiểm khi dùng); từ bằng chứng đến hành động có trách nhiệm; duy trì chuỗi trong vận hành nhà công nghiệp đang khai thác (Mục 5.2) |
| Mô hình số, bóng số, song sinh số | DM, DS, DT | Ba mức tích hợp theo chiều và mức tự động của luồng dữ liệu; song sinh số là mục tiêu kiến trúc của luận án |
| Đợt thí nghiệm, lần thiết lập trạng thái, lần chạy, bản ghi, cửa sổ | campaign, state establishment, run, recording, window | Các cấp của dữ liệu thí nghiệm (Mục 3.2.1); bản ghi là đơn vị chấm điểm, lần chạy hoặc đợt là đơn vị giữ trọn khi chia dữ liệu |
| Đợt lắp đặt | installation batch | Khoảng thời gian kể từ lần lắp ráp hoặc can thiệp gần nhất lên liên kết; trong phòng thí nghiệm, mỗi lần thiết lập trạng thái mở một đợt lắp đặt |
| Đánh giá cùng lần chạy | within-run evaluation | Chia tập huấn luyện và kiểm tra bên trong cùng các lần chạy; mốc đo mức lạc quan |
| LORO, LOCO | Leave-One-Run-Out, Leave-One-Campaign-Out | Giữ lại trọn một lần chạy; giữ lại trọn một đợt thí nghiệm làm tập kiểm tra |
| RF, SVM-RBF, 1D-CNN, ResNet1D | – | Rừng ngẫu nhiên; máy véc-tơ hỗ trợ nhân RBF; mạng tích chập một chiều; mạng phần dư một chiều |
| EOV | Environmental and Operational Variability | Biến đổi do môi trường và vận hành làm đổi tín hiệu mà không do thay đổi kết cấu |
| BIM, IFC | Building Information Modeling; Industry Foundation Classes | Mô hình thông tin công trình; lược đồ dữ liệu mở của buildingSMART |
| BCF | BIM Collaboration Format | Định dạng trao đổi vấn đề gắn với mô hình; BCF 3.0 ghi trạng thái và sự kiện đổi trạng thái |
| CMMS | Computerized Maintenance Management System | Hệ quản lý bảo trì bằng máy tính |
| IDS | Information Delivery Specification | Chuẩn mô tả và kiểm tự động yêu cầu thông tin ở cấp cấu kiện |
| SSN, PROV-O | Semantic Sensor Network; PROV Ontology | Từ vựng của W3C về cảm biến – quan trắc và về nguồn gốc dữ liệu |
| NDT | Non-Destructive Testing | Kiểm tra không phá hủy |
| priority_level | priority level | Mức ưu tiên: Bình thường → Theo dõi → Kiểm tra → Kiểm tra ưu tiên |
| Action_Status | action status | Trạng thái xử lý: Mở → Đang xử lý → Hoàn thành → Đã xác minh |
| B0, B1 | – | Đối chứng: bộ hồ sơ kiểm định cũ của nhà xưởng nghiên cứu; baseline dựa trên các khả năng của IFC 4.3, BCF 3.0 và IDS xác định từ các tiền lệ gần nhất |
| M1–M4 | – | Đủ thuộc tính; tỉ lệ phát hiện lỗi chèn mù và báo lỗi nhầm; truy ngược đúng, đủ rồi mới xét thời gian; công sức ghi nhận (Mục 4.6.3) |
| Mã chủ thể | actor reference | Mã người hoặc tổ chức thực hiện một bước, ghi cùng vai trò tại thời điểm thực hiện (Mục 4.6.2, Phụ lục A) |
| Câu hỏi năng lực | competency question | Câu hỏi mà mô hình truy vết phải trả lời đúng và đủ theo đáp án chuẩn lập trước (Mục 4.4, 4.6.2) |
| MT, RQ, WP, Gate | Evidence Gate | Mục tiêu, câu hỏi nghiên cứu, gói công việc và cổng kiểm chứng của luận án; cổng kiểm chứng là điểm duyệt bằng chứng trước khi kết quả được dùng cho bước sau |
