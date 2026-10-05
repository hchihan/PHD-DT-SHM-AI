# AESHHWVZ — Kamariotis, Chatzi & Straub (2023) [28]

Kamariotis A, Chatzi E, Straub D. A framework for quantifying the value of vibration-based structural health monitoring.
*Mechanical Systems and Signal Processing* 184: 109708. DOI 10.1016/j.ymssp.2022.109708 (thông tin thư mục theo mục Zotero
`AESHHWVZ`; phiên này không kiểm lại DOI).

**Bản đã đọc:** bản tiền in arXiv **2202.01859v2** ([stat.AP], 24/08/2022), chân trang 1 ghi "Preprint submitted to
Mechanical Systems and Signal Processing, August 25, 2022" (tr. 1); tệp `pdf/AESHHWVZ_Kamariotis2023_arXiv-v2.pdf`, 25 tr.
(tr. 1–22 thân bài, tr. 23–25 tài liệu tham khảo). **Mọi số trang dưới đây là số trang của bản tiền in**, không phải trang
bản in MSSP 184 (bản in đánh số theo mã bài 109708); chưa đối chiếu bản in, cần đối chiếu trước khi dẫn trang in.
Đọc toàn văn ngày 01/10/2026, phiên T2-3.

Ký hiệu: (a) điều tác giả nói; (b) giới hạn tác giả tự nêu; **[NCS]** nhận định của NCS.

| Cột | Nội dung |
|---|---|
| Citekey / Số cũ | AESHHWVZ / [28] |
| Tier / Cụm | Tier 2 / Giá trị quyết định |
| Luận điểm | Khó định lượng lợi ích của SHM cho hỗ trợ quyết định là một nút thắt cản trở áp dụng SHM trên công trình thật; bài đề xuất khung phân tích quyết định Bayes định lượng "giá trị của SHM" (VoSHM) bằng hiệu số chi phí vòng đời kỳ vọng giữa phương án chỉ kiểm tra bằng mắt định kỳ và phương án SHM dao động liên tục kèm kiểm tra bổ sung (tr. 1, 5). |
| Bằng chứng | Chỉ có ví dụ số: mô hình phần tử hữu hạn chuẩn của cầu hai nhịp, hư hỏng là giảm độ cứng gối giữa mô phỏng xói, biến đổi nhiệt độ, 12 gia tốc kế, dữ liệu dạng riêng nhận dạng bằng SSI từ tín hiệu mô phỏng; bốn ca nghiên cứu, mỗi ca 1000 mẫu Monte Carlo (tr. 14–21). Không có dữ liệu công trình thật. |
| Giới hạn | Xem mục 5. |
| Tác động K1/K2/K3 | K1: mở rộng (giá trị của thông tin phụ thuộc mô hình độ bất định của phép đo và của kiểm tra, và việc bù nhiệt học từ giai đoạn đầu được giả định là chưa hư hỏng). K2: không liên quan trực tiếp. K3: không liên quan trực tiếp (quyết định được mô phỏng bằng luật ngưỡng, không được ghi nhận). Xem mục 6. |
| Vị trí sử dụng | 3.2 (rào cản: khó định lượng lợi ích, khó thuyết phục chủ công trình; nhiệt độ lấn át hư hỏng); 3.6 (SHM đi cùng kiểm tra, không thay kiểm tra; dữ liệu trạng thái hư hỏng hiếm); 5.7 (so với thực hành hiện hành làm đường cơ sở, tương ứng ý B0). Không dùng phần tối ưu chi phí vòng đời (mục 7). |
| Mức đã đọc | Toàn văn, bản tiền in arXiv v2 (01/10/2026, phiên T2-3) |

## 1. Câu hỏi và đối tượng

- (a) Bối cảnh: trong vận hành – bảo trì hiện nay, kiểm tra bằng mắt vẫn là nguồn thông tin chính, nhiều khi là duy nhất, về
  tình trạng công trình (tr. 1). Rào cản áp dụng SHM: đặc trưng nhạy hư hỏng rất nhạy với điều kiện môi trường – vận hành;
  dữ liệu ở trạng thái hư hỏng hiếm khi có nên không rõ cách dùng dữ liệu quan trắc cho ra quyết định theo kiểu học có giám
  sát; khó thuyết phục chủ sở hữu và đơn vị vận hành về lợi ích kinh tế (tr. 1–2).
