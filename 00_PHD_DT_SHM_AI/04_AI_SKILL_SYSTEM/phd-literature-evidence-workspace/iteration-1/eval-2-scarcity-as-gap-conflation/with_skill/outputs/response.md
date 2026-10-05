# Append-only `Status_Event` history có đủ làm novelty chính cho Paper 2 không?

**Declaration:** RQ2 → WP2 → C5 / Paper 2 → G2–G3 → Scope: Layer 2 (information traceability), corpus-bounded (Rounds 1–3B `CLOSE_SEARCH` + Round 4)

---

## Trả lời ngắn

Chưa đủ, và có hai vấn đề khác nhau đang bị gộp làm một.

1. **Lập luận "rất ít nghiên cứu bàn về X" không phải là bằng chứng gap.** Ở dạng anh đang phát biểu, đây là `scarcity-only` → phân loại là `UNSUPPORTED NOVELTY CLAIM`. Không phải vì kết luận sai, mà vì đường đi tới kết luận không chịu được phản biện.
2. **Bản thân khoảng trống thì có thật** — nhưng nó nằm trong hồ sơ deep-read của chính anh, không nằm ở chỗ "tìm mãi không ra". Và khi đọc đúng hồ sơ đó thì nó là `PARTIALLY SUPPORTED GAP`, **không phải** một novelty độc lập đủ sức gánh Paper 2.

Nói gọn: anh đang đúng về hướng, sai về bằng chứng, và sai về đơn vị đóng góp.

---

## 1. Gap audit (theo `references/claim-source-mapping.md` §4)

```text
Gap as asserted:  "rất ít nghiên cứu bàn về append-only Status_Event history trong bảo trì
                   công trình" → đủ mạnh làm novelty chính cho Paper 2
Evidence type:    scarcity-only (theo cách anh lập luận)
                   — trong khi corpus đã có sẵn documented-absence + stated-in-source
Corpus bound:     Rounds 1–3B (CLOSE_SEARCH); Round 4 (Kim, Jia, Lee D., Keet & Khan, Pauwels)
Verdict:          Như đang phát biểu → UNSUPPORTED NOVELTY CLAIM
                   Trên bằng chứng corpus  → PARTIALLY SUPPORTED GAP
Residue:          maintenance-specific event semantics (xem §3)
```

### Vì sao `scarcity-only` bị bác

"Ít bài viết về X" có ít nhất bốn cách giải thích, và chỉ một trong số đó là "X là đóng góp":

| Khả năng | Hệ quả nếu đúng |
|---|---|
| X thực sự là khoảng trống | Đóng góp — nhưng phải chứng minh bằng absence có ghi chép, không bằng cảm giác |
| X đã được giải ở nơi khác dưới tên khác | Reviewer sẽ tìm ra và Paper 2 mất novelty ngay tại vòng 1 |
| X không thú vị với cộng đồng | Reviewer hỏi "so what" |
| Truy vấn tìm kiếm quá hẹp | Đây là lỗi phương pháp, không phải phát hiện khoa học |

Rủi ro thứ hai là rủi ro cao nhất trong trường hợp cụ thể này, và tôi nêu nó ở dạng **model inference cần kiểm chứng**, không phải fact: khái niệm "append-only history + current state là projection" tồn tại dày đặc trong các literature lân cận dưới tên khác — event sourcing, audit trail, temporal/bitemporal record, provenance log, work-order transaction history trong CMMS/EAM. Nếu reviewer thuộc nhóm đó, câu "rất ít nghiên cứu bàn về append-only history" sẽ đọc như một tuyên bố về phạm vi tìm kiếm của tác giả chứ không phải về literature.

Và corpus của anh **đã tự xác nhận rủi ro đó**: Çelik et al. (2023) có immutable/queryable provenance đã thực thi, Lee D. et al. (2021) có immutable event history dạng chained blocks có timestamp. Cả hai đều không phải bảo trì, nhưng cả hai đều là "append-only history" theo nghĩa chung.

### Điều đáng chú ý: anh đã có bằng chứng tốt hơn nhiều mà không dùng

Có một câu gap phát biểu trực tiếp trong nguồn, đã được deep-read và đánh dấu `CITE`:

