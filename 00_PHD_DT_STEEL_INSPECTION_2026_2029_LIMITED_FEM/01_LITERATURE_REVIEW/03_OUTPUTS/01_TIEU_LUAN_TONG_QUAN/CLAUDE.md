# CLAUDE.md — Hoàn thiện Tiểu luận tổng quan (NCS Hồ Chí Hân)

> Tệp này là hướng dẫn làm việc cố định cho dự án. Đọc toàn bộ tệp này ở đầu MỖI phiên
> trước khi làm bất kỳ việc gì. Khi có quyết định mới được NCS duyệt, cập nhật mục
> "Quyết định đã khóa" và "Trạng thái tiến độ".

---

## 1. Tổng quan dự án

- **Văn bản:** Báo cáo chuyên đề Tiểu luận tổng quan — "Tổng quan về hệ thống song sinh
  kỹ thuật số dựa trên dữ liệu trong giám sát trạng thái và hỗ trợ kiểm tra – bảo trì
  công trình công nghiệp khung thép". Ngành Quản lý xây dựng.
- **Bản gốc:** `HO_CHI_HAN_TIEU_LUAN_TONG_QUAN_23092026_HOANTHIEN.docx` (84 tài liệu tham khảo).
- **Mục tiêu luận án:** ba mục tiêu đã khóa ở mục 2A (MT1 phòng thí nghiệm → Bài 1; MT2 mô hình thông tin → Bài 2;
  MT3 nhà xưởng thật có BIM và cảm biến → chương luận án, bổ sung cho Bài 2).
- **Định hướng hoàn thành (NCS quyết định 01/10/2026):** tốt nghiệp sớm với **2 bài Q2/Q3**. Phạm vi rút gọn; mọi việc
  không phục vụ trực tiếp một trong hai bài thì hoãn hoặc đưa vào "hướng phát triển".
- **Luận điểm trung tâm:** Với nhà xưởng thép, dữ liệu quan trắc không thể là kết luận hư hỏng,
  nhưng có thể trở thành căn cứ kiểm tra đáng tin và giải trình được nếu mỗi bằng chứng mang
  theo nguồn gốc, phạm vi hiệu lực và lịch sử xử lý đến tận hành động.
- **Công cụ MCP:** Zotero (thư viện tài liệu — nguồn sự thật duy nhất cho trích dẫn),
  Consensus (tìm kiếm tài liệu — chỉ là gợi ý, phải xác minh).

---

## 2. Quyết định đã khóa (không tự ý thay đổi)

1. **Hướng sửa: đi xuôi từ bài toán thực tế** → đối tượng → hạn chế hiện tại → khoảng trống.
2. **Kết quả Paper 1 KHÔNG được đưa vào tiểu luận** (không số liệu, không bảng, không hình,
   không "kết quả sơ bộ"). Kết quả Paper 1 là cơ sở của Chuyên đề 1 tiếp theo.
   Tiểu luận chỉ được mô tả *thiết kế và công cụ* của thực nghiệm, không mô tả *kết quả*.
3. **Mục Công cụ AI (5.6) làm trước**, chạy song song với Giai đoạn 0–2.
4. **Công cụ AI ở WP1 theo đúng Paper 1:** Random Forest, SVM-RBF, 1D-CNN, ResNet1D;
   đánh giá theo nhóm ở hai mức (giữ lại cả lần chạy – LORO; giữ lại cả đợt – LOCO; NCS duyệt 01/10/2026), chấm điểm theo bản ghi, kiểm định hoán vị,
   báo cáo biến thiên theo seed và theo fold.
5. **Công cụ AI ở hiện trường (WP3): Autoencoder** phát hiện bất thường so với đường cơ sở
   vận hành, kèm bù EOV ở mức tối thiểu: hồi quy theo nhiệt độ và cờ cầu trục chạy/dừng. Kết quả kiểm tra của kỹ sư
   được ghi làm nhãn hiện trường; **không** làm học chủ động (rút gọn 01/10/2026).
6. **Nguyên tắc AI:** "AI tạo bằng chứng, con người quyết định". Mọi đầu ra AI trở thành
   một bản ghi `EVIDENCE` có `method_version`, `uncertainty`, `VALIDITY_SCOPE`.
7. **Schema dạng đồ thị**, không phải chuỗi tuyến tính; bản rút gọn 6 thực thể, 5 ràng buộc (xem mục 8).
8. **Tách hai trục:** `priority_level` (Bình thường → Theo dõi → Kiểm tra → Kiểm tra ưu tiên)
   và `Action_Status` (mở → đang xử lý → hoàn thành → đã xác minh).
9. **Khoảng trống: chốt hai khoảng trống** (NCS quyết định 01/10/2026, sau khi đã đọc sâu 29/30 tài liệu key):
   - **G-A — Bằng chứng trạng thái có phạm vi hiệu lực** (gộp K1; UV-02, UV-06; UV-08 làm yêu cầu nội dung): kết quả từ
     dữ liệu dao động chưa được ghi thành bằng chứng mang nguồn gốc, phương pháp và phạm vi hiệu lực (đơn vị đánh giá,
     lần lắp ráp – can thiệp, điều kiện vận hành) để kiểm được khi nào còn dùng được.
   - **G-B — Từ bằng chứng đến hành động có trách nhiệm** (gộp K3; UV-01, UV-05, UV-07): chuỗi kiểm tra – cấu kiện –
     hành động đã có chuẩn biểu diễn ([35], IFC4, BCF 3.0), nhưng bằng chứng có phạm vi hiệu lực chưa đi vào chuỗi đó và
     mỗi lần đổi trạng thái chưa được ghi thành sự kiện có căn cứ, thẩm quyền, xác minh sau sửa chữa.
   - K2 (UV-03) hạ thành **yêu cầu của schema** (ràng buộc C3), không là khoảng trống riêng. UV-04 chỉ dùng định vị (2.3).
   - ĐD3 chỉ còn: NCS duyệt câu chữ hai khoảng trống và gửi thầy. Các mục phản chứng còn mở (N-20 – N-25) ghi
     "đối chiếu ở mức tóm tắt / qua nguồn thứ cấp", không tìm thêm.
10. **Ba mục tiêu luận án đã khóa** (mục 2A). Không thêm mục tiêu, WP hay bài báo mới.
11. **Không mở rộng tổng quan:** không đọc thêm, không tìm thêm phản chứng hay tiền lệ, trừ khi thầy hướng dẫn hoặc phản
    biện tạp chí yêu cầu bằng văn bản.
12. **Đối chứng B1 và phỏng vấn (NCS duyệt F-1, F-2 của `revision/GD3b_khoang_trong_va_muc_tieu.md`, 01/10/2026):**
    MT2 so với cả B0 và B1 (định nghĩa ở mục 8); M2 là chỉ số chính. Phỏng vấn có cấu trúc 3–5 người quản lý kiểm tra – bảo
    trì phía chủ đầu tư (khoảng 30 phút/người, có đồng thuận), gộp vào đợt khảo sát nhà xưởng, trước khi khóa bộ câu hỏi truy
    ngược; chỉ để xác nhận bộ câu hỏi và nêu nhu cầu cho G-B, không thay M1–M4. Cần thầy hướng dẫn duyệt hoạt động phỏng vấn.
13. **G-A gồm hai vế** (NCS duyệt 01/10/2026): **A1 – đánh giá** (mức chênh lệch giữa đánh giá cùng lần chạy và hai mức đánh giá theo đơn vị
    độc lập, giữ lại lần chạy (LORO) và giữ lại đợt (LOCO) theo mục 3.3.3 ([18], [19], [56]), chưa được báo cáo cho phân loại dựa trên dao động của liên kết bu lông trong khung thép; [19], [15] là tiền lệ gần
    nhất, bắt buộc nêu trong Bài 1) và **A2 – khai báo** (phạm vi hiệu lực, độ bất định là trường bắt buộc của từng bằng chứng,
    kiểm tại lần sử dụng).

---

