# GXVWFUSA — Gardner và cs. (2021) — mới

Gardner P., Bull L.A., Gosliga J., Dervilis N., Worden K. Foundations of population-based SHM, Part III: Heterogeneous
populations – Mapping and transfer. *Mechanical Systems and Signal Processing* 149 (2021) 107142. DOI
10.1016/j.ymssp.2020.107142. Tiêu đề, tác giả, tạp chí, tập, mã bài và DOI đã kiểm trên trang đầu của bài (tr. 1, trang 2 của
PDF). Cả năm tác giả thuộc Dynamics Research Group, Đại học Sheffield (tr. 1). Nhận bài 23/12/2019, bản sửa 17/04/2020, chấp
nhận 15/07/2020 (tr. 1); ngày đăng trực tuyến không in trong bản này. Truy cập mở CC BY (tr. 1).

**Bản đã đọc:** bản chính thức của nhà xuất bản lưu trên White Rose Research Online (eprint 164492, "Published Version"),
tệp `pdf/GXVWFUSA_Gardner2021.pdf`, 30 trang PDF. Trang PDF 1 là trang bìa của White Rose; bài báo chiếm trang PDF 2–30.
Bài đánh số theo **mã bài 107142**; trang dẫn là **số trang in ở chân trang của bài** (tr. 1–29; tr. 1 không in số nhưng là
trang đầu). **Quy đổi: tr. n của bài = trang PDF n + 1.** Đọc toàn văn (gồm danh mục tài liệu) ngày 01/10/2026, kiểm phản chứng
GĐ2 cho UV-05 và UV-06.

Ký hiệu: (a) điều tác giả nói; (b) giới hạn tác giả tự nêu; **[NCS]** nhận định của NCS.

| Cột | Nội dung |
|---|---|
| Citekey / Số cũ | GXVWFUSA / mới |
| Tier / Cụm | Bổ sung phản chứng (không thuộc 30 key) / SHM–bu lông–EOV (phần chuyển giao tri thức giữa các công trình khác nhau) |
| Luận điểm | Trong SHM theo quần thể (PBSHM), các thành viên có phân bố dữ liệu khác nhau nên bộ phân loại học trên một công trình thường không dùng được cho công trình khác; ánh xạ và chuyển giao tri thức bằng thích nghi miền (domain adaptation) cho phép dùng nhãn của một công trình nguồn để phân loại dữ liệu chưa có nhãn của công trình đích, với điều kiện không gian đặc trưng và không gian nhãn nhất quán, hoặc được đối khớp (tr. 1–3, 6, 25). |
| Bằng chứng | Khung khái niệm (loại quần thể, loại học chuyển giao, bốn bài toán ánh xạ; tr. 2–8). Năm nhóm ca nghiên cứu dùng JDA: hai kết cấu cắt 5 tầng mô phỏng gần giống nhau (tr. 10, 13); hai kết cấu 5 tầng mô phỏng khác vật liệu (thép – nhôm) và kích thước (tr. 10, 16); các cặp kết cấu n – m tầng mô phỏng với không gian nhãn lệch một lớp, giải bằng thuật toán mới dựa trên MMD (tr. 11–24); và một mô hình số → một kết cấu 3 tầng thí nghiệm (tr. 24–27). Đặc trưng là tần số riêng có cản; bài toán là định vị vết nứt (mô phỏng) hoặc mức độ vết cưa (thí nghiệm). |
| Giới hạn | Xem mục 5. |
| Tác động K1/K2/K3 | K1: mở rộng (điều kiện chuyển giao được xác định bằng mức nhất quán đặc trưng – nhãn theo loại khác biệt và theo bài toán SHM; khác biệt do bố trí cảm biến và thu nhận dữ liệu được nêu là nguồn sai khác phân bố; tr. 2–3, 6–7). K2: không liên quan trực tiếp. K3: không liên quan. Chi tiết ở mục 7. |
| Vị trí sử dụng | 3.6 (chuyển giao giữa các công trình, thiếu nhãn ở công trình đích, mô hình số làm nguồn nhãn); 3.4 (chuyển giao âm, giả định ngầm của bộ phân loại); 5.6A (bối cảnh thích nghi miền bên cạnh [56]). |
| Mức đã đọc | Toàn văn (01/10/2026) |

