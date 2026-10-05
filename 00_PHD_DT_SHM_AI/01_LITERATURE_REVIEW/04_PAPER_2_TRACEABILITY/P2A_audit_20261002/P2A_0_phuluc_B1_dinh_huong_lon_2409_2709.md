# B1 – Kiểm toán nhóm "định hướng/outline lớn 24–25/09 và trình chiếu 27/09"

Người kiểm toán: AU-B1. Chỉ kiểm kê và đối chiếu; chưa phản biện khoa học.
Quy ước viết tắt tệp (dùng trong toàn bộ báo cáo):
- **F1** = `PAPER2_BAO_CAO_DINH_HUONG_OUTLINE_VA_KE_HOACH_THUC_THI_GATE2_GATE3.md` (808 dòng; docx SHA-256 `ea05fedb…6cd87`)
- **F2** = `PAPER2_COMPLETE_ACADEMIC_OUTLINE_AND_EXECUTION_GUIDE.md` (779 dòng; docx SHA-256 `6b1881d3…2cb`)
- **F3** = `PAPER2_NOTEBOOKLM_HUONG_DAN_HOC_VA_AUDIO_OVERVIEW_25092026.md` (262 dòng; docx SHA-256 `42649e2c…cadd`)
- **F4** = `ChuyenDe2_Paper2_DUT.md` (200 dòng; pptx SHA-256 `64cb8b06…c30`)
- **F5** = `ChuyenDe2_Paper2_Traceability.md` (237 dòng; pptx SHA-256 `0321ad50…afd`)

(SHA-256 lấy từ `/home/claude/p2/sha256_p2.txt`; chỉ ghi để định danh bản gốc. Tệp gốc docx/pptx không có trong sandbox nên không kiểm được metadata "sửa lần cuối" bên trong tệp; thứ tự thời gian dưới đây suy từ nội dung, ngoại trừ khoảng cách "~9 phút" do người gọi cung cấp.)

**Mức đọc: cả 5 tệp đã đọc hết (F1 dòng 1–808/808; F2 1–779/779; F3 1–262/262; F4 1–200/200; F5 1–237/237).** Số dòng trích là dòng trong bản text ở `/home/claude/p2/txt/`.

---

## 1. Bảng kiểm kê

| Tệp | Ngày ghi trong tệp / phiên bản | Vai trò | Nội dung chính (≤2 câu) | Đọc hết? | Đề xuất trạng thái | Lý do |
|---|---|---|---|---|---|---|
| F1 | "Ngày lập: 24/09/2026"; "bản làm việc để trao đổi với hai thầy hướng dẫn; chưa được phê duyệt" (d.17–19). Không ghi số phiên bản. | Định hướng + outline + kế hoạch thực thi (báo cáo lớn) | Định hướng Paper 2 theo GAP-A/B/C, C1–C3, RQ2.1–2.3; mô hình 10 thực thể + CORRESPONDENCE, R01–R17 (SHACL), 12 CQ, 9 loại lỗi, M1–M3; kế hoạch 18 việc Gate 2→3, 11 mâu thuẫn K1–K11, outline bản thảo 8 mục. | Có, 1–808/808 | **Lỗi thời về khung định hướng** (bị thay bởi: tinh chỉnh P/V/I 25/09 → F3/F4/F5; và bởi phạm vi đã khóa: tiểu luận + GD3b). **Tham khảo** như kho chi tiết (bảng K1–K11, REC0004, quy trình 8 bước tương ứng 1:10→1:1, phép thử G3-P/N). | Dùng RDF/SHACL, 10 thực thể, GAP-A/B/C, C1–C3, 12 CQ, không có B0/B1 (xem mục 4). Nhưng chứa nhiều dữ kiện có nguồn (mục 2) và các bảng mâu thuẫn hữu ích cho Pha 1. |
| F2 | "Ngày 24/09/2026" (d.19); không ghi số phiên bản. Phần I = dùng phát triển bản thảo; Phần II = tài liệu học/thực thi, "không đưa vào bản thảo nộp tạp chí" (d.21). | Outline (dạng bài báo) + hướng dẫn thực thi + đọc/đối chiếu nguồn | Viết lại cùng nội dung F1 thành outline học thuật 9 mục (Abstract nháp tiếng Anh, Intro, Lit, Method, Framework, Case, Results, Discussion, Conclusions) + 6 phụ lục A–F (thuật ngữ, Gate 2, Gate 3, CDE, kế hoạch/đọc, đối chiếu nguồn); 40 vị trí đánh dấu `[CẦN BỔ SUNG]`. | Có, 1–779/779 | **Lỗi thời một phần – cùng bị thay như F1** (khung C1–C3/RDF-SHACL/12 CQ/M0–M3). **Không trùng F1**: là bản tái cấu trúc, mới hơn F1 (xem 1b). Giữ **F2 làm khung outline bài báo tham khảo** (cùng F1 làm kho bảng). | Cùng khung khái niệm đã bị thay với F1; nhưng có giá trị riêng: Phụ lục F (mức đọc từng nguồn), Phụ lục D (CDE tối thiểu), phần "hai tầng xác nhận", nguồn bổ sung 24/09. |
| F3 | Không có dòng ngày trong thân; tên tệp `…25092026`; d.6: "Biên tập từ tài liệu định hướng Paper 2 ngày 25/09/2026". | Tài liệu học (NotebookLM) + prompt audio/quiz; không phải định hướng gốc | Tóm tắt "bản học nhanh" của hướng tinh chỉnh 25/09: 3 thuộc tính provenance/validity-scope/identity, Gap 2A–2C, RQ2-P2 + SRQ2.1–2.3, 3 lớp validation V2.1–V2.3, scope firewall, prompt NotebookLM, bài nói 90 giây. Không có số liệu thực nghiệm nào. | Có, 1–262/262 | **Tham khảo** (tài liệu học, thứ cấp của `PAPER2_REFINED_DIRECTION…v1.0.25092026`). Không dùng làm nguồn kết luận. | Là bản biên tập của tài liệu khác (REFINED v1.0, ngoài nhóm); khung P/V/I khác phạm vi khóa (mục 4); không có dữ kiện gốc. |
| F4 | Slide 1: "Khóa 2025", nêu hai người hướng dẫn (PGS.TS Ngô Ngọc Tri; PGS.TS Phạm Anh Đức); không ghi ngày trên slide; ghi chú giao: "sửa 27/09". Slide 10 kết "Trân trọng cảm ơn Hội đồng." | Trình chiếu (dạng báo cáo Chuyên đề 2 trước Hội đồng, có mục lục, 10 slide) | Báo cáo Chuyên đề 2: vị trí → khoảng trống 2A/2B/2C → đóng góp trung tâm P/V/I + SRQ2.1–2.3 → khung khái niệm + mô hình dữ liệu → V2.1–V2.3 + M1–M3 → kết quả đã có (6 IFC, 3.356, 10.328, 8 cặp, 15 nhóm SHACL, 12 CQ) → lộ trình B0–B9 + xin góp ý. | Có, 1–200/200 | **Trùng một phần với F5 – giữ F5** làm bản nội dung đầy đủ; F4 giữ như **Tham khảo** (bản dạng Hội đồng, chứa câu hỏi góp ý riêng d.198). | Cùng 10 slide, cùng cấu trúc; F4 là bản ngắn hơn (xem 1c). |
| F5 | Slide 1: "27/09/2026"; "Bản đề xuất định hướng trình người hướng dẫn – chưa được duyệt, không đóng Gate nào." (d.13–14). Chân trang "09/2026". | Trình chiếu (bản trình người hướng dẫn, 10 slide) | Cùng mạch với F4 nhưng chi tiết hơn: thêm bảng RQ/WP/Chương/Gate (slide 2), slide "Vấn đề" riêng (slide 3), phạm vi tìm kiếm của khoảng trống (slide 4), 10 nhóm lỗi liệt kê (slide 8), kiến nghị thêm Status_Event (slide 10). | Có, 1–237/237 | **Còn hiệu lực ở mức "bản trình mới nhất của nhóm"** nhưng **vẫn lệch phạm vi khóa** (mục 4) → dùng như nguồn cho lập luận trình bày, không dùng cho đặc tả. | Mới hơn F4 về nội dung (1c); có cảnh báo "chưa được duyệt". |

### 1b. F1 so với F2: có phải hai phiên bản của cùng một tài liệu không?

**Kết luận: cùng dòng (cùng ngày 24/09, cùng tác giả, cùng khung khái niệm, cùng số liệu), nhưng KHÔNG phải bản sửa nhỏ: F2 là bản viết lại/tái cấu trúc từ F1 sang dạng outline bài báo + phụ lục, và F2 mới hơn F1.** Không nên gọi là "trùng" để bỏ một bản.

Bằng chứng định lượng (tôi so tự động đoạn văn và hàng bảng):
- 27 đoạn giống hệt nhau giữa F1 và F2 **đều là mục tài liệu tham khảo** (ISO ×2, IfcOpenShell, Velez, …); **0 hàng bảng giống hệt**; không có đoạn thân bài nào được chép nguyên. Cả hai đều được viết lại từ đầu dù thông tin trùng.
- Danh mục tài liệu tham khảo: F1 có 37 mục, F2 có 41 mục, chung khoảng 28 (so theo tác giả-năm). **Chỉ F1**: Brake 2019, Çelik 2023, Matarneh 2022, Oraskari 2021, Piras 2026, Sedigh & Müller 2025, White 2025, Yin 2020. **Chỉ F2**: Aydın 2025, buildingSMART 2024, Cyganiak 2014, Fang 2025, Faqih & Zayed 2021, Hamledari 2018, Harris & Seaborne 2013, Kamariotis 2024, Makhoul 2022, Sagarna 2022, Stolk & McGlinn 2020, Tammik 2022 và Tammik n.d.

**Thứ tự: F1 trước, F2 sau (đồng thuận với "~9 phút" người gọi cho).** Bằng chứng nội dung, không dựa dấu thời gian tệp:
- F1 d.161 ghi "Perplexity MCP trả lỗi 401… **Consensus MCP không được dùng**"; F2 Bảng F.1 (d.660) có đề mục "Rà soát bổ sung ba nghiên cứu do **Consensus** tìm được (24/09/2026)" (Hamledari 2018, Faqih & Zayed 2021, Sagarna 2022). Tức F2 chứa kết quả tìm kiếm mà F1 nói chưa làm.
- F2 d.197 và d.210 đưa Faqih/Sagarna/Hamledari vào tổng quan; F1 không có ba bài này.
- F2 chỉ còn 8 dòng mâu thuẫn (Bảng F.2, d.668–679), F1 có 11 dòng K1–K11 (d.167–181); F2 thêm một mâu thuẫn mới (ba chỉ số vs bốn chỉ số, d.677).

**Phần TRÙNG (cùng nội dung, khác cách viết):**
- Cùng tên bài (họ tiêu đề "Validity-scoped condition evidence for … component-level … traceability", F1 d.624, F2 d.149), cùng RQ2 → RQ2.1/2.2/2.3 gắn C1/C2/C3 (F1 d.264–268; F2 d.187).
- Cùng chuỗi lõi Sensor → BIM binding → Condition Evidence → Inspection Record; cùng cặp neo Prototype_Component_ID + Binding_ID; cùng Model_Version_ID; cùng "Validity_Scope là thuộc tính của bằng chứng, tách khỏi phiên bản mô hình".
- Cùng Sổ tương ứng 1:10 → 1:1 với Physical_Identity = FALSE, Link_Basis theo nhãn trạng thái, R16/R17 (F1 d.381–431; F2 d.307–315).
- Cùng ví dụ CP2/RUN012/REC0004 (F1 d.433–453; F2 d.366).
- Cùng 12 CQ làm sổ làm việc, R01–R15 + R16–R17, 9 loại lỗi, RD-001…RD-008, phép kiểm chứng độc lập (người thứ hai lập ca lỗi, niêm phong SHA-256), kiểm thử 16/16 chỉ là kiểm thử đơn vị.
- Cùng số liệu: 216 recording, 6 IFC, 3.356, 10.328, 8 cặp, 676/596 vs 718/16 (chưa thống nhất), 573442 lệch.
- Cùng trạng thái Gate: Gate 1 OPEN (chưa ký), Gate 2 OPEN, Gate 3 chưa được phép chạy chính thức.
- Cùng danh sách đọc A1/A2 (García, Borkowski, Bellon, Hagedorn–Pauwels–König, Mariniello, Ciccarese, Mitchell, Seiß, …). Bellon 2025 vẫn "chỉ đọc tóm tắt" ở cả hai (F1 d.238, 694; F2 d.210, 645).

