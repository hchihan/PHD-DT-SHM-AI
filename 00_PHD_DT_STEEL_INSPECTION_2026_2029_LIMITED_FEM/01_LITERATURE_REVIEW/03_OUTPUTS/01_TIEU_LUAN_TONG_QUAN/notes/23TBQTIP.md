# 23TBQTIP — Figueiredo và cs. (2011)

Figueiredo E, Park G, Farrar CR, Worden K, Figueiras J. Machine learning algorithms for damage detection
under operational and environmental variability. *Structural Health Monitoring* 10(6): 559–572.
DOI 10.1177/1475921710388971.

**Bản đã đọc:** bản in của tạp chí (tệp `pdf/23TBQTIP_Figueiredo2011.pdf`, 15 tr.; trang tạp chí 559–572). Phiên 5.6A
(29/09/2026) đọc Giới thiệu, Chuẩn hóa dữ liệu, mô tả kết cấu thử, Kết luận; phiên T2-1 (01/10/2026) đọc bổ sung phần
thuật toán và kết quả (tr. 562–571). Đã đọc toàn văn.

Ký hiệu: (a) điều tác giả nói; (b) giới hạn tác giả tự nêu; **[NCS]** nhận định của NCS.

| Cột | Nội dung |
|---|---|
| Citekey / Số cũ | 23TBQTIP / mới (bosung-5.6A, Tier 2) |
| Tier / Cụm | Tier 2 / SHM–bu lông–EOV |
| Luận điểm | Biến động vận hành – môi trường có thể che lấp đặc trưng do hư hỏng; có hai cách tách: (i) đo trực tiếp biến vận hành – môi trường rồi tham số hóa đặc trưng theo các biến đó, (ii) dùng thuật toán học máy học mô hình trạng thái bình thường từ dữ liệu đáp ứng thu dưới nhiều điều kiện, không cần đo biến môi trường (tr. 560–561). |
| Bằng chứng | So sánh bốn thuật toán (AANN, FA, MSD, SVD) trên đặc trưng AR(10) của bốn gia tốc kế, khung nhôm ba tầng lắp bằng bu lông trong PTN, 17 trạng thái × 100 lần đo; biến động vận hành – môi trường mô phỏng bằng thêm khối lượng 1,2 kg và giảm 87,5 % độ cứng cột (tần số cơ bản đổi tới khoảng 7 %); hư hỏng là phi tuyến va chạm của cột treo với bộ chặn, khe 0,20–0,05 mm (tr. 564–566, Bảng 1). Đánh giá bằng ROC và sai lầm loại I/II ở ngưỡng 95 % (tr. 568–569, Bảng 2). |
| Giới hạn | Xem mục 5. |
| Tác động K1/K2/K3 | K1: mở rộng (điều kiện áp dụng của mô hình học từ trạng thái bình thường phụ thuộc dải điều kiện trong dữ liệu huấn luyện; lựa chọn thuật toán phụ thuộc mục đích báo động giả hay bỏ sót). K2, K3: không liên quan. |
| Vị trí sử dụng | 5.6A.3 (bù EOV); 3.2 (hạn chế quan trắc công trình công nghiệp, L2.2); 5.7 (báo động giả M2.2). |
| Mức đã đọc | Toàn văn (29/09 và 01/10/2026) |

## 1. Câu hỏi và dữ liệu

- (a) So sánh trực tiếp bốn thuật toán học máy đã được báo cáo là cách tách thay đổi do hư hỏng khỏi thay đổi do vận
  hành – môi trường, trên bộ dữ liệu chuẩn (tr. 559, 571).
- Kết cấu thử (tr. 564): khung **nhôm** ba tầng, cột và tấm lắp bu lông, trượt trên ray theo một phương; kích động bằng
  máy rung, ngẫu nhiên 20–150 Hz; lấy mẫu 320 Hz, 12,8 s mỗi lần đo. (a) Kết cấu **không phải mô hình thu nhỏ của công
  trình nào**, mà là bệ thử chuẩn cho kiểm chứng SHM (tr. 564).
- Bốn nhóm trạng thái (tr. 565–566): đường cơ sở; tám trạng thái "chưa hư hỏng" có thay đổi khối lượng hoặc độ cứng (mô
  phỏng EOV); năm trạng thái hư hỏng (khe va chạm); ba trạng thái hư hỏng kèm thay đổi khối lượng.
- Chia tập (tr. 567–568): huấn luyện 50/100 lần đo của mỗi trạng thái chưa hư hỏng (450 vectơ); kiểm tra 50 lần đo còn lại
  của trạng thái chưa hư hỏng cộng toàn bộ trạng thái hư hỏng (1250 vectơ).

## 2. Phần so sánh thuật toán (bổ sung T2-1)

