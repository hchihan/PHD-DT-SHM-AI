# RG9FMT8Y — Wheat, Mohrenschildt, Habibi & Al-Ani (2024) [15]

Wheat L, Mohrenschildt MV, Habibi S, Al-Ani D. Impact of Data Leakage in Vibration Signals Used for Bearing Fault
Diagnosis. *IEEE Access* 12: 169879–169895, 2024. DOI 10.1109/ACCESS.2024.3497716. Nhận 24/10/2024, chấp nhận 09/11/2024,
xuất bản 13/11/2024, phiên bản hiện hành 25/11/2024; giấy phép CC BY 4.0 (tr. 169879). Thông tin thư mục kiểm theo trang 1
và chân trang; khớp với `99_tailieu.md` [15] và `matrix/doi_chieu_danh_muc.csv` (dòng 15).

**Bản đã đọc:** bản in của nhà xuất bản (IEEE Access, truy cập mở), tệp Zotero `C:/Users/VNT/Zotero/storage/P9B5Z3IQ/Wheat
et al. - 2024 - Impact of Data Leakage in Vibration Signals Used for Bearing Fault Diagnosis.pdf`, 17 tr. PDF. Trang dẫn là
**trang in** (169879–169895); trang in = trang PDF + 169878. Văn bản trích bằng PyMuPDF; các Bảng 1–9 là ảnh, đã đọc trực
tiếp trên ảnh trang (tr. 169882, 169884, 169886, 169888, 169890–169891). Hình 6, 7, 9, 10 (đường sai số theo fc) chỉ đọc
qua lời bàn, không đọc số trên đồ thị. Đọc toàn văn (gồm danh mục tài liệu lướt và tiểu sử tác giả) ngày 01/10/2026, phiên T2-3.

Ký hiệu: (a) điều tác giả nói; (b) giới hạn tác giả tự nêu; **[NCS]** nhận định của NCS.

**Lưu ý đối tượng:** đối tượng của bài là **ổ lăn (bearing) của máy quay** (động cơ BSG trên bệ thử, bệ thử mô-đun
Paderborn), **không phải kết cấu công trình**. Mọi việc áp kết quả sang kết cấu thép hay mối nối bu lông là diễn giải [NCS].

| Cột | Nội dung |
|---|---|
| Citekey / Số cũ | RG9FMT8Y / 15 |
| Tier / Cụm | Tier 2 / Độ tin cậy đánh giá |
| Luận điểm | Dữ liệu rung của máy quay chứa "dấu vết" riêng của từng nguồn (chi tiết, máy, ngày đo) ngoài các nguyên nhân dịch chuyển miền đã được thừa nhận; khi cùng nguồn có mặt ở cả tập huấn luyện và tập kiểm tra, bộ phân loại có thể nhận ra nguồn thay vì trạng thái hư hỏng, gây rò rỉ dữ liệu và hiệu năng lạc quan. Cách chia tập theo lần chạy hay theo ngày vì vậy không đánh giá được khả năng tổng quát sang chi tiết chưa thấy (tr. 169879–169881, 169889–169890, 169892). |
| Bằng chứng | Sáu quy trình chẩn đoán (phân tích tần số hoặc phân tích bao × PCA, SPCA, LDA, cùng SVM) trên hai bộ dữ liệu: CMHT (McMaster, bộ dữ liệu đóng; 4 lớp, 32 lần chạy, 19 ngày, hai gia tốc kế ba trục A1, A2) và KAt (Paderborn; 3 lớp, 14 ổ, 280 lần chạy, một gia tốc kế). So sánh chia **theo lần chạy** với **theo ngày** (CMHT) và **theo lần chạy** với **theo chi tiết** (KAt), dạng giữ lại một (leave-one-out). Tổng quan 55 bài dùng KAt về cách chia tập (tr. 169881–169888, Bảng 1–6, 9). |
| Giới hạn | Xem mục 6. |
| Tác động K1/K2/K3 | K1: mở rộng (căn cứ thực nghiệm rằng **đơn vị dùng để chia dữ liệu** – lần chạy, ngày đo, chi tiết vật lý – quyết định ý nghĩa của con số hiệu năng; tác giả khuyến nghị báo cáo cụ thể cách chia, tr. 169892; và sửa chữa, thay chi tiết có thể tạo dịch chuyển miền, tr. 169885, 169889, 169892). K2: không liên quan trực tiếp (có ghi chú về vị trí cảm biến, mục 4). K3: không liên quan. |
| Vị trí sử dụng | 3.4 (rò rỉ do đơn vị chung; cấp chia dữ liệu); 5.6A (căn cứ cho đánh giá theo nhóm, giữ lại cả lần chạy, và cho trường `data_split`, `inference_unit` của `VALIDITY_SCOPE`); 5.7 (báo cáo cách chia tập; dùng nhiều cách chia để đo ảnh hưởng rò rỉ); 1.3A (đã trích). |
| Mức đã đọc | Toàn văn (01/10/2026) |

