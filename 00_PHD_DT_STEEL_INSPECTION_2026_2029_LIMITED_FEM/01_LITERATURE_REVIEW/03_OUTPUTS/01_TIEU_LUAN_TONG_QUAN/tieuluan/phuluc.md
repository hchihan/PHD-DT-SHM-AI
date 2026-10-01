# PHỤ LỤC

## Phụ lục A. Định danh, thực thể và thuộc tính của mô hình thông tin

### A.1. Cách đọc

Hình 5.1 trình bày chuỗi định danh *Sensor_ID → BIM_GUID → Condition_Evidence_ID → Inspection_Record_ID → Action_Status* cho người đọc. Mô hình dữ liệu dùng để lưu và kiểm là một đồ thị gồm sáu thực thể (Bảng A.1). Cột "Bắt buộc" cho biết trường phải có giá trị khi tạo bản ghi; mức đủ các trường bắt buộc được đo bằng chỉ số M1 (Mục 5.5). Tên trường giữ dạng tiếng Anh để thống nhất với công cụ kiểm ràng buộc; nghĩa tiếng Việt ghi ở cột Mô tả. Thang kiểm chứng V1–V4 được trình bày ở Bảng 5.3.

### A.2. Sáu thực thể

<span id="TLTQ_Bang_A_1" class="anchor"></span>Bảng A.1. Thực thể, định danh và thuộc tính

| Thực thể | Trường | Bắt buộc | Mô tả |
|---|---|:--:|---|
| `COMPONENT` (cấu kiện) | `BIM_GUID` | Có | Định danh cấu kiện trong mô hình IFC (GlobalId) |
| | `model_version` | Có | Phiên bản mô hình BIM chứa cấu kiện |
| `SENSOR` (cảm biến) | `Sensor_ID` | Có | Định danh nguồn đo |
| `SENSOR_MAPPING` (ánh xạ cảm biến – cấu kiện, thuộc thực thể cảm biến) | `Sensor_ID`, `BIM_GUID` | Có | Cảm biến nào gắn cấu kiện nào |
| | `valid_from`, `valid_to` | Có (`valid_to` rỗng khi còn hiệu lực) | Khoảng hiệu lực của ánh xạ |
| | `install_record_ref` | Có | Tham chiếu hồ sơ lắp đặt, dời hoặc thay cảm biến |
| `EVIDENCE` (bằng chứng trạng thái) | `Condition_Evidence_ID` | Có | Định danh bản ghi bằng chứng |
| | `evidence_type` | Có | Cảm biến, quan sát hoặc kiểm tra không phá hủy (NDT) |
| | `BIM_GUID` (một hoặc nhiều) | Có | Cấu kiện mà bằng chứng nói tới; quan hệ nhiều – nhiều |
| | `Sensor_ID` | Có với loại cảm biến | Nguồn đo |
| | `value` | Có | Trường giá trị |
| | `uncertainty` | Có | Trường độ bất định |
| | `method_version` | Có | Phiên bản phương pháp (mã git commit của chuỗi xử lý) |
| | `scope.inference_unit`, `scope.data_split`, `scope.install_batch`, `scope.applicable_conditions` | Có | Trường phạm vi hiệu lực |
| | `obs_context` | Có với loại cảm biến | Bối cảnh quan trắc: đợt đo, khoảng thời gian đo, cấu hình cảm biến, nhiệt độ, trạng thái cầu trục |
| | `created_at` | Có | Thời điểm tạo bản ghi |
| | `revision_of` | Không | Bản ghi cũ mà bản ghi này thay thế |
| `INSPECTION_RECORD` (bản ghi kiểm tra) | `Inspection_Record_ID` | Có | Định danh bản ghi kiểm tra |
| | `BIM_GUID` | Có | Cấu kiện được kiểm tra |
| | `inspector_role`, `inspected_at` | Có | Vai trò người kiểm tra, thời điểm kiểm tra |
| | `finding`, `finding_uncertainty` | Có | Kết quả kiểm tra và độ bất định của kiểm tra |
| `ACTION` (hành động) | `Action_ID` | Có | Định danh hành động kiểm tra hoặc bảo trì |
| | `Inspection_Record_ID` | Có | Bản ghi kiểm tra làm phát sinh hành động |
| | `priority_level` | Có | Mức ưu tiên: Bình thường → Theo dõi → Kiểm tra → Kiểm tra ưu tiên |
| | `Action_Status` | Suy ra | Trạng thái xử lý hiện thời, suy ra từ sự kiện chuyển trạng thái mới nhất |
| `STATUS_EVENT` (sự kiện chuyển trạng thái) | `Status_Event_ID` | Có | Định danh sự kiện |
| | `Action_ID` | Có | Hành động được đổi trạng thái |
| | `from_to` | Có | Trạng thái trước và sau |
| | `timestamp`, `actor_role` | Có | Thời điểm, vai trò người thực hiện |
| | `evidence_ref` | Có với bước chuyển cần căn cứ (Bảng A.3) | Bản ghi sử dụng bằng chứng đã dùng làm căn cứ |
| | `reason` | Có | Lý do chuyển |

