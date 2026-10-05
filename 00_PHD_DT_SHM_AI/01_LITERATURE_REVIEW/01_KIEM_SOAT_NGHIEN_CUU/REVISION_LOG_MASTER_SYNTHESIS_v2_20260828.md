# REVISION LOG — MASTER_LITERATURE_AND_EVIDENCE_SYNTHESIS_v2_20260828.md

**Ngày:** 28/08/2026 (vòng revision có mục tiêu, 6 nhiệm vụ)
**File gốc không bị ghi đè:** `MASTER_LITERATURE_AND_EVIDENCE_SYNTHESIS_20260828.md` (v1) — giữ nguyên, không sửa/xoá/di chuyển.
**File mới:** `MASTER_LITERATURE_AND_EVIDENCE_SYNTHESIS_v2_20260828.md`.

## Nguồn đối chiếu cho vòng revision này (đọc toàn văn trực tiếp)

- `00_README_START_HERE.md`
- `MASTER_RESEARCH_CHARTER.md`
- `MASTER_RESEARCH_CHARTER_v1.1_LIMITED_FEM_20260717.md`
- `RESEARCH_DIRECTION_AND_SCOPE.md` (v2.3)
- `RESEARCH_ARCHITECTURE.md` (v2.3)
- `CURRENT_STATUS_AND_NEXT_DIRECTION.md` (v2.3)
- `RESEARCH_ARCHITECTURE_DECISION_RECORD_20260717.md` (ADR-2026-001)
- `THE_COUNCIL_REVIEW_FEM_OR_NO_FEM_17.07.2026.md`

---

## 1. Khôi phục nguyên văn RQ đã khóa (v2 §1.2)

**Sửa:** RQ1–RQ3 thay bằng đúng nguyên văn tiếng Anh Charter v1.1 §7. Bốn ý mở rộng mà v1 từng chèn vào câu RQ được tách và gắn đúng vị trí:
- Claim sensor-config (v1 gắn vào RQ1) → candidate hypothesis của Paper 1B.
- CEI/justification-accountability (v1 gắn vào RQ2) → analytical objective bổ sung cho RQ2 (điều chỉnh v2.1.2 đã phê duyệt), không phải văn bản RQ.
- Cụm "dữ liệu hư hỏng hiện trường hạn chế" (v1 gắn nhầm vào RQ2) → xóa; đây là một phần của RQ3, lỗi chép nhầm.
- Khung "khung có thể triển khai tới mức nào (Rapexco)" (v1 thay cho khung câu RQ3 gốc) → design/validation objective, tương ứng Validation Ladder V3.

**Lý do:** v1 đã diễn giải/mở rộng RQ thay vì trích nguyên văn — vi phạm chính nguyên tắc "RQ khóa — không tạo thêm" mà v1 tự tuyên bố tuân thủ.

**Nguồn áp dụng:** `MASTER_RESEARCH_CHARTER_v1.1_LIMITED_FEM_20260717.md` §7 (source-of-truth level 2).

**Claim bị hạ cấp:** RQ1/RQ2/RQ3 "mở rộng" trong v1 hạ xuống candidate hypothesis / analytical objective / design objective — không còn là văn bản RQ.

**Vấn đề còn cần quyết định:** không có — đây là sửa lỗi trích dẫn, không phải quyết định học thuật mới.

---

## 2. Khóa một định nghĩa CEI duy nhất (v2 §2.3)

**Sửa:** Bỏ định nghĩa "Condition Evidence Information profile" (nguồn: `CEI_SCIENTIFIC_BASIS_AND_THESIS_SPECIFICATION_v1.1_20260812.md`, level 6, working spec Paper-1-specific chưa phê duyệt) khỏi vị trí định nghĩa chính. Thay bằng định nghĩa khóa: "CEI là confidence/evidence indicator đi kèm condition evidence, thể hiện mức độ tin cậy/qualification trong phạm vi đã kiểm chứng." Giữ lại bảy nguyên tắc khoa học (bảng) làm cơ sở hỗ trợ construct, không còn gắn với nhãn "profile". Không tạo công thức tính CEI.

**Lý do:** v1 để một tài liệu Paper-1-specific (level 6) ghi đè định nghĩa của Charter v1.1 (level 2) và bộ v2.3 hiện hành (level 3/7, cùng khóa lại định nghĩa gốc) — vi phạm thứ bậc nguồn quy định tại `SOURCE_OF_TRUTH_HIERARCHY_v2.1.md`.

**Nguồn áp dụng:** Charter v1.1 §13/§14; `RESEARCH_ARCHITECTURE.md` Lớp 2; `CURRENT_STATUS_AND_NEXT_DIRECTION.md` §2.

