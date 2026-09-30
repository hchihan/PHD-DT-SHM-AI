# Changelog — Tiểu luận tổng quan v2 (nhánh `revision-v2`)

## Giai đoạn 0 – thiết lập (28/09/2026)

### Bước 1 – Thiết lập dự án
- Thư mục nằm trong repo Git có sẵn (`03_RESEARCH/01_PHD_DT_AI_AM`), nên không `git init`. Tạo nhánh `revision-v2` từ `master` (commit 076b899).
- Tạo thư mục `tieuluan/`, `matrix/`, `notes/`, `mapping/`, `revision/`, `figures/`.

### Bước 2 – Chuyển tiểu luận sang Markdown
- Nguồn: `HO_CHI_HAN_TIEU_LUAN_TONG_QUAN_23092026_HOANTHIEN.docx` (không sửa, không xóa).
- Công cụ: pandoc (GFM, không ngắt dòng). Tách thành `00_dau.md` (bìa, mục lục, danh mục bảng/hình, thuật ngữ, Dẫn nhập), `01_chuong1.md` … `05_chuong5.md`, `99_tailieu.md`.
- Kiểm tra đối chiếu với .docx:
  - Đề mục: 7 cấp 1, 35 cấp 2, 106 cấp 3 — khớp.
  - Bảng: 12 (4 bảng thuật ngữ + 8 bảng thân bài 2.1, 3.1, 4.1, 4.2, 5.1–5.4) — khớp; không bảng nào lệch cột.
  - Chú thích: 8 chú thích bảng + 4 chú thích hình — khớp.
  - Tài liệu tham khảo: 84 mục [1]–[84] — khớp.
  - Số từ: 40.214 (docx) / 40.190 (md); chênh 24 từ do ký hiệu thoát và neo liên kết.
  - Không có ký tự lỗi, không còn mã field Zotero.
- Mất định dạng:
  - Bốn hình vẽ bằng shape (Hình 1.1, 5.1, 5.2, 5.3) pandoc không chuyển. Đã cắt ảnh từ PDF do Word xuất, lưu `figures/Hinh_*.png`, chèn dòng ảnh ngay trước chú thích (kèm ghi chú HTML). Không đổi chữ nào của văn bản.
  - Liên kết số trang trong mục lục và danh mục bảng/hình trở thành liên kết neo; số trang không còn ý nghĩa trong Markdown.
  - Chữ đậm, nghiêng và chỉ số trích dẫn `\[n\]` giữ nguyên.
- Lỗi có sẵn trong bản gốc (ghi nhận, không sửa): mục 1.1.4, câu về QĐ 258/QĐ-TTg kết thúc bằng trích dẫn lặp "[12], [12], [12]".

### Bước 3 – Đối chiếu danh mục với Zotero (28/09/2026)
- Tạo collection `TL-Key` (PRGXUPFZ) với `Tier1` (H86TEIR4), `Tier2` (WVXRDFTI), `Bổ sung` (TKVJVWDZ, đang trống).
- Đối chiếu 84 tài liệu theo DOI, sau đó theo tiêu đề, trên bản sao chỉ-đọc của `zotero.sqlite`: 84/84 có trong Zotero, 60/84 có PDF. Kết quả: `matrix/doi_chieu_danh_muc.csv` (phân cách `|`, UTF-8 BOM).
- Gán Tier theo CLAUDE.md 7.1–7.2: 12 tài liệu vào `Tier1`, 15 vào `Tier2`. Gắn tag `Chuẩn` cho [1] ISO 19650-3, [61] SOSA, [62] SSN, [69] PROV-O.
- Tag K1, K2, K3, Đối tượng chưa tồn tại: Zotero chỉ tạo tag khi gắn vào tài liệu, và CLAUDE.md chưa quy định tài liệu nào mang các tag này.
- Tài liệu 2025–2026 (19 mục): kiểm tra DOI qua Crossref. 18 mục "chính thức" (có tập và trang/số bài); [11] NĐ 207/2026/NĐ-CP "không xác minh được" (không có DOI).
- Không nhập tài liệu mới vào Zotero; không sửa siêu dữ liệu tài liệu.
- Phát hiện cần NCS xử lý:
  - [17] Wu và cs. và [80] T. Bull và cs.: năm trong danh mục khác năm bản in (xem cột ghi_chu).
  - [68] PROV-DM có 2 bản ghi trùng trong Zotero; [69] PROV-O có 4 bản ghi trùng.
  - 7 tài liệu Tier1/Tier2 chưa có PDF: [22] Hemker, [28] Kamariotis, [35] Bellon, [42] Ramonell, [53] Kapoor & Narayanan, [57] Bull 2021, [80] Bull 2025.
  - Chỉ 3/84 bản ghi có citation key; cột `citekey` dùng dạng `zotero:<item key>` cho các mục còn lại.

