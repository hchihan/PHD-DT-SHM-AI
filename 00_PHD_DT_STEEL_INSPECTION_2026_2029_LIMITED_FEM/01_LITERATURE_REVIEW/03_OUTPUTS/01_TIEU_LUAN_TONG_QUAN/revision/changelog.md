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

### Việc 1 – Luận điểm cần căn cứ
- `revision/GD1_luan_diem_can_nguon.csv`: 17 luận điểm (L1.1–L1.6, L2.1–L2.5, L3.1–L3.2, L4.1–L4.4); 14 cần tìm, 3 đã đủ nguồn (L1.6 văn bản pháp quy đã có trong Zotero; L2.3 và L2.5 đã có nguồn trong tiểu luận).

### Việc 2 – Tìm và xác minh ứng viên
- Consensus: 14 truy vấn. Tra trước thư viện Zotero (bản sao CSDL 29/09 15:03).
- `revision/GD1_ung_vien.csv`: 45 tài liệu có DOI (Cawley 2018 dùng cho hai luận điểm), cả 45 được Crossref xác minh theo DOI; tình trạng truy cập lấy từ OpenAlex. Thêm 2 chuẩn/đặc tả xác minh trên trang chính thức (ISO 55000:2024 trên iso.org; BCF 3.0 trên kho GitHub chính thức của buildingSMART) và 3 văn bản pháp quy đã có trong Zotero.
- Gợi ý của NCS đều khớp: Junker 1969 (SAE Technical Paper 690055), Phares và cs. 2004, Worden và cs. 2007, Kapteyn và cs. 2021, Farrar & Worden (Crossref ghi 2012, không phải 2013).
- CHƯA CÓ NGUỒN: L1.1 phần Việt Nam; một phần của L1.4, L1.5, L2.1, L2.4, L3.1 (xem báo cáo mục 2).
- Không nhập Zotero, không sửa tiểu luận.

### Việc 3–4 – Danh sách key và báo cáo
- `revision/bao_cao_GD1.md`: bảng theo luận điểm; 17 tài liệu đề xuất nhập (6 truy cập đóng); 5 tài liệu "nhận" đã có trong Zotero; văn bản pháp quy cho L1.6 kèm khóa Zotero; đề xuất danh sách key 30 tài liệu (Tier 1 giữ 12; Tier 2 thêm Cawley 2018, Worden 2007, Figueiredo 2011, Hughes 2022; hạ [59] xuống nguồn trích thường).
- CLAUDE.md: GĐ1 = Chờ duyệt (ĐD1).

## Phiên 30/09/2026 (2) – nhập tài liệu GĐ1 và chốt Điểm duyệt 1

