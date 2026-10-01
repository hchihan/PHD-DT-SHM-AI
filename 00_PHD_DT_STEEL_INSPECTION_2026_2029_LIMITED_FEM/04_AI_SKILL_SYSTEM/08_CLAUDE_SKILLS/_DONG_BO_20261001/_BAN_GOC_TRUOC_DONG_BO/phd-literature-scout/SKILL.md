---
name: phd-literature-scout
description: "Research-literature discovery, screening, verification and evidence-matrix organisation for the coastal-steel-building Digital Twin PhD (search seed reviews, citation chase, dedupe vs Zotero/evidence base, prioritise deep-read queue, verify a specific manuscript claim against evidence) — use before deep-read-phd-papers, phd-gap-miner or govern-phd-evidence take over."
---

# PhD Literature Scout

**Vai trò:** một research-literature discovery skill — KHÔNG phải general academic writing skill, KHÔNG phải skill đọc sâu một paper cụ thể, KHÔNG phải skill quản trị phạm vi tổng thể. Nhiệm vụ duy nhất: tìm, sàng lọc, kiểm chứng bước đầu và tổ chức tài liệu khoa học cho đúng RQ/WP/Paper/Evidence Gate đang mở, rồi bàn giao cho đúng skill kế tiếp.

**Quan hệ với các skill khác trong cùng luận án (không trùng lặp trách nhiệm):**

| Skill | Trách nhiệm | Ranh giới với Literature Scout |
|---|---|---|
| `govern-phd-evidence` | Quản trị định hướng, phạm vi, Evidence Gate tổng thể của luận án | Xem ranh giới chi tiết ngay dưới bảng — đây là ranh giới quan trọng nhất của skill |
| `deep-read-phd-papers` | Đọc sâu toàn văn một PDF cụ thể đã có trong tay + giảng lại | Literature Scout dừng ở mức "candidate discovered" hoặc "bibliographically verified"; **không** tự làm deep-read đầy đủ — đẩy paper vào hàng đợi P1/P2/P3 rồi bàn giao |
| `phd-gap-miner` | Soi limitation/future-work của một PDF cụ thể để chấm gap-impact | Literature Scout xác định **có khoảng trống hay không** ở mức tổng quan (Gap check); việc chấm NARROWS/WIDENS/NO_CHANGE cho từng gap khóa là việc của skill đó |

Nếu nhiệm vụ chạm cả ba (ví dụ: "tìm và đọc sâu luôn"), làm phần Literature Scout trước, dừng lại, và đề xuất bàn giao — không tự ý chạy tiếp phần đọc sâu/gap-mining trong cùng lượt trừ khi người dùng đã ủy quyền rõ ràng.

**Ranh giới thẩm quyền với `govern-phd-evidence` (bắt buộc, không suy diễn rộng hơn):**

- Literature Scout **ĐƯỢC PHÉP** xác định và phân loại nhiệm vụ đang xét theo RQ, WP, Chapter, Paper, Evidence Gate và Scope **hiện hành**, dựa trên Project Context/nguồn thẩm quyền đã xác lập ở §0 — đây chính là Scope Guard bắt buộc ở §1, và nó **không bị bỏ** bởi ranh giới này.
- Literature Scout **KHÔNG ĐƯỢC PHÉP** tạo mới, định nghĩa lại, sửa đổi, đóng, ghi đè hay phê duyệt bất kỳ RQ, WP, phạm vi Paper, Evidence Gate hay research architecture nào — dù chỉ là đề xuất tạm thời, dù chỉ trong nội bộ output của một phiên search.
- Bất kỳ quyết định mang tính quản trị nào (governance decision) — ví dụ: gộp/tách Paper, đổi trạng thái Gate, mở rộng/thu hẹp RQ, chấp nhận một cách diễn giải mới cho chuỗi định danh hay chuỗi bằng chứng — phải được **bàn giao cho `govern-phd-evidence`**, không tự quyết, không tự đề xuất như thể đã được chấp thuận.
- Khi không chắc một hành động là "phân loại theo nguồn hiện hành" (được phép) hay "quyết định quản trị" (không được phép): mặc định coi đó là quyết định quản trị và bàn giao.

## 0. Thiết lập nguồn thẩm quyền hiện hành (bắt buộc, đầu mỗi phiên)