## 1. Bài toán và khung khái niệm

- (a) Bài toán đặt ra: chẩn đoán lỗi (FDD) cho **cả một quần thể** máy hay chi tiết cùng mẫu, đơn giản hóa thành bài toán
  phân loại trạng thái; ví dụ hệ kiểm tra chất lượng trên dây chuyền, kiểm tra tình trạng, thử hiện trường. Đây là các ứng
  dụng **không lập được đường cơ sở lành của chính hệ đang theo dõi** vì không có dữ liệu lịch sử (tr. 169879).
- (a) Máy giống nhau trên giấy vẫn khác nhau do lịch sử riêng và dung sai chế tạo, có thể tạo **dịch chuyển miền** (domain
  shift), tức phân bố của tập huấn luyện và tập kiểm tra khác nhau (tr. 169880, Hình 1). Dữ liệu rung của máy quay đã được
  thấy chứa thông tin nhận diện máy, có thể nhận diện tới số sê-ri; thông tin này có thể đến từ các chi tiết khác được coi
  là "lành" (tr. 169880).
- (a) Dịch chuyển miền do điều kiện vận hành, mẫu chi tiết, vị trí cảm biến đã được thừa nhận; bài tập trung vào trường hợp
  **không có** các nguyên nhân đã biết đó mà vẫn có dịch chuyển chưa biết (tr. 169880).
- (a) Liên hệ rò rỉ – dịch chuyển miền (tr. 169881): nếu nguồn dữ liệu phân biệt được và gắn với nhãn lớp, bộ phân loại có
  thể học nhận ra nguồn rồi gán nhãn theo nguồn, bỏ qua việc nhận ra trạng thái; khi đó để dữ liệu cùng nguồn ở cả hai tập là
  rò rỉ, vì bộ phân loại được kỳ vọng vận hành trên nguồn chưa thấy. Tác giả dẫn Kapoor & Narayanan 2023 (= [53] của tiểu
  luận; [68] trong bài) cho khái niệm rò rỉ và đánh giá lạc quan (tr. 169881, 169890).
- (a) Tác giả nói rõ bài **không** giải quyết dịch chuyển miền (tr. 169880).
- [NCS] Theo phân loại của [53] (tr. 4–5), cơ chế ở đây thuộc **L3.2 – không độc lập giữa tập huấn luyện và tập kiểm tra**
  (cùng đơn vị – cùng ổ, cùng ngày – ở cả hai tập), không phải L1 (tiền xử lý trên toàn bộ dữ liệu) hay L2 (đặc trưng không
  hợp lệ). Bài cũng đưa ra một dạng gần với L3.3 (tập kiểm tra không thuộc phân bố mà khẳng định hướng tới): khẳng định là
  "chẩn đoán trên ổ chưa thấy", nên tập kiểm tra phải là ổ chưa thấy (tr. 169890).

## 2. Bộ dữ liệu

### 2.1 CMHT (McMaster) — bộ dữ liệu đóng (tr. 169881, 169883–169885, Bảng 2)

- (a) Động cơ Belt-Starter Generator (BSG, FCA US LLC) trên bệ thử HT-250; lỗi nhân tạo khoan vào ổ thay thế (AM) SKF
  6305-2RS1/C3; ổ nguyên bản (OEM) SKF BB1-0890BA; bộ đầy đủ có hơn 20 tổ hợp tốc độ – tải từ 1000 đến 17000 vòng/phút; bài
  dùng tập con, loại các lỗi bôi trơn (tr. 169883–169884).
- (a) Hai gia tốc kế ba trục PCB 356A16, lấy mẫu 48 kHz: A1 ở bên phải khung BSG, A2 ở dưới bệ thử (tr. 169884, Hình 3b).
  Bộ dữ liệu có cả âm thanh, dòng, áp nhưng chỉ dùng rung (tr. 169884).
