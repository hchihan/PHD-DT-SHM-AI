# MỤC LỤC ĐỀ XUẤT — TIỂU LUẬN TỔNG QUAN (TÁI CẤU TRÚC THEO MẪU MỤC LỤC CÓ TRỤC)
**Phiên bản:** v2.0 | **Ngày:** 05/08/2026 | **Kiến trúc:** Limited-FEM / Traceability-Core v2.1
**Trạng thái:** ĐỀ XUẤT — CHỜ NCS PHÊ DUYỆT (chưa viết toàn văn)
**Kế thừa:** `OUTLINE_CHUYEN_DE_TONG_QUAN_CHI_TIET_v1.md` (18/07/2026) — không xóa, giữ làm bản lịch sử.
**Căn cứ:** Charter v2.1.1 (2026-08-04); RESEARCH_DIRECTION_AND_SCOPE v2.2; RESEARCH_ARCHITECTURE v2.2; CURRENT_STATUS_AND_NEXT_DIRECTION v2.2; MASTER G1-G2-G3 EVIDENCE SYNTHESIS 20260804; LIVING_EVIDENCE_BASE v2.1/v2.2; deep-read Round 1–3B; file mẫu "Tham khao muc luc TLTQ co TRUC.docx".

> Cách tổ chức kế thừa từ file mẫu: (i) phần dẫn nhập ngắn; (ii) các chương tổng quan theo **nhóm chủ đề** (không theo công nghệ); (iii) một chương **tổng quan tích hợp** có phương pháp review, đánh giá tập tài liệu theo thời gian/nguồn công bố/phân loại, và phân tích kết quả; (iv) kết luận; (v) phụ lục + tài liệu tham khảo. Chỉ kế thừa cách chia chương, không sao chép nội dung mẫu.

---

## PHẦN 1 — MỤC LỤC CHI TIẾT ĐỀ XUẤT

### Phần đầu
- Lời cảm ơn; Tóm tắt (Việt/Anh); Mục lục; Danh mục hình; Danh mục bảng; Danh mục từ viết tắt và thuật ngữ (kèm quy ước FEM: "mô hình phần tử hữu hạn tham chiếu danh nghĩa, chưa hiệu chuẩn, chỉ dùng tham khảo và không dùng để chẩn đoán hư hỏng").

### CHƯƠNG 1. PHẦN DẪN NHẬP
1.1. Bối cảnh quản lý tài sản nhà công nghiệp khung thép trong giai đoạn khai thác
1.2. Vấn đề nghiên cứu: đứt gãy chuỗi thông tin từ dữ liệu đo đến hồ sơ kiểm tra – hành động
1.3. Sự cần thiết của tổng quan và định vị ngành Quản lý xây dựng
1.4. Mục tiêu và câu hỏi tổng quan (CH-TQ1…CH-TQ7)
1.5. Phạm vi và giới hạn (Core / Supporting / Out-of-scope; firewall bốn lớp bằng chứng; nguyên tắc Limited-FEM)
1.6. Phương pháp thực hiện tổng quan (structured, corpus-bounded review: sàng lọc → deep-read Round 1–3B; cấu trúc Claim → Evidence → Limitation → Next action)
1.7. Cấu trúc tiểu luận

### CHƯƠNG 2. TỔNG QUAN VỀ QUẢN LÝ TÀI SẢN, KIỂM TRA – BẢO TRÌ VÀ SONG SINH SỐ DỰA TRÊN DỮ LIỆU
2.1. Quản lý tài sản công trình giai đoạn khai thác và nghĩa vụ kiểm tra – bảo trì – lưu hồ sơ
2.2. Từ bảo trì theo lịch đến kiểm tra – bảo trì dựa trên thông tin trạng thái (condition-informed inspection)
2.3. Quản lý thông tin công trình và định danh tài sản (ISO 19650-3; TCVN 14177:2024; bối cảnh pháp lý Việt Nam — pending official-source verification)
2.4. BIM, Digital Model, Digital Shadow và Digital Twin: phân biệt khái niệm
2.5. Mức trưởng thành của Digital Twin trong quản lý tài sản và bảo trì thông minh
2.6. Định nghĩa làm việc: song sinh số dựa trên dữ liệu ở cấp quản lý thông tin, hướng bằng chứng – kiểm tra; vị trí của mô hình phần tử hữu hạn tham chiếu danh nghĩa
2.7. Nhận xét chương và khung phân tích cho các chương sau