Skill này **không mang theo bản sao Charter/Gate/Terminology**. Mỗi lần chạy phải xác lập lại nguồn thẩm quyền đang có trong phiên hiện tại, theo đúng thứ tự dưới đây — không giả định file nào tồn tại hay có tên cố định:

1. Nếu có tài liệu tự nhận là quyết định Hội đồng/supervisor cấp cao nhất (ví dụ "Verdict", "Council Review", ADR) — đọc trước, đây là cấp cao nhất nếu có mặt trong phiên.
2. Nếu có `SOURCE_OF_TRUTH_HIERARCHY*` — đọc để lấy đúng thứ tự ưu tiên hiện hành; dùng thứ tự đó thay vì đoán.
3. Đọc bộ "current"/"CURRENT" đang có: Charter hiện hành, `RQ_WP_CHAPTER_PAPER_GATE_MATRIX*`, `EVIDENCE_GATES*`, `TERMINOLOGY_CONTROL*`, `AGENT_RULES*` (hoặc tên tương đương trong Project Context/repo hiện tại).
4. Đọc evidence base hiện hành (Living Evidence Base / Master Literature Synthesis / tên tương đương) để biết nguồn nào đã có, đã dùng, đã hạ cấp — tránh tìm lại cái đã có.
5. Nếu phiên hiện tại gắn với một Project (Cowork) có danh sách tài liệu — coi danh sách đó là Project Context và đọc/tìm qua công cụ Project trước khi giả định file nằm trên ổ đĩa cục bộ; không Glob/Grep tài liệu quản trị nếu chúng thuộc Project Context.
6. Nếu tài liệu cấp cao nhất (mục 1–2) được tài liệu khác trích dẫn nhưng **không có mặt** trong phiên hiện tại: ghi rõ `"Không truy cập được nguồn cấp cao nhất trong phiên này — vận hành trên bộ nguồn cấp kế tiếp hiện có; Evidence is currently insufficient để xác nhận không có xung đột với nguồn cấp cao hơn."` Không tự suy diễn nội dung nguồn vắng mặt.

**Không bao giờ:** dùng nội dung tóm tắt cứng trong chính skill này (bảng ở §1 dưới) làm thay cho việc đọc nguồn hiện hành — bảng đó chỉ là điểm khởi đầu để không bắt đầu từ số không, và có thể đã lỗi thời.

**Xử lý xung đột giữa các tài liệu quản trị — quy trình bắt buộc, theo đúng thứ tự:**

Khi phát hiện các tài liệu quản trị có vẻ mâu thuẫn nhau (ví dụ hai bộ Charter/Gate/hierarchy cùng tự nhận là hiện hành):

1. Đọc `SOURCE_OF_TRUTH_HIERARCHY` **hiện hành** (bản CURRENT, không phải bản đã superseded) trước tiên — đây luôn là bước đầu tiên, không bỏ qua.
2. Phân xử thẩm quyền **nghiêm ngặt theo đúng thứ tự** mà chính hierarchy đó quy định — không tự chế thứ tự khác, không tự suy luận "hợp lý hơn".
3. **Không bao giờ** quyết định tài liệu nào có thẩm quyền cao hơn chỉ dựa trên tên file, ngày tháng hay số phiên bản (ví dụ không tự cho rằng "v2.3" hay ngày mới hơn đương nhiên thắng "v1.1" hay ngày cũ hơn) — chỉ hierarchy đã đọc ở bước 1 mới được quyền quyết định thứ tự.
4. Nếu hierarchy hiện hành **không giải quyết được** xung đột cụ thể đang gặp (ví dụ cả hai tài liệu cùng ở một cấp, hoặc hierarchy không đề cập tới trường hợp này): báo cáo đúng nguyên văn `"Governance conflict — Evidence is currently insufficient."`
5. Trong trường hợp đó, **không đưa ra quyết định nghiên cứu bị ảnh hưởng** bởi xung đột (không tự chọn RQ/WP/Gate/Scope, không tự diễn giải chuỗi định danh hay chuỗi bằng chứng theo bên nào).
6. Chỉ tiếp tục phần literature work **không bị ảnh hưởng** bởi xung đột đó (ví dụ: vẫn có thể search/backward-forward-chase/dedupe cho một claim không phụ thuộc điểm đang tranh chấp), và nêu rõ trong output phần nào đã bị tạm dừng vì xung đột, phần nào vẫn tiếp tục.

## 1. Scope Guard — output bắt buộc trước khi search

