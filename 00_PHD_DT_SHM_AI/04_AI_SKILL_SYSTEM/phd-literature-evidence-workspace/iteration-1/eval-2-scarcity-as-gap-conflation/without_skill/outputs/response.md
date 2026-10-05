# "Ít nghiên cứu về append-only Status_Event" — đã đủ làm novelty chính cho Paper 2 chưa?

**Trả lời ngắn: Chưa. Và không phải vì gap yếu, mà vì lập luận đang sai loại.**

"Tôi tìm mãi mà rất ít nghiên cứu bàn về X" là một **quan sát về tài liệu**, không phải một **research gap**. Hai thứ này khác nhau về bản chất: cái thứ nhất mô tả trạng thái của kho tài liệu và của quá trình tìm kiếm của bạn; cái thứ hai là một khẳng định rằng có một thứ **đáng biết mà chưa ai biết**, và việc không biết nó **gây ra hậu quả cụ thể**. Khoảng cách giữa hai thứ đó chính là chỗ reviewer 2 sẽ đâm vào.

Nghiêm trọng hơn: **chính evidence base của bạn đã quyết định ngược lại rồi**, và quyết định đó có căn cứ tốt hơn cảm giác "đủ rồi". Tôi sẽ trình bày theo thứ tự: (1) tại sao "ít tài liệu" không tự động là gap, (2) trường hợp cụ thể của append-only event log, (3) hồ sơ của bạn đã nói gì, (4) nên đặt novelty ở đâu, (5) việc cần làm.

---

## 1. Năm nguyên nhân khác nhau đều tạo ra cùng một triệu chứng "ít tài liệu"

Khi bạn tìm mà không thấy, có ít nhất năm khả năng. Chỉ **một** trong số đó là research gap.

| # | Nguyên nhân | Đây có phải gap không? | Dấu hiệu nhận biết |
|---|---|---|---|
| A | Thật sự chưa ai làm, và nó quan trọng | **Có** — gap thật | Nhiều bài chạm rìa rồi dừng lại đúng chỗ đó; các tác giả tự nêu nó trong future work |
| B | Đã giải quyết ở lĩnh vực khác, dưới **từ vựng khác** | Không — đây là *translation gap*, yếu hơn nhiều | Tìm bằng từ khóa của ngành khác thì ra hàng trăm kết quả |
| C | Được coi là **chi tiết triển khai**, không đáng đăng báo | Không — "sự im lặng của cái hiển nhiên" | Có trong sản phẩm thương mại / tiêu chuẩn kỹ thuật nhưng không có trong journal |
| D | Đã thử và **bị bỏ vì lý do chính đáng** | Không — đây là dead end đã được định giá | Có bài cũ, rồi tắt dần; lý do bỏ nằm trong phần limitation |
| E | **Từ khóa tìm kiếm của bạn** chưa trúng | Không — đây là vấn đề của search strategy | Bạn chỉ tìm bằng đúng cụm từ nội bộ của mình |

Câu "tôi tìm mãi mà rất ít" **không phân biệt được** A với B/C/D/E. Nó chỉ nói rằng bạn đã ở trạng thái không tìm thấy. Và có một bẫy nhận thức cụ thể ở đây: cảm giác "đủ rồi" thường xuất hiện **chính xác vào lúc ta ngừng tìm** — nó là hàm của thời điểm dừng, không phải hàm của thực trạng tài liệu. Đó là lý do trong nghiên cứu, phát biểu về sự vắng mặt luôn phải kèm theo **phạm vi**: vắng mặt *ở đâu*, tìm bằng *từ vựng nào*, trong *khoảng thời gian nào*.

---

## 2. Trường hợp cụ thể: append-only event history rơi vào ô B và C, không phải ô A

Đây là phần tôi cần nói thẳng, vì nó quyết định số phận của claim.

**Append-only log không phải là một ý tưởng mới ở bất kỳ đâu.** Nó là một pattern rất trưởng thành bên ngoài construction management. Bạn hãy tự kiểm chứng bằng cách tìm với các cụm từ sau (tôi nêu như **từ khóa cần tra cứu và tự verify**, không phải như trích dẫn đã xác minh — tôi không chạy tìm kiếm mới cho câu trả lời này):

