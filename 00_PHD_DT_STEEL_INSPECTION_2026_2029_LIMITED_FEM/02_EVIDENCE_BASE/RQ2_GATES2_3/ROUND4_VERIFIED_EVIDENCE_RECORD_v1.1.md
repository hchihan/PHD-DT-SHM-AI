# ROUND 4 — VERIFIED EVIDENCE RECORD v1.1

**Version:** v1.1
**Date:** 2026-08-09
**Status:** EVIDENCE RECORD — **PROVISIONAL IN PART.** Không phải "immutable evidence record". Một số claim vẫn ở trạng thái provisional (xem §13).
**Source-of-truth level:** evidence, không phải navigation authority.
**Supersedes:** Không supersede file nào. `G2_G3_ROUND4_CQ_CONSTRAINT_ACCOUNTABILITY_DEEP_READ_20260809.md` (v1.0) **được giữ nguyên** làm bản gốc; file này là bản audit-corrected song song.
**Superseded by:** None.
**Architecture:** Limited-FEM, Traceability-Core.

**Nguồn kiểm soát đã đọc trước khi viết (theo thứ tự):**

1. `../../00_GOVERNANCE/MASTER_RESEARCH_CHARTER.md` (v2.2 concise pointer, 2026-08-04)
2. `../../00_GOVERNANCE/MASTER_RESEARCH_CHARTER_v2.1_TRACEABILITY_CORE_20260719.md` (v2.1.1, SOURCE OF TRUTH cao nhất, level 2)
3. `../../00_GOVERNANCE/RESEARCH_DIRECTION_AND_SCOPE.md` (v2.2)
4. `../../00_GOVERNANCE/RESEARCH_ARCHITECTURE.md` (v2.2)
5. `../../01_CURRENT_CONTROL/CURRENT_STATUS_AND_NEXT_DIRECTION.md` (v2.2)
6. `../../00_GOVERNANCE/RESEARCH_ARCHITECTURE_DECISION_RECORD_20260719.md` (ACCEPTED) + `../../00_GOVERNANCE/ADR_ACTION_STATUS_EVENT_20260804_DRAFT.md` (PROPOSED — NOT YET ACCEPTED)
7. `../../00_GOVERNANCE/THE_COUNCIL_REVIEW_FEM_OR_NO_FEM_17.07.2026.md`
8. `00_README_START_HERE.md` (v2.2); `G2_G3_ROUND4_CQ_CONSTRAINT_ACCOUNTABILITY_DEEP_READ_20260809.md` (v1.0) và năm PDF gốc trong `DEEP_READ_20.07.2026/`

**Ghi chú tài liệu quản trị lịch sử:** `MASTER_RESEARCH_CHARTER_v1.1_LIMITED_FEM_20260717.md` và `RESEARCH_ARCHITECTURE_DECISION_RECORD_20260717.md` hiện chỉ tồn tại trong `90_ARCHIVE/` và đã bị supersede bởi mục 2 và mục 6 ở trên. Chúng được đọc như **nguồn quyết định lịch sử**, không phải cơ sở hiện hành. Không có file quản trị nào bị sửa, xóa, ghi đè hay đổi tên trong nhiệm vụ này.

---

## 1. Executive verdict

Round 4 đọc năm bài chưa deep-read: Keet & Khan (2025), Kim et al. (2018), Jia et al. (2025), Lee, D. et al. (2021), Pauwels & Terkaj (2016).

Bốn kết luận đứng vững sau khi kiểm chứng trực quan PDF gốc:

1. Keet & Khan (2025) là **thẩm quyền phương pháp** cho câu hỏi "CQ là gì, CQ nào hỏng" và **tách tường minh** competency question khỏi constraint-checking query. `SOURCE-VERIFIED`.
2. Kim et al. (2018) **đã đóng** phần novelty "liên kết hồ sơ công việc FM với đối tượng IFC bằng Semantic Web"; nhưng không có identity governance, không có record schema, không có integrity constraint, không có reverse query. `SOURCE-VERIFIED`.
3. Jia et al. (2025) có rule engine **đã chạy thật** trên IFC-derived RDF, nhưng họ chỉ có rule giá trị và rule không gian; **không có họ rule toàn vẹn tham chiếu**, không có fixture manifest, không có oracle. `SOURCE-VERIFIED`.
4. Pauwels & Terkaj (2016) tuyên bố rõ: `RULE`/`FUNCTION` của EXPRESS **không chuyển được** sang OWL2 DL class expression, và `WHERE` rule **không nằm trong** conversion. Đây là đóng góp **phủ định** quan trọng nhất của Round 4 cho luận án. `SOURCE-VERIFIED`.

Bốn nhóm lỗi trong v1.0 đã được sửa: (A) nhãn kiểm chứng và locator; (B) cấu trúc CQ bị trộn với constraint và test; (C) quyết định schema tuyên bố quá mức bằng chứng; (D) novelty claim gộp thành một khối.

Một lỗi **thực chất về nội dung** được phát hiện khi soi PDF: v1.0 mô tả ngược kiến trúc lưu trữ của Lee, D. et al. (2021) (xem §3, mục V-11). Đây là lý do phán quyết cuối là `ACCEPT WITH MAJOR REVISION` chứ không phải minor.

**Round 4 là literature evidence cho information traceability. Nó không phải validation evidence. Nó không đóng Gate 2 và không mở Gate 3.**

---

## 2. RQ–WP–Chapter–Paper–Gate routing

| Trường | Giá trị |
|---|---|
| **Primary mapping** | `RQ2 → WP2 → Chương 5 → Paper 2 → Gate 2` |
| Secondary 1 | `RQ2 → WP2 → Chương 5 → Paper 2 → Gate 3` (chỉ là *nghĩa vụ chứng minh tương lai*, không phải bằng chứng đã có) |
| Secondary 2 | Chương 2 — background/gap evidence |
| **Scope classification** | `Core Scope` |
| **Evidence type** | Literature evidence cho information traceability (Lớp 2 trong firewall bốn lớp) |
| **Evidence layer** | Không dùng cho Lớp 1 (lab), Lớp 3 (field feasibility), Lớp 4 (decision support) |
| **Gate effect** | **Không có.** G1 = `OPEN — PARTIAL EVIDENCE`; G2 = `OPEN — LITERATURE BOUNDARY CLOSED, SPECIFICATION NOT YET FROZEN`; G3 = `OPEN — NOT IMPLEMENTED, NOT VALIDATED, NOT OFFICIALLY PASSED`, execution `NOT OPEN` |

**FEM firewall.** Không có nội dung nào trong record này sử dụng, ngụ ý hay yêu cầu FEM hiệu chuẩn. FEM giữ nguyên: **nominal, uncalibrated, reference-only, not used for damage diagnosis.**

**Scope firewall.** Record này không mở rộng sang predictive maintenance, RUL, field damage diagnosis, calibrated FEM, blockchain adoption, weighted Health Index, Smart City, Edge AI, hay commercial software development. Lee, D. et al. (2021) được đọc như **đối thủ cạnh tranh và nguồn cảnh báo**, không phải công nghệ được nhận.

### 2.1 Chuỗi định danh — cảnh báo mâu thuẫn nguồn (control finding)

Charter v2.1 §2.2 (SOURCE OF TRUTH cao nhất) khóa chuỗi:

```text
Sensor_ID → BIM_GUID → Condition_Evidence_ID → Inspection_Record_ID → Action_Record_ID
```

Ba điểm bắt buộc phải giữ đúng:

- `Action_Status` / `Workflow_Status` là **current-state projection/attribute** của `Action_Record_ID`, **không phải mắt xích định danh**. `CURRENT_STATUS_AND_NEXT_DIRECTION.md` §6 ghi rõ: ký hiệu chuỗi kiểu `Action_Status` là lịch sử, **"must not be propagated"**.
- `Status_Event` / `Status_Event_ID` là `PROPOSED — NOT YET ACCEPTED` theo `ADR_ACTION_STATUS_EVENT_20260804_DRAFT.md`.
- `Asset_ID`, `BIM_GUID`, `Model_Version_ID` là **bối cảnh định danh cấu kiện bắt buộc trong G2** theo Charter §2.2, nhưng **không được thêm identifier mới vào canonical chain**; không tự thêm `Component_ID`.

Bản v1.0 dùng chuỗi kết thúc bằng `Status_Event` như thể đã accepted. Bản v1.1 sửa lại theo Charter và gắn nhãn `Status_Event` là `PROPOSED`. Trong tất cả các mục dưới đây, nơi cần nói về trạng thái hành động, ký hiệu dùng là `Action_Record_ID` + `Action_Status` (attribute), và `Status_Event` chỉ xuất hiện kèm nhãn `PROPOSED — NOT YET ACCEPTED`.

---

## 3. Source and verification register

**Quy tắc nhãn áp dụng trong toàn bộ record:**

| Nhãn | Nghĩa |
|---|---|
| `SOURCE-VERIFIED` | Đã đối chiếu **trực tiếp trên trang PDF gốc được render và đọc trực quan**; locator có thật; nội dung khớp |
| `TEXT-EXTRACTION-VERIFIED — provisional pending PDF visual audit` | Chỉ xác minh qua trích xuất văn bản/Markdown; chưa soi trang PDF |
| `READER-INFERRED` | Suy luận có cơ sở từ nội dung bài, **không phải câu chữ tác giả** |
| `THESIS-APPLICATION` | Đề xuất áp dụng cho luận án; **không phải tuyên bố của tác giả bài báo** |
| `UNKNOWN` / `Evidence is currently insufficient.` | Không đủ bằng chứng |

**Định dạng locator bắt buộc:** `Tên paper → PDF p. n [printed p. m] → section / table / figure`.

### 3.1 Sổ đăng ký nguồn

| # | Paper (citation đầy đủ) | File | Số trang PDF | Ánh xạ trang | Trạng thái |
|---|---|---|---|---|---|
| P1 | Keet, C. M., & Khan, Z. C. (2025). *Characterising Competency Questions for Ontologies.* In Proc. Joint Ontology Workshops (JOWO) — Episode XI, co-located with FOIS 2025, Catania, Italy, 8–9 Sept 2025. CEUR-WS Vol-4176, paper caos-9. ISSN 1613-0073. CC BY 4.0. Published 2026-03-02. | `Gate 2.1 - caos-9.pdf` | 14 | PDF p. = trang bài (không có printed page riêng) | `SOURCE-VERIFIED` (7 trang) |
| P2 | Kim, K., Kim, H., Kim, W., Kim, C., Kim, J., & Yu, J. (2018). *Integration of ifc objects and facility management work information using Semantic Web.* Automation in Construction, 87, 173–187. DOI 10.1016/j.autcon.2017.12.019 | `kim2018.pdf` | 15 | **printed p. = PDF p. + 172** | `SOURCE-VERIFIED` (8 trang) |
| P3 | Jia, L., Chen, M., Chen, C., & Jin, Y. (2025). *A Semantic Web and IFC-Based Framework for Automated BIM Compliance Checking.* Buildings, 15, 2633. DOI 10.3390/buildings15152633 | `buildings-15-02633.pdf` | 25 | PDF p. = "n of 25" in ra trên trang | `SOURCE-VERIFIED` (6 trang) |
| P4 | Lee, D., Lee, S. H., Masoud, N., Krishnan, M. S., & Li, V. C. (2021). *Integrated digital twin and blockchain framework to support accountable information sharing in construction projects.* Automation in Construction, 127, 103688. DOI 10.1016/j.autcon.2021.103688 | `Lee et al. (2021) — Provenance và accountability.pdf` | 9 | PDF p. = trang bài in ở chân trang | `SOURCE-VERIFIED` (5 trang) |
| P5 | Pauwels, P., & Terkaj, W. (2016). *EXPRESS to OWL for construction industry: Towards a recommendable and usable ifcOWL ontology.* Automation in Construction, 63, 100–133. DOI 10.1016/j.autcon.2015.12.003 | `pauwels2016.pdf` | 34 | **printed p. = PDF p. + 99** | `SOURCE-VERIFIED` (3 trang) |

### 3.2 Các trang PDF đã kiểm chứng trực quan

