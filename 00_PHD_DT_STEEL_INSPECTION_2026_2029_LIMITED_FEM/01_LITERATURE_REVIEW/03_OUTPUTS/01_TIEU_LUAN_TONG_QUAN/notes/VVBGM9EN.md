# VVBGM9EN — Eraliev, Lee & Lee (2022)

Eraliev O, Lee K-H, Lee C-H. Vibration-Based Loosening Detection of a Multi-Bolt Structure Using Machine Learning
Algorithms. *Sensors* 22(3): 1210 (14 tr.), 2022. DOI 10.3390/s22031210. Nhận 07/01/2022, chấp nhận 02/02/2022, đăng
05/02/2022; biên tập viên Mohammad Noori; © 2022 các tác giả, MDPI, giấy phép CC BY (tr. 1). Tác giả thuộc Inha University,
Incheon, Hàn Quốc (Khoa Kỹ thuật xe tương lai; Khoa Cơ khí); tác giả liên hệ Chul-Hee Lee (tr. 1). Thông tin thư mục kiểm
theo trang 1 (khối "Citation" và chân trang). [NCS] Số 3 của tập 22 lấy từ hậu tố DOI (s22031210); trang 1 chỉ in
"Sensors 2022, 22, 1210".

**Bản đã đọc:** bản chính thức của nhà xuất bản (MDPI, truy cập mở), tệp Zotero `C:/Users/VNT/Zotero/storage/B3KTWLGI/Eraliev
et al. - 2022 - Vibration-Based Loosening Detection of a Multi-Bolt Structure Using Machine Learning Algorithms.pdf`,
14 tr. Trang dẫn là **trang in "x of 14"**, trùng với trang PDF. Đọc toàn văn (gồm danh mục tài liệu) ngày 01/10/2026, kiểm
phản chứng UV-08 (trước đó chỉ đọc tóm tắt, xem `revision/GD2_nhat_ky_khoang_trong.md` mục UV-08) và UV-06.

Ký hiệu: (a) điều tác giả nói; (b) giới hạn tác giả tự nêu; **[NCS]** nhận định của NCS.

| Cột | Nội dung |
|---|---|
| Citekey / Số cũ | VVBGM9EN / mới (phanchung-GD2) |
| Tier / Cụm | Bổ sung phản chứng (không thuộc 30 key) / SHM–bu lông–EOV (phần chia dữ liệu: Độ tin cậy đánh giá) |
| Luận điểm | Phương pháp dựa trên dao động: đặc trưng biến đổi Fourier thời gian ngắn (STFT) của tín hiệu gia tốc đưa vào bộ phân loại học máy có giám sát phát hiện lỏng bu lông ở giai đoạn sớm (giảm 6 N·m mô-men siết) và chỉ ra bu lông nào bị lỏng, cho một động cơ AC bắt bằng bốn bu lông M8 lên gối cố định; Random Forest được chọn với độ chính xác khoảng 95,8 % (tr. 1, 5, 11–12). |
| Bằng chứng | Một bệ thí nghiệm: động cơ servo AC 1,8 kW, bốn bu lông M8 × 1,5 cấp 8.8; 16 ca tổ hợp bu lông siết (25 N·m) / lỏng (19 N·m); khối lệch tâm 0,25 kg gắn rotor; ba tốc độ 800, 1000, 1200 vòng/phút; hai gia tốc kế một trục, khoảng 30 s mỗi lần ghi, 10 kHz; bảy bộ phân loại sklearn; chia 80/20 sau trích đặc trưng, mỗi cửa sổ STFT là một mẫu (tr. 4–7; Bảng 1–3). |
| Giới hạn | Xem mục 6. |
| Tác động K1/K2/K3 | K1: mở rộng (cách chia theo cửa sổ của cùng lần ghi; không báo kết quả riêng theo tốc độ hay kiểm chéo tốc độ; không khai báo phạm vi hiệu lực). K2, K3: không liên quan. |
| Vị trí sử dụng | 3.3 (ví dụ học máy trên đặc trưng STFT cho lỏng bu lông, đối tượng là máy chứ không phải kết cấu nhà); 3.4 (ví dụ chia tập theo cửa sổ của cùng bản ghi và chọn đặc trưng, vị trí cảm biến theo độ chính xác kiểm tra — [NCS]); 3.2 hoặc 3.6 chỉ ở mức "tốc độ vận hành được dùng để tăng dữ liệu, chưa được xử lý như biến bù". |
| Mức đã đọc | Toàn văn (01/10/2026) |

