# BẢN NHÁP — G2 Traceability Specification (v0.2, chưa khóa)

**Loại tài liệu:** Bản nháp làm việc để người dùng review và khóa quyết định trước audit. KHÔNG phải đặc tả đã duyệt, KHÔNG phải Gate Decision Record.
**Version:** v0.2 | **Ngày:** 14/09/2026 | **Trạng thái:** DRAFT — CHƯA REVIEW — CHƯA FREEZE
**Supersedes (bản nháp nội bộ, không phải file governance chính thức):** `G2_ONE_PAGE_TRACEABILITY_DRAFT_20260914.md` v0.1 cùng ngày. Sửa bảy điểm được người dùng chỉ ra ở v0.1 (xem mục "Thay đổi so với v0.1").
**Nguồn đã đọc lại khi sửa:** giữ nguyên danh sách v0.1 — `deep-research-report_13092026_UPDATED_GATE2_GATE3_MCP.md`, `deep-research-report_13092026.md`, `PAPER2_CURRENT_DIRECTION_v2.1_20260804.md` (header v2.2), `G2_G3_PAPER2_CURRENT_ROADMAP_v2.1_20260804.md` (header v2.2), `PAPER2_VERIFIABLE_TRACEABILITY_DETAILED_OUTLINE_v0.1_20260812.md`, `01_CURRENT_CONTROL/CURRENT_STATUS_AND_NEXT_DIRECTION.md` v2.4 (13/09/2026). Không đọc thêm file mới cho lần sửa này; không có dữ liệu đo mới.

## Ký hiệu dùng xuyên suốt tài liệu

- `[DỮ LIỆU THẬT]` — quan sát trực tiếp từ audit/pilot trên live Revit model, có nguồn trích dẫn.
- `[CHƯA XÁC MINH]` — công cụ đã chạy nhưng kết quả bị block/timeout/không đầy đủ; không được diễn giải thành PASS hay FAIL.
- `[FIXTURE MÔ PHỎNG]` — dữ liệu dựng cho mục đích kiểm thử (negative fixture), không tương ứng bất kỳ sự kiện inspection/field thật nào.
- `[ĐỀ XUẤT — CHƯA DUYỆT]` — thực thể/trường noncanonical theo `CURRENT_STATUS_AND_NEXT_DIRECTION` v2.4, cần quyết định thay đổi phạm vi trước khi đưa vào schema.

## Routing block

```text
RQ:              RQ2
WP:              WP2
Chương:          Chương 5
Paper:           Paper 2
Evidence Gate:   Gate 2 (specification, đang OPEN); Gate 3 xem trạng thái chính xác bên dưới
Scope:           Core — Information traceability
Evidence type:   Information traceability
```

Giữ nguyên RQ2, WP2, Chương 5/Paper 2 và chuỗi định danh canonical như v0.1:
**`Sensor_ID → BIM_GUID → Condition_Evidence_ID → Inspection_Record_ID → Action_Status`** (nguồn: `CURRENT_STATUS_AND_NEXT_DIRECTION` v2.4 §2, source-of-truth level 5).

## Trạng thái Gate 3 — sửa chính xác (điểm 1)

v0.1 viết tắt "Gate 3 chưa mở (NOT OPEN)", gộp hai khái niệm khác nhau. Trích nguyên văn `CURRENT_STATUS_AND_NEXT_DIRECTION` v2.4 §1:

> G3: `OPEN — NOT IMPLEMENTED, NOT VALIDATED, NOT OFFICIALLY PASSED`. Execution authorization is `NOT OPEN` until G2 is baselined and explicitly accepted.

Vậy có **hai trạng thái tách biệt**:
1. **Trạng thái Gate 3** = `OPEN` (gate chưa đóng theo bất kỳ hướng nào — chưa PASS, chưa FAIL).
2. **Trạng thái execution authorization của Gate 3** = `NOT OPEN` (chưa được phép bắt đầu thực thi validation), và điều kiện để chuyển sang `OPEN` là một quyết định review tường minh chấp nhận G2 baseline — không phải do thời gian hay do có schema chạy được.

