# SL6IEB2E — Pal, Sikdar & Banerjee (2022) [48]

Pal J, Sikdar S, Banerjee S. A deep-learning approach for health monitoring of a steel frame structure with bolted
connections. *Structural Control and Health Monitoring* 29(2): e2873 (13 tr.), 2022. DOI 10.1002/stc.2873.
Nhận 20/10/2020, sửa 04/08/2021, chấp nhận 30/09/2021; © 2021 John Wiley & Sons (tr. 1). Hình 1 được đính chính ngày
10/11/2021 sau khi đăng trực tuyến lần đầu (thiếu nhãn hình; tr. 3). Thông tin thư mục kiểm theo trang 1 và dòng
"How to cite" (tr. 13).

**Bản đã đọc:** bản in của nhà xuất bản (Wiley), tệp Zotero `C:/Users/VNT/Zotero/storage/FWA4939P/Pal et al. - 2022 - A
deep-learning approach for health monitoring of a steel frame structure with bolted connections.pdf`, 13 tr. Trang dẫn là
**trang in "x of 13"**, trùng với trang PDF. Đọc toàn văn (gồm danh mục tài liệu) ngày 01/10/2026, phiên T2-2.

Ký hiệu: (a) điều tác giả nói; (b) giới hạn tác giả tự nêu; **[NCS]** nhận định của NCS.

| Cột | Nội dung |
|---|---|
| Citekey / Số cũ | SL6IEB2E / 48 |
| Tier / Cụm | Tier 2 / SHM–bu lông–EOV (phần đánh giá: Độ tin cậy đánh giá) |
| Luận điểm | Mạng nơ-ron tích chập (CNN) nhận ảnh phổ thời gian – tần số (scalogram, biến đổi wavelet liên tục) của tín hiệu biến dạng sau va đập phân biệt được trạng thái siết chặt và các trạng thái lỏng bu lông ở mối nối dầm – cột của một khung thép phẳng trong phòng thí nghiệm, kể cả xếp các ca chưa huấn luyện vào lớp gần nhất (tr. 1, 9–10). |
| Bằng chứng | Một khung thép phẳng một tầng, một nhịp (cao 0,5 m, nhịp 0,3 m) tại IIT Bombay; năm ca có kiểm soát (UD, ED1–ED4) và bốn ca kiểm tra thêm (UD-C, ED5–ED7); sáu cảm biến biến dạng, búa va đập; 10 lần thử mỗi ca; chia 6/2/2 lần thử cho huấn luyện/kiểm định/kiểm tra, có tăng cường dữ liệu bằng nhiễu Gauss; kiểm chứng chéo năm phần (tr. 3–9; Bảng 1, 2, 4). |
| Giới hạn | Xem mục 5. |
| Tác động K1/K2/K3 | K1: mở rộng (tập kiểm tra chia theo lần thử nhưng cùng lần lắp ráp với tập huấn luyện; không khai báo phạm vi hiệu lực; tác giả tự nêu một mạng chỉ hợp cho một kết cấu, đổi hình học hay điều kiện biên phải huấn luyện lại, tr. 2). K2, K3: không liên quan. |
| Vị trí sử dụng | 3.3 (CNN trên ảnh thời gian – tần số cho lỏng bu lông khung thép); 3.4 (cách chia tập theo lần thử trong cùng lần lắp ráp – ví dụ cho rủi ro đánh giá lạc quan); 3.6 (tác giả tự nêu cần kiểm chứng với điều kiện môi trường – vận hành và khó có dữ liệu thực để huấn luyện, tr. 10–11). |
| Mức đã đọc | Toàn văn (01/10/2026) |

## 1. Bài toán và kết cấu thí nghiệm

- (a) Động cơ: bu lông ở mối nối nửa cứng hấp thụ năng lượng dưới gió, động đất và có thể bị lỏng, làm đổi ứng xử của
  kết cấu (tr. 1). Bài đặt mục tiêu định vị và ước lượng mức lỏng bu lông bằng CNN (tr. 2).