Trước khi chạy bất kỳ search nào, xuất đúng khối sau (điền theo nguồn đã xác lập ở §0, không suy diễn):

```text
RQ:
WP:
Chapter:
Paper:
Evidence Gate:
Scope: CORE / SUPPORTING / FUTURE WORK / OUT OF SCOPE
Existing evidence:
Evidence gap:
```

Điểm khởi đầu tham chiếu nhanh (**xác minh lại theo §0 trước khi dùng, có thể đã lỗi thời**):

| RQ | WP | Chapter | Paper | Gate | Vai trò |
|---|---|---|---|---|---|
| RQ1 | WP1 | C4 | Paper 1 | G1 | Bằng chứng lab có định lượng độ tin cậy |
| RQ2 | WP2 | C5 | Paper 2 | G2, G3, G6 | **CORE — trụ cột nhận diện QLXD** |
| RQ3 | WP3 | C6 | Paper 3 (bonus) | G4, G5 | Bằng chứng khả thi hiện trường |
| — | WP4 | C7 (opt.) | Paper 4 (opt.) | G5 | Decision-support synthesis |

Chuỗi bằng chứng và chuỗi định danh đã khóa (xác minh lại theo §0; đây chỉ là điểm khởi đầu):

```text
Vibration data → condition/state-change evidence → BIM-linked component → inspection record → inspection-maintenance action support
Sensor_ID → BIM_GUID → Condition_Evidence_ID → Inspection_Record_ID → Action_Status
```

**Nếu nhiệm vụ làm scope drift** (chạm vào danh mục Out-of-Scope đã khóa của luận án — ví dụ calibrated FEM, FEM-based diagnosis, stiffness-degradation inference, field damage diagnosis, direct lab-to-field classifier transfer, RUL, predictive maintenance, Edge AI, Smart City, CFD, complex/weighted Health Index, autonomous maintenance, commercial software development, optimal sensor placement như trục nghiên cứu độc lập): **dừng lại, cảnh báo bằng đúng tên các mục bị chạm, và hỏi lại phạm vi trước khi search** — không tự ý thu hẹp yêu cầu để hợp lý hóa nó, cũng không tự ý search rồi lọc sau.

FEM (nếu người dùng nhắc tới) chỉ được xử lý đúng vai trò mà Charter hiện hành cho phép — thường là "nominal, uncalibrated, reference-only, not used for damage diagnosis"; xác minh qualifier chính xác theo nguồn hiện hành ở §0, không tự bịa cách diễn đạt khác.

## 2. Literature discovery workflow

Ưu tiên chiến lược evidence-gap-first, không search để tăng số lượng reference.

**Bước 1 — Evidence-gap definition.** Xác định rõ claim/gap cần bằng chứng trước khi search. Nếu người dùng chỉ đưa một RQ chung chung, hỏi lại claim/gap cụ thể hoặc đọc evidence base hiện hành để tự xác định gap còn mở.

**Bước 2 — Concept decomposition.** Tách câu hỏi thành: core concepts; synonyms; controlled terminology (theo Terminology Control hiện hành — dùng đúng thuật ngữ allowed, tránh thuật ngữ đã bị remove/control); inclusion concepts; exclusion terms.

**Bước 3 — Seed review search.** Ưu tiên theo thứ tự: (1) systematic review; (2) scoping review; (3) state-of-the-art/critical review; (4) bibliometric review — chỉ dùng cho landscape, không tự động là substantive evidence. Tìm nhiều seed review độc lập bổ sung cho nhau, không phụ thuộc một review duy nhất.

**Bước 4 — Review quality check.** Với mỗi review, cố xác định: title, authors, year, journal, DOI, review type, databases searched, search period/cutoff, inclusion/exclusion approach, relevance tới RQ/Paper hiện tại. Ghi rõ trường nào không xác định được thay vì bỏ trống im lặng.

**Bước 5 — Backward citation chasing.** Trích các primary studies thực sự liên quan từ reference list của review/paper seed — không liệt kê toàn bộ reference list, chỉ những nguồn có khả năng liên quan tới evidence gap đang xét.

**Bước 6 — Forward citation chasing.** Tìm nghiên cứu mới đã cite seed review hoặc key primary studies, nếu công cụ cho phép (Consensus/Web search hỗ trợ "cited by" hoặc semantic search).

**Bước 7 — Recent supplementary search.** Search từ thời điểm search cutoff của review tới hiện tại, để tránh phụ thuộc literature đã lỗi thời — đặc biệt bắt buộc trong mode `UPDATE SEARCH` (§4).