**Phần KHÁC (F1 có, F2 không / F2 có, F1 không / hai bên đổi):**

| Điểm | F1 | F2 |
|---|---|---|
| Đối tượng đọc / hình thức | Báo cáo trình thầy hướng dẫn, 23 mục đánh số + bảng định tuyến, nhãn `[ĐÃ CÓ]/[CANDIDATE]/[DỰ KIẾN]/[ĐỀ XUẤT]/[GIẢ THUYẾT]` (d.39–48) | Phần I viết thành luận điểm liền mạch để phát triển bản thảo; Phần II phụ lục học tập; **bỏ hệ nhãn trạng thái**, thay bằng 40 dấu `[CẦN BỔ SUNG: …]` (F1 có 0 dấu) |
| Mã quyết định D0xx và K1–K11 | Rất nhiều (D001…D026, K1–K11) | **Không còn mã D0xx hay K nào** (grep: 0). Chỉ còn "sổ quyết định" chung chung |
| Bảng riêng của F1, F2 không có | Bảng 0.3 nguồn; Bảng 0.4 K1–K11; Bảng 3.1 (6 chủ đề); Bảng 4.1 (GAP-A/B/C); Bảng 6.1–6.4 (C1–C3, ánh xạ bốn điểm Đóng góp 2); Bảng 7.1 dữ liệu Paper 1; Bảng 8.1 ba phương án 1:10→1:1; Bảng 9.1 quy trình 8 bước; Bảng 10.1 thực thể; Bảng 11.1 REC0004 từng mắt xích; Bảng 14.1 sổ 12 CQ; Bảng 17.1/17.2 phép thử G3-P/N; Bảng 18.1 ba chỉ số; Bảng 19.1 tên bài + tạp chí; Bảng 22.1 (18 việc); Bảng 23.1 ma trận Claim–Evidence–Limitation; Bảng Q.1 | Abstract nháp tiếng Anh + Highlights; Introduction 4 tiểu mục (Makhoul 2022, Kamariotis 2024); Bảng 1 đối chiếu nghiên cứu gần nhất; Bảng 2/3/4/5/6 của bản thảo; Bảng 4.1 có **M0**; Phụ lục A thuật ngữ (4 bảng); Phụ lục C (Gate 3, 8 bước C1–C8); **Phụ lục D CDE tối thiểu**; Phụ lục F.1 (3 nguồn bổ sung), F.3 (mức đọc từng nguồn) |
| Chỉ số | "Ba chỉ số M1–M3" (F1 d.608–614; M1 = phát hiện, M2 = đủ 6 trường, M3 = thời gian) | "M0–M3" bốn chỉ số (F2 d.268–275): thêm **M0 độ đúng truy vết**; M2 đổi định nghĩa thành "đầy đủ **và phù hợp** (được dùng đúng ngữ cảnh)"; M3 là "bổ trợ". F2 d.677 tự ghi đây là một mâu thuẫn nguồn ("ba chỉ số của tiểu luận vs bốn chỉ số của bản biên tập") |
| Thực thể | "7 thực thể của đặc tả v0.2 + 1" (d.408); Bảng 10.1 có 10 hàng (một hàng gộp 2 thực thể); T2.1 "10 thực thể" | Bản thảo: "sáu nhóm thực thể" (d.294, Bảng 3); phụ lục: "Mười thực thể của đặc tả v0.2 cộng CORRESPONDENCE" (d.491) |
| Tiêu chí đóng Gate 2 | Bảng 15.1: **12** tiêu chí (d.526–539); kế hoạch ghi "12/12" (d.680); nhưng d.483 ghi "0/10 tiêu chí (master lock)" | Bảng B.2: **11** tiêu chí (d.550–562) |
| Tạp chí đích | Có: Automation in Construction, JCCE, ITcon, "theo bản giải thích 16/09… chưa kiểm tra lại" (F1 d.628) | Không nêu |
| Số bước kế hoạch | 18 việc (Bảng 22.1) + T2.1–T2.11 | Bảng E.1: 14 nhiệm vụ; Gate 2 gồm B1–B9, Gate 3 gồm C1–C8 |
| Hành vi công cụ | Gate 3 "ba đường A/B/C" (d.547) | Phụ lục C: cùng kiến trúc, thêm danh sách phiên bản môi trường (Revit 27.3.0.28, Dynamo 4.2.1, DynamoMCP 0.5.6, Bridge 0.1.0.0, Write-Tools 0.4.0-preview; d.570) |
| Mức đọc nguồn | Ghi lẻ tẻ | Bảng F.3 hệ thống hóa: toàn văn / phần lớn / qua tiểu luận / tóm tắt / siêu dữ liệu / tài liệu kỹ thuật |
| Hai tầng xác nhận | Có nhưng rải (d.284, 360–372) | Mục 4.2 gom thành "hai tầng xác nhận độc lập" (vật lý/tương ứng vs định danh thông tin) |

Gợi ý Pha 1: nếu chỉ giữ một tệp làm "bản gốc 24/09" thì giữ **F1** (đầy đủ bảng và mã quyết định); F2 giữ vì Phụ lục D/F và khung outline. Không bỏ F2 vì "trùng".

### 1c. F4 so với F5 (hai pptx sửa 27/09)

Cùng 10 slide, cùng mạch, cùng số liệu, cùng từ vựng (2A/2B/2C; P/V/I; SRQ2.1–2.3; V2.1–V2.3; M1–M3; B0–B9 là "bước", không phải đối chứng). Khác ở độ chi tiết và đối tượng nghe.

| Điểm | F4 (DUT) | F5 (Traceability) |
|---|---|---|
| Đối tượng/hình thức | Bìa kiểu bảo vệ trước Hội đồng (nêu ngành, khóa 2025, tên hai người hướng dẫn), có slide mục lục (5 phần), cuối "Trân trọng cảm ơn Hội đồng" | Bìa có tiêu đề tiếng Anh, chuỗi khóa 5 mắt xích, ngày "27/09/2026" và dòng "chưa được duyệt, không đóng Gate nào"; chân trang "Chuyên đề 2 · NCS Hồ Chí Hân · 09/2026" |
| Slide vị trí/vấn đề | Gộp "vị trí" và "vấn đề" vào 1 slide (slide 3) | Tách: slide 2 (vị trí + bảng RQ/WP/Chương/Gate/Đầu vào/Đầu ra) và slide 3 (vấn đề, ba khối "Đầu bằng chứng / Khoảng giữa / Đầu định danh" kèm kết luận ngắn mỗi khối) |
| Phạm vi khoảng trống | "(12 bài toàn văn + 3 novelty check)" ở dòng cuối (F4 d.67) | Dòng phạm vi riêng: "12 bài toàn văn… + 3 bài novelty check + 1 bài chỉ có abstract – không tuyên bố 'chưa từng có'" (F5 d.57); thêm nhãn "NARROW_BUT_DEFENSIBLE" (d.75); thêm White 2025 vào 2A; ghi chú ngắn cho Çelik/Lee (d.62, 72) |
| Mô hình dữ liệu (slide 7) | Chỉ vẽ 5 hộp + 2 quan hệ | Có mô tả "Năm bản ghi lõi… + hai quan hệ phụ trợ (đặc tả v0.2, 23/09 – nháp, chưa duyệt)" (d.129) |
| V2.3 | "10 nhóm lỗi cài: thiếu Sensor_ID, sai BIM_GUID, binding trùng, ánh xạ hết hạn, dẫn ngoài phạm vi…" (rút gọn) | Liệt kê dài hơn: + CE mồ côi, lệch phiên bản, truy ngược đứt (d.174); thêm câu "V2.1 duyệt trước khi khóa schema; V2.2 và V2.3 chỉ chạy chính thức sau khi Gate 2 được baseline" (d.166) |
| Bảng "kết quả đã có" | Cùng 4 điều kiện, cùng kết luận "Chưa đủ ×4" | Thêm chi tiết: "Interface G1→G2 §7.2–7.4", "R07–R09 nháp", "(RD-001…008)", "G3 chưa mở"; ghi mức "15 nhóm quy tắc SHACL R01–R15 (nháp)" |
| Câu "số liệu chưa xác minh" | Trong khối kết luận slide 9 (F4 d.180) | Đặt ở phụ đề slide 9: "Số liệu được báo cáo ngày 23/09/2026; tệp nguồn chưa xác minh trong repository" (F5 d.186) |
| Lộ trình | B0–B9 (B3 "ADR: Model_Version_ID, neo kép") | Bước 0–9 (Bước 3 "ADR: Model_Version_ID, neo kép, **Valid_From/To**"; Bước 6 thêm "Đưa tệp nguồn vào repository") |
| Xin góp ý | 3 mục: (i) **ba lớp 2A/2B/2C có đủ hẹp so với García, Borkowski, Mariniello chưa** (chỉ F4); (ii) duyệt CQ01–CQ12 + Model_Version_ID + neo kép; (iii) thống nhất audit 718/676/596 và Gate (G2–G3 hay thêm G6) | 3 mục: (i) duyệt CQ01–CQ12 (gỡ D016); (ii) quyết định bằng văn bản cho Model_Version_ID, neo kép, **Status_Event**; (iii) audit + Gate (G2–G3 hay G6). **Không có** câu hỏi (i) của F4 |

**Bản nào mới hơn về nội dung: F5 (độ tin: trung bình).** Lý do: F5 chứa mọi phần tử của F4 và bổ sung (phạm vi tìm kiếm, nhãn mức khoảng trống, White 2025, Status_Event, ADR có Valid_From/To, 10 nhóm lỗi đầy đủ, cảnh báo "chưa duyệt"), tức là bản đã qua một vòng chỉnh theo quy tắc "không viết chưa từng có / ghi phạm vi tìm kiếm". Hai khả năng không loại trừ: (a) F4 là bản rút gọn dạng Hội đồng sinh ra từ F5; (b) F5 là bản dựng lại sau F4. Cả hai đều cho kết luận "F5 đầy đủ hơn". Điểm chỉ F4 có: tên người hướng dẫn, mục lục, câu hỏi góp ý cho Hội đồng về 2A/2B/2C. Cách chốt chắc chắn: đọc `docProps/core.xml` (modified) của hai pptx gốc; sandbox không có tệp gốc.

---

## 2. Số liệu

Chú thích mức xác nhận: **[BC]** = số lấy từ báo cáo thứ cấp (báo cáo tiến độ 23/09, master lock…), chưa thấy dữ liệu gốc trong thư mục; **[N]** = tôi đã dò ra tệp nguồn thứ cấp trong `/txt/` (ghi rõ); **[D]** = dẫn từ Paper 1 (bản thảo, ngoài thư mục); **[T]** = tôi tính lại từ số khác. Slide F4/F5 tự ghi "số liệu báo cáo 23/09, tệp nguồn chưa xác minh trong repository" (F4 d.180; F5 d.186).

### 2.1 Dữ liệu phòng thí nghiệm (Paper 1) – mức CANDIDATE vì Gate 1 chưa ký

