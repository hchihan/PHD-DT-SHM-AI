# Prompt bàn giao — tiếp tục Tiểu luận tổng quan (lập 01/10/2026)

> Dán toàn bộ phần dưới đường kẻ vào phiên Claude Code mới, mở tại thư mục dự án
> `H:\My Drive\03_RESEARCH\01_PHD_DT_AI_AM\00_PHD_DT_STEEL_INSPECTION_2026_2029_LIMITED_FEM\01_LITERATURE_REVIEW\03_OUTPUTS\01_TIEU_LUAN_TONG_QUAN`
> (nhánh git `revision-v2`, commit cuối trước bàn giao: `6709f86`).

---

Bạn tiếp tục hỗ trợ NCS Hồ Chí Hân hoàn thiện **Tiểu luận tổng quan** (song sinh số dựa trên dữ liệu cho giám sát trạng thái
và kiểm tra – bảo trì nhà công nghiệp khung thép). Trả lời bằng tiếng Việt.

## 0. Đọc trước khi làm (bắt buộc)

1. `CLAUDE.md` — toàn bộ. Đây là hướng dẫn cố định: quyết định đã khóa (mục 2), quy tắc trích dẫn và văn phong (4.1–4.5),
   quy tắc git (4.3), kế hoạch 7 giai đoạn (6), tiền lệ bắt buộc nêu (6.1), khuôn đọc sâu và **quy tắc phản chứng** (7.4),
   schema (8), thuật ngữ (10), điều cấm (11), trạng thái (12).
2. `revision/DD2_ban_trinh.md` — tình trạng GĐ2 và bảng 8 ứng viên khoảng trống (mục 3).
3. `revision/GD2_nhat_ky_khoang_trong.md` — nhật ký ứng viên UV-01 – UV-08 (căn cứ, phản chứng, phát biểu thu hẹp).
4. `revision/viec_cho_NCS.md` — 40 việc chờ NCS (N-01 – N-40). **Không chờ NCS làm các việc này**; chỉ cập nhật cột "Xong"
   khi chính bạn đóng được một việc, và thêm việc mới vào đây khi phát sinh.
5. `revision/changelog.md` (phần cuối) và `revision/GD2_ke_hoach_doc.md` mục 6.

## 1. Quá trình đã thực hiện (tóm tắt)

- **GĐ0–GĐ1 (28–30/09):** chuyển Markdown; đối chiếu 84 tài liệu với Zotero; chốt 30 tài liệu key (12 Tier 1, 18 Tier 2) ở ĐD1.
- **5.6A Công cụ AI:** đã viết và được duyệt (`tieuluan/05_chuong5.md`); câu đồng liên kết hoàn thiện theo toàn văn Cross 2011;
  câu autoencoder còn chờ PDF Ghazimoghadam 2024.
- **1.3A, 1.4A** (Chương 1): đã viết, chờ NCS duyệt (N-34).
- **GĐ2 Đọc sâu (30/09–01/10):** 29/30 tài liệu key đọc toàn văn qua 8 phiên (T1-1 – T1-4, T2-1 – T2-4); [80] Bull 2025 thiếu
  PDF (N-01). Ghi chú ở `notes/<khóa Zotero>.md`; ma trận `matrix/literature_matrix.csv` (29 dòng đủ cột); ba bảng ánh xạ
  `mapping/theiler2018.md`, `bellon2025.md`, `garcia2026.md`. Thêm 11 nguồn phản chứng/bổ sung đọc toàn văn (Cross 2011,
  Graybeal 2002, Phares 2004, Gardner 2021, Papic & Cerovsek 2019, Sepasgozar 2021 [9], Eraliev 2022, …).
- **Số liệu L1.1:** chốt 478 KCN thành lập / 324 hoạt động (~11/2025, Cục ĐTNN – Bộ Tài chính, Zotero `XM5ZUP99`);
  `revision/L1_1_so_lieu_KCN_da_kiem.md`.
- **Văn bản pháp quy:** NĐ 207/2026 và TT 32/2026 hiệu lực từ 01/7/2026; TCVN 9381:2012 còn hiệu lực (ghi ở Zotero Extra).
- **Quyết định NCS ngày 01/10 đã ghi vào CLAUDE.md:** quyết định thiết kế 5.5 và ràng buộc C9 (mục 8); [82] Seiß và [21] Hagedorn
  là tiền lệ bắt buộc nêu (6.1); sửa câu về [82] ở GĐ5 (6.2).
- **ĐD2:** trình có điều kiện (`revision/DD2_ban_trinh.md`).

**Tình trạng ứng viên khoảng trống (01/10/2026):**