## 2A. Ba mục tiêu luận án (KHÓA 01/10/2026 — yêu cầu tối thiểu của trường)

| | Mục tiêu | Có sẵn | Sản phẩm | Khoảng trống | Kết quả đo (đủ để kết luận) |
|---|---|---|---|---|---|
| **MT1** | Xác lập quy trình tạo **bằng chứng trạng thái liên kết bu lông có phạm vi hiệu lực** từ dữ liệu dao động trên khung thép thu nhỏ 1:10 trong phòng thí nghiệm, với bốn mô hình (RF, SVM-RBF, 1D-CNN, ResNet1D) dưới đánh giá theo nhóm ở hai mức (giữ lại lần chạy, giữ lại đợt), kiểm định hoán vị, báo cáo biến thiên theo seed và fold | Dữ liệu ba đợt thí nghiệm, kết quả Paper 1 (Gate 1) | **Bài 1** (Q2/Q3, SHM – đo lường) | G-A | Hiệu năng ở hai mức đơn vị độc lập (lần chạy, đợt), chênh lệch của mỗi mức so với đánh giá cùng lần chạy, khai báo phạm vi hiệu lực của kết quả |
| **MT2** | Xây dựng **mô hình thông tin truy vết bằng chứng → hành động** cho kiểm tra – bảo trì kết cấu thép, mở rộng IFC 4.3 ([35]) và BCF 3.0 bằng tầng bằng chứng và tầng trách nhiệm (6 thực thể, 5 ràng buộc kiểm tự động, logic hỗ trợ hành động bốn mức bằng luật) | Schema đồ thị, C1–C9, mapping với [2], [35], [44] | **Bài 2** (Q2, tin học xây dựng) | G-B (+G-A) | M2 (chính, theo nhóm lỗi) và M1, M3, M4 ở mục 8, so với B0 (hồ sơ kiểm định hiện hành) và B1 (IFC 4.3 theo [35] + BCF 3.0, chưa có hai tầng mới), trên cùng BIM nhà xưởng thật và dữ liệu MT1 |
| **MT3** | **Triển khai và kiểm chứng khả thi** trên một nhà xưởng khung thép thật có BIM: lắp hệ cảm biến, lập đường cơ sở vận hành, sinh bằng chứng cảm biến bằng Autoencoder (bù nhiệt độ, cờ cầu trục), chạy kịch bản kiểm tra – xử lý – truy ngược đầu cuối (kịch bản cột C3) | Công trình có BIM; NCS bảo đảm lắp cảm biến | Chương luận án; phần hiện trường của Bài 2 nếu kịp, hoặc bài hội nghị (không bắt buộc) | G-A, G-B (áp dụng) | Dữ liệu về đủ, ánh xạ cảm biến – cấu kiện đúng, kịch bản C3 truy ngược được, chi phí ghi nhận |

Quy tắc phạm vi:
- **Ba công trình (NCS quyết định 02/10/2026):** khung 1:10 trong PTN (MT1) mô phỏng một nhà xưởng ở Khánh Hòa; BIM của
  nhà xưởng Khánh Hòa là nền đánh giá MT2, và **hồ sơ B0 lấy của chính nhà xưởng này** (cùng BIM với B1 và mô hình đề xuất);
  nhà xưởng MT3 ở Đắk Lắk (địa bàn Phú Yên cũ).
- **Bài 1 (NCS quyết định 02/10/2026):** chạy đủ bốn mô hình (RF, SVM-RBF, 1D-CNN, ResNet1D) và giữ lại đợt (LOCO) trên cả
  ba đợt, kèm mốc cùng lần chạy; tiểu luận mô tả đúng thiết kế này.
- **Phần quy cho đóng góp của MT2** là chênh lệch mô hình đề xuất so với **B1**; chênh lệch so với **B0** là đóng góp bối cảnh –
  thực tiễn cho thực hành kiểm định ở Việt Nam, không khái quát sang nơi khác.
- **Song song với MT1:** khảo sát nhà xưởng, chọn vị trí cảm biến, lấy hồ sơ B0, phỏng vấn (QĐ 12).
- **Bài 2 không chờ quan trắc dài hạn:** kiểm chứng bằng BIM nhà xưởng thật + hồ sơ kiểm định cũ (B0) + B1 + dữ liệu MT1
  (bằng chứng có phạm vi đã biết, dùng để chèn ca dùng ngoài phạm vi). Dữ liệu hiện trường MT3 có sớm thì thêm một mục minh họa.
- **MT3 chỉ tuyên bố khả thi và truy vết**, không tuyên bố hiệu năng phát hiện hư hỏng ở hiện trường. Quan trắc 3–6 tháng,
  khoảng 6–10 cảm biến ở các liên kết đại diện, 1–2 đợt kiểm tra thật.
- Mức tích hợp khai báo theo Kritzinger [8]: bóng số (DS); tên đề tài giữ "song sinh số dựa trên dữ liệu" kèm khai báo này ở Chương 1.
- RQ của tiểu luận được viết lại 1:1 theo MT1–MT3 ở GĐ5 (RQ1 ↔ MT1, RQ2 ↔ MT2, RQ3 ↔ MT3).

---

## 3. Góp ý của thầy hướng dẫn → nơi xử lý

| # | Góp ý | Xử lý tại |
|---|---|---|
| G1 | Thiếu lý do chọn nhà công nghiệp khung thép liên kết bu lông | Mục 1.2 mới |
| G2 | Thiếu hạn chế của phương pháp quan trắc hiện tại với công trình công nghiệp | Mục 3.2 mới |
| G3 | Thiếu kết nối dữ liệu thực nghiệm – thực tế | Mục 3.6 mới (KHÔNG dùng kết quả Paper 1) |
| G4 | Chưa rõ "bằng chứng trạng thái" | Mục 1.3 mới: định nghĩa + ví dụ + bảng đối chiếu |
| G5 | Chuỗi phức tạp, khó hiểu | Dẫn nhập bằng kịch bản; 1.4 ba câu hỏi; chi tiết ID → Phụ lục A |
| G6 | Bổ sung công cụ AI dùng cho toàn bộ luận án | Mục 5.6 mới |
| G7 | Cần 20–30 tài liệu key, đọc sâu từng tài liệu trước khi chỉ ra khoảng trống | Giai đoạn 1–3 |

Cuối cùng phải xuất **bản giải trình tiếp thu góp ý**: góp ý → sửa ở đâu → sửa như thế nào.

---

## 4. Quy tắc bắt buộc

### 4.1 Trích dẫn
- **Không bao giờ bịa trích dẫn, tác giả, năm, tạp chí hay DOI.**
- Mọi trích dẫn đưa vào văn bản phải có trong Zotero, có DOI (hoặc định danh chuẩn) đã xác minh.
- Kết quả từ Consensus: kiểm tra bản gốc (tiêu đề, tác giả, năm, DOI) → nhập Zotero → mới được dùng.
- Không trích nội dung mà chưa đọc đoạn tương ứng trong bản gốc. Nếu chỉ đọc tóm tắt, ghi rõ trong ghi chú.
- Tài liệu 2025–2026: kiểm tra trạng thái xuất bản chính thức; không để một khoảng trống
  dựa chủ yếu vào các bài này.
- Không dùng [23] (UCLA Factor Building — nhà văn phòng) làm căn cứ cho luận điểm về nhà công nghiệp.
- Khi không tìm được nguồn đủ tin cậy: ghi `[CẦN NGUỒN]` và báo NCS, không lấp bằng nhận định chung.
- Mỗi khoảng trống ở GĐ3 cần ít nhất ba căn cứ không thuộc nhóm tài liệu 2025–2026.
- PDF lưu dạng tệp liên kết (linked file) trong thư mục `pdf/` của dự án (tên tệp bắt đầu bằng khóa Zotero); `pdf/` và `*.pdf` có trong `.gitignore`.

