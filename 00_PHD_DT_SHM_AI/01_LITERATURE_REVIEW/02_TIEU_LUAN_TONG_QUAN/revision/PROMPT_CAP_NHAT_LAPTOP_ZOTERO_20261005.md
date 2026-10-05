# Prompt cho Claude Code trên laptop có Zotero (05/10/2026)

Dán toàn bộ phần dưới đường kẻ vào Claude Code, mở tại thư mục `02_TIEU_LUAN_TONG_QUAN` trên laptop.

---

Bạn đang làm việc trên repo Tiểu luận tổng quan của NCS Hồ Chí Hân, trên laptop có cài Zotero và Zotero Word plugin. Repo nằm trên
Google Drive; đường dẫn trên laptop có thể khác máy bàn (ví dụ `H:\My Drive\...` thay cho `G:\My Drive\...`). Thư mục làm việc là
`00_PHD_DT_SHM_AI/01_LITERATURE_REVIEW/02_TIEU_LUAN_TONG_QUAN`; gốc Git là `03_RESEARCH/01_PHD_DT_AI_AM`, nhánh `revision-v2`.

Trước khi làm gì, đọc toàn bộ `CLAUDE.md` (đặc biệt QĐ 17, QĐ 18 và mục 4 quy tắc) và `README.md`. Mỗi bước dưới đây kết thúc bằng một
dòng báo cáo; gặp điểm dừng thì dừng và hỏi tôi.

## Bối cảnh

Trên máy bàn, phiên 05/10/2026 đã:
- sửa tối thiểu bản chốt theo QĐ 18: B1 gồm khả năng kiểm thuộc tính bắt buộc của IDS (nguồn de Marco và cs. 2024, khóa Zotero `QVMQGE3K`,
  DOI 10.3390/buildings14072206; số [73] trong Markdown, [87] trong bản Word) ở 4.4, 4.6.3, Bảng 5.6, bảng thuật ngữ; sửa câu 3.4.1;
- tạo `00_BAN_CHOT/HO_CHI_HAN_TIEU_LUAN_TONG_QUAN_BAN_CHOT_20261005.docx` bằng cách vá XML từ bản 04/10 (không có Zotero đang chạy);
- dựng lại từ `tieuluan/` bằng `xuat_ban/build.py` với bộ đệm `xuat_ban/zotero_cache.json`, khớp văn bản 934/934 đoạn với bản 05/10.
Các thay đổi này **có thể chưa được commit** khi bạn bắt đầu.

## Bước 1. Kiểm đồng bộ Google Drive và trạng thái Git

1. Chạy `git status` ở gốc repo. Nếu có tiến trình Git khác hoặc tệp `.git/index.lock`, dừng và báo tôi (repo nằm trên Drive, không được
   chạy Git đồng thời trên hai máy).
2. Tính SHA-256 các tệp sau và so với giá trị của máy bàn. Nếu khác, Drive chưa đồng bộ xong: dừng, báo tôi, không sửa gì.

```
f5344f2fbc1952998c172ae899a62c41031abfcee2204a1a01c122818cfedc74  00_BAN_CHOT/HO_CHI_HAN_TIEU_LUAN_TONG_QUAN_BAN_CHOT_20261005.docx
6dcc79bd362db7019076e0f51b3b13f430837548346d84919ef3366a86182125  tieuluan/01_chuong1.md
9063e60ee4f0dc4df383d6407e47466ee2acac076ffbace07ec5de9b37ad4636  tieuluan/03_chuong3.md
4f802388d099a8348deb40f2f84661a9470f2e62f13eb78e0d57626c60677122  tieuluan/04_chuong4.md
4ce3e4fa86d9518169ff43d8b59248d0f6ecd7ac28efd3b9de3ca9a35268b0a6  tieuluan/05_chuong5.md
1af5d9f1311b4cdd5e47f5e3ff3ec8cb6cbc464903e8f40c7f3e7dbf5c1bcf71  tieuluan/00_thuatngu.md
```
(`CLAUDE.md` có thể đã khác vì được sửa sau khi tính mã băm; không dùng nó để kiểm đồng bộ.)

## Bước 2. Môi trường

Kiểm `python --version`, `pandoc --version`, `python -c "import docx"`. Thiếu thì cài theo `README.md` (`pip install -r requirements.txt`;
pandoc bằng `winget install --id JohnMacFarlane.Pandoc -e --scope user`). Cài phần mềm là việc tôi đã cho phép trong prompt này; không cài
gì khác.

## Bước 3. Đối chiếu bộ đệm với thư viện Zotero (chỉ đọc)

Zotero phải đang mở; API cục bộ `http://localhost:23119/api/users/0`.
1. Lấy danh sách khóa ở cột `khoa_zotero` của `xuat_ban/danh_muc_Zotero.csv` (90 khóa). Với mỗi khóa, tải CSL-JSON từ Zotero và so với
   `xuat_ban/zotero_cache.json` ở các trường: title, author, issued, container-title, volume, issue, page, DOI, URL.