- (a) Bốn lớp: lành (AM-01, AM-02, AM-03, OEM-01, OEM-02); OR + BD (F3-01); IR + BD (F5-01); IR + OR (F7-01). Mỗi lớp lỗi
  chỉ có **một ổ**. 32 lần chạy, 19 ngày; số hiệu ngày không theo thứ tự thời gian (tr. 169884, Bảng 2).
- (a) Một lần chạy là một khoảng thu liên tục ở trạng thái ổn định trong một lần thử, khoảng 1 s, một tệp; giữa các lần chạy
  cùng ngày nghỉ tối thiểu 2 giờ; giữa các ngày từ hôm sau đến vài tuần (tr. 169885).
- (a) **Nguồn nhiễu đã biết** (tr. 169885): OEM-02 thu trên BSG-2 (động cơ thứ hai cùng mẫu), còn lại trên BSG-1; F3-01,
  F5-01, AM-02 và AM-01 (ngày 3, 4) thu trên BSG-1 **với rô-to mới sau một lần sửa chữa bắt buộc**; nhiệt độ ban đầu
  18–21 °C, đỉnh 55–65 °C; bản thân việc thay ổ có thể tạo biến động vì phải tháo một phần.

### 2.2 KAt (Paderborn) — bộ dữ liệu mở (tr. 169881, 169886–169888, Bảng 4–6)

- (a) Chọn vì có nhiều ổ riêng biệt nhất (32 chi tiết), có sáu ổ lành cùng mẫu, và gần CMHT nhất về điều kiện và loại dữ liệu
  (tr. 169881). Ổ 6203, bốn điều kiện vận hành; gia tốc kế gốc (A3) 64 kHz, lấy mẫu lại về 48 kHz (tr. 169886).
- (a) Tập con 14 ổ, chỉ ổ lành và lỗi nhân tạo có hơn một ổ cho mỗi tổ hợp hư hỏng: lành K001–K006; OR – khắc điện KA03, KA06,
  khoan KA08, KA09 (mức 2); IR – khắc điện KI03, KI05 (mức 1), KI07, KI08 (mức 2); ba lớp (tr. 169887–169888, Bảng 4).
  Không dùng ổ hư hỏng thực.

## 3. Quy trình và cách rò rỉ phát sinh

- (a) Quy trình (tr. 169883, Hình 2): lọc thông thấp Butterworth pha không; lấy mẫu lại 48 kHz; cửa sổ trượt 8192 mẫu
  (171 ms), bước 2048; phổ công suất FFT (cửa sổ Blackman) hoặc phổ bao (biến đổi Hilbert); đổi sang dB; bỏ 0 Hz và mọi tần
  số trên ngưỡng fc; chuẩn hóa; PCA, SPCA (α = 10, β = 1) hoặc LDA; SVM với C = 0,2, trọng số lớp cân bằng; scikit-learn 1.4.1.
  C được chọn tay trên một tập con nhỏ của CMHT; tác giả nói tham số có thể không tối ưu, giữ cố định để hạn chế yếu tố gây
  nhiễu (tr. 169883).
- (a) Mô hình không có thông tin điều kiện vận hành; huấn luyện và áp dụng **từng điều kiện vận hành một**, rồi lấy trung bình
  sai số (tr. 169883, 169886). Vì vậy điều kiện vận hành không bị trộn giữa hai tập (tr. 169888).
- (a) Sai số được lấy trung bình để mỗi ổ có trọng số bằng nhau trong lớp và mỗi lớp có trọng số bằng nhau (tr. 169884–169885,
  169887).
- **(a) Cơ chế rò rỉ:** các đoạn cắt từ cùng một tín hiệu có thể nằm ở cả tập huấn luyện và tập kiểm tra trong các cách chia
  phổ biến (tr. 169881); dữ liệu từ cùng một ổ tương quan quá mạnh để coi là mẫu độc lập, giả thiết độc lập cùng phân bố (iid)
  không đúng (tr. 169890); các bài dùng mã ổ làm nhãn lớp trên KAt đạt độ chính xác cao, tức đã vô tình cho thấy học máy nhận
  diện được từng ổ, kể cả ở điều kiện khác (tr. 169890).