- `event sourcing`, `CQRS`, `event log`, `immutable log`, `write-ahead log`
- `temporal database`, `bitemporal`, `valid time / transaction time`, `system-versioned tables` (SQL:2011)
- `audit trail`, `audit log`, `tamper-evident log`, `hash chain`
- `provenance model`, `W3C PROV`, `lineage`
- `work order status transition`, `state machine`, `workflow history`, `CMMS/EAM transaction table`
- Trong ngành có quy chế nghiêm ngặt: `ALCOA+`, `audit trail requirement` (dược/thiết bị y tế), `chain of custody`

Nếu ba đến bốn nhóm từ khóa này trả về kết quả dày đặc — và tôi cho là sẽ như vậy — thì cái bạn đang có **không phải là ô A**. Nó là:

- **ô B**: cơ chế đã được giải quyết triệt để ở nơi khác, chỉ chưa được nói bằng ngôn ngữ bảo trì công trình;
- cộng **ô C**: trong bảo trì công trình, người ta coi "lưu lịch sử trạng thái" là chuyện của phần mềm CMMS, không phải chuyện của bài báo.

**Và bằng chứng mạnh nhất cho điều này lại nằm ngay trong hồ sơ của bạn.** `G2_G3_ROUND3B_HISTORY_ACCOUNTABILITY_AND_SEARCH_CLOSURE.md` §3 đã deep-read Celik et al. (2023): họ **đã có** append-only, immutable, chronological provenance với tuple `operation / time / model / version / objectID / owner`, đã triển khai smart contract, đã chạy thực nghiệm truy vấn lịch sử trên Kovan. Nghĩa là: append-only event history trong môi trường BIM **đã tồn tại như prior art**. Cái Celik không có không phải là tính append-only — mà là **ngữ nghĩa bảo trì** của sự kiện.

Đây chính là điểm chết của phương án "append-only Status_Event làm novelty chính". Reviewer sẽ viết đúng một câu:

> *"The append-only event log is a standard, well-established pattern (event sourcing, temporal databases, blockchain provenance — see the authors' own cited Celik et al. 2023). Applying it to maintenance status is an implementation choice, not a research contribution. What exactly is new here?"*

Và bạn sẽ không có câu trả lời, vì lập luận của bạn được xây trên sự vắng mặt chứ không trên hậu quả.

**Một điểm kỹ thuật nữa, cũng quan trọng:** append-only *tự nó* gần như không thể falsify được trong validation. Nếu bạn thiết kế bảng chỉ cho phép INSERT thì tất nhiên nó append-only — test đó pass một cách tầm thường. Một đóng góp mà phần validation của nó không thể thất bại thì không phải là một đóng góp khoa học mạnh. Cái **có thể** thất bại — và vì thế mới đáng test — là các **guard**: đóng case khi chưa có verification được chấp nhận thì phải bị từ chối; transition không hợp lệ phải bị từ chối; người không có quyền phê duyệt phải bị từ chối; current status phải tái dựng **đúng** từ chuỗi event theo quy tắc thứ tự đã khai báo. Đó mới là chỗ có rủi ro thật, và chỗ có rủi ro thật mới là chỗ có novelty thật.

---

## 3. Hồ sơ của bạn đã ra quyết định ngược lại — và quyết định đó đúng

Đây là phần tôi muốn bạn đọc kỹ nhất, vì nếu đẩy append-only Status_Event lên làm novelty chính, bạn sẽ **tự mâu thuẫn với chính evidence base của mình**.

**(a) `G2_G3_ROUND3B_...md` §5.9 — đơn vị đóng góp đã được khóa là *chuỗi tích hợp*, không phải kỹ thuật đơn lẻ:**

> "Contribution unit is the integrated identity-event-authorization-verification contract, **not any individual BIM, history, provenance or constraint technique**." → `FREEZE_AS_CORE_GAP`

**(b) §7.3 "Claims removed from novelty" — bạn đã tự tay gạch bỏ đúng thứ bạn đang định đề cao:**

- "Generic actor-object-operation-time-version provenance"
- "Blockchain-based BIM provenance, **immutable-ledger capability** hoặc smart-contract transaction execution"
- "Inspection history, maintenance report history hoặc repaired/unrepaired display nói chung"
- "Generic user/role administration, **queryable history capability**..."

Nếu bây giờ novelty chính là "append-only Status_Event history", bạn đang **mở lại** đúng những claim đã bị loại — và loại có căn cứ, sau bốn vòng deep-read.

**(c) §7.2 — Status_Event nằm *bên trong* contribution 1, không phải là contribution 1:**

