**GIẢI THÍCH THUẬT NGỮ**

1.  **Khái niệm cốt lõi của luận án**

| **Thuật ngữ** | **Tiếng Anh** | **Giải thích** |
|:---|:---|:---|
| Kết quả phân loại | classification result | Một giá trị mà mô hình học máy gán cho một mẫu tín hiệu: nhãn, xác suất hoặc điểm số |
| Bằng chứng trạng thái | condition evidence | Một nhận định về tình trạng của một cấu kiện, kèm nguồn tạo ra nó và phạm vi mà nó được phép sử dụng. Nhận định có thể đến từ mô hình chạy trên dữ liệu cảm biến, từ quan sát của kỹ sư hoặc từ phép đo kiểm tra không phá hủy (Mục 1.3) |
| Chẩn đoán hư hỏng | damage diagnosis | Kết luận của kỹ sư sau khi kiểm tra cấu kiện về việc có hư hỏng hay không, vị trí, nguyên nhân và mức độ |
| Nguồn gốc | provenance | Thông tin về dữ liệu nào, quy trình nào và tác nhân nào đã tạo ra một bản ghi |
| Phạm vi hiệu lực | validity scope | Các điều kiện mà trong đó bằng chứng còn đúng: đơn vị suy luận, cách chia dữ liệu khi đánh giá, đợt lắp đặt, cấu hình cảm biến và điều kiện áp dụng |
| Đường cơ sở vận hành | operational baseline | Trạng thái tham chiếu của chính công trình khi vận hành bình thường, ghi kèm dải nhiệt độ và trạng thái cầu trục |
| Vòng lặp kiểm tra tạo nhãn | inspection-labelling loop | Kết quả kiểm tra xác nhận của kỹ sư được ghi thành bản ghi kiểm tra và dùng làm nhãn hiện trường gắn với cấu kiện |
| KT1 | – | Khoảng trống về bằng chứng trạng thái có phạm vi hiệu lực; vế A1 là đánh giá, vế A2 là khai báo (Mục 5.2.1) |
| KT2 | – | Khoảng trống về đường đi từ bằng chứng đến hành động có trách nhiệm (Mục 5.2.2) |
| Mô hình số, bóng số, song sinh số | Digital Model (DM), Digital Shadow (DS), Digital Twin (DT) | Ba mức tích hợp theo chiều và mức tự động của luồng dữ liệu giữa đối tượng vật lý và biểu diễn số (Kritzinger và cộng sự, 2018). Hệ thống của luận án được khai báo ở mức bóng số (Mục 1.1.3) |

2.  **Mô hình thông tin công trình và chuẩn trao đổi**

| **Viết tắt** | **Dạng đầy đủ** | **Giải thích** |
|:---|:---|:---|
| BIM | Building Information Modeling | Mô hình thông tin công trình. Trong luận án dùng làm lớp ngữ cảnh cấu kiện |
| IFC | Industry Foundation Classes | Lược đồ dữ liệu mở của buildingSMART cho trao đổi mô hình công trình giữa các phần mềm khác nhau. Là nền định danh cấu kiện của luận án |
| IFC 4.3 | IFC phiên bản 4.3 | Phiên bản IFC mà mô hình thông tin của luận án mở rộng (Mục 2.2.3) |
| BCF | BIM Collaboration Format | Định dạng của buildingSMART để trao đổi vấn đề gắn với mô hình; BCF 3.0 ghi trạng thái vấn đề và sự kiện đổi trạng thái (Mục 2.2.3) |
| GlobalId | GlobalId trong IFC | Thuộc tính định danh của đối tượng IFC, dạng chuỗi 22 ký tự. Mã này có thể đổi khi mô hình được xuất lại; đây là một giới hạn của định danh, xét ở Mục 2.2.4 |
| IDS | Information Delivery Specification | Chuẩn của buildingSMART mô tả yêu cầu thông tin dưới dạng máy đọc được và kiểm tra tự động mô hình theo yêu cầu đó. Đang thay thế mvdXML. Với luận án, IDS là hướng mở rộng |
| mvdXML | Model View Definition XML | Cơ chế cũ định nghĩa tập con của IFC cho một mục đích sử dụng. Đang được IDS thay thế |
| BrIM | Bridge Information Modeling | Biến thể của BIM cho công trình cầu |
| CMMS | Computerized Maintenance Management System | Hệ quản lý bảo trì bằng máy tính, nơi lưu lệnh công việc, lịch bảo trì và trạng thái xử lý |
| AIM, PIM | Asset Information Model, Project Information Model | Mô hình thông tin tài sản giai đoạn vận hành, và mô hình thông tin dự án giai đoạn thực hiện |
| CDE | Common Data Environment | Môi trường dữ liệu chung, nơi thông tin được chia sẻ và phê duyệt theo trạng thái |

