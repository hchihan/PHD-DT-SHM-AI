# CHƯƠNG 5. TỔNG HỢP KHOẢNG TRỐNG VÀ ĐỊNH HƯỚNG NGHIÊN CỨU

<!-- Bản r4 03/10/2026: chương kết, rút gọn. Phần diễn giải chuyển về Chương 3 (thí nghiệm 1:10, công cụ AI, quan trắc hiện trường: 3.5, 3.6) và Chương 4 (mô hình dữ liệu, công cụ, các bước của Mục tiêu 2: 4.6). 5.5 chỉ nêu phương pháp khoa học. -->

Chương này rút ra ba khoảng trống liên kết từ các chương tổng quan, rồi nêu luận đề, mục tiêu, câu hỏi, thiết kế nghiên cứu cùng các cổng kiểm chứng, đóng góp dự kiến, phạm vi và kiến trúc nghiên cứu của luận án. Nội dung chi tiết của phương pháp được trình bày ở Mục 3.4, 3.5 và 4.6.

## 5.1. Tổng hợp bằng chứng từ tài liệu

Các chương 2 đến 4 cho thấy từng mắt xích của chuỗi đều đã có nền nghiên cứu. Ở cấp quản lý tài sản, nhu cầu một dòng thông tin liên tục từ dữ liệu tới quyết định đã được thừa nhận trong chuẩn \[@8PB7EN2E\], \[1\] và trong nghiên cứu \[22\], \[24\], \[28\]. Ở cấp kỹ thuật, liên kết dữ liệu với cấu kiện \[2\], \[4\]–\[6\], chuẩn biểu diễn trạng thái và sự kiện \[35\], \[@63XPSMIR\], \[@K5SGFIGW\], \[@P3ZIHF8G\], nguyên tắc đánh giá theo đơn vị độc lập \[14\], \[15\], \[53\] và các hướng xử lý hiện trường \[@TDRPDWJE\], \[@23TBQTIP\], \[@Z9RD5DMZ\] đều đã có. Phần còn bỏ ngỏ nằm ở điểm nối giữa các thành phần và ở bước đưa chuỗi ra công trình thật. Bảng 5.1 tóm lược phần đã được xác lập, phần còn bỏ ngỏ và khoảng trống liên quan.

<span id="TLTQ_Bang_5_1" class="anchor"></span>Bảng 5.1. Tổng hợp các nghiên cứu đã rà soát và khoảng trống liên quan

| Nhóm nội dung | Tài liệu tiêu biểu | Đã được xác lập | Phần còn bỏ ngỏ | Khoảng trống |
|:---|:---|:---|:---|:--:|
| Dữ liệu dao động, học máy | \[13\], \[47\], \[48\], \[50\] | Phân biệt trạng thái liên kết trong phòng thí nghiệm | Kế thừa | – |
| Đơn vị độc lập, rò rỉ, đánh giá theo nhóm | \[14\], \[15\], \[20\], \[52\]–\[54\], \[59\] | Nguyên tắc đánh giá | Mức chênh lệch cho khung thép liên kết bu lông | KT1 |
| Hiệu lực sau lắp ráp, can thiệp | \[18\], \[19\], \[56\], \[@2ZJSENQU\] | Kết quả phụ thuộc lần lắp ráp | Điều kiện đã đánh giá thành trường bắt buộc, kiểm tại lần dùng | KT1 |
| Định danh, liên kết cảm biến – BIM | \[2\], \[4\]–\[6\], \[33\] | Liên kết dữ liệu với cấu kiện | Kế thừa; khoảng hiệu lực của ánh xạ là ràng buộc C3 | – |
| Chuẩn trạng thái, phê duyệt, lịch sử | \[35\], \[@63XPSMIR\], \[@K5SGFIGW\], \[@P3ZIHF8G\], \[44\] | Biểu diễn hành động, trạng thái, sự kiện | Sự kiện đổi trạng thái trỏ về bằng chứng có phạm vi | KT2 |
| Hồ sơ kiểm tra, CMMS, nguồn gốc | \[16\], \[34\], \[36\], \[69\], \[78\], \[82\] | Số hóa hồ sơ, điều hướng, từ vựng nguồn gốc | Truy ngược từ hành động về bằng chứng, kiểm tại lần dùng | KT2 |
| Song sinh số trong vận hành | \[3\], \[7\]–\[10\], \[40\], \[42\], \[43\] | Mức tích hợp, tích hợp dữ liệu | Trong các khung đã rà soát, chuỗi dừng ở cảnh báo | KT2 |
| Quan trắc hiện trường, biến đổi vận hành | \[45\], \[@EBB69J4F\], \[@MCNRW6F5\], \[@23TBQTIP\], \[@38FMATHE\], \[75\] | Giới hạn quan trắc; bù biến đổi; khả thi dài hạn | Duy trì chuỗi bằng chứng – kiểm tra – hành động trong vận hành nhà xưởng có cầu trục | KT3 |
| Học từ trạng thái bình thường, nhãn từ kiểm tra | \[@TDRPDWJE\], \[@G98ZWHKW\], \[@Z9RD5DMZ\], \[@87NKU5IS\] | Phát hiện bất thường không cần nhãn hư hỏng | Kiểm chứng trên nhà công nghiệp với số ít cảm biến | KT3 |
| Thực hành quan trắc tại Việt Nam | \[@8S93B6VF\], \[@G7I5JPVC\], \[@UMPDAEG5\] | Quan trắc cầu, lún, sụt lún | Trong tập đã khảo sát: chưa có nhà xưởng khung thép, chưa gắn với hồ sơ kiểm tra | KT3 |