- (a) Không thuật toán nào phân loại hoàn hảo với ngưỡng tuyến tính; AANN và MSD phát hiện tốt hơn SVD và FA trên toàn dải
  báo động giả; ở xác suất báo động giả thấp và cao, MSD tốt nhất (tr. 568–569, Hình 6).
- (a) Ở ngưỡng 95 %: AANN 9,8 % loại I / 1,3 % loại II; FA 2,2 % / 5,4 %; MSD 9,3 % / 1,0 %; SVD 6,2 % / 3,6 %; tổng sai
  4,0–4,6 % (tr. 569, Bảng 2). Có đánh đổi rõ giữa hai loại sai.
- (a) Chọn thuật toán theo mục đích: FA, SVD khi muốn giảm báo động giả (động lực kinh tế, độ tin cậy); AANN, MSD khi
  muốn giảm bỏ sót (an toàn sinh mạng) (tr. 570).
- (a) Sai lầm loại II tập trung ở mức hư hỏng nhỏ nhất (khe 0,20 mm) (tr. 570).
- (a) AANN và FA phụ thuộc số nhân tố ẩn giả định; tối ưu khi số nhân tố xấp xỉ số nguồn biến đổi mô phỏng (2 và 3);
  trong thực tế số nguồn biến đổi thường không biết trước, và giả định quá nhiều nhân tố làm giảm khả năng tổng quát hóa
  (tr. 570, Hình 8).
- (a) MSD được đánh giá tốt nhất xét hiệu năng, chi phí tính toán và việc không cần giả định kiến trúc (tr. 570–571).

## 3. Điều kiện thất bại

- (b) Thuật toán có thể thất bại nếu dữ liệu huấn luyện chỉ đại diện dải hẹp; không bảo đảm hiệu quả với điều kiện chưa
  có trong huấn luyện (tr. 571).
- (b) Nếu hư hỏng gây thay đổi giống thay đổi do nguồn biến đổi, chưa rõ thuật toán tách được (tr. 571).
- (b) Số nguồn biến đổi độc lập thường không biết trước (tr. 570).
- **[NCS]** Trong bệ thử, **giảm độ cứng cột được xếp vào nhóm "chưa hư hỏng"** để mô phỏng EOV (tr. 565, Bảng 1), còn hư
  hỏng là phi tuyến va chạm. Vậy một suy giảm độ cứng tuyến tính (ví dụ liên kết mất lực siết mà không va đập) sẽ được
  thuật toán coi là biến động bình thường. Đây là suy luận của NCS từ thiết kế thí nghiệm, bài không bàn.

## 4. Luận điểm chính

1. EOV có thể che lấp thay đổi do hư hỏng; nhiệt độ làm tần số cầu đổi 5–10 %, có trường hợp biến động do gối đóng băng
   lớn hơn nhiều so với do hư hỏng (tr. 561–562).
2. Học trạng thái bình thường từ dữ liệu đáp ứng đa điều kiện cho phép phát hiện mà không đo biến môi trường (tr. 562, 571).
3. Chọn thuật toán là chọn điểm đánh đổi báo động giả – bỏ sót, gắn với mục đích kinh tế hay an toàn (tr. 570–571).

## 5. Giới hạn

**(b) Tác giả tự nêu:** như mục 3.

**[NCS] nhận định:**
- Khung nhôm PTN, EOV mô phỏng bằng khối lượng và độ cứng, không có nhiệt độ hay tải vận hành thật.
- Một bệ thử; đánh giá bằng chia ngẫu nhiên từng lần đo trong cùng trạng thái (tr. 567–568), không giữ lại cả trạng thái
  vận hành chưa thấy, nên chưa đo được khả năng tổng quát sang điều kiện mới, đúng điều tác giả tự cảnh báo.

## 6. Điều bài không xử lý (theo chuỗi luận án, ngắn)

Không ghi lại dải điều kiện huấn luyện cùng chỉ số hư hỏng; không bàn quyết định sau báo động.

## 7. Tác động tới K1/K2/K3

- **K1: mở rộng.** Điều kiện áp dụng của bộ phát hiện = dải điều kiện huấn luyện (tr. 571); ngưỡng và lựa chọn thuật toán
  thể hiện một mức đánh đổi báo động giả – bỏ sót (tr. 569–570). **[NCS]** Cả hai nên đi cùng bằng chứng (phương pháp,
  ngưỡng, điều kiện áp dụng).
- K2, K3: không liên quan.

## 8. Vị trí sử dụng

- 5.6A.3: bù EOV; giới hạn khi điều kiện chưa có trong huấn luyện.
- 3.2: EOV che lấp hư hỏng (L2.2, mức chung).
- 5.7: báo động giả và bỏ sót (M2.2).