### Việc 1 – Nhập Zotero
- Collection đích: `TL-Key/Bổ sung` (TKVJVWDZ); Zotero không có `00_TLTQ/05_Bo_sung_GD1`.
- Kiểm tra trùng toàn thư viện (DOI, tiêu đề): không bản nào có sẵn. Nhập 17 tài liệu (16 theo DOI, BCF 3.0 dạng report có tác giả tổ chức): Cawley 2018 (EBB69J4F), Phares 2004 (J7FAWJ8I), Graybeal 2002 (8IMKCTE5), Gong 2022 (WP5WUUF9), Junker 1969 (W6IUU4MF, conferencePaper), Ju 2020 (38FMATHE), Nooralishahi 2021 (2AZ7VZ5R), Di Sarno 2021 (X4KUWKT8), Iordachescu 2022 (X2UZWVJG), Bull 2021 JSV (3U3KGTHV), Gardner 2021 (GXVWFUSA), Worden 2007 (MCNRW6F5), Farrar & Worden (HQQJMZDW, book), Kapteyn 2021 (95RKP767), van Berlo & Krijnen 2014 (ARZ6WDZQ), Saleem & Qureshi 2018 (J358BJ7Z), BCF 3.0 (K5SGFIGW).
- Không tự đính kèm PDF (Zotero đầy hạn mức 300 MB).
- Sửa sau đối chiếu Crossref: năm bản in Gong (2021 → 2022) và Ju (2019 → 2020), ngày trực tuyến ghi ở Extra; Junker thêm tên tùng thư và số báo cáo; Farrar & Worden thêm phụ đề và ghi "CHỜ KIỂM NĂM" (Crossref 2012).
- Năm tài liệu đã có (SKCFNXPU, QMVQCEL5, Z5JM78G6, ZCPMLA5V, 8PB7EN2E): thêm vào collection, gắn tag GD1 và mã luận điểm.
- Tag: `GD1` + mã luận điểm cho 22 tài liệu; `TLTQ:Tier1` cho 12 tài liệu Tier 1, `TLTQ:Tier2` cho 18 tài liệu Tier 2 (gắn cho toàn bộ danh sách key để thống nhất, vì trước đó Tier chỉ được theo dõi bằng collection); [47], [59] gắn `TLTQ:trích thường`. Collection `TL-Key/Tier2`: thêm Ju, Cawley, Worden, Figueiredo, Hughes; bỏ [47], [59].
- `matrix/doi_chieu_danh_muc.csv`: thêm 22 dòng `moi` (3 `key-T2`, 19 `bosung-GD1`); Figueiredo và Hughes đổi thành `key-T2`; [47], [59] đổi thành `trich-thuong`.
- `viec_ton_dong_GD0.md`: ghi bản trùng ISO 55000:2024 (2H6XA32D) cần gộp thủ công.

### Việc 2 – Chốt danh sách key trong CLAUDE.md
- Mục 7.1–7.2: danh sách 30 tài liệu (12 Tier 1, 18 Tier 2), ghi ngày chốt ĐD1 30/09/2026; thêm Ju 2020 vào Tier 2, hạ [47] và [59] xuống nguồn trích thường.
- Thêm mục 7.5 "Cách viết cho luận điểm chưa có nguồn"; thêm vào 4.1 quy tắc ba căn cứ không thuộc nhóm 2025–2026 cho mỗi khoảng trống.

### Việc 3 – Chuẩn bị Giai đoạn 2
- Tạo `matrix/literature_matrix.csv`: 30 dòng theo khuôn 7.4, thêm cột `thu_tu_doc`, `pdf`, `ghi_chu`; điền sẵn khóa, số cũ, Tier, cụm (đề xuất theo tiêu đề) và mức đã đọc.
- Năm dòng điền sẵn từ `notes/` và đánh dấu "CẦN NCS KIỂM": [18], [45], [56] (đọc một phần), Figueiredo 2011, Hughes 2022.
- Lập `revision/GD2_ke_hoach_doc.md`: 8 phiên (4 Tier 1, 4 Tier 2); 20 tài liệu key có PDF, 10 thiếu (tình trạng truy cập theo OpenAlex 30/09/2026); 8 PDF thiếu ngoài danh sách key.

### Việc 4 – Tiến độ
- CLAUDE.md mục 12: GĐ1 = Đã duyệt (ĐD1); GĐ2 = Sẵn sàng – chờ PDF.

## Phiên 30/09/2026 (3) – GĐ2 phiên T1-3: đọc sâu [8], [7], [3]
- Đọc toàn văn Kritzinger 2018 (`DMIUEEFB`), Boje 2020 (`5REDLQK8`), Lu 2020 (`5QX5LTMZ`); ghi chú theo khuôn 7.4 kèm mục 1–8 trong `notes/`.
- [8]: định nghĩa DM/DS/DT theo mức tích hợp dữ liệu (tr. 1017); theo định nghĩa, khung luận án ở mức bóng số (DS) [NCS, cần NCS quyết định cách khai báo]. Bài không chỉ ra bài cụ thể nào bị gọi sai tên.
- [3]: chuỗi dừng ở cảnh báo và hỗ trợ quyết định của người quản lý FM; ca nghiên cứu là bơm HVAC, dữ liệu thật nhưng một bộ ghép nhân tạo, so sánh định tính với CUSUM.
- [7]: đề cập độ tin cậy dữ liệu nguồn (một đoạn, tr. 9) và xác nhận của người dùng (tr. 12); không đề cập nguồn gốc dữ liệu, truy vết, trách nhiệm.
- Tạo `revision/GD2_nhat_ky_khoang_trong.md` (UV-01…UV-05); cập nhật `matrix/literature_matrix.csv` (3 dòng, mức đọc "toàn văn"); tag Zotero `Doc:toan_van` (3 bài), K1/K2/K3 cho [7] và [3].
- Phiên T1-1 (ba tiền lệ) chưa chạy; ghi trong `GD2_ke_hoach_doc.md` mục 6.

