# 10 — Novelty Check Summary (16/09/2026) — Paper 2 / Gate 2–3

**Phạm vi:** Kiểm tra mối đe dọa tính mới có giới hạn cho đúng 4 bài (A–D), không mở rộng tìm kiếm. Xem chi tiết Q1–Q12 từng bài trong `10_NOVELTY_CHECK_A_GRAGNANIELLO_2024.md`, `..._B_MARINIELLO_2025.md`, `..._C_GARCIA_2026.md`, `..._D_BELLON_2025.md` (cùng thư mục `01_EVIDENCE/`).

**Nguồn:** A, B, C đọc **FULL_TEXT** qua NotebookLM MCP (notebook "Ứng dụng BIM trong Giám sát Sức khỏe Công trình", 3/3 nguồn khớp chính xác tiêu đề/tác giả/DOI/tạp chí — xác nhận ở Bước 0). D đọc **ABSTRACT_ONLY** qua OpenAlex MCP (`W4409166607`) — toàn văn tại ScienceDirect bị chặn CAPTCHA, không vượt qua theo quy tắc an toàn.

---

## Bảng đối chiếu 4 bài × GAP 1/2/3 × C1/C2/C3

| | GAP 1 (Accountable Inspection Record) | GAP 2 (Condition Evidence Governance — validity/applicability) | GAP 3 (Multi-hop deterministic integrity validation) | C1 (Traceability framework 3 bản ghi) | C2 (Condition-Evidence Governance Contract) | C3 (Deterministic validation protocol) |
|---|---|---|---|---|---|---|
| **A — Gragnaniello 2024** | không | không | không | không | không | không |
| **B — Mariniello 2025** | một phần (status + performer `closedBy`; thiếu reviewer/supersession) | không (immutability ≠ validity, đã tự phân biệt) | một phần (PASS/FAIL + 4 loại negative test, nhưng thiếu BIM identity neo) | không (thiếu BIM_GUID đã xác minh — Q3 EVIDENCE_INSUFFICIENT) | không | một phần |
| **C — García 2026** | **đe dọa** (RACI đầy đủ 5 trường, thực nghiệm N=22 tệp IFC thật) | không (evidence validity vẫn NOT_ESTABLISHED; CDE state ≠ validity, đã tự phân biệt) | một phần (chuỗi 6 loại bản ghi có liên kết tường minh, nhưng không có sensor/condition evidence, không có negative-fixture tổng hợp cố ý) | không (không có sensor/condition data — chỉ quản trị publish/hold mô hình BIM) | không | không |
| **D — Bellon 2025** | **không xác định được (EVIDENCE_INSUFFICIENT)** — trùng chủ đề mạnh nhất nhưng chỉ có abstract | không xác định được | không xác định được | không xác định được | không xác định được | không xác định được |

Ký hiệu: "đe dọa" = mối đe dọa thực chất cần thu hẹp câu chữ; "một phần" = chạm một phần, chưa đủ để buộc thu hẹp nhưng cần ghi nhận; "không" = không chạm tới thành phần này; "không xác định được" = evidence insufficient, chưa thể kết luận.

---

## Kết luận theo từng khoảng trống

**GAP 1 — Accountable BIM-linked Inspection Record: THU HẸP.**
García 2026 chứng minh full-text, thực nghiệm (N=22 tệp IFC thật) rằng pattern accountable-record đầy đủ 5 trường (performer/reviewer/approver/status/supersession) **đã khả thi và đã triển khai** trong bối cảnh quản trị BIM/CDE — nhưng cho **quyết định xuất bản mô hình (model-deliverable governance)**, không phải cho **bản ghi kiểm tra tình trạng vật lý công trình neo trên Condition_Evidence_ID từ cảm biến**. Paper 2 **không được** tiếp tục claim tổng quát "accountable record pattern with performer/reviewer/approver/status/supersession chưa từng áp dụng cho bối cảnh BIM" — phải thu hẹp: novelty nằm ở việc neo accountable record vào **Condition_Evidence_ID xuất phát từ sensor/condition evidence**, điều García hoàn toàn không có (không có sensor/condition data trong bài).
Bài D (Bellon 2025) là rủi ro **chưa đóng** — trùng chủ đề mạnh nhất ("inspection... representation" trong IFC) nhưng evidence insufficient; không được coi GAP 1 là an toàn tuyệt đối cho tới khi đọc toàn văn D.
**Câu tuyên bố mới an toàn hơn (đề xuất, chưa áp dụng vào MASTER LOCK):** "Accountable inspection record fields (performer/reviewer/approver/status/supersession) anchored specifically to sensor-derived Condition_Evidence_ID — as distinct from model-deliverable governance records (e.g., García et al. 2026's CDE publish/hold decision record) — remain absent from the reviewed corpus."

