# Bảng ánh xạ: schema của luận án ↔ khung IFC cho kiểm tra – bảo trì (Bellon và cs. 2025, [35])

Lập ngày 01/10/2026, phiên T1-1. Nguồn: `notes/NUTL57KJ.md` (đọc toàn văn; số trang là trang in 1–19). Mức tương ứng:
**đủ** / **một phần** / **không có**. Mọi đánh giá mức là nhận định của NCS [NCS] dựa trên căn cứ ghi kèm.

Lưu ý đọc bảng: [35] biểu diễn **hư hỏng phát hiện bằng mắt** và **nhiệm vụ bảo trì có chi phí** trong tệp IFC 4.3, không
có cảm biến. "Đủ" nghĩa là khái niệm có cấu trúc tương ứng bằng thực thể IFC chuẩn.

## Phần A. Ánh xạ thực thể

| Thực thể schema | Khái niệm tương ứng trong bài | Mức | Căn cứ | Ghi chú |
|---|---|---|---|---|
| COMPONENT | Lớp con của `IfcElement`, chứa trong `IfcFacility` | đủ | tr. 4 | Định danh là GUID của IFC; tìm cấu kiện theo tên khi nhập dữ liệu (tr. 9) |
| MODEL_VERSION | `IfcOwnerHistory` mới cho mỗi lần sửa tệp | một phần | tr. 8–9 | Theo IFC, chỉ giữ lần sửa cuối (xem nhật ký UV-03, IFC4) |
| SENSOR | Không có | không có | — | IoT là việc sau (tr. 18) |
| SENSOR_MAPPING | Không có | không có | — | |
| OBS_CONTEXT | Lần kiểm tra (`IfcTask` INSPECTION) có ngày giờ, người kiểm tra, tài liệu | một phần | tr. 5, 8–9 | Bối cảnh của kiểm tra bằng mắt; không có cấu hình đo |
| EVIDENCE | Hư hỏng `IfcSurfaceFeature` DEFECT, loại ở `ObjectType`, số đo và trạng thái trong bộ thuộc tính | một phần | tr. 4–5, 9 | Chỉ loại quan sát; không có `value`/`uncertainty`/`method_version` theo nghĩa của schema |
| VALIDITY_SCOPE | Trạng thái `ACTIVE`/`OUTDATED` (bản mới thay bản cũ) | không có (tương tự xa) | tr. 9 | Hiệu lực theo thời gian, theo quy ước; không có điều kiện áp dụng |
| EVIDENCE_USE | Gán hư hỏng `ACTIVE` vào nhiệm vụ bảo trì cấp hư hỏng (`IfcRelAssignsToProcess`) | một phần | tr. 7, 9 | Có quan hệ dùng, không có lý do hay kiểm trong/ngoài phạm vi; việc chọn do quy ước tự động |
| INSPECTION_RECORD | Lần kiểm tra `IfcTask` INSPECTION; hư hỏng là sản phẩm của nó qua `IfcRelAssignsToProduct`; tài liệu qua `IfcRelAssociatesDocument` | đủ | tr. 5–7 | Cho kiểm tra bằng mắt |
| ACTION | Nhiệm vụ bảo trì ba cấp (`IfcTask` MAINTENANCE), khoản chi phí `IfcCostItem` | một phần | tr. 5–7 | Không có `priority_level`; không dùng `Status` của `IfcTask` |
| STATUS_EVENT | Không có. Có trạng thái hư hỏng `REPAIRED` gán theo quy ước sau bảo trì | không có | tr. 10 | Không có sự kiện, người, thời điểm, căn cứ của bước chuyển |
| AGENT | Người kiểm tra (`IfcPerson`, `IfcActor`, `IfcRelAssignsToActor`) | một phần | tr. 9 | Không có vai trò phê duyệt, không có thẩm quyền |

Tổng: 2 đủ, 6 một phần, 4 không có (tính VALIDITY_SCOPE là không có).

## Phần B. Ba câu hỏi của người quản lý

| Câu hỏi | Trả lời được? | Lý do |
|---|---|---|
| 1. Cái gì bất thường, ở đâu? | trả lời được (với hư hỏng phát hiện bằng mắt) | Hư hỏng có loại, số đo, gắn một cấu kiện, gắn lần kiểm tra (tr. 5, 7, Bảng 2) |
| 2. Tin được đến mức nào? | không | Không có độ bất định, phương pháp, phạm vi; chỉ biết ai kiểm và khi nào (tr. 9) |
| 3. Ai đã xử lý, dựa vào đâu? | một phần | Biết nhiệm vụ bảo trì nào sửa hư hỏng nào, chi phí bao nhiêu (tr. 7, 17); không biết ai quyết định, ai xác nhận đã sửa |

## Phần C. Kịch bản cột trục C3

