# Paper 2 / Gate 2–3 — Định hướng nghiên cứu hiện hành
**Ngày:** 15/09/2026 | **Trạng thái:** CURRENT — tài liệu định hướng làm việc, không phải Gate Decision Record
**Nguồn tổng hợp:**
- `03_OUTPUTS/05_PAPER_2_TRACEABILITY/` — `README_CURRENT.md`, `00_CONSOLIDATION_PLAN.md`, `00_BIBLIOGRAPHIC_VERIFICATION.md`, `06_TARGETED_GAP_AUDIT.md`, `07_BORKOWSKI_2026_FULLTEXT_REVIEW.md`, `08_CORRECTION_PASS_SUMMARY.md`, `00_CURRENT/G2_ONE_PAGE_TRACEABILITY_DRAFT_20260914.md`
- `01_CURRENT_CONTROL/` — `CURRENT_STATUS_AND_NEXT_DIRECTION.md` (v2.4), `EVIDENCE_GATES_v2.1.md` (v2.4), `RQ_WP_CHAPTER_PAPER_GATE_MATRIX_v2.1.md` (v2.4), `RESEARCH_DIRECTION_AND_SCOPE.md` (v2.3), `TERMINOLOGY_CONTROL_CURRENT.md` (v2.3)

Tài liệu này **không** tạo RQ mới, **không** mở rộng phạm vi, **không** tìm literature mới, **không** thay đổi các source-of-truth khác. Nó chỉ tổng hợp trạng thái hiện có thành một điểm tham chiếu duy nhất cho Gate 2–3.

---

## 1. Research routing

| Trục | Giá trị |
|---|---|
| RQ | RQ2 |
| WP | WP2 |
| Chương | Chương 5 |
| Paper | Paper 2 |
| Gate 2 | BIM information readiness / governance — `OPEN — LITERATURE BOUNDARY CLOSED, SPECIFICATION NOT YET FROZEN` |
| Gate 3 | BIM binding + evidence integration + deterministic traceability validation — `OPEN — NOT IMPLEMENTED, NOT VALIDATED, NOT OFFICIALLY PASSED`; execution `EXECUTION-NOT-OPEN` cho tới khi Gate 2 được baseline và chấp thuận |

Nguồn: `EVIDENCE_GATES_v2.1.md` v2.4, `RQ_WP_CHAPTER_PAPER_GATE_MATRIX_v2.1.md` v2.4 §1, §7.

---

## 2. Research chain

```text
Sensor_ID
→ BIM_GUID / governed BIM component identity
→ Condition_Evidence_ID
→ Inspection_Record_ID
```

`Action_Status` là **điểm cuối canonical của chuỗi định danh** theo `TERMINOLOGY_CONTROL_CURRENT.md` (§5–6) và `CURRENT_STATUS_AND_NEXT_DIRECTION.md` §2, nhưng đối với Paper 2 nó chỉ đóng vai trò **downstream/supporting**: một thuộc tính tại-thời-điểm-truy-vấn gắn với một `Inspection_Record_ID`, không bao giờ là khóa tra cứu, không phải trọng tâm đóng góp. Trọng tâm đóng góp của Paper 2 là ba mắt xích đầu:

```text
Condition Evidence → verified BIM/IFC component → accountable Inspection Record
```

`Asset_ID`, `Model_Version_ID`, `Action_Record_ID`, `Workflow_Status`, `Status_Event` vẫn là **noncanonical implementation proposals**, không thay thế hay mở rộng chuỗi canonical trừ khi được phê duyệt riêng (`EVIDENCE_GATES_v2.1.md` G2 hàng "Identifier governance"; `TERMINOLOGY_CONTROL_CURRENT.md` §6).

---

## 3. Literature conclusion hiện hành

### 3.1 Những gì literature đã làm — Paper 2 KHÔNG được claim là mới

Đã thiết lập vững chắc trong corpus 12-paper targeted review + CORE-5 (`06_TARGETED_GAP_AUDIT.md` Part 1, "Prior-art findings"):

