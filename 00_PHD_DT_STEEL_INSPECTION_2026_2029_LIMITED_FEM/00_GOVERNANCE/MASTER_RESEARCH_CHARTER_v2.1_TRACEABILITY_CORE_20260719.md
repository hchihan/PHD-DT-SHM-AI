# MASTER RESEARCH CHARTER — v2.1 TRACEABILITY-CORE
**Version:** v2.1.1 (administrative alignment; no scope amendment) | **Issued:** 2026-07-19 | **Updated:** 2026-08-04
**Status:** **SOURCE OF TRUTH (cao nhất).** | **Source-of-truth level:** 2
**Supersedes:** v1.1 (LIMITED-FEM) as current; v1.1 and v2.0 remain historical decision sources. | **Superseded by:** None.
**Change summary (2026-08-04):** Aligns gate-state language, the evidence firewall, corpus-bounded `CLOSE_SEARCH`, and the accepted Action-ID decision. It does not accept the proposed Action-Status-Event model or close any gate.
**Approved basis:** Council review 17–19/07/2026; supervisor Verdict B (17/07/2026); kiến trúc Limited-FEM giữ nguyên.
**Field:** Construction Management / Asset Management (Quản lý xây dựng / Quản lý tài sản công trình).

> Tài liệu này là hiến chương học thuật cao nhất. Mọi phiên Claude Cowork, Claude Code, OpenCode hoặc AI agent phải đọc file này trước tiên và tuân thủ trục nghiên cứu đã khóa dưới đây. Khi có mâu thuẫn, xem `SOURCE_OF_TRUTH_HIERARCHY_v2.1.md`.

---

## 1. v2.1 tinh chỉnh gì so với v2.0 (và vì sao)

v2.0 đã tái định khung luận án đúng trục Quản lý xây dựng (QLXD): traceability-to-decision với CEI làm thuộc tính hạng nhất, justification & accountability là mục đích cuối, "limited field damage data" là điều kiện biên. v2.1 **không thêm phạm vi**, chỉ siết bốn điều chỉnh học thuật bắt buộc để chống overclaim và bảo đảm mọi tuyên bố có bằng chứng:

1. **Field feasibility — phân biệt "publication" và "evidence".** Paper 3 (công bố hiện trường) là optional/bonus; nhưng **minimum field feasibility evidence là BẮT BUỘC đối với luận án**. Không được ghi toàn bộ RQ3/field là "optional".
2. **Paper 1 claims là candidate cho tới khi Gate 1 đóng.** Mọi kết luận định lượng (sensor configuration dominates architecture; RF/1D-CNN/ResNet1D macro-F1; ResNet1D corroboration) phải ghi **"Candidate claim pending Gate 1 closure"** cho tới khi G1 đóng.
3. **CEI là cấu trúc metadata hạng nhất, không phải scalar/Health Index.** CEI không được mặc định thành một điểm số trọng số đơn.
4. **Legal mapping chỉ để neo QLXD và nghĩa vụ quản lý, không tạo ngưỡng kỹ thuật.** Mọi tham chiếu pháp lý chưa xác minh phải ghi **"Legal reference pending official-source verification."**

---

## 2. Trục trung tâm của luận án (locked)

Một khung data-informed Digital Twin tổ chức **condition evidence cùng với độ tin cậy của nó (CEI)** thành một chuỗi truy vết kiểm chứng được tới cấu kiện BIM và hồ sơ kiểm tra, để quyết định kiểm tra–bảo trì có thể được **biện minh (justified) và truy được trách nhiệm (accountable)**, ngay cả khi dữ liệu hư hỏng hiện trường hạn chế. Mô hình FEM danh nghĩa chỉ phục vụ tham chiếu bố trí cảm biến, không bao giờ là nguồn chẩn đoán.

**Lõi QLXD** = biện minh & truy trách nhiệm của một quyết định quản lý tài sản dưới ràng buộc bằng chứng thưa. **Không phải** chẩn đoán hư hỏng. **Không phải** kỹ thuật cảm biến.

### 2.1 Core evidence chain (locked)