## 1. Bệ thí nghiệm và cách tạo trạng thái lỏng (a)

- Đối tượng: một động cơ AC (HIGEN AC Servo Motor FMATN20-AB00, 1,8 kW, mô-men 11,5 N·m, tốc độ tối đa 1500 vòng/phút) bắt
  bằng **bốn bu lông thép M8 × 1,5 cấp bền 8.8** lên một gối cố định (tr. 1, 5–6; Bảng 1; Hình 2a–b). Tác giả gọi đây là
  "kết cấu nhiều bu lông" (multi-bolt structure) (tr. 1, 2). [NCS] Đây là liên kết bệ máy, không phải liên kết kết cấu
  khung thép; hình 2 cho thấy động cơ đặt trên bệ thí nghiệm, bài không mô tả kết cấu đỡ.
- Mức siết: mô-men lớn nhất cho M8 × 1,5 cấp 8.8 là 27,5 N·m; **25 N·m = siết chặt (lành)**, **19 N·m = lỏng (không
  lành)**; khi mô-men chỉ giảm dưới 6 N·m (ví dụ 4 hoặc 5 N·m) các bộ phân loại không phát hiện được, nên mức giảm 6 N·m được
  coi là bắt đầu giai đoạn lỏng sớm (tr. 5). Siết bằng cờ lê lực Tohnichi 450QL3, độ chính xác ±3 % (tr. 5, Hình 2c).
- 16 ca (tr. 7, Bảng 2): ca #1 cả bốn bu lông siết; các ca #2–#16 là các tổ hợp một, hai, ba hoặc bốn bu lông lỏng (ca #12
  cả bốn lỏng). [NCS] 16 ca = 2⁴ tổ hợp, nên bài toán là phân loại 16 lớp có kiểm soát.
- Kích thích: khối lệch tâm 0,25 kg gắn vào rotor để tạo dao động (tr. 5). [NCS] Kích thích là do chính máy tạo ra, có chu kỳ,
  không phải rung nền từ nguồn bên ngoài.
- (a) Bài **không** mô tả thứ tự đổi ca, việc tháo – siết lại giữa các ca, hay số lần lặp lại việc lắp đặt cho cùng một ca.
  [NCS] Từ mô tả "khoảng 30 s" mỗi lần ghi (tr. 5) và việc không nêu lặp, mỗi ca ở mỗi tốc độ có vẻ chỉ có một lần ghi; điều
  này không được tác giả khẳng định.

## 2. Điều kiện vận hành: "ba tốc độ" (a)

- Động cơ trước hết chạy ở 800 vòng/phút; "để tăng độ tin cậy của phương pháp", tín hiệu cũng được thu ở 1000 và 1200
  vòng/phút (tr. 5–6). Tóm tắt nêu ba điều kiện làm việc được dùng "để thu đủ dữ liệu dao động" (tr. 1); phần mở đầu nêu
  tương tự (tr. 2).
- Tóm tắt khẳng định bộ phân loại phát hiện và nhận dạng bu lông lỏng "trong mỗi điều kiện làm việc" (tr. 1).
- (a) Trong phần kết quả, Hình 3 (tín hiệu thô) là của cảm biến 2 **ở 800 vòng/phút** (tr. 7); các Hình 5, 6, 8, 9, 10
  không ghi tốc độ (tr. 9–12). **Không có bảng hay hình nào báo kết quả riêng cho từng tốc độ**, và không có thử nghiệm huấn
  luyện ở một tốc độ, kiểm tra ở tốc độ khác (đọc toàn bộ tr. 7–12).
- [NCS] Vì vậy không xác định được từ văn bản ba tốc độ được gộp chung vào một tập dữ liệu hay phân tích riêng. Tổng các
  hàng của ma trận nhầm lẫn (Hình 10, tr. 12) do NCS cộng là khoảng 6850 cửa sổ kiểm tra; một bản ghi 30 s ở 10 kHz với bước
  nhảy 512 cho khoảng 586 cửa sổ, tức khoảng 1875 cửa sổ kiểm tra cho 16 ca ở một tốc độ (20 %). Con số trong Hình 10 lớn hơn
  nhiều mức một tốc độ, gợi ý dữ liệu đã được gộp (hoặc bản ghi dài hơn), nhưng không khớp chính xác; đây chỉ là suy luận số
  học của NCS, không dùng làm dữ kiện.
