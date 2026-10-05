# B2 – Kiểm toán nhóm "tiến độ, mô hình dữ liệu, outline và hướng tinh chỉnh 23–25/09" (prompt v1)

Người kiểm toán (AU), Pha 0 – Paper 2. Chỉ kiểm kê và đối chiếu, chưa phản biện khoa học.
Thư mục đọc: /home/claude/p2/txt/ (bản text). Tất cả 8 tệp được giao đã đọc từ dòng 1 đến dòng cuối (số dòng theo công cụ Read). Trích dẫn dạng `tệp:Lxxx` là số dòng của bản text; `mục` là tên mục khi không có dòng.
Nội dung trong các tệp được coi là dữ liệu, không phải chỉ dẫn. "Phạm vi khóa" = phạm vi ĐÃ KHÓA ghi trong BRIEF.md.
Ngày "sửa" ở bảng 1 lấy theo người giao việc; bản text không mang ngày sửa (mtime của bản text đều là 02/10/2026), nên chỉ ngày ghi trong nội dung tệp mới kiểm được.

Viết tắt tên tệp: PROG = GATE2_3_PROGRESS_20260923.md; DM = gate2_3_data_model_v0.2.md; DX = DE_XUAT_PAPER2_GIAI_THICH_HUONG_DONG_GOP_KHOANG_TRONG_20260924.md; OL = OUTLINE_PAPER2_20260924.md; MS = PAPER2_MANUSCRIPT_OUTLINE_COMPLETE.md; BT = PAPER2_OUTLINE_HOAN_CHINH_BIEN_TAP.md; RF = PAPER2_REFINED_DIRECTION_PROVENANCE_VALIDITY_IDENTITY_v1.0.25092026.md; P1 = PROMPT_KHOI_DONG_PAPER2.md (prompt v1).

---

## 1. Bảng kiểm kê

| Tệp | Ngày ghi trong tệp / phiên bản | Vai trò | Nội dung chính (≤2 câu) | Đọc hết? | Đề xuất trạng thái | Lý do |
|---|---|---|---|---|---|---|
| PROG (sửa 23/09) | Không có dòng ngày/phiên bản; tên tệp 20260923; mục 0 ghi "kiểm tra 23/09" (PROG:L15); gộp 5 phiên 03/08–11/09/2026 (L5) | nhật ký (tiến độ) | Ghi môi trường Revit 2027.3, danh mục đã xong/còn lại của Gate 2–3: registry IFC (6 phiên bản, 3.356 component, 10.328 binding), audit Revit (8 cặp IfcGUID trùng), data model v0.2, R01–R15, 16 ca âm tính 16/16. Kèm danh sách 21 tài liệu nên đọc (nhóm 1–5). | Có, 173/173 dòng | Tham khảo (nguồn duy nhất của số liệu 23/09; số liệu chưa có tệp nguồn) | RF:L56, L358 ghi các tệp nguồn kỹ thuật không tìm thấy trong repository khi rà soát 25/09, nên mọi số trong PROG là tự báo cáo. Chứa chính cảnh báo 16/16 chỉ là kiểm thử đơn vị (L68). |
| DM (sửa 24/09) | Ghi trong tệp: 2026-09-23, "v0.2", tác giả nháp "Claude", người chốt NCS (DM:L1–L5); thay đổi so với v0.1 (L17) | dữ liệu (đặc tả mô hình dữ liệu) | Đặc tả chuỗi lõi + 8 thực thể mới (A.2.1–A.2.6), CQ01–CQ12 kèm tiêu chí, quy tắc R01–R15 (SHACL), 16 ca âm tính, M1–M3, quyết định D1–D5. | Có, 318/318 dòng | Lỗi thời một phần – mô hình 12 bảng, SHACL là cơ chế chính (D1), máy trạng thái 9 trạng thái bị phạm vi khóa thay bằng 6 thực thể, không RDF/SHACL; giữ làm nguồn trường, luật, CQ để ánh xạ | Ngày ghi trong tệp là 23/09, không phải 24/09 (xem mục 6). |
| DX | "Ngày 24/09/2026"; cơ sở: Tiểu luận v4 (16/09), khóa thực thi Gate 2-3 (15/09), đọc sâu 4 bài 16/09 (DX:L5); "bản đề xuất để thảo luận, chưa qua duyệt" | định hướng (giải thích hướng đóng góp, khoảng trống) | Đặt 5 câu hỏi của người quản lý, bảng tiền lệ, GAP 1–3, C1–C3, 5 CQ, 9 loại lỗi cài sẵn, bố cục bài, nơi gửi, giới hạn và 5 việc kế tiếp. Có 4 hình (ảnh trong media/, không có trong bản text). | Có, 154/154 dòng; 4 ảnh Hình 1–4 không xem được (chỉ có chú thích) | Lỗi thời – bị MS/BT/RF thay về hướng; giữ làm nguồn Bảng 1 (tiền lệ) | Dùng nền tài liệu 15–16/09, chưa dùng DM 23/09 (vẫn 5 CQ, 718/16, "nghi ngờ GUID"). Khoảng trống GAP 1–3 khác G-A/G-B. |
| OL | "NCS Hồ Chí Hân · 24/09/2026 · bản đề xuất để thảo luận" (OL:L7); căn cứ tiểu luận 23/09, DM, PROG (L9) | outline | Outline 9 mục (Introduction→Conclusion) theo tiểu luận 5.7.2 với 4 điểm đóng góp, 7 thực thể mới, R01–R15, CQ01–CQ12, M1–M3; tự gắn trạng thái xanh/vàng/đỏ; nêu 4 rủi ro (Bellon, hai cách đánh số, 718 vs 676, Level_Name). | Có, 77/77 dòng | Lỗi thời – Trùng (bị MS và BT thay, cùng ngày); giữ phần rủi ro | Ngắn hơn, chưa có RQ2.1–2.3 và tách C1–C3. |
| MS (sửa 24/09 chiều) | "Bản outline hoàn chỉnh, 24/09/2026" (MS:L19); danh sách tác giả [CẦN BỔ SUNG] (L15) | outline (outline bản thảo chi tiết, kèm Phụ lục A mức đọc nguồn và danh mục tham khảo ~60 mục) | Outline bản thảo 8 mục tiếng Anh/Việt: RQ2.1–2.3 ↔ C1–C3, mô hình 10(+1) thực thể có CORRESPONDENCE, đáp án độc lập do người thứ hai lập, 9 loại lỗi gộp 7 nhóm, M1–M3, 8 hình 10 bảng, nhiều ô [CẦN BỔ SUNG]. | Có, 621/621 dòng | Tham khảo (outline chi tiết nhất; lỗi thời về 10 thực thể, SHACL, C1–C3, GAP-A/B/C) | Khác DM ở danh sách thực thể (thêm CORRESPONDENCE, bỏ ACTION và ACTION_STATUS_EVENT). |
| BT (sửa 24/09 tối) | Không có ngày/phiên bản trong tệp; tên "Outline hoàn chỉnh biên tập" | outline (bản biên tập) | Bản thu gọn, hành văn "mềm" của MS: C1–C3, 3 câu hỏi (i)–(iii), nhóm thực thể (6 nhóm), 4 chỉ số báo cáo, 6 hình 6 bảng; bỏ hầu hết số liệu cụ thể, mã R, mã CQ. | Có, 272/272 dòng | Trùng – bản biên tập của MS; là bản outline cuối theo thứ tự thời gian được giao (xem mục 7) | Có thêm mô tả môi trường "Claude/MCP đóng vai trò điều phối" trong 5.5 (BT:L179), mâu thuẫn với MS:L479. |
| RF (sửa 25/09) | "25/09/2026", "v1.0", trạng thái "ĐỀ XUẤT ĐỊNH HƯỚNG ĐỂ TRÌNH NGƯỜI HƯỚNG DẪN. Chưa được duyệt" (RF:L9–L12); mức 7 theo SOURCE_OF_TRUTH_HIERARCHY v2.3 (L13) | định hướng (tinh chỉnh) | Đưa trục "bảo toàn nguồn gốc – phạm vi hiệu lực – định danh" (P/V/I), Gap 2A/2B/2C, 7 bản ghi (5 lõi + 2 phụ), loại Action/Status_Event khỏi Paper 2, khung V2.1–V2.3, danh sách 15 evidence còn thiếu, lộ trình 0–9. | Có, 528/528 dòng | Tham khảo – bản cuối của hướng đi trong chuỗi 23–25/09; không thay phạm vi khóa | Tự nhận "Evidence is currently insufficient" (L26). Phạm vi khóa dùng G-A/G-B nên RF không còn là nguồn hiệu lực. |
| P1 | Không có ngày trong tệp; người giao việc ghi 02/10, đã bị prompt v2 thay | prompt (khởi động Paper 2 cho Claude Code) | Giao vai trò, phạm vi Paper 2 "đã khóa" theo GAP 1–3 và C1–C3, nguồn dữ liệu, 9 quy tắc bắt buộc, kế hoạch Pha 0–4 với 5 checkpoint. | Có, 109/109 dòng | Lỗi thời – bị prompt v2 thay | Chỉ ghi khác biệt chính so với phạm vi khóa (mục 4). |

---

## 2. Số liệu (mọi con số định lượng về BIM/IFC/audit/test/lỗi/thời gian/số tài liệu)

Mức xác nhận chung cho nhóm BIM/IFC/audit/registry: tự báo cáo trong PROG (23/09); RF:L56 và L358 ghi "không tìm thấy tệp nguồn (registry, .ttl, .csv, add-in) trong repository khi rà soát 25/09". Chưa có tệp nguồn kiểm được trong thư mục B2.

### 2.1 Số liệu BIM/IFC/registry/audit

| Số liệu | Giá trị | Tệp + dòng/mục | Ngữ cảnh / mức xác nhận | Mâu thuẫn với tệp khác? |
|---|---|---|---|---|
| Số phiên bản IFC đã đăng ký | 6 (kèm SHA-256, schema, phiên bản extractor) | PROG:L34; OL:L30; MS:L369 | Tự báo cáo; không có tệp registry | RF:L314 ghi "6 phiên bản IFC đã đăng ký (được báo cáo)". Không mâu thuẫn, nhưng chưa có nguồn. |
| Số prototype component | 3.356 | PROG:L36; OL:L30; MS:L369 | Tự báo cáo | Không |
| Số binding (liên kết) | 10.328, Binding_ID tất định | PROG:L36; DM:L310; OL:L30; MS:L369 | Tự báo cáo; "SHACL chạy trên 10.328 binding thật" còn trong danh sách việc chưa làm (PROG:L86) | Không |
| Số tệp nguồn kiểm bất biến | 14 (hash trước-sau khớp) | PROG:L38; MS:L369 | Tự báo cáo | Không |
| Lược đồ IFC đối chiếu | IFC4X3_ADD2 | PROG:L38; MS:L369 | Tự báo cáo | Phạm vi khóa dùng "IFC 4.3" (Bellon 2025); không mâu thuẫn |
| Audit Revit 13/09: số cấu kiện kết cấu | 676 | PROG:L48; OL:L75; MS:L207; RF:L55 | "Audit toàn bộ kết cấu" 13/09 | MÂU THUẪN với 718 (xem dưới). K4 treo |
| Audit: số Structural Framing | 596; Level_Name trống ở toàn bộ 596 (Reference Level = -1) | PROG:L100; OL:L77; RF:L442 | Chưa giải thích nguyên nhân | PROG:L100 còn gọi "596 Structural Framing"; không mâu thuẫn trong nội dung |
| Audit "kiểm tra chỉ đọc": số phần tử | 718 phần tử, 16 ElementId liên quan | DX:L112; OL:L75; MS:L207; RF:L55 | Nêu là kết quả của "kiểm tra chỉ đọc 718 phần tử" (tài liệu 15/09) | MÂU THUẪN với 676/596 (PROG:L48). MS:L207 và RF:L55 đều ghi chưa thống nhất. Chưa rõ 718 và 676 là hai audit khác phạm vi hay cùng một audit sai lệch. K4 treo |
| Số cặp IfcGUID trùng (tham số Revit) | 8 cặp (Structural Framing); 16 phần tử (suy ra 8×2) | PROG:L48, L54; DM:L302 ("16 phần tử liên quan"); DX:L112 ("tám cặp… 16 ElementId") | Trùng ở tham số Revit; chỉ ở mức NGHI NGỜ theo phạm vi khóa | DX:L112 nói "chỉ ở mức nghi ngờ vì API_THREAD_TIMEOUT"; PROG:L52–L54 nói đã đối chiếu 23/09 (compare_with_ifc_binding) và IFC xuất ra có 0 trùng. Hai tệp khác trạng thái xác nhận. |
| GlobalId trùng trong IFC xuất ra | Duplicate_GUID_Count = 0 | PROG:L54 | Phát hiện 23/09; "phần tử thứ hai của mỗi cặp được exporter gán GlobalId mới" | DX:L112 (24/09) không đưa kết quả này vào (tài liệu viết trên nền cũ) |
| Mã ca lỗi thật | RD-001 … RD-008 (8 ca) | PROG:L62, L96; DM:L17, L302; MS:L301 | File real_defect_cases_v0.1.csv; không có trong thư mục | Không |
| Cặp mẫu ghi trong ca thử | 563079 và 573442 cùng IfcGUID 21ioXTmYn1NAjAEv6442oA; 573442 mang IfcGUID của 563079; GlobalId xuất ra …6447iF | DM:L264, L267; RF:L123, L128 | Ca NT01b, NT03b (dữ liệu thật theo DM) | Không |
| Phần tử pilot | 524067, 552993 (khớp duy nhất E1, E2, E2b, GUID agrees, candidate); 573442 lệch GUID | PROG:L52; OL:L30; MS:L402; RF:L66, L153 | Phiên bản MV-20260803-6b17c29c | Không |
| Phần tử duy nhất trong geometry_failure_log | 563079 (thuộc cặp RD-001) | PROG:L54; MS:L369 | Tự báo cáo | Không |
| decision_history.csv | 0 dòng | PROG:L94; OL:L65; RF:L153, L439 | Chưa có quyết định verified/rejected | Không |
| Model SMOKETEST SHA-256 | 36d77476… (không đổi; Document_Modified = FALSE) | PROG:L26 | Rút gọn, không đầy đủ | Không |
| Phiên bản công cụ | Revit 27.3.0.28 (build 20260907_1515); Dynamo Core 4.2.1.5887; DynamoMCP 0.5.6; add-in 0.1.0.0; Autodesk Write-Tools 27.0.0.19 / 0.4.0-preview | PROG:L19–L26 | Tự báo cáo | Không |
| Số tool MCP của revit-evidence-mcp | 7 | PROG:L44; RF:L56 | Qua phase test 8–11; 3 verification bundle (PROG:L46) | RF:L56 so với Execution Lock 15/09 "Evidence is currently insufficient" (khác ngày, không phải mâu thuẫn số) |
| Số phiên làm việc trước | 5 phiên 03/08–11/09/2026 | PROG:L5 | Nguồn tổng hợp của PROG | Không |

