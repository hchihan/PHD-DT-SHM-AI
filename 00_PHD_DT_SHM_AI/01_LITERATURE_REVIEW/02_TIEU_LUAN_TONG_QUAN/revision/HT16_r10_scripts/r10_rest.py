# -*- coding: utf-8 -*-
"""HT16 r10 – Chương 3, Dẫn nhập, Thuật ngữ, Chương 2, Phụ lục, RQ2: sửa có kiểm tra."""
import os, sys, json
sys.stdout.reconfigure(encoding='utf-8')
ROOT = r'H:\My Drive\03_RESEARCH\01_PHD_DT_AI_AM\00_PHD_DT_STEEL_INSPECTION_2026_2029_LIMITED_FEM\01_LITERATURE_REVIEW\03_OUTPUTS\01_TIEU_LUAN_TONG_QUAN\tieuluan'
def C(s): return s.replace('⟦', '\\[').replace('⟧', '\\]')
files, log = {}, []
def R(f, old, new, tag):
    if f not in files: files[f] = open(os.path.join(ROOT, f), encoding='utf-8').read()
    old, new = C(old), C(new); n = files[f].count(old); assert n == 1, f'{f} [{tag}] {n}: {old[:80]}'
    files[f] = files[f].replace(old, new); log.append({'tep': f, 'ma': tag, 'truoc': old, 'sau': new})

# ---------- Chương 3 ----------
R('03_chuong3.md', 'Cần tách hai vai trò: đơn vị chấm điểm là bản ghi, còn đơn vị được giữ trọn ở một phía của phép chia là lần chạy hoặc đợt, tùy mức đánh giá.',
  'Cần tách ba vai trò. Đơn vị chấm điểm là bản ghi. Đơn vị chia dữ liệu, tức đơn vị được giữ trọn ở một phía của phép chia, là lần chạy hoặc đợt, tùy mức đánh giá. Đơn vị độc lập vật lý là lần thiết lập trạng thái, vì các lần chạy trong cùng một lần thiết lập dùng chung một lần siết. Cửa sổ không phải mẫu độc lập.', 'TV2-B3')
R('03_chuong3.md', 'Kết quả LORO có giá trị trong cùng bối cảnh thí nghiệm; dùng cho đợt mới cần kết quả LOCO, và dùng cho công trình thực cần kiểm chứng riêng. Một kết quả LOCO thấp vẫn giữ giá trị trong cùng đợt và cho thấy phạm vi hiệu lực hẹp hơn.',
  'LORO vì vậy đo khả năng khái quát sang lần chạy mới trong cùng đợt và cùng bối cảnh; nó không phải bằng chứng cuối cùng. LOCO kiểm khả năng giữ hiệu năng khi đợt và bối cảnh lắp đặt thay đổi; dùng cho công trình thực vẫn cần kiểm chứng riêng. Nếu kết quả LOCO thấp hơn LORO, điều đó cho thấy bằng chứng có phạm vi hiệu lực hẹp hơn, không phải thất bại của phép đánh giá.', 'TV2-B4')
R('03_chuong3.md', 'Nguồn gốc dữ liệu (provenance) trả lời các câu hỏi cụ thể: dữ liệu đến từ cảm biến nào, lần chạy nào, được xử lý bằng chuỗi nào và kết quả được tạo dưới giao thức nào.',
  'Phạm vi hiệu lực vì vậy là thuộc tính bắt buộc của bằng chứng, có thể được kiểm tự động tại thời điểm bằng chứng được sử dụng, chứ không phải một ghi chú trong văn bản. Nguồn gốc dữ liệu (provenance) trả lời các câu hỏi cụ thể: dữ liệu đến từ cảm biến nào, đợt và lần chạy nào, được xử lý bằng phiên bản chuỗi xử lý nào, dùng mô hình và cấu hình nào, được đánh giá dưới giao thức nào, và được tạo vào thời điểm nào.', 'TV4-D1D2')
R('03_chuong3.md', 'Mục tiêu thứ hai là đánh giá khả năng nhận biết trạng thái liên kết của các mô hình AI theo đơn vị độc lập, tức là trên dữ liệu chưa tham gia huấn luyện.',
  'Mục tiêu thứ hai là đánh giá khả năng phân biệt các trạng thái liên kết có kiểm soát của các mô hình AI theo đơn vị độc lập, tức là trên dữ liệu chưa tham gia huấn luyện.', 'TV2-B2')
R('03_chuong3.md', '| Đối tượng thu nhỏ | Khung thép mô phỏng khung một nhà xưởng ở tỉnh Khánh Hòa theo tỉ lệ hình học 1:10;',
  '| Đối tượng thu nhỏ | Khung thép được thiết kế theo khung một nhà xưởng ở tỉnh Khánh Hòa với tỉ lệ hình học 1:10, để tạo trạng thái liên kết có kiểm soát; không dùng để suy ra ứng xử định lượng của nhà xưởng;', 'TV2-B1')
