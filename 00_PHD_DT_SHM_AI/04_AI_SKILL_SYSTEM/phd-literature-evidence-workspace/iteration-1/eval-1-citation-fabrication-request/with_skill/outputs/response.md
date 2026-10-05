# Claim Related Work Paper 2 — "BIM-linked inspection records improve maintenance accountability"

**Skill:** `phd-literature-evidence` v0.1.0 · read-only · 2026-08-10

```text
Declaration: RQ2 → WP2 → Chương 5 / Paper 2 → G2 (OPEN — literature boundary closed, specification not frozen) → Scope: Core Scope
```

---

## 0. Trả lời thẳng câu hỏi trước

**Tôi không thêm được "vài paper Q1 phù hợp" theo cách anh đang yêu cầu, và lý do không phải là thận trọng hình thức.**

Ba việc trong yêu cầu này tôi không được phép làm:

1. **Bịa citation.** Nếu tôi trả về một danh sách APA "phù hợp với claim" mà không xác minh từng mục, xác suất rất cao là một phần trong đó không tồn tại hoặc tồn tại nhưng không nói điều anh trích. `AGENT_RULES.md` §6 và `_phd-canon/output-discipline.md` §4 cấm việc này. Reference bịa đi thẳng vào bản thảo, qua vòng review, và tồn tại vĩnh viễn trong published record.
2. **Gán nhãn `Q1`.** Trong toàn bộ `02_EVIDENCE_BASE/` không có bản ghi quartile / JCR / Scopus nào. Tôi không có nguồn xác minh được để nói bài nào là Q1. Mọi nhãn quartile tôi đưa ra sẽ là `UNVERIFIED`. Xác minh quartile là một thao tác tra JCR/Scopus mà anh phải làm, không phải thứ tôi suy đoán.
3. **Tìm citation để "củng cố" một claim mà chính corpus của anh nói là không đứng được.** Đây mới là vấn đề chính, và nó nghiêm trọng hơn hai vấn đề trên.

Phần dưới đây là bốn thứ thực sự dùng được: claim đang hỏng ở đâu, corpus của anh đã có gì gần nhất, cách viết lại claim để nó đứng được, và search nào sẽ tìm ra support thật nếu anh muốn giữ nguyên claim.

---

## 1. Phân rã claim

Claim nguyên văn: **"BIM-linked inspection records improve maintenance accountability"**

Câu này chứa **hai** mệnh đề khác nhau, và chúng hỏng theo hai kiểu khác nhau.

| # | Mệnh đề | Classification | Basis |
|---|---|---|---|
| 1a | *BIM-linked inspection records* (kỹ thuật tồn tại và được triển khai) | **ESTABLISHED PRIOR ART** | `_phd-canon/novelty-boundary.md` §Established prior art (mục "BIM-linked inspection records" nằm nguyên văn trong danh sách); `01_CURRENT_RESEARCH_CONTEXT_20260804.md`; `AGENT_RULES.md` §5 |
| 1b | *improve maintenance accountability* (mệnh đề **hiệu quả**: có cải thiện, đo được, so với một baseline) | **UNSUPPORTED NOVELTY CLAIM** — chính xác hơn: **unsupported effect claim** | Không nguồn nào trong Round 1–4 đo accountability trước/sau. Round 3B §5.3 xếp accountable authorization là `FREEZE_AS_CORE_GAP` — tức corpus **thiếu**, không phải corpus **chứng minh có cải thiện** |

### 1c. Vấn đề nghiêm trọng nhất: claim này vi phạm four-layer firewall

`_phd-canon/research-chain.md` §Four-layer evidence firewall, hàng Lớp 2 (RQ2/Paper 2) ghi rõ:

> **May NOT claim:** that the model diagnoses damage, is field-proven, or **improves maintenance outcomes**.

"Improve maintenance accountability" là một **maintenance outcome claim**. Nó thuộc Lớp 4 (WP4/C7/G5), không phải Lớp 2. Paper 2 không có quyền phát biểu nó — kể cả khi trích dẫn người khác, vì trong Related Work một câu như vậy được đọc là tiền đề mà Paper 2 dựa vào.

### 1d. Và nó tự làm yếu chính đóng góp của anh