## Phiên 30/09/2026 (4) – GĐ4, bước 4.3: viết mục 1.3A và 1.4A
- Chèn `## 1.3A. Khái niệm bằng chứng trạng thái` và `## 1.4A. Ba câu hỏi của người quản lý` vào `tieuluan/01_chuong1.md`, ngay sau mục 1.2 hiện có (mục 1.2 mới "Đối tượng" chưa viết); không sửa hay xóa đoạn cũ (diff chỉ thêm 28 dòng).
- 1.3A: 549 từ gồm Bảng 1.3A (395 từ ngoài bảng); 2 trích dẫn [14], [15]. 1.4A: 389 từ; 2 trích dẫn [16], [17]. Cả bốn đã dùng đúng ý ở 1.2.2 và 1.2.4; không có tài liệu mới.
- Ví dụ cột trục C3 và kịch bản 1.4A ghi rõ là giả định; không dùng số liệu, cấu hình hay kết quả của Paper 1.
- Tạo `revision/1_3A_nguon_hop_nhat.md`: kiểm kê các đoạn định nghĩa bằng chứng trạng thái và chuỗi định danh kèm đề xuất GĐ5; 4 điểm chờ NCS.
- CLAUDE.md mục 12: thêm dòng 4.3.

## Phiên 30/09/2026 (5) – sửa 1.3A, thêm quy tắc phản chứng
- 1.3A: giữ ba thành phần; thêm câu nguồn gốc bao gồm nguồn thu, cấu hình cảm biến, phiên bản dữ liệu – chuỗi xử lý và giao thức đánh giá (trỏ 3.4.1); thêm đoạn ba nguồn của bằng chứng (mô hình trên dữ liệu cảm biến, quan sát của kỹ sư, kiểm tra không phá hủy) và câu về trọng tâm WP1; sửa Bảng 1.3A. Không sửa 1.4A và mục khác.
- `1_3A_nguon_hop_nhat.md`: đề xuất GĐ5 cho 1.2.2, 3.1.3, 3.5 đổi thành viết lại như loại con "bằng chứng trạng thái từ dữ liệu dao động"; ghi hai điểm đã quyết.
- CLAUDE.md mục 7.4 và `GD2_nhat_ky_khoang_trong.md`: thêm hai trường "Phản chứng đã kiểm", "Phát biểu đã thu hẹp" và điều kiện vào GĐ3. Áp cho UV-01 (CMMS, BCF 3.0; phát biểu thu hẹp đề xuất), UV-03 ([2] IFC Monitor, quan hệ gán trong IFC); UV-02, UV-04, UV-05 ghi "chưa kiểm".