- (a) Ba điểm khác với các nghiên cứu trước theo tác giả: mô hình thực tế của hệ SHM dao động (dữ liệu dạng riêng nhận dạng
  liên tục bằng phân tích dạng dao động vận hành, OMA); có ảnh hưởng của biến đổi môi trường; xét toàn chuỗi quyết định kiểm
  tra và bảo trì suốt vòng đời thay vì từng quyết định riêng (tr. 2).
- (a) Phân loại ca sử dụng SHM theo thang thời gian ra quyết định (Hình 1, tr. 3): chẩn đoán thời gian thực hoặc gần thực
  (giây – giờ), quá trình suy giảm nhanh (ngày – tháng), quá trình suy giảm chậm (năm – vòng đời) (tr. 2–3). Ở thang thời gian
  thực, khó đạt các nhiệm vụ cao hơn phát hiện (định vị, định lượng hư hỏng) theo cách hoàn toàn dựa trên dữ liệu mà không có
  mô hình chuyên dụng (tr. 3).

## 2. Khung giá trị thông tin (VoI) và VoSHM

**Phân tích tiên nghiệm và tiền hậu nghiệm.**
- (a) Tiện ích được đồng nhất với chi phí vòng đời tổng âm; chi phí xây dựng và tháo dỡ không đổi khi có SHM nên bỏ qua;
  chi phí tổng = chi phí kiểm tra + chi phí bảo trì + rủi ro (chi phí kỳ vọng của sự cố) (tr. 4, phương trình 1).
- (a) Phân tích quyết định tiên nghiệm: chọn tập hành động cực tiểu chi phí kỳ vọng theo phân phối tiên nghiệm (tr. 4, pt. 2).
  Phân tích hậu nghiệm: khi đã có dữ liệu z, chọn hành động tối ưu có điều kiện theo z (tr. 4, pt. 3).
- (a) Vì muốn đánh giá **trước khi lắp** hệ SHM, dữ liệu z chưa có, nên phải dùng mô hình của hệ SHM để dự báo xác suất dữ liệu
  quan trắc; phân tích dựa trên dữ liệu mô phỏng, gọi là phân tích **tiền hậu nghiệm** (preposterior) (tr. 4, pt. 4). VoI là
  hiệu số chi phí kỳ vọng giữa phân tích tiên nghiệm và tiền hậu nghiệm (tr. 5, pt. 5).
- (a) VoI theo pt. 5 ít hữu ích cho chủ công trình vì lấy mốc so sánh là không có kiểm tra lẫn quan trắc, điều hiếm xảy ra;
  thực tế thường kiểm tra bằng mắt gián đoạn, có thêm NDT khi cần. Vì vậy dùng **VoSHM**: hiệu số giữa hai phân tích tiền hậu
  nghiệm, (i) chỉ có dữ liệu kiểm tra và (ii) có dữ liệu SHM liên tục cộng thêm kiểm tra (tr. 5, pt. 6).
- (a) VoSHM giả định SHM đi cùng một chính sách kiểm tra (được kết quả SHM định hướng), vì trong thực tế người vận hành sẽ không
  đặt đủ tin cậy vào một hệ quan trắc hoàn toàn tự động, không giám sát để thay hẳn kiểm tra (tr. 5).

**"Thông tin" của SHM là gì.**
- (a) Bất kỳ thông tin nào trích từ hệ SHM dùng được làm đặc trưng nhạy hư hỏng đều có thể là một mẫu z (tr. 5). Trong bài,
  z_SHM là vectơ các trị riêng thấp nhận dạng bằng OMA (thuật toán SSI) từ gia tốc đo dưới kích thích môi trường chưa biết,
  kèm nhiệt độ đo (tr. 8, 11, pt. 22).