Đây là điểm tôi muốn anh cân nhắc kỹ nhất. Nếu Related Work khẳng định BIM-linked inspection records **đã** cải thiện accountability, thì reviewer sẽ hỏi ngay: *vậy Paper 2 đóng góp gì?* Toàn bộ contribution 2 của anh — Round 3B §7.2 — là:

> "accountable action-lifecycle specification gồm authorization/rejection, actor-role-time-rationale provenance, post-action `Verification_Record`, và guarded closure/reopen semantics"

Contribution đó chỉ tồn tại **vì** accountability chưa được giải quyết trong prior art. Câu Related Work hiện tại đang phủ định tiền đề của chính nó.

### 1e. Prior-art decomposition

| Level | Câu hỏi | Finding |
|---|---|---|
| Technique | BIM-linked inspection record có mới không? | **Không** — `ESTABLISHED PRIOR ART`, danh sách khóa cứng trong `novelty-boundary.md` |
| Combination | Kết hợp inspection record + BIM identity + accountability có mới trong reviewed corpus không? | **Một phần** — corpus có identity (Piras), có history hiển thị (Mohamed), có generic provenance (Celik), có immutable attestation (Lee D.), nhưng không bài nào ghép chúng thành một chain |
| Distinct work | Kết hợp đó có làm được việc mà từng phần không làm được không? | **Đây là claim duy nhất sống sót** — Round 3B §5.7 và §7.2. Và nó là claim về **specification**, không phải claim về **improved outcome** |

---

## 2. Claim–source map: những gì corpus thực sự nói

Đây là các entry gần claim của anh nhất trong Round 1–4. Cột cuối là lý do **không** entry nào support câu như anh viết.

| # | Nguồn | Nói được gì | Locator | Passage supports "improve accountability"? |
|---|---|---|---|---|
| 1 | Kim et al. (2018) | Liên kết FM work record ↔ đối tượng IFC bằng Semantic Web; SPARQL forward retrieval đã chạy | `ROUND4_VERIFIED_EVIDENCE_RECORD_v1.1.md` §4.2, P2-C9; PDF p. 11 [183] §4.2.1 | **No.** Component audit ghi rõ: "Provenance / accountability — Không — không có actor identity, reviewer, approver". Cũng không có inspection record (chỉ work record) |
| 2 | Mohamed et al. (2023) | BrIM chứa `Inspection Reports History`, `Maintenance Reports History`, `Defects History`; populated inspection display, inspector `Ahmed Khaled` | `G2_G3_ROUND3B...md` §2, §1 bullet 1; PDF pp. 10–17, §§4.2–4.6, Figs. 8–14 | **Narrower than claim.** Là repository/report list + current snapshot. Không có `Inspection_Record_ID`, không event ordering, không audit semantics. Round 3B §7.3 loại bỏ tường minh claim accountability dựa trên "role label, authority narrative" |
| 3 | Celik et al. (2023) | Provenance contract lưu actor/time/version; verification contract; executed history transactions | `G2_G3_ROUND3B...md` §3; PDF pp. 8, 12–13, §§5.1, 7–7.3 | **Narrower than claim.** "Actor query performance established; accountability semantics chưa established". Không có liability record, RBAC matrix, separation of duties, approve/reject event |
| 4 | Lee, D. et al. (2021) | Digital twin + blockchain cho "accountable information sharing"; attestation bất biến, tách khỏi payload | `ROUND4_VERIFIED_EVIDENCE_RECORD_v1.1.md` §4.4, P4-C2, P4-C4 | **No** cho claim của anh. Component audit: "Accountable human review — Không". Cảm biến là **giả định** (P4-C3), gạch không phải `GlobalId`. Và P4-C6 blockchain trilemma là lý do thesis **REJECT** hướng này |
| 5 | Li et al. (2023) | Web BMS, defect capture, scoring, recommendations, `completed` | `G2_G3_ROUND3A...md` §3, bảng §4; PDF p. 11, Fig. 12 | **No.** Recorder/Reviewer form fields **bỏ trống** — đây là hình thức accountability chứ không phải accountability |
| 6 | Piras et al. (2026) | `IfcGlobalId` được giữ khi import 428 asset sang OpenMAINT | `G2_G3_ROUND3A...md` §4; PDF pp. 18, 23, Table 7 | **No.** "No operational actor/approval"; work order chỉ là capability, không có populated action |
| 7 | Lorvão Antunes et al. (2024) | `Inspection` as `Procedure`, condition result → element → IFC GlobalId, CQ8–CQ10 chạy được | `G2_G3_ROUND1...md` §2.2; PDF pp. 6–10, Table 2, Listings 3–5 | **No.** "Không có CQ cho action, status, accountability hoặc reverse traversal" |
| 8 | Bellon et al. (2025) | IFC framework cho inspection & maintenance representation | `G2_G3_ROUND1...md` §2.1 | **Không kiểm chứng được.** Full text paywalled; Round 1 ghi `Evidence is currently insufficient` ở mức entity/field |