### 4.2 Văn phong
- Tiếng Việt học thuật, trang trọng; thuật ngữ tiếng Anh để trong ngoặc ở lần đầu.
- Tách rõ **bằng chứng** (tài liệu nói gì) và **diễn giải** (tác giả suy ra gì).
- Mỗi đóng góp có một câu khẳng định tích cực; các giới hạn gom về mục giới hạn (Mục 5.9 sau khi đánh số lại 02/10/2026).
  Không rải câu "không chứng minh…" trong thân bài.
- Không dùng văn phong quảng bá, không phóng đại, không liệt kê kiểu gạch đầu dòng trong thân văn
  khi có thể viết thành đoạn.
- Dùng thuật ngữ đúng theo Bảng thuật ngữ (mục 10), nhất quán toàn bài.

### 4.3 Cách làm việc
- **Mỗi phiên chỉ một nhiệm vụ** (một mục hoặc một nhóm tài liệu).
- Làm trên bản Markdown trong `tieuluan/`, nhánh Git `revision-v2`. Không sửa tệp .docx gốc.
- Kết thúc phiên luôn có: (1) tóm tắt đã làm, (2) diff hoặc bản trước/sau,
  (3) danh sách trích dẫn mới dùng, (4) việc còn mở. Sau đó **dừng lại chờ NCS duyệt**.
- Không tự chuyển sang giai đoạn tiếp theo khi chưa qua điểm duyệt.
- Cập nhật `revision/changelog.md` và bảng Trạng thái tiến độ (mục 12) sau mỗi phiên được duyệt.
- **Git:** chỉ `git add` đúng đường dẫn tệp của phiên; không dùng `git add -A`, `git add .` hay `commit -a`.
  Trước mỗi commit chạy `git status` và `git diff --cached --stat`; nếu vùng stage có tệp ngoài phiên thì dừng và
  báo NCS (quy tắc thêm 01/10/2026 sau sự cố commit cuốn theo tệp đã xóa; xem `revision/git_tep_bi_xoa.md`).

### 4.4 Quy ước trích dẫn
- Trích dẫn hiện có giữ dạng số cũ `\[n\]` (n = `so_cu` trong `matrix/doi_chieu_danh_muc.csv`)
  cho đến hết Giai đoạn 5.
- Tài liệu MỚI bổ sung: trích dạng `\[@KHÓA_ZOTERO\]` (ví dụ `\[@RWHW6F9I\]`). KHÔNG tự gán số mới.
- Mỗi tài liệu mới phải được thêm một dòng vào `doi_chieu_danh_muc.csv` với `so_cu = "moi"`.
- Giai đoạn 6: viết script đánh số lại toàn bộ theo thứ tự xuất hiện lần đầu (chuẩn IEEE), dựa trên
  `doi_chieu_danh_muc.csv`, và tạo lại danh mục từ Zotero.
- Không bao giờ sửa tay số trích dẫn ở giữa các giai đoạn.

### 4.5 Viết về giới hạn
Góp ý của thầy hướng dẫn: mật độ câu giới hạn quá dày, nghe nặng nề. Phân loại mọi câu dạng
"không chứng minh / không phải / không thay thế / không đồng nghĩa / không đủ":
- **Loại A – phân định khái niệm cần thiết:** giữ ý, viết lại theo hướng khẳng định.
  Mỗi chương tối đa 3–4 câu.
- **Loại B – tự hạ đóng góp** ("không phải đóng góp mới", "không phải kỹ thuật mới"): chuyển thành
  câu kế thừa có dẫn nguồn ("nghiên cứu kế thừa … từ [n]").
- **Loại C – giới hạn kết luận:** xóa khỏi thân bài, thay bằng câu trỏ "Phạm vi diễn giải … được
  trình bày ở Mục 5.9", và gom nội dung về mục giới hạn.
- **Giọng văn:** dùng "được xác lập trong phạm vi", "hướng mở rộng", "được thực hiện qua kiểm tra
  của kỹ sư"; tránh chuỗi phủ định liên tiếp.
- Đây là việc của Giai đoạn 5. Danh sách câu và loại đề xuất nằm ở
  `revision/danh_sach_cau_gioi_han.csv`; chỉ sửa câu sau khi NCS duyệt danh sách.

---

## 5. Cấu trúc thư mục

```
tieuluan/          # bản Markdown theo chương: 00_bia.md, 00_thuatngu.md, 00_dannhap.md, 01_chuong1.md ... 05_chuong5.md, 99_tailieu.md, phuluc.md
matrix/            # literature_matrix.xlsx (hoặc .csv) — ma trận tài liệu key
notes/             # <citekey>.md — ghi chú đọc sâu từng tài liệu (đồng bộ với ghi chú Zotero)
mapping/           # bảng ánh xạ thực thể với tiền lệ: theiler2018.md, bellon2025.md, garcia2026.md
revision/          # changelog.md, giai_trinh_gop_y.md
figures/           # sơ đồ (Mermaid/SVG) cho schema, kịch bản, kiến trúc
```

---

## 6. Kế hoạch 7 giai đoạn và điểm duyệt

| GĐ | Nội dung | Sản phẩm | Điểm duyệt |
|---|---|---|---|
| 0 | Chuyển Markdown; tạo collection Zotero `TL-Key` (Tier1/Tier2/Bổ sung), tag `K1 K2 K3 Đối tượng Chuẩn`; đối chiếu 84 tài liệu với Zotero; kiểm tra trạng thái tài liệu 2025–2026 | Bảng đối chiếu danh mục – Zotero | ĐD0: xác nhận danh sách key |
| 1 | Tìm bổ sung qua Consensus (mục 7.3), xác minh, nhập Zotero | Danh sách bổ sung + lý do chọn | ĐD1: chốt ~30 tài liệu key |
| 2 | Đọc sâu: Tier1 2–3 tài liệu/phiên (toàn văn); Tier2 5 tài liệu/phiên (tóm tắt, phương pháp, giới hạn); ánh xạ thực thể với [2], [35], [44] | Ma trận ~30 dòng; 3 bảng ánh xạ | ĐD2: NCS kiểm cột "Giới hạn" |
| 3 | Gom 5 cụm chủ đề; rút khoảng trống từ cột Giới hạn; mỗi khoảng trống ≥ 3 tài liệu căn cứ | Bảng Khoảng trống → Căn cứ → Vì sao quan trọng | **ĐD3: chốt khoảng trống, gửi thầy** |
| 4 | Viết mục mới theo thứ tự ở mục 6.1 | Từng mục | ĐD4: duyệt từng mục |
| 5 | Tái cấu trúc, cắt gọn (mục 6.2) | Bản toàn văn v2 | ĐD5 |
| 6 | Kiểm tra nhất quán, khai báo AI tạo sinh, xuất Word theo mẫu trường, bản giải trình | Tiểu luận v2 + giải trình | ĐD6 |

### 6.0 Phạm vi rút gọn cho tiểu luận (NCS duyệt 01/10/2026)
- **GĐ2 đóng** với 29/30 tài liệu; [80] bỏ. Không mở thêm phiên đọc.
- **GĐ3 rút gọn:** viết bảng hai khoảng trống G-A, G-B → căn cứ → vì sao quan trọng (≤ 2 trang), NCS duyệt, gửi thầy.
- **GĐ4 chỉ viết các mục cần cho ba mục tiêu**, mỗi mục ≤ 1.500 từ: 1.2 Đối tượng; 3.2 Hạn chế quan trắc nhà công nghiệp
  (gộp nội dung 3.6 cầu nối PTN – hiện trường thành một tiểu mục); 5.2 Khoảng trống; 5.5 Mô hình dữ liệu (bản rút gọn);
  5.7 Kiểm chứng (1 trang, 4 chỉ số); Dẫn nhập ngắn. 1.3A, 1.4A, 5.6A đã có, chỉ sửa theo rút gọn.
- **Mỗi phiên làm trọn một mục**; không tách nhỏ thêm.

### 6.1 Thứ tự viết mục mới (Giai đoạn 4)

