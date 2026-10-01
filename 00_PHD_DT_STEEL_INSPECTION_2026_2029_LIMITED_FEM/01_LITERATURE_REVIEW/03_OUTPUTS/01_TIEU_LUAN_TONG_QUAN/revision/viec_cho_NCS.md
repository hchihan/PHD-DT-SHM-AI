# Việc chờ NCS kiểm hoặc bổ sung

Lập ngày 01/10/2026 theo yêu cầu của NCS: công việc tiếp tục, các việc cần NCS kiểm hoặc bổ sung được gom ở đây để cập nhật
sau. Mỗi việc có mã `N-xx`. Khi xong, NCS ghi ngày vào cột "Xong" (hoặc báo để cập nhật); các tệp nguồn được sửa theo cột
"Nơi cập nhật".

Cột **Chặn**: việc nào phải chờ mục này. "Không" = có thể làm tiếp, chỉ cần quay lại trước điểm duyệt ghi trong cột.

## A. Tài liệu và PDF

| Mã | Việc | Chi tiết | Nơi cập nhật | Chặn | Xong |
|---|---|---|---|---|---|
| N-01 | PDF [80] Bull 2025 | `5D5H5XGK`, DOI 10.1177/14759217251316199; bản in đóng, có thể có bản tiền in ở kho Đại học Aalborg. Lưu `pdf/5D5H5XGK_Bull2025.pdf` | ma trận dòng 22; `notes/5D5H5XGK.md` | Hoàn tất ĐD2 (dòng 22); không chặn GĐ3 | |
| N-02 | Bốn PDF không tải được | Condotta 2023 `QBTTSBTH` (phản chứng CMMS, UV-01; kho air.iuav.it chặn Cloudflare — NCS tải tay từ trình duyệt); Junker 1969 `W6IUU4MF` (L1.2); Iordachescu 2022 `X2UZWVJG` (L1.5); Ghazimoghadam 2024 `G98ZWHKW` (câu autoencoder 5.6A.3) | `viec_ton_dong_GD0.md` mục 5.1 | UV-01 (mục CMMS); câu 5.6A.3; viết 1.2 (GĐ4) | |
| N-03 | Liên kết PDF vào Zotero (linked file) | Cross `KPWFC4PI`, Graybeal `8IMKCTE5`, Phares `J7FAWJ8I`, Papic `EKAT6IMC`, Gardner `GXVWFUSA`; cùng các tệp tải ngày 29/09–01/10 trong `pdf/` chưa liên kết (thêm phiên 15: Mitchell `82WQNDHU`, Mosqueira-Rey `73MBWFVJ`) | Zotero desktop: Add Attachment → Attach Link to File | Không (trước GĐ6) | |
| N-04 | Bản in của các tài liệu đang đọc ở bản tiền in | [19] Ramasso (arXiv v1), Hughes 2022 (arXiv v2), [28] Kamariotis (arXiv v2), [14] Beleites (bản thảo tác giả), [16] Çelik (bản in thử), Cawley 2018 (bản trực tuyến), Mitchell 2019 `82WQNDHU` (arXiv v2; dự kiến tr. in = 219 + tr. PDF), Maes 2022 `2ZJSENQU` (postprint): đối chiếu số trang trước khi dẫn trang | `notes/` tương ứng; `5_6A_luan_diem_nguon.csv` | Không (trước GĐ6) | Hoãn đến GĐ6 (NCS, 01/10/2026) |
| N-05 | PDF Chen và cs. 2018 `QZ7E3HDV` | Nguồn phản chứng CMMS cho UV-01 (cùng Condotta) | nhật ký UV-01 | UV-01 vào GĐ3 | |
| N-41 | Lưu PDF Maes và cs. 2022 `2ZJSENQU` | Bản postprint trên Lirias (KU Leuven), 49 MB; kho không truy cập được bằng curl từ máy này, Claude đã đọc qua trình duyệt tích hợp. NCS tải từ https://lirias.kuleuven.be/retrieve/0de07146-3e22-4d32-b275-927f0eac667b, lưu `pdf/2ZJSENQU_Maes2022_postprint.pdf` và liên kết vào Zotero | `notes/2ZJSENQU.md` | Không (trước GĐ6, để kiểm lại trang) | Hoãn đến GĐ6 (NCS, 01/10/2026) |

## B. Kiểm nội dung (Điểm duyệt 2)