> "contribution 1 là một record-event specification **tách** `Condition_Evidence`, BIM-addressed `Component`, `Inspection_Record`, `Action_Record`, current `Workflow_Status` và append-only `Status_Event`, với explicit identity và relation semantics."

Trọng tâm của câu này là chữ **tách** (identity separation), không phải chữ **append-only**. Append-only là *hệ quả* của việc tách current scalar khỏi event history — nó là cơ chế, không phải luận điểm.

**(d) §6 decision matrix — phần dễ bị tấn công nhất vẫn chưa khóa.** `Status_Event` = `FREEZE`, nhưng `Authorization` = `FREEZE_PROVISIONALLY`, `Closure/reopen` = `FREEZE_PROVISIONALLY`, `Inspection-Action cardinality` và `Actor/role model` = `EXPERT_REVIEW_REQUIRED`. Nghĩa là: bạn đang muốn đặt novelty chính lên cấu phần **ổn định nhất và ít tranh cãi nhất**, trong khi những cấu phần **thật sự chưa có ai giải quyết** thì vẫn đang treo chờ expert review. Đó là đặt sức nặng sai chỗ.

**(e) Và câu quyết định nhất — `G2_G3_PAPER2_CURRENT_ROADMAP_v2.1_20260804.md` §3:**

> "`CLOSE_SEARCH` is corpus-bounded. It is **not universal absence**, **does not justify "first"**, and does not constitute G2 PASS."

Câu này, do chính bạn viết, đã cấm trước lập luận "tôi tìm mãi không thấy nên đây là gap". `CLOSE_SEARCH` chỉ nói rằng *không cần tìm thêm để viết spec*; nó **không** nói rằng *thế giới chưa có ai làm*. §8 của Round 3B cũng ghi rõ: "Không có tài liệu bắt buộc nào **trong bounded Round 1-3B corpus**". Chữ "trong corpus" là chữ chịu lực.

---

## 4. Ba phép thử để nâng một "sự khan hiếm" thành một "gap"

Dùng bộ ba này cho bất kỳ ứng viên gap nào, không chỉ lần này.

### Test 1 — Absence test: vắng mặt thật hay vắng mặt từ vựng?

Không tìm để **xác nhận** sự vắng mặt (bạn sẽ luôn xác nhận được). Tìm để **bác bỏ** nó: cố ý đi tìm bằng chứng rằng có người đã làm rồi. Cụ thể:
- tìm bằng ít nhất **ba bộ từ vựng ngoài ngành** (mục 2 ở trên);
- đọc phần "future work" của 5-10 bài gần nhất — nếu nhiều tác giả cùng nêu đúng thiếu sót này, đó là bằng chứng độc lập mạnh cho ô A;
- kiểm tra tài liệu **phi học thuật**: tiêu chuẩn, spec sản phẩm CMMS/EAM, ISO 19650 về information container và audit. Nếu nó nằm sẵn trong sản phẩm thương mại, đó là ô C.

Bạn đã làm phần này rất tốt **trong** ngành (bốn vòng deep-read). Chỗ chưa làm là **ngoài** ngành.

### Test 2 — Consequence test: thiếu nó thì *cái gì* hỏng?

Đây là phép thử quan trọng nhất, và may mắn là **bạn đã có sẵn dữ liệu để trả lời**. Round 3B §2.4 ghi lại các mâu thuẫn quan sát được trong chính case study của Mohamed et al. (2023):
- ngày kiểm tra `10-1-2023` ở Figs. 8/10/12 nhưng `10/1/2022` ở Fig. 14;
- cùng một bằng chứng expansion-joint gắn ở `DE-19` (Figs. 8, 12) nhưng ở `EJ-5` (Fig. 14);
- chiều dài spalling của `CO-6` là `800 mm` (Fig. 12) và `400 mm` (Fig. 14);
- `Status: not treated` là một **scalar hiện tại có thể bị ghi đè**, không có transition, không có actor, không có thời điểm.

**Đó mới là gap statement của bạn.** Không phải "ít ai bàn về append-only". Mà là: *khi trạng thái công trình được lưu như một giá trị hiện tại có thể ghi đè, hệ thống không thể trả lời được ai đã chuyển trạng thái, dựa trên bằng chứng nào, được ai phê duyệt, và đã được nghiệm thu chưa — và các bài đã công bố cho thấy sự mâu thuẫn này xảy ra ngay cả trong case study được tác giả kiểm soát.* Phát biểu đó **có hậu quả**, **có bằng chứng quan sát được**, và **có thể kiểm chứng**.

