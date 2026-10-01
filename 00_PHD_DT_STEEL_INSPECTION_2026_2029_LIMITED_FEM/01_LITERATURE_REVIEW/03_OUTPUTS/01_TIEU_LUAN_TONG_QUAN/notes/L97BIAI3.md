# L97BIAI3 — Beleites, Neugebauer, Bocklitz, Krafft & Popp (2013) [14]

Beleites C, Neugebauer U, Bocklitz T, Krafft C, Popp J. Sample size planning for classification models. *Analytica Chimica
Acta* 760 (Special Issue: Chemometrics in Analytical Chemistry 2012): 25–33, 2013. DOI 10.1016/j.aca.2012.11.007.
Thông tin thư mục kiểm theo khung "This paper has been published as" ở trang 1 của tệp và dòng trích dẫn ở tr. 12, 16
(phụ lục bổ sung).

**Bản đã đọc:** **bản thảo tác giả đã được chấp nhận** (Accepted Author Manuscript), bản arXiv 1211.1323v3 [stat.AP] ngày
03/05/2015 ("Preprint submitted to Elsevier, May 5, 2015"; tr. 1), không phải bản in của nhà xuất bản. Tệp Zotero
`C:/Users/VNT/Zotero/storage/G9WMG2DZ/Beleites et al. - 2013 - Sample size planning for classification models.pdf`, 16 tr.
PDF: thân bài tr. 1–10 (gồm tài liệu tham khảo), phụ lục bổ sung I (ma trận nhầm lẫn, tr. 11–12) và II (mã R cho mục 4,
tr. 12–16). Trang dẫn dưới đây là **trang của bản thảo** (đánh số 1–16, trùng trang PDF). Bản in là tr. 25–33; chưa đối
chiếu bản in, nên **không quy đổi** sang trang in khi trích. Trích văn bản bằng PyMuPDF; các hình (Hình 3–7) đọc qua chú
thích và lời bàn. Đọc toàn văn (gồm phụ lục bổ sung) ngày 01/10/2026, phiên T2-3.

Ký hiệu: (a) điều tác giả nói; (b) giới hạn tác giả tự nêu; **[NCS]** nhận định của NCS.

| Cột | Nội dung |
|---|---|
| Citekey / Số cũ | L97BIAI3 / 14 |
| Tier / Cụm | Tier 2 / Độ tin cậy đánh giá |
| Luận điểm | Với cỡ mẫu nhỏ điển hình (5–25 ca độc lập thống kê mỗi lớp), mô hình phân loại có thể đạt hiệu năng chấp nhận được nhưng hiệu năng đó **không chứng minh được** vì bất định ngẫu nhiên do cỡ tập kiểm tra cũng nhỏ; cần khoảng 75–100 ca kiểm tra độc lập để đo một bộ phân loại tốt với độ chính xác hợp lý, và thường cần hàng trăm ca (hoặc không thể) để chứng minh một bộ phân loại tốt hơn bộ khác (tr. 1, 9–10). Số ca độc lập là cỡ mẫu ở **mức cao nhất của cấu trúc phân cấp dữ liệu** (bệnh nhân, mẻ nuôi cấy), không phải số phổ (tr. 1). |
| Bằng chứng | Bộ dữ liệu khoảng 2550 phổ Raman tế bào đơn, năm lớp (hồng cầu, bạch cầu, ba dòng tế bào ung thư) (tr. 1, 3–4; Bảng 1); mô phỏng phổ phân phối chuẩn nhiều chiều dựng từ trung bình và hiệp phương sai của dữ liệu thật, với tập kiểm tra lớn (tr. 4); bộ phân loại PLS-LDA 10 biến ẩn (tr. 4); kiểm chứng chéo 5 phần lặp 100 lần, 100 "tập dữ liệu tăng dần" (tr. 5); khoảng tin cậy Bayes với tiên nghiệm đều (HPD) cho tỉ lệ nhị thức (tr. 8); tính cỡ mẫu so sánh hai tỉ lệ độc lập theo Fleiss (gói R Hmisc) (tr. 9); mã R ở phụ lục II (tr. 12–15). |
| Giới hạn | Xem mục 5. |
| Tác động K1/K2/K3 | K1: mở rộng (căn cứ phương pháp rằng độ bất định của một chỉ số hiệu năng do **số đơn vị độc lập** trong tập kiểm tra quyết định, và đơn vị đó là mức cao nhất của cấu trúc phân cấp; chia theo phổ thay vì theo mẻ/bệnh nhân cho kết quả lạc quan nặng, tr. 1, 3–5, Bảng 1). K2, K3: không liên quan. |
| Vị trí sử dụng | 3.4 (độ tin cậy của đánh giá: đơn vị độc lập, bất định do cỡ tập kiểm tra); 5.6A (đánh giá theo nhóm, chấm điểm theo bản ghi, báo cáo bất định; đã là số cũ được phép trích); 5.7 (khai báo khoảng tin cậy và cỡ mẫu khi đặt ngưỡng chỉ số, khóa ngưỡng trước kiểm chứng); 1.3A/3.5 (trường `uncertainty` và đơn vị suy luận của `VALIDITY_SCOPE`, mức diễn giải). |
| Mức đã đọc | Toàn văn, gồm phụ lục bổ sung I–II (01/10/2026); hình đọc qua chú thích |

