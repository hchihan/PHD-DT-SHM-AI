# C1 — Kiểm toán nhóm đọc sâu / kiểm độ mới / ma trận (Pha 0 – Paper 2)

Người kiểm toán: AU-C1. Phạm vi: 23 tệp được giao trong `/home/claude/p2/txt/`. Đã đọc hết toàn bộ 23 tệp (đọc đến dòng cuối từng tệp; CSV đọc cả 3 tệp đến hết, 05_TARGETED có 12 dòng dữ liệu, 06_CORE5 có 5, 01_ZOTERO có 26, chưa kể dòng tiêu đề).
Quy ước viết tắt: C = Có; MP = Một phần; K = Không; ? = tệp không đủ căn cứ. "tệp:dòng" lấy theo số dòng của công cụ Read.
Ghi chú phương pháp: chỉ kiểm kê và đối chiếu. Không phản biện nội dung khoa học. Nội dung trong tệp coi là dữ liệu.

---

## 1. Bảng kiểm kê

Cột "Ngày": hầu hết tệp KHÔNG ghi ngày trong nội dung. Ngày duy nhất ghi rõ là 16/09/2026 (nhóm 10_*). Tệp 07 chỉ ghi ngày của bài được đọc (nhận 18/5, đăng 6/7/2026). Các tệp còn lại ghi "không ghi".

| Tệp | Ngày / phiên bản | Vai trò | Nội dung chính | Đọc hết? | Đề xuất trạng thái | Lý do |
|---|---|---|---|---|---|---|
| 01_CORE01_DEEP_READ.md | không ghi | đọc sâu | Bài Jäkel et al. 2025 (ITcon 30:603–630), ontology SODIA nối kết quả NDE với IFC cầu qua RDF và ICDD. Mức truy vết LEVEL 2. | Hết (95 dòng) | Còn hiệu lực (phần mô tả bài); phần "Implication for Paper 2" lỗi thời so với phạm vi khóa | Mục "Implication" dùng chuỗi Sensor_ID→…→Action_Status và đối chứng bằng ontology/SPARQL (01:70,82); phạm vi khóa dùng 6 thực thể, Python/SQLite, B0/B1 |
| 02_CORE02_HAGEDORN_DEEP_READ.md | không ghi | đọc sâu | Hagedorn et al. 2023 (JCCE 37(1) 04022041): ICDD + R2RML + PROV nối BIM với hệ AMS. LEVEL 1–2. | Hết (81 dòng) | Còn hiệu lực (mô tả); Implication lỗi thời | Như trên; đồng thời mức truy vết ghi "LEVEL 1–2" (02:42) còn ma trận ghi LEVEL_1 |
| 03_CORE03_YIN_DEEP_READ.md | không ghi | đọc sâu | Yin et al. 2020 (TUST 97:103252): khung BIM + CSDL quan hệ + giám sát cho hầm tiện ích; bảng Maintenance có staff ID và ngày. LEVEL 1. | Hết (79 dòng) | Còn hiệu lực (mô tả); Implication lỗi thời | Implication đề xuất "ontology-formalized (RDF/OWL…)" (03:54), ngược phạm vi khóa (không RDF/SHACL) |
| 04_CORE04_MATARNEH_DEEP_READ.md | không ghi | đọc sâu | Matarneh et al. 2022 (AutCon 143:104569): BIM4FM, IFC→COBie→CAFM/CMMS, kiểm bằng khảo sát Likert. LEVEL 1. | Hết (82 dòng) | Còn hiệu lực (mô tả); Implication lỗi thời | Như trên |
| 05_CORE05_SEISS_DEEP_READ.md | không ghi | đọc sâu | Seiß et al. 2025 (AutCon 177:106268): ontology OCQA, dùng GlobalId thật làm khóa, LEVEL 3, bài gần nhất trong 5 bài. | Hết (86 dòng) | Còn hiệu lực (mô tả); mục Validity scope dùng định nghĩa cũ | 05:38 xếp PARTIAL cho "validity scope" theo nghĩa dung sai chất lượng; sau hiệu chỉnh (tệp 08) định nghĩa chặt hơn, tệp 05 chưa được chấm lại |
| 07_BORKOWSKI_2026_FULLTEXT_REVIEW.md | không ghi (bài: nhận 18/5/2026, đăng 6/7/2026) | đọc sâu | Đọc toàn văn Borkowski et al. 2026 (Technologies 14(7):413), định danh qua giai đoạn bằng DOLCE. Mức đe dọa HIGH, hẹp ở nhánh định danh. | Hết (212 dòng) | Còn hiệu lực; thay thế ghi chú "abstract-only" ở tệp 03 và CSV 01 | Tự ghi đã sửa kết luận "không có toàn văn" (07:5); không có số trang, chỉ có tên mục |
| 08_CORRECTION_PASS_SUMMARY.md | không ghi | nhật ký | Tóm tắt hai lượt hiệu chỉnh: định nghĩa chặt "evidence_validity_scope", và giải quyết Borkowski có toàn văn. Trạng thái CONDITIONAL_FREEZE. | Hết (22 dòng) | Còn hiệu lực một phần | Không nhắc García 2026 và Bellon 2025 (xem mục 4 và 6) |
| 10_NOVELTY_CHECK_A_GRAGNANIELLO_2024.md | 16/09/2026 | kiểm độ mới | Gragnaniello 2024 (AutCon 158:105245): thiết kế/lắp đặt SHM bằng BIM, IDS. Đe dọa LOW. | Hết (56 dòng) | Còn hiệu lực | Dùng taxonomy GAP1/2/3, C1/C2/C3 cũ |
| 10_NOVELTY_CHECK_B_MARINIELLO_2025.md | 16/09/2026 | kiểm độ mới | Mariniello 2025 (AutCon 180:106558): blockchain, smart contract cho SHM/DT (SHERPA). Đe dọa MEDIUM. | Hết (56 dòng) | Còn hiệu lực | Như trên; có Alert→resolveAlert theo vai trò, liên quan C6 |
| 10_NOVELTY_CHECK_C_GARCIA_2026.md | 16/09/2026 | kiểm độ mới | García et al. 2026 (Appl. Sci. 16(5):2562): quality gate CDE, publish/hold, RACI đầy đủ. Đe dọa HIGH (hẹp). | Hết (60 dòng) | Còn hiệu lực; DOI cần đối chiếu | DOI không hiện trong văn bản trích (10-C:12) |
| 10_NOVELTY_CHECK_D_BELLON_2025.md | 16/09/2026 | kiểm độ mới | Bellon et al. 2025 (AutCon 174:106157): khung IFC cho kiểm tra và bảo trì trong FM. Chỉ đọc abstract. Đe dọa MEDIUM (không xác định được). | Hết (62 dòng) | Còn hiệu lực nhưng CHƯA ĐÓNG | Mọi câu Q3–Q8, Q10 = EVIDENCE_INSUFFICIENT; B1 của phạm vi khóa dựa vào bài này |
| 10_NOVELTY_CHECK_SUMMARY_20260916.md | 16/09/2026 | kiểm độ mới (tổng hợp) | Bảng 4 bài × GAP1/2/3 × C1/C2/C3; kết luận SCOPE-BOUNDED FREEZE có điều kiện. | Hết (74 dòng) | Còn hiệu lực một phần | GAP1/2/3 và C1/C2/C3 là hệ cũ; GAP3 theo phạm vi khóa không còn là khoảng trống |
| 06_TARGETED_GAP_AUDIT.md | không ghi (bản "correction-pass") | đọc sâu / audit | Chấm 8 khoảng trống GAP-A…H trên 12 bài Stage B; kết luận CONDITIONAL_FREEZE. | Hết (93 dòng) | Còn hiệu lực một phần | Hệ nhãn GAP-A…H trùng tên nhưng khác nghĩa với G-A/G-B của phạm vi khóa; không có García/Bellon |
| 03_TARGETED_DEEP_READ_SELECTION.md | không ghi | outline / định hướng | Chọn 12 bài Stage B, có DOI và phần đã đọc. | Hết (20 dòng) | Lỗi thời một phần | Ghi Borkowski "Abstract only (no PDF)" (03:7), đã bị tệp 07 thay |
| 02_EXCLUDED_PAPERS_SUMMARY.md | không ghi | nhật ký | Tóm tắt bài loại và bài nền: pool 22, nền >100. | Hết (46 dòng) | Tham khảo | Số đếm không khớp CSV 01 (mục 6) |
| 00_BIBLIOGRAPHIC_VERIFICATION.md | không ghi | nhật ký | Đối chiếu Zotero với PDF cho CORE-5; phát hiện thiếu tác giả Jäkel. | Hết (30 dòng) | Còn hiệu lực | Nguồn xác định CORE01 là bài của Jäkel |
| 05_TARGETED_EVIDENCE_MATRIX.csv | không ghi | ma trận | 12 bài Stage B × 25 cột, đã thêm 3 cột model_version_context, evidence_validity_scope, validity_scope_evidence. | Hết (13 dòng) | Còn hiệu lực | Là bản mã hóa sau hiệu chỉnh |
| 06_CORE5_EVIDENCE_MATRIX.csv | không ghi | ma trận | 5 bài CORE × 24 cột. | Hết (6 dòng) | Tham khảo | Cột validity_scope dùng định nghĩa cũ; vài ô lệch với bản đọc sâu (mục 6) |
| 01_ZOTERO_TARGETED_SCREENING.csv | không ghi | dữ liệu | 26 dòng sàng lọc Zotero, phân loại DEEP_READ / BACKGROUND / EXCLUDE. | Hết (27 dòng) | Lỗi thời một phần | Dòng NQ3KGDWN ghi pdf_available=NO, DEEP_READ_ABSTRACT_ONLY (01_ZOTERO:13), đã bị tệp 07 thay |
| PAPER2_GATE2_GATE3_FINAL_SUMMARY.md | không ghi | nhật ký | Thư viện cuối 199 bài = 174 + 25; MR0005 chưa giải quyết. | Hết (90 dòng) | Tham khảo | Chỉ là số liệu thư viện, không phải nội dung khoa học |
| PAPER2_ZOTERO_IMPORT_SUMMARY.md | không ghi | nhật ký | Đối chiếu 199 ứng viên với Zotero hiện có: 35 đã có, 164 mới. | Hết (108 dòng) | Tham khảo | Như trên |