### CHƯƠNG 3. TỔNG QUAN VỀ DỮ LIỆU DAO ĐỘNG VÀ BẰNG CHỨNG TRẠNG THÁI
3.1. Giám sát trạng thái dựa trên dao động cho khung thép và liên kết bu lông
3.2. Dữ liệu có nhãn trong điều kiện thí nghiệm: trạng thái liên kết có kiểm soát, tổ chức lần đo (run) và siêu dữ liệu cảm biến
3.3. Rò rỉ dữ liệu và đánh giá theo lần đo (run-aware / LORO / grouped cross-validation)
3.4. Ảnh hưởng của cấu hình cảm biến so với lựa chọn kiến trúc mô hình (giả thuyết — candidate pending Gate 1)
3.5. Độ không đảm bảo khi số lần đo nhỏ: cỡ mẫu, mức ngẫu nhiên, kiểm định hoán vị và so sánh mô hình
3.6. Từ kết quả phân loại đến bằng chứng trạng thái: ranh giới classification / anomaly evidence / damage diagnosis và cấu trúc metadata CEI
3.7. Nhận xét chương: điều kiện để bằng chứng trạng thái đáng tin cậy trở thành đầu vào truy vết

### CHƯƠNG 4. TỔNG QUAN VỀ BIM/IFC VÀ TRUY VẾT HỒ SƠ KIỂM TRA – HÀNH ĐỘNG
4.1. Định danh cấu kiện bền vững: IFC GlobalId, bối cảnh Asset_ID @ Model_Version_ID và kiểm tra tính toàn vẹn định danh
4.2. Liên kết cảm biến – BIM và giám sát gắn mô hình thông tin
4.3. Hồ sơ kiểm tra và hồ sơ khiếm khuyết gắn BIM/IFC
4.4. Hồ sơ hành động, lịch sử trạng thái và xác minh sau hành động
4.5. Nguồn gốc dữ liệu (provenance), trách nhiệm giải trình và phê duyệt
4.6. Kiểm chứng mô hình truy vết: competency questions, ràng buộc thực thi được, bộ dữ liệu hợp lệ/không hợp lệ và truy vấn hai chiều
4.7. Nhận xét chương: ranh giới prior art và các thành phần chưa được xác lập trong corpus

### CHƯƠNG 5. TỔNG QUAN NGHIÊN CỨU TÍCH HỢP TỪ BẰNG CHỨNG TRẠNG THÁI ĐẾN HỖ TRỢ KIỂM TRA – BẢO TRÌ
5.1. Phương pháp đánh giá tập tài liệu tích hợp (corpus-bounded; tiêu chí Yes/Partial/No; quy tắc "không dùng future work làm bằng chứng")
5.2. Đánh giá tập tài liệu: phân bố theo thời gian, nguồn công bố, lớp bằng chứng và mức độ đọc
5.3. Giao thoa giữa ba nhóm chủ đề: ma trận thành phần truy vết × nghiên cứu (13 thành phần, Round 1–3B)
5.4. Điều kiện biên khả thi hiện trường: triển khai cảm biến chi phí thấp, baseline vận hành, biến động môi trường và dữ liệu khuyết
5.5. Hỗ trợ quyết định kiểm tra – bảo trì có con người rà soát: minh bạch, bốn mức hành động (đề xuất) và trách nhiệm giải trình
5.6. Ranh giới tri thức đã xác lập và khoảng trống trong phạm vi tập tài liệu (5 khoảng trống lõi + khoảng trống hỗ trợ)
5.7. Tính khả thi kiểm chứng của các khoảng trống (dữ liệu thu thập được, phương pháp kiểm chứng, sản phẩm đầu ra, thời gian – nguồn lực)
5.8. Khung nghiên cứu đề xuất xuyên suốt luận án: bốn lớp bằng chứng và chuỗi định danh khóa

