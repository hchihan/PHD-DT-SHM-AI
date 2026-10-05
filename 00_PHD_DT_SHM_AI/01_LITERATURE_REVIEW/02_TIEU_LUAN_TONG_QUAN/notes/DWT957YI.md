# DWT957YI — Ramonell, Chacón & Posada (2023) — [42]

Ramonell C, Chacón R, Posada H. Knowledge graph-based data integration system for digital twins of built assets.
*Automation in Construction* 156: 105109. DOI 10.1016/j.autcon.2023.105109. Nhận 31/05/2023, sửa 20/09/2023, chấp nhận
25/09/2023, trực tuyến 05/10/2023; truy cập mở CC BY-NC (tr. 1). Thông tin trên đã đối chiếu với trang 1 của bản PDF.

**Bản đã đọc:** toàn văn bản PDF của nhà xuất bản, tệp `pdf/DWT957YI_Ramonell2023.pdf`, 21 tr. (thân bài tr. 1–20, danh
mục tài liệu tr. 20–21). Số trang là trang in, trùng trang PDF. Văn bản trích bằng PyMuPDF; các hình chứa nội dung chính
(Hình 4, 6, 11–17, 19–21) được xem trực tiếp trên ảnh trang, vì chữ trong hình không trích được. Hình 1–3, 5, 7–10 và
Bảng 5–7 (ảnh chụp giao diện) chỉ đọc qua chú thích và lời mô tả. Đọc ngày 01/10/2026, phiên T2-4.

Ký hiệu: (a) điều tác giả nói; (b) giới hạn tác giả tự nêu; **[NCS]** nhận định của NCS.

| Cột | Nội dung |
|---|---|
| Citekey / Số cũ | DWT957YI / [42] |
| Tier / Cụm | Tier 2 / Song sinh số (phần tích hợp dữ liệu; liên quan Truy vết thông tin) |
| Luận điểm | Một đồ thị tri thức (knowledge graph) lưu trong cơ sở dữ liệu đồ thị, dựng trên lược đồ IFC và mở rộng bằng các bản thể học (ontology) riêng cho dữ liệu quá trình và nền tảng IoT, có thể làm cơ chế tích hợp dữ liệu chính cho song sinh số của công trình, đáp ứng các yêu cầu mô-đun, mở rộng được, liên tác, chạy trên đám mây và có API (tr. 2, 4, 19). |
| Bằng chứng | Hệ vi dịch vụ gồm 8 dịch vụ (Neo4j, MongoDB, RabbitMQ, IfcConvert, Ifc2Graph, Processes, MainfluxSync, máy chủ API; Bảng 3, tr. 6; Hình 4). Nhập 16 tệp IFC của các công trình thử nghiệm dự án ASHVIN vào đồ thị (từ 44 nút/122 quan hệ đến 28.664 nút/219.895 quan hệ; Bảng 4, tr. 9); số hóa ba loại hoạt động bảo trì (thử tải cầu, quét laser, kiểm tra bằng drone; Bảng 8, tr. 14); nối cảm biến IFC với "thing" của nền tảng IoT Mainflux qua GUID chung (tr. 19, Hình 20); một truy vấn mẫu trả về dữ liệu cảm biến của một cấu kiện trong thời gian một nhiệm vụ (Hình 21, tr. 19). Không có đánh giá định lượng hiệu năng hay đánh giá với người dùng; dữ liệu bảo mật (tr. 20). |
| Giới hạn | Xem mục 7. |
| Tác động K1/K2/K3 | K2: thu hẹp một phần (liên tục định danh BIM – IoT bằng GUID chung và quan hệ tương đương; thuộc tính lắp/gỡ cảm biến có trong mô hình dữ liệu thử tải). K3: không thu hẹp (nhiệm vụ có trạng thái là giá trị thuộc tính; không có nối kết quả kiểm tra → hành động, không sự kiện, không thẩm quyền). K1: không liên quan trực tiếp (kết quả đo không có độ bất định, phiên bản phương pháp, phạm vi hiệu lực). |
| Vị trí sử dụng | 2.3 (đồ thị tri thức làm nền tích hợp cho song sinh số công trình; định nghĩa song sinh số theo VanDerHorn & Mahadevan); 4.x (ánh xạ cảm biến – cấu kiện qua GUID; tiền lệ cùng [2], SSN); 5.5 (tiền lệ cho schema dạng đồ thị trên nền IFC; Phụ lục ánh xạ). |
| Mức đã đọc | Toàn văn (01/10/2026) |