- [NCS] Ba cấp nguồn có thể rò rỉ trong bài: **đoạn cùng lần chạy** (đã chặn ở mọi cách chia vì cả lần chạy được giữ lại),
  **cùng ngày đo** (chia theo lần chạy để lộ; chia theo ngày chặn được), **cùng chi tiết vật lý** (chia theo lần chạy và theo
  ngày đều để lộ trên CMHT, vì mỗi lớp lỗi chỉ có một ổ; chỉ chia theo chi tiết trên KAt chặn được). Điều kiện vận hành không
  phải nguồn rò rỉ trong thiết kế này vì đã tách riêng.

## 4. Các cách chia tập và ảnh hưởng đo được (số như tác giả báo cáo)

| Bộ dữ liệu | Cách chia | Định nghĩa (a) | Trang |
|---|---|---|---|
| CMHT | Theo lần chạy | Mọi đoạn của một lần chạy làm tập kiểm tra; 32 lần chạy (≈ 3 % dữ liệu kiểm tra) | 169885–169886 |
| CMHT | Theo ngày | Mọi đoạn của một ngày (1–2 lần chạy) làm tập kiểm tra; 19 ngày (tới 6 % dữ liệu) | 169886 |
| KAt | Theo lần chạy | Mọi đoạn của một tệp làm tập kiểm tra; 280 lần chạy | 169888, Bảng 5 |
| KAt | Theo chi tiết | Mọi đoạn của một ổ (mã ổ) làm tập kiểm tra; 14 ổ | 169888, Bảng 6 |

Dữ liệu kiểm tra không được dùng cho bất kỳ phần nào của huấn luyện (tr. 169886).

**CMHT** (tr. 169886, Bảng 3 — độ chính xác cao nhất, %; lần chạy / ngày):

| Đặc trưng | Phương pháp | A1 lần chạy | A1 ngày | A2 lần chạy | A2 ngày |
|---|---|---|---|---|---|
| Tần số | PCA | 96,73 | 94,73 | 88,58 | 84,53 |
| Tần số | SPCA | 98,28 | 96,18 | 96,95 | 91,50 |
| Tần số | LDA | 98,89 | 97,78 | 95,69 | 90,52 |
| Bao | PCA | 88,30 | 86,08 | 83,69 | 79,18 |
| Bao | SPCA | 95,16 | 90,96 | 92,16 | 84,94 |
| Bao | LDA | 95,92 | 91,18 | 89,54 | 80,54 |

- (a) Trong **mọi** trường hợp, chia theo lần chạy cho sai số thấp hơn chia theo ngày; chênh lệch sai số lớn nhất: PCA tới
  0,07, SPCA tới 0,09, LDA tới 0,17. Tác giả kết luận có biến động theo ngày trong dữ liệu làm sai số theo lần chạy thấp bất
  thường (tr. 169886).
- (a) A1 (gần ổ, tỉ số tín hiệu/nhiễu tốt hơn) cho kết quả tốt hơn A2; A2 có xu hướng chênh lệch lần chạy – ngày lớn hơn một
  chút (tr. 169886). Với A1 và phân tích tần số, mọi phương pháp có sai số tối đa 0,04 ở số đặc trưng lớn nhất (tr. 169886).
- (a) LDA có "bướu" sai số ở fc 2,5–4 kHz trên cả hai cách trích đặc trưng và hai cảm biến; tác giả cho là có thể do đặc trưng
  bị dịch chuyển miền ở dải đó (tr. 169886). PCA ở fc = 6000 Hz cho các cụm con trong lớp lành và OR-BD, có thể do nhiều ổ và
  động cơ thứ hai (tr. 169886, Hình 5).

**KAt** (tr. 169888, 169890, Bảng 8 — độ chính xác cao nhất, %; theo chi tiết / theo lần chạy):

| Quy trình | Theo chi tiết | Theo lần chạy |
|---|---|---|
| SVM-PCA-FFT | 60,92 | 93,97 |
| SVM-SPCA-FFT | 48,59 | 91,08 |
| SVM-LDA-FFT | 53,44 | 96,46 |
| SVM-PCA-EA | 58,58 | 91,35 |
| SVM-SPCA-EA | 52,67 | 74,79 |
| SVM-LDA-EA | 61,21 | 89,42 |

