# W7AEKRT8 — Bull và cs. (2021) [57]

Bull L.A., Gardner P.A., Gosliga J., Rogers T.J., Dervilis N., Cross E.J., Papatheou E., Maguire A.E., Campos C.,
Worden K. Foundations of population-based SHM, Part I: Homogeneous populations and forms. *Mechanical Systems and Signal
Processing* 148 (2021) 107141. DOI 10.1016/j.ymssp.2020.107141 (tiêu đề và DOI đã kiểm trên tr. 1 của PDF). Nhận bài
19/12/2019, trực tuyến 14/08/2020; truy cập mở CC BY.

**Bản đã đọc:** bản chính thức của nhà xuất bản, tệp `pdf/W7AEKRT8_Bull2021_PBSHM-PartI.pdf`, 19 tr. Bài đánh số theo
**mã bài 107141**; trang dẫn là **số trang in ở chân trang của bài** (tr. 1–19; tr. 1 không in số nhưng là trang đầu), trùng
với số trang PDF. Đọc toàn văn (gồm danh mục tài liệu) ngày 01/10/2026, phiên T2-2.

Ký hiệu: (a) điều tác giả nói; (b) giới hạn tác giả tự nêu; **[NCS]** nhận định của NCS.

| Cột | Nội dung |
|---|---|
| Citekey / Số cũ | W7AEKRT8 / 57 |
| Tier / Cụm | Tier 2 / SHM–bu lông–EOV (phần chuyển giao tri thức giữa các công trình tương tự) |
| Luận điểm | Với một công trình riêng lẻ hiếm khi có dữ liệu đo phủ đủ các điều kiện vận hành và hư hỏng, và tập nhãn có thể thiếu; SHM theo quần thể (PBSHM) đề xuất học một mô hình chung là "dạng quần thể" (population form) từ dữ liệu trạng thái bình thường của một phần các thành viên trong một quần thể đồng nhất, rồi dùng nó để phát hiện điểm mới cho mọi thành viên, kể cả thành viên không đóng góp dữ liệu (tr. 1, 3, 17). |
| Bằng chứng | Hai ca nghiên cứu: quần thể 19 hệ 8 bậc tự do mô phỏng cộng một giàn thí nghiệm của Los Alamos, đặc trưng là phần thực của hàm đáp ứng tần số, mô hình hồi quy quá trình Gauss (tr. 5–10); và dữ liệu SCADA đo trong 125 tuần ở một trang trại điện gió đang vận hành của Vattenfall, đặc trưng là đường cong công suất, mô hình hỗn hợp chồng lấp các quá trình Gauss (OMGP) (tr. 11–17). |
| Giới hạn | Xem mục 5. |
| Tác động K1/K2/K3 | K1: mở rộng (phạm vi áp dụng của mô hình được xác định bằng điều kiện thành viên quần thể và không gian đặc trưng, và việc chia dữ liệu theo thành viên giữ lại; tr. 2–3, 7). K2, K3: không liên quan trực tiếp. Chi tiết ở mục 7. |
| Vị trí sử dụng | 3.6 (chuyển giao tri thức trạng thái bình thường, thiếu nhãn hiện trường); 3.2 (biến động vận hành do người vận hành và bảo trì); 5.6A (học chỉ với dữ liệu trạng thái bình thường, phát hiện điểm mới). |
| Mức đã đọc | Toàn văn (01/10/2026) |

## 1. Câu hỏi và đối tượng

- (a) Bài là phần đầu của loạt ba bài đặt nền cho lý thuyết PBSHM; phần II và III (Gosliga và cs.; Gardner và cs.) bàn
  quần thể không đồng nhất (tr. 1–2).
- (a) Động cơ: trong SHM truyền thống, mô hình học từ một công trình chỉ phủ một phần các điều kiện vận hành, môi trường và
  hư hỏng; tập nhãn có thể không có hoặc không đủ; nếu chuyển được thông tin từ công trình này sang công trình tương tự thì
  có thể suy luận chẩn đoán cho công trình thiếu dữ liệu (tr. 1).