- (a) Kết cấu: khung thép phẳng một tầng, tiết diện thanh đều 0,032 × 0,006 m, cao 0,5 m, nhịp 0,3 m; mối nối dầm – cột
  bằng thép góc và bu lông, mỗi phía (phía cột, phía dầm) bốn bu lông M-5; chân cột ngàm bằng hai thép góc (tr. 3, Hình 1).
  Mô-đun đàn hồi in là E = 2,1 GPa (tr. 3). [NCS] Giá trị này khác bậc với thép thông thường, có thể là lỗi in; không dùng.
- (a) Cách tạo trạng thái (tr. 3, Bảng 1): UD – mọi bu lông siết chặt; ED1 – mối nối trái, bu lông phía cột siết tay;
  ED2 – mối nối trái, bu lông phía cột lỏng hoàn toàn; ED3 – mối nối trái, bu lông phía dầm siết tay; ED4 – mối nối phải,
  bu lông phía dầm lỏng hoàn toàn. "Siết chặt" là siết tay thêm nửa vòng; "siết tay" là siết bằng tay (tr. 3).
  [NCS] Không đo lực siết hay mô-men xoắn; mức siết là thao tác thủ công.
- (a) Ca kiểm tra không có trong huấn luyện (tr. 9, Bảng 4): **UD-C – mọi bu lông được siết chặt lại sau khi đã thực hiện
  tất cả các ca lỏng**; ED5 – mối nối trái, bu lông phía dầm lỏng hoàn toàn (gần ED2 và ED3); ED6 – mối nối phải, bu lông
  phía cột lỏng hoàn toàn (gần ED4); ED7 – mối nối trái, hai bu lông phía cột lỏng hoàn toàn.
- (a) Kích thích và cảm biến: búa va đập B&K 8202-8200 tại góc trên bên phải khung; sáu cảm biến biến dạng FLA-3 (SG1–SG6)
  đặt trên thanh, cách mỗi mối nối 35 mm; thu bằng HBM-MGC plus, tần số lấy mẫu 600 Hz (tr. 3, Hình 1b, Hình 2).

## 2. Dữ liệu và phương pháp

- (a) Tín hiệu: chỉ lấy phần dao động tự do 0,85 s sau va đập; qua cửa sổ Hamming để giảm rò rỉ tần số; biến đổi wavelet
  liên tục (hàm Morse mặc định của MATLAB) thành ảnh scalogram RGB (tr. 4–5, Hình 3–4). Mỗi lần thử cho sáu ảnh, một ảnh
  mỗi cảm biến; mỗi ca thử 10 lần (tr. 4–5).
- (a) Tiền xử lý ảnh: thu từ 875 × 656 xuống 224 × 224 × 3 bằng `imresize`; tăng cường dữ liệu bằng cách cộng nhiễu Gauss
  trung bình không ở "các mức khác nhau" (tr. 5, Hình 5). Mức nhiễu không được nêu.
- (a) Mạng: lớp tích chập với nhân 8 × 8, 20 bộ lọc, bước 1, đệm không; ReLU; gộp cực đại 2 × 2 bước 2; lớp kết nối đầy đủ;
  softmax và hàm mất mát entropy chéo (tr. 6–8, Hình 6–7). Kiến trúc được chốt "bằng thử và sai" (tr. 5). Huấn luyện
  150 vòng (epoch), lô 32, 13 lần lặp mỗi vòng (tr. 8). Tốc độ học không được nêu giá trị.
- **(a) Cách chia tập (tr. 6, Bảng 2):** chia **theo lần thử**: mỗi ca, 6 lần thử × 6 cảm biến cho huấn luyện (60 %),
  2 lần thử × 6 cảm biến cho kiểm định (20 %), 2 lần thử × 6 cảm biến cho kiểm tra (20 %). Sau khi cộng ảnh tổng hợp:
  72/24/24 ảnh mỗi ca; tổng 360/120/120. [NCS] Theo số học của Bảng 2, mỗi ảnh thực có thêm một ảnh tổng hợp
  (72 = 2 × 36); bài không nói rõ ảnh tổng hợp của tập kiểm tra được sinh từ ảnh thực nào, cũng không nói tăng cường làm
  trước hay sau khi chia (tr. 5 chỉ nói ảnh đã thu nhỏ "được dùng để sinh tổng hợp tập dữ liệu", rồi dẫn Bảng 2).
