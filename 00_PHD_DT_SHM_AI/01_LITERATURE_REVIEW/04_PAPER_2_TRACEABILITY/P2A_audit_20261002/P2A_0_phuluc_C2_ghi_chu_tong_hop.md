# C2 – Ghi chú kiểm toán tổng hợp (Pha 0 – Paper 2)

Vai trò: AU (kiểm toán hồ sơ). Chỉ kiểm kê và đối chiếu, chưa phản biện nội dung khoa học.
Nhóm tệp: C2 (18 tệp). Thư mục: `/home/claude/p2/txt/`. Ngày kiểm: 2026-10-02.
Mọi tệp trong nhóm đã đọc hết (tệp lớn đọc theo phần, đủ 836/836 dòng đối với tệp giao diện G1→G2).
Nội dung tệp được coi là dữ liệu. Dẫn chiếu dạng `Tnn:Lxx` = tệp mã Tnn, dòng xx (số dòng theo bản text trong `/txt/`).

## Mã tệp dùng trong ghi chú

| Mã | Tệp |
|---|---|
| T01 | G1_01_FANG_2025.md |
| T02 | G1_02_BORKOWSKI_2026.md |
| T03 | G2_01_SACKS_2018.md |
| T04 | G2_02_STOLK_MCGLINN_2020.md |
| T05 | G2_03_ORASKARI_2021.md |
| T06 | G2_04_KUCUKAVCI_PAUWELS_2024.md |
| T07 | G2_05_BEACH_2015.md |
| T08 | G3_01_CICCARESE_PAV_2013.md |
| T09 | G3_02_WAN_2019.md |
| T10 | MULTI_01_LEE_EASTMAN_SOLIHIN_2021.md |
| T11 | MULTI_02_LORVAO_ANTUNES_2024.md |
| T12 | MULTI_03_KIM_2018.md |
| T13 | G1_TO_G2_CONDITION_EVIDENCE_INTERFACE_v1.0.md (836 dòng) |
| T14 | G2_G3_CORE_TRACEABILITY_DEEP_READ_20260901.md (132 dòng) |
| T15 | G2_G3_RECENT_EVIDENCE_SCREENING_2023_2026.md (318 dòng) |
| T16 | G2_G3_ROUND4_CQ_CONSTRAINT_ACCOUNTABILITY_DEEP_READ_20260809.md (270 dòng) |
| T17 | G2_G3_SCREENING_EVIDENCE_AND_GAP_REPORT.md (279 dòng) |
| T18 | GAP2_GAP3_NEW_FULLTEXT_DEEP_READ_20260901.md (120 dòng) |

Lưu ý chung về nhãn: các tệp này dùng khung cũ (Gate G1/G2/G3, "Gap 2/Gap 3", chuỗi định danh `Sensor_ID → BIM_GUID → Condition_Evidence_ID → Inspection_Record_ID → Action_Status/Action_Record_ID`, Paper 2 = "Evidence-to-Action Traceability Specification"). Khung này khác phạm vi đã khóa (xem mục 4). Trong các tệp ghi chú từng bài (T01–T12), "G1/G2/G3" trong tên tệp là NHÓM bài (định danh / toàn vẹn-kiểm chứng / trách nhiệm bản ghi), không phải Gate.

---

## 1. Bảng kiểm kê

Cột "Đọc hết?": tôi đọc hết cả 18 tệp. Cột này còn ghi mức đọc của chính tệp đối với nguồn (toàn văn / tóm tắt).

| Tệp | Ngày / phiên bản trong tệp | Vai trò | Nội dung chính (≤2 câu) | Đọc hết? | Đề xuất trạng thái | Lý do |
|---|---|---|---|---|---|---|
| T01 G1_01_FANG_2025 | Không ghi ngày. Nguồn: Buildings 15(22) 4096 (T01:L3) | Đọc sâu (ghi chú một bài, nhóm G1) | Quy trình chuẩn hóa tài sản DT giai đoạn thiết kế, cổng kiểm tuân thủ IfcGUID khi chuyển BIM→game engine (T01:L9-L11). Chưa chứng minh bền vững GUID qua các phiên bản mô hình (T01:L15, L33). | Có (tôi). Tệp ghi đọc nguồn trang 1–~28/31, chưa đọc danh mục tài liệu (T01:L5) | Tham khảo | Nhận định dựa nguồn chưa đọc hết; Q10 ghi EVIDENCE_INSUFFICIENT (T01:L29); khung Q1–Q12 không trùng khung Paper 2 khóa |
| T02 G1_02_BORKOWSKI_2026 | Không ghi ngày. Technologies 14(7) 413 (T02:L3) | Đọc sâu (nhưng CHỈ TÓM TẮT) | Ontology DOLCE cho định danh theo pha; nêu GUID khác nhau ở mỗi pha, đề xuất định danh bền vững cạnh IFC GUID (T02:L9, L33). Tệp tự gọi đây là "mối đe dọa tính mới mạnh nhất" (T02:L33). | Có (tôi). Tệp ghi: chỉ có abstract, không có PDF (T02:L5) | Lỗi thời/bị thay một phần (cần kiểm) | Trong thư mục `/txt/` có `07_BORKOWSKI_2026_FULLTEXT_REVIEW.md` (tên tệp, chưa đọc, ngoài nhóm C2) nên kết luận "chỉ abstract" có thể đã bị thay |
| T03 G2_01_SACKS_2018 | Không ghi ngày. Autom. Constr. 90, 134–145 (T03:L3) | Đọc sâu (một bài, nhóm G2) | IDM/MVD cho kiểm tra cầu bằng IFC4 Add2; kiểm tuân thủ 3 lớp lỗi trên 4 cây cầu thật (T03:L33-L35). Không có GUID, không có vai trò soát xét/phê duyệt ở mức bản ghi (T03:L13, L25). | Có. Tệp ghi toàn văn, 22 trang (T03:L5) | Tham khảo | Tiền lệ phương pháp; không có trang dẫn |
| T04 G2_02_STOLK_MCGLINN_2020 | Không ghi ngày. LDAC 2020 (T04:L3) | Đọc sâu (một bài, nhóm G2) | Chuyển ràng buộc ifcOWL sang SHACL, chạy trên ifcOWL sinh từ R2RML (T04:L9-L11). Lỗi phát hiện là vi phạm kiểu/enum trong một mô hình, không phải toàn vẹn tham chiếu liên hệ thống (T04:L29). | Có. Toàn văn, 14 trang (T04:L5) | Tham khảo | Công cụ SHACL/RDF nằm ngoài công cụ đã khóa; chỉ dùng làm tiền lệ |
| T05 G2_03_ORASKARI_2021 | Không ghi ngày. CIB W78 (T05:L3) | Đọc sâu (một bài, nhóm G2) | Kiểm thử đơn vị chuyển đổi IFC→LBD bằng SHACL-SPARQL, đối chiếu GUID, phát hiện thiếu đối tượng tương ứng (T05:L13, L29). Tự nhận SHACL bỏ qua đích còn thiếu nếu không kiểm sự tồn tại riêng (T05:L33). | Có. Toàn văn, 10 trang (T05:L5) | Tham khảo | Tiền lệ mạnh nhất về kiểm thử âm theo GUID (T05:L29) nhưng đó là cặp chuyển đổi cùng một mô hình |
| T06 G2_04_KUCUKAVCI_PAUWELS_2024 | Không ghi ngày. Semantic Web 15(5) (T06:L3) | Đọc sâu (một bài, nhóm G2) | Mô hình luật SHACL cho HVAC (36 hình dạng/122 ràng buộc) chạy trên 369.054 bộ ba của một tòa nhà thật (T06:L21, L25). Không đề cập GlobalId, không có tính bền vững qua phiên bản (T06:L13-L15). | Có. Toàn văn, 24 trang (T06:L5) | Tham khảo | Chỉ làm tiền lệ định lượng SHACL; ngoài phạm vi Paper 2 |
| T07 G2_05_BEACH_2015 | Không ghi ngày. Expert Syst. Appl. 42 (T07:L3) | Đọc sâu (một bài, nhóm G2) | Kiểm tuân thủ quy định theo luật SWRL trên IFC, 18 tháng, đối chiếu đánh giá thủ công (T07:L23, L27). Xử lý thiếu dữ liệu theo giả định thế giới mở, trả "unknown" (T07:L29). | Có. Toàn văn, 29 trang (T07:L5) | Tham khảo | Tiền lệ về "unknown" thay cho suy NO; không SHACL, không GUID |
| T08 G3_01_CICCARESE_PAV_2013 | Không ghi ngày. J. Biomed. Semantics 4, 37 (T08:L3) | Đọc sâu (một bài, nhóm G3; lĩnh vực y sinh) | Từ vựng PAV phân biệt vai trò author/curator/creator, dấu thời gian từng vai trò, phiên bản previousVersion/derivedFrom (T08:L23, L15). Không có máy trạng thái phê duyệt (T08:L25). | Có. Toàn văn, 22 trang (T08:L5) | Tham khảo | Chỉ là từ vựng nền; không BIM |
| T09 G3_02_WAN_2019 | Không ghi ngày. Sustainability 11(17) 4583 (T09:L3) | Đọc sâu (một bài, nhóm G3) | Hệ thống quản lý cầu BIM mở rộng IFC/IFD, triển khai trên cầu Đại Vận Hà (T09:L11, L31). Bước "quản lý kiểm tra" có mô tả nhưng không là trường lược đồ (T09:L27, L41). | Có. Toàn văn, 17 trang (T09:L5) | Còn hiệu lực (làm ghi chú), cần kiểm tác giả | Tệp nêu xung đột tác giả PDF/Zotero (T09:L7) |
| T10 MULTI_01_LEE_EASTMAN_SOLIHIN_2021 | Không ghi ngày. JCDE 8(1) (T10:L3) | Đọc sâu (một bài, nhóm G1/G2) | Quy tắc kiểm tra trao đổi IFC/COBie, gồm quy tắc GUID (T10:L9-L13). Nêu có kiểm thử âm nhưng không liệt kê tiểu loại (T10:L29). | Có. Tệp ghi toàn văn 18 trang (T10:L5), nhưng cũng nói chưa đọc đến mức dòng (T10:L29) | Tham khảo, cần kiểm | Tự mâu thuẫn mức đọc; mâu thuẫn với T17:L32 về kiểm thử âm (xem mục 6) |
| T11 MULTI_02_LORVAO_ANTUNES_2024 | Không ghi ngày. ISWA 22, 200366 (T11:L3) | Đọc sâu (nhóm G2/G3), gắn nhãn CLOSEST_COMPETITOR | Ontology nối quan trắc cảm biến/kiểm tra → phần tử kết cấu → IFC GUID cho đường cao tốc châu Âu (T11:L11). Không có soát xét/phê duyệt, không kiểm thử lỗi dữ liệu, không xử lý phiên bản (T11:L15, L25, L35). | Có. Toàn văn, 14 trang (T11:L5) | Còn hiệu lực (đối thủ gần nhất theo tệp) | Là đối chiếu chính cho chuỗi cảm biến→GUID |
| T12 MULTI_03_KIM_2018 | Không ghi ngày. Autom. Constr. 87 (T12:L3) | Đọc sâu (nhóm G2/G3), gắn nhãn CLOSEST_COMPETITOR | Ontology OWL nối đối tượng IFC/COBie với 590 bản ghi công việc FM của 5 công ty Hàn Quốc (T12:L9, L29, L33). Dùng số `#id` STEP, không dùng GlobalId (T12:L13). | Có. Toàn văn, 15 trang (T12:L5) | Còn hiệu lực, có mâu thuẫn với T16 | T12:L33 nêu "~200%" như kết quả; T16:L91 coi là không có cơ sở |
| T13 G1_TO_G2_CONDITION_EVIDENCE_INTERFACE_v1.0 | Tên tệp v1.0; tiêu đề ghi "v1.1", cấp 2026-08-04, cập nhật 2026-08-04 (T13:L3); ghi đồng bộ 13/09/2026 (T13:L12) | Định hướng/đặc tả giao diện (không phải prompt, không phải bằng chứng) | Hợp đồng giao diện G1→G2: bản ghi `Condition_Evidence`, 6 thực thể liên kết, vòng đời, 42 quy tắc toàn vẹn, 37 phép thử âm định nghĩa trước (T13:L286-L722). Nói rõ chưa có bản ghi bằng chứng nào được chấp nhận, G1 vẫn OPEN (T13:L14, L506). | Có (836/836 dòng) | Còn hiệu lực làm nguồn đối chiếu trường; xem mục 8 và 4 | Mức nguồn ghi "level 7" (T13:L5); xung đột nội bộ về chuỗi định danh (T13:L15 vs L74) |
| T14 G2_G3_CORE_TRACEABILITY_DEEP_READ_20260901 | 2026-09-01, "EVIDENCE RECORD - NEW" (T14:L3-L4) | Đọc sâu (4 bài; 3 toàn văn + 1 thiếu toàn văn) | Piras 2026, Li 2023, Hagedorn 2023 đọc toàn văn có trang; Nuyts 2024 chỉ abstract (T14:L7, L22). Kết luận: Gap 2 hẹp nhưng còn bảo vệ được; Gap 3 dạng chung yếu (T14:L101-L115). | Có | Còn hiệu lực | Thay trạng thái đọc sâu của T15 cho 3 bài (T14:L12) |
| T15 G2_G3_RECENT_EVIDENCE_SCREENING_2023_2026 | 2026-08-04 (T15:L4) | Kiểm độ mới | Sàng 29 bản ghi Zotero còn lại + 13 bài 2023–2026; kiểm ma trận tính mới (T15:L13-L15). Hàng đợi Round 3 gồm 6 bài (T15:L21). | Có | Lỗi thời một phần: bị T14 thay cho Piras/Li/Hagedorn; bị T18 thay cho Sedigh/Wu; mâu thuẫn T14 về Nuyts | Nuyts "đã đọc toàn văn" ở T15:L75 nhưng T14:L22 ghi thiếu toàn văn |
| T16 G2_G3_ROUND4_..._20260809 | v1.0, 2026-08-09; "immutable once accepted" (T16:L3-L5) | Đọc sâu (5 bài) | Keet&Khan 2025, Kim 2018, Jia 2025, Lee D. 2021, Pauwels&Terkaj 2016; đề xuất 5 ý tưởng A1–A5 (T16:L243-L251). | Có | Còn hiệu lực với 5 bài; con trỏ "Round 3A" không kiểm được | T14:L12 nói Round 3A không có trong cây thư mục |
| T17 G2_G3_SCREENING_EVIDENCE_AND_GAP_REPORT | 2026-08-04 (T17:L5) | Kiểm độ mới (sàng lọc 34 mục) | 34 mục: 12 Tier A, 14 Tier B, 2 Tier C, 6 loại; khoảng trống mạnh nhất = kiểm lỗi tham chiếu tích hợp + truy vết hai chiều (T17:L11, L274). | Có | Lỗi thời một phần: đã bị T14, T16, T18 thay ở các bài đã đọc sâu; hàng đợi deep-read đã thực hiện | Bản ghi tiếng Việt/Anh trộn; tập 34 mục lệch với T15 (T15:L59) |
| T18 GAP2_GAP3_NEW_FULLTEXT_DEEP_READ_20260901 | 2026-09-01 (T18:L3) | Đọc sâu (2 bài toàn văn) | Sedigh & Müller 2025 và Wu et al. 2026; cả hai chỉ làm yếu dạng chung của khoảng trống (T18:L38, L55). | Có | Còn hiệu lực | Có trang dẫn, kiểm phiên bản (T18:L16-L19) |