## 5.2. Ba khoảng trống liên kết

Ba khoảng trống dưới đây là ba mặt của cùng một vấn đề ở Mục 1.4. Một kết quả từ dữ liệu dao động chỉ trở thành căn cứ quản lý khi được tổ chức thành bằng chứng có phạm vi hiệu lực, được bảo toàn và kiểm khi sử dụng, và được duy trì trong vận hành. KT1 là hiệu lực của bằng chứng: bằng chứng được tạo kèm điều kiện đã đánh giá. KT2 là truy vết của bằng chứng: điều kiện đó được bảo toàn và kiểm khi bằng chứng được dùng. KT3 là khả thi hiện trường: chuỗi được duy trì trong vận hành thực. Thiếu KT1, chuỗi không có bằng chứng mang điều kiện đã đánh giá để kiểm. Thiếu KT2, điều kiện đó mất khi bằng chứng đi vào hồ sơ. Thiếu KT3, hai lời giải dừng ở phòng thí nghiệm và mô hình dữ liệu. Vì vậy ba khoảng trống thuộc cùng một luận án. Mỗi khoảng trống được trình bày theo trình tự: nghiên cứu gần nhất, phần đã giải quyết, giới hạn và phần còn lại; mọi phát biểu được giới hạn trong tập tài liệu đã rà soát.

### 5.2.1. KT1 – Bằng chứng trạng thái có phạm vi hiệu lực từ dữ liệu dao động

Nghiên cứu gần nhất là các đánh giá theo nhóm cho dữ liệu có nguồn vật lý lặp: Beleites và cộng sự với dữ liệu quang phổ \[14\], Wheat và cộng sự với ổ lăn \[15\], Kapoor và Narayanan về rò rỉ trong khoa học dùng học máy \[53\], và Ramasso và cộng sự với phát xạ âm trên dầm nhôm lắp bu lông \[19\]. Các nghiên cứu này đã xác lập nguyên tắc đơn vị độc lập, đánh giá theo nhóm và kiểm soát rò rỉ. Chia dữ liệu dưới cấp đơn vị độc lập làm hiệu năng lạc quan \[14\], \[15\], \[53\], và độ chính xác giảm mạnh khi kiểm tra trên một lần lắp chưa thấy \[19\]. Sau mỗi lần lắp lại, phần lớn dữ liệu đáp ứng đã thu mất tác dụng cho theo dõi trạng thái \[18\]; trên cầu thép KW51, mô hình huấn luyện trước can thiệp không còn đại diện cho trạng thái bình thường sau can thiệp \[@2ZJSENQU\]. Luận án kế thừa các nguyên tắc này như phương pháp có sẵn.

Giới hạn nằm ở hai vế. Về đánh giá (vế A1), các nghiên cứu đã rà soát cho phân loại trạng thái liên kết bu lông trên khung thép chia tập trong cùng lần lắp ráp hoặc cùng bản ghi \[48\], \[@VVBGM9EN\], nên mức lạc quan với loại kết cấu này chưa được báo cáo. Về khai báo (vế A2), các chuẩn và đề xuất hiện có đã biểu diễn được nhiều phần của bài toán. SOSA/SSN biểu diễn từng quan trắc cùng cảm biến, thủ tục và đối tượng được quan trắc \[@GHAZGWUN\]; PROV-O biểu diễn nguồn gốc của từng thực thể, hoạt động và tác nhân \[69\]. Thẻ mô hình khai báo điều kiện đánh giá và mục đích sử dụng ở mức mô hình \[@82WQNDHU\], còn \[53\] đề xuất bảng thông tin mô hình để khai báo và kiểm các dạng rò rỉ. Phần còn lại là áp dụng có hệ thống các nguyên tắc đánh giá vào bằng chứng trạng thái của khung thép liên kết bu lông, và đưa bối cảnh đánh giá vào phạm vi hiệu lực như trường bắt buộc, được kiểm tại lần sử dụng trong nghiệp vụ kiểm tra – bảo trì. Khoảng trống này cần giải quyết vì hiệu lực sau can thiệp không đoán trước được: có trường hợp mất \[18\], \[@2ZJSENQU\], có trường hợp một lần siết lại vẫn được phân loại đúng \[48\]. Nó ứng với câu hỏi "tin được đến mức nào?".