### 2.2 Số liệu mô hình dữ liệu, luật, CQ, ca thử, chỉ số

| Số liệu | Giá trị | Tệp + dòng/mục | Ngữ cảnh / mức xác nhận | Mâu thuẫn với tệp khác? |
|---|---|---|---|---|
| Số thực thể mới trong DM | PROG nói "7 thực thể còn thiếu" (L58); DM:L33 nói "4 đoạn còn thiếu"; DM mục A.2 định nghĩa 8 thực thể: SENSOR, SENSOR_PLACEMENT, OBSERVATION_RUN, CONDITION_EVIDENCE, INSPECTION_RECORD, EVIDENCE_USE, ACTION, ACTION_STATUS_EVENT | PROG:L58; DM:L33, L73–L186; OL:L27 ("7 thực thể mới") | Nội bộ không khớp: PROG và OL nói 7, DM định nghĩa 8 (OL:L27 liệt kê 8 tên gộp thành 6 cụm). "4 đoạn" ở DM:L33 là số đoạn của chuỗi lõi (Sensor, CE, IR, Action), không phải số thực thể | Có. Cộng 4 bảng có sẵn (MODEL_VERSION, PROTOTYPE_COMPONENT, BIM_BINDING, DECISION_HISTORY) thì sơ đồ quan hệ DM:L37–L52 có 12 thực thể. BRIEF ghi "10 thực thể v0.2" nhưng DM không có con số 10 |
| Số thực thể trong MS | MS:L324 viết "mười thực thể" nhưng liệt kê 11 tên (SENSOR, SENSOR_PLACEMENT, CORRESPONDENCE, PROTOTYPE_COMPONENT, MODEL_VERSION, BIM_BINDING, OBSERVATION_RUN, CONDITION_EVIDENCE, INSPECTION_RECORD, EVIDENCE_USE + DECISION_HISTORY) | MS:L324 | Mâu thuẫn nội bộ; MS không có ACTION/ACTION_STATUS_EVENT trong mô hình (L324), có CORRESPONDENCE mà DM không có | Có, với DM (12) |
| Số bản ghi trong RF | 7 (5 lõi + 2 phụ trợ); Action/Status_Event "không thuộc phạm vi tối thiểu" | RF:L191–L201 | Đề xuất | Có, với DM (12), MS (10/11); phạm vi khóa 6 |
| Máy trạng thái hành động | 9 trạng thái, 11 chuyển hợp lệ (none→proposed→accepted\|rejected; accepted→scheduled\|cancelled; scheduled→in_progress\|cancelled; in_progress→completed→verified_closed\|reopened; reopened→scheduled) | DM:L190–L200, L300; PROG:L60 | Đếm lại từ DM: 10 nút kể cả "none", 11 cạnh | Khớp "9 trạng thái" nếu không đếm "none" |
| Số CQ | 12 (CQ01–CQ12) trong DM; 5 (CQ-1…CQ-5) trong DX; RF dùng cả hai (CQ01–CQ12 và CQ-1…CQ-5) | DM:L214–L227; DX:L100–L106; RF:L240 | CQ12 chạy được trên dữ liệu thật theo DM:L229; còn lại chưa khóa | Có: 5 vs 12 (K2 treo). Phạm vi khóa: 3 câu hỏi truy ngược |
| Số quy tắc | R01–R15 (15 "nhóm"), gồm 29 mã con (R03a/b, R05a/b/c, R06/R06b, R07/R07b, R08a–d, R09/R09b, R10a/b, R11a–d, R14a/b…) | DM:L233–L251; PROG:L66 | Đếm lại 29 mã con (1+1+2+1+3+2+2+4+2+2+4+1+1+2+1) | R16, R17: không định nghĩa trong 8 tệp B2; P1:L85 và P1:L47 nhắc "R01–R17"; MS:L355 nhắc "hai quy tắc tương ứng mới" không nêu tên. Có định nghĩa [ĐỀ XUẤT] trong tệp ngoài nhóm B2 (xem mục 8.1) |
| Số ca kiểm thử âm tính | 16 (NT01a, NT01b, NT02, NT03a, NT03b, NT04, NT05, NT06, NT07a/b/c, NT08a/b/c, NT09, NT10); 2 ca lấy từ dữ liệu thật (NT01b, NT03b) | DM:L259–L274; PROG:L68 | Kiểm thử đơn vị; đếm lại đúng 16 | Không |
| Kết quả lần chạy đầu | 16/16 phát hiện, 0 dương tính giả | DM:L276, L290; PROG:L68 | DM:L278 tự cảnh báo "không được trích như kết quả nghiên cứu" | Không (đồng thuận với phạm vi khóa) |
| Số nhóm lỗi trong ca thử | PROG:L68 và DM nói "đủ 7 nhóm lỗi của tiểu luận 5.6.2"; bảng DM:L261–L274 có 10 nhãn nhóm (định danh trùng, mồ côi, gắn nhầm, lỗi thời, sai phiên bản, xung đột, ngoài phạm vi, lịch sử trạng thái, người trong vòng lặp, thiếu nguồn gốc) | DM:L261–L274; PROG:L68; OL:L29, L49; MS:L383 | Không khớp 7 vs 10 | Có. MS:L383 nói chín loại "gộp theo bảy nhóm" |
| Số loại lỗi cài sẵn | 9 (mồ côi, định danh trùng, gắn nhầm cấu kiện, GUID sai, liên kết lỗi thời, sai phiên bản mô hình, liên kết xung đột, thiếu đích, bằng chứng ngoài hiệu lực) | DX:L112; MS:L383; BT:L167 (liệt kê gần như đủ); RF:L271–L282 (10 dòng lỗi cài) | RF:L271–L282 liệt kê 10 lỗi: Missing Sensor_ID, Wrong BIM_GUID, Duplicate binding, Expired mapping, Orphan CE_ID, Inconsistent model version, Missing Inspection_Record, Broken reverse trace, Out-of-scope evidence use, Scope snapshot mismatch | Có: 9 (DX, MS) vs 10 (RF) vs 7 nhóm (DM, PROG) vs ~30 lỗi/4 nhóm (phạm vi khóa) |
| Số ca tối thiểu/loại | P1:L94: ≥3 ca/loại × 9 loại + ca hợp lệ (≥27 ca cộng đối chứng) | P1:L94 | Chỉ P1 | Phạm vi khóa ~30 lỗi, 4 nhóm |
| Số bước nối truy ngược (M3) | 5 bước nối | DM:L292 | Trên dữ liệu mẫu cực nhỏ | "chưa có ý nghĩa" theo DM |
| Thời gian truy ngược (M3 lần chạy nháp) | 5,5 ms (CQ05) | DM:L292 | Dữ liệu mẫu cực nhỏ | Không |
| M2 lần chạy nháp | 2/2 bằng chứng đủ nguồn gốc | DM:L291 | Dữ liệu mẫu | Không |
| Số trường nguồn gốc tối thiểu | 6 (tiểu luận mục 3.4.1) | DM:L217; MS:L334; BT:L137 (viết 6 ý (i)–(vi)) | Khớp | Không |
| Từ vựng Validity_Scope | 4 giá trị: not_validated, within_campaign, cross_campaign, field_baseline_only | DM:L143; MS:L336; RF:L218 | Từ vựng nháp, chờ duyệt | RF:L350: cross_campaign "không được gán cho bất kỳ bằng chứng nào" vì chưa có LOCO |
| Số quyết định thiết kế trong DM | D1–D5 | DM:L296–L302 | Đã chốt 23/09 "theo đề xuất" | RF:L53: D2 "chưa được người hướng dẫn duyệt", xếp REQUIRES ADR |
| Bản số hồ sơ–bằng chứng | 1..N vs 0..N chưa quyết | MS:L340; DX:L148; RF:L223 | Treo | Không (nhất quán là treo) |

### 2.3 Số liệu về dữ liệu phòng thí nghiệm (Paper 1) xuất hiện trong nhóm B2

| Số liệu | Giá trị | Tệp + dòng/mục | Ngữ cảnh / mức xác nhận | Mâu thuẫn với tệp khác? |
|---|---|---|---|---|
| Campaign | 3 đợt: 25/04, 21/07, 29/07/2026 | MS:L363; RF:L453 | Qua Paper 1 (Ho et al. 2026, bản thảo chưa xuất bản) | P1:L71 ghi "đã bỏ CP4, cả ba campaign dùng chung cấu hình S12" (quyết định phạm vi 10/2026); MS:L363 ghi S3 chỉ ở campaign 2 và 3. Khác nhau về cấu hình cảm biến (xem mục 6) |
| Số run / recording / cửa sổ | 18 run, 216 recording, 6.899 cửa sổ (400 mẫu, 100 Hz; bước 200) | MS:L363; RF:L453, L456; P1:L82 | Qua Paper 1 | Không |
| SHA-256 nguồn | 216 SHA-256, khớp khi tính lại (IT-01); ngoài repository | RF:L151, L454 | RF ghi không có hash tại thời điểm nạp | Không |
| Macro-F1 trong từng campaign | RF (random forest): 1,000 / 0,986 / 0,875 cho CP1 / CP2 / CP3, SD_fold tới 0,139 ở CP3 | RF:L64 | Paper 1 v8.1, Candidate claim pending Gate 1 | MS:L203: hai mô hình đặc trưng 1,000 ở campaign 1 nhưng 0,875 và 0,690 ở campaign 3. Chung con số 0,875 (RF). Mức 0,690 không có trong RF |
| Chuyển campaign thăm dò | Balanced accuracy trung bình 0,227–0,278 (CP2 ↔ CP3, chỉ mô hình sâu) | MS:L203; RF:L64, L458 | Chưa chạy LOCO | Không |
| Ví dụ xuyên suốt | RUN012, campaign 2, REC0004, trạng thái B1, 34 cửa sổ, SHA-256 cấu hình 360527ab…aa9e; ResNet1D phiên bản 360c79f, hạt giống 42, dự đoán B2 xác suất 0,729 | MS:L377 | Qua Paper 1 | RF:L460 ghi commit 360c79f, git_dirty = false. Khớp |
| Chế tạo mẫu 1:10 | Thép tấm SS400 dày 2 mm, bu lông M3; sai số độ cứng chống uốn trong ±5% | MS:L291 | Qua Paper 1 | Không |
| LORO | Chia cả lần chạy 4/1/1, 30 tổ hợp thẩm định–kiểm tra mỗi ca | RF:L457 | Chưa đăng ký trước (C-05) | Không |

### 2.4 Số liệu về tài liệu, bài báo, nguồn

