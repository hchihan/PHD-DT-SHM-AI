# -*- coding: utf-8 -*-
"""HT16 r10 – Chương 1: gộp 1.2 thành hai cụm, chuyển khách thể – phạm vi vào 1.5.1, viết lại 1.4."""
import os, sys
sys.stdout.reconfigure(encoding='utf-8')
ROOT = r'H:\My Drive\03_RESEARCH\01_PHD_DT_AI_AM\00_PHD_DT_STEEL_INSPECTION_2026_2029_LIMITED_FEM\01_LITERATURE_REVIEW\03_OUTPUTS\01_TIEU_LUAN_TONG_QUAN\tieuluan'
def C(s): return s.replace('⟦', '\\[').replace('⟧', '\\]')
f = os.path.join(ROOT, '01_chuong1.md'); t = open(f, encoding='utf-8').read()
def cut(a, b=None):
    i = t.index(a); j = len(t) if b is None else t.index(b, i); return t[i:j]

head = cut('# CHƯƠNG 1.', 'Chương này đặt bài toán')
s111 = cut('Nhà công nghiệp khung thép được thiết kế và xây dựng', '### 1.1.2.')
s112 = cut('### 1.1.2. Bối cảnh pháp lý', '## 1.2.')
bang11 = cut('<span id="TLTQ_Bang_1_1"', 'Kiểm tra trực quan là phương pháp chủ đạo')
p_visual = cut('Kiểm tra trực quan là phương pháp chủ đạo', 'Quan trắc bằng cảm biến khắc phục')
p_sensor = cut('Quan trắc bằng cảm biến khắc phục', 'Biến đổi vận hành và môi trường là trở ngại')
p_eov = cut('Biến đổi vận hành và môi trường là trở ngại', 'Khoảng cách giữa phòng thí nghiệm')
p_vn = cut('Tại Việt Nam, quan trắc công trình được thực hiện', 'Tổng hợp lại, nhà công nghiệp ít được quan trắc')
s13 = cut('## 1.3.', '## 1.4.')
s152 = cut('### 1.5.2. Phương pháp tổng quan', None)

intro = C('''Chương này đặt bài toán của tiểu luận. Chương trình bày bối cảnh quản lý vận hành và pháp lý, đặc điểm của nhà công nghiệp khung thép liên kết bu lông cùng hạn chế của quan trắc và quản lý thông tin hiện nay, khái niệm bằng chứng trạng thái và nhu cầu của người quản lý, vấn đề nghiên cứu, rồi mục tiêu, phạm vi và phương pháp tổng quan. Các nội dung kỹ thuật về đánh giá mô hình, rò rỉ dữ liệu và cấu hình cảm biến được xét ở Chương 3.

## 1.1. Bối cảnh quản lý vận hành và chuyển đổi số

### 1.1.1. Quản lý thông tin trong vận hành

''')

