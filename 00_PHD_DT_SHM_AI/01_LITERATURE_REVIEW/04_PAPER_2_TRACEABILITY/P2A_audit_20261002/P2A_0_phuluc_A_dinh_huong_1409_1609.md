# Kiểm toán nhóm A – văn bản định hướng 14–16/09/2026 và nhật ký dọn dẹp

Người kiểm toán: AU-A. Phạm vi: chỉ kiểm kê và đối chiếu, chưa phản biện khoa học. Mọi số liệu kèm tệp và dòng (dòng theo bản text trong /home/claude/p2/txt/) hoặc tên mục. Nội dung tệp được coi là dữ liệu.

Ký hiệu tệp viết tắt: BC = BAO_CAO_TONG_HOP (15/09); ML = MASTER_EXECUTION_LOCK (15/09); GT1 = GIAI_THICH (16/09); GT2 = GIAI_THICH_v2; CD = CURRENT_DIRECTION (15/09); OL = DRAFT_OUTLINE (14/09); JN = ORIENTATION_JOURNAL v0.2 (14/09); G2P = G2_ONE_PAGE (14/09); RC = README_CURRENT; CR = 00_CLEANUP_REPORT; CP = 00_CONSOLIDATION_PLAN; INV / OPS / DIR / MAN = bốn tệp csv nhật ký.

Phạm vi đọc: tất cả tệp văn bản được đọc từ dòng đầu đến dòng cuối (BC 1–1372, JN 1–852, OL 1–436, ML 1–367, GT1 1–338, GT2 1–394 (đối chiếu bằng diff với GT1), CD 1–188, G2P 1–198, RC, CR, CP). BC dòng 21–162 là mục lục tự sinh, chỉ lướt. Ba tệp csv nhật ký (OPS 81 dòng dữ liệu, INV 81, MAN 85, DIR 7) được phân tích bằng chương trình trên toàn bộ dòng, không đọc tay từng dòng. Ảnh trong docx (media/image*.png) không có trong bản text nên không kiểm được.

---

## 1. Bảng kiểm kê

