# P2A-0 — Kiểm toán thư mục Paper 2 (Pha 0, vai AU)

**Ngày lập:** 02/10/2026 · **Prompt:** `PROMPT_PHAN_BIEN_PAPER2_THU_MUC_VA_KHOANG_TRONG_20261002.md` (Pha 0) · **Trạng thái:** chờ NCS duyệt tại ĐIỂM DỪNG 0.
**Vai:** chỉ kiểm kê và đối chiếu (AU). Chưa phản biện nội dung khoa học; phần đó thuộc Pha 1.

---

## 0. Phạm vi, cách làm, giới hạn

**Đã đọc (nguồn hiệu lực cao, dùng làm chuẩn đối chiếu):**
- `revision/GD3b_khoang_trong_va_muc_tieu.md` (toàn văn).
- `CLAUDE.md` (toàn văn, 499 dòng).
- `tieuluan/phuluc.md` (toàn văn; Phụ lục A, B).
- `notes/NUTL57KJ.md` ([35] Bellon 2025), `mapping/bellon2025.md`, `notes/GNTQNBWM.md` (García 2026): phần đầu và các dòng liên quan.
- Trong project: tệp 00 v1.1 và `PROMPT_KHOI_DONG_PAPER2_v2_20261002.md`.
- `tieuluan/05_chuong5.md` và `04_chuong4.md` đã chép về nhưng **chưa đọc ở Pha 0**. Chúng sẽ được đọc ở Pha 1–2 khi đối chiếu nội dung. Phụ lục A, B là phần chương 5 cần cho Pha 0, đã đọc đủ.

**Đã đọc hết (thư mục chính `05_PAPER_2_TRACEABILITY/`):**
- 61 tệp văn bản: md, docx, pptx, csv nhật ký và ma trận, 2 tệp tóm tắt Zotero.
- docx và pptx được chuyển sang text bằng pandoc và python-pptx. **Ảnh trong docx/pptx không được xem.**
- Cách đọc: chia thành 5 nhóm (A, B1, B2, C1, C2), mỗi nhóm một người kiểm toán phụ đọc từ dòng đầu đến dòng cuối. Mỗi nhóm có báo cáo chi tiết riêng ở các phụ lục `P2A_0_phuluc_*.md`, có trích dòng.
- **Không đọc:**
  - 5 PDF trong `01_EVIDENCE/PDF/`: là toàn văn nguồn, dùng ở Pha 2.
  - Các tệp Zotero thô: ris, csv thư viện ~0,7 MB, json, py.
- Thư mục phụ `06_PAPER_3_FIELD_FEASIBILITY/`: đọc cả 2 tệp.

**Giới hạn:**
1. **Ổ Google Drive không mount được vào shell của máy.** Mọi tệp được đọc qua bản sao chép về (snapshot 02/10/2026). SHA-256 tính trên bản sao (`sha256_p2.txt`, 67 tệp).
2. Ngày sửa (mtime) lấy từ danh sách thư mục trên máy, giờ Việt Nam. Ngày ghi *trong* tệp có thể khác (xem 2.2).
3. **Số dòng trích ở các phụ lục là số dòng của bản text chuyển đổi.** Nếu chuyển lại, số dòng có thể lệch.
4. **Nơi ghi sản phẩm.** Prompt đề xuất `03_PAPERS/PAPER_2/audit_YYYYMMDD/`, nhưng thư mục `03_PAPERS/` chưa có ở gốc luận án. Bản này được ghi tạm vào thư mục con **mới** `05_PAPER_2_TRACEABILITY/P2A_audit_20261002/`; không sửa hay di chuyển tệp gốc nào. Đường dẫn cuối: **[NCS XÁC NHẬN]**.

---

## 1. Kết luận nhanh cho NCS (≤ 10 dòng)

- **Toàn bộ hồ sơ trong thư mục được lập trước khi khóa phạm vi (01/10).** Không tệp nào khớp với phạm vi đã khóa ở các điểm sau:
  - 6 thực thể, 5 ràng buộc, B0/B1, M1–M4 (M2 là chỉ số chính);
  - ĐG1–ĐG3; G-B là khoảng trống chính;
  - công cụ Python + SQLite, không dùng SHACL.
- Vì vậy **không có tệp nào "Còn hiệu lực" làm nguồn quyết định phạm vi.** Chỉ còn hai vai:
  - **tài sản tham khảo** (đáng giữ: mục 6);
  - **lỗi thời** (bị GD3b, CLAUDE.md §8 hoặc prompt v2 thay).
- **Lỗ lớn nhất cho ĐG3:** chuỗi 24–27/09 (REFINED v1.0, NotebookLM, hai pptx) đã **đưa ACTION/STATUS_EVENT ra ngoài lõi Paper 2**. Điều này ngược với G-B (khoảng trống chính). Tài sản thiết kế duy nhất cho C6 là `ACTION_STATUS_EVENT` cùng luật R11–R13 trong `gate2_3_data_model_v0.2`.
- **Số liệu BIM chưa truy được về dữ liệu gốc** trong thư mục: 6 IFC, 3.356, 10.328, 718/676, 8 cặp GUID. Đây là điều kiện chặn cho mục Case study.

---

## 2. Kiểm kê tệp

### 2.1 Bảng kiểm kê

Ký hiệu trạng thái: **HL** Còn hiệu lực · **LT** Lỗi thời (ghi nguồn thay) · **TR** Trùng (ghi bản giữ) · **TK** Tham khảo.
Nguồn thay: **GD3b**, **CL8** (CLAUDE.md §8, §2A), **PV2** (prompt v2).

#### a. Gốc thư mục