s12 = C('''## 1.2. Nhà công nghiệp khung thép và bài toán kiểm tra – bảo trì

### 1.2.1. Đặc điểm vận hành và bài toán kiểm tra

Theo số liệu của Cục Đầu tư nước ngoài (Bộ Tài chính), đến khoảng tháng 11/2025 cả nước có 478 khu công nghiệp đã thành lập, trong đó 324 khu đã đi vào hoạt động với khoảng 68 nghìn ha đất công nghiệp ⟦@XM5ZUP99⟧. Nhà xưởng trong các khu này là tài sản trực tiếp phục vụ sản xuất. Bảo trì nhà công nghiệp cần thiết để công trình làm việc đúng chức năng và tránh gián đoạn cùng thiệt hại kinh tế ⟦@QMVQCEL5⟧ (tr. 1, 3). Ở phía quản lý, bảo trì kết cấu thép trong cơ sở công nghiệp được tổ chức như một chương trình kiểm tra – bảo trì cần hồ sơ hư hỏng cập nhật ⟦22⟧. Theo đánh giá của phần tổng quan nghiên cứu này, hậu quả của một sự cố kết cấu ở nhà xưởng gồm cả thời gian dừng sản xuất, không chỉ chi phí sửa chữa.

Với khung thép liên kết bu lông, nội lực giữa cột, kèo và cấu kiện phụ được truyền qua liên kết, nên tình trạng liên kết quyết định trực tiếp khả năng làm việc của khung. Ba nhóm yếu tố làm tình trạng này thay đổi trong vận hành. Nhóm thứ nhất là nới lỏng, tức sự mất lực siết, một dạng hư hỏng chủ yếu của mối ghép ren chịu dao động ⟦@WP5WUUF9⟧. Nhóm thứ hai là ăn mòn. Thử nghiệm phơi mẫu mười năm tại Việt Nam ghi nhận thời gian ẩm ướt rất dài và tốc độ ăn mòn thép các-bon ở cấp ăn mòn C3 tại hầu hết các trạm ⟦@SKCFNXPU⟧ (tr. 552, 557). Lớp mạ kẽm của bu lông suy giảm theo thời gian, nhất là trong môi trường công nghiệp và biển ⟦@IJGQYI7W⟧ (tr. 5177). Nhóm thứ ba là quá trình lắp ráp: trên mẫu có mối nối bu lông, đặc trưng động lực thay đổi giữa các lần lắp nếu quy trình không được kiểm soát ⟦18⟧. Theo đánh giá của phần tổng quan nghiên cứu này, một nhận định về liên kết vì vậy chỉ có giá trị khi kèm thời điểm, điều kiện và lần lắp ráp đã tạo ra nó.

Nhà xưởng còn làm việc ngay trong môi trường sản xuất mà nó phục vụ. Cầu trục, máy móc và thiết bị treo trên kết cấu tạo ra rung động thường xuyên. Với rung do cầu trục, năng lượng tập trung trong một dải tần nhất định và phụ thuộc vận tốc, gia tốc của cầu trục cùng độ gồ ghề của ray ⟦@38FMATHE⟧. Nghiên cứu này đo rung trên sàn nhà máy; việc rung cùng loại xuất hiện trên khung nhà xưởng là diễn giải của tiểu luận. Việc kiểm tra kết cấu nhà công nghiệp cũng tốn kém: cần nhiều nhân công, phải tiếp cận vùng cao hoặc nguy hiểm, cần thiết bị phụ trợ và có khi phải dừng sản xuất ⟦@QMVQCEL5⟧ (tr. 3, 5).

Các đặc điểm trên tạo nên bài toán kiểm tra của nhà xưởng. Người quản lý cần thông tin trạng thái giúp khoanh vùng cấu kiện cần kiểm tra trước, thay vì kiểm tra dàn trải. Thông tin đó phải dùng được dù tín hiệu chịu nhiễu do vận hành. Kết luận về tình trạng vẫn được xác lập qua kiểm tra của kỹ sư.

### 1.2.2. Hạn chế của quan trắc và quản lý thông tin hiện nay

Thông tin về tình trạng kết cấu trong vận hành đến từ hai nhóm phương pháp: kiểm tra định kỳ, chủ yếu bằng mắt, và quan trắc bằng thiết bị đo. Phần lớn nghiên cứu về hai nhóm này được thực hiện trên cầu và kết cấu hạ tầng (Bảng 1.1). Khi bằng chứng được lấy từ cầu hay kết cấu khác, tiểu luận trích đúng đối tượng của nguồn và ghi việc áp sang nhà xưởng là diễn giải.

''') + bang11 + p_visual + p_sensor + p_eov + C('''Khoảng cách giữa phòng thí nghiệm và hiện trường là giới hạn tiếp theo. Nhiều nghiên cứu làm trên mẫu đơn giản trong phòng thí nghiệm, trong khi vấn đề thực chỉ lộ ra trên kết cấu thật ⟦@EBB69J4F⟧ (tr. 14–15), ⟦45⟧. Nhãn hiện trường đến từ kiểm tra của chuyên gia nên hiếm và đắt ⟦@87NKU5IS⟧. Trong nghiên cứu của Da Silva và cộng sự, bộ phân loại lực siết học trên một dầm liên kết bu lông đã thất bại khi áp sang dầm tương tự ⟦56⟧. Vì vậy, luận án không chuyển bộ phân loại hay ngưỡng của phòng thí nghiệm ra nhà xưởng. Phần được chuyển là nguyên tắc tổ chức và đánh giá bằng chứng (Chương 3).

''') + p_vn + C('''Hạn chế cuối cùng nằm ở quản lý thông tin. Dữ liệu cảm biến, mô hình BIM và hồ sơ kiểm tra thường nằm ở các hệ khác nhau (Mục 1.1.1). Khi các nguồn này không được nối với nhau, một kết quả quan trắc khó trở thành căn cứ của một quyết định kiểm tra cụ thể. Tổng hợp lại, nhà công nghiệp ít được quan trắc bằng cảm biến vì ba nhóm lý do: chi phí cao so với kiểm tra định kỳ ⟦@EBB69J4F⟧; việc tiếp cận khó, có khi phải dừng sản xuất ⟦@QMVQCEL5⟧ (tr. 3, 5); và tín hiệu chịu biến đổi do vận hành và nhiệt độ ⟦45⟧, ⟦@38FMATHE⟧. Trong các tài liệu đã rà soát, nghiên cứu về theo dõi trạng thái và hỗ trợ kiểm tra – bảo trì cho loại công trình này còn ít. Từ đó, luận án đặt một yêu cầu: ở nhà xưởng, cả tín hiệu cảm biến lẫn kết quả kiểm tra của kỹ sư cần được ghi thành bằng chứng có nguồn gốc, độ bất định và phạm vi hiệu lực, gắn với cấu kiện và với hành động xử lý.

''')

