# DMIUEEFB — Kritzinger và cs. (2018) — [8]

Kritzinger W, Karner M, Traar G, Henjes J, Sihn W. Digital Twin in manufacturing: A categorical literature review
and classification. *IFAC-PapersOnLine* 51(11): 1016–1022. DOI 10.1016/j.ifacol.2018.08.474.

**Bản đã đọc:** toàn văn, bản PDF của nhà xuất bản (7 tr. PDF = tr. 1016–1022 của tạp chí; số trang dưới đây là số
trang tạp chí). Đọc ngày 30/09/2026, phiên T1-3. Đã đối chiếu lại Bảng 1–2 bằng cách đếm trực tiếp từ bảng.

Ký hiệu: (a) điều tác giả nói; (b) giới hạn tác giả tự nêu; **[NCS]** nhận định của NCS.

| Cột | Nội dung |
|---|---|
| Citekey / Số cũ | DMIUEEFB / [8] |
| Tier / Cụm | Tier 1 / Song sinh số |
| Luận điểm | Thuật ngữ "song sinh số" được dùng lẫn với mô hình số và bóng số; ba khái niệm khác nhau ở mức tích hợp dữ liệu giữa đối tượng vật lý và đối tượng số, và cần được tách theo tiêu chí đó (tr. 1017, 1020). |
| Bằng chứng | Tổng quan có phân loại từ Google Scholar và Scopus, chủ yếu các bài sau 2014; mỗi bài được xếp theo loại bài, mức tích hợp, lĩnh vực và công nghệ (tr. 1018, Hình 4, Bảng 1). Trong bảng, chỉ 18 % số bài mô tả đúng luồng dữ liệu hai chiều dù đa số dùng chữ "Digital Twin" (tr. 1020). |
| Giới hạn | Xem mục 5. |
| Tác động K1/K2/K3 | K1, K2, K3: không liên quan trực tiếp (bài không bàn chất lượng bằng chứng, truy vết hay hành động). Liên quan đến **định vị** của luận án (mục 7 bên dưới). |
| Vị trí sử dụng | 2.3 (định nghĩa DM/DS/DT); Bảng thuật ngữ (mục 10 của CLAUDE.md); phần tự định vị mức tích hợp ở Dẫn nhập và 5.x; trả lời câu hỏi hội đồng "đây có phải song sinh số không". |
| Mức đã đọc | Toàn văn |

## 1. Câu hỏi nghiên cứu và đối tượng

- Câu hỏi: khái niệm song sinh số đang được hiểu khác nhau giữa các nghiên cứu; cần một tổng quan có phân loại
  theo mức tích hợp, lĩnh vực ứng dụng và công nghệ (tr. 1016, 1018).
- Đối tượng: **sản xuất công nghiệp** (hệ thống sản xuất, dây chuyền, máy công cụ). Không bàn công trình xây dựng.
  Lĩnh vực được xếp gồm lập kế hoạch và điều khiển sản xuất (PPC), bảo trì, quy hoạch mặt bằng, vòng đời sản phẩm
  (tr. 1018, 1020).
- Loại dữ liệu: không có dữ liệu đo; đây là tổng quan tài liệu.

## 2. Phương pháp và kiến trúc thông tin

- Không có kiến trúc thông tin hay chuẩn dữ liệu (không IFC, SOSA, PROV). Bài chỉ nêu các công nghệ thường gặp:
  mô phỏng, giao thức truyền thông (OPC-UA, MQTT) và các công nghệ Công nghiệp 4.0 (tr. 1018).
- Đóng góp khái niệm là ba định nghĩa theo **mức tích hợp dữ liệu** (tr. 1017, Hình 1–3):
  - **Mô hình số (Digital Model, DM):** biểu diễn số của đối tượng vật lý đang có hoặc dự kiến, không có trao đổi dữ
    liệu tự động nào giữa đối tượng vật lý và đối tượng số. Dữ liệu của hệ vật lý có thể được dùng để dựng mô hình,
    nhưng mọi trao đổi làm thủ công. Thay đổi trạng thái của vật lý không ảnh hưởng trực tiếp đến đối tượng số và ngược lại.
  - **Bóng số (Digital Shadow, DS):** DM có thêm **luồng dữ liệu tự động một chiều** từ trạng thái của đối tượng vật
    lý sang đối tượng số. Vật lý đổi thì số đổi; chiều ngược lại thì không.
  - **Song sinh số (Digital Twin, DT):** luồng dữ liệu **tích hợp đầy đủ theo cả hai chiều**. Đối tượng số có thể đóng
    vai trò thực thể điều khiển đối tượng vật lý, và có thể còn các đối tượng khác (vật lý hoặc số) làm đối tượng số
    đổi trạng thái.
- Tiêu chí phân loại duy nhất là **mức tự động của luồng dữ liệu** (thủ công / tự động một chiều / tự động hai chiều).
  Việc có mô phỏng, học máy hay quyết định của con người không phải tiêu chí.