| Số liệu | Giá trị | Tệp + dòng | Ngữ cảnh / mức xác nhận | Mâu thuẫn? |
|---|---|---|---|---|
| Số recording | 216 (72/campaign; 18/lớp); 216 SHA-256 nguồn khác nhau | F1 d.136, 350, 727; F2 d.356; F4 d.176; F5 d.202 | [D] Paper 1 §3.5, §4.1; "giá trị SHA từng recording nằm trong registry canonical, chưa trích" (F1 d.350) | Không |
| Số run | 18 (RUN001–RUN018; 6/campaign) | F1 d.349; F2 d.356 | [D]; D004 BLOCKING_OPEN, D003 OPEN (F1 d.349) | Không |
| Campaign | CP1 25/04/2026 (S1–S2), CP2 21/07/2026 (S1–S3), CP3 29/07/2026 (S1–S3) | F1 d.348; F2 d.356 | [D] Paper 1 Bảng 2 | REC0004 thuộc CP2 nhưng thu 29/07 (ngày của CP3) – F1 d.445, F2 d.366; đây là dữ kiện đã ghi, không phải mâu thuẫn |
| Cửa sổ | 6.899 cửa sổ; 400 mẫu; bước 200; 100 Hz | F1 d.351 (đủ 4 thông số); F2 d.356 (không nêu bước 200) | [D]; "không phải đơn vị bằng chứng chính thức (D003)" | Không |
| Tệp NPZ | 102 tệp khớp SHA-256 registry; ví dụ `cp2_s123/R12.npz` = `360527ab…aa9e`, 513 cửa sổ × 12 kênh | F1 d.354, 445 | [BC]; hash bị cắt ngắn trong tệp, không đối chiếu được | Không |
| Dự đoán cấp recording | 1.296 dòng (1D-CNN, ResNet1D; 3 seed; 3 campaign); version git `360c79f` | F1 d.356 | [BC] `recording_predictions.csv` trong `signal-loro-ml-v1.zip` (không có trong thư mục). [T] 216×2 mô hình×3 seed = 1.296: khớp | Không |
| REC0004 | CP2/RUN012, trạng thái B1, kích động BEAT_L1, 34 cửa sổ; ResNet1D seed 42: pred B2, xác suất [0,011; 0,258; 0,729; 0,003]; cả 6 lần chạy hai mô hình sâu đều dự đoán B2 | F1 d.445, 447; F2 d.366 | [BC]; Raw_Data_SHA256 của REC0004 "trích từ registry canonical (manifest f400e943…)" nhưng chưa trích (F1 d.445) | F1 và F2 nhất quán |
| Macro-F1 LORO gộp RF/SVM | 1,000/1,000 (CP1); 0,986/0,986 (CP2); 0,875/0,690 (CP3); SD_fold tới 0,139 (CP3) | F1 d.219, 355; F2 d.179; F4 d.39; F5 d.43 | [D] Paper 1 Bảng 4. Slide chỉ ghi "1,000/0,986/0,875" không nêu mô hình | Không |
| Chuyển đợt CP2↔CP3 | balanced accuracy 0,227–0,278 | F1 d.219, 355; F2 d.179; F4 d.39; F5 d.44 | [D]. F1 d.355 ghi "(chỉ mô hình sâu)"; F2 d.179 mô tả trong câu về "hai mô hình dựa trên đặc trưng" nhưng không nói rõ | Mơ hồ nhẹ (đối tượng mô hình); không có LOCO nên không có bằng chứng cross_campaign |
| Mẫu 1:10 | thép SS400 dày 2 mm; bu lông M3 hoặc hàn điểm; độ cứng chống uốn tương đối ±5% (tiêu chí chế tạo, không phải tương tự động lực học) | F1 d.361; F2 d.309 | [D] Paper 1 §3.1 | Không |
| Số tên Paper 1 | "v8" vs "v8.1 SCIENCE LOCKED" | F1 d.180 (K10) | Số liệu dùng trùng ở hai nguồn | Ghi nhận trong F1 |

### 2.2 Phía BIM/IFC/audit

| Số liệu | Giá trị | Tệp + dòng | Ngữ cảnh / mức xác nhận | Mâu thuẫn? |
|---|---|---|---|---|
| Số phiên bản IFC đã đăng ký | 6 (có SHA-256, schema IFC4X3_ADD2, phiên bản extractor) | F1 d.136, 421, 449, 727; F2 d.362; F4 d.164; F5 d.190 | [N] `GATE2_3_PROGRESS_20260923.md` d.34 ("6 phiên bản"); dữ liệu registry gốc không có trong thư mục | Không |
| Số prototype component | 3.356 | F1 d.136, 421, 727; F2 d.362; F4 d.166; F5 d.192 | [N] PROGRESS d.36 | Không |
| Số binding | 10.328 (Binding_ID sinh tất định) | cùng các dòng trên | [N] PROGRESS d.36, 86 | Không |
| Audit Revit (A) | **718 phần tử / 16 ElementId** (8 cặp IfcGUID trùng) – "audit trước 15/09" | F1 d.174 (K4); F2 d.183, 625; F4 d.200; F5 d.238 | Nguồn dò được: master lock d.221, 284 và `G2_ONE_PAGE…14092026` (ngoài nhóm) | **Có**, với số (B) |
| Audit Revit (B) | **676 cấu kiện kết cấu / 596 Structural Framing** – "audit 13/09" | F1 d.174; F2 d.183 | [N] PROGRESS d.48 ("13/09: audit toàn bộ kết cấu (676 cấu kiện). Phát hiện 8 cặp IfcGUID trùng trong Structural Framing"), d.100, 165 (596) | **Có** với (A). Cả F1 và F2 đều ghi "chưa giải quyết/không gộp" (F1 d.174; F2 d.675). Ghi chú: nhãn ngày không phân biệt được hai audit vì 13/09 cũng "trước 15/09"; slide yêu cầu GVHD thống nhất "718/676/596" (F4 d.200; F5 d.238). Cần tệp audit gốc |
| 8 cặp IfcGUID trùng | 8 cặp = 16 ElementId; **trùng ở tham số Revit**; IFC xuất 23/09: Duplicate_GUID_Count = 0 (exporter gán GlobalId mới cho phần tử thứ hai) | F1 d.136, 221, 303, 586 (RD-001: 563079 và 573442 cùng IfcGUID `21ioXTmYn1NAjAEv6442oA`); F2 d.183, 362; F4 d.43; F5 d.51 | [N] PROGRESS d.48–54. Master lock/đề xuất 24/09 chỉ ghi SUSPECTED (F1 d.175, K5) | **Có**: F1 d.175 tự ghi nguồn cũ (SUSPECTED, API_THREAD_TIMEOUT) vs mới (đã so IFC); xem mục 4 |
| Phần tử 573442 | "bị phát hiện lệch GUID" giữa tham số Revit và GlobalId binding (MV-20260803-6b17c29c, 23/09) | F1 d.175, 578, 587, 712; F2 d.362; F4 d.178; F5 d.52, 204 | [N] PROGRESS d.52 | Slide ghi như sự kiện đã kiểm; F2 d.362 giữ thận trọng ("không đồng nhất với xung đột đã chứng minh trong IFC") |
| Phần tử pilot | 524067, 552993: khớp duy nhất ở E1, E2, E2b, trạng thái candidate | F1 d.578; F2 d.362; F4 d.178; F5 d.204 | [BC]; "E1/E2/E2b" **không được định nghĩa** trong F1/F2 | Không; thiếu định nghĩa |
| Level_Name trống | 596 Structural Framing (Reference Level = −1) | F1 d.683 (việc 15); F2 d.581 (`[CẦN BỔ SUNG]` nguyên nhân) | [N] PROGRESS d.100, 165 | Không |
| Môi trường | Revit 2027.3 (F1 d.155) / "Revit 27.3" (F1 d.547) / "Revit 27.3.0.28; Dynamo 4.2.1; DynamoMCP 0.5.6; Bridge 0.1.0.0; Write-Tools 0.4.0-preview" (F2 d.570); revit-evidence-mcp 7 tool | F1 d.155, 181, 547; F2 d.526, 570 | [BC] tiến độ 23/09 | Cách ghi phiên bản Revit khác nhau (2027.3 vs 27.3) – cùng một sản phẩm |
| Model_Version_ID ví dụ | `MV-20260803-6b17c29c` | F1 d.422, 449; F2 d.485 | Ví dụ định dạng; "noncanonical" | Không |

### 2.3 Kiểm thử, chỉ số, lỗi

| Số liệu | Giá trị | Tệp + dòng | Ngữ cảnh / mức xác nhận | Mâu thuẫn? |
|---|---|---|---|---|
| Kết quả ca lỗi 23/09 | 16/16 phát hiện, 0 dương tính giả | F1 d.176, 482, 602, 612, 714; F2 d.511, 679; F4 d.158; F5 d.182 | [N] PROGRESS d.68. **Chỉ là kiểm thử đơn vị do người viết quy tắc tạo**; F1 d.641: "Không dùng kết quả 16/16"; F1/F2/slide thống nhất | Không (khớp với phạm vi khóa) |
| M2 trên dữ liệu mẫu | 2/2 | F1 d.613 | Dữ liệu mẫu tổng hợp; không có ý nghĩa | – |
| M3 thử | 5,5 ms; 5 bước nối | F1 d.614 | "Dữ liệu mẫu rất nhỏ; chưa có ý nghĩa" | – |
| Số CQ | 12 (CQ01–CQ12) nháp, chưa khóa; ánh xạ 5 CQ của master lock (CQ-1…CQ-5) | F1 d.172, 487–504; F2 d.254, 509; F4 d.145, 199; F5 d.170, 200, 236 | Chờ duyệt (D016 BLOCKING_OPEN) | **Có** với phạm vi khóa (3 câu truy ngược) |
| Số luật toàn vẹn | R01–R15 chạy được (slide: "15 nhóm quy tắc SHACL"); F1/F2 thêm R16, R17 (đề xuất) | F1 d.136, 509–518; F2 d.544; F4 d.172; F5 d.198 | Có hậu tố a/b/c/d (R05a–c, R08a–d, R10a–b, R11a–d, R14a–b), nên "15" là số họ, không phải số luật | **Có** với phạm vi khóa (5 ràng buộc) |
| Số loại lỗi cài | **9 loại** (master lock) | F1 d.173 (K3), 482; F2 d.372, 674 | F1 "giữ 9 loại cho manifest, báo theo 7 nhóm của tiểu luận" | **Có** giữa: 9 (F1/F2), 7 nhóm (tiểu luận; F1 d.173; F2 d.674), **10 nhóm** (F4 d.149; F5 d.174), và khóa: ~30 lỗi/4 nhóm |
| Số ca tối thiểu mỗi loại | "≥ 3 ca (đề xuất)" | F1 d.482 | [T] 9 loại × 3 = ≥ 27 ca, gần với ~30 của phạm vi khóa; F2 để `[CẦN BỔ SUNG: số ca tối thiểu mỗi loại]` (d.545) | Không |
| Phép thử Gate 3 | Dương: G3-P01…P07 (7) + G3-C00; Âm: G3-N01…N12 với N09a/b/c (14 hàng) | F1 d.570–598 | [T] đếm hàng; toàn bộ "Chưa chạy" | – |
| Số chỉ số | F1: 3 (M1–M3); F2: 4 (M0–M3); F4/F5: 3 (M1–M3) | F1 d.608; F2 d.268; F4 d.150–155; F5 d.175–180 | – | **Có** giữa F1/F4/F5 và F2; và **có** với phạm vi khóa (M1–M4 khác nghĩa, mục 4) |
| Số tiêu chí đóng Gate 2 | F1 Bảng 15.1: **12**; F2 Bảng B.2: **11**; F1 d.483 và slide: **"0/10 tiêu chí (master lock)"** | F1 d.483, 526–539, 680; F2 d.550–562; F4 d.180; F5 d.206 | – | **Có** (10 / 11 / 12) |
| Số thực thể | "7 thực thể của v0.2 + 1" (F1 d.408); "7 thực thể mới" (F1 d.154); Bảng 10.1: 10 hàng (một hàng gộp PROTOTYPE_COMPONENT và BIM_BINDING, [T] 11 thực thể nếu tách); T2.1 "10 thực thể" (F1 d.473); "10 bảng CSV rỗng" (F1 d.673; F2 d.539); F2 d.491 "Mười thực thể… cộng CORRESPONDENCE"; F2 d.294 "sáu nhóm thực thể"; slide: "5 bản ghi lõi + 2 quan hệ phụ trợ" (F5 d.129) | xem trái | – | **Có** nội bộ (7+1 / 10 / 11 / 6 nhóm / 5+2) và với phạm vi khóa (6) |
| Trạng thái binding | F1 Bảng 10.1: 6 giá trị (NOT_ASSESSED, SUSPECTED_IDENTITY_ANOMALY, CANDIDATE_BINDING, BLOCKED, VERIFIED_BINDING, REJECTED_BINDING; d.421); F1 d.475: "4 trạng thái (present, candidate, verified, conflicting)"; F2 d.290: 4 (ứng viên, đã xác minh, xung đột, bị từ chối); F4/F5: 5 (UNBOUND, CANDIDATE, VERIFIED, REJECTED, SUPERSEDED; F4 d.130–134; F5 d.152–156) | xem trái | – | **Có**: 4/5/6 giá trị |
| Validity_Scope | 4 giá trị đóng: not_validated, within_campaign, cross_campaign, field_baseline_only | F1 d.313; F2 d.321 (bản tiếng Việt); F3 d.58 (within_campaign/cross_campaign) | Điều kiện: random-window chỉ mang not_validated; cross_campaign đòi LOCO | Không |
| Trường tối thiểu của bằng chứng | 6 (hoặc 6 nhóm) | F1 d.474, 476, 574; F2 d.319 | – | Không |

