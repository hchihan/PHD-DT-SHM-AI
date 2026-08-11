# Sensor-to-BIM có phải novelty chính của Paper 2 không?

## Trả lời ngắn: Không

Sensor-to-BIM **không phải** novelty của Paper 2, và việc xây contribution statement xoay quanh liên kết `Sensor_ID` ↔ IFC `GlobalId` sẽ bị reviewer đánh trượt gần như chắc chắn. Đây là điểm đã được chính hồ sơ nghiên cứu của anh/chị chốt từ trước, không phải ý kiến riêng của tôi.

---

## 1. Claim → Evidence

**Claim:** Sensor-to-BIM linking và IFC GlobalId là ESTABLISHED PRIOR ART, không được claim novelty độc lập.

**Evidence (trong chính repo luận án):**

- `03_PAPERS\PAPER_2\PAPER2_CURRENT_DIRECTION_v2.1_20260804.md` §3, mục *"Established prior art — excluded from independent novelty"* liệt kê thẳng: *"Sensor-to-BIM; BIM-linked records; IFC GlobalId; BIM-CMMS; generic maintenance/action workflow; competency questions; provenance; SHACL/SPARQL/MVD/IDS/database validation; ... direct/inverse navigation; ... viewers/websites."*
- Cũng file đó §1: *"Its novelty is not a software stack, BIM viewer, database, ontology in isolation, or automatic maintenance decision."*
- `00_GOVERNANCE\AGENT_RULES.md` §5: *"Không claim độc lập novelty cho sensor-to-BIM, IFC GlobalId, BIM-CMMS, CQ, provenance, SHACL/SPARQL/MVD/IDS/database validation, generic fixtures, direct/inverse navigation, human-in-the-loop hoặc viewer/website."*
- `08_AI_SKILL_SYSTEM\phd-dt-research-skills\_phd-canon\novelty-boundary.md` xếp "sensor-to-BIM linking" và "IFC GlobalId as a persistent component identifier" vào danh sách *classify as PRIOR ART by default*, và dùng đúng câu hỏi này làm worked example.

Nói cách khác: bốn nguồn quản trị độc lập trong repo đều đã kết luận giống nhau. Nếu contribution statement của Paper 2 đặt sensor-to-BIM ở vị trí trung tâm, nó sẽ mâu thuẫn trực tiếp với chính direction document của paper đó.

## 2. Vậy cái gì mới là candidate novelty?

Theo `PAPER2_CURRENT_DIRECTION_v2.1_20260804.md` §3 (*Candidate novelty boundary*), phần có thể bảo vệ được là **chuỗi tích hợp**, chứ không phải từng kỹ thuật rời:

- identity ổn định cho inspection–action records;
- **append-only `Status_Event` history** (lịch sử không ghi đè);
- **actor-bound authorization** và rework có trách nhiệm;
- **post-action verification** (`completed` ≠ verified closure);
- **guarded closure / reopen**;
- evidence-basis preservation; mutation/oracle đặc thù cho chuỗi;
- paired forward/reverse query-answer parity.

Quy tắc quyết định (decomposition rule): *đơn vị đóng góp có thể bảo vệ là chuỗi tích hợp, không phải từng kỹ thuật.* Câu hỏi phải trả lời được là: **tổ hợp này có làm được việc mà các thành phần rời không làm được không?** `Sensor_ID → BIM_GUID` chỉ là **mắt xích đầu** của chuỗi đó — nó là điều kiện cần, không phải đóng góp.

## 3. Contribution statement (~120 từ, tiếng Anh — bản dùng khi đã có bằng chứng G2/G3)

> This paper's contribution is not the linking of sensor identifiers to IFC GlobalId, which is established prior art in BIM-based structural health monitoring. Instead, the paper specifies and validates an identity-governed evidence-to-action traceability chain in which Sensor_ID, BIM_GUID at a declared Model_Version_ID, Condition_Evidence_ID with its structured Condition Evidence Index, Inspection_Record_ID and Action_Record_ID are bound by explicit identity, cardinality and provenance rules, and in which every action state change is retained as append-only Status_Event history under actor-bound authorization, post-action verification and guarded closure or reopen. Within the reviewed corpus, no single model carries these elements as one preregistered, query-validated chain. Each element individually is prior art; the contribution is the integrated, auditable chain and the executable acceptance tests that demonstrate it.

(120 từ. Lưu ý hai chi tiết cố ý: câu mở đầu **chủ động nhường** sensor-to-BIM cho prior art — đây là động tác làm reviewer hạ cảnh giác, chứ không phải điểm yếu; và cụm *"within the reviewed corpus"* là bắt buộc, không được bỏ.)

## 4. CẢNH BÁO QUAN TRỌNG — bản trên chưa dùng được ở thời điểm hiện tại

`PAPER2_CURRENT_DIRECTION_v2.1_20260804.md` §9 ghi rõ: **G2 chưa freeze, G3 execution chưa mở, "Evidence is currently insufficient to claim G2 completion, G3 validation, or Paper 2 submission readiness."** Vì vậy động từ *"specifies and validates"* hiện **chưa có bằng chứng đỡ**. Bản dùng được ngay hôm nay (~120 từ):

> This paper's contribution is not the linking of sensor identifiers to IFC GlobalId, which is established prior art in BIM-based structural health monitoring. The paper instead proposes an implementation-neutral, identity-governed evidence-to-action traceability specification binding Sensor_ID, BIM_GUID at a declared Model_Version_ID, Condition_Evidence_ID, Inspection_Record_ID and Action_Record_ID under explicit identity, cardinality and provenance rules, with append-only Status_Event history, actor-bound authorization, post-action verification and guarded closure. Competency questions are preregistered and mapped to executable acceptance tests. Within the reviewed corpus, no single model carries these elements as one validated chain; each element individually is prior art. The specification is a candidate contribution, corpus-bounded and pending baseline acceptance and executed validation.

## 5. Limitation

- Kết luận "prior art" ở đây là **corpus-bounded** (Rounds 1–3B, `CLOSE_SEARCH`), không phải systematic review. Không được viết "first", "no study worldwide", hay bất kỳ universal-absence claim nào.
- Ngay cả cụm candidate novelty (event history / authorization / verification / guarded closure) **cũng chưa được validate**. Trước khi G2 được chấp nhận và G3 chạy, mọi phát biểu phải mang nhãn *candidate*.
- Nếu anh/chị có bằng chứng trong corpus cho thấy sensor-to-BIM cần được phân loại lại, tôi sẵn sàng xem lại — nhưng chỉ trên cơ sở nguồn cụ thể có locator, không phải trên cơ sở khẳng định lại mạnh hơn.

## 6. Next action

1. **Đừng** viết contribution statement quanh `Sensor_ID` ↔ `GlobalId`. Chuyển nội dung đó xuống phần Background/Related Work như nền tảng đã có.
2. Dùng bản §4 (có hedging) cho draft hiện tại; nâng cấp lên bản §3 chỉ sau khi G2 được chấp nhận và G3 chạy xong.
3. Rà lại Abstract và Introduction của Paper 2 xem có chỗ nào đang vô tình nâng sensor-to-BIM lên thành contribution không — lỗi này thường nằm rải rác chứ không chỉ ở một câu.
4. Chuẩn bị sẵn một đoạn 3–4 câu trả lời cho câu hỏi phản biện chắc chắn sẽ có: *"tổ hợp này làm được gì mà các thành phần rời không làm được?"* — đó mới là chỗ contribution sống hay chết.
