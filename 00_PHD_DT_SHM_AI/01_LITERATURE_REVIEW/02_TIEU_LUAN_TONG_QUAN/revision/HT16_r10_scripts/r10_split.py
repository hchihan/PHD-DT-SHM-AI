# -*- coding: utf-8 -*-
"""HT16 r10 – tách câu dài (TV5-E4)."""
import os, sys, json
sys.stdout.reconfigure(encoding='utf-8')
ROOT = r'H:\My Drive\03_RESEARCH\01_PHD_DT_AI_AM\00_PHD_DT_STEEL_INSPECTION_2026_2029_LIMITED_FEM\01_LITERATURE_REVIEW\03_OUTPUTS\01_TIEU_LUAN_TONG_QUAN\tieuluan'
def C(s): return s.replace('⟦', '\\[').replace('⟧', '\\]')
files, log = {}, []
def R(f, old, new):
    if f not in files: files[f] = open(os.path.join(ROOT, f), encoding='utf-8').read()
    old, new = C(old), C(new); n = files[f].count(old); assert n == 1, f'{f} {n}: {old[:80]}'
    files[f] = files[f].replace(old, new); log.append({'tep': f, 'ma': 'TV5-E4', 'truoc': old, 'sau': new})

R('04_chuong4.md', 'theo cách ⟦35⟧ áp dụng: chuỗi lần kiểm tra – hư hỏng – cấu kiện – nhiệm vụ bảo trì bằng thực thể chuẩn IFC 4.3, trạng thái hư hỏng theo quy ước',
  'theo cách ⟦35⟧ áp dụng. Chuỗi lần kiểm tra – hư hỏng – cấu kiện – nhiệm vụ bảo trì được biểu diễn bằng thực thể chuẩn IFC 4.3, cùng trạng thái hư hỏng theo quy ước')
R('04_chuong4.md', '(tr. 8–10); gán cảm biến cho cấu kiện như ⟦2⟧; lệnh bảo trì có trạng thái và phê duyệt của IFC4 ⟦@63XPSMIR⟧; trạng thái và sự kiện đổi trạng thái của vấn đề theo BCF 3.0',
  '(tr. 8–10). B1 còn dùng phép gán cảm biến cho cấu kiện như ⟦2⟧, lệnh bảo trì có trạng thái và phê duyệt của IFC4 ⟦@63XPSMIR⟧, và trạng thái cùng sự kiện đổi trạng thái của vấn đề theo BCF 3.0')
R('04_chuong4.md', 'Bộ câu hỏi dự kiến gồm các loại sau: bằng chứng E sinh từ cảm biến nào; cảm biến đó được ánh xạ tới cấu kiện nào tại thời điểm E được tạo; E có còn nằm trong phạm vi hiệu lực tại thời điểm được dùng không; bản ghi kiểm tra nào được tạo từ E; ai đã đổi trạng thái hành động, với vai trò gì tại thời điểm đổi; bằng chứng và lý do nào làm căn cứ; và sau một can thiệp, bằng chứng hoặc đường cơ sở nào không còn được dùng.',
  'Bộ câu hỏi dự kiến gồm hai nhóm. Nhóm về bằng chứng hỏi: bằng chứng E sinh từ cảm biến nào; cảm biến đó được ánh xạ tới cấu kiện nào tại thời điểm E được tạo; E có còn nằm trong phạm vi hiệu lực tại thời điểm được dùng không; và bản ghi kiểm tra nào được tạo từ E. Nhóm về trách nhiệm hỏi: ai đã đổi trạng thái hành động, với vai trò gì tại thời điểm đổi; bằng chứng và lý do nào làm căn cứ; và sau một can thiệp, bằng chứng hoặc đường cơ sở nào không còn được dùng.')
R('04_chuong4.md', 'và áp cho hành động kiểm tra – bảo trì: mỗi lần chuyển trạng thái là một sự kiện ghi thời điểm, vai trò người thực hiện, bằng chứng làm căn cứ và lý do; trạng thái hiện thời',
  'và áp cho hành động kiểm tra – bảo trì. Theo đó, mỗi lần chuyển trạng thái là một sự kiện ghi thời điểm, chủ thể và vai trò người thực hiện, bằng chứng làm căn cứ và lý do. Trạng thái hiện thời')
R('05_chuong5.md', 'Gate 1 chỉ được đóng khi đủ bảy điều kiện: danh sách lần chạy được khóa; phép chia dữ liệu theo nhóm không rò rỉ; tham số tiền xử lý được học bên trong phần huấn luyện của từng lần chia; việc chọn siêu tham số không dùng phần kiểm tra; chế độ đầu vào cảm biến của ResNet1D được xác nhận; cách gộp dự đoán khi tính chỉ số được thống nhất; và LORO, LOCO chỉ dùng các đợt thỏa điều kiện so sánh (Mục 3.4.3).',
  'Gate 1 chỉ được đóng khi đủ bảy điều kiện. Ba điều kiện thuộc dữ liệu: danh sách lần chạy được khóa; phép chia dữ liệu theo nhóm không rò rỉ; và LORO, LOCO chỉ dùng các đợt thỏa điều kiện so sánh. Ba điều kiện thuộc huấn luyện: tham số tiền xử lý được học bên trong phần huấn luyện của từng lần chia; việc chọn siêu tham số không dùng phần kiểm tra; và chế độ đầu vào cảm biến của ResNet1D được xác nhận. Điều kiện cuối là cách gộp dự đoán khi tính chỉ số được thống nhất (Mục 3.4.3).')
