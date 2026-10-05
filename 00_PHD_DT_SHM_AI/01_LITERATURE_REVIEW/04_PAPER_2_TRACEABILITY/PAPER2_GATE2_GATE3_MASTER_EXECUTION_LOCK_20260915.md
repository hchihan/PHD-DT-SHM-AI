# PAPER 2 / GATE 2–3 — MASTER EXECUTION LOCK
**Ngày:** 15/09/2026 | **Trạng thái:** CURRENT AUTHORITATIVE DOCUMENT cho việc thực thi Gate 2–3 của Paper 2
**Vai trò:** Đây là điểm vào duy nhất cần đọc để hiểu Paper 2 đang nghiên cứu gì, literature đã chứng minh gì, gap còn lại là gì, contribution nào được phép claim, Gate 2/Gate 3 cần đóng bằng gì, và việc tiếp theo là gì. Mọi file phân tích/deep-read khác trong thư mục là **supporting/archive evidence**, không phải nguồn điều hành.

**Nguồn tổng hợp (đã đọc, đối chiếu, giải quyết mâu thuẫn):**
`README_CURRENT.md`, `00_CONSOLIDATION_PLAN.md`, `00_CLEANUP_REPORT.md`, `00_BIBLIOGRAPHIC_VERIFICATION.md`, `06_TARGETED_GAP_AUDIT.md`, `07_BORKOWSKI_2026_FULLTEXT_REVIEW.md`, `08_CORRECTION_PASS_SUMMARY.md`, `00_CURRENT/G2_ONE_PAGE_TRACEABILITY_DRAFT_20260914.md`, và `01_CURRENT_CONTROL/` (`CURRENT_STATUS_AND_NEXT_DIRECTION.md` v2.4, `EVIDENCE_GATES_v2.1.md` v2.4, `RQ_WP_CHAPTER_PAPER_GATE_MATRIX_v2.1.md` v2.4, `RESEARCH_DIRECTION_AND_SCOPE.md` v2.3, `TERMINOLOGY_CONTROL_CURRENT.md` v2.3).

**Source-of-truth rule áp dụng khi mâu thuẫn:** (1) kiến trúc nghiên cứu hiện hành (`01_CURRENT_CONTROL/`) > (2) correction mới nhất đã kiểm chứng full-text > (3) full-text > abstract > metadata > (4) evidence matrix đã sửa > matrix cũ > (5) Borkowski full-text review > mọi bản abstract-only cũ. **Không chọn file chỉ vì Date Modified mới hơn** — xem cảnh báo QC ở cuối file về `00_CLEANUP_REPORT.md`.

---

## 1. Research Position

Paper 2 **không** nghiên cứu "kết nối BIM" nói chung. Paper 2 nghiên cứu **verifiable asset-information traceability**: liên kết có thể kiểm chứng từ Condition Evidence → đúng BIM/IFC component → accountable Inspection Record.

Đóng góp thuộc **Construction Management / Asset Information Management**, không phải mô hình cơ học, thuật toán AI mới, hay ontology engineering. Revit, IFC, CDE, database, RDF, SHACL, IDS... là **công cụ triển khai/kiểm chứng**, không phải nội dung đóng góp.

---

## 2. Literature Review Lock

### 2.1 Literature đã giải quyết — KHÔNG được claim mới

- Sensor → BIM linkage.
- BIM → inspection/maintenance linkage (triển khai thật: G3_02 Wan et al. 2019, BMS cầu dây văng; G2_01 SeeBridge).
- IFC GlobalId usage làm định danh tra cứu/SHACL `focusNode`.
- Ontology-based representation cho quản lý thông tin xây dựng.
- SHACL/RDF-based semantic-integrity validation cho ifcOWL/LBD — "heavily worked, not a gap" (≥4 paper: G2_02, G2_03, G2_04, MULTI_01).
- Competency-question methodology tự thân.
- Deterministic pass/fail validation methodology nói chung (≥4 kỹ thuật độc lập: CQ, SHACL violation-count, conformance-error taxonomy, ground-truth comparison).
- Provenance vocabulary nói chung (PAV/PROV-O đã có sẵn, tái dùng được — G3_01 Ciccarese et al. 2013).
- Persistent identity across lifecycle phases nói chung.

**Borkowski, Jarema, Kładź & Smoliar (2026)** — *Temporally Qualified Building Elements: A DOLCE-Based Ontology for Phase-Dependent Identity and Change Tracking in BIM Models*, Technologies 14(7):413 — đã **FULL-TEXT READ** (26/26 trang, Zotero item `JSYCVGH9`/attachment `CVGD2BLV`; item trùng lặp `NQ3KGDWN` chỉ có metadata, không sửa Zotero).

Đây là **HIGH novelty threat, nhưng hẹp**, chỉ nhắm vào sub-claim **persistent identity / GUID fragmentation across lifecycle phases** (GAP-B). Borkowski đề xuất một URI mới (`BuildingElement` như DOLCE endurant) độc lập GUID, giáng GUID xuống thành thuộc tính backlink cấp-phase, kiểm chứng bằng reasoner + 8 competency question trên case study 3-file Revit/IFC thật (quy mô nhỏ). Tự nhận là ontology xây dựng đầu tiên làm điều này.