- (a) Kiểm chứng chéo năm phần: vì dữ liệu ít, "dữ liệu gốc" được chia thành năm phần bằng nhau, mỗi lượt một phần làm
  kiểm tra, bốn phần còn lại làm huấn luyện và kiểm định; ma trận nhầm lẫn là trung bình năm lượt (tr. 8–9). Bài không nói
  năm phần được chia theo lần thử hay theo ảnh.
- **[NCS] Đánh giá về rò rỉ:** việc chia theo lần thử giữ sáu ảnh của cùng một cú va đập trong cùng một tập, nên tránh được
  rò rỉ giữa các cảm biến của cùng lần đo. Tuy nhiên:
  1. Mỗi ca là **một lần lắp ráp** của khung; 10 lần thử của một ca được thực hiện trên cùng trạng thái lắp ráp (bài không mô
     tả việc tháo – lắp giữa các lần thử). Tập kiểm tra vì vậy cùng lần lắp ráp với tập huấn luyện; nhãn lớp trùng với lần
     lắp ráp, nên mạng có thể học dấu vết riêng của lần lắp ráp thay vì của mức lỏng. Đây là dạng rò rỉ do đơn vị chung mà
     [53] tr. 4–5 mô tả và [19] tr. 2, 12–14 cho thấy làm kết quả lạc quan.
  2. Nếu ảnh tổng hợp được sinh trước khi chia, bản nhiễu của một ảnh có thể rơi vào tập khác; bài không đủ thông tin để
     loại trừ.
  3. Kiến trúc chọn bằng thử và sai (tr. 5) trong khi tập kiểm định cũng được dùng để theo dõi huấn luyện (tr. 8); không có
     tập giữ lại riêng cho việc chọn mô hình.
  4. Câu "ảnh chưa thấy mô phỏng tình huống thực, nơi điều kiện môi trường và thí nghiệm có thể ảnh hưởng dữ liệu" (tr. 8)
     là nhận định của tác giả; tập kiểm tra lấy từ cùng khung, cùng lần lắp ráp, cùng điều kiện phòng thí nghiệm.

## 3. Kết quả (chỉ số như tác giả báo cáo)

- (a) Độ chính xác trung bình huấn luyện 100 %, kiểm định 98,1 % (tr. 1, 10). Kiểm định hội tụ sau khoảng 7–8 vòng; tác
  giả nói không xảy ra quá khớp (tr. 8, Hình 8).
- (a) Kiểm tra trên 120 ảnh chưa dùng: độ chính xác tổng 95,80 % (tr. 8, Bảng 3). Bảng 3: ED1, ED4, UD đúng 24/24; ED2
  đúng 22, nhầm 2 sang ED3; ED3 đúng 21, nhầm 3 sang ED1 (tr. 9).
  [NCS] Mục kết luận ghi 95,4 % và 95,40 % (tr. 10), không khớp với 95,80 % ở tr. 8; đường chéo Bảng 3 là 115/120 ≈ 95,83 %.
  Bảng 3 được nói là trung bình năm lượt (tr. 9) nhưng toàn số nguyên.
- (a) Ca chưa huấn luyện, mỗi ca 10 lần thử, 60 ảnh (tr. 9, Bảng 5): UD-C xếp vào UD 60; ED5 xếp vào lớp phía trái 43;
  ED6 xếp vào lớp phía phải 60; ED7 xếp vào UD 57. Độ chính xác 90,5 % (tr. 9). Tác giả giải thích ED7 bị xếp vào UD vì
  còn hai bu lông siết chặt, chuyển vị tương đối gần với UD (tr. 9).
  [NCS] Hàng ED5 chỉ cộng được 43/60, phần còn lại không hiện trong bảng; 90,5 % khớp với (60 + 43 + 60)/180, tức ED7 không
  tính vào độ chính xác này.
- (a) Mở rộng thành sáu lớp (thêm ED7): ED7 đúng 41, nhầm 19 sang UD; UD đúng 20, nhầm 4 sang ED7 (tr. 10, Bảng 6). Tác
  giả kết luận mạng phân loại được, dù các phần tử ngoài đường chéo giữa UD và ED7 tăng (tr. 10).
  [NCS] Hàng ED7 có 60 ảnh trong khi các lớp khác 24; cách chia cho lớp mới không được mô tả.