- Xác minh/trích xuất định danh cấu kiện từ nguồn BIM/IFC thật (GAP-A — ESTABLISHED, ≥6 paper, ≥3 kỹ thuật khác nhau).
- Sensor→BIM linkage (đã biết từ review CORE-5 trước, tái xác nhận qua MULTI_02, G1_01).
- BIM→inspection/maintenance linkage (G3_02 Wan et al. — hệ thống BMS cầu dây văng triển khai thật 2019; G2_01 SeeBridge).
- IFC GlobalId làm định danh SHACL `focusNode` / khóa tra cứu (G2_02, G2_03, MULTI_02, MULTI_03, G1_02).
- SHACL/RDF-based semantic-integrity validation cho ifcOWL/LBD — "heavily worked, not a gap" (G2_02, G2_03, G2_04, MULTI_01).
- Competency-question methodology (MULTI_02, và đặc biệt G1_02 Borkowski — 8 CQ mapped tường minh).
- Deterministic/expected-answer pass-fail validation nói chung (GAP-G — ESTABLISHED qua ≥4 kỹ thuật: CQ, SHACL violation-count, conformance-error taxonomy, ground-truth comparison).
- Ontology không phải công cụ triển khai bắt buộc — corpus chứng minh ≥3 họ công cụ khả thi: IFC/Pset thuần (G3_02), rule-engine/SWRL (G2_05), SHACL/RDF/OWL (G2_02–04, G1_02).

**Borkowski et al. (2026)** — đã đọc full text (26/26 trang, xem §3.2 bên dưới) — thu hẹp thêm phạm vi novelty được phép claim: ý tưởng "identity persistence across life-cycle phases, giải quyết bằng một định danh bền vững độc lập với GUID" **không còn là claim mới ở dạng khái quát**, vì Borkowski đã nêu tên, đề xuất cơ chế (DOLCE endurant/perdurant), và kiểm chứng (ở quy mô nhỏ, thủ công) chính xác vấn đề này, đồng thời tự nhận là ontology xây dựng đầu tiên làm điều đó.

### 3.2 Borkowski et al. (2026) — ranh giới đã xác nhận full text

Nguồn: `07_BORKOWSKI_2026_FULLTEXT_REVIEW.md`. Full text đã đọc trọn vẹn (item Zotero `JSYCVGH9`/attachment `CVGD2BLV`; item `NQ3KGDWN` là bản trùng lặp chỉ có metadata, không có PDF — vấn đề này đã được phát hiện và giải quyết, không sửa metadata Zotero).

- **Ngưỡng đe dọa novelty: HIGH nhưng hẹp**, chỉ nhắm vào sub-claim identity-governance/GAP-B, **không** lan sang 6/8 thành phần đóng góp còn lại của Paper 2 (evidence provenance vượt quá bare backlink, evidence validity/applicability, accountable inspection record, forward/reverse cross-system traceability, deterministic multi-hop integrity validation, deliberate identity-mapping negative testing).
- Cơ chế Borkowski: định danh mới (URI, `BuildingElement` như DOLCE endurant) độc lập GUID, GUID bị hạ cấp thành thuộc tính backlink cấp-phase. Khớp identity giữa các phase là **thủ công** ("expert knowledge or heuristics"), không tự động, không kiểm chứng bằng ground truth.
- Chỉ có **một** negative test duy nhất, ở mức schema/axiom (disjointness giữa `BuildingElement` và `LifecyclePhase`) — **không** kiểm thử ở mức identity-mapping (không có case orphan/duplicate/wrong/stale/conflicting).
- Không có `Condition_Evidence_ID` hay `Inspection_Record_ID` như thực thể first-class có accountability field — sự kiện "crack" và "inspection" chỉ là thay đổi giá trị thuộc tính trên endurant, không có performer/reviewer/status.
- Không có khái niệm evidence validity/applicability (đã kiểm tra hệ thống, xác nhận vắng mặt hoàn toàn — không nhầm với model/version context).
- Có tuyên bố định hướng rõ ràng (Sec. 5.1): "Sensor readings, inspection results, and maintenance events can then refer to one and the same persistent element" — xác nhận đây là **tầm nhìn bổ sung, chưa triển khai**, không phải phần đã làm.