- (a) Bài chỉ xét trường hợp đơn giản nhất: các thành viên "giống nhau trên danh nghĩa" (nominally identical), ví dụ tuabin
  gió trong một trang trại (tr. 1).

## 2. Khái niệm cốt lõi

| Khái niệm | Nội dung (a) | Trang |
|---|---|---|
| Quần thể; biểu diễn đồ thị | Công trình được biểu diễn rút gọn bằng đồ thị (nút, cạnh, nút nối đất); đồ thị cho một thước đo tương tự giữa các công trình, từ đó xác định mức suy luận có thể chuyển giữa các thành viên. Thuộc tính của nút, cạnh mô tả tô pô, vật liệu, hình học | 2–3 (Hình 1) |
| Tương đương kết cấu | Đồ thị tương đương tô pô và nút nối đất ở cùng vị trí | 2 |
| Quần thể đồng nhất (Định nghĩa 1) | M công trình tương đương kết cấu từng cặp, với tham số vật liệu, hình học, vật lý được xem như các lần rút ngẫu nhiên từ một phân bố cơ sở p(Θ); nếu có một cặp không tương đương kết cấu thì quần thể là không đồng nhất | 2 |
| Quần thể đồng nhất mạnh | p(Θ) đơn đỉnh, độ phân tán thấp (ví dụ cấu kiện cùng mẫu, chỉ khác dung sai chế tạo); khi đó phương pháp SHM thông thường có thể áp dụng cho dữ liệu quần thể. Đây là trường hợp lý tưởng; trang trại điện gió khó đồng nhất mạnh do điều kiện biên đáy biển, tương tác gió cục bộ, khác biệt trong thực hành vận hành | 2 |
| Dạng (Form) và dạng quần thể (form) | Mở rộng khái niệm Hình thức của Plato: gồm bản chất của đối tượng và mức biến động kỳ vọng quanh lý tưởng trong quần thể. Về toán học, "form" là mô hình trong một không gian đặc trưng nắm cả hai thành phần đó; đối tượng có thể là vectơ đặc trưng chứ không phải bản thân kết cấu, nên không gian đặc trưng là một phần của mô tả dạng | 2–3 |
| Kiểm định mô hình dạng | Mô hình cần được kiểm định trong quần thể và không gian đặc trưng đã chọn, sao cho biểu diễn được biến động giữa các cá thể | 3 |
| Mô hình trạng thái bình thường chuyển giữa thành viên | Dạng được học từ dữ liệu trạng thái bình thường làm chuẩn; dữ liệu không đủ hoặc vắng ở nhiều thành viên; so sánh phép đo mới với dạng để phát hiện điểm mới cho toàn quần thể | 3 |
| Lựa chọn mô hình | Đặc trưng dạng hàm (đường cong công suất, hàm đáp ứng tần số) → hồi quy quá trình Gauss: trung bình dự báo là bản chất, phương sai dự báo là biến động quần thể; đặc trưng điểm đa biến → có thể dùng mô hình hỗn hợp Gauss | 3 |
| Biến động vận hành phải nằm trong dạng | Dạng phải mô hình được biến động vận hành không liên quan hư hỏng; dữ liệu có thể đổi đáng kể khi người vận hành can thiệp hoặc trong quy trình bảo trì, những thay đổi này không chỉ ra hư hỏng nên cần được dạng nắm bắt, nếu không sẽ thành dương tính giả | 11 |
| Cập nhật dạng | Có thể thêm một hàm ẩn (ví dụ K = 3) để đưa một trạng thái bình thường được phép mới vào dạng, với điều kiện trạng thái đó thực sự là trạng thái bình thường được chấp nhận | 15, 17 |

## 3. Dữ liệu và thiết kế đánh giá

**Ca I – quần thể đồng nhất mạnh (mô phỏng + một giàn thí nghiệm)** (tr. 5–8):
- Giàn 8 bậc tự do của Los Alamos là thành viên thứ 20; tham số khối lượng, độ cứng, cản được nhận dạng từ hàm đáp ứng tần
  số đo (tr. 5, Bảng 1 tr. 6). 19 thành viên mô phỏng rút tham số từ phân bố Gauss quanh giá trị nhận dạng, độ lệch 3 %
  (khối lượng), 1 % (độ cứng), 10 % (cản) (tr. 6, công thức 13).