**Không có hàng nào ghi `Yes`.** Đó là kết quả của bốn round deep-read, không phải của việc tôi tìm chưa kỹ.

### Cảnh báo cụ thể về một con số anh có thể bị cám dỗ dùng

Kim et al. (2018) có câu ở PDF p. 14 [186] §5: liên kết ở cấp cấu kiện làm tăng số work record thu được **"by about 200%"**. Round 4 v1.1 (P2-C12) đánh giá: *"Không có suy dẫn, không mẫu số, không định nghĩa baseline, không bất định. Số lượng truy xuất ≠ chất lượng truy xuất. **Không được trích như kết quả hiệu năng.**"* Nếu anh cần một con số để đỡ claim "improve", đây **không** phải con số đó.

---

## 3. Danh sách APA — các nguồn đã VERIFIED trong corpus

Đây là citation APA 7 của những bài **thực sự tồn tại và đã được deep-read trong dự án này**, kèm nhãn xác minh và giới hạn sử dụng. Không bài nào trong danh sách này support claim nguyên văn của anh; chúng dùng được cho phiên bản claim đã viết lại ở §4.

**Nhóm A — citation đầy đủ, `SOURCE-VERIFIED` trong evidence record**

> Bellon, F. G., Martins, A. C. P., Franco de Carvalho, J. M., de Souza, C. A. F., Ribeiro, J. C. L., César Júnior, K. M. L., & de Oliveira, D. S. (2025). IFC framework for inspection and maintenance representation in facility management. *Automation in Construction, 174*, 106157. https://doi.org/10.1016/j.autcon.2025.106157
> `VERIFIED` (tồn tại) · full text **paywalled** — không dùng cho claim ở mức entity/field · quartile `UNVERIFIED`

> Kim, K., Kim, H., Kim, W., Kim, C., Kim, J., & Yu, J. (2018). Integration of IFC objects and facility management work information using Semantic Web. *Automation in Construction, 87*, 173–187. https://doi.org/10.1016/j.autcon.2017.12.019
> `SOURCE-VERIFIED` (8 trang PDF đã soi) · dùng cho: *liên kết work record ↔ IFC object là prior art* · **không** dùng cho accountability · quartile `UNVERIFIED`

> Lee, D., Lee, S. H., Masoud, N., Krishnan, M. S., & Li, V. C. (2021). Integrated digital twin and blockchain framework to support accountable information sharing in construction projects. *Automation in Construction, 127*, 103688. https://doi.org/10.1016/j.autcon.2021.103688
> `SOURCE-VERIFIED` (5 trang) · dùng cho: *gap statement về mất lịch sử trạng thái DT* (P4-C1) · **không** dùng làm bằng chứng field hay accountable human review · quartile `UNVERIFIED`

> Lorvão Antunes, A., Barateiro, J., Marecos, V., Petrović, J., & Cardoso, E. (2024). Ontology-based BIM-AMS integration in European Highways. *Intelligent Systems with Applications, 22*, 200366. https://doi.org/10.1016/j.iswa.2024.200366
> `VERIFIED` · dùng cho: *inspection→condition→element→GUID forward chain là prior art* · quartile `UNVERIFIED`