**Không được claim identity persistence riêng lẻ là novelty.** Nhưng Borkowski **không** đụng đến 6/8 thành phần đóng góp còn lại của Paper 2: identity-linking của Borkowski là **thủ công** (không tự động/không kiểm chứng deterministic); không có `Condition_Evidence_ID`/`Inspection_Record_ID` first-class với accountability field nào; chỉ một negative test duy nhất ở mức schema-axiom (không phải identity-mapping); không có khái niệm evidence validity/applicability; không có forward/reverse traceability xuyên nhiều loại bản ghi; không có CDE/ISO 19650-style model-revision governance.

### 2.2 Surviving research gaps

**GAP 1 — Accountable BIM-linked Inspection Record.** Trường explicit, queryable: performer, reviewer, approver, status, timestamp, supersession/history. Xác nhận vắng mặt độc lập bởi cả hệ thống triển khai thật (G3_02 Wan et al., có bước review thủ công nhưng chưa hình thức hóa thành field) và ontology 2026 nghiêm ngặt (Borkowski, zero accountability field). Không claim actor provenance tự thân là mới — PAV/PROV-O cung cấp vocabulary tái dùng được, chưa từng áp dụng cho BIM-anchored inspection record.

**GAP 2 — Condition Evidence Governance.** Gồm: source provenance, measurement provenance, processing/evaluation provenance, human provenance + **EVIDENCE VALIDITY/APPLICABILITY** + **MODEL/IFC VERSION CONTEXT**.

> **Phân biệt bắt buộc:** `MODEL_VERSION_CONTEXT` ≠ `EVIDENCE_VALIDITY_APPLICABILITY`.
> Validity/applicability phải trả lời: evidence này hợp lệ khi nào? trong campaign/protocol nào? sensor configuration nào? evaluation protocol nào? ngữ cảnh operational nào? đối với model revision nào? đã bị supersede chưa?
> Không dùng case-study scope, asset type, sample size, geographical scope, hay ontology scope làm validity scope.

Xác nhận full-text (tất cả 12 paper đã đọc, kể cả Borkowski): **NOT_ESTABLISHED_IN_TARGETED_CORPUS** cho evidence validity/applicability theo định nghĩa nghiêm ngặt. Tiền lệ partial gần nhất: `pav:previousVersion`/`derivedFrom` (G3_01, mạnh nhất nhưng thiếu valid-time bound + điều kiện áp dụng), `prov:atTime` (MULTI_02), timestamp trần (MULTI_03). Borkowski's `precedes`-phase-ordering là `MODEL_VERSION_CONTEXT`, không phải validity rule — đã kiểm tra và xác nhận tách biệt.

**GAP 3 — Multi-hop deterministic integrity validation.** Literature có kỹ thuật riêng lẻ (GUID check, SHACL, missing-link, checksum drift, CQ, pass/fail) nhưng luôn giới hạn trong một model hoặc một cặp chuyển đổi định dạng của cùng model. Khoảng trống là kiểm chứng **xuyên suốt toàn chuỗi** `Sensor_ID → BIM_GUID → Condition_Evidence_ID → Inspection_Record_ID` với forward, reverse, expected answer, PASS/FAIL, negative fixtures — chưa từng thực hiện trong corpus, kể cả Borkowski (chỉ một negative test ở mức schema-axiom).

### 2.3 Novelty check 16/09/2026

Kiểm tra có giới hạn 4 bài (Gragnaniello 2024, Mariniello 2025, García 2026, Bellon 2025 — chi tiết `01_EVIDENCE/10_NOVELTY_CHECK_SUMMARY_20260916.md`). García 2026 (Applied Sciences 16, 2562) — **HIGH threat hẹp**: accountable-record pattern (performer/reviewer/approver/status/supersession) đã triển khai thực nghiệm cho quyết định publish/hold mô hình BIM/CDE, buộc GAP 1/C2 phải thu hẹp câu chữ (novelty chỉ còn khi neo trên `Condition_Evidence_ID` từ sensor, García không có sensor data). Mariniello 2025 — MEDIUM (một phần C3, không đe dọa C1 do thiếu BIM identity xác minh). Gragnaniello 2024 — LOW. Bellon 2025 (Automation in Construction 174, 106157) — chỉ đọc được ABSTRACT_ONLY (ScienceDirect chặn CAPTCHA); trùng chủ đề "inspection representation" mạnh nhất, **rủi ro chưa đóng**, cần đọc toàn văn trước freeze cuối. GAP 2/GAP-D (evidence validity/applicability) và C1/C3 cấu trúc: **GIỮ NGUYÊN**. Trạng thái: **SCOPE-BOUNDED FREEZE có điều kiện**, chưa FULL_FREEZE.

---

## 3. Paper 2 Contributions — LOCK

**C1 — Verifiable Component-Level Traceability Framework.**
`Sensor_ID → governed BIM/IFC identity → Condition_Evidence_ID → Inspection_Record_ID`, tích hợp cả ba loại bản ghi với cross-reference hình thức, khóa trên identity bền vững — không paper nào trong corpus làm điều này. Bao gồm cơ chế identity-linking tự động/kiểm chứng được (phân biệt với bước khớp thủ công của Borkowski; tái dùng khung endurant/perdurant của Borkowski như prior art khi hữu ích, không phát minh lại).

**C2 — Condition-Evidence Governance Contract.**
Provenance (nguồn/đo lường/xử lý/tác nhân người, domain-adapt PAV/PROV-O) + validity/applicability (GAP-D, khoảng trống mở thực sự) + model/version context (tách bạch tường minh) + accountable inspection record (GAP-E).