- Đặc trưng: phần thực của hàm đáp ứng tần số H18, 1040 khoảng tần số 0–130 Hz, kích thích ồn trắng 8 s, nhiễu đo 40 dB
  (tr. 6). Hư hỏng: giảm độ cứng k5 7 %, 14 %, 24 % (mô phỏng) và 24 % (giàn) (tr. 6).
- Số liệu: mỗi thành viên mô phỏng 20 hàm đáp ứng bình thường để huấn luyện, 20 để kiểm tra, 20 cho mỗi mức hư hỏng; giàn
  có 8 hàm (4 bình thường, 4 hư hỏng 24 %) (tr. 6–7).
- Chia dữ liệu: chỉ S1–S10 đóng góp dữ liệu huấn luyện; S11–S20 (9 mô phỏng và giàn) giữ lại để kiểm tra khả năng tổng quát
  sang thành viên chưa thấy (tr. 7). Huấn luyện trên mẫu ngẫu nhiên 2000 quan sát vì lý do tính toán (tr. 7).
- Chỉ số điểm mới: khoảng cách Mahalanobis bình phương; ngưỡng bằng lấy mẫu bootstrap, mức 95,45 % (hai sigma) (tr. 8).

**Ca II – trang trại điện gió đang vận hành** (tr. 11–17):
- Dữ liệu SCADA của Vattenfall, 125 tuần, công suất trung bình và tốc độ gió theo khoảng 10 phút; loại, vị trí, số tuabin
  không được công bố vì bảo mật (tr. 11).
- Không có thông tin trạng thái cụ thể của từng tuabin; khi cần nhãn, đường cong công suất được phân loại "phần nào chủ
  quan" theo phán đoán kỹ thuật và tiêu chí của chuyên gia Vattenfall (tr. 11).
- Kỹ sư xem toàn bộ dữ liệu để gán nhãn bình thường là không hợp lý (125 đường cong mỗi tuabin), nên chỉ phân loại một tập
  con thành viên và một tập con tuần để học dạng (tr. 11).
- Cắt giảm công suất 50 % do người vận hành (vì bảo trì hay nhu cầu điện) xảy ra thường xuyên, không biểu thị hư hỏng, nên
  được đưa vào dạng như trạng thái bình thường (tr. 11, Hình 8b). Mô hình OMGP với K = 2 hàm ẩn (lý tưởng; cắt giảm 50 %)
  (tr. 12–15).
- Để vẽ biểu đồ kiểm soát, các đường cong tuần của **một** tuabin được gán nhãn thủ công tốt / xấu bằng quan sát trực quan
  và tiêu chí Vattenfall, thêm nhóm "mơ hồ" khi việc phân loại còn tranh cãi; tuabin dùng kiểm tra không đóng góp dữ liệu
  huấn luyện (tr. 15).

## 4. Kết quả

- (a) Ca I: dữ liệu bình thường của S1–S10 phần lớn dưới ngưỡng; có dương tính giả ở một số thành viên (S9, S11, S13, S18),
  tác giả cho là do bộ tham số "cực đoan" rút từ p(Θ) và nhiễu; giàn S20 có một hàm bình thường bị gắn cờ, số còn lại sát
  ngưỡng, giải thích bằng việc giàn không đóng góp dữ liệu huấn luyện và sai số tham số nhận dạng (tr. 8).
- (a) Ca I: dạng không phát hiện được hư hỏng 7 %, nhạy hơn với 14 %, gắn cờ được 24 %; âm tính giả ở 7 % vì biến động quần
  thể tương đương hoặc lớn hơn biến động do hư hỏng (tr. 8–9).
- (a) Ca I kết luận: dạng dùng được như biểu diễn chung của quần thể đồng nhất mạnh; với dữ liệu huấn luyện từ một tập con,
  dạng mô hình hóa được thông tin thiếu của nhóm giữ lại (tr. 9).
