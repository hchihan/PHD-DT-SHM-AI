# MANJDQEZ — Sohn (2007) — [45]

Sohn H. Effects of environmental and operational variability on structural health monitoring. *Phil. Trans. R. Soc. A*
365(1851): 539–560. DOI 10.1098/rsta.2006.1935. Trực tuyến 13/12/2006 (tr. 539).

**Bản đã đọc:** toàn văn bản in của tạp chí (tệp đính kèm trong kho Zotero, 22 tr. PDF). Trang dẫn là **trang in**:
trang in = trang PDF + 538. Phiên 5.6A (29/09/2026) đọc tóm tắt và mục 4; phiên T2-1 (01/10/2026) đọc bổ sung mục 1–3.

Ký hiệu: (a) điều tác giả nói; (b) giới hạn tác giả tự nêu; **[NCS]** nhận định của NCS.

| Cột | Nội dung |
|---|---|
| Citekey / Số cũ | MANJDQEZ / [45] |
| Tier / Cụm | Tier 2 / SHM–bu lông–EOV |
| Luận điểm | Công trình chịu biến đổi điều kiện môi trường và vận hành làm thay đổi tín hiệu đo, và các biến đổi này thường che lấp thay đổi nhỏ do hư hỏng; chuẩn hóa dữ liệu (data normalization) nhằm tách hai loại thay đổi, và là một trong các trở ngại chính để triển khai SHM cho công trình đang khai thác (tr. 539–540). |
| Bằng chứng | Tổng quan các ví dụ thực (cầu I-40, Alamosa Canyon, Z24, tàu lượn, cầu treo) về ảnh hưởng nhiệt độ, điều kiện biên, tải khối lượng, gió (tr. 540–544); tổng quan bảy nhóm kỹ thuật chuẩn hóa dữ liệu, phần lớn kiểm chứng bằng mô phỏng hay mẫu PTN (tr. 544–557). |
| Giới hạn | Xem mục 5. |
| Tác động K1/K2/K3 | K1: mở rộng (phạm vi hiệu lực của bằng chứng cảm biến phụ thuộc dải điều kiện đã có trong dữ liệu tham chiếu; chuẩn hóa là riêng cho từng công trình). K2, K3: không liên quan. |
| Vị trí sử dụng | 3.2 (EOV, L2.2); 3.6 (PTN → hiện trường, L3.1); 5.6A.3 (bù EOV). |
| Mức đã đọc | Toàn văn (29/09/2026 mục 4; 01/10/2026 mục 1–3) |

## 1. Câu hỏi và đối tượng

- Mục tiêu (tr. 539, 541): tổng quan ảnh hưởng của biến đổi môi trường – vận hành trên công trình thật và các tiến bộ về
  chuẩn hóa dữ liệu. Đối tượng: công trình đang khai thác, chủ yếu cầu.
- (a) Nhiều phương pháp thành công trên mô hình thu nhỏ hay mẫu trong PTN, nhưng hiệu quả ở hiện trường còn đáng ngờ và
  cần kiểm chứng; theo dõi máy quay đã chuyển thành thực hành, SHM cho kết cấu khác thì chưa (tr. 539–540).

## 2. Các nguồn biến đổi môi trường – vận hành (mục 2, tr. 541–544)

- **Phân loại** (a): môi trường gồm gió, nhiệt độ, độ ẩm; vận hành gồm tải môi trường xung quanh, tốc độ vận hành, tải
  khối lượng (tr. 541).
- **Nhiệt độ** (tr. 541–542): thay đổi độ cứng vật liệu và điều kiện biên (khe co giãn đóng lại); tần số dạng 1 cầu
  Alamosa Canyon thay đổi khoảng 5 % trong 24 giờ; cầu đi bộ BTCT thay đổi khoảng 10 % theo mùa; ở cầu I-40 tần số
  tăng ở hai cấp hư hỏng đầu rồi mới giảm, do nhiệt độ (tr. 540–542).
- **Điều kiện biên** (tr. 542–543): thay đổi chiều dài dầm 2 % làm tần số đổi gấp 40 lần so với vết nứt 2 % chiều cao
  (Cawley 1997); gối bị đóng băng làm tần số thay đổi lớn hơn một bậc so với vết cắt nhân tạo (tr. 542). Điều kiện biên
  khó đo trực tiếp (tr. 543).
- **Tải khối lượng** (tr. 543–544): tần số dầm cầu 46 m giảm 5,4 % khi giao thông nặng; ở tàu lượn, khác biệt do tải
  hành khách mô phỏng lớn hơn nhiều so với khác biệt do bong tách bánh xe (hư hỏng) (tr. 543–544, Hình 4).
- **Gió** (tr. 544): tần số cơ bản cầu treo giảm khi tốc độ gió tăng; cản tăng khi gió vượt ngưỡng.

## 3. Các nhóm phương pháp bù (mục 3, tr. 544–557)