## 1. Câu hỏi và đối tượng

- (a) Câu hỏi: cần bao nhiêu mẫu để **huấn luyện** một bộ phân loại tốt, và bao nhiêu mẫu để **chứng minh** nó tốt; tác giả
  cho rằng xây được mô hình tốt là chưa đủ, hiệu năng phải được chứng minh (tr. 1).
- (a) Bối cảnh: quang phổ sinh học, nơi mẫu độc lập thống kê có chú giải phù hợp hiếm và đắt; tác giả nói ý tưởng và kết
  luận áp dụng cho phạm vi rộng hơn, vì bài toán cỡ mẫu nhỏ phổ biến ở nhiều lĩnh vực (tr. 1).
- (a) Kiểm tra bộ phân loại được xem như một **phép đo** hiệu năng, chịu sai số hệ thống (thiên lệch) và ngẫu nhiên
  (phương sai), giống huấn luyện là phép đo tham số mô hình (tr. 2).

## 2. Phương pháp

### 2.1 Đơn vị độc lập (trọng tâm đọc)

- (a) **Cấu trúc phân cấp:** dù bộ dữ liệu thường có hàng nghìn phổ, số ca độc lập có ý nghĩa thống kê thường rất nhỏ vì
  nhiều phổ đo trên cùng mẫu vật, nhiều mẫu vật của cùng bệnh nhân; hoặc nhiều phổ mỗi tế bào, nhiều tế bào mỗi mẻ nuôi cấy.
  "Số ca độc lập thống kê được cho bởi cỡ mẫu ở mức cao nhất của cấu trúc phân cấp dữ liệu, tức bệnh nhân hoặc mẻ nuôi cấy
  tế bào" (tr. 1). Từ đó cỡ mẫu điển hình là 5–25 ca độc lập mỗi lớp (tr. 1).
- (a) Tóm tắt nêu ví dụ đơn vị độc lập: "bệnh nhân, mẻ, v.v." (tr. 1).
- (a) **Nguồn biến động thật của bộ dữ liệu:** tế bào từ 5 người cho khác nhau (bạch cầu, hồng cầu) và 5 mẻ nuôi cấy khác
  nhau (dòng tế bào); đo vào ngày chuẩn bị và một ngày sau (9 ngày đo); hai máy laser cùng mẫu, cùng hãng (tr. 3).
- (a) **Giả định có chủ ý:** để có bộ dữ liệu đủ lớn làm "chuẩn thật" cho tính toán tham chiếu, tác giả **giả vờ không biết**
  các yếu tố ảnh hưởng này và coi các phổ là độc lập; hệ quả là "không suy ra được hiệu năng nhận dạng dòng tế bào nói
  chung từ nghiên cứu này: kết quả sẽ lạc quan nặng" (tr. 3–4, dẫn Bảng 1 và [14] của bài về kiểm tra đại diện).