| Paper | Trang PDF đã soi | Nội dung phủ |
|---|---|---|
| P1 Keet & Khan | 1, 4, 5, 9, 11, 12, 13 | Abstract/problem; §3.2 + Def.1; Def.2–3 + Fig.1; §4.1.1 SewerNet + §4.1.2; §4.2 faulty CQ + constraint boundary; Fig.6 + ROCQS + §5; §6 Conclusion/future work |
| P2 Kim et al. | 1, 4, 7, 9, 10, 11, 12, 13, 14 | Abstract/gap; §3.1–3.2 six layers + Fig.2; IfcRelSpaceBoundary path; Table 1–2 + §4.1; case + Table 3; Table 4 + §4.2.1; Table 5–6; §4.2.2 + §5; §5 kết + §6 Conclusion |
| P3 Jia et al. | 4, 11, 16, 20, 21, 22, 23 | §2.4 + §3 Methodology; §5.1 Jena-vs-SWRL + Table 3; Table 7 + §5.2.2; §6.2 executed check; Fig.13–14 + derived link; §7 limitations |
| P4 Lee, D. et al. | 2, 3, 5, 6, 8 | §2 gap + §3 blockchain storage; §4–4.2 framework + Fig.1; §5.1 test scenario; §5.2 results; §6 trilemma + §7 Conclusion |
| P5 Pauwels & Terkaj | 4, 5, 33 | §1.3.2–1.3.4 criteria; §1.3.4 CWA rationale + §2 RULE/FUNCTION counts; §6 Conclusions |

**Giới hạn kiểm chứng còn lại.** Các trang **không** được soi trực quan trong Round 4 v1.1: P1 pp. 2–3, 6–8, 10, 14; P2 pp. 2–3, 5–6, 8, 15; P3 pp. 1–3, 5–10, 12–15, 17–19, 24–25; P4 pp. 1, 4, 7, 9; P5 pp. 1–3, 6–32, 34. Mọi claim của v1.0 neo vào các trang đó **không được nâng lên `SOURCE-VERIFIED`** trong bản này (xem §13).

### 3.3 Sai lệch phát hiện khi đối chiếu PDF (v1.0 → v1.1)

| ID | Loại | v1.0 ghi | PDF gốc thực tế | Locator | Xử lý |
|---|---|---|---|---|---|
| V-11 | **Sai nội dung thực chất** | "Framework stores only a small compliance statement on-chain; bulk sensor and BIM data go to a distributed ledger" | Ngược lại: blockchain **chính là** distributed ledger và chỉ chứa compliance statement; dữ liệu sensor và as-built BIM **không** được đưa lên ledger vì "blockchain is inherently not designed for data storage" | P4 → PDF p. 2 §3; PDF p. 3 §4 và §4.1 | Viết lại (§4, P4-C2) |
| V-12 | **Sai kết quả** | "3 of 10 nodes... those nodes were excluded from consensus; valid nodes synchronised at 2.41 s, all nodes at 3.42 s" | Node không hợp lệ là **#3, #7, #10**; bị loại khỏi *cơ chế đồng thuận*, nhưng theo **quy tắc 51%** vẫn nhận và chia sẻ cùng dữ liệu tại 3.42 s. Bảy node hợp lệ (#1,#4,#5,#2,#8,#6,#9) xác thực tại 2.41 s | P4 → PDF p. 6 §5.2 | Viết lại (§4, P4-C4) |
| V-13 | **Sai sự kiện** | "Listings are examples... **no rule IDs**, no severity, no expected-violation semantics" | Table 3 **có cột `Rule NO.`** với định danh 1-1 … 1-4 | P3 → PDF p. 11 ("11 of 25") → §5.1.1, Table 3 | Sửa: có rule ID cục bộ; thiếu bộ rule đầy đủ, severity, violation semantics |
| V-14 | **Trích dẫn không kiểm chứng** | "GB 50096-2011" | PDF in "Design Code for Residential Building (GB-50096) [46]"; **năm không xuất hiện** trên trang đã soi | P3 → PDF p. 20 §6.2 | Đổi thành `GB-50096`; năm = `UNKNOWN` |
| V-15 | Locator sai | "#31982 / #66803 ... Table 6, PDF p. 12" | ID nằm trong **thân bài §4.2.2, PDF p. 13 [printed 185]**; Table 6 (PDF p. 12) định danh vật thể chia sẻ bằng **tên element**, không bằng ID | P2 → PDF p. 12 Table 6; PDF p. 13 §4.2.2 | Tách locator |
| V-16 | Diễn giải quá đà | "deliberately excludes furniture/other elements to bound scope" | Bài viết: phần tử space-boundary được trích "to match the scope of the FM works because there are too many building elements in the IFC file (e.g., furniture, walls, columns)" | P2 → PDF p. 7 [printed 179] §3.2 layer 1 | Hạ xuống `READER-INFERRED` |
| V-17 | Locator sai | "590 records ... §4.1, PDF pp. 9–10" | PDF p. 9 ghi "almost 600 records"; con số **590** nằm ở PDF p. 10 [printed 182] | P2 → PDF pp. 9–10 | Tách locator |
| V-18 | Nhãn sai | Kim "author-stated" hỗ trợ `Model_Version_ID` | Tác giả nêu lý do BIM model ít được cập nhật là **phần cứng chạy phần mềm BIM và kỹ năng của facility manager**, không phải quản trị phiên bản | P2 → PDF p. 13 [printed 185] §4.2.2 | Hạ xuống `THESIS-APPLICATION` |
| V-19 | Locator sai | Six-layer architecture "§3.2, PDF pp. 5–9" | Danh sách sáu lớp in ở **PDF p. 4 [printed 176]**, cuối §3.2 | P2 → PDF p. 4 | Sửa |
| V-20 | Locator lệch | "Definitions 1–6, Figs. 1–4, PDF pp. 4–8" | Def.1 ở PDF p. 4; Fig.1 + Def.2 + Def.3 ở PDF p. 5 | P1 → PDF pp. 4–5 | Sửa |
| V-21 | Thiếu attribution | "should later be decomposed into less expressive profiles" | Bài ghi rõ đây là "the suggestions made by **Hoang and Törmä [47]**" | P5 → PDF p. 33 [printed 132] §6 | Bổ sung attribution |
| V-22 | Thiếu printed page | Chỉ ghi `PDF p.` cho P2 và P5 | P2 in trang 173–187; P5 in trang 100–133 | — | Bổ sung `[printed p.]` toàn bộ |
| V-23 | Nhãn tài liệu | "EVIDENCE RECORD (immutable once accepted)" | Còn claim provisional và trang chưa soi | — | Bỏ nhãn immutable |
| V-24 | Ký hiệu chuỗi | Chuỗi kết thúc `... → Action_Record → Status_Event` không nhãn | `Status_Event` là `PROPOSED — NOT YET ACCEPTED` | ADR draft 20260804 | Gắn nhãn `PROPOSED` (§2.1) |

---

## 4. Corrected cross-paper evidence matrix

Ký hiệu locator: `PDF p. n [printed p. m]`. Cột **Nhãn** áp dụng cho *nội dung claim*, không phải cho ý nghĩa luận án.

### 4.1 P1 — Keet & Khan (2025)

**Vai trò học thuật:** thẩm quyền phương pháp về bản chất và lỗi của competency question. Domain-neutral.

| ID | Claim | Locator | Nhãn | Giới hạn | Dùng cho luận án |
|---|---|---|---|---|---|
| P1-C1 | Rất ít hướng dẫn cho việc soạn CQ và đánh giá CQ tốt/xấu; hệ quả là mơ hồ và công thức không dùng được | PDF p. 1 → Abstract; PDF p. 1 → §1 | `SOURCE-VERIFIED` | Tuyên bố định vị, không đo lường | Gap statement cho Paper 2 §CQ methodology (`CITE`) |
| P1-C2 | Năm loại CQ chính: SCQ, VCQ, FCQ, RCQ, MpCQ | PDF p. 1 → Abstract; PDF p. 4 → §3.2 + Definition 1 | `SOURCE-VERIFIED` | Tác giả ghi rõ: "We do not exclude the possibility that more types of CQs for ontologies may be identified later" (PDF p. 4) | CQ Registry của G2 phải **gán type**, không liệt kê phẳng (`ADAPT`) |
| P1-C3 | **SCQ không nhất thiết phải trả lời được, thậm chí không nhất thiết hình thức hóa được; VCQ phải vừa hình thức hóa được vừa trả lời được**, và độ biểu đạt logic của VCQ không vượt quá logic của ontology (`Lv ⊆ Lo`) | PDF p. 5 → §3.2, Definition 2 và Definition 3 + đoạn dẫn | `SOURCE-VERIFIED` | Tác giả tự nhận ràng buộc `Lv ⊆ Lo` "may appear debatable"; nó phụ thuộc dự án | **Quyết định cho G2:** câu hỏi phạm vi và câu hỏi kiểm chứng là **hai artifact khác nhau** (`ADAPT`) |
| P1-C4 | Câu hỏi kiểm tra disjointness hoặc cardinality **không phải CQ**; chúng là "general constraint-checking queries" | PDF p. 11 → §4.2, đoạn "There are also questions that seek to verify constraints..." + hai bullet ví dụ | `SOURCE-VERIFIED` | Ranh giới được lập luận, không kiểm chứng thực nghiệm | **Quyết định cho G2:** Constraint Catalogue và CQ Registry là hai artifact với ngữ nghĩa chấp nhận khác nhau (`ADAPT`) |
| P1-C5 | CQ có thể hỏng vì bốn nguyên nhân: (i) cú pháp/ngữ nghĩa, (ii) lệch độ biểu đạt của query language hoặc ontology language, (iii) nội dung ontology, (iv) không khớp với chính type của nó | PDF p. 11 → §4.2 | `SOURCE-VERIFIED` | Chỉ (ii) và (iv) được triển khai, "due to space limitations" | Checklist rà soát chất lượng CQ cho G2 (`ADAPT`) |
| P1-C6 | Mẫu câu hỏi có vấn đề được đặt tên: lượng từ mơ hồ ("to what extent"), how-to quá rộng, yêu cầu hướng dẫn mô hình hóa, tham chiếu không chính xác | PDF p. 12 → Fig. 6 (cột "Problematic questions") | `SOURCE-VERIFIED` | Chỉ là mẫu minh họa, không phải phân loại đầy đủ | Quy tắc soạn CQ cho Registry (`ADAPT`) |
| P1-C7 | ROCQS (Repository of Ontology Competency QuestionS) gồm **558 CQs** cho tất cả các type, tuân thủ FAIR, có chú giải lý do câu hỏi bị coi là có vấn đề | PDF p. 12 → §4.2 | `SOURCE-VERIFIED` | Chưa được kiểm chứng độc lập; quyền chỉnh sửa mới ở mức kế hoạch ("We plan to enable edit access") | Benchmark ngoài về độ phủ CQ (`BENCHMARK`) |
| P1-C8 | Các type CQ khác nhau ánh xạ vào các giai đoạn khác nhau của NeOn methodology | PDF p. 9 → §4.1.2 + Fig. 5 | `SOURCE-VERIFIED` | Tác giả ghi rõ "leaving the *how* for future work"; không đánh giá ánh xạ | Bằng chứng yếu — chỉ dùng làm công cụ sắp xếp |
| P1-C9 | Use case SewerNet: MpCQ "Does maintenance have a definite endpoint?" và "Is maintenance's endpoint determined outside that process?" xác nhận tính **atelic**, dẫn tới biểu diễn `Maintenance` như subclass của `dolce:accomplishment`, khác với `Repair` (individual action) | PDF p. 9 → §4.1.1 | `SOURCE-VERIFIED` | Một ontology, thuật lại hồi cứu, không có baseline không-CQ để so sánh | **Tương đồng trực tiếp** với ngữ nghĩa `Action_Record` của luận án (`CITE`) |
| P1-C10 | Chưa có đánh giá dựa trên người dùng cho QuO và ROCQS | PDF p. 13 → §6 Conclusion ("We also plan to conduct user-based evaluations...") | `SOURCE-VERIFIED` (`AUTHOR-STATED` future work) | — | Khoảng trống phương pháp mà luận án **không** lấp (ngoài phạm vi) |

**Component audit — P1**

