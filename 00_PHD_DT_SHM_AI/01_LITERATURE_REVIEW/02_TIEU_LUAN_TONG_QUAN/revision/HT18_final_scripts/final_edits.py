# -*- coding: utf-8 -*-
"""HT18 final proofread: đoạn nối 3.4.3, Hình 4.2, thuật ngữ."""
import os, sys, json
sys.stdout.reconfigure(encoding='utf-8')
ROOT = r'H:\My Drive\03_RESEARCH\01_PHD_DT_AI_AM\00_PHD_DT_STEEL_INSPECTION_2026_2029_LIMITED_FEM\01_LITERATURE_REVIEW\03_OUTPUTS\01_TIEU_LUAN_TONG_QUAN\tieuluan'
files, log = {}, []
def R(f, old, new, tag):
    if f not in files: files[f] = open(os.path.join(ROOT, f), encoding='utf-8').read()
    n = files[f].count(old); assert n == 1, f'{f} [{tag}] {n}: {old[:90]}'
    files[f] = files[f].replace(old, new); log.append({'tep': f, 'nhom': tag, 'truoc': old, 'sau': new})

# 1. Đoạn nối thí nghiệm -> truy vết (cuối 3.4.3); câu cũ về ca kiểm thử chuyển vào đoạn mới
R('03_chuong3.md', ' Mục tiêu 2 dùng các bản ghi bằng chứng này làm ca kiểm thử quy tắc của lớp dữ liệu truy vết; chúng không là căn cứ cho quyết định tại nhà xưởng (Mục 4.6.3).',
  '\n\nThí nghiệm vì vậy có một vai trò xác định trong toàn luận án. Nó tạo một môi trường có trạng thái can thiệp được kiểm soát, để đánh giá cách một kết quả từ dữ liệu dao động trở thành bằng chứng trạng thái mang nguồn gốc, độ bất định và phạm vi hiệu lực. Thí nghiệm không nhằm tạo một bộ phân loại để đưa ra nhà xưởng. Các bản ghi bằng chứng sinh ra từ thí nghiệm được Mục tiêu 2 dùng làm ca thử, để kiểm xem ba thuộc tính đó có được giữ nguyên và truy vết được khi bằng chứng đi qua cấu kiện liên kết BIM, bản ghi kiểm tra và lịch sử hành động hay không (Mục 4.6.3). Khi chuyển sang hiện trường, mô hình, bộ phân loại và ngưỡng của phòng thí nghiệm không được chuyển theo; luận án chỉ kế thừa nguyên tắc tổ chức, đánh giá và sử dụng bằng chứng (Mục 3.5).',
  'Bridge')

# 2. Hình 4.2 sau đoạn ba kiểu quan hệ (4.6.1)
R('04_chuong4.md', 'Nhờ vậy, mô hình không cho phép hiểu rằng AI từ dữ liệu cảm biến đã xác định chính xác vị trí hư hỏng.',
  'Nhờ vậy, mô hình không cho phép hiểu rằng AI từ dữ liệu cảm biến đã xác định chính xác vị trí hư hỏng. Hình 4.2 đặt ba kiểu quan hệ cạnh nhau.\n\n![](../figures/Hinh_4_2_Ba_kieu_quan_he.png)\n\n<span id="TLTQ_Hinh_4_2" class="anchor"></span>Hình 4.2. Ba kiểu quan hệ: cảm biến – cấu kiện, bằng chứng – cấu kiện và bản ghi kiểm tra – phát hiện thực tế',
  'Visual')

# 3. Thuật ngữ
R('00_dannhap.md', 'Song sinh số được đề xuất như kiến trúc', 'Song sinh số (Digital Twin) được đề xuất như kiến trúc', 'Terms')
R('02_chuong2.md', 'bằng chứng tình trạng', 'bằng chứng trạng thái', 'Terms')
R('00_thuatngu.md', '| MT, RQ, WP, Gate | evidence gate |', '| MT, RQ, WP, Gate | Evidence Gate |', 'Terms')
R('00_thuatngu.md', '| Nguồn gốc | provenance |',
  '| Bản ghi kiểm tra | inspection record | Bản ghi kết quả một lần kiểm tra của kỹ sư trong mô hình dữ liệu (thực thể `INSPECTION_RECORD`); "hồ sơ kiểm tra" chỉ hồ sơ kiểm tra – kiểm định nói chung |\n| Nguồn gốc | provenance |', 'Terms')

for f, t in files.items():
    open(os.path.join(ROOT, f), 'w', encoding='utf-8', newline='').write(t)
json.dump(log, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'HT18_final_edits.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('ok', len(log))