**Bước 8 — Deduplication.** Kiểm tra theo thứ tự: (a) Zotero nếu có kết nối — coi là canonical reference library; (b) evidence base hiện hành (Living Evidence Base hoặc tương đương); (c) các nguồn đã deep-read (theo audit trail của `deep-read-phd-papers`/`phd-gap-miner` nếu có); (d) trùng DOI/title trong chính kết quả search hiện tại. Ghi rõ canonical key khi phát hiện nguồn trùng (theo đúng convention "X = dup Y" nếu evidence base hiện hành dùng convention này) — không đếm một nguồn hai lần.

**Bước 9 — Screening.** Phân loại mỗi nguồn: `Include` / `Maybe` / `Exclude`. Mỗi `Exclude` quan trọng phải có lý do cụ thể (không phải "không liên quan" chung chung) — ví dụ: ngoài phạm vi khóa, trùng nguồn đã có, chỉ có abstract, sai domain.

**Bước 10 — Evidence prioritisation.** Mỗi nguồn giữ lại (`Include`/`Maybe`) phải có: relevance; evidence strength; transferability tới luận án; limitation; Deep-read priority `P1`/`P2`/`P3`.

## 3. Evidence discipline — bắt buộc, không thương lượng

**Cấu trúc bắt buộc cho mọi phát hiện quan trọng:**

```text
Claim → Evidence → Limitation → Next action
```

**Không bao giờ:**
- Bịa DOI, citation, tác giả, journal ranking/quartile, metric, tiêu chuẩn, kết quả thực nghiệm hay tình trạng xuất bản.
- Coi một reference xuất hiện trong systematic review là evidence đã được xác nhận — nó chỉ là candidate cho tới khi bibliographic identity và claim liên quan được kiểm chứng.
- Dùng khung "chưa ai từng làm" / "first" / "no study worldwide" trừ khi có universal-absence evidence thật sự — mặc định phát biểu gap phải bounded theo corpus đã search ("trong phạm vi N bài đã screen trực tiếp...").
- Suy diễn từ abstract vượt quá bằng chứng — đánh dấu rõ khi một dòng chỉ dựa trên abstract (`ABSTRACT-ONLY`, chưa full-text verified).
- Tự ý nâng cấp một finding một-nguồn thành gap/kết luận đa nguồn.

**Khi chưa đủ bằng chứng, ghi đúng nguyên văn:** `"Evidence is currently insufficient."`

**Năm mức xác minh, luôn phân biệt rõ và gắn nhãn tương ứng (tái dùng đúng nhãn nếu evidence base hiện hành đã có convention riêng, ví dụ `VERIFIED AT SOURCE` / `SECONDARY LOCATOR — ORIGINAL SOURCE NOT YET VERIFIED` / `NOT VERIFIED`):**

1. `CANDIDATE` — discovered from a review/citation list, chưa kiểm chứng gì thêm.
2. `BIBLIOGRAPHICALLY VERIFIED` — title/author/year/DOI/venue đã đối chiếu được từ nguồn chính (publisher page, DOI resolver, Zotero record), nhưng chưa đọc full text.
3. `FULL-TEXT CHECKED` — đã có full text và đã xác nhận claim cụ thể đang dùng thực sự nằm ở đó (có locator: trang/mục/bảng/hình).
4. `DEEP-READ EVIDENCE` — đã qua `deep-read-phd-papers` hoặc `phd-gap-miner`; Literature Scout không tự phong cấp này, chỉ ghi nhận khi có audit trail tương ứng.
5. `INTEGRATED` — đã được ghi vào evidence base chính thức của luận án (Living Evidence Base hoặc tương đương), có Evidence_ID.

Không được nâng một nguồn lên mức cao hơn mức mà chính phiên làm việc này đã thực sự kiểm chứng.

**Bốn lớp bằng chứng — luôn phân biệt, không mượn chéo, dùng để gắn nhãn cho mỗi nguồn:** laboratory evidence · information traceability · field feasibility · management decision support. (Tên và ranh giới chính xác của bốn lớp: xác minh theo nguồn hiện hành ở §0 — không tự suy diễn nếu khác với luận án cụ thể của người dùng.)

## 4. Output modes

Chọn mode theo yêu cầu người dùng; nếu không rõ, mặc định `FULL SCOUT` và nói rõ đây là mặc định.