3.  **Từ vựng chuẩn về quan trắc và nguồn gốc**

| **Viết tắt** | **Dạng đầy đủ** | **Giải thích** |
|:---|:---|:---|
| SOSA, SSN | Sensor, Observation, Sample, and Actuator; Semantic Sensor Network | Từ vựng của W3C và OGC mô tả cảm biến, quy trình đo, quan trắc và điều kiện triển khai. Luận án đối chiếu khái niệm với SOSA/SSN bằng một bảng ánh xạ (Phụ lục A, Bảng A.3) |
| PROV-O | PROV Ontology | Từ vựng nguồn gốc của W3C, gồm ba lớp gốc: thực thể, hoạt động và tác nhân |

Ghi chú: W3C là World Wide Web Consortium; OGC là Open Geospatial Consortium. ISO 19650-3:2020 là phần của bộ ISO 19650 dành cho giai đoạn vận hành.

4.  **Dữ liệu thí nghiệm, đánh giá và theo dõi trạng thái kết cấu**

| **Thuật ngữ / viết tắt** | **Tiếng Anh** | **Giải thích** |
|:---|:---|:---|
| Đợt thí nghiệm | campaign | Một chuỗi lần chạy thực hiện liền nhau trên mô hình khung thép; giữa hai đợt có thể có tháo – lắp lại liên kết hoặc cảm biến. Luận án dùng dữ liệu ba đợt |
| Đợt lắp đặt | installation batch | Khoảng thời gian kể từ lần lắp ráp hoặc lần can thiệp gần nhất lên liên kết (siết lại, thay thế). Trong phòng thí nghiệm, đợt lắp đặt đổi khi liên kết được tháo – lắp lại giữa các đợt thí nghiệm; ở hiện trường, đợt lắp đặt đổi khi một hành động can thiệp được xác minh (Phụ lục B) |
| Lần chạy | run | Một lần vận hành thí nghiệm liên tục trong một đợt thí nghiệm, sinh ra nhiều bản ghi |
| Bản ghi (đo) | recording | Một chuỗi tín hiệu thu liên tục trong một lần chạy. Bản ghi là đơn vị chấm điểm khi đánh giá. Khác với "bản ghi bằng chứng", là bản ghi dữ liệu trong mô hình thông tin |
| Cửa sổ tín hiệu | window | Một đoạn cắt từ bản ghi, làm đầu vào cho mô hình. Là đơn vị tính toán, không phải đơn vị độc lập |
| Đánh giá cùng lần chạy | within-run evaluation | Chia tập huấn luyện và tập kiểm tra bên trong cùng các lần chạy, nên dữ liệu kiểm tra có thể đến từ lần chạy đã có trong huấn luyện. Dùng làm mốc để đo mức lạc quan (vế A1) |
| LORO | Leave-One-Run-Out | Giao thức đánh giá giữ lại toàn bộ dữ liệu của một lần chạy làm tập kiểm tra. Trả lời câu hỏi kết quả có khái quát sang lần chạy mới trong cùng bối cảnh hay không |
| LOCO | Leave-One-Campaign-Out | Giữ lại trọn một đợt thí nghiệm, thường là sau khi tháo lắp lại. Khắt khe hơn LORO, trả lời câu hỏi kết quả có giữ được khi sang một đợt lắp đặt mới hay không |
| RF, SVM-RBF | Random Forest; Support Vector Machine với nhân RBF | Hai mô hình học trên đặc trưng thủ công miền thời gian – tần số |
| 1D-CNN, ResNet1D | One-dimensional Convolutional Neural Network; one-dimensional Residual Network | Hai mô hình học sâu học trực tiếp trên tín hiệu đã chuẩn hóa |
| Autoencoder | autoencoder | Bộ tự mã hóa học đường cơ sở vận hành; sai số tái tạo dùng làm chỉ báo bất thường ở hiện trường (Mục 5.7.3) |
| EOV | Environmental and Operational Variability | Biến đổi do môi trường và vận hành (nhiệt độ, cầu trục, máy móc) làm thay đổi tín hiệu mà không do thay đổi trạng thái kết cấu |
| NDT | Non-Destructive Testing | Kiểm tra không phá hủy |
| FEM | Finite Element Method | Phương pháp phần tử hữu hạn. Trong luận án chỉ giữ ở vai trò mô hình danh nghĩa chưa hiệu chuẩn, theo giới hạn ở Mục 5.9.3 |
| VoI | Value of Information | Giá trị của thông tin, lượng hóa lợi ích của việc thu thêm dữ liệu quan trắc trước khi ra quyết định |
| RBI | Risk-Based Inspection | Kế hoạch kiểm tra theo rủi ro, chọn thời điểm và nội dung kiểm tra theo mức rủi ro và giá trị thông tin |

