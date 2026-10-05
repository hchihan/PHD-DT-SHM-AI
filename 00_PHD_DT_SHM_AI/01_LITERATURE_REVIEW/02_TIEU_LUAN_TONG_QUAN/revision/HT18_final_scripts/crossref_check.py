# -*- coding: utf-8 -*-
"""Đối chiếu mục tài liệu (CSL trong zotero_cache) với Crossref theo DOI."""
import json, csv, re, sys, time, unicodedata, urllib.request, urllib.parse
sys.stdout.reconfigure(encoding='utf-8')
ROOT = r'H:\My Drive\03_RESEARCH\01_PHD_DT_AI_AM\00_PHD_DT_STEEL_INSPECTION_2026_2029_LIMITED_FEM\01_LITERATURE_REVIEW\03_OUTPUTS\01_TIEU_LUAN_TONG_QUAN'
cache = json.load(open(ROOT + r'\xuat_ban\zotero_cache.json', encoding='utf-8'))
order = [r['khoa_zotero'] for r in csv.DictReader(open(ROOT + r'\xuat_ban\danh_muc_Zotero.csv', encoding='utf-8-sig'), delimiter='|')]

def norm(s):
    s = unicodedata.normalize('NFKD', str(s or '')).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', ' ', s).strip()

def year(c):
    d = (c.get('issued') or {}).get('date-parts') or [[None]]
    try: return int(d[0][0])
    except: return None

rows = []
for n, k in enumerate(order, 1):
    c = cache[k]['csl']; doi = (c.get('DOI') or '').strip()
    rec = {'so': n, 'key': k, 'type': c.get('type'), 'doi': doi, 'issues': []}
    if not doi:
        rec['issues'].append('không có DOI (kiểm qua cơ quan phát hành)')
        rows.append(rec); continue
    try:
        url = 'https://api.crossref.org/works/' + urllib.parse.quote(doi)
        req = urllib.request.Request(url, headers={'User-Agent': 'TLTQ-check/1.0 (mailto:hchihan.ntu@gmail.com)'})
        m = json.loads(urllib.request.urlopen(req, timeout=30).read())['message']
    except Exception as e:
        rec['issues'].append(f'Crossref lỗi: {e}'); rows.append(rec); continue
    ct, mt = norm(c.get('title')), norm((m.get('title') or [''])[0])
    if ct[:60] != mt[:60] and not (ct in mt or mt in ct):
        rec['issues'].append(f'tiêu đề khác: Zotero="{c.get("title")}" | Crossref="{(m.get("title") or [""])[0]}"')
    cy = year(c)
    my = None
    for fld in ('published-print', 'published-online', 'issued'):
        if m.get(fld): my = m[fld]['date-parts'][0][0]; break
    yrs = {m[f]['date-parts'][0][0] for f in ('published-print', 'published-online', 'issued') if m.get(f) and m[f]['date-parts'][0][0]}
    pr = m.get('published-print', {}).get('date-parts', [[None]])[0][0]
    if cy and yrs and cy not in yrs:
        rec['issues'].append(f'năm khác: Zotero={cy} | Crossref={sorted(yrs)}')
    elif cy and pr and cy != pr:
        rec['issues'].append(f'năm Zotero={cy} theo bản online; bản in={pr}')
    for zf, cf in (('volume', 'volume'), ('issue', 'issue')):
        zv, cv = str(c.get(zf) or ''), str(m.get(cf) or '')
        if zv and cv and norm(zv) != norm(cv):
            rec['issues'].append(f'{zf} khác: Zotero={zv} | Crossref={cv}')
        if cv and not zv:
            rec['issues'].append(f'thiếu {zf}: Crossref={cv}')
    zp = str(c.get('page') or ''); cp = str(m.get('page') or m.get('article-number') or '')
    if zp and cp and norm(zp).split(' ')[0] != norm(cp).split(' ')[0]:
        rec['issues'].append(f'trang khác: Zotero={zp} | Crossref={cp}')
    if cp and not zp:
        rec['issues'].append(f'thiếu trang/số bài: Crossref={cp}')
    zfam = [norm(a.get('family') or a.get('literal')) for a in c.get('author', [])]
    cfam = [norm(a.get('family') or a.get('name')) for a in m.get('author', [])]
    if zfam and cfam and zfam[0] and cfam[0] and zfam[0].split(' ')[-1] != cfam[0].split(' ')[-1] and zfam[0] not in cfam[0] and cfam[0] not in zfam[0]:
        rec['issues'].append(f'tác giả đầu khác: Zotero={zfam[0]} | Crossref={cfam[0]}')
    if len(zfam) != len(cfam) and cfam:
        rec['issues'].append(f'số tác giả: Zotero={len(zfam)} | Crossref={len(cfam)}')
    zc, mc = norm(c.get('container-title')), norm((m.get('container-title') or [''])[0])
    if zc and mc and zc != mc and not (zc in mc or mc in zc):
        rec['issues'].append(f'nơi công bố khác: Zotero="{c.get("container-title")}" | Crossref="{(m.get("container-title") or [""])[0]}"')
    rows.append(rec); time.sleep(0.15)

dois = [r['doi'].lower() for r in rows if r['doi']]
dup = {d for d in dois if dois.count(d) > 1}
titles = [norm(cache[k]['csl'].get('title'))[:60] for k in order]
duptitle = {t for t in titles if titles.count(t) > 1}
json.dump(rows, open(sys.argv[1], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('Tổng', len(rows), '| có DOI', len(dois), '| DOI trùng', dup or 'không', '| tiêu đề trùng', duptitle or 'không')
for r in rows:
    if r['issues']: print(r['so'], r['key'], r['type'], '|', ' ; '.join(r['issues']))
