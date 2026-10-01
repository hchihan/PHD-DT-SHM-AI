# Kế hoạch đọc sâu Giai đoạn 2

Lập ngày 30/09/2026, sau Điểm duyệt 1. Danh sách: 30 tài liệu key (12 Tier 1, 18 Tier 2) ở CLAUDE.md mục 7.1–7.2.
Ma trận: `matrix/literature_matrix.csv` (30 dòng, cột `thu_tu_doc` theo kế hoạch này).

## 1. Nguyên tắc xếp thứ tự

- Tier 1 trước, mỗi phiên 2–3 tài liệu, đọc toàn văn. Tier 2 sau, mỗi phiên tối đa 5 tài liệu, đọc tóm tắt,
  phương pháp và giới hạn.
- Trong mỗi Tier, đọc trước ba tiền lệ [2], [35], [44] (kèm ba bảng ánh xạ thực thể trong `mapping/`) và các
  tài liệu phục vụ ba mục mới 2.1.1, 3.2, 3.6.
- Mỗi tài liệu cho ra một ghi chú `notes/<khóa>.md` theo khuôn 7.4 và một dòng ma trận. Cột Giới hạn tách
  phần tác giả tự nêu và phần nhận định của NCS.
- Tài liệu chưa có PDF thì lùi sang phiên sau; phiên không chờ.

## 2. Thứ tự đọc và tình trạng PDF

Cột "Truy cập" lấy từ OpenAlex ngày 30/09/2026. Cột "PDF" kiểm trên đĩa (kho Zotero và thư mục `pdf/`).

### Tier 1 (4 phiên)

| Phiên | TT | Tài liệu | Khóa | Cụm | Phục vụ | PDF | Ghi chú đọc |
|---|---|---|---|---|---|---|---|
| T1-1 | 1 | [2] Theiler & Smarsly (2018) | 2ILY9YZ3 | Truy vết thông tin | tiền lệ; `mapping/theiler2018.md` | có | toàn văn (T1-1, 30/09/2026) |
| T1-1 | 2 | [35] Bellon và cs. (2025) | NUTL57KJ | Truy vết thông tin | tiền lệ; `mapping/bellon2025.md` | có (kho Zotero, 01/10) | toàn văn (T1-1, 01/10/2026) |
| T1-1 | 3 | [44] García và cs. (2026) | GNTQNBWM | Truy vết thông tin | tiền lệ; `mapping/garcia2026.md` | có | toàn văn (T1-1, 30/09/2026) |
| T1-2 | 4 | [22] Hemker và cs. (2019) | B2JXAM9M | Giá trị quyết định | 2.1.1 | có (01/10) | toàn văn (T1-2, 01/10/2026) |
| T1-2 | 5 | [18] Brake và cs. (2019) | VPFBB9SG | SHM–bu lông–EOV | 3.6 | có | toàn văn (T1-2, 01/10/2026) |
| T1-2 | 6 | [19] Ramasso và cs. (2025) | RWHW6F9I | SHM–bu lông–EOV | 3.6 | có | toàn văn, tiền in arXiv (T1-2, 01/10/2026) |
| T1-3 | 7 | [8] Kritzinger và cs. (2018) | DMIUEEFB | Song sinh số | 2.3 | có | toàn văn (T1-3, 30/09/2026) |
| T1-3 | 8 | [7] Boje và cs. (2020) | 5REDLQK8 | Song sinh số | 2.3 | có | toàn văn (T1-3, 30/09/2026) |
| T1-3 | 9 | [3] Lu và cs. (2020) | 5QX5LTMZ | Song sinh số | 2.3 | có | toàn văn (T1-3, 30/09/2026) |
| T1-4 | 10 | [53] Kapoor & Narayanan (2023) | JQKJGUER | Độ tin cậy đánh giá | 3.4 | có (01/10) | toàn văn (T1-4, 01/10/2026) |
| T1-4 | 11 | [16] Çelik và cs. (2023) | EMTIHHX4 | Truy vết thông tin | 3.5 | có | toàn văn (T1-4, 01/10/2026) |
| T1-4 | 12 | [17] Wu và cs. (2026) | F6XUPQKG | Truy vết thông tin | 3.5 | có | toàn văn (T1-4, 01/10/2026) |