- [NCS] Lời khẳng định "trong mỗi điều kiện làm việc" ở tóm tắt (tr. 1) không có kết quả tương ứng trong thân bài.

## 3. Cảm biến và thu dữ liệu (a)

- Hai gia tốc kế một trục Brüel & Kjær 4507B004: cảm biến 1 đặt trên nóc động cơ, trục song song trục rotor; cảm biến 2 đặt
  mặt sau động cơ, trục vuông góc trục rotor (tr. 5, Hình 2b). Thu bằng NI cDAQ-9174, LabVIEW, tần số lấy mẫu 10.000 mẫu/s,
  ghi khoảng 30 s (tr. 5).
- Hầu hết bộ phân loại chính xác hơn với cảm biến 2 (trừ SVM); tác giả kết luận vị trí cảm biến ảnh hưởng đáng kể và chọn
  cảm biến 2 cho mọi kết quả sau (tr. 7–8, Hình 5).

## 4. Đặc trưng, mô hình và cách chia dữ liệu (a)

- Đặc trưng: STFT bằng thư viện librosa (Python), cửa sổ Hann, n_fft = 1024, bước nhảy 512; lấy giá trị tuyệt đối; ma trận
  513 × số cửa sổ; **số cửa sổ được dùng làm số mẫu huấn luyện, hệ số FFT của mỗi cửa sổ là đặc trưng** (tr. 4).
- **Chia dữ liệu:** "Sau khi trích đặc trưng, dữ liệu được chia 80 % huấn luyện và 20 % kiểm tra. Mỗi thí nghiệm được thực
  hiện 20 lần và dùng giá trị trung bình" (tr. 4). Lưu đồ (Hình 1) mô tả cùng trình tự: trích đặc trưng → chia tập huấn
  luyện/kiểm tra (tr. 3). Bài không nói chia ngẫu nhiên hay theo khối thời gian, không có tập kiểm định riêng, không kiểm
  chứng chéo, không nêu cách chọn siêu tham số.
- [NCS] Vì đơn vị mẫu là cửa sổ STFT (chồng 50 % do bước nhảy 512 với n_fft 1024) và chia sau khi trích đặc trưng, các cửa sổ
  kề nhau của **cùng một bản ghi, cùng lần siết bu lông** nằm ở cả tập huấn luyện và tập kiểm tra. Đây là chia theo bản ghi/cửa
  sổ, **không** theo lần ghi, không theo lần lắp đặt, không theo tốc độ. Theo L3.2 của [53] Kapoor & Narayanan 2023 (tr. 4–5),
  đơn vị chung giữa hai tập là rò rỉ dữ liệu. Tóm tắt nói "một tập kiểm tra mới" được dùng (tr. 1), nhưng phần phương pháp
  chỉ mô tả chia 80/20 từ cùng tập đặc trưng (tr. 3–4).
- Mô hình (sklearn, tr. 7, Bảng 3): Random Forest, Bagged Trees, Decision Tree, K-Nearest Neighbors, LDA, SVM, XGBoost; mô
  tả ngắn ở tr. 5.
- Giảm đặc trưng: phổ được "phóng to", thấy đặc trưng chính nằm ở 0–5 Hz; chọn 0–5 Hz thì độ chính xác giảm mạnh; tăng dần
  từng 5 Hz "cho đến khi có kết quả thỏa mãn"; tốt nhất ở 0–25 Hz (tr. 9, Hình 7), dùng 25 đặc trưng (tr. 11, Hình 8).
  [NCS] (i) Dải tần và vị trí cảm biến được chọn theo độ chính xác trên tập kiểm tra — không có tập kiểm định riêng — nên kết
  quả cuối mang thiên lệch chọn mô hình (Cawley & Talbot; [14]). (ii) Với 10 kHz và n_fft 1024, mỗi hệ số FFT cách nhau khoảng
  9,8 Hz, nên 25 hệ số đầu tương ứng khoảng 0–240 Hz chứ không phải 0–25 Hz; văn bản (tr. 9, 12) và số đặc trưng (tr. 11)
  không khớp nhau. NCS không tự sửa; ghi là chỗ không nhất quán.