Ghi chú về tệp trùng tiền tố: `05_CORE05…` và `05_TARGETED_EVIDENCE_MATRIX`, `06_CORE5_EVIDENCE_MATRIX` và `06_TARGETED_GAP_AUDIT`, `03_CORE03…` và `03_TARGETED_DEEP_READ_SELECTION`, `02_`, `01_`, `00_` đều có hai tệp cùng số đầu. Tệp 07 và 08 tham chiếu "file 05/06/07" theo nhóm TARGETED (07:212; 06:3).

## 2. Số liệu

Chỉ ghi số định lượng có trong tệp. Các số mà phạm vi khóa yêu cầu nguồn (6 IFC, 3.356 cấu kiện, 10.328 liên kết, 718/676 phần tử audit) KHÔNG xuất hiện ở bất kỳ tệp nào trong nhóm C1 (đã tìm bằng chuỗi 3.356 / 10.328 / 718 / 676).

### 2a. Số liệu về bài báo đã đọc (không phải số liệu BIM của NCS)

| Số liệu | Giá trị | Tệp + dòng/mục | Ngữ cảnh / mức xác nhận | Mâu thuẫn? |
|---|---|---|---|---|
| Số trang PDF CORE01 đã đọc | 32/32 | 00_BIBLIO:7 | Tệp 00 ghi "fully read" | Có nghi vấn: ITcon 30:603–630 chỉ 28 trang, còn tệp 01:80 nhắc "trang 629–632 / appx. 1–4" (vượt 630) |
| Số trang PDF CORE02/03/04/05 đã đọc | 17/17; 12/12; 20/20; 19/19 | 00_BIBLIO:8–11 | Như trên | Không |
| CORE01: số CQ | 13 CQ; từ 5 phỏng vấn, 6 chuyên gia | 01_CORE01:54 (mục Validation design), 01:63 | Theo tệp, p.606 §4.1 | Không |
| CORE01: số truy vấn SPARQL | 10 (data-integrated) + 2 (ICDD) = 12 | 01_CORE01:50,54 | Kết quả có trong Bảng 4–23 p.615–620 | Không |
| CORE01: dữ liệu minh họa | 15 điểm búa bật nảy + 2 điểm chụp tia, 1 cầu bộ hành | 01_CORE01:31 | Một mô hình BIM | Không |
| CORE01: số ontology tái dùng | 7 (BROT, BRCOMP, BRIDGE, BRSTR, DOT, BMAT, FOAF) | 01_CORE01:19,88 | p.611 Bảng 1 | Không |
| CORE02: câu hỏi nghiên cứu | 4 | 02_CORE02:9 | p.04022041-2 | Không |
| CORE03: số mô-đun CSDL | 6 | 03_CORE03:15 | Bảng 2 | Không |
| CORE04: sheet COBie | "10 trên 19" tự sinh; liệt kê thực tế 20 tên | 04_CORE04:9,24,77 | §5.3 p.6 | Có, nội bộ: 19 nêu, nhưng danh sách ở 04:24 gồm Instruction…PickList = 20 tên |
| CORE04: kiểm thử beta | 12 thành viên FM, 3 dự án, Likert 10 điểm | 04_CORE04:46 | Bảng 2 p.12 | Không |
| CORE05: số CQ dự án | 11 CQ (Use Case 1); 2 nhóm chuyên gia 5+6 | 05_CORE05:42,46; 06_CORE5 (hàng CORE-05) | p.11, p.15–16 | Không |
| CORE05: so sánh ontology trước | 4 ontology × 12 tiêu chí | 05_CORE05:9 | Bảng 1 p.4 | Không |
| Borkowski: quy mô ca nghiên cứu | 1 nhà ~120 m², 3 cấu kiện, 3 pha, 9 pha thể hiện, 27 thể hiện reification | 07:99,101 | Nhập tay | Nội bộ: "3 pha" (07:101) và "9 phases" (07:99) cùng tệp |
| Borkowski: hình thức hóa | 9 lớp, 6 quan hệ đối tượng + 1 quan hệ dữ liệu, 6 tiên đề; 8 CQ | 07:68,102 | CQ trả lời đúng 8/8 | Không |
| Borkowski: trang | 26 trang đã đọc | 07:3,31 | Qua Zotero MCP, mã CVGD2BLV | Không |
| Gragnaniello: quy mô | 1 cầu (110 m, 11 nhịp), 38 cảm biến; 2 gia tốc kế thiếu Accuracy, mã lỗi 301 | 10-A:38,40 | Số trang chỉ là ước lượng theo mục | Không |
| Mariniello: quy mô | 6 gia tốc kế 3 trục + 3 cảm biến nhiệt; 3 kịch bản; 50 lần lặp trên 10 cảm biến; 50–200 cảm biến | 10-B:38 | Theo Mục/Phụ lục | Không |
| Mariniello: chi phí | triển khai $2,76–2,95; giao dịch $0,17–0,37; 172–197 ms | 10-B:42 | | Không |
| García: quy mô | 22 tệp IFC2x3 thật, 2 dự án (El Campello 4 EX + 9 PC; Nazaret 9 EW); 14/22 (63,6%) HOLD | 10-C:26,38,40 | Kiểm nội bộ: 4+9+9=22; 14/22=63,6% đúng | Không |
| García: tỉ lệ đạt toàn bộ gate | 25,0–44,4% theo Case×State | 10-C:42 | | Không |
| García: loại bản ghi truy vết | 6 | 10-C:36 | | Không |
| Bellon: số tác giả | 6 ở dòng tiêu đề, 7 ở bảng thư mục | 10-D:3,10 | Tệp tự mâu thuẫn | Có, nội bộ |
| Bellon: mã OpenAlex | W4409166607 | 10-D:5 | Chỉ abstract | Không |
| Stage B | 12 bài (11 PDF + 1 abstract-only theo tệp 03; sau tệp 07 thành 12 toàn văn) | 03_TARGETED:3; 06_GAP:3 | | Có (03 vs 07) |
| Fang 2025 đã đọc | khoảng 28/31 trang | 05_MATRIX (hàng G1_01, cột validity_scope_evidence); 03_TARGETED:8 | Bỏ phần danh mục tài liệu cuối | Có: 06_GAP:3 nói "all 12 now full-text-read" |
| Kücükavci | 369.054 triple; 36 shape / 122 ràng buộc; 372→14 vi phạm; 3,1 s | 05_MATRIX (hàng G2_04); 06_GAP:37 | Bài ngoài nhóm CORE | Không |
| Kim 2018 | 590 bản ghi, 5 công ty, ~+200% bản ghi liên quan | 05_MATRIX (hàng MULTI_03) | | Không |
| Phân loại validity | 0 YES; 3 PARTIAL; 9 NOT_REPORTED (tổng 12) | 08_CORR:15–18 | Tôi đếm lại từ cột evidence_validity_scope của 05_MATRIX: 3 PARTIAL (Lorvão, Kim, PAV) và 9 NOT_REPORTED | Không (khớp) |
| Mức truy vết 5 bài CORE | L2; L1–2; L1; L1; L3 | các tệp 01–05, mục Traceability level; 06_CORE5 | | Có nhẹ: CORE02 "LEVEL 1–2" vs ma trận LEVEL_1 |