| Thành phần | Có/Một phần/Không | Locator |
|---|---|---|
| CQ typology + definitions | Có | PDF pp. 4–5 → §3.2, Def. 1–3 |
| Tiêu chí answerability / formalisability | Có | PDF p. 5 → Definition 3 |
| Ranh giới CQ ≠ constraint query | Có | PDF p. 11 → §4.2 |
| Expected-answer shape như trường bắt buộc của CQ | Một phần — kỳ vọng câu trả lời được bàn theo type; **không** có slot hình thức trong mô hình QuO | PDF p. 5 → §3.2 |
| Acceptance criteria / pass–fail cho một bộ CQ | Không | — |
| Nội dung domain: inspection, action, status, BIM identity | Không (bài domain-neutral) | — |
| Đánh giá dựa trên người dùng | Không — future work | PDF p. 13 → §6 |

**Verdict P1.** Có mô hình khái niệm + repository; **không** có đánh giá thực nghiệm về hiệu quả, **không** có ngữ nghĩa chấp nhận (pass/fail).

---

### 4.2 P2 — Kim et al. (2018)

**Vai trò học thuật:** prior art gần nhất cho cạnh `Inspection_Record` / `Action_Record` ↔ cấu kiện BIM.

| ID | Claim | Locator | Nhãn | Giới hạn | Dùng cho luận án |
|---|---|---|---|---|---|
| P2-C1 | Thông tin công trình từ BIM khó truy cập và sử dụng trong O&M vì cấu trúc FMS DB dựa trên hoạt động công việc còn BIM dựa trên đối tượng | PDF p. 1 [173] → Abstract; PDF p. 14 [186] → §6 | `SOURCE-VERIFIED` | Tuyên bố định vị | Gap statement cho Paper 2 (`CITE`) |
| P2-C2 | So sánh phương pháp FM của **năm công ty FM Hàn Quốc** (A–E) sử dụng FMS không có BIM | PDF p. 9 [181] → Table 1 + §4.1 | `SOURCE-VERIFIED` | Mẫu thuận tiện, một quốc gia, **không nêu khung chọn mẫu**; đây là bảng so sánh, không phải khảo sát có phương pháp | Bối cảnh thực hành (`CITE`, không dùng làm bằng chứng thống kê) |
| P2-C3 | Ontology OWL liên kết ba nhóm khái niệm: IFC Concepts, COBie Concepts, Work Concepts (work area, work cycle, work category) | PDF p. 4 [176] → §3.1 + Fig. 2 | `SOURCE-VERIFIED` | Danh sách class không công bố đầy đủ; không có CQ registry | Mẫu ER dùng lại được; **không** còn là novelty cho luận án (`AVOID` claiming novelty) |
| P2-C4 | Kiến trúc sáu lớp: IFC data extraction, COBie data exchange, FMS data management, ontology management, reasoning, query | PDF p. 4 [176] → §3.2 (cuối phần dẫn) | `SOURCE-VERIFIED` | Mô tả phân lớp; không có interface contract, không có versioning | Cho thấy **stack triển khai không phải là đóng góp** (`AVOID`) |
| P2-C5 | Phạm vi công việc gắn vào đối tượng IFC qua `IfcRelSpaceBoundary` → `relatedElements` (là `IfcBuildingElement`), vật liệu qua `IfcMaterialLayerSetUsage` | PDF p. 7 [179] → §3.2 layer 1 + Figs. 7–8 | `SOURCE-VERIFIED` | Chỉ phần tử space-boundary được trích, "to match the scope of the FM works" | **Cảnh báo trực tiếp:** cấu kiện mà một evidence gắn vào **phụ thuộc đường quan hệ IFC được chọn**; G2 phải cố định đường đó tường minh (`ADAPT`) |
| P2-C6 | Việc giới hạn ở phần tử space-boundary loại bỏ furniture và các phần tử khác | PDF p. 7 [179] | **`READER-INFERRED`** (v1.0 ghi là chủ ý của tác giả; bài chỉ liệt kê furniture/walls/columns như ví dụ "too many building elements") | — | Chỉ dùng như minh họa hệ quả phạm vi |
| P2-C7 | Case study: **590** hồ sơ bảo trì kiến trúc không định kỳ, gắn với "common BIM file – office" của buildingSMART; Level 1 có 60 spaces, 262 walls, 66 doors, 25 windows, two stairs, one elevator, net area **1814.786 m²** | PDF p. 10 [182] → §4.1 (con số 590 và cấu hình model); PDF p. 9 [181] → §4.1 ("almost 600 records", Company E) | `SOURCE-VERIFIED` | **Hồ sơ là thật, model là file mẫu tham chiếu, không phải tòa nhà thật** — không có tương ứng as-is | **Then chốt:** đây là demo liên kết, không phải correspondence đã kiểm chứng. Rủi ro tương tự với G3 (`AVOID`) |
| P2-C8 | Khoảng thời gian hồ sơ in trên bài là "1/01/2016 to 6/02/2016", mô tả là "about five months" | PDF p. 9 [181] → §4.1 | `SOURCE-VERIFIED` cho chuỗi in; **`READER-INFERRED`** cho diễn giải ISO 2016-01-01 → 2016-06-02 | Định dạng ngày mơ hồ; chỉ "about five months" khử được mơ hồ | Không dùng làm dữ kiện định lượng |
| P2-C9 | Truy vấn SPARQL trả về **12** hồ sơ bảo trì cho space '139' (phòng họp), phân giải thành **7 bức tường** (`IfcWallStandardcase`) với **hai loại vật liệu hoàn thiện**: plasterboard (4 tường: #31714, #31982, #31893, #31804) và paint (3 tường: #45712, #45623, #45534) | PDF p. 11 [183] → §4.2.1; PDF p. 12 [184] → Table 5 | `SOURCE-VERIFIED` | Truy xuất happy-path; **không** precision/recall, không ground truth, không negative case | Forward retrieval only — cùng ranh giới với Antunes (R1) (`BENCHMARK` yếu) |
| P2-C10 | Space 139 kề space 140, chia sẻ **hai** đối tượng IFC: một tường (`#31982`) và một cửa (`#66803`) | PDF p. 13 [185] → §4.2.2 (thân bài, nơi hai ID xuất hiện) | `SOURCE-VERIFIED` | — | — |
| P2-C11 | Table 6 liệt kê đối tượng chia sẻ theo **tên element**: `Basic Wall:Interior - Partition (92 mm Stud):148,942` (`IfcWallStandardcase`) và `M_Single-Flush:0915 × 2134 mm:186,884` (`IfcDoor`), với hồ sơ ở cả hai space 139 và 140 | PDF p. 12 [184] → Table 6 | `SOURCE-VERIFIED` | Hai space, hai đối tượng | Cho thấy liên kết ở cấp **cấu kiện** (không phải cấp space) làm đổi tập kết quả |
| P2-C12 | "maintenance works are usually conducted at a building element in two adjacent spaces at a similar frequency, **which increases the resulting quantity of work records by about 200%**" | PDF p. 14 [186] → §5 (câu cuối) | `SOURCE-VERIFIED` cho việc **bài có nêu câu này** | **Không có suy dẫn, không mẫu số, không định nghĩa baseline, không bất định.** Số lượng truy xuất ≠ chất lượng truy xuất | **Không được trích như kết quả hiệu năng.** `Evidence is currently insufficient.` Chỉ dùng như minh họa rằng độ mịn liên kết làm đổi recall |
| P2-C13 | Giới hạn do tác giả nêu: BIM model hiếm khi được cập nhật trong thực hành FM (lý do: yêu cầu phần cứng chạy phần mềm BIM); facility manager thiếu kỹ năng BIM/Semantic Web; cần kiểm chứng thêm BIM/COBie bàn giao; cần phương pháp cập nhật hiện trạng công trình hiện hữu có liên kết với DB không đồng nhất | PDF p. 13 [185] → §4.2.2; PDF p. 14 [186] → §6 | `SOURCE-VERIFIED` (`AUTHOR-STATED`) | — | Xem P2-C14 |
| P2-C14 | Suy ra rằng điều này chứng minh `Model_Version_ID` là bắt buộc | PDF p. 13 [185]; PDF p. 14 [186] | **`THESIS-APPLICATION`** (v1.0 ghi nhầm là `AUTHOR-STATED` hỗ trợ trực tiếp) | Tác giả nói về **độ cập nhật của model trong thực hành**, không nói về quản trị phiên bản | Xem §9 và §10 — `Model_Version_ID` được khóa bởi Charter §2.2, **không** bởi Kim |

**Component audit — P2**

| Thành phần | Có/Một phần/Không | Locator |
|---|---|---|
| BIM/IFC identity | Một phần — dùng **số instance IFC** (`#32465`, `#88`), không dùng `GlobalId` | PDF pp. 10–11 [182–183] → Tables 3–4 |
| Inspection record | Không — bản ghi là công việc bảo trì, không phải kết quả kiểm tra | PDF p. 9 [181] → Table 2 |
| Action record | Một phần — có Date, Area, Elements, Work contents, Labors, Work time, Working floor; **không** ID, **không** owner, **không** approval, **không** verification | PDF p. 9 [181] → Table 2 |
| Condition evidence | Không — không có đối tượng defect/condition; chỉ text công việc | PDF p. 9 [181] → Table 2 |
| Status event / history | Không | — |
| Provenance / accountability | Không — không có actor identity, reviewer, approver | — |
| Competency questions | Không — SPARQL ad hoc, không có registry định trước | PDF p. 11 [183] → §4.2 mục 4) |
| Executable constraints | Không — reasoning là phân loại (BOSSAM), không phải kiểm tra toàn vẹn | PDF p. 4 [176] → §3.2 layer 5 |
| Deliberate negative tests | Không | — |
| Forward traceability | Một phần — object → related work records | PDF p. 12 [184] → Table 5 |
| Reverse traceability | Không — không có truy vấn work record → evidence/inspection gốc | — |
| Round-trip parity | Không | — |
| Human review | Không | — |

**Verdict P2.** Có ontology đã triển khai + forward retrieval đã chạy trên một case; **identity governance, record schema, integrity constraints, negative tests, reverse traceability và accountability đều vắng mặt.** Phát biểu "200%" là tuyên bố hiệu quả không có cơ sở suy dẫn.

---

### 4.3 P3 — Jia et al. (2025)

**Vai trò học thuật:** đối thủ gần nhất về **rule checking chạy được trên RDF suy ra từ IFC**.

