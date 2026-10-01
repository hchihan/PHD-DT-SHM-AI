# KPWFC4PI — Cross, Worden & Chen (2011)

Cross EJ, Worden K, Chen Q. Cointegration: a novel approach for the removal of environmental trends in
structural health monitoring data. *Proc. R. Soc. A* 467(2133): 2712–2732. DOI 10.1098/rspa.2011.0023.

**Bản đã đọc:** bản in, tệp `pdf/KPWFC4PI_Cross2011.pdf` (21 tr., tr. 2712–2732; trang đầu khớp DOI). Đọc toàn văn
ngày 01/10/2026 (NCS cung cấp PDF). Thay cho ghi chú "chỉ tóm tắt" ngày 29/09/2026.

Ký hiệu: (a) điều tác giả nói; (b) giới hạn tác giả tự nêu; **[NCS]** nhận định của NCS.

| Cột | Nội dung |
|---|---|
| Citekey / Số cũ | KPWFC4PI / mới (bosung-5.6A) |
| Tier / Cụm | Bổ sung 5.6A / SHM–bu lông–EOV |
| Luận điểm | Nếu hai hay nhiều biến quan trắc không dừng đồng liên kết (cointegrated) thì có tổ hợp tuyến tính của chúng là phần dư dừng đã loại các xu hướng chung do biến ẩn (môi trường, vận hành) gây ra; phần dư này là đặc trưng nhạy hư hỏng, độc lập với điều kiện môi trường – vận hành bình thường (tr. 2712, 2714). |
| Bằng chứng | Ví dụ mô phỏng hệ 10 bậc tự do có độ cứng phụ thuộc nhiệt độ, hư hỏng là giảm 50 % độ cứng lò xo thứ hai (tr. 2714–2716); ứng dụng trên dữ liệu chuẩn DAMASCOS: tấm composite CFRP trong buồng môi trường, sóng Lamb, nhiệt độ chu kỳ 10–30 °C, hư hỏng là lỗ khoan 10 mm (tr. 2726–2728). Quy trình: kiểm định ADF bậc tích hợp, thủ tục Johansen tìm vectơ đồng liên kết, kiểm định vết (tr. 2716–2726). |
| Giới hạn | Xem mục 4. |
| Tác động K1/K2/K3 | K1: mở rộng — tính hợp lệ của phần dư phụ thuộc tập huấn luyện "trạng thái bình thường"; dải điều kiện của tập này là một thành phần của phạm vi hiệu lực. K2, K3: không liên quan trực tiếp. |
| Vị trí sử dụng | 5.6A.3 (bù EOV khi biến môi trường chưa đo được); 3.2 (nhiễu vận hành nhà xưởng, UV-08); phản chứng UV-06. |
| Mức đã đọc | Toàn văn (01/10/2026) |

## 1. Vấn đề và các hướng đã có (a)

- Đặc trưng nhạy hư hỏng cũng nhạy với điều kiện môi trường – vận hành; nhiệt độ thường là yếu tố trội (tr. 2712).
- Hướng hồi quy theo biến môi trường đo được: muốn tin dự báo thì mọi yếu tố ảnh hưởng phải được đo và hiểu, là giới
  hạn rõ khi mạng cảm biến nhỏ (tr. 2713).
- Hướng dùng tập dữ liệu dài (ví dụ cả năm) làm trạng thái bình thường: tốn lưu trữ và có thể giảm độ nhạy (tr. 2713).
- Hướng chiếu PCA/FA giữ biến động môi trường ở các thành phần chính đầu (tr. 2713).

## 2. Phương pháp (a)

- Định nghĩa: chuỗi không dừng đồng liên kết nếu một tổ hợp tuyến tính của chúng dừng; các chuỗi phải cùng bậc
  tích hợp, thủ tục Johansen dùng cho biến I(1) (tr. 2716–2717, 2724).
- Bước: ADF kiểm bậc tích hợp từng biến → mô hình VAR, chọn bậc theo AIC → ước lượng VECM, vectơ đồng liên kết là
  vectơ riêng ứng với trị riêng lớn nhất → chiếu dữ liệu mới, theo dõi tính dừng của phần dư (biểu đồ X, giới hạn
  ±3 độ lệch chuẩn của phần dư huấn luyện) → kiểm định vết để biết số vectơ (tr. 2724–2726).