**C3 — Reproducible Deterministic Validation Protocol.**
Forward query + reverse query + expected answer định trước + PASS/FAIL tường minh + negative fixture cố ý (invalid-link), mở rộng kỹ thuật đơn lẻ đã có sang toàn chuỗi cross-system.

**Không tạo contribution thứ 4.**

---

## 4. Literature Freeze

**SCOPE-BOUNDED LITERATURE FREEZE.**

Quyết định kiểm soát (`README_CURRENT.md`, `CURRENT_STATUS_AND_NEXT_DIRECTION.md` §5): `CLOSE_SEARCH`/`FULL FREEZE`, đè lên nhãn nội bộ `CONDITIONAL_FREEZE` còn sót trong `08_CORRECTION_PASS_SUMMARY.md` (điều kiện chưa thỏa duy nhất là chưa re-check attachment-duplicate kiểu Borkowski cho 11/12 paper còn lại — nằm ngoài phạm vi pass sửa lỗi đó, không phải một novelty threat đã biết).

Broad literature search: **STOPPED**. Không tiếp tục Consensus broad search, Perplexity broad search, Elicit broad search, open-ended Zotero scanning, hay mở rộng số trích dẫn vì mục đích tự thân.

**Chỉ reopen nếu:** (1) direct novelty threat cụ thể; (2) supervisor/reviewer yêu cầu; (3) cần evidence cho một quyết định phương pháp cụ thể; (4) final pre-submission update.

**Không claim:** "no study worldwide" / "first study" tuyệt đối. Diễn đạt an toàn: quyết định bị giới hạn trong phạm vi corpus đã sàng lọc và đọc full-text.

---

## 5. Gate 2 — Exact Objective

Gate 2 phải trả lời: *"Thông tin có được tổ chức đủ rõ, định danh đủ chắc, và governance đủ chặt để condition evidence có thể được gắn vào đúng BIM component và Inspection Record hay chưa?"*

**Gate 2 KHÔNG cần chứng minh system chạy end-to-end** — đó là Gate 3.

**Trạng thái hiện tại (`EVIDENCE_GATES_v2.1.md` v2.4):** `OPEN — LITERATURE BOUNDARY CLOSED, SPECIFICATION NOT YET FROZEN`.

---

## 6. Gate 2 — Required Artefacts

| # | Artefact | Purpose | Current status | Missing evidence | Next action |
|---|---|---|---|---|---|
| 1 | Data Dictionary | Định nghĩa field/entity thống nhất | Chưa tồn tại như artefact riêng; rải rác trong G2_ONE_PAGE draft §10 | Bản pre-registration chính thức | Trích xuất và khóa từ §7 dưới đây |
| 2 | Information / ER model | Sơ đồ quan hệ entity tối thiểu | Nháp trong §7 dưới đây, chưa duyệt | Diagram/DB schema chính thức | Duyệt entity list §7, dựng ER diagram |
| 3 | Identifier Governance | Quy tắc định danh, trạng thái binding | Nháp trong G2_ONE_PAGE §2–§5 (3 lớp quyết định độc lập) | Phê duyệt, đưa vào control doc chính thức | Đưa vào Constraint Catalogue |
| 4 | Required / Optional fields | Trường bắt buộc theo từng entity | Nháp cho `Inspection_Record` (G2_ONE_PAGE §10); chưa có cho các entity khác | Bảng đầy đủ cho Sensor/BIM Component/Condition Evidence/Model Version | Mở rộng bảng §7 dưới đây cho mọi entity |
| 5 | Condition Evidence Contract | Metadata bắt buộc của Condition_Evidence_ID | Khung khái niệm có (§9 dưới đây); chưa formalize thành schema | Schema chính thức + liên kết WP1→WP2 | Formalize theo `CURRENT_STATUS_AND_NEXT_DIRECTION.md` §4 |
| 6 | Inspection Record schema | Schema tối thiểu | **Có** — G2_ONE_PAGE §10 (chưa duyệt) | Review + freeze | Đưa vào bản pre-registration |
| 7 | Accountability fields | performer/reviewer/approver/status/supersession | Có trong Inspection Record schema nháp | Phê duyệt cardinality, quy tắc supersession | Duyệt cùng mục 6 |
| 8 | Model/version-context definition | Định nghĩa tách bạch với evidence validity | Đã định nghĩa khái niệm (§2.2 GAP 2 ở trên), chưa formalize thành field | Field chính thức (`Model_Version_ID` hiện là `[ĐỀ XUẤT — CHƯA DUYỆT]`, noncanonical) | Quyết định phạm vi, phê duyệt hoặc bác bỏ |
| 9 | Evidence-validity/applicability definition | Quy tắc `applicability_set`/`query_context_descriptor` | **Có quy tắc tường minh** — G2_ONE_PAGE §7 | Review + freeze; chưa có case thật (chỉ có fixture mô phỏng S5) | Đưa vào Integrity Rule Register |
| 10 | Competency Question Register | Bộ CQ pre-registered | Nháp 5 CQ — G2_ONE_PAGE §11 (chưa duyệt) | Supervisor review + approval trước khi build schema | Xem §11 dưới đây |
| 11 | Integrity Rule Register | Constraint catalogue | Chưa tồn tại như artefact riêng; các họ ràng buộc được liệt kê trong `EVIDENCE_GATES_v2.1.md` G2 | Catalogue đầy đủ (identity/relation/chronology/transition/authorization/evidence/closure) | Soạn catalogue từ danh sách CQ + negative fixture |
| 12 | Expected-answer / Fixture manifest | Input/expected/PASS rule cho từng test | Nháp cho CQ-1..CQ-5 (G2_ONE_PAGE §11); 2 pilot case đề xuất S4/S5 chưa chạy | Manifest hoàn chỉnh, machine-readable | Chạy S4/S5, mở rộng cho các negative fixture còn lại (§16) |
| 13 | Gate 2 PASS criteria | Tiêu chí đóng gate | Định nghĩa ở §12 dưới đây | Sign-off Supervisor | Hoàn tất mục 1–12 rồi trình duyệt |

