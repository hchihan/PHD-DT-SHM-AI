# Sensor-to-BIM có phải novelty chính của Paper 2 không?

**Declaration:** RQ2 → WP2 → C5 / Paper 2 → G2–G3 → Scope: **Core** (Layer 2 — information traceability)

---

## Trả lời ngắn

**Không.** Sensor-to-BIM linking và việc dùng IFC GlobalId đều là `ESTABLISHED PRIOR ART` trong corpus đã deep-read. Nếu contribution statement của Paper 2 xoay quanh "link `Sensor_ID` với IFC GlobalId của cấu kiện", đó chính là claim mà Round 1 và Round 3B đã **chủ động loại khỏi novelty boundary** — và là claim reviewer sẽ đánh trúng đầu tiên.

Đoạn 120 từ anh cần vẫn có ở dưới, nhưng được viết quanh **chuỗi tích hợp**, không quanh identity link.

---

## Classification

```text
Classification: ESTABLISHED PRIOR ART
```

**Basis (đều là repository locators, không phải trí nhớ):**

| Nội dung | Nguồn + locator |
|---|---|
| "Novelty không thể là 'đưa dữ liệu cảm biến vào BIM'" — Theiler & Smarsly (2018), Theiler et al. (2017), Quinn et al. (2020), Lorvão Antunes et al. (2024) | `02_EVIDENCE_BASE/RQ2_GATES2_3/G2_G3_SCREENING_EVIDENCE_AND_GAP_REPORT.md`, §3 "Sensor-to-BIM và operational data linkage" (dòng 65–67) |
| "Novelty chỉ còn ở governance và kiểm chứng persistence/cross-system identity, **không ở việc sử dụng GlobalId**" — buildingSMART (2024), Lee et al. (2021), Lorvão Antunes et al. (2024), Oraskari et al. (2021) | cùng file, §3 "IFC GlobalId/BIM identity" (dòng 69–71) |
| "Paper 2 không được lấy 'use IFC GlobalId' làm contribution; phần còn mở là persistence, crosswalk governance và failure handling" | `G2_G3_ROUND1_DEEP_READ_AND_NOVELTY_BOUNDARY.md`, §"IFC GlobalId linkage" (dòng 202–204) |
| Claims removed from novelty: "Component coding hoặc `IfcGlobalId`-based BIM/CMMS linkage" | `G2_G3_ROUND3B_HISTORY_ACCOUNTABILITY_AND_SEARCH_CLOSURE.md`, §7.3 |
| Prohibited claims: "Novel sensor-to-BIM integration", "Novel use of IFC GlobalId" | `G2_G3_SCREENING_EVIDENCE_AND_GAP_REPORT.md`, dòng 262–263 |
| "must not be claimed for sensor-to-BIM integration generally"; PROHIBITED INFERENCE: "sensor-to-BIM integration itself is novel" | `04_RQ2_TRACEABILITY_EVIDENCE_ADDENDUM_v1.2_20260718.md`, dòng 11 và 53 |
| Đối thủ gần nhất đã làm đúng việc anh định claim: Lorvão Antunes et al. (2024) nối structural element → IFC GlobalId qua ifcOWL và trả GUID qua SPARQL/API | `G2_G3_ROUND1_DEEP_READ_AND_NOVELTY_BOUNDARY.md`, dẫn PDF p. 7 §5.2.4 Fig. 5; pp. 9–10 Listing 5, Fig. 9 |
| Piras et al. (2026) giữ nguyên `IfcGlobalId` làm CMMS asset identifier cho 428 assets | `G2_G3_RECENT_EVIDENCE_SCREENING_2023_2026.md`, dòng 17, 120, 127; trạng thái novelty: **Established** (dòng 196) |

Tất cả nguồn trên ở trạng thái `VERIFIED` **trong phạm vi project corpus** (đã được deep-read và trích locator trong các Round report). Không có reference nào được tôi tạo thêm.

---

## Prior-art decomposition — tại sao claim của anh trượt