- (a) Dữ liệu kiểm tra bằng mắt: z_insp = trạng thái suy giảm thật + sai số Gauss trung bình 0, hệ số biến thiên cv_insp
  phản ánh chất lượng kiểm tra; ví dụ số dùng cv_insp = 0,15 (tr. 11, pt. 24–25).

**Từ dữ liệu dao động đến cập nhật Bayes.**
- (a) Bài **không dùng bộ phân loại hư hỏng**. Hư hỏng được nhận dạng theo hướng dựa trên mô hình: một mô hình phần tử hữu
  hạn tuyến tính G (hoặc mô hình thay thế) dự báo trị riêng theo trạng thái suy giảm X_k và mô đun đàn hồi hiệu dụng; hàm hợp
  lý giả định sai lệch giữa trị riêng nhận dạng và trị riêng dự báo là Gauss, độ lệch chuẩn tỉ lệ với trị riêng (tr. 11,
  pt. 22–23; hệ số c_λm = 0,02, tr. 9).
- (a) Bộ lọc Bayes (bộ lọc hạt trực tuyến, lấy mẫu lại theo hỗn hợp Gauss khi cỡ mẫu hiệu dụng xuống dưới ngưỡng) ước lượng
  đồng thời trạng thái suy giảm và tham số A, B của mô hình suy giảm, dùng dữ liệu dạng riêng liên tục và dữ liệu kiểm tra gián
  đoạn (tr. 1, 10–11, 13).
- (a) Từ phân phối hậu nghiệm của trạng thái suy giảm tính lại xác suất phá hủy tích lũy và suất phá hủy (hazard) (tr. 11–12,
  pt. 26–29; tr. 13 bước 2). Khả năng chịu lực R(X_k) được mô hình hóa tất định, giả định bất định chính đến từ suy giảm và tải
  (tr. 11–12).
- (a) Bù biến đổi môi trường: mô đun đàn hồi là hàm phi tuyến của nhiệt độ (pt. 13–14, theo dạng đã dùng cho dữ liệu cầu
  thật); tham số của hàm được học bằng Bayes từ dữ liệu dạng riêng ở nhiều nhiệt độ trong vài tháng đầu vận hành, với giả định
  công trình còn lành ở đầu tuổi thọ (thường cần nửa năm đến một năm để có nhiệt độ hai đầu thang) (tr. 8–9, pt. 16). Tác giả
  đã chỉ ra ở công trình trước [40] rằng không xét đúng biến đổi môi trường có thể gây hại cho các quyết định bảo trì do SHM
  kích hoạt (tr. 8).

**Tập quyết định và hành động.**
- (a) Hành động gồm kiểm tra, sửa chữa hoặc bảo trì tại các thời điểm khác nhau (tr. 4). Chính sách tại thời điểm t trả lời
  hai câu hỏi: "Kiểm tra kết cấu?" và "Sửa chữa kết cấu?", dựa trên mọi thông tin trạng thái đến thời điểm đó (dữ liệu kiểm
  tra, quan trắc và hành động đã làm) (tr. 5). Trong ví dụ số, hai quyết định có/không được đưa ra mỗi năm một lần và tại thời
  điểm có sự kiện cực đoan được quan sát (tr. 16).
- (a) Bài toán quyết định tuần tự được thu gọn bằng ba luật kinh nghiệm (heuristic) "đơn giản, trực quan, dễ hiểu với kỹ sư và
  người vận hành": ngưỡng độ tin cậy để kiểm tra p_th^I; kiểm tra định kỳ cố định ΔtI; ngưỡng độ tin cậy để sửa chữa p_th^R
  (tr. 6). Có thể thay việc tối ưu tham số luật bằng lựa chọn theo đánh giá chuyên gia, sát với thực hành hơn (tr. 6).
- (a) Sau sửa chữa, kết cấu được giả định trở về trạng thái chưa hư hỏng và bắt đầu suy giảm lại (tr. 13, bước 3). Sau sự kiện
  cực đoan được quan sát, một lần kiểm tra được thực hiện (tr. 13, bước 5).