- (a) **Ca siết lại UD-C** được xếp vào UD 60/60 (tr. 9–10, Bảng 4–5). [NCS] Đây là lần duy nhất trong bài có tháo – siết
  lại; kết quả cho thấy, trên khung nhỏ này và với một lần siết lại, đặc trưng mà mạng dùng không bị lần siết lại làm lệch
  khỏi lớp UD. Bài không phân tích điều này và không đo mức siết.

## 4. Đề xuất và định hướng của tác giả

- (a) Kỹ thuật chỉ cần tín hiệu biến dạng theo thời gian, giảm khâu thủ công (tr. 10); có tiềm năng thành công cụ tự động
  mức công nghiệp cho mối nối khung phẳng (tr. 1, 10); hướng tiếp theo là khung 3D cỡ lớn (tr. 10).
- (a) Ứng dụng thực cần kiểm chứng với điều kiện môi trường – vận hành; có thể dùng chuẩn hóa dữ liệu để tách nhiễu môi
  trường – vận hành; huấn luyện bằng dữ liệu thực là khó, có thể dùng dữ liệu mô phỏng từ mô hình phần tử hữu hạn chính
  xác hoặc mô hình thu nhỏ trong phòng thí nghiệm (tr. 10–11).

## 5. Giới hạn

**(b) Tác giả tự nêu:**
- Một mạng đã huấn luyện không nhận biết được mọi loại hư hỏng; một mạng hợp cho một loại kết cấu, có thể không hợp cho
  kết cấu khác; đổi hình học, điều kiện biên phải huấn luyện lại (tr. 2, dẫn Avci 2021).
- Học sâu trên ảnh cần nhiều dữ liệu trong khi thí nghiệm chỉ lặp được ít lần, nên phải tăng cường dữ liệu (tr. 2, 5).
- Có thiên lệch về lớp UD khi một mối nối chỉ lỏng một phần (tr. 10).
- Cần kiểm chứng với điều kiện môi trường – vận hành thực; huấn luyện bằng dữ liệu thực là khó (tr. 10–11).
- Dữ liệu chỉ cung cấp theo yêu cầu do hạn chế về quyền riêng tư/đạo đức (tr. 11).

**[NCS] nhận định:**
- Một khung, một lần lắp ráp cho mỗi ca, 10 lần thử mỗi ca; tập kiểm tra cùng lần lắp ráp với tập huấn luyện (mục 2). Kết
  quả 95,8 % là độ chính xác **trong cùng lần lắp ráp**, chưa phải khả năng tổng quát sang lần lắp ráp khác hay kết cấu khác.
- Không báo cáo biến thiên theo lượt chia, theo lần khởi tạo, không có kiểm định thống kê hay khoảng tin cậy.
- Không có biến động môi trường – vận hành; kích thích là va đập có kiểm soát ở một vị trí. Không có nhiễu vận hành như
  cầu trục hay máy móc.
- Mức siết thủ công, không đo mô-men; nhãn "siết tay", "siết chặt" có bất định không được định lượng.
- Một số con số không nhất quán (95,80 % và 95,4 %; Bảng 5 hàng ED5; số ảnh ED7) và E = 2,1 GPa (tr. 3, 8–10).
- Khung nhỏ (0,5 × 0,3 m, bu lông M-5) khác xa nhà xưởng thép; việc áp sang nhà công nghiệp là diễn giải.

## 6. Đoạn dùng được cho tiểu luận