### 2.4 Tài liệu và tổng quan

| Số liệu | Giá trị | Tệp + dòng | Ngữ cảnh | Mâu thuẫn? |
|---|---|---|---|---|
| Tổng quan | 82 tài liệu của tiểu luận; 5 bài CORE đọc toàn văn; 12 bài targeted; novelty check **4 bài** (16/09) | F1 d.157, 225 | CLOSE_SEARCH (D021) | Slide: "12 bài toàn văn + **3** novelty check (+ 1 bài chỉ có abstract)" (F4 d.67; F5 d.57). Hợp lý nếu 3 + 1 = 4 (bài abstract-only có thể là Bellon), nhưng không có tệp nào nói rõ |
| Danh mục tham khảo | F1 37 mục; F2 41 mục; chung ~28 | [T] đếm tự động | – | – |
| Sổ nguồn K | 11 mâu thuẫn K1–K11 | F1 d.165 | – | F2 chỉ còn 8 hàng không mã (d.668–679) |
| García 2026 | 22 tệp IFC thật; Borkowski: 8 câu hỏi năng lực, 3 cấu kiện/3 giai đoạn; Seiß: 11 CQ | F1 d.233, 235; F2 d.206 | Từ hồ sơ đọc sâu (ngoài nhóm) | Không |
| Số hình/bảng bản thảo | F2 "sáu hình và chín bảng" (d.442) | F2 d.442–462 | Bảng 10.1 liệt kê Hình 1–6, Bảng 1–9; F1 có 7 hình ảnh nhúng, F2 6 | Không |

### 2.5 Số liệu cần nguồn theo BRIEF

| Cần nguồn | Kết quả dò |
|---|---|
| 6 IFC | F1, F2, F4, F5 đều dẫn; nguồn thứ cấp tìm được: `GATE2_3_PROGRESS_20260923.md` d.34. Registry gốc không có trong thư mục |
| 3.356 cấu kiện, 10.328 liên kết | PROGRESS d.36, 86. Registry gốc không có |
| 718 phần tử | master lock d.221, 284 (ngoài nhóm); không có trong PROGRESS |
| 676 phần tử | PROGRESS d.48 |
| Dữ liệu thô REC0004, manifest f400e943…, SHA `360527ab…aa9e` | Không có trong thư mục |

---

## 3. Quyết định và mã treo

Trạng thái ghi theo chính các tệp (không tự suy). "Treo" = tệp ghi OPEN/BLOCKING_OPEN/chờ duyệt; "không nêu" = tệp dùng mã nhưng không ghi trạng thái.

### 3.1 Mã D (sổ quyết định G1/G2) và quyết định thiết kế D1–D5