## 1. Câu hỏi và đối tượng

- (a) Mục tiêu (tr. 4): trình bày một hệ kết hợp mô hình ảo của công trình với nhiều nguồn dữ liệu theo các yêu cầu ở mục 2,
  gồm (i) một đồ thị tri thức trung tâm, (ii) cơ chế tích hợp và khai thác dữ liệu theo ngữ nghĩa, (iii) kiến trúc vi dịch vụ.
- (a) Yêu cầu của song sinh số công trình (Bảng 1, tr. 3): mô hình ảo đa lĩnh vực, đa tỷ lệ, mở rộng được, liên tác; dữ
  liệu từ nhiều nguồn ngoài, nhiều định dạng (chuỗi thời gian, ảnh, đám mây điểm); hệ chạy trên đám mây, có API, mô-đun.
- (a) Định nghĩa song sinh số dùng trong bài: định nghĩa tổng quát của VanDerHorn & Mahadevan, rút từ 65 định nghĩa
  (tr. 2). Tác giả nêu rằng định nghĩa này để ngỏ câu hỏi về "mức phát triển của song sinh số" (tr. 2) và mức phát triển trong
  xây dựng còn "loang lổ" (tr. 2).
- (a) Kết nối vật lý – số theo "đúng lúc" (right-time) thay vì "thời gian thực", vì thu thập và tích hợp dữ liệu cần con
  người tham gia; song sinh số cần cả luồng máy – máy qua IoT lẫn giao diện cho người tải lên dữ liệu (tr. 3).
- Đối tượng: mười công trình thử nghiệm của dự án ASHVIN (Bảng 2, tr. 5; Hình 3): cầu đường sắt cao tốc (1), nhà ở nhiều
  hộ (2), đường băng sân bay (3), **nhà công nghiệp ở Đức (4; chỉ dữ liệu ảnh, giai đoạn thi công)**, nhà văn phòng
  27 tầng (5), nhà văn phòng (6), cầu dầm hộp liên hợp thép – bê tông cong (7), cầu bộ hành (8), mái sân vận động (9),
  tường bến cảng (10). [NCS] Không có ca nhà công nghiệp khung thép ở giai đoạn vận hành; demo 4 chỉ phục vụ thi công.

## 2. Hệ thống và kiến trúc thông tin

- **Kiến trúc** (tr. 6, 11–12; Bảng 3; Hình 4): vi dịch vụ đóng gói Docker; giao tiếp HTTP/REST và AMQP (RabbitMQ) để cập
  nhật đồ thị theo sự kiện. Đồ thị tri thức lưu trong Neo4j theo mô hình đồ thị thuộc tính có nhãn (labelled property
  graph); dữ liệu quá trình lưu trong MongoDB (JSON); tệp IFC gốc và tệp hình học lưu ở máy chủ (tr. 6, 12).
- **Vai trò của đồ thị** (a): "chỉ mục ngữ nghĩa" của dữ liệu trong hệ, đặt trong ngữ cảnh mô hình thông tin công trình
  (tr. 12). [NCS] Đồ thị giữ siêu dữ liệu và bản tóm tắt; số đo nằm ở nền tảng IoT, chi tiết quá trình nằm ở MongoDB
  (Bảng 3, tr. 6; tr. 16; Hình 21).
- **Chuẩn và bản thể học dùng:**
  - IFC là nền ngữ nghĩa: đồ thị "theo lược đồ IFC" (tr. 12, 14); IFC2x3 và IFC4 (Bảng 4); tài liệu IFC 4.3.1.0 được dẫn
    cho lược đồ (tr. 12, 16; tham khảo [28]).
  - Có thể ánh xạ sang RDF/bản thể học bằng phần mở rộng Neosemantics (tr. 12; Hình 5). Bài điểm qua ifcOWL và các bản
    thể học LBD (BOT, BEO, DOT, DOT hư hỏng, bản thể học cầu, BPO, OPM, OMG, FOG; tr. 9) nhưng [NCS] không trình bày ánh xạ
    đã thực hiện sang bất kỳ bản thể học nào trong số này.
  - Hai "bản thể học" do tác giả định nghĩa: bản thể học nhiệm vụ IFC rút gọn (`IfcWorkPlan`, `IfcWorkSchedule`, `IfcTask`,
    `IfcTaskTime`, `IfcProduct` với các quan hệ Controls, Nests, IsPredecessorTo, OperatesOn, HasAssignments, hasTaskTime;
    Hình 11, tr. 12) kèm phân loại nhiệm vụ bảo trì (Hình 14, tr. 14); và bản thể học Mainflux (MFThing, MFChannel, tệp ảnh,
    đám mây điểm, video; Hình 17, tr. 17).
  - **Không dùng** SOSA/SSN, PROV-O, BCF hay SHACL. [NCS] Nhận định từ việc bài không nêu; tìm trong văn bản không có các
    từ "SOSA", "SSN", "provenance", "PROV", "SHACL".