### CHƯƠNG 6. KẾT LUẬN VÀ ĐỊNH HƯỚNG TRIỂN KHAI LUẬN ÁN
6.1. Trả lời các câu hỏi tổng quan
6.2. Tổng hợp khoảng trống nghiên cứu (corpus-bounded)
6.3. Câu hỏi nghiên cứu và gói công việc của luận án (RQ1–RQ3; WP1–WP4)
6.4. Cấu trúc luận án dự kiến và kế hoạch công bố (Paper 1–2 trụ cột; Paper 3 bonus; Paper 4 optional)
6.5. Đóng góp dự kiến và điều kiện bằng chứng (Evidence Gates G1–G7)
6.6. Giới hạn của tiểu luận tổng quan
6.7. Các bước nghiên cứu tiếp theo (ưu tiên hiện hành: đóng G1; quản trị đặc tả G2; chuẩn bị sẵn sàng G4)

### Phụ lục
- Phụ lục A. Ma trận bằng chứng (Evidence Matrix, trích từ Living Evidence Base v2.1, phân loại A–J)
- Phụ lục B. Bảng khoảng trống theo lớp nghiên cứu và điều kiện kiểm chứng
- Phụ lục C. Danh mục tài liệu với trạng thái toàn văn và trạng thái metadata (Available / Preprint / Partial / FULLTEXT_UNAVAILABLE / REVIEW NEEDED)
- Tài liệu tham khảo

---

## PHẦN 2 — MỤC TIÊU VÀ LOGIC CHUYỂN TIẾP GIỮA CÁC CHƯƠNG

| Chương | Mục tiêu | Chuyển tiếp sang chương sau |
|---|---|---|
| 1 | Xác lập vấn đề quản lý (không phải vấn đề chẩn đoán kỹ thuật), câu hỏi tổng quan, phạm vi, phương pháp | Nhu cầu quản lý → cần cơ sở lý luận về QLTS, kiểm tra – bảo trì và DT (Ch.2) |
| 2 | Hệ thống hóa nền tảng: nghĩa vụ quản lý hồ sơ, condition-informed inspection, phân biệt BIM/DM/DS/DT, mức trưởng thành, định nghĩa làm việc | DT dựa trên dữ liệu cần nguồn bằng chứng trạng thái tin cậy → lớp dữ liệu dao động (Ch.3) |
| 3 | Xác lập điều kiện để dữ liệu dao động trở thành bằng chứng trạng thái đáng tin cậy trong điều kiện thí nghiệm (run-aware, leakage-safe, uncertainty, CEI) | Bằng chứng chỉ có giá trị quản lý khi gắn được với cấu kiện và hồ sơ → lớp truy vết (Ch.4) |
| 4 | Tổng hợp prior art về định danh, liên kết cảm biến–BIM, hồ sơ kiểm tra, hồ sơ hành động, lịch sử trạng thái, trách nhiệm, xác minh và phương pháp kiểm chứng | Từng nhóm đã có prior art riêng → câu hỏi tích hợp toàn chuỗi (Ch.5) |
| 5 | Đánh giá tập tài liệu, xác định ranh giới tri thức và khoảng trống corpus-bounded, đánh giá khả thi kiểm chứng, đề xuất khung nghiên cứu | Khoảng trống + khung nghiên cứu → RQ, WP, kế hoạch triển khai (Ch.6) |
| 6 | Chốt câu hỏi nghiên cứu, gói công việc, cấu trúc luận án, kế hoạch công bố, đóng góp, giới hạn, bước tiếp theo | Kết thúc tiểu luận; đầu vào cho đề cương luận án |

Nguyên tắc xuyên suốt: các chương 2–4 chia theo **nhóm chủ đề của chuỗi nghiên cứu** (nền tảng quản lý → lớp bằng chứng → lớp truy vết), không chia theo công nghệ AI/BIM/FEM. FEM chỉ xuất hiện như mô hình tham chiếu danh nghĩa trong 2.6 và phần Limitation, không có chương/mục lớn riêng.

---

## PHẦN 3 — BẢNG NGUỒN HỌC THUẬT CHÍNH THEO TIỂU MỤC

Quy ước: chỉ dùng nguồn có trong Living Evidence Base v2.1 / Round 1–3B. "Vị trí bằng chứng" = mục trong Evidence Base hoặc báo cáo deep-read. Mức hỗ trợ: **Mạnh** (deep-read, full text, đúng nhận định) / **Trung bình** (deep-read nhưng khác miền hoặc gián tiếp) / **Nền tảng** (screened/background — chỉ dùng làm định hướng, không tuyên bố tính mới). Nguồn ghi "(tác giả–năm cần xác minh Zotero)" có title/DOI đã kiểm chứng nhưng author-year chưa ghi trong register — phải đối chiếu Zotero trước khi đưa vào bản thảo.