5.  **Mô hình thông tin, định danh và trạng thái**

| **Ký hiệu** | **Giải thích** |
|:---|:---|
| Sensor_ID | Định danh nguồn đo, gồm vị trí lắp, loại cảm biến và cấu hình thu nhận |
| BIM_GUID | Định danh cấu kiện trong mô hình, neo vào GlobalId của IFC |
| Condition_Evidence_ID | Định danh bản ghi bằng chứng trạng thái (thực thể `EVIDENCE`). Bản ghi mang giá trị kèm nguồn gốc, phiên bản phương pháp, độ bất định và phạm vi hiệu lực |
| Inspection_Record_ID | Định danh bản ghi kiểm tra (thực thể `INSPECTION_RECORD`): vai trò người kiểm tra, thời điểm, kết quả và độ bất định của kiểm tra |
| `EVIDENCE_USE` | Bản ghi sử dụng bằng chứng: quan hệ ghi việc một bản ghi kiểm tra dùng một bằng chứng, có cờ trong hay ngoài phạm vi hiệu lực và lý do khi ngoài phạm vi |
| priority_level | Mức ưu tiên của hành động, do logic bốn mức bằng luật đề xuất: Bình thường → Theo dõi → Kiểm tra → Kiểm tra ưu tiên |
| Action_Status | Trạng thái xử lý của hành động: Mở → Đang xử lý → Hoàn thành → Đã xác minh. Suy ra từ sự kiện chuyển trạng thái mới nhất |
| `STATUS_EVENT` | Sự kiện chuyển trạng thái: một lần đổi trạng thái xử lý, ghi trạng thái trước và sau, thời điểm, vai trò người thực hiện, lý do và bản ghi sử dụng bằng chứng làm căn cứ |
| FEM_Node_ID | Định danh nút trong mô hình phần tử hữu hạn. Là siêu dữ liệu tùy chọn, không nằm trong chuỗi bắt buộc |

6.  **Đối chứng, chỉ số và cấu trúc nghiên cứu**

| **Ký hiệu** | **Giải thích** |
|:---|:---|
| B0 | Đối chứng B0: hồ sơ kiểm định theo thực hành hiện hành ở Việt Nam, mã hóa tay 20–30 hồ sơ của nhà xưởng ở Khánh Hòa (cùng BIM với B1) |
| B1 | Đối chứng B1: mô hình chỉ dùng IFC 4.3 theo Bellon và cộng sự (2025) cùng BCF 3.0, chưa có tầng bằng chứng và tầng trách nhiệm, dựng trên cùng BIM nhà xưởng |
| M1 | Mức đủ thuộc tính bắt buộc: tỉ lệ bản ghi có đủ các trường bắt buộc |
| M2 | Tỉ lệ phát hiện lỗi chèn mù, báo cáo theo từng nhóm lỗi. Là chỉ số chính của Mục tiêu 2 |
| M3 | Khả năng truy ngược: thời gian hoặc số bước để trả lời ba câu hỏi của người quản lý |
| M4 | Chi phí ghi nhận: số phút cho mỗi bản ghi |
| MT1–MT3 | Ba mục tiêu cụ thể của luận án (Mục 5.3.3) |
| RQ1–RQ3 | Ba câu hỏi nghiên cứu, ứng 1:1 với ba mục tiêu (Mục 5.4) |
| WP1–WP4 | Các gói công việc: WP1 phòng thí nghiệm, WP2 mô hình thông tin, WP3 hiện trường, WP4 logic hỗ trợ hành động (Bảng 5.3) |
