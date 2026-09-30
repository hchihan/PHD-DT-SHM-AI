# 2ILY9YZ3 — Theiler & Smarsly (2018) — [2]

Theiler M, Smarsly K. IFC Monitor – An IFC schema extension for modeling structural health monitoring systems.
*Advanced Engineering Informatics* 37: 54–65. DOI 10.1016/j.aei.2018.04.011.

**Bản đã đọc:** toàn văn, bản PDF của nhà xuất bản (12 tr. PDF = tr. 54–65; thân bài tr. 54–64). Số trang dưới đây là số
trang tạp chí. Đọc ngày 30/09/2026 (kiểm phản chứng UV-03) và hoàn thiện ở phiên T1-1. Các hình và listing chỉ đọc
qua văn bản mô tả và chú thích; chưa xem ảnh Hình 2, Hình 4, Listing 1 và Listing 4.

Ký hiệu: (a) điều tác giả nói; (b) giới hạn tác giả tự nêu; **[NCS]** nhận định của NCS.

| Cột | Nội dung |
|---|---|
| Citekey / Số cũ | 2ILY9YZ3 / [2] |
| Tier / Cụm | Tier 1 / Truy vết thông tin |
| Luận điểm | Lược đồ IFC mô tả được cảm biến đơn lẻ nhưng chưa mô tả đầy đủ một hệ quan trắc kết cấu; bài đề xuất phần mở rộng IFC Monitor (ba thực thể, một kiểu liệt kê) để mô tả hệ quan trắc cùng kết cấu được quan trắc trong một mô hình (tr. 55, 58). |
| Bằng chứng | Kiểm tra lược đồ bằng phần mềm thử của chương trình chứng nhận IFC (cú pháp, ngữ nghĩa, kiểm thử đơn vị; tr. 60–61, Bảng 1); mô hình hóa một hệ quan trắc mẫu trên khung nhôm bốn tầng trong phòng thí nghiệm (tr. 61–63). |
| Giới hạn | Xem mục 5. |
| Tác động K1/K2/K3 | K2: thu hẹp (đã có cách biểu diễn quan hệ cảm biến – cấu kiện trong IFC), đồng thời để lại phần thời hạn hiệu lực. K1, K3: không liên quan. |
| Vị trí sử dụng | 2.2 (khả năng và giới hạn của IFC với thông tin quan trắc); 4.x (ánh xạ cảm biến – cấu kiện); 5.5 (tiền lệ của thực thể cảm biến và ánh xạ); Phụ lục ánh xạ. |
| Mức đã đọc | Toàn văn |

## 1. Câu hỏi nghiên cứu và đối tượng

- Câu hỏi: làm thế nào để mô tả "thông tin liên quan đến quan trắc" (thành phần của hệ quan trắc, thuật toán nhúng trên
  nút, quan hệ với kết cấu) trên một nền hình thức, tương thích IFC (tr. 54–55).
- Đối tượng: **hệ quan trắc kết cấu** (mạng cảm biến không dây) và quan hệ của nó với kết cấu. Dữ liệu đo nằm ngoài phạm
  vi: tác giả coi dữ liệu cảm biến đã mô hình hóa, lưu và trao đổi được, còn mô tả hệ quan trắc thì mới ở bước đầu (tr. 54).
- Loại công trình trong kiểm chứng: khung cắt bốn tầng bằng nhôm trong phòng thí nghiệm (tr. 61–62).

## 2. Phương pháp và kiến trúc thông tin

- Rà khả năng của IFC4 (ISO 16739): `IfcRoot` cho mỗi thực thể định danh toàn cục, thông tin quyền sở hữu và thay đổi
  (tr. 55); quan hệ được "đối tượng hóa" (`IfcRelAggregates`, `IfcRelConnectsElements`, `IfcRelAssignsToProduct`,
  `IfcRelAssignsToGroup`, `IfcRelServicesBuildings`) (tr. 55–56). `IfcSensor` có 24 loại định sẵn, thiếu gia tốc kế và
  cảm biến biến dạng (tr. 57). Phần tử thay thế (proxy), kiểu đối tượng và bộ thuộc tính do người dùng đặt gây mơ hồ
  và mất ngữ nghĩa (tr. 56–57).
- Mô hình ngữ nghĩa của hệ quan trắc (tr. 57–58, Hình 2): hệ quan trắc gồm hệ máy tính và một hay nhiều mạng cảm biến;
  mạng gồm các nút (nút cảm biến, trạm gốc); mỗi nút có nguồn, bộ truyền thông, đặc tả vị trí – hình học và tham chiếu
  ngữ nghĩa tới cấu kiện của kết cấu; mạng có cấu trúc liên kết (topology).
- Phần mở rộng IFC Monitor (tr. 58–60, Hình 4, Listing 1): ba thực thể `IfcSensorNode`, `IfcSensorNetwork`,
  `IfcSHMSystem`, một kiểu liệt kê `IfcNetworkTopologyEnum`, thêm loại cảm biến cho quan trắc kết cấu. Định nghĩa bằng
  EXPRESS, có luật miền (where clause) giới hạn loại thành phần.
- Quan hệ cảm biến – kết cấu: nút cảm biến được một cấu kiện tham chiếu bằng `IfcRelAssignsToProduct`; mạng cảm biến nối
  với phần tử không gian (tầng) bằng `IfcRelServicesBuildings` (tr. 59, 63).
- Chuẩn được nhắc nhưng không dùng: SensorML, ontology SSN, IEEE 1451 (tr. 54).