---

## 2. Số liệu

Chỉ ghi số liệu định lượng thấy trong tệp. Mức xác nhận "tự báo" = con số do tệp tự nêu, tôi chưa đối chiếu nguồn gốc.

### 2.1 Các số mà BRIEF yêu cầu cần nguồn

| Số liệu | Giá trị | Tệp + dòng | Ngữ cảnh / mức xác nhận | Mâu thuẫn? |
|---|---|---|---|---|
| 6 IFC; 3.356 cấu kiện; 10.328 liên kết; 718/676 phần tử audit; 8 cặp GUID trùng; 16/16 ngày 23/09; K1–K11; D011–D016; B0/B1/M1–M4 | KHÔNG XUẤT HIỆN trong 18 tệp nhóm C2 (tìm bằng grep trên cả 18 tệp) | — | — | — |
| D003–D010 | Chỉ D003/D004, D005, D006, D007, D010 xuất hiện (T13:L17-L21) | T13:L17-L21 | Trích từ ghi đồng bộ 13/09/2026; nội dung quyết định ghi "dispositions unchanged" | Sổ đăng ký `G1_G2_INTERFACE_DECISION_REGISTER.csv` không có trong nhóm tệp (T13:L97) |

### 2.2 Số liệu của tài liệu giao diện G1→G2 (T13)

| Số liệu | Giá trị | Tệp + dòng | Ngữ cảnh / mức xác nhận | Mâu thuẫn? |
|---|---|---|---|---|
| Số phép thử âm định nghĩa trước | 37 (CE-NEG-001…037) | T13:L684-L720 | Chỉ định nghĩa, chưa chạy (T13:L680). Tôi đếm theo ID cuối | Không. Khác với "~30 lỗi chèn mù" của phạm vi khóa |
| Số quy tắc toàn vẹn | 42 = INT 5 + REF 11 + VER 6 + BIM 7 + GOV 13 | T13:L611-L676 | Tôi tự đếm theo ID | Không |
| Số trường tiêu đề của bản ghi `Condition_Evidence` | 52 (4+8+6+10+9+6+6+3) | T13:L286-L376 | Tôi tự đếm theo mục 7.1–7.8 | Không |
| Số thực thể liên kết | 7 (Sensor_Link, Window_Link, BIM_Binding, Source_Link, Recording_Link, Fold_Link, Evidence_Status_Event) | T13:L395-L589 | Tôi tự đếm | Không |
| Số sản phẩm bàn giao G1 | 19 | T13:L243-L261 | Tôi tự đếm | Không |
| Số giá trị từ vựng cờ chất lượng | 15 (gồm NO_FLAG) | T13:L209-L223 | Tôi tự đếm | Không |
| Số quyết định treo (mục 19) | 13 | T13:L812-L824 | Đã nêu trong tệp | Không |
| Cửa sổ 400 mẫu, bước 200 | 400/200 | T13:L19 | Ghi đồng bộ về Paper 1 (D006) | T13:L159 nói các kế hoạch cửa sổ khác nhau, chưa chọn |
| Số dòng dữ liệu G1 đã kiểm | 66 (provenance log); 238 (LORO); 36 (cross-campaign); 300 (permutation); 10 (sensitivity); 12 (kiểm tự động, đều PASS) | T13:L124-L132 | Tự báo; nguồn gốc không nằm trong nhóm tệp. Tệp nói thiếu dự đoán, thiếu bằng băm | Không |
| Trạng thái cổng | G1 OPEN-PARTIAL EVIDENCE; G2 OPEN-LITERATURE BOUNDARY CLOSED, SPEC NOT FROZEN; G3 chưa thực thi | T13:L8; T14:L132 | Nhất quán T13/T14/T16/T18 | Không |

### 2.3 Số liệu từ các bài (T14, T16, T18 – có trang dẫn)

| Số liệu | Giá trị | Tệp + dòng | Ngữ cảnh / mức xác nhận | Mâu thuẫn? |
|---|---|---|---|---|
| Piras 2026: số mô hình / tòa nhà / phần tử / tài sản | 12 mô hình; 2 tòa nhà (Bologna); ~9.000 phần tử IFC; 428 tài sản | T14:L35 (PDF tr.10-11, 18, 20-24) | Đọc toàn văn; SHA-256 PDF trùng bản Zotero (T14:L20) | Không |
| Piras: hiệu quả | ~4 phút/mô hình; <3 phút/tòa nhà; kích thước +2,5%; giảm ~85% công | T14:L37 | AUTHOR-STATED, là ước lượng ca, không phải chuẩn (T14:L38) | Không |
| Li 2023 | cầu 1.767 m (Cocodala); ID mẫu `1-68-10 10 10` | T14:L52 | Toàn văn, 16 trang | Không |
| Hagedorn 2023 | 4 bộ dữ liệu; 9–832 phần tử; 8–115 tác vụ; 9–959 liên kết nhị phân; 202–27.816 bộ ba linkset; vi phạm R1 = 0/30/39/1; R2 = 0/0/0/0; R3 = 0/0/7/0; <2,5 s; giảm 24–49% bộ ba | T14:L79, L81 (PDF tr.9-17) | Toàn văn, 23 trang PDF (có 1 trang bìa) | Không |
| Sedigh 2025 | 1 bộ AHU; 8 bộ phận chính; 8 trang PDF (1 bìa) | T18:L18, L31 | Toàn văn | Không |
| Wu 2026 | 25 bài sàng; 4 phỏng vấn; 7 nhà nghiên cứu HCI + 5 xây dựng tuần hoàn; 8 công ty Thụy Sĩ; 5/7 ủng hộ; 12 trang | T18:L47, L50 | Toàn văn | Không |
| Keet & Khan 2025: kho ROCQS | 558 câu hỏi năng lực | T16:L57 | Tự báo của bài; "not independently validated" | Không |
| Kim 2018: 590 bản ghi; 5 công ty; 60 không gian, 262 tường, 66 cửa, 25 cửa sổ; 12 bản ghi cho không gian 139 → 7 tường; "~200%" | 590; 5; 60/262/66/25; 12→7; 200% | T12:L29, L33; T16:L88-L91 | Mô hình là tệp mẫu buildingSMART, không phải tòa nhà thật (T12:L27; T16:L88) | CÓ: T12:L33 nêu như kết quả so với quy trình truyền thống; T16:L91 coi "không dẫn xuất, không mẫu số" |
| Jia 2025 | nhà 21 tầng; rule lan can 1,10 m; 2 `IfcRailing` ở 900 mm; n = 1 luật | T16:L128-L129 | Không có ma trận nhầm lẫn, không bộ lỗi chèn | Không |
| Lee D. 2021 (blockchain) | 49 viên gạch; BIM 876 MB; 49 phát biểu ~0,5 kB; 3/10 nút bị gán chữ ký sai; 2,41 s và 3,42 s | T16:L160-L161 | Cảm biến giả định (T16:L160) | Không |
| Pauwels & Terkaj 2016 | Không có số liệu định lượng; điểm chính: lớp ràng buộc RULE/WHERE không chuyển sang OWL | T16:L191 | PDF tr.33 [tr.132] | Không |

### 2.4 Số liệu từ các ghi chú từng bài (T01–T12; không có số trang PDF)

| Số liệu | Giá trị | Tệp + dòng | Ngữ cảnh | Mâu thuẫn? |
|---|---|---|---|---|
| Kücükavci 2024 | 36 shape / 122 ràng buộc; 369.054 bộ ba; 372 vi phạm lần 1 → 14 lần 2; 3,1 s; 87 s | T06:L9, L21, L25 | Một tòa nhà thật (Frederiksberg Skole) | Không |
| Beach 2015 | 18 tháng; CSH 229 mục/64 thủ tục; BREEAM 854/180; Building Regs 239/166; nhà văn phòng 9 tầng 85.000 sq ft | T07:L23 | Ca thật, đối chứng thủ công | Không |
| Lorvão Antunes 2024 | 13 câu hỏi năng lực; OOPS!: 0 nghiêm trọng, 55 quan trọng (54 do ontology nhập), 9 nhỏ (3 của chính bài) | T11:L25, L33 | | Không |
| Wan 2019 | nhịp chính 464 m (108+248+108) | T09:L31 | Một cầu thật | Không |
| Sacks 2018 | 5 kỹ sư, 3 workshop; 4 cầu (Acworth, 2 cầu Cambridgeshire, Route 79 Haifa) | T03:L23, L33 | | Không |
| Stolk & McGlinn 2020 | >200.000 tòa nhà (Prime2) | T04:L11 | | Không |
| Fang 2025 | 31 trang PDF, đọc đến ~tr.28 | T01:L5 | | Không |
| Borkowski 2026 | 3 phần tử × 3 pha; 8 câu hỏi năng lực | T02:L15 | Chỉ abstract | Không |

### 2.5 Số liệu về quy mô sàng lọc (T15, T17)

| Số liệu | Giá trị | Tệp + dòng | Mức xác nhận | Mâu thuẫn? |
|---|---|---|---|---|
| T15: số bản ghi Zotero | 37 = 34 (`C9J2V33M`) + 3 (`GZYTA3TB`); 8 đã đọc sâu; 29 còn lại sàng | T15:L13 | Tôi đếm bảng L29–L57: 29 hàng, quyết định 6/10/6/7 = 29, khớp | Không |
| T15: bài 2023–2026 giữ lại | 13 | T15:L15, L74-L86 | Tôi đếm bảng: 13 hàng | Không |
| T15: hàng đợi Round 3 | 6 bài (Li, Piras, Nuyts, Hagedorn, Mohamed, Celik) | T15:L21, L248-L255 | Mới có 4 bài đọc sâu ở T14; Celik ghi Round 3B (T16:L34); Mohamed không thấy bản đọc | Mohamed 2023 chưa thấy bản ghi đọc sâu trong nhóm C2 |
| T17: số mục | 34: 12 Tier A, 14 B, 2 C, 6 loại; 13 mục có DOI qua Scite không thấy rút bài | T17:L11-L13 | Tôi đếm bảng: khớp | Tập mục lệch T15 (T17 có Keet&Khan, T15 thay bằng `LSYSC59G`, T15:L59) |
| T16: số PDF thư mục | 15 (1 trùng) | T16:L20-L38 | | Không |
| T16: phạm vi kết luận | "4 + 4 + 4 + 2 + 5 bài" | T16:L259 | Tự báo | Không |
| Monfardini 2023 | khảo sát 63 người | T15:L35; T17:L47 | | Không |
| Du 2024 | rà soát PRISMA 93 bài | T17:L53 | | Không |
| Yang 2025 | thực địa 22/10–07/11/2024 | T15:L143 | | Không |

