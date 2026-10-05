# ESTEYBHA — Chen và cs. (2021) — [10]

Chen L, Xie X, Lu Q, Parlikad AK, Pitt M, Yang J. Gemini Principles-Based Digital Twin Maturity Model for Asset
Management. *Sustainability* 2021, 13, 8224. DOI 10.3390/su13158224.

Đối chiếu trang 1 bản PDF (01/10/2026): tiêu đề, sáu tác giả, tạp chí *Sustainability*, năm 2021, tập 13, số bài
8224, DOI 10.3390/su13158224 khớp với dòng "Citation" và chân trang 1. Nhận 30/04/2021, chấp nhận 21/05/2021, xuất bản
23/07/2021. Bài có 15 trang ("1 of 15" … "15 of 15"). Trang 1 không in số kỳ (issue); chuỗi DOI "su1315…" gợi ý số 15
— bản ghi Zotero ESTEYBHA ghi Issue 15 (kiểm 01/10/2026), khớp.

**Bản đã đọc:** PDF nhà xuất bản (MDPI, truy cập mở CC BY), tệp Zotero `storage/YFD6FTS8/Chen et al. - 2021 - Gemini
Principles-Based Digital Twin Maturity Model for Asset Management.pdf`, 15 tr. Trang dẫn dưới đây là số trang của bài
(tr. 1–15). Đọc toàn văn ngày 01/10/2026, phiên T2-3, gồm Phụ lục A (Bảng A1, A2) và đọc trực tiếp số liệu trên Hình 3
(tr. 9) vì phần chữ của PDF không chứa số liệu của hình.

Ký hiệu: (a) điều tác giả nói; (b) giới hạn tác giả tự nêu; **[NCS]** nhận định của NCS.

| Cột | Nội dung |
|---|---|
| Citekey / Số cũ | ESTEYBHA / [10] |
| Tier / Cụm | Tier 2 / Song sinh số |
| Luận điểm | Các mô hình trưởng thành hiện có (chủ yếu cho BIM) chỉ xét một số khía cạnh, thiếu nền lý thuyết và không đo được việc triển khai song sinh số; tác giả đề xuất mô hình trưởng thành song sinh số cho quản lý tài sản, dựng trên Gemini Principles, gồm 3 chiều chính, 9 chiều con, 27 tiêu chí chấm điểm (rubric) và 6 giai đoạn trưởng thành theo khoảng điểm (tr. 1–2, 5, 7–8). |
| Bằng chứng | Tổng quan tài liệu và đối chiếu 8 công cụ đo trưởng thành BIM theo Gemini Principles (tr. 4–5, Bảng A1); chọn tiêu chí từ 8 ca thực tế và tài liệu (tr. 6, Bảng 1); khảo sát Likert 5 mức về mức quan trọng của tiêu chí, 100 người được mời, 40 phiếu hợp lệ (tr. 6, Bảng 3, Bảng A2); minh họa trên 2 ca: Shanghai Tower và thí điểm song sinh số CDBB West Cambridge (tr. 9–10, Bảng 6, Hình 3). |
| Giới hạn | Xem mục 6. |
| Tác động K1/K2/K3 | K1: không liên quan trực tiếp (tiêu chí chất lượng dữ liệu ở mức dự án, không ở mức bản ghi; mục 5). K2: không liên quan trực tiếp; một tiêu chí gần (T4: nhắc và ghi nhận tháo dỡ, thay thế; tr. 13). K3: không liên quan (không có hành động, trạng thái, thẩm quyền). Liên quan chủ yếu đến **định vị** (UV-04). |
| Vị trí sử dụng | 2.3 (các cách phân mức song sinh số: theo luồng dữ liệu [8], theo thế hệ [7], theo độ trưởng thành [10]); 2.1 (Gemini Principles, nguyên tắc "Trust/Quality" trong quản lý tài sản); 5.5 (câu định vị: schema của luận án không là mô hình trưởng thành). |
| Mức đã đọc | Toàn văn (01/10/2026) |

## 1. Câu hỏi, đối tượng và bối cảnh

- (a) Câu hỏi: thiếu một mô hình rõ ràng để đánh giá các giai đoạn triển khai song sinh số và đề ra lộ trình phát
  triển; công cụ hiện có (CMMI, COBIT, BIM Proficiency Index, BIM Maturity Matrix) chỉ xét khía cạnh hẹp như công nghệ,
  quy trình, thiếu căn cứ lý thuyết, và phần lớn đánh giá việc dùng BIM chứ không phải song sinh số (tr. 2).