### 2b. Số liệu thư viện / sàng lọc

| Số liệu | Giá trị | Tệp + dòng/mục | Ngữ cảnh | Mâu thuẫn? |
|---|---|---|---|---|
| RIS trước đó + thêm = tổng | 174 + 25 = 199 | FINAL_SUMMARY:11–24 | Kiểm tính đúng | Không |
| Ca thủ công | 26 xem xét, 0 trùng, 25 thêm, 1 chưa giải quyết (MR0005) | FINAL_SUMMARY:15–18 | | Không |
| Ưu tiên | A1 = 18; A2 = 17 | FINAL_SUMMARY:21–22 | | Không |
| Bài 199 đều có DOI | 199 | FINAL_SUMMARY:20 | | Nhẹ: 05_MATRIX và 01_ZOTERO ghi "no DOI recorded" cho Stolk, Oraskari (thuộc pool khác, chưa rõ có nằm trong 199) |
| Zotero hiện có | 434 × 3 bản xuất giống hệt (SHA-256) = 1302; 415 bài duy nhất; 300 có PDF | IMPORT_SUMMARY:12–18 | | Không |
| Phân vùng 199 | 35 đã có + 164 mới + 0 kiểm tay = 199 | IMPORT_SUMMARY:32–37 | Kiểm tính đúng | Không |
| Ưu tiên của 164 bài mới | A1 = 8; A2 = 15; chưa phân loại = 141 | IMPORT_SUMMARY:41–45 | 8+15+141=164 đúng | Không |
| Pool nền GATE2_GATE3 | ">100" (bị cắt ở 100) | 02_EXCL:36 | | Không |
| Pool PAPER_2/RQ2/WP2 | 22 mục | 02_EXCL:9 | 8 deep-read + 10 nền + 3 loại = 21, thiếu 1 | Có: CSV 01 có 26 dòng; trừ 4 bài tìm qua đường khác = 22, gồm 8 deep-read + 11 nền + 3 loại. Tệp 02 ghi 10 nền, CSV có 11 |

---

## 3. Quyết định và mã treo

Không tìm thấy mã K1–K11, D003…D016, R01–R17, H* trong nhóm C1. Mã có trong nhóm này như sau.

| Mã | Nội dung | Tệp + dòng | Trạng thái |
|---|---|---|---|
| Gate 2 / Gate 3, RQ2 / WP2 | Định tuyến: Paper 2, Chương 5, phạm vi "Supporting", loại bằng chứng "Information traceability" | FINAL_SUMMARY:5–7; IMPORT_SUMMARY:5–7 | Đã ghi; chưa khớp với phạm vi khóa (mục 4) |
| GAP 1 / GAP 2 / GAP 3 | GAP1 bản ghi kiểm tra có trách nhiệm; GAP2 hiệu lực bằng chứng; GAP3 kiểm chứng xác định nhiều bước | 10-SUM:11,24–33; 10-A:44; 10-C:48 | Bị thay (theo phạm vi khóa: GAP1→G-B, GAP2→A2, GAP3 thành thiết kế đánh giá) |
| C1 / C2 / C3 | C1 khung truy vết 3 bản ghi; C2 hợp đồng quản trị bằng chứng; C3 giao thức kiểm chứng xác định | 10-SUM:37–43 | Bị thay bởi ĐG1–ĐG3; kết luận "GIỮ" của tệp chưa ánh xạ được |
| GAP-A … GAP-H | A định danh đã kiểm so với IFC (ESTABLISHED); B bền định danh qua phiên bản (PARTIALLY); C nguồn gốc bằng chứng (PARTIALLY); D hiệu lực (NOT_ESTABLISHED); E trách nhiệm hồ sơ (NOT_ESTABLISHED, "mạnh nhất"); F truy vết xuôi+ngược (PARTIALLY); G kiểm chứng đáp án kỳ vọng (ESTABLISHED); H thử lỗi cố ý (PARTIALLY) | 06_GAP:9–40; 08:20 | Treo theo CONDITIONAL_FREEZE; GAP-E chưa tính García (10-C:53) |
| CONDITIONAL_FREEZE | Trạng thái kho văn liệu, thiếu điều kiện "không còn mối đe dọa chưa đọc toàn văn" | 06_GAP:91–93; 08:22 | Treo. Lý do khác nhau giữa hai tệp: 06 nêu Stolk và Oraskari chưa kiểm lại tệp đính kèm; 08 nêu "11 mục còn lại" chưa kiểm trùng |
| SCOPE-BOUNDED FREEZE / FULL_FREEZE | Điều kiện chuyển FULL_FREEZE: (a) đọc toàn văn Bellon, (b) người hướng dẫn duyệt câu GAP1/C2 thu hẹp, (c) hoặc quyết định bỏ Bellon | 10-SUM:66–72 | Treo; (a) chưa làm, (b) chưa làm (10-SUM:70) |
| Quyết định GAP1/C2 thu hẹp | Câu đề xuất: trách nhiệm hồ sơ neo vào Condition_Evidence_ID do cảm biến, khác hồ sơ quản trị bàn giao mô hình | 10-SUM:27; 10-C:60 | Đề xuất, chưa áp vào MASTER LOCK |
| Final Decision RQ2 / Gate 2 / Gate 3 | cả ba: MINOR_REFINEMENT | 06_GAP:77–87 | Đã chốt trong tệp 06; không xét García/Bellon |
| P2-A … P2-G | Hướng bài, 10-SUM nói "không tìm thấy định nghĩa" trong MASTER LOCK | 10-SUM:47–49 | Không xác định (mã không có định nghĩa) |
| §2.2, §3, §4, §18, §22 của MASTER LOCK | Dẫn chiếu tới `PAPER2_GATE2_GATE3_MASTER_EXECUTION_LOCK_20260915.md` (instrument-vs-contribution; STOP list; quy tắc không "first study") | 10-A:50; 10-B:50; 10-C (không); 10-SUM:41,70,74 | Dẫn chiếu; tệp đích nằm ngoài nhóm C1 |
| Q1–Q12 | Bộ 12 câu cho từng bài kiểm độ mới | 10-A…D | Quy trình, không phải quyết định. Đánh số khác với Q1–Q10 trong 07 (xem mục 6) |
| CQ (các bài) | CORE01: 13 CQ; CORE05: CQ.1–11; Borkowski: CQ1–CQ8 (CQ8 = thứ tự pha); Lorvão: CQ10 (kết quả mới nhất) | 01:54; 05:42; 07:88,102; 05_MATRIX (hàng MULTI_02) | CQ của bài khác, không phải CQ01–12 của NCS |
| Level 1–4 truy vết | Thang mức truy vết dùng ở 5 deep read | 01:50; 02:42; 05:42 | Thang của người đọc; không có định nghĩa đầy đủ trong nhóm C1 |
| MR0003, MR0005 | MR0003 dùng năm Springer 2026; MR0005 DOI `10.3390/buildings15152633` thuộc bài "…Compliance Checking", đầu vào ghi "…Inspection" | FINAL_SUMMARY:30–34 | MR0005 treo (không nhập). MR0003 đã chấp nhận |
| Cấm làm (STOP) | "Do not import MR0005"; "Do not declare Gate 3 closed"; không suy luận chẩn đoán hay FEM từ metadata | FINAL_SUMMARY:86–90; IMPORT_SUMMARY:103–108 | Còn hiệu lực làm quy tắc quy trình |
| Sửa Zotero cho Jäkel | Khuyến nghị thêm Jan-Iwo Jäkel làm tác giả đầu của VC5ELKN2 | 00_BIBLIO:19 | Treo (chưa sửa; tệp ghi không sửa metadata) |
| Gộp bản trùng Borkowski | NQ3KGDWN (không PDF) và JSYCVGH9 (có PDF CVGD2BLV) | 07:5,23–27 | Đã giải thích, chưa gộp (cố ý để nguyên) |
| CW-1 (García) | Ma trận crosswalk theo thời gian khi BEP đổi | 10-C:42 | Chi tiết của bài García, không phải mã của NCS |