## 5. Kết quả (chỉ như tác giả báo cáo)

- Với 513 đặc trưng (cảm biến 2): RF, Bagged Trees, XGBoost có độ chính xác trên 90 % (tr. 8, Hình 5). Thời gian huấn luyện
  (Hình 6, tr. 9): RF 79,3 s; Bagged Trees 184,7 s; Decision Tree 32,7 s; KNN 4,35 s; LDA 4,2 s; SVM 626,1 s; XGBoost 675,6 s.
- Với 25 đặc trưng (Hình 8, tr. 11): RF 95,8 %; Bagged Trees 92,2 %; Decision Tree 87,5 %; KNN 90,1 %; LDA 30,8 %; SVM 7,1 %;
  XGBoost 96,1 %. Thời gian huấn luyện (Hình 9, tr. 11): RF 16,4 s; Bagged Trees 8 s; Decision Tree 1,5 s; KNN 0,2 s; LDA 0,2 s;
  SVM 86,3 s; XGBoost 53,9 s. RF được chọn cho nghiên cứu giám sát trực tuyến sau này (tr. 11, 12).
- Ma trận nhầm lẫn RF (Hình 10, tr. 12): ca #15 khó nhất (87,1 %), ca #1 dễ nhất (khoảng 98,3 %); ca #5, #10, #16 trên 90 %
  một chút.
- Kết luận (tr. 12): chọn 0–25 Hz làm đặc trưng; vị trí cảm biến ảnh hưởng độ chính xác; RF khoảng 95,8 %, huấn luyện khoảng
  16 s; phát hiện được lỏng và nhận ra bu lông nào bắt đầu mất lực căng trước.
- **Hiệu năng có giữ được ở tốc độ chưa thấy khi huấn luyện không?** Bài **không kiểm**. Không có kết quả theo từng tốc độ, không
  có thử nghiệm huấn luyện ở một hay hai tốc độ và kiểm tra ở tốc độ còn lại (tr. 7–12). [NCS] Tốc độ vận hành được dùng để
  tăng lượng dữ liệu (tr. 1, 5–6), không được xử lý như một biến môi trường – vận hành cần bù hay cần tách khỏi tập kiểm tra.

## 6. Giới hạn

- (b) Tác giả nêu hướng tiếp theo: tối ưu vị trí cảm biến, phát triển mô hình RF để tăng độ chính xác, và áp dụng giám sát
  trực tuyến cho động cơ **trong điều kiện thực** (tr. 12) — tức kết quả hiện tại là trong phòng thí nghiệm. Mức giảm mô-men
  dưới 6 N·m không phát hiện được (tr. 5). Độ chính xác là biến tổng hợp, không chỉ ra lỗi cụ thể, nên dùng thêm ma trận nhầm
  lẫn (tr. 12).
- (b) Về các kỹ thuật dựa trên cảm biến nói chung: cần cảm biến cố định và hệ thống chi phí cao (tr. 2).
- **[NCS]** Đối tượng là bệ máy (một động cơ, bốn bu lông), không phải liên kết của kết cấu nhà; kích thích do chính máy tạo ra
  bằng khối lệch tâm, không có rung nền từ nguồn khác (cầu trục, máy lân cận), không có biến động nhiệt độ hay tải.
- **[NCS]** Chia theo cửa sổ STFT của cùng bản ghi, sau trích đặc trưng; tập huấn luyện và kiểm tra cùng lần siết, cùng lần ghi;
  không chia theo lần lắp đặt, theo lần ghi hay theo tốc độ; kết quả do đó là trong phạm vi một lần lắp cho mỗi ca.
- **[NCS]** Dải tần và vị trí cảm biến chọn theo độ chính xác kiểm tra; không có tập kiểm định, không kiểm chứng chéo, không báo
  biến thiên (chỉ nói trung bình 20 lần, tr. 4); không nêu siêu tham số; "Data Availability Statement: Not applicable" (tr. 13),
  dữ liệu không công bố.
- **[NCS]** Chỗ không nhất quán: "0–25 Hz" so với 25 hệ số FFT (tr. 9, 11); "tập kiểm tra mới" ở tóm tắt (tr. 1) so với chia
  80/20 ở phương pháp (tr. 4); lời khẳng định "trong mỗi điều kiện làm việc" (tr. 1) không có kết quả riêng theo tốc độ.

