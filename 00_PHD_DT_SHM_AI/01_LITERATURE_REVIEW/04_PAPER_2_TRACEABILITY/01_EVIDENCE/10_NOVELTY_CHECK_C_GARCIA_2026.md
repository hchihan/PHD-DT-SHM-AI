# 10-C — Novelty Check: García, Toledo, Aragonés & Bañón (2026)

**Nhiệm vụ:** Kiểm tra mối đe dọa tính mới có giới hạn cho Paper 2 / Gate 2–3 (16/09/2026).

## Thư mục

| Trường | Giá trị |
|---|---|
| Tiêu đề | A CDE-Centered Quality Gate Framework to Operationalize ISO 19650 Governance in Hybrid Railway Depots |
| Tác giả | Juan A. García, Ignacio Toledo, Luis Aragonés, Luis Bañón |
| Tạp chí | Applied Sciences, 16(5), 2562 |
| DOI | 10.3390/app16052562 (theo yêu cầu người dùng; DOI không hiển thị tường minh trong trích dẫn văn bản mà NotebookLM trả về — chỉ thấy article number `applsci-16-02562`, khớp số bài với DOI cung cấp) |
| Năm | 2026 (Published 06/03/2026; Received 11/02/2026; Accepted 04/03/2026) |
| Xác nhận nguồn | Khớp tiêu đề/tác giả/tạp chí/article-number do NotebookLM trích xuất trực tiếp từ header PDF (`applsci-16-02562-v2.pdf`). DOI không tự xuất hiện trong text trích dẫn nhưng article number khớp DOI đề bài — không mâu thuẫn. |

**Nguồn đã đọc:** Toàn văn qua NotebookLM MCP. **Mức bằng chứng: FULL_TEXT.**

---

## Q1–Q12

**Q1 — Vấn đề nghiên cứu:** **YES.** Ba vấn đề: (1) khoảng trống quản trị CDE giữa yêu cầu tài liệu (EIR/AIR/BEP) và bằng chứng có thể kiểm toán cho quyết định publish/hold theo ISO 19650; (2) đứt gãy PIM→AIM khi bàn giao cho O&M; (3) xung đột liên ngành trong depot đường sắt hỗn hợp. *Trích dẫn: Mục 1.1–1.2; Bảng 1.*

**Q2 — Chuỗi thông tin:** **PARTIAL.** Bài **không** xử lý sensor/condition data — đầu vào hoàn toàn là tệp giao nộp IFC. Chuỗi: IFC container + revision (khu vực `Shared`) → **Pre-Published Quality Gate** (3 khối: Spatial/Semantic/Data Gate) → kiểm tra ở cấp container và cấp phần tử IFC (FU/UT) → **Minimal Persistent Evidence Package** (file-level report, package-level summary, decision record, NCR/BCF log) → quyết định `Publish`/`Hold` (gate all-pass → chuyển `Shared`→`Published`; fail → giữ `Hold`, tạo BCF/NCR, nộp lại `vR+1`). *Trích dẫn: Mục 3.2–3.6; Hình 2, 4, 5; Bảng 4–6.*

**Q3 — Định danh cấu kiện:** **PARTIAL.** Không dùng thuật ngữ `IfcGlobalUniqueId`/`GlobalId` tường minh. Định danh ở 2 cấp: (i) container/tệp — unique deliverable identifier (mã doanh nghiệp + revision + ngày + hash toàn vẹn tệp); (ii) phần tử IFC — phân loại thực thể (`IfcBuildingElementProxy`) + mã nội bộ doanh nghiệp **Functional Unit (FU)** và **Technical Location (UT)** gán làm thuộc tính. Đã xác minh trên **22 tệp IFC2x3 xuất ra thật** từ CDE chủ đầu tư (FGV), 2 dự án depot thực (El Campello, Nazaret), 3 trạng thái giao nộp (EX/PC/EW). *Trích dẫn: Mục 3.1, 3.3, 3.5; Bảng 6; Phụ lục A.*

**Q4 — Quản lý phiên bản mô hình:** **YES.** Cơ chế CDE/ISO 19650 đầy đủ: `WIP→Shared→Published→Archived`, mã revision + ngày, hash toàn vẹn tệp; khi `HOLD`, tạo NCR/BCF gắn `[Container ID + Revision]`, tác giả sửa và nộp lại `vR+1`, gate chạy lại từ đầu; phiên bản cũ bị `superseded` và chuyển `Archived` giữ nguyên audit trail. **Đây là model/version context, đã phân biệt tường minh với evidence validity ở Q6.** *Trích dẫn: Bảng 1; Mục 3.5–3.7; Hình 5–6; Bảng 6–7.*