## Phiên 30/09/2026 (6) – kiểm phản chứng UV-01 (BCF 3.0) và UV-03 ([2])
- Đọc tài liệu kỹ thuật BCF-XML 3.0 (mục Topic, Comment, Components) và BCF-API 3.0 (mục 1.2, 3.1.5, 3.9) trên kho buildingSMART, nhánh `release_3_0`. Kết quả: BCF có trạng thái, người tạo, thời điểm, bình luận, liên kết cấu kiện qua góc nhìn, lịch sử sự kiện đổi trạng thái (chỉ ở BCF-API) và quyền theo người dùng; không có khái niệm bằng chứng, nguồn gốc, phạm vi hiệu lực, căn cứ của bước chuyển.
- Đọc thân bài [2] Theiler & Smarsly 2018 (tr. 54–64): IFC Monitor biểu diễn quan hệ cảm biến – cấu kiện bằng quan hệ tĩnh, không có thời hạn hiệu lực; tác giả nêu động lực học của hệ quan trắc là việc để lại (tr. 64).
- `GD2_nhat_ky_khoang_trong.md`: ghi kết quả vào "Phản chứng đã kiểm" của UV-01 và UV-03; cập nhật phát biểu thu hẹp; UV-03 có 3 căn cứ. Không sửa tiểu luận.
- Chưa làm: ghi chú đọc sâu và bảng ánh xạ cho [2] (phiên T1-1); kiểm CMMS, ISO 19650, đặc tả IFC, SOSA/SSN.

## Phiên 30/09/2026 (7) – GĐ2 phiên T1-1: đọc sâu [2], [44]; kiểm phản chứng UV-01, UV-03
- Đọc toàn văn [2] Theiler & Smarsly 2018 và [44] García 2026; ghi chú trong `notes/`; bảng ánh xạ `mapping/theiler2018.md`, `mapping/garcia2026.md` (Phần A–E). [35] Bellon chờ PDF, không đọc.
- Kiểm phản chứng bằng tài liệu chính thức: IFC4 ADD2 TC1 (IfcActionRequest, IfcProjectOrder, IfcTask, IfcWorkPlan, IfcApproval, IfcOwnerHistory, IfcRelAssigns, IfcPerformanceHistory), COBie 2.4 (NBIMS-US V3 chương 4.2, tệp tải từ nibs.org vào thư mục tạm), SSN/SOSA (Khuyến nghị W3C 19/10/2017). ISO 19650-3: không truy cập được (trả phí; bản xem trước đòi chấp nhận điều khoản).
- Kết quả: UV-01 thu hẹp thêm (IFC4, COBie, BCF có trạng thái và phê duyệt; [44] có khuôn bước chuyển có bằng chứng và thẩm quyền); UV-03 thu hẹp (SSN Deployment là tiền lệ trực tiếp; IfcOwnerHistory chỉ giữ lần sửa cuối) và là ứng viên duy nhất đủ điều kiện hình thức vào GĐ3.
- Cập nhật ma trận (2 dòng), nhật ký, CLAUDE.md mục 6.1 (tiền lệ bắt buộc nêu) và mục 12, `GD2_ke_hoach_doc.md`. Tag Zotero: Doc:toan_van cho [2], [44]; K2 cho [2]; K2, K3 cho [44]. Không sửa tiểu luận.

## Phiên 01/10/2026 – GĐ2 phiên T1-2: đọc sâu [22], [18], [19]
- NCS tải 8 PDF key; đổi tên theo khóa Zotero trong `pdf/` (AESHHWVZ, JQKJGUER, DWT957YI, W7AEKRT8, EBB69J4F, B2JXAM9M, 38FMATHE, MCNRW6F5). Còn thiếu [35] Bellon và [80] Bull 2025; `pdf/Unconfirmed 845287.crdownload` là bản tải dở. Phiên T1-1 vì vậy vẫn chưa xong phần [35].
- Đọc toàn văn [22] Hemker 2019, [18] Brake 2019 (thay ghi chú đọc một phần), [19] Ramasso 2025 (bản tiền in arXiv v1; số trang theo bản tiền in).
- Nhật ký: UV-01 thêm căn cứ [22] (nhu cầu hồ sơ khắc phục, chờ NCS chấp nhận cách tính); UV-05 thêm [19]; tạo UV-06 (lần lắp ráp hoặc can thiệp bảo trì là ranh giới phạm vi hiệu lực; K1).
- Ma trận: 3 dòng; cột `pdf` cập nhật cho 8 tài liệu. Kế hoạch đọc, CLAUDE.md mục 12. Tag Zotero: Doc:toan_van và K tương ứng. Không sửa tiểu luận.