### Tier 2 (4 phiên)

| Phiên | TT | Tài liệu | Khóa | Cụm | Phục vụ | PDF | Ghi chú đọc |
|---|---|---|---|---|---|---|---|
| T2-1 | 13 | [45] Sohn (2007) | MANJDQEZ | SHM–bu lông–EOV | 3.2 | có | toàn văn (T2-1, 01/10/2026) |
| T2-1 | 14 | Figueiredo và cs. (2011) | 23TBQTIP | SHM–bu lông–EOV | 3.2 | có | toàn văn (T2-1, 01/10/2026) |
| T2-1 | 15 | Ju và cs. (2020) | 38FMATHE | SHM–bu lông–EOV | 3.2, 2.1.1 | có (01/10) | toàn văn (T2-1, 01/10/2026) |
| T2-1 | 16 | Cawley (2018) | EBB69J4F | SHM–bu lông–EOV | 3.2, 3.6 | có (01/10) | toàn văn (T2-1, 01/10/2026) |
| T2-1 | 17 | Worden và cs. (2007) | MCNRW6F5 | SHM–bu lông–EOV | 3.1, 3.2 | có (01/10) | toàn văn (T2-1, 01/10/2026) |
| T2-2 | 18 | [56] Da Silva và cs. (2024) | IW7JBB3E | SHM–bu lông–EOV | 3.6 | có | một phần |
| T2-2 | 19 | [57] Bull và cs. (2021) | W7AEKRT8 | SHM–bu lông–EOV | 3.6 | có (01/10) | chưa |
| T2-2 | 20 | [48] Pal và cs. (2022) | SL6IEB2E | SHM–bu lông–EOV | 3.6 | có | chưa |
| T2-2 | 21 | Hughes và cs. (2022) | Z9RD5DMZ | Giá trị quyết định | 3.6 | có (bản tiền in arXiv v2) | có |
| T2-2 | 22 | [80] Bull và cs. (2025) | 5D5H5XGK | Giá trị quyết định | 2.3 | **THIẾU** | chưa |
| T2-3 | 23 | [14] Beleites và cs. (2013) | L97BIAI3 | Độ tin cậy đánh giá | 3.4 | có | chưa |
| T2-3 | 24 | [15] Wheat và cs. (2024) | RG9FMT8Y | Độ tin cậy đánh giá | 3.4 | có | chưa |
| T2-3 | 25 | [28] Kamariotis và cs. (2023) | AESHHWVZ | Giá trị quyết định | 3.2 | có (01/10) | chưa |
| T2-3 | 26 | [10] Chen và cs. (2021) | ESTEYBHA | Song sinh số | 2.3 | có | chưa |
| T2-3 | 27 | [29] Johannes và cs. (2021) | YGZ32C8M | Giá trị quyết định | 2.1 | có | chưa |
| T2-4 | 28 | [42] Ramonell và cs. (2023) | DWT957YI | Song sinh số | 2.3 | có (01/10) | chưa |
| T2-4 | 29 | [21] Hagedorn và cs. (2023) | II3UWN2C | Truy vết thông tin | 3.5 | có | chưa |
| T2-4 | 30 | [82] Seiß và cs. (2025) | JTF8EM7Y | Truy vết thông tin | 3.5 | có | chưa |

Cột "Cụm" và "Phục vụ" của các tài liệu chưa có ghi chú đọc là đề xuất theo tiêu đề và theo vị trí trích hiện
có; cả hai được xác nhận lại khi đọc. Tổng: 20 tài liệu có PDF, 10 tài liệu thiếu.

## 3. PDF còn thiếu trong danh sách key (theo thứ tự ưu tiên đọc)

