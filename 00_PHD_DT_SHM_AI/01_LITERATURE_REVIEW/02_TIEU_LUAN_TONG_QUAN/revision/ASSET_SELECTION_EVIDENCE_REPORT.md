# ASSET_SELECTION_EVIDENCE_REPORT — Lý do chọn đối tượng (Mục 1.2.1)

Ngày: 04/10/2026. Bản nguồn: `xuat_ban/HO_CHI_HAN_TIEU_LUAN_TONG_QUAN_FINAL_PROOFREAD.docx` (commit 015abd9).
Bản xuất: `xuat_ban/HO_CHI_HAN_TIEU_LUAN_TONG_QUAN_FINAL_ASSET_RATIONALE.docx` (69 trang, 87 tài liệu, 253 trường
`ZOTERO_ITEM`, 1 trường `ZOTERO_BIBL`; mục lục đã cập nhật trong Word).
Sửa trên Markdown `tieuluan/01_chuong1.md`, `tieuluan/03_chuong3.md`, dựng lại bằng `xuat_ban/build.py` (đánh số IEEE tự động
theo thứ tự xuất hiện, trường Zotero giữ nguyên). Chưa commit; chờ NCS duyệt.

**Lưu ý quy trình.** CLAUDE.md QĐ 11 và 16(o) khóa việc tìm thêm tài liệu và sửa học thuật sau bản FINAL nếu không có góp ý bằng
văn bản của GVHD hoặc Hội đồng. Lần sửa này làm theo yêu cầu trực tiếp của NCS. Nếu đây là góp ý của thầy hoặc Hội đồng, nên ghi
nguồn góp ý vào `revision/changelog.md` khi duyệt.

**Công cụ đã dùng.** Zotero (kiểm trùng, nhập, metadata Crossref), OpenAlex, Scopus (tìm và kiểm metadata), trình duyệt (đọc toàn văn
MDPI). Perplexity trả lỗi 401 (khóa API không hợp lệ), không dùng được. Consensus không có trong phiên này. Elsevier, Wiley và SAGE
chặn truy cập tự động bằng trang kiểm tra bot; không vượt qua, nên các nguồn ở đó chỉ đọc tóm tắt hoặc bị loại.

---

## A. Nguồn mới đưa vào văn bản

Số tham chiếu theo bản ASSET_RATIONALE (đã đánh số lại; mọi số từ [16] trở đi dịch thêm 2 so với bản FINAL).

| Ref | Claim | Source type | Direct/supporting | DOI |
|---|---|---|---|---|
| [16] Qin, Mason & Stewart (2024), *Engineering Structures* 316, 118600 — Zotero `S96MXF6A` (mới nhập) | Nhà công nghiệp khung cổng thép được dùng rộng rãi làm nhà kho, siêu thị, xưởng sản xuất, cơ sở lưu trữ và chiếm phần đáng kể trong quỹ công trình | Tạp chí có phản biện (Elsevier, Q1) | **Direct** (đối tượng là nhà công nghiệp khung cổng thép). Chỉ đọc tóm tắt; câu dùng có nguyên văn trong tóm tắt | 10.1016/j.engstruct.2024.118600 |
| [17] Saleem & Qureshi (2018), *Sustainability* 10(6), 1761 — Zotero `J358BJ7Z` (đã có, trước đây chưa trích trong bản FINAL) | Cấu kiện PEB chế tạo tại nhà máy, chuyển đến công trường, lắp dựng bằng bu lông; dầm, cột chữ I nối bằng liên kết bu lông tại công trường; rút ngắn thời gian thi công so với khung hàn tại công trường; nhịp và bước cột lớn cho giá kệ, thiết bị, máy móc | Tạp chí có phản biện (MDPI) | **Direct** cho nhà thép tiền chế. Đọc phần Mở đầu (bản HTML); số trang chưa kiểm vì không tải được PDF | 10.3390/su10061761 |

Nguồn đã có, dùng thêm một câu:

| Ref | Claim | Source type | Direct/supporting | DOI |
|---|---|---|---|---|
| [15] Hemker, Bartenbach & Dürr (2019), *ce/papers* 3(3–4) — `B2JXAM9M` (= [22] cũ, Tier 1) | Lão hóa kết cấu thép thường do ăn mòn, mỏi, bu lông lỏng, giòn hóa hoặc mài mòn, làm giảm khả năng chịu lực (tr. 188, đã đọc PDF) | Kỷ yếu hội nghị có phản biện (Nordic Steel 2019) | **Direct** (kết cấu thép trong cơ sở công nghiệp, kinh nghiệm chương trình bảo trì) | 10.1002/cepa.1045 |