| ID | Claim | Locator | Nhãn | Giới hạn | Dùng cho luận án |
|---|---|---|---|---|---|
| P3-C1 | "A complete code statement can be summarized as consisting of three parts: **constrained objects, constrained contents, and preconditions**" | PDF p. 4 → §3 Methodology | `SOURCE-VERIFIED` | Áp cho mã xây dựng nhà ở Trung Quốc | **Khung soạn rule chuyển giao được** cho Constraint Catalogue của G2 (`ADAPT`) |
| P3-C2 | Mô tả định lượng được quy về **ba** loại: Property, Construction, Spatial (positional / distance), với cấu trúc phần tử được đặt tên | PDF p. 16 → §5.2.1 + Table 7 | `SOURCE-VERIFIED` | Điều khoản "basic requirement" không định lượng bị loại khỏi cơ chế | Cho một **rule typology**; luận án cần **họ thứ tư** (referential integrity) không có ở đây (`ADAPT`) |
| P3-C3 | Template truy vấn SPARQL được cho theo từng loại mô tả, biến đặt trong `[]` ánh xạ vào core elements của Table 7 | PDF p. 16 → §5.2.2; Tables 8–9 (PDF pp. 17–18, **chưa soi trực quan**) | `SOURCE-VERIFIED` cho §5.2.2; Tables 8–9 = `TEXT-EXTRACTION-VERIFIED — provisional pending PDF visual audit` | Template minh họa; không tuyên bố độ phủ so với bộ mã | Mẫu **query template** dùng lại cho hình thức hóa CQ (`ADAPT`) |
| P3-C4 | Chọn Jena rules thay SWRL vì: SWRL không làm được coordinate transformation / vector calculation; triple lớn từ chuyển đổi IFC kéo dài thời gian đọc của SWRL reasoner; SWRL xử lý long attribute path kém | PDF p. 11 → §5.1 | `SOURCE-VERIFIED` | **Không có so sánh đo được** — không số liệu runtime, không đếm triple, không chạy baseline SWRL | Lập luận hợp lý nhưng **không có bằng chứng**. `Evidence is currently insufficient.` cho mọi tuyên bố hiệu năng |
| P3-C5 | Mapping rules nối IfcOWL với "building object ontology" theo ba họ: entity correspondence, entity object information, inter-entity relationships | PDF p. 11 → §5.1 + §5.1.1 + Table 3; §5.1.2–5.1.3 + Tables 4–6 (PDF pp. 12–15, **chưa soi trực quan**) | `SOURCE-VERIFIED` cho §5.1/§5.1.1/Table 3; phần còn lại `TEXT-EXTRACTION-VERIFIED — provisional pending PDF visual audit` | Table 3 **có** cột `Rule NO.` (1-1…1-4) → rule **có** định danh cục bộ. Thiếu: bộ rule đầy đủ, mức severity, ngữ nghĩa vi phạm kỳ vọng | **Khoảng trống then chốt để luận án chiếm:** rule tồn tại, nhưng **không có violation taxonomy và không có oracle** (`ADAPT`) |
| P3-C6 | Case: đơn nguyên nhà ở 21 tầng, tầng 5–21 đồng dạng; IFC xuất ra, chuyển sang RDF, lưu Jena TDB, phục vụ bằng Fuseki (Apache Jena: Ontology API, Inference API, Fuseki REST API) | PDF p. 20 → §6.1 + Fig. 12 | `SOURCE-VERIFIED` | Một công trình, một bộ mã, một tầng chuẩn | Feasibility, không phải generalisation |
| P3-C7 | Kiểm tra đã chạy: điều khoản "The clear height of balcony railings in residential buildings with seven or more stories shall not be less than 1.10 m" trả về **hai** thực thể `IfcRailing` ở **900 mm** (`ifc:IfcRailing_199427`, `ifc:IfcRailing_200165`), dưới ngưỡng 1100 mm; xác nhận bằng đối chiếu vị trí trong BIMversion | PDF p. 20 → §6.2; PDF p. 21 → Figs. 13–14 | `SOURCE-VERIFIED` | **n = 1 rule, 2 hit.** Không confusion matrix, không hạch toán false-positive/false-negative, không ground-truth manifest các vi phạm đã biết | **Gần nhất trong toàn corpus với một negative test — và vẫn không đạt tiêu chí chặt**, vì hai railing 900 mm là dữ liệu thật, không phải fixture được gieo với expected outcome định trước (`AVOID` mislabelling) |
| P3-C8 | Chuẩn được dùng: "Design Code for Residential Building (**GB-50096**) [46]" | PDF p. 20 → §6.2 | `SOURCE-VERIFIED` cho mã; **năm ban hành = `UNKNOWN`** trên các trang đã soi | v1.0 ghi "GB 50096-2011" — năm chưa kiểm chứng | Ghi là `GB-50096`; không trích năm cho tới khi xác minh reference [46] |
| P3-C9 | Railing **không có** liên kết không gian trực tiếp trong IFC, buộc phải suy ra containment bằng so sánh bounding box (min/max x/y) | PDF p. 21 → §6.2 + Fig. 15 (Fig. 15 **chưa soi trực quan**) | `SOURCE-VERIFIED` cho phát biểu ở thân bài p. 21 | Bounding-box containment là xấp xỉ; giả định trục song song | **Cảnh báo trực tiếp cho G2:** không phải cấu kiện nào cũng có quan hệ IFC dùng được; một số liên kết phải **suy ra**, và liên kết suy ra cần integrity test riêng (`ADAPT`) |
| P3-C10 | Giới hạn do tác giả nêu: ontology chưa đủ cho công trình phức tạp (đề xuất ML để mở rộng); hiệu năng suy luận Jena suy giảm mạnh khi số artifact lên hàng trăm nghìn và mức lồng rule tăng; ontology + rule gắn với tiêu chuẩn quốc gia Trung Quốc | PDF p. 23 → §7 | `SOURCE-VERIFIED` (`AUTHOR-STATED`) | — | Scalability và locale-binding là giới hạn tác giả nêu (`CITE`) |
| P3-C11 | SHACL được liệt kê trong related work như một rule language chuyên biệt được áp dụng rộng cho automated compliance checking — nhưng **không** được bài này dùng | PDF p. 4 → §2.3/§2.4 | `SOURCE-VERIFIED` | Chỉ là điểm qua tài liệu | Ghi nhận: SHACL đã tồn tại trong prior art; luận án dùng SHACL-or-equivalent **không** phải novelty (`AVOID`) |

**Component audit — P3**

| Thành phần | Có/Một phần/Không | Locator |
|---|---|---|
| BIM/IFC identity | Một phần — cá thể IfcOWL; **không** bàn về `GlobalId` governance hay tính bền của định danh | PDF p. 11 → §5.1 |
| Executable constraints | **Có** — Jena mapping rules + SPARQL query rules, đã chạy trên Fuseki | PDF pp. 11, 16, 20–21 |
| Rule typology / templates | Có | PDF p. 16 → Table 7; §5.2.2 |
| Rule identifier | Có, cục bộ (`Rule NO.` 1-1…1-4) | PDF p. 11 → Table 3 |
| Severity / expected-violation semantics | Không | — |
| Competency questions | Không — là điều khoản mã, không phải CQ; không có expected-answer registry | — |
| Deliberate negative fixtures | Không (theo tiêu chí bốn điều kiện chặt) | PDF pp. 20–21 → §6.2 |
| Referential-integrity rules (orphan, duplicate, wrong target type) | Không — rule là domain-value và spatial, không phải link-integrity | PDF p. 11 → Table 3 (+ Tables 4–6, provisional) |
| Condition evidence / inspection / action / status | Không — chỉ compliance giai đoạn thiết kế | Toàn bài |
| Provenance / accountability | Không | — |
| Reverse traceability, round-trip parity | Không | — |

**Verdict P3.** Pipeline rule-checking đã triển khai và chạy; **không có họ rule toàn vẹn tham chiếu, không fixture manifest, không oracle, không chuỗi vòng đời domain.**

---

### 4.4 P4 — Lee, D. et al. (2021)

**Vai trò học thuật:** đối thủ về accountability/immutability. Đi cặp với Çelik et al. (2023) từ Round 3B.

| ID | Claim | Locator | Nhãn | Giới hạn | Dùng cho luận án |
|---|---|---|---|---|---|
| P4-C1 | Dữ liệu digital twin dễ bị ghi đè; trạng thái lịch sử của virtual asset có thể mất; quản lý dữ liệu DT (lưu trữ, bất biến, truy vết) "has not been thoroughly realized" | PDF p. 2 → §2 (đoạn cuối) | `SOURCE-VERIFIED` | Lập luận định vị từ tài liệu | **Gap statement mạnh** cho yêu cầu lịch sử trạng thái của luận án (`CITE`) |
| P4-C2 | **Blockchain chính là distributed ledger và chỉ lưu compliance statement**; dữ liệu sensor và file as-built BIM **không** được đưa lên blockchain vì "blockchain is inherently not designed for data storage"; chỉ "the important updates essential for collaboration should selectively be stored and shared" | PDF p. 2 → §3 (đoạn cuối); PDF p. 3 → §4 và §4.1 + Fig. 1 | `SOURCE-VERIFIED` — **sửa lỗi V-11 của v1.0** | Quyết định lưu chọn lọc được khẳng định, không đánh giá so với phương án khác | **Nguyên lý thiết kế chuyển giao được:** tách **evidence payload** khỏi **attestation record** (`ADAPT`) |
| P4-C3 | Case: lắp ráp robot ảo một cầu mô hình 49 viên gạch (4 loại); as-planned BIM 876 megabytes; 49 compliance statement mỗi cái ~0.5 kilobyte; 49 block được sinh | PDF p. 5 → §5.1; PDF p. 6 → §5.2 | `SOURCE-VERIFIED` | **Cảm biến ảo/giả định** — "the authors assumed that virtual hypothetical sensors that can track locations (e.g., GPS and RFID) are attached to each brick". Không triển khai vật lý | **Không được trích như bằng chứng hiện trường.** Đây là kiểm thử pipeline mô phỏng (`AVOID`) |
| P4-C4 | Tác giả **cố ý** giả định 3 trong 10 node blockchain không có chữ ký hợp lệ (do sửa block trước). Node **#3, #7, #10** không tham gia được cơ chế đồng thuận. Bảy node hợp lệ (#1, #4, #5, #2, #8, #6, #9) xác thực và chia sẻ ở **2.41 s**; theo **quy tắc 51%**, ba node không hợp lệ vẫn đồng thuận giao dịch mới và chia sẻ cùng dữ liệu ở **3.42 s** | PDF p. 5 → §5.1 (giả định 3/10); PDF p. 6 → §5.2 + Fig. 7 | `SOURCE-VERIFIED` — **sửa lỗi V-12 của v1.0** (node không bị loại vĩnh viễn) | Một kịch bản; không lặp lại, không phương sai, không thay đổi tải; compliance check chỉ gồm vị trí và loại gạch | **Gần nhất trong Rounds 1–4 với một fixture không hợp lệ có expected outcome định trước** — nhưng nó kiểm chứng **đồng thuận sổ cái**, không phải **toàn vẹn tham chiếu domain** (`BENCHMARK`) |
| P4-C5 | Compliance checking so as-built với as-planned BIM để sinh một statement "which is a legally effective document confirming all project participants' records" | PDF p. 3 → §4.1 + Fig. 1(c); PDF p. 5 → §5.1 + Fig. 4 | `SOURCE-VERIFIED` | Chỉ kiểm vị trí và loại, "for the simplicity of testing" | Comparator hẹp; **content model của statement không được công bố** |
| P4-C6 | "Blockchain trilemma": không sổ cái nào thỏa mãn đồng thời cả ba thuộc tính security, scalability, decentralisation. Proof of concept dùng chain **private**, mang rủi ro bảo mật cố hữu và mức phi tập trung thấp về quản trị mạng | PDF p. 8 → §6 | `SOURCE-VERIFIED` (`AUTHOR-STATED`) | — | **Lý do không nhận blockchain vào G2/G3.** Nhận nó là nhập khẩu một trilemma chưa giải và một nghĩa vụ chứng minh mới không phục vụ RQ2 (`REJECT` cho Gate hiện tại) |

**Component audit — P4**

| Thành phần | Có/Một phần/Không | Locator |
|---|---|---|
| Immutable event history | Có — block chuỗi, có timestamp và Merkle root | PDF p. 3 → §4.1 + Fig. 1(d); PDF p. 6 → §5.2 |
| Attestation tách khỏi payload | Có | PDF p. 2 → §3; PDF p. 3 → §4.1 |
| Fixture không hợp lệ có chủ đích + expected outcome + thực thi + so sánh | Một phần — thỏa cho **tính hợp lệ chữ ký node**, không thỏa cho **bản ghi domain** | PDF p. 5 → §5.1; PDF p. 6 → §5.2 |
| Accountable human review (reviewer, approver, rationale, authorisation) | Không — node đồng thuận bằng mật mã; không role model, không rationale, không phân tách nhiệm vụ | PDF p. 6 → §5.2 |
| Condition evidence / inspection record / action record | Không | Toàn bài |
| BIM/IFC identity governance | Không — gạch, không phải `GlobalId` | PDF p. 5 → §5.1 |
| Reverse traceability, round-trip parity | Không | — |
| Field validation | Không — cảm biến giả định | PDF p. 5 → §5.1 |

**Verdict P4.** Pipeline mô phỏng đã triển khai và chạy, chứng minh attestation truy vết được và bất biến; **ngữ nghĩa domain, accountability của con người và bằng chứng hiện trường đều vắng mặt.**

---

### 4.5 P5 — Pauwels & Terkaj (2016)

**Vai trò học thuật:** tham chiếu nền tảng cho biểu diễn IFC→OWL mà Kim (2018), Jia (2025) và Antunes (2024) đều đứng trên. Quyết định cho lựa chọn **implementation-neutrality** của G2.