- (a) Đối tượng: quản lý tài sản công trình xây dựng ở giai đoạn vận hành – bảo trì (O&M), mức **dự án** (tr. 2–3, 10).
  Các ca tham khảo ở Bảng 1 đều là tòa nhà (trường đại học, tòa tháp, tòa thị chính, nhà hát) (tr. 3).
- (a) Song sinh số được hiểu theo định nghĩa của Gemini Principles: biểu diễn số thực tế của vật thể vật lý, tạo giá trị
  qua hiểu biết tốt hơn để hỗ trợ quyết định (tr. 2). Tác giả mô tả song sinh số thường có năm lớp: thu nhận dữ liệu,
  truyền, mô hình hóa số, tích hợp dữ liệu/mô hình, ứng dụng (tr. 2, dẫn [21]).
- **[NCS]** Ba đồng tác giả (Xie, Lu, Parlikad) cũng là tác giả của [3]; ca thí điểm West Cambridge (tòa nhà IfM) là
  cùng tòa nhà của [3] (Bảng 1, dòng cuối, tr. 3). Khi đếm căn cứ độc lập, [10] và [3] thuộc cùng một nhóm.

## 2. Gemini Principles được dùng làm khung (tr. 4, Bảng 2)

(a) Gemini Principles do CDBB đề xuất cho song sinh số quốc gia, gồm ba tiêu đề và chín nguyên tắc (tr. 4; Bảng 2 được
tác giả "sửa đổi theo" [20], tức Bolton và cs. 2018, CDBB_REP_006):

| Tiêu đề | Nguyên tắc | Phát biểu (tóm lược theo Bảng 2) |
|---|---|---|
| Purpose (mục đích) | Public good | phục vụ lợi ích công lâu dài |
| | Value creation | tạo giá trị, cải thiện hiệu năng |
| | Insight | cho thêm hiểu biết về môi trường xây dựng |
| Trust (tin cậy) | Security | bảo đảm an ninh và tự an toàn |
| | Openness | mở (ví dụ có lược đồ dữ liệu mở) |
| | Quality | dựa trên dữ liệu có chất lượng phù hợp |
| Function (chức năng) | Federation | dựa trên khả năng liên tác an toàn của dữ liệu |
| | Curation | có chủ sở hữu, quản trị và điều tiết rõ ràng |
| | Evolution | thích ứng, phát triển, mở rộng theo công nghệ |

(a) Đánh giá 8 công cụ BIM theo chín nguyên tắc: khía cạnh Trust "bị bỏ qua bởi đa số công cụ" (tr. 5, Bảng A1, tr. 12);
khía cạnh Function được xét đầy đủ ở nhiều công cụ (tr. 5).

## 3. Cấu trúc mô hình trưởng thành

### 3.1 Chiều và tiêu chí (tr. 7, Bảng A2 tr. 12–13)

(a) Ba chiều chính = ba tiêu đề Gemini; chín chiều con = chín nguyên tắc; mỗi chiều con có ba tiêu chí, tổng 27
(tr. 2, 7). Phân bố theo Bảng A2:

| Chiều | Chiều con | Tiêu chí |
|---|---|---|
| Purpose | Insight | O1 mục tiêu dự án; O2 sơ đồ quy trình nghiệp vụ; O3 kế hoạch vận hành của tổ chức |
| | Value Creation | O4 cải thiện hiệu năng quản lý khi có song sinh số; O5 có đơn vị tư vấn/chuyên gia đủ năng lực; O6 kinh nghiệm, năng lực của nhân sự và tạo giá trị |
| | Public Good | O7 định nghĩa vai trò và trách nhiệm trong tổ chức; O8 chương trình đào tạo; O9 chiến lược truyền thông giữa các bên |
| Function | Curation | F1 kỹ thuật cập nhật/thu dữ liệu–mô hình theo hiện trạng (camera, cảm biến); F2 lưu trữ, trao đổi, chia sẻ; F3 trực quan hóa |
| | Federation | F4 tích hợp dữ liệu; F5 tích hợp tài sản; F6 kỹ thuật đăng ký tài sản (RFID, QR) |
| | Evolution | F7 quy trình/công nghệ tạo và cập nhật mô hình/dữ liệu; F8 chia sẻ thông tin/mô hình; F9 cập nhật và thu dữ liệu tài sản |
| Trust | Security | T1 tính toàn vẹn và chính xác của mô hình hiện trạng (BIM); T2 bảo đảm an ninh thông tin; T3 chuẩn và giao thức chính thức |
| | Openness | T4 nhắc và ghi nhận tháo dỡ, thay thế; T5 liên tác IFC/COBie (openBIM); T6 tính toàn vẹn, chính xác, mở của thông tin/dữ liệu thu được |
| | Quality | T7 hướng dẫn triển khai song sinh số cho quản lý tài sản; T8 cơ chế/quy tắc bảo đảm chất lượng liên tục; T9 quy định chính thức về dịch vụ và cung cấp dữ liệu (chuẩn trao đổi dữ liệu) |