### 5.2.2. KT2 – Truy vết từ bằng chứng đến hành động có trách nhiệm

Nghiên cứu gần nhất là chuỗi lần kiểm tra – hư hỏng – cấu kiện – nhiệm vụ bảo trì bằng thực thể chuẩn IFC 4.3 của Bellon và cộng sự \[35\]. Cùng nhóm này có lệnh bảo trì mang trạng thái và phê duyệt của IFC4 \[@63XPSMIR\], sự kiện đổi trạng thái của BCF-API 3.0 \[@P3ZIHF8G\], khuôn bước chuyển có bằng chứng và đúng thẩm quyền cho gói thông tin bàn giao của García và cộng sự \[44\], và lược đồ IFC cho hệ theo dõi trạng thái của Theiler và Smarsly \[2\]. Các nguồn này đã giải quyết việc biểu diễn chuỗi kiểm tra – hành động, trạng thái và phê duyệt, lịch sử đổi trạng thái của vấn đề và quan hệ cảm biến – cấu kiện. Giới hạn là chuỗi của \[35\] chỉ nhận hư hỏng phát hiện bằng mắt, và trạng thái bị ghi đè khi có lần bảo trì. Trong các khung song sinh số đã rà soát, chuỗi dừng ở cảnh báo \[3\], \[7\]; xác nhận của chuyên gia thường chỉ được dùng làm nhãn \[@73MBWFVJ\], \[@Z9RD5DMZ\].

Phần còn lại có hai điểm. Bằng chứng có phạm vi hiệu lực chưa đi vào chuỗi kiểm tra – cấu kiện – hành động, và việc dùng bằng chứng chưa được kiểm so với phạm vi đó tại lần sử dụng. Mỗi lần đổi trạng thái của hành động cũng chưa được ghi thành sự kiện có căn cứ, có chủ thể và vai trò người thực hiện, với bước xác minh tách khỏi thời điểm can thiệp. Khoảng trống này khác với tích hợp cảm biến – BIM: tích hợp đã có nhiều tiền lệ, còn truy vết bằng chứng kiểm chứng được thì chưa. Nó cần giải quyết vì thiết kế một hệ theo dõi phải xác định hành động nào được đưa ra và ai có thẩm quyền \[@EBB69J4F\]. Khi xảy ra sự cố sau một lần sửa chữa, đơn vị quản lý cũng cần truy ngược được quyết định về bằng chứng và người phê duyệt. Đây là câu hỏi "ai đã xử lý, dựa vào đâu?", đặt tại đúng thời điểm của từng quyết định.

### 5.2.3. KT3 – Duy trì chuỗi bằng chứng – hành động trong vận hành nhà công nghiệp khung thép

Nghiên cứu gần nhất là quan trắc dài hạn với đường cơ sở phụ thuộc nhiệt độ trên cầu nhịp lớn \[75\], phát hiện bất thường học từ trạng thái bình thường \[@TDRPDWJE\], \[@G98ZWHKW\], bù biến đổi môi trường – vận hành \[@23TBQTIP\] và nhãn từ kiểm tra \[@Z9RD5DMZ\]. Các nghiên cứu này cho thấy cảm biến triển khai được dài hạn và đề xuất cách xử lý dữ liệu khi thiếu nhãn hư hỏng. Giới hạn là chúng được thực hiện trên cầu hoặc kết cấu thu nhỏ. Vấn đề thực của theo dõi trạng thái chỉ lộ ra trên kết cấu thật \[@EBB69J4F\] (tr. 14–15), thành công trên mô hình thu nhỏ chưa bảo đảm hiệu quả ở hiện trường \[45\], và bộ phân loại học trên một kết cấu khó chuyển sang kết cấu khác \[56\], \[57\]. Rung do cầu trục \[@38FMATHE\] và chi phí tiếp cận \[@QMVQCEL5\] là điều kiện riêng của nhà công nghiệp. Trong tập tài liệu trong nước đã khảo sát, quan trắc tập trung vào cầu, lún và sụt lún \[@8S93B6VF\], \[@G7I5JPVC\], \[@UMPDAEG5\].