**GAP 2 — Condition Evidence Governance (đặc biệt evidence validity/applicability): GIỮ NGUYÊN.**
Cả A, B, C đều xác nhận **NO** cho Q6 (phạm vi hiệu lực bằng chứng), và đều tự nhầm lẫn tiềm tàng với khái niệm khác (A: IDS `applicability` chỉ lọc loại thực thể; B: blockchain immutability; C: CDE state) — đã được phân biệt tường minh trong từng file ghi chú. Không có bài nào trong A/B/C đe dọa GAP 2/GAP-D. D chưa xác định được nhưng không có dấu hiệu topical đặc biệt hướng vào evidence-validity (title/abstract D tập trung "representation", không nhắc "validity"/"applicability").

**GAP 3 — Multi-hop deterministic integrity validation: THU HẸP (nhẹ).**
García 2026 (bài C) chứng minh một chuỗi 6 loại bản ghi có liên kết tường minh, kiểm chứng được, deterministic (`All Gates Pass` rule, N=22 tệp thật, 14/22 HOLD) — gần với tinh thần GAP 3 nhưng **không phải** chuỗi Sensor→Evidence→Inspection, và **không có** negative-fixture tổng hợp cố ý theo đúng taxonomy Gate 3 (orphan/duplicate/stale/wrong-revision/conflicting/out-of-validity) — chỉ dựa lỗi thực địa tự nhiên. Mariniello 2025 (bài B) cũng góp một phần bằng chứng tương tự (PASS/FAIL rõ ràng + 4 loại negative test) nhưng thiếu neo BIM identity. Do đó GAP 3 vẫn **mở**, nhưng câu tuyên bố phải làm rõ hơn: "chưa từng thực hiện kiểm thử âm tính đa dạng, cố ý, theo đúng taxonomy Gate 3, xuyên suốt một chuỗi cross-system thực sự Sensor→BIM→Evidence→Inspection" — không chỉ đơn thuần "chưa có multi-hop deterministic validation nào".

---

## Kết luận theo từng contribution của Paper 2

**C1 — Verifiable Component-Level Traceability Framework: GIỮ.** Không bài nào trong A–D (kể cả với evidence insufficient của D) chứng minh có framework tích hợp cả ba loại bản ghi `Sensor_ID → BIM_GUID → Condition_Evidence_ID → Inspection_Record_ID` với cross-reference hình thức, neo trên định danh BIM đã xác minh. B thiếu BIM identity; C thiếu hoàn toàn sensor/condition data.

**C2 — Condition-Evidence Governance Contract: GIỮ.** Evidence-validity/applicability (thành phần mở thực sự của C2) không bị đe dọa bởi bất kỳ bài nào (A/B/C đều NO tường minh, D chưa xác định nhưng không có dấu hiệu topical). Tuy nhiên **accountable inspection record** (một thành phần của C2 theo MASTER LOCK §3) phải **THU HẸP câu chữ** theo kết luận GAP 1 ở trên — không đổi cấu trúc C2, chỉ đổi cách diễn đạt sub-claim.

**C3 — Reproducible Deterministic Validation Protocol: GIỮ, làm rõ hơn phạm vi taxonomy.** Không bài nào thực hiện đủ forward+reverse+expected-answer+negative-fixture đa dạng xuyên chuỗi cross-system thật. Cần diễn đạt rõ "cross-system" (Sensor→BIM→Evidence→Inspection) để không bị hiểu nhầm là đã có tiền lệ ở García/Mariniello.