---

## 4. Điểm lệch so với phạm vi đã khóa

| Chiều | Tệp nói gì (trích ngắn + dòng) | Phạm vi khóa nói gì | Mức độ |
|---|---|---|---|
| Số thực thể | Chuỗi 5 định danh "Sensor_ID → BIM_GUID → Condition_Evidence_ID → Inspection_Record_ID → Action_Status" (01:70); "8 thành phần cốt lõi" (06_GAP:61; 07:195), 8 thành phần không được liệt kê ở đâu trong nhóm C1 | 6 thực thể: COMPONENT, SENSOR+SENSOR_MAPPING, EVIDENCE, INSPECTION_RECORD (qua EVIDENCE_USE), ACTION, STATUS_EVENT | Trung bình. Tên khác (Condition_Evidence, Action_Status); không có STATUS_EVENT hay EVIDENCE_USE |
| Công cụ | "ontology-formalized (RDF/OWL vs. a bespoke relational schema)" (03:54); "formal, verified, CQ-tested approach" (03:70); "ontology is not a required instrument" (06_GAP:48) | Python, IfcOpenShell, SQLite/JSON; KHÔNG RDF/SHACL/SPARQL/ontology | Cao ở 03:54 và 03:70 (đề xuất khác biệt bằng RDF/OWL). Thấp ở 06_GAP:48 (cùng hướng với phạm vi khóa) |
| Số CQ | Paper 2 được gợi ý định vị là "pre-registered expected-answer + denominator protocol" thay cho CQ (01:75,82; 05:55,75). Các bài khác dùng 13 CQ, 11 CQ, 8 CQ | 12 CQ gộp thành 3 câu hỏi truy ngược | Trung bình. Cách đo và đơn vị khác (đáp án kỳ vọng so với tỉ lệ bắt lỗi chèn mù) |
| Chỉ số | Không có M1–M4 trong nhóm C1. Chỉ có "pass/fail with denominators" (01:75; 05:65) | M2 = chỉ số chính (tỉ lệ bắt lỗi chèn mù theo nhóm); M1, M3, M4 | Trung bình. Thiếu hoàn toàn tên chỉ số |
| Đối chứng | Không có B0 hay B1 ở bất kỳ tệp nào của nhóm C1. Gần nhất: Bellon chỉ có abstract (10-D:17) | B0 = mã hóa tay 20–30 hồ sơ kiểm định VN; B1 = IFC 4.3 theo Bellon 2025 [35] + BCF 3.0 | Cao. B1 dựa vào bài chưa đọc toàn văn; nhóm C1 không xác nhận Bellon dùng IFC 4.3 (10-D:25 ghi chỉ "IFC schema-based") |
| Khoảng trống | Ba hệ nhãn cùng tồn tại: GAP 1/2/3 (10-SUM:11), GAP-A…H (06_GAP:9–40), và nhãn G-A/G-B của phạm vi khóa. Cụ thể "GAP-A" (06_GAP:11, định danh đã kiểm, ESTABLISHED) khác nghĩa với G-A (A1 đánh giá theo đơn vị độc lập; A2 phạm vi hiệu lực). "GAP-B" (06_GAP:15, bền định danh qua bản sửa) khác nghĩa với G-B (chuỗi bằng chứng→hành động có trách nhiệm). 06_GAP:31 coi GAP-E là "strongest surviving". 10-SUM:32–33 coi GAP3 "THU HẸP nhẹ, vẫn mở" | G-B chính, G-A/A2 phụ; GAP3 không còn là khoảng trống mà là thiết kế đánh giá | Cao. Trùng tên khác nghĩa dễ gây nhầm khi trích |
| Khoảng trống: tiêu chí không được rà | Không tệp nào chấm riêng "sự kiện chuyển trạng thái có căn cứ và đúng vai trò" (C6), "xác minh sau sửa chữa" hay "kiểm tại lần dùng" như một tiêu chí tiền lệ. Taxonomy 8 khoảng trống không có mục này (06_GAP:9–40). Tiền lệ liên quan nằm rải rác: García (10-C:34), Mariniello (10-B:30,34), Borkowski PhaseTransitionEvent (07:76,136) | RQ2.3 chuyển trạng thái (C6); xác minh sau sửa chữa là phần của G-B; A2 kiểm tại lần dùng | Cao. Nhóm C1 không đủ để kết luận độ mới cho C6 |
| RQ | RQ2/WP2 "Supporting" (FINAL_SUMMARY:7); 06_GAP:79 đề xuất MINOR_REFINEMENT cho RQ2 | RQ2 so B0, B1 qua M2; RQ2.1 (C1,C3), RQ2.2 (C5,C9), RQ2.3 (C6) | Thấp. Không mâu thuẫn trực tiếp, nhưng nhóm C1 không có RQ2.1–2.3 |
| Đóng góp | C1/C2/C3 (10-SUM:37–43); "8-component core contribution" (07:195) | ĐG1 mô hình 6 thực thể; ĐG2 hợp đồng bằng chứng + EVIDENCE_USE; ĐG3 STATUS_EVENT + giao thức lỗi chèn mù | Trung bình. C1≈ĐG1, C2≈ĐG2 một phần, C3 khác ĐG3 (C3 dựa kiểm chứng xác định) |
| Tạp chí đích | Không nêu trong nhóm C1 | Không rõ trong BRIEF | Không áp dụng |
| Số lỗi chèn | Không có "~30". Có taxonomy 7 loại cố ý: orphan, duplicate, stale, wrong revision, conflicting, mismatched, out-of-validity (10-C:40; 10-SUM:33; 01:58; 05:50). Không nhắc "người chèn khác người viết luật" | ~30 lỗi chèn mù, 4 nhóm (định danh-liên kết; phiên bản; ngoài phạm vi; chuyển trạng thái không căn cứ); người chèn ≠ người viết luật | Trung bình. 7 loại của tệp không khớp 4 nhóm; thiếu nhóm "chuyển trạng thái" |
| Neo định danh | Tệp lặp lại yêu cầu "xác minh GUID so với IFC xuất thật" (01:71; 05:63) | Neo kép đối chiếu IFC xuất thật (C1, C3) | Khớp (không lệch) |
| Phạm vi hiệu lực | Định nghĩa chặt: valid-time, phạm vi áp dụng, thay thế (08:13). Không bài nào có "kiểm tại lần dùng" | A2: bắt buộc, kiểm tại lần dùng | Thấp. Định nghĩa của 08 gần phạm vi khóa, nhưng không có tiêu chí "tại lần dùng" |
| Số liệu NCS | Không có 6 IFC, 3.356 cấu kiện, 10.328 liên kết, 718/676 | Cần nguồn | Không áp dụng cho nhóm C1 |

---

## 5. Tài sản đáng giữ (cho Pha 1) và thứ nên bỏ