**Q5 — Provenance:** **PARTIAL.** Con người CÓ (Author, Phase BIM Responsible, Contract Responsible/FGV, BIM Coordinator — đủ vai trò RACI). Nguồn xuất bản tệp CÓ (`Export software and version/preset`). Metadata định danh/kiểm toán CÓ (unique ID, revision+date, hash, CDE state). Đo lường và xử lý dữ liệu cảm biến: **KHÔNG CÓ** (ngoài phạm vi — không có sensor data). *Trích dẫn: Mục 3.5; Bảng 6–7.*

**Q6 — Phạm vi hiệu lực bằng chứng:** **NO.** Không có `valid_from/valid_to`, không có điều kiện tái sử dụng bằng chứng độc lập. Bằng chứng (`evidence package`) gắn cố định 1-1 với `container ID + revision` tại thời điểm chạy gate — không có scope áp dụng riêng biệt khỏi CDE state. Đã phân biệt tường minh ba khái niệm: CDE version/status (CÓ, chi tiết), case-study scope (CÓ — El Campello/Nazaret), evidence validity/applicability (KHÔNG CÓ). *Trích dẫn: Mục 3.5; Bảng 6.*

**Q7 — Accountability:** **YES.** Đầy đủ nhất trong 3 bài: performer (`BIM Coordinator`/`BIM Technical Office` — người chạy gate/tập hợp bằng chứng), reviewer/technical sign-off (`Phase BIM Responsible`), approver (`Contract Responsible`/FGV), status (CDE state; gate decision `ACCEPT/REJECT`; NCR/BCF `Open/Assign/Track/Close`), supersession (phiên bản bị thay thế lưu ở `Archived`, giữ audit trail). *Trích dẫn: Bảng 6–7; Hình 5–6; Phụ lục A, Bảng A1.*

**Q8 — Truy vết xuôi/ngược:** **PARTIAL.** CÓ truy vết 2 chiều giữa các bản ghi CDE/IFC, qua **6 loại bản ghi**: deliverable metadata (CDE), IFC data (element level), file-level report, package-level summary, NCR/BCF issue log, publish/hold decision record + CDE state. Chuỗi liên kết công bố tường minh: "*IFC → file report → package summary → NCR/BCF → decision record → state*". **KHÔNG CÓ** liên kết tới sensor/condition evidence — ngoài phạm vi bài. *Trích dẫn: Bảng 6 (Traceability CDE); Mục 3.7.*

**Q9 — Kiểm chứng:** **PARTIAL.** Không có competency questions/expected-answer kiểu ontology. Có PASS/FAIL định lượng rõ ràng: `proxy_pct<50%`, `anchor_dist_m≤5m/20m`, `data_core_pass=1` → `All Gates Pass`. Mẫu số: **N=22 tệp IFC thật** (El Campello: 4 EX+9 PC; Nazaret: 9 EW). *Trích dẫn: Mục 3.1, 3.4; Bảng 3, 5; Mục 5, Bảng 9–10; Phụ lục A.*

**Q10 — Kiểm thử âm tính cố ý:** **PARTIAL.** Dựa trên lỗi thật phát sinh tự nhiên từ dữ liệu thực địa (không phải fixture tổng hợp cố ý cấy vào): sai lệch không gian/neo (`anchor_dist_m` vượt ngưỡng, có trường hợp lệch 4,4 tỷ mét do sai đơn vị); thiếu georeferencing; lạm dụng proxy (`proxy_pct≥50%`); thiếu Pset cốt lõi; thiếu mã PK/Alignment tuyến tính; thiếu/sai mã FU. Kết quả: **14/22 tệp (63,6%) bị `HOLD`**. **KHÔNG CÓ**: orphan record, duplicate ID, stale condition data, binding conflict, missing target, out-of-evidence-validity (test tổng hợp cố ý theo đúng taxonomy Gate 3 của Paper 2 không được thực hiện). *Trích dẫn: Mục 3.3–3.4; Bảng 5; Hình 7; Bảng 10; Phụ lục A.*

**Q11 — Đã xác lập:** Khung Quality Gate 3 khối (Spatial/Semantic/Data) chuyển EIR/BEP thành quy trình kiểm soát giao nộp IFC có thể kiểm toán; lớp Functional Unit biểu diễn kép (CDE container metadata + IFC element attribute) đảm bảo liên tục PIM→AIM; thực chứng trên 22 tệp IFC thật, tỷ lệ đạt tất cả gate 25,0–44,4% theo Case×State, 14/22 (63,6%) HOLD; ma trận crosswalk theo thời gian (CW-1) đảm bảo so sánh công bằng khi BEP thay đổi. *Trích dẫn: Mục 1.3; Mục 3.3; Mục 4; Mục 5, Bảng 9–10, Hình 7.*