Phần còn lại là câu hỏi chuỗi bằng chứng – kiểm tra – hành động có được duy trì và truy ngược được trong vận hành nhà xưởng hay không. Cụ thể, dữ liệu có về đủ không, ánh xạ cảm biến – cấu kiện có giữ đúng qua thời gian không, mỗi bằng chứng có truy được về nguồn đo và hồ sơ không, và công sức ghi nhận có chấp nhận được không. KT3 giới hạn ở khả thi của việc duy trì chuỗi. Hiệu năng phát hiện hư hỏng ở hiện trường cần dữ liệu hư hỏng mà phép thử dự kiến không có, nên nằm ngoài KT3. Ở mức này, câu hỏi "cái gì bất thường, ở đâu?" chỉ được trả lời bằng việc chỉ ra khu vực cấu kiện mà bằng chứng đề nghị kiểm tra.

## 5.3. Luận đề và mục tiêu nghiên cứu

Từ ba khoảng trống, luận đề trung tâm của luận án được phát biểu như sau:

> Với nhà công nghiệp khung thép liên kết bu lông, kết quả từ dữ liệu dao động chỉ trở thành căn cứ quản lý khi được tổ chức thành bằng chứng có nguồn gốc, độ bất định và phạm vi hiệu lực. Các thuộc tính đó phải được bảo toàn và kiểm tra khi bằng chứng được sử dụng, đồng thời truy vết được qua cấu kiện, hồ sơ kiểm tra và lịch sử hành động. Kết luận hư hỏng vẫn thuộc về kỹ sư sau kiểm tra.

Mục tiêu tổng quát của luận án là phát triển và kiểm chứng một khung song sinh số dựa trên dữ liệu cho hỗ trợ kiểm tra – bảo trì nhà công nghiệp khung thép liên kết bu lông. Trong luận án, khung song sinh số là một kiến trúc tích hợp dữ liệu từ công trình, bằng chứng trạng thái, cấu kiện BIM, hồ sơ kiểm tra, lịch sử hành động và phản hồi thông tin quản lý. Chuỗi cốt lõi được kiểm chứng đi từ dữ liệu dao động tới bằng chứng trạng thái, cấu kiện BIM, hồ sơ kiểm tra và hỗ trợ hành động. Khung được kiểm chứng theo từng năng lực, không bao gồm điều khiển tự động hay chẩn đoán hư hỏng tự động; quyết định cuối cùng thuộc kỹ sư và người có thẩm quyền. Ba mục tiêu cụ thể ứng một – một với ba khoảng trống và kiểm chứng ba năng lực cốt lõi của khung: tạo bằng chứng, truy vết và duy trì chuỗi trong vận hành.

**Mục tiêu 1 (KT1).** Xác lập quy trình tạo bằng chứng trạng thái liên kết bu lông có phạm vi hiệu lực từ dữ liệu dao động trên mô hình khung thép tỉ lệ 1:10. Quy trình đo mức chênh lệch giữa đánh giá cùng lần chạy và hai mức đánh giá theo đơn vị độc lập với bốn mô hình học máy, rồi ghi điều kiện đã đánh giá và độ bất định cho từng kết quả.

**Mục tiêu 2 (KT2).** Xây dựng và kiểm chứng lớp dữ liệu truy vết bằng chứng – hành động cho kiểm tra – bảo trì kết cấu thép, liên thông với IFC 4.3 theo cách dùng của \[35\] và với BCF 3.0 mà không sửa lược đồ chuẩn, trên BIM của nhà xưởng ở Khánh Hòa.

**Mục tiêu 3 (KT3).** Triển khai và kiểm chứng khả năng duy trì chuỗi bằng chứng – hành động trong vận hành của nhà xưởng khung thép đang khai thác ở Đắk Lắk, với số ít cảm biến và kịch bản kiểm tra – xử lý – truy ngược đầu cuối được ghi tách khỏi dữ liệu và hồ sơ thật.

Bảng 5.2 là nguồn duy nhất cho quan hệ giữa khoảng trống, mục tiêu, câu hỏi, gói công việc, cổng kiểm chứng, môi trường và bằng chứng cần có; các mục sau chỉ giải thích logic, đóng góp và phạm vi.

<span id="TLTQ_Bang_5_2" class="anchor"></span>Bảng 5.2. Khoảng trống, mục tiêu, câu hỏi, gói công việc, cổng kiểm chứng và bằng chứng cần có