Nên giữ:
- Bản chấm 5 CORE theo cùng khung (01–05) và ma trận 05_TARGETED, vì mỗi ô có kèm bằng chứng và cho thấy ai đã có gì. Dùng làm bảng tiền lệ cho tiêu chí (1)–(8) ở mục 7.
- Tệp 07 (Borkowski) vì có trích nguyên văn và phân loại rõ "lỗi chèn ở mức tiên đề, không phải mức ánh xạ định danh" (07:100,126). Dùng khi viết phần phân biệt với B1 và nhóm lỗi "định danh-liên kết".
- Phần García (10-C:34–40): RACI đầy đủ 5 trường, vòng sửa và nộp lại vR+1 với gate chạy lại, 14/22 HOLD. Đây là tiền lệ gần nhất cho C6 và cho nhóm "chuyển trạng thái", dù đối tượng là bàn giao mô hình.
- Phần Mariniello (10-B:30–40): alert → `resolveAlert` theo `AUTHORITY_ROLE`, `closedBy`; lỗi chèn (nhiễu, trùng hash, thao tác trái phép). Là tiền lệ cho C6 và cho thiết kế lỗi chèn, dù không neo BIM.
- Mẫu lỗi của Oraskari (FILTER NOT EXISTS, checksum trôi) và Lee (GUID trùng/sai khuôn) từ 05_MATRIX, hữu ích cho nhóm C9 (phiên bản) và C1. Đây là kỹ thuật, không dùng SHACL theo phạm vi khóa.
- 00_BIBLIOGRAPHIC_VERIFICATION: xác nhận CORE01 là Jäkel et al., cần giữ để tránh trích sai tác giả.
- Quy tắc chặn trong FINAL_SUMMARY (MR0005, không tuyên bố đóng Gate 3).
- Tệp 10-D làm danh sách việc phải làm: đọc toàn văn Bellon trước khi chốt B1.

Nên bỏ hoặc không dùng nguyên văn:
- Mọi câu "Implication for Paper 2" trong 01–05 và 07 (Paper 2 phải khác biệt bằng RDF/OWL, CQ, "pre-registered expected-answer", Action_Status). Lý do: ngược hoặc lệch phạm vi khóa (mục 4).
- Nhãn GAP 1/2/3, C1/C2/C3, GAP-A…H khi dùng cho Paper 2 mới. Lý do: trùng tên khác nghĩa với G-A/G-B.
- Kết luận "GAP-E mạnh nhất" (06_GAP:31; 08:20). Lý do: chưa tính García (10-C:53); cần chấm lại với đối tượng "bằng chứng cảm biến".
- Cột `validity_scope` của 06_CORE5 và mục "Validity scope" của 01–05 (định nghĩa cũ). Cần mã hóa lại theo định nghĩa chặt của tệp 08 trước khi dùng.
- Số liệu thư viện (199, 164, 35…) cho nội dung bài. Chúng chỉ là số kiểm kê Zotero.

---

## 6. Ghi chú bất thường

### 6A. Hai câu hỏi kiểm riêng

**(i) Bản đọc sâu có ghi số trang thật không?**

| Bài | Có số trang? | Nhận xét |
|---|---|---|
| CORE01 Jäkel 2025 | Có, số trang in (p.604–626, Bảng 4–23 ở p.615–620) | Có điểm lạ: bài nằm ở trang 603–630 nhưng tệp ghi "appendix pp. 629–632 … appx. 1–4" (01:80), vượt trang 630; PDF đọc 32/32 trang (00_BIBLIO:7) trong khi 603–630 chỉ 28 trang. Có thể phụ lục nằm ngoài khoảng trang, nhưng tệp không giải thích. |
| CORE02 Hagedorn 2023 | Có, dạng 04022041-N | Thứ tự hình–trang lộn xộn: Hình 12 ở trang -12 (02:24), Hình 9 ở trang -11 (02:30; 02:79), nhưng các Hình 13–16 ở trang -10 đến -11 (02:80); trong khi Hình 4 và 7 ở trang -8 đến -9 (02:78) và Use Case nằm trang -8 đến -11 (02:70). Hình 12 không thể ở sau Hình 13–16. Cần đối chiếu với PDF. |
| CORE03 Yin 2020 | Có (p.4–10) | Không thấy mâu thuẫn trong tệp. |
| CORE04 Matarneh 2022 | Có (p.2–15) | Danh sách sheet COBie nêu 19 nhưng liệt kê 20 tên (04:24). |
| CORE05 Seiß 2025 | Có (p.4–16) | Không thấy mâu thuẫn. |
| Borkowski 2026 | KHÔNG. Chỉ có tên mục (Sec. 1, 2.2, 3.1–3.3, 4.1–4.3, 5.1–5.2) và "26/26 pages" | Các trích dẫn nguyên văn có mục nhưng không có trang. |
| Gragnaniello, Mariniello, García | KHÔNG. Chỉ Mục/Hình/Bảng/Phụ lục | 10-A:16 nói rõ "dùng số trang tạp chí ước lượng theo Section" nhưng thực tế không ghi số trang nào. Mariniello thừa nhận số liệu "do AI tổng hợp" (10-B:56). |
| Bellon 2025 | KHÔNG (chỉ abstract) | |
| 11 bài Stage B còn lại | KHÔNG (ma trận 05 không ghi trang) | Không kiểm được trong nhóm C1; tệp đọc sâu riêng (G1_01…) nằm ngoài nhóm. |

Kết luận: chỉ 5 bản đọc sâu CORE có số trang, và trong đó CORE01, CORE02 có điểm cần đối chiếu với PDF. Số trang của CORE chưa thể coi là đã xác minh bởi người kiểm toán (không có PDF trong thư mục text). Mọi trích dẫn có trang cho Borkowski, A, B, C phải bổ sung từ PDF.

**(ii) Mâu thuẫn giữa bản đọc sâu và bản kiểm độ mới (García 2026, Bellon 2025)?**

Không có mâu thuẫn trực tiếp kiểu "hai tệp nói ngược nhau về cùng một bài", vì García và Bellon KHÔNG xuất hiện ở bất kỳ bản đọc sâu hay audit nào của nhóm C1 (đã tìm trong 05_MATRIX, 06_GAP, 07, 08). Có bốn vấn đề liên quan:

1. Khoảng trống về độ phủ. Tệp 06 và 08 (đọc sâu sau hiệu chỉnh) khẳng định GAP-E (trách nhiệm hồ sơ) "mở và mạnh nhất, xác nhận vắng trong cả 12 bài" (06_GAP:31; 08:20) (06 chỉ nêu điều kiện FULL_FREEZE (iii) là "not fully satisfied" vì lý do khác, xem điểm 2). Trong khi tệp 10-C cho García có RACI đủ 5 trường, thực nghiệm trên 22 tệp IFC, đe dọa HIGH, buộc thu hẹp GAP1 (10-C:48–53; 10-SUM:25–27). Hai kết luận không loại nhau (đối tượng khác: bàn giao mô hình và hồ sơ kiểm tra tình trạng), nhưng 06 và 08 chưa cập nhật. Nếu chỉ đọc 06/08 thì sẽ ghi sai "trách nhiệm hồ sơ chưa tồn tại".
2. Điều kiện FULL_FREEZE bỏ sót Bellon. 06_GAP:93 và 08:22 cho thiếu điều kiện vì Stolk, Oraskari hoặc "11 mục còn lại" chưa kiểm trùng đính kèm, không nhắc Bellon, bài duy nhất được ghi rõ là mối đe dọa chưa đọc toàn văn (10-D:56; 10-SUM:68–72). Điều kiện (iii) ở 06:93 vì vậy đã yếu hơn thực tế.
3. Bellon bị mô tả khác nhau giữa các tệp ngoài nhóm C1. 10-D:17 ghi chỉ abstract và toàn văn bị CAPTCHA chặn; `G2_G3_ROUND4_..._20260809.md:259` ghi "paywalled", còn `G2_G3_RECENT_EVIDENCE_SCREENING_2023_2026.md:13` ghi Bellon (NUTL57KJ) "đã deep-read trong Round 1–2" và `G2_G3_SCREENING_EVIDENCE_AND_GAP_REPORT.md:14,26` mô tả "IFC 4.3.2.0, có implementation". Ngoài ra 10-D:15 ghi bài là truy cập mở dạng hybrid (CC BY-NC-ND) nên "paywalled" có thể không chính xác. Việc này cần người kiểm toán nhóm khác xác nhận; ở đây chỉ ghi lại.
4. Phạm vi khóa dùng Bellon làm cơ sở cho B1 ("IFC 4.3 theo Bellon 2025 [35]"). Trong nhóm C1 chỉ có abstract, và 10-D:25 nói "IFC schema-based" mà không nêu 4.3. Nên B1 đang dựa trên nội dung chưa được xác nhận trong nhóm C1.

Ngoài ra `PAPER2_REFINED_DIRECTION…25092026.md:356` nhắc "García (2026b)" (Zotero ZNSZE47J) là bài thứ hai chưa đọc. "García 2026" trong C1 chỉ là bài Applied Sciences 16(5) 2562, đừng nhầm với 2026b.