---

## 3. Quyết định và mã treo

| Mã | Nội dung | Tệp + dòng | Trạng thái |
|---|---|---|---|
| K1–K11 | Không xuất hiện trong nhóm C2 | — | Không dò được |
| D003/D004 | Run là đơn vị nhóm, recording là đơn vị chấm; run chưa là đơn vị độc lập đã kiểm | T13:L17 | Treo (sổ đăng ký không kèm; T13:L97, L812) |
| D005 | Khối cảm biến ánh xạ vị trí theo hướng trọng lực, không có hồ sơ thiết bị | T13:L18 | Treo; liên quan C1 (định danh cảm biến). Quyết định mở số 7: đối soát `S1/S2/S3` cũ với Sensor_ID vật lý (T13:L818) |
| D006 | Cửa sổ 400 mẫu, bước 200, cắt trong recording | T13:L19 | Treo; T13:L816 ghi kế hoạch cửa sổ chưa thống nhất |
| D007 | Dự đoán recording = trung bình xác suất cửa sổ rồi argmax; đã kiểm mã, chưa đăng ký trước; không lưu xác suất từng cửa sổ | T13:L20 | Treo |
| D010 | Có SD_fold và SD_seed nhưng chưa có bản ghi CEI | T13:L21 | Treo |
| D008, D009, D011–D016 | Không xuất hiện trong nhóm C2 | — | Không dò được |
| 13 quyết định mở (mục 19) | (1) đơn vị bằng chứng; (2) quy tắc tổng hợp; (3) tối thiểu cảm biến/tỉ lệ cửa sổ hợp lệ; (4) phương pháp tin cậy/chất lượng; (5) đặc tả cửa sổ; (6) đơn vị hoán vị; (7) đối soát Sensor_ID vật lý; (8) chính sách liên kết BIM một-nhiều; (9) phiên bản BIM chuẩn, bền vững GUID, thay thế/ánh xạ lại; (10) phân quyền người tạo/soát xét; (11) `Action_Status` lưu hay suy từ lịch sử `Status_Event`; (12) lưu ngoài hay nhúng IFC; (13) đóng gói tái lập | T13:L812-L824 | Treo toàn bộ; (9), (10), (11) trùng trực tiếp với C1/C3/C6/C9 của Paper 2 |
| Gate G1 / G2 / G3 | G1 OPEN-PARTIAL; G2 OPEN-LITERATURE BOUNDARY CLOSED, SPEC NOT FROZEN; G3 NOT IMPLEMENTED, EXECUTION-NOT-OPEN | T13:L8, L14; T14:L132 | Nhất quán nhiều tệp; không phải mã cổng Paper 2 đã khóa |
| ADR Action-Status-Event | Đề xuất, chưa chấp nhận: chuỗi Action_Record_ID, Status_Event, ủy quyền, xác minh, đóng/mở lại | T13:L15, L76 | Treo (`PROPOSED — NOT YET ACCEPTED`) |
| CE-INT-001…005, CE-REF-001…011, CE-VER-001…006, CE-BIM-001…007, CE-GOV-001…013 | Bộ luật toàn vẹn của giao diện Condition_Evidence | T13:L611-L676 | Đề xuất (chờ G2 chấp nhận); chưa chạy. Không phải R01–R17 |
| CE-NEG-001…037 | Phép thử âm định nghĩa trước, mỗi phép thử gán một quy tắc | T13:L684-L722 | Định nghĩa, chưa thực thi (T13:L680, L722) |
| CQ (SCQ/VCQ/FCQ/RCQ/MpCQ) | Loại câu hỏi năng lực theo Keet & Khan; yêu cầu đăng ký trước SCQ/VCQ/RCQ và tiêu chí chấp nhận | T16:L52-L53; T13:L675, L789 | Treo (CQ chưa đăng ký); không có CQ01–CQ12 |
| CQ5, CQ8, CQ9, CQ10 của Lorvão | Truy vết thuận qua SPARQL | T11:L31 | Đã nêu trong bài, không phải mã của NCS |
| R1, R2 (Oraskari); R1–R3 (Hagedorn) | Yêu cầu/luật kiểm thử của hai bài | T05:L13, L27; T14:L80 | Là mã của bài ngoài; TRÙNG KÝ HIỆU với R01–R17 của NCS, nguy cơ nhầm |
| A1–A5 (Round 4) | A1 CQ registry có kiểu: ADOPT NOW; A2 khai báo liên kết asserted/derived: ADOPT NOW; A3 danh mục ràng buộc độc lập tuần tự hóa: ADD TO REVIEW; A4 tách attestation/payload: DEFER; A5 blockchain: REJECT | T16:L247-L251 | Đề xuất của bản ghi Round 4 (chưa thấy NCS duyệt) |
| 6 "next action" của Round 4 | Viết lại schema CQ; thêm `Link_Provenance`; ghi chú RULE/WHERE không kế thừa qua ifcOWL; `Model_Version_ID` bắt buộc; tách hai "Lee 2021"; quyết định Round 5 | T16:L263-L268 | Treo |
| X-15 | Xung đột kiểm toán DOI Piras | T14:L20 | Đã giải (DOI xác nhận) |
| Mã P1/P2/P3, Tier A/B/C, DIRECTLY_RELEVANT/SUPPORTING/BACKGROUND/EXCLUDE | Ưu tiên đọc, hạng bài | T15:L29-L57; T17:L26-L59 | Phân loại của bản sàng lọc, không phải quyết định phạm vi |
| Mã Zotero (YKGTBESL, NQ3KGDWN, F8RMUZ44, …) | Khóa mục Zotero từng bài | T01:L3; T02:L3; T03:L3; … | Tham chiếu, không phải quyết định |
| G2_G3_ROUND1/2/3A/3B…, G1_G2_INTERFACE_DECISION_REGISTER.csv | Tệp được tham chiếu | T13:L97-L102; T16:L8; T14:L12 | Không nằm trong nhóm C2; T14:L12 nói Round 3A không có trong cây hiện hành |

---

## 4. Điểm lệch so với phạm vi đã khóa

| Chiều | Tệp nói gì (trích ngắn + dòng) | Phạm vi khóa nói gì | Mức độ |
|---|---|---|---|
| Số thực thể | T13 có bản ghi `Condition_Evidence` 52 trường + 7 thực thể liên kết (T13:L286-L589) và 19 sổ bàn giao (T13:L243-L261). T17:L251 nêu `Asset_ID, IFC_GlobalId, Condition_Evidence_ID, Inspection_Record_ID, Action_Record_ID, Status_Event_ID, Agent_ID`. T15:L292 tách "verification entities" thành thực thể riêng; T14:L8, T15:L297 có `Verification_Record`, `Action_Record`, `Status_Event` | 6 thực thể (COMPONENT, SENSOR+SENSOR_MAPPING, EVIDENCE, INSPECTION_RECORD qua EVIDENCE_USE, ACTION, STATUS_EVENT). Không có `Verification_Record`, `Agent` riêng, `BIM_Binding`, `Evidence_Status_Event` | Cao |
| Công cụ | T13:L40 "not ... SHACL-only specification"; T15:L286 và T17:L235 "implementation-neutral"; nhưng T04/T05/T11 kết luận đặt hướng "mở rộng SHACL-style validation" (T04:L33; T11:L39) và T17:L143 "chạy ràng buộc ở database và/hoặc RDF layer" | Python + IfcOpenShell + SQLite/JSON; KHÔNG RDF/SHACL/SPARQL/ontology | Trung bình. Tệp giao diện trung tính công nghệ, nhưng khung "mở rộng SHACL/ontology" trong T04, T05, T11, T16:L255 nghiêng sang ngôn ngữ ngoài phạm vi |
| Số CQ | T11:L25 nêu 13 CQ của Lorvão; T16:L57 ROCQS 558 CQ. Tệp NCS yêu cầu "preregistered SCQ/VCQ/RCQ" (T13:L675, L789) nhưng không nêu số | CQ01–CQ12 → 3 câu hỏi truy ngược | Trung bình. Khung CQ có kiểu SCQ/VCQ/RCQ khác cấu trúc "3 câu hỏi truy ngược" |
| Chỉ số | Không có M1–M4. Chỉ số đề xuất: "detection coverage, false passes, false failures" (T17:L143); "exact expected/actual paired forward-reverse result sets" (T14:L115); "quality/confidence" CEI (T13:L342) | M2 (tỉ lệ bắt lỗi chèn mù theo nhóm) là chỉ số chính; M1 đủ thuộc tính, M3 truy ngược 3 câu, M4 phút/bản ghi | Cao. Không có chỉ số tương ứng trong nhóm C2 |
| Đối chứng | Không có B0/B1. Có "oracle" và "Fixture/Oracle Manifest" (T14:L130) nhưng là tiêu chí chấp nhận của chính mô hình đề xuất, không phải so với hồ sơ VN hay IFC+BCF thô. Bellon 2025 chỉ là "đối thủ gần nhất" (T17:L14), kèm ghi "paywalled at entity level" (T16:L259) | B0 = 20–30 hồ sơ kiểm định VN mã hóa tay; B1 = IFC 4.3 theo Bellon 2025 + BCF 3.0 (tắt C5, C6, C9) | Cao. Cần kiểm xem Bellon 2025 đã được đọc đủ chưa để làm B1 |
| Khoảng trống | T14:L99 "Gap 2: chuỗi truy vết tích hợp ... từ condition evidence tới action đã kiểm chứng"; T14:L109 "Gap 3: toàn vẹn tham chiếu tích hợp kết hợp truy vết hai chiều" và T14:L111/T18:L97 coi Gap 3 là khoảng trống còn bảo vệ được (dạng "exact-oracle"). Còn có nhãn lạ: "GAP-B" trong T02:L5 (= đề xuất cho nhóm định danh G1) và "GAP-G/GAP-H" trong T04:L29, T11:L35 | G-A (A1 đánh giá theo đơn vị độc lập; A2 phạm vi hiệu lực bắt buộc, kiểm tại lần dùng) và G-B (chuỗi bằng chứng–quyết định–trách nhiệm–xác minh sau sửa chữa). GAP3 cũ KHÔNG còn là khoảng trống, mà là thiết kế đánh giá | Cao. (a) T14/T18 vẫn coi kiểm chứng xác định là khoảng trống; (b) nhãn "GAP-B" của T02 trùng ký hiệu G-B nhưng khác nghĩa (định danh qua pha, không phải chuỗi trách nhiệm) |
| RQ | T13:L46-L87: RQ1 thượng nguồn, RQ2 hạ nguồn, WP2, Chương 5, Paper 2, G2-G3(-G6). Không có RQ2.1/2.2/2.3 | RQ2 chia 2.1 định danh (C1,C3), 2.2 phạm vi (C5,C9), 2.3 chuyển trạng thái (C6) | Trung bình. Không mâu thuẫn trực tiếp nhưng không có ánh xạ RQ2.x |
| Đóng góp | T15:L286 và T17:L235/L249: "Evidence-to-Action Traceability Specification", gồm CQ, ràng buộc, phép thử âm, truy vết thuận/ngược, vai trò, `Verification_Record` | ĐG1 mô hình 6 thực thể mở rộng IFC4.3+BCF3.0; ĐG2 hợp đồng bằng chứng + EVIDENCE_USE(within_scope, justification); ĐG3 STATUS_EVENT + giao thức lỗi chèn mù | Trung bình. Khớp một phần ĐG3; không có `EVIDENCE_USE(within_scope, justification)` và không có BCF 3.0 trong các tệp |
| Tạp chí đích | Không thấy tên tạp chí đích của Paper 2 trong nhóm C2 | (BRIEF liệt kê chiều này) | Thấp. Không có dữ liệu để đối chiếu |
| Số lỗi chèn | 37 phép thử âm CE-NEG, định nghĩa trước với kết quả kỳ vọng và quy tắc gán sẵn (T13:L684-L722); T17:L255-L256 và T15:L228 yêu cầu "predefined violation codes", "predeclared mutations"; T13:L788 coi "hidden expected result" là LỖI | ~30 lỗi chèn MÙ, người chèn ≠ người viết luật, 4 nhóm (định danh-liên kết C1,C3; phiên bản C9; ngoài phạm vi C5,C9; chuyển trạng thái không căn cứ C6) | Cao. Thiết kế của tệp là không-mù và chỉ phủ phần bằng chứng (Condition_Evidence), không phủ INSPECTION/ACTION/STATUS; số 37 khác ~30 |
| Phạm vi hiệu lực (A2) | Giao diện không có trường bắt buộc kiểu `scope.applicable_conditions`/`install_batch`. Chỉ có `Limitation_Context` (1..*, "structured text/reference"), `Evidence_Interpretation_Boundary`, `Downstream_Use_Limitation` (T13:L345-L346, L376). Không có phép thử âm "dùng ngoài phạm vi" trong 37 phép thử (T13:L684-L720) | A2: phạm vi hiệu lực là trường bắt buộc của từng bằng chứng, kiểm tại lần dùng; C5 dùng ngoài phạm vi phải có lý do | Cao (với G-A phụ). Giao diện không có `EVIDENCE_USE` và không kiểm "tại lần dùng". Chỉ có cổng nhập G2 (T13:L726-L742) |
| Hiệu lực ánh xạ theo thời điểm (C3) | `BIM_Binding` có `Verified_At` và vòng đời trạng thái, nhưng không có khoảng hiệu lực `valid_from/valid_to` của ánh xạ cảm biến–cấu kiện (T13:L429-L449, L527-L548) | C3: thời điểm đo nằm trong hiệu lực ánh xạ | Cao. Chỉ có `Observation_Start/End_Time` (T13:L305-L306) |
| Tính hai chiều với n:m (BIM_GUID) | T13:L491-L495: mặc định bản ghi chia theo từng thành phần, "list of GUID in one field is prohibited"; ràng buộc "tối đa một liên kết VERIFIED hoạt động" (T13:L445, L544) | `BIM_GUID n:m` trong EVIDENCE | Trung bình. n:m chỉ thực hiện qua nhiều dòng `BIM_Binding` lịch sử/ngoại lệ; mặc định 1 bản ghi : 1 cấu kiện |
| Xung đột định nghĩa "trạng thái" | `Evidence_Status_Event` (T13:L578-L595) là sự kiện đổi trạng thái của bằng chứng; `Status_Event` ở T13:L62-L76 là đề xuất cho hành động | STATUS_EVENT thuộc chuỗi ACTION; C6 áp cho bước chuyển của hành động/trạng thái | Trung bình. Hai thứ cùng gọi "status event", dễ nhầm khi ánh xạ |
| Mô hình thực / BIM 1:1 | Nhóm C2 chỉ nói đến G1 phòng thí nghiệm, "legacy block position" so với Sensor_ID vật lý (T13:L186, L245, L635), không nói BIM nhà xưởng thật 1:1 hay `Physical_Identity = FALSE` | BIM 1:1 = nhà xưởng thật, khung 1:10 mô phỏng, nối qua tương ứng thông tin | Thấp-Trung bình. Cơ chế "candidate/verified binding" có thể dùng, nhưng không có khái niệm "nối chỉ qua tương ứng thông tin" |
| Nguồn hiệu lực | T13:L5 "Source-of-truth level: 7"; T16:L5 "evidence, not navigation authority" | Nguồn hiệu lực cao hơn: tiểu luận + GD3b > CLAUDE.md, tệp 00, prompt v2 > thư mục 05_PAPER_2 | Ghi nhận: cả 18 tệp thuộc tầng thấp nhất; khi khác thì phạm vi khóa thắng |

