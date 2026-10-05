# 10-B — Novelty Check: Mariniello, Gragnaniello & Asprone (2025)

**Nhiệm vụ:** Kiểm tra mối đe dọa tính mới có giới hạn cho Paper 2 / Gate 2–3 (16/09/2026).

## Thư mục

| Trường | Giá trị |
|---|---|
| Tiêu đề | Enhancing structural health monitoring data management and damage detection in digital twins with blockchain and smart contracts |
| Tác giả | Giulio Mariniello, Chiara Gragnaniello, Domenico Asprone |
| Tạp chí | Automation in Construction, 180 (2025) 106558 |
| DOI | 10.1016/j.autcon.2025.106558 |
| Năm | 2025 |
| Xác nhận nguồn | Khớp chính xác tiêu đề/tác giả/DOI/tạp chí do NotebookLM trích xuất trực tiếp từ header/footer PDF (`1-s2.0-S0926580525005989-main.pdf`). Không mâu thuẫn. |

**Nguồn đã đọc:** Toàn văn qua NotebookLM MCP. **Mức bằng chứng: FULL_TEXT.**

---

## Q1–Q12

**Q1 — Vấn đề nghiên cứu:** **YES.** Khắc phục hạn chế quản lý dữ liệu SHM/Digital Twin tập trung (nguy cơ giả mạo, single point of failure, thiếu minh bạch) và thiếu cơ chế phi tập trung kiểm tra chất lượng dữ liệu đầu vào + xác thực thuật toán. Đề xuất framework **SHERPA** dùng blockchain/smart contract. *Trích dẫn: Section 1; Section 2.2.*

**Q2 — Chuỗi thông tin:** **YES.** Sensor/DAQ → `SDL.csv`/`SPL.csv` trên IPFS (off-chain, CID) → **Data Quality Contract (DQC)** kiểm tra hợp lệ → Digital Twin/Digital Shadow (OMA, tần số riêng ω1) → **Damage Detection Contract (DDC)** xác thực thuật toán qua CID + Shewhart control chart → **Data Reaction Contract (DRC)** tạo `Alert` (Severity 1/2/3) → giải quyết bởi `AUTHORITY_ROLE` (`resolveAlert`, `closureNote`). *Trích dẫn: Section 3.2.1–3.2.3; Section 4.1–4.3; Phụ lục A.1–A.3.*

**Q3 — Định danh cấu kiện:** **EVIDENCE_INSUFFICIENT.** Digital Twin tham chiếu mô hình 3D/BIM cầu Canalone Viaduct (Fig. 7) nhưng schema dữ liệu (`SDL.csv`, `SPL.csv`) và smart contract **không** báo cáo tường minh việc dùng IFC GlobalId hay mã cấu kiện cụ thể để liên kết bản ghi với từng cấu kiện BIM; liên hệ BIM chỉ ở mức tham chiếu/hiển thị. *Trích dẫn: Section 4/4.1; Phụ lục A.1–A.3.*

**Q4 — Quản lý phiên bản mô hình:** **PARTIAL.** Có quản lý phiên bản **thuật toán/mô hình phân tích** (CID trên IPFS, đối chiếu với "previously validated version" trong DDC, cho phép re-validation khi cập nhật tham số). **Không có** quản lý phiên bản mô hình hình học/BIM. *Trích dẫn: Section 3.2.2; Phụ lục A.2 (Algorithm 2).*

**Q5 — Provenance:** **PARTIAL.** Nguồn (CÓ — đăng ký sensor/DAQ ID qua `ADMIN`); đo lường (CÓ — `Timestamp`, `Acc1..n`, `Sampling frequency`, `NOut`, nhiệt độ/điện áp trong `SDL/SPL.csv`); xử lý (CÓ — CID thuật toán, `isST_Anomaly`, `damageSeverity`, `expectedValue`); con người (CÓ MỘT PHẦN — chỉ `closedBy = msg.sender` ở bước giải quyết alert; **không có** trường người cho bước thu thập/xử lý thô, vốn tự động hóa). *Trích dẫn: Section 3.2.1; Section 4.1; Bảng 3; Phụ lục A.1–A.3.*

**Q6 — Phạm vi hiệu lực bằng chứng:** **NO.** Không có `valid_from/valid_to`, không có điều kiện tái sử dụng, không có supersession độc lập. Framework chỉ dựa vào **blockchain immutability** (hash cryptographic) — đã phân biệt tường minh: immutability KHÔNG PHẢI evidence validity/applicability. *Trích dẫn: Section 3.2.1; Phụ lục A.1.*

**Q7 — Accountability:** **PARTIAL.** Status CÓ (`isActive` trong `Alert`; `valid` trong DQC; `isST_Anomaly` trong DDC). Performer/approver CÓ MỘT PHẦN (`closedBy` = địa chỉ ví, `AUTHORITY_ROLE`). Reviewer: **KHÔNG CÓ**. Supersession: **KHÔNG CÓ**. *Trích dẫn: Phụ lục A.1–A.3 (Algorithm 1–3).*

