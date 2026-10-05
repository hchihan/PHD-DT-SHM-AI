# Prompt phiên GĐ3: cập nhật, kiểm tra, viết khoảng trống và ba mục tiêu

Đọc trước, theo thứ tự:
1. `CLAUDE.md`, bản ở commit `5bd3eb2`. Đọc kỹ mục 2 (quyết định 5, 7, 9–11), 2A, 6.0, 8, 11 và 13. **Khi mâu thuẫn với
   `revision/prompt_ban_giao.md` thì CLAUDE.md thắng.** Phạm vi đã rút gọn: hai khoảng trống G-A, G-B; ba mục tiêu MT1–MT3;
   không mở rộng tổng quan.
2. `revision/GD2_nhat_ky_khoang_trong.md` (bản chưa commit của phiên Nhiệm vụ 1).
3. `revision/DD2_ban_trinh.md` mục 3–4 và `revision/viec_cho_NCS.md`.

Phiên này **không** tìm tài liệu, **không** chạy Consensus, **không** tải PDF, **không** nhập Zotero, **không** sửa tệp
trong `tieuluan/`.

## Bước 0. Commit phần việc còn treo của Nhiệm vụ 1

- Changelog của phiên đó đã nằm trong commit `5bd3eb2`; **không** stage lại `revision/changelog.md` ở bước này.
- Chỉ `git add` đúng 9 tệp:
  - `matrix/doi_chieu_danh_muc.csv`
  - `revision/GD2_nhat_ky_khoang_trong.md`
  - `revision/DD2_ban_trinh.md`
  - `revision/viec_cho_NCS.md`
  - `notes/82WQNDHU.md`, `notes/73MBWFVJ.md`, `notes/2ZJSENQU.md`, `notes/BBAUS2Z8.md`, `notes/lebo2013provo.md`
- Trước khi commit, chạy `git status` và `git diff --cached --stat`. Nếu vùng stage có tệp khác thì dừng và báo.
- Không stage các tệp chưa theo dõi khác (.docx, .pptx, .xlsx, .csl, `TLTQ_28.09.2026/`, `~$*`).

## Bước 1. Ghi các quyết định của NCS (01/10/2026)

- **N-20 (CMMS, UV-01): chọn (a).** Dùng [29] Johannes (tr. 7, 11) làm đối chiếu thay thế. Chen 2018 `QZ7E3HDV` và
  Condotta 2023 `QBTTSBTH` ghi "đã nhập, đối chiếu qua mô tả của [35] tr. 3, chưa đọc bản gốc". Không tìm Hosamo 2022 nữa.
  UV-01 vào GĐ3 **chính thức**, kèm ghi chú mức đối chiếu.
- **N-12d, e: tính** Maes 2022 `2ZJSENQU` là căn cứ độc lập cho UV-06, và Mosqueira-Rey 2023 `73MBWFVJ` là căn cứ độc lập
  cho UV-07, theo quy ước đếm nhóm tác giả. Ghi rõ cả hai là căn cứ "cùng chiều".
- **N-41, N-04:** hoãn đến GĐ6, phiên này không làm.
- Cập nhật ba tệp: `viec_cho_NCS.md` (cột Xong), `DD2_ban_trinh.md` mục 3, nhật ký.

## Bước 2. Kiểm tra (chỉ trên tài liệu đã có, không đọc thêm)

Lập bảng kiểm cho mọi ứng viên sẽ đi vào G-A hoặc G-B:

| Ứng viên | Vào | Căn cứ độc lập trước 2025 (tính theo nhóm tác giả, kèm trang) | Tỉ trọng nguồn 2025–2026 | Còn "chưa kiểm"? | Phát biểu đã thu hẹp (1 câu) |
|---|---|---|---|---|---|

- G-A gồm UV-02, UV-06. G-B gồm UV-01, UV-05, UV-07.
- UV-03 (K2): ghi là **yêu cầu của schema** (C3).
- UV-08: ghi là **luận điểm của 3.2** và nội dung của trường `applicable_conditions` / `obs_context`.
- UV-04: ghi là **định vị ở 2.3** (khai báo mức DS theo [8]).
- Ở cấp khoảng trống (G-A, G-B), kiểm ba điều:
  - (i) có ít nhất 3 căn cứ độc lập ngoài nhóm 2025–2026;
  - (ii) không còn mục "chưa kiểm";
  - (iii) mọi trang dẫn đều có trong `notes/`.