- **IFC → đồ thị** (tr. 12, 14; Hình 6–9): Ifc2Graph (Python, IfcOpenShell, Pydantic, trình điều khiển Neo4j) chuyển thực
  thể và quan hệ IFC thành nút và cạnh; bộ thuộc tính (`IfcPropertySetDefinition`) gộp thành thuộc tính của nút; thực thể
  quan hệ (`IfcRelationship`) được "bắc cầu" thành cạnh trực tiếp bằng thuộc tính ngược (Hình 9). Hình học bỏ ra ngoài, chỉ
  giữ cờ "presentation" và GlobalId để tra tệp GLB (tr. 14). (a) Kết quả **không tương thích ngược** với định dạng IFC (tr. 14).
- **Tầng tài sản – tệp** (tr. 12; Hình 6): nút Asset nối với một hay nhiều nút File (HAS_FILE); mọi nút IFC mang `file_id`
  của tệp nguồn (Hình 12, 16, 20).
- **Dữ liệu quá trình** (tr. 15–17; Hình 10, 13–16): báo cáo hoạt động dạng văn bản được **người** số hóa theo một mô hình
  dữ liệu riêng cho từng loại báo cáo thành JSON (Hình 13); phần chung theo `IfcTask`, phần mở rộng theo nhu cầu (dữ liệu
  "đa hình", tr. 17). Phân loại nhiệm vụ bảo trì: Đánh giá (quét laser, thử tải), Kiểm tra (kiểm tra bằng drone), Sửa chữa
  (sửa nhỏ, sửa lớn, thay thế) (Hình 14, tr. 14). Bản tóm tắt nhiệm vụ được nối vào đồ thị: `IfcTask` (ObjectType LOADTEST,
  Status COMPLETED, WorkMethod STATIC) OperatesOn/HasAssignments các `IfcBeam`, có `IfcTaskTime` (ActualStart, ActualFinish,
  DataOrigin MEASURED) (Hình 16, tr. 16; Hình 12, tr. 13).
- **Mô hình dữ liệu thử tải** (Hình 15, tr. 15; theo quy định thử tải của ADIF, tham khảo [75]): LoadTest (bridgeId, tests,
  equipment: danh sách Sensor, results, **validated: Boolean**); Test (testType tĩnh/động/giả tĩnh, startTime, endTime,
  simulationId); **Sensor (id, name, measurement, unit, frequency, installation: datetime, removal: datetime)**; kết quả
  tĩnh (sensorId, elementId, testId, predicted, maximum, net, ratio, remaining, recovery) và kết quả động (va chạm, cản, tần
  số; mỗi loại có testId, elementId, sensorId).
- **Nền tảng IoT** (tr. 17, 19; Hình 17–20): Mainflux (mã nguồn mở) với thing, channel, user; nhận HTTP, MQTT, WebSocket,
  CoAP, LoRaWAN; thông điệp SenML hoặc JSON; lưu chuỗi thời gian; nhận cả tệp đám mây điểm, ảnh, video. Khi nhập một tệp IFC,
  MainfluxSync tự tạo hai kênh "Status" (đổi cấu hình thiết bị tại hiện trường) và "RawData" (số đo trực tiếp), ánh xạ mỗi
  `IfcSensor` thành một thing nối vào cả hai kênh (tr. 19; Hình 19).

## 3. Cảm biến và dữ liệu quan trắc được nối với cấu kiện thế nào

- (a) Thực thể tương đương ở nền tảng IoT và ở đồ thị BIM **dùng chung GUID**, "khía cạnh then chốt cho tích hợp" (tr. 19).
  Thing Mainflux và `IfcSensor` cùng GUID được nối bằng quan hệ `IS_A` biểu thị tương đương (tr. 19; Hình 20, ví dụ ACELV3,
  P12, G32 của cầu Viaducto La Plata).