- (a) **Đối chứng chia theo mẻ:** Bảng 1 (tr. 4) có thêm cột "real PLS-LDA batch-wise", trong đó kiểm chứng chéo chia theo
  bệnh nhân/mẻ "như cấu trúc của phép đo đòi hỏi" (tr. 5). Kết quả xem mục 3.1.
- (a) Khoảng tin cậy Bayes dựa trên phân phối Beta nên tính được với số "thành công" k không nguyên; vì vậy tỉ lệ p̂ tính từ
  nhiều phổ có thể dùng với cỡ tập kiểm tra n_test **bằng số bệnh nhân hoặc số mẻ được kiểm tra** (tr. 8).
- (a) Khi tính cỡ mẫu so sánh, đơn vị là "ca kiểm tra độc lập thật sự thuộc lớp bt" (tr. 9); kiểm định ghép cặp mạnh hơn
  nhưng không dùng được trong nghiên cứu này vì phải nuôi mẻ tế bào mới (tr. 9).
- [NCS] Bài phân biệt rõ ba khái niệm: số phổ (bản ghi đo), số đơn vị độc lập (mức cao nhất của phân cấp), và cách chia
  kiểm chứng (theo phổ hay theo mẻ). Đây là lý lẽ phương pháp cho "đơn vị suy luận" trong `VALIDITY_SCOPE`: hiệu năng chỉ
  có nghĩa với đơn vị mà tập kiểm tra đã tách độc lập.

### 2.2 Đo hiệu năng và bất định

- (a) Hiệu năng tính bằng tỉ lệ ca kiểm tra từ các phần của ma trận nhầm lẫn: độ nhạy, độ đặc hiệu, giá trị dự đoán dương/âm
  (tr. 2, Hình 1). Giá trị dự đoán cần tần suất tương đối (xác suất tiên nghiệm) của các lớp; dữ liệu đo theo kiểu phân tầng
  nên tác giả không tính được (tr. 2–3).
- (a) Mẫu số n_test khác nhau giữa các tỉ lệ: độ nhạy dùng số ca thật sự thuộc lớp, nên mẫu số nhỏ và kém chính xác hơn độ
  đặc hiệu; vì vậy bài minh họa bằng độ nhạy (tr. 2).
- (a) Độ đặc hiệu trong bài toán nhiều lớp gộp các phân biệt dễ với các phân biệt khó; tăng ca ở lớp dễ làm độ đặc hiệu tăng
  mà không cải thiện phân biệt quan trọng; đoán ngẫu nhiên đã cho độ đặc hiệu 0,77–0,85 trong bài toán năm lớp, còn độ nhạy
  đoán ngẫu nhiên khoảng 0,20 (tr. 2).
- (a) Kiểm tra mô tả như quá trình Bernoulli: p̂ = k / n_test, phương sai p(1 − p) / n_test (tr. 2, công thức 1–2).
- (a) Với cỡ mẫu nhỏ, phù hợp nhất là bootstrap hoặc kiểm chứng chéo k phần lặp; trung bình trên các mô hình thay thế
  (surrogate model) là ước lượng không thiên lệch cho mô hình cùng cỡ tập huấn luyện; **phương sai quan sát giữa các mô hình
  thay thế có thể đánh giá thấp phương sai thật**, vì dù mô hình hoàn toàn ổn định, hiệu năng quan sát vẫn chịu bất định do
  cỡ tập kiểm tra hữu hạn (tr. 2–3).
- (a) Gộp kết quả các mô hình thay thế chỉ hợp lệ nếu chúng có cùng hiệu năng thật, tức mô hình ổn định với tập huấn luyện
  bị xáo trộn; mô hình không ổn định làm tăng phương sai (tr. 3). Dùng hiệu năng của mô hình thay thế làm xấp xỉ cho mô hình
  cuối giả định đường học phẳng giữa hai cỡ tập huấn luyện; vi phạm giả định này gây thiên lệch bi quan quen biết (tr. 3).
- (a) Hai nguồn bất định ngẫu nhiên: (1) bất ổn định của mô hình (liên quan cỡ tập huấn luyện), (2) bất định kiểm tra do số
  ca kiểm tra hữu hạn (tr. 7). Mô phỏng với tập kiểm tra rất lớn cho phép tách hai nguồn; với dữ liệu thật thì không tách
  được (tr. 4).