- (a) Ca II: một quá trình Gauss đơn biểu diễn kém không gian đặc trưng của quần thể, sẽ che biến động do hư hỏng và gắn cờ
  sai các lần cắt giảm (tr. 15, Hình 9b). Với OMGP, mọi đường cong được gán nhãn "tốt" nằm trong ngưỡng (cả lý tưởng và cắt
  giảm 50 %), phần lớn đường cong "xấu" bị gắn cờ; nhóm "mơ hồ" cho kết quả kém rõ ràng (tr. 15, Hình 11–12).

## 5. Giới hạn

**(b) Tác giả tự nêu:**
- Trường hợp đồng nhất mạnh là quần thể lý tưởng; trang trại điện gió khó đáp ứng (tr. 2).
- Thành công của cách tiếp cận phụ thuộc mạnh vào p(Θ); khi p(Θ) phân tán hoặc đa đỉnh, biến động quần thể che thay đổi do
  hư hỏng (âm tính giả), hành vi ít gặp không có trong tập huấn luyện gây dương tính giả; khi đó SHM thông thường không áp
  dụng được cho dữ liệu quần thể (tr. 9–10).
- Để lộ hư hỏng mức thấp cần định nghĩa khác của dạng (không gian đặc trưng khác, mô hình khác, hoặc cả hai) (tr. 9).
- Huấn luyện trên mẫu con 2000 quan sát; cách xử lý dữ liệu lớn chặt chẽ hơn (GP thưa) để cho nghiên cứu sau (tr. 7).
- Ca II không có trạng thái cụ thể của từng tuabin; nhãn phần nào chủ quan (tr. 11); nhóm mơ hồ chưa kết luận được (tr. 15).
- Việc thêm trạng thái bình thường mới vào dạng chỉ thích hợp khi trạng thái đó là trạng thái bình thường được chấp nhận
  (tr. 17).
- Hai dạng trong bài chỉ là hai cách; cần khảo sát công nghệ khác (mô hình mật độ, học chuyển giao, học đa nhiệm), và mô hình
  vẫn phải xấp xỉ phương sai của quần thể (tr. 17–18).

**[NCS] nhận định:**
- Đối tượng là hệ cơ học 8 bậc tự do và tuabin gió; không có nhà công nghiệp khung thép, mối nối bu lông hay cầu trục. Hư
  hỏng ở Ca I là giảm độ cứng mô phỏng, chưa có hư hỏng thực ở Ca II. Việc áp sang nhà xưởng là diễn giải.
- Ca I chỉ có một thành viên thực (giàn), 19 thành viên còn lại sinh từ mô hình có tham số nhận dạng từ chính giàn đó, nên
  "quần thể" có độ đồng nhất do thiết kế mô phỏng.
- Bài không báo cáo tỉ lệ phát hiện hay báo động giả dạng số tổng hợp; kết quả trình bày bằng biểu đồ kiểm soát và mô tả.
- Nhãn ở Ca II (tốt / xấu / mơ hồ) do quan sát trực quan đường cong, không phải kết quả kiểm tra hiện trường; ai gán, khi
  nào, theo phiên bản tiêu chí nào không được ghi.
- Can thiệp của người vận hành và bảo trì được xử lý bằng cách hấp thụ vào mô hình bình thường (tr. 11), chứ không bằng cách
  ghi lại sự kiện và tách dữ liệu trước/sau; quyết định "trạng thái nào là bình thường được chấp nhận" (tr. 17) không gắn
  với người có thẩm quyền.
- Bài là của nhóm Sheffield, cùng nhóm với Worden 2007 `MCNRW6F5`, Bull 2022 `87NKU5IS`, Hughes 2022 `Z9RD5DMZ`, Cross 2011
  `KPWFC4PI`; khi đếm căn cứ độc lập theo quy ước nhóm tác giả thì tính chung một nhóm.

## 6. Đoạn dùng được cho tiểu luận