### 6B. Danh sách bất thường khác

1. Tên CORE01. Zotero VC5ELKN2 ghi "Heinlein et al." và thiếu tác giả đầu Jan-Iwo Jäkel (00_BIBLIO:17; 02_EXCL:44). PDF ghi Jäkel đầu, và tệp 01 dùng Jäkel. Tệp 00 ghi bước này "đảo ngược chỉ dẫn của NCS" ("Không dùng tên 'Jäkel et al.' từ ghi chú cũ", 00:19). Các tài liệu khác của dự án đang dùng "Jäkel et al. (2025)". Cần NCS xác nhận.
2. CORE02: tệp 00:24 nói Zotero có tác giả "Pauwels" nhưng danh sách tác giả PDF (00:8) không có Pauwels; tệp coi là "cosmetic". Tài liệu khác của dự án có "Hagedorn, Pauwels & König (2023)". Khả năng là bài khác hoặc lỗi metadata. Cần kiểm DOI.
3. Đánh số "Q" trùng: 07 dùng Q1, Q2, Q3, Q5…Q10 với nghĩa khác 10-A…D (ví dụ 07 Q2 = địa vị GUID; 10-x Q2 = chuỗi thông tin; 07 Q8 = liên kết sensor; 10-x Q8 = truy vết xuôi/ngược).
4. Ba hệ taxonomy cạnh tranh (GAP 1/2/3; GAP-A…H; G-A/G-B). Xem mục 4.
5. "6 trong 8 thành phần" (07:195; 06_GAP:61): tệp 06:61 liệt kê chỉ 5 thành phần cộng 1 mục tự động hóa định danh, và 8 thành phần không được định nghĩa ở đâu trong nhóm C1.
6. 10-SUM:47–49 nhắc "P2-A…P2-G" và nói MASTER LOCK không định nghĩa chúng: tham chiếu tới cấu trúc không tồn tại.
7. 03 ghi "11 PDF + 1 abstract-only" (03:3) và Borkowski "no PDF" (03:7); CSV 01 giữ pdf_available=NO cho NQ3KGDWN; 07 và 08 đã sửa. 03 và CSV chưa cập nhật.
8. Fang 2025 chỉ đọc ~28/31 trang (05_MATRIX hàng G1_01) nhưng 06_GAP:3 nói "all 12 now full-text-read" và 06:21 coi "full-text confidence".
9. Số đếm pool: tệp 02 nói 22 mục = 8 + 10 + 3 = 21 (02_EXCL:9–13); CSV 01 có 11 mục nền (01_ZOTERO các dòng 14–16,18–23,26–27). Thiếu 1.
10. Vài ô ma trận 06_CORE5 lệch bản đọc sâu: CORE-05 `model_version_context` PARTIAL nhưng 05:34 ghi "NOT REPORTED as tested"; CORE-05 cột CQ ghi PARTIAL dù có 11 CQ; CORE-03 forward_traceability NOT_REPORTED trong khi 03:42 mô tả duyệt GUI xuôi ở LEVEL 1; CORE-02 LEVEL_1 so với "LEVEL 1–2" (02:42).
11. Hiệu chỉnh validity (08) chỉ chạy lại cho 12 bài Stage B (08:13), không chạy cho 5 CORE. Mục "Validity scope" của CORE05 (PARTIAL, dung sai chất lượng) có thể bị hiểu là có tiền lệ.
12. Borkowski: "tracked across exactly 3 phases" (07:101) so với "9 phases" (07:99); và Zotero có hai bản (NQ3KGDWN, JSYCVGH9) với hai collection khác nhau.
13. Bellon: số tác giả 6 so với 7 (10-D:3,10).
14. García: DOI không có trong văn bản trích, chỉ suy từ số bài `applsci-16-02562` (10-C:12). Tệp 10-C:60 tự ghi cần đối chiếu DOI trước khi trích chính thức.
15. Mức "FULL_TEXT" của A, B, C là đọc qua NotebookLM (10-A:16; 10-B:56), không phải đọc PDF trực tiếp. Tệp tự thừa nhận; vẫn nên ghi riêng "FULL_TEXT qua công cụ", khác với CORE (đọc từng trang PDF, 00_BIBLIO:3) và Borkowski (Zotero MCP đọc trang, 07:3).
16. Mô tả bài Stolk và Oraskari "no DOI recorded" (03:13,14; 05_MATRIX), nhưng FINAL_SUMMARY:20 ghi toàn bộ 199 bài đều có DOI. Hai nhóm tệp có thể thuộc tập khác nhau.
17. Dữ liệu ngày: hầu hết tệp không ghi ngày. Không thể xác định thứ tự giữa 06/07/08 và 10-* chỉ từ nội dung. 10-SUM (16/09) nhắc Borkowski GAP-B "đe dọa" (10-SUM:59) khớp với 07, nên 07 hẳn có trước 16/09, nhưng đây là suy luận.

---

## 7. Bảng bài

Nguyên tắc: chỉ ghi theo tệp trong nhóm C1. Không bổ sung từ trí nhớ. "Trang?" = tệp có dẫn số trang hay không. 8 tiêu chí: (1) bằng chứng cảm biến/NDT; (2) neo định danh BIM đối chiếu IFC xuất thật; (3) phạm vi hiệu lực bắt buộc; (4) kiểm tại lần dùng; (5) sự kiện chuyển trạng thái có căn cứ và vai trò; (6) xác minh sau sửa chữa; (7) đánh giá bằng lỗi chèn có đối chứng; (8) bối cảnh vận hành–bảo trì.

CORE01 là bài: Jäkel, Heinlein, Morgenstern, Kim & Klemt-Albert (2025), "System- and data-integrated linking of digital 3D models of existing bridge structures with Knowledge Graphs of non-destructive diagnostic methods", Journal of Information Technology in Construction (ITcon) 30:603–630, DOI 10.36680/j.itcon.2025.025, Zotero VC5ELKN2, ontology SODIA (01:5; 00_BIBLIO:7,17–19). Zotero hiện ghi "Heinlein et al." vì thiếu tác giả đầu Jäkel; PDF ghi Jäkel đầu.

### 7a. Danh tính, mức đọc, mức đe dọa