### 2.3 Thiết kế thực nghiệm

- (a) Tiền xử lý phổ: căn chỉnh số sóng theo đỉnh CaF2 ở 322 cm⁻¹, nội suy làm trơn, hiệu chỉnh đường nền bằng đa thức,
  chuẩn hóa diện tích (tr. 3).
- (a) Từ khoảng 2500 phổ, rút các tập dữ liệu cỡ 25 ca mỗi lớp, phần còn lại làm tập kiểm tra lớn (tr. 4). Lớp nhỏ nhất (rbc)
  vẫn cho độ chính xác của độ nhạy tốt hơn ±0,052 (khoảng tin cậy 95 % tại độ nhạy 0,5) (tr. 4).
- (a) Mô phỏng: 100 tập nhỏ 25 phổ mỗi lớp; tập kiểm tra lớn 4 · 10⁴ phổ mỗi lớp (độ chính xác tốt hơn 0,5 ± 0,005; σ ≤ 0,0025);
  một tập huấn luyện lớn 2 · 10⁴ phổ mỗi lớp để ước lượng hiệu năng tốt nhất có thể (tr. 4).
- (a) Bộ phân loại: PLS-LDA, 10 biến ẩn khi có ít nhất 4 phổ huấn luyện mỗi lớp; với tập cực nhỏ, giới hạn tối đa bằng một
  nửa tổng số phổ huấn luyện (tr. 4). LDA trên điểm PLS ít bất ổn hơn LDA trên dữ liệu nhiều biến (tr. 4).
- (a) Kiểm chứng: kiểm chứng chéo 5 phần, lặp 100 lần; chọn thay cho out-of-bootstrap vì cỡ tập huấn luyện hiệu dụng của
  bootstrap không biết được và thiên lệch bi quan của nó thường lớn hơn kiểm chứng chéo 5 hoặc 10 phần (tr. 5).
- (a) Đường học (learning curve) tính theo kiểu "tập dữ liệu tăng dần" (100 tập), mô phỏng thực tế thu mẫu dần; phân biệt
  với đường học "hồi cứu" (tr. 5).

### 2.4 Tính cỡ tập kiểm tra

- (a) Hai kịch bản (tr. 8): (1) định trước độ rộng chấp nhận được của khoảng tin cậy; (2) số ca cần để so sánh hai bộ phân
  loại.
- (a) Kịch bản 1: khoảng tin cậy Bayes, tiên nghiệm đều, khoảng ngắn nhất (HPD), gói R `binom` (tr. 8). Khoảng rộng nhất
  tại p̂ = 0,5 và hẹp nhất tại p̂ = 0 hoặc 1; có thể tính thận trọng tại p̂ = 0,5 hoặc dùng hiểu biết về hiệu năng kỳ vọng
  (tr. 8).
- (a) Kịch bản 2: kiểm định giả thuyết cho hai tỉ lệ độc lập với cỡ mẫu khác nhau, hàm `bpower`, `bsamsize` của gói Hmisc
  theo Fleiss và cs.; xấp xỉ này đánh giá cao lực kiểm định với mẫu nhỏ; công suất có thể kiểm bằng `bpower.sim` (tr. 9).

## 3. Kết quả (số liệu như tác giả báo cáo)

### 3.1 Chia theo phổ và chia theo mẻ (Bảng 1, tr. 4)

| Lớp | Số phổ | Độ nhạy, chia theo phổ (TB, P5–P95) | Độ nhạy, chia theo bệnh nhân/mẻ |
|---|---|---|---|
| rbc (hồng cầu) | 372 | 0,99 (0,96–0,99) | 0,97 (0,96–0,98) |
| leu (bạch cầu) | 569 | 0,97 (0,96–0,97) | 0,87 (0,84–0,90) |
| mcf (MCF-7) | 558 | 0,91 (0,90–0,92) | 0,31 (0,24–0,42) |
| bt (BT-20) | 532 | 0,75 (0,74–0,76) | 0,38 (0,32–0,45) |
| oci (OCI-AML3) | 518 | 0,89 (0,88–0,90) | 0,30 (0,23–0,17) [in như vậy] |

