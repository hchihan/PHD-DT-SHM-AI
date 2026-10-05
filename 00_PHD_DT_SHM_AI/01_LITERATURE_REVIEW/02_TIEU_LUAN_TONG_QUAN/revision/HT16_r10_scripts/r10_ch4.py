# -*- coding: utf-8 -*-
"""HT16 r10 – Chương 4 sắp lại theo trình tự: yêu cầu thông tin → định danh → thời gian → ràng buộc, câu hỏi năng lực → hỗ trợ hành động → phương pháp kiểm chứng; công cụ đặt cuối."""
import os, sys
sys.stdout.reconfigure(encoding='utf-8')
ROOT = r'H:\My Drive\03_RESEARCH\01_PHD_DT_AI_AM\00_PHD_DT_STEEL_INSPECTION_2026_2029_LIMITED_FEM\01_LITERATURE_REVIEW\03_OUTPUTS\01_TIEU_LUAN_TONG_QUAN\tieuluan'
def C(s): return s.replace('⟦', '\\[').replace('⟧', '\\]')
f = os.path.join(ROOT, '04_chuong4.md'); t = open(f, encoding='utf-8').read()
def cut(a, b=None):
    i = t.index(a); j = len(t) if b is None else t.index(b, i); return t[i:j]

head = cut('# CHƯƠNG 4.', 'Chương này xét lớp thông tin')
s41_tab = cut('Liên kết, tích hợp, trực quan hóa và truy vết', 'Trong tiểu luận, truy vết là khả năng')
s41_p = cut('Trong tiểu luận, truy vết là khả năng', '## 4.2.')
s42_p1 = cut('Liên kết dữ liệu cảm biến với BIM đã được thực hiện', 'Quan hệ cảm biến – cấu kiện và quan hệ bằng chứng')
s42_p2 = cut('Quan hệ cảm biến – cấu kiện và quan hệ bằng chứng', '## 4.3.')
s43 = cut('Li và cộng sự cung cấp một ví dụ rõ', '## 4.4.')
s44_p1 = cut('Nguồn gốc dữ liệu mô tả một bản ghi được tạo từ đâu', 'Một chuỗi dữ liệu có thể tồn tại về cấu trúc')
s44_p2 = cut('Một chuỗi dữ liệu có thể tồn tại về cấu trúc', '## 4.5.')
s45 = cut('Các nghiên cứu theo dõi dài hạn trên công trình thực', '## 4.6.')
hinh41 = cut('Chuỗi định danh lõi được trình bày ở Hình 4.1.', 'Chuỗi này là cách trình bày cho người đọc.')
workflow = cut('Về nghiệp vụ, chuỗi mà RQ2 cần truy ngược', 'Bốn nguyên tắc giữ cho chuỗi')
b0b1 = cut('Bước thứ tư dựng hai đối chứng trên cùng BIM.', 'Bước thứ năm đo bốn chỉ số')
tong_hop_tab = cut('Bảng 4.2 tổng hợp các dòng nghiên cứu chính', 'Các thành phần kỹ thuật này đã tương đối trưởng thành')

s44_p2 = s44_p2.replace('Luận án kiểm chuỗi bằng năm ràng buộc viết bằng Python (Phụ lục B); kết hợp với IDS là hướng mở rộng.',
                        'Luận án kiểm chuỗi bằng năm ràng buộc (Mục 4.6.2, Phụ lục B); kết hợp với IDS là hướng mở rộng.')
s44_p2 = s44_p2.replace('Theo cùng hướng, một mô hình dữ liệu cần chứng minh cả hai điều:', 'Theo cùng hướng, một mô hình dữ liệu cần được kiểm ở cả hai phía:')
s45 = s45.replace('Luận án dùng cùng nguyên tắc cho kiểm tra – bảo trì: vai trò người kiểm tra, người phê duyệt, người thực hiện và người xác minh được ghi tại từng sự kiện.',
                  'Luận án dùng cùng nguyên tắc cho kiểm tra – bảo trì: chủ thể và vai trò của người kiểm tra, người phê duyệt, người thực hiện và người xác minh được ghi tại từng sự kiện.')
s45 = s45.replace('Giá trị của hệ thống nằm ở việc làm cho quyết định minh bạch, có căn cứ và truy ngược được.',
                  'Giá trị của hệ thống nằm ở việc làm cho quyết định minh bạch, có căn cứ và truy ngược được. Trong luận án, bốn mức ưu tiên Bình thường → Theo dõi → Kiểm tra → Kiểm tra ưu tiên là logic hỗ trợ quyết định bằng luật minh bạch. Con người rà soát bằng chứng, phê duyệt, kiểm tra, chẩn đoán và cho phép hành động; AI không tự quyết định kiểm tra hay bảo trì.')