> Digital-twin data is vulnerable to overwriting; historical state of virtual assets can be lost, and DT data management (storage, immutability, traceability) "has not been thoroughly realized"
> — Lee, D. et al. (2021), §2, PDF p. 2
> [`02_EVIDENCE_BASE/RQ2_GATES2_3/G2_G3_ROUND4_CQ_CONSTRAINT_ACCOUNTABILITY_DEEP_READ_20260809.md`, §2.4, dòng ghi `Strong gap statement for the thesis' Status_Event history requirement (CITE)`]

Đây là `stated-in-source`. Nó mạnh hơn "tôi tìm mãi mà ít thấy" ở mọi phương diện, và nó đã nằm trong hồ sơ từ 09/08. Đây là lý do quy trình bắt buộc "locate the corpus trước khi trả lời": trí nhớ về literature phai nhanh hơn hồ sơ.

---

## 2. Phân loại chính thức

**Classification (mệnh đề "append-only `Status_Event` history là novelty chính của Paper 2"):**
`UNSUPPORTED NOVELTY CLAIM` — như đang phát biểu.

**Classification (khoảng trống thực sự, đọc đúng theo corpus):**
`PARTIALLY SUPPORTED GAP` — có precedent ở mức generic, residue là maintenance-specific.

**Basis:**

- `02_EVIDENCE_BASE/RQ2_GATES2_3/G2_G3_ROUND3B_HISTORY_ACCOUNTABILITY_AND_SEARCH_CLOSURE.md`, §5.2 *Immutable/queryable `Status_Event` history* — `FREEZE_AS_CORE_GAP`, kèm liệt kê prior art đã đạt được và residue còn lại.
- Cùng file, §7.3 *Claims removed from novelty* — loại khỏi novelty một cách tường minh: *"Blockchain-based BIM provenance, immutable-ledger capability hoặc smart-contract transaction execution"*, *"Generic actor-object-operation-time-version provenance"*, *"Generic user/role administration, queryable history capability"*, *"Inspection history, maintenance report history hoặc repaired/unrepaired display nói chung"*.
- Cùng file, §5.9 và §7.2 — đơn vị đóng góp là integrated chain, không phải kỹ thuật đơn lẻ.
- `_phd-canon/novelty-boundary.md` — "immutable, queryable maintenance `Status_Event` history" nằm ở mục **strong core candidates**, tức là *một trong sáu*, không phải *cái duy nhất*.

---

## 3. Bảng phân rã prior art (bắt buộc khi có novelty claim)

| Mức | Câu hỏi | Kết luận |
|---|---|---|
| **Kỹ thuật** | Append-only / immutable event log tự nó có mới không? | **`ESTABLISHED PRIOR ART`.** Çelik et al. (2023): actor-object-operation-time-version provenance, immutable/tamper-proof chronological history, object-history verification đã chạy 5–30 updates [Round 3B §§3, 5.2; Çelik PDF pp. 8, 12–13, §§5.1, 7]. Lee D. et al. (2021): immutable event history bằng chained blocks có timestamp, `Yes` trong component audit [Round 4 §2.4; Lee PDF p. 3 §4.1, pp. 5–6 §5.2] |
| **Tổ hợp** | Tổ hợp "event append-only **gắn vào `Action_Record` bảo trì**, có previous/new state, actor, reason, transition hợp lệ, và current `Workflow_Status` là projection" có mới trong corpus không? | **`CANDIDATE NOVELTY`, corpus-bounded.** Round 3B §5.2: *"No maintenance-specific event ID, previous/new state, reason, action relation, valid transition, replay query or immutable status reconstruction."* Mohamed chỉ có `not treated`, Li có `completed`, Piras có `Condition` — đều là **current scalar**, không phải event |
| **Việc mà tổ hợp làm được còn các phần rời thì không** | Chuỗi tích hợp identity → event → authorization → post-action verification → guarded closure/reopen, có validation hai chiều exact, có làm được điều mà từng mảnh không làm được? | **Đây mới là claim sống sót.** Round 3B §5.9: *"No deep-read source integrates stable evidence/component/inspection/action identities, maintenance `Status_Event`, accountable authorization, formal post-action verification, guarded closure/reopen and exact chain-specific forward/reverse validation."* |