- (a) Với mọi phương pháp, sai số tăng mạnh khi chia theo chi tiết so với theo lần chạy (tới 0,47); sai số nhỏ nhất theo chi
  tiết là 0,39; bộ đoán ngẫu nhiên có sai số 0,67, nên SPCA chỉ nhỉnh hơn đoán ngẫu nhiên; PCA có sai số trung bình theo chi
  tiết tốt nhất trên mọi fc là 0,44, vẫn là kết quả kém (tr. 169888). Tóm tắt nói giảm hơn 40 % độ chính xác tùy cách chia
  (tr. 169879).
- (a) Chênh lệch theo chi tiết – theo lần chạy trên KAt lớn hơn nhiều so với chênh lệch theo ngày – theo lần chạy trên CMHT
  (tr. 169888). Nếu sai số chỉ do trộn lớp (như nhiễu đo), các cách chia phải cho sai số xấp xỉ nhau; vì không như vậy nên có
  dịch chuyển miền cho phép rò rỉ (tr. 169889).
- (a) Kết quả theo ngày trên CMHT cũng có thể bị rò rỉ vì cùng ổ thường có mặt ở cả hai tập; do thiếu ổ lỗi khác, không kết
  luận được mô hình đã học nhận ra trạng thái lỗi (tr. 169889–169890). Kết luận: dù kết quả CMHT với A1 rất tốt, không thể kết
  luận phương pháp nào đã nhận ra trạng thái lỗi (tr. 169892).
- (a) Thử duy nhất về khả năng tổng quát là chia theo chi tiết trên KAt, và hiệu năng rất kém ở mọi trường hợp (tr. 169891).
- (a) Bảng 7, 8 thu kết quả các bài khác; tác giả lưu ý không bài nào dùng đúng cách chia này nên không so sánh trực tiếp được
  (tr. 169888).
- **(a) Tổng quan cách chia trên KAt** (tr. 169881–169882, 169891; Bảng 1, 9): 55 bài trong 5 năm (loại học chuyển giao);
  Bảng 9: trộn chi tiết – chỉ KAt 10, trộn chi tiết – KAt và bộ khác 17, không rõ – chỉ KAt 5, không rõ – KAt và bộ khác 17,
  tách chi tiết 6. Mười bài "trộn chi tiết, chỉ KAt" là bất định nhất, cần kiểm lại; chỉ sáu bài "tách chi tiết" được coi là
  không bị ảnh hưởng (tr. 169891). Bài gốc của bộ KAt đã chia theo chi tiết nhưng các bài gần đây vẫn trộn (tr. 169891).
- [NCS] Thứ hạng phương pháp đổi theo cách chia: trên KAt, theo lần chạy LDA-FFT cao nhất (96,46) còn SPCA-FFT 91,08; theo
  chi tiết SPCA-FFT thấp nhất (48,59) còn LDA-EA cao nhất (61,21) (Bảng 8, tr. 169890). Đây là suy từ bảng, tác giả không bình
  luận riêng về đảo thứ hạng.

## 5. Khuyến nghị của tác giả

- **Khuyến nghị** (tr. 169892): thu dữ liệu mới với **nhiều chi tiết cho mỗi trạng thái** (kể cả lành) và chia chi tiết giữa
  tập huấn luyện và tập kiểm tra; trên KAt, không để mã ổ chung giữa hai tập và không dùng mã ổ làm nhãn lớp; dùng cách chia
  tái lập được trên bộ dữ liệu chuẩn; ưu tiên kỹ thuật có giám sát hơn không giám sát trong phương pháp FDD mới, vì kỹ thuật
  không giám sát có xu hướng giữ các nguồn phương sai không liên quan đến lớp.
- **Gợi ý** (tr. 169892): để thời gian nghỉ dài giữa các đợt thu (giờ, ngày); dùng **nhiều hơn một cách chia**; lọc bỏ thông
  tin tần số cao có thể giúp tổng quát; khi dùng tập con hay cách chia ít gặp, chạy kèm một bộ phân loại đơn giản (kNN, RF…)
  để cho thấy độ khó của bài toán.
- (a) Chia theo lần chạy vẫn có ích cho mục đích khác ngoài đánh giá mô hình (khắc phục sự cố, báo cáo nhất quán, so sánh);
  có thể so với các cách chia khác để kiểm ảnh hưởng của rò rỉ (tr. 169890–169891).
- (a) So sánh giữa các loại cảm biến bằng học máy không mô hình phải tính tới rò rỉ của từng loại; rung có thể **có vẻ** là
  nguồn tốt hơn chỉ vì hiệu năng bị rò rỉ thổi phồng (tr. 169891).
