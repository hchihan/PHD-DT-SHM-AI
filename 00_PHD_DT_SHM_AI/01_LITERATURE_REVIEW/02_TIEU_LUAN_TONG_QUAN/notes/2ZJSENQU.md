# 2ZJSENQU — Maes, Van Meerbeeck, Reynders & Lombaert (2022)

Maes K, Van Meerbeeck L, Reynders EPB, Lombaert G. Validation of vibration-based structural health monitoring on retrofitted
railway bridge KW51. *Mechanical Systems and Signal Processing* 165: 108380, 2022. DOI 10.1016/j.ymssp.2021.108380 (Crossref
xác minh 01/10/2026).

**Bản đã đọc:** bản postprint tác giả trên kho Lirias (KU Leuven), 34 tr., trang đầu ghi "Postprint submitted to Mechanical
Systems and Signal Processing" và thông tin bản in. Kho Lirias không truy cập được bằng `curl` từ máy này; tệp (49 MB) được mở
trong trình duyệt tích hợp và trích văn bản theo trang bằng pdf.js — **chưa lưu được vào `pdf/`** (N-41). Đọc toàn văn phần mở
đầu, mục 2 (giám sát, gia cường), mục 3 (hồi quy tuyến tính, PCA bền vững), kết luận; mục 4 (mô hình phần tử hữu hạn, sáu ca
biến đổi mô phỏng, ROC) đọc theo từ khóa. **Trang dẫn theo bản postprint**, cần đối chiếu bản in trước GĐ6 (N-04).
Ứng viên tìm qua OpenAlex cho N-23 (theo dõi dài hạn có can thiệp giữa chừng).

Ký hiệu: (a) điều tác giả nói; (b) giới hạn tác giả tự nêu; **[NCS]** nhận định của NCS.

| Cột | Nội dung |
|---|---|
| Citekey / Số cũ | 2ZJSENQU / mới (phanchung-GD2) |
| Tier / Cụm | Bổ sung phản chứng (không thuộc 30 key) / SHM–bu lông–EOV |
| Luận điểm | Tần số riêng từ theo dõi dài hạn một cầu đường sắt thép dạng vòm (KW51, Leuven) phân biệt được trạng thái trước và sau gia cường liên kết, sau khi loại ảnh hưởng nhiệt độ bằng hồi quy tuyến tính hoặc PCA bền vững; PCA bền vững tốt hơn ở mọi ca xét (tr. 1, 32). |
| Bằng chứng | Hiện trường: gia tốc kế trên mặt cầu, thêm 6 gia tốc kế trên vòm trong khi gia cường (danh sách tr. 4 là cấu hình cuối, 12 kênh gia tốc); 14 dạng dao động theo dõi hằng giờ bằng phân tích dạng dao động vận hành tự động (SSI-cov/ref); 7,5 tháng trước, 4,5 tháng trong, 3,5 tháng sau gia cường (tr. 4–6). Huấn luyện chỉ trên dữ liệu trước gia cường, chia tuần lẻ/tuần chẵn cho huấn luyện/kiểm định (tr. 11). Thêm sáu ca biến đổi nhỏ mô phỏng bằng mô hình phần tử hữu hạn đã hiệu chỉnh, đánh giá bằng đường ROC (tr. 27–32). |
| Giới hạn | Xem mục 3. |
| Tác động K1/K2/K3 | K1 (UV-06): căn cứ hiện trường cùng chiều — một lần can thiệp lên **liên kết bu lông** làm mô hình trạng thái ban đầu không còn đại diện cho trạng thái bình thường. K2 (UV-03): cùng chiều — cấu hình cảm biến thay đổi giữa chừng. K3: không liên quan. |
| Vị trí sử dụng | 3.1 hoặc 3.2 (bù ảnh hưởng môi trường trên công trình thật); 3.6 (lần can thiệp là ranh giới của đường cơ sở); 5.5 (`VALIDITY_SCOPE`, `OBS_CONTEXT`, `STATUS_EVENT` "đã gia cường"); 5.7 (ca kiểm chứng: can thiệp đã biết làm mốc). |
| Mức đã đọc | Toàn văn mục 1–3, 5; mục 4 theo từ khóa (01/10/2026), bản postprint |

## 1. Các ý chính (a)

- **Can thiệp:** từ 15/05 đến 27/09/2019 cầu được gia cường để khắc phục một lỗi thi công phát hiện khi kiểm tra; ở mỗi thanh
  xiên, một hộp thép được hàn bao quanh **liên kết bu lông** ban đầu tại nút giao với vòm và mặt cầu (tr. 6, Hình 3).
- **Đường cơ sở:** giả định chỉ dùng được dữ liệu ở trạng thái ban đầu (chưa hư hỏng) để huấn luyện (tr. 2); mô hình hồi quy và
  PCA đều huấn luyện trên dữ liệu trước gia cường (tr. 11, 15).