### Bảng sàng lọc nguồn ứng viên

| Source | Claim supported | Direct / Supporting / Inference | Strength | Use? |
|---|---|---|---|---|
| Qin, Mason & Stewart 2024, Eng. Struct. | Công năng kho, lưu trữ, sản xuất; phần đáng kể quỹ công trình | Direct | Mạnh (Q1), đọc tóm tắt | **Dùng** |
| Saleem & Qureshi 2018, Sustainability | Chế tạo sẵn, lắp dựng bằng bu lông tại công trường, rút ngắn thi công, nhịp lớn | Direct (PEB) | Trung bình – khá; đọc Mở đầu | **Dùng** |
| Hemker và cs. 2019 (đã có [22]) | Bu lông lỏng là nguyên nhân lão hóa ở kết cấu thép công nghiệp | Direct | Khá; đọc toàn văn | **Dùng thêm 1 câu** |
| Qin, Mason & Stewart 2023, Struct. Safety 100, 102287 | Nhà công nghiệp khung cổng mới và đã suy giảm dưới gió bão nhiệt đới | Direct | Mạnh, nhưng không đọc được tóm tắt/toàn văn | Không dùng |
| Haydar, Far & Saleh 2018, Steel Construction 11(3) 205–217 | Khung cổng là dạng hiệu quả cho nhà công nghiệp nhịp > 30 m; thời gian thi công | Direct | Khá; chỉ tóm tắt | Không dùng (Saleem đã đủ cho nhịp lớn) |
| Wang và cs. 2013, Int. J. Distrib. Sens. Netw. 9(12), 871213 — Zotero `ZVGGDWE8` (đã nhập) | Tổng quan quan trắc liên kết bu lông | Supporting | Khá; không đọc được toàn văn, tóm tắt không chứa câu "dùng rộng rãi" | **Không dùng**; mục Zotero giữ tag `TLTQ:1.2.1-asset-rationale`, NCS quyết định giữ hay xóa |
| Các bài IJRASET, IJSREM, IRJMETS, JETIR về PEB nhà kho | Công năng, ưu điểm PEB | Direct | Yếu (tạp chí chất lượng thấp, không lõi) | Loại |
| Bài về liên kết tháo lắp trong nhà mô-đun, sàn liên hợp | Tháo lắp, tái sử dụng | Supporting (hệ khác) | Không cùng đối tượng | Loại |

---

## B. Văn bản đã chèn

### B1. Mục 1.2.1, đoạn mới (giữa đoạn 1 và đoạn 2)

- **Vị trí:** sau đoạn mở đầu (số liệu khu công nghiệp, nhà xưởng là tài sản phục vụ sản xuất, chi phí dừng sản xuất); trước đoạn
  "Với khung thép liên kết bu lông, nội lực…" phân tích ba nhóm yếu tố (nới lỏng, ăn mòn, lắp ráp).
- **Đoạn cũ:** không có (chèn mới).
- **Đoạn mới:**

> Nhóm tài sản này rộng hơn nhà xưởng sản xuất. Nhà công nghiệp khung cổng thép được dùng rộng rãi trên thế giới làm nhà kho, siêu thị, xưởng sản xuất và cơ sở lưu trữ, và chiếm một phần đáng kể trong quỹ công trình [16]. Ở dạng nhà thép tiền chế, cấu kiện được thiết kế và chế tạo tại nhà máy, chuyển đến công trường rồi lắp dựng; dầm và cột tiết diện chữ I được nối với nhau bằng liên kết bu lông tại công trường để tạo thành khung. Cách lắp dựng này rút ngắn thời gian thi công so với khung thép thông thường có cấu kiện hàn tại công trường, và hệ kết cấu cho phép nhịp, bước cột lớn để bố trí giá kệ, thiết bị và máy móc [17]. Trong vận hành, kinh nghiệm quản lý bảo trì kết cấu thép ở cơ sở công nghiệp xếp bu lông lỏng cùng ăn mòn, mỏi, giòn hóa và mài mòn vào các nguyên nhân lão hóa làm giảm khả năng chịu lực [15] (tr. 188). Từ các nguồn này, tiểu luận nhận định rằng liên kết bu lông lắp dựng tại công trường là đặc điểm cấu tạo phổ biến của nhà công nghiệp khung thép tiền chế, bất kể công năng sản xuất hay lưu trữ, và tình trạng của liên kết là đối tượng cần quản lý trong suốt giai đoạn vận hành. Đây là cơ sở để luận án chọn nhà công nghiệp khung thép liên kết bu lông làm đối tượng nghiên cứu; công trình cụ thể là các nhà xưởng nêu ở Mục 1.5.1.