Với công trình thép ven biển — ăn mòn tiến triển, kiểm tra lặp lại nhiều chu kỳ, trách nhiệm pháp lý khi kết cấu hỏng — hậu quả này không trừu tượng. Nó là câu hỏi "ba năm sau, ai chứng minh được là hạng mục này đã được sửa và đã được nghiệm thu?".

### Test 3 — Tractability test: có oracle để test không?

Một gap chỉ thành đóng góp nếu có thể **thất bại**. Round 3B §5.2 đã liệt kê sẵn: append-only fixtures, allowed/illegal transitions, current-state projection, sequence/chronology, supersession, history replay assertions. §5.5 và §5.6 còn mạnh hơn: blocked closure khi verification vắng mặt / thất bại / không có thẩm quyền; reopen phải giữ nguyên closure trước đó.

Nhận xét: các test **thú vị** đều nằm ở guard và ở authorization/verification/closure — **không** nằm ở tính append-only.

---

## 5. Nên đặt novelty chính ở đâu

Giữ nguyên §7.2 mà bạn đã khóa, và **hạ append-only xuống đúng vai trò cơ chế**:

> **Không phải:** "Chúng tôi đề xuất một append-only Status_Event history cho bảo trì công trình."
> **Mà là:** "Chúng tôi đặc tả một hợp đồng truy vết định danh (identity-governed) trong đó trạng thái công việc bảo trì hiện tại là **một phép chiếu tái dựng được** từ chuỗi sự kiện gắn với chủ thể chịu trách nhiệm, trong đó việc đóng hạng mục bị **chặn** nếu chưa có nghiệm thu được chấp nhận bởi một chủ thể có thẩm quyền, và toàn bộ chuỗi được kiểm chứng bằng các đột biến có kiểm soát đặc thù cho chuỗi đó cùng các cặp truy vấn xuôi/ngược có kết quả kỳ vọng khai báo trước."

Khác biệt: câu thứ hai **không phụ thuộc vào việc có ai đã từng dùng append-only log hay chưa**. Kể cả khi reviewer đưa ra mười bài về event sourcing, câu này vẫn đứng — vì đóng góp nằm ở **ngữ nghĩa bảo trì cụ thể** gắn vào sự kiện (previous/new workflow state, evidence basis, authorization context, verification-guarded closure/reopen) và ở **hợp đồng validation** cho chính chuỗi đó, chứ không ở cơ chế lưu trữ.

### Mẫu viết gap statement

| Kiểu | Ví dụ | Số phận ở peer review |
|---|---|---|
| **Xấu — absence-based** | "Rất ít nghiên cứu bàn về append-only status history trong bảo trì công trình." | "Ít không có nghĩa là không nên có. Và nó đã tồn tại ở nơi khác." → chết |
| **Trung bình — novelty-based** | "Chúng tôi là những người đầu tiên áp dụng append-only event log cho Status_Event bảo trì." | "First" không kiểm chứng được, và roadmap của chính bạn cấm dùng. → chết |
| **Tốt — consequence-based** | "Các nghiên cứu đã công bố biểu diễn trạng thái bảo trì như một scalar hiện tại (`not treated`, `completed`, `Condition`); do đó không thể tái dựng ai đã chuyển trạng thái, dựa trên bằng chứng nào, và việc đóng hạng mục có được nghiệm thu hợp lệ hay không — mâu thuẫn cross-view trong chính các case study đã công bố cho thấy hệ quả này. Chúng tôi đặc tả và kiểm chứng một hợp đồng khắc phục điều đó." | Sống được — vì đứng trên **cái đã có trong tài liệu**, không đứng trên **cái không có** |

Lưu ý cấu trúc: gap statement tốt trích dẫn những gì prior art **đã làm** rồi chỉ ra chỗ nó dừng lại. Gap statement xấu trích dẫn sự trống rỗng.

---

## 6. Việc cần làm, theo thứ tự