Quan hệ có thuộc tính giữa bản ghi kiểm tra và bằng chứng là **bản ghi sử dụng bằng chứng** (`EVIDENCE_USE`), gồm `Inspection_Record_ID`, `Condition_Evidence_ID`, `used_at`, `within_scope` (bằng chứng có nằm trong phạm vi hiệu lực tại thời điểm dùng hay không) và `justification` (lý do khi dùng ngoài phạm vi).

### A.3. Định nghĩa thuật ngữ dùng ở Mục 5.6 và 5.7

**Bản ghi bằng chứng.** Một bản ghi `EVIDENCE`: nhận định về tình trạng của một hoặc nhiều cấu kiện, kèm nguồn tạo ra nó và phạm vi nó được phép dùng. Bản ghi không bị sửa đè; khi cần sửa, một bản ghi mới được tạo với `revision_of` trỏ về bản cũ.

**Trường giá trị** (`value`). Nhãn, xác suất lớp, sai số tái tạo hoặc kết quả quan sát, NDT mà bằng chứng mang.

**Trường độ bất định** (`uncertainty`). Biến thiên theo seed và fold, kết quả kiểm định hoán vị, hoặc sai số đo của phương pháp tạo ra giá trị.

**Trường phạm vi hiệu lực** (`scope`). Điều kiện mà trong đó bằng chứng còn đúng: đơn vị suy luận, cách chia dữ liệu khi đánh giá, đợt lắp đặt (lần lắp ráp hoặc lần can thiệp gần nhất lên liên kết) và điều kiện áp dụng.

**Trường điều kiện áp dụng** (`scope.applicable_conditions`). Dải điều kiện vận hành – môi trường có trong dữ liệu tạo ra bằng chứng, ở nhà xưởng gồm dải nhiệt độ và trạng thái cầu trục của đường cơ sở.

**Bối cảnh quan trắc** (`obs_context`). Điều kiện tại lần đo: đợt đo, khoảng thời gian đo, cấu hình cảm biến, nhiệt độ, trạng thái cầu trục.

**Bản ghi kiểm tra** (`INSPECTION_RECORD`). Kết quả kiểm tra của kỹ sư tại một cấu kiện, có vai trò người kiểm tra, thời điểm và độ bất định của kiểm tra; ở hiện trường, bản ghi này là nhãn hiện trường của cấu kiện (vòng lặp kiểm tra tạo nhãn).

**Bản ghi sử dụng bằng chứng** (`EVIDENCE_USE`). Quan hệ ghi việc một bản ghi kiểm tra dùng một bằng chứng, có cờ trong hay ngoài phạm vi hiệu lực và lý do khi ngoài phạm vi.

**Sự kiện chuyển trạng thái** (`STATUS_EVENT`). Một lần đổi trạng thái xử lý của hành động, ghi trạng thái trước và sau, thời điểm, vai trò người thực hiện, lý do và bản ghi sử dụng bằng chứng làm căn cứ.

**Đường cơ sở B0 và đối chứng B1.** B0 là hồ sơ kiểm định theo thực hành hiện hành, mã hóa tay 20–30 hồ sơ. B1 là mô hình chỉ dùng IFC 4.3 theo \[35\] và BCF 3.0, chưa có tầng bằng chứng và tầng trách nhiệm, dựng trên cùng BIM nhà xưởng.

**Ràng buộc về sử dụng bằng chứng ngoài phạm vi hiệu lực.** Ràng buộc C5 ở Phụ lục B.

### A.4. Trạng thái xử lý và bước chuyển được phép

<span id="TLTQ_Bang_A_3" class="anchor"></span>Bảng A.3. Bước chuyển trạng thái xử lý được phép (đề xuất, khóa trước khi đo)

