**GIẢI THÍCH THUẬT NGỮ**

1.  **Mô hình thông tin công trình và chuẩn trao đổi**

| **Viết tắt** | **Dạng đầy đủ** | **Giải thích** |
|:---|:---|:---|
| BIM | Building Information Modeling | Mô hình thông tin công trình. Trong luận án dùng làm lớp ngữ cảnh cấu kiện |
| IFC | Industry Foundation Classes | Lược đồ dữ liệu mở của buildingSMART cho trao đổi mô hình công trình giữa các phần mềm khác nhau. Là nền định danh cấu kiện của luận án |
| GUID | Globally Unique Identifier | Mã định danh duy nhất toàn cục gán cho từng đối tượng |
| GlobalId | GlobalId trong IFC | Thuộc tính định danh của đối tượng IFC, dạng chuỗi 22 ký tự. Mã này có thể đổi khi mô hình được xuất lại, nên tính bền vững của nó là vấn đề nghiên cứu ở Mục 2.2.3 |
| IDS | Information Delivery Specification | Chuẩn của buildingSMART mô tả yêu cầu thông tin dưới dạng máy đọc được, và kiểm tra tự động xem mô hình có đáp ứng hay không. Đang thay thế mvdXML |
| mvdXML | Model View Definition XML | Cơ chế cũ định nghĩa tập con của IFC cho một mục đích sử dụng. Đang được IDS thay thế |
| ICDD | Information Container for Linked Document Delivery | Container theo ISO 21597 để đóng gói và liên kết tài liệu đa miền |
| BrIM | Bridge Information Modeling | Biến thể của BIM cho công trình cầu |
| CMMS | Computerized Maintenance Management System | Hệ quản lý bảo trì bằng máy tính, nơi lưu lệnh công việc, lịch bảo trì và trạng thái xử lý |
| AIM, PIM | Asset Information Model, Project Information Model | Mô hình thông tin tài sản giai đoạn vận hành, và mô hình thông tin dự án giai đoạn thực hiện |
| CDE | Common Data Environment | Môi trường dữ liệu chung, nơi thông tin được chia sẻ và phê duyệt theo trạng thái |

2.  **Công nghệ web ngữ nghĩa và dữ liệu liên kết**

| **Viết tắt** | **Dạng đầy đủ** | **Giải thích** |
|:---|:---|:---|
| SOSA | Sensor, Observation, Sample, and Actuator | Từ vựng lõi của W3C và OGC mô tả cảm biến, quan trắc, mẫu và cơ cấu chấp hành. Luận án đặt bản ghi bằng chứng trên lớp này |
| SSN | Semantic Sensor Network | Phần mở rộng của SOSA, mô tả hệ cảm biến, quy trình đo và điều kiện triển khai |
| PROV-DM | PROV Data Model | Mô hình dữ liệu nguồn gốc của W3C, gồm ba lớp gốc là thực thể, hoạt động và tác nhân |
| PROV-O | PROV Ontology | Bản thể hóa PROV-DM dưới dạng OWL để máy suy luận được |
| PAV | Provenance, Authoring and Versioning | Từ vựng bổ sung cho PROV, phân biệt tác giả, người đóng góp, người biên tập và phiên bản |
| SHACL | Shapes Constraint Language | Ngôn ngữ ràng buộc của W3C để kiểm tra dữ liệu RDF. Luận án dùng để kiểm chứng quan hệ trong chuỗi truy vết |
| RDF | Resource Description Framework | Mô hình dữ liệu dạng bộ ba chủ thể, vị từ, đối tượng |
| SPARQL | SPARQL Protocol and RDF Query Language | Ngôn ngữ truy vấn dữ liệu RDF |
| OWL | Web Ontology Language | Ngôn ngữ mô tả bản thể luận, cho phép suy luận logic |
| DOLCE | Descriptive Ontology for Linguistic and Cognitive Engineering | Bản thể luận nền, dùng trong bài Borkowski để phân biệt cấu kiện với các giai đoạn vòng đời của nó |

**Ghi chú:**

- W3C là World Wide Web Consortium, tổ chức chuẩn hóa web, ban hành PROV, SOSA/SSN và SHACL. OGC là Open Geospatial Consortium, đồng ban hành SOSA/SSN.

- ISO 19650 là bộ tiêu chuẩn quản lý thông tin theo BIM, trong đó phần 3 năm 2020 dành cho giai đoạn vận hành. ISO 21597 là chuẩn cho container thông tin ICDD.

3.  **Theo dõi trạng thái kết cấu và đánh giá**

| **Viết tắt** | **Tên đầy đủ** | **Giải thích** |
|:---|:---|:---|
| LORO | Leave-One-Run-Out | Giao thức đánh giá giữ lại toàn bộ dữ liệu của một lần chạy làm tập kiểm tra. Trả lời câu hỏi kết quả có khái quát sang lần chạy mới trong cùng bối cảnh hay không |
| LOCO | Leave-One-Campaign-Out | Giữ lại trọn một đợt thí nghiệm, thường là sau khi tháo lắp lại. Khắt khe hơn LORO, trả lời câu hỏi kết quả có sống sót qua một lần lắp đặt mới hay không |
| FEM | Finite Element Method | Phương pháp phần tử hữu hạn. Trong luận án chỉ giữ ở vai trò mô hình danh nghĩa chưa hiệu chuẩn, theo giới hạn ở Mục 5.8.3 |
| VoI | Value of Information | Giá trị của thông tin, lượng hóa lợi ích của việc thu thêm dữ liệu quan trắc trước khi ra quyết định |
| RBI | Risk-Based Inspection | Kế hoạch kiểm tra theo rủi ro, chọn thời điểm và nội dung kiểm tra theo mức rủi ro và giá trị thông tin |

**4. Chuỗi định danh của luận án**

| **Ký hiệu** | **Giải thích** |
|:---|:---|
| Sensor_ID | Định danh nguồn đo, gồm vị trí lắp, loại cảm biến và cấu hình thu nhận |
| BIM_GUID | Định danh cấu kiện trong mô hình, neo vào GlobalId của IFC |
| Condition_Evidence_ID | Định danh bản ghi bằng chứng trạng thái. Bản ghi mang kết quả phân loại kèm nguồn gốc, giao thức đánh giá, độ bất định và phạm vi hiệu lực |
| Inspection_Record_ID | Định danh hồ sơ kiểm tra, có ngày tạo, người thực hiện, kết quả quan sát và lịch sử riêng |
| Action_Status | Trạng thái hành động theo bốn mức Bình thường, Theo dõi, Kiểm tra, Kiểm tra ưu tiên |
| FEM_Node_ID | Định danh nút trong mô hình phần tử hữu hạn. Là siêu dữ liệu tùy chọn, không nằm trong chuỗi bắt buộc |