## Phiên 01/10/2026 (2) – GĐ2 phiên T1-4: đọc sâu [53], [16], [17]; phân tích khoảng trống bằng các skill PhD
- Nạp và áp khuôn của skill deep-read-phd-papers (QA nguồn, định tuyến, bảng giới hạn có nhãn AUTHOR-STATED/READER-INFERRED, sàng lọc ý tưởng tám tiêu chí, Claim → Evidence → Limitation → Next action, bài học năm phút), phd-gap-miner (bảng gap-impact, thang mức bảo vệ, rà cơ hội mở rộng) và govern-phd-evidence (khối định tuyến RQ → WP → Chương → Paper → Gate → Scope → Evidence type). Không chấm theo "khoảng trống đã khóa" của skill; K1–K3 vẫn là giả thuyết làm việc. Không ghi vào tệp kiểm toán bên ngoài dự án; mọi kết quả ghi trong `revision/`.
- Đọc toàn văn [53] Kapoor & Narayanan 2023, [16] Çelik 2023 (bản in thử, dẫn trang PDF), [17] Wu 2026.
- Nhật ký: UV-02 thêm căn cứ [53], [16] và phản chứng đã kiểm ([16], [53]); UV-05 thêm [17]; UV-06 thêm [53]; tạo UV-07 (xác nhận của chuyên gia đối với đầu ra AI là tín hiệu học, chưa là bản ghi trách nhiệm).
- Tạo `revision/GD2_phan_tich_khoang_trong_T1.md`: tổng hợp liên tài liệu 11 tài liệu Tier 1 đã đọc và bốn chuẩn đã kiểm; mức bảo vệ làm việc của K1–K3; rà cơ hội mở rộng; ghi xung đột giữa skill và CLAUDE.md.
- [35] Bellon đã có PDF trong Zotero; [80] còn thiếu. Ma trận 3 dòng; kế hoạch; CLAUDE.md mục 12. Không sửa tiểu luận.

## Phiên 01/10/2026 (3) – đồng bộ bốn skill PhD với CLAUDE.md
- Theo yêu cầu NCS, đồng bộ deep-read-phd-papers, phd-gap-miner, govern-phd-evidence, phd-literature-scout với CLAUDE.md hiện hành: schema đồ thị có STATUS_EVENT và AGENT; K1–K3 là giả thuyết làm việc theo câu chữ tiểu luận mục 5.2; nơi ghi kết quả trong `revision/` và `notes/`; quy tắc phản chứng, ngưỡng ba căn cứ ngoài nhóm 2025–2026, tiền lệ bắt buộc; CLAUDE.md đứng đầu thứ tự nguồn với việc thuộc tiểu luận.
- Bản đồng bộ, bản gốc và gói tải lên claude.ai ở `04_AI_SKILL_SYSTEM/08_CLAUDE_SKILLS/_DONG_BO_20261001/`; đã cài vào bộ nhớ skill trên máy. Không sửa nội dung tiểu luận.

## Phiên 01/10/2026 (4) – hoàn tất đồng bộ skill; GĐ2 phiên T1-1: đọc sâu [35] Bellon
- Skill: thay bản gốc deep-read-phd-papers và govern-phd-evidence trong `04_AI_SKILL_SYSTEM/08_CLAUDE_SKILLS/` bằng bản đồng bộ (bản cũ ở `_DONG_BO_20261001/_BAN_GOC_REPO_TRUOC_THAY/`); thêm `project-canon-tltq.md` vào `phd-dt-research-skills/_phd-canon/` và dòng ưu tiên CLAUDE.md của tiểu luận ở đầu bốn tệp canon và ba SKILL.md.
- Đọc toàn văn [35] Bellon và cs. 2025 (19 tr., PDF trong kho Zotero); ghi chú `notes/NUTL57KJ.md`; bảng ánh xạ `mapping/bellon2025.md` (Phần A–E).
- Nhật ký: UV-01 kiểm [35], thu hẹp thêm (chuỗi định kiểu kiểm tra → hư hỏng → cấu kiện → bảo trì → chi phí đã có bằng thực thể chuẩn IFC 4.3 cho phát hiện bằng mắt); còn CMMS chưa kiểm. UV-03 kiểm [35], không đổi.
- Ma trận 1 dòng; kế hoạch đọc (Tier 1: 12/12); `GD2_phan_tich_khoang_trong_T1.md` mục 6; CLAUDE.md mục 6.1 (tiền lệ [35]) và mục 12. Tag Zotero: Doc:toan_van, K2, K3 cho [35]. Không sửa tiểu luận.