```text
Vibration data
→ condition / state-change evidence (+ CEI)
→ BIM-linked component
→ inspection record
→ justified, accountable inspection–maintenance action
```

### 2.2 Core identifier chain (locked)

```text
Sensor_ID → BIM_GUID → Condition_Evidence_ID → Inspection_Record_ID → Action_Record_ID
```

CEI là thuộc tính tường minh của **mọi** `Condition_Evidence_ID`. `Action_Status`/`Workflow_Status` là **current-state projection/attribute** của `Action_Record_ID`, không phải mắt xích định danh (xem `RESEARCH_ARCHITECTURE_DECISION_RECORD_ACTION_ID_20260719.md`). Bối cảnh định danh cấu kiện trong G2 phải giữ `Asset_ID`, `BIM_GUID` và `Model_Version_ID`; không tự thêm `Component_ID` vào canonical chain, và database surrogate key chỉ là technical implementation key. `Action_Record_ID` phải truy được: evidence, CEI, component, inspection record, role, timestamp, version, approval status và management/legal reference áp dụng. `FEM_Node_ID` chỉ được phép tồn tại như **optional metadata**; không bao giờ là mắt xích bắt buộc.

`Status_Event` là hướng specification hiện hành cho append-only history. Tên `Status_Event_ID`, lifecycle, transition vocabulary, authorization, verification và closure/reopen vẫn phụ thuộc `ADR_ACTION_STATUS_EVENT_20260804_DRAFT.md` ở trạng thái **PROPOSED — NOT YET ACCEPTED**, expert review và G2 baseline; phần này không âm thầm sửa quyết định Charter/ADR đã accepted.

### 2.3 Vai trò FEM (locked)

FEM luôn được mô tả: **"nominal, uncalibrated, reference-only, not used for damage diagnosis."** FEM **không có** RQ / WP / chương / Paper / Evidence Gate riêng; không vai trò chẩn đoán; không hiệu chuẩn; không suy luận suy giảm độ cứng; không chuyển kết quả định lượng lab → field.

### 2.4 Accountability — định nghĩa đã khóa

> **Accountability trong luận án là khả năng truy vết vai trò, nguồn bằng chứng, người/đơn vị tạo hoặc xác nhận hồ sơ, thời điểm, phiên bản và trạng thái phê duyệt của một quyết định quản lý. Khái niệm này KHÔNG phải kết luận trách nhiệm pháp lý hoặc quy lỗi cá nhân.**

Accountability được hiện thực hóa qua các thuộc tính của `Action_Record_ID` (role, evidence source, creator/approver, timestamp, version, approval status, management/legal reference áp dụng). Không dùng accountability như một tuyên bố pháp lý. Định nghĩa này áp dụng thống nhất trong terminology control, RQ2/Paper 2, competency questions, và Inspection_Record / Action_Record schema.

---

## 3. Research questions (locked)

**RQ1 — Evidence (Lab).** Dưới giao thức run-aware, leakage-controlled (LORO), dữ liệu dao động từ khung thép 1:10 và các cấu hình cảm biến khác nhau tạo được bằng chứng phân biệt các trạng thái liên kết có kiểm soát đến mức tin cậy nào — và cấu hình cảm biến có chi phối mạnh hơn lựa chọn kiến trúc mô hình không? *(Kết luận định lượng: candidate pending Gate 1.)*

**RQ2 — Traceability & decision (QLXD CORE, câu gốc đã khóa).**
> "How can condition evidence and its confidence be organised and linked to BIM components and inspection records to enable verifiable justification and accountability of inspection decisions under limited field damage data?"

Không mở rộng RQ2 sang: ontology engineering thuần túy; phần mềm thương mại; quyết định tự động; damage diagnosis; predictive maintenance; RUL; weighted Health Index. SCQ / VCQ / RCQ phải được **pre-register** trước khi xây schema hoặc demo.

**RQ3 — Field feasibility.** Khung có thể triển khai ở một nhà công nghiệp thép thực (Rapexco) tới mức nào để hỗ trợ lựa chọn và ghi nhận hành động kiểm tra dưới dữ liệu hư hỏng hiện trường hạn chế? *(Paper 3 optional; minimum field-feasibility evidence bắt buộc — xem §6.)*

