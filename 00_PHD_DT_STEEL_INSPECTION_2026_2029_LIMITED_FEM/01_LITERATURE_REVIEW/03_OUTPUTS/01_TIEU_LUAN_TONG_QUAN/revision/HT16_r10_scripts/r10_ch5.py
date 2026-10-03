# -*- coding: utf-8 -*-
"""HT16 r10 – Chương 5 viết lại."""
import os, sys
sys.stdout.reconfigure(encoding='utf-8')
ROOT = r'H:\My Drive\03_RESEARCH\01_PHD_DT_AI_AM\00_PHD_DT_STEEL_INSPECTION_2026_2029_LIMITED_FEM\01_LITERATURE_REVIEW\03_OUTPUTS\01_TIEU_LUAN_TONG_QUAN\tieuluan'
def C(s): return s.replace('⟦', '\\[').replace('⟧', '\\]')
f = os.path.join(ROOT, '05_chuong5.md'); t = open(f, encoding='utf-8').read()
def cut(a, b=None):
    i = t.index(a); j = len(t) if b is None else t.index(b, i); return t[i:j]

head = cut('# CHƯƠNG 5.', 'Chương này tổng hợp')
s51 = cut('## 5.1. Tổng hợp các nghiên cứu đã rà soát', '## 5.2.')
rqs = cut('> RQ1:', 'Ba câu hỏi tạo thành một mạch')
bang53 = cut('<span id="TLTQ_Bang_5_3"', 'Ba mục tiêu tạo ra bốn loại bằng chứng')
hinh_bang54 = cut('Ba mục tiêu tạo ra bốn loại bằng chứng', '## 5.6.')
bang56 = cut('<span id="TLTQ_Bang_5_6"', 'Mỗi loại bằng chứng được dùng cho kết luận cùng loại')
s51 = s51.replace('## 5.1. Tổng hợp các nghiên cứu đã rà soát', '## 5.1. Tổng hợp bằng chứng từ tài liệu')