## 1. Câu hỏi và đối tượng

- (a) Bài là phần thứ ba và cuối của loạt ba bài đặt nền cho PBSHM, sau phần I ([57] Bull 2021) và phần II (Gosliga và cs.)
  (tr. 1–2). PBSHM là quá trình dùng thông tin trong một quần thể công trình để thực hiện và cải thiện suy luận tổng quát cho
  cả quần thể (tr. 1).
- (a) Động cơ thứ nhất: các phương pháp học máy thông thường giả định dữ liệu huấn luyện và kiểm tra cùng phân bố; giả định này
  sụp đổ trong PBSHM vì mỗi thành viên có phân bố dữ liệu khác nhau "because of environmental variations, manufacturing and
  assembly differences, operational conditions etc." (tr. 2); ví dụ, bộ phân loại học trên một máy bay "will generally fail to
  classify" máy bay khác cùng đội (tr. 2).
- (a) Động cơ thứ hai: dữ liệu có nhãn hư hỏng cho mọi trạng thái quan tâm thường không thu được cho từng cá thể; thực tế
  "generally infeasible to obtain a complete label set for all possible damage states, even for one structure"; có thể gom nhãn
  từ toàn quần thể hoặc từ cơ sở dữ liệu lịch sử của các chiến dịch SHM khác (tr. 2).
- (a) Trọng tâm: đặc trưng dạng dao động riêng (modal features) và thích nghi miền như một nhánh của học chuyển giao; bài đưa ra
  cơ sở toán học về khi nào thích nghi miền khả thi, dựa trên tô pô của biểu diễn đồ thị (phần II), và đề xuất một quy trình mới
  cho kết cấu khác tô pô (tr. 1–2).

## 2. Khái niệm cốt lõi