**Ghi chú lưu ý:** Xác minh bibliographic (`00_BIBLIOGRAPHIC_VERIFICATION.md`) phát hiện một xung đột tác giả cho CORE-01 (Jäkel et al. — Zotero thiếu tác giả đầu Jan-Iwo Jäkel so với PDF); đã ghi nhận, chưa sửa Zotero. Không liên quan trực tiếp Borkowski nhưng là một cảnh báo chung về việc luôn đối chiếu PDF thay vì chỉ dùng metadata Zotero.

### 3.3 Ba khoảng trống còn bảo vệ được (surviving gaps)

**a. Accountable BIM-linked inspection record (GAP-E)** — khoảng trống mạnh nhất, được xác nhận độc lập bởi cả một hệ thống triển khai thực tế (G3_02 Wan et al., BMS cầu dây văng 2019, có bước review thủ công nhưng chưa hình thức hóa) và một ontology 2026 nghiêm ngặt (Borkowski) giải quyết vấn đề liền kề nhưng **không có một trường accountability nào**. Không claim actor provenance tự thân là mới — PAV/PROV-O (G3_01 Ciccarese) đã cung cấp vocabulary tái dùng được (provenance nguồn/xử lý/tác nhân người) nhưng chưa từng áp dụng cho BIM-anchored inspection record.

**b. Condition-evidence governance: provenance + validity/applicability + model/version context (GAP-C, GAP-D)** — không paper nào trong corpus kết hợp đủ bốn loại provenance (nguồn, đo lường, xử lý, tác nhân người) neo vào một identity BIM bền vững, độc lập-GUID. Đặc biệt GAP-D (evidence validity/applicability) là **NOT_ESTABLISHED_IN_TARGETED_CORPUS với độ tin cậy full-text**, kể cả sau khi đọc Borkowski — không paper nào có valid-time bound + điều kiện áp dụng (protocol/config/operating-condition) + quy tắc supersession tường minh **cho một mẩu evidence**. Tiền lệ gần nhất chỉ là partial: `prov:atTime` (Lorvão Antunes), timestamp trần (Kim et al.), `previousVersion`/`derivedFrom` của PAV (G3_01, tiền lệ mạnh nhất nhưng vẫn thiếu valid-time bound và điều kiện áp dụng).

> **Phân biệt bắt buộc:** `MODEL_VERSION_CONTEXT` (phase/file/revision nào một giá trị thuộc về, ví dụ `precedes`-chain của Borkowski) ≠ `EVIDENCE_VALIDITY_APPLICABILITY` (dưới điều kiện thu thập/protocol/cấu hình/ngữ cảnh vận hành nào một mẩu evidence còn hợp lệ để tái sử dụng, và nó đã bị supersede chưa). Case-study scope, asset type, sample size, geographical scope **không** tính là evidence validity.

**c. Deterministic multi-hop traceability / invalid-link validation (GAP-F, GAP-H)** — các kỹ thuật đơn lẻ (GUID check, SHACL, missing-link, checksum drift, CQ, pass/fail) đã có sẵn nhưng luôn giới hạn trong một model hoặc một cặp chuyển đổi định dạng của cùng một model. Không paper nào — kể cả Borkowski — kiểm thử forward/reverse traceability và các case invalid (orphan, duplicate, wrong component, stale binding, wrong model revision, conflicting binding, out-of-validity evidence) **xuyên suốt chuỗi cross-system nhiều bước** Sensor_ID → BIM_GUID → Condition_Evidence_ID → Inspection_Record_ID.

---

## 4. Paper 2 contribution hiện hành