---

## 4. Kiến trúc RQ – WP – Chapter – Paper – Gate

Chi tiết đầy đủ: `RQ_WP_CHAPTER_PAPER_GATE_MATRIX_v2.1.md`. Tóm tắt trục chịu lực:

| RQ | WP | Chapter | Paper | Evidence Gate | Vai trò QLXD |
|---|---|---|---|---|---|
| RQ1 | WP1 | C4 | Paper 1 | G1 | Bằng chứng lab có định lượng độ tin cậy |
| RQ2 | WP2 | C5 | Paper 2 | G2, G3, G6 | **QLXD CORE — trụ cột nhận diện ngành** |
| RQ3 | WP3 | C6 | Paper 3 (bonus) | G4, G5 | Bằng chứng khả thi hiện trường |
| — | WP4 (gộp vào WP2/WP3) | C7 (opt., có thể gộp C6) | Paper 4 (opt.) | G5 | Decision-support synthesis |

Không tạo thêm RQ, WP, chương, Paper hay Gate mới. **Không có chương/Paper/Gate FEM.** Trục chịu lực là C4 (Paper 1/RQ1) + C5 (Paper 2/RQ2); cả hai chạy song song ngay, không phụ thuộc tiếp cận hiện trường.

---

## 5. Paper portfolio (kế hoạch 3 năm / 2×Q3)

Yêu cầu tối thiểu: hai bài Q3 trong ba năm. Trụ cột = **Paper 1 (RQ1) + Paper 2 (RQ2)**, không phụ thuộc site.

- **Paper 1** — Run-aware evaluation of low-cost sensor configurations (dataset integrity, run registry, run-aware/LORO, sensor-configuration effect, CEI as by-product). Mọi con số **candidate pending Gate 1**.
- **Paper 2** — Verifiable traceability-to-decision framework (identifier chain + CEI, pre-registered SCQ/VCQ/RCQ, invalid-data test, legal-mapping table). **Đây là trụ cột nhận diện QLXD.**
- **Paper 3 (bonus)** — Field feasibility tại Rapexco. Publication là optional; **evidence tối thiểu là bắt buộc (§6).**
- **Paper 4 (optional)** — From condition evidence to inspection priority (4-level logic, expert scenario review). Có thể gộp vào Paper 3.

---

## 6. Field feasibility — publication (optional) vs evidence (MANDATORY)

Đây là điều chỉnh bắt buộc #1 của v2.1.

- **Paper 3 publication:** optional / bonus / stretch; nằm ngoài critical path.
- **Minimum field feasibility evidence cho luận án:** **BẮT BUỘC.** Gồm tối thiểu:
  1. field sensor register;
  2. Sensor_ID → BIM_GUID mapping;
  3. data return and completeness evidence;
  4. operational baseline;
  5. inspection-record workflow;
  6. tối thiểu 2–3 traceability scenarios.
- **Không yêu cầu field damage diagnosis.** Mọi bất thường hiện trường dẫn tới *kiểm tra*, không dẫn tới *kết luận hư hỏng*.

### 6.1 Field PREPARATION (được phép chạy sớm) vs field DEPLOYMENT (sau khi G4 mở)

Không chờ Paper 1–2 nộp xong mới bắt đầu Rapexco. Tách hai giai đoạn:

- **Field preparation — chi phí thấp, được phép làm ngay (song song Paper 1–2):** xác nhận field-access agreement; audit BIM model & GUID stability; chuẩn bị field sensor register; chuẩn bị Sensor_ID → BIM_GUID mapping protocol; data governance; inspection-record template; Action_Record template; danh sách 2–3 traceability scenarios; yêu cầu điện/mạng/vị trí thiết bị; điều kiện bảo quản & tháo lắp cảm biến.
- **Field deployment — chỉ sau khi Paper 1–2 đủ ổn định và G4 được mở:** lắp cảm biến chính thức; thu baseline dài hạn; kích hoạt workflow hiện trường; scenario validation; viết Paper 3.

