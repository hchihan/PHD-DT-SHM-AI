# Nhật ký ứng viên khoảng trống — Giai đoạn 2

Tạo ngày 30/09/2026 (phiên T1-3). Đây là nhật ký **làm việc**; khoảng trống chỉ được chốt ở Giai đoạn 3 (Điểm duyệt 3).
Mọi ứng viên là giả thuyết, chưa phải kết luận.

Quy ước:
- **K1** = xác lập chất lượng và phạm vi hiệu lực của bằng chứng trạng thái; **K2** = bảo toàn chất lượng bằng chứng
  trong truy vết cấp cấu kiện; **K3** = từ bằng chứng đến hành động (theo mục 5.2 của bản gốc). Đây là các giả thuyết
  làm việc.
- Căn cứ được đếm là **độc lập** khi thuộc các nhóm tác giả khác nhau và đã được đọc toàn văn hoặc đúng phần liên quan.
  Ngưỡng của Giai đoạn 3: mỗi khoảng trống cần từ 3 căn cứ, trong đó không thuộc nhóm 2025–2026 (CLAUDE.md 4.1).
- Loại căn cứ: **TG** = tác giả tự nêu; **NCS** = nhận định của NCS từ việc bài không xử lý một ý; ghi rõ khi lẫn.
- **Phản chứng đã kiểm** (quy tắc thêm ngày 30/09/2026, CLAUDE.md mục 7.4): nguồn, chuẩn hoặc hệ thống có thể đã giải quyết vấn đề
  (ví dụ CMMS, BCF 3.0, IFC Monitor [2], ISO 19650); ghi kết quả đối chiếu kèm trang, hoặc "chưa kiểm".
- **Phát biểu đã thu hẹp:** phát biểu sau khi trừ phần đã được giải quyết.
- Một ứng viên chỉ được đưa vào GĐ3 khi trường "Phản chứng đã kiểm" không còn mục nào ghi "chưa kiểm".
- Nguồn đã đọc toàn văn đến hết phiên T1-3: [8], [7], [3] (30/09/2026). Đọc thêm để kiểm phản chứng (30/09/2026): BCF 3.0 (phần mô hình vấn đề và sự kiện) và [2] (thân bài; chưa lập ghi chú đọc sâu và bảng ánh xạ, thuộc phiên T1-1). Phiên T1-1 (ba tiền lệ [2], [35], [44]) **chưa
  thực hiện**; căn cứ từ ba bài đó sẽ được bổ sung khi có. Căn cứ đã dùng ở 5.6A (Bull 2022, Wang & Cha 2021, [57],
  Hughes 2022, Figueiredo 2011) chưa được đưa vào nhật ký; cần rà lại ở phiên Tier 2.

## Bảng tóm tắt

| Mã | Phát biểu | K | Số căn cứ độc lập hiện có | Năm các căn cứ | Ghi chú |
|---|---|---|---|---|---|
| UV-01 | Chuỗi từ cảnh báo đến hành động không được ghi thành trạng thái xử lý có truy vết trong các khung song sinh số cho công trình | K3 | 2 ([3], [7]) | 2020, 2020 | Chưa đủ; cần [35], [44], [16], [17] |
| UV-02 | Đầu ra phát hiện bất thường trong khung song sinh cho công trình chưa được ghi cùng nguồn gốc xử lý, phiên bản phương pháp và phạm vi hiệu lực | K1 | 2 ([3], [7]) | 2020, 2020 | Chưa đủ; cần [18], [45], 23TBQTIP |
| UV-03 | Gắn dữ liệu cảm biến với đối tượng BIM chưa kèm thời hạn hiệu lực và lịch sử thay đổi ghép | K2 | 3 ([3], [7], [2]) | 2020, 2020, 2018 | Đủ 3 căn cứ trước 2025; phản chứng còn chờ đặc tả IFC, SOSA/SSN; cần [35] |
| UV-04 | Thiếu phân loại mức tích hợp DM/DS/DT áp cho kiểm tra – bảo trì kết cấu công trình có con người ra quyết định | mới (định vị) | 2 ([8], [7]) | 2018, 2020 | Chỉ phục vụ định vị ở 2.3, không dự kiến thành khoảng trống |
| UV-05 | Ở công trình đang vận hành thiếu dữ liệu có nhãn về bất thường; nhãn phụ thuộc đánh giá con người | mới (nhãn hiện trường; liên quan L2.3, 5.6A) | 1 ([3]) | 2020 | Căn cứ đã có ở 5.6A chưa nhập nhật ký |