- (a) Mọi tiêu chí có trung bình mức quan trọng từ 3,32 (T4) đến 4,20 (T1), Sig. (2 phía) = 0,000 (Bảng A2, tr. 12–13;
  ghi chú: p < α = 0,01, tc(40; 0,01) = 2,704).
- **[NCS] Điểm không nhất quán trong bài:** (i) đoạn văn tr. 7 gán F1 cho "liên tác dữ liệu" (Federation) và F5 cho
  "được điều tiết" (Curation), trong khi Bảng A2 xếp F1 vào Curation và F5 vào Federation; (ii) cột "Symbol" của Bảng
  A2 ghi P1–P9 cho tiêu chí O1–O9 và đổi chỗ T3/T6; (iii) tr. 7 nói tiêu chí có "mô tả chi tiết" ở Bảng A2, nhưng Bảng
  A2 chỉ có tên tiêu chí, không có mô tả từng mức điểm; (iv) ở mục 5–6 (tr. 10) ba chiều được gọi là "ontology,
  methodology, knowledge and value" thay cho Purpose/Function/Trust, ánh xạ suy từ ký hiệu là O = ontology,
  F = methodology, T = knowledge and value; (v) tr. 8 nói "năm giai đoạn" nhưng Bảng 5 liệt kê sáu.

### 3.2 Cách tính điểm (tr. 7–8, Bảng 4, Hình 2)

(a) Mỗi tiêu chí chấm theo thang Likert 5 mức; tổng mỗi chiều AO, AF, AT = tổng 9 tiêu chí (tối đa 45). Bốn chỉ số:
s = (AO + AF + AT)/3 (tác giả gọi là "tổng" ba chiều; công thức là trung bình) để xác định giai đoạn; S = diện tích tam
giác trên hệ ba trục để so sánh giữa dự án; SS (tác giả gọi là "variance"; công thức là căn của tổng bình phương độ lệch chia 2, tức độ lệch chuẩn mẫu) để đánh giá tính đồng đều; SO, SF, ST = độ
lệch của từng chiều so với s để chỉ chiều mất cân đối nhất (tr. 8, Bảng 4).

### 3.3 Giai đoạn trưởng thành (tr. 8, Bảng 5)

(a) Xây dựng dựa trên thang trưởng thành thông tin tài sản bảy giai đoạn của ICE [40] và ISO 55000 [41] (tr. 8):

| Giai đoạn | Mô tả (tóm lược) | Khoảng điểm s |
|---|---|---|
| Unaware | dự án nền: không IoT, tài sản chưa kiểm kê, ít cơ sở dữ liệu | 0 |
| Identifiable | tài sản nhận dạng và đăng ký một phần; dữ liệu thiết kế liên kết với định danh tài sản | < 9 |
| Aware | tài sản nhận dạng, đăng ký; IoT tích hợp một phần để theo dõi hiện trạng; có dùng mô hình số | ≥ 9 và < 18 |
| Communicative | có ontology; tài sản và dữ liệu chia sẻ theo định dạng chuẩn | ≥ 18 và < 27 |
| Interactive | ontology rõ; có phương pháp hỗ trợ truy xuất thông tin và tích hợp tài sản; tri thức và giá trị chia sẻ được | ≥ 27 và < 36 |
| Instructive and Intelligent | quản lý tài sản bán tự động/tự động, tự hỗ trợ quyết định thông minh và khởi phát hành động | ≥ 36 và ≤ 45 |

