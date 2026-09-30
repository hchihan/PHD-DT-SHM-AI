# 5QX5LTMZ — Lu, Xie, Parlikad & Schooling (2020) — [3]

Lu Q, Xie X, Parlikad AK, Schooling JM. Digital twin-enabled anomaly detection for built asset monitoring in
operation and maintenance. *Automation in Construction* 118: 103277. DOI 10.1016/j.autcon.2020.103277.

**Bản đã đọc:** toàn văn, bản PDF của nhà xuất bản (16 tr. PDF; thân bài tr. 1–15, tiếp theo là tài liệu tham
khảo). Số trang dưới đây là số trang in của bài. Đã xem trực tiếp Hình 4 (tr. 6) và Hình 18 (tr. 14) vì văn bản
trích không cho thấy nội dung hình. Đọc ngày 30/09/2026, phiên T1-3.

Ký hiệu: (a) điều tác giả nói; (b) giới hạn tác giả tự nêu; **[NCS]** nhận định của NCS.

| Cột | Nội dung |
|---|---|
| Citekey / Số cũ | 5QX5LTMZ / [3] |
| Tier / Cụm | Tier 1 / Song sinh số |
| Luận điểm | Phát hiện bất thường cho tài sản tòa nhà trong vận hành và bảo trì (O&M) có thể được tổ chức trên song sinh số nếu dùng cấu trúc dữ liệu mở rộng từ IFC, nối đối tượng BIM với các hệ thống dữ liệu phân tán; phát hiện điểm thay đổi theo Bayes (BOCPD) kết hợp đối chiếu với nhật ký vận hành để lọc báo động giả (tr. 1, 4–6, 13–14). |
| Bằng chứng | Một ca nghiên cứu: hai bơm ly tâm trong hệ HVAC của tòa nhà IfM (Đại học Cambridge); so sánh BOCPD với biểu đồ CUSUM trên hai bộ dữ liệu tần số dao động (tr. 9–12). |
| Giới hạn | Xem mục 5. |
| Tác động K1/K2/K3 | K2: thu hẹp một phần (đã có bảng ghép GUID – ID nguồn dữ liệu). K3: mở rộng (chuỗi dừng ở cảnh báo và hỗ trợ quyết định). K1: mở rộng yếu (đối chiếu ngữ cảnh vận hành để lọc báo động giả, không khai báo phạm vi). Chi tiết ở mục 7. |
| Vị trí sử dụng | 2.2.2 và 5.1.3 (nối dữ liệu vận hành với đối tượng IFC); 2.3 (ví dụ song sinh số cho O&M); 3.2/3.6 (bối cảnh vận hành thay đổi làm nhiễu phát hiện bất thường; thiếu dữ liệu có nhãn); 4.5 (thực thể kiểm tra – bảo trì mở rộng IFC). |
| Mức đã đọc | Toàn văn |

## 1. Câu hỏi nghiên cứu và đối tượng

- Câu hỏi: thiếu chiến lược tích hợp để giám sát, phát hiện, ghi lại và truyền thông các vấn đề O&M; làm thế nào để
  (i) tích hợp dữ liệu O&M phân tán qua IFC mở rộng và (ii) phát hiện bất thường của tài sản khi tải vận hành thay đổi
  (tr. 1–2).
- Đối tượng: **tài sản cơ điện – HVAC** (bơm ly tâm) của một tòa nhà giảng dạy, văn phòng và phòng thí nghiệm, 3
  tầng, hơn 40.000 ft² (tr. 9). **Không phải kết cấu chịu lực.** Tác giả nêu rõ phạm vi tài sản là thiết bị dịch vụ
  của tòa nhà (tr. 2, 6).
- Dữ liệu: tần số dao động trung bình theo giờ từ cảm biến gắn vỏ bơm gần ổ trục, kèm cờ vận hành từ BMS (tr. 10–11).

## 2. Phương pháp và kiến trúc thông tin