Bản nháp này không tuyên bố Gate 3 PASS, FAIL, hay "đã mở"/"đã đóng" dưới bất kỳ hình thức rút gọn nào.

## Xung đột nguồn — không âm thầm hợp nhất (giữ nguyên từ v0.1)

`CURRENT_STATUS_AND_NEXT_DIRECTION.md` v2.4 khóa `Asset_ID`, `Model_Version_ID`, `Action_Record_ID`, `Workflow_Status`, `Status_Event` là **noncanonical, chưa duyệt**. `PAPER2_CURRENT_DIRECTION`/`ROADMAP`/`DETAILED_OUTLINE` trong cùng thư mục dùng một số thực thể này như phần chuỗi mở rộng. Bản nháp tiếp tục đánh dấu `[ĐỀ XUẤT — CHƯA DUYỆT]` cho các trường này, không tự chọn bên nào superseded.

---

## (1) Mục tiêu RQ2 và hai use case — giữ nguyên nội dung v0.1

**Mục tiêu RQ2:** Tổ chức và liên kết condition evidence cùng độ tin cậy của nó với BIM component và inspection record, hỗ trợ giải trình và truy vết quyết định inspection trong điều kiện dữ liệu hư hỏng hiện trường hạn chế. Không chẩn đoán hư hỏng, không tự động hóa quyết định bảo trì.

- **UC1 — Truy vết thuận (forward).** Từ một `Condition_Evidence_ID` mới, xác định cấu kiện BIM liên quan, trạng thái đánh giá binding, và các `Inspection_Record` đã trích dẫn nó.
- **UC2 — Truy vết ngược (reverse, giải trình/audit).** Từ một `Inspection_Record_ID` đã tồn tại (không phải từ giá trị `Action_Status` — xem điểm 4 bên dưới), chứng minh nó dựa trên evidence nào, từ sensor/campaign/run nào, ai đã review, và evidence đó có đang trong phạm vi hiệu lực hay không.

---

## (2) Tách ba lớp quyết định thay vì một `Evidence_Status` gộp chung (điểm 3)

v0.1 dùng một trường `Evidence_Status (candidate/verified/ambiguous)` gộp cả ba việc khác nhau. Tách rõ:

| Lớp quyết định | Câu hỏi trả lời | Ai/cái gì quyết định | Trạng thái riêng |
|---|---|---|---|
| **A — Evidence Qualification** | Condition evidence này có đủ provenance/CEI để được dùng cho traceability không? | Rule tự động (completeness/CEI check) + reviewer | `Evidence_Qualification_Status` |
| **B — Component Selection** (Decision A trong outline) | Trong số các BIM component candidate, người có thẩm quyền chọn cái nào làm host? | Con người, có ghi actor/rationale/timestamp | `Component_Selection_Status` |
| **C — IFC-Binding Verification** (Decision B trong outline) | Correspondence giữa Revit element đã chọn với actual exported IFC GlobalId đã được xác minh độc lập chưa? | IfcOpenShell + con người duyệt | `Binding_Verification_Status` |

Ba lớp này **độc lập** — một component có thể đã qua Decision A (đã chọn) nhưng Decision B vẫn `NOT_ASSESSED` hoặc `SUSPECTED_IDENTITY_ANOMALY`.

---

## (3) Bảng trạng thái bản ghi (record status) — mới, thay cho một cột "Evidence_Status"