- Quan hệ cảm biến – cấu kiện là quan hệ có sẵn trong tệp IFC được chuyển sang đồ thị: truy vấn ở Hình 21 đi theo
  `(t:IfcTask)-->(p:IfcProduct)-->(s:IfcSensor)--(mt:MFThing)-->(mc:MFChannel {type:"RawData"})` (tr. 19). [NCS] Bài không
  nói quan hệ IFC cụ thể nào nối sản phẩm với cảm biến.
- **Khoảng thời gian** của dữ liệu lấy ra được suy từ `IfcTaskTime` (ActualStart, ActualFinish) của nhiệm vụ: truy vấn
  "lấy mọi cảm biến đã nối với sản phẩm A trong nhiệm vụ B và trả về URL dữ liệu ghi trong nhiệm vụ đó" (Hình 21, tr. 19).
  [NCS] Thời gian gắn với **nhiệm vụ**, không gắn với **quan hệ** cảm biến – cấu kiện; quan hệ này không có thuộc tính thời
  gian trong đồ thị. [NCS] Trên ảnh của Hình 21, cả hai tham số time_from và time_to của truy vấn đều lấy từ ActualStart;
  có thể là lỗi trình bày, không dùng chi tiết này.
- **Thời điểm lắp/gỡ cảm biến** có trong mô hình dữ liệu thử tải (Sensor.installation, Sensor.removal; Hình 15, tr. 15),
  tức là thuộc tính của **bản ghi cảm biến trong một hoạt động**, lưu ở MongoDB. Cặp cảm biến – cấu kiện xuất hiện ở từng
  **kết quả** (sensorId, elementId, testId). [NCS] Không có ràng buộc kiểm thời điểm đo nằm trong khoảng lắp – gỡ, không có
  lịch sử dời hay thay cảm biến, và bài không mô tả các thuộc tính này được đưa vào đồ thị.
- **Phiên bản:** [NCS] không có cơ chế phiên bản cho quan hệ hay cho mô hình. Một tài sản có nhiều tệp IFC (Hình 6), và
  Bảng 4 có hai tệp "KineumSpacesRoombasedOld.ifc" và "KineumSpacesRoombased.ifc" (tr. 9), nhưng bài không nêu quan hệ phiên
  bản giữa các tệp hay cách giữ định danh khi mô hình thay đổi.

## 4. Mức DM/DS/DT theo định nghĩa luồng dữ liệu của Kritzinger [8]

- Tác giả **không** khai báo mức tích hợp theo [8]; bài dùng định nghĩa của VanDerHorn & Mahadevan (tr. 2) và gọi hệ là nền
  cho "song sinh số" (tr. 1, 19–20).
- Chiều vật lý → số:
  - Cảm biến: số đo được truyền qua kênh RawData vào nền tảng IoT (tr. 19); đồ thị chỉ được tự động cập nhật **siêu dữ
    liệu** của nền tảng (MainfluxSync, Bảng 3, tr. 6), số đo lấy theo URL khi truy vấn (Hình 21). Ví dụ trong bài là dữ liệu
    lưu của một lần thử tải đã qua (Hình 21, tr. 19).
  - Dữ liệu quá trình: báo cáo được người số hóa theo mô hình dữ liệu (Hình 13, tr. 14; tr. 15–17), tức luồng thủ công.
  - Mô hình IFC: người dùng tải tệp lên qua giao diện (tr. 12).
- Chiều số → vật lý: kênh "Status" dùng để "giao tiếp và thay đổi cấu hình thiết bị" tại hiện trường (tr. 19). Đây là
  điều khiển **thiết bị đo**, không phải tác động lên công trình. Bài không mô tả quyết định hay hành động nào được hệ tự
  động gửi về công trình; với đường băng, "người dùng" là người kích hoạt sửa chữa sau kiểm tra (Bảng 8, tr. 14).
- **[NCS] Kết luận:** theo [8], phần cảm biến đạt cao nhất mức **bóng số (DS)**: luồng vật lý → số tự động tới nền tảng IoT,
  luồng số → vật lý về công trình là thủ công. Phần quá trình và mô hình chỉ ở mức **mô hình số (DM)** vì cập nhật thủ công.
  Hệ không đạt mức **song sinh số (DT)** theo [8]. Đây là suy luận của NCS; tác giả không phân loại như vậy. Cách nói
  "right-time" có con người tham gia (tr. 3) phù hợp với nhận định này.

## 5. Ca nghiên cứu và đánh giá