| Khái niệm | Nội dung (a) | Trang |
|---|---|---|
| Quần thể; đồng nhất – không đồng nhất | Quần thể là một nhóm công trình (tối thiểu hai) cung cấp thông tin cho theo dõi sức khỏe. Quần thể đồng nhất: mọi cặp "nominally identical" trong một bối cảnh; không đồng nhất: các công trình khác nhau. Giữa hai loại là một phổ liên tục | 2 |
| Ba nguồn khác biệt của quần thể không đồng nhất | Hình học (kích thước, tỉ lệ), vật liệu (lớp vật liệu, vật liệu cụ thể, tính chất), tô pô (biểu diễn đồ thị khác nhau, gồm cả điều kiện biên và tải trọng – chú thích 1). Các loại có thể chồng nhau (Hình 1) | 2–4 |
| Quần thể đồng nhất (định nghĩa hình thức) | Đồng nhất về tô pô, tính chất hình học và vật liệu là các lần rút ngẫu nhiên từ một phân bố cơ sở tập trung p(Θ); trường hợp chặt nhất (hàm Dirac, mọi thành viên giống hệt) "never occurs in reality, but is the assumption in applying conventional machine learning methods trained on one structure, to another" | 3 |
| Khác biệt do thu nhận và xử lý dữ liệu | Khác biệt phân bố có thể đến từ ngoài tính chất kết cấu: bố trí cảm biến khác nhau làm phân bố dữ liệu khác, kể cả khi cảm biến đặt ở "cùng" một phần tử bất khả quy; tần số lấy mẫu khác làm đặc trưng khác. Bài **đơn giản hóa**, chỉ xét khác biệt kết cấu | 3 |
| Miền, nhiệm vụ, học chuyển giao (Định nghĩa 1–3) | Miền D = {không gian đặc trưng, phân bố biên}; nhiệm vụ T = {không gian nhãn, hàm dự báo}. Học chuyển giao cải thiện hàm dự báo của đích bằng tri thức từ nguồn, khi miền và/hoặc nhiệm vụ khác nhau. Trong thực tế tập dữ liệu đích thường **không có thông tin nhãn** nào, mỗi quan sát có một nhãn "thật" chưa biết; thường giả định số quan sát nguồn nhiều hơn đích | 3–4 |
| Học chuyển giao đồng nhất / không đồng nhất (Định nghĩa 4–5) | Đồng nhất: không gian đặc trưng và nhãn như nhau (cùng số chiều). Không đồng nhất: không gian đặc trưng khác, có thể cả không gian nhãn khác. Hai loại này **không** tương ứng trực tiếp với quần thể đồng nhất / không đồng nhất | 4 |
| Ba nhóm kỹ thuật học chuyển giao | Theo tham số (tinh chỉnh mạng nơ-ron, trong SHM chủ yếu cho ảnh), theo mẫu (trọng số theo mức tương tự), theo đặc trưng (tìm biểu diễn giảm khác biệt nguồn – đích; nhóm dùng trong bài) | 5 |
| Bản thể học và đồ thị tri thức | Được nêu như cách chuyển tri thức khác; không đi sâu vì bản thể học "do not form a method themselves ... for transferring label information directly to feature data"; là hướng sẽ khảo sát sau | 5 |
| Thang bài toán SHM của Rytter | Phát hiện, định vị, phân loại, đánh giá mức độ, tiên lượng; mỗi mức đòi hỏi một mức nhất quán nhãn khác nhau. Tiên lượng không xét (chú thích 2) | 5–6 |
| Nhất quán đặc trưng – nhãn theo loại quần thể (Bảng 1) | Với đặc trưng dạng dao động và định vị ở mức nút/cạnh của đồ thị: khác hình học → nhất quán; khác vật liệu → nhãn phân loại, đánh giá có thể không nhất quán (kim loại không có tách lớp; ngay cả cùng vật liệu, "grade or batch properties" có thể làm nhãn đánh giá không nhất quán); khác tô pô → đặc trưng và nhãn định vị không nhất quán; nếu liên kết khác loại, ví dụ "one structure is assembled via bolted joints and the other structure welded", nhãn phân loại và đánh giá không nhất quán | 6–7 |
| Bốn bài toán ánh xạ (Bảng 2) | Nhất quán/không nhất quán đặc trưng × nhãn → học chuyển giao đồng nhất hoặc không đồng nhất, có hoặc không đối khớp không gian nhãn (label-space matching). Đối khớp nhãn khó vì miền đích thường không có nhãn "or minimally labelled with undamaged labels only"; nên đặt bài toán sao cho nhãn nhất quán khi có thể | 6–7 |
| Quan hệ với "dạng" (phần I) và học đa nhiệm | Dạng quần thể giả định nhãn nhất quán (theo trạng thái bình thường), học trong miền dữ liệu nên phương sai thường bị thổi phồng; học đa nhiệm có thể giúp loại ảnh hưởng gây nhiễu (dẫn Sohn 2007) | 7–8 |
| Chuyển giao âm (negative transfer) | Thông tin bị ánh xạ sai làm hiệu năng kém hơn học chỉ trên đích; hay xảy ra khi nguồn rất khác đích; khó xác định trước, đặc biệt khi nhãn không nhất quán hoặc đích không có nhãn. Đây là lý do cần thước đo tương tự giữa các công trình (phần II) | 8 |
| Thích nghi miền (Định nghĩa 6) | Không gian đặc trưng và nhãn như nhau, nhưng phân bố biên khác (và có thể phân bố có điều kiện khác) | 8 |
| JDA (Joint Distribution Adaptation, Long và cs. 2013) | Thuật toán dùng trong bài: tìm ánh xạ ẩn tối thiểu hóa khoảng cách MMD giữa phân bố biên và phân bố có điều kiện theo lớp của nguồn và đích; giả định đích **hoàn toàn không có nhãn**, dùng nhãn giả (pseudo-label) do bộ phân loại học trên nguồn dự báo, lặp nhiều lần; nghiệm qua bài toán trị riêng | 8–9 |
| TCA, ARTL, các phương pháp khác | TCA (Pan và cs. 2011) và ARTL (Long và cs. 2014) chỉ được dẫn như thuật toán thích nghi miền cho học chuyển giao đồng nhất ([13], [17]; tr. 8); không dùng trong ca nghiên cứu. **BDA không được nhắc đến** trong bài | 8, 28 |
| Bài toán (L + N) và (L + 1) | Không gian nhãn nguồn là tập con của đích, đích có thêm N (hoặc 1) nhãn không có ở nguồn | 11–12 |
| Thuật toán 1 (mới) | Phân cụm không giám sát đích thành L + 1 cụm (GMM); lần lượt bỏ một cụm, học JDA cho từng tổ hợp, chọn tổ hợp có MMD nhỏ nhất làm phần khớp với nguồn; phân cụm lại trong không gian biến đổi, gán nhãn nguồn cho cụm tương ứng, cụm thừa để không nhãn. Giả định: nguồn có nhãn đủ mọi lớp; đích không có nhãn nhưng đủ tách để phân cụm; hình học dữ liệu của L lớp ở nguồn và đích tương tự (giả định đa tạp đơn giản) | 12–15 |