- Ca 3 thêm quyết định đóng cầu một tuần chờ kiểm tra sau sự kiện cực đoan (tr. 21).

## 3. Ca nghiên cứu số

| Mục | Nội dung (a) | Trang |
|---|---|---|
| Kết cấu | Mô hình chuẩn số của cầu hai nhịp (L1 = 12 m, L2 = 13 m, h = 0,6 m, w = 0,1 m; 200×6 phần tử ứng suất phẳng), gối đàn hồi dạng lò xo Kx = 10^8 N/m, Ky = 10^7 N/m; vật liệu đàn hồi tuyến tính, E0 = 29,11 GPa ở 20 °C, đại diện bê tông cốt thép | 14 (Hình 4) |
| Mô hình hư hỏng | Giảm độ cứng phương y của lò xo gối giữa K_y^(2)(t) = K_y,0^(2) / (1 + X(t)), mô phỏng xói; X(t) là chồng chất suy giảm dần (phương trình tốc độ dạng lũy thừa theo thời gian, nhiễu Gauss) và suy giảm do va đập (quá trình Poisson phức hợp); tuổi thọ T = 50 năm | 9–10, 14 (pt. 17, 30) |
| Phân phối tiên nghiệm | Bảng 1 (Q, H, U, Y, τ của mô hình nhiệt; A, B, ω, D, N(t) của mô hình suy giảm; ví dụ N(t) Poisson trung bình 0,04·t) | 15 |
| Cảm biến | 12 cảm biến gia tốc phương đứng tại các nút định sẵn, cảm biến nhiệt độ môi trường, quan trắc liên tục từ đầu vận hành; kích thích ồn trắng Gauss phân bố | 15 |
| Sinh dữ liệu SHM | Phân tích động theo thời gian cho X_k, T_k; cộng nhiễu ồn trắng 5 % RMS (sai số đo); SSI nhận dạng 3–5 trị riêng thấp | 15 (Hình 5) |
| Học mô hình nhiệt | Nt = 50 bộ trị riêng ở các nhiệt độ khác nhau trong giai đoạn đầu giả định chưa hư hỏng; mô hình "thật" được nắm bắt tốt, khoảng tin cậy 95 % hậu nghiệm rất hẹp | 15–16 (Hình 6) |
| "Tội nghịch đảo" | Mô hình G dùng để cập nhật trùng với mô hình sinh dữ liệu (inverse crime); tác giả coi đây là đặc điểm có sẵn của phân tích tiền hậu nghiệm | 15 |
| Chi phí | Sự cố 5·10^7 €; một lần kiểm tra 2·10^4 €; một lần sửa 6·10^5 €; chiết khấu 2 %/năm | 16 |
| Tải và độ tin cậy | Tải lớn nhất mỗi khoảng theo phân phối Gumbel, chọn sao cho xác suất phá hủy ban đầu 10^-6; R(X_k) lấy từ phân tích tĩnh trên lưới giá trị X_k | 17 |
| Mô hình thay thế | Hồi quy sườn đa thức hai chiều (X, E(T)) cho từng tần số riêng | 17 (Hình 7) |

**Kết quả bốn ca (nMCS = 1000):**

| Ca | Thiết lập (a) | VoSHM (a) | Trang |
|---|---|---|---|
| 1. Suy giảm dần + va đập do sự kiện **được quan sát** | Không SHM: w1* = [p_th^I = 5·10^-4, p_th^R = 10^-3, ΔtI = 5 năm]; có SHM: cùng ngưỡng, bỏ kiểm tra định kỳ (ΔtI = ∞); kiểm tra sau sự kiện ở cả hai phương án | 1,11·10^5 € (một mẫu: 1,13·10^5 € và 6,02·10^4 €) | 17–19 |
| 2. Va đập do sự kiện **không được quan sát** (ví dụ hỏng gối cầu, xe quá tải) | Không SHM thì không có kiểm tra ngay sau sự kiện; ở một mẫu, không SHM sửa năm 38, có SHM sửa năm 36 | 1,42·10^5 € | 20 |
| 3. Gần thời gian thực sau sự kiện cực đoan | Kiểm tra chỉ làm được sau một tuần; không SHM thì luôn đóng cầu một tuần; có SHM thì chỉ đóng khi suất phá hủy cập nhật vượt p_th^I; chi phí đóng cầu 1,5·10^5 €/ngày | 1,34·10^6 € (lớn hơn một bậc vì chi phí đóng cầu chi phối) | 21 |
| 4. Quản lý theo ngưỡng độ tin cậy do cơ quan quản lý áp | p_th^R = 10^-5 áp đặt, chỉ tối ưu p_th^I* = 7·10^-6 | 7,70·10^4 € | 21 |

