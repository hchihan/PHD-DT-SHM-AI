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
- **Mục tiêu luận án:** một mô hình thông tin / schema truy vết bằng chứng – trách nhiệm
  cho kiểm tra – bảo trì kết cấu thép, được kiểm chứng trên công trình thật với chỉ số rõ ràng.
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
   đánh giá theo nhóm (giữ lại cả lần chạy), chấm điểm theo bản ghi, kiểm định hoán vị,
   báo cáo biến thiên theo seed và theo fold.
5. **Công cụ AI ở hiện trường (WP3): Autoencoder** phát hiện bất thường so với đường cơ sở
   vận hành, kèm bù ảnh hưởng môi trường – vận hành (EOV) và vòng lặp kiểm tra tạo nhãn.
6. **Nguyên tắc AI:** "AI tạo bằng chứng, con người quyết định". Mọi đầu ra AI trở thành
   một bản ghi `EVIDENCE` có `method_version`, `uncertainty`, `VALIDITY_SCOPE`.
7. **Schema dạng đồ thị**, không phải chuỗi tuyến tính (xem mục 8).
8. **Tách hai trục:** `priority_level` (Bình thường → Theo dõi → Kiểm tra → Kiểm tra ưu tiên)
   và `Action_Status` (mở → đang xử lý → hoàn thành → đã xác minh).
9. **Khoảng trống chỉ được chốt sau khi đọc sâu 20–30 tài liệu key** (yêu cầu của thầy hướng dẫn).
   K1–K3 hiện tại là giả thuyết làm việc, chờ Điểm duyệt 3.

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
- PDF lưu dạng tệp liên kết (linked file) trong thư mục `pdf/` của dự án (tên tệp bắt đầu bằng khóa Zotero); `pdf/` và `*.pdf` có trong `.gitignore`.

### 4.2 Văn phong
- Tiếng Việt học thuật, trang trọng; thuật ngữ tiếng Anh để trong ngoặc ở lần đầu.
- Tách rõ **bằng chứng** (tài liệu nói gì) và **diễn giải** (tác giả suy ra gì).
- Mỗi đóng góp có một câu khẳng định tích cực; các giới hạn gom về mục giới hạn (nhãn tạm 5.8, đánh số lại ở GĐ5).
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
  trình bày ở Mục 5.8", và gom nội dung về mục giới hạn.
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
- Khi viết 3.6, chuyển đoạn "bốn nhóm bằng chứng" (5.6A.3, đoạn 1) sang 3.6 và rút gọn phần ở 5.6A còn 1–2 câu trỏ về.
- Mục 5.5, 5.7 và Phụ lục B phải định nghĩa đủ các thuật ngữ mà 5.6A đã dùng (bản ghi bằng chứng, trường giá trị, trường độ bất định, trường phạm vi hiệu lực, trường điều kiện áp dụng, bối cảnh quan trắc, bản ghi kiểm tra, bản ghi sử dụng bằng chứng, sự kiện chuyển trạng thái, đường cơ sở B0, ràng buộc về sử dụng bằng chứng ngoài phạm vi hiệu lực).

### 6.2 Việc tái cấu trúc (Giai đoạn 5)
- Chuyển RQ và kiến trúc nghiên cứu từ Chương 1 sang Chương 5; xóa phần lặp.
- Gom các câu giới hạn về mục giới hạn (nhãn tạm 5.8, đánh số lại ở GĐ5), cắt khoảng một nửa.
- Chuỗi định danh chi tiết + thang V1–V4 → Phụ lục A; ràng buộc C1–C8 → Phụ lục B;
  ma trận RQ–WP–Paper–Gate → Phụ lục C.
- 4.5.4: tách `priority_level` và `Action_Status`.
- Bổ sung ISO 55000 (2.1) và BCF (2.2).
- Rà các tài liệu ngoài danh sách key, đặc biệt 6 tài liệu về cầu ([63]–[66], [77], [78]):
  giữ nếu còn làm căn cứ, loại nếu không.
- Khai báo sử dụng AI tạo sinh ở phần đầu.

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
- Phụ lục A, B, C.

### 6.4 Lưu ý cho Giai đoạn 6
- Trước khi chèn bản khai báo AI tạo sinh, rà cột `muc_da_doc` của mọi bảng luận điểm – nguồn; tài liệu chỉ đọc tóm tắt phải được đọc thêm, hoặc chỉ dùng cho nhận định ở mức tóm tắt, để câu "mọi trích dẫn đều được đối chiếu với bản gốc" là đúng.