| # | Tệp | Loại | Sửa (máy) | Vai trò | Trạng thái | Ghi chú ngắn |
|---|---|---|---|---|---|---|
| 1 | `PROMPT_PHAN_BIEN_PAPER2_THU_MUC_VA_KHOANG_TRONG_20261002.md` | md | 02/10 09:03 | prompt | **HL** | Prompt đang chạy |
| 2 | `PROMPT_KHOI_DONG_PAPER2.md` (v1) | md | 02/10 07:24 | prompt | **LT** – PV2 | Vẫn dùng GAP 1–3, C1–C3, 10 thực thể, R01–R17, SPARQL/SHACL, M1–M3 (Phụ lục B2 §4.2). Bản v2 nằm ở `01_TIEU_LUAN_TONG_QUAN/` và trong project, không nằm trong thư mục này |
| 3 | `BAO_CAO_TONG_HOP_PAPER2_GATE2_GATE3_DINH_HUONG_THUC_THI_20260915.docx` | docx | 16/09 07:45 | định hướng | **LT** – GD3b, CL8; TK | Không có phần kiểm độ mới 16/09. Có ví dụ minh họa (GUID X, H01) dễ bị nhầm với số thật |
| 4 | `PAPER2_GATE2_GATE3_MASTER_EXECUTION_LOCK_20260915.md` | md | 16/09 15:52 | định hướng (tự nhận "authoritative") | **LT** – GD3b, CL8; TK | Tên ghi 15/09 nhưng sửa 16/09 sau kiểm độ mới. Gọi 718 phần tử và 8 cặp GUID là "CONFIRMED"; cần hạ xuống "nghi ngờ" |
| 5 | `GATE2_GATE3_GIAI_THICH_DE_HIEU_VA_HUONG_PAPER_20260916.docx` | docx | 16/09 15:25 | định hướng (giải thích) | **TR** → giữ #6 | |
| 6 | `GATE2_GATE3_GIAI_THICH_DE_HIEU_VA_HUONG_PAPER_20260916_v2.docx` | docx | 16/09 16:06 | định hướng (giải thích) | **LT** – GD3b; TK | Kết luận §8 vẫn ghi "4 bài cần đọc", mâu thuẫn §6 của chính tệp |
| 7 | `GATE2_3_PROGRESS_20260923.docx` | docx | 23/09 16:51 | nhật ký tiến độ | **TK** | Nguồn thứ cấp duy nhất của 6 IFC / 3.356 / 10.328 / 676 / 596 / 16/16. Tệp kỹ thuật gốc không có trong thư mục |
| 8 | `gate2_3_data_model_v0.2.docx` | docx | 24/09 07:38 (trong tệp ghi 23/09) | dữ liệu (đặc tả) | **LT** – CL8; **TK quan trọng** | 8 thực thể mới + 4 bảng cũ = 12, không phải "10". SHACL là cơ chế chính (D1). Là nguồn trường, luật R01–R15, CQ01–CQ12 để ánh xạ sang 6 thực thể |
| 9 | `DE_XUAT_PAPER2_GIAI_THICH_HUONG_DONG_GOP_KHOANG_TRONG_20260924.docx` | docx | 24/09 10:26 | định hướng | **LT** – GD3b | Nhánh song song viết trên nền 15–16/09 (5 CQ, GAP 1–3, 718/16), không tiếp nối #8. 4 hình chưa xem |
| 10 | `OUTLINE_PAPER2_20260924.docx` | docx | 24/09 10:33 | outline | **TR** → giữ #11/#12 | Giữ phần 4 rủi ro (Bellon, hai cách đánh số, 718/676, Level_Name) |
| 11 | `PAPER2_MANUSCRIPT_OUTLINE_COMPLETE.docx` | docx | 24/09 14:50 | outline | **LT** – CL8; TK | Outline chi tiết nhất. Ghi "mười thực thể" nhưng liệt kê 11; bỏ ACTION/STATUS_EVENT |
| 12 | `PAPER2_OUTLINE_HOAN_CHINH_BIEN_TAP.docx` | docx | 24/09 15:58 | outline (biên tập) | **LT** – CL8; TK | **Bản outline cuối theo thời gian.** Bản biên tập của #11; thêm "Claude/MCP điều phối" vào Methods, trái #11 |
| 13 | `PAPER2_BAO_CAO_DINH_HUONG_OUTLINE_VA_KE_HOACH_THUC_THI_GATE2_GATE3.docx` | docx | 24/09 16:17 | định hướng + kế hoạch | **LT** – GD3b, CL8; **TK quan trọng** | Nguồn duy nhất của K1–K11 và sổ D001–D026. Có R16/R17 [ĐỀ XUẤT] và sổ tương ứng 1:10 → 1:1 |
| 14 | `PAPER2_COMPLETE_ACADEMIC_OUTLINE_AND_EXECUTION_GUIDE.docx` | docx | 24/09 16:25 | outline + phụ lục | **LT** – CL8; TK | Không trùng #13: là bản tái cấu trúc, mới hơn. Có thêm M0, Phụ lục D (CDE) và Phụ lục F (mức đọc nguồn) |
| 15 | `PAPER2_REFINED_DIRECTION_PROVENANCE_VALIDITY_IDENTITY_v1.0.25092026.docx` | docx | 25/09 16:04 | định hướng (tinh chỉnh) | **LT** – GD3b (trái G-B) | **Bản cuối của hướng đi.** Khung P/V/I, Gap 2A–2C. Loại ACTION/STATUS_EVENT; đẩy Khoảng trống 3 sang WP4/G5. Có danh sách 15 bằng chứng còn thiếu và cảnh báo "tệp nguồn kỹ thuật không có trong repository" |
| 16 | `PAPER2_NOTEBOOKLM_HUONG_DAN_HOC_VA_AUDIO_OVERVIEW_25092026.docx` | docx | 25/09 16:20 | tài liệu học | **TK** | Bản thứ cấp của #15; không có số liệu |
| 17 | `ChuyenDe2_Paper2_Traceability.pptx` | pptx | 27/09 14:29 | trình chiếu (trình thầy) | **LT** – GD3b; TK | Nội dung đầy đủ hơn #18 |
| 18 | `ChuyenDe2_Paper2_DUT.pptx` | pptx | 27/09 14:36 | trình chiếu (Hội đồng) | **TR** → giữ #17 làm bản nội dung | Theo mtime, #18 sửa **sau** #17 7 phút. Đây là bản rút gọn kiểu Hội đồng: có mục lục, tên hai thầy và câu hỏi góp ý về 2A–2C. Phụ lục B1 suy ngược thứ tự; mtime thắng |