---

## 5. Tài sản đáng giữ (cho Pha 1) và thứ nên bỏ

### Nên giữ

| Tài sản | Vị trí | Lý do |
|---|---|---|
| Danh sách "Claim boundary" Cho phép/Không cho phép cho Piras, Li, Hagedorn, Sedigh, Wu | T14:L40, L57, L84; T18:L36, L53, L103-L112 | Là rào chắn cách viết tính mới cho phần so sánh với B0/B1 và cho phần Related Work; đã có trang PDF |
| Khẳng định giới hạn "Trong phạm vi các tài liệu đã sàng lọc..." | T15:L9, L286; T17:L7 | Khớp quy tắc 3 (không viết "chưa ai nghiên cứu") |
| Trạng thái liên kết BIM UNBOUND/CANDIDATE/VERIFIED/REJECTED/SUPERSEDED, kiểm tra 1–10, quy tắc CE-BIM-001…007 | T13:L525-L548, L650-L658 | Mầm cho C1/C3/C9 (neo định danh, hiệu lực ánh xạ, căn cứ còn hiệu lực); cần quy đổi sang trường EVIDENCE/SENSOR_MAPPING |
| Mẫu trường sự kiện trạng thái: Previous/New status, Changed_By, Changed_At, Change_Reason, Authorization_Reference; quy tắc bất biến, không sửa tại chỗ | T13:L580-L595, L565-L574 | Mẫu thô cho STATUS_EVENT (C6) và cho nhóm lỗi "chuyển trạng thái không căn cứ" |
| Quy tắc phiên bản/thay thế: bản đã soát xét bất biến, thay thế một người kế nhiệm, không chu trình, không để bản đã thay thế còn hoạt động | T13:L641-L646, CE-NEG-014, -022, -023 | Mầm cho `revision_of` và C9 |
| Ý "liên kết dẫn xuất cần luật toàn vẹn riêng" (asserted vs derived) | T16:L241, L248, L264 | Rủi ro thật với nhà xưởng thép (cấu kiện không có một quan hệ IFC chuẩn); nên đưa vào yêu cầu cho trường liên kết |
| Nhận xét "SHACL bỏ qua đích thiếu nếu không kiểm sự tồn tại riêng" | T05:L33 | Áp dụng cho mọi trình kiểm tra, không chỉ SHACL: bộ lỗi chèn phải có phép kiểm sự tồn tại |
| Cảnh báo `#id` STEP không bền qua lần xuất lại | T12:L13; T16:L98 | Hỗ trợ C1/C9 và lý do dùng GlobalId có kiểm |
| Cảnh báo "giá trị giữ chỗ N/A/999 vẫn đủ trường mà không có giá trị chứng cứ" | T14:L38 (Piras, PDF tr.20-21) | Gợi ý lỗi chèn loại "đủ trường nhưng rỗng nghĩa" cho M1 vs M2 |
| Điểm chuẩn hóa: Wan 2019 mô tả bước quản lý kiểm tra nhưng không là trường lược đồ | T09:L27, L41; T14:L55 (Li: `completed` chỉ là cờ hiện tại, không sự kiện, không người thực hiện) | Chính xác là khoảng trống G-B cần so với B0 (hồ sơ VN) |
| Đối thủ gần nhất: Lorvão 2024, Piras 2026, Li 2023, Borkowski 2026 (nếu còn hiệu lực) | T11:L39; T14:L42, L59; T02:L33 | Cần cho bảng so sánh và định vị |
| Danh mục mất mát: lớp RULE/WHERE của IFC không sang OWL | T16:L191 | Lý do dùng Python/IfcOpenShell tự viết luật |

### Nên bỏ hoặc hạ cấp (cho Paper 2 khóa)

| Thứ | Vị trí | Lý do |
|---|---|---|
| Hướng blockchain (Lee D., Celik, Jaskula) | T16:L163, L251; T15:L79 | Ngoài phạm vi; tệp tự REJECT |
| Khung CQ có kiểu (SCQ/VCQ/…) làm đóng góp | T16:L247 | Phạm vi khóa dùng 3 câu truy ngược; giữ như tham khảo phương pháp |
| CEI (đa chiều, không vô hướng), 19 sổ bàn giao G1, từ vựng Quality_Flag, Window/Fold/Source Link, cờ Eligible_For_* | T13:L185, L243-L261, L205-L223, L395-L489, L374-L376 | Thuộc Paper 1/G1 và thí nghiệm rung; EVIDENCE khóa chỉ có `uncertainty`, `method_version` |
| Kết luận "đóng gói theo ontology/SHACL" của các ghi chú bài (T04, T05, T11) | T04:L33; T05:L29; T11:L39 | Công cụ ngoài phạm vi; giữ dữ kiện, bỏ khuyến nghị |
| Giới hạn FEM "nominal, uncalibrated..." | T13:L9, L173; T14:L9 | Không phải phạm vi Paper 2 khóa |
| Nhãn Gap 2/Gap 3, Gate G1–G3 của các tệp | nhiều | Gây nhầm với G-A/G-B và với nhóm G1–G3 của tên tệp |
| Ước lượng "~200%" của Kim, "~85%" của Piras làm kết quả | T12:L33; T14:L38 | Không có mẫu số/đối chứng (T16:L91; T14:L38) |

---

## 6. Ghi chú bất thường

1. **Ba bản chuỗi định danh khác nhau trong cùng bộ tệp.** (a) T13:L15 và T14:L8: chuỗi chuẩn kết thúc ở `Action_Status`, còn `Action_Record_ID`/`Status_Event` là "noncanonical proposals". (b) T13:L66-L74 và T13:L777: "Current governance normalizes ... `Action_Record_ID`" và yêu cầu chuỗi `Action_Record_ID`. (c) T15:L6: chuỗi "Condition_Evidence -> BIM component -> Inspection_Record -> Action_Record -> Status_Event -> accountable human review". Mâu thuẫn nội bộ ngay trong T13 (L15 so với L74).
2. **Số phiên bản T13.** Tên tệp `v1.0`, tiêu đề nội dung `Version: v1.1`, "Supersedes: v1.0 working specification" (T13:L3, L6). Có thêm "Sync note 13/09/2026" nhưng "Updated: 2026-08-04" (T13:L3, L12). Chưa rõ bản nào là bản hiệu lực.
3. **Nuyts 2024 mâu thuẫn mức đọc.** T14:L22, L65-L69: không có bản Zotero, `MISSING_FULLTEXT/ABSTRACT_VERIFIED`, không nêu chi tiết. T15:L75: "Full text and OSF reproducibility artifacts inspected"; T15:L174, L198 chấm "Yes" cho kiểm thử âm và dùng làm căn cứ làm yếu tính mới. T14:L124 nói "keep only the old screening status". Cần quyết định dùng bản nào.
4. **Con trỏ tới tệp không có.** T16:L33 "Already deep-read (Round 3A)" cho Piras; T14:L12, L20 nói Round 3A "not present in the current repository tree". T13:L98-L102 liệt kê ROUND1/2/3A/3B là "Read completely/Immutable evidence". Các tệp ROUND1, ROUND2, ROUND3A, ROUND3B, `G1_G2_INTERFACE_DECISION_REGISTER.csv`, `AUDIT_TIEU_LUAN_TONG_QUAN_KHONG_NOP.md` không có trong nhóm C2 và không thấy trong `ls /txt/`. Mohamed 2023 nằm trong hàng đợi Round 3 (T15:L254) nhưng không thấy bản đọc sâu trong nhóm C2.
5. **Hai bài "Lee et al. (2021)".** T10 = Lee, Eastman & Solihin, JCDE 8(1) (T10:L3). T16:L29, L40, L267 = Lee D. et al., Autom. Constr. 127, 103688 (blockchain). Tên tệp PDF "Lee et al. (2021) — Provenance và accountability" là bài Lee D. T15:L199 và T17 chỉ ghi "Lee (2021)" nên không phân biệt được (T15:L199 có thể là Lee D. vì liên quan trách nhiệm/chuỗi).
6. **Mức đọc của Borkowski.** T02 ghi chỉ abstract và kết luận "đe dọa tính mới mạnh nhất" (T02:L5, L33), trong khi `/txt/` có tệp `07_BORKOWSKI_2026_FULLTEXT_REVIEW.md` (chưa đọc, ngoài nhóm). DOI `10.3390/technologies14070413` (T02:L3) chưa có dấu hiệu kiểm bằng công cụ trong T02. Theo quy tắc 2/4: [CẦN KIỂM].
7. **Mâu thuẫn T10 so với T17 về Lee 2021 (Lee, Eastman, Solihin).** T10:L29: kiểm thử âm = YES, "strongest direct precedent ... rule-based negative testing of GUID integrity". T17:L32 và T17:L137-L140: "Failures không phải controlled negative fixtures". T10 cũng tự mâu thuẫn (toàn văn 18 trang, nhưng "pending closer line-level reading", T10:L5, L29).
8. **Mâu thuẫn T04 so với T17 về Stolk & McGlinn.** T04:L29 gọi hai vi phạm là "deliberate invalid-case testing YES"; thực tế đó là vi phạm thật trong dữ liệu R2RML (T04:L27); T17:L137-L140 gọi là "ordinary conformance defects". T17:L20 còn nêu khác biệt tên tác giả Zotero (Sanne/Sander) và abstract Zotero mô tả quá rộng WHERE-rule. T04 không có DOI.
9. **Mâu thuẫn T05 so với T17 về Oraskari R1.** T05:L13 trích "exactly one instance counterpart", T05:L29 nói luật bắt trường hợp thiếu. T17:L33, L218: R1 "chỉ chắc chắn bắt missing counterpart, chưa reject duplicate" và khuyến nghị "sửa R1 thành exactly-one". Cần xem lại luật thật trước khi nêu "duplicate".
10. **Mâu thuẫn T12 so với T16 về Kim 2018.** T12:L33: "≈200% increase ... compared against traditional" như kết quả đã so sánh. T16:L91: "No derivation, no denominator, no baseline definition ... Do not cite as performance result". Mô hình dùng là tệp mẫu buildingSMART, không phải tòa nhà thật (T12:L27; T16:L88).
11. **Thuật ngữ "thuận/ngược" bị đảo giữa các tệp.** T12:L31 gọi truy từ cấu kiện → hồ sơ công việc là "reverse"; T16:L107-L108 gọi cùng hướng đó là "forward partial" còn "reverse" là từ bản ghi → bằng chứng gốc. T11:L31 gọi từ cấu trúc → phần tử → quan trắc → GUID là "forward". Cần thống nhất trước khi dùng trong M3 (truy ngược).
12. **Ba nghĩa của G1/G2/G3 (và GAP).** (a) Gate (T13, T14, T18). (b) Nhóm bài (tên tệp G1_/G2_/G3_ và T10:L3 "Touches Group 1 ... Group 2"). (c) Nhãn "GAP-B", "GAP-G/GAP-H" (T02:L5; T04:L29; T11:L35) không định nghĩa trong nhóm tệp. Thêm: tiền tố tệp nguồn không khớp nhóm đã gán (T03:L5 là `G3_F8RMUZ44...`, T11:L5 là `G1_XUN8EX6X...`, T12:L5 là `G3_VI5QMSAE...`, T10:L5 là `G1_GWP87WLC...`).
13. **Kiểm tra trang dẫn.** Các tệp T01–T12 không có số trang PDF cho nhận định; chỉ có Mục/Hình/Bảng (thưa), "p.9 of extract" (T11:L11) và "p.7" (T11:L17). Chỉ T14, T16, T18 có số trang PDF kèm [trang in]. T15 và T17 không có trang.
14. **Tác giả Wan 2019.** PDF ghi Wan, Zhou, Li, Ding, Xu, Yang, Xia, Yin; Zotero ghi bộ khác (T09:L7). T09 chọn PDF. Mục Zotero `N54RGGHL` là bản trùng không tác giả (T15:L34).
15. **Hagedorn, Sedigh: lệch trang.** PDF có thêm 1 trang bìa kho lưu trữ nên số trang PDF lệch 1 so với trang in (T14:L10, L23; T18:L9, L18). Wu 2026: DOI chứa 2025 nhưng niên khóa 2026 (T18:L19).
16. **Mục tiêu thư viện trùng nhau.** T15:L59: tập 34 mục hiện hành khác ảnh chụp cũ (T17 có Keet & Khan, T15 thay bằng `LSYSC59G`). T16:L26-L27 xác nhận file #2 trùng #1 (Antunes). Có nhiều mục Zotero trùng (T15:L34-L39, L54).
17. **Tệp T13 tự khẳng định "Read completely" cho khoảng 25 tệp nguồn** (T13:L86-L115). Tôi không kiểm được; các tệp đó không thuộc nhóm C2.
18. **Số liệu dữ liệu G1 tự báo** (66/238/36/300/10/12 dòng, T13:L124-L132) kèm ghi "Referenced source registries, NPZ files ... are absent" (T13:L123) và thư mục `G1_EXECUTION_PACK/` không tồn tại (T13:L138). Không dùng làm số liệu Paper 2 khi chưa có nguồn.