| Mã | K | Phản chứng | Vào GĐ3 |
|---|---|---|---|
| UV-01 | K3 | còn CMMS | chưa |
| UV-02 | K1 | còn thẻ mô hình, PROV-O, MLflow/DVC | chưa |
| UV-03 | K2 | đã kiểm hết | đủ điều kiện ([NCS] nên coi là ràng buộc C3) |
| UV-04 | định vị | đã kiểm hết | chỉ định vị ở 2.3 |
| UV-05 | mới (nhãn hiện trường) | đã kiểm hết | đủ điều kiện (có thể gộp với UV-07) |
| UV-06 | K1 | còn theo dõi dài hạn sau bảo trì | chưa (có phát biểu thu hẹp đề xuất) |
| UV-07 | K3 | còn human-in-the-loop, thẻ mô hình | chưa |
| UV-08 | mới (L2.2) | còn toàn văn Hu 2023 | đề xuất không thành K4 |

## 2. Quyết định của NCS khi bàn giao (01/10/2026) — đã được phép làm

1. **Được phép tìm nguồn, xác minh và nhập Zotero** để đóng các nhóm phản chứng còn mở; được tải PDF **truy cập mở**
   về `pdf/` (tên tệp bắt đầu bằng khóa Zotero). Không vượt CAPTCHA/Cloudflare; bài truy cập đóng thì ghi vào `viec_cho_NCS.md`.
2. **Cho GĐ3 bắt đầu** dù ĐD2 chưa kiểm xong ([80] không làm căn cứ cho ứng viên nào). GĐ3 làm ở mức **nháp**; khoảng trống
   chỉ được **chốt** sau khi NCS kiểm ma trận (N-10) và duyệt ĐD3 (CLAUDE.md 2.9, 11).

Hai quyết định trên **đã được ghi** vào CLAUDE.md mục 12 và `revision/changelog.md` (commit bàn giao). Phiên mới bắt đầu thẳng
vào Nhiệm vụ 1.

## 3. Nhiệm vụ tiếp theo (theo thứ tự)

### Nhiệm vụ 1 — Đóng các nhóm phản chứng còn mở (một phiên)