- Bài nhắc thêm hai định nghĩa nền: Grieves (2002) và Glaessgen & Stargel (2012), nói DT là mô phỏng đa vật lý, đa
  tỷ lệ, xác suất, cập nhật từ cảm biến (tr. 1016–1017), và mô tả DT gồm cả thuật toán "quyết định hành động" trong
  hệ sản xuất từ dữ liệu đã xử lý (tr. 1017).

## 3. Cách kiểm chứng

- Không kiểm chứng thực nghiệm. Tổng quan có phân loại; chưa thấy mô tả quy trình mã hóa kép hay độ tin cậy giữa
  các người phân loại. Khi một bài thuộc nhiều loại, tác giả lấy loại trội (tr. 1018).
- Không có đường cơ sở. Bài trình bày phân bố theo loại (Hình 5), mức tích hợp (Bảng 1–2) và lĩnh vực (Hình 6).

## 4. Luận điểm chính

1. Không có định nghĩa chung của song sinh số; thuật ngữ bị dùng thay cho DM và DS vì mỗi ngành dùng theo cách
   riêng (tr. 1017, 1020).
2. Nên tách DM, DS, DT theo mức tích hợp dữ liệu. Đây là bước đầu tiến tới một định nghĩa chung (tr. 1017, 1020).
3. Trong các bài xếp được, DS (35 %) và DM (28 %) chiếm phần lớn; chỉ 18 % thực sự mô tả luồng hai chiều. Đa số bài
   dùng chữ "Digital Twin" (tr. 1020).
4. Nghiên cứu về DT còn ở giai đoạn đầu: 55 % là bài khái niệm, 26 % là ca nghiên cứu (tr. 1018); tỷ lệ ca nghiên
   cứu giảm khi mức tích hợp tăng từ DM lên DT; ca nghiên cứu duy nhất về DT được triển khai trong phòng thí nghiệm
   (Bottani và cs. 2017) (tr. 1020).
5. Bảo trì là lĩnh vực được nghiên cứu nhiều thứ hai sau PPC, chủ yếu là bảo trì theo trạng thái (tr. 1020). Tác
   giả nói DT có thể dùng cho điều khiển quy trình và bảo trì theo trạng thái bằng các phương pháp dựa trên dữ liệu,
   không cần mô phỏng nặng (tr. 1020).

### Số liệu đếm lại từ Bảng 1–2 (để dẫn khi cần)

- Nhóm DT trong Bảng 1 có 8 bài: bài tổng quan 4 (Boschert & Rosen 2016; Kuhn 2017; Müller và cs. 2017;
  Pawlaszczyk 2006), bài định nghĩa 2 (Brenner & Hummel 2017; Reeves 2017), khái niệm 1 (Uhlemann và cs. 2017a),
  ca nghiên cứu 1 (Bottani và cs. 2017). Bảng 2 cho tổng hàng DT là 19,04 %, còn văn bản viết 18 % (tr. 1020);
  chênh lệch nhỏ do làm tròn. **[NCS]** Khi dẫn số liệu nên dẫn theo văn bản (18 %) và ghi đây là số của tác giả.
- Trong nhóm bảo trì (tr. 1019): Kuhn 2017 xếp DT; Friedrich 2014, Lee 2013b, Lee 2013c, Lindström 2017 xếp DS;
  Cai 2017 xếp DM.

### Bài đánh giá tài liệu nào bị gọi sai tên?

Bài **không chỉ ra bài cụ thể nào bị dùng sai tên**. Điều tác giả nói là: có một số bài tổng quan được xếp vào DT
"vì giả định có trao đổi dữ liệu hai chiều" (tr. 1020), và đa số bài dùng chữ "Digital Twin" nhưng chỉ 18 % thực sự
mô tả luồng hai chiều (tr. 1020). Từ Bảng 1, các bài tổng quan được xếp DT là bốn bài nêu ở trên. Các bài dùng chữ
DT nhưng được xếp DM hoặc DS gồm, ví dụ, Tao và cs. (2017) (DM), Rosen và cs. (2015) (DM), Lee và cs. (2013b,c) (DS);
chi tiết ở Bảng 1 (tr. 1019). **[NCS]** Không nên viết trong tiểu luận rằng Kritzinger "chỉ ra bài X gọi sai tên";
chỉ nên viết rằng bài phân loại lại theo mức tích hợp thực tế được mô tả.

## 5. Giới hạn

**(b) Tác giả tự nêu:**
- Chưa có định nghĩa chung; cần một định nghĩa thống nhất và các mô hình tham chiếu đáp ứng yêu cầu riêng của từng
  lĩnh vực (tr. 1020).
- Nghiên cứu DT còn ở giai đoạn đầu; thiếu ca nghiên cứu áp dụng trong môi trường công nghiệp để đánh giá lợi ích
  (tr. 1020).
- Số bài xếp "chưa xác định" (khi không thể phân loại chính xác mức tích hợp) bị loại khi so sánh loại bài với mức
  tích hợp (tr. 1020, Bảng 1).