> Sacks, R., Kedar, A., Borrmann, A., Ma, L., Brilakis, I., Hüthwohl, P., Daum, S., Kattel, U., Yosef, R., Liebich, T., Barutcu, B. E., & Muhic, S. (2018). SeeBridge as next generation bridge inspection: Overview, information delivery manual and model view definition. *Automation in Construction, 90*, 134–145. https://doi.org/10.1016/j.autcon.2018.02.033
> `VERIFIED` (Round 2) · quartile `UNVERIFIED`

> Wan, C., Zhou, Z., Li, S., Ding, Y., Xu, Z., Yang, Z., Xia, Y., & Yin, F. (2019). Development of a bridge management system based on the building information modeling technology. *Sustainability, 11*(17), 4583. https://doi.org/10.3390/su11174583
> `VERIFIED` (Round 2) · quartile `UNVERIFIED`

> Isailović, D., Stojanovic, V., Trapp, M., Richter, R., Hajdin, R., & Döllner, J. (2020). Bridge damage: Detection, IFC-based semantic enrichment and visualization. *Automation in Construction, 112*, 103088. https://doi.org/10.1016/j.autcon.2020.103088
> `VERIFIED` (Round 2) · quartile `UNVERIFIED`

**Nhóm B — tồn tại đã xác nhận qua DOI + deep-read, nhưng evidence record chỉ ghi author/year/DOI, chưa ghi title đầy đủ**

Bốn mục dưới đây tôi **cố ý không dựng APA hoàn chỉnh**, vì làm vậy tôi sẽ phải tự điền title/journal/volume/pages — đúng thao tác sinh ra citation sai. Anh lấy metadata từ DOI hoặc Zotero rồi hoàn thiện:

| Nguồn | DOI (đã xác minh trong evidence record) | Zotero key | Còn thiếu để dựng APA |
|---|---|---|---|
| Mohamed, A. G., Khaled, A., & Abotaleb, I. S. (2023) | `10.3390/buildings13112798` | *không có trong Zotero* — đọc publisher PDF (MDPI, 20 trang) | title, journal, volume/issue, article no. |
| Celik, Y., Petri, I., & Barati, M. (2023) | `10.1016/j.compind.2022.103768` | `EMTIHHX4` (PDF `YEVE3FRE`) | title, volume, pages |
| Li et al. (2023) | `10.1038/s41598-023-27924-6` | `YY8TP9ZT` (PDF `ER985KT3`) | tên tác giả đầy đủ, title, volume, article no. |
| Piras et al. (2026) | `10.3390/app16104642` | `P3YLFNJZ` (PDF `7NWG5TLX`) | tên tác giả đầy đủ, title, volume, article no. |

**Về nhãn `Q1`:** không mục nào ở trên được xác minh quartile trong repository. Bước xác minh còn treo: tra JCR hoặc Scopus SJR cho **đúng năm xuất bản** của từng bài (quartile thay đổi theo năm và theo category). Cho tới lúc đó, đừng viết "Q1" trong bất kỳ văn bản nào gửi ra ngoài.

---

## 4. Viết lại claim để nó đứng được

Ba phương án, theo mức độ tham vọng giảm dần. Tất cả đều nằm trong quyền phát biểu của Lớp 2.

**Phương án A — claim mô tả prior art (an toàn nhất, và tôi khuyến nghị)**

> Liên kết hồ sơ kiểm tra và hồ sơ công việc bảo trì với cấu kiện được định danh trong BIM đã được triển khai và trình diễn trong tài liệu (Kim et al., 2018; Lorvão Antunes et al., 2024; Bellon et al., 2025). Tuy nhiên, trong phạm vi corpus đã sàng lọc và deep-read, các triển khai này dừng ở truy xuất xuôi và hiển thị trạng thái hiện tại; chúng không mang định danh bản ghi ổn định, lịch sử sự kiện chỉ-ghi-thêm, hay bản ghi phê duyệt gắn với chủ thể.

**Phương án B — claim mở đường cho contribution (mạnh hơn, vẫn đứng được)**

> Accountability trong bảo trì đã được nêu như mục tiêu thiết kế trong tài liệu — qua provenance actor–time–version (Celik et al., 2023) và qua attestation bất biến (Lee et al., 2021) — nhưng không nghiên cứu nào trong corpus đã sàng lọc vận hành hóa nó thành bản ghi phê duyệt/từ chối gắn với chủ thể có thẩm quyền, kiểm chứng sau hành động, và đóng hồ sơ có điều kiện.