## Phiên 29/09/2026 – bốn việc kỹ thuật

### Việc 1 – Tách 00_dau.md
- Tách thành `00_bia.md` (trang bìa), `00_thuatngu.md` (Giải thích thuật ngữ, nguyên văn), `00_dannhap.md` (từ "# DẪN NHẬP" đến hết).
- Xóa mục lục, danh mục bảng, danh mục hình (326 dòng, toàn bộ là dòng liên kết neo và 3 dòng tiêu đề danh mục); sẽ tạo lại khi xuất Word ở GĐ6.
- Kiểm tra: ghép 3 tệp mới với phần đã xóa trùng khớp từng ký tự với `00_dau.md`. Số câu theo từng phần: bìa 1, thuật ngữ 21, dẫn nhập 27 (tổng 49). 12 thẻ `<span id="TLTQ_...">` trong các chương giữ nguyên.
- Đã xóa `00_dau.md`.

### Việc 2 – CLAUDE.md mục 4.4 "Quy ước trích dẫn"
- Thêm mục 4.4 (số cũ `\[n\]` giữ đến hết GĐ5; tài liệu mới dạng `\[@KHÓA_ZOTERO\]`; dòng mới trong `doi_chieu_danh_muc.csv` với `so_cu = "moi"`; đánh số lại theo IEEE ở GĐ6; không sửa tay số trích dẫn).
- Cập nhật mục 5 (cấu trúc thư mục) theo tên tệp mới của phần đầu.
- Đưa CLAUDE.md vào Git (trước đó chưa được theo dõi).

### Việc 3 – CLAUDE.md mục 4.5 "Viết về giới hạn" và danh sách câu
- Thêm mục 4.5 (phân loại A/B/C, giọng văn khẳng định; là việc của GĐ5).
- Lập `revision/danh_sach_cau_gioi_han.csv`: 80 câu chứa "không chứng minh / không phải / không thay thế / không đồng nghĩa / không đủ" trong phần thuật ngữ, dẫn nhập và 5 chương (kể cả ô bảng).
- Nhãn đề xuất: A 43, B 13, C 24. Nhãn tự động được rà tay; 8 câu đổi nhãn, 7 câu có ghi chú (câu thuật lại kết quả tài liệu hoặc ô bảng — đề xuất giữ nguyên).
- Loại A vượt hạn mức 3–4 câu/chương ở Ch.1 (7), Ch.3 (8), Ch.4 (6), Ch.5 (18); cần NCS chọn câu giữ.
- Chưa sửa câu nào trong tiểu luận.

### Việc 4 – Tồn đọng GĐ0
- Sửa lỗi trích lặp ở mục 1.1.4 (`01_chuong1.md`): "\[12\], \[12\], \[12\]" → "\[12\]". Đây là thay đổi duy nhất trong văn bản tiểu luận ở phiên này.
- `doi_chieu_danh_muc.csv`: điền "không áp dụng (trước 2025)" cho 65 dòng trống ở cột `trang_thai_xuat_ban`; ghi chú [80] "cần sửa năm danh mục 2025 → 2026 theo bản in"; cập nhật ghi chú [12].
- Lập `revision/viec_ton_dong_GD0.md`: 7 tài liệu key thiếu PDF; bản ghi trùng [68] (2) và [69] (4) kèm đề xuất bản giữ lại (bản đang được trích trong .docx: B8QZMS77, FJJAV9T4), chưa gộp; [11] chờ NCS đối chiếu văn bản pháp luật.
- Chưa lưu `revision/nhap_5_8_pham_vi_ap_dung.md`: yêu cầu không kèm nội dung bản nháp.
- Cập nhật bảng Trạng thái tiến độ trong CLAUDE.md.

