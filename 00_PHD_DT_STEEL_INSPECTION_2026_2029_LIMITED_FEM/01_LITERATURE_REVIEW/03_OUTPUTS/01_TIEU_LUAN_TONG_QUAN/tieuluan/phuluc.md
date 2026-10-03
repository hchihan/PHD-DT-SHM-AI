# PHỤ LỤC

<!-- Bản rút gọn 02/10/2026: bỏ A.1 Cách đọc và A.3 Định nghĩa (trùng Giải thích thuật ngữ). -->

## Phụ lục A. Thực thể và thuộc tính của mô hình thông tin

Bảng A.1 liệt kê các thành phần của mô hình dữ liệu (Mục 4.6.1), phân thành ba loại: thực thể (năm), quan hệ có thuộc tính riêng (hai) và bản ghi sự kiện (một). Cột "Bắt buộc" cho biết trường phải có giá trị khi tạo bản ghi; mức đủ các trường này được đo bằng chỉ số M1.

<span id="TLTQ_Bang_A_1" class="anchor"></span>Bảng A.1. Thực thể, định danh và thuộc tính

| Thành phần | Loại | Trường | Bắt buộc | Mô tả |
|------|----|--------|:----:|------------|
| `COMPONENT` (cấu kiện) | Thực thể | `BIM_GUID`, `model_version` | Có | Định danh cấu kiện (GlobalId) và phiên bản mô hình BIM |
| `SENSOR` (cảm biến) | Thực thể | `Sensor_ID` | Có | Định danh nguồn đo |
| `SENSOR_MAPPING` (ánh xạ cảm biến – cấu kiện) | Quan hệ có thuộc tính | `Sensor_ID`, `BIM_GUID`, `valid_from`, `valid_to`, `install_record_ref` | Có (`valid_to` rỗng khi còn hiệu lực) | Cảm biến nào gắn cấu kiện nào, trong khoảng thời gian nào, theo hồ sơ lắp đặt nào |
| `EVIDENCE` (bằng chứng trạng thái) | Thực thể | `Condition_Evidence_ID`, `evidence_type`, `BIM_GUID` (một hoặc nhiều), `value`, `uncertainty`, `method_version`, `created_at` | Có | Loại (cảm biến, quan sát, NDT), giá trị, độ bất định, phiên bản phương pháp (git commit), thời điểm tạo; `BIM_GUID` chỉ khu vực cấu kiện mà nguồn đo giám sát, không phải vị trí hư hỏng |
| | | `scope.inference_unit`, `scope.data_split`, `scope.install_batch`, `scope.applicable_conditions` | Có | Phạm vi hiệu lực, tức điều kiện đã đánh giá và giới hạn sử dụng: đơn vị suy luận, cách chia dữ liệu, đợt lắp đặt, điều kiện áp dụng |
| | | `Sensor_ID`, `obs_context` | Có với loại cảm biến | Nguồn đo; bối cảnh quan trắc (khoảng thời gian đo, cấu hình cảm biến, nhiệt độ, trạng thái cầu trục) |
| | | `revision_of` | Không | Bản ghi cũ mà bản ghi này thay thế |
| `INSPECTION_RECORD` (bản ghi kiểm tra) | Thực thể | `Inspection_Record_ID`, `BIM_GUID`, `inspector_ref`, `inspector_role`, `inspected_at`, `finding`, `finding_uncertainty` | Có | Kết quả kiểm tra của kỹ sư, gồm vị trí và nguyên nhân hư hỏng nếu có; mã chủ thể và vai trò người kiểm tra, thời điểm, độ bất định; là nhãn hiện trường |
| `EVIDENCE_USE` (sử dụng bằng chứng) | Quan hệ có thuộc tính | `Inspection_Record_ID`, `Condition_Evidence_ID`, `used_at`, `within_scope`, `justification` | Có (`justification` khi `within_scope` sai) | Một lần bản ghi kiểm tra dùng một bằng chứng: thời điểm dùng, bằng chứng có nằm trong phạm vi hiệu lực tại thời điểm dùng hay không, lý do khi dùng ngoài phạm vi |
| `ACTION` (hành động) | Thực thể | `Action_ID`, `Inspection_Record_ID`, `priority_level` | Có | Hành động phát sinh từ bản ghi kiểm tra; mức ưu tiên bốn mức |
| | | `Action_Status` | Suy ra | Trạng thái xử lý, suy ra từ sự kiện chuyển trạng thái mới nhất |
| `STATUS_EVENT` (sự kiện chuyển trạng thái) | Bản ghi sự kiện | `Status_Event_ID`, `Action_ID`, `from_to`, `timestamp`, `actor_ref`, `actor_role`, `reason` | Có | Một lần đổi trạng thái: trước và sau, thời điểm, mã chủ thể và vai trò người thực hiện, lý do; với hành động can thiệp, `timestamp` của bước Đang xử lý → Hoàn thành là thời điểm can thiệp |
| | | `evidence_ref` | Có với bước chuyển cần căn cứ | Bản ghi sử dụng bằng chứng đã dùng làm căn cứ |