- (a) Thêm đặc trưng một cách mù quáng không phải lúc nào cũng có lợi, vì có thể đưa vào thêm đặc trưng bị dịch chuyển miền
  (tr. 169891). Kỹ thuật dựa trên mô hình có thể thích hợp hơn kỹ thuật không mô hình vì lý do này (tr. 169891).
- (a) Hướng xử lý có thể: loại đặc trưng bị dịch chuyển (lọc/chọn đặc trưng) hoặc thích nghi miền; việc dùng kỹ thuật bổ sung
  không bỏ được nhu cầu kiểm chứng mô hình trên nguồn dữ liệu mới (tr. 169891).
- (a) Kết luận (tr. 169892): kiểm chứng trên nguồn dữ liệu mới (nhiều chi tiết mỗi lớp, thay các chi tiết khác, nhiều máy);
  khuyến khích **báo cáo cụ thể cách chia tập** và tránh chia ngẫu nhiên để tái lập được. Hướng tiếp theo gồm: kỹ thuật phát
  hiện và đo dịch chuyển miền trong dữ liệu rung; dịch chuyển miền trong quần thể máy lành; **ảnh hưởng của sửa chữa và/hoặc
  thay chi tiết tới dịch chuyển miền**; mức dịch chuyển ở các loại cảm biến khác.
- (a) Mức giảm khi chuyển từ tập hư hỏng thực sang tập nhân tạo/thực trên KAt thường được quy cho khác biệt hư hỏng thực –
  nhân tạo, nhưng cũng có thể do tính riêng của từng ổ (tr. 169892).

## 6. Giới hạn

**(b) Tác giả tự nêu:**
- Bài không xử lý hay nghiên cứu cách giải quyết dịch chuyển miền (tr. 169880); việc xác định trường hợp nào (đặc trưng
  dịch chuyển có hay không cần cho phân loại) vượt phạm vi bài (tr. 169891).
- Tham số có thể không tối ưu cho bài toán, bộ dữ liệu hay từng lần chia (tr. 169883).
- Chỉ xét dữ liệu rung; dịch chuyển miền ở dòng, áp chưa được kiểm (tr. 169891).
- CMHT thiếu ổ lỗi bổ sung nên không kết luận được mô hình đã học trạng thái lỗi (tr. 169889–169890).
- Chưa biết dạng khoảng cách miền của KAt có ở bộ dữ liệu khác không; phần lớn bộ dữ liệu chỉ có một chi tiết mỗi lớp; thiếu dữ
  liệu đa dạng nên khó ước lượng phạm vi vấn đề (tr. 169892).
- Bệ thử CMHT không mô-đun, việc thay ổ cần tháo một phần, có thể đã góp phần vào khác biệt trong CMHT (tr. 169889).
- Kiểm chứng trên nhiều chi tiết, nhiều máy thường khó vì chi phí và thời gian (tr. 169892).

**[NCS] nhận định:**
- **Đối tượng là ổ lăn máy quay**, không phải kết cấu; kích thích là chính chuyển động quay ở trạng thái ổn định, không có
  biến động môi trường – vận hành kiểu công trình. Việc áp sang kết cấu thép là diễn giải.
- Bài toán của tác giả là **tổng quát sang chi tiết chưa thấy trong quần thể**, ứng với trường hợp không có đường cơ sở của
  chính hệ (tr. 169879). Hướng hiện trường của luận án (WP3, Autoencoder trên đường cơ sở vận hành của chính công trình) có
  đơn vị suy luận khác: cùng một công trình theo thời gian. Ở đó nguồn rò rỉ tương ứng không phải "chi tiết" mà là **khoảng thời
  gian và sự kiện can thiệp**; bài chỉ gợi ý điều này qua ý sửa chữa, thay chi tiết (tr. 169885, 169889, 169892).
- Bảng 3 và 8 báo cáo **độ chính xác cao nhất trên các giá trị fc** (tr. 169886, 169890); chọn fc theo kết quả kiểm tra là một
  dạng chọn mô hình trên tập kiểm tra, làm cả hai cách chia lạc quan (chênh lệch giữa hai cách chia vẫn có ý nghĩa so sánh).
  C chọn tay trên một tập con của CMHT (tr. 169883), không nói tập con đó có trùng dữ liệu đánh giá hay không.