Tình trạng phản chứng (30/09/2026, sau khi kiểm BCF 3.0 và [2]): UV-01 còn chờ CMMS và ISO 19650; UV-03 còn chờ đặc tả IFC và SOSA/SSN; UV-02, UV-04, UV-05 chưa kiểm. Chưa ứng viên nào đủ điều kiện vào GĐ3.

## UV-01 — Chuỗi cảnh báo → hành động

- **Phát biểu:** Trong các khung song sinh số đã đọc, chuỗi từ phát hiện bất thường đến hành động bảo trì dừng ở cảnh
  báo và hỗ trợ quyết định của con người, không được ghi thành trạng thái xử lý và lịch sử chuyển trạng thái có thể
  truy ngược.
- **Căn cứ:**
  - Lu và cs. 2020 [3], tr. 6 (Hình 4: kết thúc ở báo cáo – sửa chữa), tr. 13–14 (mục đích là hỗ trợ quyết định; Hình 18
    chỉ hiển thị cảnh báo), tr. 5–6 (chỉ ra IFC4 thiếu giá trị `IfcChangeActionEnum` cho FM và đề xuất
    `IfcInspectionHistory`, `IfcMaintenanceHistory`, nhưng ca nghiên cứu không dùng chúng).
  - Boje và cs. 2020 [7], tr. 12 (cảnh báo và khuyến nghị "cần người dùng xác nhận và cho phép"; không nêu mô hình ghi lại
    xác nhận), tr. 10 (Bảng 2: "chấp hành" là một khả năng, không có trạng thái hành động).
- **Loại căn cứ:** TG một phần ([3] tr. 5 tự nêu IFC4 thiếu thực thể; [7] tr. 12 tự nêu cần kiểm chứng AI trước khi
  chuyển tác vụ) + **NCS** (việc chuỗi không có trạng thái xử lý là suy từ phần bài không mô tả).
- **Liên quan:** K3.
- **Ghi chú:** đối tượng của [3] là bơm HVAC, của [7] là công trường thi công; không trực tiếp là kết cấu thép vận hành.
- **Phản chứng đã kiểm:**
  - Hệ quản lý bảo trì trên máy tính (CMMS), quản lý lệnh công việc có trạng thái: **chưa kiểm** trên nguồn chuyên về CMMS. Căn cứ gián tiếp đã có: [3] tr. 1 ghi CMMS lưu lệnh công việc hằng ngày, hồ sơ lịch sử, yêu cầu dịch vụ và thông tin bảo trì; [3] tr. 4 ghi CMMS lưu yêu cầu dịch vụ và lệnh công việc xử lý yêu cầu. Trạng thái hành động vì vậy nhiều khả năng đã được theo dõi ở CMMS.
  - BCF 3.0 (`K5SGFIGW`): **đã kiểm 30/09/2026**. Nguồn đọc: tài liệu kỹ thuật BCF-XML 3.0 và BCF-API 3.0 trên kho GitHub của buildingSMART (nhánh `release_3_0`); đặc tả không đánh số trang nên dẫn theo tên mục.
    - *Trạng thái:* mỗi vấn đề (Topic) bắt buộc có `TopicStatus` và `TopicType`, giá trị lấy từ danh sách định sẵn của dự án (BCF-XML, mục Topic). Có thêm `Priority`, `DueDate`, `Stage`, `AssignedTo` (tùy chọn).
    - *Người tạo, thời điểm:* `CreationAuthor`, `CreationDate` bắt buộc; `ModifiedAuthor`, `ModifiedDate` chỉ giữ lần sửa cuối (BCF-XML, mục Topic).
    - *Bình luận:* mỗi bình luận có `Date`, `Author`, nội dung và có thể trỏ tới một góc nhìn; mục đích là ghi lại trao đổi giữa các bên (BCF-XML, mục Comment).
    - *Liên kết cấu kiện:* qua góc nhìn (viewpoint), cấu kiện được chọn mang `IfcGuid` (BCF-XML, mục Components, Component). Phần đầu tệp còn cho phép trỏ tới `IfcProject` và phần tử không gian. Vấn đề **không** có trường riêng trỏ thẳng tới cấu kiện; liên kết đi qua góc nhìn.
    - *Lịch sử chuyển trạng thái:* BCF-API 3.0 có dịch vụ sự kiện của vấn đề (mục 3.9): mỗi lần tạo hoặc sửa sinh sự kiện có `date`, `author`, loại sự kiện (trong đó có `status_updated`, `assigned_to_updated`) và giá trị mới, nhằm giữ lịch sử đầy đủ. Lịch sử này chỉ có ở BCF-API; tệp BCF-XML không mang theo.
    - *Thẩm quyền:* BCF-API cho phép máy chủ giới hạn hành động theo người dùng, kể cả các giá trị trạng thái mà người dùng được chọn (mục 1.2, 3.1.5). Đây là quyền thao tác trên hệ thống; không có khái niệm vai trò chuyên môn hay thẩm quyền phê duyệt.
    - *Liên kết ra ngoài:* `ReferenceLink` (ví dụ tới hệ quản lý yêu cầu công việc), `DocumentReferences`, `BimSnippet`, `RelatedTopic` (BCF-XML, các mục cùng tên). Đây là liên kết tự do, không định kiểu.
    - **Kết quả đối chiếu:** BCF 3.0 **đã giải quyết** phần "trạng thái vấn đề gắn cấu kiện, ai tạo, khi nào, ai đổi trạng thái" của UV-01. Phần BCF **không có**: khái niệm bằng chứng và quan hệ định kiểu từ vấn đề về bằng chứng đã làm phát sinh nó; nguồn gốc, độ bất định, phạm vi hiệu lực; căn cứ của từng lần đổi trạng thái (sự kiện chỉ ghi loại và giá trị); máy trạng thái quy định bước chuyển hợp lệ; thẩm quyền theo vai trò chuyên môn. [NCS] Các điểm "không có" là nhận định từ việc đặc tả không nêu.
    - **Hệ quả với schema (NCS):** sự kiện chuyển trạng thái và danh sách trạng thái có tiền lệ trực tiếp ở BCF-API 3.0; mục 2.2 và 5.5 cần nêu BCF như tiền lệ, và phần mới của luận án thu về quan hệ giữa sự kiện với bản ghi sử dụng bằng chứng.
  - ISO 19650-3 [1], [44], [35]: **chưa kiểm** (phiên T1-1).