| Luận điểm | Trang | Loại |
|---|---|---|
| Với một công trình riêng lẻ, dữ liệu đo chỉ phủ một phần điều kiện vận hành, môi trường và hư hỏng; tập nhãn có thể không có hoặc không đủ | 1 | Trực tiếp |
| PBSHM chuyển thông tin giữa các công trình tương tự để suy luận cho công trình thiếu dữ liệu | 1 | Trực tiếp |
| Quần thể đồng nhất: thành viên tương đương kết cấu, tham số là các lần rút từ một phân bố cơ sở | 2 | Trực tiếp |
| Dạng quần thể = bản chất + biến động kỳ vọng, học từ dữ liệu trạng thái bình thường; mô hình phải được kiểm định trong quần thể và không gian đặc trưng đã chọn | 3 | Trực tiếp |
| Thiết kế chia theo thành viên: huấn luyện trên S1–S10, kiểm tra trên S11–S20 chưa thấy | 7 | Trực tiếp (căn cứ phương pháp cho chia theo đơn vị suy luận, 3.4/5.6A) |
| Biến động quần thể có thể che hư hỏng mức thấp (7 % không phát hiện) | 8–10 | Trực tiếp |
| Thay đổi do người vận hành can thiệp hoặc bảo trì không chỉ ra hư hỏng, phải được mô hình bình thường nắm bắt để tránh dương tính giả | 11 | Trực tiếp (3.2, EOV) |
| Không có trạng thái cụ thể của từng tuabin; nhãn theo phán đoán kỹ thuật, phần nào chủ quan; kỹ sư không thể xem hết dữ liệu | 11, 15 | Trực tiếp (UV-05, 3.6) |
| Một nhà xưởng có nhiều khung, liên kết lặp lại có thể xem như một quần thể gần đồng nhất để chuyển mô hình trạng thái bình thường | 2–3 | Diễn giải [NCS] |
| Việc đưa một trạng thái vào "bình thường được chấp nhận" là một quyết định cần người có thẩm quyền và cần được ghi | 17 | Diễn giải [NCS] (K3) |
| Phạm vi áp dụng của một mô hình trạng thái bình thường gắn với quần thể và không gian đặc trưng; đây là tiền lệ cho việc khai báo phạm vi hiệu lực | 2–3 | Gián tiếp (K1) |

## 7. Tác động tới K1/K2/K3

- **K1: mở rộng.** Bài xác định nơi mô hình được phép dùng bằng điều kiện thành viên (tương đương kết cấu, phân bố tham số;
  tr. 2) và yêu cầu kiểm định trong quần thể và không gian đặc trưng đã chọn (tr. 3); thiết kế giữ lại thành viên (tr. 7) là
  một cách chia dữ liệu theo đơn vị suy luận. [NCS] Đây là các thành phần của phạm vi hiệu lực được nêu ở mức phương pháp,
  nhưng không được ghi kèm từng kết quả phát hiện; điều này cùng chiều với K1.
- K2: không liên quan trực tiếp. [NCS] Bài phân biệt thành viên đóng góp và không đóng góp dữ liệu, nhưng không bàn ánh xạ
  cảm biến – cấu kiện hay tính liên tục định danh theo thời gian.
- K3: không liên quan trực tiếp. [NCS] Nhãn do phán đoán kỹ thuật (tr. 11, 15) và quyết định chấp nhận trạng thái bình
  thường mới (tr. 17) không được ghi như bản ghi trách nhiệm.

## 8. Kiểm phản chứng

**UV-05 (thiếu nhãn hư hỏng ở hiện trường): giải quyết một phần.**
- Điều bài đã làm: nêu rõ vấn đề thiếu nhãn và thiếu dữ liệu điều kiện hư hỏng ở từng công trình (tr. 1); đề xuất cách giảm
  nhu cầu nhãn bằng mô hình trạng thái bình thường học từ một phần quần thể và chuyển sang các thành viên còn lại (tr. 3, 9,
  17); ghi nhận ở hiện trường không có trạng thái cụ thể của từng tuabin, nhãn theo phán đoán kỹ thuật và tiêu chí chuyên gia,
  phần nào chủ quan, có nhóm mơ hồ, và kỹ sư không thể xem hết dữ liệu (tr. 11, 15).
