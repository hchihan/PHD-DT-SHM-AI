"""Xuất bản Tiểu luận tổng quan (Pha 4 / GĐ6, CLAUDE.md 4.4 và 6).

1. Ghép các tệp trong tieuluan/ theo thứ tự xuất bản, bỏ chú thích ẩn.
2. Đánh số lại trích dẫn theo thứ tự xuất hiện lần đầu (IEEE). Trích dẫn cũ dạng \\[n\\] (n = so_cu)
   và \\[@KHÓA\\] đều được ánh xạ sang số mới. Dải cũ \\[a\\]–\\[b\\] được mở ra trước khi đánh số;
   nhóm trích dẫn liền nhau được sắp tăng dần và gộp dải từ ba số liên tiếp (\\[3\\]–\\[5\\]).
3. Tạo lại danh mục tài liệu theo số mới từ các mục IEEE trong tieuluan/99_tailieu.md
   (các mục này xuất từ Zotero ở GĐ0 và HT1 phiên 3).
4. Ghi xuat_ban/<tên>.md, xuat_ban/danh_so_IEEE.csv và gọi pandoc tạo .docx với styles của bản gốc.

Tệp nguồn trong tieuluan/ giữ nguyên số cũ để truy được về so_cu, notes/ và ma trận.
Chạy: python xuat_ban/build.py
"""
import csv, os, re, subprocess, sys
sys.stdout.reconfigure(encoding='utf-8')

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC, OUT = os.path.join(ROOT, 'tieuluan'), os.path.join(ROOT, 'xuat_ban')
NAME = 'HO_CHI_HAN_TIEU_LUAN_TONG_QUAN_v2_20261002'
REFDOC = os.path.join(ROOT, 'HO_CHI_HAN_TIEU_LUAN_TONG_QUAN_23092026_HOANTHIEN.docx')
FRONT = ['00_bia.md', '00_khaibao_AI.md', '00_thuatngu.md']
BODY = ['00_dannhap.md', '01_chuong1.md', '02_chuong2.md', '03_chuong3.md', '04_chuong4.md', '05_chuong5.md']
APPX = ['phuluc.md']

BS = '\\'
CITE = re.escape(BS + '[') + r'(\d+|@[A-Za-z0-9]+)' + re.escape(BS + ']')
UNIT = CITE + r'(?:\s*–\s*' + CITE + r')?'
GROUP = re.compile(UNIT + r'(?:\s*,\s*' + UNIT + r')*')
UNIT_RE = re.compile(UNIT)

def read(f):
    return re.sub(r'<!--.*?-->', '', open(os.path.join(SRC, f), encoding='utf-8').read(), flags=re.S)

# ---------- 1. danh mục nguồn ----------
bib = read('99_tailieu.md')
entries = {}
for line in bib.split('\n'):
    m = re.match(re.escape(BS + '[') + r'(\d+|@[A-Za-z0-9]+)' + re.escape(BS + ']') + r'\s+(.*)', line)
    if m:
        entries[m.group(1)] = m.group(2).strip()

# ---------- 2. đánh số lại ----------
newnum, order = {}, []
def num(k):
    if k not in newnum:
        if k not in entries:
            sys.exit(f'Trích dẫn {k} không có trong 99_tailieu.md')
        newnum[k] = len(order) + 1; order.append(k)
    return newnum[k]

def keys_of(group_text):
    ks = []
    for u in UNIT_RE.finditer(group_text):
        a, b = u.group(1), u.group(2)
        if b:
            assert a.isdigit() and b.isdigit(), group_text
            ks += [str(i) for i in range(int(a), int(b) + 1)]
        else:
            ks.append(a)
    return ks

def fmt(nums):
    nums = sorted(set(nums)); out, i = [], 0
    while i < len(nums):
        j = i
        while j + 1 < len(nums) and nums[j + 1] == nums[j] + 1:
            j += 1
        if j - i >= 2:
            out.append(f'{BS}[{nums[i]}{BS}]–{BS}[{nums[j]}{BS}]')
        else:
            out += [f'{BS}[{n}{BS}]' for n in nums[i:j + 1]]
        i = j + 1
    return ', '.join(out)

def renumber(text):
    return GROUP.sub(lambda m: fmt([num(k) for k in keys_of(m.group(0))]), text)

PAGE = '\n```{=openxml}\n<w:p><w:r><w:br w:type="page"/></w:r></w:p>\n```\n'
TOC = ('\n**MỤC LỤC**\n\n```{=openxml}\n<w:p><w:r><w:fldChar w:fldCharType="begin" w:dirty="true"/></w:r>'
       '<w:r><w:instrText xml:space="preserve"> TOC \\o "1-3" \\h \\z \\u </w:instrText></w:r>'
       '<w:r><w:fldChar w:fldCharType="separate"/></w:r><w:r><w:t>(Nhấn chuột phải, chọn Update Field để tạo mục lục)</w:t></w:r>'
       '<w:r><w:fldChar w:fldCharType="end"/></w:r></w:p>\n```\n')