---

## 7. Gate 2 — Data Model (entity tối thiểu)

Không mở ontology phức tạp. Chỉ thêm entity nếu literature hoặc research objective yêu cầu.

| Entity | Primary ID | Foreign/reference ID | Required fields (nháp) | Optional / noncanonical |
|---|---|---|---|---|
| **Sensor** | `Sensor_ID` | — | vị trí, kênh, trục, sampling (theo `SENSOR_METADATA_REGISTER.csv`, thuộc Gate 1) | — |
| **BIM Component** | `BIM_GUID` (governed identity) | — | `Binding_Verification_Status` (`NOT_ASSESSED`/`SUSPECTED_IDENTITY_ANOMALY`/`CANDIDATE_BINDING`/`BLOCKED`/`VERIFIED_BINDING`/`REJECTED_BINDING`); `Component_Selection_Status` (`UNRESOLVED`/`MULTI_CANDIDATE`/`HUMAN_SELECTED`) | `Model_Version_ID` — `[ĐỀ XUẤT — CHƯA DUYỆT]` |
| **Condition Evidence** | `Condition_Evidence_ID` | `Sensor_ID`, `BIM_GUID` (qua binding) | source/measurement/processing/actor provenance; `Scope_of_Validity.applicability_set`; `Evidence_Qualification_Status` (`DRAFT`/`QUALIFIED`/`REJECTED`) | model confidence, run/fold variability (CEI metadata — không scalar) |
| **Inspection Record** | `Inspection_Record_ID` | `Referenced_Component` (`BIM_GUID` + `Binding_Verification_Status` snapshot); `Cited_Condition_Evidence_ID` (1..N — cardinality chưa quyết) | inspector identity; timestamp; finding (tách quan sát/diễn giải); `Inspection_Record_Status` (`DRAFT`/`REVIEWED`/`APPROVED`); reviewer identity+timestamp khi approved | `Model_Version_ID` tại thời điểm binding snapshot — `[ĐỀ XUẤT — CHƯA DUYỆT]` |
| **Model / Information Version** | (chưa formalize — candidate: `Model_Version_ID`) | — | — | Toàn bộ entity này hiện là `[ĐỀ XUẤT — CHƯA DUYỆT]`, noncanonical theo `TERMINOLOGY_CONTROL_CURRENT.md` §6 |
| **Action Status** (supporting, không phải core) | — (là thuộc tính của `Inspection_Record_ID`, không phải khóa tra cứu độc lập) | `Inspection_Record_ID` | `OPEN`/`IN_PROGRESS`/`CLOSED`/`REOPENED` | Không bao giờ là input của truy vấn ngược |

---

## 8. Gate 2 — Identity Governance

Paper 2 **không** nghiên cứu universal persistent identity (đó là điều Borkowski đang làm, ở mức ontology). Paper 2 chỉ cần: **governed BIM/IFC identity BOUND TO một model/IFC version đã khai báo**.

Phân biệt bắt buộc bốn trạng thái:
- **identifier present** — Revit-side parameter tồn tại, chưa kiểm tra.
- **identifier candidate** — có candidate binding, chưa xác minh.
- **identifier verified** — `VERIFIED_BINDING`, đã đối chiếu actual exported IFC GlobalId qua IfcOpenShell.
- **identifier conflicting** — `SUSPECTED_IDENTITY_ANOMALY` (duplicate Revit-side GUID tham số) hoặc `REJECTED_BINDING` (đã xác nhận sai qua actual IFC).

Bám vào **actual Revit / actual exported IFC**, không dựa mặc định vào tham số phía Revit (Autodesk xác nhận exporter có thể tự sinh GUID khác khi phát hiện trùng). **Không claim giải quyết toàn bộ lifecycle identity problem** — đó là claim của Borkowski (một phần), không phải của Paper 2.

---

## 9. Gate 2 — Condition Evidence Contract

Kết nối trực tiếp Gate 1 → Gate 2 (`CURRENT_STATUS_AND_NEXT_DIRECTION.md` §4, WP1→WP2 Handover). `Condition_Evidence_ID` phải mang đủ metadata để trả lời:

- Evidence này đến từ đâu? Sensor nào? Campaign/run nào (CP1/CP2/CP3, IT-01..IT-06)?
- Protocol/evaluation configuration nào?
- Kết quả gì? Variability/confidence gì (SD_fold, SD_seed)?
- Scope of validity là gì (`applicability_set`)?
- Model/context nào được phép sử dụng?

**Không biến CEI thành damage score. Không tạo complex Health Index.** CEI là first-class metadata attribute, không phải scalar (`RQ_WP_CHAPTER_PAPER_GATE_MATRIX_v2.1.md` §6 quy tắc 3).