| Level | Câu hỏi | Kết quả |
|---|---|---|
| **Technique** | `Sensor_ID` ↔ IFC GlobalId có mới không? | Không. Đã có precedent ở cả 4 nhánh: normative identity (buildingSMART 2024), format/uniqueness checking (Lee et al. 2021), inspection→GlobalId retrieval (Lorvão Antunes et al. 2024), BIM→CMMS identity preservation (Piras et al. 2026). |
| **Combination** | Tổ hợp "sensor + GlobalId + BIM" có mới không? | Không, trong corpus đã sàng lọc. Theiler và Quinn đã nối SHM/BAS data với BIM context; Antunes đã nối observation → element → GlobalId. |
| **Distinct work** | Tổ hợp có làm được việc mà từng phần không làm được không? | **Chỉ đúng khi tổ hợp mở rộng tới `Status_Event` / authorization / post-action verification / guarded closure.** Riêng identity link thì không — nó dừng ở hop đầu tiên của chuỗi. |

Thêm một điểm kỹ thuật: `Sensor_ID → BIM_GUID` **chỉ là mắt xích 1** của identifier chain đã khóa:

```text
Sensor_ID → BIM_GUID / Asset_ID @ Model_Version_ID → Condition_Evidence_ID
          → Inspection_Record_ID → Action_Record_ID
```

Viết contribution statement quanh mắt xích 1 nghĩa là bỏ trắng 4 mắt xích còn lại — chính là 4 mắt xích mang toàn bộ candidate novelty của thesis. Ngoài ra, binding này không phải một join tĩnh: theo `G1_TO_G2_CONDITION_EVIDENCE_INTERFACE_v1.0.md`, nó là một **governed binding** có trạng thái (`UNBOUND` → `CANDIDATE` → verified qua hành vi xác nhận của con người, `Candidate_BIM_GUID` dòng 341). Mô tả nó như "link" đã là mất thông tin.

---

## Phần *thật sự* còn mở quanh identity (nhưng không đủ gánh contribution)

`PARTIALLY SUPPORTED GAP` — dùng làm supporting contribution, không làm headline:

- **Persistence của GlobalId qua IFC revision / replacement / resynchronization** — Piras kiểm ở initial import, không test qua revision (`G2_G3_ROUND3A_NOVELTY_AND_SCHEMA_BOUNDARY.md`, dòng 101).
- **Crosswalk governance + ownership** — Round 1 §"IFC GlobalId linkage" ghi rõ đây là phần còn mở.
- **Negative fixtures cho chính identity chain**: orphan `Sensor_ID`, orphan `BIM_GUID`, missing `Condition_Evidence_ID`, duplicate crosswalk. `G2_G3_SCREENING_EVIDENCE_AND_GAP_REPORT.md` dòng 140: *"Trong phạm vi các tài liệu đã sàng lọc, chưa thấy kiểm thử tích hợp orphan `Sensor_ID`, orphan `BIM_GUID`..."*
- **Model-version binding** (`@ Model_Version_ID`) như một điều kiện của identity, không phải metadata.

Đây là *governance và kiểm chứng*, không phải *liên kết*. Sự khác biệt đó là toàn bộ khoảng cách giữa một claim sống sót và một claim bị bác.

---

## Contribution statement — 121 từ (bản EN cho manuscript)

> This paper contributes an implementation-neutral, identity-governed evidence-to-action specification for the inspection and maintenance of coastal industrial steel buildings. Within the reviewed corpus, sensor-to-BIM linking and IFC GlobalId anchoring are established prior art; they are used here as background instruments, not as contributions. The specification separates component identity (BIM_GUID at a declared Model_Version_ID) from record identity (Condition_Evidence_ID, Inspection_Record_ID, Action_Record_ID), distinguishes current Workflow_Status from a proposed append-only Status_Event history, and binds accountable authorization, actor-role-time-rationale provenance and post-action verification to guarded closure and reopen. It is accompanied by a validation contract: chain-specific integrity constraints, isolated invalid fixtures with expected violation codes, and paired forward/reverse competency questions, specified but not yet executed. Within the reviewed corpus, no single model carries these elements as one chain.

**Word count:** 121 (whitespace-split).

**Bản tiếng Việt để anh đối chiếu ý:**