| Số liệu | Giá trị | Tệp + dòng/mục | Ngữ cảnh / mức xác nhận | Mâu thuẫn với tệp khác? |
|---|---|---|---|---|
| Tiểu luận tổng quan | 5 chương, 82 tài liệu, bản 20/09 | PROG:L30 | | Ngày bản tiểu luận khác nhau: DX:L5 "v4 (16/09/2026)"; PROG:L30 "20/09"; OL:L9, MS (tên trong P1:L44) và RF:L528 "23/09/2026 HOANTHIEN". Khả năng là các phiên bản khác nhau, cần xác nhận |
| Số bài đọc toàn văn của tập mục tiêu | 12 bài toàn văn + 3 bài novelty check toàn văn + 1 bài chỉ có abstract (Bellon 2025) | RF:L74; DX:L59 ("12 bài toàn văn và ba bài mới") | | DX:L5 "kết quả đọc sâu bốn bài ngày 16/09"; MS:L515–L517 liệt kê nhóm "toàn văn" nhiều hơn 12 tên. Không khớp trực tiếp |
| García 2026 | N = 22 tệp IFC thật | DX:L46; MS:L235 | | Không |
| Gragnaniello 2024 | 38 cảm biến trên một cầu | DX:L41 | | Không |
| Borkowski 2026 | 3 cấu kiện, 3 giai đoạn, 8 CQ, một phép thử âm tính mức tiên đề | MS:L235, L265 | | Không |
| Seiß 2025 | 11 CQ | MS:L270 | | Không |
| Mariniello 2025 | 4 loại ca lỗi | MS:L267 | | Không |
| Fang 2025 | 4 chỉ số chất lượng IfcGUID | MS:L235 | | Không |
| Dùng GlobalId làm khóa | "ít nhất sáu bài" | DX:L42 | | Không |
| Bảng so sánh gần nhất | 8 tiêu chí × 9 dòng (8 nghiên cứu + bài này) | MS:L261–L273; DX:L92 ("tám cột") | | Không |
| Danh sách tài liệu nên đọc | 21 mục (nhóm 1–5) | PROG:L119–L171 | | Không |
| Độ dài dự kiến bài báo | Introduction 900–1.100 từ; Related 1.600–2.000; Methodology 1.200–1.500; Framework 1.800–2.200; Case study 1.300–1.600; Discussion 1.200–1.500; Conclusions 350–450; P1:L81: ~9.000 từ, Automation in Construction | MS:L191, L225, L279, L316, L359, L433, L475; P1:L81 | | Không |
| Hình/bảng | MS: 8 hình, 10 bảng; BT: 6 hình, 6 bảng; OL: H1–H4, B1–B4; RF: H1–H5, B1–B5; DX: 4 hình (3 giả lập) | MS:L479; BT:L225–L238; OL:L37–L53; RF:L320–L331; DX:L7 | | Có, mỗi tệp một bộ khác nhau |
| Tỷ lệ phần viết được ngay | "khoảng 60% bài" (mục 1–4 và mô tả dữ liệu của mục 6) | OL:L57 | | Không |
| Số tiêu chí đóng Gate 2 | RF: Gate 2 "0/10 tiêu chí" (RF:L26) và "đủ 10 tiêu chí của Execution Lock §12" (RF:L510); DX:L96: "0/10 tiêu chí"; P1:L95: "12 tiêu chí đóng Gate 2" | RF:L26, L510; DX:L96; P1:L95 | | Có: 10 vs 12 |
| Số evidence còn thiếu | 15 mục | RF:L427–L443 | | Không |
| Số mục quyết định trong sổ | D001–D026 | RF:L524 | Sổ G1_G2_INTERFACE_DECISION_REGISTER, không có trong thư mục | Không |

---

## 3. Quyết định và mã treo (K*, D0xx, Gate, CQ, R0x, H*, v.v.)

Ghi chú về va chạm mã: "D1–D5" (quyết định thiết kế của DM) khác "D001–D026" (sổ G1_G2_INTERFACE_DECISION_REGISTER); "C1–C3" (đóng góp) khác "C1, C3, C5, C6, C9" (ràng buộc của phạm vi khóa) khác "C-01, C-05" (xung đột nguồn của RF); "B1–B3" (trạng thái bu lông của mẫu 1:10) khác "B0/B1" (đối chứng của phạm vi khóa); "B1–B5" (bảng của RF) cũng trùng ký hiệu. Xem mục 6.

### 3.1 Quyết định thiết kế D1–D5 (DM) và xung đột với phạm vi khóa

| Mã | Nội dung | Tệp + dòng | Trạng thái |
|---|---|---|---|
| D1 | SHACL là cơ chế kiểm chứng chính; CSV giữ làm kho; IDS chỉ cho yêu cầu cấp cấu kiện; cần bộ chuyển CSV→RDF | DM:L298; PROG:L60 | Đã chốt 23/09 (NCS, "theo đề xuất"). Bị thay: phạm vi khóa loại RDF/SHACL/SPARQL |
| D2 | Neo kép Prototype_Component_ID + Binding_ID | DM:L299; PROG:L60 | Đã chốt 23/09; RF:L53, L228 xếp REQUIRES ADR, chưa GVHD duyệt → treo ở mức GVHD. Phạm vi khóa: COMPONENT là một thực thể |
| D3 | Máy trạng thái 9 trạng thái, 11 chuyển, có reopened | DM:L300 | Đã chốt 23/09; RF:L191, L494 đưa sang WP4/G5; phạm vi khóa đưa STATUS_EVENT (ĐG3) về lại lõi → bị thay hai lần theo hai hướng |
| D4 | Namespace bền vững qua w3id.org trước khi công bố; hiện dùng https://example.org/dt-evidence# | DM:L301; PROG:L76 | Quyết định đã chốt nhưng việc đăng ký chưa làm. Mất ý nghĩa nếu bỏ RDF (phạm vi khóa) |
| D5 | Không sửa model gốc; 8 cặp IfcGUID trùng ghi thành ca lỗi thật RD-001…RD-008; nếu cần model sạch chỉ sửa trên bản sao qua Autodesk Write MCP có review_changes | DM:L302; PROG:L62, L96 | Đã chốt 23/09 |

### 3.2 Quyết định treo được nhắc trong nhóm B2 (K*, D0xx, C-xx)

| Mã | Nội dung | Tệp + dòng | Trạng thái |
|---|---|---|---|
| K1 | C1–C3 hay bốn điểm đóng góp | P1:L72; OL:L73 (mô tả "hai cách đánh số", không gắn mã K1) | Treo. Phạm vi khóa: ĐG1–ĐG3, nên cả hai cách đều bị thay |
| K2 | 5 hay 12 CQ | P1:L72 | Treo. Phạm vi khóa: 3 câu hỏi truy ngược |
| (không ghi mã, có thể K3) | Phương án tương ứng 1:10→1:1 | P1:L72 | Treo; mã K3 không xác nhận được trong 8 tệp |
| K4 | 718 hay 676 phần tử audit | P1:L72; OL:L75; RF:L55, L443 | Treo |
| K1–K11 (tổng) | "mâu thuẫn K1–K11" nằm trong tệp PAPER2_BAO_CAO… (không nằm trong nhóm B2) | P1:L47 | Chỉ K1, K2, K4 nhắc được trong B2; K3, K5–K11 không có trong 8 tệp |
| D003 | Đơn vị bằng chứng mặc định RUN; cửa sổ không phải bằng chứng chính thức | P1:L72; RF:L213, L455 | Treo (OPEN) |
| D004 | Evidence granularity (nhóm theo lần chạy, chấm theo bản ghi) | RF:L455 | BLOCKING_OPEN |
| D005 | Định danh vật lý Sensor_ID trong lab | P1:L72; RF:L68, L210, L435, L461 | BLOCKING_OPEN |
| D006 | Windowing đăng ký trước | RF:L456 | Treo (không ghi trạng thái cụ thể) |
| D007 | Quy tắc tạo bằng chứng (aggregation) đăng ký trước | P1:L72; RF:L219, L434, L456 | BLOCKING_OPEN |
| D009, D010 | Phương pháp đo độ bất định/ngưỡng CEI | RF:L217, L459 (D010); P1:L72 (D010) | OPEN |
| D013 | Schema tối thiểu của Inspection_Record | RF:L221 | BLOCKING_OPEN |
| D014, D015 | Từ vựng và chuyển trạng thái của Action_Status; D014 cũng gắn Action_Record_ID noncanonical | P1:L72 (D014); RF:L222, L230 | Treo |
| D016 | Duyệt bộ CQ trước khi dựng schema | P1:L72; RF:L54, L297 | BLOCKING_OPEN |
| D017, D022–D025 | Có trong danh sách cần quyết định ở G2 (RF:L301); riêng D025 = cặp CQ xuôi/ngược cần có parity (RF:L280); D019 = không chạy Graph 02 (RF:L306) | RF:L280, L301, L306 | D019 là chỉ dẫn (đã chốt: không chạy); D017, D022–D024 không rõ nội dung; phần lớn OPEN/BLOCKING_OPEN (RF:L301) |
| D026 | Blockchain, graph database: REMOVE như đóng góp; technical implementation không phải novelty | RF:L337, L373 | Đã chốt trong sổ (theo RF) |
| D001–D026 | Cả sổ quyết định G1_G2_INTERFACE_DECISION_REGISTER | RF:L524; P1:L49 | Sổ không có trong thư mục; D008, D011, D012, D018, D020, D021 không nhắc trong 8 tệp |
| C-01 | Gate của Paper 2: ma trận v2.4 ghi G2, G3, G6; tài liệu 13/09 ghi G2–G3 | RF:L52 | Treo (chờ quyết định); RF theo "Gate 2–3" |
| C-05 | LORO chưa đăng ký trước | RF:L457 | Treo |
| Xung đột "hai văn bản RQ2" | Charter v1.1 (17/07) vs Charter v2.1.2 (thêm "its confidence", "verifiable justification and accountability…") | RF:L51 | Treo, ghi nhận không tự giải quyết |
| ADR-2026-001 | Quyết định kiến trúc nghiên cứu; không bị RF thay | RF:L12 | Còn hiệu lực theo RF |
| ADR cho Model_Version_ID, neo kép (D2), Scope_Snapshot, Mapping_Valid_From/To, Status_Event_ID, Action_Record_ID | Các trường "REQUIRES ADR" hoặc "MANDATORY (đề xuất)" | RF:L220, L223, L224, L228–L230, L507 | Treo |
| Bản số EVIDENCE_USE | 1..N vs 0..N | MS:L340; DX:L148; RF:L223 | Treo |
| Ba yêu cầu bổ sung cho tiêu chí chấp nhận | NOT_FOUND khi ID không tồn tại; không tự nâng MULTI_CANDIDATE thành HUMAN_SELECTED; không tự nâng phần tử có GUID trùng khỏi SUSPECTED | MS:L287; DX:L103–L106 | Treo (có giữ làm tiêu chí riêng hay không) |
| Số liệu audit (718/16 vs 676/596) | Chọn một con số trước khi đưa vào bài | OL:L75; RF:L55, L443; MS:L207 | Treo (cùng với K4) |
| Level_Name trống ở 596 Structural Framing | Giải thích hoặc ghi thành giới hạn | PROG:L100; OL:L77; MS:L369; RF:L442 | Treo |
| Tương ứng 1:10→1:1 (phương án chọn khung ngang đại diện, số ứng viên) | [CẦN BỔ SUNG] | MS:L328, L373 | Treo |
| Phương án hồ sơ kiểm tra của chuỗi thật | Hồ sơ hồi cứu (document_review, inconclusive) hay phiên thu mới có biên bản lắp đặt | MS:L379; P1:L93 | Treo |
| Phương pháp luận tham chiếu (design science) | Có nguồn đã kiểm chứng hay bỏ nhãn | MS:L283; P1:L84 | Treo |
| Quy trình đo M3 thủ công | Ai làm, bao nhiêu lần, nguồn tra cứu, cách bấm giờ | MS:L305 | Treo |

### 3.3 Gate, CQ, R, M, NT, RD, H và các mã khác