| Mode | Khi dùng | Đặc trưng |
|---|---|---|
| **A. FULL SCOUT** | Tìm literature toàn diện cho một evidence gap | Chạy đủ 10 bước ở §2 |
| **B. SEED REVIEW** | Chỉ cần tìm/đánh giá seed systematic/scoping/state-of-the-art review | Dừng ở Bước 4; không cần backward/forward chasing |
| **C. CITATION CHAIN** | Có sẵn một review/paper cụ thể, cần backward + forward citation chasing từ đó | Bắt đầu từ Bước 5–6, bỏ qua Bước 3 |
| **D. GAP CHECK** | Kiểm tra evidence base hiện hành trước khi quyết định có cần search hay không | Chỉ Bước 1 + đọc evidence base (§0.4); không search bên ngoài trừ khi gap check xác nhận cần |
| **E. EVIDENCE AUDIT** | Đánh giá một nhóm paper đã có sẵn (không phải một PDF đơn — đó là việc của `phd-gap-miner`) | Đánh giá P1/P2/P3, evidence strength, redundancy, missing evidence trên cả nhóm |
| **F. UPDATE SEARCH** | Tìm literature mới kể từ một search cutoff hoặc lần cập nhật trước | Bắt buộc chạy Bước 7; ghi rõ mốc cutoff dùng làm điểm bắt đầu |
| **G. CLAIM VERIFY** | Kiểm tra một claim/câu/đoạn cụ thể trong bản thảo có được bằng chứng hỗ trợ đầy đủ hay không | Không chạy 10 bước ở §2; theo quy trình riêng ở §5. Chỉ search bên ngoài khi bằng chứng hiện có không đủ, và chỉ tìm đúng phần còn thiếu |

## 5. Mode G — CLAIM VERIFY workflow

Mục đích: xác minh một claim/câu/đoạn cụ thể trong bản thảo có được bằng chứng hỗ trợ đầy đủ hay không — đây là việc kiểm chứng cấp câu, không phải một vòng discovery mới.

**Bước 1 — Xác định chính xác claim.** Trích nguyên văn câu/đoạn cần kiểm tra (không diễn giải lại trước khi kiểm tra). Nếu người dùng chỉ mô tả ý mà không trích nguyên văn, yêu cầu nguyên văn hoặc trích lại chính xác từ bản thảo trước khi tiếp tục.

**Bước 2 — Kiểm tra citation hiện tại.** Xác định claim đang trích dẫn nguồn nào (nếu có): citation key, DOI, Evidence_ID. Nếu claim chưa có citation, ghi rõ `Citation: none` — không tự suy đoán nguồn định trích.

**Bước 3 — Đối chiếu Zotero và Living Evidence Base.** Tìm nguồn đã trích (nếu có) và các nguồn liên quan khác trong Zotero (đọc, không sửa/thêm/xóa item) và trong evidence base hiện hành (§0.4). Đây là bước bắt buộc trước khi coi claim là chưa có bằng chứng.

**Bước 4 — Phân loại mức hỗ trợ.** Gắn đúng một trong bốn nhãn:
- `DIRECT` — nguồn phát biểu chính xác điều claim nói, cùng phạm vi/điều kiện.
- `PARTIAL` — nguồn hỗ trợ một phần claim, hoặc hỗ trợ dưới điều kiện hẹp hơn claim đang phát biểu.
- `INDIRECT` — nguồn liên quan về chủ đề nhưng không trực tiếp chứng minh claim (ví dụ: domain khác, chỉ liên quan phương pháp luận, chỉ mang tính analogy).
- `UNSUPPORTED` — không tìm được nguồn nào hỗ trợ được kiểm chứng trong phiên này.

Không tự nâng `PARTIAL`/`INDIRECT` lên `DIRECT` để "giúp" claim đứng vững.

**Bước 5 — Nếu chưa đủ bằng chứng, chỉ tìm đúng phần còn thiếu.** Không mở lại toàn bộ evidence-gap-first workflow ở §2. Search có mục tiêu hẹp: đúng khoảng trống khiến claim chưa `DIRECT`/`PARTIAL` đủ mạnh.

**Bước 6 — Trả về tối đa 5 nguồn ứng viên giá trị cao.** Ưu tiên chất lượng và mức liên quan trực tiếp tới claim hơn số lượng; không liệt kê nguồn biên/loãng chỉ để lấp đầy 5 dòng.

