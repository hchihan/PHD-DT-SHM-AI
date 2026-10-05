# IW7JBB3E — Da Silva và cs. (2024) — [56]

da Silva S., Yano M. O., Teloli R. de O., Chevallier G., Ritto T. G. Domain Adaptation of Population-Based of Bolted
Joint Structures for Loss Detection of Tightening Torque. *ASCE-ASME Journal of Risk and Uncertainty in Engineering
Systems, Part B: Mechanical Engineering* 10(1): 011102 (10 tr.), tháng 3/2024. DOI 10.1115/1.4063794 (in ở tr. 011102-1).
Nhận bản thảo 26/12/2022, bản cuối 21/04/2023, trực tuyến 23/11/2023 (tr. 011102-1). Số kỳ (1) lấy từ đường dẫn tải
tệp ("risk/article-pdf/10/1/011102") in ở chân mỗi trang; trang 1 chỉ in "Vol. 10".

**Bản đã đọc:** bản in của ASME, tệp `C:/Users/VNT/Zotero/storage/YZ6YYU2U/Da Silva et al. - 2024 - Domain Adaptation of
Population-Based of Bolted Joint Structures for Loss Detection of Tightening To.pdf`, 10 tr. (011102-1 đến 011102-10).
Trang dẫn là **trang in** dạng 011102-n. Đọc toàn văn ngày 01/10/2026, phiên T2-2; **thay cho ghi chú đọc một phần**
(phiên viết 5.6A, 29/09/2026). [NCS] Tệp chưa có bản liên kết trong `pdf/` theo quy ước 4.1.

Ký hiệu: (a) điều tác giả nói; (b) giới hạn tác giả tự nêu; **[NCS]** nhận định của NCS.