| Mã | Việc | Chi tiết | Nơi cập nhật | Chặn | Xong |
|---|---|---|---|---|---|
| N-10 | Kiểm 28 dòng ma trận mang dấu "CẦN NCS KIỂM" và dòng 13–14 (đã bỏ dấu khi đọc lại, chưa được NCS kiểm) | Trọng tâm cột **Giới hạn** (tách phần tác giả và nhận định NCS) và cột **Cụm**. Danh sách dòng ở `DD2_ban_trinh.md` mục 2 | `matrix/literature_matrix.csv` (xóa dấu sau khi kiểm) | ĐD2 | |
| N-11 | Cụm của [29] Johannes | Đề xuất đổi sang "Truy vết thông tin" (từ "Giá trị quyết định") | ma trận dòng 27 | Không | |
| N-12 | Mức căn cứ của ba bài | (a) [28] Kamariotis có tính là căn cứ độc lập cho UV-05 (nhóm TUM – ETH; chỉ một câu ở tr. 1–2)? (b) [14], [15] có tính là căn cứ phương pháp gián tiếp cho UV-06? (c) [42] Ramonell có tính là căn cứ TG gián tiếp cho UV-04? (d) Maes 2022 `2ZJSENQU` có tính là căn cứ độc lập (hiện trường) cho UV-06? (e) Mosqueira-Rey 2023 `73MBWFVJ` (tổng quan) có tính là căn cứ độc lập cho UV-07? (thêm 01/10/2026, phiên 15) | `GD2_nhat_ky_khoang_trong.md` | ĐD3 (đếm căn cứ) | (d), (e): 01/10/2026 — NCS **tính** cả hai là căn cứ độc lập, loại "cùng chiều". (a)–(c) còn mở |
| N-13 | Ba bảng ánh xạ thực thể | `mapping/theiler2018.md`, `bellon2025.md`, `garcia2026.md` — sản phẩm của GĐ2 | `mapping/` | ĐD2 | |

## C. Phản chứng còn "chưa kiểm" (quy tắc 7.4: ứng viên chỉ vào GĐ3 khi hết "chưa kiểm")

| Mã | Ứng viên | Mục chưa kiểm | Cần gì | Chặn | Xong |
|---|---|---|---|---|---|
| N-20 | UV-01 | CMMS trên nguồn chuyên về CMMS | PDF Chen 2018 (N-05) hoặc Condotta 2023 (N-02); hoặc NCS chấp nhận dùng [29] Johannes (tr. 7, 11: CMMS phân tán, không trạng thái hóa) làm đối chiếu thay thế. **Phiên 15 (01/10):** Chen 2018 xác nhận truy cập đóng; Condotta 2023 bị Cloudflare; ứng viên mới Hosamo và cs. 2022 (*Energy Build.* 261: 111988, CC BY, DOI 10.1016/j.enbuild.2022.111988) — ba kho đều chặn tải tự động, chưa nhập. NCS chọn: (a) chấp nhận [29]; hoặc (b) tải tay Condotta/Hosamo vào `pdf/` | UV-01 chốt ở GĐ3 (UV-01 vào GĐ3 nháp ở trạng thái tạm) | 01/10/2026 — NCS chọn **(a)**: dùng [29] Johannes (tr. 7, 11) làm đối chiếu thay thế; Chen 2018, Condotta 2023 ghi "đã nhập, đối chiếu qua mô tả của [35] tr. 3, chưa đọc bản gốc"; không tìm Hosamo 2022. UV-01 vào GĐ3 chính thức |
| N-21 | UV-02 | Thẻ mô hình (Mitchell 2019, chưa có trong Zotero); PROV-O [69]; MLflow/DVC | Đồng ý để Claude xác minh DOI và nhập Mitchell 2019; đọc PROV-O (chuẩn W3C, mở) | UV-02 vào GĐ3 | 01/10/2026 (Claude, phiên 15): Mitchell `82WQNDHU` nhập + đọc; PROV-O, MLflow/DVC, SSN System Capabilities đã kiểm — đều một phần |
| N-22 | UV-04 | Sepasgozar 2021 [9] | Claude đã kiểm (PDF có trong Zotero): không giải quyết | — | 01/10/2026 |
| N-23 | UV-06 | Nghiên cứu theo dõi dài hạn sau bảo trì | Đồng ý để Claude tìm 1–2 nguồn qua Consensus/OpenAlex, xác minh và nhập Zotero | UV-06 vào GĐ3 | 01/10/2026 (Claude, phiên 15): Maes 2022 `2ZJSENQU` (KW51) nhập + đọc; không giải quyết, căn cứ hiện trường cùng chiều |
| N-24 | UV-07 | Học máy có người trong vòng (human-in-the-loop); thẻ mô hình | Như N-21 và N-23 | UV-07 vào GĐ3 | 01/10/2026 (Claude, phiên 15): Mosqueira-Rey 2023 `73MBWFVJ` nhập + đọc; không giải quyết, cùng chiều; thẻ mô hình không giải quyết |
| N-25 | UV-08 | Toàn văn Hu 2023 (Eraliev 2022 Claude đã kiểm 01/10/2026: không giải quyết); 7 ứng viên Consensus chưa nhập Zotero | Đồng ý để Claude nhập Hu 2023 và tìm PDF | UV-08 (đề xuất giữ làm luận điểm 3.2, không thành K4) | 01/10/2026 (Claude, phiên 15): Hu 2023 `BBAUS2Z8` nhập; truy cập đóng, kiểm ở mức tóm tắt — không giải quyết. Còn mở nếu NCS cần toàn văn (thư viện) |