- (a) VoSHM ca 1 **chưa trừ** chi phí vòng đời của chính hệ SHM (lắp đặt, bảo trì, sửa chữa); phải so VoSHM với chi phí đó rồi
  mới quyết định có lắp hay không (tr. 19).
- (a) Ngưỡng p_th^I*, p_th^R* dùng ở ca 1–3 tương ứng suất phá hủy cao hơn mức cơ quan quản lý thường chấp nhận (tr. 21).

## 4. Phát hiện chính về khi nào SHM có giá trị

- (a) Với dữ liệu SHM liên tục, nhận thức trạng thái hệ được duy trì mọi lúc; việc bỏ kiểm tra định kỳ đem lại tiết kiệm
  (tr. 18, Hình 8–9).
- (a) SHM có giá trị cao hơn khi suy giảm đột ngột đến từ sự kiện **không được quan sát**: không có SHM thì trạng thái thật bị
  đánh giá thấp nghiêm trọng vì không có kiểm tra ngay sau bước nhảy suy giảm (tr. 20).
- (a) Giá trị lớn nhất ở ca chẩn đoán gần thời gian thực khi SHM giúp tránh đóng cửa không cần thiết (tr. 21).
- (a) Khung dùng được như công cụ hỗ trợ quyết định **tiên nghiệm** cho việc có lắp hệ SHM dao động hay không, với nhiều ca
  sử dụng (tr. 1, 4, 22). Kết quả cho thấy đầu tư vào SHM **có thể** đem lại lợi ích lớn (tr. 22).
- (a) Khung cũng dùng được cho bài toán bố trí cảm biến tối ưu (tr. 22).

## 5. Giới hạn

**(b) Tác giả tự nêu:**
- Khung không xét suy giảm hoặc hỏng của chính hệ SHM, không xét sai số mô hình; vì vậy cho **cận trên** của VoSHM "thật"
  (tr. 22). Khung giả định hệ SHM hoạt động liên tục không gián đoạn và được tin hoàn toàn để thay mọi kiểm tra định kỳ, điều
  "có vẻ không thực tế"; VoSHM thu được là cận trên của lợi ích kinh tế (tr. 19; giả định tin cậy cao, tr. 16).
- Chỉ xét **một** cấu kiện suy giảm, có xu hướng đánh giá thấp VoSHM; có thể mở rộng cho nhiều cấu kiện (tr. 22).
- Dùng cho phương án có SHM cùng ngưỡng đã tối ưu cho phương án chỉ kiểm tra, nên có thể đánh giá thấp VoSHM (tr. 16); mẫu thứ
  hai cho thấy luật w2* thực sự chưa tối ưu cho phương án có SHM (tr. 18).
- Mô hình kết quả kiểm tra bằng mắt (pt. 25) là mô hình giả định, đơn giản hóa; thực tế kết quả kiểm tra không ở dạng ước lượng
  mất độ cứng, cần phân tích chi tiết hơn để quy đổi (tr. 16).
- Giả định độc lập giữa các dạng và giữa các bộ dữ liệu trong hàm hợp lý thường không đúng (tr. 9).
- Mô hình cập nhật trùng mô hình sinh dữ liệu ("tội nghịch đảo"); ở công trình thật, sai số mô hình là không tránh được và sẽ
  ảnh hưởng độ chính xác của VoSHM (tr. 15).