- Không báo cáo biến thiên theo lượt giữ lại (chỉ đường trung bình và cực đại), không có khoảng tin cậy hay kiểm định thống kê
  cho chênh lệch giữa các cách chia.
- CMHT: mỗi lớp lỗi một ổ, và các ổ lỗi được thu sau lần thay rô-to (tr. 169885), nên trạng thái lỗi trùng một phần với "sau
  sửa chữa"; tác giả nêu yếu tố nhiễu này nhưng không tách định lượng.
- CMHT là bộ dữ liệu đóng (tr. 169881), không kiểm lại được độc lập.
- Ba lớp tương ứng sai số ngẫu nhiên 0,67 trên KAt (tr. 169888) là phép tính của tác giả, khớp với ba lớp ở Bảng 4.
- **Không nhất quán nội bộ:** tr. 169882 viết "22 bài không đủ thông tin … trong **ba mươi hai** bài còn lại chỉ sáu bài tách
  chi tiết", nhưng 55 − 22 = 33, và Bảng 9 (tr. 169891) cho 10 + 17 + 6 = 33 bài xác định được. Tóm tắt nói "mười bài có khả năng
  bị ảnh hưởng" (tr. 169879), ứng với nhóm "trộn chi tiết – chỉ KAt"; tổng số bài trộn chi tiết theo Bảng 9 là 27. Khi trích, dùng
  số theo Bảng 9 và ghi rõ nhóm.
- Tóm tắt nói hai bộ dữ liệu dùng "ba cách chia" (tr. 169879), nhưng mỗi bộ chỉ dùng hai cách (CMHT: lần chạy, ngày; KAt: lần
  chạy, chi tiết; tr. 169885–169888). Không mâu thuẫn về số liệu, chỉ cần viết đúng khi trích.

## 7. Đoạn dùng được cho tiểu luận

| Luận điểm | Trang | Loại |
|---|---|---|
| Dữ liệu rung có thể chứa dấu vết riêng của từng chi tiết, máy, ngày đo; khi cùng nguồn có ở cả hai tập, bộ phân loại có thể học nhận ra nguồn thay vì trạng thái, gây rò rỉ và hiệu năng lạc quan | 169880–169881, 169890 | Trực tiếp (đối tượng: ổ lăn) |
| Đổi đơn vị chia dữ liệu từ lần chạy sang chi tiết làm sai số tăng tới 0,47 (KAt); từ lần chạy sang ngày làm sai số tăng tới 0,17 (CMHT, LDA) | 169886, 169888–169889 | Trực tiếp |
| Dữ liệu từ cùng một chi tiết tương quan quá mạnh để coi là mẫu độc lập; giả thiết iid không đúng | 169890 | Trực tiếp |
| Trong 55 bài dùng bộ KAt, 27 bài trộn chi tiết giữa hai tập, 22 bài không đủ thông tin để xác định, chỉ 6 bài tách chi tiết | 169881–169882, 169891 (Bảng 9) | Trực tiếp (dùng số Bảng 9) |
| Tác giả khuyến nghị báo cáo cụ thể cách chia tập, dùng cách chia tái lập được và dùng nhiều hơn một cách chia | 169892 | Trực tiếp |
| Vị trí cảm biến ảnh hưởng tới hiệu năng trong cùng giao thức (A1 tốt hơn A2) | 169886 (Bảng 3), 169889 | Trực tiếp (đã dùng ở 3.3, `03_chuong3.md`) |
| So sánh giữa loại cảm biến có thể bị rò rỉ làm sai lệch; một nguồn có thể có vẻ tốt hơn chỉ vì hiệu năng bị thổi phồng | 169891 | Trực tiếp |
| Thứ hạng phương pháp đổi theo cách chia | 169890 (Bảng 8) | Diễn giải [NCS]; câu "so sánh kiến trúc dưới giao thức chưa kiểm soát rò rỉ có thể cho kết luận không ổn định" (`03_chuong3.md`) nên ghi là diễn giải hoặc dựa vào ý tr. 169891 về so sánh cảm biến |
| Sửa chữa (thay rô-to) và thay ổ có tháo một phần được tác giả nêu là nguồn biến động có thể tạo dịch chuyển miền; ảnh hưởng của sửa chữa, thay chi tiết là hướng nghiên cứu tiếp | 169885, 169889, 169892 | Trực tiếp (máy quay); áp cho can thiệp ở mối nối bu lông là diễn giải |
| Kiểm chứng trên nguồn dữ liệu mới là cần dù đã dùng kỹ thuật thích nghi | 169891–169892 | Trực tiếp |