#### b. `01_EVIDENCE/` — văn bản định hướng, nhật ký, giao diện

| # | Tệp | Sửa (máy) | Vai trò | Trạng thái | Ghi chú |
|---|---|---|---|---|---|
| 19 | `PAPER2_GATE2_GATE3_CURRENT_DIRECTION_20260915.md` | 15/09 21:48 | định hướng | **TR** → giữ #4 (đều LT) | Bản rút gọn của #4 |
| 20 | `PAPER2_DRAFT_OUTLINE_GATE2_GATE3_20260914.docx` (v0.1) | 14/09 12:19 | outline | **LT** | Có 8 CQ, 10 ca T01–T10, 8 chỉ số |
| 21 | `PAPER2_GATE2_GATE3_ORIENTATION_JOURNAL_v0.2_20260914.docx` | 14/09 12:46 | outline + đọc sơ bộ | **LT**; TK (DSR, ablation) | **Toàn bộ số [SIM] không được dùng**; có lỗi nội tại ("6 verdict sai" thực ra là 10) |
| 22 | `G2_ONE_PAGE_TRACEABILITY_DRAFT_20260914.md` | 14/09 11:21 | đặc tả Gate 2 | **TK** | Nguồn của 3 lớp trạng thái độc lập và MULTI_CANDIDATE |
| 23 | `G1_TO_G2_CONDITION_EVIDENCE_INTERFACE_v1.0.md` | 13/09 16:01 | đặc tả giao diện | **TK quan trọng** (cho mối nối 1A → P2) | Tên ghi v1.0, nội dung ghi v1.1. Tự mâu thuẫn về điểm cuối chuỗi: L15 kết thúc ở `Action_Status`, L74 ở `Action_Record_ID` |
| 24 | `README_CURRENT.md` | 15/09 22:00 | con trỏ | **LT** | Trỏ tới thư mục lưu trữ không tồn tại |
| 25–31 | `00_CLEANUP_REPORT.md`, `00_CONSOLIDATION_PLAN.md`, 5 tệp csv nhật ký `00_*` | 15/09 | nhật ký dọn dẹp | **TK** | 81/81 MOVE SUCCESS, hash trước = sau. Hậu tố "PRE_FAILURE" không có giải thích. Bố cục thư mục thực tế khác bố cục trong manifest |

#### c. `01_EVIDENCE/` — đọc sâu, kiểm độ mới, ma trận

| # | Tệp | Vai trò | Trạng thái | Ghi chú |
|---|---|---|---|---|
| 32 | `00_BIBLIOGRAPHIC_VERIFICATION.md` | nhật ký | **HL** (phần sửa metadata) | CORE01 = Jäkel et al. 2025 (Zotero thiếu tác giả đầu) |
| 33–37 | `01_CORE01…` (Jäkel 2025), `02_CORE02_HAGEDORN…`, `03_CORE03_YIN…`, `04_CORE04_MATARNEH…`, `05_CORE05_SEISS…` | đọc sâu | **HL** (mô tả bài); mục "Implication" **LT** | 5 bản duy nhất có số trang. CORE01, CORE02 có chỗ lệch trang cần đối chiếu PDF |
| 38 | `07_BORKOWSKI_2026_FULLTEXT_REVIEW.md` | đọc sâu toàn văn | **HL**; thay #45 và dòng NQ3KGDWN của #50 | Không có số trang, chỉ có tên mục |
| 39 | `08_CORRECTION_PASS_SUMMARY.md` | nhật ký | **LT** một phần | Chưa tính García và Bellon |
| 40–43 | `10_NOVELTY_CHECK_A–D` (Gragnaniello, Mariniello, García, Bellon) | kiểm độ mới | A, B: **HL**. C (García): **LT** – bị `notes/GNTQNBWM` thay (toàn văn 30/09). D (Bellon): **LT** – bị `notes/NUTL57KJ` thay (toàn văn 01/10) | A, B, C đọc qua NotebookLM, không có trang. D chỉ có abstract |
| 44 | `10_NOVELTY_CHECK_SUMMARY_20260916.md` | kiểm độ mới | **LT** một phần | Dùng GAP 1/2/3 và C1/C2/C3 cũ |
| 45 | `G1_02_BORKOWSKI_2026.md` | ghi chú (chỉ abstract) | **LT** – bị #38 thay | |
| 46–56 | `G1_01_FANG`, `G2_01…05` (Sacks, Stolk, Oraskari, Kücükavci, Beach), `G3_01_CICCARESE`, `G3_02_WAN`, `MULTI_01…03` (Lee–Eastman–Solihin, Lorvão Antunes, Kim) | ghi chú đọc sâu | **TK** (dùng cho ma trận đối thủ ở Pha 2) | Không có số trang PDF. Một số mâu thuẫn với #59 (Phụ lục C2 §6) |
| 57 | `06_TARGETED_GAP_AUDIT.md` | kiểm toán khoảng trống | **LT** một phần | Nhãn GAP-A…H trùng tên nhưng khác nghĩa G-A/G-B. Gọi GAP-E "mạnh nhất" mà chưa tính García |
| 58 | `03_TARGETED_DEEP_READ_SELECTION.md` | chọn bài | **LT** một phần | Ghi Borkowski "no PDF" |
| 59 | `G2_G3_SCREENING_EVIDENCE_AND_GAP_REPORT.md` (04/08), `G2_G3_RECENT_EVIDENCE_SCREENING_2023_2026.md` (04/08) | sàng lọc | **LT** một phần | Bị các bản đọc sâu sau thay; mâu thuẫn về Nuyts 2024 |
| 60 | `G2_G3_ROUND4_…_20260809.md`, `G2_G3_CORE_TRACEABILITY_DEEP_READ_20260901.md`, `GAP2_GAP3_NEW_FULLTEXT_DEEP_READ_20260901.md` | đọc sâu | **TK** (có trang) | Có trang PDF kèm trang in |
| 61 | `02_EXCLUDED_PAPERS_SUMMARY.md`, `01_ZOTERO_TARGETED_SCREENING.csv`, `05_TARGETED_EVIDENCE_MATRIX.csv`, `06_CORE5_EVIDENCE_MATRIX.csv` | ma trận, sàng lọc | 05 **HL** (bản sau hiệu chỉnh); 06, 01, 02 **TK** | Đếm lệch: pool ghi 22, cộng ra 21 |