s13 = s13.replace('## 1.3. Bằng chứng trạng thái và ba câu hỏi của người quản lý', '## 1.3. Bằng chứng trạng thái và nhu cầu của người quản lý')
s13 = s13.replace('(Mục 1.2.3)', '(Mục 1.2.1)')
s13 = s13.replace('Ba câu hỏi quy về một câu hỏi quản lý trung tâm có yếu tố thời gian: tại thời điểm quyết định, bằng chứng nào còn phù hợp làm căn cứ, ai đã sử dụng và vì sao?',
                  'Ba câu hỏi quy về một câu hỏi quản lý trung tâm có yếu tố thời gian: tại thời điểm quyết định, bằng chứng nào được dùng, bằng chứng đó có còn phù hợp không, ai dùng với vai trò gì, và vì sao trạng thái hành động thay đổi?')
s13 = s13.replace('Một bằng chứng phù hợp khi được tạo có thể không còn phù hợp sau một lần can thiệp lên liên kết, nên câu trả lời phải đọc được từ hồ sơ tại đúng thời điểm của quyết định.',
                  'Một bằng chứng hợp lệ tại thời điểm t1 có thể không còn phù hợp tại thời điểm t2, sau khi kết cấu được can thiệp, cảm biến được dời hoặc điều kiện lắp đặt thay đổi. Câu trả lời vì vậy phải đọc được từ hồ sơ tại đúng thời điểm của quyết định.')

