"""Vẽ lại bốn hình của Tiểu luận tổng quan (Pha 4, 02/10/2026).

Nhãn khớp văn bản sau Pha 1–3: "bản ghi kiểm tra" cho thực thể INSPECTION_RECORD;
lớp 3 gọi là "Khả năng áp dụng trong bối cảnh thực tế".
Chạy: python figures/ve_hinh.py  (tạo các tệp .png cạnh tệp này)
"""
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

plt.rcParams['font.family'] = 'Times New Roman'
OUT = os.path.dirname(os.path.abspath(__file__))
GREY, BLUE, EDGE, EDGE_HL = '#F1F1F1', '#E3EBF5', '#555555', '#2F5E8E'


def box(ax, x, y, w, h, text, hl=False, size=15, title=None):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0,rounding_size=0.08',
                                fc=BLUE if hl else GREY, ec=EDGE_HL if hl else EDGE, lw=1.4))
    if title:
        ax.text(x + w / 2, y + h * 0.66, title, ha='center', va='center', fontsize=size, fontweight='bold')
        ax.text(x + w / 2, y + h * 0.30, text, ha='center', va='center', fontsize=size - 1)
    else:
        ax.text(x + w / 2, y + h / 2, text, ha='center', va='center', fontsize=size, linespacing=1.4)


def arrow(ax, x1, y1, x2, y2):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle='-|>', mutation_scale=14, lw=1.4, color=EDGE))


def chain(name, labels, size=15):
    n, w, h, gap = len(labels), 2.0, 1.15, 0.45
    fig, ax = plt.subplots(figsize=(12.6, 2.0))
    for i, lab in enumerate(labels):
        x = i * (w + gap)
        box(ax, x, 0, w, h, lab, hl=(i == n - 1), size=size)
        if i < n - 1:
            arrow(ax, x + w, h / 2, x + w + gap, h / 2)
    ax.set_xlim(-0.05, n * w + (n - 1) * gap + 0.05); ax.set_ylim(-0.05, h + 0.05); ax.axis('off')
    fig.savefig(os.path.join(OUT, name), dpi=200, bbox_inches='tight', pad_inches=0.05); plt.close(fig)


chain('Hinh_1_1_Chuoi_nghien_cuu_tong_the.png',
      ['Dữ liệu\ndao động', 'Bằng chứng\ntrạng thái', 'Cấu kiện\nliên kết BIM', 'Bản ghi\nkiểm tra', 'Hỗ trợ hành động\nkiểm tra – bảo trì'])
chain('Hinh_5_1_Chuoi_dinh_danh_cot_loi.png',
      ['Sensor_ID', 'BIM_GUID', 'Condition_\nEvidence_ID', 'Inspection_\nRecord_ID', 'Action_Status'])
chain('Hinh_5_3_Logic_ho_tro_hanh_dong.png', ['Bình thường', 'Theo dõi', 'Kiểm tra', 'Kiểm tra ưu tiên'])

# Hình 5.2 – bốn lớp, lớp 1 ở dưới cùng
layers = [
    ('Hỗ trợ quyết định quản lý', 'Người rà soát; trạng thái hành động; căn cứ truy ngược'),
    ('Khả năng áp dụng trong bối cảnh thực tế', 'Đăng ký cảm biến; ánh xạ cấu kiện; đường cơ sở vận hành'),
    ('Truy vết thông tin', 'Chuỗi định danh; liên kết BIM; bản ghi kiểm tra'),
    ('Bằng chứng phòng thí nghiệm', 'Dữ liệu dao động; đánh giá theo đơn vị độc lập; kiểm soát rò rỉ'),
]
fig, ax = plt.subplots(figsize=(8.6, 7.4))
w, h, gap = 8.0, 1.35, 0.55
for i, (title, sub) in enumerate(layers):
    y = (len(layers) - 1 - i) * (h + gap)
    box(ax, 0, y, w, h, sub, hl=(i == 0), size=15, title=title)
    if i < len(layers) - 1:
        arrow(ax, w / 2, y, w / 2, y - gap)
ax.set_xlim(-0.05, w + 0.05); ax.set_ylim(-0.05, len(layers) * (h + gap) - gap + 0.05); ax.axis('off')
fig.savefig(os.path.join(OUT, 'Hinh_5_2_Kien_truc_kiem_chung_bon_lop.png'), dpi=200, bbox_inches='tight', pad_inches=0.05)
plt.close(fig)
print('OK')