- (a) Khi chia theo bệnh nhân/mẻ, PLS-LDA 10 biến ẩn vẫn nhận dạng hồng cầu gần hoàn hảo, độ nhạy bạch cầu gần 0,90, nhưng
  với các dòng tế bào ung thư mô hình "về cơ bản là đoán" (tr. 5). Ma trận nhầm lẫn chia theo mẻ ở phụ lục I (tr. 12) cho thấy
  ba dòng ung thư bị xếp gần đều vào ba lớp (ví dụ hàng mcf: 0,33 / 0,37 / 0,30).
- [NCS] Đây là bằng chứng định lượng trong chính bài: cùng mô hình, cùng dữ liệu, chỉ đổi đơn vị chia tập từ phổ sang mẻ,
  độ nhạy ba lớp khó giảm từ 0,75–0,91 xuống 0,30–0,38.
- (a) Hiệu năng tốt nhất trên dữ liệu mô phỏng (tập huấn luyện 2 · 10⁴ mỗi lớp): LDA không PLS đạt 1,00 cho rbc, leu và 0,91
  cho bt; PLS-LDA 10 biến ẩn đạt 1,00, 0,99 và 0,72 (tr. 4).

### 3.2 Đường học bị bất định kiểm tra che khuất (tr. 5–8)

- (a) Với cỡ mẫu nhỏ, một tập cụ thể cỡ n_train có thể khác xa tập trung bình cùng cỡ (tr. 5; Hình 3–4, vùng tô gồm 90 trong
  100 tập).
- (a) Kiểm chứng chéo là ước lượng không thiên lệch của hiệu năng mô hình nhưng chịu bất định ngẫu nhiên lớn hơn nhiều vì số
  ca kiểm tra ít hơn tập kiểm tra lớn (tr. 6). Với dữ liệu thật chỉ có khoảng 350–540 phổ kiểm tra tham chiếu; bất định ngẫu
  nhiên tổng của kiểm chứng chéo bị chi phối bởi việc chỉ kiểm tra với tối đa 25 mẫu của tập nhỏ (tr. 7).
- (a) Trong lượt ví dụ trên dữ liệu mô phỏng: độ nhạy hồng cầu bị đánh giá cao nhiều (lượt khác đánh giá thấp tương tự); hiệu
  năng đặc biệt tốt của bạch cầu với 4–10 mẫu huấn luyện không được kiểm chứng chéo phát hiện, ngược lại xuất hiện hai chỗ
  trũng; với BT-20 có dao động khi thêm từng ca đến 9 mẫu (trung bình 7,2 mẫu huấn luyện) (tr. 7). Với dữ liệu thật, đường học
  của bạch cầu khớp khá sát, của BT-20 "không giống cả về hình dạng" (tr. 7–8).
- (a) Kết luận mục: trung bình kiểm chứng chéo lặp **không khôi phục đáng tin hình dạng đường học** của tập cụ thể trong các
  kịch bản cỡ mẫu nhỏ; trong khi hiệu năng thật của bộ phân loại là chấp nhận được đến rất tốt: với 20 ca huấn luyện mỗi lớp,
  hồng cầu gần như nhận đúng hoàn toàn, bạch cầu độ nhạy khoảng 0,90, BT-20 khoảng 2/3 (tr. 8).

### 3.3 Cỡ tập kiểm tra theo độ rộng khoảng tin cậy (tr. 8–9; phụ lục II tr. 13)

- (a) Kiểm 100 bạch cầu, đúng 90: khoảng tin cậy 95 % từ 0,83 đến 0,94 — từ "khá kém" đến "khá tốt" trong bối cảnh bài, còn
  quá rộng để đánh giá thực tế (tr. 8, Hình 5). Mã R: 0,8254–0,9444 (tr. 13).
- (a) 6/6 hồng cầu đúng: khoảng tin cậy 95 % vẫn xuống tới 0,65 (tr. 8; mã R 0,6518, tr. 13). Với p̂ = 1, "đã" cần 58 ca để
  cận dưới đạt 0,95 (tr. 8; mã R tr. 13).