- **Lý do:** trả lời "vì sao loại tài sản này" theo chuỗi công năng → đặc trưng tiền chế → liên kết bu lông lắp dựng tại công trường →
  ý nghĩa bảo trì → lý do chọn. Câu bằng chứng và câu suy luận được tách: phần "tiểu luận nhận định" là suy luận ghép [16] và [17].
  Câu cuối giữ phạm vi: đối tượng vẫn là nhà công nghiệp khung thép; công trình nghiên cứu vẫn là hai nhà xưởng.

### B2. Mục 3.4.1, đoạn 2 (chỉnh nhẹ)

- **Đoạn cũ:** "Thí nghiệm dùng một mô hình khung thép tỉ lệ 1:10 trong phòng thí nghiệm, cho phép tạo trạng thái liên kết có kiểm soát, …"
- **Đoạn mới:** thêm câu đầu "Khung nhà công nghiệp thép tiền chế được lắp dựng bằng liên kết bu lông tại công trường (Mục 1.2.1), nên đối
  tượng can thiệp của thí nghiệm là liên kết bu lông." Phần còn lại giữ nguyên.
- **Lý do:** nối lý do chọn đối tượng với thí nghiệm. Đoạn nối cuối 3.4.3 (thí nghiệm → bằng chứng → truy vết → MT2, MT3) đã đủ, không sửa.

### B3. Mục 1.5.2 (số liệu)

- "Kết quả cuối cùng là 85 tài liệu được trích dẫn" → "87 tài liệu". Số tài liệu key (30; 29 giữ lại) không đổi.

### Kiểm tra sau khi dựng

So văn bản bản ASSET_RATIONALE với bản FINAL sau khi chuẩn hóa số trích dẫn: chỉ khác ở ba chỗ B1–B3 (và dòng mục lục). Danh mục:
85 → 87 mục, không mục nào bị mất; thêm Qin 2024 và Saleem 2018. Số trích dẫn dịch do đánh số lại theo thứ tự xuất hiện, tạo
bằng script, không sửa tay. `matrix/doi_chieu_danh_muc.csv`: thêm dòng Qin 2024 (`so_cu = moi`), bổ sung ghi chú dòng Saleem.

---

## C. Luận điểm đã cân nhắc nhưng không chèn

| Luận điểm | Kết luận |
|---|---|
| PEB là hệ nhà công nghiệp chiếm ưu thế toàn cầu / được dùng nhiều nhất | **Rejected — Evidence is currently insufficient.** |
| Nhà công nghiệp khung thép có vai trò then chốt với chuỗi cung ứng, logistics, phân phối | **Rejected — Evidence is currently insufficient.** Nguồn đã đọc chỉ nêu nhà kho, siêu thị, cơ sở lưu trữ; không nêu "trung tâm phân phối" hay "logistics" |
| Liên kết bu lông là liên kết phổ biến nhất trong kết cấu thép | **Rejected — Evidence is currently insufficient.** Chỉ có căn cứ cho việc PEB lắp dựng bằng bu lông tại công trường |
| Liên kết bu lông cho phép thay thế, tháo dỡ, tái sử dụng khung nhà công nghiệp | **Rejected — Evidence is currently insufficient.** Nguồn tìm được về nhà mô-đun và sàn liên hợp, khác đối tượng |
| Tính mô-đun, khả năng mở rộng, cải tạo của PEB | **Rejected — Evidence is currently insufficient.** Không có nguồn đọc được |
| Liên kết của khung công nghiệp khó tiếp cận để kiểm tra | **Không chèn thêm.** Văn bản hiện có đã dẫn [@QMVQCEL5] (tr. 3, 5) cho chi phí, tiếp cận vùng cao. Lưu ý phản chứng: Hemker và cs. (tr. 187) nêu mối nối quan trọng của kết cấu thép công nghiệp "nhìn chung dễ tiếp cận". Hai nguồn nói về hai khía cạnh khác nhau (chi phí, an toàn tiếp cận so với vị trí nối có thể quan sát); NCS cân nhắc nếu phản biện hỏi |
| Khung PEB ít có nguy cơ lỏng theo thời gian | **Không dùng.** Saleem & Qureshi (Mở đầu) có câu này trong ngữ cảnh độ kín khí, không có dẫn chứng; trái với kinh nghiệm bảo trì của Hemker và cs. (tr. 188). Ghi nhận như một nhận định không có căn cứ trong nguồn |
| Đóng góp kinh tế của khu công nghiệp, quy mô thị trường nhà kho | **Không chèn.** Ngoài phạm vi lý do chọn tài sản; số liệu khu công nghiệp đã có ở đoạn 1 |