- Khả năng chịu lực tất định là lựa chọn đơn giản hóa để chi phí tính toán chấp nhận được (tr. 12).
- Khung cần định nghĩa tiên nghiệm các kịch bản hư hỏng, mô hình suy giảm ngẫu nhiên và mô hình hệ SHM riêng cho từng ca (tr. 22);
  khó khăn chính khi mở rộng là cần mô hình chi tiết hơn, thường khó biện minh trong dự án thực (tr. 22).

**[NCS] nhận định:**
- Toàn bộ bằng chứng là mô phỏng trên một mô hình cầu bê tông với hư hỏng xói ở gối; không có công trình thật, không có nhà
  khung thép, không có mối nối bu lông. Áp kết luận sang nhà xưởng là diễn giải.
- Biến đổi vận hành chỉ được mô hình qua nhiệt độ; kích thích là ồn trắng phân bố. Rung vận hành có nguồn rõ (cầu trục, máy móc)
  như ở nhà xưởng không được xét (liên quan UV-08).
- Bù nhiệt dựa trên giả định giai đoạn đầu chưa hư hỏng (tr. 8, 15). Với nhà xưởng đã vận hành nhiều năm, giả định này không
  có sẵn; đây là một điều kiện của phạm vi hiệu lực mà đầu ra phải mang theo.
- Quyết định được mô phỏng bằng luật ngưỡng trong vòng Monte Carlo; không có người ra quyết định, không có bản ghi quyết định,
  không có trạng thái xử lý.
- Ở tr. 14 (bản tiền in), công thức chi phí sửa C_R^(i) ghi đơn giá kiểm tra c̃_I thay cho đơn giá sửa; có thể là lỗi in của bản
  tiền in, chưa đối chiếu bản in. Không ảnh hưởng nội dung dùng cho tiểu luận.

## 6. Tác động tới K1/K2/K3

- **K1: mở rộng.** Giá trị của thông tin SHM được tính qua hàm hợp lý, tức là qua mô hình độ bất định của phép đo (c_λm, tr. 9,
  11) và của kiểm tra (cv_insp, tr. 11, 16); không bù đúng biến đổi môi trường thì quyết định bảo trì bị ảnh hưởng xấu (tr. 8).
  [NCS] Điều này ủng hộ việc bằng chứng phải mang độ bất định và điều kiện áp dụng (gồm giả định giai đoạn tham chiếu chưa hư
  hỏng dùng để học mô hình nhiệt); bài không bàn việc ghi nhận các thông tin đó cùng đầu ra.
- **K2: không liên quan trực tiếp.** Cảm biến đặt tại nút phần tử hữu hạn định sẵn, không đổi suốt 50 năm (tr. 15); không có
  ánh xạ cảm biến – cấu kiện theo thời gian.
- **K3: không liên quan trực tiếp.** Chính sách quyết định là luật ngưỡng minh bạch, "dễ hiểu với kỹ sư và người vận hành"
  (tr. 6), và SHM được giả định đi cùng kiểm tra vì người vận hành không tin hệ tự động hoàn toàn (tr. 5). [NCS] Hai ý này cùng
  chiều với logic bốn mức bằng luật minh bạch ở WP4 và nguyên tắc "AI tạo bằng chứng, con người quyết định", nhưng bài không ghi
  ai quyết định, căn cứ nào, trạng thái hành động ra sao.

## 7. Phần nằm ngoài phạm vi luận án (CLAUDE.md mục 11)

Phần cốt lõi của bài là **tối ưu chi phí vòng đời** (pt. 1–9, tr. 4–7; tối ưu ngưỡng kiểm tra – sửa chữa, tr. 6, 16–17, 21),
**dự báo suy giảm và cập nhật độ tin cậy** theo thời gian (tr. 9–12), và việc học tham số suy giảm A, B mà tác giả nói là "thiết
yếu cho các nhiệm vụ bảo trì dự đoán" (tr. 18); thêm bố trí cảm biến tối ưu (tr. 22). Các phần này thuộc bảo trì dự đoán / tuổi
thọ / tối ưu chi phí, **không** đưa vào tiểu luận như nội dung luận án. Chỉ dùng bài ở mức: (i) nhận định về rào cản (khó định
lượng lợi ích, dữ liệu hư hỏng hiếm, ảnh hưởng EOV); (ii) cách so với thực hành hiện hành làm mốc; (iii) SHM đi cùng kiểm tra;
(iv) kiểm tra có độ bất định. Nếu cần nói về giá trị kinh tế, chỉ nêu như hướng mở rộng ở mục giới hạn (nhãn tạm 5.8).