**Claim bị hạ cấp:** "CEI = Condition Evidence Information profile" hạ xuống ghi chú lịch sử (đã dùng sai ở v1), không còn là định nghĩa chính thức; chỉ còn dùng để tham chiếu cơ sở khoa học phụ trợ, có gắn cảnh báo tại §2.3 và dòng C18 của bảng locator (§8).

**Vấn đề còn cần quyết định:** phương pháp vận hành hóa (operational validation) CEI vẫn chưa có — cần thầy hướng dẫn phê duyệt trước khi bất kỳ công thức hoặc thang đo nào được đề xuất.

---

## 3. Tách Paper 1A/1B (v2 §4.3–4.5)

**Sửa:** Paper 1 tách nội bộ thành Paper 1A (Core Scope: dataset integrity, run registry, leakage-safe run-aware/LORO, condition-evidence qualification, provenance, cross-campaign transportability, validated scope — mang trách nhiệm Gate 1 duy nhất) và Paper 1B (Supporting Scope: sensor count/composition, sensor subsets, performance retention, marginal benefit, held-out-run robustness, consistency giữa campaign — không RQ/WP/Gate riêng). Thêm bảng phân định Topic/claim → 1A → 1B → Shared evidence → Prohibited overlap (7 dòng) và danh sách 3 điểm rủi ro overlap/self-plagiarism cao nhất kèm cách xử lý.

**Lý do:** claim "sensor configuration dominates architecture" đang xung đột (M-02, §2.4) không nên tiếp tục nằm trong cùng phạm vi trách nhiệm đóng Gate 1 như dataset integrity/leakage-safe evaluation — gộp chung tạo rủi ro Gate 1 bị trì hoãn bởi một claim chưa phân xử. Tách rõ cũng giảm rủi ro overlap/self-plagiarism giữa nội dung "giao thức" và nội dung "so sánh cấu hình".

**Nguồn áp dụng:** Charter v1.1 §10 (Paper portfolio gốc — một Paper 1 duy nhất), §13 (Allowed claim sensor-config). Việc tách 1A/1B là **cấu trúc nội bộ do file tổng hợp này đề xuất** để tổ chức nội dung, không tạo Paper/WP/Gate mới trong hệ thống quản trị.

**Claim bị hạ cấp:** không có claim mới bị hạ cấp; claim sensor-config giữ nguyên trạng thái `CANDIDATE — ĐANG XUNG ĐỘT`, nay được cô lập rõ khỏi phạm vi trách nhiệm Gate 1.

**Vấn đề còn cần quyết định:** (a) liệu cấu trúc 1A/1B có được áp dụng chính thức cho chiến lược nộp bài Paper 1 thật hay chỉ dùng nội bộ trong tài liệu tổng hợp — cần thầy hướng dẫn xác nhận; (b) Paper 1A và 1B nộp cùng thời điểm/cùng tạp chí hay tách biệt — chưa quyết định, ngoài phạm vi revision này.

---

## 4. Thu gọn research gap Gate 1 (v2 §3.1)

**Sửa:** Bỏ khung "chín thành phần đồng thời" (dễ bị đọc như liệt kê novelty rời rạc). Thay bằng phát biểu gap khái niệm ba trục: (1) đơn vị độc lập vật lý; (2) rò rỉ dữ liệu; (3) phạm vi chuyển giao run/session/campaign. Ghi rõ multi-seed/permutation test/uncertainty/run registry là **cơ chế kiểm chứng gap**, không phải novelty riêng. Thêm bảng phân loại SUPPORTED / PARTIALLY SUPPORTED / Evidence is currently insufficient thay cho khung "No study has…".

**Lý do:** khung "chín thành phần" có rủi ro bị phản biện chẻ nhỏ từng thành phần để bác bỏ toàn bộ gap; khung ba trục khái niệm rõ ràng, bảo vệ được hơn, và đúng tinh thần "không suy diễn hệ thống khi chưa có bằng chứng hệ thống".

**Nguồn áp dụng:** `GATE1_BATCH_B_DEEP_READ_20260827.md` §7/§9.5 (giữ nguyên nội dung nền, chỉ đổi cách trình bày); nguyên tắc "không suy diễn" theo yêu cầu revision.

**Claim bị hạ cấp:** không có nhận định mới bị hạ cấp; nhận định "chưa ai áp dụng deep learning cho khung thép bắt bu lông" tiếp tục ở trạng thái `BLOCKED` (đã đúng từ v1).

**Vấn đề còn cần quyết định:** không có.

---

## 5. Sửa diễn giải LOCO và tách cấp đóng góp (v2 §2.2)