1. **Chạy một vòng absence-confirmation search ngoài ngành** (một buổi là đủ) với các từ khóa ở mục 2. Ghi lại thành một mục ngắn trong evidence base: từ vựng đã tìm, cơ sở dữ liệu, khoảng thời gian, kết quả. Mục tiêu **không** phải để tìm thêm bài cho Paper 2 — mà để **biết trước** reviewer sẽ ném gì vào bạn, và để có thể viết một câu phòng thủ chủ động trong phần Related Work.
2. **Viết một đoạn "delimitation" thẳng thắn**: "append-only event history là một pattern đã có (event sourcing, temporal database, blockchain provenance); đóng góp của bài này không phải cơ chế đó, mà là ngữ nghĩa bảo trì và các guard gắn vào nó, cùng hợp đồng validation cho chuỗi tích hợp." Chủ động thừa nhận trước sẽ mạnh hơn nhiều so với bị chỉ ra.
3. **Không sửa §7.2 / §7.3 của Round 3B.** Chúng đang đúng. Nếu có sửa, chỉ sửa theo hướng làm rõ hơn rằng append-only là cơ chế.
4. **Chuyển trọng lượng novelty sang các mục đang `FREEZE_PROVISIONALLY` / `EXPERT_REVIEW_REQUIRED`** (authorization, closure/reopen guard, cardinality, SoD). Đó là chỗ prior art thật sự yếu — Round 3B §5.3, §5.5, §5.6 đều ghi `FREEZE_AS_CORE_GAP` với lý do rõ ràng. Tổ chức expert review theo mục §10.7 của Round 3B là đường đi hợp lý nhất hiện giờ.
5. **Viết gap statement theo mẫu consequence-based**, dùng chính dữ liệu mâu thuẫn trong Round 3B §2.4 làm bằng chứng.
6. **Kiểm tra lại ADR** `ADR_ACTION_STATUS_EVENT_20260804_DRAFT.md` (roadmap §6.2 ghi rõ: chưa được chấp nhận) để bảo đảm nó phát biểu Status_Event như một *cấu phần của hợp đồng*, chứ không như *đóng góp trung tâm*.

---

## Kết luận

Bạn nghĩ "đủ rồi" — tôi hiểu vì sao, bốn vòng deep-read là một khối lượng công việc nghiêm túc và kết luận `CLOSE_SEARCH` là hợp lý **cho mục đích của nó**. Nhưng `CLOSE_SEARCH` trả lời câu hỏi "*tôi có cần tìm thêm để viết spec không?*", chứ không trả lời câu hỏi "*cái này có phải là điều chưa ai biết không?*". Bạn đang dùng câu trả lời của câu hỏi thứ nhất cho câu hỏi thứ hai.

Và tin tốt: **bạn không cần append-only làm novelty chính**. Bạn đã có một novelty mạnh hơn nhiều, đã được khóa trong §7.2 và §5.9 sau bốn vòng deep-read — hợp đồng tích hợp identity → event → authorization → verification → guarded closure, kèm hợp đồng validation cho chính chuỗi đó. Nó khó tấn công hơn, có hậu quả thực tế rõ hơn, và quan trọng nhất: **nó có thể thất bại trong kiểm chứng**, nên khi nó vượt qua thì kết quả mới có ý nghĩa.

Hạ append-only xuống làm cơ chế. Đẩy guard và accountability lên làm luận điểm.

---

### Giới hạn của câu trả lời này

- Tôi **không chạy tìm kiếm tài liệu mới** cho câu trả lời này. Các thuật ngữ ở mục 2 là **gợi ý từ khóa để bạn tự tra cứu và tự xác minh**, không phải trích dẫn đã kiểm chứng. Đừng đưa bất kỳ thuật ngữ nào trong đó vào bản thảo dưới dạng citation trước khi tự đọc nguồn gốc.
- Tôi đọc ở chế độ chỉ-đọc các file trong `02_EVIDENCE_BASE/RQ2_GATES2_3/`: `00_README_START_HERE.md` (v2.2), `G2_G3_ROUND3B_HISTORY_ACCOUNTABILITY_AND_SEARCH_CLOSURE.md`, `G2_G3_PAPER2_CURRENT_ROADMAP_v2.1_20260804.md`, và phần đầu `G2_G3_ROUND4_CQ_CONSTRAINT_ACCOUNTABILITY_DEEP_READ_20260809.md`. Tôi chưa đọc Round 1, Round 2, Round 3A, ADR draft, và các file governance cấp trên — nếu ở đó có quyết định khác, ưu tiên theo `SOURCE_OF_TRUTH_HIERARCHY_v2.1.md`.
- Không có file nào trong thesis repository bị chỉnh sửa.