## 3. Dữ liệu và thiết kế đánh giá

**Ca 3.2 – quần thể đồng nhất (mô phỏng)** (tr. 10, 13):
- Hai kết cấu cắt 5 bậc tự do; độ cứng mỗi tầng là tổng độ cứng đầu bốn dầm công xôn; hư hỏng là vết nứt mở ở một dầm
  (10 % bề rộng, cách chân 15 % chiều dài), mô phỏng ở mỗi tầng → 6 lớp (không hư hỏng + 5 vị trí) (tr. 10). Tham số nguồn và đích
  gần như nhau (Bảng 3, tr. 11).
- Đặc trưng: 5 tần số riêng có cản; Ns = 1800, Nt = 1200, tập kiểm tra đích riêng Ntest = 1500, các lớp cân bằng (tr. 10).
- JDA 10 vòng lặp, nhân tuyến tính, kNN 5 láng giềng; kiểm định chéo 5 phần chọn μ = 1 × 10⁻³, k = 4 (tr. 10).

**Ca 3.3 – khác hình học và vật liệu, nhãn nhất quán (mô phỏng)** (tr. 10, 13, 16):
- Hai kết cấu 5 tầng, một bằng thép, một bằng nhôm, khác kích thước (Bảng 5, tr. 13); cùng bài toán định vị 6 lớp; cùng cỡ
  dữ liệu và thiết lập JDA như Ca 3.2 (tr. 10).

**Ca 3.4 – khác tô pô, nhãn không nhất quán (mô phỏng)** (tr. 11–24):
- Các cặp kết cấu n – m tầng, chỉ khác số tầng (Bảng 7, tr. 16); định vị vết nứt mở ở mỗi tầng; phân cụm bằng GMM; JDA 10 vòng
  lặp, nhãn giả bằng kNN (tr. 14–15).
- 3.4.1: 3 tầng → 3 tầng, khác vật liệu – hình học (Bảng 8, tr. 17), cụm hư hỏng tầng 2 bị bỏ khỏi nguồn; Ns = 900, Nt = 800,
  Ntest = 1000; k = 2, μ = 0,5 (tr. 15).
- 3.4.2: 3 → 4 tầng, đánh nhãn từ đầu ngàm; Ns = 1200, Nt = 1000, Ntest = 1250 (tr. 18).
- 3.4.3: 4 → 5 tầng, đánh nhãn từ đầu ngàm; Ns = 1500, Nt = 1200, Ntest = 1500; μ = 10 (tr. 18).
- 3.4.4: 2 → 3 tầng, đánh nhãn từ đầu ngàm; Ns = 900, Nt = 800, Ntest = 1000; k = 1, μ = 0,5 (tr. 19–20).
- 3.4.5–3.4.7: lặp lại 2 → 3, 3 → 4, 4 → 5 tầng với cách đánh nhãn từ đầu tự do xuống (tr. 21–24).

**Ca 3.5 – mô hình số → kết cấu thí nghiệm** (tr. 24–27):
- Nguồn có nhãn: mô phỏng số kết cấu cắt 3 tầng, kích thước đo từ kết cấu thật, tính chất vật liệu và cản ước lượng (nhôm 6082)
  (Bảng 9, tr. 26); mô hình "deliberately oversimplified" (tr. 24).
- Bài toán mức độ: vết cưa giữa nhịp ở một dầm giữa nền và tầng 1, tăng 5 mm từ 0 đến 20 mm → 5 lớp (tr. 24); tác giả lưu ý bài
  toán mức độ đúng ra nên đặt là hồi quy, ở đây giải như phân loại để minh họa (chú thích 6, tr. 23).