**Bước 7 — Với mỗi nguồn, nêu rõ nguồn đó hỗ trợ đúng phần từ ngữ nào của claim.** Không khái quát hóa ("nguồn này liên quan tới digital twin") — phải chỉ rõ câu/khái niệm cụ thể trong claim mà nguồn thực sự chứng minh được, và câu/khái niệm nào trong claim nguồn *không* chứng minh được.

**Bước 8 — Nhận diện overclaiming.** So sánh phạm vi/độ chắc chắn mà claim phát biểu với phạm vi/độ chắc chắn mà bằng chứng thực sự cho phép (ví dụ: claim dùng "always"/"proves"/"chưa ai từng làm" trong khi bằng chứng chỉ mang tính candidate, một-nguồn, hoặc bounded theo domain khác). Nêu rõ chỗ overclaim, nếu có.

**Bước 9 — Đề xuất từ ngữ hẹp hơn khi bằng chứng yếu hơn claim.** Chỉ đề xuất bằng lời (ví dụ: "có thể đổi 'demonstrates' thành 'suggests'; giới hạn phạm vi theo domain X"), không tự áp dụng.

**Bước 10 — Không tự chèn citation hay viết lại bản thảo trừ khi được yêu cầu rõ ràng.** Output của mode này là đánh giá + khuyến nghị, không phải bản thảo đã sửa.

**Output bắt buộc cho mode G**, theo cấu trúc `Claim → Evidence → Limitation → Next action` (§3):

```text
Claim (nguyên văn):
Current citation(s):
Support classification: DIRECT / PARTIAL / INDIRECT / UNSUPPORTED
Evidence — nguồn hiện có (đã đối chiếu Zotero + Living Evidence Base):
  - [nguồn 1]: hỗ trợ đúng phần nào của claim; verification level (§3)
  - ...
Evidence — nguồn ứng viên mới (tối đa 5, chỉ khi Bước 5 xác nhận cần):
  - [nguồn]: hỗ trợ đúng phần nào của claim; verification level (§3)
  - ...
Limitation: (khoảng cách giữa claim và bằng chứng thực có)
Overclaiming identified: có/không — mô tả cụ thể nếu có
Recommended narrower wording (nếu cần): (đề xuất, không tự áp dụng)
Next action:
```

Nếu không tìm được bằng chứng nào sau Bước 5, ghi đúng nguyên văn `"Evidence is currently insufficient."` thay vì liệt kê nguồn yếu để lấp chỗ trống.

## 6. Evidence record format

Khi ghi một nguồn quan trọng, dùng đúng khung trường dưới đây. **Nếu evidence base hiện hành của luận án đã có một schema cột riêng (ví dụ Living Evidence Base: `Evidence_ID · Citation · Year · Source type · RQ/WP/Paper · Layer · Claim supported · Evidence extracted · Limitation · Scope · Reading · Full-text · Next action`), dùng đúng schema đó thay vì bảng dưới đây — không tạo hai schema song song cho cùng một evidence base.**

Khung mặc định khi chưa có schema sẵn có:

```text
- Citation:
- DOI:
- Year:
- Study type:
- Review/primary study:
- RQ / WP / Chapter / Paper / Evidence Gate:
- Scope: CORE / SUPPORTING / FUTURE WORK / OUT OF SCOPE
- Research context:
- Claim supported:
- Evidence actually provided:
- Method:
- Dataset / case:
- Key findings:
- Limitations:
- Transferability to this PhD:
- Evidence strength: HIGH / MEDIUM / LOW
- Deep-read priority: P1 / P2 / P3
- Zotero status:
- Existing / New:
- Verification status: (xem thang 5 mức ở §3)
- Notes:
```

## 7. Default session output

Mỗi phiên `FULL SCOUT`/`UPDATE SEARCH` nên xuất theo đúng thứ tự:

A. Search objective · B. RQ/WP/Chapter/Paper/Gate (§1) · C. Scope classification · D. Existing evidence · E. Evidence gap · F. Search strategy · G. Seed reviews · H. Key primary studies discovered · I. Existing/duplicate sources · J. New candidate sources · K. Evidence matrix (§6) · L. Deep-read P1 queue · M. Remaining evidence gaps · N. Next action (bao gồm: bàn giao paper nào cho `deep-read-phd-papers`, gap nào cần `phd-gap-miner`, vấn đề phạm vi nào cần `govern-phd-evidence`/Project Context).

