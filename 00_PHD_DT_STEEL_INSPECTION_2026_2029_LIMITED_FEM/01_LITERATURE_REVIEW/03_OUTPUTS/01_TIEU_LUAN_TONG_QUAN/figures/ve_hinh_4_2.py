"""Hình 4.2 – Ba kiểu quan hệ: cảm biến – cấu kiện, bằng chứng – cấu kiện, bản ghi kiểm tra – phát hiện thực tế.

Cùng phong cách với figures/ve_hinh.py (Times New Roman, khung xám, khung nhấn xanh).
Chạy: python figures/ve_hinh_4_2.py
"""
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

plt.rcParams['font.family'] = 'Times New Roman'
OUT = os.path.dirname(os.path.abspath(__file__))
GREY, BLUE, EDGE, EDGE_HL = '#F1F1F1', '#E3EBF5', '#555555', '#2F5E8E'


def box(ax, x, y, w, h, text, hl=False, size=14):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0,rounding_size=0.08',
                                fc=BLUE if hl else GREY, ec=EDGE_HL if hl else EDGE, lw=1.4))
    ax.text(x + w / 2, y + h / 2, text, ha='center', va='center', fontsize=size, linespacing=1.35)


rows = [
    ('Cảm biến', 'giám sát, trong khoảng hiệu lực\ncủa ánh xạ', 'Cấu kiện hoặc khu vực\nđược giám sát', False),
    ('Bằng chứng trạng thái', 'được tạo từ bối cảnh\nquan trắc của', 'Cấu kiện hoặc khu vực\nđược giám sát', False),
    ('Bản ghi kiểm tra\n(kỹ sư)', 'xác nhận', 'Phát hiện thực tế:\nvị trí, tình trạng hư hỏng', True),
]
fig, ax = plt.subplots(figsize=(11.0, 4.6))
wl, wr, h, gap_x, gap_y = 3.0, 3.6, 1.05, 3.4, 0.45
for i, (left, rel, right, hl) in enumerate(rows):
    y = (len(rows) - 1 - i) * (h + gap_y)
    box(ax, 0, y, wl, h, left)
    box(ax, wl + gap_x, y, wr, h, right, hl=hl)
    ax.add_patch(FancyArrowPatch((wl, y + h / 2), (wl + gap_x, y + h / 2), arrowstyle='-|>',
                                 mutation_scale=14, lw=1.4, color=EDGE))
    ax.text(wl + gap_x / 2, y + h / 2 + 0.08, rel, ha='center', va='bottom', fontsize=12.5, style='italic', linespacing=1.2)
ax.set_xlim(-0.05, wl + gap_x + wr + 0.05)
ax.set_ylim(-0.05, len(rows) * (h + gap_y) - gap_y + 0.05)
ax.axis('off')
fig.savefig(os.path.join(OUT, 'Hinh_4_2_Ba_kieu_quan_he.png'), dpi=200, bbox_inches='tight', pad_inches=0.05)
plt.close(fig)
print('OK')
