# ĐỀ CƯƠNG CHI TIẾT — CHUYÊN ĐỀ TỔNG QUAN
**Phiên bản:** v1 | **Ngày:** 18/07/2026 | **Kiến trúc:** Limited-FEM

**Tên chuyên đề:** Tổng quan về khung Digital Twin dựa trên dữ liệu phục vụ giám sát trạng thái và hỗ trợ kiểm tra – bảo trì nhà công nghiệp khung thép

---

## Chương 1. Mở đầu

### 1.1 Bối cảnh quản lý nhà công nghiệp khung thép
- **Mục đích:** Trình bày vai trò của nhà công nghiệp khung thép trong sản xuất; thực trạng quản lý trạng thái, kiểm tra và bảo trì.
- **Claim chính:** Dữ liệu đo, hồ sơ BIM và biên bản kiểm tra vẫn được quản lý tách rời, làm giảm khả năng truy xuất và giải trình.
- **Evidence cần dùng:** Thực trạng quản lý tài sản công trình tại Việt Nam; khung pháp lý (Nghị định, Thông tư); tiêu chuẩn ISO 19650, TCVN 14177:2024.
- **Còn thiếu:** Số liệu thống kê cụ thể về tình trạng quản lý nhà công nghiệp tại Việt Nam.

### 1.2 Nhu cầu condition-informed inspection
- **Mục đích:** Giải thích vì sao kiểm tra định kỳ thuần túy không đủ; cần bổ sung thông tin trạng thái.
- **Claim chính:** Kiểm tra theo lịch cố định thiếu cơ sở ưu tiên dựa trên bằng chứng trạng thái thực tế.
- **Evidence cần dùng:** Literature về condition-based maintenance vs time-based maintenance.

### 1.3 Vai trò của vibration data, BIM và Digital Twin
- **Mục đích:** Giới thiệu ba thành phần kỹ thuật chính và cách chúng hỗ trợ quản lý.
- **Claim chính:** Ba thành phần đã được phát triển riêng lẻ nhưng chưa được tích hợp thành chuỗi truy xuất thống nhất.

### 1.4 Mục tiêu, câu hỏi tổng quan, phạm vi và phương pháp
- **Mục đích:** Khai báo rõ ràng 7 CH, phạm vi Core/Supporting/Out of Scope, và phương pháp structured review.

---

## Chương 2. Cơ sở khái niệm về Digital Twin trong quản lý tài sản công trình

### 2.1 Phân biệt BIM, Digital Model, Digital Shadow và Digital Twin
- **Mục đích:** Làm rõ các khái niệm thường bị dùng lẫn trong literature.
- **Claim chính:** Digital Twin khác Digital Model và Digital Shadow ở mức độ liên kết dữ liệu hai chiều giữa tài sản vật lý và biểu diễn số.
- **Evidence cần dùng:** Kritzinger et al. (2018); Fuller et al. (2020); Boje et al. (2020).
- **Còn thiếu:** Cần xác minh thêm nguồn cho phân loại mức trưởng thành DT trong construction.

### 2.2 Mức tự động hóa và Digital Twin maturity
- **Mục đích:** Chứng minh DT không nhất thiết phải tự động hoàn toàn mới có giá trị quản lý.
- **Claim chính:** Mức tự động hóa cần phù hợp với bối cảnh tổ chức, nguồn lực và loại hình tài sản.
- **Evidence cần dùng:** Literature về DT maturity levels trong AEC.
- **Còn thiếu:** Nguồn cụ thể cho DT maturity trong industrial buildings — đã ghi nhận trong UNRESOLVED_ITEMS.

### 2.3 Định nghĩa evidence-centred, inspection-oriented Digital Twin
- **Mục đích:** Đề xuất và bảo vệ định nghĩa làm việc phù hợp với luận án.
- **Claim chính:** Digital Twin trong luận án này là biểu diễn số hướng bằng chứng và kiểm tra, liên kết dữ liệu dao động → condition evidence → BIM component → inspection record → action support.
- **Evidence cần dùng:** Tổng hợp từ các nguồn DT + asset management + inspection.

### 2.4 Các lớp của khung Digital Twin đề xuất
- **Mục đích:** Trình bày 7 lớp: physical asset, sensing/data, condition evidence, BIM/asset context, inspection records, action support, human review.
- **Liên hệ:** Nền tảng cho CH1; liên kết với toàn bộ kiến trúc luận án.

---

## Chương 3. Dữ liệu dao động, bằng chứng trạng thái và độ tin cậy