**Q12 — Không làm (so C1/C2/C3):** **NO** cho cả ba. Không có framework tích hợp Sensor_ID/Condition_Evidence_ID/Inspection_Record_ID (C1) — hoàn toàn không có sensor/condition data, bài chỉ quản trị xuất bản mô hình BIM. Không có evidence-validity/applicability rule tách biệt khỏi CDE status (C2). Không có giao thức đa chặng kèm competency-question-style expected-answer và bộ negative-fixture tổng hợp cố ý theo đúng taxonomy Gate 3 (C3) — chỉ có quy tắc tính toán (`computable rules`) trên lỗi thực địa tự nhiên.

---

## Mức đe dọa: **HIGH — hẹp, nhắm vào GAP 1 (accountable record pattern) và một phần GAP 3 (multi-record traceability chain)**

**Lý do:**
- Bài C là bằng chứng **full-text, thực nghiệm trên 22 tệp IFC thật**, cho thấy một **accountable-record pattern hoàn chỉnh** (performer + reviewer + approver + status + supersession — đủ cả 5 trường mà GAP 1/GAP-E của Paper 2 đòi hỏi) **đã được triển khai và kiểm chứng thực tế** trong bối cảnh CDE/ISO 19650. Đây là bằng chứng **mạnh hơn** cả G3_02 Wan et al. 2019 (chỉ narrative, chưa hình thức hóa) — tương tự mức độ nghiêm ngặt của Borkowski 2026 cho GAP-B.
- Bài C cũng chứng minh một **chuỗi truy vết đa bản ghi (6 loại) có liên kết tường minh, kiểm chứng được** (`IFC → file report → package summary → NCR/BCF → decision record → state`) — đây là dạng multi-hop traceability gần với tinh thần GAP 3, dù không đúng chuỗi Sensor→Evidence→Inspection của Paper 2.
- **Ranh giới thu hẹp bắt buộc, để Paper 2 không bị trùng:** đối tượng của accountable record trong bài C là **quyết định xuất bản mô hình BIM** (publish/hold một deliverable IFC), **không phải** bản ghi kiểm tra tình trạng vật lý công trình (inspection of physical condition) gắn với Condition_Evidence_ID từ cảm biến. Bài C hoàn toàn không có sensor/condition data (Q2, Q5 xác nhận). Do đó GAP 1 của Paper 2 (Accountable **BIM-linked Inspection Record** cho condition evidence) **không bị mất**, nhưng **claim "accountable record pattern with performer/reviewer/approver/status/supersession chưa từng áp dụng cho bối cảnh BIM" không còn giữ được ở mức tổng quát** — phải thu hẹp câu chữ để chỉ rõ đối tượng của Paper 2 là **inspection/condition-evidence record**, khác với **model-deliverable quality-gate record** của García.
- Không đạt VERY_HIGH vì: (a) không có sensor/condition evidence nào trong bài; (b) không có evidence-validity/applicability rule (Q6 = NO, xác nhận GAP 2/GAP-D vẫn mở); (c) không có kiểm thử âm tính tổng hợp cố ý theo đúng taxonomy Gate 3 (chỉ dựa lỗi thực địa tự nhiên).

## Claim → Evidence → Limitation → Implication

| Claim | Evidence | Limitation | Implication |
|---|---|---|---|
| García 2026 đe dọa hẹp sub-claim "accountable record pattern chưa từng áp dụng trong quản trị BIM" (một phần GAP 1) và củng cố multi-record traceability (một phần GAP 3), nhưng không đe dọa C1 toàn phần vì thiếu hoàn toàn sensor/condition evidence | Q5, Q7, Q8: RACI đầy đủ 5 trường + chuỗi 6 loại bản ghi có liên kết tường minh, kiểm chứng trên N=22 tệp IFC thật | Đọc qua NotebookLM, DOI không tự xuất hiện trong trích dẫn text (chỉ suy ra từ article number khớp với DOI người dùng cung cấp) — cần đối chiếu DOI trực tiếp nếu trích dẫn chính thức trong bản thảo Paper 2 | Paper 2 phải viết lại câu tuyên bố C1/GAP1 theo hướng an toàn hơn: nêu rõ đối tượng của Inspection Record là **condition-evidence-anchored inspection**, phân biệt tường minh với **model-deliverable governance record** (như García) — tái dùng RACI pattern của García như prior art hợp lệ, không tái phát minh, nhưng khẳng định novelty nằm ở việc neo accountable record vào Condition_Evidence_ID xuất phát từ sensor, điều García không có |