---

## D. Kiểm tra phạm vi

- Không thêm, không sửa RQ1–RQ3.
- Không thêm, không sửa WP1–WP4, Gate 1–5, KT1–KT3.
- Không thay đổi đóng góp (ba tầng ở 5.6), không thêm bài báo, mô hình AI, thí nghiệm.
- Logistics, chuỗi cung ứng không trở thành phạm vi nghiên cứu; đoạn mới chỉ nêu công năng của nhóm tài sản.
- Đối tượng vẫn là "nhà công nghiệp khung thép liên kết bu lông"; công trình nghiên cứu vẫn là hai nhà xưởng ở Mục 1.5.1.
- Mục tiêu luận án (MT1–MT3) không đổi.

## E. Bốn câu hỏi kết thúc

1. **Vì sao chọn nhà công nghiệp khung thép?** Đoạn 1 (quy mô khu công nghiệp, chi phí dừng sản xuất, chương trình bảo trì) và đoạn
   mới (phần đáng kể quỹ công trình [16]). Đủ.
2. **Vì sao không chỉ giới hạn ở nhà xưởng sản xuất?** Đoạn mới: cùng hệ kết cấu dùng làm nhà kho, cơ sở lưu trữ [16]. Đủ ở mức
   công năng; vai trò với logistics, chuỗi cung ứng: *Evidence is currently insufficient.*
3. **Vì sao liên kết bu lông?** Lắp dựng bằng bu lông tại công trường [17]; bu lông lỏng là nguyên nhân lão hóa [15]; cơ chế nới
   lỏng, ăn mòn, lắp ráp ở đoạn kế tiếp [18] và các nguồn sẵn có. Đủ; mức "phổ biến nhất": *Evidence is currently insufficient.*
4. **Vì sao dẫn tới thí nghiệm trạng thái liên kết và chuỗi bằng chứng?** Câu nối mới ở 3.4.1 và đoạn nối cuối 3.4.3 (đã có). Đủ.

## F. Việc còn mở

1. NCS đọc và duyệt đoạn B1, B2.
2. Kiểm số trang của Saleem & Qureshi trên PDF (Mở đầu, khoảng tr. 1–2) nếu muốn thêm số trang.
3. Nếu muốn đọc toàn văn Qin 2024 (CC-BY): tải PDF thủ công qua trình duyệt của NCS, lưu `pdf/S96MXF6A_Qin2024.pdf`.
4. (Đã xử lý ở vòng 2: Wang 2013 được dùng.)
5. Sau khi duyệt: cập nhật `revision/changelog.md`, CLAUDE.md QĐ 16(n) (85 → 88 tài liệu), commit đúng các tệp
   `tieuluan/01_chuong1.md`, `tieuluan/03_chuong3.md`, `matrix/doi_chieu_danh_muc.csv`, `xuat_ban/zotero_cache.json`,
   `revision/ASSET_SELECTION_EVIDENCE_REPORT.md` và bản .docx mới.
6. (Đã xử lý ở vòng 2: slide 20261004.)

---

## G. Vòng 2 (04/10/2026): đọc toàn văn ba PDF, thêm số trang và ý bổ trợ

