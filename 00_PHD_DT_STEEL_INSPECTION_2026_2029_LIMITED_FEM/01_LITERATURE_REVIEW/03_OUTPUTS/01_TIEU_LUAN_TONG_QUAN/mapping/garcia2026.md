# Bảng ánh xạ: schema của luận án ↔ khung cổng chất lượng trong CDE (García và cs. 2026, [44])

Lập ngày 30/09/2026, phiên T1-1. Nguồn: `notes/GNTQNBWM.md` (đọc toàn văn thân bài; số trang là trang PDF 1–45). Mức tương
ứng: **đủ** / **một phần** / **không có**. Mọi đánh giá mức là nhận định của NCS [NCS] dựa trên căn cứ ghi kèm.

Lưu ý đọc bảng: đối tượng được quản trị trong [44] là **tệp IFC bàn giao**, còn trong schema là **tình trạng cấu kiện**.
"Đủ" ở đây nghĩa là khái niệm có đủ cấu trúc tương ứng, áp cho đối tượng của bài.

## Phần A. Ánh xạ thực thể

| Thực thể schema | Khái niệm tương ứng trong bài | Mức | Căn cứ | Ghi chú |
|---|---|---|---|---|
| COMPONENT | Phần tử IFC mang Đơn vị chức năng (FU) và vị trí kỹ thuật | một phần | tr. 14, 20 | Đơn vị quản trị là tệp, không phải cấu kiện |
| MODEL_VERSION | Gói (container) theo phiên bản, ngày, mã băm | đủ | tr. 17–18, 20 | Chặt hơn schema: có mã băm của tệp |
| SENSOR | Không có | không có | — | |
| SENSOR_MAPPING | Không có | không có | — | |
| OBS_CONTEXT | Không có. Có siêu dữ liệu ngữ cảnh của tệp (giai đoạn, trạng thái, phần mềm xuất) | không có | tr. 17–18 | Tương tự về vai trò, khác đối tượng |
| EVIDENCE | Gói bằng chứng: báo cáo mức tệp, tóm tắt gói, bản ghi quyết định, tham chiếu NCR/BCF | một phần | tr. 3, 19–21 | Là bằng chứng về chất lượng thông tin, không phải về tình trạng công trình |
| VALIDITY_SCOPE | Bảng đối chiếu theo thời gian: đường cơ sở yêu cầu áp cho từng kỳ; ngưỡng có thể tham số hóa | một phần | tr. 17, 25–27 | Tương tự về ý: điều kiện mà trong đó một quyết định còn so sánh được |
| EVIDENCE_USE | Bản ghi quyết định tham chiếu tường minh tới bằng chứng và vai trò | một phần | tr. 19, 21 | Không có khái niệm "dùng trong hay ngoài phạm vi" |
| INSPECTION_RECORD | Báo cáo kiểm tra mức tệp theo ba nhóm | một phần | tr. 15–17, 20 | Là kiểm tra mô hình, không phải kiểm tra hiện trường |
| ACTION | Vấn đề NCR/BCF: mã, tệp và phiên bản, bộ môn/FU, mô tả, người chịu trách nhiệm, trạng thái, ngày | một phần | tr. 20, 22 | Hành động sửa thông tin; có vòng đóng và xác minh lại |
| STATUS_EVENT | Bước Shared → Published như "sự kiện được quản trị", có bản ghi quyết định công bố/giữ lại | đủ | tr. 3, 10, 19, 24 | Cho trạng thái của thông tin |
| AGENT | Vai trò theo giai đoạn, ma trận RACI, tách nhiệm vụ, hai cấp ký | đủ | tr. 21–25, Bảng 7 | Chặt hơn schema ở nguyên tắc tách nhiệm vụ |

Tổng: 3 đủ, 6 một phần, 3 không có.

## Phần B. Ba câu hỏi của người quản lý

| Câu hỏi | Trả lời được? | Lý do |
|---|---|---|
| 1. Cái gì bất thường, ở đâu? | không (với tình trạng công trình) | "Bất thường" trong bài là tệp không đạt cổng; vị trí là tệp, bộ môn, FU (tr. 20). Không có bất thường của cấu kiện |
| 2. Tin được đến mức nào? | một phần | Biết tệp đã qua những kiểm tra nào, theo đường cơ sở yêu cầu nào, ngưỡng nào (tr. 16–17, 26). Không có độ bất định |
| 3. Ai đã xử lý, dựa vào đâu? | trả lời được (với quyết định công bố) | Bản ghi quyết định, vai trò ký, gói bằng chứng, lịch sử vấn đề (tr. 21, 24, 33) |