---

## 7. Bảng bài

Quy ước.
- Giá trị tiêu chí: **Có / Một phần / Không / ?**. "Không" = tệp nêu rõ không có hoặc NOT_REPORTED. "?" = tệp không đủ dữ liệu hoặc chỉ có tóm tắt. "Có, hẹp" = có nhưng phạm vi hẹp (ghi rõ ngay sau).
- Tôi chấm theo nội dung các tệp C2, không đọc lại bài gốc. Kèm `Tnn:Lxx` để truy.
- Định nghĩa tôi áp: (2) = có neo bằng GlobalId được đối chiếu trên dữ liệu IFC thật trong bài, kể cả một lần chụp; (3) = phạm vi hiệu lực là TRƯỜNG bắt buộc của bản ghi bằng chứng (phạm vi ứng dụng của cả bài không tính); (4) = kiểm tại thời điểm dùng bằng chứng (kiểm lúc xuất/nhập/chuyển đổi chỉ tính "Một phần"); (5) = sự kiện chuyển trạng thái có căn cứ và có vai trò (cả hai); (7) = lỗi được chèn có chủ đích, có đối chứng/kết quả kỳ vọng (vi phạm thật phát hiện được không tính).
- Cột "Trang dẫn" = tệp nguồn của tôi có số trang PDF cho nhận định hay không.
- Tiêu chí (1)–(8) ứng với: (1) bằng chứng cảm biến/NDT; (2) neo BIM đối chiếu IFC xuất thật; (3) phạm vi hiệu lực bắt buộc; (4) kiểm tại lần dùng; (5) sự kiện chuyển trạng thái có căn cứ & vai trò; (6) xác minh sau sửa chữa; (7) đánh giá bằng lỗi chèn có đối chứng; (8) bối cảnh vận hành–bảo trì.

### 7A. Bài có ghi chú riêng hoặc đọc sâu (22 bài)

| # | Tác giả-năm | DOI ghi trong tệp | Mức đọc | Trang dẫn | Vai trò với Paper 2 | (1) | (2) | (3) | (4) | (5) | (6) | (7) | (8) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Fang et al. 2025 | 10.3390/buildings15224096 (T01:L3) | Toàn văn một phần: tr.1–~28/31, chưa đọc danh mục tài liệu (T01:L5) | Không | Tiền lệ cổng kiểm IfcGUID ở một bước chuyển (C1); không đụng C9 (T01:L33) | Không (T01:L11) | Có, hẹp: GUID qua 1 bước BIM→game engine (T01:L13, L15) | Không: chỉ nêu phạm vi ứng dụng (T01:L23) | Một phần: cổng kiểm ở bước chuyển, không ở lúc dùng (T01:L11) | Không (T01:L17-L19, L31) | Không (không nêu) | ? (T01:L29) | Không: thiết kế, nhà thông minh (T01:L23) |
| 2 | Borkowski et al. 2026 | 10.3390/technologies14070413 (T02:L3) [CẦN KIỂM] | Chỉ tóm tắt; không có PDF (T02:L5) | Không | Mối đe dọa tính mới: GUID đổi theo pha, đề xuất định danh bền vững (C1, C9) (T02:L33) | Không (T02:L17) | Một phần: nêu GUID khác nhau mỗi pha; ca Revit 3 phần tử × 3 pha (T02:L9, L15) | ? (T02:L23) | ? | Không (T02:L17-L19) | ? | ? (T02:L29) | Một phần: pha vận hành là 1 trong 3 pha, không nêu bảo trì (T02:L9) |
| 3 | Sacks et al. 2018 | 10.1016/j.autcon.2018.02.033 (T03:L3) | Toàn văn, 22 tr. (T03:L5) | Không (có Mục 6, Hình 9–10: T03:L19, L35) | Tiền lệ IDM/MVD và ba lớp lỗi kiểm tuân thủ; "không có soát xét/phê duyệt" (T03:L25) | Một phần: ảnh/điểm đám mây → khuyết tật; thiếu siêu dữ liệu thiết bị (T03:L11, L19) | Không (T03:L13) | Không: phạm vi chỉ ở cấp phương pháp (T03:L29) | Một phần: kiểm XBIM trên IFC đầu ra (T03:L33) | Không (T03:L23, L25) | Không nêu (T03; T17:L204: đóng/sửa chưa chứng minh) | Một phần: 3 lớp lỗi trên 4 cầu thật, không chèn lỗi (T03:L35) | Một phần: kiểm tra cầu, chưa tới bảo trì (T03:L9) |
| 4 | Stolk & McGlinn 2020 | Không ghi DOI (T04:L3) | Toàn văn, 14 tr. (T04:L5) | Không | Tiền lệ kiểm lược đồ ifcOWL (công cụ ngoài phạm vi) | Không (T04:L11) | Một phần: GUID chỉ là nút trong báo cáo; ifcOWL sinh từ R2RML, không là IFC xuất thật (T04:L11, L13) | Không (T04:L23) | Một phần: kiểm trước khi nhập lại CAD (T04:L9) | Không (T04:L19) | Không | Một phần: vi phạm thật, không chèn có đối chứng (T04:L27, L29) | Không |
| 5 | Oraskari et al. 2021 | Không ghi DOI (T05:L3) | Toàn văn, 10 tr. (T05:L5) | Không | Tiền lệ kiểm âm theo GUID (thiếu đối tượng/quan hệ), C1; cảnh báo SHACL bỏ qua đích thiếu (T05:L29, L33) | Không | Có, hẹp: đối chiếu GUID IFC↔LBD trên mẫu BOT Duplex; là chuyển định dạng, không qua phiên bản (T05:L13, L15) | Không (T05:L23) | Một phần: kiểm đơn vị sau chuyển đổi (T05:L27) | Không (T05:L17, L19) | Không | Một phần: luật bắt "thiếu đối tượng tương ứng"; chạy trên cặp đầu ra, không chèn lỗi (T05:L29, L33) | Không |
| 6 | Kücükavci et al. 2024 | 10.3233/SW-243595 (T06:L3) | Toàn văn, 24 tr. (T06:L5) | Không | Tiền lệ SHACL định lượng (ngoài phạm vi) | Không (T06:L11) | Không (T06:L13) | Không | Không | Không (T06:L17) | Không: có hai lượt kiểm sau sửa dữ liệu mô hình (372→14), không phải sửa chữa vật lý (T06:L21) | Một phần: 372 vi phạm thật, ràng buộc số lượng/giá trị, không chèn lỗi (T06:L27) | Không: giai đoạn thiết kế |
| 7 | Beach et al. 2015 | 10.1016/j.eswa.2015.02.029 (T07:L3) | Toàn văn, 29 tr. (T07:L5) | Không | Tiền lệ "unknown" thay vì suy NO; đối chứng thủ công (T07:L27, L29) | Không (T07:L17) | Không (T07:L13) | Một phần: luật "ngoài phạm vi trừ khi xác định được"; áp cho điều khoản, không cho bằng chứng (T07:L29) | Một phần: chạy lặp khi mô hình thay đổi (T07:L15, L27) | Không (T07:L19, L31) | Không | Không: đối chứng là đánh giá thủ công, không chèn lỗi (T07:L27, L29) | Không: thiết kế |
| 8 | Ciccarese et al. 2013 | 10.1186/2041-1480-4-37 (T08:L3) | Toàn văn, 22 tr. (T08:L5) | Không (Bảng 1–3, Hình 2, 4, 5, 14: T08:L15, L23) | Từ vựng vai trò/phiên bản (C6, revision_of); không BIM | Không (T08:L19) | Không (T08:L13) | Không (T08:L29) | Không | Một phần: vai trò author/curator/creator + thời điểm; không có phê duyệt (T08:L23-L25, L37) | Không | Không (T08:L35) | Không |
| 9 | Wan et al. 2019 | 10.3390/su11174583 (T09:L3) | Toàn văn, 17 tr. (T09:L5) | Không (Bảng 1–4, Hình 1, 11–16: T09:L13) | Tiền lệ vận hành kiểm tra→sửa chữa→quản lý kiểm; so với B0 (T09:L27, L41) | Một phần: thuộc tính vết nứt, ảnh/video; thiếu siêu dữ liệu thiết bị (T09:L21) | Một phần: GUID ngầm định (T09:L15) | Không nêu | Không nêu | Một phần: quản lý kiểm tra tường thuật, không trường lược đồ (T09:L27, L39) | Một phần: quản lý kiểm kết quả sửa chữa, tường thuật (T09:L27) | Không (T09:L37) | Có (T09:L31) |
| 10 | Lee, Eastman & Solihin 2021 | 10.1093/jcde/qwaa064 (T10:L3) | Toàn văn 18 tr. nhưng chưa đọc mức dòng (T10:L5, L29) | Không | Tiền lệ kiểm GUID trong một lần trao đổi (C1) | Không (T10:L11) | Có, hẹp: quy tắc GUID trên dữ liệu trao đổi thật; một chu kỳ xuất–nhập (T10:L13, L15, L27) | Không (T10:L23) | Một phần: kiểm lúc trao đổi (T10:L9) | Không (T10:L17, L19) | Không | ? (T10:L29 "YES" so với T17:L32 "không phải fixture có kiểm soát") | Không |
| 11 | Lorvão Antunes et al. 2024 | 10.1016/j.iswa.2024.200366 (T11:L3) | Toàn văn, 14 tr. (T11:L5) | Rời rạc: "p.9 of extract", "p.7" (T11:L11, L17) | Đối thủ gần nhất chuỗi cảm biến→GUID; khoảng trống: phiên bản, soát xét (T11:L15, L25) | Một phần: SOSA/SSN, kết quả 1–5, không hiệu chuẩn/độ bất định (T11:L11, L19) | Có, hẹp: `ifc:globalId_IfcRoot` qua SPARQL, 3 dự án; ánh xạ thủ công, không xét phiên bản (T11:L11, L15) | Không: phạm vi thí điểm nêu như giới hạn (T11:L29) | Không nêu | Không (T11:L25); chỉ có `prov:atTime` (T11:L37) | Không nêu | Không (T11:L35) | Có (T11:L9) |
| 12 | Kim et al. 2018 | 10.1016/j.autcon.2017.12.019 (T12:L3) | Toàn văn 15 tr. (T12:L5); đọc sâu lại ở T16 | Có ở T16 (PDF tr.4–14: T16:L84-L92) | Tiền lệ nối bản ghi công việc FM–IFC; cảnh báo `#id` STEP (T12:L13; T16:L98) | Không (T12:L19) | Không: dùng `#id` STEP; mô hình mẫu buildingSMART (T12:L13, L27; T16:L88) | Không | Không nêu | Không (T12:L25; T16:L102) | Không | Không (T12:L35; T16:L109) | Có (T12:L9) |
| 13 | Piras et al. 2026 | 10.3390/app16104642 (T14:L20, L29) | Toàn văn, 32 tr.; SHA-256 PDF khớp (T14:L20) | Có: PDF tr. (T14:L33-L40) | Đối thủ BIM–CMMS, neo GlobalId (C1); "claim boundary" (T14:L40) | Không: dữ liệu tĩnh, không luồng IoT/BMS (T14:L38) | Có: `IfcGlobalId`→mã tài sản OpenMAINT, 428 tài sản; không ghi trùng/mồ côi (T14:L35, L37; tr.10–11, 18, 20–24) | Không: giữ chỗ N/A/999 vẫn đủ trường (T14:L38) | Một phần: kiểm buildingSMART khi xuất/nhập (T14:L36) | Không: chưa có lệnh công việc, không ghi hoàn thành (T14:L37, L40) | Không (T14:L40, L42) | Không: chỉ đường dương (T14:L36) | Có (T14:L33) |
| 14 | Li et al. 2023 | 10.1038/s41598-023-27924-6 (T14:L21, L46) | Toàn văn, 16 tr. (T14:L21) | Có: PDF tr. (T14:L50-L57) | Đối thủ vận hành khuyết tật→sửa chữa→`completed` (T14:L57) | Không: kiểm tra thủ công, cảm biến là hướng tương lai (T14:L55-L56; PDF tr.13) | Một phần: ID khuyết tật nội bộ; Revit→OBJ mất tham số; không GlobalId (T14:L52, L55) | Không | Không (T14:L55) | Một phần: cờ `completed` vô hướng, không thời điểm/người thực hiện; biểu mẫu có recorder/reviewer (T14:L52, L54, L57) | Không: không nối với kiểm tra lại (T14:L54) | Không (T14:L53) | Có (T14:L50) |
| 15 | Nuyts et al. 2024 | 10.1016/j.aei.2024.102443, kiểm Crossref/OpenAlex (T14:L22, L63) | Chỉ tóm tắt theo T14:L22, L65; T15:L75 ghi "toàn văn + OSF" (mâu thuẫn) | Không | Tiền lệ bộ dữ liệu cặp đúng/sai ở mức chung (tiêu chí 7) (T15:L198) | Không (T15:L174) | Một phần (T15:L174) | ? | ? | Không (T15:L174) | Không (T15:L174) | Có, hẹp (mức sàng lọc): cặp tuân thủ/không tuân thủ, không oracle chính xác (T15:L75, L198); T14:L124 chưa xác minh lại | Không |
| 16 | Hagedorn et al. 2023 | 10.1016/j.autcon.2023.105106 (T14:L23, L73) | Toàn văn, 23 tr. PDF (22 tr. in) (T14:L23) | Có: PDF tr. kèm [tr. in] (T14:L77-L84) | Tiền lệ SHACL kiểm liên kết chéo miền, thuận/nghịch; dạng chung làm yếu Gap 3 (T14:L86) | Không (T14:L79) | Một phần: định danh chuỗi/URI trong ICDD; thực thể IFC thiếu sau chuyển RDF thì không có bộ ba (T14:L77, L82) | Không | Một phần: kiểm SHACL chạy trên bộ dữ liệu (T14:L80-L81) | Không (T14:L82) | Không | Không: vi phạm có trong dữ liệu, không chèn đột biến có oracle (T14:L82; T15:L175) | Không: 4D tiến độ (T14:L79) |
| 17 | Sedigh & Müller 2025 | 10.1088/1742-6596/3140/4/042023 (T18:L18, L25) | Toàn văn, 8 tr. (T18:L18) | Có: PDF tr. [tr. in] (T18:L27-L36) | Tiền lệ cảm biến↔GUID↔IFC xuất lại (T18:L38) | Có: BACnet AHU (cảm biến, không phải NDT) (T18:L30-L31) | Có: `Asset Identifier`→`GlobalId` bằng JSON; IFC từ Revit (T18:L30, L32) | Không | Không (T18:L34) | Không (T18:L31, L36) | Không | Không (T18:L32, L34) | Một phần: vận hành/bàn giao, không bảo trì (T18:L29, L36) |
| 18 | Wu et al. 2026 | 10.1016/j.eswa.2025.130514 (T18:L19, L42) | Toàn văn, 12 tr. (T18:L19) | Có: PDF tr. (T18:L44-L53) | Tiền lệ khung HITL; giới hạn "bi-directional" (T18:L53, L109) | Không: ML chỉ đề xuất, chưa triển khai (T18:L47, L49) | Không: tích hợp BIM chưa giải (T18:L51) | Không | Không | Một phần: HITL/điểm soát xét, chưa kiểm vai trò/lịch sử (T18:L64, L66) | Không | Không: khảo sát chuyên gia (T18:L49) | Không: kiểm toán trước phá dỡ/cải tạo (T18:L46) |
| 19 | Keet & Khan 2025 | Không ghi DOI; CEUR-WS ISSN 1613-0073 (T16:L46) | Toàn văn; hình không xem (T16:L18, L44-L73) | Có: PDF tr. (T16:L51-L59) | Phương pháp CQ (không phải nội dung miền) | Không (n/a: miền trung tính, T16:L70) | Không (n/a) | Không (n/a) | Không (n/a) | Không (n/a) | Không (n/a) | Không (n/a; T16:L69) | Không (n/a) |
| 20 | Jia et al. 2025 | 10.3390/buildings15152633 (T16:L118) | Toàn văn; hình không xem (T16:L18, L116-L147) | Có: PDF tr. (T16:L123-L131) | Tiền lệ luật thực thi; cảnh báo liên kết dẫn xuất (T16:L130, L241) | Không (T16:L143) | Một phần: cá thể IfcOWL, không quản trị GlobalId (T16:L137) | Một phần: "tiền điều kiện" của điều khoản, không phải của bằng chứng (T16:L123) | Một phần: truy vấn chạy trên mô hình tại lúc kiểm (T16:L129) | Không (T16:L143) | Không (T15:L113) | Không: 2 lan can 900 mm không chèn có chủ đích (T16:L129, L141) | Không: thiết kế (T16:L143) |
| 21 | Lee D. et al. 2021 | 10.1016/j.autcon.2021.103688 (T16:L153) | Toàn văn; hình không xem (T16:L18, L151-L178) | Có: PDF tr. (T16:L158-L163) | Tiền lệ trạng thái bất biến/chữ ký; tệp đề xuất REJECT blockchain (T16:L163, L251) | Không: cảm biến giả định (T16:L160) | Không: ID viên gạch (T16:L174) | Không | Không | Một phần: chuỗi khối có thời điểm; không mô hình vai trò/lý do (T16:L169, L172) | Không | Một phần: 3/10 nút bị chèn chữ ký sai, kết quả kỳ vọng đúng; thuộc đồng thuận sổ cái (T16:L161, L171) | Không |
| 22 | Pauwels & Terkaj 2016 | 10.1016/j.autcon.2015.12.003 (T16:L184) | Toàn văn; hình không xem (T16:L18, L182-L207) | Có: PDF tr. [tr. in] (T16:L189-L194) | Căn cứ "lớp ràng buộc IFC không sang OWL" (T16:L191) | Không | Không: không quản trị định danh (T16:L203) | Không | Không | Không | Không | Không (T16:L205) | Không |