- Mười công trình thử nghiệm ASHVIN quyết định yêu cầu cho hệ (tr. 4–5; Bảng 2). Hoạt động bảo trì được số hóa cho các
  công trình 1, 3, 7, 9 (tr. 17; Bảng 8). [NCS] Tr. 17 ghi "demonstrators 1, 3, 7 and 9 of Table 1", nhưng danh sách công
  trình là Bảng 2; có thể là lỗi đánh số.
- Đánh giá gồm: (i) nhập 16 tệp IFC do nhiều người, nhiều nhóm lập "giúp kiểm tính tổng quát" của chuyển đổi, báo số nút
  và quan hệ (tr. 15; Bảng 4); (ii) ảnh giao diện cho ba ca (một cầu, hai nhà; Bảng 5–7, tr. 10–11); (iii) ví dụ cấu trúc
  nhiệm vụ cho thi công (rung bê tông cột, demo 6; Hình 12) và cho thử tải (Hình 16); (iv) ví dụ thiết lập Mainflux (Hình 19)
  và một truy vấn BIM – IoT – quá trình (Hình 21).
- [NCS] Không có số đo hiệu năng truy vấn, không so với cách làm hiện hành, không đánh giá với người dùng, không kiểm độ đúng
  hay độ đầy đủ của liên kết. Đánh giá ở mức minh chứng khả thi.

## 6. Luận điểm chính

1. Đồ thị tri thức là cơ chế tích hợp phù hợp cho song sinh số công trình vì cho phép ghép ngữ nghĩa IFC với các bản thể học
   khác, cập nhật linh hoạt, truy vấn chi tiết (tr. 19).
2. Mô hình quan hệ không phù hợp để lưu IFC vì số thực thể lớn và lược đồ cứng, cản trở làm giàu ngữ nghĩa (tr. 5).
3. Tích hợp một nền tảng dữ liệu ngoài cần mô tả tường minh nguyên tắc tổ chức của nó bằng một bản thể học rồi nối với
   khái niệm IFC (tr. 11, 17).
4. Định danh chung (GUID) giữa BIM và IoT là điều kiện then chốt của tích hợp (tr. 19).
5. (a) Ở cấp tòa nhà, chưa thấy hệ dựa trên đồ thị tri thức trong tài liệu học thuật (tr. 9). [NCS] Đây là nhận định của
   tác giả năm 2023; [16] Çelik 2023 và [44] García 2026 cần đối chiếu nếu dùng câu này.

## 7. Giới hạn

**(b) Tác giả tự nêu:**
- Bài không phát triển phân loại và mô hình dữ liệu đầy đủ cho quá trình thi công, bảo trì; yêu cầu thông tin khác nhau theo
  tổ chức và quốc gia; cần thư viện quá trình chung, làm cùng doanh nghiệp, học thuật và cơ quan tiêu chuẩn (tr. 16–17).
- Số hóa hoạt động thành dạng máy đọc được chưa phải thực hành phổ biến (tr. 15).
- Đồ thị không tương thích ngược với định dạng IFC và chỉ giữ thông tin ngữ nghĩa (tr. 14).
- Các bản thể học LBD chưa phủ hết độ giàu ngữ nghĩa của IFC; ifcOWL cho mô hình rất lớn (tr. 9–10).
- Hiệu quả của hệ phụ thuộc vào công cụ cho người dùng cuối có giao diện phù hợp (tr. 12).
- Quản lý xác thực, an ninh dữ liệu và cải thiện quy trình tương tác là các bước tiếp theo (tr. 20).
- Dữ liệu dùng là bảo mật (tr. 20).

**[NCS] nhận định:**
- Không có nguồn gốc (provenance) của dữ liệu hay kết quả: không ghi ai tạo, bằng phương pháp nào; chỉ có `CreationDate` của
  kế hoạch, `DataOrigin = MEASURED` của thời gian nhiệm vụ (Hình 12) và cờ `validated` của thử tải (Hình 15), không có người
  xác nhận.
- Không có độ bất định, phiên bản phương pháp, phạm vi hiệu lực của kết quả đo.
- Trạng thái nhiệm vụ (`Status = COMPLETED`) là giá trị thuộc tính, không có lịch sử chuyển trạng thái, không có người và
  thẩm quyền (Hình 12, 16).
- Phân loại có "Kiểm tra" và "Sửa chữa" (Hình 14) nhưng bài không mô tả quan hệ nào nối một kết quả kiểm tra với một nhiệm
  vụ sửa chữa.