| Cột | Nội dung |
|---|---|
| Citekey / Số cũ | IW7JBB3E / [56] |
| Tier / Cụm | Tier 2 / SHM–bu lông–EOV |
| Luận điểm | Dùng thích nghi miền bằng phân tích thành phần chuyển giao (transfer component analysis, TCA) để tái sử dụng bộ phân loại lực siết bu lông (GMM trên tần số riêng) học trên một kết cấu liên kết bu lông có nhãn (miền nguồn) cho kết cấu bu lông khác, dữ liệu hạn chế, nhãn chưa biết (miền đích) (tr. 011102-1, Tóm tắt). Bộ phân loại học trên một kết cấu thường thất bại khi áp sang kết cấu tương tự (tr. 011102-1, -2, -4). |
| Bằng chứng | Thí nghiệm PTN trên bốn dầm Orion (nhôm duralumin, ba bu lông M4): ba mẫu cùng hình học, một mẫu khác mặt tiếp xúc; lực siết bu lông ngoài 10–80 cNm, bước 5 cNm; 128 lần đo mỗi mức lực siết, gồm 8 đợt × 16 lần đo, mỗi đợt sau khi tháo – lắp hoàn toàn, ở các ngày khác nhau (tr. 011102-3). Kết quả cho một cặp nguồn – đích (Dầm #2 → Dầm #1) ở mức 25 cNm (tr. 011102-4 đến -5, Hình 6, 8, 11, 12) và tổng hợp mọi cặp ở 25, 20, 15 cNm (Hình 13, tr. 011102-9). |
| Giới hạn | Xem mục 6. |
| Tác động K1/K2/K3 | K1: mở rộng (hiệu năng phụ thuộc mẫu kết cấu cụ thể, lịch sử mài mòn, cấu hình mặt tiếp xúc và việc chọn kết cấu nguồn; các yếu tố này thuộc phạm vi hiệu lực). K2, K3: không liên quan. |
| Vị trí sử dụng | 3.3 (hiện có); 3.6 (khoảng cách giữa các kết cấu, chuyển giao); 5.6A.3. |
| Mức đã đọc | Toàn văn (01/10/2026) |

## 1. Câu hỏi và đối tượng

- (a) Câu hỏi: bộ phân loại lực siết học trên một kết cấu bu lông có nhãn có dùng lại được cho kết cấu khác cùng loại hư
  hỏng không, và thích nghi miền giúp đến đâu (tr. 011102-1, -4).
- (a) Lý do: đo trực tiếp lực siết từng bu lông có thể không khả thi vì số cảm biến hoặc khó tiếp cận (tr. 011102-1);
  bộ phân loại "có xu hướng thất bại" khi dùng cho kết cấu bu lông tương tự khác, huấn luyện lại thì tốn kém (tr. 011102-1).
- (a) Đặt bài trong SHM theo quần thể (population-based SHM) và song sinh số: chuyển giao giúp "mở rộng hiệu lực" của
  song sinh số bằng cách dùng lại tri thức cũ (tr. 011102-2).

## 2. Kết cấu và trạng thái lực siết

- (a) Dầm Orion: hai dầm duralumin 200 × 30 × 2 mm nối chồng bằng ba bu lông M4 (một giữa, hai ngoài) trên chiều dài
  30 mm; bản tiếp xúc (patch) 12 × 12 mm², dày thêm 1 mm, chỉ ở dầm gắn máy rung; điều kiện ngàm – tự do (tr. 011102-3).
- (a) Dầm #1, #2, #3: ba mẫu chế tạo cùng kích thước danh nghĩa, nhưng dao động không nhất thiết giống nhau do sai khác
  chế tạo (tr. 011102-3).
- (a) Dầm #4: dùng chính các chi tiết của Dầm #3, lật dầm ngàm qua đường tâm để tạo mặt tiếp xúc phẳng – phẳng
  30 × 80 mm², không có bản tiếp xúc (tr. 011102-3).
- (a) Dầm #1 có vết đen do mài mòn ma sát ở bản tiếp xúc ngoài; đã qua nhiều thí nghiệm trước để khảo sát tính phi tuyến,
  nên hành vi động khác các dầm còn lại do mài mòn bề mặt và "thời gian đã qua của vòng đời" (tr. 011102-7 đến -8).
- (a) Kích thích nền ồn trắng Gauss 4 m/s² RMS bằng máy rung; đo vận tốc đầu tự do bằng vibrometer laser quét 3D, gia
  tốc nền bằng gia tốc kế (tr. 011102-3).
- (a) Lắp ráp: cả bốn kết cấu dùng cùng quy trình; bu lông giữa siết đủ 80 cNm suốt chiến dịch; hai bu lông ngoài
  10–80 cNm, bước 5 cNm; lực siết kiểm lại bằng cờ-lê lực sau thí nghiệm (tr. 011102-3).
- (a) **Tháo – lắp:** mỗi kết cấu đo 8 đợt × 16 lần, mỗi đợt "sau khi lắp ráp và tháo rời hoàn toàn", lặp ở các ngày khác
  nhau, tổng 128 lần cho mỗi mức lực siết (tr. 011102-3).
- (a) Phân loại trạng thái theo Dầm #1: 80–60 cNm coi là khỏe; 60–30 cNm hư hỏng mức thấp, vẫn vận hành được; từ
  25 cNm trở xuống bộ phân loại phải báo hư hỏng (tr. 011102-4). Độ phân tán của cùng tham số dao động khác nhau theo dầm
  (tr. 011102-4).

## 3. Đặc trưng và phương pháp thích nghi miền

- (a) Đặc trưng: tần số riêng các dạng uốn bậc 4, 5, 6 (X1, X2, X3), khoảng 700 và 1900 Hz, rút từ hàm truyền giữa gia tốc
  nền và vận tốc đầu tự do, vì các dạng này gây ứng suất rõ ở vùng nối chồng (tr. 011102-3, -4).
- (a) Bộ phân loại: GMM học trên dữ liệu khỏe có nhãn; điểm là khoảng cách Mahalanobis bình phương D; ngưỡng β theo kiểm
  định χ² với xác suất báo động giả 5 % (tr. 011102-3, -4). Tác giả chọn GMM vì đã được kiểm chứng ở công trình trước;
  đóng góp nằm ở việc kết hợp bộ phân loại đó với chuyển giao cho bốn dầm (tr. 011102-3).
- (a) Thích nghi miền: TCA của Pan và cs., ánh xạ đặc trưng nguồn và đích vào không gian Hilbert tái sinh nhân, cực tiểu
  sai khác trung bình cực đại (MMD) giữa hai phân bố biên, có số hạng chính quy và ràng buộc giữ phương sai (tr. 011102-2
  đến -3, phương trình 1–5). Trước TCA chuẩn hóa z-score mọi tập; nhân tuyến tính; giảm từ 3 xuống 2 chiều (tr. 011102-5).
- (a) Nguồn: kết cấu có nhãn đầy đủ khỏe – hư hỏng; đích: kết cấu khác, "giả định chưa có nhãn" ở mỗi mức lực siết, dữ liệu
  hạn chế (tr. 011102-1, -2, -4). Nếu ánh xạ tốt, dùng cùng ngưỡng của bộ phân loại nguồn cho đích (tr. 011102-3).
- (a) Nhãn của đích: không dùng để huấn luyện; tỉ lệ dương tính giả và âm tính giả trên đích được tính để đánh giá
  (Hình 12, 13, tr. 011102-9). (a) TCA là thủ tục "một – một": mỗi lần chạy dùng đích với một mức lực siết (tr. 011102-10).

## 4. Chia dữ liệu

- (a) Nguồn (Dầm #2): học trên 70 % dữ liệu khỏe (448 mẫu, mức 80, 75, 70, 65, 60 cNm); kiểm chứng trên 30 % còn lại
  (192 mẫu khỏe) và 128 mẫu hư hỏng ở 25 cNm (tr. 011102-4; Bảng 1, tr. 011102-9).
- [NCS] Bài không nói 70/30 chia ngẫu nhiên theo lần đo hay theo đợt tháo – lắp. Với 8 đợt tháo – lắp mỗi mức, nếu chia theo
  lần đo thì cùng một đợt lắp có thể có mặt ở cả tập học và tập kiểm chứng của nguồn; khi đó kết quả ở không gian gốc của
  nguồn có thể lạc quan. Đây là suy luận từ việc thiếu thông tin, không phải điều tác giả nói.

## 5. Kết quả (theo trang)

| Kết quả (a) | Trang |
|---|---|
| Nguồn Dầm #2, không gian gốc: tỉ lệ dương tính giả 1,9 %, âm tính giả 0; ngưỡng 22 | 011102-4 (văn bản), -7 (chú thích Hình 6) |
| Bộ phân loại học trên Dầm #2, áp trực tiếp cho Dầm #1 (đích, giả định chưa nhãn) ở không gian gốc, hư hỏng 25 cNm: **phân loại thất bại** | 011102-4 (văn bản: "fails to classify the structural conditions of the target domain"), -7 (chú thích Hình 8: "Classification failed…") |
| Sau TCA, không gian ẩn: nguồn dương tính giả 1,2 %, âm tính giả 7,0 % (hiệu năng nguồn giảm do âm tính giả tăng, vì nén không gian đặc trưng) | 011102-5 (văn bản), -9 (chú thích Hình 11) |
| Sau TCA, đích Dầm #1: dùng lại được bộ phân loại "với độ chính xác hợp lý"; văn bản ghi dương tính giả 1,25 %, chú thích Hình 12 ghi dương tính giả 0,3 %, âm tính giả 0 | 011102-5 (văn bản), -9 (chú thích Hình 12) |
| Mọi cặp nguồn – đích ở 25, 20, 15 cNm: Dầm #2 làm nguồn cho hiệu năng tốt nhất, phân loại được cả Dầm #4 (mặt tiếp xúc khác), nhất là ở 20 và 15 cNm; Dầm #1 và #4 làm nguồn cho báo động giả cao trên các đích khác | 011102-5, -7; Hình 13, -9 |
| Giải thích: Dầm #1 mài mòn, đã qua nhiều thí nghiệm; Dầm #4 phân bố áp lực tiếp xúc không đều, biến thiên dữ liệu lớn hơn, nhất là ở lực siết thấp; khác biệt hiệu năng chịu ảnh hưởng của khả năng bộ phân loại hơn là của TCA | 011102-7 đến -9 |
| Kết luận: TCA mở rộng khả năng dùng bộ phân loại sang đích chưa nhãn, nhưng việc chọn tập nguồn là quan trọng | 011102-10 |

[NCS] Có hai chỗ không khớp trong bài: (i) tỉ lệ dương tính giả của đích ở không gian ẩn là 1,25 % trong văn bản
(tr. 011102-5) nhưng 0,3 % trong chú thích Hình 12 (tr. 011102-9); (ii) văn bản tr. 011102-4 dẫn "(Fig. 7)" cho hiệu năng
nguồn, trong khi chú thích Hình 7 (tr. 011102-7) mô tả đích Dầm #1. Khi trích chỉ nên dùng nhận định định tính, không dẫn
con số đích.

## 6. Giới hạn

**(b) Tác giả tự nêu:**
- Việc chọn cơ sở dữ liệu nguồn là quan trọng; dùng Dầm #1 (có vết mài mòn) hay Dầm #4 (mặt tiếp xúc khác hẳn) làm nguồn
  cho báo động giả cao hơn (tr. 011102-10; tr. 011102-5, -7).
- Hiệu năng trong không gian ẩn có thể bị ảnh hưởng do mất bớt thông tin khi nén và do biến thiên lớn giữa các dầm
  (tr. 011102-5).
- Khác biệt hiệu năng chịu ảnh hưởng chủ yếu của khả năng bộ phân loại; một bộ phân loại phù hợp hơn với dữ liệu từng
  trường hợp có thể cải thiện (tr. 011102-9).
- TCA là thủ tục một – một: mỗi lần chỉ xét đích với một mức lực siết (tr. 011102-10).
- Mức độ tin cậy của tỉ lệ dương tính giả và âm tính giả phụ thuộc lựa chọn nguồn/đích (tr. 011102-5).

**[NCS] nhận định:**
- Thí nghiệm PTN trên dầm nhôm nhỏ, bu lông M4, lực siết cNm, kích thích máy rung có kiểm soát; không có biến đổi môi
  trường – vận hành. Áp sang mối nối bu lông của nhà xưởng thép là diễn giải.
- Nhãn đích được giả định là chưa biết khi chuyển giao, nhưng thực tế đã biết và dùng để đánh giá; dữ liệu đích được tổ
  chức theo từng mức lực siết (tr. 011102-10). Ở hiện trường không có cấu trúc dữ liệu như vậy.
- Đơn vị miền là **mẫu kết cấu** (dầm). Tám đợt tháo – lắp của mỗi dầm được gộp vào cùng một miền (tr. 011102-3); bài
  không phân tích ảnh hưởng của từng lần tháo – lắp lên đặc trưng hay lên bộ phân loại.
- Không báo cáo biến thiên theo lần chạy, theo đợt, theo seed hay khoảng tin cậy; mỗi cặp nguồn – đích một con số.
- Cách chia 70/30 không nêu rõ có tách theo đợt tháo – lắp không (mục 4).
- Dữ liệu chỉ cung cấp theo yêu cầu (tr. 011102-10, mục Data Availability).

## 7. Điều bài không xử lý (theo chuỗi luận án, ngắn)

Bài coi việc kết cấu nguồn khác kết cấu đích là vấn đề phân bố dữ liệu cần thích nghi, không ghi nhận nguồn gốc của bộ
phân loại (kết cấu nguồn, lịch sử mài mòn, cấu hình mặt tiếp xúc) như một phần của kết quả, cũng không gắn kết quả với
hành động kiểm tra hay bảo trì.

## 8. Tác động tới K1/K2/K3

- **K1: mở rộng.** Hiệu năng của cùng một bộ phân loại thay đổi theo mẫu kết cấu (sai khác chế tạo, tr. 011102-3), lịch sử
  mài mòn (tr. 011102-7 đến -8), cấu hình mặt tiếp xúc (tr. 011102-9) và việc chọn kết cấu nguồn (tr. 011102-10). [NCS]
  Các yếu tố này là thành phần của phạm vi hiệu lực (đơn vị suy luận, đợt lắp đặt, điều kiện áp dụng); kết quả phân loại
  không ghi kèm chúng thì không biết được có dùng ngoài phạm vi hay không.
- K2: không liên quan (không có ánh xạ cảm biến – cấu kiện theo thời gian).
- K3: không liên quan.

## 9. Đoạn dùng được cho tiểu luận

| # | Nội dung dùng được | Trang | Loại | Mục |
|---|---|---|---|---|
| D1 | Bộ phân loại lực siết học trên một kết cấu bu lông có xu hướng thất bại khi dùng cho kết cấu bu lông tương tự khác; huấn luyện lại tốn kém | 011102-1 | (a) | 3.3, 3.6 |
| D2 | Ba dầm cùng kích thước danh nghĩa nhưng dao động không nhất thiết giống nhau do sai khác chế tạo | 011102-3 | (a) | 3.6 |
| D3 | Bộ phân loại học trên Dầm #2 áp trực tiếp cho Dầm #1 ở không gian đặc trưng gốc thì phân loại thất bại | 011102-4; Hình 8, -7 | (a) | 3.6, 5.6A.3 |
| D4 | Sau TCA, bộ phân loại nguồn dùng lại được cho đích chưa nhãn với độ chính xác hợp lý, nhưng việc chọn kết cấu nguồn là quan trọng | 011102-5, -10 | (a) | 3.6, 5.6A.3 |
| D5 | Mài mòn bề mặt và lịch sử thí nghiệm làm hành vi động của một dầm khác các dầm cùng thiết kế, làm bộ phân loại kém hơn | 011102-7 đến -8 | (a) | 3.6 |
| D6 | Chuyển giao giúp mở rộng hiệu lực của song sinh số bằng cách dùng lại tri thức trước | 011102-2 | (a) | 2.3 (tùy chọn) |
| D7 | Các yếu tố trên cần được ghi thành phạm vi hiệu lực của bằng chứng | — | [NCS] | 3.5, 5.5 |

Không dẫn con số dương tính giả của đích (mâu thuẫn 1,25 % / 0,3 %, mục 5).

## 10. Kiểm phản chứng

**Xác nhận/điều chỉnh câu ở UV-06** ("Da Silva và cs. 2024 [56], tr. 011102-7 (bộ phân loại học trên một dầm bu lông áp
trực tiếp sang dầm khác thì thất bại)"): **đúng về nội dung, cần chỉnh trang và bối cảnh.**
- Văn bản ở tr. 011102-4: "the classifier trained on the source domain data fails to classify the structural conditions of
  the target domain"; chú thích Hình 8 ở tr. 011102-7: "Classification failed using the previously trained algorithm with a
  dataset of the source domain (Beam #2)". Nhận định chung ở tr. 011102-1: các bộ phân loại "tend to fail when used in
  other similar bolted structures".
- Bối cảnh cần ghi kèm: nguồn Dầm #2, đích Dầm #1, không gian đặc trưng gốc, hư hỏng 25 cNm; Dầm #1 khác Dầm #2 do sai khác
  chế tạo và do mài mòn tích lũy (tr. 011102-3, -7 đến -8). Sau TCA thì dùng lại được (tr. 011102-5).
- [NCS] Thất bại được chứng minh **giữa hai mẫu kết cấu**, không giữa hai lần lắp ráp của cùng một kết cấu. Với UV-06, [56]
  là căn cứ cho "đơn vị kết cấu và lịch sử mài mòn là ranh giới hiệu lực", còn cho "lần lắp ráp" chỉ là căn cứ gián tiếp
  (Dầm #4 là lắp lại chi tiết của Dầm #3 theo cấu hình khác, tr. 011102-3; Dầm #3 và Dầm #4 có hiệu năng chuyển giao khác
  nhau, Hình 13, tr. 011102-9). Đề xuất sửa căn cứ trong nhật ký thành: "tr. 011102-1, -4 (Hình 8, tr. -7): bộ phân loại học
  trên một dầm bu lông áp trực tiếp sang dầm khác cùng thiết kế thì thất bại; tr. 011102-7 đến -8: mài mòn và lịch sử thí
  nghiệm làm hành vi động khác; TG".

**UV-05 (thiếu nhãn hư hỏng ở hiện trường): một phần đối với phát biểu gốc; không giải quyết đối với phát biểu đã thu hẹp.**
- Một phần: bài đề xuất dùng kết cấu nguồn có nhãn để phân loại kết cấu đích chưa nhãn (tr. 011102-1, -2, -5); đây là một
  lời giải theo hướng SHM theo quần thể cho việc thiếu nhãn ở đích.
- Không giải quyết phần đã thu hẹp: nhãn nguồn do cờ-lê lực trong PTN đặt (tr. 011102-3), không đến từ kiểm tra ở công
  trình đang vận hành; nhãn đích có sẵn và dùng để đánh giá (Hình 12, 13, tr. 011102-9); bài không bàn bản ghi nhãn, độ bất
  định của kiểm tra hay liên kết nhãn với phép đo và cấu kiện. [NCS] [56] chỉ là một trường hợp của SHM theo quần thể; mục
  "[57] Bull 2021 và SHM theo quần thể" ở UV-05 vẫn cần [57] để kiểm xong.

**UV-06 (lần lắp ráp hoặc can thiệp là ranh giới phạm vi hiệu lực): không giải quyết; củng cố căn cứ (có điều chỉnh).**
- Bài gộp tám đợt tháo – lắp của mỗi dầm vào một miền (tr. 011102-3) và không xét lần lắp ráp hay can thiệp như ranh giới
  hiệu lực; cách xử lý khác biệt giữa kết cấu là thích nghi miền (tr. 011102-2 đến -5), không phải ghi ranh giới hiệu lực
  kèm kết quả. Việc phải chọn đúng nguồn (tr. 011102-10) cho thấy [NCS] thông tin "bộ phân loại học từ kết cấu nào, ở trạng
  thái mặt tiếp xúc nào" cần đi kèm kết quả.
- [NCS] Thích nghi miền là một hướng phản chứng một phần cho UV-06 ở mức kỹ thuật (giảm sai khác giữa miền), nhưng vẫn cần
  biết miền nào là nguồn, nên không thay được việc ghi phạm vi hiệu lực. Các mục phản chứng khác của UV-06 ([57], Gardner
  2021 phần III, theo dõi dài hạn sau bảo trì) vẫn chưa kiểm.