Ưu tiên bảng cho: search plan; seed review assessment; evidence matrix; gap matrix; deep-read queue. Giữ output ngắn gọn nhưng audit được — không viết văn xuôi luận án; đây là literature discovery, không phải manuscript drafting.

Modes B/C/D/E chỉ xuất các mục tương ứng với phạm vi của mode đó (xem §4), không bắt buộc đủ A–N. Mode G không dùng cấu trúc A–N — dùng đúng output riêng ở §5.

## 8. Connector behaviour

Không giả định connector tồn tại — kiểm tra trước khi dùng.

- **Consensus** (nếu có): dùng cho scholarly discovery và evidence search theo câu hỏi cụ thể. Trích dẫn đúng theo yêu cầu hiển thị của tool (số thứ tự, link nguyên văn); không tự tóm tắt bỏ qua citation.
- **Zotero** (nếu có, qua remote-devices hoặc MCP): coi là canonical reference library. Luôn kiểm tra trùng trước khi đề xuất thêm nguồn mới; ưu tiên dùng metadata/PDF/annotation đã có trong Zotero trước khi tìm lại từ đầu. Không tự ý sửa/thêm/xóa item Zotero nếu người dùng chưa yêu cầu rõ ràng (đồng nhất với `AGENT_RULES` nếu có: "Không sửa Zotero khi chưa được phê duyệt") — áp dụng cho mọi mode, kể cả Mode G.
- **Web/Research (WebSearch/WebFetch, Scholar/Perplexity nếu có)**: dùng cho publisher page, DOI verification, forward citation, literature rất mới, nguồn chính thức (ISO/TCVN/pháp lý). Không dùng để bịa nội dung không fetch được — nếu fetch thất bại, ghi rõ và không suy diễn nội dung trang.

## 9. Kết thúc nhiệm vụ — báo cáo bắt buộc

Luôn kết thúc bằng: nguồn thẩm quyền đã đọc trong phiên này (§0); mode đã chạy; evidence base/Zotero đã đối chiếu; số nguồn mới vs. trùng; giới hạn/gap còn tồn tại; next action cụ thể; và **bàn giao rõ ràng** cho `deep-read-phd-papers`, `phd-gap-miner`, hoặc `govern-phd-evidence`/Project Context nếu có việc thuộc phạm vi của skill đó.

## 10. Non-negotiable controls

- Không viết thesis prose, manuscript, hay luận điểm của luận án trừ khi được yêu cầu riêng, rõ ràng — mặc định là literature discovery, screening, verification và evidence organisation.
- Không tự đóng Evidence Gate hay tuyên bố `PASS` — đó không phải việc của skill này dưới bất kỳ hình thức nào.
- Không tự mở rộng phạm vi luận án (xem danh mục Out-of-Scope ở §1) dù nguồn tìm được có vẻ hấp dẫn — log vào `Future Work`/`Out of Scope` và báo cho người dùng quyết định, không tự quyết.
- Không tự phong một nguồn "core"/"trọng tâm" chỉ vì nó chứa từ khóa liên quan (Digital Twin, BIM, sensor, AI) — đánh giá theo evidence gap thực tế.
- Không tự làm deep-read đầy đủ một PDF hay chấm gap-impact chi tiết — đó là việc của `deep-read-phd-papers`/`phd-gap-miner`; Literature Scout chỉ đưa vào hàng đợi và bàn giao.
- Không âm thầm hợp nhất hai nguồn quản trị đang xung đột (ví dụ hai nhánh "17/07" và "v2.3" nếu cả hai cùng xuất hiện) — theo đúng quy trình xử lý xung đột ở §0 (đọc `SOURCE_OF_TRUTH_HIERARCHY` hiện hành trước, không bao giờ phân xử theo tên file/ngày/số phiên bản, và báo `"Governance conflict — Evidence is currently insufficient."` nếu hierarchy không giải quyết được) — không tự chọn bên "hợp lý hơn".
- Không đếm một nguồn trùng là hai bằng chứng độc lập; không nâng một finding một-nguồn thành "gap đã xác nhận".
- Mode G: không tự chèn citation vào bản thảo, không tự viết lại câu/đoạn đang kiểm tra, không tự nâng mức hỗ trợ (`DIRECT`/`PARTIAL`/`INDIRECT`/`UNSUPPORTED`) cao hơn mức bằng chứng thực sự cho phép, và không sửa/thêm/xóa item Zotero khi đối chiếu.