- Chỗ nào không đạt thì ghi rõ, **không vá bằng nhận định chung**.

## Bước 3. Viết `revision/GD3_khoang_trong_va_muc_tieu.md` (tối đa khoảng 3 trang, văn xuôi học thuật)

**Phần A — Hai khoảng trống.** Mỗi khoảng trống gồm:
1. Phát biểu, 1–2 câu.
2. Phần đã được giải quyết, kèm tiền lệ bắt buộc nêu ở CLAUDE.md 6.1:
   - G-A: SSN `ssn-system:Condition`, PROV-O, thẻ mô hình, MLflow/DVC, [53].
   - G-B: [35], IFC4, BCF 3.0, [44], `IfcApproval`.
3. Phần còn thiếu, chính là phát biểu đã thu hẹp.
4. Căn cứ: ít nhất 3, có trang.
5. Vì sao quan trọng với quản lý kiểm tra – bảo trì nhà xưởng (góc nhìn ngành QLXD).
6. Mục tiêu nào đáp ứng.

Tách rõ bằng chứng (tài liệu nói gì) với diễn giải (NCS suy ra gì). Không dùng chữ "đầu tiên" hay "chưa có nghiên cứu
nào"; dùng "trong các tài liệu đã rà soát".

**Phần B — Ba mục tiêu.** Viết lại MT1, MT2, MT3 **đúng phạm vi CLAUDE.md 2A**. Không thêm mục tiêu, không thêm chỉ số
ngoài mục 8. Mỗi mục tiêu gồm:
1. Phát biểu mục tiêu: một câu, có động từ đo được.
2. Câu hỏi nghiên cứu (RQ1 ↔ MT1, RQ2 ↔ MT2, RQ3 ↔ MT3).
3. Nội dung thực hiện: 3–4 ý.
4. Dữ liệu và tài sản đã có:
   - dữ liệu ba đợt thí nghiệm;
   - BIM nhà xưởng thật;
   - cam kết lắp cảm biến;
   - schema rút gọn;
   - hồ sơ kiểm định cũ làm B0.
5. Tiêu chí hoàn thành: dùng các tiêu chí đo ở 2A và 4 chỉ số M1–M4 ở mục 8.
6. Sản phẩm: Bài 1 / Bài 2 / chương luận án.
7. Một rủi ro chính và phương án giảm. MT3: quan trắc ngắn hơn dự kiến thì vẫn đủ cho tuyên bố khả thi và truy vết; Bài 2
   không phụ thuộc MT3.

Không dùng kết quả Paper 1 (chỉ mô tả thiết kế và công cụ).

**Phần C — Ma trận một bảng:** Khoảng trống → Mục tiêu → RQ → Bài báo → Chương luận án → Chỉ số.

**Phần D — Văn bản đề xuất thay mục 5.2 và mục RQ của tiểu luận** (≤ 800 từ; trích `\[n\]` hoặc `\[@KHÓA\]` theo
CLAUDE.md 4.4). Chỉ để NCS duyệt, **chưa** chèn vào `tieuluan/`.

Áp skill strict-writing-discipline cho phần văn xuôi.

## Bước 4. Cập nhật và commit

- CLAUDE.md mục 12:
  - GĐ2 đóng (29/30; 5 nhóm phản chứng đã xử lý theo bước 1);
  - GĐ3: bản nháp xong, chờ NCS duyệt và gửi thầy.
- `revision/changelog.md`: thêm mục cho phiên này.
- Commit chỉ các tệp của phiên: tệp mới `GD3_...md`, CLAUDE.md, changelog, cùng các tệp sửa ở bước 1. Kiểm vùng stage
  trước khi commit như bước 0.

## Báo cáo cuối phiên (ngắn), sau đó DỪNG

1. Hai khoảng trống: mỗi khoảng trống 2 dòng, kèm số căn cứ trước 2025.
2. Ba mục tiêu: mỗi mục tiêu 1 dòng, kèm sản phẩm.
3. Bảng kiểm ở bước 2: chỉ nêu các chỗ không đạt (nếu có).
4. Danh sách tệp đã sửa, mã commit.
5. Việc phiên sau: chèn 5.2 và RQ vào `tieuluan/05_chuong5.md` sau khi NCS duyệt; rồi chuyển sang hoàn thiện Bài 1.