- (a) Yêu cầu độ rộng khoảng tin cậy dưới 0,10 khi hiệu năng kỳ vọng 0,90–0,95 tương ứng 3–5½ lần số mẫu kiểm tra thường có
  trong quang phổ sinh học; dưới 0,05 cần hàng trăm ca (tr. 8). Kết quả nhạy với p thật: p = 0,89 thay vì 0,90 thì cần 153
  thay vì 141 ca (tr. 8; Hình 6 tr. 9: n_test ≥ 141 khi độ nhạy kỳ vọng 0,9 và độ rộng ≤ 0,1; mã R tr. 13).

### 3.4 Cỡ tập kiểm tra để chứng minh bộ phân loại mới tốt hơn (tr. 9; phụ lục II tr. 14–15)

- (a) Giả sử BT-20 cải thiện từ độ nhạy 0,75 (bộ cũ kiểm với 25 ca) lên 0,90: kể cả cho bộ mới 10⁵ ca, lực kiểm định tối đa
  chỉ 1 − β = 0,62, tức không thể chứng minh tốt hơn với sai lầm loại II chấp nhận được vì tập kiểm tra của bộ cũ nhỏ (tr. 9;
  mã R 0,6218, tr. 14).
- (a) Với cỡ mẫu bằng nhau, lực 0,8 (α = 0,05) cần ít nhất 100 ca độc lập thuộc lớp bt cho mỗi mô hình (tr. 9; mã R 99,54,
  tr. 14).
- (a) Nếu đạt 0,975, cần 63 ca (α = β = 0,10); nếu thực chỉ 0,96, cần 117 ca (tr. 9; mã R tr. 15). Với α = β = 0,05, mô hình
  0,975 cần ít nhất 300 ca, mô hình 0,99 cần 116 ca (tr. 9, chú thích Hình 7).
- (a) Kết luận mục: bộ phân loại tốt cần kiểm với **ít nhất 75 ca** để có khoảng tin cậy đủ hẹp cho kết luận thực tế; chứng
  minh bộ mới tốt hơn thường cần nhiều hơn và thường không thể nếu tập kiểm tra của bộ cũ nhỏ (tr. 9).

### 3.5 Khuyến nghị

- (a) Bắt đầu kế hoạch cỡ mẫu bằng việc **định trước độ rộng khoảng tin cậy chấp nhận được** cho độ nhạy kỳ vọng; cỡ mẫu đó
  cho phép tính đường học hồi cứu và lập lại kế hoạch cỡ mẫu cho cả tập huấn luyện và tập kiểm tra (tr. 10).
- (a) Tóm tắt: 75–100 mẫu thường cần để kiểm một bộ phân loại tốt nhưng chưa hoàn hảo (tr. 1); > 75 ca (tr. 10); 140 ca cho
  độ rộng ≤ 0,1 khi độ nhạy kỳ vọng 90 % (tr. 10), trong khi bạch cầu đạt 90 % chỉ với khoảng 20 mẫu huấn luyện (tr. 10).

## 4. Điểm không nhất quán trong nguồn ([NCS] ghi nhận)

1. Bảng 1 (tr. 4), lớp oci, chia theo mẻ: "0.30 (0.23 – 0.17)" — cận trên nhỏ hơn cận dưới và nhỏ hơn trung bình; có thể là lỗi
   in. Không dùng khoảng này.
2. Cỡ tập kiểm tra lớn của mô phỏng: tr. 4 ghi 4 · 10⁴ phổ mỗi lớp (phụ lục I tr. 11 cũng là 40000), nhưng chú thích Bảng 1
   (tr. 4) và tr. 7 ghi n_test = 2 · 10⁴. Số 2 · 10⁴ ở tr. 4 là cỡ tập **huấn luyện** lớn.
3. Cỡ mẫu cho độ rộng ≤ 0,1 tại 0,9: 141 (tr. 8, chú thích Hình 6 tr. 9, mã R tr. 13) và 140 (tóm tắt, tr. 10).
4. Ngưỡng tổng quát: "75–100" (tr. 1), "ít nhất 75" (tr. 9), "> 75" (tr. 10). Không mâu thuẫn thực chất nhưng nên trích đúng câu
   theo trang.