- **Kiến trúc DT năm lớp** (thu thập dữ liệu, truyền, mô hình số, tích hợp dữ liệu/mô hình, dịch vụ) (tr. 4).
- **IFC mở rộng cho O&M** (tr. 4–6, Hình 6): tác giả đối chiếu yêu cầu thông tin O&M với IFC4 và COBie 2.4 (Bảng 1,
  tr. 5, 7–8), chỉ ra IFC4 thiếu thực thể riêng cho hoạt động O&M, `IfcRoleEnum` chỉ có một vai trò FM (người quản lý
  cơ sở vật chất), `IfcOwnerHistory` và `IfcPerformanceHistory` không đủ để ghi lịch sử tài sản, và
  `IfcChangeActionEnum` không có giá trị cho FM (tr. 5). Đề xuất mở rộng `IfcProcess`, `IfcControl` thành các lớp con
  cho vận hành – bảo trì và mở rộng `IfcAsset` bằng ba thực thể `IfcMaintenanceHistory`, `IfcInspectionHistory`,
  `IfcSpareRecord` (tr. 6, Hình 6).
- **Tích hợp phân tán bằng bảng ghép** (tr. 6, 10, Hình 7, 11): IFC là mô hình trung tâm; các nguồn khác (AMS, BMS,
  hệ cảm biến) giữ nguyên nơi lưu; một **bảng ghép** liên kết GUID của đối tượng BIM với ID của bản ghi trong từng
  nguồn. Chỉ bảng ghép cần bảo trì (thao tác CRUD) (tr. 10).
- Hệ thống cảm biến ghi các trường Sensor_ID, Gateway_ID, Location_ID, Asset_ID, Sensor_Timestamp, Unit, Value
  (Hình 3, tr. 5).
- **Quy trình phát hiện** (tr. 6, Hình 4, Hình 8): (1) phát hiện điểm thay đổi bằng BOCPD, tính phân bố hậu nghiệm của
  độ dài chuỗi, không cần ngưỡng đặt trước (tr. 6–8); (2) nhận diện bất thường bằng **đối chiếu chéo** với nhật ký
  vận hành của BMS: điểm thay đổi nằm gần thời điểm biến đổi vận hành đã ghi là phản ứng bình thường; điểm thay đổi
  "không có ai nhận" được coi là bất thường nghi ngờ (tr. 6).
- Không dùng chuẩn SOSA/SSN, PROV-O, ISO 19650 hoặc SHACL; ràng buộc kiểm tra dữ liệu không được nêu.

## 3. Cách kiểm chứng

- **Dữ liệu thật, một công trình, hai bơm** (tr. 9–12). Trường hợp 1: bơm 1 ngừng theo lịch nghỉ lễ, dữ liệu 4 tuần
  (5/12/2018 – 1/1/2019). Trường hợp 2: dữ liệu **ghép nhân tạo** từ 14 ngày của bơm bình thường và 14 ngày của bơm
  bất thường (9–22/7/2018); bơm bất thường được mô tả là phát tiếng ồn mạnh (tr. 11).
- Đường cơ sở duy nhất: CUSUM. Kết quả **định tính** trên hình: CUSUM tạo hai báo động giả ở trường hợp 1 (tr. 11) và
  phát hiện chậm gần một tuần ở trường hợp 2 (tr. 12); BOCPD tránh báo động giả và định vị thời điểm thay đổi chính xác
  hơn, dù có chậm nhận biết (tr. 11–12). Không có bảng chỉ số, không có độ nhạy hay tỷ lệ báo động giả định lượng,
  không có kiểm tra hiện trường sau cảnh báo.
- Tính được thực hiện của phần IFC được minh họa bằng ứng dụng tạo tệp IFC mới và bảng ghép (tr. 10); không có chỉ số
  đánh giá tích hợp.

## 4. Luận điểm chính

1. IFC4 chưa có thực thể riêng cho hoạt động và lịch sử O&M; cần mở rộng lớp quá trình/điều khiển và tài sản (tr. 4–6).
2. Tích hợp phân tán bằng bảng ghép GUID – ID cho phép IFC và các hệ khác cập nhật độc lập mà vẫn liên kết (tr. 6, 10).
3. Phát hiện bất thường theo ngữ cảnh: phân biệt được điểm thay đổi do biến đổi vận hành đã ghi với bất thường thật
   bằng cách đối chiếu với nhật ký vận hành, nhờ đó giảm báo động giả (tr. 6, 13–14).
4. Với tài sản chạy dưới tải thay đổi và ít dữ liệu có nhãn, phát hiện điểm bất thường tĩnh không phân biệt được hành
   vi bình thường và bất thường; huấn luyện bộ phân loại một lớp cần dữ liệu lớn ở nhiều điều kiện bình thường và
   tác giả coi là không thực tế (tr. 2–3, 13).