def prep(text, fname):
    if fname == '00_thuatngu.md':
        text = text.replace('**GIẢI THÍCH THUẬT NGỮ**', '# GIẢI THÍCH THUẬT NGỮ', 1)
    # chú thích bảng, hình: dùng style CaptionTLTQ của bản gốc
    text = re.sub(r'^(<span id="TLTQ_(?:Bang|Hinh)_[^"]+" class="anchor"></span>(?:Bảng|Hình) .+)$',
                  lambda m: '::: {custom-style="CaptionTLTQ"}\n' + m.group(1) + '\n:::', text, flags=re.M)
    return text

parts = []
for f in FRONT + BODY + APPX:
    t = prep(read(f), f)
    if f in BODY + APPX:
        t = renumber(t)
    parts.append((f, t))
leftover = re.findall(CITE, ''.join(t for _, t in parts if _ in FRONT))
assert not leftover, f'Còn trích dẫn ở phần đầu: {leftover}'

refs = '# TÀI LIỆU THAM KHẢO\n\n' + '\n\n'.join(f'{BS}[{i}{BS}] {entries[k]}' for i, k in enumerate(order, 1)) + '\n'
doc = []
for f, t in parts:
    if f == 'phuluc.md':
        doc.append(PAGE + refs)
    doc.append((PAGE if f != '00_bia.md' else '') + t)
    if f == '00_khaibao_AI.md':
        doc.append(PAGE + TOC)
md = '\n'.join(doc)

os.makedirs(OUT, exist_ok=True)
open(os.path.join(OUT, NAME + '.md'), 'w', encoding='utf-8', newline='').write(md)

so_cu = {r['citekey'].replace('zotero:', ''): r['so_cu']
         for r in csv.DictReader(open(os.path.join(ROOT, 'matrix', 'doi_chieu_danh_muc.csv'), encoding='utf-8-sig'), delimiter='|')}
with open(os.path.join(OUT, 'danh_so_IEEE.csv'), 'w', encoding='utf-8-sig', newline='') as fh:
    w = csv.writer(fh, delimiter='|'); w.writerow(['so_moi', 'nguon_trong_tieuluan', 'so_cu_hoac_moi', 'muc_dau_tien'])
    for i, k in enumerate(order, 1):
        w.writerow([i, k, k if k.isdigit() else so_cu.get(k[1:], 'moi'), entries[k][:90]])

uncited = sorted(set(entries) - set(order))
print(f'Trích dẫn: {len(order)} tài liệu; mục danh mục không được trích: {uncited}')
print('Còn thẻ [CẦN KIỂM]/[CẦN NGUỒN]:', len(re.findall(r'CẦN (?:KIỂM|NGUỒN)', md)))

subprocess.run(['pandoc', NAME + '.md', '-f', 'markdown', '-o', NAME + '.docx',
                '--reference-doc', REFDOC, '--resource-path', os.pathsep.join(['.', '..'])], cwd=OUT, check=True)

# ---------- 5. hậu xử lý định dạng (python-docx) ----------
import docx
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

def set_font(style, name='Times New Roman'):
    style.font.name = name
    rpr = style.element.get_or_add_rPr()
    rfonts = rpr.find(qn('w:rFonts'))
    if rfonts is None:
        rfonts = OxmlElement('w:rFonts'); rpr.append(rfonts)
    for a in ('w:ascii', 'w:hAnsi', 'w:cs', 'w:eastAsia'):
        rfonts.set(qn(a), name)
    for a in ('w:asciiTheme', 'w:hAnsiTheme', 'w:cstheme', 'w:eastAsiaTheme'):
        rfonts.attrib.pop(qn(a), None)

path = os.path.join(OUT, NAME + '.docx')
d = docx.Document(path)
for n in ('Heading 1', 'Heading 2', 'Heading 3', 'Body Text', 'First Paragraph', 'Compact', 'CaptionTLTQ'):
    if n in [s.name for s in d.styles]:
        set_font(d.styles[n])
# bìa: căn giữa, bỏ thụt dòng, giãn đoạn
for p in d.paragraphs:
    if p.style.name == 'Heading 1':
        break
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.first_line_indent = Cm(0)
    p.paragraph_format.space_after = Pt(14)
# bảng: lưới đơn, chữ 11 pt, căn trái, không thụt dòng
for t in d.tables:
    tblPr = t._tbl.tblPr
    borders = OxmlElement('w:tblBorders')
    for edge in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
        e = OxmlElement(f'w:{edge}')
        e.set(qn('w:val'), 'single'); e.set(qn('w:sz'), '4'); e.set(qn('w:color'), '808080')
        borders.append(e)
    old = tblPr.find(qn('w:tblBorders'))
    if old is not None:
        tblPr.remove(old)
    tblPr.append(borders)
    for row in t.rows:
        for cell in row.cells:
            for p in cell.paragraphs:
                pf = p.paragraph_format
                pf.first_line_indent = Cm(0); pf.line_spacing = 1.1; pf.space_after = Pt(2)
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                for r in p.runs:
                    r.font.size = Pt(11)
d.save(path)
print('Đã tạo', os.path.join('xuat_ban', NAME + '.docx'), '(mở bằng Word, cập nhật mục lục: chuột phải → Update Field)')