### Chương 2

| Tiểu mục | Nhận định cần hỗ trợ | Trích dẫn (Tác giả, năm) | Vị trí bằng chứng | Mức hỗ trợ |
|---|---|---|---|---|
| 2.1/2.3 | Nghĩa vụ quản lý thông tin và định danh tài sản giai đoạn khai thác | ISO 19650-3 (2020); TCVN 14177:2024 | LEB §F | Mạnh (chuẩn quy phạm) |
| 2.1 | Nghĩa vụ kiểm tra – bảo trì – hồ sơ theo pháp luật VN | Luật XD 135/2025; NĐ 207/2026; TT 32/2026 | LEB §F (VN-LEGAL) | **Chưa đủ — pending official-source verification** |
| 2.4 | Phân biệt BIM/DM/DS/DT | (Kritzinger và cộng sự, 2018); (Fuller và cộng sự, 2020); (Boje và cộng sự, 2020) | Gaps v1 §1 — đã có sẵn, cần xác nhận trạng thái đọc trong Zotero | Trung bình (chưa deep-read trong register v2.1) |
| 2.5 | Mức trưởng thành DT/bảo trì thông minh có thể tự định nghĩa minh bạch | Gemini Principles DT maturity (2021; ESTEYBHA — tác giả cần xác minh Zotero); Smart Maintenance Maturity (2021; YGZ32C8M — tác giả cần xác minh Zotero) | LEB §E, §C | Mạnh (deep-read) |
| 2.5 | Khái niệm và mức trưởng thành DT theo chuẩn | ISO/IEC 30173:2023; ISO/IEC 30186:2025 | LEB §F | Trung bình (**Partial** — chỉ có preview, cần bản đầy đủ) |
| 2.6 | DT ở cấp quản lý thông tin; FEM danh nghĩa reference-only | Lập luận từ Charter v2.1 §2.3 + RESEARCH_DIRECTION_AND_SCOPE §3 | Governance | Lập luận quản trị (không phải bằng chứng thực nghiệm) |

### Chương 3

| Tiểu mục | Nhận định cần hỗ trợ | Trích dẫn (Tác giả, năm) | Vị trí bằng chứng | Mức hỗ trợ |
|---|---|---|---|---|
| 3.1 | Tổng quan vibration-based SHM và giới hạn validation | (Avci và cộng sự, 2021) | LEB §A (QUGY4928) | Mạnh (review framing) |
| 3.1 | Tiền lệ phân loại liên kết bu lông khung thép | (Zhang, Biswal và Wang, 2020 — SHMnet) | LEB §A (YR2NQWE7) | Mạnh (tiền lệ, không phải chứng minh giao thức) |
| 3.1/3.2 | Phân loại nới lỏng nhiều bu lông; caveat chia cửa sổ | (Eraliev, Lee và Lee, 2022) | LEB §A (VVBGM9EN) | Mạnh |
| 3.2 | Tổ chức dataset có nhãn, metadata cảm biến, run lặp | (Valdez-Yepez và cộng sự, 2024) | LEB §A (HWUA93NT) | Mạnh (miền lân cận — jacket structure) |
| 3.3 | Leakage làm lạc quan hóa kết quả; nhóm theo nguồn trước khi cắt cửa sổ | Test-Training Leakage in ML for CBM (2024; M8LMWFQH — tác giả cần xác minh Zotero); Impact of Data Leakage in Vibration Signals (2024; RG9FMT8Y — tác giả cần xác minh Zotero) | LEB §A | Mạnh (direct) |
| 3.3 | LOGO/grouped CV so với K-fold | (Goodarzi và cộng sự, 2025); Impact of Choice of CV Techniques (2021; XE9XS6BQ — tác giả cần xác minh Zotero) | LEB §A | Mạnh / Trung bình (miền khác) |
| 3.3 | Holdout theo campaign/reassembly; so sánh cảm biến | (Ramasso và cộng sự, 2024) | LEB §A (RWHW6F9I) | Trung bình (**preprint** — xác nhận tình trạng bình duyệt) |
| 3.4 | Vị trí cảm biến/nguồn dữ liệu làm thay đổi kết quả biểu kiến (tới 0,47 error change) | Impact of Data Leakage in Vibration Signals (2024; RG9FMT8Y) | LEB §A | Mạnh (miền bearing; dùng làm cơ sở giả thuyết) |
| 3.4 | "Sensor configuration dominates architecture" | Kết quả lab của đề tài | Gate 1 | **Candidate claim pending Gate 1 closure — chỉ nêu như giả thuyết** |
| 3.5 | Cỡ mẫu và độ chụm; vượt mức ngẫu nhiên do mẫu nhỏ; so sánh mô hình | (Beleites và cộng sự, 2013); (Combrisson và Jerbi, 2015); (Demšar, 2006) | LEB §A | Mạnh (phương pháp, ngoài miền SHM) |
| 3.5 | Kiểm định hoán vị cho hiệu năng phân loại | (Ojala và Garriga, 2009/2010) | LEB §A (ZLFATP2Z) | Trung bình (**REVIEW NEEDED — xung đột phiên bản**) |
| 3.6 | CEI là cấu trúc metadata độ tin cậy (không phải severity/Health Index) | Charter v2.1 §7 + nguồn uncertainty (RG9FMT8Y; Beleites 2013; Combrisson & Jerbi 2015); modal-tracking uncertainty (Weil và cộng sự, 2025) | LEB §A, §G (L56P7RAF); CEI rule | Đề xuất của luận án — nêu là đề xuất, không phải khái niệm đã được chấp nhận |