| ID | Claim | Locator | Nhãn | Giới hạn | Dùng cho luận án |
|---|---|---|---|---|---|
| P5-C1 | Không có một ifcOWL thống nhất được thừa nhận; các ứng dụng xây trên các ontology hơi khác nhau và "work as isolated examples" | PDF p. 4 [103] → §1.3.2; xác nhận lại PDF p. 33 [132] → §6 ("the resulting ontologies do not appear to evolve into one referential standard or recommended ifcOWL ontology") | `SOURCE-VERIFIED` | Phân tích định vị các converter trước đó | **Hỗ trợ trực tiếp** cho việc giữ đặc tả G2 độc lập với serialization (`CITE`) |
| P5-C2 | Ba tiêu chí thiết kế, theo thứ tự: (1) ifcOWL phải nằm trong OWL2 DL; (2) ifcOWL phải khớp EXPRESS schema gốc càng sát càng tốt; (3) ifcOWL **chủ yếu** dùng để cho phép chuyển IFC instance file thành RDF graph tương đương | PDF p. 33 [132] → §6 (danh sách đánh số 1–3); lập luận ở PDF p. 5 [104] → §1.3.4 | `SOURCE-VERIFIED` | Tiêu chí 1 được mua bằng cái giá về hiệu năng suy luận | **Tiêu chí 3 là điều quan trọng ở đây:** ifcOWL là **đích chuyển đổi**, không phải schema để soạn thảo (`CITE`) |
| P5-C3 | Khai báo thủ tục `RULE` và `FUNCTION` **không thể** chuyển thành OWL2 DL class expression; cần cách tiếp cận khác. `WHERE` rule declarations **không nằm trong** conversion approach đề xuất, dù có thể chuyển ở mức độ nào đó (Terkaj & Šojić) | PDF p. 33 [132] → §6, hai bullet đầu của "open issues"; lý do ở PDF p. 5 [104] → §1.3.4 | `SOURCE-VERIFIED` | Chuyển đổi một phần là khả thi theo Terkaj & Šojić | **Quyết định:** chuyển IFC sang OWL **làm mất lớp ràng buộc của chính schema**. Mọi Constraint Catalogue của G2 phải được **soạn riêng**, không thừa kế từ ifcOWL (`ADAPT`) |
| P5-C4 | IFC4_ADD1.exp chứa **hai** khai báo `RULE` và **45** khai báo `FUNCTION` | PDF p. 5 [104] → §2 | `SOURCE-VERIFIED` | Con số cho một phiên bản schema cụ thể | Định lượng quy mô lớp ràng buộc bị mất (`CITE`) |
| P5-C5 | ifcOWL hiện là phiên bản "maximal" trong OWL2 DL (`SROIQ(D)`); bước tiếp theo nên phân rã thành module trong các profile ít biểu đạt hơn (DL, EL, QL), **theo đề xuất của Hoang & Törmä [47]** | PDF p. 33 [132] → §6 | `SOURCE-VERIFIED` (`AUTHOR-STATED` future work; attribution bổ sung, sửa V-21) | Chưa thực hiện trong bài | Rủi ro hiệu năng nếu luận án gắn chặt vào ifcOWL; khớp với giới hạn scalability của Jia |
| P5-C6 | Qua phân tích ontology, ifcOWL "might be greatly simplified so that it would become easier to use the IFC information" (Borgo et al., Venugopal et al., de Farias et al.) | PDF p. 33 [132] → §6 | `SOURCE-VERIFIED` (`AUTHOR-STATED` future work) | Không được chứng minh trong bài | Tính khả dụng của ifcOWL là bài toán mở, không phải nền đã giải xong |
| P5-C7 | Kiểm tra nhất quán được kỳ vọng diễn ra trong công cụ BIM gốc theo **CWA**, không trong RDF graph theo **OWA**: "most instance RDF graphs will already be checked for consistency in the native BIM tools. As a result, we can opt to not convert all procedural RULE and FUNCTION declarations..." | PDF p. 5 [104] → §1.3.4 | `SOURCE-VERIFIED` | Giả định quy trình một chiều BIM→RDF | **Cảnh báo:** nếu luận án chỉ kiểm chứng trong RDF, nó kiểm chứng trong một world model (OWA) nơi "thiếu" ≠ "vi phạm" (`ADAPT`) |
| P5-C8 | `INVERSE` attribute được xử lý đúng, "except for a small number of exceptional cases" | PDF p. 33 [132] → §6 | `SOURCE-VERIFIED` | Ngoại lệ không liệt kê ở §6 | Ghi nhận giới hạn kỹ thuật |

**Component audit — P5**

| Thành phần | Có/Một phần/Không | Locator |
|---|---|---|
| Thủ tục chuyển schema IFC→OWL | Có | §3 (PDF pp. 7+, **chưa soi trực quan**); §4.1 converter (PDF p. 28, **chưa soi**) → `TEXT-EXTRACTION-VERIFIED — provisional pending PDF visual audit` |
| Xử lý INVERSE attributes | Có, có ngoại lệ nêu rõ | PDF p. 33 [132] → §6 |
| Lớp ràng buộc (`RULE`/`FUNCTION`/`WHERE`) được bảo toàn | **Không** | PDF p. 33 [132] → §6 |
| Identifier governance / tính bền của `GlobalId` qua file hoặc phiên bản | Không đề cập trên các trang đã soi | — |
| Chuỗi domain (evidence, inspection, action, status) | Không — ngoài phạm vi | — |
| CQ, negative fixtures, parity | Không — ngoài phạm vi | — |

**Verdict P5.** Converter đã triển khai và tài liệu hóa, với các phát biểu ranh giới tường minh và trung thực. Đóng góp quan trọng nhất cho luận án là một đóng góp **phủ định**: lớp ràng buộc của IFC không sống sót qua chuyến đi sang OWL.

---

### 4.6 Bảng so sánh chéo Round 4 (đã sửa)

| Study | Artifact chính | Identity | Độ phủ chuỗi domain | CQ | Executable constraints | Negative test có chủ đích | Forward / reverse | Thiếu chính |
|---|---|---|---|---|---|---|---|---|
| Keet & Khan (2025) | QuO typology + ROCQS (558 CQ) | n/a | Không (domain-neutral) | **Thẩm quyền phương pháp** | **Loại trừ tường minh** constraint query khỏi CQ | Không | n/a | Đánh giá thực nghiệm; ngữ nghĩa chấp nhận |
| Kim et al. (2018) | Ontology OWL + hệ FM 6 lớp | Số instance IFC `#id`, không `GlobalId` | Chỉ work record ↔ đối tượng IFC | Không | Không | Không | Forward một phần; reverse không | Record schema, identity, integrity, review |
| Jia et al. (2025) | IfcOWL + domain ontology + Jena/SPARQL trên Fuseki | Cá thể IfcOWL | Không (giai đoạn thiết kế) | Không | **Có, đã chạy** (rule có `Rule NO.`) | Không — 2 railing 900 mm là dữ liệu thật, không gieo | Forward only | Họ rule toàn vẹn, oracle, độ phủ, severity |
| Lee, D. et al. (2021) | DT (Unity) + private Quorum blockchain | Brick ID | Không | Không | Compliance = vị trí + loại gạch | **Một phần — 3/10 node gieo không hợp lệ, kết quả kỳ vọng được xác nhận; nhưng node vẫn đồng bộ ở 3.42 s theo quy tắc 51%** | Forward only | Ngữ nghĩa domain, vai trò con người, dữ liệu thật |
| Pauwels & Terkaj (2016) | Converter EXPRESS→OWL, ifcOWL | n/a | Không | Không | **Lớp ràng buộc tường minh không được chuyển** | Không | n/a | Tính bền định danh; bảo toàn ràng buộc |

---

## 5. CQ Registry (artifact 1/3)

> **Nhãn toàn mục:** `THESIS-APPLICATION`. Typology là của Keet & Khan (P1-C2, P1-C3). Việc áp typology này vào chuỗi truy vết của luận án là đề xuất của luận án, **không phải claim của tác giả bài báo**. Registry này là **đề xuất thiết kế, chưa được phê duyệt schema governance**.

**Mục đích của artifact.** Đăng ký, phân loại và định phạm vi các câu hỏi mà mô hình dữ liệu truy vết phải phục vụ. **Không** phải nơi chứa tiêu chí đạt/không đạt. **Không** phải nơi chứa constraint.

**Nguyên tắc (từ P1).**

- Mỗi CQ **bắt buộc có type**: `SCQ` | `VCQ` | `FCQ` | `RCQ` | `MpCQ` (P1-C2).
- `SCQ` **không bắt buộc** trả lời được hay hình thức hóa được (P1-C3, PDF p. 5, Definition 2 + đoạn dẫn).
- `VCQ` **bắt buộc** vừa hình thức hóa được vừa trả lời được, và `Lv ⊆ Lo` (P1-C3, Definition 3).
- **Không** mọi CQ phải có expected answer hoặc fixture. Chỉ VCQ được dùng để kiểm chứng mới đi kèm expected answer và fixture — và những trường đó nằm ở **Validation Test Registry**, không ở đây.
- Câu hỏi kiểm tra disjointness / cardinality / toàn vẹn **không được đăng ký ở đây** (P1-C4). Chúng thuộc Constraint Catalogue.

**Trường bắt buộc của CQ Registry**

| Trường | Bắt buộc | Ghi chú |
|---|---|---|
| `CQ_ID` | Có | Định danh ổn định |
| `CQ_Type` | Có | SCQ / VCQ / FCQ / RCQ / MpCQ |
| `Wording` | Có | Câu hỏi bằng ngôn ngữ tự nhiên |
| `Purpose` | Có | Mục đích theo nghĩa `p ∈ P` của P1 (scoping, validation, foundational alignment, relationship, metaproperty) |
| `Scope_Note` | Có | Phần nào của chuỗi được chạm tới |
| `Formalisable` | Có | `yes` / `no` / `n/a`. Với SCQ được phép `no` |
| `Answerable` | Có | Với VCQ bắt buộc `yes` |
| `Expressivity_Check` | Chỉ VCQ | `Lv ⊆ Lo` đạt / không đạt |
| `Quality_Review` | Có | Rà theo bốn nguyên nhân hỏng (P1-C5) và mẫu câu hỏi có vấn đề (P1-C6) |
| `Linked_Test_ID` | Không bắt buộc | Trỏ sang Validation Test Registry nếu có |

**Khung nội dung dự kiến theo type (đề xuất, chưa duyệt)**

| CQ_Type | Vai trò trong G2 | Ví dụ chủ đề (chưa phải wording chốt) |
|---|---|---|
| `SCQ` | Khoanh phạm vi mô hình dữ liệu: cái gì thuộc chuỗi, cái gì không | Loại evidence nào được ghi nhận? Cấu kiện được định danh thế nào? Hồ sơ kiểm tra gồm gì? |
| `VCQ` | Kiểm chứng nội dung: mô hình có trả lời được câu hỏi truy vết thật không | Truy xuất xuôi và ngược trên chuỗi `Condition_Evidence_ID ↔ BIM_GUID ↔ Inspection_Record_ID ↔ Action_Record_ID` |
| `FCQ` | Căn chỉnh phạm trù nền: evidence là gì về mặt bản thể, action là process hay event | Phân biệt kiểm tra (inspection) với hành động khắc phục — tương ứng Maintenance/Repair của P1-C9 |
| `RCQ` | Ràng buộc tính chất quan hệ: đối xứng, bắc cầu, phản xạ trên các cạnh của chuỗi | Quan hệ "evidence attaches to component" có bắc cầu không? |
| `MpCQ` | Metaproperty: rigidity, identity, unity của các lớp chính | `Action_Record` có endpoint xác định không (telic/atelic)? — trực tiếp mượn P1-C9 |

**Giới hạn.** Keet & Khan **không** cung cấp acceptance semantics (P1 component audit). Vì vậy CQ Registry **một mình không đủ** để đóng bất kỳ Gate nào. `Evidence is currently insufficient.` cho mọi tuyên bố rằng registry này đã được kiểm chứng.

---

## 6. Validation Test Registry (artifact 2/3)

> **Nhãn toàn mục:** `THESIS-APPLICATION`. Không paper nào trong Rounds 1–4 công bố artifact tương đương (xem §8, C2). Đây là **đề xuất thiết kế, chưa được phê duyệt schema governance**.

**Phạm vi.** **Chỉ** dành cho các `VCQ` được chọn làm câu hỏi kiểm chứng. SCQ, FCQ, RCQ, MpCQ **không** vào registry này trừ khi được nâng cấp thành VCQ và vượt qua `Expressivity_Check`.

**Trường bắt buộc**