| # | Mục | Phụ thuộc |
|---|---|---|
| 4.1 | **5.6 Công cụ AI và vai trò trong chuỗi bằng chứng** — LÀM TRƯỚC | Không |
| 4.2 | 1.2 Đối tượng: nhà công nghiệp khung thép liên kết bu lông | GĐ1 |
| 4.3 | 1.3 Khái niệm bằng chứng trạng thái; 1.4 Ba câu hỏi của người quản lý | Không |
| 4.4 | 3.2 Hạn chế của quan trắc hiện tại với công trình công nghiệp | GĐ1–2 |
| 4.5 | 3.6 Cầu nối phòng thí nghiệm – hiện trường | GĐ2 |
| 4.6 | 5.2 Khoảng trống (viết lại) | ĐD3 |
| 4.7 | 5.5 Mô hình dữ liệu dạng đồ thị | GĐ2 |
| 4.8 | 5.7 Thiết kế kiểm chứng và chỉ số | 4.7 |
| 4.9 | Dẫn nhập mở bằng kịch bản | Sau cùng |

Ghi chú (NCS duyệt 29/09/2026):
- Khi viết 3.6, chuyển đoạn "bốn nhóm bằng chứng" (5.6A.3, đoạn 1) sang 3.6 và rút gọn phần ở 5.6A còn 1–2 câu trỏ về. **Đã làm 01/10/2026:** đoạn chuyển sang mục nhãn tạm 3.6A (trước 3.5); 5.6A.3 còn một câu trỏ về. **02/10/2026:** 3.6A gộp vào 3.2A thành tiểu mục 3.2A.4; 5.6A.3 trỏ về 3.2A.4.
- Mục 5.5, 5.7 và Phụ lục B phải định nghĩa đủ các thuật ngữ mà 5.6A đã dùng (bản ghi bằng chứng, trường giá trị, trường độ bất định, trường phạm vi hiệu lực, trường điều kiện áp dụng, bối cảnh quan trắc, bản ghi kiểm tra, bản ghi sử dụng bằng chứng, sự kiện chuyển trạng thái, đường cơ sở B0, ràng buộc về sử dụng bằng chứng ngoài phạm vi hiệu lực).

Tiền lệ bắt buộc nêu (kết quả kiểm phản chứng GĐ2, 30/09/2026; chi tiết ở `revision/GD2_nhat_ky_khoang_trong.md`):
- **BCF 3.0** là tiền lệ bắt buộc nêu ở 2.2 và 5.5 (trạng thái vấn đề, sự kiện chuyển trạng thái); phần mới của luận án là quan hệ giữa sự kiện chuyển trạng thái với bản ghi sử dụng bằng chứng.
- **IFC4** (`IfcActionRequest`, `IfcProjectOrder` loại lệnh bảo trì, `IfcTask`, `IfcApproval`, `IfcPerformanceHistory`) là tiền lệ bắt buộc nêu ở 2.2 và 5.5 cho hành động có trạng thái, phê duyệt và dữ liệu đo theo thời gian; phần mới là lịch sử chuyển trạng thái và quan hệ định kiểu từ hành động về bằng chứng tình trạng.
- **SSN `Deployment`** (cảm biến triển khai trên nền tảng) là tiền lệ bắt buộc nêu ở 4.x và 5.5 cho ánh xạ cảm biến – cấu kiện; cùng [2] IFC Monitor. Phần mới là khoảng hiệu lực bắt buộc và ràng buộc thời điểm quan trắc nằm trong khoảng đó (C3).
- **[44] García 2026** là tiền lệ của khuôn "bước chuyển có bằng chứng và đúng thẩm quyền" (C6), áp cho gói thông tin bàn giao; nêu ở 4.5 và 5.5. Phần mới là áp khuôn đó cho hành động kiểm tra – bảo trì dựa trên bằng chứng tình trạng.
- **[35] Bellon 2025** là tiền lệ của chuỗi định kiểu lần kiểm tra → hư hỏng → cấu kiện → nhiệm vụ bảo trì → chi phí bằng thực thể chuẩn IFC 4.3 (`IfcRelAssignsToProduct`, `IfcRelAdheresToElement`, `IfcRelAssignsToProcess`), cho phát hiện bằng mắt; nêu ở 2.2 và 5.5. Phần mới là bằng chứng có nguồn gốc và phạm vi hiệu lực (gồm cảm biến, NDT) đi vào chuỗi đó và sự kiện chuyển trạng thái của hành động có căn cứ (kết quả T1-1, 01/10/2026).
- Đề xuất bổ sung schema từ `mapping/garcia2026.md` Phần D (tách nhiệm vụ, phiên bản bộ luật quyết định, mã băm) chờ NCS quyết định khi viết 5.5. Hai điểm của `mapping/bellon2025.md` Phần D (bản số EVIDENCE–COMPONENT khi xuất IFC, bản ghi mới thay bản ghi cũ) đã được NCS quyết định ngày 01/10/2026, ghi ở mục 8 "Quyết định thiết kế cho 5.5".
- **Khi viết 5.5:** trình bày schema như phần mở rộng của mô hình IFC 4.3 của [35] và của BCF 3.0, không như một mô hình mới độc lập.
- **[82] Seiß 2025** (NCS duyệt 01/10/2026; điều chỉnh theo rút gọn): nêu ở 3.5 như ontology liên quan cho lần kiểm tra – cấu kiện – quy chuẩn; luận án không xuất RDF nên không căn chỉnh; **không** dùng làm tiền lệ cho G-B (không có hành động, phê duyệt, sự kiện chuyển trạng thái; phạm vi thi công).
- **[21] Hagedorn 2023** (NCS duyệt 01/10/2026; điều chỉnh theo rút gọn): tiền lệ khái niệm cho kiểm ràng buộc tự động — C1 (R1) và C3/C9 (R2, ràng buộc thời gian, tr. 17–18); luận án kiểm bằng script Python thay cho SHACL.

### 6.2 Việc tái cấu trúc (Giai đoạn 5)
- Chuyển RQ và kiến trúc nghiên cứu từ Chương 1 sang Chương 5; xóa phần lặp.
- Gom các câu giới hạn về mục giới hạn (Mục 5.9), cắt khoảng một nửa. **Đã làm 02/10/2026** (danh sách v2).
- Chuỗi định danh chi tiết + thang V1–V4 → Phụ lục A; 5 ràng buộc (mục 8) → Phụ lục B;
  ma trận RQ–WP–Paper–Gate: **bỏ Phụ lục C** (NCS quyết định 02/10/2026; Bảng 5.2 ở Chương 5 đã làm phần này).
- 4.5.4: tách `priority_level` và `Action_Status`.
- Bổ sung ISO 55000 (2.1) và BCF (2.2).
- Rà các tài liệu ngoài danh sách key, đặc biệt 6 tài liệu về cầu ([63]–[66], [77], [78]):
  giữ nếu còn làm căn cứ, loại nếu không.
- Khai báo sử dụng AI tạo sinh ở phần đầu.
- Rút gọn 5.6A theo mục 9 (bỏ học chủ động, LLM, MLflow/DVC; WP2 mã hóa tay hồ sơ cũ làm B0); viết lại RQ theo MT1–MT3;
  thay K1–K3 bằng G-A, G-B trong toàn văn.
- Sửa câu ở `05_chuong5.md` gọi đối tượng của [82] là "hồ sơ kiểm tra": thực chất là lần kiểm tra theo kế hoạch trong thi công (NCS duyệt 01/10/2026; xem `notes/JTF8EM7Y.md`).

### 6.3 Cấu trúc đích của tiểu luận v2
- Phần đầu: Khai báo AI tạo sinh; Dẫn nhập (kịch bản).
- Ch.1: 1.1 Bối cảnh; 1.2 Đối tượng [MỚI]; 1.3 Bằng chứng trạng thái [MỚI]; 1.4 Ba câu hỏi [MỚI];
  1.5 Vấn đề; 1.6 Mục tiêu – phạm vi; 1.7 Phương pháp tổng quan; 1.8 Cấu trúc.