#### d. Thư mục con

| # | Thư mục / tệp | Vai trò | Trạng thái | Ghi chú |
|---|---|---|---|---|
| 62 | `01_EVIDENCE/PDF/` (5 PDF: Hagedorn, Yin, García = applsci-16-02562, 2 bài Elsevier) | dữ liệu nguồn | **TK** (Pha 2) | Chưa đọc ở Pha 0 |
| 63 | `01_EVIDENCE/ZOTERO/` (gồm `zotero_final/`, `zotero_import_ready/`) | dữ liệu thư viện | **TK** | Chỉ đọc 2 tệp summary: thư viện 199 bài, 35 đã có, 164 mới, MR0005 chưa giải |
| 64 | `06_PAPER_3_FIELD_FEASIBILITY/` (2 tệp, v2.2 ngày 04/08) | định hướng MT3 | **LT** – GD3b, CL2A | Xem điểm lệch Đ15 ở mục 4 |

### 2.2 Chuỗi phiên bản của văn bản định hướng và outline

Thứ tự sắp theo mtime trên máy; đối chiếu chéo nội dung ở các Phụ lục A, B1, B2.

| Bước | Ngày | Văn bản | Đổi gì so với bước trước |
|---|---|---|---|
| 0 | 13/09 | Giao diện G1 → G2 v1.1 (#23) | Hợp đồng `Condition_Evidence`, 37 phép thử âm định nghĩa trước. Chuỗi kết thúc ở `Action_Status` |
| 1 | 14/09 11:21 → 12:46 | G2 one-page (#22) → Outline v0.1 (#20) → Journal v0.2 (#21) | Thêm 3 lớp trạng thái độc lập, 5 CQ → 8 CQ, 10 ca T01–T10, 8 chỉ số; quyết định D1–D11; số [SIM] |
| 2 | 15/09 20:31 → 22:00 | Đọc sâu targeted (#38, #57), dọn thư mục, Current Direction (#19), README (#24) | Khung GAP 1/2/3, C1–C3, 5 CQ; đóng tìm kiếm (CLOSE_SEARCH) |
| 3 | 16/09 07:45 → 16:06 | Báo cáo tổng hợp (#3) → Kiểm độ mới 4 bài (#40–44) → Master Lock (#4) → Giải thích v1/v2 (#5, #6) | Thêm kiểm độ mới: García HIGH hẹp; Bellon chưa đóng (chỉ abstract) |
| 4 | 23/09 → 24/09 07:38 | Progress (#7) + Data model v0.2 (#8) | Đổi sang SHACL; 8 + 4 thực thể; CQ01–CQ12; R01–R15; 16 ca âm (16/16); M1–M3. Đối chiếu IFC 23/09 cho kết quả 0 GUID trùng trong IFC xuất ra |
| 4b | 24/09 10:26 | Đề xuất (#9) | **Nhánh song song** trên nền 15–16/09 |
| 5 | 24/09 10:33 → 15:58 | Outline (#10) → Manuscript outline (#11) → Biên tập (#12) | 4 điểm đóng góp chuyển thành C1–C3 và RQ2.1–2.3; thêm CORRESPONDENCE; bỏ ACTION; thêm đáp án độc lập của người thứ hai |
| 6 | 24/09 16:17 → 16:25 | Báo cáo định hướng (#13) → Complete academic outline (#14) | #13 gom K1–K11 và D001–D026. #14 tái cấu trúc thành outline bài báo, thêm M0 |
| 7 | 25/09 16:04 → 16:20 | REFINED v1.0 (#15) → NotebookLM (#16) | **Xoay trục** sang P/V/I và Gap 2A–2C; loại ACTION/STATUS_EVENT |
| 8 | 27/09 14:29 → 14:36 | Slide Traceability (#17) → slide DUT (#18) | Giữ khung 25/09 nhưng dùng lại thân kỹ thuật 23–24/09 (SHACL, 12 CQ) |
| 9 | 02/10 07:24 | Prompt v1 (#2) | Không thừa kế #15; quay lại GAP 1–3, C1–C3 |
| — | 01–02/10 | **GD3b, CLAUDE.md §8, Phụ lục A–B, tệp 00, prompt v2** | **Khóa phạm vi (nguồn hiệu lực cao)**: thay toàn bộ chuỗi trên |

**Bản cuối:**
- Hướng đi: #15 (25/09).
- Outline: #12 (24/09 15:58), với #11 là bản chi tiết nhất.
- Báo cáo có mã quyết định: #13.

Cả ba **lỗi thời** so với phạm vi khóa.

---

## 3. Số liệu và quyết định treo

### 3.1 Số liệu (có tệp nguồn, mức xác nhận)

**Quy tắc chung:** mọi số dưới đây là **tự báo cáo**. Tệp nguồn kỹ thuật không có trong thư mục: registry, `.ttl`, `real_defect_cases_v0.1.csv`, `decision_history.csv`, verification bundle. Tệp #15 (L56, L358) cũng ghi chúng không có trong repository ngày 25/09.

| Số liệu | Giá trị | Tệp nguồn (thứ cấp) | Mức theo quy tắc | Mâu thuẫn |
|---|---|---|---|---|
| Phiên bản IFC đã đăng ký | 6 (IFC4X3_ADD2, có SHA-256) | #7 (L34); nhắc lại ở #11, #13, #17, #18 | Tự báo cáo; **[CẦN NGUỒN: registry]** | — |
| Prototype component | 3.356 | #7 (L36) | Tự báo cáo | Quan hệ với 676/718 chưa được giải thích |
| Binding (liên kết) | 10.328 | #7 (L36); #8 (L310) | Tự báo cáo | — |
| Audit Revit chỉ đọc | 718 phần tử (= 676 + 41 + 1), 16 ElementId | #4 (L221, L284), #20, #3, #9 (L112) | #4 gọi "CONFIRMED"; #3, #20 ghi "chưa kiểm lại" | **K4 treo**: 718/16 so với 676/596 |
| Audit 13/09 | 676 cấu kiện kết cấu = 596 Framing + 56 Cột + 24 Móng | #7 (L48), #20 | Tự báo cáo | K4 |
| Level_Name trống | ở toàn bộ 596 Framing | #7 (L100), #15 (L442) | Tự báo cáo | Chưa giải thích nguyên nhân |
| IfcGUID tham số trùng | 8 cặp / 16 phần tử (RD-001…RD-008) | #7 (L48–L54), #8 (L302), #4, #22 | **Chỉ là NGHI NGỜ** (quy tắc PV2). #4 ghi "CONFIRMED", không đạt mức này | #7 (L54): IFC xuất ra có 0 GlobalId trùng; #9 vẫn ghi "nghi ngờ do timeout" |
| Phần tử lệch GUID | 573442 mang IfcGUID của 563079 | #8 (L264), #15 (L123) | Tự báo cáo | — |
| Kiểm thử âm | **16/16, 0 dương tính giả (23/09)** | #7 (L68), #8 (L276, L290) | **Chỉ là kiểm thử đơn vị.** Chính #8 (L278) tự cấm trích như kết quả nghiên cứu | — |
| Lần chạy nháp M2/M3 (nghĩa cũ) | 2/2; 5,5 ms; 5 bước nối | #8 (L291–L292) | Dữ liệu mẫu cực nhỏ; không dùng | — |
| decision_history | 0 dòng | #7 (L94), #15 | — | — |
| Tiêu chí đóng Gate 2 | 10, 11 hoặc 12 | #4 (§12), #14 (B.2), #13 (Bảng 15.1) | — | Ba con số khác nhau |
| Số phép thử âm | 9 loại (#4); 10 ca T01–T10 (#20); 16 NT (#8); 37 CE-NEG (#23); 10 nhóm (slide); 7 nhóm (tiểu luận 23/09) | như trên | — | Khác **~30 lỗi, 4 nhóm** của phạm vi khóa |
| Số liệu Paper 1 xuất hiện trong thư mục | Macro-F1 RF 1,000 / 0,986 / 0,875; SD_fold 0,139; 216 recording | #3 (L440), #15 (L64), #11 | Sở hữu của **1A (R1, R2)** theo tệp 00. Paper 2 chỉ trích, không trình bày như kết quả mới | #11 có thêm 0,690, không có ở nguồn khác |
| Số [SIM] của Journal v0.2 | 30 đối tượng, 240 trường, 38/40… | #21 Phần C | **Giả lập; cấm dùng** | Có lỗi nội tại |

### 3.2 Quyết định và mã treo

Cột cuối là **đề xuất đóng theo nguồn cao**. Đây là đề xuất của AU, chưa áp dụng, chờ NCS duyệt.

| Mã | Nội dung | Tệp nguồn | Trạng thái trong thư mục | Đề xuất đóng theo nguồn cao |
|---|---|---|---|---|
| K1 | C1–C3 hay bốn điểm đóng góp | #13 (L171) | Treo | Đóng bằng **ĐG1–ĐG3** (PV2). Cả hai cách cũ bị thay |
| K2 | 5 hay 12 CQ | #13 (L172) | Treo (gắn D016) | Đóng bằng **3 câu hỏi truy ngược**, chốt sau phỏng vấn F-2 (CLAUDE.md QĐ 12). Ứng viên CQ05/CQ06/CQ07 (Phụ lục B2 §8.2) |
| K3 | 9 loại hay 7 nhóm lỗi | #13 (L173) | Treo | Đóng bằng **4 nhóm, ~30 lỗi** (PV2). Số lỗi mỗi nhóm [NCS XÁC NHẬN] lúc khóa |
| K4 | 718/16 hay 676/596 | #13 (L174) | **Treo, chặn** | [NCS XÁC NHẬN] từ tệp audit gốc; ghi phạm vi category của từng con số |
| K5 | 8 cặp GUID: nghi ngờ hay đã đối chiếu | #13 (L175) | Dùng nguồn 23/09 | Giữ **NGHI NGỜ** đến khi chạy lại đối chiếu (PV2 Pha 4) |
| K6 | Đã chạy 16 ca trước khi Gate 3 mở | #13 (L176) | Xếp là kiểm thử đơn vị | Khớp PV2; đóng |
| K7 | ACTION_STATUS_EVENT (9 trạng thái) hay Status_Event noncanonical | #13 (L177) | Để ngoài lõi | **Đảo lại:** STATUS_EVENT thuộc lõi (CL8, ĐG3); bước chuyển theo **Bảng A.2** |
| K8 | Action_Status thuộc Inspection Record hay thuộc ACTION | #13 (L178) | Chờ D014 | Đóng: `Action_Status` là thuộc tính **suy ra** của `ACTION` từ STATUS_EVENT mới nhất (CL8, Phụ lục A.2) |
| K9 | Nhánh quản trị 17/07 hay bộ v2.x | #13 (L179) | — | Không còn liên quan; nguồn khóa là GD3b + CLAUDE.md |
| K10 | Tên Paper 1: v8 hay v8.1 | #13 (L180) | — | Theo tệp 00: 1A = `Q1_PAPER1_v8_SHM_pre_SUBMISSION_13.09.2026.docx` |
| K11 | Revit Evidence Bridge: "insufficient" hay add-in 7 tool | #13 (L181) | — | Công cụ không phải đóng góp; chỉ mô tả ở Methods nếu cần |
| D003 | Đơn vị bằng chứng mặc định: RUN | #13, #15 (L213) | OPEN | Theo GD3b MT1(d): `scope.inference_unit`. Chốt cùng 1A-5 (tệp 00 §4) [NCS XÁC NHẬN] |
| D004 | Run là đơn vị nhóm; Assembly_ID chưa có | #13, #15 | BLOCKING_OPEN | Gắn với `scope.install_batch` (Phụ lục A.1). **Trường này chưa có ở giao diện G1→G2** (xem Đ11) |
| D005 | Định danh vật lý Sensor_ID trong phòng thí nghiệm | #13, #15, slide | BLOCKING_OPEN | [NCS XÁC NHẬN]; cần cho `SENSOR_MAPPING` và C3 |
| D007 | Quy tắc gộp xác suất cửa sổ → recording | #13, #15 | BLOCKING_OPEN | Thuộc pipeline 1A (đơn vị chấm điểm theo bản ghi, tệp 00 §3). Paper 2 chỉ nhận `value` |
| D010 | CEI: độ bất định có cấu trúc | #13, #15 | OPEN | Gắn `uncertainty` (seed, fold, p hoán vị; Phụ lục A.3). [NCS XÁC NHẬN] dạng vô hướng hay cấu trúc |
| D013 | Schema tối thiểu của Inspection_Record | #13, #15 | BLOCKING_OPEN | Đóng bằng Bảng A.1 (`INSPECTION_RECORD`) |
| D014, D015 | Action_Status / máy trạng thái hành động | #13 | BLOCKING_OPEN | Đóng bằng CL8 + Bảng A.2 (5 bước chuyển) |
| D016 | Duyệt bộ CQ | #13, slide | BLOCKING_OPEN | Như K2 |
| D1 (data model) | SHACL là cơ chế chính | #8 (L298) | "Đã chốt 23/09" | **Bị thay** bởi CL8 (Python + SQLite, không SHACL) |
| D2 | Neo kép Prototype_Component_ID + Binding_ID | #8 (L299) | Chốt 23/09; #15 ghi cần ADR | [NCS XÁC NHẬN]: giữ làm thuộc tính của `COMPONENT` hay bỏ |
| D3 | Máy 9 trạng thái | #8 (L300) | Chốt 23/09 | Thu về 4 trạng thái (CLAUDE.md QĐ 8) + Bảng A.2 |
| D4 | Namespace w3id | #8 (L301) | Chốt | Mất cơ sở khi bỏ RDF |
| D5 | Không sửa model gốc; RD-001…008 là ca lỗi thật | #8 (L302) | Chốt | Giữ (khớp quy tắc không sửa tệp gốc) |
| D001–D026 | Sổ `G1_G2_INTERFACE_DECISION_REGISTER.csv` | #13 (L150) | — | **MISSING**: sổ không có trong thư mục (PV2 nguồn 6) |
| Gate 1, 2, 3 | G1 OPEN-PARTIAL; G2 0/10; G3 chưa mở | #4, #15 | Treo | Bằng chứng 1A ở mức CANDIDATE (tệp 00 §2). Dùng được khi giao thức 1A đã khóa (GD3b D7) |

---

## 4. Điểm lệch so với nguồn hiệu lực cao hơn

Nguồn cao thắng mọi dòng dưới đây. Các mã **Đ1–Đ16** dùng để tham chiếu ở Pha 1 và Pha 4.

| Mã | Chiều | Thư mục 05 (các bản 14–27/09, prompt v1) | Nguồn cao (GD3b, CL8, Phụ lục A–B, PV2) | Mức |
|---|---|---|---|---|
| Đ1 | Số thực thể | 5 (#4); 7 (#7, #10, #15); 8 + 4 = 12 (#8); "10" mà liệt kê 11 (#11, #13); "6 nhóm" khác nghĩa (#14) | **6 thực thể** + quan hệ `EVIDENCE_USE`. PV2 gọi "10 thực thể v0.2" nhưng #8 thực có 12; bảng ánh xạ phải lập từ #8 | Cao |
| Đ2 | ACTION, STATUS_EVENT | Ngoài lõi ở #4, #13 (K7), #15, #16, #17, #18 | **Lõi**: G-B chính, ĐG3, C6 | **Cao, chặn ĐG3** |
| Đ3 | Công cụ | SHACL/RDF/SPARQL/w3id (#8 D1, D4; #11, #13, #14, slide); "nếu cần" (#4) | Python + IfcOpenShell + SQLite/JSON; ánh xạ SOSA/SSN, PROV-O chỉ trong 1 bảng | Cao |
| Đ4 | CQ | 5 (#4); 8 (#20); 12 (#8, #13) | 3 câu hỏi truy ngược | Trung bình (ánh xạ được) |
| Đ5 | Luật | R01–R15 (#8, 29 mã con); R16, R17 chỉ có ở #13 dạng [ĐỀ XUẤT]; PV2 ghi "R01–R17" | 5 ràng buộc C1, C3, C5, C6, C9. **C9 chưa có luật tương ứng trực tiếp** (Phụ lục B2 §8.1) | Trung bình |
| Đ6 | Chỉ số | M1 = phát hiện, M2 = đủ trường, M3 = thời gian (#8, #13); M0–M3 (#14); 4 chỉ số không số hiệu (#12); M1–M11 là sổ thiếu (#21) | M1 đủ thuộc tính (chỉ mô tả); **M2 lỗi chèn mù (chính)**; M3 truy ngược 3 câu; M4 phút/bản ghi. **Tên trùng nhưng nghĩa hoán đổi** | Cao |
| Đ7 | Đối chứng | Không có B0/B1. **BCF 3.0 không xuất hiện ở bất kỳ tệp nào.** Chỉ có "tra cứu thủ công" làm đối chứng thời gian | B0 (20–30 hồ sơ VN) + B1 ([35] tr. 4–7 + BCF 3.0) | **Cao** |
| Đ8 | Khoảng trống | GAP 1/2/3 với GAP 3 vẫn là khoảng trống (#4, #9, #2); GAP-A/B/C (#11, #13); Gap 2A–2C với 2B là trung tâm và bỏ hành động (#15, slide); GAP-A…H (#57) | G-B chính, G-A vế A2 phụ; GAP 3 trở thành thiết kế đánh giá | Cao |
| Đ9 | RQ | RQ2.1–2.3 theo ba đóng góp (#11, #13); SRQ2.1–2.3 (#15) | RQ2 bản F-1; RQ2.1 định danh (C1, C3), RQ2.2 phạm vi (C5, C9), RQ2.3 chuyển trạng thái (C6) | Cao (trùng nhãn, khác nội dung) |
| Đ10 | Đóng góp | C1–C3 (#4, #11, #13); một đóng góp P/V/I (#15) | ĐG1–ĐG3. ĐG1 (mở rộng IFC 4.3 + BCF 3.0) và ĐG3 (STATUS_EVENT) **không có đối ứng** trong thư mục; ĐG2 có đối ứng gần (Validity_Scope, EVIDENCE_USE, Scope_Snapshot) | Cao |
| Đ11 | Trường EVIDENCE (mối nối 1A → P2) | Giao diện #23: **thiếu `scope.install_batch`, `scope.applicable_conditions`**; không có kiểm "tại lần dùng"; không có phép thử "dùng ngoài phạm vi"; `uncertainty` buộc là cấu trúc (CEI) | Bảng A.1 bắt buộc 4 trường scope; C5 tính `within_scope` theo `install_batch` và `applicable_conditions` (Bảng B.1) | **Cao, chặn nhóm lỗi C5** |
| Đ12 | Lỗi chèn | 9, 10 hoặc 16 ca, do người viết luật tạo; 37 CE-NEG định nghĩa trước kèm kết quả kỳ vọng | ~30 lỗi chèn mù, người chèn ≠ người viết luật, 4 nhóm | Trung bình (nguyên tắc "người thứ hai lập ca" đã có ở #11, #13) |
| Đ13 | Bellon 2025 [35] | "Chỉ abstract / CAPTCHA / paywalled" (#43, #13, #14, #15) | **Đã đọc toàn văn 01/10** (`notes/NUTL57KJ`): IFC 4.3 ADD2, không mở rộng lược đồ, tr. 3–10, 17. Kết luận rủi ro ở thư mục **lỗi thời** | Đã giải ở nguồn cao |
| Đ14 | García 2026 [44] | Kiểm qua NotebookLM, không có trang (#42) | Đọc toàn văn 30/09 (`notes/GNTQNBWM`); CLAUDE.md §6.1 ghi là tiền lệ của C6 | Đã giải ở nguồn cao |
| Đ15 | MT3, hiện trường | `06_PAPER_3` v2.2: Paper 3 là "bonus"; thỏa thuận Rapexco "chưa xác nhận ký"; luận án "2×Q3" | GD3b, CLAUDE.md §2A: "đã có thỏa thuận với chủ đầu tư"; MT3 = chương luận án + phần minh họa của Bài 2; Bài 1 Q2/Q3, Bài 2 Q2 | Trung bình; **cần xác nhận văn bản thỏa thuận** |
| Đ16 | Lỗi trong nguồn cao (ghi lại, chưa sửa) | — | (a) CLAUDE.md §8, PV2 và prompt này gọi "**Bảng A.3**" là bảng bước chuyển dùng cho C6, nhưng `phuluc.md` hiện đánh số **Bảng A.2** = bước chuyển, A.3 = ánh xạ chuẩn. (b) PV2 mục "Đối tượng kiểm chứng" ghi "Bằng chứng MT1 lấy từ **B1**", đúng ra là **Bài 1A**; trùng ký hiệu với đối chứng B1. (c) PV2 ghi "mô hình 10 thực thể v0.2", nhưng #8 có 12 | Thấp; đề xuất sửa ở Pha 4 |

---

## 5. Phát hiện quan trọng (xếp theo mức chặn; nguồn đe dọa khoảng trống đứng đầu)

1. **[Đe dọa khoảng trống: chưa kiểm]** García et al. (2026b) "From IFC validation to publish/hold decisions" (Zotero `ZNSZE47J`).
   - Bài được nêu ở #15 (L356) và trên slide, ghi "có trong thư viện nhưng chưa đọc".
   - `notes/` không có ghi chú cho bài này.
   - Cùng nhóm tác giả với [44]. Chủ đề quyết định publish/hold có thể chạm khuôn C6.
   - **Cần đọc ở Pha 2**, trước khi viết phát biểu G-B.
2. **[Chặn ĐG3]** Chuỗi định hướng mới nhất (#15 → #18) đã đưa ACTION/STATUS_EVENT ra ngoài Paper 2.
   - Tài sản duy nhất còn dùng được cho C6 là `ACTION_STATUS_EVENT` trong #8:
     - các trường From/To, Actor_Role, Reason, Basis_Refs, Post_Action_Verification_Ref;
     - các luật R11a–d, R12, R13.
   - Cần dựng lại theo Bảng A.2.
3. **[Chặn Case study]** Mọi số liệu BIM chỉ có nguồn thứ cấp (#7):
   - 6 IFC, 3.356, 10.328;
   - 718 hay 676 (K4);
   - 8 cặp GUID.
   - Tệp gốc (registry, audit, `real_defect_cases`) không có trong thư mục. Riêng #4 tự gắn "CONFIRMED" cho 718 và 8 cặp.
4. **[Chặn nhóm lỗi C5, mối nối 1A → P2]** Giao diện G1→G2 (#23) chưa có `scope.install_batch`, `scope.applicable_conditions` và chưa có kiểm "tại lần dùng". Bài 1A hiện chưa sinh được bằng chứng đủ trường để chèn ca "dùng ngoài phạm vi". Điểm này gắn với việc 1A-5 ở tệp 00 §4.
5. **[Chặn tính công bằng của B1, R1]** Thư mục không có gì về B0, B1 và BCF 3.0. Ngoài ra có một điểm cần làm rõ trước khi đặc tả B1:
   - `notes/NUTL57KJ` (tr. 9): [35] tạo `IfcOwnerHistory` **mới** cho mỗi lần sửa tệp.
   - `mapping/bellon2025`: "theo IFC, chỉ giữ lần sửa cuối".
   - Hai câu nói về hai việc khác nhau: cách [35] làm và ngữ nghĩa của chuẩn. Nếu B1 dựng theo câu thứ hai thì B1 yếu hơn [35]. Xử lý ở Pha 1 (R1).

**Bất thường phụ** (chi tiết ở các phụ lục):
- Va chạm ký hiệu:
  - B1 là trạng thái bu lông, là đối chứng, và là tên bảng;
  - C1–C3 là đóng góp và là ràng buộc;
  - M1–M3 hai nghĩa; GAP-B ba nghĩa; RQ2.1–2.3 ba bộ;
  - D1 dễ nhầm D001.
- CORE01 là Jäkel et al. 2025, nhưng Zotero thiếu tác giả đầu.
- Hai bài khác nhau cùng là "Lee et al. 2021".
- Nuyts 2024: mức đọc mâu thuẫn giữa các tệp.
- Bản manuscript outline (#11) ghi đơn vị "ĐH Bách khoa – ĐH Đà Nẵng". [NCS XÁC NHẬN] đơn vị dùng cho bản thảo.
- Nghị định 207/2026/NĐ-CP (#15): [CẦN KIỂM].

---

## 6. Tài sản đáng giữ (đưa sang Pha 1) — tóm tắt

Danh sách đầy đủ có lý do ở mục 5 của từng phụ lục.

| Tài sản | Ở đâu | Phục vụ |
|---|---|---|
| SENSOR_PLACEMENT (Valid_From/To, không ghi đè); CONDITION_EVIDENCE (6 nhóm trường, Validity_Scope, Superseded_By); EVIDENCE_USE (Scope_Snapshot, Acknowledged_By, Cross_Component_Reason); ACTION_STATUS_EVENT | #8 A.2 | Ánh xạ sang 6 thực thể; C3, C5, C6, C9 |
| Bảng ánh xạ R01–R15 → C1/C3/C5/C6/C9; NT01–NT10 → 4 nhóm lỗi; CQ05–CQ07 làm ứng viên 3 câu truy ngược | Phụ lục B2 §8 [ĐỀ XUẤT] | PV2 Pha 0 |
| Nguyên tắc: người thứ hai lập ca lỗi sau khi luật khóa, niêm phong SHA-256, báo cả bỏ sót và dương tính giả; máy chỉ ghi tối đa candidate | #11, #13, #8 (L280) | Giao thức M2 |
| Sổ tương ứng 1:10 → 1:1 (Physical_Identity = FALSE), R16, R17 [ĐỀ XUẤT] | #13 (L359–L431) | Mối nối 1A → BIM nhà xưởng |
| RD-001…008: ca lỗi định danh thật (mức NGHI NGỜ) | #7, #8 | Tình huống mở bài; nhóm lỗi định danh |
| Bảng Claim–Evidence–Limitation; danh sách 15 bằng chứng còn thiếu; Phụ lục D (CDE tối thiểu) | #4 §21, #15 (L427–L443), #14 | Checklist Pha 1, Pha 4 |
| Bản đọc sâu có trang: CORE01–05, Borkowski toàn văn, Round 4, đọc sâu 01/09 | 01_EVIDENCE | Ma trận đối thủ ở Pha 2 |

**Nên bỏ hoặc hạ cấp:**
- RDF/SHACL/SPARQL/w3id cùng các quyết định D1, D4;
- 12 CQ và R01–R17 làm đơn vị khóa;
- mô hình 10–12 thực thể;
- các nhãn GAP 1/2/3, GAP-A/B/C, 2A–2C, C1–C3, M0–M3;
- số [SIM];
- số 16/16 dùng như kết quả;
- nhãn "CONFIRMED" cho 718 và 8 cặp;
- MCP/Bridge mô tả như một phần đóng góp.

---

## 7. Câu hỏi cần NCS hoặc thầy quyết

1. **Nơi lưu sản phẩm.** Giữ `05_PAPER_2_TRACEABILITY/P2A_audit_20261002/` hay tạo `03_PAPERS/PAPER_2/audit_20261002/` (chưa tồn tại)?
2. **K4 và tệp gốc.** NCS có registry 6 IFC, tệp audit 13/09 (676) và tệp audit trước 15/09 (718), `real_defect_cases_v0.1.csv` ở đâu ngoài thư mục này không? Nếu có, cấp quyền để đối chiếu ở Pha 1.
3. **Sổ `G1_G2_INTERFACE_DECISION_REGISTER.csv`** (D001–D026): còn không? Nếu không, ghi MISSING và đóng các D theo bảng 3.2.
4. **Thỏa thuận hiện trường (Rapexco).** Đã ký chưa? `06_PAPER_3` (04/08) ghi "chưa xác nhận ký"; GD3b ghi "đã có thỏa thuận".
5. **Pha 2 được phép đọc García 2026b (`ZNSZE47J`) toàn văn không?** Prompt cho phép tìm kiếm cho Paper 2, nhưng bài này chưa nằm trong `notes/`.

---

## 8. Tự kiểm (Pha 0)

- [x] Đã đọc hết 61 tệp văn bản trong phạm vi pha; PDF và Zotero thô ghi rõ là chưa đọc. Ảnh trong docx/pptx chưa xem.
- [x] Mọi số liệu có tệp nguồn. Số 16/16 ghi là kiểm thử đơn vị; 8 cặp GUID ghi là nghi ngờ.
- [x] Không thêm nguồn mới ở Pha 0, nên chưa có nhật ký tìm kiếm.
- [x] Không dùng "chưa ai nghiên cứu" hay "đầu tiên".
- [x] Không đổi phạm vi đã khóa. Các đề xuất đóng K/D chỉ là đề xuất. Các lỗi nguồn cao (Đ16) chỉ ghi lại, chưa sửa.
- [x] Không sửa, xóa hay di chuyển tệp gốc.
- [x] Dừng ở ĐIỂM DỪNG 0.

**Phụ lục chi tiết (cùng thư mục):**
- `P2A_0_phuluc_A_dinh_huong_1409_1609.md`
- `P2A_0_phuluc_B1_dinh_huong_lon_2409_2709.md`
- `P2A_0_phuluc_B2_outline_datamodel_2309_2509.md`
- `P2A_0_phuluc_C1_doc_sau_do_moi.md`
- `P2A_0_phuluc_C2_ghi_chu_tong_hop.md`
- `P2A_0_sha256_snapshot_20261002.txt`

Lưu ý khi đọc phụ lục: thứ tự hai pptx trong Phụ lục B1 bị đảo so với mtime; dùng mục 2.2 của bản này.