**Ràng buộc từ Gate 1 (xem §22 QC bên dưới về trạng thái Gate 1):** cho tới khi G1 có sign-off chính thức, mọi record bắt nguồn từ Paper 1 chỉ được dùng ở Gate 2–3 như `CANDIDATE`/`DRAFT` cho mục đích đặc tả và thiết kế fixture — chưa có handoff được chấp thuận.

---

## 10. Gate 2 — Inspection Record

Inspection Record phải là **first-class accountable record**. Tối thiểu (đã có trong nháp `G2_ONE_PAGE_TRACEABILITY_DRAFT_20260914.md` §10, chưa duyệt):

`Inspection_Record_ID` · `Referenced_Component` (snapshot BIM_GUID + Binding_Verification_Status) · `Cited_Condition_Evidence_ID` (1..N) · performer (inspector identity) · timestamp · finding (tách biệt quan sát khỏi diễn giải) · reviewer · `Inspection_Record_Status` (approval/status) · supersession/history · `Model_Version_ID` (noncanonical, chờ duyệt).

**Phân biệt bắt buộc:** observation/finding ≠ engineering diagnosis. **Human-in-the-loop bắt buộc** — không có tự động hóa quyết định.

---

## 11. Gate 2 — Competency Questions

Rà lại toàn bộ CQ nháp (`G2_ONE_PAGE_TRACEABILITY_DRAFT_20260914.md` §11). Giữ 5 CQ trực tiếp kiểm chứng RQ2:

| CQ | Input | Expected answer | PASS rule |
|---|---|---|---|
| **CQ-1 Forward** | `Condition_Evidence_ID` | Danh sách BIM component candidate kèm `Binding_Verification_Status`; danh sách `Inspection_Record_ID` trích dẫn | Tập trả về khớp chính xác fixture; không candidate hiển thị trạng thái cao hơn trạng thái đã khai báo |
| **CQ-2 Reverse** | `Inspection_Record_ID` (không phải `Action_Status`) | `Condition_Evidence_ID`, `Sensor_ID`, campaign/run, protocol, reviewer identity/timestamp, `Action_Status` hiện tại (chỉ đọc) | Mọi trường khớp fixture; nếu ID không tồn tại → `NOT_FOUND` tường minh |
| **CQ-3 Identity governance** | `Sensor_ID`/vị trí quan trắc | Candidate/verified/conflicting binding, kèm `Component_Selection_Status` | Không tự động collapse `MULTI_CANDIDATE` thành `HUMAN_SELECTED` khi chưa có Decision A |
| **CQ-4 Evidence validity** | `Condition_Evidence_ID` + `query_context_descriptor` | `PASS` nếu `query_context_descriptor ∈ applicability_set`; `FAIL: SCOPE_VIOLATION` nếu không | Không có ngoại lệ ngầm định, không silent-accept |
| **CQ-5 Integrity anomaly** | Cặp element có duplicate `IfcGUID` tham số | Cả hai trả `Binding_Verification_Status = SUSPECTED_IDENTITY_ANOMALY` | Không tự động promote sang `VERIFIED_BINDING`/`REJECTED_BINDING` khi binding check `BLOCKED`/`NOT_ASSESSED` |

**Trạng thái:** cả 5 CQ đều DRAFT — chưa được Supervisor review, chưa pre-register chính thức. Theo `EVIDENCE_GATES_v2.1.md` G2, CQ phải được duyệt **trước khi build/freeze schema**.

---

## 12. Gate 2 PASS Criteria (deterministic)

Gate 2 chỉ PASS khi **tất cả** đúng — không dùng câu "framework works":

- [ ] Schema frozen (entity §7).
- [ ] Required/optional fields frozen (bảng §7, §9, §10).
- [ ] Identifier governance frozen (§8).
- [ ] Validity/provenance rules frozen (§9, quy tắc `applicability_set`/`query_context_descriptor`).
- [ ] Inspection accountability frozen (§10).
- [ ] CQ pre-registered và duyệt (§11).
- [ ] Integrity rules (Constraint Catalogue) pre-registered.
- [ ] Expected answers định nghĩa cho từng CQ.
- [ ] Test fixture định nghĩa (bao gồm negative fixtures §16).
- [ ] Không còn unresolved specification conflict (ví dụ: cardinality `Cited_Condition_Evidence_ID`, các trường `[ĐỀ XUẤT — CHƯA DUYỆT]`).

**Trạng thái hiện tại: 0/10 tick.** Gate 2 `OPEN — SPECIFICATION NOT YET FROZEN`.

---

## 13. Gate 3 — Exact Objective

Gate 3 phải trả lời: *"Chuỗi thông tin đã định nghĩa ở Gate 2 có thực sự hoạt động và phát hiện được liên kết sai trên Revit/IFC/evidence data hay không?"* Gate 3 = **implementation evidence**.

**Trạng thái hiện tại:** `OPEN — NOT IMPLEMENTED, NOT VALIDATED, NOT OFFICIALLY PASSED`; execution `EXECUTION-NOT-OPEN` cho tới khi Gate 2 baseline được duyệt (`EVIDENCE_GATES_v2.1.md` v2.4).

---

## 14. Gate 3 — Actual Binding

Trọng tâm: **Revit → actual exported IFC → governed BIM identity.** Không mặc định dựa vào tham số Revit-side; phải kiểm tra actual IFC GlobalId/entity.