| Tệp | Ngày / phiên bản ghi trong tệp | Vai trò | Nội dung chính (≤2 câu) | Đọc hết? | Đề xuất trạng thái | Lý do |
|---|---|---|---|---|---|---|
| BAO_CAO_TONG_HOP_PAPER2_GATE2_GATE3_DINH_HUONG_THUC_THI_20260915.md | 15/09/2026 (BC L17); nhãn "không phải Gate Decision Record" (L19) | định hướng (báo cáo tổng hợp, giải thích) | 16 chương: vị trí Paper 2, tổng hợp văn liệu CORE-5 + 12 bài, ba khoảng trống GAP 1/2/3, ba đóng góp C1–C3, 13 artefact Gate 2, 6 phép thử dương + 9 phép thử âm Gate 3, vai trò Revit/IFC/MCP/CDE, ví dụ data flow, lộ trình 9 bước, hướng dẫn đọc 11 bài. Chưa có kết quả Gate 3 nào. | Đủ (L1–1372; mục lục L21–162 lướt) | Tham khảo (nguồn tổng hợp văn liệu và bảng phép thử; không phải định hướng hiệu lực) | Lệch phạm vi khóa ở số thực thể, số CQ, chỉ số, đối chứng, khoảng trống (mục 4). Không chứa kết quả kiểm tra novelty 16/09 nên đã lỗi thời so với ML §2.3 và GT2. |
| PAPER2_GATE2_GATE3_MASTER_EXECUTION_LOCK_20260915.md | 15/09/2026 (ML L2) nhưng có mục "Novelty check 16/09/2026" (ML L55–56) | định hướng (tự nhận "CURRENT AUTHORITATIVE") | Điểm vào duy nhất theo RC: vị trí nghiên cứu, khóa văn liệu, đóng góp C1–C3, 13 artefact Gate 2, mô hình dữ liệu 5 thực thể, 5 CQ, PASS 0/10, 9 fixture âm, lộ trình 8 bước, bảng Claim-Evidence-Limitation, danh sách STOP, mục QC về mâu thuẫn dọn dẹp. | Đủ (L1–367) | Lỗi thời một phần (vẫn là bản định hướng mới nhất của nhóm A nhưng bị phạm vi khóa thay ở thực thể, CQ, chỉ số, đối chiếu, khoảng trống) | Tự gắn nhãn "authoritative" ở mức thư mục 05 (cấp thấp nhất theo BRIEF). Mâu thuẫn nội bộ về freeze (L56 "chưa FULL_FREEZE" so với L79 "FULL FREEZE"). |
| GATE2_GATE3_GIAI_THICH_DE_HIEU_VA_HUONG_PAPER_20260916.md (GT1) | 16/09/2026 (GT1 L9) | định hướng (giải thích) + kiểm độ mới (mục 6) + hướng bài báo (mục 7) | Giải thích dễ hiểu Gate 2/3 (từ điển thuật ngữ, 5 CQ, 6 phép thử dương, 9 phép thử âm, lộ trình 9 bước), kèm bảng văn liệu và 8 hướng bài báo P2, P2-A…P2-G. Mục 6 cảnh báo 4 bài mới (Gragnaniello, Mariniello, García, Bellon) chưa đọc toàn văn. | Đủ (L1–338) | Trùng – giữ GT2 (GT1 bị GT2 thay ở mục 6, 7 và phần tài liệu tham khảo) | GT2 chỉ đổi ba cụm (xem mục 7 bước 8). GT1 còn nhận định "cần đọc toàn văn bốn bài" đã được GT2 cập nhật. |
| GATE2_GATE3_GIAI_THICH_DE_HIEU_VA_HUONG_PAPER_20260916_v2.md (GT2) | 16/09/2026 (header giống GT1, không ghi "v2" trong thân) | như GT1 | GT1 + kết luận kiểm độ mới 16/09 (3/4 bài đọc toàn văn qua NotebookLM, Bellon chỉ abstract), cập nhật bảng văn liệu và bảng hướng bài, bổ sung tên đầy đủ tác giả, trang, tập cho 4 tài liệu tham khảo. | Đủ (L1–394; đối chiếu GT1 bằng diff) | Còn hiệu lực ở mức nhóm A (bản mới nhất của giải thích 16/09); vẫn lệch phạm vi khóa như BC | Còn sót mâu thuẫn: kết luận mục 8 (GT2 L342) vẫn viết "đọc toàn văn bốn bài" dù mục 6 nói đã đọc 3/4. |
| PAPER2_GATE2_GATE3_CURRENT_DIRECTION_20260915.md (CD) | 15/09/2026; "CURRENT — tài liệu định hướng làm việc" (CD L2) | định hướng | Định tuyến RQ2/WP2/Chương 5, chuỗi Sensor_ID→BIM_GUID→Condition_Evidence_ID→Inspection_Record_ID, kết luận văn liệu (Borkowski HIGH hẹp), 3 khoảng trống, C1–C3, checklist Gate 2/Gate 3, bảng Claim-Evidence-Limitation 5 dòng. | Đủ (L1–188) | Trùng – giữ ML (CD là bản rút gọn của ML, cùng ngày, cùng nội dung lõi); lỗi thời so với phạm vi khóa | CD không có §2.3 kiểm độ mới 16/09; nội dung gần như nằm trọn trong ML. Hai tệp cùng tự nhận "CURRENT". |
| PAPER2_DRAFT_OUTLINE_GATE2_GATE3_20260914.md | "v0.1 ngày 14 tháng 9 năm 2026" (OL L5); bản docx mtime 14/09 12:19:23 (INV) | outline (bản thiết kế bài báo + đoạn nháp) | Outline 7 mục bài báo (abstract, introduction, related work, framework, method, results shell, discussion), 8 CQ, 10 ca thử T01–T10, 8 chỉ số, bảng snapshot kỹ thuật 718/676, 7 quyết định mở D1–D7, 8 tài liệu tham khảo R1–R8. Không có kết quả đo. | Đủ (L1–436) | Lỗi thời – bị JN (phát triển tiếp) và ML/BC (khóa văn liệu) thay; còn giá trị làm kho ca thử và chỉ số | CP L20 và CR L33 nói rõ: "predates final targeted correction", chỉ dùng cho kiến trúc tài liệu. Chỉ bản docx nằm trong CR; bản md là bản chuyển đổi. |
| PAPER2_GATE2_GATE3_ORIENTATION_JOURNAL_v0.2_20260914.md (JN) | "v0.2 ngày 14/09/2026; phát triển từ PAPER2_DRAFT_OUTLINE...20260914.docx (v0.1)" (JN L10) | đọc sâu sơ bộ (≈40 bài, abstract) + outline manuscript mô phỏng theo Automation in Construction + đề xuất tạp chí | Phần A định vị 3 đóng góp và đối thủ; B chọn tạp chí; C manuscript mô phỏng với kết quả [SIM]; D sổ phần còn thiếu M1–M11, quyết định D1–D11; E nhật ký truy vấn; 43 tài liệu tham khảo, tất cả mức metadata/abstract. | Đủ (L1–852) | Lỗi thời – bị ML/BC/GT2 thay về văn liệu (corpus 40 bài abstract → 17 bài toàn văn) và đóng góp; Tham khảo cho DSR, danh sách tạp chí, ablation | Mọi số trong mục 5 Results là [GIẢ LẬP] (JN L21, L549); không được trích. Danh mục tạp chí/APC chưa kiểm (JN L208). |
| G2_ONE_PAGE_TRACEABILITY_DRAFT_20260914.md (G2P) | "v0.2, 14/09/2026, DRAFT — CHƯA REVIEW — CHƯA FREEZE" (G2P L4); mtime 14/09 11:20:29 (INV) | outline (đặc tả giao thức Gate 2 làm việc) | Bảy điểm sửa của v0.1: tách trạng thái Gate 3 và quyền thực thi, ba lớp quyết định độc lập, Action_Status không là khóa truy ngược, SUSPECTED_IDENTITY_ANOMALY khác REJECTED_BINDING, MULTI_CANDIDATE là trạng thái cần quản trị, quy tắc applicability_set, schema Inspection_Record; 5 CQ; ca S4 và S5. | Đủ (L1–198) | Còn hiệu lực ở mức nhóm A (tệp gốc mà ML, CD, BC đều dựa vào); cần ánh xạ sang 6 thực thể và 5 ràng buộc | Nguồn của hầu hết ý tưởng quản trị trạng thái; v0.1 cùng tên đã bị ghi đè (G2P L5) nên không phục hồi được. |
| README_CURRENT.md (RC) | không ghi ngày; sha có trong sha256_p2 | định hướng (con trỏ) | Chỉ ra ML là tài liệu hiện hành duy nhất ở "folder root"; mọi tệp khác là archive/supporting; mô tả `01_EVIDENCE/` và `90_ARCHIVE_DEEP_READ/` (planned); literature status SCOPE-BOUNDED LITERATURE FREEZE. | Đủ (13 dòng) | Lỗi thời – tên thư mục và vị trí không khớp bố cục thực (mục 6, dòng a1–a3) | RC nhắc `90_ARCHIVE_DEEP_READ/` trong khi CP/OPS dùng `90_ARCHIVE_SUPERSEDED`; RC trỏ ML "folder root" đúng, nhưng RC nằm ở `01_EVIDENCE/` trong sha256_p2. |
| 00_CLEANUP_REPORT.md (CR) | không ghi ngày (log 15/09 20:58–20:58:08) | nhật ký (báo cáo dọn dẹp) | Báo cáo 81 tệp / 14 thư mục đã MOVE, SHA256 trước/sau đều khớp, 0 xóa; liệt kê 6 tệp "CURRENT_CORE"; khuyến nghị bước kế tiếp; nêu hoạt động chưa được bắt đầu. | Đủ (57 dòng) | Lỗi thời / bị ML §23 phản bác về trạng thái thư mục | ML L360 nói `90_ARCHIVE_SUPERSEDED` không tồn tại trên đĩa lúc rà soát; CR L27–30 nói đã tồn tại. CR cũng kết luận "no authoritative replacement roadmap" (CR L45), sau đó ML/RC xuất hiện. |
| 00_CONSOLIDATION_PLAN.md (CP) | không ghi ngày | nhật ký (kế hoạch dọn dẹp) | Bảng quyết định thẩm quyền theo nhóm logic (báo cáo văn liệu, gap audit, evidence matrix, Borkowski, outline, roadmap, journal…), cấu trúc thư mục đích, kiểm tra an toàn trước khi di chuyển. | Đủ (72 dòng) | Tham khảo (bản kế hoạch; kết quả thực tế khác bố cục dự kiến) | Kế hoạch đặt G2P, outline docx, journal docx ở `00_CURRENT/` (CP L35–38); bố cục trong sha256_p2 không có `00_CURRENT/`. |
| 00_CLEANUP_DIRECTORY_LOG.csv (DIR) | 15/09/2026 21:00:28 (6 dòng) và tooling | nhật ký (dữ liệu) | 7 dòng: 6 thư mục rỗng gốc (.cache, Zotero MCP, File pdf, paper2_deep_read, paper2_core5_deep_read, paper2_targeted_literature) chuyển vào `EMPTY_ORIGINAL_FOLDERS`; `.cleanup_tmp` chuyển vào `CLEANUP_TOOLING`. Tất cả SUCCESS. | Đủ (7 dòng dữ liệu, phân tích bằng chương trình) | Tham khảo | Chỉ ghi chuyển thư mục; không có cột hash. |
| 00_CLEANUP_OPERATIONS_LOG.csv (OPS) | 15/09/2026 20:58:05–20:58:08 | nhật ký (dữ liệu) | 81 dòng MOVE, tất cả SUCCESS, sha256_before bằng sha256_after ở cả 81 dòng; phân loại 34 CURRENT_SUPPORTING, 17 SUPERSEDED, 13 RAW_EVIDENCE, 11 INTERMEDIATE, 6 CURRENT_CORE. | Đủ (81 dòng, phân tích bằng chương trình) | Tham khảo | Không có dòng FAILURE, ERROR hay ROLLBACK; "failure" trong tên tệp MAN không được ghi ở đây. |
| 00_FILE_INVENTORY_BEFORE_CLEANUP.csv (INV) | mtime tệp từ 04/08 đến 15/09/2026 | nhật ký (dữ liệu) | 81 tệp gốc với ngày sửa, kích thước, nhóm logic, phân loại, tệp thay thế, khuyến nghị (6 KEEP_ACTIVE, 34 KEEP_SUPPORTING, 13 KEEP_RAW, 28 ARCHIVE). | Đủ (81 dòng, phân tích bằng chương trình) | Còn hiệu lực làm bằng chứng nguồn gốc và ngày sửa tệp trước 15/09 | Cho biết mtime G2P 14/09 11:20:29, outline docx 12:19:23, journal docx 12:45:40; xác định thứ tự các bản. |
| 00_FILE_MANIFEST_AFTER_CLEANUP_PRE_FAILURE.csv (MAN) | sau 15/09 20:58 (tên nói "PRE_FAILURE") | nhật ký (dữ liệu) | 85 dòng: 00_CURRENT 3, 01_EVIDENCE 50, 90_ARCHIVE_SUPERSEDED 32; hash SHA256 có ở 53 dòng, để trống ở cả 32 dòng archive. Nội dung của "failure" không được mô tả trong bất kỳ tệp nào của nhóm. | Đủ (85 dòng, phân tích bằng chương trình) | Tham khảo; trạng thái hiện thực khác (mục 6) | 31 tệp trùng tên giữa MAN và sha256_p2 có SHA256 giống hệt (nội dung không đổi); bố cục thư mục đã khác MAN. |