| Trường | Bắt buộc | Ghi chú |
|---|---|---|
| `Test_ID` | Có | Định danh ổn định |
| `Source_CQ_ID` | Có | Phải trỏ về một `VCQ` trong CQ Registry |
| `Query_Direction` | Có | `forward` \| `reverse` \| `round-trip` |
| `Query_Input` | Có | Điểm vào của truy vấn |
| `Expected_Answer` | Có | **Hình dạng** câu trả lời kỳ vọng (kiểu, lực lượng tập kết quả, trường bắt buộc), không chỉ giá trị |
| `Fixture_Ref` | Có | Trỏ tới fixture hợp lệ hoặc không hợp lệ trong Fixture/Oracle Manifest |
| `Pass_Fail_Criterion` | Có | Điều kiện quyết định, phát biểu trước khi chạy |
| `Result` | Điền sau khi chạy | Chỉ ghi khi G3 execution được mở |

**Quy tắc forward/reverse.**

Cặp forward/reverse **chỉ áp dụng khi truy vết hai chiều có ý nghĩa** trên cạnh đang xét. Không áp dụng máy móc cho mọi VCQ. Ví dụ:

| Cạnh | Forward có nghĩa? | Reverse có nghĩa? | Ghi chú |
|---|---|---|---|
| `Condition_Evidence_ID` → `BIM_GUID` | Có | Có | Cần cả hai: từ evidence tìm cấu kiện, và từ cấu kiện liệt kê evidence |
| `BIM_GUID` → `Inspection_Record_ID` | Có | Có | Kim (2018) chỉ làm forward (P2 component audit) |
| `Inspection_Record_ID` → `Action_Record_ID` | Có | Có | Reverse cần thiết cho justification: hành động này dựa trên hồ sơ nào |
| `Action_Record_ID` → `Action_Status` | Có | **Không** | `Action_Status` là projection, không phải thực thể độc lập → truy ngược từ trạng thái về hành động không phải bài toán truy vết hai chiều |
| `Sensor_ID` → `Condition_Evidence_ID` | Có | Có | — |

**Round-trip parity.** Một test `round-trip` chỉ đạt khi tập kết quả đi xuôi rồi đi ngược trả về đúng điểm xuất phát, không thừa không thiếu. Không paper nào trong Rounds 1–4 báo cáo round-trip parity (§4.6).

**Giới hạn.** Registry này **chưa được chạy**. G3 execution là `NOT OPEN`. `Evidence is currently insufficient.` cho mọi tuyên bố về kết quả kiểm chứng.

---

## 7. Constraint Catalogue (artifact 3/3)

> **Nhãn toàn mục:** `THESIS-APPLICATION`. Cơ sở học thuật cho việc **tách** artifact này khỏi CQ Registry là P1-C4 (`SOURCE-VERIFIED`). Cơ sở cho việc phải **soạn riêng, không thừa kế** là P5-C3 (`SOURCE-VERIFIED`). Nội dung catalogue là đề xuất, **chưa được phê duyệt schema governance**.

**Nguyên tắc nền (đã kiểm chứng).**

1. Constraint-checking query **không phải** competency question (P1-C4, PDF p. 11).
2. Lớp `RULE`/`FUNCTION`/`WHERE` của IFC **không** đi qua được ifcOWL (P5-C3, PDF p. 33 [132]). Mọi integrity rule phải soạn tường minh.
3. Trong OWA, "thiếu" không tự động là "vi phạm" (P5-C7, PDF p. 5 [104]). Mỗi rule phải phát biểu rõ giả định thế giới.
4. Prior art chỉ có rule **giá trị** và rule **không gian** (P3-C2, P3-C5). Họ rule **toàn vẹn tham chiếu** không có trong corpus Rounds 1–4.

**Khung soạn rule** (mượn P3-C1, `ADAPT`): mỗi rule phát biểu **constrained object**, **constrained content**, **precondition**.

**Bảy họ ràng buộc bắt buộc**

| ID | Họ ràng buộc | Constrained object | Constrained content | Precondition | Negative fixture / expected failure |
|---|---|---|---|---|---|
| CC-1 | **Orphan record** | Mọi record trong chuỗi | Phải tồn tại record cha hợp lệ được tham chiếu | Record đã được tạo và không ở trạng thái nháp | Fixture: một `Inspection_Record_ID` trỏ tới `Condition_Evidence_ID` không tồn tại → **expected: FAIL, báo orphan** |
| CC-2 | **Duplicate identifier** | Mọi identifier trong chuỗi lõi | Tính duy nhất trong không gian định danh đã khai báo | Không gian định danh được khai báo | Fixture: hai `Condition_Evidence_ID` trùng nhau, khác payload → **expected: FAIL, báo duplicate** |
| CC-3 | **Wrong target type** | Mọi cạnh có kiểu | Đích của cạnh phải đúng lớp đã khai báo | Kiểu cạnh được khai báo trong ER model | Fixture: evidence gắn vào một `IfcSpace` thay vì một cấu kiện → **expected: FAIL, báo type violation** |
| CC-4 | **Stale crosswalk** | Ánh xạ `Sensor_ID → BIM_GUID`, và `BIM_GUID @ Model_Version_ID` | Ánh xạ phải trỏ tới phiên bản model còn hiệu lực | `Model_Version_ID` có mặt (Charter §2.2) | Fixture: ánh xạ trỏ tới `Model_Version_ID` đã bị thay thế → **expected: FAIL, báo stale** |
| CC-5 | **Conflicting binding** | Một evidence, nhiều cấu kiện | Không được có hai binding mâu thuẫn cùng hiệu lực | Binding có nhãn thời gian và nhãn provenance | Fixture: cùng `Condition_Evidence_ID` gắn đồng thời vào hai `BIM_GUID` khác nhau mà không có quy tắc phân giải → **expected: FAIL, báo conflict** |
| CC-6 | **Illegal status transition** | `Action_Status` như attribute của `Action_Record_ID` | Chuyển trạng thái phải nằm trong tập chuyển hợp lệ | Từ vựng vòng đời đã được duyệt — **hiện `GOVERNANCE_DECISION_REQUIRED`** | Fixture: chuyển thẳng sang `completed` mà không có bản ghi verification → **expected: FAIL**. Áp `completed` ≠ verified closure |
| CC-7 | **Derived-link integrity** | Mọi cạnh có `Link_Provenance = derived` | Quy tắc suy dẫn phải chạy lại được và cho cùng kết quả | Cạnh được khai báo là `derived` (xem §9, S-P2) | Fixture: một cạnh derived mà quy tắc suy dẫn không tái tạo được → **expected: FAIL**. Cơ sở: P3-C9, containment bằng bounding box là xấp xỉ |

**Ghi chú bắt buộc trong catalogue (cite P5-C3):** *"Lớp `RULE`/`FUNCTION`/`WHERE` của IFC không được thừa kế qua ifcOWL (Pauwels & Terkaj 2016, PDF p. 33 [printed 132], §6). Mọi integrity rule ở đây phải được soạn tường minh và không được giả định là đã tồn tại trong serialization."* Ghi chú này cần **một nguồn xác nhận thứ hai** trước khi coi là đã ổn định (xem §13, TV-1).

**Giới hạn.** Không rule nào trong catalogue này đã được chạy. Không fixture nào đã được tạo. `Evidence is currently insufficient.` cho mọi tuyên bố về khả năng phát hiện vi phạm.

---

## 8. Candidate-contribution matrix

> Chỉ dùng thuật ngữ **`candidate contribution`**. Không tuyên bố novelty cuối cùng khi chưa có evidence matrix đầy đủ. Ngôn ngữ novelty bị chặn phạm vi: *trong các bài đã deep-read ở Rounds 1–4*, không phải "trong tài liệu".

### C1 — Truy vết hai chiều xuyên suốt

**Phát biểu.** `condition evidence ↔ BIM component ↔ inspection record ↔ action status` được truy vết được theo cả hai chiều trên toàn chuỗi.

| Trường | Nội dung |
|---|---|
| **Literature evidence** | Kim (2018) chỉ forward: object → work records, không có truy vấn ngược (P2-C9, P2 component audit; PDF p. 12 [184] Table 5). Jia (2025) forward only (P3 component audit). Lee, D. (2021) forward only (P4 component audit). Antunes (2024) publish CQ và forward query, không có action/status (Round 1). Không bài nào trong Rounds 1–4 báo cáo round-trip parity (§4.6). |
| **Thesis evidence required** | ER model đã baseline; cặp VCQ forward/reverse cho mỗi cạnh có nghĩa hai chiều (§6); fixture hợp lệ; kết quả round-trip parity đã chạy |
| **Limitation** | Kết luận bị chặn theo corpus 4+4+4+2+5 bài, không phải theo tài liệu. Chuỗi kết thúc ở `Action_Record_ID` theo Charter §2.2; `Action_Status` là attribute; `Status_Event` là `PROPOSED — NOT YET ACCEPTED` |
| **Validation obligation** | G3: chạy đủ cặp forward/reverse; báo cáo parity; báo cáo cả trường hợp không đạt |
| **Current status** | `CANDIDATE — literature boundary supported, thesis evidence not produced` |

### C2 — Kiểm chứng integrity bằng expected outcomes + positive/negative fixtures + pass/fail criteria

**Phát biểu.** Toàn vẹn của chuỗi được kiểm chứng bằng bộ kỳ vọng kết quả, fixture hợp lệ và không hợp lệ, và tiêu chí đạt/không đạt phát biểu trước.

| Trường | Nội dung |
|---|---|
| **Literature evidence** | Keet & Khan (2025) cung cấp typology nhưng **không** acceptance semantics (P1 component audit; PDF p. 13 §6). Jia (2025) chạy rule thật nhưng hai railing 900 mm là dữ liệu thật, **không phải fixture gieo có expected outcome** (P3-C7; PDF pp. 20–21). Lee, D. (2021) **có** gieo fixture không hợp lệ với kết quả kỳ vọng — nhưng cho **đồng thuận sổ cái**, không cho toàn vẹn tham chiếu domain, và trên **cảm biến giả định** (P4-C3, P4-C4; PDF pp. 5–6). Kim (2018) không có constraint nào (P2 component audit). |
| **Thesis evidence required** | Constraint Catalogue đã baseline (§7); Fixture/Oracle Manifest với ít nhất một negative fixture cho mỗi trong bảy họ CC-1…CC-7; tiêu chí pass/fail đăng ký **trước** khi chạy; log thực thi |
| **Limitation** | Chưa có fixture nào tồn tại. Từ vựng vòng đời cho CC-6 là `GOVERNANCE_DECISION_REQUIRED`. Kiểm chứng chỉ trong RDF chịu vấn đề OWA (P5-C7) |
| **Validation obligation** | G3: thực thi toàn bộ manifest; báo cáo cả pass và fail; không được im lặng sửa fixture sau khi thấy kết quả |
| **Current status** | `CANDIDATE — literature boundary supported, thesis evidence not produced` |

### C3 — Quản trị provenance và model version cho liên kết cấp cấu kiện

**Phát biểu.** Mỗi cạnh cấp cấu kiện mang provenance của chính liên kết (asserted hay derived) và được neo vào một phiên bản model xác định.

| Trường | Nội dung |
|---|---|
| **Literature evidence** | Jia (2025): railing không có liên kết không gian trực tiếp, containment phải **suy ra** từ bounding box (P3-C9; PDF p. 21). Kim (2018): đường liên kết cấu kiện được **chọn** là `IfcRelSpaceBoundary` (P2-C5; PDF p. 7 [179]). Kim (2018) dùng số instance IFC, không `GlobalId` (P2 component audit). Pauwels (2016) không bàn tính bền định danh trên các trang đã soi (P5 component audit). Kim nêu BIM model hiếm được cập nhật trong thực hành FM (P2-C13; PDF p. 13 [185]) — **hỗ trợ bối cảnh, không phải phát biểu về quản trị phiên bản** (P2-C14). |
| **Thesis evidence required** | Thuộc tính `Link_Provenance` (`asserted` \| `derived`) + `Derivation_Rule` trên mọi cạnh có kiểu; ràng buộc CC-7; ràng buộc CC-4 cho stale crosswalk; quyết định governance chấp nhận thuộc tính này vào ER model |
| **Limitation** | `Link_Provenance` hiện là **đề xuất chưa duyệt** (§9, S-P2). `Model_Version_ID` **đã** được Charter §2.2 khóa như bối cảnh định danh cấu kiện trong G2 — nó **không** là phát hiện của Round 4 và **không** được thêm vào canonical chain như một mắt xích mới |
| **Validation obligation** | G3: negative fixture cho mỗi loại cạnh derived; test stale-crosswalk; chứng minh quy tắc suy dẫn tái tạo được |
| **Current status** | `CANDIDATE — literature boundary supported, schema decision pending governance approval` |