### Chương 4

| Tiểu mục | Nhận định cần hỗ trợ | Trích dẫn (Tác giả, năm) | Vị trí bằng chứng | Mức hỗ trợ |
|---|---|---|---|---|
| 4.1 | GUID length/uniqueness và họ luật kiểm tra tham chiếu IFC/MVD | (Lee, Eastman và Solihin, 2021) | Round 1 §2.3 | Mạnh |
| 4.1 | IfcGlobalId được bảo toàn khi tích hợp BIM–CMMS | (Piras và cộng sự, 2026) | Round 3A §4 | Mạnh |
| 4.1 | Định danh cấu kiện là prior art nhưng thiếu chính sách ổn định qua phiên bản | (Mohamed và cộng sự, 2023) | Round 3B §2 | Mạnh |
| 4.2 | Liên kết cảm biến–BIM/IFC cho SHM | (Theiler và Smarsly, 2018); (Valinejadshoubi và cộng sự, 2019); (Rio và cộng sự, 2013) | Gaps v1 §1; PDF RQ1 folder | Trung bình (đã có full text; cần xác nhận mức đọc trong Zotero) |
| 4.2 | Cảnh báo theo ngưỡng định vị theo element-ID kích hoạt kiểm tra | (Deng và cộng sự, 2022) | LEB §C (GIIUUEW8) | Mạnh |
| 4.3 | Ontology nối inspection result với IFC GlobalId, 13 CQ, thực thi SPARQL | (Lorvão Antunes và cộng sự, 2024) | Round 1 §2.2; LEB §B (XUN8EX6X) | Mạnh (closest competitor) |
| 4.3 | IDM/MVD cho kiểm tra cầu; mô hình khiếm khuyết IFC | (Sacks và cộng sự, 2018); (Xu và cộng sự, 2022); (Isailović và cộng sự, 2020); (Wan và cộng sự, 2019) | Round 2 | Mạnh |
| 4.3 | Khung IFC inspection–maintenance rộng (đối thủ schema gần nhất) | (Bellon và cộng sự, 2025) | Round 1 §2.1 (NUTL57KJ) | **Chưa đủ — FULLTEXT_UNAVAILABLE (paywall)** |
| 4.3/4.4 | Cấu trúc hồ sơ khiếm khuyết/tình trạng/sửa chữa; trạng thái `completed` chỉ là scalar hiện tại | (Li và cộng sự, 2023) | Round 3A §3; LEB §C (4LKDXFMK) | Mạnh |
| 4.4 | History dạng danh sách báo cáo ≠ event history; repaired/unrepaired ≠ transition | (Mohamed và cộng sự, 2023) | Round 3B §2 | Mạnh |
| 4.5 | Provenance actor–operation–time–version; ranh giới với operational approval | (Celik, Petri và Barati, 2023) | Round 3B §3; LEB §B (EMTIHHX4) | Mạnh |
| 4.5 | Truy xuất hồ sơ công việc gắn object IFC | (đối chiếu VI5QMSAE, 2018 — tác giả cần xác minh Zotero) | LEB §B | Mạnh |
| 4.6 | Phân loại SCQ/VCQ/RCQ cho competency questions | Characterising Competency Questions (LSYSC59G — tác giả–năm cần xác minh Zotero) | LEB §C | Mạnh (phương pháp) |
| 4.6 | SHACL cho LBD; kiểm tra tương ứng IFC↔LBD | (Oraskari, Senthilvel và Beetz, 2021) | Round 1 §2.4 | Mạnh |
| 4.6 | Fixture hợp lệ/không hợp lệ có chủ đích; thiếu oracle máy-đọc-được | (Nuyts và cộng sự, 2024) | Round 3A §5 | Mạnh |
| 4.6 | Direct/inverse link validation bằng SHACL trên ICDD | (Hagedorn và cộng sự, 2023) | Round 3A §6 | Mạnh |

