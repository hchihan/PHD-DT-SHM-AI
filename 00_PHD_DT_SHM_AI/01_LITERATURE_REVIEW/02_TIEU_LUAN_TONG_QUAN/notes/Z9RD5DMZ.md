# Z9RD5DMZ — Hughes và cs. (2022)

Hughes AJ, Bull LA, Gardner P, Barthorpe RJ, Dervilis N, Worden K. On risk-based active learning for
structural health monitoring. *Mechanical Systems and Signal Processing* 167: 108569.
DOI 10.1016/j.ymssp.2021.108569.

**Bản đã đọc:** bản tiền in arXiv 2105.05622v2 (16/11/2021, 30 tr.), "Preprint submitted to MSSP" (tệp `pdf/Z9RD5DMZ_Hughes2022_arXiv-v2.pdf`). Kiểm tra 29/09/2026: bản in MSSP 167:108569 là truy cập đóng (OpenAlex), các kho lưu trữ (arXiv, White Rose, Glasgow) chỉ có bản tiền in; chưa đối chiếu được số trang bản in. Số trang
dưới đây là số trang của bản tiền in; cần đối chiếu bản in trước khi dẫn trang.

| Cột | Nội dung |
|---|---|
| Citekey / Số cũ | Z9RD5DMZ / mới (bosung-5.6A) |
| Tier / Cụm | Tier 2 (chốt ĐD1; trước đó Bổ sung 5.6A) / Giá trị quyết định |
| Luận điểm | Học chủ động theo rủi ro: việc hỏi nhãn được **ánh xạ thành việc kiểm tra kết cấu** để xác định trạng thái; điểm dữ liệu chỉ được hỏi nhãn (kiểm tra) khi giá trị kỳ vọng của thông tin hoàn hảo (EVPI) với quyết định bảo trì vượt chi phí kiểm tra (tr. 1, 7). Nhãn mới là thông tin chẩn đoán do kỹ sư cung cấp sau kiểm tra (tr. 2). |
| Bằng chứng | Ví dụ số và dữ liệu cầu bê tông Z24 (4 tần số riêng, 3932 quan sát; 4 lớp: bình thường, bình thường khi lạnh, hư hỏng sớm, hư hỏng nặng), quyết định nhị phân "không làm gì" / "bảo trì"; đánh giá bằng "độ chính xác quyết định" thay vì độ chính xác phân loại (tr. 7, 19–20). |
| Giới hạn | *Tác giả:* phải biết trước số lớp trạng thái; giả định kiểm tra cho thông tin hoàn hảo, trong khi kiểm tra có thể có sai sót của con người; thiên lệch lấy mẫu làm giảm hiệu quả quyết định sau một số lần hỏi; mới xét quyết định nhị phân (tr. 27–28). *NCS:* dữ liệu cầu bê tông với nhãn định sẵn, không phải nhãn từ kiểm tra thực. |
| Tác động K1/K2/K3 | K3: mở rộng — gắn việc kiểm tra với giá trị cho quyết định; giả định "kiểm tra hoàn hảo" cho thấy cần ghi lại ai kiểm tra và căn cứ nào (bản ghi kiểm tra có nguồn gốc). |
| Vị trí sử dụng | 5.6A.3 (học chủ động, vòng lặp kiểm tra tạo nhãn); 4.5.5. |
| Mức đã đọc | Toàn văn, bản tiền in (phần 5 đọc bổ sung 01/10/2026, phiên T2-2). |

## Bổ sung phiên T2-2 (01/10/2026): phần 5, ví dụ số (tr. 8–18, bản tiền in)

- (a) Kết cấu giả định S có bốn trạng thái: không hư hỏng; hư hỏng nhẹ, vẫn hoạt động đủ; hư hỏng đáng kể, giảm khả
  năng khai thác; hư hỏng nghiêm trọng, ngừng khai thác (tr. 8–9). Quyết định nhị phân "không làm gì" / "bảo trì";
  hàm lợi ích và xác suất chuyển trạng thái được **chọn để đại diện**, việc lấy ý kiến chuyên gia để xác định hàm lợi ích
  nằm ngoài phạm vi bài (tr. 9).
- (a) Nhãn trạng thái thật thu được qua kiểm tra với chi phí Cins = 7 (tr. 10). Lưu đồ Hình 7: khi EVPI > Cins thì hỏi
  thông tin trạng thái, trạng thái "do kỹ sư cung cấp qua kiểm tra", rồi cập nhật tập có nhãn (tr. 9).
- (a) Bộ phân loại: hỗn hợp bốn phân phối Gauss học theo Bayes với tiên nghiệm NIW và Dirichlet (tr. 10–13); ví dụ
  tính EVPI = 5,415 (tr. 13–14).
- (a) Dữ liệu: 1997 điểm hai chiều **được sinh** để đại diện cho thay đổi đặc trưng khi hư hỏng tăng dần; một nửa
  làm tập kiểm tra độc lập; 1,5 % của phần còn lại có nhãn ban đầu (tr. 14–15).
- (a) Kết quả: điểm ở vùng chồng lấn giữa các lớp đòi hỏi chính sách bảo trì khác nhau được hỏi nhãn nhiều; lớp 1 và 4
  ít được hỏi nên mô hình của hai lớp này khớp kém (tr. 16). Lặp 1000 lần với hạt giống ngẫu nhiên khác nhau: độ chính
  xác quyết định tăng nhanh hơn lấy mẫu ngẫu nhiên; sau khoảng 20 lần hỏi mức cải thiện giảm mạnh, sau 28 lần bắt đầu
  giảm nhẹ, có thể do thiên lệch lấy mẫu (tr. 18).
- **[NCS]** Phần 5 dùng dữ liệu sinh, nhãn đúng tuyệt đối khi "kiểm tra"; không có thông tin về người kiểm tra, phương
  pháp hay độ bất định của kết quả kiểm tra. Điều này củng cố nhận định đã ghi ở bảng (kiểm tra được giả định hoàn hảo)
  và ở UV-05 / UV-07; không thay đổi phát biểu thu hẹp của UV-05.
- Đoạn dùng được: tr. 9 (Hình 7: nhãn do kỹ sư cung cấp qua kiểm tra, khi EVPI vượt chi phí kiểm tra) — trực tiếp, cho
  vòng lặp kiểm tra tạo nhãn ở 3.6 và 5.6A.