| Thực thể | Trạng thái khả dĩ | Là gì | Có phải khóa tra cứu không |
|---|---|---|---|
| `Evidence_Qualification_Status` | `DRAFT`, `QUALIFIED`, `REJECTED` | Thuộc tính của `Condition_Evidence_ID` | Không — chỉ là filter |
| `Component_Selection_Status` | `UNRESOLVED`, `MULTI_CANDIDATE`, `HUMAN_SELECTED` | Thuộc tính theo cặp (prototype location, model version) | Không |
| `Binding_Verification_Status` | `NOT_ASSESSED`, `SUSPECTED_IDENTITY_ANOMALY`, `CANDIDATE_BINDING`, `BLOCKED`, `VERIFIED_BINDING`, `REJECTED_BINDING` | Thuộc tính của một binding cụ thể (Revit UID ↔ actual IFC GlobalId, tại một model version) | Không |
| `Inspection_Record_Status` | `DRAFT`, `REVIEWED`, `APPROVED` | Thuộc tính của `Inspection_Record_ID` | Không |
| `Action_Status` | `OPEN`, `IN_PROGRESS`, `CLOSED`, `REOPENED` | **Projection hiện tại** gắn với một `Inspection_Record_ID` cụ thể, canonical theo v2.4 nhưng KHÔNG phải identity | **Không — xem điểm (4)** |

`MULTI_CANDIDATE` là **trạng thái cần quản trị**, không phải lỗi cần xóa bỏ (điểm 6). Một prototype location ở trạng thái `MULTI_CANDIDATE` là kết quả hợp lệ, đòi hỏi con người ra Decision A, không phải một defect phải ép về 1:1.

`SUSPECTED_IDENTITY_ANOMALY` và `BLOCKED` là hai trạng thái riêng biệt với `REJECTED_BINDING` — xem điểm (5).

---

## (4) Không dùng `Action_Status` làm khóa truy ngược (điểm 4)

**Vấn đề ở v0.1:** CQ-Backward và bảng field dùng ngầm "từ `Action_Status`, trả về..." — sai, vì `Action_Status` là một giá trị projection (`OPEN`/`IN_PROGRESS`/...) có thể trùng lặp trên nhiều `Inspection_Record_ID` cùng lúc; dùng nó làm khóa tra cứu sẽ trả về tập kết quả mơ hồ.

**Sửa:** mọi truy vết ngược (UC2) phải neo vào `Inspection_Record_ID` (canonical, là khóa duy nhất) làm điểm vào. `Action_Status` chỉ xuất hiện trong kết quả trả về như một **thuộc tính tại thời điểm truy vấn** của `Inspection_Record_ID` đó, không bao giờ là input của câu truy vấn ngược.

Điều này không đổi chuỗi canonical `... → Inspection_Record_ID → Action_Status` — chuỗi đó mô tả quan hệ dữ liệu (Inspection dẫn tới Action_Status), không phải quy tắc lập chỉ mục truy vấn.

---

## (5) Phân biệt duplicate Revit-side GUID với actual binding failure (điểm 5)

`[DỮ LIỆU THẬT]` Gate-2 read-only audit ghi nhận Structural Framing có 8 cặp duplicate Revit-side `IFC_GUID`, ảnh hưởng 16 ElementIds (nguồn: `deep-research-report_13092026_UPDATED_GATE2_GATE3_MCP.md` dòng 143).

`[CHƯA XÁC MINH]` Lần audit đó, `compare_with_ifc_binding` bị `API_THREAD_TIMEOUT`; do đó binding thực sự (actual IFC GlobalId) ở trạng thái `BLOCKED / NOT ASSESSED`, **không phải FAIL**.

Quy tắc bắt buộc trong schema: một Revit element có duplicate `IfcGUID` **tham số** chỉ được gắn `Binding_Verification_Status = SUSPECTED_IDENTITY_ANOMALY`. Trạng thái này **không được tự động chuyển** sang `REJECTED_BINDING` (actual binding failure) trừ khi IfcOpenShell đã đọc actual exported IFC và xác nhận trùng GlobalId thật trên file IFC đã xuất — vì Autodesk xác nhận exporter có thể tự sinh GUID khác khi phát hiện trùng, nên tham số phía Revit không đồng nghĩa với actual export identity.

---

## (6) Coi multi-candidate là trạng thái cần quản trị (điểm 6)

Đã đưa vào bảng (3) như một giá trị hợp lệ của `Component_Selection_Status`. Không còn liệt kê "cardinality không phải 1:1" trong mục "dữ liệu sai" — xem mục (8), case thứ hai đã được viết lại thành ví dụ về trạng thái cần quản trị, không phải lỗi.