**Đọc bảng này theo chiều dọc:** nếu Paper 2 lấy hàng 2 làm novelty chính, phần lớn phản biện sẽ tấn công vào hàng 1 và anh sẽ phải phòng thủ ở mặt trận yếu nhất (Çelik và Lee đã có immutability chạy thật, có số đo gas, có consensus test). Nếu Paper 2 lấy hàng 3 làm novelty chính, hàng 1 trở thành *background* — và Çelik/Lee từ đối thủ chuyển thành nguồn trích dẫn ủng hộ.

---

## 4. Ba lý do cụ thể vì sao "novelty chính" là sai vị trí

**(a) Nó phá vỡ contribution statement đã chốt.** Round 3B §7.2 đã viết sẵn ba contribution, và `append-only Status_Event` là **một thành phần bên trong contribution 1**, đứng cạnh `Condition_Evidence`, `Component`, `Inspection_Record`, `Action_Record`, `Workflow_Status`. Nâng một thành phần lên thành trục chính sẽ làm Paper 2 hẹp hơn chính ranh giới G2 đã đóng, và ba contribution còn lại mất chỗ đứng.

**(b) Nó rơi thẳng vào danh sách đã bị loại.** §7.3 loại "immutable-ledger capability" và "queryable history capability" khỏi novelty. Một tiêu đề dạng "An append-only status-event history for building maintenance" sẽ được reviewer đọc đúng vào ô đã bị loại đó trước khi họ đọc tới phần maintenance-specific.

**(c) Nó chưa đủ rung bậc để được gọi là novelty ở thì hiện tại.** `Status_Event_ID` đang ở trạng thái `PROPOSED — NOT YET ACCEPTED`, chờ `00_GOVERNANCE/ADR_ACTION_STATUS_EVENT_20260804_DRAFT.md`. Roadmap Paper 2 v2.1 ghi đúng như vậy: *"Append-only history and current-state reconstruction; exact naming/transitions pending proposed ADR and expert review — NOT YET ACCEPTED"*. G2 = `OPEN — LITERATURE BOUNDARY CLOSED, SPECIFICATION NOT YET FROZEN`; G3 execution = `NOT OPEN` [Round 4 §6, Gate status]. Ở rung 1–2 của thang epistemic, ngôn ngữ đúng là *proposed / design boundary*, không phải *đóng góp chính đã xác lập*.

---

## 5. Câu nên viết thay cho câu đang có

**Không viết:**
> "Rất ít nghiên cứu bàn về append-only `Status_Event` history trong bảo trì công trình, do đó đây là đóng góp chính của bài báo này."

**Viết (documented absence, có corpus bound, có residue):**
> Trong phạm vi corpus đã sàng lọc và deep-read (Rounds 1–3B, Round 4), immutable và queryable history đã được xác lập ở mức provenance tổng quát: Çelik et al. (2023) triển khai chuỗi actor–object–operation–time–version bất biến và đã thực thi truy vấn lịch sử đối tượng; Lee D. et al. (2021) triển khai lịch sử sự kiện bất biến dạng khối có timestamp. Trong cùng phạm vi đó, không nguồn nào cung cấp một sự kiện đặc thù cho bảo trì mang định danh riêng, trạng thái trước/sau, lý do, quan hệ tới `Action_Record`, quy tắc chuyển trạng thái hợp lệ và khả năng tái dựng `Workflow_Status` hiện thời từ chuỗi sự kiện; các công trình gần nhất chỉ dừng ở scalar hiện thời (`not treated`, `completed`, `Condition`). Đóng góp của bài báo này do đó không phải bản thân cơ chế append-only, mà là hợp đồng tích hợp giữa định danh, sự kiện, ủy quyền có trách nhiệm, xác minh sau thi công và đóng/mở lại có điều kiện.

Ba khác biệt đáng chú ý so với bản gốc: có corpus bound tường minh, có tên nguồn cụ thể cho prior art, và đóng góp được phát biểu ở mức tổ hợp chứ không ở mức kỹ thuật.

---

## 6. Claim → Evidence → Limitation → Next action