### 3.1 Vibration-based condition monitoring cho khung thép và liên kết bu lông
- **Mục đích:** Tổng hợp các phương pháp monitoring dựa trên dao động.
- **Claim chính:** Dữ liệu dao động có thể hỗ trợ nhận diện sự khác biệt giữa các trạng thái liên kết trong điều kiện phòng thí nghiệm có kiểm soát.
- **Evidence cần dùng:** Avci et al. (2021); Zhang/Biswal/Wang (2020); Eraliev et al. (2022); Ramasso et al. (2024).

### 3.2 Controlled connection states và labelled lab data
- **Mục đích:** Mô tả cách tạo dữ liệu có nhãn trong phòng thí nghiệm.
- **Claim chính:** Dữ liệu lab có kiểm soát là cơ sở để đánh giá khả năng phân biệt trạng thái; không suy rộng thành kết luận hư hỏng hiện trường.

### 3.3 Phân biệt classification, anomaly evidence và damage diagnosis
- **Mục đích:** Ranh giới quan trọng nhất trong luận án.
- **Claim chính:** Classification trong lab chỉ là bằng chứng phân biệt trạng thái; anomaly evidence trong field chỉ là dấu hiệu cần kiểm tra; không phải damage diagnosis.
- **Limitation:** Ranh giới này chưa được làm rõ nhất quán trong literature hiện có.

### 3.4 Run-aware evaluation và kiểm soát rò rỉ dữ liệu
- **Mục đích:** Trọng tâm kỹ thuật lớn nhất của RQ1/Paper 1.
- **Claim chính:** Nhiều nghiên cứu phân loại trạng thái không tách biệt run khi chia tập dữ liệu, dẫn đến kết quả lạc quan quá mức.
- **Evidence cần dùng:** Literature về data leakage trong SHM/time-series classification; LORO methodology.
- **Còn thiếu:** Cần thêm nguồn chứng minh leakage là vấn đề phổ biến trong SHM vibration studies.

### 3.5 Sensor configuration vs model choice
- **Mục đích:** Đánh giá vai trò của cấu hình cảm biến.
- **Claim chính:** Cấu hình cảm biến có thể ảnh hưởng đến kết quả phân loại mạnh hơn lựa chọn kiến trúc mô hình AI.
- **Evidence cần dùng:** Evidence từ kết quả lab của luận án (Gate 1); literature về sensor placement trong vibration SHM.

### 3.6 Small-n uncertainty và reproducibility
- **Mục đích:** Trình bày hạn chế khi số lượng run nhỏ.
- **Claim chính:** Với ít run, khoảng tin cậy rộng; cần group-preserving permutation và báo cáo uncertainty.
- **Liên hệ:** CH2, CH3 → RQ1 → Paper 1 → Gate 1.

---

## Chương 4. Liên kết bằng chứng với BIM, hồ sơ kiểm tra và dữ liệu hiện trường

### 4.1 Chuỗi định danh Sensor_ID → BIM_GUID
- **Mục đích:** Tổng hợp cách liên kết vật lý cảm biến với cấu kiện số.
- **Claim chính:** Liên kết sensor-BIM đã được nghiên cứu nhưng thường dừng ở mapping, chưa kéo dài đến inspection record.
- **Evidence cần dùng:** Rio et al. (2013); Theiler & Smarsly (2018); Valinejadshoubi et al. (2019).

### 4.2 Condition_Evidence_ID và Inspection_Record_ID
- **Mục đích:** Mở rộng liên kết từ kết quả phân loại đến hồ sơ kiểm tra.
- **Claim chính:** Lớp Condition_Evidence_ID và Inspection_Record_ID chưa được hình thức hóa rõ trong literature.
- **Còn thiếu:** Cần thêm evidence về inspection record management trong asset management/facility management.

### 4.3 Provenance, traceability và bidirectional queries
- **Mục đích:** Yêu cầu truy xuất hai chiều: từ cảnh báo đến cấu kiện, và từ cấu kiện đến lịch sử cảnh báo.
- **Evidence cần dùng:** Literature về data provenance trong BIM/IoT; competency questions methodology.
- **Còn thiếu:** Nguồn cho competency questions methodology trong construction DT — đã ghi nhận.

### 4.4 Constraint testing và invalid-data tests
- **Mục đích:** Framework truy vết cần được kiểm chứng bằng các trường hợp sai để chứng minh khả năng phát hiện lỗi.
- **Liên hệ:** CH4 → RQ2 → Paper 2 → Gates 2–3.

### 4.5 Sensor qualification cho dữ liệu hiện trường
- **Mục đích:** Đánh giá khả năng hoạt động của cảm biến giá rẻ tại hiện trường.
- **Claim chính:** Cảm biến cần được xác nhận khả năng thu thập dữ liệu có chất lượng tối thiểu trước khi dùng cho monitoring.