**Không gộp ba đóng góp này thành một tuyên bố novelty duy nhất.** Mỗi cái có literature evidence riêng, nghĩa vụ chứng minh riêng và trạng thái riêng.

---

## 9. Schema decisions

### 9.1 LOCKED (do governance đã accepted, không do Round 4)

| ID | Quyết định | Nguồn |
|---|---|---|
| S-L1 | Chuỗi định danh lõi: `Sensor_ID → BIM_GUID → Condition_Evidence_ID → Inspection_Record_ID → Action_Record_ID` | Charter v2.1 §2.2 |
| S-L2 | `Action_Status` / `Workflow_Status` là **current-state projection/attribute** của `Action_Record_ID`, **không phải mắt xích định danh** | Charter v2.1 §2.2; ADR ACTION_ID 20260719 (ACCEPTED) |
| S-L3 | Bối cảnh định danh cấu kiện trong G2 phải giữ `Asset_ID`, `BIM_GUID`, `Model_Version_ID` | Charter v2.1 §2.2 |
| S-L4 | Không thêm `Component_ID` vào canonical chain; database surrogate key chỉ là technical key | Charter v2.1 §2.2 |
| S-L5 | CEI là first-class attribute của `Condition_Evidence_ID`, cấu trúc metadata, không phải scalar/Health Index/severity | Charter v2.1 §7 |
| S-L6 | `FEM_Node_ID` chỉ là optional metadata, không bao giờ là mắt xích bắt buộc | Charter v2.1 §2.2 |
| S-L7 | `completed` không tự động là verified closure; recommendation không tự động là `Action_Record` | Charter v2.1 §2.4; ADR draft §Proposed 6 |

**Ghi chú quan trọng về `Model_Version_ID`.** v1.0 phát biểu "`Model_Version_ID` is mandatory, not optional metadata" như một kết luận rút từ Kim (2018). Đây là **định tuyến sai**. `Model_Version_ID` đã được Charter §2.2 khóa như **bối cảnh định danh cấu kiện bắt buộc trong G2**. Kim (2018) chỉ cung cấp **lý lẽ hỗ trợ về thực hành**, và ngay cả lý lẽ đó cũng là `THESIS-APPLICATION` chứ không phải `AUTHOR-STATED` (P2-C14). Không được trình bày điều này như một phát hiện của Round 4.

### 9.2 PROPOSED — chưa được phê duyệt

| ID | Quyết định đề xuất | Trạng thái | Cơ sở literature |
|---|---|---|---|
| S-P1 | Đặc tả G2 phải **implementation-neutral** (không ràng buộc vào ifcOWL hay bất kỳ serialization nào) | **`THESIS-APPLICATION` — proposed design decision, pending schema governance approval** | P5-C1, P5-C2, P5-C3 (`SOURCE-VERIFIED`) |
| S-P2 | Mọi cạnh có kiểu mang thuộc tính `Link_Provenance` (`asserted` \| `derived`) + trường `Derivation_Rule` bắt buộc khi `derived` | **`THESIS-APPLICATION` — proposed design decision, pending schema governance approval** | P3-C9, P2-C5 (`SOURCE-VERIFIED`) |
| S-P3 | Constraint Catalogue được soạn độc lập với serialization, kèm ghi chú lớp `RULE`/`WHERE` không thừa kế qua ifcOWL | **`THESIS-APPLICATION` — proposed design decision, pending schema governance approval**; cần nguồn xác nhận thứ hai | P5-C3 (`SOURCE-VERIFIED`, một nguồn) |
| S-P4 | CQ Registry, Validation Test Registry, Constraint Catalogue là **ba artifact tách biệt** | **`THESIS-APPLICATION` — proposed design decision, pending schema governance approval** | P1-C4 (`SOURCE-VERIFIED`) |
| S-P5 | Mỗi VCQ mang `Expressivity_Check` (`Lv ⊆ Lo`) | **`THESIS-APPLICATION` — proposed design decision, pending schema governance approval** | P1-C3 (`SOURCE-VERIFIED`); tác giả tự nhận ràng buộc "may appear debatable" |
| S-P6 | `Status_Event` / `Status_Event_ID` là nguồn lịch sử append-only | **`PROPOSED — NOT YET ACCEPTED`** | `ADR_ACTION_STATUS_EVENT_20260804_DRAFT.md` |

### 9.3 UNRESOLVED — `GOVERNANCE_DECISION_REQUIRED`

| ID | Vấn đề | Thẩm quyền cần |
|---|---|---|
| S-U1 | Từ vựng vòng đời và tập chuyển trạng thái hợp lệ (điều kiện tiên quyết cho CC-6) | Expert review + supervisor acceptance |
| S-U2 | Cardinality chính xác giữa `Inspection_Record` và `Action_Record` | Expert review |
| S-U3 | Ma trận role/permission và phân tách nhiệm vụ | Expert review |
| S-U4 | `Verification_Record` là thực thể riêng hay subtype của `Inspection_Record` | Expert review + supervisor acceptance |
| S-U5 | Tiêu chí verification và quy tắc closure/reopen chính xác | Expert review |
| S-U6 | Trường ràng buộc payload của G1 | Cần G1 payload đã được chấp nhận |
| S-U7 | Con số về `asserted` vs `derived` link trong ER model thực tế của luận án | Chưa có ER model baseline |

---

## 10. Claim → Evidence → Limitation → Next action

**Claim.** *Trong các bài đã deep-read ở Rounds 1–4*, không nghiên cứu nào công bố đồng thời: (a) một CQ registry có gán type với hình dạng câu trả lời kỳ vọng, (b) một bộ test kiểm chứng có fixture hợp lệ và không hợp lệ với tiêu chí đạt/không đạt định trước, (c) một constraint catalogue có họ toàn vẹn tham chiếu, và (d) khai báo provenance của liên kết (asserted vs derived) cho từng loại cạnh — trên một chuỗi `Condition_Evidence_ID → BIM_GUID → Inspection_Record_ID → Action_Record_ID` hoàn chỉnh.

**Evidence.**
- Keet & Khan (2025) cung cấp typology CQ và tách tường minh constraint query khỏi CQ, nhưng **không** có acceptance semantics và **không** có đánh giá dựa trên người dùng — PDF pp. 4–5 §3.2 Def. 1–3; PDF p. 11 §4.2; PDF p. 13 §6.
- Kim (2018) liên kết work record với đối tượng IFC, **không** identity governance (dùng số instance, không `GlobalId`), **không** constraint, **không** truy vấn ngược — PDF pp. 4, 7, 9–14 [176, 179, 181–186].
- Jia (2025) chạy rule thật trên Fuseki, **không** có họ rule toàn vẹn tham chiếu và **không** có fixture gieo — PDF pp. 11, 16, 20–21, 23.
- Lee, D. (2021) gieo 3/10 node không hợp lệ với kết quả kỳ vọng, nhưng cho **đồng thuận sổ cái** trên **cảm biến giả định**, và các node đó vẫn đồng bộ ở 3.42 s theo quy tắc 51% — PDF pp. 2–3, 5–6, 8.
- Pauwels & Terkaj (2016) nêu rõ lớp `RULE`/`FUNCTION` của IFC **không** chuyển được sang OWL2 DL và `WHERE` rule **không** nằm trong conversion — PDF p. 33 [132] §6; PDF p. 5 [104] §1.3.4.

**Limitation.**
1. Đây là kết luận **bị chặn theo corpus** (4 + 4 + 4 + 2 + 5 bài), **không** phải tuyên bố về tài liệu. `CLOSE_SEARCH` từ Round 3B là corpus-bounded và không phải quyết định Gate.
2. Bellon et al. (2025) vẫn bị paywall ở mức entity (R1) và có thể chồng lấn.
3. Hình vẽ trong cả năm bài Round 4 **không** được kiểm tra như nguồn nội dung độc lập; các claim dựa hoàn toàn vào nội dung hình được ghi `Evidence is currently insufficient.`
4. Các trang PDF chưa soi trực quan liệt kê ở §3.2 — mọi claim neo vào đó giữ nhãn provisional.
5. Sáu PDF trong `DEEP_READ_20.07.2026` (Boje, Chen, Johannes, Yang và hai bản trùng) chưa deep-read.
6. **Cảnh báo tên file (giữ nguyên từ v1.0):** file `Lee et al. (2021) — Provenance và accountability.pdf` là **Dongmin Lee et al., DT + blockchain**, khác với **Lee, Y.-C., Eastman & Solihin (2021)**, *JCDE* 8(1) từ Round 1. Hai citation "Lee et al. (2021)" cùng tồn tại trong evidence base. Phải phân biệt citation key trước mọi bản thảo Paper 2.
7. Ba artifact ở §5, §6, §7 và ba candidate contribution ở §8 đều là `THESIS-APPLICATION`. **Chưa artifact nào được xây, chạy hay duyệt.**

**Next action.**

1. Đưa ba artifact §5/§6/§7 vào Stream B của `CURRENT_STATUS_AND_NEXT_DIRECTION.md` như **draft chưa duyệt**; xin quyết định governance cho S-P1…S-P5 trước khi xây.
2. Giải quyết S-U1 (từ vựng vòng đời) vì CC-6 không soạn được nếu thiếu.
3. Tìm **nguồn xác nhận thứ hai** cho việc mất lớp ràng buộc khi chuyển IFC→OWL (TV-1) trước khi coi S-P3 là ổn định.
4. Phân biệt hai citation "Lee et al. (2021)" trên toàn bộ evidence base.
5. Quyết định Boje (2020), Chen (2026), Johannes (2021), Yang (2025) là Round 5 hay chỉ là background Chương 2. **Không** mở lại `CLOSE_SEARCH` nếu không có trigger được phát biểu rõ.
6. Hoàn tất targeted verification còn thiếu ở §13.

**Gate status.** Record này **không** thay đổi trạng thái Gate nào. G1 = `OPEN — PARTIAL EVIDENCE`. G2 = `OPEN — LITERATURE BOUNDARY CLOSED, SPECIFICATION NOT YET FROZEN`. G3 = `OPEN — NOT IMPLEMENTED, NOT VALIDATED, NOT OFFICIALLY PASSED`, execution `NOT OPEN`. **Không artifact nào trong record này là validation evidence.**

---

## 11. Những nội dung đủ dùng cho G2

Dùng được **như literature evidence** trong đặc tả và trong phần lập luận thiết kế của Paper 2:

| # | Nội dung | Neo bằng chứng |
|---|---|---|
| 1 | Gap statement: thiếu hướng dẫn soạn và đánh giá CQ | P1-C1 |
| 2 | Yêu cầu **gán type** cho mỗi CQ (SCQ/VCQ/FCQ/RCQ/MpCQ) | P1-C2 |
| 3 | Yêu cầu VCQ phải formalisable + answerable + `Lv ⊆ Lo` | P1-C3 |
| 4 | Cơ sở học thuật để **tách** CQ Registry khỏi Constraint Catalogue | P1-C4 |
| 5 | Checklist rà chất lượng CQ theo bốn nguyên nhân hỏng + mẫu câu hỏi có vấn đề | P1-C5, P1-C6 |
| 6 | Tương đồng ngữ nghĩa Maintenance (atelic) vs Repair cho `Action_Record` | P1-C9 |
| 7 | Gap statement: FMS DB dựa hoạt động vs BIM dựa đối tượng | P2-C1 |
| 8 | Cảnh báo: cấu kiện mà evidence gắn vào phụ thuộc **đường quan hệ IFC được chọn** | P2-C5 |
| 9 | Cảnh báo: demo liên kết trên model mẫu ≠ correspondence đã kiểm chứng | P2-C7 |
| 10 | Khung soạn rule ba phần (constrained object / content / precondition) | P3-C1 |
| 11 | Rule typology (property / construction / spatial) và nhận định luận án cần thêm họ toàn vẹn tham chiếu | P3-C2, P3-C5 |
| 12 | Cảnh báo: liên kết **suy ra** (bounding box) cần integrity test riêng | P3-C9 |
| 13 | Giới hạn scalability và locale-binding của rule engine dựa Jena | P3-C10 |
| 14 | Gap statement: lịch sử trạng thái của virtual asset dễ mất | P4-C1 |
| 15 | Nguyên lý tách attestation record khỏi evidence payload | P4-C2 |
| 16 | Lý do **không** nhận blockchain: trilemma + nghĩa vụ chứng minh không phục vụ RQ2 | P4-C6 |
| 17 | Cơ sở giữ đặc tả G2 độc lập serialization | P5-C1, P5-C2 |
| 18 | **Lớp ràng buộc IFC không sống sót qua ifcOWL** → integrity rule phải soạn riêng | P5-C3, P5-C4 |
| 19 | Cảnh báo CWA vs OWA khi chỉ kiểm chứng trong RDF | P5-C7 |

