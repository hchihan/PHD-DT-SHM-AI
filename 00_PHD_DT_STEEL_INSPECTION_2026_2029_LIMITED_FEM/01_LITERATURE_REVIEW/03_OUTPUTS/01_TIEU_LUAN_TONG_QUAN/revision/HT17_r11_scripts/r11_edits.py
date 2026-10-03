# -*- coding: utf-8 -*-
"""HT17 r10 -> r11: hoàn thiện theo góp ý vòng 2 + kỷ luật viết (strict-writing-discipline)."""
import os, sys, json
sys.stdout.reconfigure(encoding='utf-8')
ROOT = r'H:\My Drive\03_RESEARCH\01_PHD_DT_AI_AM\00_PHD_DT_STEEL_INSPECTION_2026_2029_LIMITED_FEM\01_LITERATURE_REVIEW\03_OUTPUTS\01_TIEU_LUAN_TONG_QUAN\tieuluan'
def C(s): return s.replace('⟦', '\\[').replace('⟧', '\\]')
files, log = {}, []
def get(f):
    if f not in files: files[f] = open(os.path.join(ROOT, f), encoding='utf-8').read()
    return files[f]
def R(f, old, new, tag):
    t = get(f); old, new = C(old), C(new); n = t.count(old); assert n == 1, f'{f} [{tag}] {n}: {old[:90]}'
    files[f] = t.replace(old, new); log.append({'tep': f, 'nhom': tag, 'truoc': old, 'sau': new})
def S(f, start, end, new, tag):
    t = get(f); i = t.index(C(start)); j = len(t) if end is None else t.index(C(end), i)
    log.append({'tep': f, 'nhom': tag, 'truoc': t[i:j], 'sau': C(new)}); files[f] = t[:i] + C(new) + t[j:]

# ================= Dẫn nhập (rút gọn, thêm câu đóng góp) =================
R('00_dannhap.md', 'Theo đánh giá của phần tổng quan nghiên cứu này, khó khăn hiện nay nằm ở các điểm nối giữa những thành phần đó, nhiều hơn ở từng thành phần riêng lẻ.',
  'Tiểu luận nhận định rằng khó khăn nằm ở các điểm nối giữa những thành phần đó, nhiều hơn ở từng thành phần riêng lẻ.', 'TQ')
R('00_dannhap.md', 'cảm biến, AI, BIM và song sinh số là công cụ.',
  'cảm biến, AI, BIM và song sinh số là công cụ. Đóng góp chính của luận án nằm ở quản trị vòng đời của bằng chứng kỹ thuật, từ lúc được tạo ra đến lúc được dùng làm căn cứ cho hành động kiểm tra – bảo trì.', 'TQ')
S('00_dannhap.md', 'Kết quả là ba khoảng trống nối tiếp nhau', 'Tiểu luận gồm năm chương.',
  'Kết quả là ba khoảng trống nối tiếp nhau trên cùng một chuỗi. KT1 là hiệu lực của bằng chứng tạo từ dữ liệu dao động. KT2 là truy vết bằng chứng tới hành động có trách nhiệm; phần này khác với việc tích hợp cảm biến vào BIM. KT3 là khả thi của việc duy trì chuỗi đó trong vận hành nhà công nghiệp khung thép. Ba mục tiêu tương ứng dùng ba môi trường: mô hình khung thép 1:10 trong phòng thí nghiệm, mô hình thông tin trên BIM của một nhà xưởng ở Khánh Hòa, và một nhà xưởng đang khai thác ở Đắk Lắk. Quyết định kiểm tra và bảo trì thuộc về kỹ sư và người có thẩm quyền; AI chỉ tạo bằng chứng.\n\n', 'TQ')

# ================= Chương 1 =================
R('01_chuong1.md', 'Theo đánh giá của phần tổng quan nghiên cứu này, mức chuyển đổi số trong vận hành nên được đo bằng',
  'Tiểu luận vì vậy đề xuất đo mức chuyển đổi số trong vận hành bằng', 'CT')
