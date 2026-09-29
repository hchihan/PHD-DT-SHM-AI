# Báo cáo kiểm kê dung lượng Zotero (29/09/2026)

> Phiên chỉ kiểm kê. Không xóa, không chuyển Thùng rác, không sửa bản ghi nào. Mọi số liệu đọc từ
> **bản sao** `zotero.sqlite` (chụp 29/09/2026) và thư mục `C:\Users\VNT\Zotero\storage`.
> Đơn vị MB = 10^6 byte. Dung lượng mỗi tệp = kích thước thư mục `storage/<khóa>/` trừ các tệp đệm
> `.zotero-*` (chỉ mục toàn văn, trạng thái trình đọc; các tệp này không đồng bộ lên máy chủ).

Sản phẩm kèm theo:
- `revision/zotero_kiem_ke_dung_luong.csv`: 678 bản ghi (644 bản ghi thư mục + 34 tệp đính kèm độc lập), phân cách `|`.
- `revision/zotero_tep_dinh_kem.csv`: 549 tệp đính kèm lưu trong storage, sắp theo dung lượng giảm dần (Việc 1.1).

---

## 1. Thống kê dung lượng (Việc 1)

| Chỉ số | Giá trị |
|---|---|
| Tệp lưu trong storage (imported file + imported URL; không tính linked file/URL) | 549 tệp |
| Tổng dung lượng trên đĩa | **2.431,4 MB** |
| PDF | 439 tệp — 2.247,5 MB |
| Snapshot HTML | 107 tệp — 183,9 MB |
| XLSX | 3 tệp — 0,05 MB |
| Tệp đệm `.zotero-*` (không tính ở trên) | 38,5 MB |
| **Đã đồng bộ lên máy chủ Zotero** (syncState = đã đồng bộ) | **98 tệp — 335,3 MB** |
| Chờ tải lên | 451 tệp — 2.096,1 MB |
| 30 tệp lớn nhất | 916,8 MB = **37,7 %** tổng dung lượng |
| Tệp lớn nhất | `EY4H3ZM8` (bài gỗ Nhật Bản, hướng UAV) — 238,0 MB, một mình chiếm 9,8 % |

**Nhận xét chính.** Phần đã đồng bộ (335,3 MB, đo theo kích thước cục bộ) đã vượt hạn mức 300 MB, trong
khi còn 2,1 GB đang chờ tải lên. Máy chủ có thể nén snapshot nên con số quota thật có thể thấp hơn đôi
chút; cần xem số chính xác tại zotero.org/settings/storage. Hệ quả: chỉ xóa bớt tệp thì không thể đưa
toàn bộ thư viện vào 300 MB, vì riêng nhóm BẢO VỆ đã có 1.823 MB. Phương án tệp liên kết (mục 4) là
phương án duy nhất giải quyết được gốc vấn đề.

### 1.3 Tệp trùng

98 bản ghi có ít nhất một dấu hiệu trùng (cột `tep_trung` trong CSV):
- **Snapshot HTML kèm PDF:** 43 snapshot trong nhóm BẢO VỆ đi kèm PDF của cùng bài — 92,7 MB
  (26,5 MB đã đồng bộ). Chỉ đánh dấu, không đề xuất xóa vì thuộc nhóm BẢO VỆ. Nếu NCS cho phép dọn
  riêng loại này thì đây là nguồn giải phóng an toàn nhất (PDF vẫn còn).
- **Nhiều PDF cho một bài:** ví dụ `LDSESVP3` (tài liệu đào tạo BIM, 4 PDF, 50,5 MB), `PHXJ2KJN`, `DFAJFF8J`,
  `M8LMWFQH`, `ZLFATP2Z`, `PRQL4Y8P`, `ESQIRHVE`, `E3TKVJJY` (2 PDF mỗi bài).
- **Bản ghi trùng (cùng DOI hoặc cùng tiêu đề):** ví dụ `CFMKARTI`↔`FN87VGNV` (Sensing Techniques for SHM,
  51,6 + 2,8 MB), `NP4A2BIZ`↔`9EKEI636`, `XVLWEXVZ`↔`KCKVN2FM`, `N54RGGHL`↔`Y44EIXWG`, PROV-O
  (`TMZJ5PYK`, `3XFEVIGR`, `FJJAV9T4`), PROV-DM (`B8QZMS77`↔`M8AI7TWT`), competency questions
  (`K9TSRA2X`↔`Q4PJY4QN`). Việc gộp bản ghi (Merge) là thao tác sửa bản ghi, cần NCS duyệt riêng.
- **Cùng MD5:** `AWZSYR8J`, `M54R42EK`, `AFG4UMCC` là ba bản của cùng một tệp (1,86 MB mỗi bản, hướng UAV).

### 1.4 Bản ghi đính kèm rỗng (không có tệp trên đĩa)