**C1 — Verifiable component-level traceability framework.**
Khung tích hợp định danh cấu kiện neo-GUID với condition evidence và inspection record thành một chuỗi cross-system, tường minh, có thể truy vấn: `Sensor_ID → BIM_GUID/governed identity → Condition_Evidence_ID → Inspection_Record_ID`. Không paper nào trong corpus, kể cả Borkowski, kết hợp cả ba loại bản ghi với cross-reference hình thức, khóa trên một identity bền vững. Bao gồm cơ chế identity-linking **tự động hoặc kiểm chứng được** (phân biệt rõ với bước khớp thủ công của Borkowski), tái dùng khung endurant/perdurant của Borkowski như prior art khi hữu ích thay vì phát minh lại.

**C2 — Condition-evidence governance contract.**
Hợp đồng governance tách bạch bốn thành phần: (i) provenance (nguồn/đo lường/xử lý/tác nhân người — domain-adapt từ PAV/PROV-O, không phát minh role taxonomy mới); (ii) evidence validity/applicability (valid-time, protocol/config/operating-condition, supersession — GAP-D, khoảng trống mở thực sự); (iii) model/version context (tách bạch tường minh khỏi (ii)); (iv) inspection-record accountability (performer/reviewer/approver/status/supersession — GAP-E).

**C3 — Reproducible deterministic validation protocol.**
Giao thức kiểm chứng multi-hop forward/reverse với expected-answer xác định, mở rộng các kỹ thuật đơn lẻ đã có (G2_02/G2_03/G2_04/MULTI_01/Borkowski) sang toàn chuỗi, cộng với bộ negative fixture cross-system có chủ đích (orphan, duplicate, wrong component, stale binding, wrong model revision, conflicting binding, out-of-validity evidence) — chưa từng được kiểm thử xuyên suốt chuỗi này trong corpus.

**Không claim mới cho:** sensor→BIM, BIM→inspection, IFC GlobalId, SHACL/RDF validation, competency-question methodology tự thân, ontology tự thân, identity persistence cô lập (đã được Borkowski làm ở quy mô nhỏ/thủ công), deterministic pass/fail validation paradigm tự thân.

---

## 5. Gate 2 cần chứng minh gì

Checklist tổng hợp từ `EVIDENCE_GATES_v2.1.md` G2 table và `G2_ONE_PAGE_TRACEABILITY_DRAFT_20260914.md`:

- **Entities / IDs.** Chuỗi canonical `Sensor_ID → BIM_GUID → Condition_Evidence_ID → Inspection_Record_ID → Action_Status` (Action_Status downstream). Không thay thế/mở rộng bằng các proposal noncanonical (`Asset_ID`, `Model_Version_ID`, `Action_Record_ID`, `Workflow_Status`, `Status_Event`) trừ khi được phê duyệt.
- **Required vs optional fields.** Schema `Inspection_Record` tối thiểu: `Inspection_Record_ID` (required, khóa chính); `Referenced_Component` = (`BIM_GUID`, `Binding_Verification_Status` tại thời điểm inspection — snapshot, không phải tham chiếu sống); `Cited_Condition_Evidence_ID` (1..N, cardinality còn cần quyết định); actor identity; timestamp; finding (tách quan sát khỏi diễn giải); `Inspection_Record_Status` (`DRAFT`/`REVIEWED`/`APPROVED`); reviewer identity+timestamp khi approved; `Action_Status` (chỉ đọc, không phải input truy vấn); `Model_Version_ID` tại thời điểm binding snapshot — **`[ĐỀ XUẤT — CHƯA DUYỆT]`**, noncanonical.
- **Identity governance.** Ba lớp quyết định độc lập: Evidence Qualification (`DRAFT`/`QUALIFIED`/`REJECTED`), Component Selection (`UNRESOLVED`/`MULTI_CANDIDATE`/`HUMAN_SELECTED`), IFC-Binding Verification (`NOT_ASSESSED`/`SUSPECTED_IDENTITY_ANOMALY`/`CANDIDATE_BINDING`/`BLOCKED`/`VERIFIED_BINDING`/`REJECTED_BINDING`). `MULTI_CANDIDATE` là trạng thái cần quản trị, không phải lỗi. `SUSPECTED_IDENTITY_ANOMALY` (duplicate GUID tham số phía Revit) không tự động chuyển thành `REJECTED_BINDING` hay `VERIFIED_BINDING` cho tới khi IfcOpenShell xác nhận trên actual exported IFC.
- **Model/version context.** Phải tách bạch tường minh khỏi evidence validity/applicability (xem §3.3). Chưa có cơ chế CDE/ISO 19650-style revision governance trong thiết kế hiện tại — đây là khoảng trống cần lấp ở Gate 2, không phải ở Gate 3.
- **Provenance.** Nguồn + đo lường + xử lý + tác nhân người, neo vào identity bền vững. Domain-adapt PAV/PROV-O thay vì tự phát minh.
- **Evidence validity/applicability.** Quy tắc tường minh: mỗi `Condition_Evidence_ID` mang `Scope_of_Validity.applicability_set` (ví dụ {campaign_id, evaluation_protocol_id, structural_context}); mọi truy vấn/Inspection_Record trích dẫn phải khai báo `query_context_descriptor` cùng cấu trúc; nếu `query_context_descriptor ∉ applicability_set` → `FAIL: SCOPE_VIOLATION`, không có ngoại lệ ngầm định.
- **Inspection-record accountability.** Trường performer/reviewer/approver/status/supersession như required field trong schema tối thiểu ở trên (xem `Inspection_Record_Status`, reviewer identity+timestamp).
- **Competency questions.** Phải được pre-register và phê duyệt **trước khi build/freeze schema** (`EVIDENCE_GATES_v2.1.md` G2, hàng "Competency questions"). Bộ CQ nháp hiện có (5 câu, `G2_ONE_PAGE...` §11): CQ-1 Forward, CQ-2 Backward (khóa vào `Inspection_Record_ID`, không phải `Action_Status`), CQ-3 Multi-candidate governance, CQ-4 Scope-of-validity, CQ-5 Duplicate-identity negative — mỗi câu có input/expected-result/PASS-rule tường minh nhưng **chưa được review, chưa freeze**.
- **Integrity rules.** Constraint Catalogue theo các họ: identity, relation, chronology, transition, authorization, evidence, closure (`EVIDENCE_GATES_v2.1.md` G2).
- **Gate 2 pass criteria.** G2 Final Decision Register (mọi item FREEZE/FREEZE_PROVISIONALLY/EXPERT_REVIEW_REQUIRED/WAIT_FOR_G1_PAYLOAD/REMOVE có basis+owner+approval); Action-Status-Event ADR; Identifier governance doc; CEI attribute structure (metadata, không phải scalar); CQ đã duyệt; Verification criteria đã duyệt; Constraint Catalogue; Fixture/Oracle Manifest; G2 baseline/sign-off bởi Supervisor.

---

## 6. Gate 3 cần chứng minh gì

Checklist từ `EVIDENCE_GATES_v2.1.md` G3 table:

- **Revit↔IFC binding thực tế.** Audit read-only 718-element ghi nhận 8 cặp duplicate `IFC_GUID` tham số phía Revit, ảnh hưởng 16 ElementIds. Lần chạy `compare_with_ifc_binding` trước đó bị `API_THREAD_TIMEOUT` → binding thật ở trạng thái `BLOCKED/NOT_ASSESSED`, **không phải FAIL đã xác nhận**. Cần chạy lại để có kết quả binding thật (case pilot S4 đề xuất).
- **Forward traceability.** CQ-1: từ `Condition_Evidence_ID` → danh sách component candidate kèm `Binding_Verification_Status`, và danh sách `Inspection_Record_ID` trích dẫn.
- **Reverse traceability.** CQ-2: từ `Inspection_Record_ID` (không phải từ `Action_Status`) → evidence trích dẫn, `Sensor_ID`, campaign/run, protocol, reviewer identity/timestamp, và `Action_Status` hiện tại như một thuộc tính kết quả.
- **Expected-answer tests / exact oracle validation.** Kết quả thực tế (violations/results) phải khớp chính xác với focus IDs/codes/counts đã pre-register — không PASS chỉ vì code chạy thành công.
- **PASS/FAIL criteria.** Tường minh cho từng CQ (xem bảng CQ §5 ở trên); không có ngoại lệ ngầm định, không silent-accept.
- **Negative fixtures bắt buộc:**
  - **Orphan** record.
  - **Duplicate** identity — case S4: một trong 8 cặp duplicate GUID tham số, kỳ vọng cả hai element nhận `SUSPECTED_IDENTITY_ANOMALY`, không tự động promote sang `VERIFIED_BINDING`/`REJECTED_BINDING`.
  - **Wrong component** (mismatched binding).
  - **Stale binding.**
  - **Wrong model revision.**
  - **Conflicting binding.**
  - **Out-of-validity evidence** — case S5 (fixture mô phỏng): `Condition_Evidence_ID` gốc CP3 với `applicability_set` = {CP3, protocol X}, một `query_context_descriptor` cố ý ngoài tập đó, kỳ vọng CQ-4 trả `FAIL: SCOPE_VIOLATION` đúng quy tắc, không PASS sai hoặc bỏ qua kiểm tra.