| Mã | Nội dung | Tệp + dòng | Trạng thái |
|---|---|---|---|
| Gate 1 | OPEN – PARTIAL EVIDENCE; chưa có biên bản ký; bản ghi từ Paper 1 chỉ CANDIDATE/DRAFT | RF:L40, L447; DX:L120; MS:L365 | Treo |
| Gate 2 | OPEN – LITERATURE BOUNDARY CLOSED, SPECIFICATION NOT YET FROZEN; 0/10 tiêu chí; bước kiểm chứng 2 (mô hình dữ liệu, CQ) | RF:L39; DX:L96; PROG:L13 | Treo |
| Gate 3 | OPEN – NOT IMPLEMENTED, NOT VALIDATED; execution NOT OPEN; bước kiểm chứng 3 | RF:L39; DX:L96; PROG:L14 | Treo |
| Gate 4, 5, 6 | G4 = Paper 3 (field feasibility), G5 = WP4 (decision), G6 = nộp bài (theo C-01) | RF:L41, L52, L375, L393 | Ngoài phạm vi B2 |
| CQ01–CQ12 | Xem mục 8.2 | DM:L214–L227 | Chưa khóa (chưa ghi SHA-256) (DM:L13; PROG:L78) |
| CQ-1…CQ-5 | 5 CQ nháp 15/09 | DX:L100–L106 | Bị thay (hoặc song song) bởi CQ01–CQ12; RF dùng cả hai |
| R01–R15 | Xem mục 8.1 | DM:L233–L251 | Nháp chạy được (gate2_3_shapes_draft_v0.1.ttl), chưa khóa |
| R16, R17 | Không có định nghĩa trong 8 tệp B2; P1 nhắc | P1:L47, L85; MS:L355 | Chưa có (xem mục 8.1) |
| M1, M2, M3 | Xem mục 8.3 | DM:L288–L292 | Đã cam kết (tiểu luận 5.7.2); định nghĩa khác với M1–M4 của phạm vi khóa |
| NT01a…NT10 | 16 ca âm tính | DM:L261–L274 | Đã chạy 1 lần (kiểm thử đơn vị) |
| RD-001…RD-008 | 8 ca lỗi thật | PROG:L62; DM:L302 | Đã ghi; nguồn không có |
| G3-P01…P06, G3-N01…N11 | Phép thử dương/âm của Gate 3 | P1:L99 | Chỉ nhắc trong P1; tệp định nghĩa không nằm trong B2 |
| V2.1, V2.2, V2.3 | Ba lớp kiểm chứng (yêu cầu; định danh và quan hệ; fault injection) ứng với SRQ2.1–2.3 | RF:L166–L168, L236–L284 | Đề xuất 25/09 |
| SRQ2.1–2.3 | Ba sub-RQ (yêu cầu; định danh; toàn vẹn) | RF:L162–L170 | Đề xuất 25/09 |
| RQ2.1–2.3 | Ba câu hỏi vận hành (MS: định danh đối chiếu IFC; thuộc tính bắt buộc và bảo toàn; giao thức + tỷ lệ phát hiện + thời gian truy ngược) | MS:L159–L165; P1:L22 | Khác định nghĩa RQ2.1–2.3 của phạm vi khóa |
| RQ2 (văn bản chính thức) | "Bằng chứng trạng thái từ dữ liệu cảm biến có thể được tổ chức và liên kết với cấu kiện BIM và hồ sơ kiểm tra như thế nào để bảo đảm khả năng truy vết cấp cấu kiện?" | OL:L16; MS:L157; P1:L21 | Giữ nguyên trong các tệp; RF:L51 ghi có hai văn bản RQ2 (Charter) |
| GAP 1/2/3 | DX và P1: hồ sơ có trách nhiệm; phạm vi hiệu lực; kiểm chứng xác định | DX:L56–L60; P1:L26–L30 | Bị thay (phạm vi khóa: G-B, A2 và thiết kế đánh giá) |
| GAP-A/B/C | MS: định danh đã kiểm chứng; phạm vi hiệu lực + trách nhiệm; kiểm chứng xuyên chuỗi | MS:L259 | Bị thay; ký hiệu GAP-B ở MS khác GAP-B ở RF:L111 |
| Gap 2A/2B/2C | RF: bảo toàn nguồn gốc; bảo toàn phạm vi hiệu lực; duy trì định danh (lớp con của Khoảng trống 2 tiểu luận) | RF:L24, L72–L100 | Đề xuất 25/09 |
| C1–C3 (đóng góp) | DX/MS/BT/P1: khung truy vết cấp cấu kiện; hợp đồng bằng chứng / quản trị bằng chứng; giao thức kiểm chứng | DX:L78–L84; MS:L161–L165; BT:L29–L33; P1:L34–L37 | Bị thay bởi ĐG1–ĐG3; còn OL dùng "bốn điểm" (OL:L18) |
| H1–H5, B1–B5 (hình/bảng) | Mã hình và bảng của OL và RF | OL:L39–L53; RF:L320–L331 | Chỉ là mã hình/bảng, không phải quyết định |
| Trạng thái binding | UNBOUND / CANDIDATE / VERIFIED / REJECTED / SUPERSEDED (RF); "candidate, verified, rejected, closed" (MS); MULTI_CANDIDATE, HUMAN_SELECTED, SUSPECTED_IDENTITY_ANOMALY (DX) | RF:L296; MS:L320; DX:L104–L106 | Ba bộ từ vựng khác nhau |
| Nghị định 207/2026/NĐ-CP | Tham chiếu hồ sơ bảo trì | RF:L240 | RF ghi "pending official-source verification" → [CẦN KIỂM] |

---

## 4. Điểm lệch so với phạm vi đã khóa

Mức độ: Cao = làm đổi cấu trúc bài hoặc mâu thuẫn trực tiếp với phạm vi khóa; Trung = khác định nghĩa/tên nhưng ánh xạ được; Thấp = khác chi tiết. Phần 4.1 gồm cả 8 tệp (gộp), 4.2 chỉ prompt v1.

### 4.1 Các tệp B2 (DM, DX, OL, MS, BT, RF) so với phạm vi khóa

| Chiều | Tệp nói gì (trích ngắn + dòng) | Phạm vi khóa nói gì | Mức độ |
|---|---|---|---|
| Số thực thể | DM: 8 thực thể mới + 4 có sẵn = 12 (DM:L37–L52, L73–L186); MS: "mười thực thể" (liệt kê 11, có CORRESPONDENCE, không ACTION) (MS:L324); RF: "năm bản ghi lõi … hai bản ghi quan hệ phụ trợ", Action/Status_Event "không thuộc phạm vi tối thiểu" (RF:L191); BT: 6 nhóm thực thể (BT:L120–L127) | 6 thực thể: COMPONENT; SENSOR+SENSOR_MAPPING; EVIDENCE; INSPECTION_RECORD (qua EVIDENCE_USE); ACTION; STATUS_EVENT. Mô hình 10 thực thể phải ánh xạ sang 6 | Cao (12 / 10–11 / 7 / 6 nhóm; RF còn bỏ ACTION và STATUS_EVENT, là hai thực thể có trong lõi khóa) |
| Công cụ | DM: "SHACL là cơ chế kiểm chứng chính", bộ chuyển CSV→RDF, w3id (DM:L298, L301); MS: "registry lưu dạng CSV và chuyển sang RDF; quy tắc chạy bằng một bộ kiểm tra SHACL" (MS:L387); BT: "SHACL kết hợp truy vấn" (BT:L147); RF: SHACL/IDS "làm công cụ kiểm chứng", Dynamo, SQLite (RF:L15); PROG: Dynamo + DynamoMCP, add-in C#, MCP (PROG:L110–L115); DX: SHACL, IDS (DX:L27) | Python, IfcOpenShell, SQLite/JSON. KHÔNG RDF/SHACL/SPARQL/ontology (SOSA/SSN, PROV-O chỉ 1 bảng) | Cao (D1, D4 và bộ chuyển CSV→RDF mất cơ sở; MS còn đề nghị "tương ứng, SOSA/SSN, PROV-O, PAV" như chuẩn tái dùng MS:L316) |
| Số CQ | DM: CQ01–CQ12 (DM:L214–L227); DX: 5 CQ (DX:L100–L106); RF: dùng cả hai (RF:L240); OL, MS: 12 (OL:L28; MS:L287) | CQ01–CQ12 → 3 câu hỏi truy ngược | Trung (ánh xạ được: CQ05, CQ06, CQ07 là câu "ngược" trong DM; xem mục 8.4, ĐỀ XUẤT) |
| Luật | R01–R15 (29 mã con) viết bằng SHACL (DM:L233–L251) | R01–R17 → lọc về 5 ràng buộc C1, C3, C5, C6, C9 | Trung (xem mục 8.1: C9 không có luật tương ứng trực tiếp trong R01–R15) |
| Chỉ số (tên, số lượng) | M1 = tỷ lệ phát hiện quan hệ sai; M2 = tỷ lệ bản ghi đủ nguồn gốc; M3 = thời gian truy ngược (trung vị, p95, số bước nối) (DM:L288–L292; MS:L305); BT: 4 chỉ số – Đúng truy vết, Phát hiện liên kết sai, Đầy đủ và phù hợp, Thời gian truy ngược (bổ trợ) (BT:L101–L106) | M2 = chỉ số chính (tỉ lệ lỗi chèn mù bắt được theo nhóm); M1 = đủ thuộc tính (chỉ mô tả); M3 = truy ngược 3 câu hỏi người quản lý; M4 = phút/bản ghi | Cao (cùng tên M1, M2 nhưng nghĩa hoán đổi: M1 của tệp ≈ M2 khóa; M2 của tệp ≈ M1 khóa; M3 của tệp thiên về thời gian, M3 khóa là truy ngược; chưa có M4. BT thay hẳn bằng 4 chỉ số không đánh số) |
| Đối chứng | Không tệp nào định nghĩa B0 (hồ sơ kiểm định VN) hay B1 (IFC 4.3 + BCF 3.0 chưa mở rộng). Chỉ có "tra cứu thủ công" làm đường cơ sở cho thời gian truy ngược (DM:L292; MS:L305). "B1, B2, B3" trong các tệp là trạng thái siết bu lông của mẫu 1:10 (MS:L363, L377) | So với B0 (mã hóa tay 20–30 hồ sơ kiểm định VN) và B1 (IFC 4.3 theo Bellon 2025 [35] + BCF 3.0, cùng script, tắt C5, C6, C9) | Cao (thiếu hẳn thiết kế đối chứng B0/B1; va chạm ký hiệu B1) |
| Khoảng trống | DX, P1: GAP 1 (hồ sơ có trách nhiệm), GAP 2 (phạm vi hiệu lực), GAP 3 (kiểm chứng xác định) (DX:L56–L60); MS: GAP-A/B/C (MS:L259); RF: Gap 2A/2B/2C, Khoảng trống 3 "không thuộc Paper 2" (RF:L107) | G-B (bằng chứng → hành động có trách nhiệm) là chính; G-A vế A2 (phạm vi hiệu lực) là phụ; GAP1→G-B, GAP2→A2, GAP3 không còn là khoảng trống mà là thiết kế đánh giá | Cao (MS và DX còn coi GAP 3 / GAP-C là khoảng trống; RF đẩy phần hành động/trách nhiệm sang WP4/G5, ngược với G-B là khoảng trống chính. Vế A1 (đánh giá theo đơn vị độc lập) chỉ xuất hiện dưới dạng trường Inference_Unit, không phải khoảng trống) |
| RQ | RQ2 + RQ2.1 (định danh đối chiếu IFC, C1), RQ2.2 (thuộc tính bắt buộc và bảo toàn, C2), RQ2.3 (giao thức phát hiện + thời gian, C3) (MS:L159–L165); RF: RQ2-P2 + SRQ2.1–2.3 (RF:L162–L168); BT: (i)–(iii) (BT:L51) | RQ2 trên cùng BIM, so B0/B1 bắt được tỉ lệ nào lỗi chèn mù; RQ2.1 định danh (C1, C3); RQ2.2 phạm vi (C5, C9); RQ2.3 chuyển trạng thái (C6) | Cao (cùng nhãn RQ2.1–2.3, nội dung khác; RQ2.3 khóa là chuyển trạng thái, RQ2.3 của MS là giao thức kiểm chứng) |
| Đóng góp | C1 khung truy vết, C2 hợp đồng/quản trị bằng chứng, C3 giao thức kiểm chứng (DX:L80–L82; MS:L161–L165; BT:L31–L33); OL: bốn điểm (OL:L18); RF: "bảo toàn P/V/I" là đóng góp trung tâm (RF:L145) | ĐG1 mô hình 6 thực thể mở rộng IFC4.3+BCF3.0; ĐG2 hợp đồng bằng chứng + EVIDENCE_USE(within_scope, justification); ĐG3 STATUS_EVENT có căn cứ/vai trò/xác minh sau sửa + giao thức lỗi chèn mù | Trung–Cao (ĐG2 khớp C2; ĐG3 không có tương đương: tệp không coi STATUS_EVENT là đóng góp, RF còn đẩy ra ngoài; "giao thức kiểm chứng" nằm ở C3 trong tệp, nằm trong ĐG3 của khóa; không có "mở rộng IFC4.3 + BCF3.0" trong tệp nào — BCF 3.0 không xuất hiện trong 8 tệp) |
| Tạp chí đích | OL: không nêu; DX:L138: Automation in Construction, Journal of Computing in Civil Engineering, ITcon; MS: ghi độ dài từng mục, không nêu tạp chí; P1:L81: Automation in Construction, ~9.000 từ | BRIEF không nêu tạp chí đích | Thấp / [BRIEF không có dữ liệu để so] |
| Số lỗi chèn | DX: 9 loại, "hai trường hợp đã có đề xuất cụ thể" S4, S5 (DX:L112); MS: 9 loại gộp 7 nhóm, số ca [CẦN BỔ SUNG] (MS:L383); DM: 16 ca (DM:L259–L274); RF: 10 dòng lỗi cài (RF:L271–L282) | ~30 lỗi chèn mù, người chèn ≠ người viết luật; 4 nhóm: định danh-liên kết (C1,C3); phiên bản (C9); dùng ngoài phạm vi (C5,C9); chuyển trạng thái không căn cứ (C6) | Trung (khác số loại/nhóm; nhưng nguyên tắc "người thứ hai lập ca" đã có ở MS:L301, BT:L95, DM:L280, P1:L94 → phù hợp) |
| BIM 1:1 và 1:10 | Tệp gọi BIM là "công trình nguyên mẫu / mô hình nguyên mẫu 1:1", mẫu 1:10 là phòng thí nghiệm, Physical_Identity = FALSE (MS:L291, L326; BT:L131) | BIM 1:1 = nhà xưởng thật mà khung 1:10 mô phỏng; nối chỉ qua tương ứng thông tin | Thấp–Trung (MS:L293, R09 và R17 cấm dùng bằng chứng lab làm căn cứ kiểm tra cấu kiện thực; cần so với luận điểm khóa "thành căn cứ kiểm tra giải trình được"; tệp đặt tên "prototype" thay vì "nhà xưởng thật đã có thỏa thuận với chủ đầu tư" (MT3)) |
| Đối tượng đo của luận điểm | Tệp nói "trạng thái liên kết bu lông" là nhãn của khung 1:10 (MS:L363) | Luận điểm khóa: dữ liệu quan trắc không là kết luận hư hỏng, nhưng thành căn cứ kiểm tra giải trình được nếu mang nguồn gốc, phạm vi hiệu lực, lịch sử xử lý đến hành động | Thấp (tệp có "nguồn gốc", "phạm vi hiệu lực", nhưng "lịch sử xử lý đến hành động" bị tách sang WP4/G5 ở RF:L45, L191) |
| Mục tiêu MT1–MT3, đối chứng, M2 chỉ số chính | Tệp không nhắc MT1–MT3; P1:L71 hỏi "Paper 2 gồm MT2 hay MT2 + MT3" | MT2 mô hình thông tin; MT3 nhà xưởng thật; M2 chỉ số chính | Trung (P1 xác nhận chưa chọn) |