### Chương 5

| Tiểu mục | Nhận định cần hỗ trợ | Trích dẫn (Tác giả, năm) | Vị trí bằng chứng | Mức hỗ trợ |
|---|---|---|---|---|
| 5.3 | Không nguồn nào trong corpus nối stable identities với Status_Event, authorization, verification, closure/reopen và forward/reverse acceptance | Tổng hợp Round 1–3B | Master Synthesis §E; Round 3B §1 | Mạnh (corpus-bounded — không tuyên bố "first") |
| 5.4 | Tiền lệ quan trắc nhà khung thép; baseline bị chi phối bởi vận hành/môi trường | UCLA Factor Building (2006; 9823WXJZ — tác giả cần xác minh Zotero, file gợi ý Kohler 2005) | LEB §D | Mạnh (tiền lệ; không có chuỗi BIM/inspection) |
| 5.4 | Baseline theo nhiệt độ; ngưỡng động; dữ liệu khuyết chi phối đặc trưng hiện trường | Temperature-based baseline (2015; TRZY4P6X); Dynamic Threshold (2023; GE3XSAYV); Long-term HM missing data (2023; D3TGCKXW) — tác giả cần xác minh Zotero | LEB §D | Mạnh (miền cầu — cần chuyển vị thận trọng) |
| 5.4 | Cảm biến giá rẻ cần qualification theo ứng dụng; workflow MEMS hiện trường | Low-Cost Wireless Multinode (2023; LZPF7ILT — tác giả cần xác minh Zotero); (Armijo và Zamora-Sanchez, 2024) | LEB §D | Mạnh |
| 5.5 | Kiến trúc hỗ trợ quyết định quản lý SHM; quản trị con người trong bảo trì thông minh | (Chen và cộng sự, 2014); Smart Maintenance Maturity (2021; YGZ32C8M) | LEB §C | Trung bình / Mạnh |
| 5.5 | Bốn mức hành động Normal→Watch→Inspect→Priority | Đề xuất kiến trúc của luận án | Gaps v1 §3 | **Chưa có nguồn implement — nêu là đề xuất, kiểm chứng tại G5** |
| 5.6 | 5 khoảng trống lõi (linkage ổn định Inspection–Action; Status_Event append-only; actor-bound authorization; post-action verification + guarded closure/reopen; chuỗi identity–event–authorization–verification hoàn chỉnh) | Tổng hợp Round 1–3B | Master Synthesis §E | Mạnh (candidate contribution boundary, chưa phải đóng góp hoàn thành) |

### Chương 6

| Tiểu mục | Nhận định cần hỗ trợ | Trích dẫn (Tác giả, năm) | Vị trí bằng chứng | Mức hỗ trợ |
|---|---|---|---|---|
| 6.3–6.5 | RQ–WP–Chapter–Paper–Gate; bốn lớp firewall; trạng thái gate | Charter v2.1 §3–§9; Master Synthesis §B–§M | Governance | Mạnh (quản trị nội bộ) |
| 6.5 | Điều kiện đóng góp: G1 candidate claims; G2 chưa freeze; G3 chưa thực thi | CURRENT_STATUS v2.2 §1 | Governance | Mạnh |

---

## PHẦN 4 — DANH SÁCH HÌNH VÀ BẢNG DỰ KIẾN