Bảng A.2 nêu các bước chuyển trạng thái được phép; tên vai trò theo tổ chức của chủ đầu tư được điền khi khóa đặc tả của Mục tiêu 2. Mã chủ thể (`inspector_ref`, `actor_ref`) là mã người hoặc tổ chức theo danh mục của chủ đầu tư; luận án không thiết kế hệ thống tài khoản. Bước đề nghị kiểm tra, từ bằng chứng và mức ưu tiên tới quyết định mở một lần kiểm tra, sẽ được đặc tả trong giai đoạn triển khai Mục tiêu 2 và phải truy được về bằng chứng, chủ thể và vai trò (Mục 4.6.1).

<span id="TLTQ_Bang_A_2" class="anchor"></span>Bảng A.2. Bước chuyển trạng thái xử lý được phép

| Bước chuyển | Vai trò được phép | Căn cứ bắt buộc |
|---|---|---|
| (tạo) → Mở | Kỹ sư kiểm tra | Bản ghi kiểm tra |
| Mở → Đang xử lý | Người phê duyệt | Bản ghi sử dụng bằng chứng của bản ghi kiểm tra |
| Đang xử lý → Hoàn thành | Người thực hiện | Lý do; tham chiếu công việc đã làm |
| Hoàn thành → Đã xác minh | Kỹ sư kiểm tra | Bản ghi kiểm tra sau sửa chữa |
| Hoàn thành → Mở | Kỹ sư kiểm tra | Bản ghi kiểm tra sau sửa chữa cho thấy chưa đạt |

Bảng A.3 đối chiếu khái niệm của mô hình với các chuẩn; lớp dữ liệu được lưu bằng SQLite và ánh xạ sang IFC 4.3, BCF 3.0 khi xuất, không sửa lược đồ chuẩn và không triển khai RDF. Bảng là phương án biểu diễn; việc giữ khóa và liên kết khi xuất – nhập được kiểm như nêu ở Mục 4.6.4.

<span id="TLTQ_Bang_A_3" class="anchor"></span>Bảng A.3. Ánh xạ khái niệm sang IFC 4.3, BCF 3.0, SSN và PROV-O

| Khái niệm của luận án | IFC 4.3 / BCF 3.0 | SSN, PROV-O |
|---|---|---|
| Ánh xạ cảm biến – cấu kiện có khoảng hiệu lực | Không có trường thời hạn; gán bằng `IfcRelAssignsToProduct` \[2\] | `ssn:Deployment` \[@GHAZGWUN\], thời gian bằng `prov:startedAtTime`, `prov:endedAtTime` \[69\] |
| Bản ghi kiểm tra → bằng chứng | `IfcTask` loại INSPECTION, `IfcRelAssignsToProduct` \[35\] | `prov:wasGeneratedBy`, `prov:used` \[69\] |
| Bằng chứng → cấu kiện | `IfcRelAdheresToElement`, mỗi cấu kiện một quan hệ \[35\] | `sosa:hasFeatureOfInterest` \[@GHAZGWUN\] |
| Bằng chứng → hành động | `IfcRelAssignsToProcess` \[35\] | `prov:used` \[69\] |
| Bản ghi mới thay bản cũ | Không có (trạng thái ghi đè trong \[35\]) | `prov:wasRevisionOf` \[69\] |
| Trạng thái và sự kiện của hành động | Trạng thái và sự kiện của vấn đề BCF \[@K5SGFIGW\], \[@P3ZIHF8G\] | `prov:Activity`, `prov:wasAssociatedWith` \[69\] |

## Phụ lục B. Năm ràng buộc kiểm bằng máy

Mỗi ràng buộc được kiểm bằng một truy vấn của công cụ viết bằng Python trên cơ sở dữ liệu SQLite; số hiệu giữ theo bộ ràng buộc đầy đủ ban đầu (C1–C9). Bảng B.1 phát biểu từng ràng buộc.