5. Vì hạn chế ngân sách, chỉ giám sát tài sản quan trọng; tài sản không quan trọng được theo dõi gián tiếp qua chất
   lượng dịch vụ (tr. 14).

### Chuỗi từ phát hiện bất thường đến hành động bảo trì dừng ở đâu

- Quy trình DT (Hình 4, tr. 6, cột phải): xác nhận hiệu năng bất thường → tình trạng khiếm khuyết → **thủ tục tự động**
  (truy vấn thông tin, phân tích, xác nhận nguyên nhân) → báo cáo → sửa chữa. Hình kết thúc ở "sửa chữa"; không có
  trạng thái hành động hay chuyển trạng thái.
- Mục đích cuối của nền tảng là **trực quan hóa và hỗ trợ quyết định cho người làm FM** (tr. 13). Nền tảng "kích hoạt
  cảnh báo" khi thủ tục phát hiện hành vi bất thường (tr. 13); Hình 18 (tr. 14) cho thấy giao diện: mô hình BIM, chọn
  đối tượng (bơm), biểu đồ điểm thay đổi với chấm đỏ tại thời điểm phát hiện. Không có nút hay bản ghi cho việc ai
  xử lý.
- **Ai ra quyết định:** người quản lý FM. Trong quy trình truyền thống, người quản lý FM là điều phối trung tâm và
  quyết định dựa trên thông tin và kinh nghiệm chuyên gia (tr. 4). Trong quy trình DT, quyết định của người không có
  bước riêng ở Hình 4.
- **Cảnh báo có được lưu cùng căn cứ không:** bài không mô tả. Dữ liệu thô có Sensor_ID, Gateway_ID, Sensor_Timestamp
  (Hình 3, tr. 5). Đầu ra của phát hiện (điểm thay đổi, cảnh báo) không được mô tả như một bản ghi với phiên bản thuật
  toán, độ bất định hay phạm vi. Các thực thể `IfcInspectionHistory` và `IfcMaintenanceHistory` được đề xuất (tr. 6)
  nhưng ca nghiên cứu không cho thấy chúng được điền hoặc nối với cảnh báo.
- Trạng thái thực hiện trong bài: **phát hiện → đối chiếu ngữ cảnh → cảnh báo hiển thị**. Dừng ở đây.

## 5. Giới hạn

**(b) Tác giả tự nêu:**
- Vì ngân sách, không thể giám sát mọi tài sản ở độ chi tiết mịn; chỉ tài sản quan trọng có dữ liệu cảm biến/BMS;
  tài sản không quan trọng không có dữ liệu gắn với đối tượng (tr. 14).
- Bộ phân loại một lớp/không giám sát cần dữ liệu lớn ở nhiều điều kiện bình thường nên không thực tế; vì vậy
  chọn hướng phát hiện điểm thay đổi (tr. 13–14).
- Việc đối chiếu chéo được làm đơn giản ("khá trực quan"), bài tập trung vào thuật toán phát hiện điểm thay đổi
  (tr. 6).
- Công việc tương lai: tích hợp kinh nghiệm chuyên gia, mở rộng sang tài sản đô thị và ứng dụng rộng hơn (tr. 15).

**[NCS] nhận định:**
- Đối tượng là bơm HVAC; đặc tính dao động, điều kiện vận hành (tải theo nhu cầu người dùng) và loại hỏng hóc khác
  kết cấu thép nhà công nghiệp. Không dùng làm căn cứ cho nhà xưởng thép.
- Trường hợp 2 dùng dữ liệu ghép nhân tạo từ hai máy khác nhau; chưa thấy mô tả cách xác nhận chẩn đoán "bất thường".
- Không có chỉ số định lượng; so sánh chỉ với CUSUM.
- Bảng ghép GUID – ID không có thời hạn hiệu lực; bài không nói khi cảm biến được thay, dời hay hiệu chuẩn lại thì
  liên kết cũ được xử lý thế nào.
- Ý "điểm thay đổi không được nhật ký vận hành giải thích là bất thường" cần nhật ký vận hành đầy đủ; nếu nhật ký
  thiếu hoặc lệch giờ thì điểm thay đổi bình thường cũng bị coi là bất thường.