| Tác giả-năm | DOI ghi trong tệp | Đã đọc toàn văn (theo tệp)? | Có số trang dẫn? | Kết luận mức đe dọa / độ mới với Paper 2 (theo tệp) |
|---|---|---|---|---|
| Jäkel et al. 2025 (CORE01) | 10.36680/j.itcon.2025.025 | Có, PDF 32/32 trang (00_BIBLIO:7) | Có (p.604–626) | Không có xếp hạng đe dọa bằng nhãn. 01:82 kết luận không thể tuyên bố độ mới cho "nối kết quả kiểm tra với cấu kiện bằng ontology + SPARQL". Còn khác biệt: không có hành động/bảo trì, không kiểm định danh, không thử lỗi định danh. LEVEL 2 |
| Hagedorn et al. 2023 (CORE02) | 10.1061/(ASCE)CP.1943-5487.0001051 | Có, 17/17 | Có (04022041-N), có điểm lệch thứ tự | Không xếp hạng. 02:72: không thể tuyên bố đầu tiên dùng PROV hay phiên bản gói thông tin; còn khác biệt ở mức cấu kiện và hành động đóng. LEVEL 1–2 |
| Yin et al. 2020 (CORE03) | 10.1016/j.tust.2019.103252 | Có, 12/12 | Có | Không xếp hạng. 03:70: không thể nói nối cấu kiện với bảo trì là chưa giải quyết; chính bài tự nhận chưa kiểm chứng thực tế (03:42). LEVEL 1 |
| Matarneh et al. 2022 (CORE04) | 10.1016/j.autcon.2022.104569 | Có, 20/20 | Có | Không xếp hạng. 04:73: không thể nói tự động hóa BIM→FM hay nối cấu kiện→nhiệm vụ bảo trì là mới. Kiểm bằng Likert, không kiểm tính đúng. LEVEL 1 |
| Seiß et al. 2025 (CORE05) | 10.1016/j.autcon.2025.106268 | Có, 19/19 | Có | Không xếp hạng bằng nhãn; 05:75 gọi là "single closest paper… strongest threat" cho truy vết thông tin và neo định danh (GlobalId thật). LEVEL 3. Thiếu: hành động/đóng vòng, xác minh định danh, thử lỗi định danh |
| Borkowski et al. 2026 | 10.3390/technologies14070413 | Có, 26/26 trang (07:3) qua Zotero MCP | KHÔNG (chỉ tên mục) | HIGH, hẹp ở nhánh bền định danh qua pha (07:195; 06_GAP:57). Không đạt VERY_HIGH vì ghép định danh thủ công, không có trách nhiệm, không có thử lỗi ánh xạ |
| Gragnaniello et al. 2024 (10-A) | 10.1016/j.autcon.2023.105245 | Có, qua NotebookLM (FULL_TEXT) | KHÔNG (Mục/Hình) | LOW (10-A:48): công cụ thiết lập SHM, IDS; không chạm GAP 1/2/3 |
| Mariniello et al. 2025 (10-B) | 10.1016/j.autcon.2025.106558 | Có, qua NotebookLM | KHÔNG (Mục/Phụ lục) | MEDIUM (10-B:48): một phần C3 (PASS/FAIL, lỗi âm tính), không chạm C1 vì thiếu định danh BIM. Q3 = EVIDENCE_INSUFFICIENT |
| García et al. 2026 (10-C) | 10.3390/app16052562 (suy từ số bài; DOI không hiện trong văn bản, 10-C:12) | Có, qua NotebookLM | KHÔNG (Mục/Bảng/Hình) | HIGH hẹp (10-C:48): mẫu bản ghi có trách nhiệm đủ 5 trường đã triển khai trên 22 tệp IFC thật; chuỗi 6 loại bản ghi; không có cảm biến/tình trạng; không có hiệu lực bằng chứng |
| Bellon et al. 2025 (10-D) | 10.1016/j.autcon.2025.106157 | KHÔNG. Chỉ abstract (OpenAlex), toàn văn bị CAPTCHA chặn (10-D:17) | KHÔNG | MEDIUM do trùng chủ đề; không xác định được nội dung (10-D:49–56). Rủi ro chưa đóng |
| Fang et al. 2025 | 10.3390/buildings15224096 | Một phần, ~28/31 trang (05_MATRIX) | KHÔNG | MEDIUM (05_MATRIX): kiểm GUID trong một bước chuyển đổi |
| Lee, Eastman, Solihin 2021 | 10.1093/jcde/qwaa064 | Có, "complete" (03_TARGETED:9) | KHÔNG | HIGH (05_MATRIX): tiền lệ gần nhất cho kiểm GUID có ca âm tính |
| Lorvão Antunes et al. 2024 | 10.1016/j.iswa.2024.200366 | Có, "complete" (03_TARGETED:10) | KHÔNG | HIGH (05_MATRIX): đối thủ kiến trúc gần nhất; tự nhận ghép thủ công ontology-ifcOWL |
| Kim et al. 2018 | 10.1016/j.autcon.2017.12.019 | Có, "complete" (03_TARGETED:11) | KHÔNG | HIGH (05_MATRIX): nối bản ghi FM với đối tượng IFC; dùng mã STEP nội bộ, không GUID |
| Sacks et al. 2018 | 10.1016/j.autcon.2018.02.033 | Có, "complete" (03_TARGETED:12) | KHÔNG | MEDIUM (05_MATRIX): IDM/MVD cho kiểm tra cầu |
| Stolk & McGlinn 2020 | không ghi (03_TARGETED:13) | Có, "complete" | KHÔNG | MEDIUM (05_MATRIX): SHACL kiểm lược đồ nội mô hình |
| Oraskari et al. 2021 | không ghi (03_TARGETED:14) | Có, "complete" | KHÔNG | HIGH (05_MATRIX): tiền lệ mạnh nhất cho thử lỗi định danh và băm kiểm trôi phiên bản |
| Kücükavci et al. 2024 | 10.3233/SW-243595 | Có, "complete" (03_TARGETED:15) | KHÔNG | HIGH (05_MATRIX): SHACL quy mô thật, đo định lượng |
| Beach et al. 2015 | 10.1016/j.eswa.2015.02.029 | Có, "complete" (03_TARGETED:16) | KHÔNG | MEDIUM (05_MATRIX) |
| Ciccarese et al. 2013 (PAV) | 10.1186/2041-1480-4-37 | Có, "complete" (03_TARGETED:17) | KHÔNG | HIGH (05_MATRIX): từ vựng vai trò tác giả/hiệu đính/thay thế dùng chung, ngoài BIM |
| Wan et al. 2019 | 10.3390/su11174583 | Có, "complete" (03_TARGETED:18) | KHÔNG | HIGH (05_MATRIX): hệ BMS thật, vai trò duyệt chỉ mô tả bằng lời |

Ghi chú: mục "đã đọc" của 11 bài Stage B cuối bảng chỉ dựa vào tệp 03 và ma trận 05. Các tệp đọc sâu riêng của chúng nằm ngoài nhóm C1 nên tôi không kiểm lại.

### 7b. Tám tiêu chí

Mỗi ô: giá trị và căn cứ (tệp:dòng, hoặc Mục/Trang trích từ tệp). Ô "K" cũng cần căn cứ: tệp ghi NOT REPORTED hoặc không nhắc.