**[NCS] nhận định:**
- Phạm vi chỉ có sản xuất; công cụ tìm chỉ gồm Google Scholar và Scopus với các từ khóa nêu ở tr. 1018; không có tiêu
  chí loại trừ nào được nêu. Không có phân loại cho công trình xây dựng hoặc kết cấu.
- Tiêu chí "mức tự động của luồng dữ liệu" không nói rõ trường hợp **con người làm khâu trung gian** ở chiều ngược
  (kỹ sư đọc kết quả rồi ra quyết định và tác động lên vật lý). Định nghĩa chỉ chia thủ công / tự động (tr. 1017).
- Không có quy trình phân loại kép; các số phần trăm là của một nhóm tác giả.

## 6. Điều bài KHÔNG xử lý, xét theo chuỗi của luận án

| Ý | Mức | Căn cứ |
|---|---|---|
| Nguồn gốc bằng chứng cảm biến | không xử lý | Bài không bàn dữ liệu đo hay nguồn gốc; chỉ nhắc cảm biến và IoT là công nghệ hỗ trợ (tr. 1016, 1018) |
| Phạm vi hiệu lực của bằng chứng | không xử lý | Không có |
| Quan hệ bằng chứng – cấu kiện có thời hạn | không xử lý | Không có; bài ở mức khái niệm và phân loại |
| Trách nhiệm, thẩm quyền | không xử lý | DT được mô tả như hệ tự "quyết định hành động" (tr. 1017); không nói ai chịu trách nhiệm |
| Trạng thái hành động và lịch sử chuyển trạng thái | không xử lý | Không có |
| Truy ngược từ hành động về dữ liệu gốc | không xử lý | Không có |

Ghi chú: bài không nhằm xử lý các ý trên (đối tượng là sản xuất, mục đích là phân loại thuật ngữ); bảng này chỉ ghi
lại sự vắng mặt để định vị, không nhằm chê bài.

## 7. Tác động tới K1/K2/K3, và định vị mức tích hợp của luận án

- K1, K2, K3: **không liên quan** trực tiếp.
- **Định vị của khung luận án theo định nghĩa Kritzinger** (**[NCS]**, suy luận từ tr. 1017 và Hình 1–3):
  - Khung đề xuất: dữ liệu cảm biến → bằng chứng → kiểm tra → hành động do con người quyết định.
  - Chiều vật lý → số: dữ liệu cảm biến được nạp **tự động**; đầu ra AI được ghi thành bản ghi bằng chứng tự động.
    Kết quả kiểm tra của kỹ sư và trạng thái hành động được **nhập thủ công** vào hệ thống.
  - Chiều số → vật lý: không có tác động tự động; kỹ sư đọc bằng chứng, ra quyết định và thực hiện hành động ngoài
    hệ thống. Đối tượng số **không** đóng vai trò thực thể điều khiển.
  - Theo định nghĩa: DM là mọi trao đổi thủ công; DS là tự động một chiều từ vật lý sang số; DT là tự động cả hai
    chiều và đối tượng số có thể điều khiển vật lý. Khung của luận án có luồng tự động một chiều (cảm biến) và không
    có luồng tự động chiều ngược. Vì vậy **khung nằm ở mức bóng số (DS)**, không đạt mức DT. Mô hình BIM/IFC đứng riêng
    (chưa nối dữ liệu) là mức DM.
  - Hai điểm cần NCS quyết định: (i) Bài không nói luồng ngược **qua con người** có được coi là "tự động" hay không.
    Đọc theo chữ của định nghĩa thì không, vì DT đòi hỏi tích hợp hai chiều đầy đủ. (ii) Nếu tên đề tài còn dùng
    "song sinh số", tiểu luận cần khai báo mức DS rõ ràng ở lần đầu dùng (CLAUDE.md mục 11) và ghi rằng chiều ngược
    chủ ý do con người thực hiện (vì lý do giải trình an toàn, xem 5.6A). Hướng mở rộng lên DT chỉ nên nêu như một
    hướng sau này, không phải mục tiêu của luận án.
- Kết luận này chỉ đúng theo định nghĩa của một bài (2018, sản xuất). Boje và cs. (2020) đưa ra thang ba thế hệ cho
  song sinh số xây dựng, trong đó khung của luận án gần thế hệ 1–2 (xem `notes/5REDLQK8.md`).

## 8. Vị trí sử dụng trong tiểu luận v2

- 2.3: dẫn định nghĩa DM/DS/DT làm khung phân loại; nêu khoảng cách giữa số bài dùng chữ DT và số bài đạt mức DT.
- Dẫn nhập và 5.x: câu khai báo mức tích hợp của khung luận án (DS).
- Bảng thuật ngữ (đã có dòng "Song sinh số / Bóng số / Mô hình số theo Kritzinger 2018").
- Không dùng số liệu phần trăm để nói về công trình xây dựng; đây là số liệu của lĩnh vực sản xuất.