---

## Hướng bài Paper 2 (P2, P2-A…P2-G) — nếu áp dụng

Tài liệu nguồn (`MASTER_EXECUTION_LOCK`) không định nghĩa các hướng P2-A…P2-G cụ thể trong nội dung đã đọc ở phiên này — chỉ có C1/C2/C3 làm 3 contribution chính, không có sub-labeling P2-A…G. **Evidence is currently insufficient** để đánh giá riêng từng hướng P2-A…P2-G theo đúng khuôn GIỮ/ĐỔI ĐỐI THỦ/HẠ ƯU TIÊN/BỎ — không tìm thấy cấu trúc này trong `PAPER2_GATE2_GATE3_MASTER_EXECUTION_LOCK_20260915.md` đã đọc. Nếu người dùng có ý là C1/C2/C3, kết luận đã nêu ở mục trên (GIỮ cả ba, thu hẹp câu chữ một phần của C2/GAP1).

---

## Mức đe dọa tổng thể

| Bài | Mức đe dọa | Sub-claim bị đe dọa | Đối thủ gần nhất |
|---|---|---|---|
| A — Gragnaniello 2024 | LOW | Không có | — |
| B — Mariniello 2025 | MEDIUM | Một phần C3 (deterministic PASS/FAIL + negative testing), không đe dọa C1 (thiếu BIM identity) | SHERPA (blockchain SHM-DT) — đối thủ gần cho khía cạnh "deterministic validation trên chuỗi dữ liệu", không cho identity/traceability BIM |
| C — García 2026 | **HIGH (hẹp)** | GAP 1/C2 (accountable record pattern — phải thu hẹp: chỉ còn novel khi neo trên Condition_Evidence_ID từ sensor); một phần GAP 3 (multi-record traceability, không phải chuỗi Sensor→Evidence→Inspection) | CDE-Centered Quality Gate (García 2026) — đối thủ gần nhất hiện tại cho pattern "accountable governance record + multi-record traceability trong CDE/ISO 19650", cùng nhóm với Borkowski 2026 (đe dọa GAP-B) như hai đối thủ hẹp riêng biệt |
| D — Bellon 2025 | MEDIUM (do trùng chủ đề, chưa xác nhận được nội dung) | Không xác định — cần đọc toàn văn | Tiềm năng là đối thủ gần nhất cho GAP 1 nếu toàn văn xác nhận có accountable inspection schema — **chưa thể kết luận** |

---

## Trạng thái tài liệu sau kiểm tra

**SCOPE-BOUNDED FREEZE có điều kiện (không phải FULL_FREEZE).**

Lý do không thể tuyên bố FULL_FREEZE:
1. Bài D (Bellon 2025) chỉ đọc được ở mức ABSTRACT_ONLY do CAPTCHA chặn truy cập toàn văn hợp pháp tại ScienceDirect trong phiên này — đây là **novelty threat chưa được xác nhận hoặc loại trừ**, không phải threat đã đóng.
2. Bài C (García 2026) đã xác nhận là **HIGH threat hẹp**, đòi hỏi Paper 2 phải cập nhật cách diễn đạt GAP 1/C2 (xem đề xuất câu tuyên bố mới ở trên) trước khi đưa vào bản thảo chính thức — hành động này **chưa được thực hiện** trong phiên này (nằm ngoài phạm vi §22 STOP list của MASTER LOCK, cần supervisor review).

**Điều kiện để chuyển sang FULL_FREEZE:** (a) đọc toàn văn hợp pháp bài D (qua thư viện trường hoặc quyền truy cập khác); (b) supervisor/tác giả duyệt câu tuyên bố GAP 1/C2 đã thu hẹp; hoặc (c) quyết định tường minh rằng D không cần đọc thêm (ví dụ nếu phạm vi Paper 2 được xác nhận không chạm FM/O&M mà García/Bellon nhắm tới).

**Không claim "no study worldwide"/"first study" tuyệt đối** — giữ đúng theo quy tắc MASTER LOCK §4.