### 7B. Bài chỉ có ghi chú sàng lọc (không có bản đọc sâu trong nhóm C2)

Cột "Trang dẫn": Không với toàn bộ bảng này (T15, T17 không có số trang). Mức đọc = tiêu đề/tóm tắt/ghi chú Zotero hoặc "đọc có mục tiêu"; chấm tiêu chí dựa ma trận T15:L169-L179 và các bảng sàng lọc.

| # | Tác giả-năm | DOI ghi trong tệp | Mức đọc (theo tệp) | Vai trò với Paper 2 | (1) | (2) | (3) | (4) | (5) | (6) | (7) | (8) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 23 | Bellon et al. 2025 | Không ghi DOI | Chưa đủ toàn văn: "paywalled at entity level" (T16:L259); T17 sàng lọc, P1 (T17:L26) | Đối thủ lược đồ gần nhất (T17:L14); liên quan B1 | ? | Một phần (T17:L201: định danh quản trị chưa xác nhận) | ? | ? | Một phần: lược đồ bảo trì/chi phí, chưa thấy Status_Event (T17:L201) | ? | Không (T17:L201) | Có (T17:L26) |
| 24 | Xu et al. 2022 | Không ghi DOI | Chỉ tóm tắt; không có PDF (T17:L29, L214) | Biểu diễn khuyết tật–hành động bảo trì trong IFC | Một phần: hình học khuyết tật tham số (T17:L29) | Một phần: quan hệ thực thể IFC (T17:L203) | ? | ? | Một phần: hành động bảo trì có, trạng thái sự kiện chưa thấy (T17:L203) | ? | Không (T17:L203) | Một phần |
| 25 | Isailović et al. 2020 | Không ghi DOI | Đã đọc sâu ở vòng trước (T15:L13); ở đây chỉ ma trận (T17:L31) | Hồ sơ ngữ cảnh phát hiện (ngày, loại, mức độ) | Một phần: phát hiện hư hỏng, so với cơ sở thủ công (T17:L31) | Một phần: liên kết tới phần tử (T17:L31) | Không (T17:L105: ngữ cảnh có, không là trường phạm vi) | ? | Không: chưa mã hóa người soát xét (T17:L31) | Không (T17:L31) | Không (T17:L31) | Một phần |
| 26 | Hüthwohl et al. 2018 | Không ghi DOI | Abstract + ghi chú Zotero; không có PDF (T15:L29; T17:L34) | Lược đồ khuyết tật/kiểm tra cầu BTCT | ? | ? | ? | ? | ? | ? | ? | Một phần |
| 27 | Theiler & Smarsly 2018 | Không ghi DOI | Sàng lọc (T15:L30; T17:L39) | Lược đồ IFC Monitor, tiền lệ mô hình cố ý sai | Có: lược đồ cảm biến SHM (T17:L39) | Một phần: định danh lược đồ (T17:L39) | ? | ? | Không | Không | Một phần: kiểm mô hình cố ý sai; chưa đạt tiêu chí bốn phần (T15:L30) | Không: giám sát, không bản ghi hành động |
| 28 | Theiler et al. 2017 | Không ghi DOI | Sàng lọc (T15:L45; T17:L41) | Ứng dụng IFC Monitor cho SHM phòng thí nghiệm | Có (T17:L41) | ? | ? | ? | Không | Không | Không (T17:L41) | Không |
| 29 | Quinn et al. 2020 | Không ghi DOI | Sàng lọc (T15:L41; T17:L42) | Trạng thái thời gian BAS ↔ BIM | Có: ~10.000 điểm BAS (T17:L42) | Một phần: chuỗi đặt tên, không GlobalId (T17:L42) | ? | ? | Không | Không | Không (T17:L42) | Một phần: vận hành tòa nhà |
| 30 | Carvalho et al. 2023 | Không ghi DOI | Sàng lọc; tóm tắt/ghi chú (T15:L40; T17:L43) | Phiếu bảo trì gắn Element ID | Không | Một phần: Element ID (T15:L40) | ? | ? | Không (T15:L40; T17:L43) | ? | Không (T17:L43) | Có |
| 31 | Wang et al. 2024 | Không ghi DOI | Tóm tắt/siêu dữ liệu nhà xuất bản (T17:L35) | Ràng buộc WHERE→SHACL cho ifcOWL | Không | ? | ? | ? | Không | Không | Không: không có fixture miền (T15:L53) | Không |
| 32 | Yang et al. 2025 | Không ghi DOI | Sàng lọc có mục tiêu; không vào hàng đợi (T15:L55, L138-L146) | Giám sát thực địa BIM–DT–IoT | Có: chuỗi thời gian thực địa 22/10–07/11/2024 (T15:L143) | Một phần: không hợp đồng GlobalId (T15:L150) | ? | ? | Một phần: cờ cảnh báo, không sự kiện (T15:L153) | Không (T15:L159) | Không (T15:L156) | Có |
| 33 | Celik et al. 2023 | 10.1016/j.compind.2022.103768 (T15:L255) | Sàng lọc; T16:L34 ghi "đã đọc sâu Round 3B" (không có bản trong nhóm) | Nguồn gốc giao dịch BIM, trách nhiệm | Không | Một phần (T15:L177) | ? | ? | Một phần: giao dịch, phiên bản, vai trò/trách nhiệm cho thông tin thiết kế–thi công (T15:L52, L177) | Không | Không (T15:L177) | Không: thiết kế/thi công (T15:L52) |
| 34 | Mohamed et al. 2023 | 10.3390/buildings13112798 (T15:L77) | Sàng lọc, toàn văn nhà xuất bản "inspected" (T15:L77); chưa có bản đọc sâu | Lịch sử sửa/chưa sửa, trạng thái hiện tại | ? | Có (T15:L173) | ? | ? | Một phần: trạng thái hiện tại là trường (T15:L173, L185) | Không (T15:L173) | Không (T15:L173) | Có (T15:L77) |
| 35 | Jeon et al. 2023 | 10.3390/buildings13092332 (T15:L78) | Sàng lọc, toàn văn mở (T15:L78) | Mã kho cầu, thông tin kiểm tra | ? | Một phần (T15:L176) | ? | ? | Không (T15:L176) | Không | Không | Có |
| 36 | Jaskula et al. 2025 | 10.1061/JCEMD4.COENG-14852 (T15:L79) | Siêu dữ liệu + bản thảo tác giả (T15:L79) | Yêu cầu lịch sử tài sản bất biến (khái niệm) | Không | Không (T15:L179) | ? | ? | Một phần: khái niệm, chưa thao tác (T15:L179, L189) | Không | Không | Một phần |
| 37 | Schuler et al. 2025 | 10.1007/978-3-031-84224-5_32 (T15:L80) | Chỉ xác minh điểm cuối nhà xuất bản (T15:L80) | Container ICDD cho thí nghiệm vật liệu cầu | Một phần: thử vật liệu → kết quả (T15:L80) | Một phần (T15:L178) | ? | ? | Không (T15:L178) | Không | Không | Một phần |
| 38 | Pauwels et al. 2024 | 10.1016/j.aei.2024.102426 (T15:L81) | Toàn văn mở, xác minh (T15:L81) | Kiểm yêu cầu kỹ thuật BIM | Không | ? | ? | ? | Không | Không | Một phần: điều kiện kích thước sai đã biết (T15:L81) | Không |
| 39 | Oliveira et al. 2024 | 10.36680/j.itcon.2024.014 (T15:L82) | Toàn văn mở (T15:L82) | Yêu cầu thông tin FM theo chuẩn | Không | ? | ? | ? | Không | Không | Không | Có (T15:L82) |
| 40 | Cerovšek & Omar 2025 | 10.3390/buildings15152621 (T15:L83) | Toàn văn mở, "inspected" (T15:L83) | Kiểm tính tương thích công cụ IDS | Không | ? | ? | ? | Không | Không | Không: khác biệt giữa công cụ, không là oracle (T15:L83) | Không |
| 41 | Cavieres-Lagos et al. 2024 | 10.3390/app14146209 (T15:L84) | Toàn văn mở (T15:L84) | Trao đổi hai chiều Revit–Dynamo–Excel, cầu đường sắt | Không | ? | ? | ? | Không (T15:L84) | Không | Không | Có |
| 42 | Jeon et al. 2024 | 10.3390/buildings14124032 (T15:L85) | Toàn văn mở, "inspected" (T15:L85) | Quan sát tình trạng sau sửa nhưng không mã hóa xác minh | ? | ? | ? | ? | Không | Một phần: ghi tình trạng sau sửa, không gắn đóng việc (T15:L85, L236) | Không | Có |
| 43 | Gao et al. 2024 | 10.3390/buildings14123731 (T15:L86) | Toàn văn mở (T15:L86) | Bối cảnh GIS–BIM cầu | ? | Không: không ID liên hệ thống ổn định (T15:L86) | ? | ? | Không | Không | Không | Một phần |
| 44 | Armijo & Zamora-Sánchez 2024 | Không ghi DOI | Loại khỏi hàng đợi (T15:L33; T17:L54) | Ngoài phạm vi (SHM/cảnh báo ML) | Có: gia tốc kế (T17:L54) | ? | ? | ? | ? | ? | ? | ? |
| 45 | Monfardini et al. 2023 | Không ghi DOI | Sàng lọc (T15:L35; T17:L47); bản trùng bị loại | Khảo sát CQ, 63 người | Không áp dụng | Không áp dụng | Không áp dụng | Không áp dụng | Không áp dụng | Không áp dụng | Không áp dụng | Không áp dụng |
| 46 | Du et al. 2024 | Không ghi DOI | Sàng lọc (T17:L53) | Bối cảnh sẵn sàng dữ liệu IFC/AI | Không áp dụng | Không áp dụng | Không áp dụng | Không áp dụng | Không áp dụng | Không áp dụng | Không áp dụng | Không áp dụng |
| 47 | Rasmussen et al. 2020 (BOT) | Không ghi DOI | Sàng lọc (T15:L48) | Quan hệ tô-pô nhẹ, căn với IFC | Không áp dụng | ? | Không áp dụng | Không áp dụng | Không áp dụng | Không áp dụng | Không áp dụng | Không áp dụng |
| 48 | Chuẩn/đặc tả: buildingSMART IfcRoot 2024; ISO 55000:2024; GSA BIM Guide 08 (2011); PROV-DM, PROV-O 2013 | Không ghi DOI | Sàng lọc (T15:L42-L49; T17:L37, L50-L53) | Nền định danh/từ vựng. GSA yêu cầu GUID + Asset ID bền vững (T17:L50) | Không áp dụng | Có (yêu cầu, không phải nghiên cứu; buildingSMART T17:L37, GSA T17:L50) | Không áp dụng | Không áp dụng | Không áp dụng | Không áp dụng | Không áp dụng | Không áp dụng |