Kiểm câu đang có trong bản thảo: `01_chuong1.md` (1.3A) và `03_chuong3.md` ("đổi cấp nguồn vật lý dùng để chia dữ liệu là
hiệu năng thay đổi mạnh") được tr. 169886–169889 ủng hộ. Bảng ở `03_chuong3.md` ghi "Lần chạy, ngày đo, chi tiết vật lý": đúng
cho cả bài, nhưng mỗi bộ dữ liệu chỉ dùng hai cấp. Câu `03_chuong3.md` "ngay cả khi đã tách theo lần chạy, dữ liệu vẫn có thể
chia sẻ cùng ngày đo hoặc cùng chi tiết vật lý" được tr. 169886, 169889–169890 ủng hộ.

## 8. Kiểm phản chứng

- **UV-02 (nguồn gốc, phiên bản phương pháp, phạm vi hiệu lực của đầu ra phát hiện): không giải quyết.**
  - Đầu ra là độ chính xác và sai số tổng hợp của từng quy trình (tr. 169886, 169888–169890); không có bản ghi nguồn gốc xử lý,
    phiên bản phương pháp hay phạm vi hiệu lực cho từng kết quả. Tác giả có ghi phiên bản thư viện (scikit-learn 1.4.1) và tham
    số trong văn bản (tr. 169883), ở mức bài báo.
  - Khuyến nghị "báo cáo cụ thể cách chia tập", "cách chia tái lập được", "nhiều hơn một cách chia" (tr. 169892) là tiền lệ ở
    **mức báo cáo của bài nghiên cứu**, cùng nhóm với phiếu thông tin mô hình của [53] (tr. 5–6), không phải bản ghi đi theo
    từng kết quả khi dùng về sau. Phát biểu đã thu hẹp của UV-02 không đổi.
  - Bổ sung cho **nội dung** phạm vi hiệu lực (cùng nhóm Figueiredo 2011, [45], Worden 2007, Cawley 2018): hiệu năng chỉ có
    nghĩa gắn với đơn vị chia dữ liệu (lần chạy / ngày / chi tiết), tr. 169886–169890; TG. Đây là căn cứ trực tiếp cho hai trường
    `inference_unit`, `data_split`. Không tính vào số căn cứ của phát biểu "chưa được ghi".
- **UV-06 (lần lắp ráp hoặc can thiệp là ranh giới phạm vi hiệu lực của bằng chứng từ mối nối bu lông): không giải quyết; có
  căn cứ cùng chiều gián tiếp.**
  - Bài không xét mối nối bu lông hay kết cấu. Tác giả nêu thay rô-to sau sửa chữa và thay ổ có tháo một phần là nguồn biến
    động có thể tạo dịch chuyển miền (tr. 169885, 169889), và đưa "ảnh hưởng của sửa chữa và/hoặc thay chi tiết tới dịch chuyển
    miền" vào hướng nghiên cứu tiếp (tr. 169892); TG. [NCS] Điều này cùng chiều với tiền đề vật lý của UV-06 (can thiệp làm đổi
    phân bố dữ liệu) và cho thấy ngay trong lĩnh vực máy quay vấn đề còn mở; nhưng đối tượng khác (máy quay, không phải mối nối)
    và tác giả không tách định lượng ảnh hưởng của sửa chữa.
  - Bài không có cơ chế ghi sự kiện sửa chữa, thay chi tiết thành ranh giới phạm vi hiệu lực; các yếu tố này chỉ được kể trong
    văn bản mô tả dữ liệu (tr. 169885).
  - Đề nghị: ghi [15] vào UV-06 như **căn cứ gián tiếp, khác đối tượng** (tr. 169885, 169889, 169892), không tính vào số căn cứ độc
    lập trước 2025 về mối nối bu lông. Có thể dẫn kèm [53] cho cơ chế rò rỉ do đơn vị chung.
- Tác động tới UV khác (ghi chú, không yêu cầu): UV-03 (ghép cảm biến – cấu kiện có thời hạn) — bài cho thấy vị trí cảm biến đổi
  hiệu năng (tr. 169886, 169889) nhưng không bàn ghép cảm biến – chi tiết theo thời gian; không giải quyết, không liên quan trực tiếp.