- Ch.2: Quản lý tài sản (+ISO 55000); BIM/IFC (+BCF); Song sinh số; Tổng hợp.
- Ch.3: 3.1 Dao động; 3.2 Hạn chế với công trình công nghiệp [MỚI]; 3.3 Cảm biến – xử lý – học máy;
  3.4 Độ tin cậy; 3.5 Nguồn gốc – phạm vi hiệu lực; 3.6 Cầu nối PTN – hiện trường [MỚI]; 3.7 Tổng hợp.
- Ch.4: giữ; sửa 4.5.4.
- Ch.5: 5.1 Tổng hợp; 5.2 Khoảng trống; 5.3 Luận đề; 5.4 RQ; 5.5 Schema đồ thị; 5.6 Công cụ AI [MỚI];
  5.7 Kiểm chứng – chỉ số [MỚI]; 5.8 Đóng góp; Phạm vi – giới hạn = mục giới hạn (nhãn tạm 5.8, đánh số lại ở GĐ5); 5.10 Lộ trình; 5.11 Tổng hợp.
- Phụ lục A, B (Phụ lục C bỏ, 02/10/2026).
- **Đã đánh số lại 02/10/2026** (cấu trúc thực tế, khác 6.3 ở chỗ giữ một số mục cũ):
  Ch.1: 1.1 Bối cảnh; 1.2 Đối tượng (cũ 1.2A); 1.3 Bằng chứng trạng thái (cũ 1.3A); 1.4 Ba câu hỏi (cũ 1.4A); 1.5 Vấn đề (cũ 1.2);
  1.6 Sự cần thiết (cũ 1.3); 1.7 Mục tiêu và phạm vi TLTQ (gộp cũ 1.4, 1.5); 1.8 Phương pháp (cũ 1.6); 1.9 Mục tiêu, RQ và kiến
  trúc luận án (gộp cũ 1.7, 1.8); 1.10 Cấu trúc (cũ 1.9). Ch.2: 2.2.3 Chuẩn biểu diễn vấn đề – hành động (cũ 2.2.2A), 2.2.4 (cũ
  2.2.3). Ch.3: 3.2 Hạn chế quan trắc (cũ 3.2A, gồm 3.2.4 cầu nối PTN – hiện trường), 3.3–3.6 (cũ 3.2–3.5). Ch.5: 5.7 Công cụ AI
  (cũ 5.6A), 5.8 Đóng góp, 5.9 Phạm vi – giới hạn, 5.10 Định hướng, 5.11 Tổng hợp. Schema ở 5.6.2; kiểm chứng và chỉ số ở 5.5.2.
  Bảng 1.1 (cũ 1.1A), Bảng 5.4 (cũ 5.6A), Bảng 5.5 (cũ 5.4). Các nhãn cũ ở mục 6.1, 9, 12 là ghi chép lịch sử.

### 6.4 Lưu ý cho Giai đoạn 6
- Trước khi chèn bản khai báo AI tạo sinh, rà cột `muc_da_doc` của mọi bảng luận điểm – nguồn; tài liệu chỉ đọc tóm tắt phải được đọc thêm, hoặc chỉ dùng cho nhận định ở mức tóm tắt, để câu "mọi trích dẫn đều được đối chiếu với bản gốc" là đúng.

---

## 7. Tài liệu key

### 7.1 Tier 1 — đọc sâu toàn văn (12 tài liệu; chốt ĐD1 ngày 30/09/2026)
[8] Kritzinger 2018 · [7] Boje 2020 · [3] Lu, Xie, Parlikad & Schooling 2020 · [22] Hemker 2019 ·
[18] Brake 2019 · [19] Ramasso · [53] Kapoor & Narayanan 2023 · [2] Theiler & Smarsly 2018 ·
[35] Bellon 2025 · [44] García 2026 · [16] Çelik 2023 · [17] Wu 2026

### 7.2 Tier 2 — đọc có trọng tâm (18 tài liệu; chốt ĐD1 ngày 30/09/2026)
Số cũ: [10] Chen 2021 · [29] Johannes 2021 · [45] Sohn 2007 · [57] Bull 2021 · [56] Da Silva 2024 ·
[48] Pal 2022 · [14] Beleites 2013 · [15] Wheat 2024 · [42] Ramonell 2023 · [21] Hagedorn 2023 ·
[82] Seiß 2025 · [28] Kamariotis, Chatzi & Straub 2023 · [80] Bull 2025
Tài liệu mới (trích bằng khóa Zotero): Cawley 2018 `EBB69J4F` · Worden và cs. 2007 `MCNRW6F5` ·
Ju và cs. 2020 `38FMATHE` · Figueiredo và cs. 2011 `23TBQTIP` · Hughes và cs. 2022 `Z9RD5DMZ`
Hạ xuống nguồn trích thường (ĐD1): [47] Zhang, Biswal & Wang 2020 · [59] Ojala & Garriga 2009
Chuẩn tra cứu: [1] ISO 19650-3 · [61]–[62] SOSA/SSN · [69] PROV-O · ISO 55000:2024 `8PB7EN2E` · BCF 3.0 `K5SGFIGW`
Trong Zotero: collection `TL-Key/Tier1`, `TL-Key/Tier2`; tag `TLTQ:Tier1`, `TLTQ:Tier2`. Ma trận: `matrix/literature_matrix.csv`.

### 7.3 Cần tìm bổ sung (Consensus → xác minh → Zotero) — **ĐÃ ĐÓNG 01/10/2026, không tìm thêm** (mục 2, quyết định 11)
| Nhóm | Truy vấn gợi ý | Phục vụ |
|---|---|---|
| Kinh điển SHM | Farrar Worden structural health monitoring machine learning; fundamental axioms structural health monitoring | 3.1 |
| Thiên lệch chọn mô hình | Varma Simon cross-validation model selection bias; Cawley Talbot over-fitting model selection | 3.4, 5.6 |
| Quản lý tài sản | ISO 55000 asset management; asset management built assets maintenance | 2.1 |
| openBIM cho vấn đề | BCF BIM collaboration format issue | 2.2 |
| Song sinh số xác suất | probabilistic graphical model digital twin Kapteyn Willcox | 2.3 |
| **Autoencoder cho SHM** | autoencoder anomaly detection structural health monitoring; unsupervised damage detection autoencoder vibration | 5.6, 3.6 |
| Bù EOV | environmental operational variability compensation SHM; cointegration SHM | 3.2, 5.6 |
| Học chủ động | active learning structural health monitoring | 3.6, 5.6 |
| **Quan trắc nhà xưởng** | crane-induced vibration steel building; industrial building monitoring operational variability; portal frame monitoring | 1.2, 3.2 |
| **Bu lông hiện trường** | bolt loosening field monitoring steel structure; in-situ bolted connection inspection | 1.2, 3.6 |
| **Sự cố nhà thép công nghiệp** | steel industrial building failure; corrosion pre-engineered steel building | 1.2 |
| LLM trích xuất hồ sơ | large language model information extraction inspection report construction | 5.6 |

Tiêu chí nhận: tạp chí có phản biện hoặc chuẩn chính thức; tối đa 2–3 tài liệu mỗi nhóm.

### 7.4 Khuôn đọc sâu (mỗi tài liệu = 1 ghi chú `notes/<citekey>.md` + 1 dòng ma trận)
| Cột | Nội dung |
|---|---|
| Citekey / Số cũ | citekey Zotero; số trong danh mục gốc nếu có |
| Tier / Cụm | Tier1/2; một trong 5 cụm: Song sinh số · SHM–bu lông–EOV · Độ tin cậy đánh giá · Truy vết thông tin · Giá trị quyết định |
| Luận điểm | Tài liệu khẳng định gì (1–2 câu) |
| Bằng chứng | Dữ liệu, phương pháp, phạm vi kiểm chứng |
| Giới hạn | Tác giả tự nêu + giới hạn nhận thấy (ghi rõ đâu là của tác giả, đâu là nhận định của NCS) |
| Tác động K1/K2/K3 | Thu hẹp / mở rộng / không liên quan, kèm lý do |
| Vị trí sử dụng | Mục trong tiểu luận v2 |
| Mức đã đọc | Toàn văn / tóm tắt + phương pháp / chỉ tóm tắt |