**Sửa:** Thay câu "LOCO thấp... là đóng góp quản lý thông tin" (v1) bằng khung bốn cấp tách bạch: (1) empirical evidence — transportability giữa campaign còn hạn chế; (2) interpretation — prediction không nên dùng ngoài phạm vi campaign đã kiểm chứng; (3) implication for information management — condition evidence cần mang provenance/validated scope; (4) potential management contribution — có điều kiện, chưa xác nhận, chỉ hình thành sau khi Gate 2–3 kiểm chứng.

**Lý do:** câu gốc ở v1 biến một kết quả âm/hạn chế thành tuyên bố thành công bằng diễn giải hậu nghiệm — vi phạm nguyên tắc không suy diễn, có rủi ro bị phản biện xem là ngụy biện (post-hoc rationalization).

**Nguồn áp dụng:** Ramasso et al. (SECONDARY LOCATOR, §8 dòng C10 của v2) cho hiện tượng LORO cao/LOCO thấp nói chung; nguyên tắc bốn lớp bằng chứng không mượn chéo (`RESEARCH_ARCHITECTURE.md`).

**Claim bị hạ cấp:** "LOCO thấp = đóng góp quản lý thông tin" (khẳng định, v1) hạ xuống "potential management contribution — có điều kiện, chưa xác nhận, chỉ hình thành sau Gate 2–3" (v2).

**Vấn đề còn cần quyết định:** không có.

---

## 6. Bảng claim-to-source locator (v2 §8, mới)

**Thêm:** bảng 18 dòng (Claim_ID C01–C18) theo cấu trúc `Claim_ID | Exact claim | Claim type | Source file/paper | Page/section/table/figure or artefact path | Verification status | Allowed use | Limitation`, phân biệt `SOURCE EVIDENCE` / `SYNTHESIS/INTERPRETATION` / `THESIS APPLICATION`, và `VERIFIED AT SOURCE` / `SECONDARY LOCATOR — ORIGINAL SOURCE NOT YET VERIFIED` / `NOT VERIFIED`.

**Lý do:** yêu cầu truy xuất minh bạch ở cấp từng claim cốt lõi (không chỉ cấp nguồn như bảng §6 của v1), đặc biệt cho các claim liên quan bản thảo 24/08 chưa xác minh trực tiếp (C11, C12) và cho chính lỗi định nghĩa CEI đã sửa (C18).

**Nguồn áp dụng:** toàn bộ nguồn đã trích dẫn trong tài liệu; không tạo locator giả cho bất kỳ dòng nào.

**Claim bị hạ cấp:** không có claim mới; bảng làm rõ trạng thái verification vốn đã ghi rải rác trong v1 (ví dụ C11/C12 tương ứng nội dung §0.2 và §2.4 của v1, nay có locator tường minh).

**Vấn đề còn cần quyết định:** cần xác minh trực tiếp PDF gốc cho toàn bộ dòng `SECONDARY LOCATOR` (C08, C09, C10, C13, C14, C16, C18) trước khi dùng làm căn cứ trích dẫn học thuật chính thức trong bản thảo nộp tạp chí.

---

## Tổng kết trạng thái sáu nhiệm vụ

| # | Nhiệm vụ | Kết quả |
|---|---|---|
| 1 | Khôi phục nguyên văn RQ đã khóa | PASS |
| 2 | Khóa một định nghĩa CEI duy nhất | PASS |
| 3 | Tách Paper 1A/1B + bảng phân định | PASS |
| 4 | Thu gọn research gap Gate 1 | PASS |
| 5 | Sửa diễn giải LOCO và tách cấp đóng góp | PASS |
| 6 | Bổ sung claim-to-source locator | PASS |

Chi tiết đầy đủ và bảng tự kiểm tra mở rộng: xem `MASTER_LITERATURE_AND_EVIDENCE_SYNTHESIS_v2_20260828.md` §10.

## Vấn đề tổng hợp còn cần NCS/thầy hướng dẫn quyết định (không thuộc phạm vi tự quyết của phiên này)

1. Vị trí vật lý của `00_CURRENT_SOURCE_OF_TRUTH` và quyền đọc trực tiếp bản thảo Paper 1 24/08/2026 — vẫn treo từ v1.
2. Phân xử xung đột M-02 (claim "sensor configuration dominates architecture") — vẫn treo từ v1, nay cô lập rõ trong phạm vi Paper 1B.
3. Phê duyệt phương pháp operational validation cho CEI trước khi vận hành hóa (mục 2 ở trên).
4. Xác nhận có áp dụng chính thức cấu trúc Paper 1A/1B cho chiến lược nộp bài thật hay không (mục 3 ở trên).