**Known issue (xác nhận, chưa xác minh actual binding):** audit read-only 718-element ghi nhận **8 cặp duplicate `IFC_GUID` tham số phía Revit, ảnh hưởng 16 ElementIds**. Lần chạy `compare_with_ifc_binding` bị `API_THREAD_TIMEOUT` → binding thật ở trạng thái `BLOCKED/NOT_ASSESSED`. **Đây hiện chỉ là `SUSPECTED_IDENTITY_ANOMALY`, cho đến khi actual IFC comparison xác nhận** — không được suy diễn thành lỗi binding đã xác nhận.

---

## 15. Gate 3 — Positive Tests

| Test | Input | Expected | Observed | PASS/FAIL |
|---|---|---|---|---|
| Forward traceability | `Condition_Evidence_ID` (CQ-1) | Danh sách component + Inspection Record | Chưa chạy | — chưa thực thi (EXECUTION-NOT-OPEN) |
| Reverse traceability | `Inspection_Record_ID` (CQ-2) | Evidence + Sensor + provenance | Chưa chạy | — |
| Provenance recovery | `Condition_Evidence_ID` | Source/measurement/processing/actor | Chưa chạy | — |
| Model-version recovery | `Condition_Evidence_ID`/`Inspection_Record_ID` | Model/context tại thời điểm binding | Chưa chạy | — |
| Validity check | `Condition_Evidence_ID` + `query_context_descriptor` (CQ-4) | PASS/FAIL SCOPE_VIOLATION | Chỉ có fixture mô phỏng S5, chưa chạy | — |
| Inspection accountability recovery | `Inspection_Record_ID` | performer/reviewer/status | Chưa chạy | — |

Tất cả positive test **chưa thực thi** — nằm dưới execution authorization `EXECUTION-NOT-OPEN`.

---

## 16. Gate 3 — Negative Fixtures (bắt buộc)

| Fixture | Trạng thái chuẩn bị | Ghi chú |
|---|---|---|
| Orphan record | Chưa chuẩn bị | — |
| Duplicate identity | **Case S4 đề xuất** (G2_ONE_PAGE §9) — dựa trên 1 trong 8 cặp duplicate GUID thật | Chưa chạy; cần `compare_with_ifc_binding` không timeout |
| Wrong component | Chưa chuẩn bị | — |
| Wrong GUID | Chưa chuẩn bị | — |
| Stale binding | Chưa chuẩn bị | — |
| Wrong model revision | Chưa chuẩn bị | — |
| Conflicting binding | Chưa chuẩn bị | — |
| Missing target | Chưa chuẩn bị | — |
| Out-of-validity evidence | **Case S5 đề xuất** (G2_ONE_PAGE §9) — fixture mô phỏng, dựa trên CP3/SD_fold=0.139 làm giá trị ví dụ (không phải payload đã accept) | Chưa chạy |

**Không coi sensor anomaly hay damage case là invalid-link test** — đó là nội dung của lớp evidence khác (laboratory evidence), không phải integrity test của lớp information-traceability.

---

## 17. CDE Role

CDE chỉ là **SUPPORTING governance context**. Dùng cho: model revision, information status, approval/published state, superseded/current model, information provenance. **Không biến Paper 2 thành nghiên cứu ISO 19650/CDE. Không cần xây CDE platform.**

---

## 18. Technical Direction

```text
Revit
→ IFC
→ CDE/model-version context
→ governed BIM component identity
→ Condition Evidence
→ Inspection Record
→ deterministic validation
```

Đóng góp là **INFORMATION MANAGEMENT**, không phải Revit automation, IFC exporter, database engineering, ontology development, hay dashboard/software. Instrument boundary: Revit, IFC, Dynamo, Pset, IDS, SQLite, viewer là công cụ triển khai hỗ trợ, sự hiện diện/chạy được của chúng không phải novelty (`RESEARCH_DIRECTION_AND_SCOPE.md` §3). **Không chạy Graph 02** (`CURRENT_STATUS_AND_NEXT_DIRECTION.md` §6).

---

## 19. Current Technical Evidence

| Hạng mục | Trạng thái | Nguồn |
|---|---|---|
| Model identity / element inventory | **CONFIRMED** — audit 718-element (read-only) | `G2_ONE_PAGE_TRACEABILITY_DRAFT_20260914.md` §5, §8 |
| Duplicate GUID anomalies | **CONFIRMED (dữ liệu thật)** — 8 cặp duplicate Revit-side `IFC_GUID`, 16 ElementIds | như trên |
| Actual Revit↔IFC binding comparison | **BLOCKED** — `compare_with_ifc_binding` gặp `API_THREAD_TIMEOUT`, chưa có kết quả | như trên |
| Binding status của các element duplicate | **SUSPECTED** — `SUSPECTED_IDENTITY_ANOMALY`, không phải `REJECTED_BINDING` đã xác nhận | như trên |
| Pilot elements (multi-candidate) | **CONFIRMED (dữ liệu thật)** — Pilot Run 01/02, case S2 (cột–rafter tại grid B-5), S3 (2 composite bracing assemblies) | như trên |
| Pilot case S4 (duplicate-GUID disambiguation) | **NOT TESTED** — đề xuất, chưa chạy | như trên |
| Pilot case S5 (cross-scope fixture) | **NOT TESTED** — fixture mô phỏng, chưa chạy | như trên |
| Level_Name issue | **EVIDENCE IS CURRENTLY INSUFFICIENT** — không tìm thấy trong tài liệu đã rà soát | — |
| "Revit Evidence Bridge" | **EVIDENCE IS CURRENTLY INSUFFICIENT** — không tìm thấy trong tài liệu đã rà soát | — |
| IFC_GUID coverage tổng thể (% element có GUID hợp lệ) | **EVIDENCE IS CURRENTLY INSUFFICIENT** — chỉ có số liệu duplicate, không có coverage tổng | — |