| Khóa đính kèm | Bản ghi cha | Tệp khai báo | Ghi chú |
|---|---|---|---|
| `RHTDGT76` | `SE3JRQTF` (enterprise BIM, ITcon 2022) | 10.36680_j.itcon.2022.053.pdf | Trạng thái "đã đồng bộ" nhưng không có tệp cục bộ; có thể tải về lại từ máy chủ |
| `2U98RKJR`, `TWQJWB88`, `2MNI6S6J` | `D28DT7CE` (Varma & Simon 2006) | các bản PDF | Đã nằm trong Thùng rác; PDF thật đang là tệp liên kết trong `pdf/` |
| `FZD5BAMT`, `VA37SNIK`, `CF3IB3BK` | `6JAQQCGE` (Vabalas 2019) | các bản PDF | Đã nằm trong Thùng rác; PDF thật đang là tệp liên kết trong `pdf/` |

Ngoài ra có 7 thư mục tạm `storage/tmp-*` rỗng (0 MB), không gắn bản ghi nào.
Thùng rác hiện có 6 bản ghi thư mục (0 MB) và 7 tệp đính kèm (0,79 MB). Dọn Thùng rác là xóa vĩnh
viễn, NCS tự thực hiện nếu muốn.

---

## 2. Phân loại mức bảo vệ (Việc 2)

### 2.1 Tiêu chí đã áp dụng

| Tiêu chí | Cách xác định | Số bản ghi thỏa |
|---|---|---|
| Có trong `doi_chieu_danh_muc.csv` | 99 dòng (84 cũ + 15 `moi`), khớp 99/99 theo khóa Zotero hoặc citationKey | 99 |
| Collection bảo vệ | Tên hoặc đường dẫn collection chứa PAPER, RQ, WP, Gate, TIEU_LUAN, CHUYEN_DE, TL-Key, TLTQ (không phân biệt hoa thường; collection con kế thừa) | 529 |
| Có ghi chú con | `itemNotes` gắn với bản ghi | 210 |
| Có tag thủ công | Tag loại 0 (người dùng gắn) trên bản ghi hoặc tệp đính kèm | 215 |
| Được trích trong .docx | Field Zotero trong tệp tiểu luận `HO_CHI_HAN_TIEU_LUAN_TONG_QUAN_23092026_HOANTHIEN.docx` (86 khóa); Paper 1 khớp DOI/tiêu đề (xem 2.2) | 100 |
| Bổ sung thận trọng | Collection `PhD_UAV_Inspection/01_ATCESD_CORE` và `…/02_GSD_DETECTABILITY/TCXD_2026` có dấu hiệu dùng cho bài báo khác | 13 |

Một bản ghi thỏa bất kỳ tiêu chí nào thì vào nhóm BẢO VỆ. Lý do cụ thể ghi ở cột `ly_do` của CSV.

### 2.2 Lưu ý về Paper 1

Đã quét 60 tệp .docx có tên chứa TIEU_LUAN/PAPER/Paper trong `01_PHD_DT_AI_AM`. Chỉ tệp tiểu luận
23/09 có field Zotero. Các bản Paper 1 (v7, v8 pre-submission, v8.1, BUILDINGS_FULL_MANUSCRIPT v3.0,
Paper 1 10.06) **không có field Zotero** (tài liệu tham khảo dạng văn bản tĩnh). Để thay thế, đã khớp
DOI (v7: 34 DOI; v3.0: 22 DOI) và khớp tiêu đề (≥ 30 ký tự) trên v7, v8, v8.1. Mọi bản ghi khớp được
xếp BẢO VỆ. Phương pháp khớp văn bản có thể sót tài liệu có tiêu đề bị viết khác trong Paper 1; rủi ro
này thấp vì toàn bộ nhóm XEM XÉT chỉ nằm trong hai collection UAV và SUSTAINABILITY_REPORT.

### 2.3 Kết quả

| Nhóm | Bản ghi | Tệp | Dung lượng | Trong đó đã đồng bộ |
|---|---|---|---|---|
| BẢO VỆ | 546 | 433 | 1.823,1 MB | 168,4 MB (52 tệp) |
| XEM XÉT | 132 | 116 | 608,3 MB | 166,9 MB (46 tệp) |
| — Đề xuất A (xóa tệp, giữ bản ghi) | 84 | 94 | 573,6 MB | 155,9 MB |
| — Đề xuất B (chuyển Thùng rác) | **0** | 0 | 0 MB | 0 MB |
| — Đề xuất C (NCS quyết định) | 48 | 22 | 34,7 MB | 11,1 MB |