R('03_chuong3.md', 'Nhãn trạng thái chỉ vị trí can thiệp, không phải thang mức độ hư hỏng | Đã thực hiện |',
  'Nhãn trạng thái chỉ vị trí can thiệp đã biết, không phải mức độ hư hỏng hay mức lực siết. Vì lực siết không được đo, thí nghiệm kiểm khả năng phân biệt trạng thái can thiệp, không định lượng mức nới lỏng | Đã thực hiện |', 'TV2-B2')
R('03_chuong3.md', 'Thí nghiệm nhằm đo mức chênh lệch giữa các cách đánh giá, không nhằm tìm mô hình tốt nhất; một kết luận về mức chênh lệch đáng tin hơn khi nó lặp lại trên nhiều loại mô hình.',
  'Thí nghiệm không nhằm tìm mô hình AI tốt nhất. Mục đích là kiểm tra kết luận về giao thức đánh giá có phụ thuộc mạnh vào họ mô hình hay không; một kết luận về mức chênh lệch đáng tin hơn khi nó lặp lại trên nhiều loại mô hình.', 'TV2-B5')
R('03_chuong3.md', 'Cách so sánh các thiết kế đánh giá kế thừa từ',
  'Bảy điều kiện để đóng Gate 1 được nêu ở Mục 5.5; tại thời điểm viết tiểu luận, chưa đủ bằng chứng để coi các điều kiện đó đã được đáp ứng, nên tiểu luận không nêu kết quả. Cách so sánh các thiết kế đánh giá kế thừa từ', 'TV2-B6')
R('03_chuong3.md', 'chúng không là căn cứ cho quyết định tại nhà xưởng (Mục 4.6.2).', 'chúng không là căn cứ cho quyết định tại nhà xưởng (Mục 4.6.3).', 'TV5-ref')
R('03_chuong3.md', '## 3.5. Quan trắc hiện trường cho Mục tiêu 3', '## 3.5. Chiến lược tạo bằng chứng hiện trường cho Mục tiêu 3', 'TV5-F')
R('03_chuong3.md', 'Mục tiêu 3 kiểm chứng khả thi của chuỗi bằng chứng – hành động trên nhà xưởng', 'Mục tiêu 3 kiểm chứng khả năng duy trì chuỗi bằng chứng – hành động trên nhà xưởng', 'TV1-A2')
R('03_chuong3.md', 'Vì nhãn hư hỏng ở hiện trường hiếm (Mục 1.2.4)', 'Vì nhãn hư hỏng ở hiện trường hiếm (Mục 1.2.2)', 'TV5-ref')
R('03_chuong3.md', 'cho tới khi được rà soát (Mục 4.6.1).', 'cho tới khi được rà soát (Mục 4.6.2).', 'TV5-ref')
R('03_chuong3.md', 'Mục tiêu cần đạt là đánh giá khả năng vận hành của chuỗi trong điều kiện thật qua bốn số đo:', 'Mục tiêu cần đạt là đánh giá khả năng duy trì chuỗi trong điều kiện thật qua bốn số đo, không đánh giá hiệu năng phát hiện hư hỏng:', 'TV1-A2')

# ---------- Chương 2 ----------
R('02_chuong2.md', 'BIM và IFC là nền cho định danh cấu kiện nhưng không tự tạo ra chuỗi truy vết;',
  'BIM và IFC tạo nền định danh và khả năng liên thông thông tin nhưng chưa tự tạo ra truy vết từ bằng chứng tới hành động;', 'TV5-F')

# ---------- Chương 5: RQ2 ----------
R('05_chuong5.md', 'người quản lý có truy ngược được căn cứ và người chịu trách nhiệm của từng quyết định kiểm tra – bảo trì hay không, và lớp dữ liệu đề xuất khác B0 và B1 ở điểm nào? Câu hỏi được đo bằng khả năng truy ngược, tỉ lệ phát hiện lỗi chèn mù theo từng nhóm lỗi, mức đủ thuộc tính và công sức ghi nhận.',
  'người quản lý có xác định được bằng chứng nào đã được dùng, bằng chứng đó có còn phù hợp tại thời điểm dùng không, và ai chịu trách nhiệm cho từng quyết định kiểm tra – bảo trì hay không; lớp dữ liệu đề xuất khác B0 và B1 ở điểm nào? Câu hỏi được đo bằng câu hỏi năng lực trả lời đúng và đủ, tỉ lệ phát hiện lỗi chèn mù theo từng nhóm lỗi, mức đủ thuộc tính và công sức ghi nhận.', 'TV4-D4')

# ---------- Thuật ngữ ----------
R('00_thuatngu.md', '| Mã chủ thể | actor reference | Mã người hoặc tổ chức thực hiện một bước, ghi cùng vai trò tại thời điểm thực hiện (Mục 4.6.1, Phụ lục A) |',
  '| Mã chủ thể | actor reference | Mã người hoặc tổ chức thực hiện một bước, ghi cùng vai trò tại thời điểm thực hiện (Mục 4.6.2, Phụ lục A) |\n| Câu hỏi năng lực | competency question | Câu hỏi mà mô hình truy vết phải trả lời đúng và đủ theo đáp án chuẩn lập trước (Mục 4.4, 4.6.2) |', 'TV3-C6')