<span id="TLTQ_Bang_B_1" class="anchor"></span>Bảng B.1. Năm ràng buộc

| Mã | Tên | Phát biểu |
|:--:|---|---|
| C1 | Không mồ côi | Mỗi bằng chứng gắn ít nhất một cấu kiện; mỗi ánh xạ trỏ tới cảm biến và cấu kiện tồn tại; mỗi bản ghi kiểm tra gắn một cấu kiện; mỗi hành động gắn một bản ghi kiểm tra; mỗi sự kiện gắn đúng một hành động |
| C3 | Thời điểm đo nằm trong hiệu lực ánh xạ | Với mỗi bằng chứng loại cảm biến, tồn tại một ánh xạ cùng cảm biến và cấu kiện sao cho khoảng thời gian đo nằm trong [`valid_from`, `valid_to`) |
| C5 | Dùng ngoài phạm vi phải có lý do | Mỗi bản ghi sử dụng bằng chứng có `within_scope` sai phải có `justification`; `within_scope` đúng khi đợt lắp đặt và điều kiện vận hành tại thời điểm dùng nằm trong phạm vi hiệu lực |
| C6 | Bước chuyển có căn cứ và đúng vai trò | Mỗi sự kiện có `from_to` thuộc Bảng A.2, mã chủ thể, vai trò được phép và `evidence_ref` khi bảng yêu cầu |
| C9 | Căn cứ còn hiệu lực tại thời điểm chuyển | Bằng chứng được sự kiện trỏ tới chưa bị một bản ghi khác thay thế trước thời điểm của sự kiện |

Đợt lắp đặt hiện hành của cấu kiện được đánh dấu cần rà soát kể từ thời điểm can thiệp, ghi ở sự kiện Đang xử lý → Hoàn thành của hành động can thiệp; từ thời điểm đó, bằng chứng của đợt trước được tính là ngoài phạm vi khi xét C5, và sự kiện Hoàn thành → Đã xác minh xác nhận đợt lắp đặt mới. Lý do ghi theo C5 chỉ làm ngoại lệ truy ngược được, không xác nhận giá trị kỹ thuật của bằng chứng. Kiểm ràng buộc tự động đã có tiền lệ trong quản lý tiến độ 4D: \[21\] kiểm mỗi cấu kiện liên kết với ít nhất một công việc và kiểm các công việc gắn cùng cấu kiện không chồng lấn thời gian (tr. 17–18), là kỹ thuật tương tự C1, C3 và C9. Khuôn "bước chuyển có căn cứ và đúng thẩm quyền" của C6 có tiền lệ ở \[44\]. Bảng B.2 nối mỗi nhóm lỗi chèn mù với ràng buộc phát hiện và với khả năng của hai đối chứng. Cột B1 là phân tích dự kiến, được rà lại khi khóa đặc tả B1 (Mục 4.6.3); tỉ lệ phát hiện thực tế là kết quả đo của Mục tiêu 2. Bộ thử có cả bản ghi hợp lệ không chèn lỗi để đo việc báo lỗi nhầm.

<span id="TLTQ_Bang_B_2" class="anchor"></span>Bảng B.2. Nhóm lỗi dùng cho chỉ số M2

| Nhóm lỗi | Ràng buộc | B0 có trường để kiểm | Khả năng của B1 (phân tích dự kiến) |
|----------|:---:|:---:|------------|
| Bản ghi mồ côi, tham chiếu sai | C1 | Một phần | Có |
| Bằng chứng gán cho cảm biến đã dời hoặc ánh xạ đã hết hạn | C3 | Không | Một phần: có gán cảm biến – cấu kiện \[2\], chưa có khoảng hiệu lực của ánh xạ (Bảng A.3) |
| Dùng bằng chứng ngoài phạm vi hiệu lực mà không có lý do | C5 | Không | Chưa có trường phạm vi hiệu lực của bằng chứng |
| Đổi trạng thái không có căn cứ hoặc sai vai trò | C6 | Một phần | Một phần: trạng thái, sự kiện của BCF 3.0 và phê duyệt của IFC4 |
| Chuyển trạng thái dựa trên bằng chứng đã bị thay thế | C9 | Không | Một phần: lịch sử sửa đổi và quy ước `OUTDATED` \[35\]; chưa có quan hệ từ sự kiện tới bằng chứng |