Paper 3 publication là optional/bonus; minimum field-feasibility evidence là mandatory cho luận án.

---

## 7. CEI — định nghĩa hạng nhất (điều chỉnh bắt buộc #3)

CEI (confidence/evidence indicator) là **first-class attribute** của `Condition_Evidence_ID`. **Không** mặc định biến CEI thành weighted scalar score hay Health Index.

CEI được định nghĩa như **cấu trúc metadata** gồm tối thiểu:
- evidence validity status;
- model confidence;
- run/fold variability;
- sensor configuration;
- data-quality status;
- provenance;
- timestamp / version.

Nếu chưa đủ bằng chứng để tổng hợp thành một chỉ số đơn, phải ghi: **"Evidence is currently insufficient to define CEI as a universal scalar index."** CEI **không** phải là severity, **không** phải là mức độ hư hỏng vật lý.

---

## 8. Legal mapping — chỉ để neo QLXD (điều chỉnh bắt buộc #4)

Legal mapping **chỉ** dùng để: (i) neo đóng góp vào QLXD; (ii) thể hiện nghĩa vụ quản lý hồ sơ; (iii) thể hiện trách nhiệm kiểm tra/quan trắc/bảo trì; (iv) hỗ trợ justification & accountability.

**Không được:** dùng văn bản pháp luật để suy ra ngưỡng hư hỏng; tuyên bố mọi công trình đều bắt buộc quan trắc; dùng điều khoản pháp lý làm căn cứ chẩn đoán kỹ thuật; tự tạo ngưỡng Normal–Watch–Inspect–Priority từ luật.

Mọi luật/nghị định/thông tư/quyết định/số điều phải được xác minh bằng nguồn chính thức. Mục chưa kiểm chứng ghi: **"Legal reference pending official-source verification."** (Danh mục cần xác minh: Luật Xây dựng 135/2025; NĐ 207/2026/NĐ-CP; TT 32/2026/TT-BXD; QĐ 46/2026/QĐ-UBND Khánh Hòa; Công văn 3839 — tất cả **pending official-source verification**, xem `../01_CURRENT_CONTROL/CURRENT_STATUS_AND_NEXT_DIRECTION.md`; danh mục lịch sử ở `../90_ARCHIVE/CURRENT_RESET_20260804/CURRENT_CONTROL_HISTORY/UNRESOLVED_ITEMS_TRACKER_v2.1.md`.)

---

## 9. Evidence Gates (đồng bộ)

Chi tiết: `EVIDENCE_GATES_v2.1.md`. Tóm tắt:

- **G1** — Dataset integrity & run-aware evaluation (run registry, sensor metadata, file provenance, leakage-safe split, split-before-windowing, train-only preprocessing, LORO, common seeds, run-level metrics & uncertainty, ResNet1D sensor-mode verification).
- **G2** — Traceability model & competency questions (identifier schema, CEI attribute structure, SCQ/VCQ/RCQ, acceptance criteria, Inspection_Record minimum schema).
- **G3** — End-to-end lab traceability-to-decision demo (evidence → CEI → BIM component → inspection record → action; round-trip; orphan-ID / duplicate-ID / missing-CEI tests; invalid-data / SHACL-or-equivalent validation).
- **G4** — Minimum field mapping & baseline feasibility (field-access basis; sensor register; Sensor_ID → BIM_GUID; data return; completeness & drift; operational baseline; traceability scenarios).
- **G5** — Inspection-action scenario review (transparent 4-level logic; facility-manager/expert review; no automated decision; no field damage conclusion without inspection).
- **G6** — Paper 2 submission.
- **G7** — Thesis synthesis and, when feasible, Paper 3 submission.

**Không tồn tại Gate** liên quan calibrated FEM, MAC, EMA, equivalent stiffness, stiffness degradation, FEM sensitivity, optimal sensor placement.

**Current gate: G1** (materially strengthened nhưng experimentally open — LORO + ResNet1D provenance pending).

---

## 10. Allowed / prohibited claims