| Bước | Trong khung của [35] |
|---|---|
| Cảm biến ghi nhận bất thường | **Chuỗi gãy ngay bước đầu**: không có cảm biến |
| Tạo bằng chứng gắn cột C3 | Có, nếu phát hiện bằng mắt: hư hỏng gắn cột qua `IfcRelAdheresToElement` (tr. 5) |
| Kỹ sư A kiểm tra, xác nhận bu lông lỏng | Có một phần: lần kiểm tra có người kiểm tra; hư hỏng là sản phẩm của lần kiểm tra (tr. 7, 9) |
| Trưởng phòng B phê duyệt siết lại | Không có: không có phê duyệt; hư hỏng được đưa vào bảo trì theo quy ước tự động (tr. 9) |
| Hành động đóng | Một phần: hư hỏng chuyển `REPAIRED` khi có lần bảo trì, không có kiểm tra xác minh (tr. 10) |
| Sáu tháng sau truy ngược | Có một phần: từ nhiệm vụ bảo trì lần về hư hỏng, lần kiểm tra, tài liệu, chi phí (tr. 17, Hình 20); không có ai quyết định và căn cứ của quyết định |

## Phần D. Kết luận ánh xạ [NCS]

Điểm chung: cả hai coi lần kiểm tra là nơi tạo ra nhận định tình trạng gắn cấu kiện, và nối nhận định đó tới hành động
bảo trì bằng quan hệ định kiểu. Với phát hiện bằng mắt, [35] là **ràng buộc IFC có sẵn** cho phần INSPECTION_RECORD →
EVIDENCE → ACTION của schema. Schema có mà bài không có: bằng chứng cảm biến và NDT, độ bất định và phạm vi hiệu lực,
sự kiện chuyển trạng thái của hành động, phê duyệt và thẩm quyền, kiểm tra xác minh sau sửa. Điểm cần xử lý khi viết 5.5:

1. **Dùng lại ràng buộc IFC của [35]** cho bằng chứng loại quan sát: lần kiểm tra → bằng chứng bằng
   `IfcRelAssignsToProduct`, bằng chứng → cấu kiện bằng `IfcRelAdheresToElement`, bằng chứng → hành động bằng
   `IfcRelAssignsToProcess`. Nêu [35] như tiền lệ, không trình bày như đóng góp.
2. **Bản số khác nhau:** schema để EVIDENCE n:m COMPONENT, còn `IfcRelAdheresToElement` chỉ cho một cấu kiện mỗi bản ghi
   (tr. 5). Khi ánh xạ sang IFC cần chọn: chia bằng chứng theo cấu kiện như [35], hoặc giữ quan hệ n:m ở tầng đồ thị và
   chỉ xuất IFC theo từng cấu kiện. Đây là quyết định của NCS khi viết 5.5.
3. **Định danh bền của bằng chứng:** [35] nhận ra "cùng một hư hỏng" qua tên (tr. 12). Schema đã có
   `Condition_Evidence_ID`; nên ghi rõ quan hệ "bản ghi mới thay bản ghi cũ" (tương ứng `OUTDATED`) là một quan hệ giữa hai
   EVIDENCE, không phải ghi đè thuộc tính.
4. **Xác minh sau sửa:** giả định "có bảo trì thì đã sửa" (tr. 10) là điều trạng thái "đã xác minh" của trục trạng thái xử
   lý và ràng buộc C6–C7 nhằm tránh; có thể dùng làm ví dụ đối chiếu ở 4.5.4.
5. **Khả năng hiển thị:** tệp hợp lệ lược đồ vẫn bị đa số phần mềm bỏ qua phần quá trình và chi phí (tr. 17–18). Nếu
   luận án xuất IFC, chỉ số kiểm chứng nên đo trên bộ công cụ truy vấn của luận án (ví dụ IfcOpenShell), không dựa vào
   phần mềm xem.

## Phần E. So với [2], [44] và BCF 3.0

| Phần của chuỗi | [35] Bellon 2025 | [44] García 2026 | BCF 3.0 | [2] IFC Monitor |
|---|---|---|---|---|
| Đối tượng mang trạng thái | Hư hỏng (quy ước ACTIVE/OUTDATED/REPAIRED) | Tệp IFC theo phiên bản | Vấn đề (Topic) | không |
| Gắn với cấu kiện | có (`IfcRelAdheresToElement`, một cấu kiện) | gián tiếp (FU) | có, qua góc nhìn | có (cảm biến ↔ cấu kiện) |
| Lần kiểm tra → phát hiện | có (`IfcRelAssignsToProduct`) | có, cho kiểm tra mô hình | không | không |
| Phát hiện → hành động | có (`IfcRelAssignsToProcess`) | có (NCR/BCF ↔ quyết định) | không định kiểu | không |
| Căn cứ của bước chuyển | không | có | không | không |
| Lịch sử đổi trạng thái | không (bản ghi mới thay bản cũ) | có | có (BCF-API) | không |
| Vai trò và thẩm quyền | chỉ người kiểm tra | có, theo vai trò | quyền thao tác | không |
| Cảm biến, bằng chứng có phạm vi | không | không | không | chỉ cảm biến |

[35] cho đoạn mà ba nguồn kia thiếu: chuỗi định kiểu kiểm tra → phát hiện → cấu kiện → nhiệm vụ bảo trì → chi phí bằng
thực thể IFC chuẩn. [44] cho căn cứ và thẩm quyền của bước chuyển, BCF cho lịch sử trạng thái của vấn đề, [2] cho hệ đo.
Ghép bốn nguồn vẫn thiếu: bằng chứng từ cảm biến hoặc NDT có nguồn gốc và phạm vi hiệu lực đi vào cùng chuỗi đó, và sự
kiện chuyển trạng thái của hành động có căn cứ trỏ về bản ghi sử dụng bằng chứng.