| Khoảng trống | Mục tiêu | Câu hỏi | Gói công việc | Cổng kiểm chứng | Môi trường | Bằng chứng cần có |
|:--:|:--:|:--:|:---:|:---:|:-----|:----------|
| KT1 | Mục tiêu 1 | RQ1 | WP1 | Gate 1 (bằng chứng phòng thí nghiệm) | Phòng thí nghiệm, khung thép 1:10 | Hiệu năng ở ba mức đánh giá; bản ghi bằng chứng có điều kiện đã đánh giá |
| KT2 | Mục tiêu 2 | RQ2 | WP2 | Gate 2–3 (mô hình truy vết và kiểm chứng) | Lớp dữ liệu truy vết trên BIM nhà xưởng ở Khánh Hòa | Câu hỏi năng lực được trả lời đúng, đủ; M1–M4 so với B0 và B1 trên bộ ca đã khóa |
| KT3 | Mục tiêu 3 | RQ3 | WP3 | Gate 4–5 (khả thi hiện trường, hỗ trợ quyết định) | Nhà xưởng đang khai thác ở Đắk Lắk | Dữ liệu thật về đủ, ánh xạ đúng; kịch bản giả định truy ngược được đầu cuối; công sức ghi nhận |
| KT2, KT3 | Mục tiêu 2, 3 | RQ2, RQ3 | WP4 (tổng hợp hỗ trợ quyết định) | Gate 5 (hỗ trợ quyết định) | Lớp dữ liệu và hiện trường | Mỗi mức ưu tiên và mỗi sự kiện chuyển trạng thái truy được về luật, bằng chứng và người rà soát |

## 5.4. Câu hỏi nghiên cứu

Ba câu hỏi nghiên cứu (RQ) được đặt cho ba mục tiêu:

> RQ1: Khi đánh giá theo đơn vị độc lập ở hai mức, giữ lại một lần chạy (LORO) và giữ lại một đợt thí nghiệm (LOCO), các mô hình phân biệt trạng thái liên kết bu lông có kiểm soát trên khung thép 1:10 ở mức nào, chênh lệch bao nhiêu so với đánh giá cùng lần chạy, và mỗi kết quả được ghi kèm những điều kiện đã đánh giá nào?
>
> RQ2: Khi bằng chứng trạng thái được nối với cấu kiện BIM, hồ sơ kiểm tra và lịch sử hành động, người quản lý có truy ngược được bằng chứng đã dùng, tính phù hợp của bằng chứng tại thời điểm sử dụng và trách nhiệm của từng chủ thể hay không?
>
> RQ3: Trên nhà xưởng đang khai thác, chuỗi bằng chứng – hành động có thu đủ dữ liệu thật, giữ đúng ánh xạ cảm biến – cấu kiện qua thời gian quan trắc, và truy ngược được đầu cuối một kịch bản kiểm tra – xử lý giả định được ghi tách khỏi dữ liệu thật hay không, với công sức ghi nhận bao nhiêu?

Ba câu hỏi tạo thành một mạch: RQ1 xác định điều kiện tạo và đánh giá bằng chứng; RQ2 bảo toàn và kiểm các điều kiện đó khi bằng chứng được sử dụng; RQ3 kiểm khả năng duy trì chuỗi trong vận hành thực. Về dữ liệu, RQ1 cấp cho RQ2 các bản ghi bằng chứng dùng làm ca kiểm thử quy tắc, và RQ2 cấp lớp dữ liệu truy vết cùng công cụ kiểm ràng buộc cho RQ3. Đánh giá của RQ2 không phụ thuộc thời gian quan trắc của RQ3, và số liệu phòng thí nghiệm không được dùng làm kết luận về hiện trường.

## 5.5. Thiết kế nghiên cứu và cổng kiểm chứng

Luận án dùng bốn phương pháp khoa học (Bảng 5.3). Tổng quan tài liệu theo chủ đề có cấu trúc xác lập cơ sở lý luận và khoảng trống (Mục 1.5.2). Thực nghiệm có kiểm soát trong phòng thí nghiệm trả lời RQ1 (Mục 3.4). Xây dựng một lớp dữ liệu truy vết rồi đánh giá bằng so sánh với hai đối chứng trả lời RQ2 (Mục 4.6); RQ2 được đo bằng câu hỏi năng lực (M3), tỉ lệ phát hiện lỗi chèn mù (M2), mức đủ thuộc tính (M1) và công sức ghi nhận (M4) trên BIM của nhà xưởng ở Khánh Hòa, so với B0 và B1. Nghiên cứu trường hợp trên một nhà xưởng đang khai thác trả lời RQ3 (Mục 3.5). Vai trò của AI theo nguyên tắc ở Mục 3.4.2.

<span id="TLTQ_Bang_5_3" class="anchor"></span>Bảng 5.3. Phương pháp khoa học theo câu hỏi nghiên cứu