- **Ba tình huống** (a, tr. 544–546, Hình 5): (1) đo được biến môi trường – vận hành → hồi quy, nội suy; (2) không đo
  được nhưng hư hỏng gây thay đổi "trực giao" với thay đổi do môi trường → mô hình hóa ngầm hoặc chia đường cơ sở theo
  điều kiện; (3) trích đặc trưng nhạy hư hỏng nhưng không nhạy môi trường.
- **Bảy kỹ thuật** được tổng quan: hồi quy (ARX theo nhiệt độ ở Z24; lọc tuyến tính nhiều nhiệt kế ở Alamosa) (tr.
  546–548); nhận dạng không gian con có cơ sở dữ liệu theo nhiệt độ (tr. 548–549); phát hiện điểm mới với đường cơ sở
  tham số hóa theo biến môi trường (tr. 549–550); thành phần chính nhỏ (tr. 550–551); SVD (tr. 551); mạng nơ-ron tự liên
  kết (AANN) (tr. 551–554); phân tích nhân tố (tr. 554–555); sóng Lamb (tr. 555–557).
- (a) **Chuẩn hóa là bài toán riêng của từng công trình**: hai cầu cần hai cách mô hình nhiệt độ khác nhau (tr. 548).
- (a) Phát hiện điểm mới chỉ trả lời mức có/không có hư hỏng, và thành công phụ thuộc vào độ chính xác của mô tả trạng
  thái bình thường (tr. 549).

## 4. Giới hạn khi điều kiện vận hành chưa có trong dữ liệu huấn luyện

- (a) Với AANN, sai số dự báo tăng khi mạng gặp **bất kỳ** tín hiệu nào chưa được "ghi" vào mạng, không riêng hư hỏng;
  vì vậy phải thu dải điều kiện rộng của đường cơ sở (tr. 553).
- (a) Phương pháp không gian con và SVD dựa trên giả định hư hỏng tạo thay đổi trực giao với không gian đường cơ sở; điều
  kiện vận hành khác cũng có thể tạo thay đổi trực giao, và hư hỏng có thể nằm trong không gian đường cơ sở (tr. 548–549, 551).
- (a) Đường cơ sở dịch chuyển do nhiệt độ có thể khiến quan sát bị gắn cờ hư hỏng sai, hoặc hư hỏng thật không bị gắn cờ
  (tr. 557).
- (a) Nếu dữ liệu huấn luyện không phủ dải rộng điều kiện, bộ phân loại không thể khẳng định có hư hỏng hay không, vì điều
  kiện vận hành bất thường có thể gây hiệu ứng giống hư hỏng (tr. 557).

## 5. Giới hạn

**(b) Tác giả tự nêu:**
- Hệ SHM sẽ không được chấp nhận trong thực tế nếu chưa có kỹ thuật tính tường minh điều kiện môi trường – vận hành; ít kỹ
  thuật đã được chứng minh (tr. 557).
- Nhiều kỹ thuật mới chỉ thử bằng mô phỏng hay mẫu PTN đơn giản: không gian con (tr. 548), phân tích nhân tố (tr. 555, mô
  hình FE của một xe cẩu), sóng Lamb (tr. 556).
- Cần nghiên cứu tập trung theo ứng dụng và ngành, thử trên công trình thật trong môi trường vận hành; thực tế có lẽ cần
  kết hợp cả ba nhóm (tr. 557–558).

**[NCS] nhận định:**
- Ví dụ thực đều là cầu, tháp, tàu lượn; không có nhà công nghiệp. Ví dụ "xe cẩu" (Kullaa) là mô hình FE của xe cẩu tự
  hành, không phải cầu trục trong nhà xưởng (tr. 555).
- Bài năm 2007; các nhóm phương pháp về sau (đồng liên kết, học sâu) không có mặt.

## 6. Điều bài không xử lý (theo chuỗi luận án, ngắn)

Không bàn cách ghi dải điều kiện của đường cơ sở cùng kết quả phát hiện; không bàn quyết định hay hành động.

## 7. Tác động tới K1/K2/K3

- **K1: mở rộng.** Một đầu ra phát hiện chỉ có nghĩa trong dải điều kiện đã có trong dữ liệu tham chiếu (tr. 553, 557), và
  cách chuẩn hóa là riêng từng công trình (tr. 548). **[NCS]** Hai ý này là căn cứ để "điều kiện áp dụng" và "đường cơ sở"
  là trường bắt buộc của phạm vi hiệu lực.
- K2, K3: không liên quan.

## 8. Vị trí sử dụng

- 3.2: EOV che lấp hư hỏng (L2.2), tải khối lượng vận hành lớn hơn hiệu ứng hư hỏng (tr. 543–544).
- 3.6: cần thử trên công trình thật (L3.1, tr. 539–540, 558).
- 5.6A.3: nhóm phương pháp bù EOV; giới hạn khi điều kiện mới.