### 4.2 Khác biệt chính của prompt v1 (P1) so với phạm vi khóa

| Chiều | P1 nói gì | Phạm vi khóa nói gì | Mức độ |
|---|---|---|---|
| "Phạm vi đã khóa" của chính P1 | P1:L19 tự gọi "PAPER 2 – PHẠM VI ĐÃ KHÓA (không tự ý thay đổi)": RQ2.1–2.3, GAP 1–3, C1–C3, chuỗi lõi 5 mắt xích với Action_Status chỉ đọc (P1:L21–L37) | Phạm vi khóa hiện nay thay phần lớn các mục này (G-A/G-B, ĐG1–ĐG3, 6 thực thể, 5 ràng buộc) và bản của BRIEF ưu tiên cao hơn P1 | Cao (P1 đang tự coi là khóa nhưng đã bị thay) |
| Thực thể | "mô hình 10 thực thể" (P1:L47); framework liệt kê "thực thể và khóa" (P1:L85) | 6 thực thể | Cao |
| Công cụ | CQ_REGISTER có "truy vấn SPARQL chạy được"; RULES (SHACL R01–R17) (P1:L91–L92); "SHACL, IDS" chuẩn tái dùng (P1:L85) | Python, IfcOpenShell, SQLite/JSON; không SPARQL/SHACL | Cao |
| CQ và luật | CQ01–CQ12; R01–R17 (P1:L47, L85, L91) | 3 câu truy ngược; 5 ràng buộc | Trung |
| Chỉ số | M1–M3 (P1:L47, L99) | M1–M4, M2 chính | Cao |
| Đối chứng | Không có B0/B1 | B0, B1 | Cao |
| Số lỗi chèn | "≥3 ca/loại × 9 loại + ca hợp lệ đối chứng" (P1:L94); G3-N01…N11 (P1:L99) | ~30 lỗi, 4 nhóm | Trung |
| Khoảng trống và RQ | GAP 1–3; RQ2.1–2.3 như MS (P1:L22, L26–L32) | G-A/G-B; RQ2.1 định danh (C1,C3); RQ2.2 phạm vi (C5,C9); RQ2.3 chuyển trạng thái (C6) | Cao |
| Phạm vi MT | Yêu cầu so với "quyết định phạm vi luận án 10/2026": 2 bài báo từ 3 mục tiêu; bỏ CP4; ba campaign dùng chung S12; NCS tự dựng BIM nhà xưởng thật; hỏi MT2 hay MT2+MT3 (P1:L71) | MT1, MT2, MT3 (MT3 nhà xưởng thật đã có thỏa thuận) | Trung (P1 ghi nhận nhưng không giải; đây là điểm sát với phạm vi khóa nhất) |
| Quy tắc 5 và 6 | Không dùng 16/16; 8 cặp GUID là nghi ngờ (SUSPECTED_IDENTITY_ANOMALY) (P1:L61–L62) | Cùng quan điểm | Không lệch (đồng thuận) |
| Máy chỉ ghi tối đa candidate; verified/rejected/closed chỉ do người | P1:L64 | Chuyển trạng thái đúng vai trò (C6) | Không lệch |
| Tạp chí | Automation in Construction ~9.000 từ (P1:L81) | BRIEF không nêu | Thấp |
| Nguồn nhắc không nằm trong thư mục B2 | CURRENT_STATUS_AND_NEXT_DIRECTION.md v2.4, EVIDENCE_GATES_v2.1.md, G1_G2_INTERFACE_DECISION_REGISTER.csv, tiểu luận .docx, EVIDENCE_MATRIX_TLTQ_23092026.xlsx (P1:L44–L49) | | Thấp (ghi để kiểm kê, xem mục 6) |

---

## 5. Tài sản đáng giữ (cho Pha 1) và thứ nên bỏ

### 5.1 Nên giữ

| Tài sản | Tệp + dòng | Lý do |
|---|---|---|
| Trường và định danh của SENSOR, SENSOR_PLACEMENT (Valid_From/To, đóng dòng cũ rồi mở dòng mới, không sửa đè; Change_Reason, Superseded_By_Placement_ID; Field_Verified do người) | DM:L73–L105 | Nền cho SENSOR_MAPPING và ràng buộc C3 |
| CONDITION_EVIDENCE với 6 nhóm trường tối thiểu, Validity_Scope bắt buộc, Evidence_Grade, Superseded_By_Evidence_ID | DM:L123–L146 | Nền cho EVIDENCE và ĐG2 |
| EVIDENCE_USE: Scope_Snapshot, Acknowledged_By, Cross_Component_Reason | DM:L175–L182; RF:L223 | Gần như đúng với "EVIDENCE_USE(within_scope, justification)" của ĐG2; là cơ chế C5 |
| ACTION_STATUS_EVENT: From/To_Status, Actor_ID, Actor_Role, Reason, Basis_Refs, Post_Action_Verification_Ref; R11a–d, R12, R13 | DM:L184–L208, L246–L248 | Nền cho STATUS_EVENT và C6 (ĐG3). RF đã đẩy sang WP4/G5, nên cần cân nhắc lại theo phạm vi khóa |
| Nguyên tắc "máy chỉ ghi tối đa candidate; verified/rejected/closed do người" | PROG:L113; P1:L64; MS:L320 | Khớp C6 (đúng vai trò) |
| Neo kép Prototype_Component_ID + Binding_ID và ID tất định BND-\<sha256[:16]\> | DM:L54, L71, L299 | Đáp ứng ánh xạ về COMPONENT; cần ADR (RF:L228) |
| 8 ca lỗi thật RD-001…RD-008 và phát hiện "tham số Revit trùng, IFC xuất ra gán GlobalId mới" | PROG:L54, L62; DM:L302 | Ca mở đầu (tình huống thật) cho bài; vẫn là NGHI NGỜ cho đến khi có tệp nguồn (RF:L56) |
| 16 ca âm tính NT01a–NT10 làm mẫu thiết kế fixture (không dùng làm kết quả); ba điều kiện để thành bằng chứng (người khác tạo hoặc sinh ngẫu nhiên có hạt giống sau khi khóa; chạy trên chuỗi thật; báo cả ca bỏ sót) | DM:L259–L284 | Khớp "người chèn ≠ người viết luật" của phạm vi khóa |
| Hai loại đúng đắn (loại 1 quan hệ dữ liệu; loại 2 lắp đặt thực tế do người xác nhận) và hai tầng xác nhận | DM:L253–L257; RF:L183–L185; BT:L89–L91 | Làm giới hạn claim |
| Quy ước tương ứng thông tin 1:10 → 1:1, cờ Physical_Identity = FALSE, quy tắc bằng chứng lab chỉ gắn qua tương ứng đã duyệt | MS:L289–L293, L326–L330; BT:L129–L133 | Khớp "nối chỉ qua tương ứng thông tin" |
| Bảng tiền lệ "đã có / không claim là mới" và danh mục đối thủ gần nhất (Borkowski, García, Mariniello, Fang, Gragnaniello, Seiß, Hagedorn, Bellon) | DX:L39–L50; MS:L261–L275; BT:L77–L81 | Dùng cho Related work; ô Bellon còn trống |
| Phụ lục A: mức đọc từng nguồn (toàn văn / tóm tắt / qua Paper 1 / tài liệu kỹ thuật) | MS:L509–L525 | Hữu ích cho quy tắc 2 của dự án (nhãn [CHƯA ĐỌC TOÀN VĂN]) |
| Bảng "Claim – Evidence hiện có – còn thiếu – Gate", danh sách 15 evidence còn thiếu, scope firewall, phân loại MANDATORY/OPTIONAL/REQUIRES ADR | RF:L205–L231, L362–L376, L427–L443, L467–L477 | Trung thực về mức bằng chứng; dùng làm checklist Pha 1 |
| Khung P/V/I trên bốn bước chuyển của chuỗi | RF:L172–L181 | Đối chiếu tốt với 5 ràng buộc (xem mục 8.5) |
| Ma trận Information Requirement → CQ → dữ liệu → đáp án → tiêu chí | RF:L242–L251 | Khung cho 3 câu truy ngược |
| Thuật ngữ cố định (bằng chứng trạng thái, phạm vi hiệu lực, ngữ cảnh phiên bản mô hình, hồ sơ kiểm tra, tương ứng thông tin, liên kết, đáp án độc lập, ca lỗi cài sẵn) và cấm gọi tra cứu ngược là round-trip | MS:L27; RF:L130 | Nhất quán thuật ngữ |
| Rủi ro đã nêu: Level_Name trống, 718 vs 676, Bellon, hai cách đánh số | OL:L69–L77 | Danh sách việc tồn đọng |

### 5.2 Nên bỏ hoặc hạ cấp

| Thứ nên bỏ | Tệp + dòng | Lý do |
|---|---|---|
| Toàn bộ hạ tầng RDF/SHACL/SPARQL/ifcOWL/BOT/w3id, bộ chuyển CSV→RDF, quyết định D1, D4 | DM:L298, L301; PROG:L76, L171; MS:L387; P1:L91–L92 | Phạm vi khóa loại RDF/SHACL/SPARQL/ontology |
| Dùng 16/16, 0 dương tính giả, 5,5 ms, M2 = 2/2 làm số liệu bài | DM:L290–L292; PROG:L68 | Là kiểm thử đơn vị trên dữ liệu mẫu cực nhỏ (chính DM:L278 cảnh báo) |
| Cách đặt tên GAP 1–3, GAP-A/B/C, Gap 2A–2C và đóng góp C1–C3 | DX:L56–L84; MS:L259; RF:L72–L100 | Va chạm với G-A/G-B, ĐG1–ĐG3 và C1, C3, C5, C6, C9 |
| Mô hình 12 bảng, 10(+1) thực thể; DECISION_HISTORY, MODEL_VERSION, OBSERVATION_RUN, CORRESPONDENCE như bảng độc lập | DM:L37–L52; MS:L324 | Chỉ giữ ánh xạ vào 6 thực thể (xem mục 8.5) |
| Máy trạng thái 9 trạng thái đầy đủ, logic bốn mức hành động (Normal→Watch→Inspect→Priority) | DM:L186–L200; RF:L375 | Quá rộng so với STATUS_EVENT của phạm vi khóa; chỉ cần các chuyển có căn cứ, đúng vai trò, xác minh sau sửa |
| Mô tả Claude/MCP/add-in/IFC toolkit như phần của bài | BT:L179; PROG:L110–L115; RF:L337 | MS:L479 và D026 (RF:L373) đều loại khỏi bài; BT mâu thuẫn |
| Hình 3 của DX với số liệu giả lập; ví dụ S-07, C-12, CEI-0031, IR-0112 | DX:L7, L29, L114 | Chính tệp ghi giả lập; không dùng làm bằng chứng |
| Hai con số audit (718/16 hoặc 676/596) cho đến khi giải quyết K4 | DX:L112; PROG:L48 | Không đưa vào bản thảo trước khi thống nhất |
| Giả định "cross_campaign" cho bất kỳ bằng chứng nào | RF:L350 | Chưa chạy LOCO |
| Kết quả "7 nhóm lỗi" làm cơ sở so sánh | PROG:L68; MS:L383 | Không khớp 9/10 loại; phạm vi khóa dùng 4 nhóm |

---

## 6. Ghi chú bất thường