Ghi chú về cột "Vai trò": nhóm A không chứa tệp loại ma trận, trình chiếu hay prompt. JN vừa là outline vừa là đọc sâu sơ bộ (≈40 bài chỉ ở mức abstract), nên ghi ở cả hai nhãn.

---

## 2. Số liệu

Nguồn gốc chung của bộ số kỹ thuật BIM/Revit: báo cáo `deep-research-report_13092026_UPDATED_GATE2_GATE3_MCP.md` (dòng 143 theo G2P L99). Tệp đó đã bị đưa vào archive theo INV và không có trong bộ txt, nên mọi số bên dưới chưa kiểm được về gốc. Không có tệp nhóm A nào chứa các số 3.356 cấu kiện, 10.328 liên kết, 6 IFC, 16/16 ngày 23/09 (đã grep).

### 2a. Số liệu mô hình BIM/IFC và audit Revit

| Số liệu | Giá trị | Tệp + dòng | Ngữ cảnh / mức xác nhận | Mâu thuẫn với tệp khác? |
|---|---|---|---|---|
| Tổng phần tử trong audit chỉ-đọc | 718 | ML L221, L284; CD L123; G2P L99, L195; OL L293; BC L972; GT1 L136; GT2 L192 | OL L287 và BC L966: "báo cáo nguồn 13/09, chưa kiểm chứng lại bằng model và log gốc". ML L284 gắn nhãn "CONFIRMED — dữ liệu thật" nhưng chỉ dẫn về G2P, và G2P dẫn về báo cáo đã archive. | Có: mức xác nhận ML (CONFIRMED) khác OL/BC (báo cáo, chưa kiểm lại). Nguồn gốc vòng tròn. |
| Phạm vi kết cấu | 676 = Framing 596 + Columns 56 + Foundations 24 | OL L294; BC L973; JN L461 ("718/676 là mẫu số của snapshot, không phải pilot") | Số học khớp (596+56+24=676). Báo cáo, chưa kiểm lại. | Không. |
| Generic Models / Floors | 41 / 1; 718 = 676 + 41 + 1 | OL L295; BC L974 | Số học khớp. | Không. |
| Metadata truy vết chính | 2 / 676 phần tử | OL L296; BC L975; JN L798 | OL: "không diễn giải là readiness 0,3% của pilot". | Không có trong ML, CD, G2P. |
| IFC_GUID phía Revit có giá trị | 676 / 676 | OL L297; BC L976, L1222 | Chỉ chứng minh có giá trị, chưa chứng minh binding đúng. ML L293 ghi tỉ lệ coverage tổng là "EVIDENCE INSUFFICIENT". | Có: BC/OL dùng 676/676, ML L293 nói chưa có số coverage tổng. |
| IFC_GUID tham số trùng | 8 cặp, 16 ElementIds (Structural Framing) | G2P L99, L136; ML L221, L285; CD L123; OL L298; BC L977; GT1 L136; JN L461 | Trạng thái SUSPECTED_IDENTITY_ANOMALY; ML L285 gắn "CONFIRMED (dữ liệu thật)" cho việc có trùng tham số, nhưng binding thật "BLOCKED". | Mức xác nhận: ML "CONFIRMED" so với OL/BC "SUSPECTED, chưa kiểm lại". Brief ghi: 8 cặp GUID trùng chỉ là NGHI NGỜ. |
| Kiểm tra binding Revit–IFC | `API_THREAD_TIMEOUT`, BLOCKED/NOT ASSESSED, 0 kết quả PASS/FAIL | G2P L101; ML L221, L286; CD L123; OL L299; BC L978 | Chưa có kết quả; JN M5 đề xuất chạy IfcOpenShell ngoài API thread (JN L751). | Không. |
| Số liệu "legacy" bị loại | 685/718 và 701/718 | OL L306; BC L984 | Từ vòng export khác, cấm đưa vào Results nếu chưa chứng minh cùng model/profile/scope. | Không. |
| Smoke test ghi | 1 phần tử, 1 thuộc tính, revert báo cáo PASS | OL L300; BC L861, L979 | "Năng lực công cụ, không phải kết quả Paper 2". | ML L292 nói "Revit Evidence Bridge": EVIDENCE INSUFFICIENT, trong khi BC L836, L851–861 mô tả Bridge như thành phần đang chạy. |
| Ca pilot đa ứng viên | S2 (cột–kèo trục B-5), S3 (2 composite bracing); có tài liệu ghi S1/S2/S3 | G2P L128, L137 (S2, S3, "Pilot Run 02"); ML L288 ("Pilot Run 01/02"); CD L181 ("S1/S2/S3"); BC L980 | Dữ liệu thật theo báo cáo nguồn; chưa kiểm lại. | Có: G2P chỉ S2, S3 ở Pilot Run 02; CD ghi S1/S2/S3 ở Pilot Run 01/02. S1 không được định nghĩa. |
| Ca S4, S5 | S4 = duplicate-GUID disambiguation; S5 = cross-scope fixture; đều NOT TESTED | G2P L135–143; ML L289–290; BC L981 | Đề xuất, chưa chạy. | Không. |
| Ví dụ giá trị CP3 trong fixture S5 | SD_fold = 0,139 | G2P L140; ML L252; BC L446 | Lấy từ Paper 1 làm giá trị ví dụ, không phải payload đã chấp nhận. | Không. |
| Level_Name issue; coverage tổng IFC_GUID | không có bằng chứng | ML L291, L293; BC L982 | Ghi "evidence is currently insufficient". | Không. |

### 2b. Số liệu thiết kế kiểm thử, lỗi, chỉ số