**Claim.** Lập luận khan hiếm không nâng append-only `Status_Event` history lên thành novelty chính của Paper 2. Khoảng trống thực sự tồn tại, đã được ghi chép, nhưng ở dạng `PARTIALLY SUPPORTED GAP` với residue là ngữ nghĩa sự kiện đặc thù bảo trì; đơn vị đóng góp bảo vệ được vẫn là chuỗi tích hợp.

**Evidence.**
- `02_EVIDENCE_BASE/RQ2_GATES2_3/G2_G3_ROUND3B_HISTORY_ACCOUNTABILITY_AND_SEARCH_CLOSURE.md` §5.2 (`FREEZE_AS_CORE_GAP`), §5.9, §6 (dòng `Status_Event`), §7.2, §7.3
- `02_EVIDENCE_BASE/RQ2_GATES2_3/G2_G3_ROUND4_CQ_CONSTRAINT_ACCOUNTABILITY_DEEP_READ_20260809.md` §2.4 (Lee D. 2021, gap statement `CITE`; component audit `Immutable event history: Yes`), §4.1, §6
- `02_EVIDENCE_BASE/RQ2_GATES2_3/G2_G3_PAPER2_CURRENT_ROADMAP_v2.1_20260804.md`, dòng `Status_Event` — `NOT YET ACCEPTED`
- `_phd-canon/novelty-boundary.md` (quy tắc phân rã; danh sách strong core candidates), `_phd-canon/epistemic-ladder.md` (rung 1–2)

**Limitation.** Đây là kết luận **bounded theo corpus**, không phải phát biểu về literature thế giới. `CLOSE_SEARCH` không cấp phép cho "first", "no study worldwide" hay bất kỳ tuyên bố vắng mặt phổ quát nào, và không phải một quyết định gate. Round 4 §6 còn ghi rõ các giới hạn chưa gỡ: Bellon et al. (2025) vẫn bị paywall ở mức entity và vẫn có thể chồng lấn; sáu PDF trong `DEEP_READ_20.07.2026` (Boje, Chen, Johannes, Yang và hai bản trùng) chưa deep-read; hình trong cả năm bài Round 4 chưa được kiểm tra trực quan. Ngoài ra, phân tích này chỉ nói về **phân loại literature**; nó không nói gì về việc đặc tả có khả thi hay nhất quán nội tại hay không — G3 execution vẫn `NOT OPEN`, nên chưa tồn tại bằng chứng validation cho bất kỳ hành vi nào của `Status_Event`.

Một điểm tôi **không** khép lại được: liệu append-only maintenance history đã được giải dưới tên khác trong literature ngoài corpus (event sourcing, temporal database, CMMS audit trail) hay chưa. `Evidence is currently insufficient.` Bằng chứng cần thiết là một vòng sàng lọc có ghi chép trên các từ khóa đó; nó sẽ nằm ở `02_EVIDENCE_BASE/RQ2_GATES2_3/` như một Round 5 record. Mở lại phạm vi tìm kiếm là **quyết định của anh**, không phải của phân tích này, và Round 4 §6 mục 6 yêu cầu phải nêu trigger rõ ràng trước khi mở.

**Next action.**

1. Gỡ mọi câu dạng "rất ít nghiên cứu bàn về…" khỏi bản nháp Paper 2 và khỏi ghi chú novelty. Thay bằng câu documented-absence ở §5 phía trên.
2. Đưa Lee D. et al. (2021) §2, PDF p. 2 vào phần motivation như gap statement `stated-in-source`. Đây là câu trích mạnh nhất hiện có cho yêu cầu history, và nó đang không được dùng.
3. Giữ contribution statement theo Round 3B §7.2: `Status_Event` là thành phần của contribution 1, không phải trục bài báo. Nếu muốn một section riêng cho event history, đặt nó dưới tiêu đề residue (maintenance-specific event semantics), không dưới tiêu đề append-only.
4. Ban hành ADR `Action-Status-Event` để `Status_Event_ID` rời khỏi trạng thái `PROPOSED — NOT YET ACCEPTED`. Trước khi ADR được chấp nhận, mọi câu về `Status_Event` trong bản thảo phải ở ngôn ngữ đề xuất/thiết kế.
5. Nếu vẫn muốn nâng lên `SUPPORTED GAP` mức mạnh: quyết định có mở Round 5 trên nhóm từ khóa "event sourcing / temporal record / audit trail / work-order transaction history" hay không, và ghi trigger vào `01_CURRENT_CONTROL/`. Nếu không mở, ranh giới hiện tại vẫn dùng được — với điều kiện mọi phát biểu novelty đều mang corpus bound.