**[NCS]** Giai đoạn được xác định bằng **điểm trung bình** của ba chiều, không bằng việc thỏa các điều kiện mô tả trong
cột thứ hai; mô tả giai đoạn và cách chấm không được nối với nhau bằng quy tắc nào trong bài.

## 4. Phương pháp và kiểm chứng

- (a) Ba bước (tr. 5–6, Hình 1): (1) tổng quan tài liệu về mô hình trưởng thành; (2) dựng mô hình: chiều từ Gemini
  Principles, tiêu chí chọn từ phân tích ưu, nhược điểm của 8 ca thực tế (Bảng 1) và tổng quan tài liệu; (3) xác nhận
  tiêu chí bằng khảo sát trực tuyến, rồi kiểm chứng mô hình trên hai ca thật "bằng phương pháp bảng hỏi" (tr. 6).
- (a) Khảo sát: gửi 100 chuyên gia; sau ba tuần thu 41 phiếu (41 %), loại 1 phiếu thiếu, còn 40 (tr. 6). Kinh nghiệm:
  < 2 năm 4 (10 %), 2–4 năm 18 (45 %), 5–7 năm 16 (40 %), > 8 năm 2 (5 %); 100 % có hiểu biết về hoạt động O&M số hóa
  (tr. 6, Bảng 3). Câu hỏi là mức quan trọng của từng tiêu chí (1 = không quan trọng, 5 = rất quan trọng) (tr. 6).
  Không có phỏng vấn sâu hay Delphi (tìm trong văn bản: không có "Delphi", "interview").
- (a) Ca nghiên cứu (tr. 9, Bảng 6): Shanghai Tower (đối tượng khảo sát: Giám đốc nền tảng FM-BIM; dữ liệu tích hợp BIM,
  BMS, hệ quản lý cơ sở vật chất; thiết bị: cảm biến BMS, QR, RFID) và thí điểm CDBB West Cambridge (đối tượng: nghiên cứu
  viên chính của dự án; BIM, BMS, các hệ quản lý tài sản, không gian, đăng ký tài sản; cảm biến BMS, cảm biến không dây,
  QR). "Nghiên cứu hiện trường" được thực hiện riêng cho từng dự án (tr. 9).
- (a) Kết quả trên Hình 3 (tr. 9; đọc trực tiếp từ hình): Dự án 1 AO = 30, AF = 30, AT = 31, s1 = 30,33, S1 = 199,35,
  SS1 = 0,58; Dự án 2 AO = 33, AF = 36, AT = 37, s2 = 35,33, S2 = 270,32, SS2 = 2,08, SO2 = −2,33. Cả hai ở giai đoạn
  Interactive (tr. 10, mục a); Dự án 2 trưởng thành hơn (S2 > S1); Dự án 2 cần cải thiện chiều "ontology", ví dụ O4
  (tr. 10, mục b–d). Tiêu chí T4 (ghi nhận tháo dỡ, thay thế) được 2/5 ở cả hai dự án (Hình 3).
- (a) Tác giả kết luận mô hình cho phương pháp trực quan, có hệ thống và định lượng để tự đánh giá và so sánh chéo
  (tr. 10). Tóm tắt dùng cụm "đánh giá định tính" (tr. 1) **[NCS: không nhất quán với "định lượng" ở tr. 2, 10]**.

## 5. Quan hệ với DM/DS/DT của Kritzinger và cs. [8] và với độ tin cậy dữ liệu

- **Mức tích hợp luồng dữ liệu:** (a) bài không dùng hay dẫn khái niệm mô hình số, bóng số (tìm "shadow", "Kritzinger":
  0 kết quả); không phân biệt luồng dữ liệu thủ công / tự động một chiều / hai chiều. Yếu tố tự động chỉ xuất hiện ở
  mô tả giai đoạn cao nhất ("bán tự động/tự động quản lý tài sản … khởi phát hành động", tr. 8, Bảng 5) và ở tiêu chí
  F1, F9 (kỹ thuật cập nhật, thu dữ liệu) (tr. 13). **[NCS]** Trục phân mức của [10] là độ trưởng thành tổ chức – kỹ
  thuật tổng hợp (mục đích, tin cậy, chức năng); trục của [8] là mức tự động của luồng dữ liệu. Hai trục khác nhau: một
  hệ có thể đạt "Interactive" theo [10] mà vẫn chỉ là DM hoặc DS theo [8]. Bài gọi cả hai ca là song sinh số; Bảng 1 lại
  mô tả Shanghai Tower là "digital prototype based on BIM" (tr. 3). Bài không mô tả chiều luồng dữ liệu của hai ca nên
  không xếp được theo [8] từ nội dung bài.