## 3. Cách kiểm chứng

- Kiểm tra lược đồ (verification): ba bước cú pháp, ngữ nghĩa, kiểm thử đơn vị bằng phần mềm thử của chương trình chứng
  nhận IFC; ví dụ gán một bức tường vào hệ quan trắc để luật miền trả về sai như mong đợi (tr. 60–61, Bảng 1).
- Kiểm chứng mô hình (validation): một hệ mẫu gồm bốn nút cảm biến không dây, một trạm gốc, một máy tính, cấu trúc hình
  sao, trên khung nhôm bốn tầng; tệp trao đổi STEP được kiểm tra không lỗi cú pháp và đạt yêu cầu ngữ nghĩa (tr. 61–64,
  Bảng 2).
- Không có dữ liệu đo, không có chỉ số định lượng, không so sánh đường cơ sở. "Đúng" ở đây là đúng về lược đồ.

## 4. Luận điểm chính

1. IFC hiện hành mô tả được cảm biến đơn lẻ và một số thiết bị dùng chung, nhưng chưa đủ để mô tả hệ quan trắc một cách
   chính xác; dùng phần tử thay thế và thuộc tính tự đặt làm mất ngữ nghĩa và cản trở xử lý tự động (tr. 55–57).
2. Ba thực thể mới đủ để mô tả thành phần của hệ quan trắc, cấu trúc mạng và quan hệ ngữ nghĩa với kết cấu trong cùng
   một mô hình IFC (tr. 58–60, 64).
3. Phần mở rộng tuân thủ IFC: qua được kiểm tra của phần mềm chứng nhận, và mô hình hệ mẫu đạt các tiêu chí (tr. 61, 63–64).
4. Mô tả hình thức hệ quan trắc giúp việc theo dõi thay đổi và thay thế thành phần của hệ dễ hơn (tr. 55). Đây là mục
   tiêu được nêu; bài không trình bày cơ chế.

## 5. Giới hạn

**(b) Tác giả tự nêu:**
- Thông tin về truyền thông (giao thức) để cho công việc sau (tr. 64).
- Động lực học của hệ quan trắc chưa mô tả được đầy đủ bằng các cách mô hình hóa trên nền IFC hiện có (tr. 64).
- Thông tin cấu trúc mạng bị mô tả hai lần (kiểu liệt kê và từng kết nối); luật miền bảo đảm nhất quán mới ở dạng dự
  định (tr. 59).
- Cổng truyền thông qua đám mây nằm ngoài phạm vi (tr. 57).

**[NCS] nhận định:**
- Chỉ kiểm chứng tính đúng của lược đồ trên một hệ mẫu trong phòng thí nghiệm; chưa có công trình thực, chưa có người
  dùng, chưa có phần mềm BIM thương mại hỗ trợ (tác giả nói thông tin quan trắc phải nhập bằng phần mềm thử, tr. 62).
- Trạm gốc được mô hình bằng `IfcSensorNode` "để minh họa" (tr. 62), tức lược đồ chưa phân biệt hai loại nút.
- Không có thuộc tính thời gian ở thực thể mới và quan hệ dùng lại; mô hình là ảnh chụp tại một thời điểm.
- Không mô tả dữ liệu đo, kết quả phân tích hay người chịu trách nhiệm.

## 6. Điều bài KHÔNG xử lý, xét theo chuỗi của luận án

| Ý | Mức | Căn cứ |
|---|---|---|
| Nguồn gốc bằng chứng cảm biến | xử lý một phần | Mô tả được thành phần hệ đo (nút, cảm biến, mạng, máy tính) là nửa "thiết bị" của nguồn gốc (tr. 58–60); không có dữ liệu, thuật toán, phiên bản xử lý. Thuật toán nhúng được nêu như thông tin cần mô tả (tr. 55) nhưng không có thực thể |
| Phạm vi hiệu lực của bằng chứng | không xử lý | Không có khái niệm bằng chứng |
| Quan hệ bằng chứng – cấu kiện có thời hạn | xử lý một phần | Có quan hệ cảm biến – cấu kiện (tr. 59, 63); không có thời hạn hiệu lực; tác giả nêu động lực học của hệ là việc để lại (tr. 64) |
| Trách nhiệm, thẩm quyền | không xử lý | Chỉ nhắc `IfcRoot` mang thông tin quyền sở hữu (tr. 55) |
| Trạng thái hành động và lịch sử chuyển trạng thái | không xử lý | Không có |
| Truy ngược từ hành động về dữ liệu gốc | không xử lý | Không có |

## 7. Tác động tới K1/K2/K3

- **K2: thu hẹp.** Biểu diễn cảm biến, mạng cảm biến và quan hệ với cấu kiện trong IFC đã có tiền lệ hình thức (tr. 58–60, 63).
  Phần còn lại: thời hạn hiệu lực của quan hệ và bằng chứng sinh ra từ hệ đo. Căn cứ tác giả tự nêu ở tr. 64.
- **K1, K3: không liên quan** (bài không bàn kết quả phân tích hay hành động).

## 8. Vị trí sử dụng trong tiểu luận v2

- 2.2: giới hạn của IFC4 với thông tin quan trắc (tr. 55–57) và phần mở rộng IFC Monitor.
- 4.x và 5.5: tiền lệ của thực thể cảm biến và ánh xạ cảm biến – cấu kiện; nêu rõ phần thời hạn hiệu lực là phần bổ sung.
- Bảng ánh xạ: `mapping/theiler2018.md`.