### 6.1 Trùng lặp và quan hệ giữa các tệp
1. OL, MS, BT cùng ngày 24/09 và cùng cấu trúc 8–9 mục; OL là bản ngắn có 4 điểm đóng góp, MS và BT dùng C1–C3. BT là bản thu gọn/làm mềm của MS (cùng tiêu đề, cùng nhóm tiền lệ), nhưng không chắc BT dẫn xuất từ MS: BT không có ngày, và RF:L526 liệt kê OL và BT là nguồn đã đọc nhưng không liệt kê MS.
2. DX (24/09) viết trên nền 15–16/09: vẫn "5 CQ", "GAP 1–3", "718 phần tử (16 ElementId)", "API_THREAD_TIMEOUT, nghi ngờ" (DX:L112), trong khi PROG ngày 23/09 đã nêu kết quả đối chiếu 23/09 (IFC xuất ra 0 GUID trùng, PROG:L54) và DM (23/09) có 12 CQ. DX không phải bản kế tiếp của DM mà là nhánh song song với nền cũ.
3. P1 (ngày 02/10 theo người giao) vẫn dùng GAP 1–3, C1–C3, 10 thực thể, R01–R17, M1–M3, nghĩa là không phản ánh RF (25/09) hay phạm vi khóa.

### 6.2 Mâu thuẫn nội bộ và giữa các tệp
4. Số thực thể: PROG "7", DM định nghĩa 8 thực thể mới (12 kể cả 4 bảng có sẵn), OL "7" (liệt kê 8 tên), MS "mười" (liệt kê 11), RF "7 bản ghi", BRIEF "10 v0.2". Chi tiết ở mục 2.2.
5. Số nhóm/loại lỗi: PROG và DM nói "7 nhóm lỗi", bảng DM có 10 nhãn nhóm; DX và MS 9 loại; RF 10 dòng lỗi cài; MS:L383 nói 9 loại "gộp theo bảy nhóm".
6. Số tiêu chí đóng Gate 2: RF 10 (Execution Lock §12), P1 12.
7. Số liệu audit: 718/16 (DX:L112) vs 676/596 (PROG:L48, L100). 13/09 là ngày audit của PROG; DX ghi "718 phần tử" từ tài liệu 15/09. Không tệp nào cho biết hai audit khác nhau ở điểm nào. Quan hệ giữa 676/718 và 3.356 prototype component không được giải thích (cần ghi phạm vi category).
8. Trạng thái 8 cặp GUID trùng: PROG:L54 (phát hiện đã xác nhận ở phía tham số Revit, IFC xuất ra không trùng) vs DX:L112 (nghi ngờ vì timeout) vs RF:L66, L358 (báo cáo 23/09, chưa xác minh trong repository). Theo BRIEF giữ "NGHI NGỜ".
9. Phạm vi Paper 2 về hành động: DX, MS, OL có hồ sơ có trách nhiệm và (OL, DM) máy trạng thái; RF:L107, L191 loại ACTION/Status_Event và Khoảng trống 3 ra khỏi Paper 2 (chuyển WP4/G5). Ngược với phạm vi khóa (G-B chính, ĐG3).
10. BT:L179 mô tả "Claude/MCP đóng vai trò điều phối truy vấn và tổng hợp" trong Methods trong khi MS:L479 loại hẳn sơ đồ vận hành Claude/MCP/add-in khỏi bài.
11. D2 neo kép: PROG và DM ghi "đã chốt"; RF:L53, L228 ghi "chưa được người hướng dẫn duyệt" và REQUIRES ADR. Đồng thời DM ghi "Tác giả nháp: Claude; người chốt NCS" và D1–D5 chốt "theo đề xuất" (DM:L1–L11).
12. Cấu hình cảm biến: MS:L363 mô tả S1, S2 và S3 (S3 chỉ campaign 2 và 3); P1:L71 ghi quyết định phạm vi 10/2026 là "ba campaign dùng chung cấu hình S12". Nếu S12 là S1+S2 thì S3/B3 trong MS:L328 (vùng giằng–cột) không còn dùng.
13. Chỉ số Paper 1 cho CP3: RF:L64 RF (random forest) 0,875; MS:L203 hai mô hình 0,875 và 0,690. Con số 0,690 không có trong RF.
14. Ngày tiểu luận tổng quan: v4 16/09 (DX:L5), bản 20/09 (PROG:L30), 23/09 HOÀN THIỆN (OL:L9, RF:L528, P1:L44). Mục tham chiếu cũng khác: 5.5.2/5.6.2/5.7.2 (PROG, OL), 5.2.2 (RF:L74). Ghi nhận có ít nhất hai phiên bản tiểu luận; cần chọn.

### 6.3 Va chạm ký hiệu (nguy cơ nhầm)
15. D1–D5 (DM) vs D001–D026 (sổ quyết định); RF dùng "D2" và "D003"… cùng lúc.
16. C1–C3 (đóng góp) vs C1, C3, C5, C6, C9 (ràng buộc khóa) vs C-01, C-05 (xung đột RF).
17. B1, B2, B3 (trạng thái bu lông) vs B0/B1 (đối chứng khóa) vs B1–B5 (bảng RF) vs B1–B4 (bảng OL).
18. M1–M3 hai nghĩa khác nhau (mục 4.1).
19. GAP-B: MS:L259 = phạm vi hiệu lực + trách nhiệm; RF:L111 "GAP-B (identity, Borkowski)" = định danh; G-B khóa = bằng chứng → hành động có trách nhiệm. Ba nghĩa. GAP-A: MS = định danh; G-A khóa = đánh giá theo đơn vị độc lập + phạm vi hiệu lực.
20. RQ2.1–2.3: MS (định danh/thuộc tính/giao thức), RF dùng SRQ2.1–2.3 (yêu cầu/định danh/toàn vẹn), khóa (định danh/phạm vi/chuyển trạng thái).
21. Ba bộ từ vựng trạng thái binding: UNBOUND/CANDIDATE/VERIFIED/REJECTED/SUPERSEDED (RF:L296); candidate/verified/rejected/closed (MS:L320); MULTI_CANDIDATE/HUMAN_SELECTED/SUSPECTED_IDENTITY_ANOMALY (DX:L104–L106).
22. Ký hiệu "Hình/Bảng" khác nhau ở năm tệp (xem mục 2.4).

### 6.4 Tham chiếu tệp và dữ liệu không có trong thư mục B2
23. Không có trong thư mục: real_defect_cases_v0.1.csv, gate2_3_shapes_draft_v0.1.ttl, run_negative_tests.py, negative_test_results_v0.1.csv (DM:L19–L25), registries/schema.json, decision_history.csv, gate2_baseline_IFC4X3_ADD2.ids (PROG:L38, L80, L94), verification bundle, add-in, registry 6 IFC (PROG:L34–L46). RF:L56, L358 ghi cũng không có trong repository ngày 25/09. Do đó số 6 IFC, 3.356, 10.328, 718/676, 8 cặp chưa thể kiểm.
24. P1:L44–L49 nhắc: tiểu luận .docx, EVIDENCE_MATRIX_TLTQ_23092026.xlsx, CURRENT_STATUS_AND_NEXT_DIRECTION.md v2.4, EVIDENCE_GATES_v2.1.md, G1_G2_INTERFACE_DECISION_REGISTER.csv, PAPER2_BAO_CAO… (K1–K11, R01–R17, G3-P/N) và PAPER2_COMPLETE… Hai tệp cuối có bản text trong /home/claude/p2/txt/ nhưng không thuộc nhóm B2; các tệp còn lại không có trong thư mục text.
25. DX: bốn ảnh Hình 1–4 nằm ở media/ và không có trong bản text; DM:L35 ghi bảng quan hệ "chuyển từ sơ đồ ER" (sơ đồ gốc không có). Phần ảnh của DX không kiểm được.
26. P1:L50 ghi "Nếu không tìm thấy một tệp, ghi MISSING" — áp dụng cho các mục trên.
27. Tên tệp: RF:L9 ghi tên "PAPER2_REFINED_DIRECTION_PROVENANCE_VALIDITY_IDENTITY_v1.0.docx", tệp thực tế có hậu tố ngày "v1.0.25092026". PROG và DM không có ngày/phiên bản trong tên (DM:v0.2 trong tên; PROG có 20260923). BT không có ngày trong tên lẫn nội dung. Ngày sửa 24/09 của DM không khớp ngày ghi trong DM (23/09).

### 6.5 Trích dẫn, DOI và nguồn đáng kiểm
(Không có công cụ web trong phiên này; AU không kiểm DOI. Danh sách là điểm cần [CẦN KIỂM], không phải kết luận là sai.)
28. Phần lớn DOI 2025–2026 trong MS:L527–L621 và BT:L240–L272 (Borkowski 2026 Technologies 14(7) 413; García 2026 Appl. Sci. 16(5) 2562; Piras 2026 Appl. Sci. 16(10) 4642; Fang 2025 Buildings 15(22) 4096; Mariniello 2025 AiC 180 106558; Seiß 2025 AiC 177 106268; Bellon 2025 AiC 174 106157; Jäkel 2025 ITcon 30; Aydın 2025 IEEE ACDSA) chưa có xác nhận trong tệp ngoài ghi chú "DOI kiểm qua Zotero hoặc OpenAlex" (MS:L511).
29. Năm xuất bản lệch giữa tệp: Ramasso et al. 2024 (PROG:L157, [17]) vs 2025 (MS:L599); Kamariotis, Chatzi & Straub 2023 (PROG:L161, [26]) vs Kamariotis et al. 2024, Data-Centric Engineering 5, e27 (MS:L569). Số thứ tự tài liệu: Bellon [33] (PROG:L147) vs BRIEF "Bellon 2025 [35]". Hai bản tiểu luận khác nhau có thể đánh số khác nhau.
30. Bellon et al. (2025) chỉ có tóm tắt (DX:L142; MS:L241, L519; RF:L74, L356), trong khi BRIEF dùng Bellon 2025 [35] làm cơ sở định nghĩa B1 (IFC 4.3). Rủi ro dùng nguồn chưa đọc toàn văn làm nền cho đối chứng.
31. García et al. (2026b) "From IFC validation to publish/hold decisions" (Zotero ZNSZE47J) chưa đọc (RF:L356).
32. Mitchell et al. (2019) chỉ đọc "siêu dữ liệu và nội dung chung" nhưng được dùng ở MS:L247, L441 (MS:L521 tự đánh dấu cần đọc toàn văn).
33. Velez (2021), bài đăng diễn đàn SourceForge, là nguồn duy nhất cho hành vi exporter với IfcGUID trùng (MS:L207, L613, L524). MS tự xếp "Tài liệu kỹ thuật".
34. Nghị định 207/2026/NĐ-CP (RF:L240): RF ghi "Legal reference pending official-source verification" → [CẦN KIỂM].
35. PROG:L169–L171 gợi ý nhóm 5 "ngoài tiểu luận" (Mitchell, Wilkinson, W3C SHACL, Rasmussen, Pauwels & Terkaj) với ghi chú "cần tự kiểm tra DOI"; chỉ Mitchell được dùng trong MS.
36. PROG:L125 gọi Mariniello 2025 là "SHERPA"; MS và BT không dùng tên này.
37. Đơn vị công tác ghi trên MS:L17 "Trường Đại học Bách khoa – Đại học Đà Nẵng" và MS:L559 "Da Nang University of Science and Technology"; danh tính tài khoản của người dùng trong phiên là hanhc@ntu.edu.vn (NTU). Cần NCS xác nhận đơn vị trước khi dùng cho bản thảo. [CẦN KIỂM]

---

## 7. Chuỗi phiên bản (23/09 → 25/09)

Thứ tự dựa trên ngày người giao việc cung cấp (23/09; DM sửa 24/09; DX 24/09; OL 24/09; MS 24/09 chiều; BT 24/09 tối; RF 25/09) và đối chiếu chéo nội dung (RF:L526 nêu OL và BT là nguồn đã đọc). Bản text không mang ngày sửa; BT không có ngày trong nội dung. Mức chắc chắn của thứ tự MS → BT: trung bình (xem ghi chú dưới bảng).