**Quy tắc phản chứng cho ứng viên khoảng trống** (`revision/GD2_nhat_ky_khoang_trong.md`; NCS duyệt 30/09/2026). Mỗi ứng viên có thêm hai trường:
- **Phản chứng đã kiểm:** nguồn, chuẩn hoặc hệ thống có thể đã giải quyết vấn đề (ví dụ CMMS, BCF 3.0, IFC Monitor [2], ISO 19650); ghi kết quả đối chiếu kèm trang, hoặc "chưa kiểm".
- **Phát biểu đã thu hẹp:** phát biểu sau khi trừ phần đã được giải quyết.

Một ứng viên chỉ được đưa vào GĐ3 khi trường "Phản chứng đã kiểm" không còn mục nào ghi "chưa kiểm".

### 7.5 Cách viết cho luận điểm chưa có nguồn (NCS quyết định ở ĐD1, 30/09/2026)
| Luận điểm | Cách viết |
|---|---|
| L1.1 (Việt Nam) | Số liệu chính thức về quy mô khu công nghiệp + nhận định của NCS từ thực tế kiểm định, ghi rõ là nhận định, không kèm tỷ trọng. **Mốc đã chốt (01/10/2026):** 478 KCN thành lập, 324 hoạt động, khoảng 11/2025, số liệu Cục ĐTNN (Bộ Tài chính) qua `XM5ZUP99`; chi tiết `revision/L1_1_so_lieu_KCN_da_kiem.md` |
| L1.1 (quốc tế) | Saleem & Qureshi (2018) `J358BJ7Z` chỉ dùng cho nhận định chung "nhà thép tiền chế được dùng rộng rãi vì hiệu quả kinh tế"; không dùng làm căn cứ tỷ trọng |
| L1.4 | Nhận định của NCS; kiểm ý "tránh gián đoạn" trong toàn văn Torres-Barriuso và cs. (2025) `QMVQCEL5` trước khi trích |
| L1.5, L2.4, L3.1 | Trích đúng đối tượng của nguồn (kết cấu thép ngoài trời, cầu); việc áp sang nhà xưởng ghi là diễn giải |
| L2.1 | Tách bằng chứng (Cawley 2018, Ostachowicz 2019: chi phí là rào cản) và diễn giải; nối diễn giải với chỉ số M3.4 (chi phí ghi nhận) |
| Farrar & Worden `HQQJMZDW` | Ghi năm theo trang bản quyền của sách in; chưa xem được thì ghi chú "chờ kiểm năm" |

Danh sách luận điểm và ứng viên: `revision/GD1_luan_diem_can_nguon.csv`, `revision/GD1_ung_vien.csv`.

---

## 8. Schema rút gọn (tham chiếu khi viết 5.5, 5.7, Bài 2) — NCS duyệt 01/10/2026

Bản đầy đủ 12 thực thể, C1–C9, 12 chỉ số trước đây xem lịch sử git (commit trước 01/10/2026 tối); không dùng nữa.

**Định vị:** mở rộng trên nền IFC 4.3 của [35] (`IfcRelAssignsToProduct` lần kiểm tra → bằng chứng,
`IfcRelAdheresToElement` bằng chứng → cấu kiện, `IfcRelAssignsToProcess` bằng chứng → hành động) và BCF 3.0 (trạng thái,
sự kiện), bổ sung **tầng bằng chứng** và **tầng trách nhiệm**. Không dựng mô hình song song.

**6 thực thể:**
| Thực thể | Trường chính (thuộc tính đã gộp) |
|---|---|
| `COMPONENT` | BIM_GUID, model_version |
| `SENSOR` + `SENSOR_MAPPING` | Sensor_ID; valid_from, valid_to, install_record_ref |
| `EVIDENCE` | Condition_Evidence_ID, evidence_type (cảm biến / quan sát / NDT), BIM_GUID (n:m), Sensor_ID (loại cảm biến), value, uncertainty, method_version (git commit), scope: inference_unit, data_split, install_batch, applicable_conditions; obs_context (đợt đo, **khoảng thời gian đo**, cấu hình cảm biến, nhiệt độ, cờ cầu trục); **created_at**; revision_of (bản ghi không sửa đè) |
| `INSPECTION_RECORD` | Inspection_Record_ID, BIM_GUID, **inspector_role, inspected_at, finding, finding_uncertainty**; dùng EVIDENCE qua quan hệ `EVIDENCE_USE` có trường **used_at**, within_scope, justification |
| `ACTION` | Action_ID, **Inspection_Record_ID**, priority_level (4 mức), Action_Status (mở → đang xử lý → hoàn thành → đã xác minh; suy ra từ STATUS_EVENT mới nhất) |
| `STATUS_EVENT` | Status_Event_ID, Action_ID, from_to, timestamp, actor_role, evidence_ref (trỏ `EVIDENCE_USE`), reason |

Trường in đậm thêm theo Phụ lục A, NCS duyệt 02/10/2026 (cần cho C3, C5, C9 và vòng lặp kiểm tra tạo nhãn). Danh mục đầy đủ, cột bắt buộc, bước chuyển trạng thái được phép (Bảng A.2, dùng cho C6) và cách tính `within_scope` (Bảng B.1): `tieuluan/phuluc.md`.

Quan hệ: EVIDENCE n:m COMPONENT ở tầng dữ liệu; khi xuất IFC tách mỗi cặp thành một `IfcRelAdheresToElement`.

**5 ràng buộc** (kiểm bằng script Python): **C1** không mồ côi · **C3** thời điểm đo nằm trong hiệu lực ánh xạ
cảm biến – cấu kiện · **C5** dùng bằng chứng ngoài phạm vi phải có lý do · **C6** bước chuyển có căn cứ và đúng vai trò ·
**C9** sự kiện trỏ tới phiên bản bằng chứng còn hiệu lực tại thời điểm chuyển.

**Công cụ (một bộ duy nhất):** Python, IfcOpenShell, SQLite hoặc JSON, script kiểm ràng buộc; scikit-learn/PyTorch cho
MT1, MT3. Không dùng RDF/SHACL/ontology; ánh xạ khái niệm sang SOSA/SSN, PROV-O chỉ trình bày bằng một bảng trong Bài 2.

**Đối chứng:** **B0** = hồ sơ kiểm định theo thực hành hiện hành ở Việt Nam, mã hóa tay 20–30 hồ sơ của nhà xưởng Khánh Hòa (cùng BIM). **B1** = mô hình IFC 4.3
theo [35] + BCF 3.0, **chưa có** tầng bằng chứng và tầng trách nhiệm, dựng trên **cùng** BIM nhà xưởng, cùng script (tắt các
ràng buộc C5, C6, C9 và các trường mới). B0, B1 và mô hình đề xuất dùng cùng danh sách lỗi chèn mù, cùng bộ câu hỏi truy ngược,
cùng tập bằng chứng MT1.

**4 chỉ số:**
| Chỉ số | Đo |
|---|---|
| M1 Đủ thuộc tính bắt buộc | tỉ lệ bản ghi đầy đủ; chỉ mô tả — chênh lệch so với B0 hiển nhiên do schema bắt buộc trường, so sánh có ý nghĩa là với B1 |
| **M2 Phát hiện lỗi chèn mù (chỉ số chính)** | khoảng 30 lỗi do người thứ ba chèn; báo cáo theo từng nhóm lỗi, trọng tâm "dùng bằng chứng ngoài phạm vi" (C5, C9) và "đổi trạng thái không căn cứ" (C6); tỉ lệ bắt được ở B0, B1, mô hình đề xuất |
| M3 Truy ngược | thời gian hoặc số bước trả lời ba câu hỏi của người quản lý |
| M4 Chi phí ghi nhận | số phút mỗi bản ghi |
**Khóa trước khi đo** (lưu trong repo, có commit trước lần đo đầu): quy tắc mã hóa B0; đặc tả B1 (bám sát [35] tr. 4–7 và BCF 3.0,
ghi mọi lựa chọn khi dựng); danh sách lỗi chèn mù và người chèn; bộ câu hỏi truy ngược (sau phỏng vấn); cách tính M1–M4. Nơi lưu
đề xuất `03_PAPERS/PAPER_2/khoa_truoc_khi_do/` (NCS xác nhận). Bỏ chỉ số tính tổng quát (một công trình, ghi ở phần giới hạn).