---

## 7. Tài liệu key

### 7.1 Tier 1 — đọc sâu toàn văn (số hiệu theo danh mục bản gốc)
[8] Kritzinger 2018 · [7] Boje 2020 · [3] Lu, Xie, Parlikad & Schooling 2020 · [22] Hemker 2019 ·
[18] Brake 2019 · [19] Ramasso · [53] Kapoor & Narayanan 2023 · [2] Theiler & Smarsly 2018 ·
[35] Bellon 2025 · [44] García 2026 · [16] Çelik 2023 · [17] Wu 2026

### 7.2 Tier 2 — đọc có trọng tâm
[10] Chen 2021 · [29] Johannes 2021 · [45] Sohn 2007 · [57] Bull 2021 · [56] Da Silva ·
[47] Zhang, Biswal & Wang 2020 · [48] Pal 2022 · [14] Beleites 2013 · [15] Wheat 2024 ·
[59] Ojala & Garriga 2009 · [42] Ramonell 2023 · [21] Hagedorn 2023 · [82] Seiß 2025 ·
[28] Kamariotis, Chatzi & Straub 2023 · [80] Bull 2025
Chuẩn tra cứu: [1] ISO 19650-3 · [61]–[62] SOSA/SSN · [69] PROV-O

### 7.3 Cần tìm bổ sung (Consensus → xác minh → Zotero)
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

---

## 8. Schema (tham chiếu khi viết 5.5, 5.7, Phụ lục)

**Thực thể:** `COMPONENT` (BIM_GUID, model_version) · `MODEL_VERSION` · `SENSOR` (Sensor_ID) ·
`SENSOR_MAPPING` (valid_from, valid_to, install_record_ref) · `OBS_CONTEXT` (campaign, sensor_config) ·
`EVIDENCE` (Condition_Evidence_ID, evidence_type = cảm biến | quan sát | NDT, value, uncertainty,
method_version) · `VALIDITY_SCOPE` (inference_unit, data_split, install_batch, applicable_conditions) ·
`EVIDENCE_USE` (within_scope, justification) · `INSPECTION_RECORD` · `ACTION`
(priority_level, Action_Status) · `STATUS_EVENT` (from_to, reason, timestamp) · `AGENT` (role, authority).

**Quan hệ chính:** SENSOR–COMPONENT qua SENSOR_MAPPING có thời hạn; EVIDENCE n:m COMPONENT;
EVIDENCE 1:1 VALIDITY_SCOPE (bắt buộc); INSPECTION_RECORD dùng EVIDENCE qua EVIDENCE_USE;
INSPECTION_RECORD → ACTION → STATUS_EVENT; STATUS_EVENT dựa trên EVIDENCE_USE; AGENT thực hiện/chuyển trạng thái.

**Ánh xạ chuẩn:** SOSA/SSN (cảm biến, quan trắc) · PROV-O (derivedFrom, generatedBy, Agent) ·
IFC (cấu kiện) · IDS (thuộc tính bắt buộc) · SHACL (ràng buộc).

**Ràng buộc C1–C8:** C1 không mồ côi · C2 ID duy nhất · C3 thời điểm quan trắc nằm trong hiệu lực
ánh xạ · C4 khớp phiên bản mô hình · C5 dùng ngoài phạm vi phải có lý do · C6 bước chuyển có căn cứ
và đúng thẩm quyền · C7 bước chuyển hợp lệ theo máy trạng thái · C8 bằng chứng cảm biến bắt buộc có
OBS_CONTEXT và method_version.

**Chỉ số (5.7):** đường cơ sở B0 = thực hành hiện hành; B1 = schema cắt giảm (chỉ liên kết định danh).
RQ2: M2.1 độ nhạy phát hiện lỗi theo loại · M2.2 báo động giả · M2.3 đủ thuộc tính bắt buộc ·
M2.4 phát hiện dùng ngoài phạm vi · M2.5 độ phủ câu hỏi năng lực · M2.6 thời gian/số bước truy ngược.
RQ3: M3.1 liên tục định danh sau sự kiện thay đổi · M3.2 độ đầy đủ theo thời gian · M3.3 độ đúng
ánh xạ thực tế · M3.4 chi phí ghi nhận · M3.5 bài kiểm toán giải trình · M3.6 tính tổng quát.
Nguyên tắc: khóa câu hỏi năng lực, ngưỡng và phân loại lỗi TRƯỚC khi kiểm chứng; ca lỗi do người thứ ba chèn mù.

---