| Luận điểm | Trang | Loại |
|---|---|---|
| CNN trên ảnh scalogram của tín hiệu biến dạng sau va đập đã được dùng để phân biệt trạng thái lỏng bu lông và vị trí lỏng ở mối nối dầm – cột của khung thép phẳng trong phòng thí nghiệm | 1, 3–5, 8–9 | Trực tiếp |
| Trạng thái lỏng được tạo bằng thao tác siết tay/nới hoàn toàn có kiểm soát, nhãn do người thí nghiệm đặt | 3 (Bảng 1) | Trực tiếp |
| Tác giả tự nêu: một mạng chỉ hợp cho một kết cấu; đổi hình học, điều kiện biên phải huấn luyện lại | 2 | Trực tiếp |
| Tác giả tự nêu: cần kiểm chứng trong điều kiện môi trường – vận hành; huấn luyện bằng dữ liệu thực là khó | 10–11 | Trực tiếp |
| Dữ liệu học sâu cho SHM hạn chế vì thí nghiệm chỉ lặp được ít lần, nên phải tăng cường dữ liệu | 2, 5 | Trực tiếp |
| Tập kiểm tra chia theo lần thử trong cùng lần lắp ráp; độ chính xác cao trong điều kiện này không cho biết khả năng tổng quát sang lần lắp ráp khác | 6 (Bảng 2), 3, 9 | Diễn giải |
| Ca suy giảm một phần (ED7) bị xếp vào trạng thái nguyên vẹn, minh họa rằng kết quả phân loại không tự nó là chẩn đoán | 9–10 (Bảng 5–6) | Gián tiếp |
| Ca siết lại toàn bộ (UD-C) được xếp vào lớp nguyên vẹn trên khung này | 9–10 (Bảng 4–5) | Trực tiếp (kết quả); ý nghĩa cho phạm vi hiệu lực là diễn giải |

## 7. Kiểm phản chứng

- **UV-02 (nguồn gốc, phiên bản phương pháp, phạm vi hiệu lực của đầu ra phát hiện): không giải quyết.** Đầu ra là nhãn lớp
  và ma trận nhầm lẫn (tr. 8–10); bài không ghi nguồn gốc xử lý, phiên bản phương pháp hay phạm vi áp dụng cho kết quả.
  Tham số tiền xử lý được mô tả trong văn bản (tr. 4–6) nhưng thiếu mức nhiễu tăng cường, tốc độ học và tiêu chí chọn kiến
  trúc (tr. 5). Bổ sung cho **nội dung** phạm vi hiệu lực (cùng nhóm với Figueiredo 2011, [45]): tác giả tự nêu mạng gắn với
  một kết cấu và điều kiện biên (tr. 2) và cần kiểm chứng điều kiện môi trường – vận hành (tr. 10–11); TG. Không tính vào số
  căn cứ của phát biểu "chưa được ghi".
- **UV-05 (thiếu nhãn hư hỏng ở hiện trường): không giải quyết.** Nhãn do thao tác thí nghiệm tạo ra (tr. 3). Bài cho một
  căn cứ cùng chiều: huấn luyện bằng dữ liệu thực là khó; tác giả đề xuất thay bằng dữ liệu mô phỏng phần tử hữu hạn hoặc
  mô hình thu nhỏ (tr. 10–11); TG. Không đề cập việc lấy nhãn bằng kiểm tra.
- **UV-06 (lần lắp ráp hoặc can thiệp là ranh giới phạm vi hiệu lực): không giải quyết; có một điểm cần ghi nhận.**
  - Bài không xem lần lắp ráp là đơn vị chia tập hay ranh giới phạm vi; tập kiểm tra cùng lần lắp ráp với tập huấn luyện
    (tr. 6, Bảng 2; [NCS] suy từ mô tả tr. 3–5).
  - Ca UD-C (siết lại sau mọi ca lỏng) được xếp đúng vào UD 60/60 (tr. 9–10). [NCS] Đây là dữ liệu ngược chiều một phần với
    tiền đề vật lý của UV-06 ("sau siết lại, dữ liệu tham chiếu không còn đương nhiên dùng được"): trên khung nhỏ này, một lần
    siết lại không làm lệch kết quả. Tuy nhiên chỉ có một lần siết lại, một khung, không đo mô-men, không phân tích; nó cho
    thấy ảnh hưởng của lần lắp ráp **có thể nhỏ hoặc lớn tùy trường hợp**, tức cần được **kiểm và ghi** thay vì giả định.
    Đề nghị: khi viết UV-06 ở GĐ3, phát biểu theo hướng "phải ghi lần lắp ráp/can thiệp để kiểm được", không theo hướng
    "luôn làm mất hiệu lực". Không tính [48] vào số căn cứ của UV-06.
  - Bài không có cơ chế ghi sự kiện can thiệp hay lập lại dữ liệu tham chiếu.