new = head + C('''Chương này rút ra ba khoảng trống liên kết từ các chương tổng quan, rồi nêu luận đề, mục tiêu, câu hỏi, thiết kế nghiên cứu cùng các cổng kiểm chứng, đóng góp dự kiến, phạm vi và kiến trúc nghiên cứu của luận án. Nội dung chi tiết của phương pháp được trình bày ở Mục 3.4, 3.5 và 4.6.

''') + s51 + C('''## 5.2. Ba khoảng trống liên kết

Ba khoảng trống dưới đây là ba mặt của cùng một vấn đề ở Mục 1.4. Một kết quả từ dữ liệu dao động chỉ trở thành căn cứ quản lý khi được tổ chức thành bằng chứng có phạm vi hiệu lực, được bảo toàn và kiểm khi sử dụng, và được duy trì trong vận hành. KT1 tạo ra bằng chứng có phạm vi hiệu lực; KT2 bảo toàn và kiểm bằng chứng đó khi được dùng; KT3 duy trì chuỗi trong vận hành thực. Thiếu KT1, chuỗi không có bằng chứng mang điều kiện đã đánh giá để kiểm. Thiếu KT2, điều kiện đó mất khi bằng chứng đi vào hồ sơ. Thiếu KT3, hai lời giải dừng ở phòng thí nghiệm và mô hình dữ liệu. Vì vậy ba khoảng trống thuộc cùng một luận án. Mỗi khoảng trống được trình bày theo trình tự: nghiên cứu gần nhất, phần đã giải quyết, giới hạn và phần còn lại; mọi phát biểu được giới hạn trong tập tài liệu đã rà soát.

### 5.2.1. KT1 – Bằng chứng trạng thái có phạm vi hiệu lực từ dữ liệu dao động

Nghiên cứu gần nhất là các đánh giá theo nhóm cho dữ liệu có nguồn vật lý lặp: Beleites và cộng sự với dữ liệu quang phổ ⟦14⟧, Wheat và cộng sự với ổ lăn ⟦15⟧, Kapoor và Narayanan về rò rỉ trong khoa học dùng học máy ⟦53⟧, và Ramasso và cộng sự với phát xạ âm trên dầm nhôm lắp bu lông ⟦19⟧. Các nghiên cứu này đã xác lập nguyên tắc đơn vị độc lập, đánh giá theo nhóm và kiểm soát rò rỉ. Chia dữ liệu dưới cấp đơn vị độc lập làm hiệu năng lạc quan ⟦14⟧, ⟦15⟧, ⟦53⟧, và độ chính xác giảm mạnh khi kiểm tra trên một lần lắp chưa thấy ⟦19⟧. Sau mỗi lần lắp lại, phần lớn dữ liệu đáp ứng đã thu mất tác dụng cho theo dõi trạng thái ⟦18⟧; trên cầu thép KW51, mô hình huấn luyện trước can thiệp không còn đại diện cho trạng thái bình thường sau can thiệp ⟦@2ZJSENQU⟧. Luận án kế thừa các nguyên tắc này; đánh giá chống rò rỉ không phải phần mới của luận án.

Giới hạn nằm ở hai vế. Về đánh giá (vế A1), các nghiên cứu đã rà soát cho phân loại trạng thái liên kết bu lông trên khung thép chia tập trong cùng lần lắp ráp hoặc cùng bản ghi ⟦48⟧, ⟦@VVBGM9EN⟧, nên mức lạc quan với loại kết cấu này chưa được báo cáo. Về khai báo (vế A2), các chuẩn và đề xuất hiện có đã biểu diễn được nhiều phần của bài toán. SOSA/SSN biểu diễn từng quan trắc cùng cảm biến, thủ tục và đối tượng được quan trắc ⟦@GHAZGWUN⟧; PROV-O biểu diễn nguồn gốc của từng thực thể, hoạt động và tác nhân ⟦69⟧. Thẻ mô hình khai báo điều kiện đánh giá và mục đích sử dụng ở mức mô hình ⟦@82WQNDHU⟧, còn ⟦53⟧ đề xuất bảng thông tin mô hình để khai báo và kiểm các dạng rò rỉ. Phần còn lại là áp dụng có hệ thống các nguyên tắc đánh giá vào bằng chứng trạng thái của khung thép liên kết bu lông, và đưa bối cảnh đánh giá vào phạm vi hiệu lực như trường bắt buộc, được kiểm tại lần sử dụng trong nghiệp vụ kiểm tra – bảo trì. Khoảng trống này cần giải quyết vì hiệu lực sau can thiệp không đoán trước được: có trường hợp mất ⟦18⟧, ⟦@2ZJSENQU⟧, có trường hợp một lần siết lại vẫn được phân loại đúng ⟦48⟧. Nó ứng với câu hỏi "tin được đến mức nào?".

### 5.2.2. KT2 – Truy vết từ bằng chứng đến hành động có trách nhiệm

Nghiên cứu gần nhất là chuỗi lần kiểm tra – hư hỏng – cấu kiện – nhiệm vụ bảo trì bằng thực thể chuẩn IFC 4.3 của Bellon và cộng sự ⟦35⟧. Cùng nhóm này có lệnh bảo trì mang trạng thái và phê duyệt của IFC4 ⟦@63XPSMIR⟧, sự kiện đổi trạng thái của BCF-API 3.0 ⟦@P3ZIHF8G⟧, khuôn bước chuyển có bằng chứng và đúng thẩm quyền cho gói thông tin bàn giao của García và cộng sự ⟦44⟧, và lược đồ IFC cho hệ theo dõi trạng thái của Theiler và Smarsly ⟦2⟧. Các nguồn này đã giải quyết việc biểu diễn chuỗi kiểm tra – hành động, trạng thái và phê duyệt, lịch sử đổi trạng thái của vấn đề và quan hệ cảm biến – cấu kiện. Giới hạn là chuỗi của ⟦35⟧ chỉ nhận hư hỏng phát hiện bằng mắt, và trạng thái bị ghi đè khi có lần bảo trì. Trong các khung song sinh số đã rà soát, chuỗi dừng ở cảnh báo ⟦3⟧, ⟦7⟧; xác nhận của chuyên gia thường chỉ được dùng làm nhãn ⟦@73MBWFVJ⟧, ⟦@Z9RD5DMZ⟧.

Phần còn lại có hai điểm. Bằng chứng có phạm vi hiệu lực chưa đi vào chuỗi kiểm tra – cấu kiện – hành động, và việc dùng bằng chứng chưa được kiểm so với phạm vi đó tại lần sử dụng. Mỗi lần đổi trạng thái của hành động cũng chưa được ghi thành sự kiện có căn cứ, có chủ thể và vai trò người thực hiện, với bước xác minh tách khỏi thời điểm can thiệp. Khoảng trống này khác với tích hợp cảm biến – BIM: tích hợp đã có nhiều tiền lệ, còn truy vết bằng chứng kiểm chứng được thì chưa. Nó cần giải quyết vì thiết kế một hệ theo dõi phải xác định hành động nào được đưa ra và ai có thẩm quyền ⟦@EBB69J4F⟧. Khi xảy ra sự cố sau một lần sửa chữa, đơn vị quản lý cũng cần truy ngược được quyết định về bằng chứng và người phê duyệt. Đây là câu hỏi "ai đã xử lý, dựa vào đâu?", đặt tại đúng thời điểm của từng quyết định.

### 5.2.3. KT3 – Duy trì chuỗi bằng chứng – hành động trong vận hành nhà công nghiệp khung thép

Nghiên cứu gần nhất là quan trắc dài hạn với đường cơ sở phụ thuộc nhiệt độ trên cầu nhịp lớn ⟦75⟧, phát hiện bất thường học từ trạng thái bình thường ⟦@TDRPDWJE⟧, ⟦@G98ZWHKW⟧, bù biến đổi môi trường – vận hành ⟦@23TBQTIP⟧ và nhãn từ kiểm tra ⟦@Z9RD5DMZ⟧. Các nghiên cứu này cho thấy cảm biến triển khai được dài hạn và đề xuất cách xử lý dữ liệu khi thiếu nhãn hư hỏng. Giới hạn là chúng được thực hiện trên cầu hoặc kết cấu thu nhỏ. Vấn đề thực của theo dõi trạng thái chỉ lộ ra trên kết cấu thật ⟦@EBB69J4F⟧ (tr. 14–15), thành công trên mô hình thu nhỏ chưa bảo đảm hiệu quả ở hiện trường ⟦45⟧, và bộ phân loại học trên một kết cấu khó chuyển sang kết cấu khác ⟦56⟧, ⟦57⟧. Rung do cầu trục ⟦@38FMATHE⟧ và chi phí tiếp cận ⟦@QMVQCEL5⟧ là điều kiện riêng của nhà công nghiệp. Trong tập tài liệu trong nước đã khảo sát, quan trắc tập trung vào cầu, lún và sụt lún ⟦@8S93B6VF⟧, ⟦@G7I5JPVC⟧, ⟦@UMPDAEG5⟧.

Phần còn lại là câu hỏi chuỗi bằng chứng – kiểm tra – hành động có được duy trì và truy ngược được trong vận hành nhà xưởng hay không. Cụ thể, dữ liệu có về đủ không, ánh xạ cảm biến – cấu kiện có giữ đúng qua thời gian không, mỗi bằng chứng có truy được về nguồn đo và hồ sơ không, và công sức ghi nhận có chấp nhận được không. KT3 là khả thi của việc duy trì chuỗi, không phải kiểm chứng phát hiện hư hỏng ở hiện trường; phép thử dự kiến không có đủ dữ liệu hư hỏng cho câu hỏi đó. Ở mức này, câu hỏi "cái gì bất thường, ở đâu?" chỉ được trả lời bằng việc chỉ ra khu vực cấu kiện mà bằng chứng đề nghị kiểm tra.

## 5.3. Luận đề và mục tiêu nghiên cứu

Từ ba khoảng trống, luận đề trung tâm của luận án được phát biểu như sau:

> Với nhà công nghiệp khung thép liên kết bu lông, kết quả rút từ dữ liệu dao động là căn cứ đề nghị kiểm tra, còn kết luận hư hỏng do kỹ sư đưa ra sau kiểm tra. Kết quả đó trở thành căn cứ có thể truy xuất, rà soát mức phù hợp và giải trình khi mỗi bằng chứng trạng thái mang theo nguồn gốc, độ bất định và phạm vi hiệu lực, được kiểm tại lần sử dụng, và được nối qua bản ghi kiểm tra tới lịch sử trạng thái của hành động kiểm tra – bảo trì. Độ tin cậy kỹ thuật của bản thân kết quả được đánh giá riêng.

Mục tiêu tổng quát của luận án là phát triển và kiểm chứng một chuỗi thông tin truy vết từ bằng chứng trạng thái tới hành động kiểm tra – bảo trì cho nhà công nghiệp khung thép liên kết bu lông, hướng tới song sinh số dựa trên dữ liệu như mục tiêu kiến trúc. Ba mục tiêu cụ thể ứng một – một với ba khoảng trống.

**Mục tiêu 1 (KT1).** Xác lập quy trình tạo bằng chứng trạng thái liên kết bu lông có phạm vi hiệu lực từ dữ liệu dao động trên mô hình khung thép tỉ lệ 1:10, bằng cách đo mức chênh lệch giữa đánh giá cùng lần chạy và hai mức đánh giá theo đơn vị độc lập với bốn mô hình học máy, rồi ghi điều kiện đã đánh giá và độ bất định cho từng kết quả.

**Mục tiêu 2 (KT2).** Xây dựng và kiểm chứng lớp dữ liệu truy vết bằng chứng – hành động cho kiểm tra – bảo trì kết cấu thép, liên thông với IFC 4.3 theo cách dùng của ⟦35⟧ và với BCF 3.0 mà không sửa lược đồ chuẩn, trên BIM của nhà xưởng ở Khánh Hòa.

**Mục tiêu 3 (KT3).** Triển khai và kiểm chứng khả năng duy trì chuỗi bằng chứng – hành động trong vận hành của nhà xưởng khung thép đang khai thác ở Đắk Lắk, với số ít cảm biến và kịch bản kiểm tra – xử lý – truy ngược đầu cuối được ghi tách khỏi dữ liệu và hồ sơ thật.

Bảng 5.2 là nguồn duy nhất cho quan hệ giữa khoảng trống, mục tiêu, câu hỏi, gói công việc, cổng kiểm chứng, môi trường và bằng chứng cần có; các mục sau chỉ giải thích logic, đóng góp và phạm vi.

<span id="TLTQ_Bang_5_2" class="anchor"></span>Bảng 5.2. Khoảng trống, mục tiêu, câu hỏi, gói công việc, cổng kiểm chứng và bằng chứng cần có

| Khoảng trống | Mục tiêu | Câu hỏi | Gói công việc | Cổng kiểm chứng | Môi trường | Bằng chứng cần có |
|:--:|:--:|:--:|:---:|:---:|:-----|:----------|
| KT1 | Mục tiêu 1 | RQ1 | WP1 | Gate 1 | Phòng thí nghiệm, khung thép 1:10 | Hiệu năng ở ba mức đánh giá với điều kiện so sánh đã khóa; biến thiên theo seed và fold; bản ghi bằng chứng có điều kiện đã đánh giá |
| KT2 | Mục tiêu 2 | RQ2 | WP2 | Gate 2–3 | Lớp dữ liệu truy vết trên BIM nhà xưởng ở Khánh Hòa | Câu hỏi năng lực được trả lời đúng, đủ; M1–M4 so với B0 và B1 trên bộ ca đã khóa |
| KT3 | Mục tiêu 3 | RQ3 | WP3 | Gate 4–5 | Nhà xưởng đang khai thác ở Đắk Lắk | Dữ liệu thật về đủ, ánh xạ đúng; kịch bản giả định truy ngược được đầu cuối; công sức ghi nhận |
| KT2, KT3 | Mục tiêu 2, 3 | RQ2, RQ3 | WP4 (tổng hợp hỗ trợ quyết định) | Gate 5 | Lớp dữ liệu và hiện trường | Mỗi mức ưu tiên và mỗi sự kiện chuyển trạng thái truy được về luật, bằng chứng và người rà soát |

## 5.4. Câu hỏi nghiên cứu

Ba câu hỏi nghiên cứu (RQ) được đặt cho ba mục tiêu:

''') + rqs + C('''Ba câu hỏi tạo thành một mạch: RQ1 xác định điều kiện tạo và đánh giá bằng chứng; RQ2 bảo toàn và kiểm các điều kiện đó khi bằng chứng được sử dụng; RQ3 kiểm khả năng duy trì chuỗi trong vận hành thực. Về dữ liệu, RQ1 cấp cho RQ2 các bản ghi bằng chứng dùng làm ca kiểm thử quy tắc, và RQ2 cấp lớp dữ liệu truy vết cùng công cụ kiểm ràng buộc cho RQ3. Đánh giá của RQ2 không phụ thuộc thời gian quan trắc của RQ3, và số liệu phòng thí nghiệm không được dùng làm kết luận về hiện trường.

## 5.5. Thiết kế nghiên cứu và cổng kiểm chứng

Luận án dùng bốn phương pháp khoa học (Bảng 5.3). Tổng quan tài liệu theo chủ đề có cấu trúc xác lập cơ sở lý luận và khoảng trống (Mục 1.5.2). Thực nghiệm có kiểm soát trong phòng thí nghiệm trả lời RQ1 (Mục 3.4). Xây dựng một lớp dữ liệu truy vết rồi đánh giá bằng so sánh với hai đối chứng trả lời RQ2 (Mục 4.6). Nghiên cứu trường hợp trên một nhà xưởng đang khai thác trả lời RQ3 (Mục 3.5). Vai trò của AI theo nguyên tắc ở Mục 3.4.2.

''') + bang53 + hinh_bang54 + C('''Mỗi gói công việc kết thúc ở một cổng kiểm chứng, tức điểm duyệt bằng chứng trước khi kết quả được dùng cho bước sau. Gate 1 chỉ được đóng khi đủ bảy điều kiện: danh sách lần chạy được khóa; phép chia dữ liệu theo nhóm không rò rỉ; tham số tiền xử lý được học bên trong phần huấn luyện của từng lần chia; việc chọn siêu tham số không dùng phần kiểm tra; chế độ đầu vào cảm biến của ResNet1D được xác nhận; cách gộp dự đoán khi tính chỉ số được thống nhất; và LORO, LOCO chỉ dùng các đợt thỏa điều kiện so sánh (Mục 3.4.3). Tại thời điểm viết tiểu luận, các điều kiện này chưa được xác nhận đầy đủ, nên chưa đủ bằng chứng để nêu kết quả của Mục tiêu 1. Gate 2 khóa đặc tả lớp dữ liệu, năm ràng buộc, bộ câu hỏi năng lực và bộ ca thử; Gate 3 đóng khi phép so sánh với B0 và B1 được thực hiện trên bộ ca đã khóa. Gate 4 mở việc triển khai hiện trường khi Gate 1–3 đã ổn định và khảo sát nhà xưởng hoàn tất; Gate 5 đóng khi chuỗi hiện trường và logic hỗ trợ quyết định được kiểm theo các lớp V3, V4 ở Bảng 5.4.

## 5.6. Đóng góp dự kiến

Đóng góp dự kiến được phát biểu dưới dạng tri thức và nguyên tắc mà luận án muốn rút ra, theo ba tầng (Bảng 5.5). Các kết quả LORO, LOCO, M1–M4 và tỉ lệ trả lời đúng câu hỏi năng lực là bằng chứng dùng để kiểm chứng đóng góp, không phải bản thân đóng góp. Mỗi đóng góp chỉ được khẳng định khi kết quả kiểm chứng ủng hộ.

<span id="TLTQ_Bang_5_5" class="anchor"></span>Bảng 5.5. Ba tầng đóng góp dự kiến và bằng chứng kiểm chứng

| Đóng góp | Nội dung dự kiến | Bằng chứng kiểm chứng | Khoảng trống, mục tiêu |
|:-----|:--------------|:--------|:---:|
| 1. Quản trị hiệu lực của bằng chứng | Điều kiện đánh giá, nguồn gốc, độ bất định và phạm vi hiệu lực được ghi thành thuộc tính kiểm tra được của bằng chứng trạng thái; với dữ liệu dao động của khung thép liên kết bu lông, cấp đơn vị được giữ trọn khi chia dữ liệu quyết định phạm vi được phép dùng | Hiệu năng ở LORO, LOCO so với đánh giá cùng lần chạy; biến thiên theo seed và fold; kiểm định hoán vị | KT1; Mục tiêu 1 |
| 2. Truy vết bằng chứng – hành động kiểm chứng được | Bằng chứng được nối tới cấu kiện BIM, bản ghi kiểm tra và lịch sử hành động bằng mô hình dữ liệu, ràng buộc toàn vẹn và câu hỏi năng lực | M3 (câu hỏi năng lực trả lời đúng, đủ), M2 và M1 so với B1 | KT2; Mục tiêu 2 |
| 3. Sử dụng bằng chứng theo thời gian và có trách nhiệm | Bằng chứng chỉ được dùng trong phạm vi còn hiệu lực; can thiệp vật lý mở lại điều kiện dùng bằng chứng và đường cơ sở; mỗi bước chuyển trạng thái truy được chủ thể, vai trò, bằng chứng và lý do | M2 ở nhóm lỗi dùng ngoài phạm vi và đổi trạng thái không căn cứ; câu hỏi năng lực về can thiệp; kịch bản hiện trường | KT2, KT3; Mục tiêu 2, 3 |
| Thực tiễn | Mức truy ngược đúng so với công sức ghi nhận, trên bộ hồ sơ của công trình nghiên cứu; điều kiện duy trì chuỗi với số ít cảm biến trong vận hành nhà xưởng | M3 đọc cùng M4, so với B0; dữ liệu thật về đủ, ánh xạ đúng | KT2, KT3; Mục tiêu 2, 3 |

Nếu bỏ đi hình BIM và bảng điểm của các mô hình AI, phần tri thức quản lý còn lại là một cách kiểm soát căn cứ của quyết định kiểm tra – bảo trì qua thời gian. Cách đó trả lời được câu hỏi: tại thời điểm quyết định, bằng chứng nào được dùng, bằng chứng đó có còn phù hợp không, ai dùng với vai trò gì, và vì sao trạng thái hành động thay đổi, với công sức ghi nhận chấp nhận được. Ba câu hỏi nghiên cứu cung cấp bằng chứng cho phát biểu này ở ba môi trường. Hiệu quả kinh tế, mức giảm sự cố hay chất lượng bảo trì không được đo nên không được suy ra. Các khái niệm của SSN và PROV-O được đối chiếu bằng một bảng ánh xạ (Phụ lục A); luận án không xây dựng ontology hay nền tảng phần mềm mới.

## 5.7. Phạm vi và giới hạn

''') + bang56 + C('''Các giới hạn được gom theo ba loại bằng chứng. Về bằng chứng phòng thí nghiệm, mô hình 1:10 cho phép tạo trạng thái liên kết có kiểm soát nhưng không chứng minh tương tự động lực học với nhà xưởng. Lực siết bu lông không được đo, nên thí nghiệm kiểm khả năng phân biệt vị trí can thiệp, không định lượng mức nới lỏng; bộ phân loại và ngưỡng học trên mô hình 1:10 không được dùng ở nhà xưởng. Nguồn gốc, độ bất định và phạm vi hiệu lực làm bằng chứng rà soát được, không bảo đảm dự đoán đúng.

Về truy vết thông tin, bằng chứng từ mô hình 1:10 chỉ là ca kiểm thử quy tắc, và kết quả M2 có giá trị cho bộ ca đã khóa trên một công trình. Hồ sơ B0 gồm 20–30 hồ sơ của một nhà xưởng nên chỉ đại diện cho thực hành tại công trình nghiên cứu. Vị trí cảm biến chỉ khu vực cần xem xét; vị trí hư hỏng do kiểm tra xác lập.

Về khả thi hiện trường, với số ít cảm biến, Mục tiêu 3 kết luận về khả năng vận hành và truy vết của chuỗi tại các vị trí đã đo, không kết luận về toàn bộ kết cấu. Phần truy ngược đầu cuối được kiểm trên kịch bản giả định; bản ghi kiểm tra thật chỉ được đưa vào khi có đợt kiểm tra trong thời gian quan trắc. Mục tiêu 3 không đánh giá hiệu năng phát hiện của autoencoder hay hiệu quả của bước bù nhiệt độ – cầu trục. Bất thường trong dữ liệu vận hành dẫn tới xem xét và kiểm tra, không dẫn trực tiếp tới kết luận hư hỏng. Điều kiện môi trường, kể cả yếu tố ven biển nếu có, được ghi như bối cảnh của công trình; tác động của ăn mòn không được đo.

Mô hình phần tử hữu hạn, nếu được dùng, chỉ là mô hình danh nghĩa, chưa hiệu chuẩn, dùng để tham chiếu và không dùng cho chẩn đoán hư hỏng. Song sinh số dựa trên dữ liệu là mục tiêu kiến trúc; năng lực thực tế được đánh giá sau triển khai (Mục 2.3). Về phương pháp tổng quan, các khoảng trống và nhận định về thực hành quan trắc ở Việt Nam, về các khung song sinh số được xác lập trong tập tài liệu đã rà soát; một số nguồn về thực hành trong nước mới được đối chiếu ở mức tóm tắt.

## 5.8. Kiến trúc nghiên cứu của luận án

Nghiên cứu được tổ chức thành ba bước theo ba mục tiêu và một bước tổng hợp; các bước kế tiếp nhau về dữ liệu nhưng một phần làm song song được. Bước thứ nhất thực hiện thí nghiệm trên mô hình khung thép 1:10 và đóng Gate 1; song song, nhà xưởng ở Đắk Lắk được khảo sát để chọn vị trí đặt cảm biến, và hồ sơ kiểm định của nhà xưởng ở Khánh Hòa được thu thập cho đối chứng B0. Bước thứ hai đặc tả và kiểm chứng lớp dữ liệu truy vết qua Gate 2–3; bước này không chờ quan trắc dài hạn. Bước thứ ba lắp cảm biến, lập đường cơ sở vận hành và chạy kịch bản giả định cột C3 tách khỏi dữ liệu thật qua Gate 4–5. Gói tổng hợp hỗ trợ quyết định nối kết quả của hai bước sau thành logic bốn mức có người rà soát.

Sau luận án, hướng nghiên cứu có thể mở rộng theo đối tượng: các loại nhà công nghiệp khác, như nhà kho, nhà xưởng không có cầu trục và nhà khung thép có liên kết hàn; các kết cấu thép khác như mái không gian, giàn và cầu thép nhịp nhỏ; và các tài sản khác trong khu công nghiệp. Mỗi mở rộng cần kiểm lại phạm vi hiệu lực của bằng chứng cho đối tượng mới. Cùng với đó là các hướng nêu ở Bảng 5.6.

Tóm lại, luận án giải quyết một bài toán quản lý: biến dữ liệu kỹ thuật thành bằng chứng có phạm vi hiệu lực, bảo toàn và kiểm chứng bằng chứng đó qua BIM/IFC và hồ sơ kiểm tra, rồi dùng nó minh bạch, có trách nhiệm để hỗ trợ quyết định kiểm tra – bảo trì. Khoảng trống trung tâm là chuỗi bằng chứng – hành động chưa giữ được điều kiện đã đánh giá của bằng chứng từ lúc tạo tới lúc dùng. Mô hình 1:10 cung cấp bằng chứng phòng thí nghiệm về các điều kiện đó, không cung cấp kết luận định lượng cho nhà xưởng. Quyết định kiểm tra và bảo trì thuộc về kỹ sư và người có thẩm quyền; AI chỉ tạo bằng chứng.
''')
open(f, 'w', encoding='utf-8', newline='').write(new)
print('ok', len(t.split()), '->', len(new.split()))