## Phần C. Kịch bản cột trục C3

| Bước | Trong khung của [44] |
|---|---|
| Cảm biến ghi nhận bất thường | **Chuỗi gãy ngay bước đầu**: không có cảm biến hay dữ liệu vận hành |
| Tạo bằng chứng gắn cột C3 | Không có bằng chứng tình trạng; không gắn bằng chứng với cấu kiện |
| Kỹ sư A kiểm tra | Có khuôn tương tự: người điều phối chạy kiểm tra, lập báo cáo (tr. 22) |
| Trưởng phòng B phê duyệt | Có khuôn tương tự: ký kỹ thuật rồi phê duyệt hợp đồng, tách nhiệm vụ (tr. 24) |
| Hành động đóng | Có khuôn tương tự: vấn đề được đóng sau khi chạy lại cổng (tr. 22) |
| Sáu tháng sau truy ngược | Có khuôn tương tự: tái dựng cái gì được công bố, khi nào, ai, bằng chứng nào (tr. 21, 33) |

Nếu thay "tệp IFC" bằng "bằng chứng tình trạng" thì bốn bước sau của kịch bản chạy được theo khuôn của bài; hai bước đầu
bài không có.

## Phần D. Kết luận ánh xạ [NCS]

Điểm chung: cả hai coi bước chuyển trạng thái là sự kiện phải có bằng chứng lưu giữ, đúng vai trò và tái dựng được; ràng
buộc "bước chuyển có căn cứ và đúng thẩm quyền" của schema vì vậy có tiền lệ trực tiếp ở [44], cho gói thông tin. Schema
có mà bài không có: cảm biến và ánh xạ có thời hạn, bằng chứng về tình trạng cấu kiện, phạm vi hiệu lực của bằng chứng,
và việc gắn mọi thứ vào cấu kiện thay vì vào tệp. Bài có mà schema chưa có, **đề xuất xem xét bổ sung**:

1. **Tách nhiệm vụ** như một ràng buộc: người tạo bằng chứng, người kiểm tra và người phê duyệt là các tác nhân khác
   nhau (tr. 23). Có thể thêm vào ràng buộc về thẩm quyền của bước chuyển.
2. **Phiên bản của bộ luật quyết định**: logic bốn mức ưu tiên và các ngưỡng cần có phiên bản, ngày, người lập, và
   không viết lại quyết định cũ khi luật đổi (ý "đóng băng" của bảng đối chiếu, tr. 26). Có thể thêm một trường phiên
   bản luật vào sự kiện chuyển trạng thái.
3. **Mã băm** của tệp dữ liệu hoặc mô hình mà bằng chứng dựa vào (tr. 18, 20), để định danh chính xác đối tượng đã kiểm.
4. **Trạng thái "giữ lại" kèm vòng xác minh lại** (tr. 22): đã có tương ứng ở trạng thái "đã xác minh" của trạng thái
   xử lý; nên ghi rõ xác minh là một lần kiểm tra mới, tạo bản ghi riêng.

## Phần E. So với BCF 3.0 và [2]

| Phần của chuỗi | [44] García 2026 | BCF 3.0 | [2] IFC Monitor |
|---|---|---|---|
| Đối tượng mang trạng thái | Tệp IFC theo phiên bản | Vấn đề (Topic) | không |
| Gắn với cấu kiện | gián tiếp (FU ở phần tử) | có, qua góc nhìn và `IfcGuid` | có (cảm biến ↔ cấu kiện) |
| Căn cứ của bước chuyển | có: gói bằng chứng, bản ghi quyết định | không (sự kiện chỉ ghi loại và giá trị) | không |
| Lịch sử đổi trạng thái | có | có (BCF-API) | không |
| Vai trò và thẩm quyền | có, theo vai trò chuyên môn | quyền thao tác theo người dùng | không |
| Cảm biến, bằng chứng tình trạng | không | không | chỉ cảm biến |

[44] dùng BCF làm phương tiện ghi vấn đề và thêm đúng phần BCF thiếu: căn cứ và thẩm quyền của bước chuyển. [2] cho phần
cả hai không có: hệ đo và quan hệ với cấu kiện. Ghép ba nguồn vẫn thiếu bằng chứng tình trạng có phạm vi hiệu lực và
quan hệ định kiểu từ hành động về bằng chứng đó.