- Quan hệ cảm biến – cấu kiện trong đồ thị là tĩnh; thời gian lắp/gỡ chỉ có ở bản ghi thử tải; không có ràng buộc thời gian.
- Ca thử nghiệm chủ yếu là cầu và nhà thi công; nhà công nghiệp (demo 4) chỉ có ảnh giai đoạn thi công. Không dùng [42]
  làm căn cứ cho luận điểm về nhà công nghiệp khung thép vận hành.
- Không phân biệt dữ liệu đo, kết quả phân tích và kết luận; [NCS] với khung của luận án, "kết quả phân loại ≠ bằng chứng
  trạng thái ≠ chẩn đoán" không có tương ứng.

## 8. Đoạn dùng được cho tiểu luận

| Mục | Ý dùng | Trang | Loại |
|---|---|---|---|
| 2.3 | Định nghĩa song sinh số còn chưa thống nhất; VanDerHorn & Mahadevan rút định nghĩa tổng quát từ 65 định nghĩa, để ngỏ câu hỏi về mức phát triển | 2 | (a) |
| 2.3 | Mức phát triển song sinh số trong xây dựng còn không đồng đều, từ mô hình khó cập nhật bằng dữ liệu vật lý đến song sinh đơn chức năng | 2 | (a) |
| 2.3, 3.6 | Kết nối "đúng lúc" thay cho "thời gian thực" vì cần con người tham gia thu thập và tích hợp dữ liệu | 3 | (a) |
| 2.3 | Yêu cầu của song sinh số công trình theo ba nhóm mô hình ảo – dữ liệu – hệ thống | 3 (Bảng 1) | (a) |
| 2.2, 5.5 | Đồ thị thuộc tính dựng trên lược đồ IFC giúp mở rộng ngữ nghĩa linh hoạt hơn mô hình quan hệ; mô hình quan hệ cứng cản trở làm giàu ngữ nghĩa | 5, 7 | (a) |
| 4.x, 5.5 | GUID chung giữa đối tượng BIM và thực thể IoT là then chốt cho tích hợp; quan hệ tương đương `IS_A` giữa `IfcSensor` và thing | 19, Hình 20 | (a) |
| 5.5 | Tiền lệ đồ thị nối nhiệm vụ IFC (`IfcTask`, `IfcTaskTime`) – cấu kiện – cảm biến – kênh dữ liệu, truy vấn dữ liệu cảm biến của cấu kiện trong thời gian một nhiệm vụ | 13, 16, 19 (Hình 12, 16, 21) | (a) |
| 4.x | Thời điểm lắp, gỡ cảm biến đã được đưa vào mô hình dữ liệu của một hoạt động thử tải, ở mức bản ghi cảm biến | 15 (Hình 15) | (a) + [NCS] diễn giải |
| 3.2 hoặc 1.x | Số hóa hoạt động thành dạng máy đọc được chưa phổ biến; báo cáo được người chuyển thành dữ liệu cấu trúc | 14–15 (Hình 13) | (a) |
| 2.3, 5.5 | Phân loại và mô hình dữ liệu cho quá trình bảo trì khác nhau theo tổ chức, quốc gia; cần thư viện quá trình chung | 16–17 | (b) |
| 2.3 (định vị) | Hệ đạt mức DS cho luồng cảm biến, DM cho quá trình; không phải DT theo [8] | 3, 6, 14, 19 | [NCS] |

## 9. Ánh xạ với schema của luận án (CLAUDE.md mục 8)