| Bước chuyển | Vai trò được phép | Căn cứ bắt buộc |
|---|---|---|
| (tạo) → Mở | Kỹ sư kiểm tra | Bản ghi kiểm tra |
| Mở → Đang xử lý | Người phê duyệt | Bản ghi sử dụng bằng chứng của bản ghi kiểm tra |
| Đang xử lý → Hoàn thành | Người thực hiện | Lý do; tham chiếu công việc đã làm |
| Hoàn thành → Đã xác minh | Kỹ sư kiểm tra | Bản ghi kiểm tra sau sửa chữa |
| Hoàn thành → Mở | Kỹ sư kiểm tra | Bản ghi kiểm tra sau sửa chữa cho thấy chưa đạt |

Một bước chuyển không có trong bảng không có vai trò hợp lệ, nên vi phạm C6. Tên vai trò theo tổ chức của chủ đầu tư được điền khi khóa đặc tả Bài báo 2.

Mức ưu tiên do logic bốn mức bằng luật đề xuất; bộ luật (ngưỡng và điều kiện) được khóa trước khi đo và có phiên bản, để mỗi mức ưu tiên truy được về luật đã áp dụng.

### A.5. Ánh xạ khái niệm sang chuẩn

<span id="TLTQ_Bang_A_4" class="anchor"></span>Bảng A.4. Ánh xạ khái niệm của mô hình thông tin sang IFC 4.3, BCF 3.0, SOSA/SSN và PROV-O

| Khái niệm của luận án | IFC 4.3 / BCF 3.0 | SOSA/SSN, PROV-O |
|---|---|---|
| Cấu kiện | Lớp con của `IfcElement` \[35\] | `sosa:FeatureOfInterest` \[CẦN NGUỒN: Khuyến nghị W3C SSN\] |
| Ánh xạ cảm biến – cấu kiện có khoảng hiệu lực | Không có trường thời hạn; gán bằng `IfcRelAssignsToProduct` \[2\] | `ssn:Deployment` trên nền tảng \[CẦN NGUỒN: Khuyến nghị W3C SSN\], ghép thời gian bằng `prov:startedAtTime`, `prov:endedAtTime` \[69\] |
| Bản ghi kiểm tra → bằng chứng | `IfcTask` loại INSPECTION, `IfcRelAssignsToProduct` \[35\] | `prov:wasGeneratedBy` (bằng chứng quan sát sinh từ lần kiểm tra); `prov:used` (lần kiểm tra dùng bằng chứng cảm biến) \[69\] |
| Bằng chứng → cấu kiện | `IfcRelAdheresToElement`, mỗi cấu kiện một quan hệ \[35\] | `sosa:hasFeatureOfInterest` |
| Bằng chứng → hành động | `IfcRelAssignsToProcess` \[35\] | `prov:used` (hành động dùng bằng chứng) \[69\] |
| Phiên bản phương pháp | Không có | `prov:Plan` qua `prov:qualifiedAssociation` \[69\] |
| Bản ghi mới thay bản cũ | Không có (trạng thái ghi đè của \[35\]) | `prov:wasRevisionOf`, `prov:wasInvalidatedBy` \[69\] |
| Trạng thái và sự kiện của hành động | Trạng thái và sự kiện của vấn đề BCF \[@K5SGFIGW\] | `prov:Activity` có `prov:wasAssociatedWith` |

Bảng chỉ đối chiếu khái niệm; luận án lưu dữ liệu bằng SQLite và xuất IFC, không triển khai RDF.

## Phụ lục B. Năm ràng buộc kiểm bằng máy

### B.1. Phát biểu

Năm ràng buộc giữ số hiệu của bộ ràng buộc đầy đủ ban đầu (C1–C9) để truy được lịch sử thiết kế. Mỗi ràng buộc được kiểm bằng một truy vấn của công cụ viết bằng Python trên cơ sở dữ liệu SQLite; một bản ghi vi phạm được báo kèm định danh và lý do.

<span id="TLTQ_Bang_B_1" class="anchor"></span>Bảng B.1. Năm ràng buộc