| Mục | Ứng viên | Việc cụ thể |
|---|---|---|
| N-21 | UV-02 | (a) Đọc PROV-O (Khuyến nghị W3C, https://www.w3.org/TR/prov-o/) phần Starting Point và Qualified terms: có biểu diễn được nguồn gốc xử lý, phiên bản phương pháp, phạm vi hiệu lực cho **từng** kết quả không. (b) Mitchell và cs. 2019 "Model Cards for Model Reporting" (FAT* 2019) — xác minh DOI qua Crossref, nhập Zotero, đọc bản arXiv mở: thẻ mô hình ở mức mô hình hay mức từng kết quả. (c) MLflow/DVC: đối chiếu tài liệu chính thức (model registry, lineage) — không cần nhập Zotero nếu không trích. |
| N-24 | UV-07 | Tìm 1–2 tổng quan về học máy có người trong vòng (human-in-the-loop), ví dụ Mosqueira-Rey và cs. 2023 (*Artif. Intell. Rev.*); xác minh, nhập, đọc: xác nhận của chuyên gia có được ghi như bản ghi trách nhiệm (người, thẩm quyền, thời điểm, căn cứ) hay chỉ là tín hiệu học. |
| N-23 | UV-06 | Tìm 1–2 nghiên cứu theo dõi dài hạn có can thiệp/sửa chữa/thay thế giữa chừng (cập nhật đường cơ sở sau bảo trì; ví dụ theo dõi dài hạn cầu có sửa chữa). Kiểm: can thiệp có được ghi thành ranh giới hiệu lực của dữ liệu/mô hình không. |
| N-25 | UV-08 | Nhập Hu và cs. 2023 (DOI 10.1142/s0219455424502171); đọc nếu có bản mở, nếu không ghi "chỉ tóm tắt". |
| N-20 | UV-01 | Tìm bản mở của Chen và cs. 2018 `QZ7E3HDV` (OpenAlex); nếu có, đọc phần lệnh công việc/trạng thái. Nếu không có bản mở: đề xuất NCS chấp nhận dùng [29] Johannes (tr. 7, 11) làm đối chiếu thay thế. |

Mỗi nguồn: xác minh tiêu đề, tác giả, năm, nơi đăng, DOI qua Crossref **trước** khi nhập; nhập vào collection
`TL-Key/Bổ sung` (khóa `TKVJVWDZ`) với tag `GD2-phanchung` và `UV-0x`; thêm một dòng `so_cu = moi` vào
`matrix/doi_chieu_danh_muc.csv`; viết `notes/<khóa>.md` theo khuôn của `notes/EKAT6IMC.md` (có mục "Kiểm phản chứng" với
phán định "giải quyết / một phần / không giải quyết" kèm trang); cập nhật nhật ký UV tương ứng (đổi "chưa kiểm" thành kết quả,
cập nhật phát biểu thu hẹp); cập nhật bảng ở `DD2_ban_trinh.md` mục 3 và cột "Xong" ở `viec_cho_NCS.md`.

### Nhiệm vụ 2 — GĐ3 nháp: khoảng trống (phiên sau, hoặc cùng phiên nếu Nhiệm vụ 1 xong sớm)

Theo CLAUDE.md mục 6 (GĐ3): **gom 5 cụm chủ đề** (Song sinh số · SHM–bu lông–EOV · Độ tin cậy đánh giá · Truy vết thông tin ·
Giá trị quyết định); **rút khoảng trống từ cột Giới hạn** của ma trận và từ nhật ký UV; mỗi khoảng trống **≥ 3 căn cứ** độc lập,
không thuộc nhóm 2025–2026 (đếm theo quy ước nhóm tác giả trong nhật ký: nhóm Sheffield – Los Alamos tính một; [10] cùng nhóm [3]).

Sản phẩm: `revision/GD3_khoang_trong_nhap.md` gồm:
1. Bảng **Khoảng trống → Căn cứ (trang, loại TG/NCS) → Phản chứng đã kiểm → Phát biểu đã thu hẹp → Vì sao quan trọng
   (gắn ba câu hỏi người quản lý và luận điểm trung tâm)**.
2. Đối chiếu với giả thuyết K1–K3 (giữ / sửa / gộp / bỏ), kèm đề xuất về UV-03 (ràng buộc C3, không thành khoảng trống riêng?),
   gộp UV-05 + UV-07, UV-04 chỉ định vị, UV-08 thành luận điểm 3.2.
3. Danh sách quyết định cho NCS ở ĐD3 (để gửi thầy hướng dẫn).

Không viết lại mục 5.2 của tiểu luận ở GĐ3 (đó là GĐ4 mục 4.6, sau ĐD3). Ứng viên còn "chưa kiểm" thì đánh dấu "tạm", không chốt.

## 4. Cách làm đã dùng (giữ nguyên)

- **Mỗi phiên một nhiệm vụ**; cuối phiên báo: (1) đã làm, (2) diff/trước–sau, (3) trích dẫn mới dùng, (4) việc còn mở; rồi dừng
  chờ NCS (NCS thường trả lời "commit đi").
- **Đọc nhiều tài liệu:** giao agent (general-purpose) đọc song song, mỗi agent viết đúng một tệp `notes/<khóa>.md`, không sửa tệp
  chung, không dùng git. Sau đó **tự kiểm lại** thông tin thư mục, câu trích và số liệu chính trên bản gốc (trích văn bản bằng
  Python `fitz`, `PYTHONIOENCODING=utf-8`; hình thì kết xuất ảnh trang để xem). Chỉ bạn sửa ma trận, nhật ký, changelog.
- **Git:** chỉ `git add -- <đúng tệp của phiên>`; kiểm `git diff --cached --name-status` trước commit; repo đang có ~330 tệp ở
  trạng thái đã xóa ngoài phiên (không được stage). Commit kết thúc bằng
  `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` (hoặc dòng tương ứng của mô hình đang dùng).
- **Sửa tệp CSV/MD bằng Python:** giữ nguyên BOM và kiểu xuống dòng (đọc/ghi nhị phân); CSV dùng dấu `|`, đọc/ghi bằng module
  `csv`. Heredoc dài trong Bash có thể lỗi — khi đó ghi script ra thư mục scratchpad rồi chạy.
- **Zotero MCP:** đọc metadata, nhập theo DOI/CSL JSON, sửa trường Extra được; **không** tạo linked file được (NCS tự làm trong
  Zotero desktop — N-03). Tải PDF bằng `curl` từ URL truy cập mở (OpenAlex `best_oa_location`, kho trường); kiểm trang đầu khớp DOI.
- **Ngôn ngữ ghi chú:** tiếng Việt học thuật; ký hiệu (a) tác giả nói, (b) giới hạn tác giả tự nêu, **[NCS]** nhận định; mọi ý có trang.
- **Không bao giờ** nhắc kết quả Paper 1; không bịa thư mục; không gọi hệ là "song sinh số" khi chưa khai báo DM/DS/DT;
  không mở rộng sang bảo trì dự đoán/RUL/tối ưu chi phí.