| Câu hỏi | Phương pháp khoa học | Kế thừa từ | Trình bày chi tiết |
|:--:|:---|:---|:--:|
| RQ1 | Thực nghiệm có kiểm soát; đánh giá theo đơn vị độc lập | Đơn vị độc lập \[14\]; cấp chia dữ liệu \[15\]; rò rỉ \[53\]; giữ lại đợt sau tháo – lắp \[19\]; kiểm định hoán vị \[59\]; thiên lệch khi chọn mô hình \[@D28DT7CE\] | Mục 3.4 |
| RQ2 | Xây dựng lớp dữ liệu truy vết; so sánh với hai đối chứng bằng bộ câu hỏi năng lực và lỗi chèn mù | Chuỗi kiểm tra – cấu kiện – hành động \[35\]; sự kiện đổi trạng thái \[@P3ZIHF8G\]; bước chuyển có bằng chứng \[44\]; kiểm ràng buộc tự động \[21\]; kiểm bằng ca vi phạm cố ý \[2\] | Mục 4.6 |
| RQ3 | Nghiên cứu trường hợp; triển khai và đánh giá khả thi | Học từ trạng thái bình thường \[@TDRPDWJE\], \[@G98ZWHKW\]; tham số hóa theo biến môi trường – vận hành \[@23TBQTIP\]; nhãn từ kiểm tra \[@Z9RD5DMZ\]; quan trắc dài hạn \[75\] | Mục 3.5 |

Ba mục tiêu tạo ra bốn loại bằng chứng, mỗi loại chỉ khẳng định điều nó kiểm chứng được. Hình 5.1 xếp bốn lớp từ bằng chứng phòng thí nghiệm ở dưới cùng tới hỗ trợ quyết định quản lý ở trên cùng; Bảng 5.4 ghi nội dung kiểm chứng và điều không được suy ra ở mỗi lớp.

![](../figures/Hinh_5_2_Kien_truc_kiem_chung_bon_lop.png)

<span id="TLTQ_Hinh_5_1" class="anchor"></span>Hình 5.1. Kiến trúc kiểm chứng bốn lớp

<span id="TLTQ_Bang_5_4" class="anchor"></span>Bảng 5.4. Bốn lớp bằng chứng và thang kiểm chứng

| Lớp và mức | Mục tiêu | Nội dung kiểm chứng | Điều không được suy ra |
|:---|:--:|:---|:---|
| Lớp 1 – Bằng chứng phòng thí nghiệm (V1) | 1 | Phân biệt trạng thái có kiểm soát dưới đánh giá theo đơn vị độc lập; mức chênh lệch so với đánh giá cùng lần chạy | Chẩn đoán hiện trường |
| Lớp 2 – Truy vết thông tin (V2) | 2 | Trả lời đúng và đủ bộ câu hỏi năng lực về căn cứ và người chịu trách nhiệm; tỉ lệ phát hiện lỗi chèn mù và báo lỗi nhầm so với B0 và B1 trên bộ ca đã khóa | Độ chính xác kỹ thuật của mô hình phân loại; giá trị của bằng chứng 1:10 cho quyết định tại nhà xưởng |
| Lớp 3 – Khả năng áp dụng trong bối cảnh thực tế (V3) | 3 | Dữ liệu thật về đủ, ánh xạ đúng; truy ngược được kịch bản giả định đầu cuối; công sức ghi nhận | Phát hiện hư hỏng thực; hiệu năng phát hiện bất thường |
| Lớp 4 – Hỗ trợ quyết định quản lý (V4) | 2, 3 | Mỗi mức ưu tiên và mỗi sự kiện chuyển trạng thái truy được về luật, bằng chứng và người rà soát | Quyết định tự động hoặc tính tối ưu của quyết định |

Mỗi gói công việc kết thúc ở một cổng kiểm chứng, tức điểm duyệt bằng chứng trước khi kết quả được dùng cho bước sau. Gate 1 xác nhận bằng chứng phòng thí nghiệm: kết quả của Mục tiêu 1 chỉ được dùng sau khi dữ liệu, cách chia theo đơn vị độc lập, quy trình tiền xử lý và đánh giá được kiểm soát để tránh rò rỉ và tái lập được. Gate 2–3 khóa và kiểm chứng mô hình truy vết. Gate 4–5 kiểm khả thi hiện trường và logic hỗ trợ quyết định. Chi tiết kỹ thuật của Gate 1 thuộc Chuyên đề 1.

## 5.6. Đóng góp dự kiến

Đóng góp dự kiến được phát biểu dưới dạng tri thức và nguyên tắc mà luận án muốn rút ra, theo ba tầng (Bảng 5.5). Các kết quả LORO, LOCO, M1–M4 và tỉ lệ trả lời đúng câu hỏi năng lực chỉ là bằng chứng kiểm chứng đóng góp. Mỗi đóng góp chỉ được khẳng định khi kết quả kiểm chứng ủng hộ.