> Bài báo đóng góp một specification evidence-to-action trung lập về implementation, có identity governance, cho công tác inspection–maintenance nhà thép công nghiệp ven biển. Trong phạm vi corpus đã sàng lọc, sensor-to-BIM linking và IFC GlobalId anchoring là prior art đã xác lập; ở đây chúng là instrument nền, không phải đóng góp. Specification tách component identity (`BIM_GUID` tại một `Model_Version_ID` được khai báo) khỏi record identity (`Condition_Evidence_ID`, `Inspection_Record_ID`, `Action_Record_ID`), phân biệt `Workflow_Status` hiện thời với lịch sử `Status_Event` append-only (đang ở trạng thái đề xuất), và ràng buộc accountable authorization, provenance actor–role–time–rationale, post-action verification vào guarded closure/reopen. Kèm theo là một validation contract: constraint toàn vẹn đặc thù cho chuỗi, invalid fixture cô lập với violation code kỳ vọng, và cặp competency question xuôi/ngược — đã đặc tả nhưng chưa thực thi.

### Ba điều đã được cài sẵn trong đoạn văn, đừng gỡ ra khi biên tập

1. **"Within the reviewed corpus"** xuất hiện hai lần. `CLOSE_SEARCH` là corpus-bounded; nó không cho phép "first", "no study worldwide" hay bất kỳ universal-absence claim nào. Câu cuối cố ý viết *"no single model carries these elements as one chain"* chứ không phải *"no study has done this"*.
2. **Động từ ở rung 2 (DESIGN)**, không phải rung 5 (VALIDATED). "Specification", "specified but not yet executed" — vì G2 đang `OPEN — SPECIFICATION NOT YET FROZEN` và G3 là `EXECUTION-NOT-OPEN`. Lưu ý: bản wording ở `G2_G3_SCREENING_EVIDENCE_AND_GAP_REPORT.md` dòng 235 dùng *"develops **and validates**"* — đó là đích G2+G3, **chưa dùng được ở thời điểm hiện tại**. Nếu copy nguyên câu đó vào manuscript hôm nay thì đấy là một silent promotion.
3. **"a proposed append-only Status_Event history"** — chữ *proposed* là bắt buộc. `Status_Event_ID` đang ở trạng thái `PROPOSED — NOT YET ACCEPTED` chờ `ADR_ACTION_STATUS_EVENT_20260804_DRAFT.md`. Nếu ADR bị sửa, câu này phải sửa theo.

---

## Sensor-to-BIM nên nằm ở đâu trong Paper 2

Không xoá — chuyển vị trí:

- **Related Work / Background:** một đoạn ngắn thừa nhận Theiler et al. (2017), Theiler & Smarsly (2018), Quinn et al. (2020), Lorvão Antunes et al. (2024), Piras et al. (2026) đã xác lập sensor-to-BIM và GlobalId anchoring. Thừa nhận sớm và rõ ràng làm reviewer tin phần novelty còn lại.
- **Method:** `Sensor_ID → BIM_GUID @ Model_Version_ID` là **CQ01** trong CQ Registry (`G2_G3_PAPER2_REVISED_ROADMAP_v1.1.03.08.2026.md`, dòng 596) và là input cho constraint IR-03 / negative fixture IF-01 — tức là *đối tượng được kiểm chứng*, không phải *đóng góp được tuyên bố*.
- **Discussion:** phần persistence/crosswalk governance ở trên, khung trong "within the reviewed corpus".

---

## Claim → Evidence → Limitation → Next action

**Claim.** Sensor-to-BIM và IFC GlobalId linkage là `ESTABLISHED PRIOR ART`; contribution phòng thủ được của Paper 2 là chuỗi tích hợp identity-governed evidence-to-action với event history, authorization, post-action verification và guarded closure.

**Evidence.** `G2_G3_SCREENING_EVIDENCE_AND_GAP_REPORT.md` §3 và dòng 262–263, 275; `G2_G3_ROUND1_DEEP_READ_AND_NOVELTY_BOUNDARY.md` §"IFC GlobalId linkage" + dòng 360; `G2_G3_ROUND3B_HISTORY_ACCOUNTABILITY_AND_SEARCH_CLOSURE.md` §7.2–7.3 (ba contribution statement đã được duyệt) và §9 (search closure register: "Complete integrated chain — CLOSED"); `G2_G3_RECENT_EVIDENCE_SCREENING_2023_2026.md` dòng 196; `04_RQ2_TRACEABILITY_EVIDENCE_ADDENDUM_v1.2_20260718.md` dòng 11, 53.