s14 = C('''## 1.4. Vấn đề nghiên cứu

Vấn đề nghiên cứu xuất phát từ sự không liên tục giữa dữ liệu kỹ thuật và thông tin quản lý, và được phát biểu như sau:

> Một kết quả từ dữ liệu dao động chỉ có giá trị như một căn cứ quản lý khi được tổ chức thành bằng chứng trạng thái có nguồn gốc, độ bất định và phạm vi hiệu lực. Các thuộc tính đó phải được bảo toàn, được kiểm tại thời điểm sử dụng và truy vết được qua cấu kiện, hồ sơ kiểm tra và lịch sử hành động. Hiện nay, thông tin giám sát, kiểm tra và bảo trì tồn tại song song nhưng chưa được nối thành chuỗi như vậy.

Vấn đề có ba mặt nối tiếp nhau, không phải ba bài toán độc lập. Mặt thứ nhất là tạo ra bằng chứng có phạm vi hiệu lực. Theo dõi trạng thái kết cấu bằng dữ liệu dao động đã có nền nghiên cứu rộng; riêng Jia và Li tổng hợp 337 công bố về học sâu trong lĩnh vực này ⟦13⟧. Áp dụng thêm một mô hình phân loại vì vậy không tự tạo thành khoảng trống. Với kết cấu có liên kết, kết quả phụ thuộc vào lần lắp ráp ⟦18⟧ và vào cách chia dữ liệu khi đánh giá ⟦19⟧, ⟦20⟧. Bằng chứng kỹ thuật vì vậy phải mang theo điều kiện đã đánh giá của chính nó (KT1).

Mặt thứ hai là bảo toàn và kiểm bằng chứng khi nó được sử dụng. Các nghiên cứu đã nối cảm biến với BIM, gắn hồ sơ kiểm tra với cấu kiện và đồng bộ tài sản sang hệ quản lý bảo trì (Chương 4). Tích hợp cảm biến – BIM vì vậy khác với truy vết bằng chứng. Câu hỏi còn lại là hệ thống có phát hiện được khi bằng chứng bị dùng ngoài điều kiện đã đánh giá, hoặc khi một bước chuyển trạng thái thiếu căn cứ hay không. Từng phần của câu hỏi này đã có tiền lệ: ràng buộc ngữ nghĩa phát hiện vi phạm trong liên kết xuyên miền ⟦21⟧, lược đồ IFC mở rộng được kiểm bằng ca vi phạm cố ý ⟦2⟧, nguồn gốc dữ liệu được ghi trong trao đổi thông tin xây dựng ⟦16⟧ và khung kiểm định công trình có chuyên gia rà soát ⟦17⟧ (KT2). Ở Việt Nam, quy định về bảo trì công trình và yêu cầu cập nhật mô hình BIM phục vụ vận hành (Mục 1.1.2) tạo nhu cầu ghi được căn cứ của từng quyết định kiểm tra – bảo trì trong hồ sơ số.

Mặt thứ ba là duy trì chuỗi đó trong vận hành thực. Trên nhà xưởng, dữ liệu hư hỏng có nhãn khó thu, số cảm biến bị giới hạn bởi chi phí và khả năng tiếp cận, còn cầu trục và nhiệt độ làm thay đổi tín hiệu (Mục 1.2.2). Việc duy trì và truy ngược chuỗi trên công trình thật vì vậy cần được kiểm chứng riêng (KT3). Ba mặt nối với nhau qua cùng một bản ghi bằng chứng (Hình 1.1) và cùng phục vụ câu hỏi quản lý trung tâm ở Mục 1.3. Chương 5 phát biểu ba khoảng trống tương ứng (Mục 5.2).

![](../figures/Hinh_1_1_Chuoi_nghien_cuu_tong_the.png)

<span id="TLTQ_Hinh_1_1" class="anchor"></span>Hình 1.1. Chuỗi nghiên cứu tổng thể

## 1.5. Mục tiêu, phạm vi và phương pháp tổng quan

### 1.5.1. Mục tiêu và phạm vi của tiểu luận

Tiểu luận hệ thống hóa và tổng hợp có chọn lọc cơ sở lý luận cùng bằng chứng nghiên cứu về chuỗi thông tin từ dữ liệu dao động tới bằng chứng trạng thái, cấu kiện trong mô hình thông tin, bản ghi kiểm tra và trạng thái hành động. Các mắt xích được rà soát theo chương: quản lý tài sản, BIM/IFC và song sinh số trong vận hành (Chương 2); dữ liệu dao động và bằng chứng trạng thái (Chương 3); truy vết bằng chứng và hỗ trợ hành động kiểm tra – bảo trì (Chương 4). Chương 3 và Chương 4 còn trình bày phương pháp dự kiến của luận án cho ba mục tiêu. Chương 5 tách phần các nghiên cứu đã giải quyết khỏi phần còn lại, xác lập khoảng trống và thiết kế nghiên cứu. Tiểu luận trình bày thiết kế và công cụ của thực nghiệm; kết quả thực nghiệm thuộc các chuyên đề và chương tiếp theo của luận án.

Khách thể nghiên cứu là nhà công nghiệp khung thép có liên kết bu lông trong giai đoạn vận hành. Đối tượng nghiên cứu gồm trạng thái liên kết bu lông xét qua dữ liệu dao động, bằng chứng trạng thái tạo từ dữ liệu đó, và chuỗi bằng chứng – kiểm tra – hành động trong mô hình thông tin công trình.

Phạm vi không gian gồm phòng thí nghiệm và hai nhà xưởng đang khai thác. Mô hình khung thép tỉ lệ 1:10 trong phòng thí nghiệm được thiết kế theo khung một nhà xưởng ở tỉnh Khánh Hòa và cho phép tạo các trạng thái liên kết có kiểm soát (Mục tiêu 1). Mô hình này không được dùng để chứng minh tương tự động lực học với nhà xưởng, và kết quả định lượng trên mô hình không được chuyển sang công trình thật (Mục 3.4.1). Mô hình BIM và hồ sơ kiểm định cũ của nhà xưởng ở Khánh Hòa là nền đánh giá mô hình thông tin (Mục tiêu 2). Nhà xưởng thứ hai ở tỉnh Đắk Lắk (địa bàn tỉnh Phú Yên cũ), đã có mô hình BIM, là nơi triển khai và kiểm chứng khả năng duy trì chuỗi (Mục tiêu 3). Môi trường ven biển làm tăng nguy cơ ăn mòn liên kết (Mục 1.2.1); điều kiện môi trường thực tế của từng nhà xưởng sẽ được ghi khi khảo sát như một phần bối cảnh vận hành, và luận án không đo tác động của ăn mòn. Phạm vi thời gian là giai đoạn vận hành; quan trắc hiện trường dự kiến kéo dài 3–6 tháng. Các nội dung ngoài phạm vi được nêu ở Mục 5.7.

''')

new = head + intro + s111 + s112 + s12 + s13 + s14 + s152
open(f, 'w', encoding='utf-8', newline='').write(new)
print('ok', len(t.split()), '->', len(new.split()))