---

## (7) Định nghĩa fixture ngoài scope bằng quy tắc tường minh (điểm 7)

v0.1 mô tả case #3 bằng lời văn, không có quy tắc kiểm tra được. Quy tắc tường minh thay thế:

> Mỗi `Condition_Evidence_ID` mang một `Scope_of_Validity.applicability_set` khai báo — tập hợp {campaign_id, evaluation_protocol_id, structural_context} mà evidence này được coi là có hiệu lực. Một truy vấn hoặc một `Inspection_Record` trích dẫn evidence này phải khai báo `query_context_descriptor` cùng cấu trúc. Quy tắc: nếu `query_context_descriptor ∉ Scope_of_Validity.applicability_set` → trả về `FAIL: SCOPE_VIOLATION`. Không có ngoại lệ ngầm định.

Fixture cụ thể theo quy tắc này ở case S5, mục (9).

---

## (8) Ba trường hợp dữ liệu sai — viết lại theo bảy điểm sửa

| # | Loại | Nguồn dữ liệu | Mô tả | Hành vi kỳ vọng |
|---|---|---|---|---|
| 1 | Suspected identity anomaly (không phải verified binding failure) | `[DỮ LIỆU THẬT]` 8 cặp duplicate Revit-side `IFC_GUID`, 16 ElementIds | Evidence có thể bị binding nhầm vào 1 trong các element trùng tham số GUID | `Binding_Verification_Status = SUSPECTED_IDENTITY_ANOMALY`; không tự chuyển sang `REJECTED_BINDING` hay `VERIFIED_BINDING` — xem mục (5) |
| 2 | Multi-candidate — trạng thái cần quản trị, không phải lỗi | `[DỮ LIỆU THẬT]` Pilot Run 02, case S2 (cột–rafter tại grid B-5) và S3 (2 composite bracing assemblies) | Một `Sensor_ID`/vị trí quan trắc ánh xạ hợp lý tới nhiều BIM component | `Component_Selection_Status = MULTI_CANDIDATE`; yêu cầu Decision A của con người, không ép về 1:1 — xem mục (6) |
| 3 | Vi phạm scope-of-validity theo quy tắc tường minh | `[FIXTURE MÔ PHỎNG]` — chưa từng xảy ra trên hồ sơ inspection thật | `query_context_descriptor` của một inspection giả định không nằm trong `applicability_set` đã khai báo của evidence | `FAIL: SCOPE_VIOLATION` theo quy tắc ở mục (7); không được âm thầm chấp nhận |

---

## (9) Hai ca pilot đề xuất — mới

**S4 — Duplicate-GUID disambiguation (đề xuất, dựa trên dữ liệu thật).**
`[DỮ LIỆU THẬT]` Chọn một trong 8 cặp Structural Framing có duplicate `IFC_GUID` tham số (16 ElementIds đã ghi nhận). Chạy cả hai element qua pipeline binding.
Mục tiêu kiểm thử: xác nhận cả hai element được gắn `SUSPECTED_IDENTITY_ANOMALY`, hệ thống từ chối gán `VERIFIED_BINDING` hoặc `REJECTED_BINDING` cho tới khi IfcOpenShell đọc actual exported IFC GlobalId. `[CHƯA XÁC MINH]` — lần chạy `compare_with_ifc_binding` trước đó bị timeout nên case này hiện chưa có kết quả binding thật; ca pilot đề xuất là để chạy lại, không phải báo cáo kết quả đã có.

**S5 — Cross-scope fixture (đề xuất, fixture mô phỏng).**
`[FIXTURE MÔ PHỎNG]` Dựng một `Condition_Evidence_ID` có nguồn gốc CP3 (biến động cao, SD_fold quan sát 0.139 — con số này là `[DỮ LIỆU THẬT]` từ Paper 1, nhưng việc "trích dẫn nó cho một inspection ở ngữ cảnh khác" là dựng, không có thật). Gán `applicability_set` = {CP3, protocol X}. Tạo một `query_context_descriptor` cố ý không thuộc tập đó.
Mục tiêu kiểm thử: xác nhận CQ-4 trả về `FAIL: SCOPE_VIOLATION` đúng theo quy tắc mục (7), không trả PASS sai hoặc bỏ qua kiểm tra.

