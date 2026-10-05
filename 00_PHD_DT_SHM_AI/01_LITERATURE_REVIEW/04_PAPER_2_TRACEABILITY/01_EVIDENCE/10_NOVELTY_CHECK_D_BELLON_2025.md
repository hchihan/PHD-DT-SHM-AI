# 10-D — Novelty Check: Bellon, Martins, Franco de Carvalho, Feitosa de Souza, Ribeiro & Lenz César Júnior (2025)

**Nhiệm vụ:** Kiểm tra mối đe dọa tính mới có giới hạn cho Paper 2 / Gate 2–3 (16/09/2026).

## Thư mục (OpenAlex, id `W4409166607`)

| Trường | Giá trị |
|---|---|
| Tiêu đề | IFC framework for inspection and maintenance representation in facility management |
| Tác giả đầy đủ | Fernando Gussão Bellon (corresponding); Ana Carolina Pereira Martins; José Maria Franco de Carvalho; Christian Alexandre Feitosa de Souza; José Carlos Lopes Ribeiro; Kléos Magalhães Lenz César Júnior; Diôgo Silva de Oliveira |
| Affiliation (tác giả chính) | Department of Civil Engineering, Federal University of Viçosa (Universidade Federal de Viçosa), Minas Gerais, Brazil |
| Tạp chí | Automation in Construction, tập 174, bài số 106157 |
| DOI | 10.1016/j.autcon.2025.106157 |
| Năm | 2025 |
| Open Access | `is_oa: true`, `oa_status: hybrid`, license CC BY-NC-ND, `oa_url` = trang publisher (ScienceDirect); `any_repository_has_fulltext: false` — không có bản lưu trữ song song (không có PDF trong repository khác) |

**Nguồn đã đọc:** **ABSTRACT_ONLY** qua OpenAlex MCP (metadata + abstract đầy đủ). Đã thử mở toàn văn hợp pháp tại trang publisher (ScienceDirect, DOI resolve) qua trình duyệt built-in — trang chặn bằng CAPTCHA ("Are you a robot?"), không được phép vượt qua theo quy tắc an toàn của phiên làm việc này. Không tìm bản PDF từ nguồn khác (không hợp lệ theo yêu cầu nhiệm vụ — chỉ dùng OpenAlex cho bài D, không mở rộng truy vấn). **Mức bằng chứng: ABSTRACT_ONLY.**

---

## Q1–Q12

**Q1 — Vấn đề nghiên cứu:** **PARTIAL** (chỉ từ abstract). "Effectively managing inspection and maintenance data in facility management remains challenging due to the lack of structured and interoperable data representation." Giải pháp: framework dựa trên schema IFC để chuẩn hóa biểu diễn dữ liệu inspection, damage, maintenance, và maintenance cost. *Trích dẫn: Abstract (OpenAlex).*

**Q2 — Chuỗi thông tin:** **EVIDENCE_INSUFFICIENT.** Abstract không mô tả đủ chi tiết luồng nguồn dữ liệu→cơ chế→cấu kiện BIM→hồ sơ→đầu ra ở mức có thể gán nhãn tin cậy. Chỉ biết: framework IFC-based, được xác thực qua "IFC schema verification and semantic evaluation of generated case studies across multiple BIM software", áp dụng cho buildings/industrial plants/infrastructure. *Trích dẫn: Abstract (OpenAlex).*

**Q3 — Định danh cấu kiện:** **EVIDENCE_INSUFFICIENT.** Abstract không đề cập rõ cơ chế định danh (GlobalId hay mã khác), không nêu có xác minh với IFC xuất ra thật hay không.

**Q4 — Quản lý phiên bản mô hình:** **EVIDENCE_INSUFFICIENT.** Không có thông tin trong abstract.

**Q5 — Provenance:** **EVIDENCE_INSUFFICIENT.** Không có thông tin trong abstract về phân biệt trường nguồn/đo lường/xử lý/con người.

**Q6 — Phạm vi hiệu lực bằng chứng:** **EVIDENCE_INSUFFICIENT.** Không có thông tin trong abstract.

**Q7 — Accountability hồ sơ kiểm tra:** **EVIDENCE_INSUFFICIENT.** Không có thông tin trong abstract về performer/reviewer/approver/status/supersession.

**Q8 — Truy vết xuôi/ngược:** **EVIDENCE_INSUFFICIENT.** Không có thông tin trong abstract.

**Q9 — Kiểm chứng:** **PARTIAL** (chỉ từ abstract). "The framework was validated through IFC schema verification and semantic evaluation of generated case studies across multiple BIM software" — có xác nhận việc có validation nhưng **không rõ** phương pháp cụ thể, không rõ có competency questions/expected-answer/PASS-FAIL định lượng hay mẫu số (sample size) là bao nhiêu. *Trích dẫn: Abstract (OpenAlex).*