- **Điều kiện thực thi.** Execution authorization = `EXECUTION-NOT-OPEN` cho tới khi gói Gate 2 được duyệt và baseline. Real Condition_Evidence từ Gate 1 chỉ được dùng sau khi Gate 1 payload được chấp thuận provenance-complete (hiện Gate 1 vẫn `OPEN — PARTIAL EVIDENCE`).

---

## 7. Current technical direction

```text
Revit
→ IFC
→ CDE / model-version context
→ governed BIM component identity
→ Condition Evidence
→ Inspection Record
→ deterministic traceability validation
```

Đóng góp là **INFORMATION MANAGEMENT**, không phải Revit automation hay ontology development. Revit, IFC, Dynamo, Pset, IDS, SQLite và bất kỳ viewer nào là **supporting implementation instrument** — sự hiện diện hay việc chạy được của chúng không phải là novelty và không thể thay thế cho traceability completeness, provenance, integrity validation, human review, hay gate acceptance (`RESEARCH_DIRECTION_AND_SCOPE.md` §3; `TERMINOLOGY_CONTROL_CURRENT.md` "website/viewer (as novelty) — REMOVE"). **Không chạy Graph 02** (`CURRENT_STATUS_AND_NEXT_DIRECTION.md` §6). FEM là **nominal, uncalibrated, reference-only, not used for damage diagnosis** trong toàn bộ luận án, không có RQ/WP/chương/Paper/Gate riêng.

---

## 8. Literature status

**SCOPE-BOUNDED LITERATURE FREEZE.**

Quyết định kiểm soát hiện hành (`README_CURRENT.md`, `CURRENT_STATUS_AND_NEXT_DIRECTION.md` §5) là `CLOSE_SEARCH`/`FULL FREEZE`, đè lên nhãn nội bộ `CONDITIONAL_FREEZE` còn sót trong `08_CORRECTION_PASS_SUMMARY.md` (điều kiện chưa thỏa duy nhất của `CONDITIONAL_FREEZE` là chưa re-check attachment-duplicate của 11/12 paper còn lại theo kiểu vừa phát hiện ở Borkowski — nằm ngoài phạm vi pass sửa lỗi đó, không phải một novelty threat đã biết). Quyết định này **bị giới hạn trong phạm vi corpus đã sàng lọc và đọc full-text** (12-paper targeted review + CORE-5); nó **không** phải tuyên bố toàn bộ literature toàn cầu đã được rà soát cạn kiệt, và **không** cho phép một claim "first/no study worldwide".

Không tiếp tục broad search (Consensus/Perplexity/Elicit), không tiếp tục quét Zotero mở rộng, không mở rộng số lượng trích dẫn vì mục đích tự thân. Corpus hiện có đủ để định vị Paper 2 và thiết kế Gate 2–3.

**Chỉ mở lại literature nếu:**
1. Xuất hiện direct novelty threat mới, cụ thể.
2. Supervisor/reviewer yêu cầu.
3. Cần nguồn cụ thể cho một quyết định phương pháp.
4. Cập nhật trước submission (final pre-submission check).