- **Phát biểu đã thu hẹp (sau khi kiểm BCF 3.0; còn chờ CMMS và ISO 19650):** trạng thái của vấn đề gắn cấu kiện, cùng lịch sử ai đổi trạng thái và khi nào, đã theo dõi được bằng BCF 3.0; phần chưa có là quan hệ định kiểu nối ngược từ hành động và từng lần đổi trạng thái về bằng chứng cảm biến cùng nguồn gốc và phạm vi hiệu lực của nó, và căn cứ kèm thẩm quyền chuyên môn của mỗi bước chuyển.

## UV-02 — Nguồn gốc, phiên bản phương pháp, phạm vi hiệu lực của đầu ra phát hiện

- **Phát biểu:** Đầu ra phát hiện bất thường và dự đoán trong các khung song sinh số công trình chưa được ghi như một
  bản ghi có nguồn gốc xử lý, phiên bản phương pháp và phạm vi hiệu lực.
- **Căn cứ:**
  - [3], tr. 5 (Hình 3: dữ liệu thô có Sensor_ID, Sensor_Timestamp), tr. 13–14 (đầu ra là điểm thay đổi và cảnh báo hiển
    thị; không mô tả phiên bản thuật toán, tham số hay điều kiện áp dụng). Đối chiếu ngữ cảnh vận hành để lọc điểm thay
    đổi (tr. 6) là xử lý một phần.
  - [7], tr. 9 (độ tin cậy dữ liệu nguồn là mối quan ngại; cần phân biệt dữ liệu cảm biến thật và mô phỏng; tính hợp lệ
    của dự đoán cần kiểm chứng), tr. 11 (kiểm chứng tính đúng và đủ của dữ liệu còn khó). Tìm trong văn bản: không có
    provenance, traceability, accountability, audit.
- **Loại căn cứ:** TG ([7] tr. 9, 11) + **NCS** (không có cơ chế ghi nguồn gốc/phạm vi là suy từ phần bài không xử lý).
- **Liên quan:** K1.
- **Ghi chú:** cần đối chiếu với [18], [45], Figueiredo 2011 (Tier 2) về phạm vi hiệu lực phụ thuộc điều kiện huấn luyện.
- **Phản chứng đã kiểm:** **chưa kiểm**. Cần đối chiếu PROV-O [69], SOSA/SSN [61]–[62], [16] Çelik 2023 (nguồn gốc dữ liệu BIM) và công cụ quản lý phiên bản mô hình (MLflow/DVC).
- **Phát biểu đã thu hẹp:** chưa có; chờ kết quả kiểm.