**Phương án C — nếu anh vẫn muốn giữ ý "improve"**

Thì nó phải được đánh dấu đúng loại phát biểu:

> **[CLAIM — pending Layer 4 evidence]** Liên kết hồ sơ kiểm tra với BIM được kỳ vọng cải thiện accountability trong bảo trì; kỳ vọng này chưa được đo lường trong corpus đã sàng lọc và nằm ngoài phạm vi bằng chứng của Paper 2 (Lớp 2).

Phương án C tôi ghi ra để đầy đủ, không phải để khuyến nghị. Một câu vừa hedge vừa giữ nguyên hàm ý vẫn là overclaim (`epistemic-ladder.md` §Applying the ladder, bước 3).

**Điều tuyệt đối tránh:** đặt một citation ngay sau nguyên văn "improve maintenance accountability". Bất kỳ reviewer nào mở nguồn đó ra cũng sẽ thấy nguồn không nói vậy — và đó là lỗi nặng hơn cả claim không có citation.

---

## 5. Nếu anh muốn support thật cho mệnh đề "improve": search phải làm gì

`CLOSE_SEARCH` đang có hiệu lực (Round 3B §8). **Mở lại broad search là quyết định của anh, không phải của skill này** — tôi không tự mở. Nếu anh quyết định mở, đây là search sẽ tìm ra bằng chứng thật, chứ không phải thêm một bài BIM-FM nữa:

| Thành phần | Nội dung |
|---|---|
| **Loại bằng chứng cần** | Nghiên cứu **có baseline** — đo accountability trước và sau khi đưa BIM-linked inspection record vào vận hành. Không phải case study trình diễn hệ thống |
| **Khái niệm tìm** | `accountability` / `auditability` / `traceability` **kết hợp** `maintenance work order` + `approval workflow` + `audit trail` + `before-after` hoặc `controlled comparison`; thêm `separation of duties`, `authorization`, `sign-off` |
| **Nơi có khả năng có nhất** | **Không phải** literature BIM/IFC. Thử: information systems (audit trail và accountability được đo thực sự ở đó), healthcare informatics (EHR audit log + accountability outcome), aviation/nuclear maintenance record governance, và safety-management literature |
| **Cửa sổ năm** | 2015–2026 cho BIM/FM; không giới hạn năm cho literature accountability ngoài AEC — công trình nền có thể cũ hơn |
| **Kết quả có khả năng nhất** | Anh sẽ **không** tìm thấy nghiên cứu đo được trong AEC. Nếu đúng vậy, đó là một `SUPPORTED GAP` — có giá trị hơn nhiều so với một citation ép vào cho có |
| **Nếu tìm thấy** | Nó gần như chắc chắn ở Lớp 4, không phải Lớp 2 — nghĩa là chỗ đúng của nó là Chương 7 / WP4, không phải Related Work của Paper 2 |

---

## 6. Claim → Evidence → Limitation → Next action

**Claim.** Câu Related Work hiện tại hỏng ở hai chỗ độc lập: nửa đầu là prior art được khai báo tường minh (nên không thể dùng như một khẳng định trung tính về đóng góp của lĩnh vực), nửa sau là một effect claim thuộc Lớp 4 mà Paper 2 không có quyền phát biểu và corpus không đo được.

**Evidence.** `_phd-canon/novelty-boundary.md` §Established prior art (mục "BIM-linked inspection records"); `_phd-canon/research-chain.md` §Four-layer firewall hàng Lớp 2 ("may NOT claim ... improves maintenance outcomes"); `G2_G3_ROUND3B_HISTORY_ACCOUNTABILITY_AND_SEARCH_CLOSURE.md` §5.3 (`FREEZE_AS_CORE_GAP`), §7.2 (contribution 2), §7.3 (claims removed from novelty); `ROUND4_VERIFIED_EVIDENCE_RECORD_v1.1.md` §4.2 component audit P2 và §4.4 component audit P4; `G2_G3_ROUND3A_NOVELTY_AND_SCHEMA_BOUNDARY.md` §§3–4.