Ghi chú Bảng bài.
- Bảng 7A–7B đủ 48 dòng, gồm cả bài trùng với tập đã đọc sâu ở vòng trước nhưng chỉ có ma trận trong nhóm C2 (Bellon, Xu, Isailović).
- Boje 2020, Chen 2026 (ITcon), Johannes 2021 được T16:L35-L37 nhắc nhưng KHÔNG có dòng riêng: T16 chỉ ghi "không đọc" và vai trò (nền Chương 2, sinh mô hình IFC, độ trưởng thành). Yang S.-W. 2025 (T16:L38) đã vào dòng 32 nhờ T15:L55.
- Không có DOI trong tệp nghĩa là "tệp không ghi", chưa nói bài không có DOI. Theo quy tắc 2 và 4 của project, DOI/đường dẫn nào chưa kiểm bằng công cụ: [CẦN KIỂM]. DOI nào tệp ghi đã kiểm bằng công cụ: Piras (T14:L20), Li (T14:L21), Nuyts (T14:L22), Hagedorn (T14:L23), Sedigh/Wu (T18:L18-L19); các DOI còn lại là tự báo.

---

## 8. Giao diện G1→G2 (T13) đối chiếu với trường EVIDENCE đã khóa

Nguồn: `G1_TO_G2_CONDITION_EVIDENCE_INTERFACE_v1.0.md` (T13), mục 7–8, 12.3. Trường EVIDENCE khóa (theo yêu cầu giao việc): `Condition_Evidence_ID, evidence_type, BIM_GUID (n:m), Sensor_ID, value, uncertainty, method_version, scope.{inference_unit, data_split, install_batch, applicable_conditions}, obs_context, created_at, revision_of`.
Tôi chỉ có TÊN các trường khóa, không có định nghĩa chi tiết. Chỗ nào phải đoán nghĩa của tên, ghi [CẦN XÁC NHẬN].
Quy ước cột đối chiếu: **Khớp** (cùng nghĩa, có thể khác cách viết); **Khác tên** (cùng nghĩa gần đúng, tên/cấu trúc khác); **Thừa** (không có trường khóa tương ứng); **Thiếu** (trường khóa không có tương ứng trong giao diện).

### 8.1 Các trường giao diện yêu cầu cho EVIDENCE (52 trường tiêu đề + liên kết)

| Nhóm (mục) | Trường giao diện | Bậc/Bắt buộc (T13) | Dòng | Đối chiếu trường EVIDENCE khóa |
|---|---|---|---|---|
| 7.1 Định danh | `Condition_Evidence_ID` | 1, bắt buộc, duy nhất, không dùng lại | L290 | Khớp `Condition_Evidence_ID` |
| 7.1 | `Evidence_Record_Version` | 1, bắt buộc, tăng đơn điệu trong chuỗi thay thế | L291 | Thừa (khóa chỉ có `revision_of`); liên quan `revision_of` |
| 7.1 | `Evidence_Status` (DRAFT, FOR_REVIEW, VERIFIED_EVIDENCE, REJECTED, SUPERSEDED, WITHDRAWN) | 1, bắt buộc | L292, L554-L561 | Thừa (vòng đời của bằng chứng) |
| 7.1 | `Supersedes_Condition_Evidence_ID` | 0..1, có điều kiện; phải tồn tại, không tự tham chiếu | L293 | Khác tên `revision_of` |
| 7.2 Nguồn | `Source_Data_ID` | 1 chính; bắt buộc | L299 | Thừa |
| 7.2 | `Source_File_SHA256` | 1 mỗi tệp; bắt buộc | L300 | Thừa |
| 7.2 | `Campaign_ID` | 1; bắt buộc | L301 | Thừa (có thể thuộc `obs_context`) [CẦN XÁC NHẬN] |
| 7.2 | `Acquisition_Session_ID` | 1; bắt buộc cho bàn giao | L302 | Thừa (có thể thuộc `obs_context`) [CẦN XÁC NHẬN] |
| 7.2 | `Run_ID` | 1; bắt buộc | L303 | Thừa; có thể là giá trị của `scope.inference_unit` hoặc thuộc `obs_context` [CẦN XÁC NHẬN]. D003/D004: run chưa là đơn vị độc lập đã kiểm (T13:L17) |
| 7.2 | `Recording_ID` | 0..1 tiêu đề, 1..* qua liên kết; có điều kiện | L304 | Thừa |
| 7.2 | `Observation_Start_Time` | 1; bắt buộc | L305 | Khác tên: thuộc `obs_context` [CẦN XÁC NHẬN] |
| 7.2 | `Observation_End_Time` | 1; bắt buộc | L306 | Khác tên: thuộc `obs_context` [CẦN XÁC NHẬN] |
| 7.3 Cảm biến | `Sensor_Mode_ID` | 1; bắt buộc; khai báo định danh vật lý hay "legacy block" | L312 | Thừa |
| 7.3 | `Primary_Sensor_ID` | 0..1; tùy chọn | L313 | Thừa (một phần liên quan `Sensor_ID`) |
| 7.3 | `Condition_Evidence_Sensor_Link` (`Sensor_ID`, `Sensor_Role`, `Channel_or_Axis`, `Contribution_Context`, `Link_Status`) | 1..*; bắt buộc | L314, L395-L411 | Khác cấu trúc `Sensor_ID`: giao diện là bảng liên kết nhiều cảm biến, khóa duy nhất 4 cột (L408) |
| 7.3 | `Channel_Schema_ID` | 1; bắt buộc | L315 | Thừa |
| 7.3 | `Axis_Context` | 1 tóm tắt; bắt buộc | L316 | Thừa (có thể thuộc `obs_context`) |
| 7.3 | `Sampling_Rate_Hz` | 1 mỗi lược đồ kênh; bắt buộc | L317 | Thừa (có thể thuộc `obs_context`) |
| 7.4 Xử lý | `Preprocessing_Spec_ID` | 1; bắt buộc | L323 | Thừa; có thể gộp vào `method_version` [CẦN XÁC NHẬN] |
| 7.4 | `Windowing_Spec_ID` | 1 nếu dựa cửa sổ; có điều kiện | L324 | Thừa; như trên |
| 7.4 | `Aggregation_Rule_ID` | 1; bắt buộc | L325 | Thừa; như trên |
| 7.4 | `Model_Name` | 1; bắt buộc nếu dựa mô hình | L326 | Khác tên: một phần `method_version` |
| 7.4 | `Model_Version` | 1; bắt buộc nếu dựa mô hình | L327 | Khác tên: một phần `method_version` |
| 7.4 | `Model_Config_ID` | 1; bắt buộc nếu dựa mô hình | L328 | Thừa; như trên |
| 7.4 | `Evaluation_Protocol_ID` | 1; bắt buộc | L329 | Thừa |
| 7.4 | `Split_or_Fold_ID` (+ `Condition_Evidence_Fold_Link`: `Split_or_Fold_ID`, `Fold_Role`, `Result_Reference`) | 0..1 tiêu đề, 1..* qua liên kết; bắt buộc cho kết quả mô hình | L330, L476-L489 | Khác tên `scope.data_split` |
| 7.4 | `Code_Commit` | 1; bắt buộc cho bàn giao | L331 | Thừa |
| 7.4 | `Environment_ID` | 1; bắt buộc | L332 | Thừa |
| 7.5 Nội dung | `Evidence_Type` (chỉ `LAB_STATE_EVIDENCE`, `LAB_STATE_CHANGE_EVIDENCE`) | 1; bắt buộc | L338, L202-L203 | Khớp `evidence_type` về tên; tập giá trị chỉ 2 loại phòng thí nghiệm [CẦN XÁC NHẬN tập giá trị khóa] |
| 7.5 | `Evidence_Granularity` (WINDOW/RECORDING/RUN/CAMPAIGN) | 1; bắt buộc | L339 | Khác tên: gần nghĩa `scope.inference_unit` [CẦN XÁC NHẬN] |
| 7.5 | `Evidence_Result` | 1; bắt buộc; "no hidden scalar collapse" | L340 | Khác tên `value` |
| 7.5 | `Predicted_or_Observed_State` | 1; bắt buộc | L341 | Khác tên: một phần `value` |
| 7.5 | `CEI` (validity, model confidence, run/fold variability, sensor configuration, data quality, provenance, timestamp/version) | 1; bắt buộc; "never a universal scalar" | L342, L185 | Khác tên và khác cấu trúc `uncertainty` |
| 7.5 | `Quality_or_Confidence` | 1; bắt buộc; phải bằng khối con của CEI | L343 | Khác tên: một phần `uncertainty` |
| 7.5 | `Quality_Flag` (15 giá trị) | 1..*; bắt buộc, `NO_FLAG` khi không có | L344, L205-L223 | Thừa |
| 7.5 | `Limitation_Context` | 1..*; bắt buộc; "structured text/reference" | L345 | Khác tên rất gần: tương ứng một phần `scope.applicable_conditions`; không có cấu trúc kiểm được (xem 8.3) |
| 7.5 | `Evidence_Interpretation_Boundary` | 1; bắt buộc | L346 | Thừa / tương ứng một phần `scope.applicable_conditions` (chỉ ranh giới "không chẩn đoán, không hành động") |
| 7.6 BIM | `Candidate_Asset_ID` | 1; bắt buộc cho tính đủ điều kiện G2 | L352 | Thừa |
| 7.6 | `Candidate_BIM_GUID` | 0..1; tùy chọn khi UNBOUND | L353 | Khác tên: một dòng của `BIM_GUID` (n:m) |
| 7.6 | `Model_Version_ID` | 0..1; bắt buộc khi có GUID | L354 | Thừa (không có trường khóa; liên quan C9 phiên bản) |
| 7.6 | `BIM_Link_Status` (UNBOUND, CANDIDATE, VERIFIED, REJECTED, SUPERSEDED) | 1; bắt buộc | L355, L527-L533 | Thừa |
| 7.6 | `BIM_Binding_ID` (+ thực thể `BIM_Binding`: `BIM_Binding_ID`, `Condition_Evidence_ID`, `Asset_ID`, `BIM_GUID`, `Model_Version_ID`, `Binding_Status`, `Binding_Method`, `Binding_Evidence_Reference`, `Verified_By`, `Verified_At`) | 0..1 hoạt động; 0..* lịch sử | L356, L429-L449 | Khác cấu trúc `BIM_GUID n:m`: n:m thể hiện qua nhiều dòng `BIM_Binding` (xem 8.3) |
| 7.6 | `Binding_Evidence_Reference` | 0 khi UNBOUND, 1..* từ CANDIDATE | L357 | Thừa |
| 7.7 Trách nhiệm | `Created_By` | 1; bắt buộc | L363 | Thừa |
| 7.7 | `Created_At` | 1; bắt buộc; chỉ thêm | L364 | Khớp `created_at` |
| 7.7 | `Reviewed_By` | 0..1; bắt buộc cho VERIFIED_EVIDENCE | L365 | Thừa |
| 7.7 | `Reviewed_At` | 0..1 | L366 | Thừa |
| 7.7 | `Review_Status` (NOT_REVIEWED, APPROVED, REJECTED) | 1; bắt buộc | L367, L597-L603 | Thừa |
| 7.7 | `Review_Rationale` | 0..1; bắt buộc khi soát xét xong | L368 | Thừa |
| 7.8 Quản trị hạ nguồn | `Eligible_For_G2_Traceability` | 1; bắt buộc | L374 | Thừa |
| 7.8 | `Eligible_For_Inspection_Review` | 1; bắt buộc | L375 | Thừa |
| 7.8 | `Downstream_Use_Limitation` | 1..*; bắt buộc | L376 | Thừa; tương ứng một phần `scope.applicable_conditions` |
| 8 Liên kết (không nằm tiêu đề) | `Condition_Evidence_Window_Link`, `Condition_Evidence_Source_Link`, `Condition_Evidence_Recording_Link` | 1..* khi dựa cửa sổ/nguồn/recording | L413-L427, L456-L473 | Thừa |
| 12.3 Sự kiện | `Evidence_Status_Event` (`Evidence_Status_Event_ID`, `Condition_Evidence_ID`, `Previous_Evidence_Status`, `New_Evidence_Status`, `Changed_By`, `Changed_At`, `Change_Reason`, `Authorization_Reference`) | 1..* mỗi CE; bất biến | L578-L595 | Thừa so với EVIDENCE; dễ nhầm với STATUS_EVENT của chuỗi ACTION (xem mục 4) |