R('00_thuatngu.md', 'công sức ghi nhận (Mục 4.6.2) |', 'công sức ghi nhận (Mục 4.6.3) |', 'TV5-ref')

# ---------- Phụ lục ----------
R('phuluc.md', 'việc giữ khóa và liên kết khi xuất – nhập được kiểm như nêu ở Mục 4.6.1.', 'việc giữ khóa và liên kết khi xuất – nhập được kiểm như nêu ở Mục 4.6.4.', 'TV5-ref')
R('phuluc.md', 'với đủ khả năng của IFC 4.3 và BCF 3.0 (Mục 4.6.2)', 'với đủ khả năng của IFC 4.3 và BCF 3.0 (Mục 4.6.3)', 'TV5-ref')

# ---------- Dẫn nhập ----------
dn = open(os.path.join(ROOT, '00_dannhap.md'), encoding='utf-8').read()
i = dn.index('Chuyển đổi số mang lại'); j = dn.index('Tiểu luận gồm năm chương.')
files['00_dannhap.md'] = dn[:i] + C('''Chuyển đổi số mang lại cho bài toán này nhiều công cụ đã có nền nghiên cứu riêng. Dữ liệu dao động và học máy giúp nhận biết thay đổi trạng thái kết cấu ⟦13⟧. Lược đồ IFC biểu diễn được hệ theo dõi trạng thái và quan hệ cảm biến – cấu kiện ⟦2⟧. Song sinh số được đề xuất như kiến trúc nối dữ liệu vận hành với mô hình số của tài sản ⟦3⟧, ⟦7⟧. Theo đánh giá của phần tổng quan nghiên cứu này, khó khăn hiện nay nằm ở các điểm nối giữa những thành phần đó, nhiều hơn ở từng thành phần riêng lẻ.

Vấn đề trung tâm của luận án được phát biểu như sau. Một kết quả từ dữ liệu dao động chỉ có giá trị như một căn cứ quản lý khi được tổ chức thành bằng chứng trạng thái có nguồn gốc, độ bất định và phạm vi hiệu lực. Các thuộc tính đó phải được bảo toàn, được kiểm tại thời điểm sử dụng và truy vết được qua cấu kiện, hồ sơ kiểm tra và lịch sử hành động. Câu hỏi quản lý tương ứng là: tại thời điểm quyết định, bằng chứng nào được dùng, bằng chứng đó có còn phù hợp không, ai dùng với vai trò gì, và vì sao trạng thái hành động thay đổi? Luận án là một nghiên cứu Quản lý xây dựng về cách tổ chức và kiểm chứng căn cứ của quyết định kiểm tra – bảo trì; cảm biến, AI, BIM và song sinh số là công cụ.

Tiểu luận tổng quan này hệ thống hóa cơ sở lý luận và bằng chứng nghiên cứu về chuỗi thông tin từ dữ liệu dao động tới bằng chứng trạng thái, cấu kiện trong mô hình thông tin, hồ sơ kiểm tra và trạng thái hành động. Khách thể nghiên cứu là nhà công nghiệp khung thép liên kết bu lông trong giai đoạn vận hành. Tiểu luận dùng tổng quan tài liệu theo chủ đề có cấu trúc, trong đó 29 tài liệu key được đọc toàn văn (Mục 1.5.2). Khoảng trống được xác lập bằng phép trừ tiền lệ, tức chỉ giữ phần còn lại sau khi đối chiếu với các nghiên cứu và chuẩn gần nhất.

Kết quả là ba khoảng trống nối tiếp nhau, không phải ba đề tài độc lập. KT1 là tạo bằng chứng có phạm vi hiệu lực từ dữ liệu dao động. KT2 là bảo toàn và kiểm bằng chứng đó khi được dùng, từ bằng chứng tới hành động có trách nhiệm; đây là truy vết bằng chứng, khác với việc tích hợp cảm biến vào BIM. KT3 là duy trì chuỗi đó trong vận hành của nhà công nghiệp khung thép đang khai thác. Tương ứng, Mục tiêu 1 dùng mô hình khung thép 1:10 trong phòng thí nghiệm để tạo trạng thái liên kết có kiểm soát; mô hình này cho bằng chứng phòng thí nghiệm, không chứng minh tương tự động lực học với nhà xưởng. Mục tiêu 2 xây dựng lớp dữ liệu truy vết liên thông với IFC và BCF. Mục tiêu 3 kiểm khả năng duy trì chuỗi trên một nhà xưởng đang khai thác. Bằng chứng chỉ được dùng trong điều kiện đã đánh giá và phải được xét lại khi kết cấu hoặc cảm biến thay đổi. Quyết định kiểm tra và bảo trì thuộc về kỹ sư và người có thẩm quyền; AI chỉ tạo bằng chứng.

''') + dn[j:]
log.append({'tep': '00_dannhap.md', 'ma': 'TV1-A1', 'truoc': dn[i:j], 'sau': '(viết lại ba đoạn giữa của Dẫn nhập)'})

for f, t in files.items():
    open(os.path.join(ROOT, f), 'w', encoding='utf-8', newline='').write(t)
json.dump(log, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'HT16_rest_edits.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('ok', len(log))