- Đặc trưng: 3 tần số uốn riêng; nguồn 250 điểm mỗi lớp, Ns = 1250 (tr. 24–25).
- Đích: thử nghiệm dao động bằng máy rung điện động gắn ở tầng 1, ba gia tốc kế một trục ở mỗi tầng, kích thích ồn trắng dải rộng
  6553,6 Hz, 16384 vạch phổ (độ phân giải 0,2 Hz), cửa sổ Hanning; mỗi mức hư hỏng kích thích 5 lần → **Nt = 25** (tr. 24–25).
  Kết cấu thí nghiệm lấy từ nghiên cứu trước [4] (Hình 24, tr. 26).
- JDA: k = 2, μ = 1 theo kiểm định chéo 5 phần; kNN k = 4 (tr. 24–25).

## 4. Kết quả (như tác giả báo cáo)

- (a) Ca 3.2: độ chính xác kNN không JDA 83,8 % (huấn luyện ánh xạ) và 83,9 % (kiểm tra); JDA 100,0 % và 100,0 % (Bảng 4, tr. 13).
- (a) Ca 3.3: kNN không JDA 16,7 % và 16,7 %, "equivalent to random guessing"; JDA 100,0 % và 100,0 % (tr. 10, Bảng 6 tr. 16).
  Tác giả kết luận các kịch bản PBSHM đặt được dưới dạng nhất quán đặc trưng – nhãn "are achievable with current transfer learning
  technologies" (tr. 10).
- (a) 3.4.1: MMD nhỏ nhất khi bỏ cụm "3", đúng với giả định; 100 % chính xác với các lớp L đã biết ở cả tập huấn luyện và kiểm
  tra đích, cụm thừa được một thành phần Gauss riêng nắm trọn (tr. 15–17).
- (a) 3.4.2: chọn đúng cụm thừa, chuyển giao dương, phân loại đúng các lớp L (tr. 18).
- (a) 3.4.3: MMD nhỏ nhất không ở tổ hợp đúng; "all of the JDA mappings produce negative transfer"; thuật toán "has been demonstrated
  to fail" (tr. 18–19).
- (a) 3.4.4: MMD chọn sai, nhưng nếu bỏ đúng cụm "4" thì chuyển giao dương, độ chính xác 99,9 %, 98,9 %, 98,1 % (nguồn, huấn luyện
  đích, kiểm tra đích) (tr. 20).
- (a) 3.4.5: đánh nhãn từ đầu tự do làm thuật toán chọn đúng cụm, nhưng không gian biến đổi một chiều khó tách lớp: 99,1 % ở
  nguồn, 76,6 % và 76,0 % ở đích; phần lớn lớp "3" bị nhầm thành lớp "1" (không hư hỏng) (tr. 22).
- (a) 3.4.6: chọn sai cụm; chuyển giao âm kể cả khi chọn đúng (tr. 22). 3.4.7: chọn sai cụm; nếu chọn đúng thì chuyển giao dương
  (tr. 24).
- (a) Ca 3.5: tần số riêng của mô hình số chỉ khoảng một nửa của kết cấu thật; độ chính xác tăng từ 48,0 % (kNN không JDA) lên
  88,0 % (JDA) (tr. 25, Bảng 10 tr. 27). Tác giả kết luận mô hình vật lý có thể cung cấp "label knowledge not currently obtainable
  from real world structures" (tr. 26–27).

## 5. Giới hạn

**(b) Tác giả tự nêu:**
- Bài chỉ xét khác biệt kết cấu; khác biệt do bố trí cảm biến, thu nhận và xử lý dữ liệu được nêu nhưng bị đơn giản hóa bỏ qua
  (tr. 3).
- Chỉ dùng một thuật toán (JDA) và một biến thể; thuật toán khác có thể cho hiệu năng khác, dù các thách thức chung vẫn áp dụng
  (tr. 8).
- Thuật toán 1 dựa trên giả định hình học cụm tương tự; ngoài một số trường hợp kết cấu cắt cụ thể, giả định này sụp đổ; không
  tổng quát cho mọi cặp n – m tầng; cho thấy "the issues with a fully black-box approach" (tr. 19, 22, 26).
- MMD có thể không phải tiêu chí tốt để chọn ánh xạ, nhưng vì đích không có nhãn nên khó vượt ra ngoài tiêu chí khoảng cách nếu
  không đưa thêm tri thức vật lý (tr. 20, 24).