## Phiên 29/09/2026 (2) – chuẩn bị nguồn cho mục Công cụ AI (5.6A)

### Việc 0 – Lưu bản nháp mục 5.8
- Lưu nguyên văn bản nháp NCS cung cấp vào `revision/nhap_5_8_pham_vi_ap_dung.md` (7 đoạn). Chưa chèn vào Chương 5.

### Việc 1 – Kiểm kê Zotero các tài liệu phương pháp
- `revision/nguon_5_6A_kiem_ke.csv`: 9 tài liệu. DOI của 7 tài liệu mới được xác minh qua Crossref (tác giả đầu, tạp chí, tập, trang, năm khớp mô tả trong yêu cầu).
- Có trong Zotero (kèm PDF): Kiranyaz và cs. 2021 (IU5KZQEA), Avci và cs. 2021 (QUGY4928), Sohn 2007 [45] (MANJDQEZ), Keshmiry và cs. 2023 [46] (ESQIRHVE).
- Chưa có trong Zotero: Breiman 2001, Cortes & Vapnik 1995, He và cs. 2016 (CVPR, không có số tập), Varma & Simon 2006, Vabalas và cs. 2019.
- Chỉ dùng làm nguồn phương pháp; không lấy kết quả Paper 1.

### Việc 2 – Tìm và xác minh ứng viên G1–G6
- Consensus: 17 truy vấn (G1 3, G2 3 + 1 truy vấn kiểm gợi ý Figueiredo, G3 3, G4 3, G5 2, G6 2). Mỗi nhóm giữ tối đa 5 ứng viên.
- `revision/nguon_5_6A_ung_vien.csv`: 29 ứng viên; cả 29 được Crossref xác minh (tiêu đề, tác giả, năm, tạp chí, tập/trang, DOI). Không ứng viên nào bị loại vì không xác minh được.
- Các gợi ý của NCS đều khớp Crossref: Pathirage 2018, Figueiredo 2011, Cross/Worden/Chen 2011, Bull 2018 và 2019, Wang/Yan/Oates 2017, Abdeljaber 2017.
- Năm theo Crossref khác Consensus ở 5 bài (Wang & Cha, Shang, Maes, Hughes, Ismail Fawaz); CSV dùng năm Crossref.
- Đề xuất: 16 nhận (14 cần nhập Zotero; 2 đã có: Kiranyaz, Avci), 13 dự phòng (trong đó Pal [48] đã có trong danh mục). Đánh giá dựa trên tóm tắt, chưa đọc toàn văn.
- Không nhập Zotero, không sửa chương.

### Việc 3 – Báo cáo nguồn 5.6A
- `revision/bao_cao_nguon_5_6A.md`: bảng tổng hợp G1–G6; danh sách 14 tài liệu đề xuất nhập Zotero theo ưu tiên (tối đa 3/nhóm) cùng 4 tài liệu phương pháp của Việc 1; các nhóm chưa có nguồn đủ tin cậy cho một phần lập luận (G6 nhà công nghiệp, G1 nhà xưởng thép, G4 ResNet1D trong SHM, G3 công trình xây dựng).
- Cập nhật bảng Trạng thái tiến độ trong CLAUDE.md. Dừng chờ NCS duyệt danh sách trước khi nhập Zotero.

## Phiên 29/09/2026 (3) – nhập tài liệu 5.6A đã duyệt vào Zotero

NCS duyệt ĐD0; collection đích `TL-Key/Bổ sung`.

### Kiểm tra collection
- `TL-Key` (PRGXUPFZ) và `Bổ sung` (TKVJVWDZ, con của TL-Key) đã tồn tại; không tạo mới. Dòng "chưa tạo" trong `bao_cao_nguon_5_6A.md` là sai, đã ghi đính chính.