<span id="TLTQ_Bang_5_5" class="anchor"></span>Bảng 5.5. Ba tầng đóng góp dự kiến và bằng chứng kiểm chứng

| Đóng góp | Nội dung dự kiến | Bằng chứng kiểm chứng | Khoảng trống, mục tiêu |
|:-----|:--------------|:--------|:---:|
| 1. Quản trị hiệu lực của bằng chứng | Bằng chứng trạng thái mang nguồn gốc, độ bất định và phạm vi hiệu lực, và các thuộc tính này được kiểm khi bằng chứng được sử dụng; với dữ liệu dao động của khung thép liên kết bu lông, cấp đơn vị được giữ trọn khi chia dữ liệu là một yếu tố quan trọng quyết định cách diễn giải phạm vi hiệu lực của kết quả | Hiệu năng ở LORO, LOCO so với đánh giá cùng lần chạy; biến thiên theo seed và fold; kiểm định hoán vị | KT1; Mục tiêu 1 |
| 2. Truy vết bằng chứng – hành động kiểm chứng được | Bằng chứng được nối tới cấu kiện BIM, bản ghi kiểm tra và lịch sử hành động bằng mô hình dữ liệu, ràng buộc toàn vẹn và câu hỏi năng lực | M3 (câu hỏi năng lực trả lời đúng, đủ), M2 và M1 so với B1 | KT2; Mục tiêu 2 |
| 3. Sử dụng bằng chứng theo thời gian và có trách nhiệm | Mỗi lần dùng bằng chứng hoặc đổi trạng thái hành động truy được chủ thể, vai trò, thời điểm, bằng chứng và lý do; can thiệp vật lý làm phát sinh yêu cầu rà soát lại hiệu lực của bằng chứng và đường cơ sở trước đó | M2 ở nhóm lỗi dùng ngoài phạm vi và đổi trạng thái không căn cứ; câu hỏi năng lực về can thiệp; kịch bản hiện trường | KT2, KT3; Mục tiêu 2, 3 |
| Thực tiễn | Mức truy ngược đúng so với công sức ghi nhận, trên bộ hồ sơ của công trình nghiên cứu; điều kiện duy trì chuỗi với số ít cảm biến trong vận hành nhà xưởng | M3 đọc cùng M4, so với B0; dữ liệu thật về đủ, ánh xạ đúng | KT2, KT3; Mục tiêu 2, 3 |

Nếu bỏ đi hình BIM và bảng điểm của các mô hình AI, phần tri thức quản lý còn lại là một cách kiểm soát căn cứ của quyết định kiểm tra – bảo trì qua thời gian. Cách đó trả lời được câu hỏi: tại thời điểm quyết định, bằng chứng nào được dùng, bằng chứng đó có còn phù hợp không, ai dùng với vai trò gì, và vì sao trạng thái hành động thay đổi, với công sức ghi nhận chấp nhận được. Ba câu hỏi nghiên cứu cung cấp bằng chứng cho phát biểu này ở ba môi trường. Hiệu quả kinh tế, mức giảm sự cố hay chất lượng bảo trì không được đo nên không được suy ra. Các khái niệm của SSN và PROV-O được đối chiếu bằng một bảng ánh xạ (Phụ lục A); luận án không xây dựng ontology hay nền tảng phần mềm mới.

## 5.7. Phạm vi và giới hạn

Bảng 5.6 tách phạm vi chính, phạm vi hỗ trợ, hướng phát triển sau luận án và các nội dung ngoài phạm vi.

<span id="TLTQ_Bang_5_6" class="anchor"></span>Bảng 5.6. Phạm vi của luận án

| Nhóm | Nội dung |
|:---|:---|
| Phạm vi chính | Dữ liệu dao động → bằng chứng trạng thái; truy vết tới cấu kiện BIM; bản ghi kiểm tra; trạng thái và hỗ trợ hành động; duy trì chuỗi trong vận hành nhà công nghiệp khung thép |
| Phạm vi hỗ trợ | Học máy như công cụ tạo bằng chứng; BIM/IFC; nguồn gốc dữ liệu; con người trong vòng lặp; mô hình phần tử hữu hạn danh nghĩa để tham chiếu |
| Hướng phát triển sau luận án | Kết cấu và tài sản khác; hiệu năng phát hiện hư hỏng ở hiện trường; mở rộng số cảm biến; chọn lần kiểm tra theo giá trị kỳ vọng của thông tin; bù biến đổi bằng đồng liên kết; kiểm yêu cầu thông tin bằng IDS; đánh giá kinh tế quy mô lớn |
| Ngoài phạm vi | Chẩn đoán hư hỏng hiện trường khi chưa có kiểm tra xác nhận; dự báo tuổi thọ còn lại; bảo trì dự báo; suy luận suy giảm độ cứng; tối ưu vị trí cảm biến; bảo trì tự động |