- Cách đánh nhãn (từ đầu ngàm hay đầu tự do) ảnh hưởng kết quả; tương ứng vật lý của nhãn định vị khó xác định chắc chắn; cần
  nghiên cứu để PBSHM vững với chiến lược đánh nhãn (tr. 22, 26).
- Không gian biến đổi một chiều làm các lớp khó tách; việc cải thiện khả năng tách lớp không được theo đuổi (tr. 22).
- Bài toán mức độ đúng ra nên là hồi quy (chú thích 6, tr. 23); mô hình số trong Ca 3.5 cố ý đơn giản hóa và chưa được kiểm định
  (tr. 24, 26).
- Không có tri thức vật lý thì "there will always be a danger of black-box domain adaptation performing negative transfer" (tr. 26).
- Bản thể học và đồ thị tri thức chưa được khảo sát (tr. 5).

**[NCS] nhận định:**
- Bốn trong năm nhóm ca là dữ liệu mô phỏng kết cấu cắt nhiều tầng; ca thật duy nhất là một kết cấu 3 tầng nhôm trong phòng thí
  nghiệm, Nt = 25 phép đo, hư hỏng tạo bằng vết cưa. Không có công trình đang vận hành, không có nhà công nghiệp khung thép, mối
  nối bu lông, cầu trục hay biến động môi trường – vận hành. Việc áp sang nhà xưởng là diễn giải.
- Nhãn thật của miền đích được biết và dùng để chấm độ chính xác ở mọi ca (Bảng 4, 6, 10; Hình 26 phân biệt nhãn thật và nhãn dự
  báo, tr. 27). Thiết kế "đích không có nhãn" là giả lập; vấn đề nhãn đích ở hiện trường đến từ đâu không được bàn.
- Kết quả 100 % ở Ca 3.2, 3.3 đến từ dữ liệu mô phỏng, lớp cân bằng, hư hỏng đã định trước; không có báo cáo biến thiên theo lần
  lặp hay theo seed.
- Bài coi "assembly differences" là một nguồn khác biệt **giữa các thành viên** (tr. 2) và liên kết bu lông – hàn là một khác biệt
  tô pô **giữa hai công trình** (tr. 6); không có chỗ nào xét thay đổi theo thời gian của **cùng một** công trình (sửa chữa, thay
  thế, tháo – lắp, siết lại). Tìm trong toàn văn không thấy các từ repair, maintenance, replacement, inspection (trừ tên luận án
  Rytter trong danh mục, tr. 28).
- Bài là của nhóm Sheffield (năm tác giả cùng Dynamics Research Group, tr. 1), cùng nhóm với [57] Bull 2021 `W7AEKRT8`, Bull 2022
  `87NKU5IS`, Hughes 2022 `Z9RD5DMZ`, Worden 2007 `MCNRW6F5`, Cross 2011 `KPWFC4PI`. Theo quy ước đếm căn cứ theo nhóm tác giả,
  bài **không thêm một căn cứ độc lập**.

## 6. Đoạn dùng được cho tiểu luận