### Allowed
- Bằng chứng lab phân biệt được các trạng thái liên kết có kiểm soát dưới đánh giá leakage-controlled. *(định lượng: candidate pending G1)*
- CEI là confidence/evidence indicator gắn với condition evidence (cấu trúc metadata, không phải severity).
- Chuỗi truy vết liên kết evidence + CEI tới cấu kiện và hồ sơ kiểm tra, kiểm chứng qua SCQ/VCQ/RCQ công bố trước.
- Một quyết định kiểm tra có thể được biện minh và truy trách nhiệm về evidence, confidence, cấu kiện, và nghĩa vụ quản lý áp dụng.
- Khung khả thi triển khai tại công trình thực (feasibility, không phải diagnosis).
- FEM danh nghĩa cung cấp tham chiếu bố trí cảm biến.

### Candidate (pending Gate 1 closure — phải ghi nhãn)
- "Sensor configuration dominates model architecture."
- RF / 1D-CNN / ResNet1D macro-F1 (RF ~0.862; 1D-CNN S12 ~0.841; ResNet1D ~0.828) — **candidate claim pending Gate 1 closure.**
- "ResNet1D corroborates the finding" — pending ResNet1D sensor-mode & provenance verification.

### Prohibited
- Field damage diagnosis khi chưa có kiểm tra xác nhận; direct lab-to-field classifier transfer.
- Mọi tuyên bố dựa trên calibrated FEM; suy luận bolt-preload/stiffness degradation từ FEM.
- Chuyển kết luận định lượng 1:10 → công trình thực.
- Ordinal severity / DSI; mô tả CEI như severity vật lý.
- RUL / predictive maintenance; weighted Health Index; "optimal" sensor placement; autonomous maintenance; general AI-superiority; commercial Digital Twin platform.

---

## 11. Cấu trúc phân tích bắt buộc

Mọi file chiến lược/review/status dùng: **Claim → Evidence → Limitation → Next action.** Phải phân biệt và không trộn lẫn bốn lớp bằng chứng: (1) laboratory evidence; (2) information traceability; (3) field feasibility; (4) management decision support. Không dùng bằng chứng lớp này để tuyên bố kết quả lớp khác.

**Gate status at 2026-08-04:** G1 = `OPEN — PARTIAL EVIDENCE`; G2 = `OPEN — LITERATURE BOUNDARY CLOSED, SPECIFICATION NOT YET FROZEN`; G3 = `OPEN — NOT IMPLEMENTED, NOT VALIDATED, NOT OFFICIALLY PASSED`, while G3 execution remains **NOT OPEN** until the G2 package is baselined and explicitly accepted. `CLOSE_SEARCH` is corpus-bounded, not universal absence and not a G2 PASS.

---

## 12. Current priority (G1)

1. Khóa canonical run registry; 2. xác nhận sensor identity/provenance; 3. audit split-before-windowing; 4. thực hiện leakage-safe run-aware/LORO với multi-seed evaluation; 5. xác nhận hoặc loại ResNet1D theo provenance; 6. cập nhật run/fold uncertainty; 7. hoàn tất acceptance matrix và sign-off; 8. **chỉ sau đó** mới khóa claim Paper 1.

Song song (được phép): draft SCQ/VCQ/RCQ; thiết kế CEI metadata structure; draft Inspection_Record schema; legal-reference inventory. Không xây framework phức tạp hoặc decision logic chi tiết trước khi competency questions và acceptance criteria được pre-register.

---

## 13. Terminology & governance

Thuật ngữ theo `TERMINOLOGY_CONTROL_CURRENT.md`. Mọi lần nhắc FEM kèm qualifier bắt buộc. Chạy keyword check trước mọi gate closure. Quy tắc file, source-of-truth và xử lý file cũ: xem `SOURCE_OF_TRUTH_HIERARCHY_v2.1.md` và `AGENT_RULES.md`.

**End of Charter v2.1.** Trục: RQ1 + RQ2 là spine chịu lực; RQ2/Paper 2 là trụ cột nhận diện QLXD; RQ3/Rapexco minimum evidence bắt buộc, publication bonus.