## Phiên 01/10/2026 (5) – quy tắc git, tệp bị xóa, quyết định thiết kế 5.5, nguồn phản chứng CMMS
- CLAUDE.md mục 4.3: quy tắc git (chỉ add đúng tệp của phiên; kiểm `git status`, `git diff --cached --stat` trước commit; vùng stage có tệp ngoài phiên thì dừng và báo).
- `revision/git_tep_bi_xoa.md`: 330 tệp đang ở trạng thái đã xóa, gom 55 nhóm; 180 có bản cùng nội dung ở nơi khác, 71 chỉ cùng tên, 79 không thấy bản thay thế; đề xuất theo nhóm; ghi chú về việc repo nằm trong Google Drive. Không khôi phục, không commit lệnh xóa.
- CLAUDE.md mục 8: quyết định thiết kế cho 5.5 (mở rộng trên nền IFC 4.3 của [35]; quan hệ bằng chứng – cấu kiện n:m ở tầng đồ thị, IFC là khung nhìn xuất; bản ghi bất biến với prov:wasRevisionOf / prov:wasInvalidatedBy); thêm ràng buộc C9. Mục 6.1: trình bày schema như mở rộng của [35] và BCF 3.0.
- Nguồn CMMS cho UV-01: Chen và cs. 2018 `QZ7E3HDV`, Condotta & Scanagatta 2023 `QBTTSBTH` (DOI xác minh Crossref, nhập TL-Key/Bổ sung, tag GD2-phanchung, 2 dòng `moi` trong `doi_chieu_danh_muc.csv`). Chưa có PDF; mục CMMS vẫn "chưa kiểm".
- [80] Bull 2025 (`5D5H5XGK`): không có tệp đính kèm trong Zotero, không có tệp trong `pdf/`; `Unconfirmed 845287.crdownload` là bản tải dở.

## Phiên 01/10/2026 (6) – GĐ2 phiên T2-1: [45] Sohn, Figueiredo 2011, Ju 2020, Cawley 2018, Worden 2007
- Bản Condotta 2023 trên air.iuav.it bị Cloudflare chặn bằng xác minh người dùng; không vượt qua; NCS cần tải tay.
- Đọc toàn văn Worden 2007 `MCNRW6F5`, Cawley 2018 `EBB69J4F` (bản trực tuyến tr. 1–20), Ju 2020 `38FMATHE` (bản trực tuyến tr. 1–14); đọc bổ sung [45] Sohn 2007 (mục 1–3) và Figueiredo 2011 `23TBQTIP` (phần thuật toán, kết quả), nay là toàn văn; bỏ dấu "CẦN NCS KIỂM" ở hai dòng này.
- `GD1_luan_diem_can_nguon.csv`: thêm cột `doan_dung_duoc` cho L2.1, L2.2, L2.3, L3.1, L4.1, ghi phần còn là diễn giải của NCS.
- Nhật ký khoảng trống: nhập căn cứ 5.6A (Bull 2022, Hughes 2022, Wang & Cha 2021, Figueiredo 2011) vào UV-02 và UV-05; quy ước đếm nhóm tác giả Sheffield – Los Alamos là một; UV-05 kiểm phản chứng một phần (Hughes, Bull 2022) và có phát biểu thu hẹp đề xuất; tạo UV-08 (nhiễu vận hành nhà xưởng) với phản chứng Zotero + 3 truy vấn Consensus (7 ứng viên, DOI xác minh Crossref, chưa nhập Zotero).
- Ma trận 5 dòng; tag Zotero Doc:toan_van và K tương ứng; kế hoạch đọc; CLAUDE.md mục 12. Không sửa tiểu luận.