## D. Văn bản, số liệu, quyết định đang chờ

| Mã | Việc | Chi tiết | Nơi cập nhật | Chặn | Xong |
|---|---|---|---|---|---|
| N-30 | Nghị định 207/2026: ngày ban hành | Tên Thông tư 32/2026 ghi 15/6/2026; NCS xác nhận để điền trường Date của `R5P8K8CG` | Zotero; `viec_ton_dong_GD0.md` mục 3 | Không | |
| N-31 | Nghị định 207/2026: Điều 34, 37 | Đối chiếu đoạn đang trích ở 1.1 | `tieuluan/01_chuong1.md` | GĐ5 | |
| N-32 | Năm bản in [80] Bull | Crossref ghi trực tuyến 13/03/2025, tập 25(4); danh mục đang ghi 2025, đề xuất 2026 theo bản in — cần xác minh | `doi_chieu_danh_muc.csv` | GĐ6 | |
| N-33 | Năm sách Farrar & Worden `HQQJMZDW` | Kiểm trang bản quyền (Crossref ghi 2012) | Zotero | GĐ4 (viết 3.1) | |
| N-34 | Duyệt mục 1.3A, 1.4A | Đang chờ duyệt từ 30/09 | `tieuluan/01_chuong1.md` | GĐ4 mục 4.3 | |
| N-35 | Duyệt danh sách 80 câu giới hạn | Phân loại A/B/C | `revision/danh_sach_cau_gioi_han.csv` | GĐ5 | |
| N-36 | Ba đề xuất schema từ [44] | Tách nhiệm vụ; phiên bản bộ luật quyết định; mã băm (`mapping/garcia2026.md` Phần D) | CLAUDE.md mục 8 | GĐ4 mục 4.7 (viết 5.5) | |
| N-37 | Gộp bản ghi trùng trong Zotero | PROV-DM, PROV-O, ISO 55000 (`viec_ton_dong_GD0.md` mục 2) | Zotero desktop | GĐ6 | |
| N-38 | Better BibTeX | Cân nhắc cài trước GĐ6 (chỉ 3/84 bản ghi có citation key) | Zotero | GĐ6 | |
| N-39 | Tệp Perplexity gốc | `Số liệu chính thức mới nhất về quy mô khu công nghiệp Việt Nam.md` ở thư mục gốc, chưa theo dõi bằng git: chuyển vào `revision/` hay để nguyên? | — | Không | |
| N-40 | Nhận định NCS cho L1.1 và L1.4 | Câu nhận định từ thực tế kiểm định (nhà khung thép phổ biến trong KCN; tránh gián đoạn sản xuất) — NCS viết hoặc duyệt câu nháp | `revision/L1_1_so_lieu_KCN_da_kiem.md` | GĐ4 mục 4.2 (viết 1.2) | |

## E. Ghi nhận cho GĐ5 (không cần NCS làm ngay)

- Câu ở `03_chuong3.md` về "so sánh kiến trúc dưới giao thức chưa kiểm soát rò rỉ" là diễn giải, không phải lời [15] (`notes/RG9FMT8Y.md`).
- Câu ở `05_chuong5.md` gọi đối tượng của [82] là "hồ sơ kiểm tra" (đã ghi CLAUDE.md 6.2).
- Bảng ở `03_chuong3.md` ghi "lần chạy, ngày đo, chi tiết vật lý" cho [15]: mỗi bộ dữ liệu chỉ dùng hai cấp.
- Số liệu không thống nhất trong nguồn, không dẫn: [56] (1,25 % / 0,3 %), [48] (95,80 % / 95,4 %), [14] (141 / 140 ca), [15] (32 / 33 bài), [10] (5 / 6 giai đoạn).