R('01_chuong1.md', 'Theo đánh giá của phần tổng quan nghiên cứu này, hậu quả của một sự cố kết cấu ở nhà xưởng gồm cả thời gian dừng sản xuất, không chỉ chi phí sửa chữa.',
  'Từ hai nguồn này, tiểu luận suy ra rằng hậu quả của một sự cố kết cấu ở nhà xưởng gồm cả chi phí sửa chữa lẫn thời gian dừng sản xuất.', 'CT')
R('01_chuong1.md', 'Theo đánh giá của phần tổng quan nghiên cứu này, một nhận định về liên kết vì vậy chỉ có giá trị',
  'Tiểu luận rút ra từ ba nhóm yếu tố này rằng một nhận định về liên kết chỉ có giá trị', 'CT')
R('01_chuong1.md', 'Theo đánh giá của phần tổng quan nghiên cứu này, mất lực siết không kèm dấu hiệu hình học còn khó phát hiện bằng mắt hơn,',
  'Mất lực siết không kèm dấu hiệu hình học còn khó phát hiện bằng mắt hơn (suy luận của tiểu luận),', 'CT')
R('01_chuong1.md', 'Vấn đề có ba mặt nối tiếp nhau, không phải ba bài toán độc lập.', 'Vấn đề có ba mặt nối tiếp nhau trên cùng một chuỗi.', 'TQ')
R('01_chuong1.md', 'Mô hình này không được dùng để chứng minh tương tự động lực học với nhà xưởng, và kết quả định lượng trên mô hình không được chuyển sang công trình thật (Mục 3.4.1).',
  'Mô hình này tạo bằng chứng phòng thí nghiệm. Tương tự động lực học với nhà xưởng nằm ngoài phạm vi kiểm chứng, và kết quả định lượng trên mô hình không được chuyển sang công trình thật (Mục 3.4.1).', 'SHM')

# ================= Chương 2 =================
R('02_chuong2.md', 'Dữ liệu trạng thái vì vậy cần được đặt trong bối cảnh thời gian và vận hành thay vì được đọc như một chỉ báo vật lý độc lập, và lịch sử kiểm tra, sửa chữa cùng các thay đổi vận hành là thông tin cần được duy trì cùng hồ sơ tài sản.',
  'Dữ liệu trạng thái vì vậy cần được đọc cùng thời điểm và điều kiện vận hành đã tạo ra nó. Lịch sử kiểm tra, sửa chữa và các thay đổi vận hành cần được duy trì cùng hồ sơ tài sản.', 'CT')
R('02_chuong2.md', 'Theo đánh giá của phần tổng quan nghiên cứu này, trong IFC4 cả yêu cầu hành động lẫn lịch sử đo đều là lớp con của `IfcControl`,',
  'Đối chiếu đặc tả IFC4, tiểu luận nhận thấy cả yêu cầu hành động lẫn lịch sử đo đều là lớp con của `IfcControl`,', 'BIM')
R('02_chuong2.md', 'Năng lực mà hệ thống thực sự đạt được được đánh giá sau triển khai theo các khung của ⟦9⟧, ⟦10⟧.',
  'Năng lực mà hệ thống đạt được sẽ được đánh giá sau triển khai theo các khung của ⟦9⟧, ⟦10⟧. Song sinh số vì vậy là kiến trúc đích của luận án; phần được kiểm chứng và quy cho đóng góp là chuỗi bằng chứng – hành động bên trong kiến trúc đó.', 'BIM')

# ================= Chương 3 =================
R('03_chuong3.md', 'LORO vì vậy đo khả năng khái quát sang lần chạy mới trong cùng đợt và cùng bối cảnh; nó không phải bằng chứng cuối cùng.',
  'LORO vì vậy đo khả năng khái quát sang lần chạy mới trong cùng đợt và cùng bối cảnh lắp đặt, và cần được đọc cùng LOCO.', 'SHM')
R('03_chuong3.md', 'Nếu kết quả LOCO thấp hơn LORO, điều đó cho thấy bằng chứng có phạm vi hiệu lực hẹp hơn, không phải thất bại của phép đánh giá. Cách đọc này quan trọng',
  'Nếu kết quả LOCO thấp hơn LORO, bằng chứng có phạm vi hiệu lực hẹp hơn, và chính phép đánh giá đã chỉ ra giới hạn đó. Cách đọc này cần thiết', 'SHM')