### Việc 1 – Nhập 13 tài liệu
- Kiểm tra trùng theo DOI và tiêu đề trên toàn thư viện: không bản nào có sẵn.
- Nhập theo DOI vào TL-Key/Bổ sung: Wang & Cha 2021 (TDRPDWJE), Ghazimoghadam & Hosseinzadeh 2024 (G98ZWHKW), Figueiredo 2011 (23TBQTIP), Cross 2011 (KPWFC4PI), Hughes 2022 (Z9RD5DMZ), Bull 2022 (87NKU5IS), Abdeljaber 2017 (HPREAQAJ), He 2016 (69U5H3TZ, conferencePaper), Wang/Yan/Oates 2017 (WXHN9TA2, conferencePaper), Breiman 2001 (5TQ4AZVX), Cortes & Vapnik 1995 (JVI2GUPC), Varma & Simon 2006 (D28DT7CE), Vabalas 2019 (6JAQQCGE).
- Tag: "5.6A" + nhóm G1–G5; bốn tài liệu phương pháp ngoài G1–G6 (Breiman, Cortes & Vapnik, Varma & Simon, Vabalas) mang tag "5.6A-phương pháp". Kiranyaz (IU5KZQEA) và Avci (QUGY4928) được gắn thêm "5.6A", "G5".
- Đối chiếu Crossref sau khi nhập; đã sửa: năm bản in Wang & Cha (2020-07-08 → 2021-01) và Figueiredo (2010-11-26 → 2011-11), ngày trực tuyến ghi ở Extra; tên kỷ yếu cho He 2016 và Wang/Yan/Oates 2017 (trống → theo Crossref); số trang/mã bài Varma & Simon (91), Bull 2022 (20210790). Vabalas có thêm một biên tập viên trong trường người tạo — đúng dữ liệu nhập, không phải lỗi.
- `matrix/doi_chieu_danh_muc.csv`: thêm 13 dòng `so_cu = moi`, `tier = bosung-5.6A`.

### Việc 2 – Dự phòng
- Thêm mục 5 "Dự phòng" vào `bao_cao_nguon_5_6A.md`: Bull 2018, Ismail Fawaz 2019, Zhang 2023, Zhang C. 2024, Xu 2024, kèm vai trò dự kiến và điều kiện dùng. Không nhập Zotero.

### Việc 3 – PDF
- Thêm mục 6 vào `bao_cao_nguon_5_6A.md`: 13/13 tài liệu chưa có tệp PDF thực trong Zotero (Varma & Simon, Vabalas có 4 bản ghi đính kèm rỗng). Ưu tiên: Wang & Cha 2021 và Figueiredo 2011 (đóng, cần thư viện), Hughes 2022 (arXiv), Bull 2022 (hybrid OA). 8 bài có bản mở (OpenAlex/arXiv).

### Việc 4 – Quyết định viết 5.6A
- CLAUDE.md mục 9: thêm "Quyết định viết 5.6A" (G1 đề xuất của luận án, kiểm chứng ở WP3; G3 chủ yếu từ dữ liệu cầu và máy bay; G4 không tìm thêm nguồn; G6 không trích nguồn; nhãn tạm mục giới hạn là 5.8).
- Bảng tiến độ: ĐD0 đã duyệt; cập nhật dòng 5.6A.

## Phiên 29/09/2026 (4) – viết mục 5.6A

### Việc 0 – Dọn dẹp
- Zotero: chuyển 4 bản ghi đính kèm rỗng của Varma & Simon và Vabalas vào Thùng rác. Tải lại PDF truy cập mở thành công nhưng tải lên Zotero bị từ chối vì đầy hạn mức 300 MB; hai bản ghi đính kèm hỏng phát sinh (2MNI6S6J, CF3IB3BK) cũng được chuyển vào Thùng rác. Ghi vào `bao_cao_nguon_5_6A.md`.
- CLAUDE.md: thay "5.9" ở 4.2, 6.2, 6.3 bằng "mục giới hạn (nhãn tạm 5.8, đánh số lại ở GĐ5)"; xóa ghi chú "hiểu là…" ở mục 9.