Diễn đạt an toàn: *"The literature search is frozen within the declared review scope. Further searching is triggered only by a specific evidence need, reviewer request, newly identified direct novelty threat, or final pre-submission verification."* Không dùng diễn đạt tuyệt đối kiểu "no other study exists".

---

## 9. Current status + next actions

| # | Claim | Evidence | Limitation | Next action |
|---|---|---|---|---|
| 1 | Literature đủ để định vị Paper 2 và thiết kế Gate 2–3 | 12-paper targeted review full-text + CORE-5; Borkowski full-text resolved; validity/applicability re-audit hoàn tất | Chưa re-check attachment-duplicate cho 11/12 paper còn lại (nhãn nội bộ `CONDITIONAL_FREEZE`, không phải novelty threat đã biết) | **Freeze Data Dictionary** — khóa entity/field list ở §5 làm cơ sở cho CEI attribute structure và Inspection_Record schema |
| 2 | Gate 2 vẫn `OPEN — SPECIFICATION NOT YET FROZEN` | `EVIDENCE_GATES_v2.1.md` G2 table — mọi hàng đang `OPEN` hoặc `EXECUTION-NOT-OPEN` | CQ và verification criteria nháp (`G2_ONE_PAGE...` v0.2) chưa được review/duyệt; cardinality `Cited_Condition_Evidence_ID` (1..N hay 1..1) chưa quyết | **Freeze Gate 2 criteria** — đưa CQ-1..CQ-5 và bảng trạng thái bản ghi (§5 ở trên) vào bản pre-registration chính thức (Competency Question Register, Integrity Rule Register); giải quyết cardinality và các trường `[ĐỀ XUẤT — CHƯA DUYỆT]` |
| 3 | Tồn tại vấn đề định danh Revit/IFC chưa giải quyết | Audit 718-element: 8 cặp duplicate `IFC_GUID` tham số / 16 ElementIds; `compare_with_ifc_binding` bị `API_THREAD_TIMEOUT` | Binding thật `BLOCKED/NOT_ASSESSED`, chưa phải FAIL đã xác nhận; không được tự suy diễn thành lỗi binding | **Resolve Revit/IFC identity issues** — chạy lại `compare_with_ifc_binding` trên actual exported IFC cho pilot case S4 để xác nhận hoặc bác bỏ `SUSPECTED_IDENTITY_ANOMALY` |
| 4 | Pilot binding chưa được validate | Pilot Run 01/02 (case S1/S2/S3 — multi-candidate tại grid B-5, 2 composite bracing assemblies) | S4/S5 vẫn là đề xuất, chưa chạy; Gate 1 payload vẫn `OPEN — PARTIAL EVIDENCE` nên mọi ví dụ evidence trong pilot vẫn là candidate/draft | **Validate pilot binding** — chạy case S4 (duplicate-GUID disambiguation) và S5 (cross-scope fixture) sau khi CQ được duyệt |
| 5 | Gate 3 execution vẫn `NOT OPEN` | `EVIDENCE_GATES_v2.1.md` G3 — mọi hàng `EXECUTION-NOT-OPEN` cho tới khi Gate 2 baseline được chấp thuận | Không được chạy thử nghiệm Gate 3 trước khi Gate 2 sign-off | **Implement Gate 3 negative tests** — chuẩn bị (không thực thi) bộ fixture orphan/duplicate/wrong-component/stale/wrong-revision/conflicting/out-of-validity theo §6, sẵn sàng chạy ngay khi execution authorization mở |

---

## Kết luận

Hướng nghiên cứu hiện hành của Paper 2 (Gate 2–3) là tích hợp **identity governance + condition-evidence governance + deterministic multi-hop traceability validation** thành một chuỗi thông tin có thể kiểm chứng, không phải phát minh lại từng kỹ thuật thành phần (đã có sẵn trong literature) hay phát triển ontology/tự động hóa Revit. Trọng tâm hành động kế tiếp là kỹ thuật thông tin (Revit → IFC → CDE → governed identity → Condition Evidence → Inspection Record → deterministic validation), không phải mở rộng literature search.