---

## 9. Đặc tả nhiệm vụ đầu tiên: Mục 5.6 "Công cụ AI và vai trò trong chuỗi bằng chứng"

**Yêu cầu nội dung:**
1. Mở mục bằng nguyên tắc "AI tạo bằng chứng, con người quyết định" và giải thích vì sao
   (trách nhiệm giải trình trong kiểm định an toàn).
2. Bảng công cụ theo gói:

| Gói | Công cụ AI | Vai trò → trường schema |
|---|---|---|
| WP1 Phòng thí nghiệm | RF, SVM-RBF (đặc trưng thủ công miền thời gian – tần số); 1D-CNN, ResNet1D (tín hiệu chuẩn hóa) | Phân biệt trạng thái liên kết có kiểm soát → `value` |
| | Đánh giá theo nhóm (giữ lại cả lần chạy; giữ lại cả đợt), chấm điểm theo bản ghi, kiểm định hoán vị, báo cáo biến thiên theo seed và fold | Căn cứ khai báo → `VALIDITY_SCOPE`, `uncertainty` |
| WP3 Hiện trường | **Autoencoder** học đường cơ sở vận hành; sai số tái tạo làm chỉ báo bất thường | Tín hiệu đề nghị kiểm tra, không phải chẩn đoán → `EVIDENCE` loại cảm biến |
| | Bù EOV (hồi quy theo nhiệt độ, trạng thái vận hành) | Giảm báo động giả do cầu trục, máy móc, nhiệt |
| WP2 Schema | Không dùng AI; mã hóa tay 20–30 hồ sơ kiểm định cũ | Phân loại lỗi, đường cơ sở B0 |
| WP4 Hỗ trợ hành động | Không dùng AI hộp đen; logic bốn mức bằng luật minh bạch | Mọi `STATUS_EVENT` truy ngược được |

3. Giải thích vì sao đổi vai AI từ **phân loại (PTN)** sang **phát hiện bất thường (hiện trường)**:
   hiện trường không có nhãn hư hỏng, điều kiện khác PTN. Lập luận bằng TÀI LIỆU
   (ví dụ [18], [45], [57], [56] và tài liệu Autoencoder tìm bổ sung), **không bằng kết quả Paper 1**.
4. Nêu công cụ hỗ trợ không phải AI: Python, scikit-learn, PyTorch; git commit làm `method_version`;
   IfcOpenShell; SQLite (rút gọn 01/10/2026: bỏ MLflow/DVC, ifctester, rdflib, pySHACL).
5. Đoạn ngắn về khai báo sử dụng AI tạo sinh (chi tiết đặt ở phần đầu tiểu luận).

**Cấm trong mục này:** số liệu, bảng hoặc nhận định về hiệu năng từ Paper 1; tên mô hình ngoài
danh sách trên nếu NCS chưa duyệt (calibration/conformal, SHAP/Grad-CAM, Gradient Boosting chỉ
được thêm khi NCS xác nhận).

**Trích dẫn cần có trong Zotero trước khi viết:** tài liệu gốc về RF, SVM, 1D-CNN/ResNet trong SHM
(chỉ dùng nếu tìm và xác minh được); ít nhất 2 tài liệu Autoencoder cho SHM; [53], [14], [59] cho
đánh giá; [45] cho EOV.

**Sản phẩm phiên:** `tieuluan/05_chuong5.md` (mục 5.6), danh sách trích dẫn mới, việc còn mở. Dừng chờ duyệt.

**Quyết định viết 5.6A (NCS duyệt 29/09/2026):**
- **Nguồn:** chỉ dùng tài liệu tag `5.6A` trong `TL-Key/Bổ sung` và các số cũ đã nêu ở trên; danh sách
  dự phòng ở `revision/bao_cao_nguon_5_6A.md` mục 5 không được trích khi chưa nhập Zotero.
- **G1 – Autoencoder:** việc áp dụng Autoencoder cho nhà xưởng được viết như **đề xuất của luận án**,
  dựa trên các nghiên cứu huấn luyện chỉ với dữ liệu trạng thái bình thường (Wang & Cha 2021;
  Ghazimoghadam & Hosseinzadeh 2024). Hiệu quả khi có cầu trục là nội dung kiểm chứng ở WP3, không
  khẳng định trong tiểu luận.
- **G3 – Học chủ động:** ghi nhận rằng hướng này chủ yếu được phát triển trên dữ liệu cầu và máy bay
  (Hughes 2022; Bull 2022); áp dụng cho nhà công nghiệp là đề xuất của luận án.
- **G4 – ResNet1D:** trích He 2016 + Wang/Yan/Oates 2017 + tổng quan Avci 2021/Kiranyaz 2021.
  Không tìm thêm nguồn.
- **G6 – LLM:** không trích nguồn. Chỉ 1–2 câu mô tả LLM là công cụ hỗ trợ WP2, có kỹ sư xác nhận và
  báo cáo độ chính xác trích xuất.
- **Mục giới hạn:** nhãn tạm là **5.8** (thay mục 5.8 hiện có; bản nháp ở
  `revision/nhap_5_8_pham_vi_ap_dung.md`); đánh số lại toàn Chương 5 ở GĐ5.

---

## 10. Bảng thuật ngữ (dùng nhất quán)

| Thuật ngữ | Tiếng Anh | Định nghĩa dùng trong tiểu luận |
|---|---|---|
| Bằng chứng trạng thái | condition evidence | Một nhận định về tình trạng của một cấu kiện, kèm nguồn tạo ra nó và phạm vi mà nó được phép sử dụng |
| Phạm vi hiệu lực | validity scope | Điều kiện (đơn vị suy luận, cách chia dữ liệu, đợt lắp đặt, cấu hình cảm biến, điều kiện áp dụng) mà trong đó bằng chứng còn đúng |
| Nguồn gốc | provenance | Ai, cái gì, quy trình nào tạo ra dữ liệu/bằng chứng |
| Đường cơ sở vận hành | operational baseline | Trạng thái tham chiếu của chính công trình trong vận hành bình thường |
| Vòng lặp kiểm tra tạo nhãn | inspection-labelling loop | Kết quả kiểm tra xác nhận của kỹ sư trở thành nhãn hiện trường gắn vào cấu kiện |
| Mức ưu tiên | priority level | Bình thường → Theo dõi → Kiểm tra → Kiểm tra ưu tiên |
| Trạng thái xử lý | action status | Mở → Đang xử lý → Hoàn thành → Đã xác minh |
| Song sinh số / Bóng số / Mô hình số | DT / DS / DM | Theo mức tự động hóa luồng dữ liệu (Kritzinger và cs., 2018) |

Phân biệt bắt buộc: **kết quả phân loại** (một con số) ≠ **bằng chứng trạng thái** (con số + nguồn gốc
+ phạm vi) ≠ **chẩn đoán hư hỏng** (kết luận của kỹ sư sau kiểm tra).

**Kịch bản minh họa chuẩn:** cảm biến ghi nhận bất thường → tạo bằng chứng gắn cột trục C3 →
kỹ sư A kiểm tra, xác nhận bu lông lỏng → trưởng phòng B phê duyệt siết lại → hành động đóng →
sáu tháng sau có sự cố, truy ngược được toàn bộ.

**Ba câu hỏi của người quản lý:** Cái gì bất thường, ở đâu? Tin được đến mức nào? Ai đã xử lý, dựa vào đâu?

---

## 11. Những điều KHÔNG làm