### Việc 1 – Kiểm tra điều kiện: DỪNG
- Kiểm tra trên đĩa (bản sao `zotero.sqlite` lúc 09:53 và thư mục `storage`): Wang & Cha 2021 (TDRPDWJE), Figueiredo 2011 (23TBQTIP), Hughes 2022 (Z9RD5DMZ), Bull 2022 (87NKU5IS) đều **không có tệp đính kèm**.
- Theo yêu cầu, dừng phiên: chưa đọc, chưa ghi `notes/`, chưa viết 5.6A, chưa lập các sản phẩm của Việc 3.
- Nguồn phụ đã có PDF sẵn cho lần sau: [18] Brake (VPFBB9SG), [45] Sohn (MANJDQEZ), [56] Da Silva (IW7JBB3E).

### Việc 1 (tiếp, sau khi NCS bổ sung PDF) – Đọc và ghi chú
- NCS đặt 4 PDF ưu tiên vào thư mục gốc TLTQ. Phiên bản: Figueiredo 2011 và Bull 2022 là bản in; Wang & Cha 2021 là bản thảo tác giả; Hughes 2022 là tiền in arXiv v2 (số trang ghi theo bản đã đọc).
- Đọc giới thiệu, phương pháp, kết luận của 4 bài; đọc phần liên quan của [18] Brake, [45] Sohn, [56] Da Silva; tóm tắt/kết luận của Varma & Simon, Vabalas (PDF tải lại, chưa gắn Zotero), tóm tắt Kiranyaz, Avci.
- Ghi chú theo khuôn 7.4: `notes/TDRPDWJE.md`, `23TBQTIP.md`, `Z9RD5DMZ.md`, `87NKU5IS.md` (đầy đủ); `VPFBB9SG.md`, `MANJDQEZ.md`, `IW7JBB3E.md` (đọc một phần).

### Việc 2 – Viết mục 5.6A
- Chèn `## 5.6A. Công cụ trí tuệ nhân tạo và vai trò trong chuỗi bằng chứng` vào `tieuluan/05_chuong5.md`, ngay trước 5.7 (chỉ thêm 44 dòng; không sửa mục khác). Năm tiểu mục 5.6A.1–5.6A.5 và Bảng 5.6A.
- Trỏ về Mục 3.2.3, 3.3, 4.5.2 và mục giới hạn 5.8; không lặp nội dung các mục đó. Không có số liệu hay kết quả của Paper 1.

### Việc 3 – Sản phẩm kiểm tra
- `revision/5_6A_luan_diem_nguon.csv`: 27 luận điểm → trích dẫn → vị trí trong nguồn → mức đã đọc.
- `revision/nhap_khai_bao_AI_tao_sinh.md`: bản nháp khai báo AI tạo sinh (chưa chèn), kèm đề xuất NCS khai thêm việc AI soạn nháp một số mục.
- `matrix/doi_chieu_danh_muc.csv`: thêm dòng `moi` cho Kiranyaz 2021 và Avci 2021 (trích lần đầu ở 5.6A).
- Thống kê 5.6A: 1.599 từ (văn xuôi 1.347 + bảng 252; không tính ký hiệu trích dẫn); trích dẫn cũ 7 lần / 7 tài liệu ([14], [18], [45], [53], [56], [57], [59]); trích dẫn mới 20 lần / 15 tài liệu; câu dạng giới hạn ("không chứng minh / không phải / không thay thế / không đồng nghĩa / không đủ"): 0.

## Phiên 29/09/2026 (5) – sửa mục 5.6A theo phản biện của NCS