## Phiên 01/10/2026 (7) – hiệu lực Nghị định 207/2026 và TCVN 9381:2012
- NCS xác nhận cả hai văn bản còn hiệu lực. Zotero: ghi trường Extra của R5P8K8CG, NDR2XMRJ.
- `matrix/doi_chieu_danh_muc.csv` dòng [11]: `trang_thai_xuat_ban` "không xác minh được" → "còn hiệu lực (NCS kiểm 01/10/2026)".
- `revision/viec_ton_dong_GD0.md` mục 3, `revision/bao_cao_GD1.md` mục 4, `revision/GD1_ung_vien.csv` (L1.6): ghi kết quả. Còn mở: ngày ban hành trong bản ghi Zotero, đối chiếu Điều 34, 37, tên chính thức TCVN 9381.
- Bổ sung (cùng phiên): NCS xác nhận Nghị định 207/2026 và Thông tư 32/2026/TT-BXD (HNY4EZVB) có hiệu lực từ 01/7/2026 (ghi Extra cả hai bản ghi, cột trạng thái dòng [11]); tên TCVN 9381 là "mức độ nguy hiểm", khớp Zotero.
- Đợt tải PDF: có Cross 2011, Graybeal 2002, Phares 2004 trong `pdf/` (kiểm trang đầu khớp DOI/tiêu đề); NCS không tải được Condotta 2023, Junker 1969, Iordachescu 2022, Ghazimoghadam 2024. Ghi ở `viec_ton_dong_GD0.md` mục 5, 5.1.

## Phiên 01/10/2026 (8) – đọc Cross 2011, Graybeal 2002, Phares 2004; kiểm số liệu KCN cho L1.1
- Cross, Worden & Chen 2011 `KPWFC4PI`: đọc toàn văn (PDF NCS cung cấp); viết lại `notes/KPWFC4PI.md`. 5.6A.3: hoàn thiện câu đồng liên kết (thêm "không cần đo điều kiện môi trường – vận hành", yêu cầu tập huấn luyện, tr. 2728). `5_6A_luan_diem_nguon.csv`: vị trí trang, `muc_da_doc` = toàn văn. Nhật ký khoảng trống UV-06: Cross 2011 đã kiểm phản chứng, không giải quyết.
- Graybeal 2002 `8IMKCTE5`, Phares 2004 `J7FAWJ8I`: đọc toàn văn; tạo `notes/8IMKCTE5.md`, `notes/J7FAWJ8I.md`; điền `doan_dung_duoc` cho L2.4 (hai bài cùng một nghiên cứu FHWA, tính là một căn cứ).
- L1.1: kiểm nguyên văn bảng Perplexity của NCS (subagent mở từng trang). Nhập Zotero (TL-Key/Bổ sung; tag GD1, L1.1, nguon-chinh-thuc-VN): `EC43U223` (447 KCN cuối 2024), `XM5ZUP99` (478 KCN ~11/2025), `TAA8G76D` (lấp đầy 75 % năm 2025). 3 dòng `moi` trong `doi_chieu_danh_muc.csv`; `doan_dung_duoc` cho L1.1; tổng hợp ở `revision/L1_1_so_lieu_KCN_da_kiem.md`. Không dùng số MPI 7/2024 (trang lỗi), số JLL, bài VnEconomy (thứ cấp).
- Không sửa tiểu luận ngoài một câu ở 5.6A.3.
- NCS duyệt (01/10/2026): mốc L1.1 = 478/324 (~11/2025, `XM5ZUP99`); câu 5.6A.3 đã sửa. CLAUDE.md mục 7.5 (L1.1) và mục 12 (4.1) cập nhật.