- Phần dư sẽ không dừng khi có sự kiện làm **thay đổi quan hệ giữa các biến** trong tổ hợp, tức khi hệ vận hành ra
  ngoài trạng thái bình thường (tr. 2715).

## 3. Kết quả (a)

- DAMASCOS: tập huấn luyện 1000 điểm (355 điểm nhiệt độ hằng, 645 điểm nhiệt độ chu kỳ); phần dư dừng trong phần lớn
  thời gian và vượt giới hạn quanh điểm 2500 khi khoan lỗ (tr. 2727–2728).
- Một lần vượt giới hạn khác tại điểm 1364, trùng lúc buồng bắt đầu đổi nhiệt; phần dư nhanh chóng dừng trở lại
  (tr. 2728). Phần dư trôi nhẹ trong khoảng ngắn dù "dừng về thống kê"; dùng 20 đặc trưng đầu thì hết trôi và gián đoạn,
  vẫn nhạy hư hỏng (tr. 2728).

## 4. Giới hạn

- (b) Thủ tục Johansen chỉ cho biến xấp xỉ I(1); tác giả cho rằng phần lớn biến SHM không có quá một nghiệm đơn vị
  (tr. 2729).
- (b) Phương pháp chỉ áp cho biến **quan hệ tuyến tính**; phần mở rộng phi tuyến đang được nghiên cứu (tr. 2729).
- (b) Tập huấn luyện phải lấy từ trạng thái bình thường và phải chọn cẩn thận: nếu một điều kiện vận hành – môi trường
  bình thường gây thay đổi lớn trong đáp ứng thì dữ liệu của sự kiện đó phải có trong tập huấn luyện, nếu không sẽ báo
  động giả khi sự kiện lặp lại (tr. 2728).
- **[NCS]** Kiểm chứng chỉ trên mô phỏng và một tấm composite trong buồng môi trường với một nguồn biến động (nhiệt);
  chưa có kết cấu thực ngoài hiện trường, chưa có nguồn biến động vận hành như tải cầu trục, chưa có kết cấu thép bu lông.
- **[NCS]** Theo tr. 2715, mọi sự kiện làm đổi quan hệ giữa các biến đều làm phần dư mất tính dừng. Một lần siết lại hay
  thay bu lông (can thiệp bảo trì) cũng có thể đổi quan hệ đó; phương pháp không tự phân biệt can thiệp với hư hỏng,
  nên sau can thiệp cần ghi sự kiện và lập lại tập huấn luyện. Đây là suy luận của NCS, tác giả không bàn.

## 5. Đoạn dùng được cho tiểu luận

| Luận điểm trong tiểu luận | Trang | Loại |
|---|---|---|
| Đồng liên kết tạo phần dư dừng đã loại xu hướng chung của các biến quan trắc | 2712, 2714 | trực tiếp |
| Có thể áp dụng khi không đo được điều kiện môi trường – vận hành; chỉ cần huấn luyện bằng dữ liệu trạng thái bình thường | 2728 | trực tiếp |
| Sự kiện vận hành bình thường gây thay đổi lớn phải có trong tập huấn luyện để tránh báo động giả | 2728 | trực tiếp |
| Hồi quy theo biến môi trường đòi hỏi đo được mọi yếu tố ảnh hưởng | 2713 | trực tiếp (dùng cho 3.2) |
| Áp sang nhà xưởng có cầu trục | — | diễn giải của NCS |

## 6. Kiểm phản chứng

- **UV-06** (phạm vi hiệu lực theo lần lắp ráp – can thiệp): đã kiểm. Bài không bàn lần lắp ráp hay can thiệp; chỉ yêu cầu
  tập huấn luyện là trạng thái bình thường (tr. 2728). Không giải quyết UV-06; củng cố ý ở mục 4 dòng cuối ([NCS]).
- **UV-08** (nhiễu vận hành nhà xưởng): bài cho một cách bù khi biến vận hành chưa đo, nhưng chỉ kiểm chứng với nhiệt độ
  trong PTN; không giải quyết phần nhà xưởng.