---

## 7. Về câu "Tôi nghĩ là đủ rồi"

Tôi không rút lại phân loại ở đây. Không phải vì phán đoán của anh vô lý — trực giác về hướng là đúng — mà vì lập luận khan hiếm là thứ reviewer tấn công trước tiên và rẻ nhất: họ chỉ cần một bài dùng tên gọi khác là toàn bộ mệnh đề novelty sụp. Nếu muốn tôi đổi phân loại, thứ cần đưa ra là bằng chứng mới trong corpus — một nguồn phát biểu khoảng trống ở đúng mức maintenance-specific, hoặc một absence có ghi chép kèm phạm vi tìm kiếm cụ thể. Phát biểu lại mức độ tự tin thì không đổi được phân loại, và tôi cho rằng đó chính là phần giá trị của việc hỏi ở đây thay vì hỏi ở vòng phản biện.

Tin tốt: đóng góp thật sự của anh **lớn hơn** cái anh đang định claim, chứ không nhỏ hơn. Chuỗi tích hợp ở Round 3B §5.9 là một mệnh đề khó bác hơn nhiều so với "append-only history còn ít người làm", và nó đã có sẵn bằng chứng, có sẵn residue, có sẵn danh sách validation cần thiết. Vấn đề chỉ là đang claim nhầm tầng.

---

## Báo cáo thực thi

**Files read (read-only, không sửa gì):**
- `08_AI_SKILL_SYSTEM/phd-dt-research-skills/phd-literature-evidence/SKILL.md`
- `_phd-canon/novelty-boundary.md`, `output-discipline.md`, `research-chain.md`, `epistemic-ladder.md`, `failure-modes.md`
- `phd-literature-evidence/references/corpus-map.md`, `claim-source-mapping.md`, `source-verification.md`
- `02_EVIDENCE_BASE/RQ2_GATES2_3/G2_G3_ROUND3B_HISTORY_ACCOUNTABILITY_AND_SEARCH_CLOSURE.md`
- `02_EVIDENCE_BASE/RQ2_GATES2_3/G2_G3_ROUND4_CQ_CONSTRAINT_ACCOUNTABILITY_DEEP_READ_20260809.md`
- `02_EVIDENCE_BASE/RQ2_GATES2_3/G2_G3_PAPER2_CURRENT_ROADMAP_v2.1_20260804.md`

**Files created:** chỉ file trả lời này. Không file nào trong `00_GOVERNANCE`, `01_CURRENT_CONTROL`, `02_EVIDENCE_BASE`, `03_PAPERS`, `05_DATA_CODE_AND_EXPERIMENTS`, `06_LITERATURE_AND_ZOTERO`, `07_PROMPTS_AND_HANDOFFS` bị tạo, sửa hay xóa. Zotero không bị chạm tới.

**Failure modes đã kiểm:** F1 novelty inflation (phát hiện — đây là finding chính); F2 design→result promotion (phát hiện — `Status_Event` ở rung 1–2 nhưng được nói như đóng góp đã xác lập); F5 claim–source drift (không phát hiện — không có citation nào bị dùng sai trong câu hỏi); F10 chain notation drift (không phát hiện — anh dùng đúng `Status_Event`, không nhầm với `Action_Status`); F4 citation fabrication (không có — mọi nguồn nêu ở đây đều đã deep-read trong corpus).

**Unresolved:** khả năng chồng lấn ngoài corpus dưới tên gọi khác; Bellon et al. (2025) paywalled; 6 PDF chưa deep-read.

**Gate movement:** không. Phân tích này không đưa G2 hay G3 tới gần hơn theo nghĩa bằng chứng; nó ngăn một novelty claim sai đi vào bản thảo Paper 2. G2 vẫn `OPEN — LITERATURE BOUNDARY CLOSED, SPECIFICATION NOT YET FROZEN`; G3 execution vẫn `NOT OPEN`.

---

*v1.0 · 2026-08-10 · phd-literature-evidence · read-only*