## UV-03 — Ghép cảm biến – cấu kiện có thời hạn

- **Phát biểu:** Việc gắn dữ liệu cảm biến với đối tượng BIM, khi có, được thực hiện bằng bảng ghép hoặc tương đương
  mà không có thời hạn hiệu lực và lịch sử thay đổi ghép.
- **Căn cứ:**
  - [7], tr. 7 (các nghiên cứu cảm biến trong xây dựng **không xử lý việc căn chỉnh dữ liệu cảm biến với chính mô hình BIM**),
    tr. 2 (dữ liệu từ nhiều nguồn phải được đối chiếu với BIM ở mức đối tượng và nhất quán theo thời gian).
  - [3], tr. 6, 10 (Hình 7, 11: bảng ghép GUID ↔ ID nguồn dữ liệu; chỉ bảng ghép cần bảo trì); không nêu thời hạn hiệu
    lực hoặc cách xử lý khi cảm biến được thay hay dời.
- **Loại căn cứ:** TG ([7] tr. 7 tự nêu chưa giải quyết) + **NCS** (không thời hạn hiệu lực là suy từ [3]).
- **Liên quan:** K2.
- **Căn cứ bổ sung (30/09/2026):** Theiler & Smarsly 2018 [2], tr. 58–60, 63 (quan hệ tĩnh, không thuộc tính thời gian; NCS), tr. 64 (động lực học của hệ quan trắc chưa mô tả được; TG).
- **Ghi chú:** [3] là **tiền lệ** cho việc ghép; điểm còn thiếu là thời hạn và lịch sử. Cần đối chiếu [2] (IFC Monitor),
  [35] ở phiên T1-1 trước khi coi đây là khoảng trống.
- **Phản chứng đã kiểm:**
  - [3] Lu 2020: đã kiểm. Có bảng ghép GUID ↔ ID nguồn dữ liệu (tr. 6, 10); không có thời hạn hiệu lực hay lịch sử thay đổi ghép.
  - [2] IFC Monitor (Theiler & Smarsly 2018, *Adv. Eng. Inform.* 37: 54–65): **đã kiểm 30/09/2026**, đọc toàn văn thân bài (tr. 54–64).
    - Quan hệ cảm biến – cấu kiện: nút cảm biến (`IfcSensorNode`) được tham chiếu ngữ nghĩa tới cấu kiện bằng `IfcRelAssignsToProduct`; mạng cảm biến nối với phần tử không gian (tầng) bằng `IfcRelServicesBuildings` (tr. 56, 59, 63; Listing 4).
    - Thời hạn hiệu lực: **không xử lý**. Ba thực thể mới (`IfcSensorNode`, `IfcSensorNetwork`, `IfcSHMSystem`) và kiểu liệt kê cấu trúc mạng không có thuộc tính thời gian; các quan hệ dùng lại của IFC được mô tả như quan hệ tĩnh (tr. 58–60, Hình 4, Listing 1). Tìm trong văn bản không có thuộc tính ngày lắp, ngày gỡ hay khoảng hiệu lực. [NCS] nhận định từ việc bài không nêu.
    - Bài đặt mục tiêu hỗ trợ lập hồ sơ và theo dõi thay đổi của hệ quan trắc trong vòng đời vận hành (tr. 55) nhưng không trình bày cơ chế; ca kiểm chứng là một hệ mẫu trên khung nhôm bốn tầng trong phòng thí nghiệm, mô hình hóa tại một thời điểm (tr. 61–63).
    - Tác giả tự nêu: động lực học của hệ quan trắc chưa mô tả được đầy đủ bằng các cách mô hình hóa trên nền IFC hiện có, để cho công việc sau (tr. 64).
    - **Kết quả đối chiếu:** [2] giải quyết phần "biểu diễn quan hệ cảm biến – cấu kiện trong IFC"; **không** giải quyết thời hạn hiệu lực và lịch sử thay đổi ghép. Có một căn cứ tác giả tự nêu (tr. 64).
  - Quan hệ gán và ánh xạ sẵn có trong IFC (IfcRelAssigns và các quan hệ liên quan, IfcOwnerHistory): **kiểm một phần, qua nguồn thứ cấp**. Theo [2] tr. 55, `IfcRoot` cho mỗi thực thể định danh toàn cục cùng thông tin quyền sở hữu và thay đổi; theo [3] tr. 5, `IfcOwnerHistory` không đủ cho lịch sử tài sản trong vận hành. **Chưa kiểm** trên chính đặc tả IFC (ISO 16739-1): thông tin thay đổi của một quan hệ có biểu diễn được khoảng hiệu lực không.
  - SOSA/SSN [61]–[62] (triển khai cảm biến trên nền tảng theo thời gian): **chưa kiểm**.