**Limitation.**
- Đoạn 121 từ là văn bản ở **rung 2 (DESIGN)**. Nó không được đọc như bằng chứng rằng specification chạy được, nhất quán nội tại, hay đã validated — theo §7.4 của Round 3B, các claim đó **chỉ được phép sau G3**, mà G3 đang `EXECUTION-NOT-OPEN`.
- Ngay cả candidate cluster (event history / authorization / verification / closure) cũng chưa validated: G2 chưa frozen, một số quyết định còn `EXPERT_REVIEW_DEPENDENT` (cardinality Inspection–Action, role/permission/SoD, transition vocabulary, closure/reopen policy) và `G1_DEPENDENT` (evidence payload binding).
- Firewall Layer 2: đoạn này chỉ được claim rằng mô hình *kiểm tra được*. Nó không được claim chẩn đoán hư hỏng, không được claim đã chứng minh ngoài hiện trường, không được claim cải thiện kết quả bảo trì.
- Kết luận prior-art này bị chặn bởi corpus Round 1–3B. Nếu anh muốn mở lại search vì một câu hỏi mới có khả năng dịch chuyển structural novelty boundary, đó là **quyết định của anh**, không phải của skill này.

**Next action.** Dán đoạn 121 từ vào draft Paper 2, rồi chạy một pass rà soát Abstract + Introduction + figure caption để tìm mọi chỗ còn khung sensor-to-BIM hoặc GlobalId như đóng góp — theo kinh nghiệm, những chỗ đó sống sót lâu nhất trong Abstract và caption. Sau đó đối chiếu ba contribution statement ở Round 3B §7.2 để chắc rằng cả ba đều hiện diện trong bài (record-event specification / accountable action lifecycle / validation contract).

---

## Báo cáo

**Files đọc:**
- `08_AI_SKILL_SYSTEM/phd-dt-research-skills/phd-literature-evidence/SKILL.md` + `references/{corpus-map, claim-source-mapping, source-verification}.md`
- `08_AI_SKILL_SYSTEM/phd-dt-research-skills/_phd-canon/{novelty-boundary, output-discipline, research-chain, gate-model, epistemic-ladder, scope-control}.md`
- `02_EVIDENCE_BASE/RQ2_GATES2_3/`: `G2_G3_SCREENING_EVIDENCE_AND_GAP_REPORT.md`, `G2_G3_ROUND1_DEEP_READ_AND_NOVELTY_BOUNDARY.md`, `G2_G3_ROUND3B_HISTORY_ACCOUNTABILITY_AND_SEARCH_CLOSURE.md`, `G2_G3_RECENT_EVIDENCE_SCREENING_2023_2026.md`, `G2_G3_ROUND3A_NOVELTY_AND_SCHEMA_BOUNDARY.md`, `04_RQ2_TRACEABILITY_EVIDENCE_ADDENDUM_v1.2_20260718.md`, `G1_TO_G2_CONDITION_EVIDENCE_INTERFACE_v1.0.md`, `G2_G3_PAPER2_REVISED_ROADMAP_v1.1.03.08.2026.md`, `00_README_START_HERE.md`

**Files tạo/sửa:** chỉ file này. Không có thay đổi nào trong `00_GOVERNANCE`, `01_CURRENT_CONTROL`, `02_EVIDENCE_BASE`, `03_PAPERS`, `05_DATA_CODE_AND_EXPERIMENTS`, `06_LITERATURE_AND_ZOTERO`, `07_PROMPTS_AND_HANDOFFS`. Không đụng Zotero.

**Gate movement:** không. Đây là công việc chuẩn bị manuscript ở Layer 2; G2 vẫn `OPEN — SPECIFICATION NOT YET FROZEN`, G3 vẫn `EXECUTION-NOT-OPEN`. Không có `PASS` nào được phát ra.

*AI-assisted research disclosure: phân loại prior art và soạn thảo đoạn contribution statement được thực hiện với hỗ trợ AI, dựa trên các Round report bất biến trong repository; không có reference nào được tạo mới.*

---

*v1.0 · 2026-08-10 · read-only output*