- Không đưa kết quả Paper 1 vào tiểu luận dưới bất kỳ hình thức nào.
- Không bịa hoặc "hoàn thiện" thông tin thư mục từ trí nhớ.
- Không chốt hay viết lại khoảng trống trước Điểm duyệt 3.
- Không sửa nhiều chương trong một phiên; không sửa tệp .docx gốc.
- Không gọi hệ thống là "song sinh số" mà không khai báo mức tích hợp (DM/DS/DT).
- Không mở rộng phạm vi sang bảo trì dự đoán, tuổi thọ còn lại hay tối ưu chi phí.
- Không thêm mục tiêu, WP, bài báo, thực thể schema, ràng buộc hay chỉ số ngoài mục 2A và 8.
- Không đọc thêm tài liệu hay tìm thêm phản chứng cho tiểu luận (trừ yêu cầu bằng văn bản của thầy hoặc phản biện).
- Không làm việc "meta" (đồng bộ skill, quản trị nhiều tầng) khi chưa xong hai bài báo.

---

## 12. Trạng thái tiến độ (cập nhật sau mỗi phiên được duyệt)

| Hạng mục | Trạng thái | Ghi chú |
|---|---|---|
| Kế hoạch 7 giai đoạn | ✅ Đã duyệt | |
| 4.1 Mục 5.6A Công cụ AI | ✅ Đã duyệt; câu đồng liên kết hoàn thiện theo toàn văn Cross 2011 (01/10); còn câu autoencoder chờ PDF Ghazimoghadam | `tieuluan/05_chuong5.md` mục 5.6A, 1.691 từ, 1 bảng; nguồn: `revision/5_6A_luan_diem_nguon.csv`; chờ PDF: xem `revision/viec_ton_dong_GD0.md` mục 5 |
| 4.3 Mục 1.3A, 1.4A (Chương 1) | 🟡 Chờ duyệt, đã sửa 1.3A theo góp ý (30/09) | `tieuluan/01_chuong1.md`, nhãn tạm đặt sau 1.2 hiện có; 1.3A ba thành phần, ba nguồn bằng chứng; 1.4A 389 từ; nguồn hợp nhất: `revision/1_3A_nguon_hop_nhat.md` |
| 5.6A Chuẩn bị nguồn | ✅ Xong (29/09) | 13 tài liệu nhập vào TL-Key/Bổ sung (tag 5.6A); 5 dự phòng; PDF ưu tiên: Wang & Cha, Figueiredo, Hughes, Bull 2022 (revision/bao_cao_nguon_5_6A.md mục 6). Quyết định viết ở mục 9. Chưa viết 5.6A |
| GĐ0 Chuẩn bị | ✅ ĐD0 đã duyệt (29/09) | Markdown + đối chiếu 84 tài liệu xong (28–29/09); tồn đọng: `revision/viec_ton_dong_GD0.md` |
| Quy ước trích dẫn (4.4), viết về giới hạn (4.5) | ✅ Đã thêm (29/09) | Danh sách 80 câu giới hạn chờ NCS duyệt (GĐ5) |
| GĐ1 Bổ sung tài liệu | ✅ Đã duyệt (ĐD1) (30/09) | Nhập 17 tài liệu mới, gắn 5 tài liệu có sẵn; danh sách key 30 (12 Tier 1, 18 Tier 2) ở mục 7.1–7.2; báo cáo: `revision/bao_cao_GD1.md` |
| GĐ2 Đọc sâu | ✅ Đóng (01/10): 29/30 đọc toàn văn ([80] bỏ); 5 nhóm phản chứng N-20, N-21, N-23, N-24, N-25 đã xử lý (N-20 qua nguồn thứ cấp [29], N-25 mức tóm tắt); N-12d, e tính Maes 2022, Mosqueira-Rey 2023 là căn cứ cùng chiều | Bản trình: `revision/DD2_ban_trinh.md`; việc chờ NCS: `revision/viec_cho_NCS.md`; nhật ký: `revision/GD2_nhat_ky_khoang_trong.md` |
| Rút gọn phạm vi, khóa 3 mục tiêu | ✅ NCS duyệt (01/10) | Mục 2 (QĐ 5, 7, 9–11), 2A, 6.0, 8, 9, 11, 13 |
| GĐ3 Khoảng trống | ✅ NCS duyệt bản GĐ3b (01/10): G-A (A1, A2), G-B; F-1 (B1), F-2 (phỏng vấn) duyệt; còn gửi thầy | `revision/GD3_khoang_trong_va_muc_tieu.md`: bảng kiểm, hai khoảng trống (G-A 7 nhóm căn cứ trước 2025, G-B 6), ba mục tiêu MT1–MT3, ma trận, văn bản đề xuất thay 5.2 và RQ (785 từ, chưa chèn `tieuluan/`); `[CẦN NGUỒN]`: IFC4 ADD2 TC1, Khuyến nghị W3C SSN |
| GĐ4 Viết mục mới (4.2–4.9) | ✅ Xong (02/10): 5.2, 1.2A, 3.2A, Dẫn nhập NCS duyệt | `tieuluan/01_chuong1.md` 1.2A (`revision/1_2A_luan_diem_nguon.csv`); `tieuluan/03_chuong3.md` 3.2A (gộp 3.6A; `revision/3_2A_luan_diem_nguon.csv`); `tieuluan/00_dannhap.md` mở bằng kịch bản cột C3 |
| GĐ5 Tái cấu trúc | 🟡 Đã duyệt (02/10): đồng bộ Ch.1, 2, 4, 5, Phụ lục A, B; MT1 ba mức; câu giới hạn v2; 6 tài liệu cầu (giữ [64], [66], [78]). Đánh số lại toàn bộ mục, bảng, tham chiếu chéo; rút trùng 1.1.1/1.2; 2.5, 3.6 nhắc mục mới (02/10), chờ NCS duyệt | Còn ngoài GĐ5: [61], [62] ở 4.2.1 (chuyển sang Khuyến nghị W3C khi nhập Zotero); câu autoencoder chờ PDF Ghazimoghadam; toàn văn ISO 55000:2024; giọng 5.9.2 (tùy chọn) |
| Hoàn thiện tiểu luận (prompt 02/10) | 🟡 NCS duyệt (02/10): HT0; Pha 1 (HT1 p1–p3); Pha 2 (HT2 T1–T4); Pha 3 Chương 1 (HT3). Rà soát tổng thể `revision/RS_ra_soat_tong_the_20261002.md`. HT4 sửa gộp A1–A7, A9 và Pha 3 Chương 5, 4, 3 NCS duyệt. Đang làm: Pha 3 Chương 2 | Nhãn khoảng trống trong văn bản: **KT1** (vế A1 đánh giá, A2 khai báo) và **KT2** (= G-A, G-B ở mục 2); G1–G7 giữ cho góp ý của thầy. `revision/HT0_…`, `HT1_…` |
| GĐ6 Nhất quán & xuất bản | ⬜ | |

---

## 13. Kế hoạch bài báo và lộ trình (NCS duyệt 01/10/2026)

| Bài | Mục tiêu | Nội dung cốt lõi | Điều kiện nộp |
|---|---|---|---|
| Bài 1 | MT1 | Đánh giá theo nhóm ở hai mức (lần chạy, đợt) cho thấy mức lạc quan của đánh giá cùng lần chạy; kết quả phải kèm phạm vi hiệu lực | Gate 1 đóng; nộp ngay sau khi tiểu luận chốt |
| Bài 2 | MT2 (+MT3) | Schema rút gọn mở rộng IFC 4.3/BCF; 4 chỉ số so với B0 trên BIM nhà xưởng thật và dữ liệu MT1 | Schema + script + B0 xong; không chờ quan trắc dài hạn |

Lộ trình gợi ý: tháng 0–1 chốt tiểu luận, nộp Bài 1 · tháng 1–3 schema, script, lắp cảm biến, mã hóa B0 · tháng 3–7
quan trắc, kịch bản C3, đo chỉ số · tháng 7–9 nộp Bài 2, ghép luận án 5 chương theo ba mục tiêu.
Chọn tạp chí: kiểm xếp hạng SJR hiện hành khi nộp.