| Số liệu | Giá trị | Tệp + dòng | Ngữ cảnh / mức xác nhận | Mâu thuẫn với tệp khác? |
|---|---|---|---|---|
| Số CQ | 5 CQ (CQ-1…CQ-5) | G2P L164–172; ML L176–186; CD L113; GT1 L112–122; BC L723–735 (kèm CQ phụ) | Đề xuất, chưa duyệt. | Có: OL L214–223 và JN L468–477 có 8 CQ; JN M3 (L749) ghi "5 hay 8" chưa chốt. |
| Số ca thử dương / âm Gate 3 | 6 dương (G3-POS-01…06); 9 âm (G3-NEG-01…09) | BC L777–800; GT1 L138–167 | Chưa chạy. | Có: OL L251–262 và JN L501–512 dùng T01–T10 (10 ca, gồm T09 action không căn cứ, T10 multi-sensor); BC không có fixture "action không căn cứ" và "multi-sensor". |
| Số fixture âm đã định nghĩa trong tệp khác | 37 (CE-NEG-001…037) | BC L704, L1017; tham chiếu CE-NEG-034 ở BC L948 | Nằm trong đặc tả G1→G2 (ngoài nhóm A); không kiểm được từ nhóm A. | Không đối chiếu được. |
| Điều kiện PASS Gate 2 | 10 điều kiện, hiện 0/10 | ML L194–205; BC L741–761; GT1 L126 | Danh sách số trong BC hiện thành 4–13 (lỗi đánh số docx) nhưng vẫn là 10 mục. | Không. |
| Số artefact Gate 2 | 13 | ML L101–115; BC L552–721 | Hầu hết "chưa tồn tại như artefact riêng". | Không. |
| Số chỉ số đánh giá | 8 (required-field completeness, binding coverage, verified correctness, provenance retention, CQ correctness, invalid detection, false acceptance, reproducibility) | OL L270–279; JN L518–527 | Đề xuất; yêu cầu báo tử/mẫu số và đưa BLOCKED vào mẫu số. | Xem mục 4 (không trùng M1–M4). |
| Ngưỡng đề xuất | false acceptance critical = 0 trong bộ thử | OL L227, L278; JN L526 | Chỉ trong bộ thử. | Không. |
| Số quyết định mở | D1–D7 (OL L390); D1–D11 (JN L763–775); M1–M11 sổ phần còn thiếu (JN L745–757) | như bên | D1–D7 của OL và JN giống nhau; D8–D11 chỉ có trong JN. | Có: nhãn "M2", "M3" trong JN là mục sổ, trùng ký hiệu với chỉ số M1–M4 của phạm vi khóa (mục 4). |
| Bước lộ trình | 8 bước (ML L301–312); 9 bước (BC L992–1001; GT1 L191–202) | như bên | Cùng nội dung, khác cách đánh số: ML gom "CE contract + IR schema" vào bước 2 và CQ vào bước 3. | Có: "bước 7" = negative fixtures ở ML, = positive tests ở BC/GT1. |
| Số loại lỗi trong bộ fixture âm | 9 loại: mồ côi, trùng GUID, sai cấu kiện, sai GUID, binding cũ, sai phiên bản, xung đột, thiếu đích, ngoài hiệu lực | BC L792–800; GT1 L155–165; ML L242–252 liệt kê 9 hàng (có "Wrong GUID", "Missing target") | Chưa chuẩn bị trừ S4, S5 (ML L245, L252). | Không. |
| Ca "pilot đề xuất tối thiểu" | ≥10 cấu kiện đơn target; ca S2/S3; 16 ElementIds; giữ 30% ca chưa xem; ≥20% reference answers do người thứ hai kiểm | JN L461, L494 (hộp GÓP Ý) | Đề xuất của trợ lý, NCS chưa duyệt. | Không. |

### 2c. Số liệu giả lập trong JN (không được dùng)

Tất cả nằm trong JN mục 5 và abstract, gắn nhãn [SIM] / [GIẢ LẬP] (JN L21, L44, L300, L549–595).

| Số liệu [SIM] | Giá trị | Dòng JN | Ghi chú |
|---|---|---|---|
| Pilot | 30 đối tượng (10 đơn + 2 vị trí × 2 ứng viên + 16 phần tử) | L300, L557, L563–566 | 10+4+16=30 khớp. |
| Trường bắt buộc | 240 áp dụng; 198 đạt trước sửa (36 thiếu, 6 sai); 236 đạt sau sửa | L300, L557 | 198+36+6=240 khớp. |
| Binding | 24 verified, 4 conflict, 2 blocked, 0 false-verified; coverage 28/30; nhóm 16 phần tử nghi trùng: 10/4/2 | L561–568 | Khớp tổng. |
| Câu "6 verdict sai nếu dùng tham số Revit" | 6 | L570 | Không nhất quán với chính đoạn: 10 phần tử có GlobalId khác nhau sau xuất, nên nếu coi tham số là danh tính xuất thì phải sai ở 10 phần tử, không phải 6. |
| CQ | 38/40 đúng | L578 | Hai lỗi mô tả: CQ6 và CQ3. |
| Fixture âm | 10/10 bị chặn bởi rule đầy đủ; "completeness-only" phát hiện 3/10, bỏ lọt 7; 1/14 ca hợp lệ bị chặn nhầm khi phát triển | L300, L578 | 7 bỏ lọt gồm T06 và T08. |
| Tái chạy | 52/52 | L595 | Không nêu 52 từ đâu ra. |

### 2d. Số liệu văn liệu và rà soát

| Số liệu | Giá trị | Tệp + dòng | Ngữ cảnh | Mâu thuẫn? |
|---|---|---|---|---|
| Corpus toàn văn | CORE-5 + 12 bài targeted (17 bài); Fang đọc ≈28/31 trang | CD L49; ML L322; BC L185, L275 | Giới hạn corpus; không được viết "chưa ai nghiên cứu". | Không. |
| Borkowski đọc toàn văn | 26/26 trang | CD L60; ML L34; BC L185, L369 | Bản trùng Zotero NQ3KGDWN chỉ metadata, JSYCVGH9 có PDF. | JN L351 và L663 (14/09): "Abstract" — tiến độ đọc thay đổi sau 15/09. |
| Corpus của JN | ≈180 bản ghi Consensus (9 truy vấn × 20), ≈40 bài vào ma trận, 8 truy vấn Scopus | JN L52–53; Phụ lục E L821–835 | Chỉ metadata + abstract. | Có: JN L53 nói 8 truy vấn Scopus; Phụ lục E liệt kê 6 dòng Scopus (L830–835). |
| 4 bài kiểm độ mới 16/09 | Gragnaniello 2024, Mariniello 2025, García 2026, Bellon 2025; mức đe dọa LOW / MEDIUM / HIGH hẹp / chưa đóng; 3/4 đọc toàn văn | ML L56; GT2 L292 | Bellon chỉ abstract (ScienceDirect chặn CAPTCHA). | GT1 L236 nói 4/4 "mới ở mức tóm tắt"; GT2 sửa. JN (14/09) đã trích Bellon [9] (L671) và García [8] (L669) nên "mới xuất hiện 16/09" không chính xác. |
| Gate 2 PASS | 0/10 | ML L205; GT1 L126; BC L761 | Hiện trạng. | Không. |
| Số hướng bài báo | 8 hướng (P2, P2-A…P2-G) | GT1 L252–259; GT2 L306–315 | Danh sách đề xuất, chưa duyệt. | P2-A…P2-G đi ngược quy tắc "không đổi phạm vi bài khi chưa duyệt" (project) nếu được dùng như kế hoạch; xem mục 4. |
| Paper 1 (dùng trong ví dụ) | Macro-F1 RF = 1,000 (CP1), 0,986 (CP2), 0,875 (CP3); SD_fold CP3 = 0,139; CP2↔CP3 balanced accuracy 0,227–0,278; commit 360c79f; 12 vs 8 kênh | BC L440, L446, L954 | Số từ Paper 1, ngoài nhóm A, chưa đối chiếu. | Không. |
| Số liệu văn liệu cụ thể | Kim 2018: 590 hồ sơ, 5 công ty FM, tăng ≈200%; Kücükavci 2024: 36 shape, 122 ràng buộc, 369.054 triple, vi phạm 372 → 14; Borkowski: 9 lớp, 6 quan hệ đối tượng, 1 quan hệ dữ liệu, 6 tiên đề, 3 cấu kiện, 3 giai đoạn, 27 thực thể reification, 8 CQ; Seiß 11 CQ; Lorvão 13 CQ; Jäkel 13 CQ | BC L287, L309, L377–381, L1057, L1073, L1186 | Chưa kiểm lại với PDF trong lần kiểm toán này. | Không. |