R('05_chuong5.md', 'trên mô hình khung thép tỉ lệ 1:10, bằng cách đo mức chênh lệch giữa đánh giá cùng lần chạy và hai mức đánh giá theo đơn vị độc lập với bốn mô hình học máy, rồi ghi điều kiện đã đánh giá và độ bất định cho từng kết quả.',
  'trên mô hình khung thép tỉ lệ 1:10. Quy trình đo mức chênh lệch giữa đánh giá cùng lần chạy và hai mức đánh giá theo đơn vị độc lập với bốn mô hình học máy, rồi ghi điều kiện đã đánh giá và độ bất định cho từng kết quả.')
R('03_chuong3.md', 'Mỗi kết quả được ghi thành một bản ghi bằng chứng: cấp nhóm, đơn vị chấm điểm, đợt lắp đặt và cấu hình cảm biến vào trường phạm vi hiệu lực; biến thiên theo seed và fold vào trường độ bất định; kết quả kiểm định hoán vị vào mô tả giao thức đánh giá, như căn cứ rằng hiệu năng vượt mức ngẫu nhiên; nhãn hoặc xác suất vào trường giá trị; mã phiên bản chuỗi xử lý vào trường phiên bản phương pháp.',
  'Mỗi kết quả được ghi thành một bản ghi bằng chứng. Cấp nhóm, đơn vị chấm điểm, đợt lắp đặt và cấu hình cảm biến được ghi vào trường phạm vi hiệu lực; biến thiên theo seed và fold vào trường độ bất định. Kết quả kiểm định hoán vị được ghi vào mô tả giao thức đánh giá, như căn cứ rằng hiệu năng vượt mức ngẫu nhiên. Nhãn hoặc xác suất được ghi vào trường giá trị, và mã phiên bản chuỗi xử lý vào trường phiên bản phương pháp.')
R('03_chuong3.md', 'với cấu trúc gọn ⟦@HPREAQAJ⟧, và là nhóm mô hình được dùng nhiều trong phát hiện hư hỏng dựa trên dao động ⟦@QUGY4928⟧; các nghiên cứu',
  'với cấu trúc gọn ⟦@HPREAQAJ⟧, và là nhóm mô hình được dùng nhiều trong phát hiện hư hỏng dựa trên dao động ⟦@QUGY4928⟧. Các nghiên cứu')
R('03_chuong3.md', 'Mục tiêu cần đạt là đánh giá khả năng duy trì chuỗi trong điều kiện thật qua bốn số đo, không đánh giá hiệu năng phát hiện hư hỏng: tỉ lệ dữ liệu về đủ',
  'Mục tiêu cần đạt là đánh giá khả năng duy trì chuỗi trong điều kiện thật, không đánh giá hiệu năng phát hiện hư hỏng. Bốn số đo được dùng: tỉ lệ dữ liệu về đủ')
R('01_chuong1.md', 'quanh giá trị trung bình, và tỷ lệ phát hiện đúng', 'quanh giá trị trung bình. Tỷ lệ phát hiện đúng')
R('01_chuong1.md', 'Chương trình bày bối cảnh quản lý vận hành và pháp lý, đặc điểm của nhà công nghiệp khung thép liên kết bu lông cùng hạn chế của quan trắc và quản lý thông tin hiện nay, khái niệm bằng chứng trạng thái và nhu cầu của người quản lý, vấn đề nghiên cứu, rồi mục tiêu, phạm vi và phương pháp tổng quan.',
  'Chương trình bày bối cảnh quản lý vận hành và pháp lý, đặc điểm của nhà công nghiệp khung thép liên kết bu lông, và hạn chế của quan trắc cùng quản lý thông tin hiện nay. Tiếp theo là khái niệm bằng chứng trạng thái, nhu cầu của người quản lý, vấn đề nghiên cứu, rồi mục tiêu, phạm vi và phương pháp tổng quan.')
R('02_chuong2.md', 'Luận án dùng phân loại của ⟦8⟧ làm thước đo mức tích hợp và đặt song sinh số dựa trên dữ liệu làm mục tiêu kiến trúc: luồng dữ liệu',
  'Luận án dùng phân loại của ⟦8⟧ làm thước đo mức tích hợp và đặt song sinh số dựa trên dữ liệu làm mục tiêu kiến trúc. Trong kiến trúc đó, luồng dữ liệu')
R('01_chuong1.md', 'Tiểu luận không lập sơ đồ PRISMA vì hai lý do: đây là tổng quan theo chủ đề có cấu trúc, không phải tổng quan hệ thống; và số kết quả tìm kiếm ban đầu ở từng cơ sở dữ liệu chưa được lưu đầy đủ, nên không lập được sơ đồ phản ánh trung thực quá trình sàng lọc.',
  'Tiểu luận không lập sơ đồ PRISMA vì hai lý do. Đây là tổng quan theo chủ đề có cấu trúc, không phải tổng quan hệ thống. Số kết quả tìm kiếm ban đầu ở từng cơ sở dữ liệu cũng chưa được lưu đầy đủ, nên không lập được sơ đồ phản ánh trung thực quá trình sàng lọc.')

for f, t in files.items():
    open(os.path.join(ROOT, f), 'w', encoding='utf-8', newline='').write(t)
json.dump(log, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'HT16_split_edits.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('ok', len(log))