### Hình
| Ký hiệu | Nội dung | Chương |
|---|---|---|
| Hình 1.1 | Chuỗi nghiên cứu đã khóa: dữ liệu dao động → bằng chứng trạng thái (+CEI) → cấu kiện BIM → hồ sơ kiểm tra → hồ sơ hành động → lịch sử trạng thái → xác minh → hỗ trợ quyết định | 1 |
| Hình 1.2 | Phạm vi Core/Supporting/Out-of-scope và firewall bốn lớp bằng chứng | 1 |
| Hình 1.3 | Quy trình tổng quan corpus-bounded (sàng lọc → deep-read Round 1–3B → CLOSE_SEARCH) | 1 |
| Hình 2.1 | Phân biệt BIM → Digital Model → Digital Shadow → Digital Twin | 2 |
| Hình 2.2 | Vị trí DT dựa trên dữ liệu ở cấp quản lý thông tin trong vòng đời tài sản | 2 |
| Hình 3.1 | Rò rỉ dữ liệu: random split so với run-aware/LORO (minh họa nguyên lý) | 3 |
| Hình 3.2 | Cấu trúc metadata CEI (7 thành phần tối thiểu theo Charter §7) | 3 |
| Hình 4.1 | Chuỗi định danh: Sensor_ID → BIM_GUID/Asset_ID@Model_Version_ID → Condition_Evidence_ID → Inspection_Record_ID → Action_Record_ID (Status_Event: candidate) | 4 |
| Hình 5.1 | Phân bố tập tài liệu theo năm công bố và lớp bằng chứng | 5 |
| Hình 5.2 | Khung nghiên cứu bốn lớp và ánh xạ RQ–WP–Paper–Gate | 5 |
| Hình 6.1 | Lộ trình ba dòng công việc song song: G1 closure — G2 specification — G4 readiness | 6 |

### Bảng
| Ký hiệu | Nội dung | Chương |
|---|---|---|
| Bảng 1.1 | Câu hỏi tổng quan và chương trả lời tương ứng | 1 |
| Bảng 2.1 | So sánh khái niệm BIM/DM/DS/DT theo nguồn | 2 |
| Bảng 2.2 | Các khung mức trưởng thành DT/bảo trì thông minh và giới hạn áp dụng | 2 |
| Bảng 3.1 | Tổng hợp nghiên cứu phân loại trạng thái liên kết: đối tượng, giao thức chia dữ liệu, kiểm soát leakage, cấu hình cảm biến | 3 |
| Bảng 3.2 | Nguồn phương pháp thống kê cho small-n (cỡ mẫu, chance level, permutation, so sánh mô hình) | 3 |
| Bảng 4.1 | Ma trận 13 thành phần truy vết × nghiên cứu deep-read (Yes/Partial/No — từ Round 1–3B) | 4 |
| Bảng 4.2 | Prior art đã xác lập so với thành phần chưa xác lập trong corpus | 4 |
| Bảng 5.1 | Đánh giá tập tài liệu theo lớp bằng chứng, mức đọc, trạng thái full-text | 5 |
| Bảng 5.2 | Bảng khoảng trống: Lớp nghiên cứu / Đã có / Chưa có / Khoảng trống luận án xử lý / Điều kiện kiểm chứng | 5 |
| Bảng 5.3 | Đánh giá khả thi từng khoảng trống (dữ liệu – phương pháp – sản phẩm – thời gian) | 5 |
| Bảng 6.1 | Ma trận RQ–WP–Chapter–Paper–Gate | 6 |
| Bảng 6.2 | Kế hoạch công bố và trạng thái Evidence Gate hiện hành | 6 |

---

## PHẦN 5 — CÁC PHẦN HIỆN CHƯA ĐỦ BẰNG CHỨNG