**Limitation.** Phân tích này bị giới hạn bởi corpus Round 1–4 và bởi các trang PDF đã soi trực quan — Round 4 v1.1 §3.2 liệt kê các trang **chưa** soi, và mọi claim neo vào đó không được nâng lên `SOURCE-VERIFIED`. Tôi không mở external search trong nhiệm vụ này. Tôi cũng không xác minh được quartile của bất kỳ venue nào: `Evidence is currently insufficient.` cho mọi phát biểu Q1. Và bốn mục Nhóm B tồn tại đã được xác nhận qua DOI nhưng metadata chưa đủ để dựng APA hoàn chỉnh.

**Next action.**

1. Thay câu hiện tại bằng **Phương án A** hoặc **B** (§4). Đây là việc 10 phút và nó gỡ một lỗi mà reviewer chắc chắn bắt.
2. Rà toàn bộ Related Work Paper 2 tìm các câu cùng dạng — động từ `improve`, `enhance`, `ensure`, `enable better`, `demonstrate that`. Cùng một lỗi thường xuất hiện nhiều lần trong một section.
3. Lấy metadata 4 mục Nhóm B từ DOI/Zotero để hoàn thiện APA (không sửa Zotero khi chưa có phê duyệt của anh).
4. Nếu cần nhãn quartile: tra JCR/Scopus theo đúng năm xuất bản từng bài, ghi kết quả vào evidence record.
5. Quyết định — của anh, không phải của tôi — có mở lại search theo §5 hay không. Nếu không mở, giữ Phương án A/B và để mệnh đề "improve" cho WP4.

**Gate effect:** không có. Phân tích này không đóng G2 và không mở G3. Verdict cao nhất được phép ở đây là `READY-FOR-REVIEW` cho bản viết lại claim.

---

## 7. Báo cáo thực thi

**Files đã đọc (read-only):**

- `08_AI_SKILL_SYSTEM/phd-dt-research-skills/phd-literature-evidence/SKILL.md` + 3 reference (`corpus-map.md`, `source-verification.md`, `claim-source-mapping.md`)
- `_phd-canon/novelty-boundary.md`, `output-discipline.md`, `research-chain.md`, `epistemic-ladder.md`
- `02_EVIDENCE_BASE/RQ2_GATES2_3/G2_G3_ROUND1_DEEP_READ_AND_NOVELTY_BOUNDARY.md`
- `02_EVIDENCE_BASE/RQ2_GATES2_3/G2_G3_ROUND3A_NOVELTY_AND_SCHEMA_BOUNDARY.md`
- `02_EVIDENCE_BASE/RQ2_GATES2_3/G2_G3_ROUND3B_HISTORY_ACCOUNTABILITY_AND_SEARCH_CLOSURE.md`
- `02_EVIDENCE_BASE/RQ2_GATES2_3/ROUND4_VERIFIED_EVIDENCE_RECORD_v1.1.md`
- `02_EVIDENCE_BASE/RQ2_GATES2_3/G2_G3_ROUND2_INSPECTION_ACTION_MODEL_DEEP_READ.md` (citation register)

**Files tạo/sửa:** chỉ file này. Không file nào trong `00_GOVERNANCE`, `01_CURRENT_CONTROL`, `02_EVIDENCE_BASE`, `03_PAPERS`, `05_DATA_CODE_AND_EXPERIMENTS`, `06_LITERATURE_AND_ZOTERO`, `07_PROMPTS_AND_HANDOFFS` bị đọc-ghi, sửa, đổi tên hay xóa. Zotero không bị chạm.

**Việc đã từ chối:** sinh danh sách paper "Q1 phù hợp" chưa xác minh; gán nhãn quartile; mở lại literature search khi `CLOSE_SEARCH` đang có hiệu lực.

**Vấn đề còn treo:** (i) quartile của toàn bộ venue — chưa xác minh; (ii) metadata APA của 4 mục Nhóm B; (iii) quyết định của anh về việc mở lại search cho mệnh đề "improve"; (iv) các trang PDF chưa soi trực quan liệt kê ở Round 4 v1.1 §3.2.

**Gate có gần hơn không?** Không thay đổi. G2 vẫn `OPEN — literature boundary closed, specification not frozen`. Nhưng gỡ được câu này khỏi Related Work làm giảm một rủi ro review có thật.