## 9. Đặc tả nhiệm vụ đầu tiên: Mục 5.6 "Công cụ AI và vai trò trong chuỗi bằng chứng"

**Yêu cầu nội dung:**
1. Mở mục bằng nguyên tắc "AI tạo bằng chứng, con người quyết định" và giải thích vì sao
   (trách nhiệm giải trình trong kiểm định an toàn).
2. Bảng công cụ theo gói:

| Gói | Công cụ AI | Vai trò → trường schema |
|---|---|---|
| WP1 Phòng thí nghiệm | RF, SVM-RBF (đặc trưng thủ công miền thời gian – tần số); 1D-CNN, ResNet1D (tín hiệu chuẩn hóa) | Phân biệt trạng thái liên kết có kiểm soát → `value` |
| | Đánh giá theo nhóm (giữ lại cả lần chạy), chấm điểm theo bản ghi, kiểm định hoán vị, báo cáo biến thiên theo seed và fold | Căn cứ khai báo → `VALIDITY_SCOPE`, `uncertainty` |
| WP3 Hiện trường | **Autoencoder** học đường cơ sở vận hành; sai số tái tạo làm chỉ báo bất thường | Tín hiệu đề nghị kiểm tra, không phải chẩn đoán → `EVIDENCE` loại cảm biến |
| | Bù EOV (hồi quy theo nhiệt độ, trạng thái vận hành) | Giảm báo động giả do cầu trục, máy móc, nhiệt |
| | Học chủ động | Ưu tiên bất thường cần kiểm tra → vòng lặp kiểm tra tạo nhãn |
| WP2 Schema | LLM trích xuất hồ sơ kiểm tra cũ, kỹ sư xác nhận | Phân loại lỗi, đường cơ sở B0; báo cáo độ chính xác trích xuất |
| WP4 Hỗ trợ hành động | Không dùng AI hộp đen; logic bốn mức bằng luật minh bạch | Mọi `STATUS_EVENT` truy ngược được |

3. Giải thích vì sao đổi vai AI từ **phân loại (PTN)** sang **phát hiện bất thường (hiện trường)**:
   hiện trường không có nhãn hư hỏng, điều kiện khác PTN. Lập luận bằng TÀI LIỆU
   (ví dụ [18], [45], [57], [56] và tài liệu Autoencoder tìm bổ sung), **không bằng kết quả Paper 1**.
4. Nêu công cụ hỗ trợ không phải AI: Python, scikit-learn, PyTorch; MLflow/DVC (cấp `method_version`);
   IfcOpenShell, ifctester; rdflib, pySHACL.
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

---

## 12. Trạng thái tiến độ (cập nhật sau mỗi phiên được duyệt)

| Hạng mục | Trạng thái | Ghi chú |
|---|---|---|
| Kế hoạch 7 giai đoạn | ✅ Đã duyệt | |
| 4.1 Mục 5.6A Công cụ AI | ✅ Đã duyệt (chờ hoàn thiện 2 câu khi có PDF) (29/09) | `tieuluan/05_chuong5.md` mục 5.6A, 1.691 từ, 1 bảng; nguồn: `revision/5_6A_luan_diem_nguon.csv`; chờ PDF: xem `revision/viec_ton_dong_GD0.md` mục 5 |
| 5.6A Chuẩn bị nguồn | ✅ Xong (29/09) | 13 tài liệu nhập vào TL-Key/Bổ sung (tag 5.6A); 5 dự phòng; PDF ưu tiên: Wang & Cha, Figueiredo, Hughes, Bull 2022 (revision/bao_cao_nguon_5_6A.md mục 6). Quyết định viết ở mục 9. Chưa viết 5.6A |
| GĐ0 Chuẩn bị | ✅ ĐD0 đã duyệt (29/09) | Markdown + đối chiếu 84 tài liệu xong (28–29/09); tồn đọng: `revision/viec_ton_dong_GD0.md` |
| Quy ước trích dẫn (4.4), viết về giới hạn (4.5) | ✅ Đã thêm (29/09) | Danh sách 80 câu giới hạn chờ NCS duyệt (GĐ5) |
| GĐ1 Bổ sung tài liệu | ⬜ | |
| GĐ2 Đọc sâu | ⬜ | |
| GĐ3 Khoảng trống | ⬜ | Cần gửi thầy |
| GĐ4 Viết mục mới (4.2–4.9) | ⬜ | |
| GĐ5 Tái cấu trúc | ⬜ | |
| GĐ6 Nhất quán & xuất bản | ⬜ | |