Lưu vào `pdf/` với tên bắt đầu bằng khóa Zotero (ví dụ `pdf/NUTL57KJ_Bellon2025.pdf`), rồi liên kết vào Zotero
dạng linked file.

| Ưu tiên | Tài liệu | Khóa | DOI | Truy cập | Phiên cần |
|---|---|---|---|---|---|
| 1 | [35] Bellon và cs. (2025) | NUTL57KJ | 10.1016/j.autcon.2025.106157 | mở (hybrid) | T1-1 |
| 2 | [22] Hemker và cs. (2019) | B2JXAM9M | 10.1002/cepa.1045 | **đóng** | T1-2 |
| 3 | [53] Kapoor & Narayanan (2023) | JQKJGUER | 10.1016/j.patter.2023.100804 | mở (gold) | T1-4 |
| 4 | Ju và cs. (2020) | 38FMATHE | 10.1177/1461348419837416 | mở (gold) | T2-1 |
| 5 | Cawley (2018) | EBB69J4F | 10.1177/1475921717750047 | mở (hybrid) | T2-1 |
| 6 | Worden và cs. (2007) | MCNRW6F5 | 10.1098/rspa.2007.1834 | **đóng** | T2-1 |
| 7 | [57] Bull và cs. (2021) | W7AEKRT8 | 10.1016/j.ymssp.2020.107141 | mở (hybrid) | T2-2 |
| 8 | [80] Bull và cs. (2025) | 5D5H5XGK | 10.1177/14759217251316199 | bản in đóng; có bản tiền in ở kho Đại học Aalborg | T2-2 |
| 9 | [28] Kamariotis và cs. (2023) | AESHHWVZ | 10.1016/j.ymssp.2022.109708 | bản in đóng; có bản tiền in arXiv 2202.01859 | T2-3 |
| 10 | [42] Ramonell và cs. (2023) | DWT957YI | 10.1016/j.autcon.2023.105109 | mở (hybrid) | T2-4 |

Hai tài liệu truy cập đóng ([22], Worden 2007) cần tải qua thư viện trường. Với [80] và [28], nên lấy bản in;
nếu chỉ có bản tiền in thì ghi chú đọc ghi rõ phiên bản và số trang theo bản tiền in. Bảy tài liệu có số cũ
trong bảng này chính là bảy tài liệu ở `viec_ton_dong_GD0.md` mục 1.

## 4. PDF thiếu ngoài danh sách key (không chặn Giai đoạn 2)

| Tài liệu | Khóa | DOI | Dùng cho |
|---|---|---|---|
| Cross, Worden & Chen (2011) | KPWFC4PI | 10.1098/rspa.2011.0023 | hoàn thiện câu ở 5.6A.3 |
| Ghazimoghadam & Hosseinzadeh (2024) | G98ZWHKW | 10.1016/j.measurement.2024.114410 | hoàn thiện câu ở 5.6A.3 |
| Hughes và cs. (2022), bản in | Z9RD5DMZ | 10.1016/j.ymssp.2021.108569 | đối chiếu số trang |
| Phares và cs. (2004) | J7FAWJ8I | 10.1061/(asce)1084-0702(2004)9:4(403) | L2.4 (3.2) |
| Graybeal và cs. (2002) | 8IMKCTE5 | 10.1023/a:1022508121821 | L2.4 (3.2) |
| Junker (1969) | W6IUU4MF | 10.4271/690055 | L1.2 (2.1.1) |
| Iordachescu và cs. (2022) | X2UZWVJG | 10.1016/j.engfailanal.2022.106322 | L1.5 (2.1.1) |
| Farrar & Worden, sách Wiley | HQQJMZDW | 10.1002/9781118443118 | L4.1 (3.1); kiểm năm trên trang bản quyền |

Trong sáu tài liệu truy cập đóng của GĐ1, chỉ Worden và cs. (2007) thuộc danh sách key. Năm tài liệu còn lại
cần có trước khi viết các mục 2.1.1, 3.1, 3.2 ở Giai đoạn 4.