| Thực thể luận án | Ở [42] | Mức | Trang |
|---|---|---|---|
| `COMPONENT` (BIM_GUID, model_version) | Nút IFC (ví dụ `IfcBeam`) mang GlobalId, nhãn lớp IFC và cha, thuộc tính gộp từ bộ thuộc tính, `file_id` | **Có** (định danh); model_version: tương đương một phần qua `file_id` | 12, 14, Hình 8, 16 |
| `MODEL_VERSION` | Nút File nối với Asset (HAS_FILE); một tài sản nhiều tệp | **Tương đương một phần**; không có quan hệ phiên bản giữa tệp | 12, Hình 6; Bảng 4 |
| `SENSOR` (Sensor_ID) | `IfcSensor` (GlobalId, Tag) và MFThing cùng GUID, nối `IS_A` | **Có** | 19, Hình 20 |
| `SENSOR_MAPPING` (valid_from, valid_to, install_record_ref) | Quan hệ sản phẩm – cảm biến lấy từ IFC, không thuộc tính thời gian; Sensor.installation/removal ở mô hình thử tải; cặp sensorId – elementId ở từng kết quả | **Tương đương một phần**: có thời điểm lắp/gỡ ở bản ghi cảm biến của hoạt động, không ở quan hệ; không ràng buộc | 15 (Hình 15), 19 (Hình 21) |
| `OBS_CONTEXT` (campaign, sensor_config) | `IfcTask` (LOADTEST, WorkMethod) + `IfcTaskTime`; Test (testType, startTime, endTime, simulationId); kênh Status cho cấu hình thiết bị | **Tương đương** | 15–16, 19; Hình 15, 16 |
| `EVIDENCE` (value, uncertainty, method_version, evidence_type) | Kết quả tĩnh/động của thử tải (giá trị, sensorId, elementId, testId); tệp ảnh, đám mây điểm, video gắn `IfcElement` (RELATED TO) | **Tương đương một phần**: có giá trị và liên kết cảm biến – cấu kiện – lần thử; **không** có uncertainty, method_version | 15 (Hình 15), 17 (Hình 17) |
| `VALIDITY_SCOPE` | — | **Không có** | — |
| `EVIDENCE_USE` | — | **Không có** | — |
| `INSPECTION_RECORD` | Nhiệm vụ loại Kiểm tra / Đánh giá (kiểm tra drone, quét laser, thử tải) theo `IfcTask`, OperatesOn cấu kiện; cờ `validated` của thử tải | **Tương đương** | 14 (Hình 14, Bảng 8), 15–16 |
| `ACTION` (priority_level, Action_Status) | Nhiệm vụ loại Sửa chữa (nhỏ, lớn, thay thế) trong phân loại; `IfcTask.Status` | **Tương đương một phần**: có loại và trạng thái hiện tại; không có mức ưu tiên; không nối với kết quả kiểm tra | 14 (Hình 14, Bảng 8), 13, 16 |
| `STATUS_EVENT` (from_to, reason, timestamp) | — (trạng thái là giá trị thuộc tính) | **Không có** | 13, 16 (Hình 12, 16) |
| `AGENT` (role, authority) | User của Mainflux là người, tổ chức **sở hữu** kênh và thing; xác thực để cho bước sau | **Không có** theo nghĩa vai trò – thẩm quyền | 17, 20 |

Quan hệ: [NCS] [42] có chuỗi `IfcTask` → `IfcProduct` → `IfcSensor` → thing → kênh dữ liệu (Hình 21) và kết quả → cảm biến,
cấu kiện, lần thử (Hình 15). Không có quan hệ kết quả → hành động, hành động → sự kiện chuyển trạng thái, hay bằng chứng →
phạm vi hiệu lực. Mô hình đồ thị thuộc tính của [42] là tiền lệ công nghệ cho "schema dạng đồ thị" (quyết định 7); khác ở
chỗ [42] lấy nút IFC làm thực thể chính, còn luận án đặt bằng chứng và bước chuyển trạng thái làm thực thể chính trên nền IFC.

## 10. Kiểm phản chứng

### UV-01 — Chuỗi cảnh báo → hành động (K3)

- **Kết quả: không giải quyết.**
- Có: phân loại nhiệm vụ bảo trì gồm Kiểm tra và Sửa chữa, trên nền `IfcTask` (Hình 14, tr. 14); nhiệm vụ gắn cấu kiện
  (OperatesOn, HasAssignments) và có `Status`, `IfcTaskTime` (Hình 12, 16); với đường băng, người dùng kích hoạt sửa chữa
  dựa trên kết quả kiểm tra (Bảng 8, tr. 14).
- Không có: quan hệ định kiểu từ kết quả kiểm tra hay số đo tới nhiệm vụ sửa chữa; sự kiện chuyển trạng thái; người, căn cứ,
  thẩm quyền của bước chuyển; xác minh sau sửa. Trạng thái là giá trị thuộc tính hiện tại. [NCS] Các điểm "không có" là
  nhận định từ việc bài không nêu.
- Phát biểu đã thu hẹp của UV-01 **giữ nguyên**. [42] có thể nêu thêm như ví dụ rằng một khung song sinh số công trình có
  nhiệm vụ sửa chữa trong phân loại nhưng dừng ở trạng thái thuộc tính (căn cứ loại NCS, 2023).

### UV-03 — Ghép cảm biến – cấu kiện có thời hạn (K2)