Tổng: 52 trường tiêu đề (7.1–7.8) + 7 thực thể liên kết (Sensor, Window, BIM_Binding, Source, Recording, Fold, Evidence_Status_Event). 19 sổ bàn giao G1 (T13:L243-L261) không được tính ở đây vì không phải trường của một bản ghi bằng chứng.

### 8.2 Trường EVIDENCE khóa → tương ứng trong giao diện

| Trường EVIDENCE khóa | Tương ứng trong T13 | Kết luận |
|---|---|---|
| `Condition_Evidence_ID` | `Condition_Evidence_ID` (L290) | Khớp |
| `evidence_type` | `Evidence_Type` (L338), 2 giá trị (L202-L203) | Khớp tên; giá trị khác phạm vi [CẦN XÁC NHẬN] |
| `BIM_GUID` (n:m) | `Candidate_BIM_GUID` 0..1 (L353) + `BIM_Binding` (L429-L449) | Khác cấu trúc: 1 CE có tối đa 1 liên kết VERIFIED hoạt động (L445, L544); một-nhiều là ngoại lệ, "list of GUIDs prohibited" (L495) |
| `Sensor_ID` | `Condition_Evidence_Sensor_Link.Sensor_ID` (L398), `Primary_Sensor_ID` (L313) | Khác cấu trúc (bảng liên kết, thêm Role/Channel) |
| `value` | `Evidence_Result` (L340) + `Predicted_or_Observed_State` (L341) | Khác tên (tách hai trường) |
| `uncertainty` | `CEI` (L342) + `Quality_or_Confidence` (L343) | Khác tên, khác cấu trúc: CEI đa chiều, cấm dạng vô hướng/Health Index (L342, L185, L673) |
| `method_version` | `Model_Name`, `Model_Version`, `Model_Config_ID`, `Aggregation_Rule_ID`, `Preprocessing_Spec_ID`, `Windowing_Spec_ID`, `Evaluation_Protocol_ID`, `Code_Commit`, `Environment_ID` (L323-L332) | Khác tên; giao diện chi tiết hơn nhiều |
| `scope.inference_unit` | `Evidence_Granularity` (L339), `Run_ID` (L303) | Khác tên [CẦN XÁC NHẬN]; đơn vị độc lập chưa chốt (D003/D004, T13:L17; mục 19 số 1) |
| `scope.data_split` | `Split_or_Fold_ID` + `Condition_Evidence_Fold_Link` (L330, L476-L489) | Khác tên |
| `scope.install_batch` | Không có | Thiếu. Gần nhất: `Campaign_ID`/`Acquisition_Session_ID` (L301-L302), là lô thí nghiệm chứ không là lô lắp đặt cảm biến [CẦN XÁC NHẬN] |
| `scope.applicable_conditions` | Không có trường cấu trúc. Gần nhất: `Limitation_Context` (L345), `Evidence_Interpretation_Boundary` (L346), `Downstream_Use_Limitation` (L376) | Thiếu ở dạng trường kiểm được; chỉ có văn bản có cấu trúc và ranh giới "không chẩn đoán/không hành động" |
| `obs_context` | `Observation_Start_Time`/`Observation_End_Time` (L305-L306), `Campaign_ID`, `Acquisition_Session_ID`, `Run_ID`, `Recording_ID`, `Axis_Context`, `Sampling_Rate_Hz` | Khác tên; nhiều trường [CẦN XÁC NHẬN phạm vi `obs_context`] |
| `created_at` | `Created_At` (L364) | Khớp |
| `revision_of` | `Supersedes_Condition_Evidence_ID` (L293) + `Evidence_Record_Version` (L291) | Khác tên; thêm quy tắc không chu trình, một người kế nhiệm (L643, L646) |

### 8.3 Tóm tắt thừa / thiếu / khác tên

**Khớp (3):** `Condition_Evidence_ID`; `created_at` (`Created_At`); `evidence_type` (khớp tên, tập giá trị cần xác nhận).

**Khác tên hoặc khác cấu trúc (9 trường khóa):** `revision_of` ← `Supersedes_Condition_Evidence_ID` (+ `Evidence_Record_Version`); `value` ← `Evidence_Result`/`Predicted_or_Observed_State`; `uncertainty` ← `CEI`/`Quality_or_Confidence`; `method_version` ← 9 trường xử lý/mô hình; `scope.inference_unit` ← `Evidence_Granularity`/`Run_ID`; `scope.data_split` ← `Split_or_Fold_ID` + Fold_Link; `obs_context` ← thời điểm quan sát + ngữ cảnh chiến dịch/phiên/run/recording/trục/tần số; `Sensor_ID` ← bảng liên kết Sensor_Link; `BIM_GUID n:m` ← `BIM_Binding`; thêm: tập giá trị `evidence_type` cần xác nhận.

**Thiếu so với trường khóa (2 + 1 gợi ý):**
1. `scope.install_batch`: không có.
2. `scope.applicable_conditions`: không có trường có cấu trúc; chỉ có `Limitation_Context` (văn bản có cấu trúc, L345) và ranh giới chung (L346, L376). Không có phép thử âm "dùng ngoài phạm vi" trong 37 phép thử CE-NEG (L684-L720), không có bước "kiểm tại lần dùng" (chỉ cổng nhập G2, L726-L742).
3. (Gợi ý, từ C3 của phạm vi khóa) khoảng hiệu lực của ánh xạ cảm biến–cấu kiện (`valid_from/valid_to`): giao diện không có; `BIM_Binding` chỉ có `Verified_At`/`Binding_Status` (L429-L449). Không thuộc danh sách trường EVIDENCE khóa nên chỉ ghi nhận.

**Thừa (không có trường khóa tương ứng) gồm các nhóm sau. Theo cột đối chiếu ở 8.1: trong 52 trường tiêu đề có 3 khớp, 15 khác tên/khác cấu trúc, 34 thừa:**
- Vòng đời/soát xét: `Evidence_Status`, `Evidence_Record_Version`, `Created_By`, `Reviewed_By`, `Reviewed_At`, `Review_Status`, `Review_Rationale`, `Evidence_Status_Event` (cả thực thể).
- Nguồn/tái lập: `Source_Data_ID`, `Source_File_SHA256`, `Campaign_ID`, `Acquisition_Session_ID`, `Run_ID`, `Recording_ID`, `Preprocessing_Spec_ID`, `Windowing_Spec_ID`, `Aggregation_Rule_ID`, `Model_Config_ID`, `Evaluation_Protocol_ID`, `Code_Commit`, `Environment_ID`, ba bảng liên kết Source/Recording/Window.
- Cảm biến chi tiết: `Sensor_Mode_ID`, `Primary_Sensor_ID`, `Channel_Schema_ID`, `Axis_Context`, `Sampling_Rate_Hz`, `Quality_Flag`.
- Liên kết BIM chi tiết: `Candidate_Asset_ID`, `Model_Version_ID`, `BIM_Link_Status`, `BIM_Binding_ID`, `Binding_Evidence_Reference`.
- Quản trị hạ nguồn: `Eligible_For_G2_Traceability`, `Eligible_For_Inspection_Review`, `Downstream_Use_Limitation`, `Evidence_Interpretation_Boundary`, `Limitation_Context` (chỉ tương ứng một phần).

(Các con số 3/15/34 là đếm của tôi trên cột đối chiếu; một số trường vừa "thừa" vừa "tương ứng một phần" nên ranh giới chưa tuyệt đối.)

**Ghi nhận cho NCS quyết, không tự đổi phạm vi (quy tắc 6):**
- `Model_Version_ID` (L354) và các quy tắc phiên bản/thay thế (L641-L646, CE-NEG-014/-022/-023/-034) là dữ kiện có sẵn cho nhóm lỗi "phiên bản (C9)", trong khi EVIDENCE khóa chỉ có `method_version` và `revision_of`.
- `Review_*`/`Created_By`/`Evidence_Status_Event` chạm C6 (căn cứ và vai trò) nhưng ở đây là vòng đời của BẰNG CHỨNG, chưa phải của HÀNH ĐỘNG; tránh nhập nhằng với STATUS_EVENT.
- `CEI` đa chiều so với `uncertainty`: nếu `uncertainty` khóa là một số/khoảng thì không tương thích với "never a universal scalar" (L342); nếu là cấu trúc thì cần ánh xạ từng chiều.
- n:m `BIM_GUID` so với chính sách "mặc định 1 bản ghi : 1 cấu kiện" (L491-L495).
- Trạng thái nguồn: giao diện là "working specification", G1 còn OPEN, chưa có bản ghi bằng chứng nào được chấp nhận (T13:L14, L506), nên mọi trường ở trên là đề xuất, không phải dữ liệu đã có.