---

## 12. Những nội dung chưa được phép tuyên bố

| # | Không được tuyên bố | Lý do |
|---|---|---|
| 1 | "Kim (2018) chứng minh liên kết cấp cấu kiện tăng recall 200%" | Không có suy dẫn, mẫu số, baseline hay bất định (P2-C12). `Evidence is currently insufficient.` |
| 2 | "Jia (2025) chứng minh Jena nhanh hơn SWRL" | Không có so sánh đo được (P3-C4). `Evidence is currently insufficient.` |
| 3 | "Jia (2025) đã thực hiện negative test" | Hai railing 900 mm là dữ liệu thật, không phải fixture gieo có expected outcome (P3-C7) |
| 4 | "Lee, D. (2021) là bằng chứng hiện trường" | Cảm biến giả định, mô phỏng (P4-C3) |
| 5 | "Luận án là bài đầu tiên làm X" | Novelty bị chặn theo corpus Rounds 1–4; `CLOSE_SEARCH` là corpus-bounded, không phải universal absence |
| 6 | "Round 4 chứng minh `Model_Version_ID` là bắt buộc" | `Model_Version_ID` do Charter §2.2 khóa; Kim chỉ hỗ trợ bối cảnh và ở mức `THESIS-APPLICATION` (P2-C14) |
| 7 | "`Link_Provenance` là quyết định schema đã chốt" | `THESIS-APPLICATION`, chờ phê duyệt (S-P2) |
| 8 | "Implementation-neutrality là ràng buộc đã chốt của G2" | `THESIS-APPLICATION`, chờ phê duyệt (S-P1) |
| 9 | "Asserted-vs-derived linkage đã được xác nhận là novelty" | Chỉ là `candidate contribution` C3; chưa có evidence matrix đầy đủ |
| 10 | "Ba artifact CQ/Test/Constraint đã được kiểm chứng" | Chưa xây, chưa chạy, chưa duyệt |
| 11 | Chuỗi định danh kết thúc bằng `Action_Status` hoặc `Status_Event` | Trái Charter §2.2; `Status_Event` là `PROPOSED — NOT YET ACCEPTED` |
| 12 | Bất kỳ tuyên bố nào dựa trên FEM hiệu chuẩn, chẩn đoán hư hỏng, RUL, predictive maintenance, Health Index trọng số | Charter §10 Prohibited |
| 13 | "Record này là immutable evidence record" | Còn claim provisional và trang PDF chưa soi (§13) |
| 14 | "Round 4 đóng Gate 2" hoặc "Round 4 mở Gate 3" | Literature evidence không phải validation evidence |

---

## 13. Targeted verification còn thiếu

Chỉ ba hướng targeted verification được phép (không mở lại tìm kiếm diện rộng):

### 13.1 Constraint preservation

| ID | Cần xác minh | Trạng thái hiện tại | Cách xác minh |
|---|---|---|---|
| TV-1 | Lớp `RULE`/`FUNCTION`/`WHERE` của IFC không được bảo toàn qua chuyển đổi sang OWL — cần **nguồn thứ hai** | Một nguồn: P5-C3 (`SOURCE-VERIFIED`) | Truy Terkaj & Šojić (được P5 dẫn ở §6) và các trang §3 của P5 (PDF pp. 7–27, chưa soi) |
| TV-2 | Có hay không một cơ chế được công bố để tái tạo ràng buộc EXPRESS trong RDF (SHACL hoặc tương đương) trong corpus hiện có | `UNKNOWN` — SHACL chỉ được P3 nhắc trong related work (P3-C11) | Soi P3 PDF pp. 1–3 (§2 related work) và Boje (2020) nếu được đưa vào Round 5 |
| TV-3 | Tables 4–6 của P3 (mapping rule) có hay không chứa rule toàn vẹn tham chiếu | `TEXT-EXTRACTION-VERIFIED — provisional pending PDF visual audit` | Soi P3 PDF pp. 12–15 |

### 13.2 Version governance

| ID | Cần xác minh | Trạng thái hiện tại | Cách xác minh |
|---|---|---|---|
| TV-4 | Có bài nào trong corpus xử lý tính bền của `GlobalId` qua các phiên bản model | `UNKNOWN`; P5 không đề cập trên trang đã soi | Soi P5 PDF §3.6 (pp. ~20–27) và Antunes (2024) từ Round 1 |
| TV-5 | Kim (2018) có bất kỳ trường phiên bản nào trong record schema không | Table 2 (PDF p. 9 [181]) không có; cần xác nhận không có ở nơi khác | Soi P2 PDF pp. 5–6, 8, 15 |
| TV-6 | Năm ban hành của `GB-50096` mà P3 dùng | `UNKNOWN` (V-14) | Soi P3 reference [46] ở PDF pp. 23–25 |

### 13.3 Asserted versus derived linkage

| ID | Cần xác minh | Trạng thái hiện tại | Cách xác minh |
|---|---|---|---|
| TV-7 | Fig. 15 của P3 (cơ chế xác định vị trí không gian + Jena rule tương ứng) có phát biểu integrity test cho liên kết suy ra không | `Evidence is currently insufficient.` — hình chưa soi | Soi P3 PDF p. 21–22, Fig. 15 |
| TV-8 | Kim (2018) có nêu trường hợp `IfcRelSpaceBoundary` thất bại hay không, và xử lý thế nào | `UNKNOWN` | Soi P2 PDF pp. 5–6, 8 |
| TV-9 | Có bài nào trong corpus khai báo provenance của **liên kết** (khác với provenance của **dữ liệu**) như một nghĩa vụ schema | `UNKNOWN` — Çelik et al. (2023) từ Round 3B là ứng viên gần nhất | Rà lại record Round 3B; nếu không đủ, soi Çelik PDF |

**Không có hạng mục nào ở trên được coi là đã giải quyết trong bản v1.1.**

---

## 14. Change log v1.0 → v1.1

| # | Nhóm | Thay đổi |
|---|---|---|
| 1 | Nhãn tài liệu | Bỏ "(immutable once accepted)". Trạng thái đổi thành "PROVISIONAL IN PART" vì còn claim provisional và trang PDF chưa soi |
| 2 | **A — Kiểm chứng nguồn** | Render và soi trực quan **31 trang PDF** trên 5 bài; lập §3.2 liệt kê chính xác trang đã soi và trang chưa soi |
| 3 | A | Bổ sung `[printed p.]` cho Kim (2018) (+172) và Pauwels (2016) (+99); lập bảng ánh xạ trang ở §3.1 |
| 4 | A | Áp nhãn ba mức `SOURCE-VERIFIED` / `TEXT-EXTRACTION-VERIFIED — provisional pending PDF visual audit` / `READER-INFERRED` cho từng claim |
| 5 | A | **Sửa lỗi nội dung V-11:** kiến trúc lưu trữ của Lee, D. (2021) bị mô tả ngược trong v1.0. Blockchain chính là distributed ledger và chỉ chứa compliance statement; dữ liệu sensor/BIM **không** lên ledger |
| 6 | A | **Sửa lỗi kết quả V-12:** node không hợp lệ là #3, #7, #10; chúng bị loại khỏi cơ chế đồng thuận nhưng vẫn đồng bộ ở 3.42 s theo quy tắc 51% |
| 7 | A | **Sửa lỗi sự kiện V-13:** Jia Table 3 **có** cột `Rule NO.`; v1.0 ghi "no rule IDs" là sai |
| 8 | A | **Gỡ trích dẫn không kiểm chứng V-14:** "GB 50096-2011" → `GB-50096`, năm = `UNKNOWN` |
| 9 | A | Sửa 6 locator (V-15, V-17, V-19, V-20) và bổ sung attribution Hoang & Törmä (V-21) |
| 10 | A | Hạ hai diễn giải xuống `READER-INFERRED` (V-16 furniture; V-18/P2-C8 diễn giải ngày) |
| 11 | A | Bổ sung dữ kiện mới đã kiểm chứng: IFC4_ADD1.exp có 2 `RULE` + 45 `FUNCTION` (P5-C4); SHACL xuất hiện trong related work của P3 (P3-C11); vật liệu hoàn thiện chia 4 plasterboard / 3 paint (P2-C9) |
| 12 | **B — Cấu trúc CQ** | Tách một khối CQ của v1.0 thành **ba artifact độc lập**: §5 CQ Registry, §6 Validation Test Registry, §7 Constraint Catalogue |
| 13 | B | CQ Registry phủ đủ năm type SCQ/VCQ/FCQ/RCQ/MpCQ; **bỏ** yêu cầu mọi CQ phải có expected answer và fixture |
| 14 | B | Validation Test Registry chỉ nhận VCQ; có `Query_Direction`, `Expected_Answer`, `Fixture_Ref`, `Pass_Fail_Criterion`; forward/reverse **chỉ áp dụng khi có nghĩa hai chiều** (bảng ở §6) |
| 15 | B | Constraint Catalogue liệt kê **bảy họ** CC-1…CC-7 (orphan, duplicate, wrong target, stale crosswalk, conflicting binding, illegal status transition, derived-link integrity), mỗi họ có negative fixture và expected failure |
| 16 | B | Ghi rõ constraint-checking query **không** được đăng ký như competency question (neo P1-C4) |
| 17 | **C — Hạ mức quyết định** | `Model_Version_ID is mandatory` → định tuyến lại: **LOCKED bởi Charter §2.2** (S-L3), không phải phát hiện Round 4; lý lẽ từ Kim hạ xuống `THESIS-APPLICATION` |
| 18 | C | "mọi edge phải có `Link_Provenance`" → `THESIS-APPLICATION — proposed design decision, pending schema governance approval` (S-P2) |
| 19 | C | "G2 bắt buộc implementation-neutral" → `THESIS-APPLICATION — proposed design decision, pending schema governance approval` (S-P1) |
| 20 | C | "asserted-versus-derived linkage đã được xác nhận là novelty" → chỉ còn `candidate contribution` C3 |
| 21 | C | Khôi phục chuỗi định danh lõi đúng Charter §2.2 (kết thúc `Action_Record_ID`); gắn nhãn `Status_Event` = `PROPOSED — NOT YET ACCEPTED`; ghi cảnh báo `Action_Status`-as-chain là ký hiệu lịch sử không được lan truyền (§2.1). Không thêm identifier mới vào chuỗi lõi |
| 22 | C | Bổ sung §9.3 liệt kê 7 hạng mục `GOVERNANCE_DECISION_REQUIRED` |
| 23 | **D — Contribution** | Tách một novelty claim dài của v1.0 thành **ba candidate contribution** C1, C2, C3, mỗi cái có bảng đủ 6 cột: Candidate contribution / Literature evidence / Thesis evidence required / Limitation / Validation obligation / Current status |
| 24 | D | Chỉ dùng thuật ngữ `candidate contribution`; bỏ mọi ngôn ngữ novelty cuối cùng |
| 25 | Cấu trúc | Tái cấu trúc thành đúng 14 mục theo yêu cầu audit |
| 26 | Phạm vi | Bổ sung §11 (đủ dùng cho G2), §12 (chưa được phép tuyên bố), §13 (targeted verification còn thiếu, 9 hạng mục TV-1…TV-9) |
| 27 | Gate | Xác nhận **không** thay đổi trạng thái Gate; **không** sửa file quản trị nguồn; **không** mở lại tìm kiếm diện rộng |
| 28 | Giữ nguyên | Cảnh báo tên file hai "Lee et al. (2021)" được giữ nguyên từ v1.0 (§10 Limitation 6) |

---

**Hết ROUND 4 — VERIFIED EVIDENCE RECORD v1.1.**
Bản v1.0 `G2_G3_ROUND4_CQ_CONSTRAINT_ACCOUNTABILITY_DEEP_READ_20260809.md` được giữ nguyên không sửa đổi làm nguồn lịch sử.