- **Phát biểu đã thu hẹp (sau khi kiểm [2]; còn chờ đặc tả IFC và SOSA/SSN):** quan hệ cảm biến – cấu kiện đã biểu diễn được trong IFC (IFC Monitor) và bằng bảng ghép GUID – ID; phần chưa có là thời hạn hiệu lực của quan hệ đó và lịch sử thay đổi khi cảm biến được lắp, dời, thay hoặc hiệu chuẩn lại.

## UV-04 — Định vị mức tích hợp DM/DS/DT cho kiểm tra – bảo trì

- **Phát biểu:** Chưa có phân loại mức tích hợp DM/DS/DT gắn với các khung có con người ra quyết định cho kiểm tra –
  bảo trì kết cấu công trình.
- **Căn cứ:**
  - Kritzinger và cs. 2018 [8], tr. 1020 (chưa có định nghĩa chung; cần mô hình tham chiếu theo lĩnh vực và các ca nghiên
    cứu); phạm vi bài là sản xuất (tr. 1018).
  - [7], tr. 12–13 (thang ba thế hệ cho song sinh số xây dựng, thế hệ 2 có xác nhận của người dùng).
- **Loại căn cứ:** TG ([8] tr. 1020) + **NCS** (việc chưa có phân loại cho kiểm tra – bảo trì kết cấu là suy từ phạm vi hai bài).
- **Liên quan:** mới, chỉ phục vụ **định vị** (mục 2.3 và câu khai báo mức DS ở Dẫn nhập). **[NCS]** Không nên phát triển
  thành khoảng trống của luận án: đây là câu hỏi khái niệm, không phải điều luận án kiểm chứng.
- **Phản chứng đã kiểm:** **chưa kiểm**. Cần đối chiếu [10] Chen 2021 (mô hình trưởng thành theo Gemini Principles) và Sepasgozar 2021 [9].
- **Phát biểu đã thu hẹp:** chưa có; ứng viên chỉ dùng để định vị.

## UV-05 — Thiếu nhãn hư hỏng ở hiện trường

- **Phát biểu:** Ở công trình đang vận hành, khó có dữ liệu có nhãn về bất thường; phân biệt bình thường – bất thường phụ
  thuộc nhiều vào đánh giá của con người, nên nhãn cần đến từ kiểm tra.
- **Căn cứ:** [3], tr. 2 (dữ liệu có nhãn tốt thường không sẵn có ở môi trường xây dựng), tr. 3 (khó phân biệt điều
  kiện bình thường và bất thường, hiện phụ thuộc đánh giá của con người), tr. 13 (huấn luyện bộ phân loại một lớp cần dữ
  liệu lớn ở nhiều điều kiện bình thường, không thực tế).
- **Loại căn cứ:** TG.
- **Liên quan:** mới (nhãn hiện trường, vòng lặp kiểm tra tạo nhãn). Trong GD1 đây là luận điểm L2.3 ("thiếu dữ liệu hư
  hỏng có nhãn ở hiện trường"), đã có nguồn ở 5.6A (Bull 2022, Wang & Cha 2021, [57]) mà chưa đưa vào nhật ký này.
- **Ghi chú:** đối tượng của [3] là bơm HVAC; chỉ dùng như căn cứ cùng chiều.
- **Phản chứng đã kiểm:** **chưa kiểm**. Cần đối chiếu học chủ động theo rủi ro (Hughes 2022 `Z9RD5DMZ`, Bull 2022 `87NKU5IS`) và SHM theo quần thể [57], là các hướng đã đề xuất cách lấy nhãn từ kiểm tra.
- **Phát biểu đã thu hẹp:** chưa có; chờ kết quả kiểm.