2. Kiểm riêng `QVMQGE3K`: có trong thư viện, DOI đúng như trên, có tệp PDF đính kèm hay không, ghi chú đọc trong Zotero có không.
3. Lập bảng: khóa | trạng thái (trùng / khác trường nào / không có trong Zotero). **Không sửa bộ đệm, không sửa Zotero.**
4. **Điểm dừng 1:** báo bảng cho tôi. Chỉ khi tôi đồng ý mới làm mới bộ đệm (xóa đúng các mục tôi chỉ định khỏi `zotero_cache.json` để
   `build.py` tải lại).

## Bước 4. Dựng lại bản Word

1. Chạy `python xuat_ban/build.py HO_CHI_HAN_TIEU_LUAN_TONG_QUAN_REBUILD_20261005` (sinh trong `xuat_ban/`, không ghi đè `00_BAN_CHOT/`).
2. Kiểm kết quả in ra: 90 tài liệu, 261 nhóm trích dẫn, 0 thẻ `[CẦN KIỂM]`.
3. So văn bản từng đoạn của bản dựng với `00_BAN_CHOT/..._BAN_CHOT_20261005.docx`, bỏ qua đoạn mục lục, danh mục bảng, hình và
   chỗ giữ chỗ "(Cập nhật…)". Mong đợi: không khác. Có khác thì liệt kê, không sửa gì.

## Bước 5. Làm việc trong Word (tôi thao tác, bạn hướng dẫn và kiểm)

Trên bản `00_BAN_CHOT/..._BAN_CHOT_20261005.docx`:
1. Tôi mở bằng Word, chọn Zotero → Refresh. Nếu Zotero hỏi về trích dẫn đã sửa tay hoặc không tìm thấy mục, ghi lại nguyên văn và dừng.
2. Tôi cập nhật mục lục, danh mục bảng, danh mục hình (Ctrl+A, F9), lưu.
3. Sau khi tôi lưu, bạn kiểm lại: số trích dẫn [87] xuất hiện ở 4.4 và 4.6.3; danh mục tài liệu vẫn 90 mục, mục [87] là de Marco 2024;
   văn bản thân bài vẫn khớp bản dựng ở bước 4. Tính lại SHA-256 tệp và ghi vào báo cáo.

## Bước 6. Slide (chỉ làm khi tôi đồng ý ở điểm dừng 2)

**Điểm dừng 2:** hỏi tôi có sửa slide không. `00_BAN_CHOT/BAO_CAO_TLTQ_BAN_CHOT_20261004.pptx` còn ghi B1 là "IFC 4.3/BCF 3.0" ở slide 11, 12,
16, 20 và ghi chú thuyết trình của các slide đó. Nếu tôi đồng ý: lưu thành tệp mới `..._20261005.pptx`, chỉ đổi cụm mô tả B1 thành
"IFC 4.3, BCF 3.0, IDS và các tiền lệ gần nhất" (giữ cỡ chữ theo `README.md`), chạy `revision/HT21_slide_scripts/overflow_check.ps1`
để kiểm chữ tràn, xuất PDF. Không đổi nội dung khác.

## Bước 7. Commit (chỉ khi tôi đồng ý ở điểm dừng 3)

Theo `CLAUDE.md` mục 4.3: chỉ `git add` đúng đường dẫn của phiên; không dùng `git add -A`, `git add .`, `commit -a`. Trước khi commit
chạy `git status` và `git diff --cached --stat`; nếu vùng stage có tệp ngoài danh sách dưới đây thì dừng.

Danh sách được phép (đường dẫn tương đối từ thư mục tiểu luận):
`.gitignore`, `CLAUDE.md`, `README.md`, `requirements.txt`, `revision/changelog.md`, `revision/PROMPT_CAP_NHAT_LAPTOP_ZOTERO_20261005.md`,
`tieuluan/00_thuatngu.md`, `tieuluan/01_chuong1.md`, `tieuluan/03_chuong3.md`, `tieuluan/04_chuong4.md`, `tieuluan/05_chuong5.md`,
`00_BAN_CHOT/HO_CHI_HAN_TIEU_LUAN_TONG_QUAN_BAN_CHOT_20261005.docx`, và `xuat_ban/zotero_cache.json`, `xuat_ban/danh_muc_Zotero.csv`
nếu bước 3–4 làm chúng thay đổi. Không commit: bản dựng trong `xuat_ban/`, slide (bị `.gitignore` loại), ba ảnh `.jpg` ở gốc thư mục.

**Điểm dừng 3:** trình danh sách tệp và nội dung commit, chờ tôi đồng ý. Thông điệp commit tiếng Việt, kết thúc bằng dòng
`Co-Authored-By: Claude <noreply@anthropic.com>` (hoặc dòng ghi công mà Claude Code trên laptop đang dùng). Không push.

## Báo cáo cuối

Một bảng ngắn: bước | kết quả | bằng chứng (lệnh, số liệu, mã băm) | việc còn mở. Thêm một dòng vào `revision/changelog.md` mô tả phiên
trên laptop (chỉ sau khi tôi duyệt nội dung dòng đó).