Cả hai ca đều là **đề xuất chưa thực thi**; không case nào trong mục này đã có kết quả PASS/FAIL chính thức.

---

## (10) Schema `Inspection_Record` tối thiểu — mới

| Trường | Bắt buộc? | Ghi chú |
|---|---|---|
| `Inspection_Record_ID` | Required | Canonical, khóa chính |
| `Referenced_Component` = (`BIM_GUID`, `Binding_Verification_Status` tại thời điểm inspection) | Required | Snapshot tại thời điểm, không phải tham chiếu sống — vì binding có thể đổi trạng thái sau đó |
| `Cited_Condition_Evidence_ID` (1..N) | Required | Cardinality 1..N cần được xác nhận trong quyết định (5) ở mục (11) |
| Inspector actor identity | Required | Cho accountability (UC2) |
| Inspection timestamp | Required | |
| Finding (quan sát tách biệt khỏi diễn giải) | Required | Không gộp observation và interpretation vào một field tự do |
| `Inspection_Record_Status` (`DRAFT`/`REVIEWED`/`APPROVED`) | Required | Theo bảng (3) |
| Reviewer identity + timestamp khi `APPROVED` | Required nếu đã approved | |
| `Action_Status` (thuộc tính hiện tại, không phải khóa) | Required | Xem điểm (4) — chỉ đọc, không dùng làm input truy vấn |
| `Model_Version_ID` tại thời điểm binding snapshot | `[ĐỀ XUẤT — CHƯA DUYỆT]` | Noncanonical theo v2.4; cần quyết định thay đổi phạm vi trước khi coi là required |

---

## (11) Bảng CQ — input, expected result, PASS rule (thay bảng CQ cũ)

| CQ | Input | Expected result | PASS rule |
|---|---|---|---|
| CQ-1 Forward | `Condition_Evidence_ID` | Danh sách component candidate, mỗi candidate kèm `Binding_Verification_Status`; danh sách `Inspection_Record_ID` trích dẫn evidence này (hoặc rỗng + lý do) | Tập trả về khớp chính xác tập đã khai báo trong fixture (định danh + trạng thái từng candidate); không candidate nào hiển thị trạng thái cao hơn trạng thái đã khai báo (vd. `SUSPECTED_IDENTITY_ANOMALY` không được hiển thành `CANDIDATE_BINDING`) |
| CQ-2 Backward | `Inspection_Record_ID` (không phải `Action_Status` — xem mục (4)) | `Condition_Evidence_ID` được trích dẫn, `Sensor_ID`, campaign/run, protocol, reviewer identity/timestamp, và `Action_Status` hiện tại như một thuộc tính | Mọi trường khớp chính xác provenance đã khai báo trong fixture; nếu `Inspection_Record_ID` không tồn tại, trả về `NOT_FOUND` tường minh, không trả evidence rỗng |
| CQ-3 Multi-candidate governance | `Sensor_ID` hoặc vị trí quan trắc | Danh sách đầy đủ candidate kèm `Component_Selection_Status` riêng từng candidate; nếu >1 candidate hợp lý, trạng thái tổng thể = `MULTI_CANDIDATE` | Số lượng và trạng thái từng candidate khớp fixture; hệ thống không tự động collapse `MULTI_CANDIDATE` thành `HUMAN_SELECTED` khi chưa có bản ghi Decision A |
| CQ-4 Scope-of-validity | `Condition_Evidence_ID` + `query_context_descriptor` | `PASS` nếu `query_context_descriptor ∈ applicability_set`; `FAIL: SCOPE_VIOLATION` nếu không | Đúng quy tắc tường minh ở mục (7); không có ngoại lệ ngầm định, không silent-accept |
| CQ-5 Duplicate-identity negative | Một cặp element có duplicate `IfcGUID` tham số (case S4) | Cả hai trả về `Binding_Verification_Status = SUSPECTED_IDENTITY_ANOMALY` | Không có tự động promotion sang `VERIFIED_BINDING` hoặc `REJECTED_BINDING` khi binding check chưa chạy hoặc đang `BLOCKED`/`NOT_ASSESSED` — xem mục (5) |