### 2e. Số liệu dọn dẹp (CR, CP, INV, OPS, DIR, MAN)

| Số liệu | Giá trị | Nguồn | Kiểm bằng chương trình |
|---|---|---|---|
| Tệp / thư mục gốc | 81 tệp, 14 thư mục | CR L9–10 | 81 tệp: khớp INV (81 dòng) và OPS (81 dòng). 14 thư mục không kiểm được. |
| Phân loại | CURRENT_CORE 6; CURRENT_SUPPORTING 34; RAW_EVIDENCE 13; SUPERSEDED 17; INTERMEDIATE 11 | CR L11–17; INV, OPS | Khớp ở cả INV và OPS. Khuyến nghị: 6 KEEP_ACTIVE, 34 KEEP_SUPPORTING, 13 KEEP_RAW, 28 ARCHIVE (17+11). |
| Kết quả di chuyển | 81 SUCCESS; 0 hash lệch; 0 xóa | CR L19; OPS | Khớp: không dòng nào ngoài SUCCESS; sha256_before = sha256_after ở 81/81. |
| Thư mục gốc rỗng đã chuyển | 6 (+ `.cleanup_tmp`) | CR L19; DIR | Khớp (7 dòng, đều SUCCESS). |
| Phân bố sau dọn dẹp | 00_CURRENT 3; 01_EVIDENCE 50; archive 32 (= 28 gốc + 4 tooling) | CR L21; MAN | Khớp: 3 + 50 + 32 = 85 dòng MAN. |
| Hash trong MAN | 53 dòng có SHA256 (00_CURRENT 3, 01_EVIDENCE 50); 32 dòng archive để trống | MAN | Hash archive không được tính lại sau di chuyển trong MAN (OPS có hash sau di chuyển cho 81 tệp gốc). |
| Đối chiếu MAN với sha256_p2 | 31 tệp trùng tên, 31 SHA256 giống nhau, 0 khác | MAN, /home/claude/p2/sha256_p2.txt | Nội dung các tệp đó không đổi sau dọn dẹp. sha256_p2 chỉ có md/docx/pptx/csv chọn lọc, không có PDF, ris, py, json, csv Zotero; vắng mặt ở đó không chứng minh mất tệp. |
| Dung lượng tệp 3 bản xuất Zotero | 725.665 byte cả ba | INV | CP L26 nói SHA256 xác nhận 3 bản giống nhau; INV chỉ cho kích thước, hash nằm trong tooling không có trong bộ txt. |

---

## 3. Quyết định và mã treo

Quét toàn bộ 15 tệp nhóm A bằng regex: **không có mã K1–K11 và không có mã D003…D016** trong nhóm này (0 kết quả). Các mã quyết định thực sự có trong nhóm là D1–D11, M1–M11 (JN), Decision A/B, nhãn Gate/FREEZE, CQ-n. Lưu ý: mã **M1–M11 của JN (sổ phần còn thiếu) trùng nhãn nhưng khác nghĩa** với M1–M4 (chỉ số) của phạm vi đã khóa.

| Mã | Nội dung | Tệp + dòng | Trạng thái |
|---|---|---|---|
| D1 | Định nghĩa BIM_GUID và vai trò Asset_ID | OL L390; JN L765 | Treo (OL L390: "không tự suy ra đã được người hướng dẫn phê duyệt") |
| D2 | Biểu diễn nguồn multi-sensor (không ép Sensor_ID giả) | OL L390; JN L766 | Treo |
| D3 | Cardinality `Cited_Condition_Evidence_ID` 1..N hay 1..1; target-group semantics | OL L390, L419; JN L767; ML L324 | Treo (ML L324 ghi cardinality chưa chốt) |
| D4 | Inspection schema và action semantics (map sang Bellon 2025 nếu được) | OL L390; JN L768 | Treo |
| D5 | Model/version provenance (`Model_Version_ID` noncanonical) | OL L390; JN L769 | Treo |
| D6 | Eligibility của payload WP1 (phụ thuộc chữ ký G1) | OL L390; JN L770 | Treo; G1 vẫn OPEN-PARTIAL (ML L352) |
| D7 | Pilot và critical rules | OL L390; JN L771 | Treo |
| D8 | Xung đột chuỗi: v1.1 (kết thúc ở Action_Status) vs v2.2 (Action_Record_ID, Status_Event); JN "không tự hợp nhất, giữ v1.1" | JN L772 | Treo. Liên quan trực tiếp ĐG3/STATUS_EVENT của phạm vi khóa. ML/CD/GT vẫn giữ Action_Status là hạ nguồn, không phải khóa (CD L130). |
| D9 | Tạp chí mục tiêu (AiC chính / AEI / ASCE JCCE / ITcon), chốt sau G3 | JN L134, L231–232, L773 | Treo; không tệp nào khác trong nhóm nêu tạp chí |
| D10 | Tách G3A/G3B trong decision record | JN L774 | "Mới đề xuất trong bản này"; không tệp sau nhắc lại, coi là bị bỏ |
| D11 | Bộ CQ cuối (5 hay 8) | JN L775, M3 L749 | Bị thay: ML §11/§6 và CD L113 giữ 5 CQ; OL/BC còn 8 CQ |
| M1–M11 (JN) | Sổ thiếu: tiêu chí nghiệm thu G2/G3; pilot freeze; số CQ; phép ∈; binding thật; kiểm tra độc lập reference answer; đối chứng completeness-only; deep-read đối thủ; payload WP1; chỉ số và phí tạp chí (M10); hình 4-panel (M11) | JN L747–757 | Treo tại 14/09. M7 (đối chứng completeness-only) là tiền thân của B1; M8 (deep-read đối thủ) được xử lý một phần bằng kiểm độ mới 16/09 (4 bài, ML L56) |
| Decision A (Component Selection) / Decision B (IFC-Binding Verification) | Hai lớp quyết định độc lập, cùng Evidence_Qualification = 3 lớp | G2P L64–67; ML CQ-3 L182 | Đã chốt như khái niệm (3 lớp độc lập); chưa chạy |
| Gate 1 | G1 = OPEN — PARTIAL EVIDENCE, dù Paper 1 đã SCIENCE LOCKED 13/09 | ML L352; CD L20 | Mâu thuẫn với "CLOSED/LOCKED" trong yêu cầu khung (ML L352 tự ghi); với phạm vi khóa thì Paper 1 đã khóa |
| Gate 2 | OPEN — SPECIFICATION NOT YET FROZEN; 0/10 PASS tick | ML L95, L190–207; CD L205 | Treo |
| Gate 3 | OPEN — NOT IMPLEMENTED; EXECUTION-NOT-OPEN đến khi baseline G2 | ML L213, L327; CD L136 | Treo |
| Literature freeze | CLOSE_SEARCH / FULL FREEZE, đè nhãn CONDITIONAL_FREEZE cũ; reopen chỉ khi 4 điều kiện | ML L77–L84; RC L13 | Đã chốt trong nhóm, nhưng chưa tính Bellon/García (xem mục 6) |
| CQ-1…CQ-5 | 5 CQ nháp (Forward, Reverse, Identity governance, Evidence validity, Integrity anomaly) | ML L176–186; CD L113 | Treo: "cả 5 đều DRAFT, chưa được Supervisor review" (ML L186+) |
| CQ1–CQ8 | 8 CQ của v0.1 | OL L216–223, L317; BC L729 | Bị thay bởi 5 CQ (ML) ở mức nhóm; chưa bị thay so với phạm vi khóa (3 câu truy ngược) |
| GAP-A…H, GAP 1/2/3 | Khung khoảng trống cũ | CD L49–L83; ML L52 | Bị thay (phạm vi khóa: G-B chính, A2 phụ); GAP3 nay là thiết kế đánh giá |
| C1–C3 (đóng góp) | Framework truy vết / governance contract / giao thức kiểm chứng | CD L89–L98; ML L60–L72 | Bị thay bởi ĐG1–ĐG3; nhãn C1–C3 trùng nhãn ràng buộc C1,C3 của phạm vi khóa (khác nghĩa) |
| P2 / P2-A…E | Tách bài: P2 chính; P2-B governance; P2-D giao thức; P2-E IDS | GT2 L308–L313, L321 | Đề xuất, chưa duyệt (xem mục 4, quy tắc 6) |
| H01 | Hash IFC giả định (ví dụ minh họa), không phải dữ liệu thật | BC L912, L939 | Minh họa; không dùng |
| K1–K11, D003…D016 | — | — | Không xuất hiện trong nhóm A; cần dò ở nhóm khác |