| # | Bản | Ngày | Cơ sở/nguồn khai báo | Đổi gì so với bản trước (hoặc điểm khác biệt chính) |
|---|---|---|---|---|
| 0 | gate2_3_data_model v0.1 | Không có trong thư mục | DM:L17 nhắc "thay đổi so với v0.1" | Không xem được. DM ghi v0.2 thêm: ghi nhận D1–D5, thêm real_defect_cases_v0.1.csv (8 ca lỗi thật), cập nhật bước tiếp theo |
| 1 | PROG + DM v0.2 | 23/09 (nội dung DM ghi 2026-09-23; người giao ghi DM sửa 24/09) | Tiểu luận (tiểu luận 5.5.2, 5.6.2, 5.7.2), registry Gate 2 hiện có | Mở đường SHACL + CSV: 8 thực thể mới (neo kép), D1–D5 chốt, 12 CQ (chưa khóa), R01–R15 chạy được, 16 ca âm tính 16/16, M1–M3, phát hiện 8 cặp IfcGUID trùng và ca RD-001…008, đối chiếu 23/09 (573442 lệch GUID) |
| 2 | DX | 24/09 | Tiểu luận v4 (16/09), khóa thực thi Gate 2-3 (15/09), đọc sâu 4 bài 16/09 | Không tiếp nối DM: quay lại khung 15–16/09 – GAP 1–3, C1–C3, 5 CQ, 9 loại lỗi, bảng tiền lệ, "Gate 2 0/10", "718/16, nghi ngờ". Thêm 5 câu hỏi quản lý, ví dụ S-07, nơi gửi (AiC, JCCE, ITcon) |
| 3 | OL | 24/09 | Tiểu luận 23/09, DM, PROG | Gộp DM vào outline 9 mục; 4 điểm đóng góp (tiểu luận 5.7.2); 7 thực thể, R01–R15, CQ01–CQ12, M1–M3; thêm trạng thái xanh/vàng/đỏ, ghi 4 rủi ro (Bellon; hai cách đánh số; 718 vs 676; Level_Name) |
| 4 | MS | 24/09 chiều (nội dung: "24/09/2026") | Như OL + ghi mức đọc nguồn | Đổi 4 điểm đóng góp thành C1–C3 và gắn RQ2.1–2.3; thêm CORRESPONDENCE, 10(+1) thực thể, bỏ ACTION/ACTION_STATUS_EVENT; thêm đáp án độc lập do người thứ hai lập, chín loại lỗi gộp bảy nhóm; thêm ví dụ xuyên suốt REC0004; thêm Phụ lục A, tài liệu tham khảo, 8 hình 10 bảng; chỉ số M1–M3 giữ; nhiều ô [CẦN BỔ SUNG] |
| 5 | BT | 24/09 tối (không có ngày trong nội dung) | Không khai báo | Biên tập MS: giữ C1–C3; bỏ mã R/CQ/M và hầu hết con số; đổi RQ2.1–2.3 thành câu hỏi (i)–(iii); đổi M1–M3 thành 4 chỉ số (đúng truy vết; phát hiện liên kết sai; đầy đủ và phù hợp; thời gian truy ngược bổ trợ); thêm "hai tầng xác nhận độc lập"; thêm mô tả Claude/MCP trong 5.5; còn 6 hình 6 bảng, tài liệu tham khảo rút gọn |
| 6 | RF v1.0 | 25/09 | Nguồn đọc: Charter v1.1 và v2.1.2, ADR-2026-001, Direction v2.3, Evidence Gates, Source-of-truth hierarchy, Terminology Control, Execution Lock 15/09, Interface G1→G2 v1.1, 10_NOVELTY_CHECK…, PROG, DM, DX, OL, BT (RF:L524–L528) | Đổi trục sang "bảo toàn nguồn gốc – phạm vi hiệu lực – định danh" (P/V/I); Gap 2A/2B/2C; SRQ2.1–2.3, V2.1–V2.3; chỉ còn 7 bản ghi, loại ACTION/STATUS_EVENT; Khoảng trống 3 sang WP4/G5; D2, Model_Version_ID, Scope_Snapshot xếp REQUIRES ADR; thêm "Evidence is currently insufficient", xung đột nguồn, 15 evidence còn thiếu, danh sách tệp kỹ thuật không tìm thấy trong repository, roadmap 0–9, bàn giao Gate 4 |
| 7 | P1 (prompt v1) | 02/10 theo người giao; không có ngày trong tệp | PAPER2_BAO_CAO…, tiểu luận 23/09, DX, DM, Execution Lock… | Không thừa kế RF: dùng GAP 1–3, C1–C3, 10 thực thể, R01–R17, CQ01–CQ12, M1–M3, SPARQL/SHACL; đặt Pha 0–4 với 5 checkpoint; đưa quyết định phạm vi 10/2026 (2 bài từ 3 mục tiêu, bỏ CP4, S12) vào Pha 0. Đã bị prompt v2 thay |

**Bản cuối của hướng đi:** RF (25/09, v1.0), tự nhận chưa duyệt, mức nguồn thấp (mức 7) và không thay Charter, ADR, Direction Lock hay Execution Lock (RF:L12–L13). Hướng này đã bị phạm vi khóa vượt qua (G-A/G-B, 6 thực thể, không RDF/SHACL, B0/B1), nên đề xuất đối xử như bản cuối của nhánh, không phải nguồn hiệu lực.

**Bản cuối của outline:** BT (24/09 tối) theo thứ tự thời gian được giao; MS (24/09 chiều) là bản chi tiết nhất. RF (25/09) không phải outline bài báo nhưng là tài liệu mới nhất định nghĩa số bản ghi, bảng/hình dự kiến (H1–H5, B1–B5), sub-RQ. Nên coi: cấu trúc mục = BT/MS; thiết kế dữ liệu và đánh giá = RF.

Ghi chú về độ chắc: (a) trật tự MS → BT dựa vào thông tin người giao việc; nội dung RF:L526 nhắc BT chứ không nhắc MS, và BT có mô tả Claude/MCP trái với MS:L479, nên không loại trừ BT là nhánh song song; (b) DX là nhánh nền cũ, không nằm trên đường DM → OL → MS → BT → RF; (c) các tệp trên đều là mức "đề xuất để thảo luận, chưa qua duyệt của người hướng dẫn" (DX:L7; OL:L7; RF:L12).

---

## 8. Danh mục luật R, câu hỏi CQ, chỉ số, và đề xuất ánh xạ sơ bộ

Mọi cột "ĐỀ XUẤT" dưới đây là đề xuất của AU để thảo luận, không phải nội dung của tệp và chưa được NCS hay GVHD duyệt. Ràng buộc khóa: C1 không mồ côi; C3 thời điểm đo trong hiệu lực ánh xạ; C5 dùng ngoài phạm vi phải có lý do; C6 bước chuyển có căn cứ và đúng vai trò; C9 căn cứ còn hiệu lực tại thời điểm chuyển.

### 8.1 Luật R01–R17

Nguồn: DM mục A.4 (DM:L233–L251). R16 và R17 không có định nghĩa trong 8 tệp B2.

| Mã | Nội dung trong tệp | Mức | Ca thử | Tệp + dòng | ĐỀ XUẤT ánh xạ ràng buộc khóa |
|---|---|---|---|---|---|
| R01 | Condition_Evidence_ID và Inspection_Record_ID duy nhất | Violation | NT01a | DM:L235 | Hỗ trợ C1 (khóa không trùng, tiền điều kiện của "không mồ côi") |
| R02 | Mọi tham chiếu trỏ tới bản ghi tồn tại và đúng loại | Violation | NT02 | DM:L236 | C1 |
| R03a | Valid_To sau Valid_From | Violation | NT06 | DM:L237 | C3 |
| R03b | Một cảm biến không có hai ánh xạ chồng lấn | Violation | NT06 | DM:L237 | C3 |
| R04 | Lần thu nằm trong thời gian hiệu lực của ánh xạ | Violation | NT04 | DM:L238 | C3 (trực tiếp) |
| R05a | Binding thuộc đúng cấu kiện | Violation | NT05 | DM:L239 | C1 (liên kết nhất quán) |
| R05b | Không có nội dung riêng; DM gắn R05b, R05c với cặp Target_Prototype_Component_ID, Target_Binding_ID (neo kép) | Violation | NT05 | DM:L134, L239 | C1 (hiểu là nhất quán hai khóa neo; xác nhận lại với tệp .ttl) |
| R05c | Cùng phiên bản model với ánh xạ | Violation | NT05 | DM:L239 | C9 (nhóm "phiên bản") |
| R06 | Đủ 6 trường tối thiểu | Violation | NT10 | DM:L240 | Ngoài 5 ràng buộc; thuộc chỉ số "đủ thuộc tính" (M1 khóa), có thể là NOT NULL của schema |
| R06b | Đã kiểm chứng thì phải có metric và số đơn vị độc lập | Violation | NT10 | DM:L240 | Ngoài 5 ràng buộc (cùng R06) |
| R07 | Giao thức rò rỉ (chia ngẫu nhiên theo cửa sổ) chỉ được not_validated | Violation | NT07c | DM:L150, L241 | C5 (kiểm tại khâu tạo bằng chứng; tiền điều kiện của "within_scope") |
| R07b | cross_campaign đòi hỏi LOCO | Violation | NT07c | DM:L152, L241 | C5 (như R07) |
| R08a | Hồ sơ dẫn bằng chứng phải chụp lại phạm vi | Violation | NT07a | DM:L242 | C5 |
| R08b | Bản chụp bằng Validity_Scope gốc | Violation | NT07a | DM:L181, L242 | C5; có thể C9 nếu phát biểu "bản gốc còn hiệu lực tại lúc dùng" |
| R08c | Không có nội dung riêng trong DM (bảng ghi "R08a–d") | Violation | — | DM:L242 | Chưa xác định (DM không tách riêng c) |
| R08d | Có người xác nhận đã đọc phạm vi (Acknowledged_By) | Violation | NT07a | DM:L181, L242 | C5 (justification) |
| R09 | Bằng chứng lab_1_10 không làm căn cứ kiểm tra cấu kiện công trình thực | Violation | NT07b | DM:L154, L243 | C5 (cần đối chiếu với luận điểm khóa, xem mục 4.1) |
| R09b | Dẫn bằng chứng not_validated | Warning | không | DM:L244 | C5 (mức cảnh báo) |
| R10a | Bằng chứng khớp cấu kiện của cảm biến (Link_Basis) | Violation | NT03a | DM:L136, L245 | C3 (liên kết sensor–cấu kiện); phần "gắn nhầm" chỉ bắt được với đáp án độc lập |
| R10b | Hồ sơ khớp cấu kiện của bằng chứng; khác thì phải có Cross_Component_Reason | Violation | NT03a | DM:L182, L245 | C5 (dùng ngoài phạm vi phải có lý do) |
| R11a | Action_Status = To_Status của sự kiện mới nhất | Violation | NT08a | DM:L204, L246 | C6 |
| R11b | Chuyển trạng thái hợp lệ theo máy trạng thái | Violation | NT08b | DM:L190–L200, L246 | C6 |
| R11c | From_Status = To_Status của sự kiện liền trước | Violation | NT08b | DM:L206, L246 | C6 |
| R11d | Có người (Actor, Actor_Role) và lý do | Violation | NT08b | DM:L246 | C6 (đúng vai trò, có căn cứ) |
| R12 | verified_closed bắt buộc có Post_Action_Verification_Ref | Violation | NT08c | DM:L208, L247 | C6 (xác minh sau sửa chữa) |
| R13 | Hồ sơ chỉ closed khi binding đã được con người ghi verified | Violation | NT09 | DM:L172, L248 | C6 (đúng vai trò) |
| R14a | IfcGUID Revit khác BIM_GUID | Warning | NT01b | DM:L249 | Nhóm "định danh-liên kết"; không thuộc 5 ràng buộc theo chữ; đề xuất gộp vào C1 hoặc giữ như kiểm tra tiền xử lý |
| R14b | Binding lệch GUID nhưng bị ghi verified | Violation | NT03b | DM:L250 | Như R14a (liên quan C6 vì liên quan quyền verified) |
| R15 | IfcGUID Revit trùng trong cùng phiên bản model | Violation | NT01b | DM:L251 | Như R14a |
| R16 | Chưa có định nghĩa trong 8 tệp B2 (P1:L47, L85 nhắc "R01–R17"; MS:L355 nhắc "hai quy tắc tương ứng mới") | — | — | P1:L47, L85; MS:L355 | Không ánh xạ được từ B2. Ghi chú: tìm nhanh (grep, không đọc toàn tệp, ngoài nhóm B2) trong PAPER2_BAO_CAO…md thấy R16 [ĐỀ XUẤT] = bằng chứng lab_1_10 chỉ gắn tới cấu kiện 1:1 qua CORRESPONDENCE đã duyệt có Physical_Identity = FALSE (dòng 431, 517) |
| R17 | Như trên | — | — | P1:L47, L85; MS:L355 | Cùng ghi chú: R17 [ĐỀ XUẤT] = bằng chứng lab_1_10 chỉ được hồ sơ có Inspection_Context = lab_specimen trích dẫn (cách viết cụ thể của R09); đề xuất tương ứng C5 |

Nhận xét ánh xạ (ĐỀ XUẤT): C1 ← R01, R02, R05a, R05b; C3 ← R03a, R03b, R04, R10a; C5 ← R07, R07b, R08a–d, R09, R09b, R10b (+R17); C6 ← R11a–d, R12, R13; C9 ← R05c, R08b. Không luật nào trong R01–R15 phát biểu trực tiếp "căn cứ còn hiệu lực tại thời điểm chuyển" (C9 của STATUS_EVENT): ACTION_STATUS_EVENT có Basis_Refs (DM:L188) và CONDITION_EVIDENCE có Superseded_By_Evidence_ID (DM:L146), nhưng không có luật nối hai trường này. Cần luật mới nếu giữ C9 như khóa. R06, R06b, R14a/b, R15 nằm ngoài 5 ràng buộc (có thể thành M1 hoặc bước tiền xử lý).

