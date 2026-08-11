# CHIẾN LƯỢC BA BÀI HỘI THẢO HỖ TRỢ — v1.1

**Phiên bản:** v1.1  
**Ngày ban hành:** 07/08/2026  
**Trạng thái:** SẴN SÀNG TRÌNH THẦY — CHƯA PHẢI PHÊ DUYỆT NỘP BÀI  
**Thay thế:** `CONFERENCE_PAPER_PLAN_v1_0_20260807.md`  
**Cấp quản trị:** Kế hoạch công bố thuộc Supporting Scope; phụ thuộc Charter Limited-FEM, các ADR đã chấp thuận, Evidence Gates và định hướng Papers 1–3.  
**Mục tiêu:** Xây dựng ba bài hội thảo nhỏ có đóng góp độc lập, đồng thời bảo vệ đóng góp lõi, bằng chứng và quyền công bố của luận án.

---

## 1. Phán quyết chiến lược

Giữ chiến lược ba bài hội thảo nhưng thay hoặc thu hẹp cả ba chủ đề của v1.0. Không bài nào được mở, đóng hoặc thay đổi trạng thái Evidence Gate của luận án.

| Mã | Định hướng bài hội thảo | Phân loại | Quan hệ với luận án | Rủi ro chồng lấn sau kiểm soát |
|---|---|---|---|---:|
| **SC-1** | Đánh giá mức độ tương hợp và chất lượng dữ liệu PASCO–ADXL đo đồng bộ | Supporting Scope | Tiếp giáp RQ1/WP1/C4/Paper 1/G1 nhưng không công bố kết quả phân loại hoặc LORO | Trung bình |
| **SC-2** | HPO có kiểm soát ngân sách tính toán cho 1D-CNN trên bộ dữ liệu độc lập | Supporting Scope | Không có RQ, WP, chương, Paper hoặc Gate trong luận án; chỉ là nghiên cứu phương pháp AI hỗ trợ | Thấp |
| **SC-3** | Ánh xạ yêu cầu thông tin tài sản đã kiểm chứng sang thuộc tính IFC | Supporting Scope | Tiếp giáp RQ2/WP2/C5/Paper 2/G2 nhưng chỉ xét thông tin tài sản tĩnh | Trung bình |

**Ưu tiên hiện hành của luận án:** Gate 1 — khóa run registry, hoàn thành đánh giá run-aware/LORO chống rò rỉ và xác nhận sensor mode của ResNet1D. Các bài hội thảo không được làm chậm ba việc này.

---

## 2. Firewall công bố và đạo đức học thuật

### 2.1 Quy tắc đúng

Mức độ chồng lấn phải được đánh giá trên toàn bộ **câu hỏi nghiên cứu, dữ liệu, phương pháp, phân tích, kết quả, hình, bảng, thảo luận và kết luận**. Chỉ đổi tiêu đề hoặc câu kết luận không đủ để tạo ra một bài độc lập.

Do đó:

1. Không nộp đồng thời các bản thảo chồng lấn đáng kể.
2. Khi nộp phải khai báo các bài hội thảo, bản thảo tạp chí và bộ dữ liệu có liên quan.
3. Phải trích dẫn bài trước nếu dữ liệu, phiên đo hoặc phương pháp đã được công bố.
4. Không tái sử dụng kết quả, hình, bảng hoặc phần văn bản đáng kể nếu chưa khai báo và chưa có quyền sử dụng.
5. Trước khi nộp phải kiểm tra chính sách của cả proceedings hội thảo và tạp chí dự kiến nộp bài lõi sau này.
6. Nếu chính sách không rõ, chuyển sang abstract/poster không lưu proceedings hoặc hoãn nộp.