R('03_chuong3.md', 'Kết quả kiểm định là căn cứ để chấp nhận rằng mô hình học được tín hiệu, không phải thước đo độ bất định.',
  'Kết quả kiểm định là căn cứ để chấp nhận rằng mô hình học được tín hiệu; độ bất định được đo riêng bằng hai cơ chế trên.', 'SHM')
R('03_chuong3.md', 'có thể được kiểm tự động tại thời điểm bằng chứng được sử dụng, chứ không phải một ghi chú trong văn bản.',
  'có thể được kiểm tự động tại thời điểm bằng chứng được sử dụng.', 'SHM')
R('03_chuong3.md', '| Ba đợt đã thực hiện; đợt bổ sung dự kiến khi cần |', '| Ba đợt đã thực hiện |', 'SHM')
R('03_chuong3.md', 'Một đợt chỉ được đưa vào phép giữ lại đợt khi thỏa điều kiện so sánh đã khóa (Mục 3.4.3).',
  'Dữ liệu hiện có gồm ba đợt thí nghiệm; việc bổ sung dữ liệu, nếu phát sinh do lỗi kỹ thuật, sẽ được xử lý ngoài phạm vi của báo cáo tổng quan này.', 'SHM')
R('03_chuong3.md', 'Bảy điều kiện để đóng Gate 1 được nêu ở Mục 5.5; tại thời điểm viết tiểu luận, chưa đủ bằng chứng để coi các điều kiện đó đã được đáp ứng, nên tiểu luận không nêu kết quả.',
  'Kết quả của Mục tiêu 1 chỉ được sử dụng sau khi dữ liệu, cách chia theo đơn vị độc lập, quy trình tiền xử lý và đánh giá được kiểm soát để tránh rò rỉ và tái lập được (Gate 1). Chi tiết kỹ thuật thuộc Chuyên đề 1; tiểu luận không nêu kết quả.', 'SHM')

# ================= Chương 4 =================
R('04_chuong4.md', 'truy vết trong quản lý tài sản là truy vết theo thời gian, không chỉ là truy vấn quan hệ tại trạng thái hiện tại.',
  'truy vết trong quản lý tài sản là truy vết theo thời gian: nó phải dựng lại được quan hệ giữa các bản ghi tại một thời điểm đã qua.', 'BIM')
R('04_chuong4.md', 'nên mô hình được đánh giá bằng việc trả lời đúng và đủ, không chỉ bằng việc lưu được dữ liệu.',
  'nên mô hình được đánh giá bằng việc trả lời đúng và đủ các câu hỏi đó.', 'BIM')
R('04_chuong4.md', 'chuỗi hồ sơ vận hành được trong bối cảnh thật.', 'chuỗi hồ sơ vận hành được tại công trình thật.', 'CT')
R('04_chuong4.md', '⟦@63XPSMIR⟧; theo đánh giá của phần tổng quan nghiên cứu này, các ví dụ đó trộn', '⟦@63XPSMIR⟧. Tiểu luận nhận thấy các ví dụ đó trộn', 'BIM')
R('04_chuong4.md', 'đây không phải quan hệ chỉ vị trí hư hỏng.', 'vị trí hư hỏng nằm ở quan hệ thứ ba dưới đây.', 'BIM')
R('04_chuong4.md', 'Việc cảm biến có thực sự được lắp ở cấu kiện đã khai báo', 'Việc cảm biến có được lắp đúng ở cấu kiện đã khai báo hay không', 'CT')
R('04_chuong4.md', 'Bước đề nghị kiểm tra là phần mô hình sẽ đặc tả khi khóa Mục tiêu 2: ghi thành một loại hành động kiểm tra hay một bản ghi riêng, cùng vai trò và căn cứ bắt buộc. Khi bước này được đặc tả, câu hỏi "ai đã đề nghị kiểm tra, dựa vào bằng chứng nào" trở thành truy ngược được như các bước sau.',
  'Bước đề nghị kiểm tra sẽ được đặc tả chi tiết trong giai đoạn triển khai Mục tiêu 2; báo cáo tổng quan chỉ xác lập yêu cầu rằng bước này phải truy được về bằng chứng, chủ thể và vai trò.', 'BIM')