**Không nâng status nếu evidence chưa đủ** — hai hạng mục cuối cùng chưa có bằng chứng trong thư mục đã rà soát và được ghi nhận đúng như vậy thay vì suy diễn.

---

## 20. Execution Roadmap

```text
STEP 1  Freeze Data Dictionary (§7)
STEP 2  Freeze Condition Evidence Contract (§9) + Inspection Record schema (§10)
STEP 3  Freeze CQ (§11) + Integrity Rules + PASS criteria (§12)
        → GATE 2 SPECIFICATION FREEZE
STEP 4  Resolve Revit native-level / identity metadata (§8, §14)
STEP 5  Verify actual Revit↔IFC binding trên pilot + known anomaly elements
        (chạy lại compare_with_ifc_binding không timeout, cho 8 cặp duplicate)
STEP 6  Create end-to-end valid scenarios (positive tests §15)
STEP 7  Execute negative fixtures (§16), bắt đầu từ S4/S5 đã có đề xuất
STEP 8  Produce Gate 3 evidence package
```

Không thêm infrastructure nếu không phục vụ trực tiếp một bước trên.

---

## 21. Claim → Evidence → Limitation → Next Action (bảng điều hành chính)

| Claim | Evidence hiện có | Limitation | Next action bắt buộc | Gate | Status |
|---|---|---|---|---|---|
| Literature đủ để định vị Paper 2 và thiết kế Gate 2–3 | 12-paper targeted review full-text + CORE-5; Borkowski full-text resolved; validity/applicability re-audit hoàn tất | Chưa re-check attachment-duplicate cho 11/12 paper còn lại (nhãn nội bộ `CONDITIONAL_FREEZE`, không phải novelty threat đã biết) | Không hành động — chấp nhận `SCOPE-BOUNDED FREEZE` | — | LOCKED |
| Borkowski (2026) đã được xử lý đầy đủ | Full-text review 26/26 trang; ranh giới novelty đã xác nhận, hẹp vào GAP-B | Review bị giới hạn bởi nội dung đã công bố; không kiểm chứng được deployability quy mô lớn | Không hành động thêm trừ khi có novelty threat mới | — | LOCKED |
| Gate 2 specification chưa frozen | `EVIDENCE_GATES_v2.1.md` — mọi hàng G2 `OPEN`/`EXECUTION-NOT-OPEN` | CQ/verification criteria vẫn ở dạng nháp chưa duyệt (§11); cardinality `Cited_Condition_Evidence_ID` chưa quyết | STEP 1–3 (§20): freeze Data Dictionary → Condition Evidence Contract + Inspection Record schema → CQ + Integrity Rules + PASS criteria | G2 | OPEN |
| Tồn tại vấn đề định danh Revit/IFC chưa giải quyết | Audit 718-element: 8 cặp duplicate `IFC_GUID`/16 ElementIds; `compare_with_ifc_binding` `API_THREAD_TIMEOUT` | Binding thật `BLOCKED/NOT_ASSESSED`, chưa phải FAIL đã xác nhận | STEP 4–5: resolve identity metadata, chạy lại binding comparison cho pilot + known anomaly | G2→G3 | BLOCKED (chờ resolve) |
| Pilot binding chưa được validate | Pilot Run 01/02 (S1/S2/S3 — multi-candidate) | S4/S5 vẫn là đề xuất, chưa chạy; Gate 1 payload vẫn chỉ dùng được như CANDIDATE/DRAFT | STEP 6–7: chạy S4 (duplicate-GUID) và S5 (cross-scope) sau khi CQ được duyệt | G3 | NOT EXECUTED |
| Gate 3 execution vẫn NOT OPEN | `EVIDENCE_GATES_v2.1.md` G3 — mọi hàng `EXECUTION-NOT-OPEN` | Không được chạy thử nghiệm Gate 3 trước Gate 2 sign-off | Hoàn tất Gate 2 PASS criteria (§12) trước | G3 | EXECUTION-NOT-OPEN |
| Archival của file phân tích cũ trong thư mục này | Xem cảnh báo §22 | `00_CLEANUP_REPORT.md` claim đã MOVE 81 file nhưng thư mục `90_ARCHIVE_SUPERSEDED` **không tồn tại** trên đĩa tại thời điểm rà soát này | Cần thực hiện move thật (yêu cầu công cụ shell có quyền ghi/xóa trên ổ đĩa này — hiện không khả dụng trong phiên này) | — | **CHƯA THỰC HIỆN — xem §22** |

---

## 22. Explicit STOP / DO-NOT-DO List

Không:
- broad literature search;
- redesign RQ2;
- open new WP;
- create new Gate;
- calibrated FEM;
- damage diagnosis;
- predictive maintenance;
- RUL;
- complex Health Index;
- ontology research (Paper 2 dùng ontology/RDF/SHACL như công cụ triển khai nếu cần, không nghiên cứu ontology tự thân);
- build commercial app/dashboard;
- solve universal BIM identity persistence (đó là hướng của Borkowski, không phải Paper 2).

---

## 23. QUALITY CONTROL — cảnh báo bắt buộc đọc