**Vì sao B = 0.** Toàn bộ 132 bản ghi XEM XÉT đều nằm trong collection `PhD_UAV_Inspection` (hướng UAV)
hoặc `SUSTAINABILITY_REPORT`; không có bản ghi nào "không collection". Theo tiêu chí B của NCS, không
bản ghi nào đủ điều kiện. Sáu bản ghi rác lưu từ trình duyệt (`5MZED9C6` "Cart", `TR9NNF4E` "Join
ResearchGate for free", `HGV9KG2R` "Support for Phantom 4 Pro", `Q8G86IWM` "Publications Search
Result", `MCERTWEY` trang mục lục tạp chí, `CA53QHU2` "NATIONAL ASSEMBLY") được xếp C kèm ghi chú "có
dấu hiệu B"; NCS có thể chuyển chúng sang B.

**Quy tắc chia A/C.** A = bài báo tạp chí tiếng Anh tải lại được, không ghi chú, không tag, cộng các bản
ghi trang web trùng với bản ghi bài báo đã có. C = văn bản quy phạm, sổ tay phần mềm, tệp độc lập, tài
liệu tiếng Việt, trang web khó tải lại, và mọi bản ghi không có tệp.

**Câu hỏi cần NCS trả lời trước khi làm A:** hướng UAV (`PhD_UAV_Inspection`) và `SUSTAINABILITY_REPORT`
còn dùng cho bài báo/đề tài nào không? Nếu còn, cả hai nên chuyển sang BẢO VỆ và phương án A chỉ còn
áp dụng cho `EY4H3ZM8` (238 MB, tệp lớn bất thường; nên tải lại bản nhẹ hơn từ nhà xuất bản).

---

## 3. Dung lượng giải phóng theo từng phương án

| Phương án | Giải phóng trên đĩa | Giải phóng trên máy chủ (quota) | Quota còn lại sau khi làm (ước tính từ 335,3 MB) | Tệp chờ tải lên còn lại |
|---|---|---|---|---|
| A (84 bản ghi, 94 tệp) | 573,6 MB | 155,9 MB | ≈ 179 MB | ≈ 1.678 MB |
| B | 0 | 0 | 335 MB | — |
| A + C (nếu NCS duyệt cả C) | 608,3 MB | 166,9 MB | ≈ 168 MB | ≈ 1.655 MB |
| Tệp liên kết cho nhóm BẢO VỆ (mục 4) | 0 trên đĩa (tệp chỉ đổi chỗ) | 168,4 MB | ≈ 167 MB | ≈ 441 MB (chỉ còn nhóm XEM XÉT) |
| **A + tệp liên kết BẢO VỆ** | 573,6 MB | 324,3 MB | **≈ 11 MB** | ≈ 24 MB (nhóm C) |
| Chỉ dọn snapshot kèm PDF trong BẢO VỆ (nếu NCS cho phép) | 92,7 MB | 26,5 MB | ≈ 309 MB | — |

Diễn giải: phương án A giúp quota xuống dưới 300 MB ngay, nhưng khi Zotero tiếp tục tải lên 1,7 GB
còn lại của nhóm BẢO VỆ thì sẽ vượt hạn mức lần nữa sau khoảng 120 MB. Chỉ tổ hợp A + tệp liên kết
mới giữ thư viện ổn định dưới 300 MB mà không phải nâng gói lưu trữ.

---

## 4. Phương án thay thế: tệp liên kết (Việc 3, chưa thực hiện)

**Con số.** Nhóm BẢO VỆ có 433 tệp, 1.823,1 MB (354 PDF = 1.682,4 MB; snapshot HTML = 140,7 MB). Chuyển
sang tệp liên kết thì toàn bộ 1.823,1 MB rời khỏi storage của Zotero; quota máy chủ giảm 168,4 MB
(phần đã đồng bộ) và 1.654,8 MB đang chờ tải lên sẽ không bao giờ cần tải nữa. Dung lượng trên
Google Drive (ổ `H:`) tăng tương ứng khoảng 1,8 GB.

**Lưu ý trước khi làm.**
1. Nhóm BẢO VỆ gồm cả tài liệu của Paper 1, Paper 2, Gate, TLTQ… chứ không chỉ tiểu luận. Nên chọn một
   thư mục gốc chung cấp luận án (ví dụ `…/01_PHD_DT_AI_AM/00_ZOTERO_PDF/`) thay vì dồn tất cả vào
   `pdf/` của tiểu luận. Quy ước hiện tại (`pdf/`, tên tệp bắt đầu bằng khóa Zotero, đã có trong
   `.gitignore`) vẫn giữ cho các tài liệu của tiểu luận.
2. Snapshot HTML không nên chuyển thành tệp liên kết (một snapshot gồm nhiều tệp). Với các bài đã có PDF,
   giải pháp gọn hơn là bỏ snapshot; với bài chỉ có snapshot, giữ dạng lưu trữ.
3. Tệp liên kết không đồng bộ giữa các máy qua Zotero; đồng bộ do Google Drive đảm nhận.

**Các bước trong Zotero desktop (bản 9.0.6).**
1. Sao lưu: đóng Zotero, sao chép `C:\Users\VNT\Zotero\zotero.sqlite` và thư mục `storage` sang nơi an toàn.
2. Settings → Advanced → Files and Folders → **Linked Attachment Base Directory**: chọn thư mục gốc ở
   lưu ý 1. Zotero sẽ lưu đường dẫn tương đối, nên đổi ổ đĩa sau này vẫn giữ được liên kết.
3. Zotero chỉ có sẵn chiều ngược lại (Tools → Manage Attachments → Convert Linked Files to Stored
   Files). Để chuyển stored → linked, dùng plugin **ZotMoov** (hoặc Attanger); kiểm tra plugin có
   hỗ trợ Zotero 9 trước khi cài. Trong plugin: đặt thư mục đích = thư mục ở bước 2, mẫu tên tệp
   `{khóa}_{tác giả}{năm}`.
4. Tạo saved search: Collection thuộc nhóm BẢO VỆ + Attachment File Type = PDF; chọn các tệp đính kèm →
   chuột phải → lệnh chuyển của plugin (ví dụ "Move Selected to Directory").
5. Kiểm tra ngẫu nhiên 10 tệp mở được; chạy lại kiểm kê này để xác nhận storage đã giảm.
6. Settings → Sync → Sync Now. Zotero xóa bản trên máy chủ của các tệp đã chuyển; kiểm tra quota tại
   zotero.org/settings/storage.

Phương án phụ không cần plugin: bỏ chọn "Sync attachment files in My Library" (Settings → Sync). Cách
này dừng việc tải lên nhưng không giải phóng 335 MB đã có trên máy chủ và làm mất PDF khi dùng máy khác.

---

## 5. Danh sách chờ NCS duyệt

### Đề xuất B

Không có bản ghi nào (lý do ở mục 2.3). Nếu NCS muốn, có thể chuyển 6 bản ghi rác đánh dấu "có dấu
hiệu B" trong danh sách C bên dưới sang B.

### Đề xuất C (48 bản ghi)

### C1. Có tệp đính kèm (22 bản ghi)

| # | Khóa | Tiêu đề | Năm | Loại | Collection | MB | Lý do |
|---|---|---|---|---|---|---|---|
| 1 | `QI6SU568` | Agisoft Metashape User Manual: Professional Edition, Version 2.3 | 2024 | report | PhD_UAV_Inspection | 8.56 | tài liệu khó tải lại (văn bản quy phạm, sổ tay, tệp độc lập, tài liệu tiếng Việt, trang web); hướng UAV/kiểm tra bằng ảnh, ngoài phạm vi luận án khung thép; NCS quyết định hướng này còn dùng hay không |
| 2 | `ZHDXX9WJ` | Quyết định số 348/QĐ-BXD ngày 02/4/2021 công bố Hướng dẫn chung áp dụng Mô hình thông tin  | 2021 | report | PhD_UAV_Inspection/09_REGULATIONS_AND_STANDARDS | 6.77 | tài liệu khó tải lại (văn bản quy phạm, sổ tay, tệp độc lập, tài liệu tiếng Việt, trang web); hướng UAV/kiểm tra bằng ảnh, ngoài phạm vi luận án khung thép; NCS quyết định hướng này còn dùng hay không |
| 3 | `G79CRE7D` | Kết hợp dữ liệu đám mây điểm từ các thiết bị 3D Laser scanning và phương tiện bay không ng |  | journalArticle | PhD_UAV_Inspection | 2.64 | tài liệu khó tải lại (văn bản quy phạm, sổ tay, tệp độc lập, tài liệu tiếng Việt, trang web); hướng UAV/kiểm tra bằng ảnh, ngoài phạm vi luận án khung thép; NCS quyết định hướng này còn dùng hay không |
| 4 | `XETJ2QE5` | Kết hợp công nghệ chụp ảnh từ UAV và mặt đất xây dựng dữ liệu không gian địa lý 3D cho thà |  | journalArticle | PhD_UAV_Inspection | 1.94 | tài liệu khó tải lại (văn bản quy phạm, sổ tay, tệp độc lập, tài liệu tiếng Việt, trang web); hướng UAV/kiểm tra bằng ảnh, ngoài phạm vi luận án khung thép; NCS quyết định hướng này còn dùng hay không |
| 5 | `PH64CINF` | Error Assessment of Point Cloud and BIM Models to Actual Works | 2023 | bookSection | PhD_UAV_Inspection | 1.57 | tài liệu khó tải lại (văn bản quy phạm, sổ tay, tệp độc lập, tài liệu tiếng Việt, trang web); hướng UAV/kiểm tra bằng ảnh, ngoài phạm vi luận án khung thép; NCS quyết định hướng này còn dùng hay không |
| 6 | `EFFFVZDH` | ĐÁNH GIÁ TÁC ĐỘNG CỦA MỘT SỐ CÔNG NGHỆ SỐ HÓA 3D ĐỐI VỚI NGHIÊN CỨU BẢO TỒN DI SẢN KIẾN TR | 2020 | journalArticle | PhD_UAV_Inspection | 1.42 | tài liệu khó tải lại (văn bản quy phạm, sổ tay, tệp độc lập, tài liệu tiếng Việt, trang web); hướng UAV/kiểm tra bằng ảnh, ngoài phạm vi luận án khung thép; NCS quyết định hướng này còn dùng hay không |
| 7 | `5U3UFGR3` | Xây dựng quy trình thực hiện dự án Scan to BIM và ứng dụng vào case study | 2023 | journalArticle | PhD_UAV_Inspection | 1.17 | tài liệu khó tải lại (văn bản quy phạm, sổ tay, tệp độc lập, tài liệu tiếng Việt, trang web); hướng UAV/kiểm tra bằng ảnh, ngoài phạm vi luận án khung thép; NCS quyết định hướng này còn dùng hay không |
| 8 | `BRP4AV34` | Ứng dụng công nghệ chụp không ảnh cận thám cung cấp thông tin cho mô hình BIM của dự án hạ | 2018 | journalArticle | PhD_UAV_Inspection | 1.03 | tài liệu khó tải lại (văn bản quy phạm, sổ tay, tệp độc lập, tài liệu tiếng Việt, trang web); hướng UAV/kiểm tra bằng ảnh, ngoài phạm vi luận án khung thép; NCS quyết định hướng này còn dùng hay không |
| 9 | `UXPKCA2I` | Environmental optimization and benchmarking of walls through a BIM plugin: Architectural E |  | webpage | SUSTAINABILITY_REPORT | 1.00 | tài liệu khó tải lại (văn bản quy phạm, sổ tay, tệp độc lập, tài liệu tiếng Việt, trang web); báo cáo phát triển bền vững/LCA, ngoài phạm vi luận án; NCS quyết định hướng này còn dùng hay không |
| 10 | `NW73Q52L` | Empowering sustainable project management: analysing barriers in developing nations / Smar |  | webpage | SUSTAINABILITY_REPORT | 0.94 | tài liệu khó tải lại (văn bản quy phạm, sổ tay, tệp độc lập, tài liệu tiếng Việt, trang web); báo cáo phát triển bền vững/LCA, ngoài phạm vi luận án; NCS quyết định hướng này còn dùng hay không |
| 11 | `HGCEPZCY` | (không tiêu đề) |  | statute | PhD_UAV_Inspection | 0.93 | tài liệu khó tải lại (văn bản quy phạm, sổ tay, tệp độc lập, tài liệu tiếng Việt, trang web); hướng UAV/kiểm tra bằng ảnh, ngoài phạm vi luận án khung thép; NCS quyết định hướng này còn dùng hay không |
| 12 | `I4LH2HQT` | A BIM-based LCA tool for sustainable building design during the early design stage / Smart |  | webpage | SUSTAINABILITY_REPORT | 0.93 | tài liệu khó tải lại (văn bản quy phạm, sổ tay, tệp độc lập, tài liệu tiếng Việt, trang web); báo cáo phát triển bền vững/LCA, ngoài phạm vi luận án; NCS quyết định hướng này còn dùng hay không |
| 13 | `8IBANS8X` | Luật di sản văn hoá 2001 số 28/2001/QH10 áp dụng 2024 | 2025 | webpage | PhD_UAV_Inspection | 0.90 | tài liệu khó tải lại (văn bản quy phạm, sổ tay, tệp độc lập, tài liệu tiếng Việt, trang web); hướng UAV/kiểm tra bằng ảnh, ngoài phạm vi luận án khung thép; NCS quyết định hướng này còn dùng hay không |
| 14 | `EGCHB7H4` | Reconstructing BIM from 2D structural drawings for existing buildings / Request PDF |  | webpage | PhD_UAV_Inspection | 0.83 | tài liệu khó tải lại (văn bản quy phạm, sổ tay, tệp độc lập, tài liệu tiếng Việt, trang web); hướng UAV/kiểm tra bằng ảnh, ngoài phạm vi luận án khung thép; NCS quyết định hướng này còn dùng hay không |
| 15 | `CZFSVTAT` | NGHIÊN CỨU ỨNG DỤNG CÔNG NGHỆ PHOTOGRAMMETRY TÁI HIỆN CÁC HIỆN VẬT LỊCH SỬ TẠI BẢO TÀNG MỸ | 2024 | journalArticle | PhD_UAV_Inspection | 0.77 | tài liệu khó tải lại (văn bản quy phạm, sổ tay, tệp độc lập, tài liệu tiếng Việt, trang web); hướng UAV/kiểm tra bằng ảnh, ngoài phạm vi luận án khung thép; NCS quyết định hướng này còn dùng hay không |
| 16 | `HNY4EZVB` | Thông tư số 32/2026/TT-BXD quy định chi tiết một số điều của Nghị định số 207/2026/NĐ-CP n | 2026 | report | PhD_UAV_Inspection/09_REGULATIONS_AND_STANDARDS | 0.75 | tài liệu khó tải lại (văn bản quy phạm, sổ tay, tệp độc lập, tài liệu tiếng Việt, trang web); hướng UAV/kiểm tra bằng ảnh, ngoài phạm vi luận án khung thép; NCS quyết định hướng này còn dùng hay không |
| 17 | `5MZED9C6` | Cart |  | blogPost | PhD_UAV_Inspection | 0.74 | bản ghi rác lưu từ trình duyệt (trang web, giỏ hàng, trang đăng nhập); có dấu hiệu B nhưng đang nằm trong collection nên không xếp B; hướng UAV/kiểm tra bằng ảnh, ngoài phạm vi luận án khung thép |
| 18 | `RC3BGGV7` | Characterizing Strategies of Fixing Full-Scale Models in Construction Photogrammetric Surv | 2014 | conferencePaper | PhD_UAV_Inspection | 0.74 | tài liệu khó tải lại (văn bản quy phạm, sổ tay, tệp độc lập, tài liệu tiếng Việt, trang web); hướng UAV/kiểm tra bằng ảnh, ngoài phạm vi luận án khung thép; NCS quyết định hướng này còn dùng hay không |
| 19 | `NDR2XMRJ` | TCVN 9381:2012: Hướng dẫn đánh giá mức độ nguy hiểm của kết cấu nhà | 2012 | report | PhD_UAV_Inspection/09_REGULATIONS_AND_STANDARDS | 0.69 | tài liệu khó tải lại (văn bản quy phạm, sổ tay, tệp độc lập, tài liệu tiếng Việt, trang web); hướng UAV/kiểm tra bằng ảnh, ngoài phạm vi luận án khung thép; NCS quyết định hướng này còn dùng hay không |
| 20 | `WA5P3M7X` | ICOMOS. International Charter for the Conservation and Restoration of Monuments and Sites  |  | webpage | PhD_UAV_Inspection | 0.22 | tài liệu khó tải lại (văn bản quy phạm, sổ tay, tệp độc lập, tài liệu tiếng Việt, trang web); hướng UAV/kiểm tra bằng ảnh, ngoài phạm vi luận án khung thép; NCS quyết định hướng này còn dùng hay không |
| 21 | `CA53QHU2` | NATIONAL ASSEMBLY |  | journalArticle | PhD_UAV_Inspection | 0.16 | bản ghi rác lưu từ trình duyệt (trang web, giỏ hàng, trang đăng nhập); có dấu hiệu B nhưng đang nằm trong collection nên không xếp B; hướng UAV/kiểm tra bằng ảnh, ngoài phạm vi luận án khung thép |

### C2. Không có tệp (26 bản ghi, không ảnh hưởng dung lượng)

| # | Khóa | Tiêu đề | Năm | Loại | Collection | MB | Lý do |
|---|---|---|---|---|---|---|---|
| 1 | `2AGFKZXI` | A BIM-based LCA tool for sustainable building design during the early design stage | 2022 | journalArticle | SUSTAINABILITY_REPORT | 0.00 | không có tệp trong storage, xử lý không giải phóng dung lượng; báo cáo phát triển bền vững/LCA, ngoài phạm vi luận án |
| 2 | `35IX73HN` | Close-Range Photogrammetry and 3D Imaging | 2023 | book | PhD_UAV_Inspection | 0.00 | không có tệp trong storage, xử lý không giải phóng dung lượng; hướng UAV/kiểm tra bằng ảnh, ngoài phạm vi luận án khung thép |
| 3 | `6QAUXAF3` | Decision Promulgating the General Guidelines for the Application of Building Information M | 2021 | report | PhD_UAV_Inspection/09_REGULATIONS_AND_STANDARDS | 0.00 | không có tệp trong storage, xử lý không giải phóng dung lượng; hướng UAV/kiểm tra bằng ảnh, ngoài phạm vi luận án khung thép |
| 4 | `97QIP5PF` | Scan4Façade: Automated As-Is Façade Modeling of Historic High-Rise Buildings Using Drones  | 2022 | journalArticle | PhD_UAV_Inspection | 0.00 | không có tệp trong storage, xử lý không giải phóng dung lượng; hướng UAV/kiểm tra bằng ảnh, ngoài phạm vi luận án khung thép |
| 5 | `B77FFHHY` | (không tiêu đề) |  | report | PhD_UAV_Inspection | 0.00 | không có tệp trong storage, xử lý không giải phóng dung lượng; hướng UAV/kiểm tra bằng ảnh, ngoài phạm vi luận án khung thép |
| 6 | `FZAXNHMN` | Building energy technologies towards achieving net-zero pathway: A comprehensive review, c | 2025 | journalArticle | SUSTAINABILITY_REPORT | 0.00 | không có tệp trong storage, xử lý không giải phóng dung lượng; báo cáo phát triển bền vững/LCA, ngoài phạm vi luận án |
| 7 | `GKTL2VRL` | Status, Challenges and Future Directions in the Evaluation of Net-Zero Energy Building Ret | 2024 | journalArticle | SUSTAINABILITY_REPORT | 0.00 | không có tệp trong storage, xử lý không giải phóng dung lượng; báo cáo phát triển bền vững/LCA, ngoài phạm vi luận án |
| 8 | `HGV9KG2R` | Support for Phantom 4 Pro |  | webpage | PhD_UAV_Inspection | 0.00 | bản ghi rác lưu từ trình duyệt (trang web, giỏ hàng, trang đăng nhập); có dấu hiệu B nhưng đang nằm trong collection nên không xếp B; hướng UAV/kiểm tra bằng ảnh, ngoài phạm vi luận án khung thép |
| 9 | `IKWFMTQL` | Decision Approving the Roadmap for the Application of Building Information Modeling (BIM)  | 2023 | report | PhD_UAV_Inspection/09_REGULATIONS_AND_STANDARDS | 0.00 | không có tệp trong storage, xử lý không giải phóng dung lượng; hướng UAV/kiểm tra bằng ảnh, ngoài phạm vi luận án khung thép |
| 10 | `J5IRYGKZ` | (không tiêu đề) |  | report | PhD_UAV_Inspection/09_REGULATIONS_AND_STANDARDS | 0.00 | không có tệp trong storage, xử lý không giải phóng dung lượng; hướng UAV/kiểm tra bằng ảnh, ngoài phạm vi luận án khung thép |
| 11 | `JIDHD28W` | Barriers to Using Cloud Computing in Sustainable Construction in Nigeria: A Fuzzy Syntheti | 2023 | journalArticle | SUSTAINABILITY_REPORT | 0.00 | không có tệp trong storage, xử lý không giải phóng dung lượng; báo cáo phát triển bền vững/LCA, ngoài phạm vi luận án |
| 12 | `KHW5MRKU` | Circular Detailing a Number of Articles of Decree No. 207/2026/ND-CP Regarding Quality Man | 2026 | report | PhD_UAV_Inspection/09_REGULATIONS_AND_STANDARDS | 0.00 | không có tệp trong storage, xử lý không giải phóng dung lượng; hướng UAV/kiểm tra bằng ảnh, ngoài phạm vi luận án khung thép |
| 13 | `L8YXQ64C` | A stakeholder perspective on the challenges of sustainable material management in construc | 2025 | journalArticle | SUSTAINABILITY_REPORT | 0.00 | không có tệp trong storage, xử lý không giải phóng dung lượng; báo cáo phát triển bền vững/LCA, ngoài phạm vi luận án |
| 14 | `MCERTWEY` | Vol. 23, No. 9D, 2025 / Tạp chí Khoa học và Công nghệ Đại học Đà Nẵng |  | webpage | PhD_UAV_Inspection | 0.00 | bản ghi rác lưu từ trình duyệt (trang web, giỏ hàng, trang đăng nhập); có dấu hiệu B nhưng đang nằm trong collection nên không xếp B; hướng UAV/kiểm tra bằng ảnh, ngoài phạm vi luận án khung thép |
| 15 | `Q3E28QMM` | An Overview on LCA Integration in BIM: Tools, Applications, and Future Trends | 2025 | journalArticle | SUSTAINABILITY_REPORT | 0.00 | không có tệp trong storage, xử lý không giải phóng dung lượng; báo cáo phát triển bền vững/LCA, ngoài phạm vi luận án |
| 16 | `Q8G86IWM` | Publications Search Result – The International Association for Automation and Robotics in  |  | blogPost | PhD_UAV_Inspection | 0.00 | bản ghi rác lưu từ trình duyệt (trang web, giỏ hàng, trang đăng nhập); có dấu hiệu B nhưng đang nằm trong collection nên không xếp B; hướng UAV/kiểm tra bằng ảnh, ngoài phạm vi luận án khung thép |
| 17 | `QCLWN6EA` | Analytical Review of Key Barriers in Implementing Sustainable Construction | 2023 | journalArticle | SUSTAINABILITY_REPORT | 0.00 | không có tệp trong storage, xử lý không giải phóng dung lượng; báo cáo phát triển bền vững/LCA, ngoài phạm vi luận án |
| 18 | `QDAS79T4` | Decree Detailing a Number of Articles of the Law on Construction Regarding Quality Managem | 2023 | report | PhD_UAV_Inspection/09_REGULATIONS_AND_STANDARDS | 0.00 | không có tệp trong storage, xử lý không giải phóng dung lượng; hướng UAV/kiểm tra bằng ảnh, ngoài phạm vi luận án khung thép |
| 19 | `RJQKMJKW` | Image-based crack detection approaches: a comprehensive survey | 2022 | journalArticle | PhD_UAV_Inspection | 0.00 | không có tệp trong storage, xử lý không giải phóng dung lượng; hướng UAV/kiểm tra bằng ảnh, ngoài phạm vi luận án khung thép |
| 20 | `RPRF7KG8` | Level of Development Specification, Part I | 2024 | report | PhD_UAV_Inspection | 0.00 | không có tệp trong storage, xử lý không giải phóng dung lượng; hướng UAV/kiểm tra bằng ảnh, ngoài phạm vi luận án khung thép |
| 21 | `SUS4W3PA` | USIBD Level of Accuracy (LOA) Specification, Version 3.1 | 2025 | report | PhD_UAV_Inspection | 0.00 | không có tệp trong storage, xử lý không giải phóng dung lượng; hướng UAV/kiểm tra bằng ảnh, ngoài phạm vi luận án khung thép |
| 22 | `TFBXIDCE` | A Systematic Review of Automated BIM Modelling for Existing Buildings from 2D Documentatio | 2021 | conferencePaper | PhD_UAV_Inspection | 0.00 | không có tệp trong storage, xử lý không giải phóng dung lượng; hướng UAV/kiểm tra bằng ảnh, ngoài phạm vi luận án khung thép |
| 23 | `UGKPZ64T` | Close-Range Photogrammetry and 3D Imaging | 2023 | bookSection | PhD_UAV_Inspection | 0.00 | không có tệp trong storage, xử lý không giải phóng dung lượng; hướng UAV/kiểm tra bằng ảnh, ngoài phạm vi luận án khung thép |
| 24 | `UUQ2SS7C` | A critical review on BIM and LCA integration using the ISO 14040 framework | 2022 | journalArticle | SUSTAINABILITY_REPORT | 0.00 | không có tệp trong storage, xử lý không giải phóng dung lượng; báo cáo phát triển bền vững/LCA, ngoài phạm vi luận án |
| 25 | `UX9NI23D` | Environmental optimization and benchmarking of walls through a BIM plugin | 2025 | journalArticle | SUSTAINABILITY_REPORT | 0.00 | không có tệp trong storage, xử lý không giải phóng dung lượng; báo cáo phát triển bền vững/LCA, ngoài phạm vi luận án |
| 26 | `Y2W6QLPR` | Moving toward Net Zero Carbon Buildings to Face Global Warming: A Narrative Review | 2023 | journalArticle | SUSTAINABILITY_REPORT | 0.00 | không có tệp trong storage, xử lý không giải phóng dung lượng; báo cáo phát triển bền vững/LCA, ngoài phạm vi luận án |
| 27 | `YLDBIAVB` | Empowering sustainable project management: analysing barriers in developing nations | 2025 | journalArticle | SUSTAINABILITY_REPORT | 0.00 | không có tệp trong storage, xử lý không giải phóng dung lượng; báo cáo phát triển bền vững/LCA, ngoài phạm vi luận án |

### Đề xuất A — 20 bản ghi lớn nhất (đầy đủ 84 bản ghi trong CSV)

| # | Khóa | Tiêu đề | Năm | Collection | MB | Đồng bộ |
|---|---|---|---|---|---|---|
| 1 | `EY4H3ZM8` | A deep learning‐based crack damage detection in exterior finish of timber houses in Japan  | 2023 | PhD_UAV_Inspection | 237.99 | chờ tải lên |
| 2 | `AJXVG5JJ` | UAV + BIM: Incorporation of Photogrammetric Techniques in Architectural Projects with Buil | 2020 | PhD_UAV_Inspection | 30.50 | đã đồng bộ |
| 3 | `VJ4CTQH7` | UAV Platforms and the SfM-MVS Approach in the 3D Surveys and Modelling: A Review in the Cu | 2022 | PhD_UAV_Inspection | 25.84 | chờ tải lên |
| 4 | `IV534P26` | EN-LiDAR360 MLS_V7 |  | PhD_UAV_Inspection | 21.61 | đã đồng bộ |
| 5 | `ZUNE8M77` | A Digital Framework for the Implementation of the Circular Economy in the Construction Sec | 2024 | SUSTAINABILITY_REPORT | 21.59 | chờ tải lên |
| 6 | `5HD8H2E8` | BIM-based life cycle assessment: A systematic review on automation and decision-making dur | 2025 | SUSTAINABILITY_REPORT | 13.64 | chờ tải lên |
| 7 | `GU9U25N4` | Net zero energy buildings: An overview of passive and active designs | 2025 | SUSTAINABILITY_REPORT | 12.56 | một phần |
| 8 | `W989MW8H` | Level of Accuracy (LOA) Specification Guide, Version 3.1 |  | PhD_UAV_Inspection | 12.08 | chờ tải lên |
| 9 | `3LIAUXDB` | Implementation of Facility Management for Port Infrastructure through the Use of UAVs, Pho | 2021 | PhD_UAV_Inspection | 11.88 | đã đồng bộ |
| 10 | `KAD3Q96C` | Reconstructing BIM from 2D structural drawings for existing buildings | 2021 | PhD_UAV_Inspection | 10.44 | chờ tải lên |
| 11 | `TS2XQIZ5` | Circular Material Usage Strategies and Principles in Buildings: A Review | 2024 | SUSTAINABILITY_REPORT | 8.68 | chờ tải lên |
| 12 | `GI9EANR2` | Automation of embodied carbon calculation in digital built environment- tool utilizing UK  | 2023 | SUSTAINABILITY_REPORT | 7.89 | chờ tải lên |
| 13 | `H6UN3FDY` | Net Zero in Healthcare Buildings: Lessons from Assessing the Strategies of 214 NHS Trusts  | 2025 | SUSTAINABILITY_REPORT | 7.37 | một phần |
| 14 | `IXSTKWY8` | Scanning Technologies to Building Information Modelling: A Review | 2022 | PhD_UAV_Inspection | 6.81 | đã đồng bộ |
| 15 | `2FJ7S4I2` | Surface Damage Detection in Hydraulic Structures from UAV Images Using Lightweight Neural  | 2025 | PhD_UAV_Inspection | 6.64 | đã đồng bộ |
| 16 | `F2MMXE6H` | Combining inverse photogrammetry and BIM for automated labeling of construction site image | 2019 | PhD_UAV_Inspection | 6.60 | đã đồng bộ |
| 17 | `WLNB93CY` | Combined use of Terrestrial Laser Scanning and UAV Photogrammetry in producing the LoD3 of | 2022 | PhD_UAV_Inspection | 6.15 | chờ tải lên |
| 18 | `27XV83J7` | Deep learning in crack detection: A comprehensive scientometric review | 2025 | PhD_UAV_Inspection | 6.14 | đã đồng bộ |
| 19 | `D73467DY` | Detecting surface defects of heritage buildings based on deep learning | 2024 | PhD_UAV_Inspection | 5.67 | đã đồng bộ |
| 20 | `YGDGPSY2` | Scan-to-BIM method in construction: assessment of the 3D buildings model accuracy in terms | 2022 | PhD_UAV_Inspection | 5.42 | chờ tải lên |

---

Sau khi NCS duyệt từng danh sách, phiên sau mới thực hiện; mọi thao tác chỉ chuyển vào Thùng rác hoặc xóa tệp đính kèm, không xóa vĩnh viễn.