## 5. Sản phẩm và điểm duyệt

- Sau mỗi phiên: ghi chú đọc, dòng ma trận, cập nhật `mapping/` (phiên T1-1), commit, dừng chờ NCS xem.
- Sau phiên cuối: ma trận 30 dòng đủ cột và ba bảng ánh xạ, trình Điểm duyệt 2 (NCS kiểm cột Giới hạn).
- Năm dòng đã điền sẵn từ `notes/` ([18], [45], [56], Figueiredo, Hughes) mang dấu "CẦN NCS KIỂM"; ba dòng đầu
  mới đọc một phần và sẽ được đọc lại theo kế hoạch.

## 6. Tiến độ phiên

- **T1-3 (30/09/2026): xong** — [8], [7], [3] đọc toàn văn; ghi chú `notes/DMIUEEFB.md`, `notes/5REDLQK8.md`, `notes/5QX5LTMZ.md`; nhật ký `revision/GD2_nhat_ky_khoang_trong.md` (5 ứng viên).
- **T1-1 (30/09/2026): xong 2/3** — [2], [44] đọc toàn văn; ghi chú `notes/2ILY9YZ3.md`, `notes/GNTQNBWM.md`; bảng ánh xạ `mapping/theiler2018.md`, `mapping/garcia2026.md`; kiểm phản chứng UV-01, UV-03. **[35] Bellon chờ PDF**; `mapping/bellon2025.md` chưa lập.
- **T1-2 (01/10/2026): xong** — [22], [18], [19] đọc toàn văn ([19] bản tiền in arXiv v1); ghi chú `notes/B2JXAM9M.md`, `notes/VPFBB9SG.md` (thay bản đọc một phần), `notes/RWHW6F9I.md`; nhật ký thêm UV-06.
- **PDF (01/10/2026):** NCS tải 8 tệp, đã đổi tên theo khóa Zotero trong `pdf/`. Còn thiếu: [35] Bellon (`NUTL57KJ`) và [80] Bull 2025 (`5D5H5XGK`). Tệp `pdf/Unconfirmed 845287.crdownload` là bản tải dở (0 trang, không có định danh), có thể là một trong hai bài này; cần tải lại.
- **T1-4 (01/10/2026): xong** — [53], [16] (bản in thử), [17] đọc toàn văn; áp khuôn của skill deep-read-phd-papers, phd-gap-miner, govern-phd-evidence; ghi chú `notes/JQKJGUER.md`, `notes/EMTIHHX4.md`, `notes/F6XUPQKG.md`; phân tích liên tài liệu và mức bảo vệ K1–K3: `revision/GD2_phan_tich_khoang_trong_T1.md`; nhật ký thêm UV-07.
- **PDF (01/10/2026):** [35] Bellon đã có trong kho Zotero (19 tr.); T1-1 có thể hoàn tất. [80] Bull 2025 vẫn thiếu.
- **Tier 1: 11/12 đã đọc toàn văn**; còn [35].
- **T1-1 (01/10/2026): xong 3/3** — [35] Bellon đọc toàn văn; ghi chú `notes/NUTL57KJ.md`; bảng ánh xạ `mapping/bellon2025.md`; kiểm [35] như phản chứng cho UV-01 (thu hẹp thêm) và UV-03 (không đổi). **Tier 1: 12/12 đã đọc toàn văn.**
- **T2-1 (01/10/2026): xong** — Worden 2007, Cawley 2018, Ju 2020 đọc toàn văn; [45] Sohn 2007, Figueiredo 2011 đọc bổ sung thành toàn văn. Ghi chú trong `notes/`; 5 dòng ma trận; cột `doan_dung_duoc` trong `GD1_luan_diem_can_nguon.csv`; nhật ký: nhập căn cứ 5.6A cho UV-02, UV-05; tạo UV-08. **Đã đọc toàn văn: 17/30.**
