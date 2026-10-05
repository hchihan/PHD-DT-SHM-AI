# -*- coding: utf-8 -*-
"""r5: chuẩn hóa cỡ chữ để nhìn rõ khi ngồi xa: thân bài >= 14pt, trích dẫn và chú thích 12pt, tiêu đề lớn hơn.
Chạy: python revision/HT21_slide_scripts/fonts_r5.py IN.pptx OUT.pptx"""
import sys, re, copy
from pptx import Presentation
from pptx.util import Pt, Inches
from pptx.dml.color import RGBColor

sys.stdout.reconfigure(encoding='utf-8')
prs = Presentation(sys.argv[1])
CITE = re.compile(r'\((?=[^()]*(?:19|20)\d\d)[^()]*\)')
GREY = RGBColor.from_string('555555')
BODY_MIN, CITE_PT, TITLE_PT, SECTION_PT = 16, 12, 26, 20


def color_of(r):
    try:
        return r.font.color.rgb
    except Exception:
        return None


def split_citations(p):
    """Tách các đoạn trích dẫn (tác giả, năm) trong một run thành run riêng."""
    for r in list(p.runs):
        t = r.text
        ms = list(CITE.finditer(t))
        if not ms or (len(ms) == 1 and ms[0].start() == 0 and ms[0].end() == len(t)):
            continue
        parts, last = [], 0
        for m in ms:
            if m.start() > last:
                parts.append((t[last:m.start()], False))
            parts.append((m.group(0), True))
            last = m.end()
        if last < len(t):
            parts.append((t[last:], False))
        r.text = parts[0][0]
        prev = r._r
        for txt, _ in parts[1:]:
            nr = copy.deepcopy(r._r)
            prev.addnext(nr)
            prev = nr
        # đặt lại chữ cho các run mới
        runs = p.runs
        i0 = [k for k, x in enumerate(runs) if x._r is r._r][0]
        for k, (txt, _) in enumerate(parts):
            runs[i0 + k].text = txt


def is_cite(r):
    t = r.text.strip()
    if not t:
        return False
    if CITE.fullmatch(t) or re.fullmatch(r'\(?[^()]*(?:và cs\.|&|cộng sự)[^()]*(?:19|20)\d\d\)?;?', t):
        return True
    if r.font.italic and color_of(r) == GREY:
        return True
    return False


def walk(shapes):
    for s in shapes:
        if s.shape_type == 6:
            yield from walk(s.shapes)
        else:
            yield s


log = []
def _rep(slide, old, new):
    for sh in slide.shapes:
        if sh.has_text_frame:
            for p in sh.text_frame.paragraphs:
                for r in p.runs:
                    if old in r.text:
                        r.text = r.text.replace(old, new)
_rep(prs.slides[5], 'tài liệu key đọc toàn văn', 'tài liệu trọng điểm đọc toàn văn')
nt = prs.slides[5].notes_slide.notes_text_frame
nt.text = nt.text.replace('29 tài liệu key được đọc toàn văn', '29 tài liệu trọng điểm được đọc toàn văn')
_rep(prs.slides[11], 'ĐỐI TƯỢNG VÀ PHẠM VI: BA MÔI TRƯỜNG NGHIÊN CỨU VÀ KIỂM CHỨNG', 'BA MÔI TRƯỜNG NGHIÊN CỨU VÀ KIỂM CHỨNG')
for n, slide in enumerate(prs.slides, 1):
    if n in (1, 2):
        continue
    for s in walk(slide.shapes):
        if not s.has_text_frame:
            continue
        if s.shape_id == 2 and s.top < Inches(0.2):           # dòng tên phần
            for p in s.text_frame.paragraphs:
                for r in p.runs:
                    r.font.size = Pt(SECTION_PT)
            continue
        if s.shape_id == 3 and s.top < Inches(0.6):           # ô tiêu đề
            r = s.text_frame.paragraphs[0].runs[0]
            L = len(r.text)
            size = min(TITLE_PT, int(8.45 / (L * 0.0088)))
            r.font.size = Pt(size)
            s.width = Inches(min(8.83, 0.45 + L * 0.0088 * size))
            log.append(f'S{n} tiêu đề {size}pt')
            continue
        for p in s.text_frame.paragraphs:
            split_citations(p)
            for r in p.runs:
                sz = r.font.size.pt if r.font.size else 14
                if is_cite(r):
                    r.font.size = Pt(CITE_PT)
                elif sz < BODY_MIN:
                    r.font.size = Pt(BODY_MIN)
prs.save(sys.argv[2])
print(chr(10).join(log)); print('saved', sys.argv[2])