- Điều bài không làm: nhãn không đến từ kiểm tra thực tại công trình mà từ quan sát trực quan đường cong; không có cơ chế lấy
  thêm nhãn bằng kiểm tra; không mô hình hóa độ bất định của nhãn ngoài việc tách nhóm mơ hồ; không ghi ai gán nhãn, khi nào,
  theo tiêu chí phiên bản nào. Phần nhận dạng hư hỏng (ngoài phát hiện điểm mới) vẫn cần nhãn và không được giải quyết.
- **Phát biểu thu hẹp đề xuất:** việc thiếu nhãn ở hiện trường đã được nêu và được giảm nhẹ bằng hai hướng: chuyển mô hình
  trạng thái bình thường giữa các thành viên của một quần thể đồng nhất ([57], tr. 1, 3) và lấy nhãn bằng kiểm tra có chọn
  lọc (Bull 2022, Hughes 2022). Trong cả hai, nhãn được coi như dữ liệu đầu vào (phán đoán kỹ thuật trên đường cong, hoặc
  nhãn định sẵn với giả định kiểm tra hoàn hảo). Phần chưa thấy giữ nguyên như bản thu hẹp hiện có: nhãn sinh từ kiểm tra
  thực ở công trình đang vận hành, mang độ bất định của kiểm tra, được ghi như một bản ghi gắn với phép đo đã kích hoạt kiểm
  tra, với cấu kiện và với người gán. [NCS] Mục "[57] chưa kiểm" trong UV-05 có thể chuyển thành "đã kiểm".

**UV-06 (lần lắp ráp hoặc can thiệp bảo trì là ranh giới phạm vi hiệu lực): không giải quyết.**
- Bài không bàn mối nối bu lông, lần lắp ráp hay siết lại. Điểm gần nhất: dữ liệu có thể đổi đáng kể khi người vận hành can
  thiệp hoặc trong quy trình bảo trì, và tác giả xử lý bằng cách để mô hình trạng thái bình thường **hấp thụ** các thay đổi đó
  (tr. 11), hoặc cập nhật dạng bằng một thành phần bình thường mới khi trạng thái đó được chấp nhận (tr. 15, 17). Đây là
  hướng ngược với việc coi can thiệp là ranh giới phạm vi hiệu lực.
- Điều kiện thành viên quần thể (tương đương kết cấu, phân bố tham số, điều kiện biên; tr. 2) cho một tiêu chí về khi nào mô
  hình còn chuyển được, nhưng xác định ở mức quần thể và một lần, không theo sự kiện can thiệp trên từng thành viên theo thời
  gian. [NCS] Tác giả cũng ghi nhận điều kiện biên và thực hành vận hành làm quần thể kém đồng nhất (tr. 2); một lần tháo –
  lắp liên kết có thể làm một cấu kiện rời khỏi phân bố tham số đã học, điều này củng cố UV-06 nhưng không tính là căn cứ.
- **Phát biểu thu hẹp:** không cần thu hẹp do [57]. Có thể bổ sung một câu định vị: PBSHM xác định phạm vi chuyển giao
  của mô hình bằng điều kiện thành viên quần thể ([57], tr. 2–3) và xử lý biến động do bảo trì bằng cách đưa vào mô hình
  bình thường (tr. 11); chưa coi lần can thiệp là ranh giới được ghi của phạm vi hiệu lực. Phần III (Gardner 2021, thích nghi
  miền) vẫn **chưa kiểm**.

## 9. Vị trí sử dụng

- 3.6: thiếu dữ liệu điều kiện hư hỏng và nhãn ở từng công trình; chuyển tri thức trạng thái bình thường giữa các công trình
  tương tự; chia dữ liệu theo thành viên giữ lại (tr. 1, 3, 7, 11).
- 3.2: can thiệp vận hành, bảo trì gây biến động không phải hư hỏng, nguồn dương tính giả (tr. 11).
- 5.6A: căn cứ cho cách học chỉ với dữ liệu trạng thái bình thường và phát hiện điểm mới bằng ngưỡng (tr. 3, 8); nội dung
  5.6A trước đây lấy [57] từ tóm tắt, nay đối chiếu được với toàn văn.