| Bài | (1) cảm biến/NDT | (2) neo định danh đối chiếu IFC xuất thật | (3) phạm vi hiệu lực bắt buộc | (4) kiểm tại lần dùng | (5) chuyển trạng thái có căn cứ + vai trò | (6) xác minh sau sửa chữa | (7) lỗi chèn có đối chứng | (8) vận hành–bảo trì |
|---|---|---|---|---|---|---|---|---|
| Jäkel 2025 | MP: kết quả NDE tĩnh (búa bật nảy, chụp tia), không phải dòng cảm biến (01:31; Query 01 p.615–616) | MP: GUID chỉ là thuộc tính, URI do bộ chuyển đổi sinh (Bảng 3 p.615); linkset ICDD buộc GUID thật bằng StringBasedIdentifier (p.622 §5.3.1); không kiểm so với tệp xuất (01:27,71) | K (01:46) | K | K: không có lớp hành động (01:33); chỉ Evaluation | K | MP: một thử luật miền (Query 02 p.616–617: chụp tia cần 2 lối vào); không có lỗi định danh, không đối chứng (01:58) | MP: chẩn đoán cầu, không có bảo trì (01:33) |
| Hagedorn 2023 | MP: bản ghi CSDL đo định kỳ mặt đường, không phải cảm biến (02:23) | K: URI do bộ chuyển đổi, GlobalId không bàn (02:19) | K (02:38) | K | MP: mã trạng thái ISO 19650 cho cả container (p.-6, 02:34) và PROV `wasAssociatedWith` (p.-12, 02:24); không phải chuyển trạng thái của bằng chứng | K: kế hoạch bảo trì chưa phải hành động đã thực hiện (02:25,61) | K (02:50) | C: quản lý tài sản, kiểm tra và kế hoạch bảo trì (02:9,24–25) |
| Yin 2020 | C: bảng giám sát Sensor ID, Location (p.8 Bảng 2; 03:23) | K: E/P ID không nói quan hệ với GlobalId (03:19) | K (03:36) | K | MP: bảng Maintenance có Maintenance staff ID + Date (p.8; 03:25), chỉ là lược đồ; không nối cảnh báo với dòng bảo trì (03:26) | K (03:26,63) | K (03:50) | C: O&M hầm tiện ích (03:9) |
| Matarneh 2022 | K (04:23) | K: theo số dòng STEP (p.7), không bàn GUID (04:19) | K (04:38) | K | K: Job gán theo Type, chỉ phân quyền vai trò (p.6, p.8; 04:25,30) | K (04:25,62) | K: đánh giá bằng Likert, không kiểm tính đúng (p.12; 04:46) | C: FM, CAFM/CMMS (04:9) |
| Seiß 2025 | MP: căn chỉnh SOSA/SAREF có thiết kế (p.9 Hình 7), ca thực dùng đo thủ công (05:23) | MP: GlobalId thật làm khóa (p.11 Bảng 4; p.13), không kiểm so với tệp xuất, không bàn trùng (05:19) | K, theo định nghĩa chặt: dung sai chất lượng không phải phạm vi hiệu lực (05:38; ma trận cũ xếp PARTIAL) | K | K: trạng thái chỉ của quá trình kiểm tra (05:25) | K (05:62) | K: không có lỗi chèn, không đối chứng (05:50) | K: QA xây dựng (05:9), không phải O&M |
| Borkowski 2026 | K: không có cảm biến (07:162) | MP: GUID gốc làm `hasIFCGuid` từ 3 IFC xuất thật (Sec. 3.3, 4); ghép định danh thủ công, không đo độ chính xác (07:104,183) | K (07:144–148) | K | MP: `PhaseTransitionEvent` không ghi ai/gì gây ra (07:76,136) | K | MP: một thử tiên đề rời nhau ở mức lược đồ (Sec. 5.1; 07:100,126); không đối chứng | MP: pha FM; vết nứt và gia cố CFRP chỉ là đổi giá trị thuộc tính (07:159–160) |
| Gragnaniello 2024 | MP: IfcSensor ở giai đoạn thiết kế/lắp đặt, không có dữ liệu quan trắc (Q2) | C: GlobalId thật `28xt…` trên IFC4x3 xuất thật (Mục 3.2, 4; Hình 5, 9; Q3) | K (Q6) | K | K cho bằng chứng: chỉ trạng thái CDE của mô hình và vai trò quy trình (Q4, Q7) | K | MP: thiếu thuộc tính `Accuracy` ở 2 gia tốc kế, mã 301 (Mục 4.2; Hình 10; Q10); chỉ một loại lỗi, không đối chứng | K: giai đoạn thiết kế/lắp đặt (Q2) |
| Mariniello 2025 | C: gia tốc kế và nhiệt độ thực địa cầu Canalone (Q9) | ?: EVIDENCE_INSUFFICIENT (Q3) | K (Q6); bất biến blockchain ≠ hiệu lực | K: DQC kiểm lúc nạp dữ liệu, không phải lúc dùng (Q2, Q9) | MP: Alert giải quyết bởi `AUTHORITY_ROLE`, `closedBy`; thiếu người duyệt và thay thế (Q5, Q7; Phụ lục A.3) | K (Q7) | MP: nhiễu chèn cố ý (Scenario 3), trùng hash, thao tác trái phép (Q10; Mục 4.2.1); do tác giả chèn, chưa neo BIM, không đối chứng như B0/B1 | MP: SHM/Digital Twin vận hành; không có bản ghi bảo trì (Q2) |
| García 2026 | K: không có dữ liệu cảm biến (Q2) | MP: mã container + revision + băm tệp; mã FU/UT ở cấp phần tử; không nêu GlobalId (Q3; Mục 3.1, 3.3; Bảng 6); 22 IFC2x3 thật | K (Q6) | K: gate chạy lúc xuất bản mô hình, không phải lúc dùng bằng chứng (Q2) | C với đối tượng khác: quyết định publish/hold, RACI đủ 5 trường, NCR/BCF Open→Close (Q7; Bảng 6–7; Hình 5–6); đối tượng là bàn giao mô hình, không phải bằng chứng hư hỏng | MP: sửa và nộp lại vR+1, gate chạy lại từ đầu, bản cũ chuyển Archived (Q4; Mục 3.5–3.7); đối tượng mô hình | MP: lỗi tự nhiên của dữ liệu thật (14/22 HOLD; Q10); không chèn lỗi, không đối chứng | MP: bàn giao PIM→AIM cho O&M kho đường sắt (Q1) |
| Bellon 2025 | ? (abstract: chưa tích hợp thu thập tự động, 10-D:43; suy ra có thể K) | ? (Q3) | ? (Q6) | ? | ? (Q7) | ? | ?: abstract chỉ nói "IFC schema verification and semantic evaluation", không rõ phương pháp (Q9, Q10) | C theo abstract: biểu diễn kiểm tra, hư hại, bảo trì, chi phí trong FM (Q1) |
| Fang 2025 | K | MP: cổng tuân thủ IfcGUID khi chuyển BIM sang game engine, một bước chuyển đổi (05_MATRIX hàng G1_01) | K | K | K | K | K (invalid_link_tests = NOT_REPORTED) | K |
| Lee 2021 | K | MP: quy tắc GUID duy nhất/khuôn/khứ hồi trong một chu kỳ xuất-nhập (05_MATRIX) | K | K | K | K | MP: ca âm tính GUID trùng/sai khuôn (05_MATRIX: YES), không rõ chèn mù hay đối chứng | K |
| Lorvão Antunes 2024 | MP: Agent vai trò Sensor, chỉ số 1–5 (05_MATRIX) | MP: `ifc:globalId_IfcRoot` qua chuỗi ifcOWL; ghép thủ công, bền qua bản sửa chưa bàn (05_MATRIX) | MP/K: chọn kết quả mới nhất bằng `prov:atTime` (CQ10), không phải quy tắc hiệu lực | K | K: không có người duyệt, người phê duyệt | K | K: chỉ kiểm lỗi soạn thảo OOPS! | C: AMS đường cao tốc |
| Kim 2018 | K: bản ghi nhật ký văn bản | K: mã STEP nội bộ, không GUID (05_MATRIX) | K: chỉ có trường Date | K | K | K | K | C: bản ghi công việc FM |
| Sacks 2018 | MP: đường ống phát hiện hư hại được hàm ý | K: không nhắc định danh | K | K | K | K | MP: 3 lớp lỗi tuân thủ (cú pháp, cấu trúc, thiếu), không phải lỗi chèn | MP: kiểm tra cầu |
| Stolk 2020 | K | MP: IfcGloballyUniqueId làm focusNode | K | K | K | K | MP: phát hiện giá trị enum sai và sai lớp, không phải chèn mù | K |
| Oraskari 2021 | K | MP: GUID đối chiếu hai bộ chuyển đổi (05_MATRIX) | K | K | K | K | MP: FILTER NOT EXISTS, băm kiểm trôi, kiểm trên hai bộ chuyển đổi; trong cặp chuyển đổi cùng một mô hình | K |
| Kücükavci 2024 | K | K: URI RDF không neo GlobalId (05_MATRIX) | K | K | K | K | MP: 372→14 vi phạm trên tòa nhà thật; vi phạm tự nhiên, không phải GUID | K |
| Beach 2015 | K | K: dựa lớp IFC, không dựa GUID | K | K | K | K | MP: xử lý "unknown" khi thiếu dữ liệu, so sánh với đánh giá thủ công | K |
| Ciccarese 2013 (PAV) | K | K: không áp dụng (tài nguyên, không phải cấu kiện BIM) | MP: `previousVersion`/`derivedFrom` thay thế; không có valid_from/valid_to (05_MATRIX) | K | MP: vai trò `authoredBy/curatedBy`; không có trạng thái phê duyệt | K | K | K |
| Wan 2019 | MP: chỉ số nứt có cấu trúc | ?: GUID ngầm, không bàn (05_MATRIX) | K | K | MP: quy trình thanh tra viên nộp, quản lý duyệt; chỉ mô tả bằng lời, không là trường lược đồ | MP: duyệt kết quả sửa chữa chỉ mô tả bằng lời (05_MATRIX) | K | C: BMS cầu dây văng thật |

Nhận xét tổng hợp rút từ bảng (không phản biện):
- Tiêu chí (3), (4) và (6): không bài nào có "C". Có MP duy nhất ở (3) là PAV và Lorvão (thay thế theo phiên bản/thời điểm); và ở (6) là García (chạy lại gate sau sửa, đối tượng là mô hình).
- Tiêu chí (7): không bài nào có đối chứng kiểu B0/B1 và không có lỗi chèn mù bởi người khác người viết luật. Gần nhất: Mariniello, Lee, Oraskari (lỗi chèn bởi tác giả, không đối chứng).
- Tiêu chí (5): có tiền lệ ở García (đối tượng mô hình) và Mariniello (cảnh báo), không có ở đối tượng "bằng chứng cảm biến + người giữ vai trò".
- Tiêu chí (2): chỉ Gragnaniello xác minh GlobalId trên IFC4x3 xuất thật (nhưng cho vị trí cảm biến, không phải bản ghi bằng chứng). CORE05 và Borkowski lấy GUID từ IFC thật nhưng không kiểm so với tệp xuất.