## Phiên 01/10/2026 (9) – GĐ2 phiên T2-2: [56] Da Silva, [57] Bull 2021, [48] Pal 2022, Hughes 2022
- Đọc toàn văn [57] `W7AEKRT8`, [48] `SL6IEB2E`; đọc lại [56] `IW7JBB3E` thành toàn văn; Hughes 2022 `Z9RD5DMZ` đọc bổ sung phần 5 (ví dụ số). Ba bài đầu đọc song song bằng agent; các trích dẫn chính được kiểm lại trên bản gốc.
- Ma trận: điền đủ 4 dòng (18–21). Kế hoạch đọc: T2-2 xong 4/5, [80] thiếu PDF; 21/30.
- Nhật ký khoảng trống: UV-05 — [57], [56] đã kiểm phản chứng (một phần), phát biểu thu hẹp giữ nguyên; UV-06 — [57], [56], [48] đã kiểm (không giải quyết), sửa trang và mức căn cứ của [56] (gián tiếp: giữa các mẫu dầm, không giữa các lần lắp), thêm dữ liệu ngược chiều một phần từ [48] (ca siết lại UD-C xếp đúng 60/60).
- Lưu ý số liệu không thống nhất trong bản gốc: [56] tỷ lệ dương tính giả 1,25 % / 0,3 %; [48] độ chính xác 95,80 % / 95,4 % — không dẫn các con số này.
- CLAUDE.md mục 12. Không sửa tiểu luận.

## Phiên 01/10/2026 (10) – GĐ2 phiên T2-3: [14] Beleites, [15] Wheat, [28] Kamariotis, [10] Chen, [29] Johannes
- Đọc toàn văn cả năm tài liệu (song song bằng agent; thông tin thư mục, trích dẫn và số liệu chính được kiểm lại trên bản gốc). [14] là bản thảo tác giả (arXiv 1211.1323v3), [28] là bản tiền in (arXiv 2202.01859v2): trang dẫn theo bản đó.
- Ghi chú `notes/L97BIAI3.md`, `notes/RG9FMT8Y.md`, `notes/AESHHWVZ.md`, `notes/ESTEYBHA.md`, `notes/YGZ32C8M.md`; ma trận dòng 23–27; [29] đổi cụm đề xuất sang Truy vết thông tin (CẦN NCS KIỂM).
- Nhật ký khoảng trống: UV-04 có phản chứng một phần ([10]) và phát biểu thu hẹp đề xuất; UV-05 thêm [28] (một phần; có thể là căn cứ độc lập mới, CẦN NCS KIỂM); UV-01, UV-02, UV-06, UV-07 thêm kết quả kiểm (không giải quyết). Ứng viên phản chứng mới cho UV-04: Papic & Cerovsek 2019 (chưa có trong Zotero).
- Ghi nhận chỗ không thống nhất trong nguồn: [14] (cỡ tập mô phỏng, 141/140 ca), [15] (32/33 bài; "ba cách chia"), [10] ("năm giai đoạn" / Bảng 5 sáu giai đoạn) — không dẫn các số này. `notes/RG9FMT8Y.md` mục đoạn dùng được lưu ý một câu ở `03_chuong3.md` về so sánh kiến trúc là diễn giải — xử lý ở GĐ5.
- Kế hoạch đọc; CLAUDE.md mục 12. Không sửa tiểu luận.
- Xác minh DOI qua Crossref (01/10/2026): [80] Bull và cs. `5D5H5XGK` — 10.1177/14759217251316199, SHM 25(4): 2383–2402, trực tuyến 13/03/2025, khớp Zotero; Gardner và cs. 2021 `GXVWFUSA` — 10.1016/j.ymssp.2020.107142, MSSP 149: 107142, **đã có trong Zotero** (sửa nhật ký UV-05, UV-06); Papic & Cerovsek 2019 — 10.35490/ec3.2019.234, Proc. EC3 2019: 387–394, chưa nhập Zotero.
- Nhập Papic & Cerovsek 2019 vào Zotero `EKAT6IMC` (TL-Key/Bổ sung; tag GD2-phanchung, UV-04); 1 dòng `moi` trong `doi_chieu_danh_muc.csv`.