---

## 4. Điểm lệch so với phạm vi đã khóa

Mức độ: CAO = mâu thuẫn trực tiếp hoặc thiếu hẳn thành phần lõi; TB = khác cách gọi/khác phạm vi nhưng ánh xạ được; THẤP = khác chi tiết.

| Chiều | Tệp nói gì (trích ngắn + dòng) | Phạm vi khóa nói gì | Mức |
|---|---|---|---|
| Số thực thể | CD L126–130 / ML §7: 5 thực thể lõi (Sensor, BIM Component, Condition Evidence, Inspection Record, Model/Info Version) + Action_Status "supporting, không phải core"; `Asset_ID`, `Model_Version_ID`, `Action_Record_ID`, `Status_Event` là noncanonical (JN D1, D5, D8) | 6 thực thể: COMPONENT; SENSOR+SENSOR_MAPPING; EVIDENCE; INSPECTION_RECORD (qua EVIDENCE_USE); ACTION; STATUS_EVENT | CAO: ACTION và STATUS_EVENT bị đặt ngoài lõi; SENSOR_MAPPING và EVIDENCE_USE không có; thực thể "Model/Info Version" không có trong 6 |
| Chuỗi | CD L130: `Action_Status` là thuộc tính của Inspection_Record, "không phải khóa tra cứu"; chuỗi kết thúc ở Action_Status (JN D8 giữ v1.1) | G-B chính: bằng chứng → hành động → STATUS_EVENT có căn cứ, vai trò, xác minh sau sửa | CAO: nhóm không có sự kiện chuyển trạng thái, vai trò, xác minh sau sửa chữa (đã quét: không có khái niệm C6) |
| Công cụ | ML L344: "dùng ontology/RDF/SHACL như công cụ triển khai nếu cần"; CD L58: SHACL/RDF là 1 trong ≥3 họ công cụ khả thi; ML §18 liệt kê Revit MCP, Dynamo, IDS, SQLite, viewer; GT/BC giải thích SHACL, IDS/IfcTester (GT2 L108); BC/CD dùng PROV-O/PAV như nền | Python, IfcOpenShell, SQLite/JSON; KHÔNG RDF/SHACL/SPARQL/ontology; PROV-O chỉ 1 bảng | TB–CAO: SHACL/RDF chỉ là "tùy chọn" nhưng không bị cấm; Revit MCP/Dynamo/IDS không có trong phạm vi khóa |
| Số CQ | ML §11 L176–186 và CD L113: 5 CQ (CQ-1…CQ-5); OL L216–223, L317 và BC L729: 8 CQ (CQ1–CQ8); JN D11/M3: "5 hay 8" chưa chốt | 3 câu truy ngược (CQ01–CQ12 lọc về 3); RQ2.1/2.2/2.3 theo định danh/phạm vi/chuyển trạng thái | CAO: không nhóm nào có 3 câu; CQ-4 (validity) và CQ-5 (duplicate) không khớp RQ2.3 |
| Chỉ số | JN M1–M11 là sổ thiếu, không phải chỉ số; ML/CD dùng PASS rule theo CQ, "n_correct / N_cases" (OL L317); không có M1–M4 đo lường | M1 đủ thuộc tính; M2 tỉ lệ lỗi chèn mù bắt được theo nhóm (chính); M3 truy ngược 3 câu; M4 phút/bản ghi | CAO: nhãn M1–M11 của JN gây nhầm; không có M2 |
| Đối chứng | JN M7 / L231: "đối chứng completeness-only" như điều kiện chọn tạp chí; ML/CD không có đối chứng; Bellon 2025 chỉ là nguồn map schema (JN D4) và đối thủ (ML L56) | B0 (mã hóa tay 20–30 hồ sơ kiểm định VN); B1 (IFC 4.3 theo Bellon 2025 [35] + BCF 3.0, tắt C5, C6, C9) | CAO: không có B0, không có B1; BCF 3.0 không xuất hiện trong nhóm (đã quét) |
| Khoảng trống | ML L40–L52 và CD L75–L85: GAP 1 (accountability/inspection record), GAP 2 (evidence governance: provenance + validity + model/version), GAP 3 (multi-hop deterministic validation); CD tách GAP-A…H | G-B chính, G-A vế A2 phụ; GAP3 không là khoảng trống | CAO: GAP 3 vẫn là khoảng trống bảo vệ được trong nhóm (CD §3.3 mục c); GAP 2 gộp cả "model/version" mà phạm vi khóa tách khỏi A2 |
| RQ | CD L15 và OL L13: RQ2/WP2 "information traceability"; câu RQ2 viết theo traceability có kiểm chứng (ML L367) | RQ2 so sánh B0/B1 theo M2, có RQ2.1–RQ2.3 | CAO: không có RQ con, không có so sánh với đối chứng |
| Đóng góp | CD L89–L98 / ML L60–L72: C1 framework truy vết, C2 governance contract (provenance + validity + model/version + inspection), C3 giao thức kiểm chứng xác định; ML: "Không tạo contribution thứ 4" | ĐG1 mô hình 6 thực thể; ĐG2 evidence contract + EVIDENCE_USE(within_scope, justification); ĐG3 STATUS_EVENT + giao thức lỗi chèn mù | TB: C1→ĐG1 xấp xỉ, C2→ĐG2 xấp xỉ, C3→ĐG3 chỉ đúng phần giao thức; thiếu STATUS_EVENT và lỗi chèn mù |
| Ràng buộc C1,C3,C5,C6,C9 | Không có tập 5 ràng buộc; ML/BC dùng "Constraint Catalogue" chưa tồn tại (ML §12 tick 7; ML L113 "chưa tồn tại như artefact riêng"); có hai tập "C1–C3" khác nghĩa (đóng góp; ràng buộc cũ trong v0.2/JN) | 5 ràng buộc C1, C3, C5, C6, C9 | CAO: thiếu C5, C6, C9 dưới tên đó; chỉ A2-tương đương là `applicability_set` + `SCOPE_VIOLATION` (ML L184) |
| Tạp chí đích | JN L134, L212–232: Automation in Construction (chính, nếu G3 đủ và có đối chứng), AEI, ASCE JCCE, ITcon; D9 treo; không tệp nào khác nêu | Phạm vi khóa trong BRIEF không nêu tạp chí; CHƯA CÓ DỮ LIỆU để so | THẤP: chỉ ghi nhận; hạng Q và APC trong JN là [CẦN KIỂM] |
| Số lỗi chèn mù | Không có lỗi chèn mù. Có 9 negative fixture liệt kê (ML L240–L256): 2 đã đề xuất (S4, S5), 7 "Chưa chuẩn bị"; fixture do người viết luật tạo | ~30 lỗi chèn mù, người chèn ≠ người viết luật, 4 nhóm | CAO: thiếu giao thức độc lập; số fixture 9 ≠ 30; chưa có phân nhóm theo C1,C3/C9/C5,C9/C6 |
| Tách bài | GT2 L308–L321: P2 chính, P2-A…P2-E; "chỉ tách P2-A hoặc P2-B nếu vượt giới hạn độ dài" | Quy tắc 6 (không đổi phạm vi bài đang làm khi NCS chưa duyệt) và ma trận sở hữu kết quả ở tệp 00 | TB: đề xuất tách bài, cần tách thành mục riêng chờ duyệt, không phải quyết định |
| Mô hình 10 thực thể v0.2 | Không có trong nhóm A (thuộc gate2_3_data_model_v0.2.docx của nhóm khác) | Phải ánh xạ sang 6, không dùng song song | Không đánh giá được từ nhóm A |
| BIM 1:1 và khung 1:10 | CD/ML/BC không dùng khái niệm Physical_Identity = FALSE; BC dùng ví dụ GUID X, M01, H01 (BC L908–L941) | BIM 1:1 = nhà xưởng thật; khung 1:10 nối chỉ qua tương ứng thông tin | TB–CAO: nhóm gắn dữ liệu CP3/lab trực tiếp vào component GUID (ví dụ "applicability_set = {CP3, LORO, 12 kênh, lab, M01}", BC) mà không ghi khoảng cách giữa khung 1:10 và nhà xưởng |
| Kết quả "16/16", GUID trùng | ML/CD/OL gọi 8 cặp duplicate IFC_GUID là "known issue (xác nhận, chưa xác minh actual binding)" (ML L221); ML §23 và nhóm dùng "CONFIRMED" cho 718/8 cặp | 16/16 ngày 23/09 chỉ là kiểm thử đơn vị; 8 cặp chỉ NGHI NGỜ | TB: nhóm A cùng dùng "xác nhận" cho 8 cặp (chỉ từ báo cáo audit đã lưu, OL/BC ghi "chưa chạy lại"); 16/16 ngày 23/09 nằm ngoài khoảng ngày của nhóm A (14–16/09) |