- **Vai trò con người trong quyết định:** (a) có tiêu chí O7 "định nghĩa vai trò và trách nhiệm trong tổ chức" (tr. 12)
  và giai đoạn cao nhất là hỗ trợ quyết định "on its own" (tr. 8). **[NCS]** Không có định nghĩa ai ra quyết định gì,
  dựa vào dữ liệu nào; vai trò được chấm như một thuộc tính của tổ chức.
- **Tin cậy – chất lượng – nguồn gốc dữ liệu:** (a) Trust là một trong ba chiều; nguyên tắc Quality yêu cầu dữ liệu "có
  chất lượng phù hợp" (tr. 4); tiêu chí liên quan: T1 toàn vẹn, chính xác của mô hình hiện trạng; T6 toàn vẹn, chính xác,
  mở của dữ liệu thu được; T8 cơ chế/quy tắc bảo đảm chất lượng liên tục; T4 ghi nhận tháo dỡ, thay thế (tr. 13).
  (a) Không có từ "provenance", "uncertainty", "traceability", "lineage" trong văn bản. **[NCS]** Chất lượng được đánh
  giá như một mức độ của cả dự án trên thang 1–5, không như thuộc tính gắn với từng bản ghi dữ liệu hay từng đầu ra phân
  tích; không có nguồn gốc xử lý, phiên bản phương pháp hay phạm vi hiệu lực.

## 6. Giới hạn

**(b) Tác giả tự nêu:**
- Mô hình ở mức dự án; song sinh số cấp thành phố, quốc gia chịu ảnh hưởng khác (văn hóa, chính sách) nên không suy ra
  trực tiếp từ mức dự án (tr. 10).
- Hướng tiếp theo: dùng "nhóm chuyên gia" (expert pool) ở bước đánh giá; mở rộng mô hình cho cấp thành phố (tr. 10).
  **[NCS]** Điều này ngầm cho thấy bước đánh giá hai ca hiện tại chưa dùng nhóm chuyên gia.

**[NCS] nhận định:**
- Khảo sát chỉ đo **mức quan trọng** của tiêu chí đã chọn sẵn, không kiểm độ tin cậy giữa người chấm, độ giá trị cấu
  trúc hay khả năng phân biệt giai đoạn. Kiểm định có p = 0,000 cho mọi tiêu chí nhưng bài không nêu giả thuyết so sánh
  (giá trị kiểm định) của phép kiểm (Bảng A2). 85 % người trả lời có 2–7 năm kinh nghiệm (Bảng 3).
- Kiểm chứng trên hai ca, mỗi ca một nhóm đối tượng được nêu bằng một vai trò (Bảng 6); không rõ ai chấm từng tiêu chí và
  dựa trên chứng cứ gì. Ca 2 là dự án của chính nhóm tác giả và nhà tài trợ (CDBB; mục Funding, tr. 11), nên có nguy cơ tự
  đánh giá.
- Không có mô tả mức điểm cho từng tiêu chí (mục 3.1), nên khó lặp lại việc chấm.
- Các điểm không nhất quán nội bộ nêu ở mục 3.1, 3.3, 4 (tên chiều, ánh xạ F1/F5, số giai đoạn, "định tính/định lượng").
- Đối tượng là tòa nhà và quản lý cơ sở vật chất; không có kết cấu, kiểm tra kết cấu hay bảo trì kết cấu. Áp sang nhà công
  nghiệp khung thép là diễn giải.

## 7. Đoạn dùng được cho tiểu luận