5. Khoảng 0,83–0,94 được gọi là "đến quite good" trong thân bài (tr. 8) nhưng "đến really good" trong chú thích Hình 5 (tr. 8).
6. Số phổ: "khoảng 2550" (tr. 1) và "khoảng 2500" (tr. 4); tổng Bảng 1 là 2549.

## 5. Giới hạn

**(b) Tác giả tự nêu:**
- Coi các phổ là độc lập dù có cấu trúc người cho/mẻ/ngày đo/máy laser; vì vậy không suy ra được hiệu năng nhận dạng dòng tế bào
  nói chung, kết quả sẽ lạc quan nặng (tr. 3–4).
- PLS-LDA 10 biến ẩn là thiết lập rất hạn chế, hợp với cỡ mẫu nhỏ trong bài, còn nhận dạng tế bào ung thư lưu hành cần mô hình
  phức tạp hơn (tr. 5).
- Dữ liệu đo phân tầng, không phản ánh tần suất trong quần thể bệnh nhân, nên không tính được giá trị dự đoán (tr. 3).
- Phương pháp tính lực kiểm định (Fleiss) đánh giá cao lực với cỡ mẫu nhỏ; các cỡ mẫu tính ra chỉ là ước lượng thô; hiệu năng
  của bộ cải tiến chưa biết nên phải kiểm độ nhạy của kết quả với giả định (tr. 9).
- Phương sai giữa các mô hình thay thế có thể đánh giá thấp phương sai thật (tr. 3); với dữ liệu thật không tách được bất ổn định
  mô hình và bất định kiểm tra (tr. 4).
- Ví dụ cải thiện 0,75 → 0,975 là trường hợp cực đoan, lớn hơn nhiều so với cải thiện thường gặp (tr. 9).

**[NCS] nhận định:**
- Lĩnh vực quang phổ sinh học, một loại bộ phân loại (PLS-LDA), một bộ dữ liệu; không có SHM, kết cấu hay biến động môi trường –
  vận hành. Việc áp khái niệm "đơn vị độc lập ở mức cao nhất của phân cấp" sang kết cấu (lần lắp ráp, mẫu thí nghiệm, công trình)
  là **diễn giải**.
- Các con số cỡ mẫu (75, 100, 141…) phụ thuộc phương pháp khoảng tin cậy (Bayes, tiên nghiệm đều), mức tin cậy, hiệu năng kỳ vọng
  và giả định Bernoulli độc lập; không phải ngưỡng chung. Chỉ nên trích như ví dụ về bậc độ lớn.
- Mô phỏng phân phối chuẩn nhiều chiều là tình huống lý tưởng; không có cấu trúc phân cấp trong dữ liệu mô phỏng.
- Bài chỉ có một cột chia theo mẻ, không báo cáo cỡ mẫu tính theo số mẻ (5 mẻ/người cho mỗi lớp); không phân tích riêng ảnh hưởng
  của ngày đo hay máy laser.
- Bản đã đọc là bản thảo tác giả trên arXiv; số trang không phải trang in.
- Không có cơ chế ghi lại đơn vị độc lập, cách chia hay khoảng tin cậy kèm theo từng kết quả; bài là hướng dẫn phương pháp thiết kế
  và báo cáo.

## 6. Đoạn dùng được cho tiểu luận