## 7. Đoạn dùng được cho tiểu luận

| Luận điểm trong tiểu luận | Trang | Loại |
|---|---|---|
| Học máy trên đặc trưng STFT của gia tốc đã được thử để phát hiện lỏng bu lông sớm (giảm 6 N·m) và nhận dạng bu lông lỏng ở bệ động cơ bốn bu lông trong phòng thí nghiệm | 1, 5, 11–12 | trực tiếp |
| Vị trí cảm biến ảnh hưởng độ chính xác phát hiện lỏng bu lông | 7–8, 12 | trực tiếp |
| Kiểm tra bằng mắt khó phát hiện lỏng sớm; gõ búa bị nhiễu môi trường và tốn thời gian khi có nhiều bu lông | 1–2 | trực tiếp (tác giả tổng quan, dẫn [2], [3]) |
| Tác giả tự nêu việc áp dụng trong điều kiện thực là bước sau | 12 | trực tiếp |
| Nhiều tốc độ vận hành được dùng để tăng dữ liệu, chưa được xử lý như biến cần bù hay kiểm chéo | 1, 5–6, 7–12 | diễn giải của NCS |
| Tập kiểm tra chia theo cửa sổ của cùng bản ghi, cùng lần siết — ví dụ cho rủi ro đánh giá lạc quan | 3–4 | diễn giải của NCS (dựa trên mô tả tr. 4) |

[NCS] Không dùng bài này làm căn cứ cho luận điểm về nhà xưởng khung thép hay về rung do cầu trục.

## 8. Kiểm phản chứng

- **UV-08 (ảnh hưởng của rung vận hành lên phát hiện suy giảm liên kết trong nhà xưởng khung thép chưa được nghiên cứu bằng dữ
  liệu hiện trường): không giải quyết.** Bài có lỏng bu lông dưới nhiều tốc độ vận hành, nhưng: (i) đối tượng là bệ động cơ bốn
  bu lông, không phải liên kết khung nhà (tr. 1, 5); (ii) dữ liệu phòng thí nghiệm, tác giả tự nêu điều kiện thực là bước sau
  (tr. 12); (iii) rung vận hành là do chính máy được giám sát tạo ra bằng khối lệch tâm (tr. 5), không phải rung từ cầu trục hay
  máy khác truyền vào kết cấu; (iv) ba tốc độ dùng để tăng dữ liệu (tr. 1, 5–6), không có kết quả theo tốc độ hay kiểm tra ở tốc
  độ chưa thấy (tr. 7–12), nên bài không đo **ảnh hưởng** của điều kiện vận hành lên phát hiện. Kết luận ở mức tóm tắt trong
  nhật ký ("lỏng bu lông dưới nhiều tốc độ vận hành, máy") được xác nhận và thu hẹp thêm: bài không phải phản chứng, và cũng
  không phải căn cứ riêng cho nhà xưởng. [NCS] Có thể dùng như ví dụ cùng chiều (gián tiếp) rằng ngay trong nghiên cứu lỏng bu
  lông có nhiều điều kiện vận hành, điều kiện vận hành chưa được đưa vào cách đánh giá (tr. 4, 7–12); không tính là căn cứ độc
  lập. Với UV-08 còn lại Hu 2023 chưa đọc toàn văn.
- **UV-06 (lần lắp ráp hoặc can thiệp bảo trì là ranh giới phạm vi hiệu lực của bằng chứng từ mối nối bu lông): không giải
  quyết.** Bài không mô tả tháo – siết lại giữa các ca, không lặp lại việc lắp đặt, không kiểm tra trên một lần lắp khác (tr. 5–7);
  tập kiểm tra là cửa sổ của cùng bản ghi với tập huấn luyện (tr. 4). [NCS] Kết quả 95,8 % (tr. 11) vì vậy chỉ có hiệu lực trong
  phạm vi lần lắp của mỗi ca; bài là thêm một ví dụ cho hiện tượng UV-06 mô tả (lần lắp không được ghi thành ranh giới phạm vi
  hiệu lực), cùng chiều gián tiếp, không tính là căn cứ độc lập (không có dữ liệu về việc lắp lại).