## 6. Điều bài KHÔNG xử lý, xét theo chuỗi của luận án

| Ý | Mức | Căn cứ |
|---|---|---|
| Nguồn gốc bằng chứng cảm biến | xử lý một phần | Dữ liệu thô có định danh cảm biến, cổng, vị trí, thời điểm (Hình 3, tr. 5), và ghép với đối tượng BIM (tr. 10); đầu ra phát hiện không có phiên bản phương pháp, tham số hay người/quy trình tạo ra (tr. 13–14) |
| Phạm vi hiệu lực của bằng chứng | xử lý một phần (**[NCS]**, yếu) | Đối chiếu với điều kiện vận hành đã ghi để lọc điểm thay đổi (tr. 6, 13–14) là một dạng xử lý ngữ cảnh; cảnh báo không được khai báo phạm vi hay điều kiện áp dụng |
| Quan hệ bằng chứng – cấu kiện có thời hạn | xử lý một phần | Bảng ghép GUID ↔ ID cảm biến/BMS (tr. 6, 10, Hình 7, 11); không có thời hạn hiệu lực hay lịch sử thay đổi ghép |
| Trách nhiệm, thẩm quyền | xử lý một phần | Nêu IFC4 thiếu vai trò O&M (tr. 5), người quản lý FM là người quyết định (tr. 4, 13); không đề xuất mô hình thẩm quyền |
| Trạng thái hành động và lịch sử chuyển trạng thái | xử lý một phần | Đề xuất `IfcMaintenanceHistory`, `IfcInspectionHistory` (tr. 6, Hình 6) và chỉ ra thiếu giá trị trong `IfcChangeActionEnum` (tr. 5); không có trạng thái hay chuyển trạng thái |
| Truy ngược từ hành động về dữ liệu gốc | không xử lý | Hình 4 kết thúc ở báo cáo – sửa chữa (tr. 6); Hình 18 chỉ hiển thị cảnh báo (tr. 14) |

## 7. Tác động tới K1/K2/K3

- **K2 (truy vết cấp cấu kiện): thu hẹp một phần.** Bảng ghép GUID – ID và mô hình trung tâm IFC với nguồn phân tán
  (tr. 6, 10) là tiền lệ cụ thể cho việc gắn dữ liệu cảm biến với cấu kiện. Phần chưa có: thời hạn hiệu lực của ghép,
  bảo toàn thuộc tính chất lượng của bằng chứng khi đi qua các nguồn. Đối tượng là thiết bị MEP, không phải kết cấu.
- **K3 (từ bằng chứng đến hành động): mở rộng.** Chuỗi dừng ở cảnh báo và hỗ trợ quyết định; thực thể lịch sử kiểm
  tra – bảo trì được đề xuất nhưng chưa nối với cảnh báo, không có trạng thái xử lý (tr. 6, 13–14).
- **K1 (phạm vi hiệu lực): mở rộng yếu.** Có xử lý ngữ cảnh vận hành để giảm báo động giả (tr. 6, 13); không có khái
  niệm phạm vi hiệu lực hay bản ghi bằng chứng.
- **Ghi chú cho mục 3.2, 5.6A (NCS):** bài cho căn cứ cùng chiều rằng dữ liệu có nhãn hư hỏng khó có ở tòa nhà đang
  vận hành và việc phân biệt bình thường – bất thường phụ thuộc nhiều vào đánh giá của con người (tr. 2–3); nhưng
  đối tượng là bơm HVAC.

## 8. Vị trí sử dụng trong tiểu luận v2

- 2.2.2/5.1.3: tiền lệ nối dữ liệu vận hành với đối tượng IFC bằng bảng ghép GUID – ID; nhu cầu mở rộng IFC cho lịch
  sử kiểm tra – bảo trì và vai trò FM (tr. 4–6).
- 2.3: ví dụ song sinh số cho O&M dừng ở mức phát hiện – cảnh báo – hỗ trợ quyết định.
- 3.2/3.6: căn cứ về tải vận hành thay đổi làm nhiễu bất thường và thiếu dữ liệu có nhãn, ghi rõ đối tượng là bơm HVAC.
- Không trích cho kết luận về nhà công nghiệp khung thép; không dùng chỉ số hiệu năng của BOCPD.