| Luận điểm | Trang | Loại |
|---|---|---|
| Số ca độc lập thống kê là cỡ mẫu ở mức cao nhất của cấu trúc phân cấp dữ liệu (bệnh nhân, mẻ), không phải số phổ; nhiều nghìn phổ có thể chỉ tương ứng 5–25 ca độc lập mỗi lớp | 1 | Trực tiếp |
| Kiểm tra bộ phân loại là một phép đo hiệu năng, chịu thiên lệch và phương sai | 2 | Trực tiếp |
| Bất định của một tỉ lệ hiệu năng do số ca kiểm tra trong mẫu số quyết định (p̂ = k/n, Var = p(1−p)/n) | 2 | Trực tiếp |
| Coi các phổ cùng mẻ là độc lập cho kết quả lạc quan nặng; chia theo mẻ làm độ nhạy ba lớp khó giảm từ 0,75–0,91 xuống 0,30–0,38 | 3–5, Bảng 1 | Trực tiếp |
| Phương sai giữa các lượt kiểm chứng chéo có thể đánh giá thấp phương sai thật; báo cáo biến thiên theo lượt chưa đủ để thể hiện bất định do cỡ tập kiểm tra | 2–3 | Trực tiếp |
| Với cỡ mẫu nhỏ, kiểm chứng chéo không khôi phục đáng tin hình dạng đường học | 7–8, 10 | Trực tiếp |
| Kiểm 90/100 đúng vẫn cho khoảng tin cậy 95 % là 0,83–0,94, quá rộng để kết luận thực tế | 8 | Trực tiếp |
| Bộ phân loại tốt thường cần ít nhất 75 ca kiểm tra; so sánh hai bộ thường cần hàng trăm ca độc lập hoặc không thể | 1, 9–10 | Trực tiếp |
| Nên định trước độ rộng khoảng tin cậy chấp nhận được trước khi thu mẫu | 10 | Trực tiếp |
| Độ đặc hiệu nhiều lớp có thể cao ngay cả khi đoán ngẫu nhiên (0,77–0,85) | 2 | Trực tiếp |
| Trường `uncertainty` của bằng chứng cần gắn với số đơn vị độc lập đã kiểm tra, và đơn vị suy luận cần được khai báo trong `VALIDITY_SCOPE` | 1, 3–5, 8 | Diễn giải |
| Với kết cấu bu lông, lần lắp ráp/mẫu thí nghiệm đóng vai trò tương tự "mẻ" của bài: nhiều bản ghi đo trên cùng lần lắp ráp không phải là nhiều ca độc lập | 1, 3–5 | Diễn giải |
| Ngưỡng chỉ số ở 5.7 nên được khóa cùng độ rộng khoảng tin cậy và cỡ mẫu tính trước | 8–10 | Gián tiếp |

## 7. Kiểm phản chứng

- **UV-02 (nguồn gốc, phiên bản phương pháp, phạm vi hiệu lực của đầu ra phát hiện): không giải quyết.** Bài là hướng dẫn thiết
  kế và báo cáo đánh giá ở mức nghiên cứu; không có bản ghi nguồn gốc xử lý, phiên bản phương pháp hay phạm vi hiệu lực gắn với từng
  kết quả (toàn văn; [NCS]). Bổ sung cho **nội dung** phạm vi hiệu lực và độ bất định, cùng nhóm với Figueiredo 2011, [45], [48]:
  đơn vị độc lập là mức cao nhất của phân cấp (tr. 1); kết quả chia theo phổ không suy rộng được (tr. 3–4); khoảng tin cậy phụ thuộc
  số ca kiểm tra độc lập (tr. 2, 8); TG. Không tính vào số căn cứ của phát biểu "chưa được ghi".
- **UV-06 (lần lắp ráp hoặc can thiệp là ranh giới phạm vi hiệu lực): không giải quyết (không cùng đối tượng); có căn cứ phương
  pháp cùng chiều.**
  - Bài không bàn mối nối bu lông, lần lắp ráp hay can thiệp bảo trì.
  - Bài cho căn cứ phương pháp chung, tương tự [53] tr. 4–5: chia theo đơn vị cấp thấp (phổ) trong khi biến động thật nằm ở cấp
    mẻ/người cho/ngày đo cho kết quả lạc quan nặng, và chênh lệch đo được trong cùng bài (tr. 3–5, Bảng 1; TG). [NCS] Nếu coi lần
    lắp ráp là "mẻ" của kết cấu bu lông, đây là căn cứ cho việc phải ghi lần lắp ráp để chia tập và khai báo đơn vị suy luận; nhưng
    việc ánh xạ "mẻ" sang "lần lắp ráp" là diễn giải.
  - Đề nghị: NCS quyết định có tính [14] (2013, trước 2025) là căn cứ phương pháp chung gián tiếp của UV-06 như [53] hay không;
    nếu tính, ghi rõ "căn cứ phương pháp, khác lĩnh vực". Bài không có dữ liệu ngược chiều.