S('04_chuong4.md', 'Kiểm chứng so sánh ba phương án trên cùng BIM của nhà xưởng ở Khánh Hòa.', 'Ba phương án được so sánh theo năm khía cạnh',
  'Kiểm chứng so sánh ba phương án trên cùng BIM của nhà xưởng ở Khánh Hòa. Đối chứng B0 là 20–30 hồ sơ kiểm định cũ của chính nhà xưởng, đại diện cho thực hành tại công trình nghiên cứu. Đối chứng B1 là baseline dựa trên các khả năng của IFC 4.3 và BCF 3.0 đã được xác định từ các tiền lệ gần nhất trong tổng quan: chuỗi lần kiểm tra – hư hỏng – cấu kiện – nhiệm vụ bảo trì của ⟦35⟧, phép gán cảm biến cho cấu kiện của ⟦2⟧, lệnh bảo trì có trạng thái và phê duyệt của IFC4 ⟦@63XPSMIR⟧, và sự kiện đổi trạng thái của BCF ⟦@K5SGFIGW⟧, ⟦@P3ZIHF8G⟧ (Mục 2.2.2). Các ràng buộc chạy trên B1 ở dạng tương ứng với những trường B1 có. Phương án đề xuất bổ sung hai quy tắc: phạm vi hiệu lực là trường bắt buộc của bằng chứng và được kiểm tại lần dùng; mỗi bước chuyển trạng thái của hành động trỏ tới lần dùng bằng chứng làm căn cứ, kèm chủ thể và vai trò người thực hiện. Nhóm lỗi nào B1 phát hiện được bằng cơ chế sẵn có thì không được tính vào phần đóng góp.\n\n', 'BIM')
R('04_chuong4.md', 'Bằng chứng từ mô hình 1:10 khi đặt lên BIM nhà xưởng chỉ là ca kiểm thử quy tắc, không phải căn cứ hợp lệ cho quyết định tại nhà xưởng.',
  'Bằng chứng từ mô hình 1:10 khi đặt lên BIM nhà xưởng chỉ đóng vai ca kiểm thử quy tắc; nó không làm căn cứ cho quyết định tại nhà xưởng.', 'SHM')
R('04_chuong4.md', 'Bảng ánh xạ là phương án biểu diễn, chưa chứng minh dữ liệu được bảo toàn khi trao đổi.',
  'Bảng ánh xạ là phương án biểu diễn; nó chưa cho biết dữ liệu có được bảo toàn khi trao đổi hay không.', 'BIM')
R('04_chuong4.md', 'Các công cụ dưới đây là môi trường hiện thực và tham chiếu, không phải đóng góp khoa học.',
  'Các công cụ dưới đây là môi trường hiện thực và tham chiếu; đóng góp khoa học nằm ở các quy tắc và mô hình ở Mục 4.6.1–4.6.3.', 'BIM')

# ================= Chương 5 =================
R('05_chuong5.md', 'KT1 tạo ra bằng chứng có phạm vi hiệu lực; KT2 bảo toàn và kiểm bằng chứng đó khi được dùng; KT3 duy trì chuỗi trong vận hành thực.',
  'KT1 là hiệu lực của bằng chứng: bằng chứng được tạo kèm điều kiện đã đánh giá. KT2 là truy vết của bằng chứng: điều kiện đó được bảo toàn và kiểm khi bằng chứng được dùng. KT3 là khả thi hiện trường: chuỗi được duy trì trong vận hành thực.', 'TQ')
R('05_chuong5.md', 'Luận án kế thừa các nguyên tắc này; đánh giá chống rò rỉ không phải phần mới của luận án.',
  'Luận án kế thừa các nguyên tắc này như phương pháp có sẵn.', 'TQ')
R('05_chuong5.md', 'KT3 là khả thi của việc duy trì chuỗi, không phải kiểm chứng phát hiện hư hỏng ở hiện trường; phép thử dự kiến không có đủ dữ liệu hư hỏng cho câu hỏi đó.',
  'KT3 giới hạn ở khả thi của việc duy trì chuỗi. Hiệu năng phát hiện hư hỏng ở hiện trường cần dữ liệu hư hỏng mà phép thử dự kiến không có, nên nằm ngoài KT3.', 'TQ')