Các kiểm soát này phù hợp với nguyên tắc chung của [COPE về nội dung trùng lặp và salami slicing](https://publicationethics.org/guidance/cope-position/handling-duplicated-or-redundant-content-salami-slicing) và [chính sách đạo đức xuất bản của Elsevier](https://www.elsevier.com/about/policies-and-standards/publishing-ethics). Chính sách của đúng hội thảo và tạp chí mục tiêu vẫn là căn cứ quyết định cuối cùng.

### 2.2 Nội dung lõi phải được bảo vệ

| Đầu ra lõi | Nội dung dành riêng | Nội dung bị cấm trong bài hỗ trợ |
|---|---|---|
| **Paper 1 / G1** | Run registry với vai trò bằng chứng; so sánh random split với run-aware/LORO; xếp hạng cấu hình cảm biến; so sánh RF/CNN/ResNet1D; kết quả phân loại trạng thái kiểm soát; diễn giải CEI | SC-1 không được phân loại S0/B1/B2/B3, so sánh split, xếp hạng cấu hình hoặc báo cáo metric của Paper 1. SC-2 không được dùng Campaign 1–3. |
| **Paper 2 / G2–G3** | Schema truy vết hình thức; chuỗi định danh lõi; competency questions; truy vấn hai chiều evidence-to-record; vòng đời Inspection_Record và Action_Status; quyền hạn, xác nhận và đóng hồ sơ | SC-3 không được sử dụng Sensor_ID, Condition_Evidence_ID, Inspection_Record_ID, Action_Status, Status_Event hoặc competency questions của Paper 2. |
| **Paper 3 / G4** | Triển khai hiện trường, baseline vận hành, truy vết hiện trường và quy trình hồ sơ kiểm tra tại Rapexco | Không bài hỗ trợ nào được tuyên bố field feasibility, chẩn đoán hiện trường hoặc chuyển giao lab-to-field. |

### 2.3 Tuyên bố cấm chung

- Không chẩn đoán hư hỏng hiện trường, field readiness, predictive maintenance hoặc RUL.
- Không chuyển kết luận định lượng từ khung 1:10 sang công trình thực.
- Không mô tả CEI/softmax là xác suất hư hỏng, mức độ hư hỏng vật lý hoặc Health Index.
- Không FEM hiệu chuẩn, chẩn đoán bằng FEM, suy luận suy giảm độ cứng hoặc “optimal sensor placement”.
- Không tuyên bố bất kỳ SC nào đã kiểm chứng hoặc đóng G1–G4.
- Không công bố kết quả ResNet1D chưa khóa của bộ dữ liệu lõi.

---

## 3. SC-1 — Mức độ tương hợp PASCO–ADXL

### 3.1 Tên bài dự kiến

**Cross-Sensor Agreement and Data-Quality Assessment of Synchronized PASCO and ADXL Measurements on a Scaled Steel Frame**

Tên thay thế:

**Assessing Agreement between Low-Cost Vibration Measurement Systems under Synchronized Laboratory Excitation**

### 3.2 Vị trí trong kiến trúc nghiên cứu

| Hạng mục | Quyết định |
|---|---|
| Ánh xạ luận án | Tiếp giáp RQ1/WP1/C4/Paper 1/G1 |
| Trạng thái chính thức | Supporting Scope; không có RQ hoặc Gate riêng |
| Đơn vị phân tích | Một cặp phép đo PASCO–ADXL đồng bộ |
| Mục tiêu chính | Đánh giá tương hợp thiết bị và đặc trưng chất lượng dữ liệu |
| Không nhằm | Phân loại trạng thái hoặc tối ưu cấu hình cảm biến |

### 3.3 Claim → Evidence → Limitation → Next action

**Claim.** Trong cùng khoảng thời gian hợp lệ và dải tần chung đã xác định, hai hệ thống có mức độ tương hợp đo được, đồng thời tồn tại các khác biệt có hệ thống về chất lượng tín hiệu và đặc trưng phổ.

**Evidence.** Hồ sơ thí nghiệm hiện có cho thấy 36 cặp đo đồng bộ: 4 trạng thái × 3 loại kích thích × 3 run, với PASCO và ADXL tại các vị trí tương ứng. Chỉ được dùng con số này trong bài sau khi paired-file registry xác nhận tên file, thời gian, vị trí, trục, tần số lấy mẫu và khoảng dữ liệu hợp lệ.

**Limitation.** Bằng chứng chỉ có giá trị đối với thiết bị, cách gá, khung thí nghiệm, điều kiện kích thích và dải tần chung đã khảo sát. Kết quả không chứng minh hai hệ thống có thể thay thế nhau trong mọi trường hợp, không chứng minh hiệu quả hiện trường và không chứng minh khả năng chẩn đoán.

**Next action.** Tạo và khóa `PASCO_ADXL_PAIR_REGISTRY` trước mọi phân tích thống kê.

### 3.4 Câu hỏi nghiên cứu hỗ trợ

1. Các phép đo PASCO và ADXL đồng bộ tương hợp đến mức nào về các chỉ báo miền thời gian và miền tần số trong dải dữ liệu chung hợp lệ?
2. Những khác biệt chất lượng nào lặp lại theo tần số lấy mẫu, thời lượng hợp lệ, giá trị thiếu, bão hòa, kênh phẳng hoặc độ trễ thời gian?

Đây chỉ là câu hỏi hỗ trợ, không sửa hoặc bổ sung RQ1 của luận án.

### 3.5 Phương pháp tối thiểu

1. Kiểm tra cặp file, tính đồng thời, vị trí cảm biến, trục đo và tần số lấy mẫu.
2. Cắt đoạn thời gian hợp lệ chung. NaN tập trung ở cuối file PASCO được xem là giới hạn xuất dữ liệu, không tự động coi là lỗi phép đo.
3. Ước lượng và báo cáo độ trễ thời gian; không căn chỉnh âm thầm.
4. Giới hạn so sánh trong dải tần chung đã khai báo trước; lọc chống aliasing trước khi giảm tần số lấy mẫu.
5. Sử dụng một bộ metric gọn:
   - thời lượng hợp lệ, giá trị thiếu, kênh phẳng và bão hòa;
   - độ trễ tương quan chéo và mức tương hợp dạng sóng đã chuẩn hóa;
   - sai khác tần số trội và độ tương đồng mật độ phổ công suất;
   - magnitude-squared coherence hoặc chỉ số tương hợp phổ tương đương đã khai báo trước.
6. Có thể phân tầng kết quả mô tả theo điều kiện kích thích. Nhãn trạng thái chỉ được dùng để phân tầng, không được dùng làm biến đích dự báo.
7. Báo cáo kết quả theo từng run và độ biến thiên, không chỉ báo cáo trung bình gộp.

### 3.6 Nội dung loại trừ

- Không dùng RF, SVM, logistic regression, 1D-CNN hoặc ResNet1D để phân loại.
- Không random split, LORO, LOCO hoặc phân tích leakage.
- Không xếp hạng S1/S2/S3 hoặc cấu hình cảm biến.
- Không Autoencoder và không claim về phát hiện bất thường hiện trường sau này.
- Không tuyên bố PASCO hoặc ADXL tốt hơn một cách phổ quát.

### 3.7 Điều kiện Go / No-Go

**GO khi và chỉ khi:** cặp đo và tính đồng vị trí được xác nhận; có đủ thời lượng chung hợp lệ; biết rõ sampling rate và trục đo; kế hoạch phân tích được khóa trước khi xem kết quả so sánh cuối cùng.

**NO-GO nếu:** không thể khôi phục tính đồng bộ; vị trí cảm biến không thể so sánh; đóng góp chính phải dựa vào phân loại trạng thái; hoặc chính sách tạp chí của Paper 1 không cho phép tái sử dụng minh bạch các phiên đo đã ghép cặp.

### 3.8 Cấu trúc bài 6 trang

1. Bối cảnh đo lường và khoảng trống nghiên cứu  
2. Bộ dữ liệu PASCO–ADXL đồng bộ và pair registry  
3. Giao thức căn chỉnh, dải tần chung và kiểm soát chất lượng  
4. Kết quả tương hợp miền thời gian và tần số  
5. Hàm ý thực hành cho thu nhận dữ liệu trong phòng thí nghiệm  
6. Giới hạn và kết luận

---

## 4. SC-2 — HPO theo ngân sách tính toán trên dữ liệu độc lập

### 4.1 Tên bài dự kiến

**Compute-Budget-Aware Hyperparameter Optimization for 1D-CNN-Based Structural Vibration Classification: A Fair Comparative Study**

Tên thay thế:

**Performance versus Search Cost in Hyperparameter Optimization of 1D-CNN Models for Structural Vibration Data**

### 4.2 Vị trí trong kiến trúc nghiên cứu

| Hạng mục | Quyết định |
|---|---|
| Ánh xạ luận án | Không |
| Trạng thái chính thức | Supporting Scope; nghiên cứu phương pháp AI độc lập |
| Quy tắc dữ liệu | Benchmark công khai hoặc dữ liệu của hướng nghiên cứu phụ, có quyền sử dụng và nguồn gốc rõ ràng |
| Mục tiêu chính | So sánh các chiến lược HPO dưới cùng ngân sách tính toán đã khai báo |
| Không nhằm | Tạo evidence cho G1 hoặc xếp hạng mô hình trên dữ liệu luận án |

### 4.3 Claim → Evidence → Limitation → Next action

**Claim.** Dưới cùng ngân sách tìm kiếm minh bạch, các chiến lược HPO khác nhau không chỉ về macro-F1 tốt nhất mà còn về độ ổn định, tốc độ hội tụ và chi phí tính toán.

**Evidence.** Đánh giá lồng và lặp lại đối với các phương pháp ứng viên như Random Search, GWO và SAFCA, với cùng số lần đánh giá hàm mục tiêu, giao thức huấn luyện và lịch seed. Danh sách thuật toán cuối cùng chỉ được khóa sau kiểm tra khả năng tái lập; không giữ một thuật toán chỉ vì đã có mã nguồn.

**Limitation.** Kết luận phụ thuộc bộ dữ liệu, không gian tìm kiếm, ngân sách, giao thức huấn luyện và phần cứng. Kết quả không chứng minh một thuật toán vượt trội phổ quát, không chuyển sang dữ liệu luận án và không chuyển sang công trình thực.

**Next action.** Chọn một bộ dữ liệu độc lập và lập phiếu một trang về nguồn gốc, quyền sử dụng và cấu trúc nhóm dữ liệu trước khi chạy HPO.

### 4.4 Câu hỏi nghiên cứu hỗ trợ

1. Dưới cùng số lần đánh giá hàm mục tiêu, chiến lược HPO nào cho cân bằng hiệu năng–chi phí tốt nhất đối với tác vụ 1D-CNN đã chọn?
2. Siêu tham số được chọn và hiệu năng test ổn định đến mức nào qua các outer fold và seed lặp lại?

### 4.5 Phương pháp tối thiểu

1. Khóa bộ dữ liệu, định nghĩa nhãn, đơn vị nhóm, không gian tìm kiếm và ngân sách tính toán.
2. Dùng nested group-aware evaluation nếu dữ liệu có run/specimen/subject tự nhiên; nếu không, dùng thiết kế nested stratified có giải trình.
3. Giữ giống nhau giữa các phương pháp HPO: preprocessing, khởi tạo mô hình, early stopping và metric đánh giá.
4. So sánh dưới cùng số lần đánh giá hàm mục tiêu; bổ sung wall-clock time hoặc thời gian accelerator như chi phí tham chiếu.
5. Kết quả chính: macro-F1 trên outer test. Kết quả phụ: độ biến thiên, đường hội tụ, trial thất bại và chi phí tính toán.
6. Lặp lại nhiều seed và báo cáo phân bố, không chỉ lấy trial tốt nhất.
7. Lưu toàn bộ trial log và cấu hình cuối để tái lập.

### 4.6 Nội dung loại trừ

- Không dùng Campaign 1, Campaign 2, Campaign 3 hoặc các window dẫn xuất từ dữ liệu luận án.
- Không dùng cấu hình cảm biến, run registry, kết quả LORO hoặc CEI của Paper 1.
- Không claim thuật toán tối ưu mới nếu chưa thật sự phát triển và kiểm chứng độc lập; đây không phải mục tiêu hiện tại.
- Không thêm claim Quản lý xây dựng, Digital Twin, BIM hoặc hiện trường chỉ để làm bài có vẻ liên quan đến luận án.

### 4.7 Điều kiện Go / No-Go

**GO khi và chỉ khi:** bộ dữ liệu hoàn toàn độc lập; quyền sử dụng rõ; metadata nhóm đủ để thiết kế đánh giá hợp lệ; mọi HPO chạy tái lập; ngân sách chung đã khóa.

**NO-GO nếu:** chỉ có thể dùng Campaign 1–3; một phương pháp được tuning nhiều hơn; đơn vị nhóm không rõ; hoặc kết quả phụ thuộc việc chọn seed tốt nhất.

### 4.8 Cấu trúc bài 6–8 trang

1. Động cơ và khoảng trống của so sánh công bằng  
2. Bộ dữ liệu và đơn vị đánh giá  
3. Mô hình 1D-CNN và không gian tìm kiếm chung  
4. Giao thức HPO chuẩn hóa theo ngân sách  
5. Kết quả hiệu năng, độ ổn định và chi phí tính toán  
6. Phân tích độ nhạy và giới hạn  
7. Kết luận

---

## 5. SC-3 — Từ yêu cầu thông tin tài sản đến IFC

### 5.1 Tên bài dự kiến

**From Asset-Information Requirements to IFC Properties: A Validation-Oriented Mapping for Building Maintenance Data**

Tên thay thế:

**A Requirement-to-IFC Mapping for Static Asset Information in Building Maintenance Management**

### 5.2 Vị trí trong kiến trúc nghiên cứu

| Hạng mục | Quyết định |
|---|---|
| Ánh xạ luận án | Tiếp giáp RQ2/WP2/C5/Paper 2/G2 |
| Trạng thái chính thức | Supporting Scope; chỉ xét tập con thông tin tài sản tĩnh |
| Đơn vị phân tích | Một yêu cầu thông tin đã kiểm chứng được ánh xạ sang biểu diễn IFC hoặc hồ sơ ngoài IFC |
| Mục tiêu chính | Ánh xạ requirement-to-field và kiểm tra chất lượng dữ liệu tĩnh |
| Không nhằm | Truy vết evidence-to-inspection hoặc vòng đời hành động |

### 5.3 Claim → Evidence → Limitation → Next action

**Claim.** Một tập yêu cầu thông tin tài sản tĩnh được kiểm chứng đến cấp điều khoản có thể được biểu diễn bằng ma trận liên kết từng yêu cầu với entity/property IFC hoặc hồ sơ ngoài IFC, kèm quy tắc kiểm tra bằng máy.

**Evidence.** Lập requirement matrix chỉ từ nguồn chính thức đã xác nhận điều khoản, sau đó thực hiện một pilot Revit–IFC round-trip trên mẫu cấu kiện cố định. Các trường ứng viên có thể gồm mã tài sản, định danh BIM/IFC, loại đối tượng, vị trí, tài liệu liên kết, nguồn dữ liệu, trạng thái thông tin và metadata cập nhật; không trường nào được gọi là “bắt buộc theo tiêu chuẩn” trước khi điều khoản tương ứng được kiểm chứng.

**Limitation.** Nghiên cứu chỉ chứng minh một ánh xạ giới hạn và phép kiểm tra chất lượng dữ liệu. Kết quả không chứng minh tuân thủ AIM đầy đủ, không chứng minh Digital Twin vận hành, không chứng minh truy vết inspection-action và không đại diện cho mọi phần mềm BIM.

**Next action.** Thu thập văn bản chính thức và lập bảng bằng chứng điều khoản cho TCVN 14177:2024 cùng các tài liệu ISO 19650 được lựa chọn trước khi khóa danh sách trường.

### 5.4 Câu hỏi nghiên cứu hỗ trợ

1. Những yêu cầu thông tin tài sản tĩnh nào đã được kiểm chứng có thể biểu diễn trực tiếp trong IFC; yêu cầu nào cần hồ sơ ngoài IFC được kiểm soát?
2. Có thể kiểm tra tái lập sự hiện diện, kiểu dữ liệu, tính duy nhất và khả năng giữ giá trị qua vòng Revit–IFC hay không?

Các câu hỏi này không thay thế competency questions được đăng ký trước của Paper 2.

### 5.5 Ma trận ánh xạ bắt buộc

| Cột | Mục đích |
|---|---|
| Requirement_ID | Định danh ổn định được tạo cho nghiên cứu này |
| Nguồn và điều khoản | Vị trí chính xác trong tiêu chuẩn/quy định/tài liệu |
| Nội dung yêu cầu | Diễn giải ngắn, trung thành; không tự tạo nghĩa vụ |
| Bắt buộc / tùy chọn / có điều kiện | Phân loại có bằng chứng từ nguồn |
| Trường thông tin tài sản | Tên trường đã chuẩn hóa |
| Biểu diễn IFC | Entity, property chuẩn hoặc user-defined property |
| Biểu diễn ngoài IFC | Trường hồ sơ/cơ sở dữ liệu khi IFC không phù hợp |
| Kiểu dữ liệu và giá trị cho phép | Định nghĩa có thể kiểm tra bằng máy |
| Quy tắc kiểm tra | Hiện diện, định dạng, duy nhất, toàn vẹn tham chiếu hoặc khả năng giữ giá trị |
| Kết quả pilot | Pass / limitation / fail kèm bằng chứng |

### 5.6 Phương pháp tối thiểu

1. Kiểm chứng tiêu chuẩn và văn bản quản lý đến cấp điều khoản.
2. Định nghĩa một tập con thông tin tài sản tĩnh có chủ ý và đủ nhỏ.
3. Ánh xạ từng yêu cầu sang IFC hoặc biểu diễn ngoài IFC có giải trình.
4. Xác định quy tắc kiểm tra trước khi chạy round-trip.
5. Áp dụng ánh xạ cho mẫu cấu kiện cố định và đã khai báo.
6. Xuất, mở lại và kiểm tra sự hiện diện, kiểu dữ liệu, tính duy nhất và khả năng giữ nguyên giá trị.
7. Báo cáo Pass, limitation và fail; không biến limitation thành claim tuân thủ.

### 5.7 Nội dung loại trừ

- Không sử dụng chuỗi `Sensor_ID → BIM_GUID → Condition_Evidence_ID → Inspection_Record_ID → Action_Status`.
- Không xây schema Condition_Evidence, Inspection_Record, Action_Status hoặc Status_Event.
- Không dùng competency questions, kiểm tra truy vết hai chiều, quyền hạn, xác nhận, đóng hoặc mở lại hồ sơ của Paper 2.
- Không dùng baseline hiện trường, ánh xạ cảm biến hiện trường hoặc kết quả khả thi Rapexco.
- Không claim “AIM tuân thủ TCVN” nếu chưa có đánh giá tuân thủ chính thức riêng. Cách viết ưu tiên: **aligned with the verified requirements selected for this study**.

### 5.8 Điều kiện Go / No-Go

**GO khi và chỉ khi:** có văn bản nguồn chính thức; mỗi yêu cầu đều có neo điều khoản; tập trường chỉ là thông tin tĩnh; pilot độc lập với schema truy vết động của Paper 2.

**NO-GO nếu:** không thể kiểm chứng tiêu chuẩn; đóng góp phải dùng Condition_Evidence hoặc Inspection_Record; hoặc bài tái sử dụng competency questions/kết quả của Paper 2.

### 5.9 Cấu trúc bài 6–8 trang

1. Vấn đề quản lý thông tin tài sản  
2. Phạm vi và nguồn yêu cầu đã kiểm chứng  
3. Phương pháp ánh xạ requirement-to-IFC  
4. Tập trường tĩnh và quy tắc kiểm tra  
5. Pilot round-trip và kết quả  
6. Hàm ý, giới hạn và kết luận

---

## 6. Ma trận chống chồng lấn

| Thành phần nghiên cứu | Paper 1 | Paper 2 | Paper 3 | SC-1 | SC-2 | SC-3 |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| Phân loại trạng thái kiểm soát | **Lõi** | Đầu vào | — | Loại trừ | Loại trừ | — |
| Random split so với run-aware/LORO | **Lõi** | — | — | Loại trừ | Loại trừ | — |
| So sánh cấu hình cảm biến | **Lõi** | — | — | Loại trừ | Loại trừ | — |
| Tương hợp phép đo PASCO–ADXL | — | — | — | **Chính** | — | — |
| Cân bằng hiệu năng–chi phí HPO | — | — | — | — | **Chính; dữ liệu độc lập** | — |
| Schema evidence-to-record hình thức | — | **Lõi** | Áp dụng | Loại trừ | — | Loại trừ |
| Competency questions và truy vết hai chiều | — | **Lõi** | Áp dụng | — | — | Loại trừ |
| Ánh xạ yêu cầu thông tin tĩnh sang IFC | — | Công cụ/bối cảnh | — | — | — | **Chính** |
| Baseline hiện trường và khả thi Rapexco | — | — | **Lõi** | Loại trừ | Loại trừ | Loại trừ |
| Hỗ trợ hành động bốn mức | — | Ranh giới | **Lõi/Paper 4 tùy chọn** | Loại trừ | Loại trừ | Loại trừ |

---

## 7. Thứ tự thực hiện và bảo vệ nguồn lực

### 7.1 Thứ tự nộp khuyến nghị

1. **SC-2 nộp trước**, khi và chỉ khi bộ dữ liệu độc lập đã sẵn sàng. Đây là bài có firewall sạch nhất.
2. **SC-1 chỉ hoàn tất sau khi phân tích lõi và bảng/hình của Paper 1 đã khóa; tốt nhất sau khi Paper 1 đã nộp.** Nếu muốn nộp sớm hơn phải có chấp thuận bằng văn bản của thầy và xác nhận chính sách prior publication của cả hai venue.
3. **SC-3 chỉ hoàn tất sau khi ranh giới đóng góp Paper 2 và bộ competency questions của G2 đã khóa.** Có thể chuẩn bị ánh xạ tĩnh sớm hơn nhưng không đưa nội dung truy vết động vào bài.

Nếu các điều kiện trên xung đột với deadline hội thảo, phải bảo vệ bài tạp chí lõi và hoãn bài hội thảo. Deadline không phải lý do để hạ firewall.

### 7.2 Kế hoạch theo giai đoạn

| Giai đoạn | Công việc | Đầu ra | Điều kiện dừng |
|---|---|---|---|
| **S0 — Thầy chấp thuận** | Trình v1.1, thống nhất chủ đề, phạm vi và thứ tự | Quyết định Go/No-Go được ghi nhận | Chưa đồng ý → chưa nộp |
| **S1 — Sẵn sàng bằng chứng** | SC-1 pair registry; SC-2 phiếu dữ liệu độc lập; SC-3 bảng bằng chứng điều khoản | Ba hồ sơ readiness | Hở provenance → dừng bài tương ứng |
| **S2 — Khóa trước phân tích** | Khóa câu hỏi, kết quả chính, loại trừ, split/evaluation và hình dự kiến trước khi chạy cuối | Protocol một trang cho từng bài | Trôi phạm vi vào core → dừng |
| **S3 — Pilot** | Chạy pilot kỹ thuật nhỏ để kiểm tra khả thi, không tối ưu câu chuyện | Báo cáo pilot ghi cả fail/limitation | Claim chính không được hỗ trợ → thiết kế lại hoặc bỏ |
| **S4 — Chọn venue** | Kiểm tra proceedings, indexing, copyright, prior publication, page limit và deadline | Phiếu quyết định venue | Chính sách không rõ/không phù hợp → đổi venue |
| **S5 — Viết và audit** | Viết từng bài; hoàn thành ma trận chồng lấn và disclosure | Manuscript sẵn sàng nộp | Có claim/kết quả lõi bị tái sử dụng → bỏ hoặc hoãn |

### 7.3 Quy tắc bảo vệ Gate 1

Cho đến khi G1 đóng về mặt kỹ thuật, công việc hội thảo chỉ giới hạn ở các nhiệm vụ readiness không cạnh tranh với run registry, LORO và xác nhận ResNet1D. Không deadline hội thảo nào được phép thay đổi thứ tự ưu tiên Gate 1 nếu chưa có chỉ đạo rõ của thầy hướng dẫn.

---

## 8. Checklist bắt buộc trước khi nộp

### Tính độc lập khoa học

- [ ] Câu hỏi nghiên cứu không phải RQ lõi hoặc phiên bản thu nhỏ của RQ lõi.
- [ ] Kết quả chính không xuất hiện trong Papers 1–3.
- [ ] Nguồn gốc dữ liệu, phần phiên đo dùng chung và các lần sử dụng trước được khai báo.
- [ ] Không tái sử dụng kết quả, bảng, hình hoặc phần văn bản đáng kể của bài lõi.
- [ ] Limitation mô tả đúng giới hạn khoa học, không dùng câu “internal gate chưa đóng”.

### Phương pháp và bằng chứng

- [ ] Đơn vị phân tích và đơn vị nhóm được nêu rõ.
- [ ] Protocol được khóa trước các lần chạy so sánh cuối.
- [ ] Kết quả được báo cáo theo run/fold/seed khi phù hợp, kèm độ biến thiên.
- [ ] Kết quả thất bại hoặc không kết luận được vẫn được giữ trong hồ sơ.
- [ ] Bằng chứng đủ cho claim; nếu chưa đủ phải ghi **Evidence is currently insufficient**.

### Đạo đức công bố và quản trị

- [ ] Đã kiểm tra chính sách của proceedings và tạp chí dự kiến nộp sau.
- [ ] Không có bản thảo chồng lấn đáng kể đang được xét đồng thời.
- [ ] Bài liên quan và dữ liệu dùng chung được khai báo trong cover letter.
- [ ] Authorship và mức đóng góp đã thống nhất trước khi nộp.
- [ ] Cả hai thầy đã xem ma trận chồng lấn cuối và đồng ý nộp.

---

## 9. Câu limitation dự kiến

**SC-1:**  
*The findings are limited to the tested sensors, mounting arrangement, controlled laboratory frame, excitation conditions and common measurable bandwidth. Agreement should not be interpreted as universal sensor interchangeability, field performance or damage-diagnosis capability.*

**SC-2:**  
*The comparison is conditional on the selected dataset, search space, evaluation budget, training protocol and hardware. It does not establish general optimizer superiority or transferability to other structural systems or field monitoring.*

**SC-3:**  
*The study evaluates a bounded, clause-verified subset of static asset information and a limited round-trip pilot. It does not demonstrate full AIM compliance, operational Digital Twin capability or evidence-to-inspection traceability.*

---

## 10. Nội dung xin ý kiến thầy

1. Chấp thuận ba chủ đề là **Supporting Scope**, không có RQ, WP, chương, Paper hoặc Evidence Gate riêng trong luận án.
2. SC-1 chỉ được triển khai sau khi khóa paired-data registry và bảo vệ kết quả lõi Paper 1.
3. SC-2 bắt buộc dùng bộ dữ liệu hoàn toàn độc lập.
4. SC-3 chỉ xét trường thông tin tài sản tĩnh đã kiểm chứng, loại trừ chuỗi truy vết của Paper 2.
5. Trước mỗi lần nộp phải audit chồng lấn và kiểm tra chính sách venue.

### Đoạn trình bày ngắn với thầy

> Em dự kiến ba bài hội thảo nhỏ thuộc phạm vi hỗ trợ, gồm: so sánh mức độ tương hợp PASCO–ADXL; đánh giá HPO của 1D-CNN trên một bộ dữ liệu độc lập; và ánh xạ yêu cầu thông tin tài sản tĩnh sang IFC. Ba bài không sử dụng kết quả LORO, không xếp hạng cấu hình cảm biến, không công bố chuỗi Condition Evidence–Inspection Record–Action Status và không dùng dữ liệu hiện trường Rapexco. Em xin thầy thống nhất phạm vi và thứ tự thực hiện; trước mỗi lần nộp, em sẽ lập ma trận chồng lấn, kiểm tra chính sách proceedings và xin thầy duyệt Go/No-Go. Gate 1 vẫn là ưu tiên trước hết.

---

## 11. Hành động tiếp theo

| Ưu tiên | Công việc | Đầu ra |
|---:|---|---|
| 1 | Tiếp tục Gate 1: run registry → LORO → xác nhận sensor mode ResNet1D | Bằng chứng kỹ thuật G1 |
| 2 | Trình v1.1 cho hai thầy | Quyết định phạm vi được ghi nhận |
| 3 | Lập paired-file registry cho SC-1 | Danh mục 36 cặp đã xác nhận hoặc số lượng được hiệu chỉnh |
| 4 | Chọn và kiểm chứng bộ dữ liệu độc lập cho SC-2 | Phiếu nguồn gốc/quyền sử dụng dữ liệu |
| 5 | Thu thập văn bản tiêu chuẩn chính thức và lập clause-evidence table cho SC-3 | Ma trận nguồn đã kiểm chứng |
| 6 | Chỉ sàng lọc hội thảo sau khi từng bài đạt điều kiện Go | Phiếu quyết định venue |

---

## 12. Source-of-truth sử dụng

Kế hoạch này phụ thuộc và phải phù hợp với:

- `MASTER_RESEARCH_CHARTER.md`
- `MASTER_RESEARCH_CHARTER_v1.1_LIMITED_FEM_20260717.md`
- `RESEARCH_DIRECTION_AND_SCOPE.md`
- `RESEARCH_ARCHITECTURE.md`
- `CURRENT_STATUS_AND_NEXT_DIRECTION.md`
- `RESEARCH_ARCHITECTURE_DECISION_RECORD_20260717.md`
- `THE_COUNCIL_REVIEW_FEM_OR_NO_FEM_17.07.2026.md`

Nếu quyết định mới đã được hai thầy chấp thuận khác với tài liệu này, quyết định của thầy có giá trị ưu tiên và v1.1 phải được cập nhật trước khi tiếp tục sử dụng.