- **Gate 1 status — mâu thuẫn với yêu cầu khung "CLOSED/LOCKED":** hồ sơ điều hành hiện tại (`EVIDENCE_GATES_v2.1.md` v2.4, `CURRENT_STATUS_AND_NEXT_DIRECTION.md` v2.4 §1) ghi G1 = `OPEN — PARTIAL EVIDENCE` — bằng chứng khoa học của Paper 1 đã được thực thi và audit, thủ tục nhưng **chưa có `G1_ACCEPTANCE_MATRIX.md` ký duyệt**, và §4 nói rõ "Until G1 is signed, records derived from Paper 1 may be used only as CANDIDATE/DRAFT instances... No accepted handoff exists." **Paper 1 (manuscript) đã `SCIENCE LOCKED` (13/09/2026)** — đây là trạng thái của paper, không phải trạng thái ký duyệt của Gate 1. Để giữ nhất quán với chính nguyên tắc "không đóng gate bằng giả định" của corpus này, MASTER file này ghi nhận: **Paper 2 không mở lại hay làm lại công việc Gate 1** (đúng theo yêu cầu điều hành), nhưng **không tự ý nâng trạng thái Gate 1 lên CLOSED/PASS** khi hồ sơ chính thức chưa ký. Mọi Condition Evidence bắt nguồn từ Gate 1 trong Gate 2–3 tiếp tục ở trạng thái CANDIDATE/DRAFT cho tới khi có sign-off riêng, độc lập với tiến độ Gate 2–3.
- **Identity persistence không phải novelty riêng** — đã khóa đúng theo Borkowski full-text (§2.1).
- **Model version ≠ evidence validity** — đã khóa và định nghĩa tách bạch (§2.2 GAP 2, §9).
- **`Action_Status` không phải Paper 2 core novelty** — xác nhận, chỉ downstream/supporting (§0 chuỗi định danh, §7).
- **CDE không phải research contribution** — xác nhận (§17).
- **Ontology/SHACL/CQ không được claim novel** — xác nhận (§2.1).
- **Duplicate IFC_GUID chỉ là suspected anomaly** cho tới khi actual IFC verified — xác nhận (§14, §19).
- **FEM firewall giữ nguyên** — nominal, uncalibrated, reference-only, not used for damage diagnosis; không có RQ/WP/chương/Paper/Gate riêng cho FEM (`RQ_WP_CHAPTER_PAPER_GATE_MATRIX_v2.1.md` §6 quy tắc 1).
- **Cảnh báo về `00_CLEANUP_REPORT.md`:** file này tự báo cáo "All 81 original files were moved... SHA256 values were checked before and after every file move; all 81 matched" và ghi `90_ARCHIVE_SUPERSEDED` đã tồn tại với 28 file gốc + 4 file manifest. Rà soát trực tiếp thư mục tại thời điểm viết MASTER file này (15/09/2026) cho thấy **`90_ARCHIVE_SUPERSEDED` không tồn tại trên đĩa**, và toàn bộ file gốc (deep-read notes, evidence matrices cũ, v.v.) vẫn nằm phẳng ở root `05_PAPER_2_TRACEABILITY/`. Đây là một mâu thuẫn evidence-vs-record chưa giải quyết được trong phiên làm việc này (xem §22 cuối, mục "archival"). **Không tin cậy báo cáo cleanup này như bằng chứng đã hoàn tất** — chỉ tin cậy trạng thái thư mục quan sát trực tiếp.
- **Archival trong phiên làm việc này:** việc di chuyển file phân tích cũ vào `90_ARCHIVE_DEEP_READ/` theo yêu cầu **chưa được thực hiện** trong phiên hiện tại vì công cụ có sẵn trong phiên này không có quyền ghi/di chuyển/xóa trực tiếp trên ổ đĩa chứa thư mục này (ổ Google Drive `H:`, không mount được vào shell của phiên). Không có file nào bị xóa (đúng yêu cầu KHÔNG DELETE). Danh sách file cần archive và cách thực hiện được nêu ở phần báo cáo cuối cùng gửi người dùng.

---

## Final Research Position

Paper 2 đang nghiên cứu **verifiable traceability** từ Condition Evidence đến đúng BIM component và accountable Inspection Record — không phải BIM integration nói chung. Novelty thực sự nằm ở **sự tích hợp** ba mắt xích này thành một chuỗi cross-system có thể kiểm chứng deterministic (C1–C3), không nằm ở từng kỹ thuật thành phần (sensor→BIM, IFC GlobalId, SHACL, CQ, identity persistence) — tất cả đều đã có sẵn trong literature, kể cả sau khi đọc full-text Borkowski (2026). Gate 2 phải đóng bằng: schema frozen, identifier governance frozen, provenance/validity rules frozen, inspection accountability frozen, CQ và integrity rules pre-registered, fixture manifest sẵn sàng (§12). Gate 3 phải chứng minh: actual Revit↔IFC binding hoạt động trên pilot + known duplicate-GUID case, forward/reverse traceability đúng expected answer, và toàn bộ negative fixture (đặc biệt orphan/duplicate/stale/wrong-revision/out-of-validity) bị phát hiện chính xác. Việc tiếp theo duy nhất, theo đúng thứ tự: **freeze Data Dictionary → freeze Condition Evidence Contract + Inspection Record schema → freeze CQ/Integrity Rules/PASS criteria → GATE 2 SPECIFICATION FREEZE → resolve Revit/IFC identity → verify actual binding → GATE 3 IMPLEMENTATION & VALIDATION.**