---

## Thay đổi so với v0.1

1. Tách "trạng thái Gate 3" khỏi "trạng thái execution authorization của Gate 3", trích nguyên văn v2.4 thay vì diễn đạt gộp.
2. Required fields nay được gắn theo vòng đời bản ghi (Evidence Qualification → Component Selection → IFC-Binding Verification → Inspection → Action-projection) thay vì một bảng phẳng.
3. Tách `Evidence_Qualification_Status`, `Component_Selection_Status`, `Binding_Verification_Status` thành ba trục độc lập thay vì một `Evidence_Status` gộp.
4. `Action_Status` không còn là input của bất kỳ truy vấn ngược nào; khóa vào là `Inspection_Record_ID`.
5. Thêm trạng thái riêng `SUSPECTED_IDENTITY_ANOMALY`, tách khỏi `REJECTED_BINDING`/`VERIFIED_BINDING`.
6. `MULTI_CANDIDATE` chuyển từ "case dữ liệu sai" sang "trạng thái cần quản trị" trong bảng (3).
7. Case scope-of-validity nay có quy tắc kiểm tra tường minh (`applicability_set` / `query_context_descriptor`) thay vì mô tả bằng lời.
8. Thêm hai ca pilot đề xuất S4, S5 (đều đánh dấu đề xuất/fixture, chưa có kết quả).
9. Thêm bảng trạng thái bản ghi (mục 3) và schema `Inspection_Record` tối thiểu (mục 10).
10. Bảng CQ nay có ba cột input/expected/PASS rule; số CQ giữ ở 5, đổi CQ-5 từ "negative chung chung" thành ca cụ thể theo case S4.

---

## Kết thúc nhiệm vụ

- **File đã đọc:** không đọc thêm nguồn mới; dùng lại nguyên bộ nguồn đã đọc cho v0.1 (liệt kê ở đầu file).
- **File đã sửa:** `G2_ONE_PAGE_TRACEABILITY_DRAFT_20260914.md` (file này, ghi đè v0.1 bằng v0.2). Không sửa Revit, không điền metadata, không tạo/ghi đè file governance chính thức nào khác.
- **Evidence đã dùng:** như v0.1 — audit 718-element (duplicate GUID, `compare_with_ifc_binding` timeout/BLOCKED), Pilot Run 01/02 (S1/S2/S3), Paper 1 SD_fold CP3 (chỉ dùng làm giá trị ví dụ trong fixture mô phỏng, không phải payload đã accept).
- **Hạn chế chưa giải quyết:** cardinality `Cited_Condition_Evidence_ID` (1..N hay 1..1) chưa quyết; xung đột canonical/noncanonical giữa v2.4 và bộ tài liệu v2.1/v2.2 trong thư mục này vẫn chưa giải quyết; S4/S5 là đề xuất, chưa chạy; G1 payload vẫn `OPEN — PARTIAL EVIDENCE` nên mọi ví dụ evidence trong bản nháp vẫn là candidate/draft.
- **Next action:** người dùng review bảy điểm sửa và hai ca pilot mới; nếu chấp nhận, đưa mục (2)(3)(10)(11) vào bản pre-registration chính thức của Gate 2 (Competency Question Register, Integrity Rule Register) — vẫn cần thêm quyết định về `Cited_Condition_Evidence_ID` cardinality và về việc phê duyệt các trường `[ĐỀ XUẤT — CHƯA DUYỆT]`.
- **Gate kế tiếp có gần hơn không:** Không. Đây vẫn là tài liệu Supporting; không có artifact bắt buộc nào của Gate 2/Gate 3 được tạo ra, và không trạng thái Gate nào thay đổi.