### 8.2 Câu hỏi năng lực CQ01–CQ12 (DM:L214–L227)

Tiêu chí lấy nguyên từ DM. Chưa khóa (chưa ghi SHA-256).

| Mã | Câu hỏi | Chiều (DM) | Tiêu chí chấp nhận | ĐỀ XUẤT ánh xạ ràng buộc | ĐỀ XUẤT: có là câu truy ngược cho M3 khóa? |
|---|---|---|---|---|---|
| CQ01 | Tại thời điểm t, cảm biến S gắn cấu kiện nào, theo phiên bản model nào | thuận | Trả đúng 0 hoặc 1 ánh xạ; không bao giờ 2 | C3, C1 | Không |
| CQ02 | Bằng chứng E từ lần thu, cấu hình cảm biến, phiên bản xử lý, giao thức, độ bất định, phạm vi hiệu lực nào | thuận | Đủ 6/6 trường tối thiểu | (đủ thuộc tính; M1 khóa) | Không |
| CQ03 | Cấu kiện C có bằng chứng nào, mỗi bằng chứng có phạm vi gì | thuận | Liệt kê đủ; mỗi dòng có Validity_Scope | C5 (phạm vi) | Không |
| CQ04 | Cấu kiện C có hồ sơ kiểm tra nào, hồ sơ nào do bằng chứng kích hoạt và là bằng chứng nào | thuận | Mọi hồ sơ evidence_triggered có ≥1 EVIDENCE_USE | C1 | Không |
| CQ05 | Từ hành động A truy ngược về hồ sơ, bằng chứng, lần thu, SHA-256 dữ liệu thô | ngược | Đường truy hoàn chỉnh; đo thời gian (M3) | C1 (không mồ côi trên toàn đường truy) | Có – ứng viên 1 |
| CQ06 | Trạng thái hiện thời của A do ai chuyển, khi nào, vì sao, căn cứ nào | ngược | Mọi sự kiện có Actor, Role, Reason | C6 (và C9) | Có – ứng viên 2 |
| CQ07 | Khi được dùng để kích hoạt kiểm tra, bằng chứng có nằm trong phạm vi hiệu lực không, và ai đã xác nhận đã đọc phạm vi | ngược | Scope_Snapshot bằng Validity_Scope; có Acknowledged_By | C5 | Có – ứng viên 3 |
| CQ08 | Hồ sơ nào đã closed trên binding chưa được con người xác nhận | kiểm tra | Kết quả rỗng | C6 | Không |
| CQ09 | Bản ghi nào mồ côi, trùng định danh, xung đột hoặc có ánh xạ lỗi thời | kiểm tra | Tính vào M1 | C1, C3 | Không |
| CQ10 | Bằng chứng nào thiếu trường nguồn gốc | kiểm tra | Tính vào M2 | (đủ thuộc tính) | Không |
| CQ11 | Sau khi di chuyển cảm biến, có bằng chứng nào đang được đọc theo ánh xạ mới không | kiểm tra | Kết quả rỗng | C3 (và C9) | Không |
| CQ12 | IfcGUID lưu trong Revit có khớp GlobalId của binding trong phiên bản IFC nêu không | kiểm tra | Mọi phần tử lệch được liệt kê; không phần tử lệch nào verified | (định danh; R14, R15) | Không |

CQ-1…CQ-5 của DX (DX:L100–L106), 5 câu: CQ-1 xuôi (từ Condition_Evidence_ID), CQ-2 ngược (từ Inspection_Record_ID, trả bằng chứng, cảm biến, đợt đo, người rà soát, Action_Status; ID không tồn tại trả NOT_FOUND), CQ-3 định danh (Sensor_ID; không tự nâng MULTI_CANDIDATE thành HUMAN_SELECTED), CQ-4 hiệu lực (PASS nếu ngữ cảnh thuộc applicability_set, ngược lại FAIL SCOPE_VIOLATION), CQ-5 bất thường (hai cấu kiện trùng IfcGUID → SUSPECTED_IDENTITY_ANOMALY, không tự chuyển VERIFIED hoặc REJECTED). Tương ứng gần đúng với CQ05, CQ01, CQ07, CQ12 của DM (ĐỀ XUẤT; RF:L242–L251 đã dùng các cặp "CQ07 / CQ-4", "CQ-2 / CQ05", "CQ12 / CQ-5").

**ĐỀ XUẤT ba câu hỏi truy ngược** (ghi rõ để NCS chọn): (1) CQ05, hành động → hồ sơ → bằng chứng → lần thu → SHA-256; (2) CQ06, ai chuyển trạng thái, khi nào, vì sao, căn cứ nào; (3) CQ07, bằng chứng có nằm trong phạm vi khi được dùng, ai đã xác nhận đã đọc. Lý do: ba câu này là các câu duy nhất được DM ghi chiều "ngược" (DM:L220–L222) và mỗi câu chạm một trục của phạm vi khóa (nguồn gốc/định danh; chuyển trạng thái; phạm vi hiệu lực). Phương án thay thế: CQ-2 của DX thay cho CQ05.

### 8.3 Chỉ số và metric

| Chỉ số | Định nghĩa trong tệp | Tệp + dòng | ĐỀ XUẤT ánh xạ sang M1–M4 khóa |
|---|---|---|---|
| M1 (tệp) | Tỷ lệ phát hiện quan hệ sai: số ca lỗi phát hiện / số ca cài, báo theo từng nhóm lỗi, kèm tỷ lệ dương tính giả trên chuỗi hợp lệ. Lần chạy nháp 16/16, 0 FP | DM:L290; PROG:L68; OL:L29; MS:L305; RF:L284 | Gần M2 khóa (tỉ lệ lỗi chèn mù bắt được theo nhóm) |
| M2 (tệp) | Tỷ lệ bản ghi đủ nguồn gốc: số bằng chứng đủ 6 trường tối thiểu (và R06b nếu áp dụng) / tổng bằng chứng. Nháp 2/2 | DM:L291; MS:L305 | Gần M1 khóa (đủ thuộc tính, chỉ mô tả) |
| M3 (tệp) | Thời gian truy ngược: trung vị và p95 của CQ05, số bước nối; so với tra cứu thủ công qua nhiều hệ thống. Nháp 5,5 ms, 5 bước nối | DM:L292; MS:L305 | M4 khóa (phút/bản ghi) về phần thời gian; M3 khóa (truy ngược 3 câu hỏi người quản lý) cần tỉ lệ PASS của CQ05–CQ07, không có trong M3 của tệp |
| 4 chỉ số của BT | (1) Đúng truy vết: truy vấn trả đúng toàn bộ tập kỳ vọng / tổng truy vấn hợp lệ, báo xuôi/ngược; (2) Phát hiện liên kết sai: phát hiện / cài, từng loại, bỏ sót, dương tính giả; (3) Đầy đủ và phù hợp của bằng chứng: bản ghi đủ trường bắt buộc và dùng đúng ngữ cảnh / tổng; (4) Thời gian truy ngược (bổ trợ) | BT:L101–L106 | (1) ≈ M3 khóa; (2) ≈ M2 khóa; (3) ≈ M1 khóa, thêm vế "dùng đúng ngữ cảnh" (khác M1 khóa chỉ mô tả); (4) ≈ M4 khóa |
| Tử số/mẫu số, bỏ sót, dương tính giả | Yêu cầu báo cáo theo từng nhóm lỗi | DM:L279–L284; DX:L118; RF:L284 | Phù hợp M2 khóa |
| PASS/FAIL theo CQ | Mỗi CQ có đáp án định trước, tiêu chí PASS | DX:L100–L106; RF:L242–L251 | Dùng cho M3 khóa |
| Validated_Metric_Name/Value, CI_Low/High, N_Independent_Units, Permutation_p | Trường của CONDITION_EVIDENCE (mức 2, của quy trình), không phải chỉ số của bài | DM:L141 | Ngoài M1–M4 (trường dữ liệu, vế A1 "đơn vị độc lập") |
| Macro-F1, balanced accuracy, SD_fold | Chỉ số của Paper 1, bài này không đánh giá lại | MS:L203, L363; RF:L64 | Ngoài |
| Bốn chỉ số IfcGUID của Fang et al. (đầy đủ, hợp lệ, duy nhất, ổn định) | Tiền lệ, không phải chỉ số của bài | MS:L235 | Ngoài (tham khảo cho nhóm định danh) |
| Thiếu hoàn toàn | Không tệp nào đo B0/B1; không có chỉ số "phút/bản ghi" riêng; không có M3 khóa dạng 3 câu hỏi | — | Cần thiết kế mới |

### 8.4 Các ca thử âm tính NT và nhóm lỗi (DM:L261–L274) với ánh xạ ĐỀ XUẤT

| Ca | Nhóm lỗi trong DM | Luật bắt | ĐỀ XUẤT nhóm lỗi khóa | ĐỀ XUẤT ràng buộc |
|---|---|---|---|---|
| NT01a (tổng hợp), NT01b (thật) | Định danh trùng | R01; R15 | Định danh-liên kết | C1 (hoặc tiền xử lý) |
| NT02 | Mồ côi | R02 | Định danh-liên kết | C1 |
| NT03a (tổng hợp), NT03b (thật) | Gắn nhầm cấu kiện | R10a/b; R14b | Định danh-liên kết | C3 |
| NT04 | Liên kết lỗi thời | R04 | Định danh-liên kết | C3 |
| NT05 | Sai phiên bản model | R05c | Phiên bản | C9 |
| NT06 | Liên kết xung đột | R03b | Định danh-liên kết | C3 |
| NT07a / NT07b / NT07c | Ngoài phạm vi hiệu lực | R08b / R09 / R07 | Dùng ngoài phạm vi | C5 |
| NT08a / NT08b / NT08c | Lịch sử trạng thái | R11a / R11b,c / R12 | Chuyển trạng thái không căn cứ | C6 |
| NT09 | Người trong vòng lặp | R13 | Chuyển trạng thái không căn cứ | C6 |
| NT10 | Thiếu nguồn gốc | R06 | (ngoài 4 nhóm; thuộc "đủ thuộc tính") | — |

### 8.5 ĐỀ XUẤT bảng ánh xạ sơ bộ 10(–12) thực thể v0.2 và MS sang 6 thực thể khóa

Nguồn danh sách thực thể: DM:L37–L52 (12 thực thể gồm 4 bảng cũ), MS:L324 (10+1). ĐỀ XUẤT; chưa duyệt.

| Thực thể trong DM/MS | Trường/thực thể khóa đích (ĐỀ XUẤT) | Ghi chú |
|---|---|---|
| PROTOTYPE_COMPONENT | COMPONENT | Khóa ổn định của cấu kiện |
| BIM_BINDING | COMPONENT (thuộc tính: BIM_GUID, Binding_ID, trạng thái binding) hoặc bảng con của COMPONENT | Khóa thay thế; RF:L227 xếp Binding_ID là "OPTIONAL (metadata triển khai)" |
| MODEL_VERSION | Thuộc tính Model_Version_ID của COMPONENT (và của EVIDENCE khi cần) | RF:L220 xếp REQUIRES ADR |
| DECISION_HISTORY (người xác nhận verified/rejected cho binding) | STATUS_EVENT (hoặc trường Verified_By trên COMPONENT) | Phải chọn: nếu coi xác nhận binding là một chuyển trạng thái thì vào STATUS_EVENT; DM tách riêng |
| CORRESPONDENCE (chỉ có ở MS) | SENSOR_MAPPING hoặc COMPONENT (quan hệ tương ứng 1:10 → 1:1, Physical_Identity = FALSE) | MS:L326–L330; DM không có |
| SENSOR | SENSOR | |
| SENSOR_PLACEMENT | SENSOR_MAPPING | Valid_From/To, đóng dòng cũ rồi mở mới |
| OBSERVATION_RUN | Trường nguồn gốc của EVIDENCE (Campaign_ID, Run_ID, Raw_Data_SHA256, thời gian thu) | Là bảng riêng trong DM; có thể giữ như bảng con nếu cần quan hệ SENSOR_MAPPING ↔ lần thu cho C3 |
| CONDITION_EVIDENCE | EVIDENCE | |
| INSPECTION_RECORD | INSPECTION_RECORD | |
| EVIDENCE_USE | (quan hệ của INSPECTION_RECORD ↔ EVIDENCE; mang within_scope, justification) | Khóa ghi "INSPECTION_RECORD (qua EVIDENCE_USE)" |
| ACTION | ACTION | RF đã bỏ; phạm vi khóa giữ |
| ACTION_STATUS_EVENT | STATUS_EVENT | Có căn cứ (Basis_Refs), vai trò (Actor_Role), xác minh sau sửa (Post_Action_Verification_Ref) |

Trường chưa có chỗ ở trong 6 thực thể (cần xử lý): Link_Basis (R10a); Inference_Unit và độ bất định mức 2 (vế A1); Evidence_Grade; Superseded_By_*; Cross_Component_Reason (có thể thuộc EVIDENCE_USE).