| Mục | Thiếu gì | Xử lý trong tiểu luận |
|---|---|---|
| 1.1 | Số liệu thống kê về thực trạng quản lý nhà công nghiệp khung thép tại Việt Nam | Viết định tính; ghi "Hiện chưa có đủ bằng chứng để kết luận" cho các nhận định định lượng |
| 2.1/2.3 | Văn bản pháp lý VN chưa xác minh nguồn chính thức (Luật 135/2025; NĐ 207/2026; TT 32/2026; QĐ 46/2026; CV 3839) | Ghi "Legal reference pending official-source verification"; không suy ngưỡng kỹ thuật từ luật |
| 2.4 | Kritzinger/Fuller/Boje chưa có record deep-read trong register v2.1 | Dùng làm nền tảng khái niệm; xác nhận metadata Zotero trước khi trích dẫn |
| 2.5 | ISO/IEC 30173 và 30186 chỉ có bản preview | Trích dẫn giới hạn ở điều khoản đã đọc; ghi chú Partial |
| 3.4 | "Sensor configuration dominates architecture" và các macro-F1 | Chỉ nêu giả thuyết — candidate claim pending Gate 1 closure |
| 3.5 | Ojala & Garriga xung đột phiên bản 2009/2010 | REVIEW NEEDED trước khi trích dẫn chính thức |
| 4.3 | Bellon et al. (2025) và Z4IBWW9Y (IFC defect) thiếu toàn văn; 3II2WKLN (ifcOWL-SHACL) chỉ có HTML | So sánh ở mức đã đọc được; ghi "Evidence is currently insufficient" cho so sánh field/entity |
| 4.6 | Hiệu quả thực nghiệm của phân loại SCQ/VCQ/RCQ | Nêu là phương pháp; hiệu quả empirical là future work của nguồn |
| 5.4 | Baseline vận hành cho nhà công nghiệp khung thép ven biển (corpus chủ yếu là cầu/tòa nhà) | Ghi rõ khoảng trống chuyển vị miền; thuộc G4 |
| 5.5 | Bốn mức hành động chưa có nguồn implement và chưa có validation | Nêu là đề xuất kiến trúc, kiểm chứng tại G5 |
| 5.6 | Mọi tuyên bố "chưa có nghiên cứu nào" | Bắt buộc dùng "Trong phạm vi tập tài liệu đã rà soát…" (CLOSE_SEARCH là corpus-bounded) |
| Ch.2 | DT maturity riêng cho industrial buildings | Hiện chưa có đủ bằng chứng để kết luận; dùng ESTEYBHA/YGZ32C8M làm khung gần nhất |

---

## PHẦN 6 — NHẬN XÉT TÍNH KHẢ THI CỦA CẤU TRÚC

**Claim:** Cấu trúc 6 chương khả thi để viết ngay bằng corpus hiện có, không cần mở lại tìm kiếm diện rộng.

**Evidence:** (i) Ch.3 có ≥15 nguồn deep-read lớp lab (LEB §A); (ii) Ch.4 có ≥16 nguồn deep-read lớp truy vết (Round 1–3B + LEB §B/§C); (iii) Ch.5 kế thừa trực tiếp ma trận thành phần, prior-art list và 5 khoảng trống lõi từ Master Synthesis 20260804 — phần phân tích tích hợp (mục 5.1–5.3) mô phỏng đúng cách tổ chức "phương pháp tổng quan → đánh giá dữ liệu → phân tích kết quả" của file mẫu; (iv) mọi mục tiêu chương khớp ánh xạ RQ–WP–Chapter–Paper–Gate v2.1; FEM không có chương/mục lớn riêng, đúng Limited-FEM.

**Limitation:** (1) Ch.1–2 là phần yếu nhất về bằng chứng (pháp lý VN chưa xác minh; DT khái niệm nền chưa deep-read trong register hiện hành); (2) corpus lớp truy vết chủ yếu là cầu/hạ tầng — cần chuyển vị thận trọng sang nhà công nghiệp; (3) một số nguồn thiếu author-year đã xác minh trong register (đánh dấu "cần xác minh Zotero") — phải đối chiếu trước khi viết bản thảo; (4) các con số Gate 1 chỉ được nêu như candidate.

**Next action:** (1) NCS phê duyệt/điều chỉnh mục lục này; (2) xác minh author-year các nguồn đánh dấu; (3) xác minh nguồn pháp lý chính thức cho 2.1/2.3; (4) sau phê duyệt mới viết toàn văn theo thứ tự Ch.3 → Ch.4 → Ch.5 (nhiều bằng chứng nhất) rồi Ch.2 → Ch.1 → Ch.6.

**Phân loại phạm vi:** Toàn bộ nội dung thuộc Core/Supporting scope theo Charter v2.1; không mở rộng sang chẩn đoán hiện trường, FEM hiệu chuẩn, suy giảm độ cứng, RUL, bảo trì dự báo, Health Index phức tạp, bảo trì tự động hoặc phần mềm thương mại.