**Q10 — Kiểm thử âm tính cố ý:** **EVIDENCE_INSUFFICIENT.** Không có thông tin trong abstract.

**Q11 — Đã xác lập (chỉ suy ra từ abstract, mức tin cậy thấp):** Framework dựa trên schema IFC để chuẩn hóa biểu diễn dữ liệu inspection/damage/maintenance/maintenance-cost trong facility management; đã thử nghiệm qua nhiều phần mềm BIM; tác giả tự nhận "Future work should focus on extending its application in real-world scenarios, specifically through integration with facility management systems and automated data acquisition technologies" — cho thấy **chính tác giả xác nhận framework CHƯA tích hợp với hệ thống FM thực và CHƯA có automated data acquisition** (tức chưa có sensor/condition-evidence integration) tại thời điểm công bố. *Trích dẫn: Abstract (OpenAlex).*

**Q12 — Không làm (so C1/C2/C3), chỉ suy ra từ abstract:** **EVIDENCE_INSUFFICIENT** cho đánh giá chi tiết, nhưng chính abstract tự nhận **chưa** tích hợp automated data acquisition (tức chưa nối với Sensor_ID/Condition_Evidence_ID) — đây là dấu hiệu gián tiếp cho thấy C1 (chuỗi Sensor→Evidence→Inspection tích hợp) **khó bị đe dọa trực tiếp bởi chính bản thân bài D**, nhưng **không thể loại trừ** khả năng bài D có accountable inspection-record schema mạnh (gần đúng GAP 1) — cần đọc toàn văn để xác nhận/loại trừ.

---

## Mức đe dọa: **MEDIUM — do trùng lặp chủ đề mạnh (title/abstract) nhưng KHÔNG THỂ xác nhận chi tiết vì chỉ có abstract**

**Lý do:**
- Tiêu đề "IFC framework for **inspection and maintenance representation** in facility management" trùng khớp trực tiếp về **chủ đề** với GAP 1 (Accountable BIM-linked Inspection Record) của Paper 2 — đây là bài **duy nhất trong 4 bài có tên gọi chạm thẳng vào "inspection representation trong IFC"**, mức độ trùng chủ đề cao hơn cả A/B/C.
- Tuy nhiên, **không có bằng chứng full-text** để xác nhận bài D có: accountable fields (performer/reviewer/approver/status/supersession), evidence validity/applicability, multi-hop traceability, hay negative-fixture testing theo đúng taxonomy Gate 3. Mọi câu Q3–Q8, Q10 đều **EVIDENCE_INSUFFICIENT**.
- Điểm giảm nhẹ đe dọa: chính tác giả tự nhận trong abstract rằng framework **chưa tích hợp với FM systems thực và automated data acquisition** — gợi ý bài D có thể **không** có chuỗi Sensor_ID→Condition_Evidence_ID hoàn chỉnh, nhưng đây chỉ là suy luận gián tiếp từ "Future work", không phải xác nhận trực tiếp.
- **Không nâng lên HIGH/VERY_HIGH** vì thiếu bằng chứng cụ thể — theo đúng quy tắc "không suy diễn", giữ nguyên MEDIUM dựa trên độ trùng chủ đề, không phải dựa trên nội dung đã xác nhận.
- **Hành động bắt buộc tiếp theo:** đọc toàn văn bài D trước khi Paper 2 submission (Zotero/thư viện trường, hoặc quyền truy cập hợp pháp khác) — đây là rủi ro chưa đóng, không được coi là literature freeze đầy đủ cho tới khi giải quyết.

## Claim → Evidence → Limitation → Implication

| Claim | Evidence | Limitation | Implication |
|---|---|---|---|
| Bellon 2025 có nguy cơ đe dọa GAP 1 do trùng chủ đề "inspection representation in IFC" mạnh nhất trong 4 bài, nhưng mức đe dọa thực tế **không xác định được** vì chỉ có abstract | OpenAlex metadata + abstract (W4409166607); ScienceDirect chặn CAPTCHA khi thử truy cập toàn văn hợp pháp | Không đọc được toàn văn trong phiên này; mọi câu Q3, Q4, Q5, Q6, Q7, Q8, Q10 đều EVIDENCE_INSUFFICIENT — đây là giới hạn nghiêm trọng nhất trong 4 bài kiểm tra | **Bắt buộc**: đưa bài D vào hàng ưu tiên đọc toàn văn tiếp theo (qua thư viện trường/Zotero nếu có quyền truy cập hợp pháp) trước khi khóa (freeze) cuối cùng cho Paper 2 submission; cho tới lúc đó, GAP 1 chỉ được coi là "GIỮ NGUYÊN có điều kiện", không phải "GIỮ NGUYÊN tuyệt đối" |