## 8. Đoạn dùng được cho tiểu luận

| # | Ý (a) | Trang | Mục dùng | Mức trực tiếp |
|---|---|---|---|---|
| 1 | Khó định lượng lợi ích của SHM cho hỗ trợ quyết định là một nút thắt của việc áp dụng rộng rãi trên công trình thật; khó thuyết phục chủ sở hữu về lợi ích kinh tế | 1, 2 | 3.2 (L2.1) | Trực tiếp; đối tượng là công trình hạ tầng nói chung |
| 2 | Kiểm tra bằng mắt vẫn là nguồn thông tin chính, nhiều khi duy nhất, về tình trạng công trình trong vận hành – bảo trì | 1 | 1.1 hoặc 3.2 | Trực tiếp, nhận định chung |
| 3 | Dữ liệu ở trạng thái hư hỏng hiếm khi có, nên không rõ cách dùng dữ liệu quan trắc cho ra quyết định theo kiểu học có giám sát | 1–2 | 3.6, 5.6A (L2.3) | Trực tiếp; căn cứ cùng chiều cho UV-05 |
| 4 | Biến đổi dạng riêng do nhiệt độ thường lớn hơn biến đổi do hư hỏng đáng kể; không xét đúng biến đổi môi trường có hại cho quyết định bảo trì do SHM kích hoạt | 7–8 | 3.2 (L2.2), 5.6A (bù EOV) | Trực tiếp; đối tượng là kết cấu xây dựng (cầu) |
| 5 | SHM được giả định đi cùng chính sách kiểm tra vì người vận hành không tin hệ tự động hoàn toàn để thay kiểm tra; giả định thay hết kiểm tra định kỳ là "có vẻ không thực tế" | 5, 19 | 3.6, 5.6A (nguyên tắc "AI tạo bằng chứng, con người quyết định") | Trực tiếp |
| 6 | Mốc so sánh có ý nghĩa với chủ công trình là thực hành hiện hành (kiểm tra bằng mắt gián đoạn, có NDT khi cần), không phải "không có thông tin" | 5 | 5.7 (lý do chọn B0 = thực hành hiện hành) | Gián tiếp: cùng cách lập luận, khác đại lượng đo |
| 7 | Kết quả kiểm tra bằng mắt được mô hình như phép đo có độ bất định; tác giả tự nêu mô hình này là giả định, đơn giản hóa | 11, 16 | 3.6, 5.5 (trường độ bất định của bản ghi kiểm tra) | Gián tiếp |
| 8 | Bù nhiệt được học từ giai đoạn đầu vận hành với giả định công trình còn lành | 8, 15 | 3.6 (đường cơ sở vận hành), 5.6A | Trực tiếp về phương pháp; [NCS] với nhà xưởng cũ giả định này phải ghi thành điều kiện áp dụng |

## 9. Kiểm phản chứng

- **UV-01 (chuỗi cảnh báo → hành động; phát biểu thu hẹp: bằng chứng có nguồn gốc và phạm vi hiệu lực đi vào chuỗi hành động;
  sự kiện đổi trạng thái của hành động có căn cứ và thẩm quyền): KHÔNG GIẢI QUYẾT.** Bài mô hình hóa quyết định kiểm tra / sửa
  chữa / đóng cầu như hàm của độ tin cậy cập nhật (tr. 5–6, 13, 21), tức là có liên kết **tính toán** từ dữ liệu SHM và kiểm tra
  tới hành động. Nhưng hành động chỉ tồn tại trong mô phỏng Monte Carlo: không có trạng thái xử lý, sự kiện chuyển trạng thái,
  người thực hiện, thẩm quyền hay bản ghi căn cứ (tr. 5–6, 13–14) [NCS: các điểm "không có" suy từ việc bài không nêu]. Phát
  biểu thu hẹp giữ nguyên. Không tính là căn cứ cho UV-01 vì bài không bàn việc ghi nhận.