NCS lưu ba PDF; đã đổi tên theo khóa Zotero: `pdf/S96MXF6A_Qin2024.pdf`, `pdf/J358BJ7Z_Saleem2018.pdf`, `pdf/ZVGGDWE8_Wang2013.pdf`.
Bản xuất mới: `xuat_ban/HO_CHI_HAN_TIEU_LUAN_TONG_QUAN_FINAL_ASSET_RATIONALE_r2.docx` (70 trang, 88 tài liệu, 257 trường Zotero;
mục lục đã cập nhật). Tên mới vì bản vòng 1 đang mở trong Word. So với bản FINAL (chuẩn hóa số trích dẫn): chỉ khác ở các đoạn
dưới đây và B1–B3; danh mục 85 → 88, không mất mục nào.

| Vị trí | Nội dung thêm | Nguồn, trang | Loại |
|---|---|---|---|
| 1.2.1, đoạn mới | Số trang: Qin (tr. 1–2; tr. 2 ghi "phần lớn quỹ công trình ở nhiều đô thị"), Saleem (tr. 2) | [16], [17] | Direct |
| 1.2.1, đoạn mới | Bu lông được dùng rộng rãi để lắp ghép cấu kiện trong kết cấu cơ khí và xây dựng nhờ độ tin cậy, khả năng chịu lực, dễ bảo trì | Wang 2013 [18] (tr. 6) | Supporting (kết cấu nói chung) |
| 1.2.1, đoạn "Với khung thép liên kết bu lông" | Khung cổng thép ít dư thừa kết cấu; hư hỏng một cấu kiện có thể lan truyền tới sập; công trình hư hỏng kết cấu rất có thể không còn an toàn và mất công năng. Câu này làm căn cứ cho nhận định sẵn có "tình trạng liên kết quyết định trực tiếp khả năng làm việc của khung" | Qin [16] (tr. 3; tác giả dẫn lại hai nguồn khác) | Direct |
| như trên | Trong đánh giá dưới tác động lũ, khả năng chịu cắt của bu lông neo chân cột thấp hơn nhiều so với cột; cắt bu lông neo là dạng phá hoại tới hạn | Qin [16] (tr. 4) | Direct, nhưng chỉ trong bối cảnh tải lũ |
| 1.2.1, nhóm yếu tố lắp ráp | Lực siết thiếu hoặc thừa là nguyên nhân thường gặp gây hỏng mối nối; siết bằng cờ lê lực có thể sai lệch tới 50% lực căng do ma sát | Wang 2013 [18] (tr. 1) | Supporting |
| 3.1, đoạn 2 | Phương pháp dao động làm được với thiết bị thông dụng, nhưng với kết cấu bu lông phức tạp vẫn khó xác định trạng thái và vị trí bu lông lỏng | Wang 2013 [18] (tr. 1–2) | Supporting |
| 1.5.2 | 87 → 88 tài liệu trích dẫn | — | — |

Ghi nhận thêm khi đọc toàn văn (không chèn):
- Saleem & Qureshi (tr. 2) có câu cho rằng khung PEB rất ít khả năng bị lỏng theo thời gian; câu này nằm trong ngữ cảnh độ kín
  khí, không có dẫn chứng. Không dùng; trái với Hemker và cs. (tr. 188) và Wang và cs. (tr. 1, 6).
- Saleem & Qureshi (tr. 14): với khung PEB nhẹ, tải gió chi phối thiết kế. Có thể dùng sau này nếu cần lập luận về tải động; chưa chèn.
- Qin và cs. (tr. 2): nhà công nghiệp ở Úc có cấp quan trọng thấp nên không thiết kế cho tải lũ. Ngoài phạm vi.

### Slide (HT20)

`BAO_CAO_TLTQ_FINAL_20261004.pptx`, giữ nguyên bản 03/10; script `revision/HT20_slide_scripts/edit_slides_asset.py`.
- Slide 3: ô 1 đổi thành "Vai trò trong sản xuất và lưu trữ" (thêm Qin và cs., 2024); ô Đề tài thêm "lắp dựng bằng bu lông tại
  công trường (Saleem & Qureshi, 2018)"; ghi chú thuyết trình thêm hai câu tương ứng.
- Slide 4: gạch đầu dòng lắp ráp thêm "lực siết khó kiểm soát (… ; Wang và cs., 2013)"; ghi chú thêm câu về sai số cờ lê lực và
  ít dư thừa kết cấu.
- Slide 6: 85 → 88 tài liệu (ô và ghi chú).
- Đã xuất ảnh slide 3, 4 để kiểm: chữ không tràn khung.