| Luận điểm | Trang | Loại |
|---|---|---|
| Phương pháp học máy thông thường giả định huấn luyện và kiểm tra cùng phân bố; giả định này không đúng giữa các công trình vì khác biệt môi trường, chế tạo, lắp ráp, vận hành; bộ phân loại học trên một công trình thường thất bại ở công trình khác | 2 | Trực tiếp (3.4, 3.6) |
| Không khả thi thu đủ nhãn cho mọi trạng thái hư hỏng, kể cả cho một công trình | 2 | Trực tiếp (UV-05, 3.6) |
| Không thể và không kinh tế khi làm hư hỏng một công trình theo nhiều cách để lấy dữ liệu cho học máy | 24 | Trực tiếp (3.6) |
| Giả định mọi thành viên giống hệt không bao giờ xảy ra trong thực tế, nhưng là giả định ngầm khi dùng bộ phân loại học trên công trình này cho công trình khác | 3 | Trực tiếp (3.4, K1) |
| Bố trí cảm biến và tần số lấy mẫu khác nhau làm phân bố dữ liệu khác nhau, kể cả trên cùng một phần tử | 3 | Trực tiếp (K1: cấu hình cảm biến, `OBS_CONTEXT`) |
| Mức nhất quán nhãn cần có phụ thuộc bài toán SHM (phát hiện → đánh giá); liên kết bu lông và liên kết hàn cho không gian nhãn phân loại, đánh giá khác nhau | 5–7 | Trực tiếp (1.2, 3.6) |
| Thích nghi miền (JDA) giả định đích không có nhãn, dùng nhãn giả; dễ chuyển giao âm khi nguồn khác xa đích hoặc nhãn không nhất quán | 8–9 | Trực tiếp (3.6, 5.6A) |
| Thích nghi miền hoạt động khi đặc trưng và nhãn nhất quán (khác vật liệu, kích thước), nhưng thất bại ở nhiều cặp khác tô pô | 10, 18–19, 22, 26 | Trực tiếp |
| Mô hình số chưa kiểm định có thể dùng để gán nhãn cho kết cấu thí nghiệm qua thích nghi miền | 24–27 | Trực tiếp (3.6; chỉ PTN, Nt = 25) |
| Bản thể học, đồ thị tri thức được nêu là hướng chuyển tri thức khác, chưa được khảo sát | 5 | Gián tiếp (2.2, 5.5: tiền lệ nhắc tới biểu diễn tri thức dạng đồ thị trong SHM) |
| Điều kiện để chuyển giao một mô hình (loại khác biệt, mức nhất quán đặc trưng – nhãn, cách đánh nhãn) là thông tin cần đi kèm kết quả nếu kết quả được dùng ở công trình khác | 2–7, 22 | Diễn giải [NCS] (K1, `VALIDITY_SCOPE`) |

## 7. Tác động tới K1/K2/K3

- **K1: mở rộng.** Bài xác định khi nào kết quả học được trên một công trình còn dùng được ở công trình khác bằng loại khác biệt
  (hình học, vật liệu, tô pô; tr. 2–4), mức nhất quán đặc trưng – nhãn theo bài toán SHM (Bảng 1, 2; tr. 6–7) và nêu thêm khác biệt
  do bố trí cảm biến, thu nhận dữ liệu (tr. 3). [NCS] Đây là các thành phần của phạm vi hiệu lực ở mức phương pháp; bài không ghi
  chúng kèm từng kết quả phân loại, và chỉ xét khác biệt giữa các công trình, không xét theo thời gian. Cùng chiều với K1.
- K2: không liên quan trực tiếp. [NCS] Bài nêu bố trí cảm biến làm đổi phân bố dữ liệu (tr. 3) nhưng không bàn ánh xạ cảm biến –
  cấu kiện theo thời gian hay tính liên tục định danh.
- K3: không liên quan. Bài không có người ra quyết định, kiểm tra hay hành động.

## 8. Kiểm phản chứng

**UV-05 (thiếu nhãn hư hỏng ở hiện trường): giải quyết một phần phát biểu gốc; không giải quyết phát biểu thu hẹp.**
- Điều bài đã làm: nêu rõ việc không thể thu đủ nhãn hư hỏng, kể cả cho một công trình, và gợi ý gom nhãn từ quần thể hoặc từ cơ sở
  dữ liệu lịch sử của các chiến dịch SHM khác (tr. 2); nêu việc làm hư hỏng công trình để lấy dữ liệu là không khả thi và không kinh
  tế (tr. 24); đề xuất hai cách giảm nhu cầu nhãn ở đích: chuyển nhãn từ công trình nguồn có nhãn bằng thích nghi miền (tr. 8–10) và
  dùng mô hình vật lý làm nguồn nhãn (tr. 24–27). Bài cũng ghi nhận miền đích thường không có nhãn, "or minimally labelled with
  undamaged labels only" (tr. 6, 11).
- Điều bài không làm: nhãn nguồn là nhãn mô phỏng hoặc nhãn hư hỏng tạo có chủ đích trong PTN (vết cưa); nhãn đích được biết và
  dùng để chấm điểm; không có nhãn sinh từ kiểm tra thực ở công trình đang vận hành, không có độ bất định của nhãn, không có người gán
  nhãn, không có bản ghi nối nhãn với phép đo và cấu kiện. Bài không bàn kiểm tra (không xuất hiện từ inspection trong thân bài).