---

## 5. Tài sản đáng giữ (cho Pha 1) và thứ nên bỏ

**Giữ (đề xuất, chờ NCS duyệt):**
| Tài sản | Tệp | Lý do |
|---|---|---|
| Ba lớp trạng thái độc lập (Evidence_Qualification / Component_Selection / Binding_Verification) và trạng thái MULTI_CANDIDATE là trạng thái được quản trị | G2P L64–81; ML CQ-3; CD L126 | Khớp ý C1/C3 (định danh) của phạm vi khóa; có sẵn định nghĩa |
| Quy tắc `applicability_set` vs `query_context_descriptor` → `FAIL: SCOPE_VIOLATION`; tách model/version khỏi validity | ML L111, L184; CD L93 | Tiền thân trực tiếp của A2 và C5 |
| Danh sách negative fixture (9 loại) và nguyên tắc "sensor anomaly không phải invalid-link test" | ML L240–L258 | Nguồn gợi ý nhóm lỗi chèn mù; cần người chèn độc lập |
| Phân biệt nguồn dữ liệu: `[DỮ LIỆU THẬT]`, `[MÔ PHỎNG]` trong G2P | G2P L128 | Mẫu ghi nhãn mức xác nhận |
| Ranh giới novelty Borkowski 2026 ("HIGH nhưng hẹp") và danh sách "không claim mới" | CD L62–L66, L98; ML L22–L32 | Dùng để đặt đóng góp; cần kiểm lại toàn văn theo quy tắc 2 |
| Bảng Claim → Evidence → Limitation → Next Action và danh sách STOP | ML §21–22 | Mẫu kiểm soát claim, tương thích quy tắc 1, 7 |
| Ghi nhận "known issue 8 cặp GUID trùng" (nghi ngờ, 16 ElementIds) và `API_THREAD_TIMEOUT` | ML L221, L286 | Dữ kiện cho C1; phải ghi NGHI NGỜ |
| Nhật ký dọn dẹp CSV (OPS 81/81 SUCCESS, hash trước = sau) | OPS, INV, MAN | Bằng chứng toàn vẹn tệp; dùng để khẳng định không mất tệp nào |
| Phụ lục A/B của OL (phụ trách, điều kiện hoàn tất, bảng nguồn I1…) | OL L366–L420 | Mẫu quản lý artefact |

**Nên bỏ hoặc hạ cấp:**
| Thứ | Tệp | Lý do |
|---|---|---|
| Toàn bộ số liệu [SIM] của manuscript mô phỏng (JN Phần C) | JN L264+ | Giả lập, không được trích; chứa lỗi nội tại ("6 wrong verdicts" nên là 10, "8 Scopus queries" nhưng chỉ liệt kê 6) |
| Tài khẳng định "CONFIRMED" cho 718 phần tử và 8 cặp trùng | ML §23 (so với OL/BC "chưa chạy lại") | Mức xác nhận không đủ; hạ về NGHI NGỜ/[CẦN NGUỒN] |
| Chuỗi 5 thực thể + Action_Status làm điểm cuối | CD L126–130 | Thay bằng 6 thực thể; chỉ giữ như lịch sử |
| 8 CQ (OL/BC) và 5 CQ (ML) | OL, BC, ML | Thay bằng 3 câu truy ngược; giữ lại như nguồn lọc |
| Hai bản GT1/GT2 | GT1, GT2 | Giữ GT2; GT1 trùng (xem mục 7) |
| BC (báo cáo lớn 15/09) làm nguồn "hiệu lực" | BC | Có ví dụ minh họa (GUID X, H01) dễ bị nhầm với số thật; chứa freeze chưa tính Bellon/García |
| Nhãn "C1–C3" cho đóng góp | CD, ML | Trùng nhãn C1,C3 của ràng buộc; nên đặt lại tên khi lập Pha 1 |
| Các số dung lượng/hash cho ba bản xuất Zotero trong CP | CP L26 | Hash không có trong bộ txt, không kiểm lại được |

---

## 6. Ghi chú bất thường