- **Kết quả: giải quyết một phần, phạm vi hẹp.**
- Có: (i) liên tục định danh giữa BIM và nền tảng IoT bằng GUID chung và quan hệ tương đương `IS_A`, cảm biến được tự tạo ở
  nền tảng IoT khi nhập IFC (tr. 19; Hình 19, 20); (ii) thuộc tính `installation` và `removal` của cảm biến trong mô hình dữ
  liệu thử tải (Hình 15, tr. 15); (iii) mỗi kết quả mang sensorId, elementId, testId (Hình 15); (iv) truy vấn giới hạn dữ liệu
  cảm biến theo thời gian của nhiệm vụ (Hình 21, tr. 19).
- Không có: thời hạn hiệu lực trên **quan hệ** cảm biến – cấu kiện trong đồ thị; lịch sử lắp – dời – thay – hiệu chuẩn; ràng
  buộc kiểm thời điểm đo nằm trong khoảng lắp – gỡ. [NCS] Nhận định từ việc bài không nêu.
- **Phát biểu đã thu hẹp (bổ sung):** ngoài các tiền lệ đã ghi ([2], [3], IFC4, SSN/SOSA), thời điểm lắp và gỡ cảm biến đã
  xuất hiện như thuộc tính của bản ghi cảm biến trong mô hình dữ liệu của một hoạt động thử tải, và định danh chung BIM – IoT
  đã được dùng trong một đồ thị tri thức [42]. Phần chưa có giữ nguyên: một cách ghép được quy định, với khoảng hiệu lực
  bắt buộc **trên quan hệ** cảm biến – cấu kiện, lịch sử thay đổi, và ràng buộc thời điểm quan trắc nằm trong khoảng đó (C3).
  [NCS] Đánh giá UV-03 là yêu cầu của mô hình dữ liệu (C3) càng được củng cố.

### UV-04 — Định vị mức tích hợp DM/DS/DT (định vị)

- **Kết quả: không giải quyết.**
- [42] dùng định nghĩa tổng quát của VanDerHorn & Mahadevan và tự nêu rằng định nghĩa này để ngỏ "mức phát triển của song
  sinh số", mức phát triển trong xây dựng còn không đồng đều (tr. 2); đề xuất kết nối "đúng lúc" có con người tham gia (tr. 3).
  Không có phân loại DM/DS/DT hay thang mức tích hợp.
- [NCS] [42] là căn cứ bổ sung loại TG (gián tiếp) cho UV-04: tác giả nêu câu hỏi về mức phát triển nhưng không trả lời,
  đồng thời gọi hệ là song sinh số dù luồng số → vật lý về công trình là thủ công (mục 4). CẦN NCS KIỂM có tính [42] là căn
  cứ độc lập thứ ba cho UV-04 hay không. Phát biểu đã thu hẹp giữ nguyên; vẫn chỉ dùng để định vị.

## 11. Tác động tới K1/K2/K3

- **K2: thu hẹp một phần.** Định danh chung BIM – IoT và quan hệ tương đương đã có tiền lệ trong đồ thị tri thức (tr. 19);
  thời điểm lắp/gỡ cảm biến có ở mức bản ghi hoạt động (Hình 15). Còn lại: khoảng hiệu lực trên quan hệ, lịch sử, ràng buộc.
- **K3: không thu hẹp.** Có nhiệm vụ kiểm tra, sửa chữa với trạng thái hiện tại; không có nối kết quả → hành động, sự kiện
  chuyển trạng thái, thẩm quyền.
- **K1: không liên quan trực tiếp.** Kết quả đo có giá trị và liên kết cảm biến – cấu kiện – lần thử nhưng không có nguồn
  gốc xử lý, độ bất định, phiên bản phương pháp, phạm vi hiệu lực.

## 12. Vị trí sử dụng trong tiểu luận v2

- 2.3: đồ thị tri thức làm nền tích hợp dữ liệu cho song sinh số công trình; định nghĩa song sinh số chưa thống nhất; khai báo
  rằng hệ đạt DS/DM theo [8] là nhận định của NCS.
- 4.x: ánh xạ cảm biến – cấu kiện qua GUID chung (cùng [2] IFC Monitor, [3] bảng ghép GUID, SSN `Deployment`).
- 5.5: tiền lệ công nghệ cho schema dạng đồ thị trên nền IFC; nêu điểm khác (thực thể chính là bằng chứng và bước chuyển).
- Không dùng làm căn cứ cho nhà công nghiệp khung thép vận hành.