Các giới hạn được gom theo ba loại bằng chứng. Về bằng chứng phòng thí nghiệm, mô hình 1:10 cho phép tạo trạng thái liên kết có kiểm soát; tương tự động lực học với nhà xưởng nằm ngoài phạm vi kiểm chứng. Lực siết bu lông không được đo, nên thí nghiệm kiểm khả năng phân biệt vị trí can thiệp, không định lượng mức nới lỏng; bộ phân loại và ngưỡng học trên mô hình 1:10 không được dùng ở nhà xưởng. Nguồn gốc, độ bất định và phạm vi hiệu lực làm bằng chứng rà soát được, không bảo đảm dự đoán đúng.

Về truy vết thông tin, bằng chứng từ mô hình 1:10 chỉ là ca kiểm thử quy tắc, và kết quả M2 có giá trị cho bộ ca đã khóa trên một công trình. Hồ sơ B0 gồm 20–30 hồ sơ của một nhà xưởng nên chỉ đại diện cho thực hành tại công trình nghiên cứu. Vị trí cảm biến chỉ khu vực cần xem xét; vị trí hư hỏng do kiểm tra xác lập.

Về khả thi hiện trường, với số ít cảm biến, Mục tiêu 3 kết luận về khả năng vận hành và truy vết của chuỗi tại các vị trí đã đo, không kết luận về toàn bộ kết cấu. Phần truy ngược đầu cuối được kiểm trên kịch bản giả định; bản ghi kiểm tra thật chỉ được đưa vào khi có đợt kiểm tra trong thời gian quan trắc. Mục tiêu 3 không đánh giá hiệu năng phát hiện của autoencoder hay hiệu quả của bước bù nhiệt độ – cầu trục. Bất thường trong dữ liệu vận hành dẫn tới xem xét và kiểm tra, không dẫn trực tiếp tới kết luận hư hỏng. Điều kiện môi trường, kể cả yếu tố ven biển nếu có, được ghi như bối cảnh của công trình; tác động của ăn mòn không được đo.

Mô hình phần tử hữu hạn, nếu được dùng, chỉ là mô hình danh nghĩa, chưa hiệu chuẩn, dùng để tham chiếu và không dùng cho chẩn đoán hư hỏng. Song sinh số dựa trên dữ liệu là mục tiêu kiến trúc; năng lực thực tế được đánh giá sau triển khai (Mục 2.3). Về phương pháp tổng quan, các khoảng trống và nhận định về thực hành quan trắc ở Việt Nam, về các khung song sinh số được xác lập trong tập tài liệu đã rà soát; một số nguồn về thực hành trong nước mới được đối chiếu ở mức tóm tắt.

## 5.8. Kiến trúc nghiên cứu của luận án

Nghiên cứu được tổ chức thành ba bước theo ba mục tiêu và một bước tổng hợp; các bước kế tiếp nhau về dữ liệu nhưng một phần làm song song được. Bước thứ nhất thực hiện thí nghiệm trên mô hình khung thép 1:10 và đóng Gate 1; song song, nhà xưởng ở Đắk Lắk được khảo sát để chọn vị trí đặt cảm biến, và hồ sơ kiểm định của nhà xưởng ở Khánh Hòa được thu thập cho đối chứng B0. Bước thứ hai đặc tả và kiểm chứng lớp dữ liệu truy vết qua Gate 2–3; bước này không chờ quan trắc dài hạn. Bước thứ ba lắp cảm biến, lập đường cơ sở vận hành và chạy kịch bản giả định cột C3 tách khỏi dữ liệu thật qua Gate 4–5. Gói tổng hợp hỗ trợ quyết định nối kết quả của hai bước sau thành logic bốn mức có người rà soát.

Tiểu luận khép lại bằng ba nhận định. Thứ nhất, luận án giải quyết một bài toán quản lý thông tin: căn cứ của quyết định kiểm tra – bảo trì phải truy xuất và rà soát được qua thời gian. Thứ hai, đóng góp dự kiến nằm ở truy vết bằng chứng có phạm vi hiệu lực, từ lúc bằng chứng được tạo tới lúc được dùng cho hành động; AI và BIM là công cụ. Thứ ba, quyết định kiểm tra và bảo trì vẫn thuộc về kỹ sư và người có thẩm quyền.