| Mã | Tên | Phát biểu | Trường tham gia |
|:--:|---|---|---|
| C1 | Không mồ côi | Mỗi bằng chứng gắn ít nhất một cấu kiện; mỗi ánh xạ trỏ tới cảm biến và cấu kiện tồn tại; mỗi bản ghi kiểm tra gắn một cấu kiện; mỗi hành động gắn một bản ghi kiểm tra; mỗi sự kiện gắn đúng một hành động | Các khóa tham chiếu ở Bảng A.1 |
| C3 | Thời điểm đo nằm trong hiệu lực ánh xạ | Với mỗi bằng chứng loại cảm biến, tồn tại một ánh xạ cùng `Sensor_ID` và cùng `BIM_GUID` sao cho khoảng thời gian đo trong `obs_context` nằm trong [`valid_from`, `valid_to`) | `EVIDENCE.obs_context`, `SENSOR_MAPPING` |
| C5 | Dùng ngoài phạm vi phải có lý do | Với mỗi bản ghi sử dụng bằng chứng có `within_scope` sai, `justification` khác rỗng. `within_scope` do công cụ tính: đúng khi `scope.install_batch` trùng đợt lắp đặt hiện hành của cấu kiện tại `used_at` và điều kiện vận hành tại `used_at` nằm trong `scope.applicable_conditions` | `EVIDENCE.scope`, `EVIDENCE_USE` |
| C6 | Bước chuyển có căn cứ và đúng vai trò | Với mỗi sự kiện, `from_to` có trong Bảng A.3, `actor_role` thuộc vai trò được phép, và `evidence_ref` khác rỗng khi bảng yêu cầu căn cứ | `STATUS_EVENT`, Bảng A.3 |
| C9 | Căn cứ còn hiệu lực tại thời điểm chuyển | Với mỗi sự kiện có `evidence_ref`, bằng chứng được trỏ tới chưa bị một bản ghi khác thay thế (`revision_of`) trước `timestamp` của sự kiện | `STATUS_EVENT.evidence_ref`, `EVIDENCE.revision_of`, `EVIDENCE.created_at` |

Đợt lắp đặt hiện hành của cấu kiện đổi khi một hành động can thiệp lên liên kết (siết lại, thay thế) chuyển sang "Đã xác minh"; cách ghi cụ thể được khóa cùng đặc tả Bài báo 2. Các trường bắt buộc ở Bảng A.1 được bảo đảm bằng ràng buộc rỗng của cơ sở dữ liệu và đo bằng M1, không tính là ràng buộc riêng.

### B.2. Nhóm lỗi chèn mù và ràng buộc tương ứng

<span id="TLTQ_Bang_B_2" class="anchor"></span>Bảng B.2. Nhóm lỗi dùng cho chỉ số M2 và khả năng kiểm theo thiết kế

| Nhóm lỗi | Ràng buộc phát hiện | B0 có trường để kiểm | B1 có trường để kiểm |
|---|:--:|:--:|:--:|
| Bản ghi mồ côi, tham chiếu sai | C1 | Một phần | Có (quan hệ IFC) |
| Bằng chứng gán cho cảm biến đã dời hoặc ánh xạ đã hết hạn | C3 | Không | Không |
| Dùng bằng chứng ngoài phạm vi hiệu lực mà không có lý do | C5 | Không | Không |
| Đổi trạng thái không có căn cứ hoặc sai vai trò | C6 | Một phần | Một phần (BCF ghi người và loại thay đổi, không ghi căn cứ) |
| Chuyển trạng thái dựa trên bằng chứng đã bị thay thế | C9 | Không | Không |

Hai cột cuối mô tả trường mà mỗi đối chứng có theo thiết kế; tỉ lệ phát hiện thực tế là kết quả đo của Bài báo 2. Danh sách lỗi, người chèn lỗi và cách tính M2 được khóa trước khi đo (Mục 5.5).

### B.3. Tiền lệ và giới hạn

Kiểm ràng buộc tự động trên dữ liệu công trình đã có tiền lệ trong quản lý tiến độ 4D: \[21\] kiểm mỗi cấu kiện liên kết với ít nhất một công việc, là kỹ thuật tương tự C1, và kiểm các công việc gắn cùng một cấu kiện không chồng lấn thời gian bằng thời điểm bắt đầu và kết thúc, là kỹ thuật tương tự C3 và C9 (tr. 17–18). Khuôn "bước chuyển có căn cứ và đúng thẩm quyền" của C6 có tiền lệ ở quản trị gói thông tin bàn giao \[44\]. SSN mô tả triển khai cảm biến trên nền tảng \[CẦN NGUỒN: Khuyến nghị W3C SSN\]; C3 thêm khoảng hiệu lực bắt buộc và kiểm thời điểm đo theo khoảng đó.

Năm ràng buộc kiểm tính toàn vẹn của dữ liệu. Việc cảm biến có thực sự được lắp ở cấu kiện đã khai báo được kiểm bằng hồ sơ lắp đặt và đối chiếu tại hiện trường trong Mục tiêu 3 (Mục 5.6.2).
