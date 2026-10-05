# Bảng ánh xạ: schema của luận án ↔ IFC Monitor (Theiler & Smarsly 2018, [2])

Lập ngày 30/09/2026, phiên T1-1. Nguồn: `notes/2ILY9YZ3.md` (đọc toàn văn; số trang là trang tạp chí 54–65). Mức tương
ứng: **đủ** / **một phần** / **không có**. Mọi đánh giá mức là nhận định của NCS [NCS] dựa trên căn cứ ghi kèm.

## Phần A. Ánh xạ thực thể

| Thực thể schema | Khái niệm tương ứng trong bài | Mức | Căn cứ | Ghi chú |
|---|---|---|---|---|
| COMPONENT | Cấu kiện kết cấu (`IfcElement` và lớp con), có định danh toàn cục từ `IfcRoot` | đủ | tr. 55–56, 63 | Dùng nguyên IFC |
| MODEL_VERSION | Không có. `IfcRoot` mang "thông tin thay đổi" nói chung | không có | tr. 55 | Mô hình là ảnh chụp một thời điểm |
| SENSOR | `IfcSensor` (thêm loại gia tốc kế, cảm biến biến dạng), `IfcSensorNode` | đủ | tr. 57, 59 | Chi tiết hơn schema: nút gồm cảm biến, nguồn, bộ truyền thông |
| SENSOR_MAPPING | `IfcRelAssignsToProduct` (nút ↔ cấu kiện), `IfcRelServicesBuildings` (mạng ↔ tầng) | một phần | tr. 59, 63 | Không có thời hạn hiệu lực, không có tham chiếu biên bản lắp đặt |
| OBS_CONTEXT | `IfcSensorNetwork` (cấu trúc mạng), `IfcSHMSystem` | một phần | tr. 58–60 | Có cấu hình hệ đo; không có đợt đo, điều kiện đo |
| EVIDENCE | Không có. Dữ liệu cảm biến được coi là lưu ở nguồn ngoài | không có | tr. 54–55 | |
| VALIDITY_SCOPE | Không có | không có | — | |
| EVIDENCE_USE | Không có | không có | — | |
| INSPECTION_RECORD | Không có | không có | — | |
| ACTION | Không có | không có | — | |
| STATUS_EVENT | Không có | không có | — | |
| AGENT | Không có (chỉ nhắc thông tin quyền sở hữu của `IfcRoot`) | không có | tr. 55 | |

Tổng: 2 đủ, 2 một phần, 8 không có.

## Phần B. Ba câu hỏi của người quản lý

| Câu hỏi | Trả lời được? | Lý do |
|---|---|---|
| 1. Cái gì bất thường, ở đâu? | một phần | Biết cảm biến nào gắn với cấu kiện nào, thuộc mạng nào (tr. 59, 63). Không có bản ghi "bất thường" nào để hỏi |
| 2. Tin được đến mức nào? | không | Không có kết quả phân tích, độ bất định hay phạm vi |
| 3. Ai đã xử lý, dựa vào đâu? | không | Không có hồ sơ kiểm tra, hành động, vai trò |

## Phần C. Kịch bản cột trục C3

| Bước | Trong IFC Monitor |
|---|---|
| Cảm biến ghi nhận bất thường | Biểu diễn được cảm biến và nút trên cột C3; không biểu diễn được phép đo hay bất thường |
| Tạo bằng chứng gắn cột C3 | **Chuỗi gãy ở đây**: không có thực thể cho kết quả phân tích |
| Kỹ sư A kiểm tra | Không có |
| Trưởng phòng B phê duyệt | Không có |
| Hành động đóng | Không có |
| Sáu tháng sau truy ngược | Chỉ truy được "cảm biến nào đang gắn ở C3 theo mô hình hiện tại"; nếu cảm biến đã được dời, mô hình không cho biết lúc xảy ra sự cố nó ở đâu |

## Phần D. Kết luận ánh xạ [NCS]

IFC Monitor và schema của luận án trùng nhau ở ba thực thể đầu chuỗi: cấu kiện, cảm biến, và quan hệ giữa chúng, đều
trên nền IFC. Schema có thêm toàn bộ phần sau phép đo (bằng chứng, phạm vi hiệu lực, kiểm tra, hành động, sự kiện chuyển
trạng thái, tác nhân) và thời hạn hiệu lực của ánh xạ; bài không có các phần này và tự nêu động lực học của hệ quan
trắc là việc để lại (tr. 64). Bài có một phần mà schema chưa có: cấu tạo của hệ đo (nút gồm cảm biến, nguồn, bộ truyền
thông; mạng và cấu trúc liên kết; hệ máy tính). **Đề xuất xem xét:** không thêm thực thể mới; cho trường cấu hình cảm
biến của bối cảnh quan trắc tham chiếu tới mô tả mạng kiểu IFC Monitor, và ghi [2] là tiền lệ của SENSOR và SENSOR_MAPPING ở 5.5.

## Phần E. So với BCF 3.0 và [44]

| Phần của chuỗi | [2] IFC Monitor | BCF 3.0 | [44] García 2026 |
|---|---|---|---|
| Cảm biến, hệ đo | có | không | không |
| Quan hệ cảm biến – cấu kiện | có, tĩnh | không | không |
| Bằng chứng tình trạng và phạm vi hiệu lực | không | không | không |
| Vấn đề/hành động có trạng thái | không | có | có (vấn đề về thông tin) |
| Lịch sử đổi trạng thái | không | có (BCF-API) | có (bản ghi quyết định) |
| Thẩm quyền theo vai trò | không | quyền thao tác | có (RACI, tách nhiệm vụ) |

Ba nguồn phủ ba đoạn khác nhau của chuỗi và gần như không chồng nhau: [2] ở đầu (hệ đo ↔ cấu kiện), BCF ở cuối (vấn đề
có trạng thái gắn cấu kiện), [44] ở lớp quản trị (bước chuyển có bằng chứng và vai trò). Đoạn giữa, tức bằng chứng tình
trạng có phạm vi hiệu lực và quan hệ định kiểu nối nó với hành động, không nguồn nào trong ba nguồn có.