- (1) Câu siêu tham số: "được cố định trước hoặc chọn bên trong vòng huấn luyện của từng lần chia"; giữ hai trích dẫn.
- (2) Văn xuôi 5.6A dùng tên tiếng Việt thay tên mã (bản ghi bằng chứng, trường giá trị / độ bất định / phạm vi hiệu lực / điều kiện áp dụng, bối cảnh quan trắc, bản ghi kiểm tra, bản ghi sử dụng bằng chứng, sự kiện chuyển trạng thái, phiên bản phương pháp); lần nhắc đầu có "(xem Mục 5.5)"; "ràng buộc C5" → "ràng buộc về sử dụng bằng chứng ngoài phạm vi hiệu lực, Phụ lục B"; "C1–C8" → "các ràng buộc ở Phụ lục B"; "đường cơ sở B0 (xem Mục 5.7)". Tên mã giữ trong Bảng 5.6A.
- (3) Thêm \[57\], gắn với ý "dữ liệu đo phủ đủ các điều kiện vận hành và hư hỏng của một công trình hiếm khi có sẵn" (đúng theo tóm tắt [57] qua OpenAlex); giữ Wang & Cha cho ý điều kiện biên và vật liệu riêng (ghi chú đọc xác nhận, tr. 2, 20 bản thảo).
- (4) "mức may rủi" → "mức ngẫu nhiên".
- (5) Cross 2011: truy cập đóng, không có bản lưu trữ mở. Ghazimoghadam 2024: ScienceDirect chặn bằng CAPTCHA, không có bản lưu trữ mở. Chưa đọc được phần phương pháp; giữ hai câu ở mức tóm tắt; thêm `notes/KPWFC4PI.md`, `notes/G98ZWHKW.md` và cập nhật cột muc_da_doc.
- (6) Hughes 2022: bản in MSSP truy cập đóng; các kho (arXiv, White Rose, Glasgow) chỉ có bản tiền in; chưa đối chiếu được số trang, ghi chú vào CSV và `notes/Z9RD5DMZ.md`.
- (7) CLAUDE.md: mục 4.1 thêm quy ước lưu PDF trong `pdf/` (linked file); mục 6.1 thêm hai ghi chú (chuyển đoạn "bốn nhóm bằng chứng" sang 3.6; 5.5, 5.7, Phụ lục B định nghĩa đủ thuật ngữ 5.6A).
- (8) Tạo `.gitignore` (`pdf/`, `*.pdf`); chuyển 4 PDF ưu tiên vào `pdf/`, đổi tên theo khóa Zotero; chép thêm PDF Varma & Simon, Vabalas vào `pdf/`.
- (9) `nhap_khai_bao_AI_tao_sinh.md`: mục 4 đưa vào danh sách chính theo lời NCS; sửa câu "không dùng để tạo… trích dẫn" thành "mọi trích dẫn được đối chiếu với bản gốc và Crossref" để thống nhất với mục 4. Chưa chèn vào tiểu luận.
- Thống kê sau sửa: 1.691 từ (văn xuôi 1.439 + bảng 252), vượt khung 1.600 do tên tiếng Việt dài hơn tên mã; trích dẫn cũ 8 lần / 7 tài liệu; mới 20 lần / 15 tài liệu; câu dạng giới hạn: 0.

## Phiên 29/09/2026 (6) – chốt mục 5.6A

- 5.6A.3: "Nhà xưởng ghi được … nên hướng thứ nhất được ưu tiên." → "Khi nhà xưởng ghi được nhiệt độ và trạng thái thiết bị trong bối cảnh quan trắc, hướng thứ nhất được ưu tiên." Giữ độ dài 1.691 từ (NCS duyệt).
- CLAUDE.md: thêm mục 6.4 "Lưu ý cho Giai đoạn 6" (rà cột `muc_da_doc` trước khi chèn khai báo AI tạo sinh); bảng tiến độ: 4.1 Mục 5.6A = Đã duyệt (chờ hoàn thiện 2 câu khi có PDF).
- `revision/viec_ton_dong_GD0.md`: thêm mục 5 "Chờ PDF" (Cross 2011 – KPWFC4PI, Ghazimoghadam 2024 – G98ZWHKW, bản in Hughes 2022 – Z9RD5DMZ).

## Phiên 30/09/2026 – Giai đoạn 1: tìm tài liệu bổ sung

### Việc 0 – Dọn tệp tồn đọng
- `viec_ton_dong_GD0.md`: xóa dòng về bản nháp 5.8 (đã lưu); tag K1/K2/K3/Đối tượng gắn ở GĐ2; ghi collection đích GĐ1 là `TL-Key/Bổ sung` (TKVJVWDZ) vì Zotero không có `00_TLTQ/05_Bo_sung_GD1`.