- **Sau can thiệp:** độ lệch của mô hình dịch rõ cho hầu hết dạng dao động (tr. 12, 14); với PCA bền vững, độ lệch vượt khoảng
  ±3σ ở **mọi điểm dữ liệu** của bảy dạng xét (tr. 20). Phần lớn dạng dao động tạo hai cụm tách biệt trước/sau gia cường (tr. 8).
  Tần số tăng do liên kết cứng hơn, giảm do khối lượng hộp thép (tr. 7–8).
- **Trong khi can thiệp:** tần số thay đổi mạnh chủ yếu do giàn giáo hai bên cầu; một số dạng không theo dõi được; chỉ dùng dữ liệu
  trước và sau (tr. 7).
- **Cấu hình quan trắc đổi giữa chừng:** sáu gia tốc kế được lắp thêm trên vòm trong khi gia cường, làm tỉ lệ nhận dạng thành công
  thay đổi và giảm độ phân tán ước lượng tần số của một số dạng (tr. 6, 9, Bảng 1).
- Ngưỡng cho chỉ số Youden lớn nhất phụ thuộc ca hư hỏng nên **không xác định trước được**; khuyến nghị ngưỡng cao theo đánh giá
  kỹ thuật và lấy trung bình độ lệch theo cửa sổ dài (tr. 32).

## 2. Đoạn dùng được cho tiểu luận

| Luận điểm trong tiểu luận | Trang (postprint) | Loại |
|---|---|---|
| Trên một công trình thép thật theo dõi dài hạn, can thiệp lên liên kết bu lông làm dữ liệu sau can thiệp lệch khỏi mô hình trạng thái ban đầu | 6, 12, 20 | trực tiếp |
| Mốc can thiệp được lấy từ hồ sơ thi công (ngày bắt đầu, kết thúc gia cường) và dùng để tách dữ liệu | 6–7 | trực tiếp |
| Cấu hình cảm biến thay đổi trong thời gian theo dõi, ảnh hưởng độ bất định của đặc trưng | 6, 9 | trực tiếp |
| Lần can thiệp cần được ghi như một sự kiện có thời điểm để kiểm được bằng chứng trước/sau có còn dùng được | — | diễn giải của NCS |

## 3. Giới hạn

- (b) Gia cường là một thay đổi lớn: ngưỡng tách hai trạng thái rất dễ chọn; với hư hỏng sớm, chọn ngưỡng là then chốt (tr. 15);
  các ca biến đổi nhỏ được mô phỏng, không phải hư hỏng thật (tr. 27). Ngưỡng tối ưu không xác định trước được (tr. 32).
- (b) Hồi quy tuyến tính giả định đo đủ mọi biến môi trường – vận hành; mô hình giới hạn ở nhiệt độ trên 2 °C nên phát hiện bị gián
  đoạn khi băng giá (tr. 11, 15).
- **[NCS]** Bài dùng mốc can thiệp như "đáp án" đã biết để kiểm chứng phương pháp; không đề xuất ghi lần can thiệp thành ranh giới
  phạm vi hiệu lực của mô hình hay bằng chứng, không bàn việc lập lại đường cơ sở sau gia cường. Đối tượng là cầu đường sắt, không
  phải nhà xưởng; can thiệp là hàn hộp bao liên kết (gia cường), không phải siết lại bu lông — áp sang nhà xưởng là diễn giải.

## 4. Kiểm phản chứng

- **UV-06 (lần lắp ráp/can thiệp là ranh giới phạm vi hiệu lực): không giải quyết; căn cứ hiện trường cùng chiều (TG về hiện
  tượng).** Đây là nguồn đầu tiên trong nhật ký cho thấy trên công trình thép thật theo dõi dài hạn, một lần can thiệp lên liên kết
  bu lông làm mô hình trạng thái ban đầu mất tính đại diện (tr. 6, 20). Mốc can thiệp có sẵn từ hồ sơ thi công và được dùng thủ công
  để tách dữ liệu (tr. 6–7); bài không biến nó thành thành phần được ghi của phạm vi hiệu lực. Đề xuất NCS tính là **căn cứ độc
  lập** của UV-06 (nhóm KU Leuven, 2022, trước 2025). Không mâu thuẫn với dữ liệu ngược chiều một phần của [48] (siết lại trong
  PTN): gia cường ở đây thay đổi độ cứng và khối lượng liên kết, khác về mức độ với siết lại.
- **UV-03 (ghép cảm biến – cấu kiện có thời hạn): cùng chiều, không đổi kết luận.** Cấu hình cảm biến đổi giữa chừng (tr. 6, 9)
  là ví dụ thực cho `SENSOR_MAPPING` có `valid_from` và `OBS_CONTEXT.sensor_config`.
- **Ứng viên liên quan chưa đọc (không nhập):** Maes & Lombaert 2021 (*J. Bridge Eng.* 26(3): 04721001, DOI
  10.1061/(ASCE)BE.1943-5592.0001668, mô tả chiến dịch đo, truy cập đóng); bộ dữ liệu Zenodo 10.5281/zenodo.3745914.