- **UV-05 (thiếu nhãn hiện trường; phát biểu thu hẹp: nhãn sinh từ kiểm tra thực ở công trình đang vận hành, mang độ bất định
  của kiểm tra, được ghi như bản ghi gắn với phép đo đã kích hoạt kiểm tra và với cấu kiện): MỘT PHẦN (phát biểu gốc); KHÔNG
  GIẢI QUYẾT (phát biểu thu hẹp).**
  - (a) Bài nêu việc dữ liệu trạng thái hư hỏng hiếm khi có, gây khó cho học có giám sát (tr. 1–2) — **căn cứ cùng chiều (TG)**
    cho phát biểu gốc. Nhóm tác giả TUM – ETH, khác nhóm Sheffield – Los Alamos; năm 2023 (bản tiền in 2022), không thuộc nhóm
    2025–2026. [NCS] Có thể tính là căn cứ độc lập bổ sung cho UV-05; CẦN NCS KIỂM vì căn cứ chỉ là một câu ở phần mở đầu.
  - (a) Bài đi đường vòng không cần nhãn: nhận dạng hư hỏng dựa trên mô hình phần tử hữu hạn và cập nhật Bayes (tr. 8–11). Kết
    quả kiểm tra được mô hình như phép đo có độ bất định (cv_insp = 0,15, tr. 11), khác với giả định kiểm tra hoàn hảo của Hughes
    2022. Nhưng mô hình kiểm tra là giả định (tr. 16), kết quả kiểm tra được **lấy mẫu** chứ không đến từ kiểm tra thực, và không
    được ghi như bản ghi gắn phép đo, cấu kiện, người kiểm tra. [NCS] Phát biểu thu hẹp giữ nguyên; có thể bổ sung câu: độ bất
    định của kết quả kiểm tra đã được đưa vào **mô hình tính toán** giá trị thông tin [28], phần chưa thấy là việc **ghi nhận** nó
    như một trường của bản ghi kiểm tra.
- **UV-07 (xác nhận của chuyên gia đối với đầu ra AI chưa được ghi như bản ghi trách nhiệm): KHÔNG GIẢI QUYẾT.** Bài không có
  đầu ra AI/học máy cần xác nhận; kiểm tra bổ sung cho SHM được kích hoạt bằng luật ngưỡng (tr. 6, 13) và kết quả kiểm tra vào bộ
  lọc như một hàm hợp lý (tr. 13, bước 7), không có vai trò, thẩm quyền, thời điểm xác nhận hay bản ghi. (a) Ý người vận hành
  không đặt đủ tin cậy vào hệ quan trắc tự động hoàn toàn (tr. 5) là căn cứ **nhu cầu** cùng chiều cho việc giữ con người trong
  vòng quyết định, không phải căn cứ rằng lần xác nhận chưa được ghi. Phát biểu giữ nguyên; không tính là căn cứ độc lập.

## 10. Vị trí sử dụng

- 3.2: rào cản lợi ích – chi phí (L2.1: khó định lượng lợi ích, khó thuyết phục chủ công trình, tr. 1–2); EOV (L2.2, tr. 7–8).
- 3.6: SHM đi cùng kiểm tra (tr. 5, 19); dữ liệu hư hỏng hiếm (tr. 1–2); kiểm tra có độ bất định (tr. 11, 16); đường cơ sở học từ
  giai đoạn đầu (tr. 8, 15).
- 5.7: lý do lấy thực hành hiện hành làm mốc so sánh (tr. 5), ứng với B0.
- Mục giới hạn (nhãn tạm 5.8): giá trị kinh tế của SHM là hướng mở rộng, không thuộc phạm vi luận án.