new = head + C('''Chương này xét lớp thông tin của chuỗi: bằng chứng kỹ thuật được liên kết với cấu kiện, hồ sơ kiểm tra và trạng thái hành động theo cách nào để người quản lý truy xuất và kiểm lại được căn cứ của một quyết định. Các mục 4.1 đến 4.5 tổng quan nghiên cứu và chuẩn theo trình tự mà một mô hình truy vết cần: phân biệt các mức liên kết, yêu cầu thông tin và định danh, bằng chứng theo thời gian, ràng buộc toàn vẹn cùng câu hỏi năng lực, và hỗ trợ hành động. Mục 4.6 trình bày phương pháp kiểm chứng của Mục tiêu 2; công cụ hiện thực được đặt ở cuối mục.

## 4.1. Từ liên kết dữ liệu đến truy vết kiểm chứng được

''') + s41_tab + s41_p + C('''Tích hợp cảm biến – BIM vì vậy chưa phải truy vết bằng chứng. Tích hợp trả lời câu hỏi dữ liệu nằm ở cấu kiện nào; truy vết còn phải trả lời bằng chứng được tạo trong điều kiện nào, được dùng cho quyết định nào và bởi ai.

## 4.2. Yêu cầu thông tin và mô hình định danh

Yêu cầu thông tin của chuỗi xuất phát từ phía quản lý tài sản, không suy ra được từ mô hình thiết kế ⟦24⟧. Với bài toán của luận án, yêu cầu đó là các câu hỏi của người quản lý ở Mục 1.3. Mô hình định danh phải cho phép trả lời các câu hỏi này mà không dựa vào tên gọi thủ công.

''') + s42_p1 + s42_p2 + C('''## 4.3. Bằng chứng theo thời gian và hồ sơ kiểm tra

''') + s43 + s44_p1 + C('''Tính thời gian là điểm cần nhấn mạnh. Một bằng chứng có thể hợp lệ tại thời điểm t1 nhưng không còn phù hợp tại thời điểm t2, sau khi kết cấu được can thiệp, ánh xạ cảm biến thay đổi hoặc điều kiện lắp đặt khác đi. Truy vết vì vậy phải cho phép đọc lại quan hệ giữa các bản ghi tại đúng thời điểm của một quyết định.

## 4.4. Ràng buộc toàn vẹn và câu hỏi năng lực

''') + s44_p2 + C('''Ngoài ràng buộc, một mô hình truy vết cần được kiểm bằng các câu hỏi mà nó phải trả lời được. Tiểu luận gọi đó là câu hỏi năng lực (competency questions). Mỗi câu hỏi năng lực có đáp án chuẩn lập trước, nên mô hình được đánh giá bằng việc trả lời đúng và đủ, không chỉ bằng việc lưu được dữ liệu. Bộ câu hỏi của luận án được nêu ở Mục 4.6.2.

## 4.5. Hỗ trợ hành động kiểm tra – bảo trì

''') + s45 + C('''## 4.6. Phương pháp kiểm chứng cho Mục tiêu 2

Các mục 4.1 đến 4.5 cho thấy những gì đã có và những gì truy vết bằng chứng còn cần. Mục này trình bày phương pháp dự kiến của Mục tiêu 2 theo trình tự: thực thể và quan hệ, quy tắc thời gian, ràng buộc và câu hỏi năng lực, thiết kế kiểm chứng, rồi ánh xạ hiện thực và công cụ.

### 4.6.1. Thực thể, quan hệ và chuỗi nghiệp vụ

''') + hinh41 + C('''Chuỗi này là cách trình bày cho người đọc. Mô hình dữ liệu là một đồ thị gồm năm thực thể: cấu kiện, cảm biến, bằng chứng trạng thái, bản ghi kiểm tra và hành động. Hai quan hệ có thuộc tính riêng là ánh xạ cảm biến – cấu kiện có khoảng hiệu lực và sử dụng bằng chứng. Sự kiện chuyển trạng thái là một loại bản ghi sự kiện; trạng thái xử lý của hành động được suy ra từ sự kiện mới nhất (Bảng A.1). Bản ghi bằng chứng không bị sửa đè; bản ghi mới thay bản cũ bằng một quan hệ trỏ về bản cũ.

Ba kiểu quan hệ cần được phân biệt rõ. Quan hệ cảm biến – cấu kiện cho biết cảm biến phục vụ khu vực hoặc cấu kiện nào trong một khoảng thời gian. Quan hệ bằng chứng – cấu kiện cho biết bằng chứng được tạo từ bối cảnh quan trắc của khu vực hoặc cấu kiện nào; đây không phải quan hệ chỉ vị trí hư hỏng. Quan hệ giữa bản ghi kiểm tra và phát hiện thực tế là nơi kỹ sư xác nhận vị trí và tình trạng hư hỏng sau kiểm tra. Nhờ vậy, mô hình không cho phép hiểu rằng AI từ dữ liệu cảm biến đã xác định chính xác vị trí hư hỏng.

''') + workflow + C('''### 4.6.2. Quy tắc thời gian, ràng buộc toàn vẹn và câu hỏi năng lực

Ba quy tắc giữ cho chuỗi trả lời được câu hỏi trung tâm ở Mục 1.3. Thứ nhất, mỗi bản ghi kiểm tra và mỗi sự kiện chuyển trạng thái ghi mã chủ thể, tức người hoặc tổ chức thực hiện, cùng vai trò của chủ thể đó tại thời điểm thực hiện, lý do và bằng chứng làm căn cứ. Chỉ ghi vai trò thì không phân biệt được hai kỹ sư cùng vai trò. Thứ hai, thời điểm can thiệp vật lý được tách khỏi thời điểm xác minh hồ sơ. Khi một hành động can thiệp lên liên kết được thực hiện, bằng chứng và đường cơ sở gắn với đợt lắp đặt trước phải được rà soát hoặc tạm ngừng dùng làm căn cứ kể từ thời điểm can thiệp; bước xác minh sau sửa chữa xác nhận điều kiện mới. Thứ ba, phạm vi hiệu lực là trường bắt buộc của bằng chứng và được kiểm tự động tại lần sử dụng. Lý do ghi kèm khi dùng bằng chứng ngoài phạm vi chỉ làm cho ngoại lệ truy ngược được. Nó không xác nhận giá trị kỹ thuật của bằng chứng và không tự cho phép can thiệp, vì quyết định can thiệp cần căn cứ kiểm tra phù hợp được người có thẩm quyền xác nhận.

Năm ràng buộc kiểm tính toàn vẹn của dữ liệu: bản ghi mồ côi, ánh xạ đã hết hiệu lực tại thời điểm đo, bằng chứng dùng ngoài phạm vi mà không có lý do, bước chuyển trạng thái không căn cứ hoặc sai vai trò, và căn cứ đã bị thay thế (Phụ lục B). Việc cảm biến có thực sự được lắp ở cấu kiện đã khai báo được kiểm bằng hồ sơ lắp đặt và đối chiếu tại hiện trường (Mục 3.5).

Câu hỏi năng lực là thành phần trung tâm của phép kiểm chứng. Bộ câu hỏi dự kiến gồm các loại sau: bằng chứng E sinh từ cảm biến nào; cảm biến đó được ánh xạ tới cấu kiện nào tại thời điểm E được tạo; E có còn nằm trong phạm vi hiệu lực tại thời điểm được dùng không; bản ghi kiểm tra nào được tạo từ E; ai đã đổi trạng thái hành động, với vai trò gì tại thời điểm đổi; bằng chứng và lý do nào làm căn cứ; và sau một can thiệp, bằng chứng hoặc đường cơ sở nào không còn được dùng. Bộ câu hỏi cùng đáp án chuẩn được khóa trước lần hiện thực cuối và sẽ được xác nhận qua phỏng vấn người quản lý kiểm tra – bảo trì phía chủ đầu tư.

### 4.6.3. Thiết kế kiểm chứng

Kiểm chứng so sánh ba phương án trên cùng BIM của nhà xưởng ở Khánh Hòa. Phương án B0 là bộ hồ sơ kiểm định hiện có, phân tán, của chính công trình nghiên cứu. Phương án B1 biểu diễn chuỗi bằng các khả năng sẵn có của IFC và BCF. Phương án đề xuất bổ sung truy vết bằng chứng có phạm vi hiệu lực cùng các quy tắc kiểm toàn vẹn ở Mục 4.6.2.

''') + b0b1.replace('Bước thứ tư dựng hai đối chứng trên cùng BIM. ', '') + C('''Ba phương án được so sánh theo năm khía cạnh, không theo nhận xét chung "tốt hơn". Mức đầy đủ được đo bằng M1, tỉ lệ trường bắt buộc có giá trị. Tính đúng và toàn vẹn được đo bằng M2, tỉ lệ phát hiện lỗi chèn mù theo từng nhóm lỗi. Khoảng 30 lỗi do một người không tham gia thiết kế chèn vào cả ba phương án; bộ thử có cả các bản ghi hợp lệ không chèn lỗi để đo việc báo lỗi nhầm. Khả năng truy vết được đo bằng M3: câu trả lời cho mỗi câu hỏi năng lực trước hết được chấm đúng và đủ theo đáp án chuẩn, sau đó mới so thời gian hoặc số bước. Công sức được đo bằng M4, số phút ghi nhận mỗi bản ghi. M3 và M4 được đọc cùng nhau: giá trị thực tiễn là việc tìm đúng căn cứ thuận lợi hơn bao nhiêu, đổi lại công sức ghi nhận tăng thêm bao nhiêu.

Dữ liệu thử gồm hồ sơ kiểm định cũ được mã hóa tay và các bản ghi bằng chứng của Mục tiêu 1 (Mục 3.4.3). Bằng chứng từ mô hình 1:10 khi đặt lên BIM nhà xưởng chỉ là ca kiểm thử quy tắc, không phải căn cứ hợp lệ cho quyết định tại nhà xưởng. Bộ ca thử vì vậy cần có cả ca trong và ngoài phạm vi hiệu lực. Quy tắc mã hóa B0, đặc tả B1, danh sách lỗi cùng các ca hợp lệ, bộ câu hỏi năng lực kèm đáp án chuẩn và cách tính chỉ số được khóa và lưu có phiên bản trước lần đo đầu tiên. Khi bộ ca chưa được khóa, tiểu luận không nêu kết quả dự kiến của M2.

Kết quả cần đạt là một lớp dữ liệu truy vết và bộ công cụ kiểm cho phép người quản lý trả lời các câu hỏi năng lực, trước hết là truy ngược căn cứ và người chịu trách nhiệm của từng quyết định. Phần quy cho đóng góp là chênh lệch so với B1. Chênh lệch so với B0 mô tả khoảng cách với bộ hồ sơ của công trình nghiên cứu, chưa đại diện cho thực hành kiểm định chung.

### 4.6.4. Ánh xạ hiện thực và công cụ

Mô hình là một lớp dữ liệu truy vết liên thông với IFC 4.3 theo cách dùng của ⟦35⟧ và với BCF 3.0. Dữ liệu được lưu trong cơ sở dữ liệu riêng và được ánh xạ sang thực thể, quan hệ chuẩn khi xuất (Bảng A.3); luận án không thêm thực thể hay sửa lược đồ IFC. Bảng ánh xạ là phương án biểu diễn, chưa chứng minh dữ liệu được bảo toàn khi trao đổi. Việc khóa định danh và liên kết có còn nguyên sau khi xuất rồi đọc lại hay không sẽ được kiểm bằng một phép xuất – nhập trên chính dữ liệu thử.

Các công cụ dưới đây là môi trường hiện thực và tham chiếu, không phải đóng góp khoa học. Mô hình BIM của nhà xưởng ở Khánh Hòa được dựng và quản lý trong Revit, rồi xuất sang IFC 4.3; IfcOpenShell được dùng để đọc và ghi tệp IFC. Vấn đề và lịch sử trạng thái được biểu diễn theo BCF 3.0 ⟦@K5SGFIGW⟧. Các bản ghi được lưu trong SQLite. Năm ràng buộc và logic hỗ trợ hành động bốn mức được viết bằng Python, dưới dạng luật minh bạch để mỗi mức ưu tiên truy được về luật đã áp dụng. Phần này không dùng mô hình AI.

## 4.7. Tổng hợp chương

''') + tong_hop_tab + C('''Các thành phần kỹ thuật này đã tương đối trưởng thành nhưng thường được phát triển trong những hệ thống hoặc cho những mục tiêu riêng. Chương 4 cung cấp ba nhận định cho Chương 5. Thứ nhất, bằng chứng kỹ thuật cần giữ nguồn gốc và phạm vi hiệu lực khi đi vào hệ thống thông tin. Thứ hai, giá trị nghiên cứu nằm ở tính liên tục, tính thời gian và khả năng kiểm chứng của quan hệ, không ở bản thân việc tích hợp. Thứ ba, hỗ trợ hành động phải duy trì căn cứ cùng lịch sử rà soát, còn quyết định thuộc người có trách nhiệm.
''')
open(f, 'w', encoding='utf-8', newline='').write(new)
print('ok', len(t.split()), '->', len(new.split()))