S('05_chuong5.md', '> Với nhà công nghiệp khung thép liên kết bu lông, kết quả rút từ dữ liệu dao động là căn cứ', 'Mục tiêu tổng quát của luận án',
  '> Với nhà công nghiệp khung thép liên kết bu lông, kết quả từ dữ liệu dao động chỉ trở thành căn cứ quản lý khi được tổ chức thành bằng chứng có nguồn gốc, độ bất định và phạm vi hiệu lực. Các thuộc tính đó phải được bảo toàn và kiểm tra khi bằng chứng được sử dụng, đồng thời truy vết được qua cấu kiện, hồ sơ kiểm tra và lịch sử hành động. Kết luận hư hỏng vẫn thuộc về kỹ sư sau kiểm tra.\n\n', 'TQ')
R('05_chuong5.md', '| Gate 1 | Phòng thí nghiệm, khung thép 1:10 | Hiệu năng ở ba mức đánh giá với điều kiện so sánh đã khóa; biến thiên theo seed và fold; bản ghi bằng chứng có điều kiện đã đánh giá |',
  '| Gate 1 (bằng chứng phòng thí nghiệm) | Phòng thí nghiệm, khung thép 1:10 | Hiệu năng ở ba mức đánh giá; bản ghi bằng chứng có điều kiện đã đánh giá |', 'CT')
R('05_chuong5.md', '| Gate 2–3 | Lớp dữ liệu truy vết', '| Gate 2–3 (mô hình truy vết và kiểm chứng) | Lớp dữ liệu truy vết', 'CT')
R('05_chuong5.md', '| Gate 4–5 | Nhà xưởng đang khai thác', '| Gate 4–5 (khả thi hiện trường, hỗ trợ quyết định) | Nhà xưởng đang khai thác', 'CT')
R('05_chuong5.md', '| Gate 5 | Lớp dữ liệu và hiện trường', '| Gate 5 (hỗ trợ quyết định) | Lớp dữ liệu và hiện trường', 'CT')
t5 = get('05_chuong5.md'); i = t5.index('> RQ2:'); j = t5.index('\n', i)
files['05_chuong5.md'] = t5[:i] + '> RQ2: Khi bằng chứng trạng thái được nối với cấu kiện BIM, hồ sơ kiểm tra và lịch sử hành động, người quản lý có truy ngược được bằng chứng đã dùng, tính phù hợp của bằng chứng tại thời điểm sử dụng và trách nhiệm của từng chủ thể hay không?' + t5[j:]
log.append({'tep': '05_chuong5.md', 'nhom': 'TQ', 'truoc': t5[i:j], 'sau': '(RQ2 rút gọn, chỉ số chuyển xuống 5.5)'})
R('05_chuong5.md', 'Xây dựng một lớp dữ liệu truy vết rồi đánh giá bằng so sánh với hai đối chứng trả lời RQ2 (Mục 4.6).',
  'Xây dựng một lớp dữ liệu truy vết rồi đánh giá bằng so sánh với hai đối chứng trả lời RQ2 (Mục 4.6); RQ2 được đo bằng câu hỏi năng lực (M3), tỉ lệ phát hiện lỗi chèn mù (M2), mức đủ thuộc tính (M1) và công sức ghi nhận (M4) trên BIM của nhà xưởng ở Khánh Hòa, so với B0 và B1.', 'CT')
S('05_chuong5.md', 'Mỗi gói công việc kết thúc ở một cổng kiểm chứng,', '## 5.6. Đóng góp dự kiến',
  'Mỗi gói công việc kết thúc ở một cổng kiểm chứng, tức điểm duyệt bằng chứng trước khi kết quả được dùng cho bước sau. Gate 1 xác nhận bằng chứng phòng thí nghiệm: kết quả của Mục tiêu 1 chỉ được dùng sau khi dữ liệu, cách chia theo đơn vị độc lập, quy trình tiền xử lý và đánh giá được kiểm soát để tránh rò rỉ và tái lập được. Gate 2–3 khóa và kiểm chứng mô hình truy vết. Gate 4–5 kiểm khả thi hiện trường và logic hỗ trợ quyết định. Chi tiết kỹ thuật của Gate 1 thuộc Chuyên đề 1.\n\n', 'SHM')