- **Kết luận:** phát biểu thu hẹp hiện có của UV-05 giữ nguyên. [NCS] Có thể thêm vào câu định vị: hướng PBSHM còn giảm nhu cầu nhãn
  bằng chuyển nhãn giữa các công trình qua thích nghi miền và bằng mô hình vật lý làm nguồn nhãn (Gardner 2021, tr. 2, 24–27), trên
  dữ liệu mô phỏng và một kết cấu PTN. Mục "SHM theo quần thể phần III chưa kiểm" trong UV-05 có thể chuyển thành "đã kiểm".

**UV-06 (lần lắp ráp hoặc can thiệp bảo trì là ranh giới phạm vi hiệu lực của bằng chứng từ mối nối bu lông): không giải quyết.**
- Bài có hai chỗ gần nhất, đều xét khác biệt **giữa các thành viên** của quần thể, không theo thời gian của cùng một công trình:
  - "each member of the population will have differences in their data distributions, because of environmental variations,
    manufacturing and assembly differences, operational conditions etc." (tr. 2). "Assembly differences" là khác biệt lắp ráp giữa
    các cá thể, không phải giữa hai lần lắp của cùng một cá thể.
  - "if the joints change between structures, e.g. one structure is assembled via bolted joints and the other structure welded, then
    the classification and assessment label spaces will be inconsistent" (tr. 6). Đây là khác biệt loại liên kết giữa hai công trình.
- Bài **không** coi sửa chữa, thay thế, tháo – lắp hay siết lại của cùng một công trình là một dịch chuyển miền; trong toàn văn không
  có các từ repair, maintenance, replacement, reassembly, và không có ca nào mà miền nguồn và miền đích là hai giai đoạn của cùng một
  kết cấu. Mọi cặp nguồn – đích là hai kết cấu khác nhau hoặc mô hình số – kết cấu thật (tr. 10, 11–24, 24–27).
- [NCS] Khung khái niệm của bài cho phép đặt hai lần lắp của cùng một mối nối như hai miền (khác phân bố biên, tr. 2–3, 8), và ý
  "grade or batch properties" làm nhãn đánh giá không nhất quán (tr. 6) gần với ý đợt lắp đặt trong `VALIDITY_SCOPE`. Tuy nhiên đây là
  suy diễn của NCS, không phải điều bài nói; củng cố UV-06 về hướng, không tính là căn cứ.
- **Kết luận:** không cần thu hẹp UV-06 do bài này. Có thể thêm một câu định vị: PBSHM phần III xác định điều kiện chuyển giao giữa
  các công trình bằng loại khác biệt (gồm khác biệt lắp ráp và loại liên kết) và mức nhất quán đặc trưng – nhãn (tr. 2, 6–7), nhưng
  không xét thay đổi theo thời gian của cùng một công trình do can thiệp. Cách viết khuyến nghị "lần lắp ráp – can thiệp phải được ghi
  để kiểm được hiệu lực" giữ nguyên. Mục "phần III Gardner 2021 chưa kiểm" trong UV-06 có thể chuyển thành "đã kiểm"; còn "nghiên cứu
  theo dõi dài hạn sau bảo trì" vẫn chưa kiểm.

**Ghi chú nhóm tác giả:** cùng nhóm Sheffield với [57], Hughes 2022, Bull 2022, Worden 2007, Cross 2011; không tăng số căn cứ độc lập
cho UV-05 hay UV-06.

## 9. Vị trí sử dụng

- 3.6: thiếu nhãn ở từng công trình; chuyển nhãn giữa công trình bằng thích nghi miền; mô hình số làm nguồn nhãn; ranh giới
  chuyển giao (tr. 2, 6–10, 24–27).
- 3.4: giả định ngầm cùng phân bố khi dùng bộ phân loại cho công trình khác; chuyển giao âm (tr. 2–3, 8).
- 5.6A: bối cảnh cho thích nghi miền bên cạnh [56] (TCA); bài này dùng JDA (tr. 8–9). [NCS] Nếu dẫn, phải là nguồn mới
  `\[@GXVWFUSA\]` và cần dòng mới trong `matrix/doi_chieu_danh_muc.csv` (`so_cu = "moi"`); chưa thêm trong phiên này.