**Q8 — Truy vết xuôi/ngược:** **PARTIAL.** Có luồng dữ liệu xuôi qua 4 loại bản ghi (`SDL.csv`, `SPL.csv`, `analysisResults` DDC, `alerts` DRC), tác giả tự nhận "traceability/auditability" nhưng **không có bài kiểm thử hình thức chuyên biệt** chứng minh truy vết ngược từ 1 Alert ID cụ thể quay về đúng Sensor_ID/cấu kiện qua nhiều nấc. *Trích dẫn: Section 3.2; Phụ lục A.1–A.3.*

**Q9 — Kiểm chứng:** **PARTIAL.** Không có competency questions. Có expected-answer/PASS-FAIL rõ ràng: `addSimulatedData` (DDC) so khớp `expectedValue`; `analyzeData` (DQC) so ngưỡng nhiệt độ/`NOut`. Mẫu số: 6 gia tốc kế 3 trục + 3 cảm biến nhiệt độ (thực địa cầu Canalone); 3 kịch bản mô phỏng; 50 lần lặp trên 10 cảm biến; kiểm thử mở rộng 50–200 cảm biến. *Trích dẫn: Section 3.2.2; Section 4.2.1, 4.4; Phụ lục A.1–A.2.*

**Q10 — Kiểm thử âm tính cố ý:** **PARTIAL.** CÓ: dữ liệu cảm biến bị lỗi/nhiễu cố ý chèn (Scenario 3); ghi trùng dữ liệu (`verifyData` kiểm tra hash đã tồn tại); thuật toán cho kết quả sai lệch so kỳ vọng (`addSimulatedData`); thao tác trái phép (`resolveAlert` không có `AUTHORITY_ROLE`). **KHÔNG CÓ**: orphan record, duplicate component ID, wrong component/binding, stale data, wrong BIM model version, missing target, out-of-validity. *Trích dẫn: Section 4.2.1; Phụ lục A.1–A.3.*

**Q11 — Đã xác lập:** Kiến trúc 3 smart contract (DQC/DDC/DRC); lưu trữ hỗn hợp off-chain (IPFS)/on-chain (CID+metadata) tối ưu chi phí gas; thử nghiệm thực trên cầu Canalone Viaduct + Ethereum testnet; đo lường chi phí gas ($2.76–$2.95 deploy, $0.17–$0.37 giao dịch) và thời gian phản hồi ổn định (~172–197 ms) khi mở rộng 50–200 cảm biến. *Trích dẫn: Abstract; Section 1; Section 3.2; Section 4–4.4; Section 5.*

**Q12 — Không làm (so C1/C2/C3):** **NO** cho cả ba. Không có framework tích hợp chính thức Sensor_ID/Condition_Evidence_ID/Inspection_Record_ID neo trên BIM_GUID (C1) — 4 loại bản ghi của SHERPA không neo trên định danh BIM đã xác minh. Không có evidence-validity/applicability rule tường minh, chỉ dựa blockchain immutability (C2). Không có deterministic multi-hop protocol xuyên chuỗi với forward+reverse+expected-answer+negative-fixture đầy đủ — mỗi smart contract kiểm tra độc lập theo từng bước (C3).

---

## Mức đe dọa: **MEDIUM**

**Lý do:** Bài B là đe dọa **rõ hơn bài A** vì: (i) có accountability một phần (status + performer `closedBy`, dù thiếu reviewer/supersession); (ii) có deterministic PASS/FAIL với expected-answer và một tập kiểm thử âm tính đa dạng hơn (duplicate-hash check, unauthorized-access test, algorithm-mismatch test) — gần chạm tới tinh thần GAP 3 (multi-hop deterministic validation). Tuy nhiên bài B **không đe dọa C1** vì hoàn toàn thiếu định danh BIM/IFC đã xác minh (Q3 = EVIDENCE_INSUFFICIENT) — 4 loại bản ghi của SHERPA không neo trên `BIM_GUID` governed identity, khác cấu trúc lõi của Paper 2. Bài B cũng minh chứng cụ thể một lỗi khái niệm cần Paper 2 tránh: nhầm blockchain immutability với evidence validity/applicability — Paper 2 phải giữ phân biệt tường minh này (đã làm đúng theo MASTER LOCK §2.2 GAP 2). Không đủ mạnh để đạt HIGH vì thiếu hoàn toàn liên kết BIM identity và thiếu đa số trường accountability (reviewer, supersession).

## Claim → Evidence → Limitation → Implication

| Claim | Evidence | Limitation | Implication |
|---|---|---|---|
| Bài B đe dọa một phần sub-claim "deterministic multi-hop validation" (hướng tới C3) nhưng không đe dọa C1 (thiếu BIM identity) | Q8–Q10: PASS/FAIL rõ ràng, 4 loại negative test, nhưng Q3 = EVIDENCE_INSUFFICIENT (không có BIM/IFC identity xác minh) | Đọc qua NotebookLM, không tự đọc mã Solidity gốc; số liệu trích dẫn theo Section/Phụ lục do AI tổng hợp, chưa đối chiếu dòng-mã trực tiếp | Paper 2 nên nhấn mạnh: (a) validation phải neo trên BIM_GUID đã xác minh — điều SHERPA không có; (b) evidence validity/applicability phải tách bạch tường minh khỏi "immutability"/"integrity", không chỉ dựa cryptographic hash |