R('05_chuong5.md', 'là bằng chứng dùng để kiểm chứng đóng góp, không phải bản thân đóng góp.', 'chỉ là bằng chứng kiểm chứng đóng góp.', 'DG')
R('05_chuong5.md', '| Điều kiện đánh giá, nguồn gốc, độ bất định và phạm vi hiệu lực được ghi thành thuộc tính kiểm tra được của bằng chứng trạng thái; với dữ liệu dao động của khung thép liên kết bu lông, cấp đơn vị được giữ trọn khi chia dữ liệu quyết định phạm vi được phép dùng |',
  '| Bằng chứng trạng thái mang nguồn gốc, độ bất định và phạm vi hiệu lực, và các thuộc tính này được kiểm khi bằng chứng được sử dụng; với dữ liệu dao động của khung thép liên kết bu lông, cấp đơn vị được giữ trọn khi chia dữ liệu là một yếu tố quan trọng quyết định cách diễn giải phạm vi hiệu lực của kết quả |', 'DG')
R('05_chuong5.md', '| Bằng chứng chỉ được dùng trong phạm vi còn hiệu lực; can thiệp vật lý mở lại điều kiện dùng bằng chứng và đường cơ sở; mỗi bước chuyển trạng thái truy được chủ thể, vai trò, bằng chứng và lý do |',
  '| Mỗi lần dùng bằng chứng hoặc đổi trạng thái hành động truy được chủ thể, vai trò, thời điểm, bằng chứng và lý do; can thiệp vật lý làm phát sinh yêu cầu rà soát lại hiệu lực của bằng chứng và đường cơ sở trước đó |', 'DG')
R('05_chuong5.md', 'mô hình 1:10 cho phép tạo trạng thái liên kết có kiểm soát nhưng không chứng minh tương tự động lực học với nhà xưởng.',
  'mô hình 1:10 cho phép tạo trạng thái liên kết có kiểm soát; tương tự động lực học với nhà xưởng nằm ngoài phạm vi kiểm chứng.', 'SHM')
S('05_chuong5.md', 'Sau luận án, hướng nghiên cứu có thể mở rộng theo đối tượng', None,
  'Tiểu luận khép lại bằng ba nhận định. Thứ nhất, luận án giải quyết một bài toán quản lý thông tin: căn cứ của quyết định kiểm tra – bảo trì phải truy xuất và rà soát được qua thời gian. Thứ hai, đóng góp dự kiến nằm ở truy vết bằng chứng có phạm vi hiệu lực, từ lúc bằng chứng được tạo tới lúc được dùng cho hành động; AI và BIM là công cụ. Thứ ba, quyết định kiểm tra và bảo trì vẫn thuộc về kỹ sư và người có thẩm quyền.\n', 'TQ')

# ================= Thuật ngữ, Phụ lục =================
R('00_thuatngu.md', 'IFC 4.3 theo cách dùng của Bellon và cộng sự cùng BCF 3.0, dựng với đủ các khả năng sẵn có của hai chuẩn',
  'baseline dựa trên các khả năng của IFC 4.3 và BCF 3.0 xác định từ các tiền lệ gần nhất', 'BIM')
R('phuluc.md', 'được rà lại khi khóa đặc tả B1 với đủ khả năng của IFC 4.3 và BCF 3.0 (Mục 4.6.3)', 'được rà lại khi khóa đặc tả B1 (Mục 4.6.3)', 'BIM')
R('phuluc.md', 'Bước đề nghị kiểm tra, từ bằng chứng và mức ưu tiên tới quyết định mở một lần kiểm tra, chưa có loại bản ghi riêng trong Bảng A.1; loại bản ghi, vai trò và căn cứ của bước này được đặc tả khi khóa mô hình của Mục tiêu 2 (Mục 4.6.1).',
  'Bước đề nghị kiểm tra, từ bằng chứng và mức ưu tiên tới quyết định mở một lần kiểm tra, sẽ được đặc tả trong giai đoạn triển khai Mục tiêu 2 và phải truy được về bằng chứng, chủ thể và vai trò (Mục 4.6.1).', 'BIM')

for f, t in files.items():
    open(os.path.join(ROOT, f), 'w', encoding='utf-8', newline='').write(t)
json.dump(log, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'HT17_r11_edits.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('ok', len(log))