| # | Nội dung dùng được | Trang | Dùng ở | Ghi chú |
|---|---|---|---|---|
| 1 | Gemini Principles: 3 tiêu đề (Purpose, Trust, Function), 9 nguyên tắc; Quality = dữ liệu có chất lượng phù hợp | 4 (Bảng 2) | 2.1, 2.3 | Nguồn gốc là [20] Bolton 2018; nếu trích chính văn Gemini Principles cần nhập [20] vào Zotero |
| 2 | Mô hình trưởng thành song sinh số cho quản lý tài sản: 3 chiều, 9 chiều con, 27 tiêu chí, 6 giai đoạn theo điểm | 2, 7–8 | 2.3 | Viết "sáu giai đoạn (Bảng 5)", không chép chữ "năm" của tr. 8 |
| 3 | Chiều Trust bị đa số công cụ đo trưởng thành BIM bỏ qua | 5, 12 (Bảng A1) | 2.3 | Bằng chứng (a) |
| 4 | Đối chiếu trục phân mức: [8] theo luồng dữ liệu, [7] theo thế hệ, [10] theo độ trưởng thành tổng hợp | 4–8 | 2.3, Dẫn nhập (khai báo mức DS) | Phần đối chiếu là diễn giải [NCS] |
| 5 | Chất lượng và tin cậy dữ liệu được coi là một chiều của trưởng thành song sinh số, đánh giá ở mức dự án | 4, 7, 13 | 3.5, 5.5 | Câu cùng chiều cho K1; diễn giải "mức dự án, không mức bản ghi" là [NCS] |
| 6 | Tiêu chí T4 "nhắc và ghi nhận tháo dỡ, thay thế"; điểm 2/5 ở cả hai ca | 13, 9 (Hình 3) | 4.x (K2), chỉ minh họa | Số liệu đọc từ hình; chỉ hai ca, không khái quát |

## 8. Kiểm phản chứng

### UV-04 (định vị mức tích hợp DM/DS/DT cho kiểm tra – bảo trì)

- **Đối chiếu:** [10] đưa ra một thang phân mức song sinh số cho quản lý tài sản công trình (Bảng 5, tr. 8), dựng trên
  Gemini Principles (tr. 4, 7). Thang này xếp theo điểm tổng hợp của mục đích – tin cậy – chức năng; không có tiêu chí về
  chiều và mức tự động của luồng dữ liệu (mục 5); đối tượng là tòa nhà, quản lý cơ sở vật chất, không có kiểm tra – bảo
  trì kết cấu (tr. 3, 9); vai trò ra quyết định chỉ là một tiêu chí cấp tổ chức (O7, tr. 12).
- **Kết luận: giải quyết một phần.** Phần đã có: một phân loại mức độ song sinh số cho quản lý tài sản công trình đã tồn
  tại, nên không thể nói "chưa có phân loại mức" một cách chung. Phần không giải quyết: phân loại theo mức tích hợp luồng
  dữ liệu DM/DS/DT, gắn với kiểm tra – bảo trì kết cấu và với việc con người ra quyết định dựa trên dữ liệu.
- **Phát biểu thu hẹp đề xuất:** "Đã có thang trưởng thành song sinh số cho quản lý tài sản công trình (Chen và cs.
  2021, theo Gemini Principles), nhưng thang này đo độ trưởng thành tổng hợp ở mức dự án (mục đích, tin cậy, chức năng),
  không đo chiều và mức tự động của luồng dữ liệu như phân loại DM/DS/DT của [8], và không gắn với kiểm tra – bảo trì kết
  cấu có kỹ sư ra quyết định. Vì vậy luận án khai báo mức tích hợp của hệ đề xuất theo [8], và chỉ dùng [10] để nêu rằng
  độ trưởng thành là một trục phân loại khác."
- **Còn chưa kiểm:** Sepasgozar 2021 [9]. [NCS] Giữ nguyên đánh giá trước: UV-04 chỉ dùng để định vị, không phát triển
  thành khoảng trống.

### UV-02 (nguồn gốc, phiên bản phương pháp, phạm vi hiệu lực của đầu ra phát hiện)

- **Đối chiếu:** chiều Trust có nguyên tắc Quality và các tiêu chí T1, T6, T8 về toàn vẹn, chính xác và bảo đảm chất lượng
  liên tục (tr. 4, 13). Không có nguồn gốc, độ bất định, phiên bản phương pháp hay phạm vi hiệu lực; không có đầu ra phát
  hiện hay dự đoán nào được đánh giá (mục 5).
- **Kết luận: không giải quyết.** [10] chỉ là căn cứ cùng chiều cho nhận định rằng chất lượng dữ liệu được coi là điều
  kiện của song sinh số trong quản lý tài sản (tr. 4), ở mức dự án. Phát biểu thu hẹp của UV-02 giữ nguyên. Về đếm căn
  cứ: [10] cùng nhóm tác giả với [3], không tăng số căn cứ độc lập.