### 4.6 Operational baseline và anomaly evidence
- **Mục đích:** Trong điều kiện không nhãn, xây dựng baseline vận hành và phát hiện sai lệch.
- **Claim chính:** Anomaly evidence tại hiện trường chỉ là dấu hiệu cần kiểm tra, không phải kết luận hư hỏng.
- **Limitation:** Không chuyển classifier lab sang field; không suy diễn damage diagnosis.

### 4.7 Environmental/operational variability và missing data
- **Mục đích:** Các thách thức thực tế khi triển khai monitoring tại công trình thực.
- **Liên hệ:** CH5 → RQ3 → Paper 3 → Gate 4.

---

## Chương 5. Hỗ trợ quyết định kiểm tra – bảo trì và vai trò của FEM

### 5.1 Human-in-the-loop và transparency
- **Mục đích:** Vai trò không thể thay thế của con người trong quyết định kiểm tra.
- **Claim chính:** Hệ thống hỗ trợ quyết định cần minh bạch về căn cứ, không tự động thay thế chuyên gia.

### 5.2 Evidence-to-action linkage và bốn mức hành động
- **Mục đích:** Trình bày logic Normal → Watch → Inspect → Priority Inspection.
- **Claim chính:** Bốn mức hành động đơn giản, dựa trên bằng chứng có truy xuất, có thể kiểm chứng qua kịch bản.
- **Limitation:** Không dùng weighted Health Index phức tạp; không autonomous maintenance.

### 5.3 Action-status history và scenario-based validation
- **Mục đích:** Lưu trữ lịch sử hành động và kiểm chứng bằng kịch bản.
- **Liên hệ:** CH6 → WP4-support → Paper 4 (optional) → Gate 5.

### 5.4 Vai trò và giới hạn của FEM trong luận án
- **Mục đích:** Giải thích rõ ràng vì sao FEM chỉ là nominal, uncalibrated, reference-only.
- **Claim chính:** FEM danh nghĩa có thể hỗ trợ mô tả hình học, vị trí cảm biến và giả thuyết định tính, nhưng không dùng cho chẩn đoán, suy giảm độ cứng hoặc transfer định lượng.
- **Claim phụ:** Limited-FEM không làm giảm chất lượng luận án Quản lý xây dựng vì đóng góp chính nằm ở quy trình quản lý thông tin và hỗ trợ quyết định, không ở mô hình cơ học.
- **Evidence cần dùng:** Literature về vai trò FEM trong SHM; lập luận từ Research Direction and Scope.

---

## Chương 6. Tổng hợp khoảng trống và kiến trúc nghiên cứu đề xuất

### 6.1 Bảng tổng hợp khoảng trống nghiên cứu
- **Mục đích:** Tạo bảng: Lớp nghiên cứu | Đã có | Chưa có | Khoảng trống luận án xử lý.
- **8 khoảng trống trọng tâm** theo prompt đã xác định.
- **Lưu ý:** Dùng "Trong phạm vi tập bằng chứng đã rà soát..." thay vì "no study exists."

### 6.2 Kiến trúc nghiên cứu đề xuất
- **Mục đích:** Trình bày RQ → Paper → Gate mapping.
- **Sơ đồ logic:**
  ```
  Paper 1: tạo bằng chứng đáng tin (RQ1 → Gate 1)
  → Paper 2: truy vết và quản lý bằng chứng (RQ2 → Gates 2–3)
  → Paper 3: kiểm chứng khả thi hiện trường (RQ3 → Gate 4)
  → Paper 4: hỗ trợ quyết định có con người kiểm soát (WP4 → Gate 5)
  ```
- **Liên hệ:** CH7 → kiến trúc nghiên cứu toàn bộ luận án.

---

## Chương 7. Kết luận và kiến nghị

### 7.1 Tổng hợp trả lời bảy câu hỏi tổng quan
### 7.2 Tóm tắt khoảng trống nghiên cứu
### 7.3 Giới hạn của tiểu luận tổng quan
### 7.4 Ý nghĩa đối với luận án
### 7.5 Hành động nghiên cứu kế tiếp
- Ưu tiên đóng Gate 1: run registry → LORO → xác nhận ResNet1D sensor mode.

---

## Phụ lục

### Phụ lục A. Ma trận bằng chứng (Evidence Matrix)
### Phụ lục B. Bảng tổng hợp khoảng trống theo lớp nghiên cứu
### Phụ lục C. Danh mục tài liệu tham khảo đầy đủ với trạng thái toàn văn

---

*Ghi chú: Đề cương này phục vụ mục đích xây dựng báo cáo Tiểu luận tổng quan. Các claim chính và evidence sẽ được kiểm chứng lại trong quá trình viết báo cáo hoàn chỉnh.*