1. **Mâu thuẫn nội bộ về dọn dẹp.** CR nói thư mục lưu trữ (archive) tồn tại (CR L21: archive 32); ML §23 nói archive không tồn tại trên đĩa; bố cục thật trong sha256_p2.txt là phẳng (01_EVIDENCE/ và tệp gốc). MAN liệt kê 85 dòng (3 + 50 + 32) nhưng MAN không có SHA256 cho 32 dòng archive.
2. **"PRE_FAILURE" trong tên tệp MAN.** Không có tệp nhóm A nào ghi một lần "failure": OPS 81/81 SUCCESS, DIR 7/7 SUCCESS, không có từ "failure" trong bất kỳ CSV. Nguyên nhân của hậu tố "PRE_FAILURE" không được ghi trong nhóm; mọi giải thích đều là suy luận. Cần hỏi NCS.
3. **Tệp được tham chiếu nhưng không có trong bộ txt/nhóm A:** `EVIDENCE_GATES_v2.1.md`, `CURRENT_STATUS_AND_NEXT_DIRECTION.md`, `01_EVIDENCE/10_NOVELTY_CHECK_SUMMARY_20260916.md`, `06_TARGETED_GAP_AUDIT.md`, `07_BORKOWSKI_2026_FULLTEXT_REVIEW.md`, `08_CORRECTION_PASS_SUMMARY.md`, `00_BIBLIOGRAPHIC_VERIFICATION.md` (xuất hiện trong ML/CD/CP). sha256_p2.txt (67 dòng) không liệt kê chúng; nhiều tệp chỉ có trong bản sao lưu trước dọn dẹp. [CẦN KIỂM: có còn trong thư mục NCS không]
4. **Sai ngày.** ML mang tên/ngày 15/09 nhưng chứa phần kiểm độ mới ngày 16/09 (ML L56); BC (15/09) không có phần này. GT1 tuyên bố "mới ngày 16/09" về việc phát hiện Bellon/García trong khi JN (14/09) đã trích cả hai.
5. **Mâu thuẫn về mức xác nhận.** ML gọi 718 phần tử và 8 cặp trùng là "CONFIRMED"; OL/BC ghi "chưa chạy lại"; nguồn gốc là một báo cáo đã lưu (ML L221, "chưa xác minh actual binding").
6. **Tham chiếu § lệch.** ML dẫn các số § lệch một so với tiêu đề thực tế (theo ghi nhận khi đọc; ví dụ tham chiếu "G2_ONE_PAGE §11" cho CQ nháp; số dòng cụ thể [CẦN KIỂM]).
7. **Lỗi trong JN.** "8 Scopus queries" nhưng chỉ liệt kê 6; [SIM] "6 wrong verdicts" thực ra 10; số liệu [SIM] bị lẫn với số thật nếu không đọc nhãn.
8. **GT2 lỗi thời trong kết luận.** GT2 thêm hộp novelty và dòng tài liệu nhưng §8 và kết luận vẫn nói "4 bài cần đọc" trong khi §6 ghi 3/4 đã đọc.
9. **Hai tập "C1–C3" khác nghĩa** (đóng góp C1–C3 trong CD/ML; ràng buộc C1–C3 cũ trong v0.2/JN) và hai tập mã CQ4 (CQ-4 evidence validity ở ML, CQ4 scope ở OL/BC) cùng nhãn. Hai bộ trạng thái binding khác nhau (ML: NOT_ASSESSED/SUSPECTED/CANDIDATE/BLOCKED/VERIFIED/REJECTED; BC: VERIFIED, rút gọn).
10. **G1 OPEN dù Paper 1 đã khóa.** ML L352 tự ghi mâu thuẫn với "CLOSED/LOCKED" của yêu cầu khung; phạm vi khóa nói Paper 1 đã SCIENCE LOCKED 13/09.
11. **Nhãn MCP/công cụ.** Nhóm dùng "Revit MCP / DT Evidence Bridge"; `compare_with_ifc_binding` bị `API_THREAD_TIMEOUT` (ML L286); không có kết quả binding thật.
12. **Trích dẫn đáng ngờ/chưa kiểm:** GT2 tham khảo (L348–L390) và JN [1]–[…] ghi mức kiểm "metadata + abstract" (JN L655–L673), không phải toàn văn → [CHƯA ĐỌC TOÀN VĂN]. Bellon 2025 DOI trong JN L671 (10.1016/j.autcon.2025.106157) chưa kiểm bằng công cụ trong phiên này → [CẦN KIỂM]. Hạng Q, APC của tạp chí trong JN L212–L232 → [CẦN KIỂM].
13. **Chi tiết chính xác của các dòng trong bảng ở mục 3–4** lấy từ grep số dòng của bản txt hiện tại; nếu bản txt được chuyển lại, số dòng có thể lệch.

---

## 7. Chuỗi phiên bản (theo thời gian, nhóm A)

Thứ tự dựa trên mtime trong INV, nhãn phiên bản trong tệp và trích dẫn chéo. Thứ tự giữa CD, ML, RC trong ngày 15/09 không xác định được từ nội dung.

| # | Ngày | Tệp / phiên bản | Đổi gì so với bản trước |
|---|---|---|---|
| 1 | 14/09 11:20 | G2P (G2 one-page, v0.2; ghi đè v0.1) | Giữ RQ2, WP2, chuỗi định danh v0.1; thêm 3 lớp trạng thái độc lập, trạng thái MULTI_CANDIDATE, 5 CQ nháp (§11), case S4/S5; G3 = OPEN, EXECUTION NOT OPEN |
| 2 | 14/09 (12:19) | OL v0.1 (outline docx) | Dàn bài bài báo; 8 CQ (CQ1–CQ8); Phụ lục A/B; D1–D7 quyết định mở; số liệu để trống "[n_correct]/[N_cases]" |
| 3 | 14/09 (12:45) | JN v0.2 (nhật ký định hướng docx) | Thêm đề xuất tạp chí (AiC chính), manuscript [SIM], sổ thiếu M1–M11, quyết định D1–D11 (thêm D8–D11 so với OL), dẫn chứng Consensus/Scopus ("8 queries"/6 liệt kê) |
| 4 | 14–15/09 | (báo cáo deep-research 14/09 14:45 và 15/09 07:56, rà soát targeted 15/09 19:25–20:31; không thuộc nhóm A) | Kết quả rà soát 12 bài + CORE-5; Borkowski toàn văn 26/26 trang |
| 5 | 15/09 20:58 | CR, CP, OPS, DIR, INV, MAN (dọn dẹp) | 81 tệp chuyển (MOVE 81/81 SUCCESS); sinh README_CURRENT, tạo 00_CURRENT/01_EVIDENCE/archive |
| 6 | 15/09 | CD (Current Direction) | Chuyển sang khung GAP-A…H, GAP 1/2/3, C1–C3, 5 CQ, G1 OPEN-PARTIAL, bảng 9 mục 5–9; chuỗi giữ dạng kết thúc ở Action_Status (CD L130) |
| 7 | 15/09 | ML (Master Execution Lock) | Khóa: literature freeze (CLOSE_SEARCH), "không tạo contribution thứ 4", Gate 2 PASS criteria 0/10, 9 negative fixture, bảng Claim→Evidence, STOP/DO-NOT-DO, §23 cảnh báo; chứa mục novelty 16/09 (L56) dù ngày 15/09 |
| 8 | 15/09 | RC (README_CURRENT) | 13 dòng chỉ đường, dẫn ML §4 literature freeze |
| 9 | 15/09 | BC (Báo cáo tổng hợp) | Báo cáo dài (1.372 dòng) mô tả chuỗi, ví dụ minh họa (CE-001, BND-001, H01), CQ1–CQ8; không chứa kiểm độ mới 16/09 |
| 10 | 16/09 | GT1 (giải thích dễ hiểu) | Bản giải thích cho NCS; hộp "novelty mới ngày 16/09" |
| 11 | 16/09 | GT2 (v2) | So với GT1: thêm hộp novelty, dòng bảng và tài liệu tham khảo mới (Bellon 2025, Gragnaniello 2024, Mariniello 2025, García 2026…); P2/P2-A…E; kết luận §8 chưa cập nhật (còn "4 bài cần đọc") |

Ghi chú: các tệp 15/09 CD, ML, RC, BC có thứ tự tương đối không chắc chắn; việc xếp #6–#9 là theo logic nội dung (CD → ML → RC), còn BC xếp cuối vì không có phần 16/09. Chuỗi trên dựa trên mtime của INV cho G2P, OL, JN (14/09 11:20:29; 12:19:23; 12:45:40); các dòng còn lại không có mtime riêng trong dữ kiện đã đọc.