| Mã | Nội dung | Tệp + dòng | Trạng thái |
|---|---|---|---|
| D001 | Chuỗi luận án: dữ liệu dao động → bằng chứng → cấu kiện BIM → hồ sơ kiểm tra → hỗ trợ hành động | F1 d.150, 187 | Đã chốt (F1: "đã khóa") |
| D002 | Status_Event noncanonical | F1 d.177 (K7) | Treo/không canonical |
| D003 | Đơn vị bằng chứng: run hay recording (run là mặc định) | F1 d.349, 351, 447, 476, 528, 671, 715, 728 | Treo (OPEN) |
| D004 | Run là đơn vị nhóm khi chia dữ liệu; Assembly_ID chưa có | F1 d.349, 423, 445 | Treo (BLOCKING_OPEN) |
| D005 | Định danh vật lý Sensor_ID (khối kế thừa, không serial) | F1 d.353, 395, 474, 671, 715, 728; F4 d.41, 176; F5 d.48, 202 | Treo (BLOCKING_OPEN) |
| D007 | Quy tắc gộp xác suất cấp cửa sổ → recording | F1 d.356, 447, 476, 671, 715, 728 | Treo (BLOCKING_OPEN) |
| D010 | CEI (độ bất định/SD_fold dạng có cấu trúc) | F1 d.447, 476, 671 | Treo ("chưa chốt") |
| D011 | Quản trị định danh (identifier governance) | F1 d.475 | Không nêu |
| D012 | Ngoại lệ một-nhiều có quản trị (nút cột–kèo ↔ 2 cấu kiện) | F1 d.401 | Không nêu |
| D013 | Lược đồ hồ sơ kiểm tra, bản số trích dẫn bằng chứng | F1 d.425, 477, 676, 728 | Treo (BLOCKING_OPEN) |
| D014 | Action_Status là thuộc tính hay thực thể ACTION | F1 d.177, 178 | Treo (BLOCKING_OPEN) |
| D015 | Máy trạng thái hành động | F1 d.177 | Treo (BLOCKING_OPEN) |
| D016 | Bộ câu hỏi nghiệp vụ (5 hay 12 CQ) | F1 d.172, 480, 677, 728; F5 d.236 ("gỡ D016") | Treo (BLOCKING_OPEN); slide kiến nghị GVHD duyệt |
| D017 | Chỉ xuất hiện trong dải "D003–D017" (tiêu chí Gate 2 #1) | F1 d.528 | Không nêu nội dung |
| D021 | Tổng quan đóng CLOSE_SEARCH | F1 d.161, 225 | Đã chốt |
| D026 | Chỉ xuất hiện trong dải "D001–D026" (nguồn: sổ G1_G2) | F1 d.150 | Không nêu |
| D1 | SHACL là cơ chế kiểm chứng chính | F4 d.139; F5 d.162 (và F1 d.154 "D1–D5" của v0.2) | Chốt (theo v0.2, "quyết định của NCS") → **mâu thuẫn với phạm vi khóa** (mục 4) |
| D2 | Neo kép Prototype_Component_ID + Binding_ID | F1 d.302, 673 | Chốt theo v0.2 (23/09) nhưng F3/F4/F5 coi là "ADR chờ quyết định" (F3 d.84, 147; F4 d.189; F5 d.220, 237) |
| D3 | ACTION_STATUS_EVENT, máy 9 trạng thái | F1 d.177 | "Chốt 23/09" bởi NCS, chưa có phê duyệt GVHD; ngoài lõi Paper 2 theo F1 |
| D4 | – | không xuất hiện riêng | – |
| D5 | Không sửa mô hình gốc; ghi trên bản sao | F1 d.154, 553 | Chốt theo v0.2 |

Lưu ý: tên "D1…D5" (v0.2, ngày 23/09) và "D001…D026" (sổ quyết định G1/G2) là hai không gian mã khác nhau nhưng viết gần giống nhau; F4/F5 chỉ ghi "D1", dễ nhầm với D001.

### 3.2 Mâu thuẫn K1–K11 (F1 d.167–181) và tương ứng trong F2

| Mã | Nội dung | Tệp + dòng | Xử lý/Trạng thái |
|---|---|---|---|
| K1 | Đóng góp: C1–C3 hay bốn điểm của Đóng góp 2 (tiểu luận 5.7.2) | F1 d.171, 329–336, 669 | Tạm dùng C1–C3; cần GVHD chốt. F2 d.672 có (không mã). **Bị thay** trong F3/F4/F5 bằng một đóng góp trung tâm P/V/I |
| K2 | 5 CQ hay 12 CQ | F1 d.172, 487; F2 d.673 | Tạm dùng 12; chưa duyệt (D016) |
| K3 | 9 loại hay 7 nhóm lỗi | F1 d.173; F2 d.674 | 9 cho manifest, báo 7 nhóm; F4/F5 lại ghi 10 nhóm |
| K4 | Audit 718/16 vs 676/596 | F1 d.174, 640, 712; F2 d.675 | **Chưa giải quyết**; slide vẫn xin GVHD thống nhất |
| K5 | 8 cặp GUID trùng: SUSPECTED vs đã đối chiếu IFC 23/09 | F1 d.175; F2 d.676 | Dùng nguồn 23/09; phía Revit xác nhận trùng; trạng thái binding 16 phần tử chờ quyết định người |
| K6 | Gate 3 chưa mở nhưng đã chạy 16 ca 23/09 | F1 d.176; F2 d.679 | Xếp là kiểm thử đơn vị |
| K7 | ACTION_STATUS_EVENT 9 trạng thái vs Status_Event noncanonical | F1 d.177; F2 d.678 | Giữ Action_Status là thuộc tính hỗ trợ; ngoài lõi |
| K8 | Action_Status thuộc Inspection Record hay ACTION | F1 d.178 | Chờ D014 |
| K9 | Nhánh quản trị 17/07 vs bộ v2.x | F1 d.179 | Dùng CURRENT_STATUS v2.4; **F2 bỏ** |
| K10 | Tên Paper 1: v8 vs v8.1 | F1 d.180 | Số liệu trùng; **F2 bỏ** |
| K11 | DT Revit Evidence Bridge: "insufficient" (master lock) vs add-in 0.1.0.0/7 tool (23/09) | F1 d.181 | Dùng nguồn 23/09; công cụ không là đóng góp; **F2 bỏ** (chỉ còn trong Phụ lục C) |
| (mới F2) | 3 chỉ số vs 4 chỉ số | F2 d.677 | Dùng M0–M3, M3 bổ trợ |

### 3.3 Gate, mã công việc, mã câu hỏi, mã luật, mã phép thử

| Mã | Nội dung | Tệp + dòng | Trạng thái |
|---|---|---|---|
| Gate 1 | Bằng chứng phòng thí nghiệm (Paper 1) | F1 d.33, 140, 203, 730; F2 d.466; F4 d.180; F5 d.206 | OPEN, chưa ký; bản ghi chỉ dùng ở mức CANDIDATE |
| Gate 2 | Đặc tả (khóa từ điển, hợp đồng bằng chứng, CQ, luật, manifest) | F1 d.459–539; F2 d.530–562 | OPEN; "0/10 tiêu chí" (slide, F1 d.483) hoặc 12/11 tiêu chí (F1 Bảng 15.1/F2 B.2) |
| Gate 3 | Kiểm chứng thực thi | F1 d.545; F2 d.570; F5 d.210 | Chưa được phép chạy chính thức; điều kiện mở: Gate 2 baseline + GVHD cho dùng CANDIDATE (F1 d.730) |
| Gate 4/5 | Paper 3 / WP4 (hỗ trợ hành động); Gate 5 ngoài phạm vi | F1 d.34, 187; F4 d.30–32; F5 d.22–24 | Ngoài phạm vi Paper 2 |
| G6 | Có thêm G6 cho Paper 2 hay không | F4 d.200; F5 d.238 | Treo, xin GVHD thống nhất (không xuất hiện trong F1/F2) |
| ADR | "ADR: Model_Version_ID, neo kép, Valid_From/To" | F3 d.84, 147; F4 d.189; F5 d.220 | Treo |
| T2.1–T2.11 | Nhiệm vụ Gate 2 | F1 d.473–483 | Trạng thái "Nháp/Chưa có" 24/09 (cột cuối) |
| Việc 1–18 | Kế hoạch ưu tiên | F1 d.669–686 | Chưa làm |
| B1–B9 / C1–C8 (F2) | Bước Gate 2 / Gate 3 | F2 d.538–546; d.580–587 | Chưa làm. **Va chạm mã** với C1–C3 (đóng góp) và với C1, C3, C5, C6, C9 (ràng buộc theo phạm vi khóa), và "B0–B9" của slide (F4 d.186–196) với B0/B1 (đối chứng theo phạm vi khóa) |
| CQ01–CQ12 | Sổ câu hỏi nghiệp vụ nháp | F1 d.489–504 | Chưa khóa SHA-256, chưa duyệt |
| CQ-1…CQ-5 | Câu hỏi của master lock (ánh xạ vào CQ01–CQ12: CQ-1→CQ03/04; CQ-2→CQ05/06; CQ-3→CQ01; CQ-4→CQ07; CQ-5→CQ12) | F1 d.487–504 | Chỉ còn dạng ánh xạ |
| R01–R15 | Luật SHACL nháp (`gate2_3_shapes_draft_v0.1.ttl`) | F1 d.481, 509–516 | Chạy được, chưa khóa |
| R16, R17 | Bằng chứng lab_1_10 chỉ gắn tới 1:1 qua CORRESPONDENCE đã duyệt (R16); chỉ hồ sơ lab_specimen trích dẫn (R17) | F1 d.431, 517–518; F2 d.315, 544 | [ĐỀ XUẤT], chờ duyệt |
| R07/R07b/R08a–d/R09/R09b | Giao thức–phạm vi hiệu lực, bản chụp phạm vi, người xác nhận | F1 d.514; F5 d.203 (nháp) | Nháp |
| G3-P01…P07, G3-C00, G3-N01…N12 | Phép thử Gate 3 | F1 d.570–598 | [DỰ KIẾN]; "Chưa chạy" |
| RD-001…RD-008 | Ca lỗi định danh thật (8 cặp) | F1 d.303, 586; F2 d.512; F4 d.147; F5 d.172 | Dùng như ca thật; trạng thái binding chờ người |
| Gap 2A/2B/2C, V2.1–V2.3, SRQ2.1–2.3, RQ2-P2 | Khung 25/09 | F3 d.105–129; F4 d.49–81; F5 d.60–93 | Đề xuất chưa duyệt (F5 d.14) |
| GAP-A/B/C | Khung 24/09 (F1) | F1 d.246–250 | Bị thay trong khung 25/09 |
| C1/C2/C3 | Ba đóng góp (F1/F2) | F1 d.296–336; F2 d.189 | Bị thay trong F3/F4/F5 |
| M0–M3 | Chỉ số | F1 d.610–614; F2 d.270–275 | Chờ dữ liệu |
| Trạng thái chain "Action_Status" | Cuối chuỗi, chỉ đọc | F3 d.82; F4 d.91; F5 d.108 | Hỗ trợ, ngoài lõi |
| Status_Event | Quyết định bằng văn bản về Status_Event | F5 d.237 | Treo (xin GVHD) |
| NOT_ESTABLISHED, NARROW_BUT_DEFENSIBLE | Nhãn mức khoảng trống/bằng chứng | F4 d.60; F5 d.69, 75 | Nhãn của hồ sơ khóa (nguồn ngoài nhóm) |

---

## 4. Điểm lệch so với phạm vi đã khóa

Mức độ: **Cao** = mâu thuẫn trực tiếp với một mục trong phạm vi khóa; **Trung bình** = cùng hướng nhưng khác tên/định nghĩa hoặc nhẹ hơn mức khóa; **Thấp** = khác biệt hình thức; **Khớp** = phù hợp phạm vi khóa.
Ghi chú chung: không tệp nào trong nhóm chứa "BCF" (grep: 0 kết quả), "M4", "B0/B1" theo nghĩa đối chứng, "ĐG1–ĐG3", "chèn mù", "STATUS_EVENT" viết hoa như thực thể lõi.

| Chiều | Tệp nói gì (trích ngắn + dòng) | Phạm vi khóa nói gì | Mức độ |
|---|---|---|---|
| **Số thực thể** | F1: "giữ nguyên chuỗi lõi và 7 thực thể của đặc tả v0.2, thêm một thực thể" (d.408); Bảng 10.1 có 10 hàng (d.417–427); T2.1 "10 thực thể" (d.473). F2: "Mười thực thể… cộng CORRESPONDENCE" (d.491) và "sáu nhóm" (d.294). F4/F5: "5 bản ghi lõi + 2 quan hệ phụ trợ" (F5 d.129) | 6 thực thể: COMPONENT; SENSOR+SENSOR_MAPPING; EVIDENCE; INSPECTION_RECORD (qua EVIDENCE_USE); ACTION; STATUS_EVENT. Mô hình 10 thực thể v0.2 phải ánh xạ sang 6, không dùng song song | **Cao** (dùng song song 10/11 thực thể, không có bảng ánh xạ 10→6; F2 "sáu nhóm" trùng số 6 nhưng nhóm khác: Nguồn đo, Tương ứng thông tin, Cấu kiện và phiên bản, Bằng chứng, Hồ sơ, Lịch sử quyết định, d.299–305) |
| **ACTION và STATUS_EVENT** | F1: "ACTION và STATUS_EVENT nằm ngoài lõi Paper 2" (d.177, K7; d.287 "Máy trạng thái hành động… ngoài phạm vi"); R11–R12 "hỗ trợ, ngoài lõi" (d.515). F2: "Action_Status… không là đối tượng kiểm chứng của bài" (d.288). F3: "Không làm logic 4 mức hành động" (d.164). F5: Status_Event còn là quyết định treo (d.237) | G-B (bằng chứng → hành động có trách nhiệm: sự kiện chuyển trạng thái có căn cứ, vai trò, xác minh sau sửa chữa) là khoảng trống **chính**; ACTION và STATUS_EVENT là thực thể lõi; ràng buộc C6 (bước chuyển có căn cứ & đúng vai trò), C9 | **Cao** (loại bỏ đúng phần lõi G-B/ĐG3) |
| **Công cụ** | F1: SHACL/RDF/SPARQL làm đường C của Gate 3 (d.547), R01–R17 trong `.ttl` khóa (d.481, 638), "SHACL R01–R17" (d.579), "công bố .ttl… namespace w3id" (d.643), "Chuyển registry CSV sang RDF" (d.547). F2: "Bộ kiểm tra dữ liệu (SHACL kết hợp truy vấn)" (d.333); RDF/SHACL/SPARQL trong Phụ lục A.4 (d.518–520), B7, C7–C8. F4/F5: "SHACL là cơ chế kiểm chứng chính (D1)" (F4 d.139; F5 d.162). F3 gọi SQLite/SHACL là Supporting (d.133) | Python, IfcOpenShell, SQLite/JSON. KHÔNG RDF/SHACL/SPARQL/ontology (SOSA/SSN, PROV-O chỉ 1 bảng) | **Cao** (F1, F2, F4, F5); F3 **Trung bình** (SHACL chỉ ở vai trò công cụ hỗ trợ, nhưng vẫn nêu) |
| **Tham chiếu chuẩn ngữ nghĩa** | F1 d.408: "SOSA/SSN… PROV-O và PAV… IDS… SHACL"; F2 d.283 cùng; F2 A.4 giải thích RDF/SPARQL | SOSA/SSN, PROV-O chỉ ánh xạ 1 bảng; không ontology | **Trung bình** (nêu là "tái dùng chuẩn, không phải đóng góp", nhưng ánh xạ ở cấp trường, R-luật và `.ttl`) |
| **Số CQ** | F1: 12 CQ làm sổ làm việc + ánh xạ 5 CQ master lock (d.487–504); F2: "Bộ làm việc gồm 12 câu ở ba nhóm" (d.254); slide: "CQ01–CQ12 khóa SHA-256" (F4 d.145; F5 d.170) | CQ01–CQ12 → lọc về **3 câu hỏi truy ngược người quản lý** | **Cao** (12 CQ vẫn là đơn vị thiết kế/khóa; chỉ có phần nhóm "ngược" tương ứng; 3 câu truy ngược không xuất hiện như tên gọi) |
| **Số ràng buộc** | F1: R01–R15 + R16/R17, nhiều hậu tố (d.509–518); slide: "15 nhóm quy tắc SHACL" (F5 d.198) | Luật R01–R17 → lọc về **5 ràng buộc**: C1 (không mồ côi), C3 (thời điểm đo trong hiệu lực ánh xạ), C5 (dùng ngoài phạm vi phải có lý do), C6 (bước chuyển có căn cứ & đúng vai trò), C9 (căn cứ còn hiệu lực tại thời điểm chuyển) | **Cao** (chưa lọc; có R02/R05/R10 ~ C1; R03/R04 ~ C3; R07–R09, R16–R17 ~ C5; R11–R12 ~ C6 nhưng bị gạt ngoài lõi; R05c/R13 ~ C9). Va chạm mã: "C1–C3" của F1/F2 là đóng góp, không phải ràng buộc |
| **Chỉ số** | F1: "Ba chỉ số" M1 (phát hiện liên kết sai theo loại lỗi + dương tính giả) – M2 (tỷ lệ bản ghi đủ 6 trường) – M3 (thời gian truy ngược CQ05) (d.608–614); F2: M0–M3, M2 = "đầy đủ và phù hợp" (d.268–275); slide: M1–M3 (F5 d.175–180) | M1 = đủ thuộc tính (chỉ mô tả); **M2 = chỉ số chính** (tỉ lệ lỗi chèn mù bị bắt, theo nhóm); M3 = truy ngược 3 câu hỏi người quản lý; M4 = phút/bản ghi | **Cao** về tên/định nghĩa: M1 của tệp ≈ M2 của khóa; M2 của tệp ≈ M1 của khóa; M3 của tệp (thời gian CQ05) ≈ M4 một phần; **không có M4**; M3 của khóa (truy ngược 3 câu) không xuất hiện; F2 thêm M0 |
| **Đối chứng B0/B1** | F1/F2 không có đối chứng nào ngoài "tra cứu thủ công qua thư mục dữ liệu, Revit và biểu mẫu" để so M3 (F1 d.614; F2 d.275; F5 d.180). "Đường cơ sở" của M1 ghi "–" (F1 d.612). Bellon 2025 xuất hiện chỉ như đối thủ/nguồn đọc thêm, "chỉ đọc tóm tắt" (F1 d.238; F2 d.210) | B0 = mã hóa tay 20–30 hồ sơ kiểm định VN; B1 = IFC 4.3 theo Bellon 2025 [35] + BCF 3.0, chưa có tầng bằng chứng & trách nhiệm (cùng script, tắt C5, C6, C9) | **Cao** (thiếu hoàn toàn cả B0 và B1; BCF 3.0 vắng; Bellon bị xem là "rủi ro tính mới", không là cơ sở dựng B1) |
| **Khoảng trống** | F1: GAP-A (chuỗi Sensor→…→Inspection liên kết chéo), GAP-B (phạm vi hiệu lực + bản ghi trách nhiệm), GAP-C (kiểm chứng xác định xuyên chuỗi) (d.246–250). F2: ba yêu cầu đồng thời (d.222). F3/F4/F5: Gap 2A nguồn gốc, 2B phạm vi hiệu lực, 2C định danh; "2B là lớp duy nhất chưa thấy tiền lệ trực tiếp" (F4 d.67; F5 d.75) | G-B chính; G-A vế A2 (phạm vi hiệu lực là trường bắt buộc, kiểm tại lần dùng) là phụ. GAP1→G-B, GAP2→A2, GAP3 (kiểm chứng xác định) KHÔNG còn là khoảng trống mà là thiết kế đánh giá | **Cao**: F1 coi GAP-C (kiểm chứng) là khoảng trống/đóng góp C3; F3/F4/F5 coi **A2 (2B) là lớp trung tâm** và bỏ G-B (hành động có trách nhiệm); khung 2A–2C không tương ứng GAP1/2/3 của bản cũ |
| **RQ** | F1: RQ2 + RQ2.1 (định danh/C1), RQ2.2 (thuộc tính bắt buộc và bảo toàn/C2), RQ2.3 (giao thức phát hiện + thời gian/C3) (d.264–268). F3–F5: RQ2-P2 + SRQ2.1 (yêu cầu) / SRQ2.2 (định danh) / SRQ2.3 (toàn vẹn) | RQ2: trên cùng BIM nhà xưởng, so B0 và B1, mô hình đề xuất bắt được tỉ lệ nào lỗi chèn mù theo nhóm (M2 chính). RQ2.1 định danh (C1,C3); RQ2.2 phạm vi (C5,C9); RQ2.3 chuyển trạng thái (C6) | **Cao**: tên RQ2.1–2.3 trùng, nhưng nội dung khác (khóa: theo nhóm ràng buộc; tệp: theo ba đóng góp). RQ2.3 khóa là chuyển trạng thái; RQ2.3 F1 là giao thức phát hiện. Khung SRQ của F3–F5 khác hẳn |
| **Đóng góp** | F1/F2: C1 (khung truy vết cấp cấu kiện có thể kiểm chứng), C2 (quản trị bằng chứng + hồ sơ có trách nhiệm), C3 (giao thức kiểm chứng xác định) (F1 d.296–327). F3/F4/F5: một đóng góp trung tâm (mô hình truy vết với P/V/I bắt buộc + quy tắc thực thi + CQ/lỗi cài) | ĐG1 mô hình 6 thực thể mở rộng IFC4.3 + BCF3.0; ĐG2 hợp đồng bằng chứng + EVIDENCE_USE(within_scope, justification); ĐG3 STATUS_EVENT có căn cứ/vai trò/xác minh sau sửa + giao thức lỗi chèn mù | **Cao**: chỉ ĐG2 có đối ứng gần (Validity_Scope + EVIDENCE_USE + Scope_Snapshot + Acknowledged_By). ĐG1 (mở rộng IFC4.3+BCF3.0) và ĐG3 (STATUS_EVENT) không có. Va chạm mã C1–C3 |
| **Tạp chí đích** | F1 d.628: "Automation in Construction, Journal of Computing in Civil Engineering, ITcon… chưa được kiểm tra lại về phạm vi và định dạng". F2, F3, F4, F5: không nêu | Không có phạm vi riêng trong BRIEF (nguồn khóa: tiểu luận + GD3b) | **Thấp**/chưa đối chiếu được; ghi [CẦN KIỂM] |
| **Số lỗi chèn** | F1/F2: 9 loại; ≥ 3 ca/loại (đề xuất) (F1 d.482); slide: 10 nhóm; 7 nhóm (tiểu luận); 16 ca đã chạy là kiểm thử đơn vị | ~30 lỗi chèn mù, người chèn ≠ người viết luật; **4 nhóm**: định danh–liên kết (C1,C3), phiên bản (C9), dùng ngoài phạm vi (C5,C9), chuyển trạng thái không căn cứ (C6) | **Trung bình**: nguyên tắc "bên độc lập lập ca lỗi, niêm phong SHA-256" khớp (Khớp); số nhóm lệch (9/10/7 vs 4); nhóm "chuyển trạng thái không căn cứ" chỉ có một phần (N10 đóng hồ sơ sai) vì R11–R12 bị gạt |
| **BIM 1:1 và tương ứng thông tin** | F1/F2: Physical_Identity = FALSE, "tương ứng thông tin", không dùng đồng nhất vật lý (F1 d.363–369, 420; F2 d.307–315). F1: "Không tồn tại [đồng nhất vật lý] giữa mẫu 1:10 và công trình" (d.365) | BIM 1:1 = nhà xưởng thật mà khung 1:10 mô phỏng; nối chỉ qua tương ứng thông tin (Physical_Identity = FALSE) | **Khớp** (và có thêm thiết kế Sổ tương ứng, R16/R17) |
| **Kết quả 16/16 ngày 23/09** | "chỉ là kiểm thử đơn vị" (F1 d.176, 602, 641; F2 d.511, 679; F4 d.158; F5 d.182) | 16/16 chỉ là kiểm thử đơn vị | **Khớp** |
| **8 cặp GUID trùng** | Revit: trùng "đã xác nhận" ("ca lỗi thật", F1 d.221); IFC xuất: 0 trùng; 573442 "bị phát hiện lệch" (F1 d.175; F5 d.52, 204). Slide: "Phần tử 573442 bị phát hiện lệch GUID… nối theo Revit sẽ gắn nhầm" (F5 d.52–53) | 8 cặp GUID trùng chỉ là NGHI NGỜ | **Trung bình**: F1 d.175 đã nêu nguồn cũ (SUSPECTED) và nguồn mới (đối chiếu IFC xuất thật 23/09), chọn mới; F2 d.362 vẫn giữ giới hạn ("không đồng nhất… xung đột đã chứng minh trong IFC"); slide nói như sự kiện. Trạng thái verified/rejected của người: 0 dòng (decision_history) |
| **Nguồn cho 6 IFC / 3.356 / 10.328 / 718 / 676** | Nguồn tệp: báo cáo tiến độ 23/09; slide tự ghi "chưa xác minh trong repository" | Cần nguồn | Xem mục 2.5 – **Trung bình** |
| **Khóa định danh Model_Version_ID, Binding_ID, Prototype_Component_ID** | F1/F2 dùng như đã quyết (D2) (F1 d.302, 673); F3 d.84: "chỉ được dùng khi đã có quyết định/ADR"; F4/F5 đưa vào kiến nghị cần GVHD quyết (F5 d.237) | Phạm vi khóa dùng COMPONENT + SENSOR_MAPPING; không nêu ba khóa này | **Trung bình** (không mâu thuẫn trực tiếp, nhưng nội bộ nhóm bất nhất về việc đã chốt chưa) |
| **Vai trò Bellon 2025** | "Rủi ro tính mới chưa đóng… chỉ đọc tóm tắt" (F1 d.238, 694; F2 d.210, 645) | B1 = IFC 4.3 theo Bellon 2025 [35] + BCF 3.0 | **Trung bình**: chưa đọc toàn văn nhưng khóa đã dựa vào Bellon; F5 d.216 vẫn xếp "đọc toàn văn Bellon 2025" vào Bước 1 |
| **"Chưa ai nghiên cứu" / "đầu tiên"** | F1 d.254, F2 d.222, F3 d.150 đều cấm dùng; F5 d.57 nêu phạm vi tìm kiếm | Quy tắc dự án 3: viết theo phạm vi tìm kiếm | **Khớp** (F4 d.67: "chưa thấy tiền lệ trực tiếp (12 bài toàn văn + 3 novelty check)" cũng nêu phạm vi) |
| **Phạm vi Gate Paper 2** | F4 d.200; F5 d.238: "G2–G3 hay thêm G6" | – | Ghi nhận mâu thuẫn trong hồ sơ điều hành (REFINED C-01); không đối chiếu được với khóa |

---

## 5. Tài sản đáng giữ (cho Pha 1) và thứ nên bỏ

### 5.1 Nên giữ

| Tài sản | Ở đâu | Vì sao giữ (đối chiếu phạm vi khóa) |
|---|---|---|
| **Nguyên tắc lập ca lỗi độc lập**: người thứ hai lập ca lỗi và đáp án sau khi luật khóa; manifest niêm phong SHA-256; báo cả ca bỏ sót và dương tính giả; tách ca thật (RD-001…008) và ca tổng hợp | F1 d.559–562, 602–606; F2 d.256–258, Hình 4 | Trùng nguyên tắc "người chèn ≠ người viết luật" của khóa; tách "kiểm thử đơn vị 16/16" khỏi bằng chứng |
| **Sổ tương ứng 1:10 → 1:1** (Physical_Identity = FALSE), ba phương án A/B/C, quy trình 8 bước, Link_Basis theo nhãn trạng thái, R16/R17; lưu cả nhãn dự đoán và nhãn đúng | F1 d.359–404, 420, 431; F2 d.307–315 | Khớp "BIM 1:1 = nhà xưởng thật… nối chỉ qua tương ứng thông tin" |
| **Hợp đồng bằng chứng**: Validity_Scope từ vựng đóng (4 giá trị), điều kiện giao thức ↔ giá trị, Scope_Snapshot, Acknowledged_By, EVIDENCE_USE, "phiên bản mô hình ≠ phạm vi hiệu lực" | F1 d.313, 424, 426, 429; F2 d.317–325 | Đối ứng gần nhất với ĐG2 và C5 (dùng ngoài phạm vi phải có lý do) |
| **Bốn nguyên tắc quản trị**: định danh tất định từ nội dung, không sửa đè (Superseded_By); máy chỉ ghi tối đa candidate, người ghi verified/rejected/closed; phạm vi thuộc bằng chứng, phiên bản thuộc binding; quan sát tách diễn giải | F1 d.429; F2 d.290, 329 | Hữu ích cho C1/C6/C9 và cho ACTION/STATUS_EVENT (vai trò, căn cứ) |
| **Ví dụ xuyên suốt REC0004** với 7 mắt xích, trạng thái từng mắt xích và cờ provenance (thay thế, dấu thời gian tổng hợp, ba mục chưa xác minh của Paper 1) | F1 d.433–453; F2 d.366 | Ví dụ dữ liệu thật hiếm, có cờ MISSING thay vì bịa; nhưng cần Gate 1 hoặc ngoại lệ bằng văn bản mới dùng ngoài mức CANDIDATE |
| **Bảng K1–K11 và F.2** (mâu thuẫn nguồn đã nhận diện), cùng quy tắc ưu tiên nguồn (F2 d.658) | F1 d.165–181; F2 d.658–679 | Lịch sử mâu thuẫn dùng để dò "mã treo"; K4 (718/676/596) vẫn mở |
| **Hai tầng xác nhận / hai loại đúng đắn**: toàn vẹn quan hệ dữ liệu (luật kiểm được) và tính đúng vị trí lắp đặt (chỉ hồ sơ lắp đặt xác nhận) | F1 d.284; F2 d.248–250; F5 d.125 | Giới hạn tuyên bố rõ; phù hợp tinh thần khóa |
| **Bảng "Claim → Evidence → Limitation → Next action"** và Bảng Q.1 (5 câu trả lời ngắn, điều kiện mở Gate 3) | F1 d.705–730 | Dùng làm khung kiểm soát tuyên bố |
| **Bảng "điều kiện claim – bằng chứng hiện có – còn thiếu – kết luận" (4 hàng đều "Chưa đủ")** | F4 d.175–180; F5 d.201–206 | Thẳng thắn về mức bằng chứng; nên giữ nguyên tinh thần |
| **Scope firewall** và danh sách "Không claim" | F3 d.152–166; F5 d.94–95 | Khớp quy tắc dự án (không chẩn đoán, không RUL, không FEM hiệu chuẩn) |
| **Mức đọc từng nguồn** (toàn văn/tóm tắt/siêu dữ liệu) và danh sách đọc A1/A2 có DOI | F2 d.639–654, 681–693; F1 d.688–703 | Cần cho quy tắc "[CHƯA ĐỌC TOÀN VĂN]". **DOI chưa được kiểm trong lượt này** (ngoài phạm vi kiểm kê) |
| **Phụ lục D CDE tối thiểu** (D.1: Model_Version_ID, hash IFC, trạng thái vùng chứa, người phát hành, thay thế; D.2: bắt buộc vs không cần) | F2 d.591–616 | Hữu ích cho C9 (căn cứ còn hiệu lực theo phiên bản) khi bỏ ontology |
| **Dữ kiện thật dẫn được kèm nguồn thứ cấp** (6 IFC, 3.356, 10.328, 676/596, 573442, pilot 524067/552993) | mục 2.2 | Chỉ dùng kèm nguồn và nhãn [BC] |
| **Thuật ngữ** (Phụ lục A.1–A.4) và **bài nói 90 giây + prompt tutor** (F3) | F2 d.468–528; F3 d.200–250 | Chỉ để học; không là nguồn |

### 5.2 Nên bỏ hoặc tách khỏi khung chính

| Thứ nên bỏ/gạt | Vì sao |
|---|---|
| Toàn bộ phần **RDF/SHACL/SPARQL/`.ttl`/namespace w3id** làm công cụ trung tâm (F1 d.481, 547, 578–599, 638, 643; F2 d.333, 386, 518–520, 544, 587) | Mâu thuẫn trực tiếp công cụ đã khóa (Python, IfcOpenShell, SQLite/JSON) |
| **Sổ 12 CQ** (và 5 CQ) làm đơn vị khóa SHA-256 | Khóa: lọc về 3 câu hỏi truy ngược |
| **R01–R17** nguyên danh mục | Khóa: lọc về 5 ràng buộc C1, C3, C5, C6, C9. Có thể dùng làm kho đối chiếu để lọc |
| **Mô hình 10(+1) thực thể** và bộ 10 bảng CSV | Khóa: 6 thực thể; cần bảng ánh xạ 10→6, không dùng song song |
| **Ba đóng góp C1–C3**, **GAP-A/B/C**, **Gap 2A–2C**, **P/V/I** như khung chính | Khóa dùng ĐG1–ĐG3 và G-B chính, G-A vế A2 phụ |
| **Ba/bốn chỉ số M0–M3** như đặt tên hiện tại | Khóa dùng M1–M4 với nghĩa khác (M2 chính) |
| **9 loại / 10 nhóm / 7 nhóm lỗi** | Khóa: ~30 lỗi, 4 nhóm |
| **Danh sách tạp chí** (F1 d.628) | Chưa kiểm phạm vi/định dạng; không dùng làm cơ sở |
| **Kiến trúc MCP/Bridge/Dynamo/Write-Tools** như một phần luận chứng | Chỉ là phương tiện (cả F1 d.718, F3 d.133 đều nói vậy); nếu có thì chỉ ở Methods |
| **Máy trạng thái hành động 9 trạng thái (D3)** như hạng mục ngoài lõi | Khóa coi STATUS_EVENT/ACTION là lõi (G-B); thiết kế D3 có thể là tài sản để dựng lại ở dạng STATUS_EVENT, không bỏ hẳn |
| **Mã `[ĐỀ XUẤT]/[GIẢ THUYẾT]`, nhãn "D1"** trong slide | Nhãn "D1" dễ nhầm D001; "D1" cũng mâu thuẫn khóa |

---

## 6. Ghi chú bất thường

**A. Tham chiếu tới tệp/nguồn không có trong thư mục `/txt/` (đối chiếu danh sách thư mục)**
1. `gate2_3_shapes_draft_v0.1.ttl` (F1 d.481; nguồn của R01–R15) – không có (chỉ có `gate2_3_data_model_v0.2.md`, mục A.4 d.231 cũng trỏ đến tệp này).
2. `CURRENT_STATUS_AND_NEXT_DIRECTION.md` v2.4, `EVIDENCE_GATES_v2.1.md` v2.4, `G1_G2_INTERFACE_DECISION_REGISTER.csv` (01_CURRENT_CONTROL) (F1 d.150) – không có. Tên "EVIDENCE_GATES_v2.1.md" kèm "v2.4" là bất thường (tên tệp ghi 2.1, phiên bản ghi 2.4).
3. `HO_CHI_HAN_TIEU_LUAN_TONG_QUAN_23092026_HOANTHIEN.docx` (tiểu luận) và `PAPER1_v8_SHM_SUBMISSION.docx` (F1 d.152–153) – không có trong thư mục (đúng với việc tiểu luận/Paper 1 nằm ngoài 05_PAPER_2).
4. `D:/01_RESEARCH/08_Output_07.09/` (index.csv, manifest.json, NPZ, recording_predictions.csv) và `signal-loro-ml-v1.zip` (F1 d.158, 356) – dữ liệu gốc của REC0004; không có.
5. Hình `media/image1.png … image7.png` trong F1 (7 hình) và `image1…6.png` trong F2 (6 hình) – ảnh không nằm trong bản text; không kiểm được nội dung hình (chú thích alt có đọc được, ví dụ F1 d.371, 410, 437, 549, 604).
6. Slide F4 d.187, F5 d.216 nhắc "**García 2026b**" nhưng danh mục F1/F2 chỉ có một García et al. (2026). Chưa rõ có bài thứ hai hay là cách gọi nội bộ → [CẦN KIỂM].
7. F3 d.188–192 hướng dẫn "Upload thêm tài liệu Paper 2 gốc 25/09/2026 và Charter/Current Status" – tệp gốc 25/09 (`PAPER2_REFINED_DIRECTION…v1.0.25092026`) có trong thư mục nhưng thuộc nhóm khác; Charter/Current Status không có.

**B. Mâu thuẫn nội bộ và giữa các tệp trong nhóm**
1. **Số tiêu chí đóng Gate 2**: 12 (F1 Bảng 15.1), 11 (F2 Bảng B.2), "0/10 tiêu chí (master lock)" (F1 d.483; F4 d.180; F5 d.206). F1 tự mâu thuẫn trong một tệp.
2. **Số thực thể**: F1 viết "7 thực thể của v0.2 + 1" (d.408), nhưng bảng ngay sau liệt kê 10 hàng, trong đó một hàng gộp hai thực thể; T2.1 nói "10 thực thể"; F2 nói "sáu nhóm" ở thân bài và "mười + 1" ở phụ lục.
3. **K4 (718/16 vs 676/596)**: nhãn ngày không phân biệt được hai audit. F1 d.174 gán 718/16 cho "audit trước 15/09" và 676/596 cho "audit 13/09", F2 d.183 gán 8 cặp cho "audit ngày 13/09"; 13/09 cũng là "trước 15/09". Hai tệp F1/F2 đều để mở; slide vẫn xin GVHD thống nhất.
4. **Số loại lỗi**: 9 (F1/F2), 7 nhóm (tiểu luận), **10 nhóm** (F4 d.149, F5 d.174). F5 liệt kê tên "thiếu Sensor_ID, sai BIM_GUID, binding trùng, ánh xạ hết hạn, CE mồ côi, lệch phiên bản, truy ngược đứt, dẫn ngoài phạm vi…" khác danh sách 9 loại của F2 d.372 (có "thiếu hoặc sai GlobalId", "tham chiếu sai phiên bản", "liên kết xung đột", "thiếu đích"; F5 có "thiếu Sensor_ID", "truy ngược đứt" mà F2 không có).
5. **Trạng thái binding**: 4 (F1 d.475; F2 d.290), 5 (F4/F5: có UNBOUND, SUPERSEDED), 6 (F1 d.421: có NOT_ASSESSED, SUSPECTED_IDENTITY_ANOMALY, BLOCKED).
6. **Định nghĩa M2**: F1 = đủ 6 trường; F2 = đủ **và phù hợp ngữ cảnh**; slide = "đủ nguồn gốc". Cùng tên, ba nghĩa.
7. **D2 (neo kép) chốt hay chưa**: F1 d.302, 673 xem là quyết định D2; F3 d.84 và F5 d.220, 237 xem là cần ADR/quyết định bằng văn bản.
8. **"E1/E2/E2b"** (F1 d.400, 578) dùng không định nghĩa trong cả F1 lẫn F2.
9. **Trạng thái kiểm thử Gate 3 trước khi mở**: F1 d.176 và d.602 xếp 16/16 là kiểm thử đơn vị nhưng F1 d.729–730 vẫn đưa vào tiêu chí điều kiện "(4) compare_with_ifc_binding chạy lại được…" – không mâu thuẫn, ghi cho rõ.
10. **F2 d.183 `[CẦN BỔ SUNG]`** nêu "audit 13/09 là 676/596" và "audit trước 15/09 là 718/16", trong khi F2 d.362 ở Case study mô tả "8 cặp tham số IfcGUID trùng trong Revit (16 phần tử)" mà không nêu audit nào – hai đoạn dùng hai cách ghi.
11. **Tên bản Paper 1**: "PAPER1_v8_SHM_SUBMISSION" vs "v8.1 SCIENCE LOCKED" (F1 d.180, K10). F2 bỏ K10 nhưng vẫn tham chiếu Ho et al. (2026) là "bản thảo của nhóm".

**C. Khác biệt trong quy trình tạo tài liệu**
1. F1 d.161 nói Perplexity lỗi 401 và "Consensus MCP không được dùng", F2 Bảng F.1 (d.660) lại dựa trên tìm kiếm Consensus ngày 24/09 → F2 viết sau F1 (bằng chứng thứ tự, mục 1b).
2. Cả F1 và F2 đều đề "24/09/2026" mà không ghi giờ; mối quan hệ "F2 sau F1 ~9 phút" chỉ đến từ metadata ngoài; trong tệp text không kiểm được.
3. F3 không có ngày trong thân; chỉ có "Biên tập từ tài liệu định hướng Paper 2 ngày 25/09/2026" (d.6). F4 không ghi ngày trên slide; F5 ghi "27/09/2026" ở slide 1 nhưng chân trang "09/2026".
4. F3 d.82: chuỗi "Sensor_ID → BIM_GUID → Condition_Evidence_ID → Inspection_Record_ID → Action_Status" gọi là "canonical, không được tự ý thay đổi" (d.84) và coi Model_Version_ID/Binding_ID/Prototype_Component_ID/Status_Event_ID/Action_Record_ID là "chỉ dùng khi đã có quyết định/ADR". F1/F2 dùng Model_Version_ID, Binding_ID, Prototype_Component_ID thường xuyên và định nghĩa quy tắc sinh. Bất nhất về mức "canonical".
5. F3 d.141 ghi "novelty chung mới ở mức moderate và có điều kiện"; F5 d.75 ghi "Gap 2 giữ mức NARROW_BUT_DEFENSIBLE"; F1/F2 không dùng nhãn này. Không mâu thuẫn rõ nhưng là hai thang nhãn.

**D. Trích dẫn/DOI đáng ngờ hoặc chưa kiểm**
- Tôi **không kiểm DOI** (ngoài phạm vi kiểm kê và không dùng công cụ tra cứu). F1 d.734 ghi DOI "lấy từ Zotero, OpenAlex hoặc danh mục đã kiểm tra của tiểu luận (23/09/2026)"; F2 Bảng F.3 ghi mức đọc từng nguồn. Quy tắc dự án 2/4: chưa thể coi các DOI này là đã kiểm trong hồ sơ của tôi.
- Nguồn nhận cảnh báo chính thức ngay trong tệp: Bellon 2025 (tóm tắt), Hamledari 2018 (tóm tắt), Aydın 2025 (tóm tắt), Mitchell 2019 (chỉ siêu dữ liệu) (F2 d.689–690), Faqih & Zayed và Sagarna đọc 24/09 (F2 d.687).
- Một số nguồn là bài 2026 (Borkowski, García, Piras: Applied Sciences 16(10) 4642) – cần kiểm DOI/đường dẫn trước khi trích (quy tắc 2).
- Cách viết "Çelik 2023" (F4 d.52; F5 d.62) khác "Celik" ở danh mục F1 (d.742).
- Hai nguồn là diễn đàn/blog kỹ thuật (Velez 2021, SourceForge; Tammik 2022, blog Autodesk) là căn cứ cho hành vi exporter bỏ qua IfcGUID trùng (F1 d.221; F2 d.183): mức nguồn thấp, cần kiểm tại thời điểm viết bài.

**E. Khác**
- F2 là tài liệu duy nhất dùng dấu `[CẦN BỔ SUNG: …]` (40 chỗ); các chỗ này là danh sách việc thiếu sẵn có, hữu ích cho Pha 1 (38 dòng chứa dấu thực chất, d.154, 158, 183, 210, 246, 254, 258, 309, 329, 358, 362 [2 dấu], 366, 368, 372, 386, 394, 398, 402, 406, 414, 426, 434, 438, 481, 493, 524, 545, 581, 589, 593, 601, 603–607, 664, 666; d.27 chỉ là câu mô tả quy ước; tổng 40 lần xuất hiện của cụm kể cả d.27 và 2 dấu ở d.362).
- F1 d.252–254: một bảng 1 ô chứa "Ranh giới diễn đạt…" (chuyển đổi từ khung/callout của docx), không phải bảng dữ liệu.
- F3 d.242 yêu cầu NotebookLM dùng ví dụ "S-07, C-12, INS-001": mã minh họa hư cấu, không thuộc dữ liệu thực (cần không nhầm với ID thật).
- F3 không chứa số liệu thực nghiệm nào; mọi số liệu trong nhóm (mục 2) đến từ F1, F2, F4, F5.

---

## 7. Chuỗi phiên bản

Quy ước: các hàng "bối cảnh" là tệp ngoài nhóm B1, tôi chỉ nêu vì chính F1/F2/F3 tham chiếu chúng (F1 d.150–159) hoặc nằm cạnh nhóm; **tôi chưa đọc chúng trong lượt này**, nên cột "đổi gì" của các hàng đó chỉ lấy theo lời F1.

| # | Tệp | Ngày | Vai trò trong chuỗi | Đổi gì so với bản trước (theo nội dung đã đọc) |
|---|---|---|---|---|
| 0a | (bối cảnh) master lock `PAPER2_GATE2_GATE3_MASTER_EXECUTION_LOCK_20260915` + `BAO_CAO_TONG_HOP…20260915` | 15/09 | Nguồn điều hành Paper 2 (F1 d.151) | Khóa GAP 1–3, C1–C3, 5 CQ (CQ-1…5), 9 loại lỗi, artefact Gate 2, phép thử Gate 3 (theo F1 d.151, 171–173) |
| 0b | (bối cảnh) `GATE2_GATE3_GIAI_THICH…20260916` (+ v2) | 16/09 | Bản giải thích; nguồn danh sách tạp chí (F1 d.628) | – |
| 0c | (bối cảnh) tiểu luận tổng quan 23/09, `gate2_3_data_model_v0.2`, `GATE2_3_PROGRESS_20260923` | 23/09 | Nguồn lý luận (bốn điểm Đóng góp 2, 7 nhóm lỗi, ba chỉ số, hai loại đúng đắn) và nguồn kỹ thuật (6 IFC, 3.356, 10.328, 8 cặp, 16/16) | Lần đối chiếu Revit–IFC 23/09 làm đổi trạng thái 8 cặp GUID từ SUSPECTED sang đã đối chiếu IFC (F1 d.175) |
| 0d | (bối cảnh) `DE_XUAT_PAPER2…20260924`, `OUTLINE_PAPER2_20260924` | 24/09 | Đề xuất và outline trước đó; F1 d.156, 626 nhắc "phương án tên bài đã có (outline 24/09)" | Bảng tiền lệ; dùng bốn điểm Đóng góp 2 (F1 d.171) |
| **1** | **F1** `PAPER2_BAO_CAO_DINH_HUONG_OUTLINE_VA_KE_HOACH_THUC_THI_GATE2_GATE3` | 24/09 (tối) | **Báo cáo lớn đầu tiên của nhóm** | Hợp nhất các nguồn 0a–0d; **đưa ra 11 mâu thuẫn K1–K11**; **thêm CORRESPONDENCE** (sổ tương ứng 1:10→1:1), Link_Basis = state_label_location, R16/R17, Placement_Context/Inspection_Context (đều [ĐỀ XUẤT]); đổi C1–C3 chính thức làm khung (ánh xạ bốn điểm Đóng góp 2 sang C1–C3); GAP-A/B/C; 12 CQ làm sổ làm việc; bảng phép thử G3-P/N; kế hoạch 18 việc. Không có `[CẦN BỔ SUNG]`; dùng hệ nhãn `[ĐÃ CÓ]/[CANDIDATE]/[DỰ KIẾN]/[ĐỀ XUẤT]/[GIẢ THUYẾT]`; không dùng Consensus |
| **2** | **F2** `PAPER2_COMPLETE_ACADEMIC_OUTLINE_AND_EXECUTION_GUIDE` | 24/09 (tối, ~9 phút sau F1) | **Bản tái cấu trúc F1** thành outline bài báo + phụ lục; **bản mới nhất của dòng "C1–C3 / RDF-SHACL"** | **Chia Phần I (outline 9 mục, abstract nháp) / Phần II (6 phụ lục)**; bỏ hệ nhãn và mã D/K; thêm 40 `[CẦN BỔ SUNG]`; **thêm 11 nguồn mới** (Fang, Faqih & Zayed, Sagarna, Hamledari, Stolk & McGlinn, Aydın, Makhoul, Kamariotis, Tammik, buildingSMART, Cyganiak/Harris) qua Consensus 24/09 và bỏ 8 nguồn của F1; **thêm M0** (4 chỉ số) và đổi M2; thêm "hai tầng xác nhận"; thêm Phụ lục D (CDE), F (mức đọc nguồn); rút Gate 2 xuống 11 tiêu chí, kế hoạch xuống 14 nhiệm vụ; bỏ danh sách tạp chí; bỏ bảng phép thử G3-P/N, bảng REC0004 từng mắt xích, K9–K11 (chỉ còn lược) |
| 3a | (bối cảnh) `PAPER2_REFINED_DIRECTION_PROVENANCE_VALIDITY_IDENTITY_v1.0.25092026` | 25/09 | **Điểm xoay khái niệm**: F3 d.6 xác nhận F3 "biên tập từ tài liệu định hướng Paper 2 ngày 25/09/2026"; từ vựng của F3–F5 (Gap 2A–2C, P/V/I, SRQ2.1–2.3, V2.1–V2.3, RQ2-P2) khớp với tệp này (tôi chỉ đọc đầu tệp để xác nhận từ vựng) | Tệp tự nhận "tinh chỉnh trục trung tâm… hợp nhất ba khoảng trống của Master Execution Lock 15/09/2026" (mục Tóm tắt điều hành của chính tệp đó); không đọc hết, không kết luận chi tiết |
| **3** | **F3** `PAPER2_NOTEBOOKLM_HUONG_DAN_HOC_VA_AUDIO_OVERVIEW_25092026` | 25/09 | Bản học/Audio dẫn xuất từ 3a | **Đổi khung**: bỏ C1–C3 và GAP-A/B/C, thay bằng P/V/I, Gap 2A–2C, RQ2-P2 + SRQ2.1–2.3, V2.1–V2.3; hạ SHACL xuống "Supporting" (d.133); hạ Model_Version_ID/Binding_ID/Prototype_Component_ID xuống "chỉ khi có ADR" (d.84); bỏ mọi số liệu thực nghiệm; nêu novelty "moderate" (d.141); nhấn "Gate 2 OPEN, Gate 3 chưa mở" |
| **4** | **F4** `ChuyenDe2_Paper2_DUT` (pptx) | 27/09 | Slide báo cáo Chuyên đề 2 dạng Hội đồng | Biến khung 25/09 (2A–2C, P/V/I, V2.x) thành 10 slide; **quay lại dùng số liệu và kỹ thuật của F1/F2 (23–24/09)**: 6 IFC, 3.356, 10.328, 8 cặp, 15 nhóm SHACL, 12 CQ, 5 trạng thái binding, "D1: SHACL là cơ chế kiểm chứng chính", "10 nhóm lỗi"; thêm mục lục, tên hai người hướng dẫn, câu hỏi góp ý cho Hội đồng về 2A–2C |
| **5** | **F5** `ChuyenDe2_Paper2_Traceability` (pptx) | 27/09 | **Bản trình người hướng dẫn mới nhất của nhóm (nội dung đầy đủ nhất)** | Giữ khung F4, **bổ sung**: phạm vi tìm kiếm và nhãn mức khoảng trống (NARROW_BUT_DEFENSIBLE), White 2025, tiêu đề tiếng Anh, bảng RQ/WP/Chương/Gate, slide "Vấn đề" riêng, 10 nhóm lỗi liệt kê đầy đủ, "R07–R09 nháp", ADR có Valid_From/To, kiến nghị thêm Status_Event, dòng "chưa được duyệt, không đóng Gate nào". Bỏ mục lục và câu hỏi góp ý riêng của F4 |

**Tóm tắt mạch thay đổi trong nhóm:**
1. **24/09 (F1 → F2)**: cùng khung C1–C3 + GAP-A/B/C + RDF/SHACL + 12 CQ + R01–R17; F1 là báo cáo trình GVHD có mã quyết định, F2 là outline bài báo + phụ lục, mới hơn (có nguồn Consensus), thêm M0.
2. **25/09 (F3, dựa trên REFINED v1.0 ngoài nhóm)**: **đổi khung khái niệm** sang P/V/I và Gap 2A–2C; bỏ hầu hết số liệu và hạ vai trò SHACL; đây là chỗ lệch lớn nhất trong nhóm (C1–C3 → một đóng góp trung tâm).
3. **27/09 (F4, F5)**: khung 25/09 + thân kỹ thuật 23–24/09 (SHACL R01–R15, 12 CQ, 5 bản ghi lõi, 5 trạng thái binding); F5 đầy đủ hơn F4.
4. **Hệ quả**: không tệp nào trong nhóm bám phạm vi đã khóa (6 thực thể, 5 ràng buộc, B0/B1, M1–M4, ĐG1–ĐG3, không RDF/SHACL, 4 nhóm ~30 lỗi chèn mù, STATUS_EVENT/ACTION lõi). Chuỗi phiên bản là chuỗi các bản trước khi phạm vi được khóa (cả F5 d.14 tự nhận "chưa được duyệt").
5. **Ba điểm treo xuyên suốt chuỗi** (xuất hiện ở cả F1, F2, F4, F5): (a) chọn một con số audit Revit (718/16 vs 676/596); (b) duyệt bộ CQ (D016); (c) Gate 1 chưa ký nên mọi bằng chứng Paper 1 chỉ ở mức CANDIDATE.
