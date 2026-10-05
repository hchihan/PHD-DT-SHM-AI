# MASTER LITERATURE AND EVIDENCE SYNTHESIS — v2

**Ngày lập bản v1:** 28/08/2026 | **Ngày revision v2 (có mục tiêu, 6 nhiệm vụ):** 28/08/2026
**Quan hệ với v1:** File này **không ghi đè** `MASTER_LITERATURE_AND_EVIDENCE_SYNTHESIS_20260828.md` (v1) — v1 giữ nguyên, không bị sửa/xóa. Chi tiết từng thay đổi, lý do, nguồn áp dụng và claim bị hạ cấp: xem `REVISION_LOG_MASTER_SYNTHESIS_v2_20260828.md`.
**Luận án:** Data-informed Digital Twin Framework for Condition Monitoring and Inspection–Maintenance Support of Coastal Industrial Steel Buildings — kiến trúc **Limited-FEM** (Verdict B, Council 17/07/2026, hai thầy hướng dẫn phê duyệt)
**Vai trò file này:** Tổng hợp một lần, không tạo thẩm quyền mới, không tạo RQ/WP/Paper/Gate mới, không mở rộng phạm vi. Toàn bộ nội dung được truy ngược về file nguồn trong `01_LITERATURE_REVIEW/`. File nguồn không bị sửa, xoá hay di chuyển.
**Không có Gate nào PASS.** Mọi con số/kết luận định lượng của Paper 1A/1B là **candidate claim pending Gate 1 closure**, trừ khi ghi chú khác.

---

## 0. Phạm vi truy cập, giới hạn phiên làm việc và nguyên tắc dựng file

### 0.1 Phạm vi đã đọc (v1, không đổi ở v2)

File này tổng hợp toàn bộ nội dung đọc sâu trong thư mục `01_LITERATURE_REVIEW` (159 file, gồm `01_CORE_SOURCE_OF_TRUTH`, `02_EVIDENCE`, `03_PAPER_1`, `04_PAPER_2`, `05_PAPER_3`) và các file lịch sử bắt buộc phải đối chiếu tại gốc dự án (`08-RESEARCH_ARCHITECTURE_DECISION_RECORD_20260717.md`, `MASTER_RESEARCH_CHARTER_v1.1_LIMITED_FEM_20260717.md`, `THE_COUNCIL_REVIEW_FEM_OR_NO_FEM_17.07.2026.md` — hiện lưu tại `90_ARCHIVE/` nhưng vẫn là **thẩm quyền cao nhất** theo `SOURCE_OF_TRUTH_HIERARCHY_v2.1.md`). Các PDF nguồn (~30 bài) không được đọc lại trực tiếp; nội dung của chúng được lấy từ các bản deep-read đã có locator cấp trang — đây là nguồn `SOURCE EVIDENCE` cấp hai, không phải suy diễn.

### 0.2 Vấn đề truy cập nghiêm trọng — bản thảo Paper 1 24/08/2026 (v1, không đổi ở v2)

Thư mục `01_CORE_SOURCE_OF_TRUTH/_NEW_DOCS/` (28/08/2026) mô tả chi tiết một workspace tái tổ chức `00_CURRENT_SOURCE_OF_TRUTH` chứa `PAPER1_BUILDINGS_VIETNAMESE_DRAFT_v0.2.md` (sửa lần cuối 24/08/2026 09:41) — báo cáo 510 lần chạy (17 cấu hình × 30 hoán vị LORO), macro-F1 trong-campaign CP2_21 tới 0,955 (ResNet1D), liên-campaign rơi còn 0,147, và chênh lệch pipeline (0,34–0,48) >> chênh lệch cấu hình cảm biến (0,070–0,166, CP3 không tách được khỏi nhiễu). File này **không truy cập được** trong phiên tạo v1 dù đã Glob nhiều lần trên toàn bộ gốc dự án. Toàn bộ con số trên được trích dẫn ở v2 dưới nhãn **"reported, chưa xác minh trực tiếp"** (xem bảng locator §8, dòng C11–C12) — không được nâng thành `SOURCE EVIDENCE` cấp một. Xem thêm chi tiết đầy đủ trong v1 §0.2 (không lặp lại toàn văn ở đây để tránh trùng lặp).

**Next action bắt buộc cho NCS (không đổi từ v1):** xác nhận vị trí vật lý `00_CURRENT_SOURCE_OF_TRUTH` và cấp quyền đọc trực tiếp bản thảo 24/08 trước khi các con số trên được dùng chính thức trong Paper 1A/1B.

### 0.3 Thứ bậc nguồn áp dụng (v1, không đổi, bổ sung 8 file đọc mới cho vòng revision này)

```text
1. Quyết định Hội đồng 17/07/2026 (Verdict B) — THE_COUNCIL_REVIEW_FEM_OR_NO_FEM_17.07.2026.md
2. MASTER_RESEARCH_CHARTER_v1.1_LIMITED_FEM_20260717.md + ADR-2026-001 (RESEARCH_ARCHITECTURE_DECISION_RECORD_20260717.md)
   — CẢ HAI ĐỌC TOÀN VĂN LẦN NỮA TRONG VÒNG REVISION NÀY (28/08/2026)
3. Bộ v2.3 hiện hành trong 01_CORE_SOURCE_OF_TRUTH (tự khai subordinate với mục 1–2):
   SOURCE_OF_TRUTH_HIERARCHY_v2.1.md · MASTER_RESEARCH_CHARTER_CURRENT_20260812.md (v2.1.2) ·
   RQ_WP_CHAPTER_PAPER_GATE_MATRIX_v2.1.md (v2.3) · EVIDENCE_GATES_v2.1.md (v2.3) ·
   TERMINOLOGY_CONTROL_CURRENT.md (v2.3) · AGENT_RULES.md (v2.3) ·
   RESEARCH_DIRECTION_AND_SCOPE.md (v2.3) · RESEARCH_ARCHITECTURE.md (v2.3) · CURRENT_STATUS_AND_NEXT_DIRECTION.md (v2.3)
   — BA FILE CUỐI ĐỌC TOÀN VĂN LẦN NỮA TRONG VÒNG REVISION NÀY
4. CURRENT_DIRECTION_LOCK_20260804.md
5. Evidence hiện có theo Gate: LIVING_EVIDENCE_BASE_CURRENT_20260812.md, ba deep-read 27/08, ROUND4_VERIFIED_EVIDENCE_RECORD_v1.1
6. Tài liệu Paper-specific, roadmap, đặc tả kỹ thuật (working spec, chưa phê duyệt) — bao gồm
   CEI_SCIENTIFIC_BASIS_AND_THESIS_SPECIFICATION_v1.1_20260812.md (nguồn của lỗi định nghĩa CEI ở v1, xem §2.3)
7. 01_CORE_SOURCE_OF_TRUTH/CURRENT_LIMITED_FEM_BY_GATE_20260809/ (snapshot 09/08, lịch sử)
8. _NEW_DOCS/ (28/08) — con trỏ cho trạng thái không truy cập được; dùng để cảnh báo, không dùng làm evidence số liệu
9. 00_README_START_HERE.md và MASTER_RESEARCH_CHARTER.md (bản tóm tắt điều hướng 17/07/2026, đọc toàn văn lần này) —
   dùng để xác nhận thứ tự đọc và không mâu thuẫn với mục 1–3; MASTER_RESEARCH_CHARTER.md là bản tóm tắt 12 mục
   của chính Charter v1.1, không phải nguồn độc lập.
```

**Ghi chú vòng revision (28/08/2026):** tám file được người dùng chỉ định đọc lại toàn văn: `00_README_START_HERE.md`, `MASTER_RESEARCH_CHARTER.md`, `MASTER_RESEARCH_CHARTER_v1.1_LIMITED_FEM_20260717.md`, `RESEARCH_DIRECTION_AND_SCOPE.md`, `RESEARCH_ARCHITECTURE.md`, `CURRENT_STATUS_AND_NEXT_DIRECTION.md`, `RESEARCH_ARCHITECTURE_DECISION_RECORD_20260717.md`, `THE_COUNCIL_REVIEW_FEM_OR_NO_FEM_17.07.2026.md`. Đối chiếu các file này với nội dung v1 phát hiện hai vi phạm thứ bậc nguồn: (1) RQ1–RQ3 ở v1 không phải nguyên văn khóa (§1.2 đã sửa); (2) định nghĩa CEI ở v1 dùng một tài liệu Paper-specific chưa phê duyệt (level 6) thay vì định nghĩa khóa ở Charter v1.1/bộ v2.3 (§2.3 đã sửa). Cả hai lỗi đã được sửa ở v2 — chi tiết đầy đủ trong `REVISION_LOG_MASTER_SYNTHESIS_v2_20260828.md`.

---

## 1. Định hướng và kiến trúc nghiên cứu hiện hành

### 1.1 Vấn đề nghiên cứu và mục tiêu (v1, không đổi)

Chủ sở hữu nhà công nghiệp khung thép hiện không có cách kiểm chứng được để trả lời: một cảnh báo dao động đến từ cảm biến nào, thuộc cấu kiện nào, lần kiểm tra gần nhất là khi nào, và hành động kiểm tra–bảo trì đang ở trạng thái gì (`RESEARCH_DIRECTION_AND_SCOPE.md`). Luận án xây dựng và kiểm chứng một khung Digital Twin dựa trên dữ liệu (data-informed) tổ chức, liên kết và truy vết bằng chứng trạng thái từ dữ liệu dao động tới hành động kiểm tra–bảo trì, kèm bằng chứng lab về độ tin cậy của lớp evidence và bằng chứng field về tính khả thi triển khai (`MASTER_RESEARCH_CHARTER_v1.1_LIMITED_FEM_20260717.md` §2).

Đóng góp nằm ở **quy trình quản lý thông tin và hỗ trợ quyết định kiểm tra** (Construction Management / Asset Management), không nằm ở mô hình cơ học hay thuật toán AI mới. Hội đồng 17/07/2026 chọn phương án B (FEM hỗ trợ hạn chế) thay vì phương án A (FEM là trục lõi, điểm 28/40/38) hoặc C (loại bỏ hoàn toàn FEM) — điểm Hội đồng: A=28, B=40, C=38 trên mười tiêu chí (`RESEARCH_ARCHITECTURE_DECISION_RECORD_20260717.md`; `THE_COUNCIL_REVIEW_FEM_OR_NO_FEM_17.07.2026.md` Phần 3).

### 1.2 Câu hỏi nghiên cứu (RQ) — nguyên văn đã khóa, không diễn giải thêm — **SỬA Ở V2 (Nhiệm vụ 1)**

**Nguồn khóa duy nhất, đọc toàn văn trực tiếp trong vòng revision này:** `MASTER_RESEARCH_CHARTER_v1.1_LIMITED_FEM_20260717.md` §7 (Source-of-truth level 2). Đây là văn bản RQ duy nhất được phép trích dẫn nguyên văn trong mọi bản thảo. Bản dịch tiếng Việt đi kèm chỉ là **bản dịch làm việc để hỗ trợ đọc**, không phải văn bản khóa.

- **RQ1 (nguyên văn khóa):** *"How reliably can vibration data from the 1:10 steel frame model and different sensor configurations produce evidence distinguishing controlled connection states under a run-aware, leakage-controlled evaluation protocol?"*
  Bản dịch làm việc: Dữ liệu dao động từ mô hình khung thép 1:10 và các cấu hình cảm biến khác nhau tạo được bằng chứng phân biệt các trạng thái liên kết có kiểm soát ở mức độ tin cậy nào, dưới một giao thức đánh giá run-aware, leakage-controlled?

- **RQ2 (nguyên văn khóa):** *"How can state evidence from sensor data be organized and linked to BIM components and inspection records to ensure component-level traceability?"*
  Bản dịch làm việc: Bằng chứng trạng thái từ dữ liệu cảm biến có thể được tổ chức và liên kết với cấu kiện BIM và hồ sơ kiểm tra như thế nào để bảo đảm khả năng truy vết cấp cấu kiện?

- **RQ3 (nguyên văn khóa):** *"How can a data-informed Digital Twin framework support the selection and recording of inspection actions at a real building under limited field damage data?"*
  Bản dịch làm việc: Một khung Digital Twin dựa trên dữ liệu có thể hỗ trợ việc lựa chọn và ghi nhận hành động kiểm tra tại một công trình thực như thế nào, dưới điều kiện dữ liệu hư hỏng hiện trường hạn chế?

**Ý mở rộng mà v1 từng chèn nhầm vào văn bản RQ — nay đã tách khỏi RQ và chuyển đúng vị trí:**

| Ý mở rộng (đã loại khỏi RQ ở v2) | Vị trí đúng | Trạng thái | Nguồn |
|---|---|---|---|
| "...và cấu hình cảm biến có chi phối mạnh hơn lựa chọn kiến trúc mô hình không?" (v1 gắn vào RQ1) | Candidate hypothesis của **Paper 1B — Supporting Scope** (§4.4) | `CANDIDATE — ĐANG XUNG ĐỘT` (xem M-02, §2.4) | Charter v1.1 §13 "Allowed claims": "Sensor configuration influences classification more strongly than model architecture choice" |
| "...cùng độ tin cậy của nó (CEI)... để bảo đảm biện minh và truy trách nhiệm (justification & accountability) được kiểm chứng..." (v1 gắn vào RQ2) | Mục đích phân tích bổ sung cho cách trả lời RQ2 (analytical objective) — không phải văn bản RQ2 | `APPROVED ADJUSTMENT` — điều chỉnh bắt buộc v2.1.2 đã phê duyệt | `MASTER_RESEARCH_CHARTER_CURRENT_20260812.md` v2.1.2, ghi nhận lại trong header `RESEARCH_DIRECTION_AND_SCOPE.md`: "(2) mục đích cuối = justification & accountability của quyết định kiểm tra" |
| "...dưới điều kiện dữ liệu hư hỏng hiện trường hạn chế" (v1 gắn vào RQ2) | Không thuộc RQ2 — cụm này là một phần của RQ3 | `REMOVED — LỖI SAO CHÉP` | Đối chiếu trực tiếp Charter v1.1 §7 |
| "Khung có thể triển khai tới mức nào tại một nhà công nghiệp thép thực (Rapexco)..." (v1 dùng thay khung câu RQ3 gốc "how can... support") | Design/validation objective hỗ trợ RQ3, tương ứng Validation Ladder **V3 — Field feasibility** | `APPROVED — thuộc V3, không phải văn bản RQ3` | Charter v1.1 §12 |

**Nguyên tắc áp dụng từ v2 trở đi:** mọi bản thảo trích RQ1–RQ3 dùng đúng nguyên văn tiếng Anh ở trên. Không chèn thêm mệnh đề vào câu hỏi dưới bất kỳ hình thức nào, kể cả khi mệnh đề đó có nguồn hợp lệ ở nơi khác trong hệ thống tài liệu.

### 1.3 Work Package, Chương, Paper, Evidence Gate (khoá — không tạo thêm; cập nhật ghi chú Paper 1A/1B)

| RQ | WP | Chương | Paper | Evidence Gate | Loại bằng chứng | Vai trò QLXD |
|---|---|---|---|---|---|---|
| RQ1 | WP1 — Lab evidence | C4 | **Paper 1** (nội bộ chia Core Scope = 1A, Supporting Scope = 1B — xem §4.3–4.5; **1B không tạo Paper/WP/Gate mới**) | **G1** | Laboratory evidence | Bằng chứng lab có định lượng độ tin cậy |
| RQ2 | WP2 — Traceability-to-decision | C5 | Paper 2 | **G2, G3, G6** | Information traceability | **CORE — trụ cột nhận diện ngành QLXD** |
| RQ3 | WP3 — Field feasibility | C6 | Paper 3 (bonus) | **G4, G5** | Field feasibility | Bằng chứng khả thi hiện trường |
| — | WP4 (gộp WP2/WP3) | C7 (opt., gộp C6) | Paper 4 (opt., gộp Paper 3) | **G5** | Management decision support | Hỗ trợ quyết định minh bạch, human-reviewed |

Trục chịu lực luận án là **C4 (Paper 1/RQ1) + C5 (Paper 2/RQ2)**. Yêu cầu tối thiểu của luận án: hai bài Q3 trong ba năm — Paper 1 + Paper 2 (`MASTER_RESEARCH_CHARTER_v1.1_LIMITED_FEM_20260717.md` §10). **Không có chương, Paper hay Gate FEM. Paper 1B không phải Paper thứ tư trong danh mục — nó là phạm vi hỗ trợ nội bộ của WP1, xem §4.4.**

### 1.4 Chuỗi bằng chứng và chuỗi định danh đã khoá (v1, không đổi)

```text
Vibration data
→ condition/state-change evidence (kèm CEI)
→ BIM-linked component
→ inspection record
→ inspection-maintenance action support
```

```text
Sensor_ID → BIM_GUID → Condition_Evidence_ID → Inspection_Record_ID → Action_Status
```

`Action_Status` là **điểm cuối canonical**. CEI là metadata cấu trúc hạng nhất gắn với `Condition_Evidence_ID` — định nghĩa khóa và những gì CEI không phải: xem §2.3 (đã sửa ở v2). `Asset_ID`, `Model_Version_ID`, `Action_Record_ID`, `Workflow_Status`, `Status_Event` là **noncanonical implementation proposals**. `FEM_Node_ID` chỉ là metadata tuỳ chọn, không bao giờ là mắt xích bắt buộc.

Bốn lớp bằng chứng tách biệt, không mượn chéo (`RESEARCH_ARCHITECTURE.md`):

| Lớp | Chứng minh được | Không được dùng để tuyên bố |
|---|---|---|
| 1. Laboratory evidence | Phân biệt trạng thái liên kết có kiểm soát trên mô hình 1:10 dưới đánh giá run-aware chống rò rỉ | Chẩn đoán hiện trường; suy giảm độ cứng công trình thực; ngưỡng định lượng chuyển giao được |
| 2. Information traceability | Định danh, hồ sơ, provenance, competency questions, truy vết hai chiều, toàn vẹn chuỗi | Độ chính xác chẩn đoán; khả thi hiện trường; hiệu quả quyết định |
| 3. Field feasibility | Triển khai được, dữ liệu về, baseline vận hành, ánh xạ Sensor→BIM, kịch bản truy vết end-to-end | Phát hiện hư hỏng thực; chuyển classifier lab→field; kiểm chứng chẩn đoán |
| 4. Management decision support | Hỗ trợ hành động minh bạch bốn mức, có con người rà soát | Quyết định tự động; thay thế đánh giá kỹ thuật; chấm severity/priority |

Mọi bất thường hiện trường dẫn tới **kiểm tra**, không dẫn tới **kết luận hư hỏng**.

### 1.5 Xung đột định danh đã được giải quyết theo bộ v2.3 (v1, không đổi)

Giữa 19/07 và 04/08/2026, một nhánh quản trị từng đề xuất thay điểm cuối chuỗi định danh bằng `Action_Record_ID` + `Status_Event`. Bộ v2.3 hiện hành (`SOURCE_OF_TRUTH_HIERARCHY_v2.1.md`, `TERMINOLOGY_CONTROL_CURRENT.md`, `AGENT_RULES.md`, `CURRENT_DIRECTION_LOCK_20260804.md` — Updated 11/08/2026) đã tự sửa: "Restores `Action_Status` as the canonical endpoint." `Action_Record_ID`/`Status_Event` vẫn ghi nhận như **PROPOSED — chờ ADR riêng**. `CONFLICT_AND_GAP_REGISTER_20260828.md` mục X-02 xác nhận cùng kết luận.

### 1.6 Vai trò giới hạn của FEM (v1, không đổi)

FEM là **nominal, uncalibrated, reference-only, not used for damage diagnosis** — bắt buộc kèm qualifier này ở mọi lần nhắc. Được phép: mô hình thiết kế tham chiếu danh nghĩa; tham khảo hỗ trợ chọn vị trí đặt cảm biến; minh hoạ vị trí cấu kiện; giả thuyết cơ học định tính trong Discussion/Limitation, nhãn "hypothesis, not confirmed". Bị chặn: hiệu chuẩn FEM; model updating; EMA; MAC làm tiêu chí nghiệm thu; suy luận suy giảm độ cứng hoặc lực siết bu lông; chẩn đoán hư hỏng bằng FEM; chuyển kết luận định lượng 1:10 → công trình thực. FEM **không có** RQ, WP, chương, Paper hay Evidence Gate riêng (`RESEARCH_ARCHITECTURE_DECISION_RECORD_20260717.md`).

---

## 2. Tổng hợp văn liệu theo các chủ đề nghiên cứu chính

> Nguồn chính: `LIVING_EVIDENCE_BASE_CURRENT_20260812.md`; `CITATION_AUDIT_GATE1_TO_GATE23_20260811.md`; `GATE1_BATCH_B_DEEP_READ_20260827.md`; `GATE1_00_INBOX_NEW_FULLTEXT_PRIOR_ART_SCREENING_20260827.md`; `ZOTERO_SCREENING_TLTQ_20260827.md`; `G2_G3_SCREENING_EVIDENCE_AND_GAP_REPORT.md`; `G2_G3_RECENT_EVIDENCE_SCREENING_2023_2026.md`; `ROUND4_VERIFIED_EVIDENCE_RECORD_v1.1.md`. Nhãn `SYNTHESIS/INTERPRETATION` áp dụng cho toàn bộ mục 2.

### 2.1 Dữ liệu dao động và condition/state-change evidence (RQ1/G1) — thuộc phạm vi Paper 1A (v1, giữ nguyên nội dung nền)

Bằng chứng trực tiếp mạnh nhất: **`YR2NQWE7`** Zhang, Biswal & Wang (SHMnet, 2020); **`SL6IEB2E`** Pal, Sikdar & Banerjee (2022) — khung thép một tầng, sáu strain gauge, 10 trial/điều kiện; **`RA7ZWAFU`** Parziale et al. (2024) — khung thép quy mô lớn, 30 khớp bu lông; **`YTH389L4`** Biswal et al. (2022); **`C9EKJYEC`** Naresh, Sikdar & Pal (2023) — có unseen-data testing (abstract-only).

**Phát biểu gap tóm tắt (xem bản đầy đủ, đã sửa ở v2, tại §3.1):** trong phạm vi 13 bài đã screen trực tiếp, chưa nguồn nào kiểm soát và báo cáo tường minh đồng thời cả ba trục — đơn vị độc lập vật lý, rò rỉ dữ liệu, phạm vi chuyển giao run/session/campaign — cho khung thép bắt bu lông. Tuyên bố rộng "chưa ai áp dụng deep learning cho khung thép bắt bu lông" **bị chặn** bởi `SL6IEB2E` và `RA7ZWAFU` — không được dùng.

### 2.2 Run-aware, leakage-safe evaluation, LORO/LOCO và khả năng khái quát — **SỬA Ở V2 (Nhiệm vụ 5)**

Bằng chứng phương pháp mạnh nhất: **`RG9FMT8Y`** Wheat et al. (2024) — sai số thay đổi tới **0,47** khi chuyển từ tách theo run sang tách theo part; **`M8LMWFQH`** Test-Training Leakage in CBM (2024); **`XE9XS6BQ`** grouped/LOGO cross-validation; **`PEUHYBPS`** Goodarzi et al. (2025); **`L97BIAI3`** Beleites et al. (2013) — độ nhạy khối u giảm từ 0,75 xuống 0,38 khi tách đúng nhóm; **`ZLFATP2Z`** Ojala & Garriga (2009); **`9XNSNIPX`** Demšar (2006).

Bảy bài đã kiểm chứng DOI (Ramasso 2024/2025, Ozdagli & Koutsoukos 2020, Sohn/Worden/Farrar 2002, Amin/Najeh/Ghoul 2026, Brake/Schwingshackl/Reuß 2019, Vieira et al. 2026, da Silva et al. 2024) hội tụ ở một nguyên tắc: **nhãn/trạng thái dự đoán không phải bằng chứng độc lập với bối cảnh**. Ramasso et al. giải thích trực tiếp hiện tượng LORO cao nhưng LOCO thấp, và tại sao tháo–lắp lại (reassembly) làm khó bảo đảm khả năng lặp lại giữa các campaign.

**Diễn giải LOCO theo bốn cấp (đã sửa ở v2 — thay cho phát biểu "LOCO thấp là đóng góp quản lý thông tin" ở v1, vốn biến một kết quả âm thành thành công bằng diễn giải hậu nghiệm):**

1. **Empirical evidence:** nếu LOCO thấp hơn đáng kể so với LORO — hiện tượng được ghi nhận trong văn liệu phương pháp luận nói chung (Ramasso et al., SECONDARY LOCATOR, §8 dòng C10) và được **báo cáo, chưa xác minh trực tiếp**, cho riêng dataset luận án ở bản thảo 24/08 (§0.2) — thì bằng chứng thực nghiệm cho thấy **khả năng chuyển giao (transportability) giữa các campaign còn hạn chế**.
2. **Interpretation:** kết quả dự đoán từ mô hình được huấn luyện trên một campaign **không nên được sử dụng ngoài phạm vi campaign/điều kiện đã kiểm chứng** mà không có qualification bổ sung.
3. **Implication for information management:** vì vậy, condition evidence **cần mang theo provenance và validated scope** — đây là lý do trực tiếp CEI, provenance và validated scope là thành phần bắt buộc của **Paper 1A** (§4.3), không phải một lựa chọn tùy chọn.
4. **Potential management contribution (có điều kiện, chưa xác nhận):** giá trị quản lý **chỉ được hình thành khi** các trường provenance/scope này được hình thức hóa, liên kết tới cấu kiện BIM, và kiểm chứng tại Gate 2–3 (Paper 2). Bản thân kết quả LOCO thấp, tại Gate 1, **không phải** và **không được gọi là** một "management contribution" — đây là một giới hạn thực nghiệm cần được quản lý bằng thông tin, không phải một thành công cần diễn giải lại.

**Nguyên tắc bắt buộc:** không biến kết quả âm (LOCO thấp) thành tuyên bố thành công bằng diễn giải hậu nghiệm. Bốn cấp trên phải trình bày tách bạch trong mọi bản thảo — không gộp cấp 1 (thực nghiệm) với cấp 4 (đóng góp tiềm năng, có điều kiện) trong cùng một câu.

### 2.3 Định nghĩa CEI (đã khóa) và validated scope của condition evidence — **SỬA Ở V2 (Nhiệm vụ 2)**

**Định nghĩa khóa duy nhất, dùng nhất quán trong toàn bộ tài liệu này và mọi bản thảo:**

> CEI là **confidence/evidence indicator** đi kèm condition evidence, nhằm thể hiện mức độ tin cậy hoặc qualification của evidence đó trong phạm vi đã kiểm chứng.

Nguồn khóa (đọc toàn văn trong vòng revision này): `MASTER_RESEARCH_CHARTER_v1.1_LIMITED_FEM_20260717.md` §13 ("CEI is a confidence/evidence indicator"), §14 (cấm "describing CEI as physical severity"); `RESEARCH_ARCHITECTURE.md` v2.3, Lớp 2 ("CEI là metadata của condition evidence"); `CURRENT_STATUS_AND_NEXT_DIRECTION.md` v2.3 §2 ("CEI remains structured evidence metadata and cannot be converted into a scalar, Health Index, severity, damage probability or priority without approved evidence and governance").

**CEI không phải (đã khóa, không được diễn giải khác):**
- physical damage severity;
- DSI (damage severity index);
- stiffness degradation;
- weighted Health Index;
- xác suất hư hỏng công trình thực;
- **không phải một "Condition Evidence Information profile"** — xem cảnh báo dưới.

**Cảnh báo vi phạm thứ bậc nguồn đã tồn tại ở v1 (đã sửa ở v2):** v1 (§2.3 bản gốc) định nghĩa CEI là "Condition Evidence Information profile — hồ sơ thông tin có phiên bản..." dựa theo `CEI_SCIENTIFIC_BASIS_AND_THESIS_SPECIFICATION_v1.1_20260812.md` — một tài liệu **Paper-1-specific working spec, chưa phê duyệt** (level 6 trong thứ bậc nguồn §0.3, mục 6), thấp hơn Charter v1.1 (level 2) và bộ v2.3 (level 3, cùng nhóm đã khóa lại định nghĩa gốc). Dùng định nghĩa "profile" làm định nghĩa chính là **vi phạm thứ bậc nguồn** — đã hạ cấp ở v2 (chi tiết: `REVISION_LOG_MASTER_SYNTHESIS_v2_20260828.md` mục 2).

**Không có công thức tính CEI đã khóa — không được tự tạo.** Bảy nguyên tắc khoa học dưới đây mô tả cơ sở khoa học cho một **construct cần operational validation**, không phải một quy trình tính toán đã phê duyệt:

| Nguyên tắc | Cơ sở khoa học | Ranh giới |
|---|---|---|
| Thay đổi đo được không tự động là hư hỏng | SHM literature về đặc trưng nhạy trạng thái và biến thiên môi trường/vận hành | Không nguồn nào xác nhận ngưỡng CEI riêng của luận án |
| Bối cảnh cảm biến/thu nhận ảnh hưởng kết quả | Condition-monitoring và sensing studies | Không chứng minh ba cảm biến là đủ phổ quát |
| Chất lượng dữ liệu phải đi kèm bằng chứng | SHM data-quality literature | Không áp dụng một điểm chất lượng tổng hợp |
| Đánh giá phải nhận biết phụ thuộc (dependence-aware) | Grouped validation, leakage literature | Không thay thế run registry của luận án |
| Xác suất mô hình không đồng nghĩa độ tin cậy | Calibration, dataset-shift literature | Hiệu chuẩn là tuỳ chọn trừ khi tuyên bố confidence |
| Bằng chứng cần provenance tái lập được | W3C PROV, FAIR principles | Provenance không tự chứng minh giá trị kết cấu |
| Bằng chứng động phải nối được với thông tin tài sản | Construction Digital Twin, information-processing literature | Paper 1A không sở hữu schema truy vết (thuộc Paper 2) |

**Evidence còn thiếu để vận hành hóa (operational validation) CEI — không được tự tạo trong lúc thiếu:**
- Chưa có phương pháp tính/gán giá trị CEI đã phê duyệt (thang đo, ngưỡng, hoặc quy tắc tổng hợp).
- Chưa có dữ liệu thực nghiệm kiểm chứng CEI trên đúng condition evidence của Gate 1 (chờ G1_EXECUTION_PACK).
- Chưa có liên kết đã phê duyệt giữa CEI và `G1_ACCEPTANCE_MATRIX.md` (chưa tồn tại).
- Quy tắc CEI được mang theo (propagate) qua `Condition_Evidence_ID` sang Gate 2–3 mới ở dạng nguyên tắc phát biểu (`G1_TO_G2_CONDITION_EVIDENCE_INTERFACE_v1.0.md`, working spec chưa phê duyệt), chưa có cơ chế kỹ thuật cụ thể.

**Next action:** không tạo công thức CEI trong bất kỳ bản thảo nào cho tới khi có (1) operational validation trên dữ liệu Gate 1 thực tế, và (2) phê duyệt từ thầy hướng dẫn theo đúng quy trình Stream B (pre-register trước khi khóa spec).

### 2.4 Sensor configuration và robustness — thuộc phạm vi Paper 1B, Supporting Scope (v1, giữ nội dung nền, bổ sung ghi chú phân định)

> **Ghi chú v2:** toàn bộ nội dung mục này thuộc **Paper 1B — Supporting Scope của WP1** (§4.4), không có RQ/WP/Gate riêng, và không đóng góp vào việc đóng Gate 1. Xem bảng phân định đầy đủ tại §4.5.

**`L9I5H6F9`** Dadoulis & Manolis (2026) — định lượng đóng góp cảm biến bằng multichannel CNN có giải thích được (Grad-CAM++/SCI), CI bootstrap 95% [0,9111; 0,9667]; **không** có ablation retrain khi bỏ cảm biến. **`RG9FMT8Y`** so sánh hai vị trí cảm biến (A1/A2). Chưa có bài nào trong corpus vừa (a) khung thép bắt bu lông, vừa (b) so sánh cấu hình/subset cảm biến có kiểm soát dưới đánh giá run-aware.

Candidate claim trong governance (`RQ_WP_CHAPTER_PAPER_GATE_MATRIX_v2.1.md` §5, lập 12/08; cũng ghi ở `MASTER_RESEARCH_CHARTER_v1.1_LIMITED_FEM_20260717.md` §13 Allowed claims): "Sensor configuration dominates architecture" — RF ~0,862, 1D-CNN S12 ~0,841, ResNet1D ~0,828 — **candidate claim pending Gate 1 closure**, nay thuộc phạm vi Paper 1B.

`CONFLICT_AND_GAP_REGISTER_20260828.md` (mục M-02) ghi nhận kết quả mới hơn — báo cáo lại từ bản thảo 24/08, chưa truy cập trực tiếp được (§0.2) — đo chênh lệch **pipeline** (0,34–0,48 macro-F1) lớn hơn nhiều so với chênh lệch **cấu hình cảm biến** (chỉ 0,070–0,166); ở CP3, mức 0,166 cùng bậc độ lớn với SD giữa các hoán vị (0,120–0,198) nên **không tách được khỏi nhiễu**. Claim "sensor configuration dominates architecture" **có khả năng bị đảo ngược hoặc thu hẹp đáng kể**.

File tổng hợp này **không tự hợp nhất** hai nguồn và **không tự chọn bên nào đúng**. Ghi nhận đúng nguyên tắc: **claim này hiện đang có xung đột giữa hai nguồn nội bộ (12/08 vs. báo cáo 24/08), chưa được thầy hướng dẫn phân xử — không dùng claim này ở dạng khẳng định trong bất kỳ bản thảo nào cho tới khi (1) xác minh trực tiếp được bản 24/08 và (2) có kết quả đa hạt giống.** Vì claim này thuộc Paper 1B (Supporting Scope, không Gate), xung đột này **không được phép trì hoãn việc đóng Gate 1** vốn thuộc trách nhiệm của Paper 1A.

### 2.5 BIM/IFC, component-level traceability và inspection records (RQ2/G2–G3) (v1, không đổi)

Đối thủ gần nhất: **`XUN8EX6X`** Lorvão Antunes et al. (2024) — 13 competency questions, SPARQL/GlobalId, 3 pilot. **Bellon et al. (2025)** *(`NUTL57KJ`, FULLTEXT_UNAVAILABLE)* — khung IFC 4.3.2.0 tích hợp inspection/damage/maintenance/cost. **`VI5QMSAE`** Kim et al. (2018). **`9TDVUE9Q`** Isailović et al. (2020). **Sacks et al. (2018)** SeeBridge. **`10.3390/buildings15152633`** Jia et al. (2025). **`10.1016/j.autcon.2015.12.003`** Pauwels & Terkaj (2016) — đóng góp phủ định: EXPRESS `RULE`/`FUNCTION` không chuyển được sang OWL2 DL. **`LSYSC59G`** Keet & Khan (2025) — 5 loại CQ. **`10.1016/j.autcon.2021.103688`** Lee, D. et al. (2021). **Nuyts et al. (2024)**. **Hagedorn et al. (2023)**. **Piras et al. (2026)**. **Li et al. (2023)**.

**Kết luận khoá:** BIM-linked inspection/maintenance, BIM-CMMS mở, SHACL/SPARQL/IDS compliance checking, fixture hợp lệ/không hợp lệ chung chung đều **Established**. Bốn khoảng trống **Still strong**: (1) lịch sử `Status_Event` bất biến, truy vấn được; (2) accountable authorization; (3) post-action verification hình thức có đóng bảo vệ; (4) chuỗi tích hợp đầy đủ, có định danh, đồng thời.

### 2.6 Field feasibility và hỗ trợ quyết định kiểm tra–bảo trì (RQ3/G4–G5) (v1, không đổi)

**`9823WXJZ`** Kohler et al. (2006). **`TRZY4P6X`** Yarnold (2015). **`D3TGCKXW`** Entezami et al. (2023). **`LZPF7ILT`** hệ thống multinode giá rẻ. **`XSKNR656`** Armijo & Zamora-Sánchez (2024).

**Kết luận khoá:** chưa có nguồn nào trong corpus cho nhà công nghiệp thép ven biển với `Sensor_ID → BIM_GUID` + hồ sơ kiểm tra kiểm toán được + lịch sử hành động → **Evidence is currently insufficient** để đóng G4.

### 2.7 Digital Twin, quản lý tài sản và định vị trong ngành Quản lý xây dựng (v1, không đổi)

**`ESTEYBHA`** Gemini Principles-Based DT Maturity Model (2021). **`YGZ32C8M`** Identifying Maturity Dimensions for Smart Maintenance Management (2021). Chuẩn: ISO 19650-3, TCVN 14177:2024; ISO/IEC 30173:2023 và 30186:2025 chỉ preview một phần.

**Định vị:** đóng góp là quy trình quản lý thông tin và hỗ trợ quyết định — đúng phạm vi Quản lý xây dựng/Quản lý tài sản (`THE_COUNCIL_REVIEW_FEM_OR_NO_FEM_17.07.2026.md` §2.1).

---

## 3. Research gaps và đóng góp dự kiến

> Mọi gap dưới đây ghi rõ closest competitor, bằng chứng ủng hộ, bằng chứng phản biện (nếu có) và giới hạn. Gap không đủ căn cứ ghi đúng `Evidence is currently insufficient` — không suy diễn. Không dùng khung "No study has..." nếu chưa có systematic evidence — mọi phát biểu bounded theo corpus đã screen.

### 3.1 Gap G1 — Qualification condition evidence cho khung thép bắt bu lông dưới kiểm soát đồng thời ba trục — **SỬA Ở V2 (Nhiệm vụ 4)**

**Trạng thái:** Còn bảo vệ được, ở dạng khái niệm hẹp, không phải tuyên bố rộng. Thuộc phạm vi **Paper 1A** (§4.3) — Paper 1B (§4.4) không đóng góp vào việc đóng gap này.

**Phát biểu gap (đã thu gọn — thay cho khung "chín thành phần đồng thời" ở v1):**

> Trong phạm vi văn liệu đã được kiểm chứng (13 bài screen trực tiếp — batch B + inbox 27/08 — đối chiếu thêm với Living Evidence Base), còn thiếu bằng chứng về việc qualification condition evidence dựa trên dao động của khung thép liên kết bu lông khi ba trục sau được kiểm soát và báo cáo tường minh **đồng thời**: (1) đơn vị độc lập vật lý (physical independent unit — run/specimen, không phải window/sample); (2) rò rỉ dữ liệu giữa train và test (leakage); (3) phạm vi chuyển giao được kiểm chứng giữa run/session/campaign (transfer scope).

**Vai trò của các thủ tục kiểm chứng — là cơ chế, không phải novelty độc lập:** multi-seed replication, permutation/null test, uncertainty reporting cấp run/fold, và run registry là **cơ chế để kiểm chứng gap nói trên có tồn tại và có được đóng hay không** — không phải bốn novelty tách biệt. Không trình bày riêng lẻ bất kỳ thủ tục nào trong số này như một đóng góp độc lập.

**Phân loại theo mức độ bằng chứng (thay cho "No study has…"):**

| Nhận định | Trạng thái | Căn cứ |
|---|---|---|
| Trong 13 bài đã screen trực tiếp, không nguồn nào kiểm soát và báo cáo tường minh đồng thời cả ba trục cho khung thép bắt bu lông | `SUPPORTED` (trong phạm vi corpus đã screen) | Bảng đối chiếu 16 trường, `GATE1_BATCH_B_DEEP_READ_20260827.md` §7 — SECONDARY LOCATOR, §8 dòng C16 |
| Từng trục riêng lẻ (leakage; grouped/run-aware CV) đã có tiền lệ phương pháp luận rộng trong SHM/ML nói chung | `SUPPORTED` cho tồn tại tiền lệ phương pháp; `PARTIALLY SUPPORTED` cho việc tiền lệ áp dụng đồng thời cho khung thép bắt bu lông | Wheat 2024 (`RG9FMT8Y`), Beleites 2013 (`L97BIAI3`) — SECONDARY LOCATOR |
| Gap còn tồn tại sau khi mở rộng tìm kiếm ra ngoài corpus hiện tại | `Evidence is currently insufficient` | Saturation chưa đạt, tự đánh giá trong `GATE1_BATCH_B_DEEP_READ_20260827.md` §9.5; 5 hướng tìm kiếm bổ sung còn mở (giữ nguyên từ v1) |
| "Chưa ai áp dụng deep learning cho khung thép bắt bu lông" (tuyên bố rộng) | `BLOCKED — không được dùng` | Bị chặn bởi Pal et al. 2022 (`SL6IEB2E`) và Parziale et al. 2024 (`RA7ZWAFU`) |

**Closest competitors:** `SL6IEB2E` Pal et al. 2022; `RA7ZWAFU` Parziale et al. 2024; `C9EKJYEC` Naresh et al. 2023.

**Giới hạn:** kết luận trong phạm vi corpus đã screen (targeted, không phải PRISMA hệ thống); saturation sơ bộ chưa đạt — 5 hướng tìm kiếm bổ sung: (1) khung thép bắt bu lông có split run/session tường minh hoặc LORO/LOGO; (2) sensor-subset ablation dưới fold theo nhóm; (3) multi-seed + CI cấp run/fold trên tập nhỏ; (4) permutation/null-test toàn pipeline bảo toàn nhóm; (5) khả năng chuyển giao liên phiên/liên đợt.

**Next action:** hoàn tất G1_EXECUTION_PACK — multi-seed, permutation test, uncertainty, run registry đóng vai trò **kiểm chứng gap này có được đóng hay không**, không phải mục tiêu tự thân.

### 3.2 Gap RQ2/G2 — Chuỗi truy vết tích hợp, có định danh, từ condition evidence tới action đã kiểm chứng (v1, không đổi)

**Trạng thái:** Mạnh, verdict "Still strong" trong stress-test 2023–2026 gần nhất.

**Closest competitors:** Bellon et al. 2025; `XUN8EX6X` Lorvão Antunes et al. 2024; Piras et al. 2026; Li et al. 2023.

**Bằng chứng ủng hộ gap:** bảng novelty-impact (`G2_G3_RECENT_EVIDENCE_SCREENING_2023_2026.md` §5.0.1) xác nhận bốn mảng còn "Still strong". Không nguồn nào trong 47 bài đã screen (2018–2026, hai vòng) kết hợp đồng thời cả 4 yếu tố.

**Bằng chứng phản biện (thu hẹp):** BIM-linked inspection/maintenance riêng lẻ, BIM-CMMS mở, SHACL/SPARQL/IDS, fixture hợp lệ/không hợp lệ chung chung đều **Established** — không được claim độc lập.

**Giới hạn:** kết quả tìm kiếm có giới hạn (targeted); `CLOSE_SEARCH` không phải universal absence — không được dùng để tuyên bố "đầu tiên trên thế giới".

**Next action:** pre-register competency questions và verification criteria; khoá Constraint Catalogue riêng (không thừa kế ifcOWL); chuẩn bị Fixture/Oracle Manifest.

### 3.3 Gap RQ2/G3 — Toàn vẹn tham chiếu tích hợp kết hợp truy vết hai chiều (v1, không đổi)

**Trạng thái:** Mạnh. **Closest competitors:** Hagedorn et al. 2023; Oraskari et al. 2021; Jia et al. 2025. **Giới hạn:** "bidirectional information flow" hoặc viewer retrieval **không đồng nghĩa** round-trip validation. **Next action:** khoá forward/reverse CQ; thực thi set-equality/uniqueness assertions.

### 3.4 Gap RQ3/G4 — Field feasibility cho nhà công nghiệp thép ven biển (v1, không đổi)

**Trạng thái:** `Evidence is currently insufficient` — chưa đủ căn cứ đánh giá mức độ gap vì chưa có field-access xác nhận. **Next action:** xác nhận cơ sở tiếp cận hiện trường Rapexco trước khi chuẩn bị field sensor register.

### 3.5 Gap WP4/G5 — Logic hỗ trợ quyết định bốn mức có rà soát chuyên gia (v1, không đổi)

**Trạng thái:** `Evidence is currently insufficient` để đóng, nhưng khung khái niệm có cơ sở. **Next action:** soạn tài liệu logic bốn mức + bản ghi rà soát chuyên gia.

---

## 4. Nhóm nội dung phục vụ từng mục tiêu

> Nguyên tắc chống tự đạo văn: nội dung **dùng chung** chỉ được viết một lần đầy đủ ở vị trí "gốc" và các đầu ra khác **tham chiếu**. Nội dung **riêng** không được sao chép sang đầu ra khác.

### 4.1 Tiểu luận tổng quan (v1, không đổi)

**Dùng chung:** nền tảng lý thuyết bốn lớp bằng chứng (§1.4), định vị QLXD (§1.1), vai trò giới hạn FEM (§1.6), toàn bộ §2 (bảy chủ đề văn liệu chính, trình bày như các dòng nghiên cứu). **Không dùng:** bảng chi tiết theo Gate ở §5; locator cấp trang PDF (thuộc hồ sơ nội bộ Paper 1/Paper 2).

### 4.2 Chuyên đề 1 (v1, không đổi)

**Dùng chung:** tham chiếu §1 (kiến trúc), §2.1–2.4 (RQ1/G1) làm nền. **Riêng:** vấn đề nghiên cứu và kiến trúc phương pháp (run-aware/LORO, CEI như construct đã khóa §2.3, narrow gap G1 §3.1); evidence chain RQ1; RQ–WP–Gate mapping; kế hoạch kiểm chứng 14 hạng mục `G1_EXECUTION_PACK`.

### 4.3 Paper 1A — Core Scope (WP1 / Gate 1) — **MỚI Ở V2 (Nhiệm vụ 3)**

**Phạm vi:** dataset integrity; run registry; leakage-safe run-aware/LORO evaluation; condition-evidence qualification (CEI như construct đã khóa, §2.3); provenance; cross-campaign transportability (LOCO trên cấu hình cảm biến chính/đầy đủ — diễn giải theo khung bốn cấp §2.2); validated scope.

**Vai trò Gate:** Paper 1A là bài duy nhất mang trách nhiệm đóng Gate 1. Mọi tiêu chí nghiệm thu G1 (§5) áp dụng cho Paper 1A. Paper 1B (§4.4) **không** đóng góp vào việc đóng Gate 1.

**Dùng chung:** tham chiếu §1.2 (RQ1), §1.4 (chuỗi khóa), §2.1–2.3.

**Nội dung riêng (không lặp sang Paper 1B, Chuyên đề 1 hay Tiểu luận tổng quan dưới dạng bảng số liệu):**
- Leakage-safe run-aware evaluation: chi tiết kỹ thuật LORO, split-before-windowing, train-only preprocessing.
- Condition-evidence qualification: định nghĩa CEI đã khóa (§2.3) — Paper 1A là nơi thực thi operational validation của CEI; Paper 2 chỉ nhận `Condition_Evidence_ID` và metadata tối thiểu khi bàn giao.
- Kết quả LORO/LOCO trên cấu hình chính: bảng `PAPER1_SOURCE_AND_RESULT_TRACEABILITY_MATRIX_20260812.csv` (12/08) chỉ chứa claim về pipeline dữ liệu, không chứa kết quả phân loại đã kiểm chứng nguồn. Bản thảo 24/08 được báo cáo có kết quả đầy đủ (§0.2) — **chưa xác minh trực tiếp**, không trích dẫn như fact cho tới khi NCS xác nhận.
- Provenance: `RESNET1D_PROVENANCE_AUDIT.md` — chưa tồn tại.
- Validation scope: giới hạn ở laboratory evidence, không transfer field.
- Giới hạn và cầu nối sang Gate 2–3: bàn giao `Condition_Evidence_ID` + CEI, không bàn giao kết luận chẩn đoán.

**Claim thuộc Paper 1A (được phép, có điều kiện):** bằng chứng lab phân biệt được trạng thái liên kết có kiểm soát dưới đánh giá leakage-controlled (Charter v1.1 §13). Transportability liên-campaign hạn chế (nếu xác nhận) diễn giải theo bốn cấp §2.2 — **không tự thân là "management contribution"**.

### 4.4 Paper 1B — Supporting Scope (WP1, không có RQ, WP hoặc Evidence Gate riêng) — **MỚI Ở V2 (Nhiệm vụ 3)**

**Ghi rõ:** Paper 1B là phạm vi hỗ trợ của WP1. Nó **không có RQ riêng, không có WP riêng, không có Evidence Gate riêng**. Nó không đóng góp vào việc đóng Gate 1.

**Phạm vi:** sensor count/composition; sensor subsets; performance retention; marginal benefit; held-out-run robustness; consistency giữa các campaign (riêng cho hiệu ứng cấu hình cảm biến, không phải cho core condition evidence).

**Nội dung riêng:**
- Candidate claim "sensor configuration dominates architecture" (Charter v1.1 §13) — hiện `CANDIDATE — ĐANG XUNG ĐỘT` do M-02 (§2.4).
- Dadoulis & Manolis (2026) SCI/Grad-CAM++ làm nền phương pháp so sánh đóng góp cảm biến — tài liệu tham khảo phương pháp, không phải kết quả của luận án.
- Held-out-run robustness theo từng subset cảm biến — chưa có dữ liệu, phụ thuộc cùng execution pack G1 nhưng phân tích riêng theo subset.

**Trạng thái:** toàn bộ nội dung Paper 1B hiện ở mức `Evidence is currently insufficient` để khóa bất kỳ claim nào.

### 4.5 Bảng phân định Paper 1A / Paper 1B — **MỚI Ở V2 (Nhiệm vụ 3)**

| Topic/claim | Paper 1A | Paper 1B | Shared evidence | Prohibited overlap |
|---|---|---|---|---|
| Dataset integrity, run registry, provenance | Sở hữu — nghĩa vụ Gate 1 | Tái sử dụng, không tạo claim mới | `DATASET_MANIFEST.csv`, `RUN_REGISTRY_LOCKED.csv`, `FILE_PROVENANCE_REGISTER.csv` | 1B không được trình bày dataset integrity như đóng góp riêng |
| Thiết kế và thực thi giao thức leakage-safe run-aware/LORO | Sở hữu (thiết kế + kết quả cấu hình chính) | Dùng lại giao thức cho so sánh cấu hình | `LORO_PROTOCOL_PREREGISTERED.md`, thủ tục permutation/null test | 1B không trình bày bản thân giao thức LORO là đóng góp mới; phải trích dẫn 1A |
| CEI construct (định nghĩa, §2.3) | Sở hữu — định nghĩa và operational validation | Chỉ báo cáo giá trị CEI mô tả theo cấu hình, không định nghĩa lại | Định nghĩa CEI đã khóa | 1B không đề xuất định nghĩa/công thức CEI khác |
| Cross-campaign transportability (LOCO) của condition evidence cốt lõi | Sở hữu (cấu hình chính/đầy đủ) | Không thuộc phạm vi | Tập chia liên-campaign | 1B không báo cáo LOCO như phát hiện riêng nếu dùng cùng cấu hình chính với 1A |
| Sensor count/composition, subset comparison, marginal benefit, claim "sensor configuration dominates" | Không phán quyết claim này | Sở hữu (Supporting Scope) | Cùng dataset LORO, cùng base models | 1A không dựa vào claim đang xung đột này để củng cố validated scope của chính mình |
| Held-out-run robustness theo từng subset cảm biến | Chỉ báo cáo cho cấu hình chính | Sở hữu (đa subset) | Cấu trúc run/fold | Không lặp lại cùng bảng robustness ở cả hai bài mà không dẫn nguồn chéo |
| Trách nhiệm đóng Gate 1 | Sở hữu duy nhất | Không có | — | 1B không tuyên bố đóng góp vào việc đóng Gate 1 |

**Nội dung có nguy cơ overlap/self-plagiarism cao nhất và cách xử lý:**
1. **Mô tả giao thức LORO/leakage-safe** (dùng chung cả hai bài) — 1B trích dẫn 1A bằng tham chiếu, không viết lại narrative phương pháp.
2. **Bảng kết quả macro-F1 theo cấu hình** — 1A chỉ báo cáo cấu hình chính (đại diện cho validated scope); 1B báo cáo toàn bộ ma trận cấu hình như phân tích so sánh; không trùng lặp con số ở cả hai bảng.
3. **Diễn giải LOCO** — 1A dùng khung bốn cấp (§2.2) cho ý nghĩa evidence/validated-scope; 1B (nếu có) chỉ mô tả tính nhất quán của hiệu ứng cấu hình giữa các campaign, không lặp lại toàn bộ khung diễn giải bốn cấp.

---

## 5. Evidence theo từng Gate

> Nguồn: `EVIDENCE_GATES_v2.1.md`, `RQ_WP_CHAPTER_PAPER_GATE_MATRIX_v2.1.md` §7, `CONFLICT_AND_GAP_REGISTER_20260828.md` Phần 2, `GATE_STATUS_DASHBOARD.md` (09/08, tham chiếu chéo lịch sử). **Không Gate nào PASS.**

### G1 — Dataset integrity & run-aware evaluation (`OPEN — PARTIAL EVIDENCE`, ưu tiên hiện tại) — **thuộc trách nhiệm Paper 1A duy nhất (§4.3); Paper 1B (§4.4) không liên quan tới việc đóng Gate này**

- **Evidence hiện có:** `LIVING_EVIDENCE_BASE_CURRENT_20260812.md` mục A (17 nguồn), bổ sung 13 nguồn 27/08; `CEI_SCIENTIFIC_BASIS_AND_THESIS_SPECIFICATION_v1.1_20260812.md` (dùng làm cơ sở khoa học phụ trợ, không dùng định nghĩa "profile" — xem §2.3); `PAPER1_SOURCE_AND_RESULT_TRACEABILITY_MATRIX_20260812.csv` (claim T01–T14 về pipeline dữ liệu).
- **Claim được phép:** bằng chứng lab phân biệt được trạng thái liên kết có kiểm soát dưới đánh giá leakage-controlled — mọi con số phải ghi "Candidate claim pending Gate 1 closure".
- **Limitation:** thiếu toàn bộ `G1_EXECUTION_PACK`; bảy CSV/DOI nguồn cần hoàn thiện metadata.
- **Evidence còn thiếu:** toàn bộ execution pack; bản thảo 24/08 chưa truy cập/xác minh trực tiếp (§0.2), tự nhận chưa đóng được Gate 1 vì một hạt giống và thiếu thông tin mẫu vật lý.
- **Next action:** (1) NCS xác nhận vị trí `00_CURRENT_SOURCE_OF_TRUTH` và cấp quyền đọc trực tiếp bản thảo 24/08; (2) chạy lại cấu hình chủ đạo với đa hạt giống 42/43/44; (3) khoá canonical run registry + sensor/file provenance; (4) audit split-before-windowing và train-only preprocessing; (5) xác minh ánh xạ S1/S2/S3 → vị trí cảm biến vật lý; (6) bổ sung kích thước mẫu/tiết diện/chi tiết bu lông/mô men siết; (7) hoàn tất bảy CSV bibliographic còn thiếu DOI.

### G2 — Traceability model & competency questions (`OPEN — SPECIFICATION NOT YET FROZEN`) (v1, không đổi)

- **Evidence hiện có:** `G1_TO_G2_CONDITION_EVIDENCE_INTERFACE_v1.0.md`; `G2_G3_SCREENING_EVIDENCE_AND_GAP_REPORT.md`; `G2_G3_RECENT_EVIDENCE_SCREENING_2023_2026.md`; `ROUND4_VERIFIED_EVIDENCE_RECORD_v1.1.md`; `G1_G2_INTERFACE_DECISION_REGISTER.csv`.
- **Limitation:** CQ và verification criteria chưa pre-register/phê duyệt; ADR "Action-Status-Event" vẫn OPEN.
- **Next action:** pre-register và phê duyệt CQ + verification criteria trước; sau đó mới xây schema tối thiểu.

### G3 — End-to-end laboratory traceability (`EXECUTION-NOT-OPEN`) (v1, không đổi)

**Next action:** chờ G2 baseline; sau đó thực thi bounded prototype theo đúng 8 mục.

### G4 — Field mapping & baseline feasibility (Rapexco) (`READINESS ONLY`) (v1, không đổi)

**Next action:** xác nhận field-access basis (Rapexco) — bước bắt buộc trước mọi hạng mục khác của G4.

### G5 — Inspection-action scenario review (`OPEN`) (v1, không đổi)

**Next action:** soạn tài liệu logic Normal→Watch→Inspect→Priority + tổ chức rà soát chuyên gia/facility manager.

### G6 — Paper 2 submission (`OPEN`) (v1, không đổi)

**Next action:** phụ thuộc hoàn toàn vào G2 (và G3 khi mở).

### G7 — Thesis synthesis & Paper 3 (`OPEN` / `N/A-until-G4`) (v1, không đổi)

**Next action:** chờ G4 mở; tổng hợp bốn lớp bằng chứng cho luận án độc lập với việc Paper 3 có công bố.

---

## 6. Danh mục nguồn và khả năng tái sử dụng (v1, không đổi — xem bảng đầy đủ tại v1 §6; tóm tắt cấu trúc dưới đây)

> `SOURCE EVIDENCE` = trích trực tiếp từ bản deep-read đã đối chiếu PDF gốc. `SYNTHESIS/INTERPRETATION` = tổng hợp lại từ nhiều `SOURCE EVIDENCE`. `THESIS APPLICATION` = đề xuất áp dụng cho luận án. DOI chỉ ghi khi đã được một bản deep-read xác nhận kiểm chứng.

- **§6.1 Nguồn cốt lõi RQ1/Gate 1 (Laboratory evidence):** 17 nguồn — dùng cho Paper 1A (dataset/protocol) và Paper 1B (sensor-config: Dadoulis & Manolis 2026, Wheat et al. 2024 A1/A2 comparison).
- **§6.2 Nguồn cốt lõi RQ2/Gate 2–3 (Information traceability):** 14 nguồn.
- **§6.3 Nguồn cốt lõi RQ3/Gate 4 (Field feasibility) và nền DT/QLTS:** 6 nguồn.

Bảng đầy đủ với DOI/locator giữ nguyên như v1 §6.1–6.3 (không lặp lại toàn văn ở đây để tránh trùng lặp nguồn dữ liệu — tham chiếu trực tiếp file v1 khi cần bảng đầy đủ). Bảng **claim-to-source locator mới, cấp claim riêng lẻ** (không phải cấp nguồn) nằm tại §8 dưới đây — đáp ứng yêu cầu Nhiệm vụ 6.

**Nguyên tắc truy ngược bắt buộc:** mọi nhận định trong §2–§5 có thể tìm lại đúng dòng nguồn trong bảng §6 (v1) hoặc bảng locator §8 (v2). Nhận định không tìm được dòng nguồn tương ứng phải coi là `SYNTHESIS/INTERPRETATION`, cần thầy hướng dẫn xác nhận trước khi trích dẫn ra ngoài.

---

## 7. Bảng Claim → Evidence → Limitation → Next action

### 7.1 Vấn đề quan trọng nhất của luận án

| # | Claim | Evidence | Limitation | Next action |
|---|---|---|---|---|
| 1 | Kiến trúc Limited-FEM là kiến trúc hiện hành, đã phê duyệt | ADR-2026-001; Council Verdict B 17/07/2026; bộ v2.3 xác nhận lại không đổi | Không có | Giữ nguyên; mọi tài liệu mới kèm qualifier FEM bắt buộc |
| 2 | Chuỗi định danh canonical kết thúc bằng `Action_Status` | `SOURCE_OF_TRUTH_HIERARCHY_v2.1.md`, `TERMINOLOGY_CONTROL_CURRENT.md`, `AGENT_RULES.md`; `CONFLICT_AND_GAP_REGISTER_20260828.md` X-02 | `Action_Record_ID`/`Status_Event` chờ ADR riêng | Ghi quyết định quản trị bằng văn bản để đóng X-02 |
| 3 | Gap Gate 1 (khái niệm ba trục, §3.1) còn bảo vệ được | `GATE1_BATCH_B_DEEP_READ_20260827.md`, `GATE1_00_INBOX...20260827.md` — 13 bài đã screen | Saturation chưa đạt; cần thêm 5 hướng tìm kiếm | Chạy 5 tìm kiếm mục tiêu; đánh giá lại saturation |
| 4 | Gap Gate 1 có bằng chứng thực thi (LORO, macro-F1 cụ thể) — **đã báo cáo, chưa xác minh trực tiếp** | `00_LATEST_EVIDENCE_POINTER_20260828.md` + `CONFLICT_AND_GAP_REGISTER_20260828.md` X-01 | File 24/08 chính chủ không truy cập được (§0.2); tự nhận `[BLOCKING BEFORE SUBMISSION]` | NCS cấp quyền đọc trực tiếp; chạy lại đa hạt giống 42/43/44 |
| 5 | Claim "sensor configuration dominates architecture" (**nay thuộc Paper 1B, §4.4–4.5**) | Matrix 12/08 (RF~0,862...) | Xung đột với 24/08 (M-02): pipeline 0,34–0,48 >> sensor-config 0,070–0,166 | Thầy hướng dẫn xem lại; không dùng khẳng định; không để trì hoãn Gate 1 (thuộc 1A) |
| 6 | Gap Gate 2 (chuỗi tích hợp evidence-to-action) là đóng góp mạnh nhất | `G2_G3_RECENT_EVIDENCE_SCREENING_2023_2026.md` §5.0.1 | Kết quả tìm kiếm có giới hạn, không phải universal absence | Pre-register CQ + verification criteria trước khi xây schema |
| 7 | CEI là confidence/evidence indicator, không phải scalar — **định nghĩa đã khóa lại ở v2, §2.3** | Charter v1.1 §13/§14; `RESEARCH_ARCHITECTURE.md`; `CURRENT_STATUS_AND_NEXT_DIRECTION.md` | Chưa thực thi operational validation trên dữ liệu Gate 1 thực tế; không có công thức đã khóa | Thực thi CEI trên condition evidence Gate 1 thực tế sau khi có G1_EXECUTION_PACK; không tự tạo công thức |
| 8 | Minimum field feasibility evidence bắt buộc độc lập với việc Paper 3 công bố | Charter v1.1 §3; `EVIDENCE_GATES_v2.1.md` G4 | Field-access Rapexco chưa xác nhận | Xác nhận field-access basis trước mọi hạng mục G4 khác |
| 9 | **RQ1–RQ3 dùng đúng nguyên văn khóa Charter v1.1 §7 (sửa ở v2, §1.2)** | Đọc toàn văn trực tiếp `MASTER_RESEARCH_CHARTER_v1.1_LIMITED_FEM_20260717.md` §7 trong vòng revision này | v1 từng chèn thêm mệnh đề vào RQ1/RQ2/RQ3 — đã sửa | Dùng đúng nguyên văn trong mọi bản thảo kể từ v2; không chèn thêm mệnh đề dưới bất kỳ hình thức nào |

### 7.2 Bốn đầu ra chính (mở rộng từ ba đầu ra gốc do Paper 1 tách 1A/1B — §4.3–4.4)

| Đầu ra | Claim | Evidence | Limitation | Next action |
|---|---|---|---|---|
| **Tiểu luận tổng quan** | Bảy dòng nghiên cứu chính (§2) đã được lập bản đồ đầy đủ; khoảng trống định vị ở chuỗi tích hợp | `LIVING_EVIDENCE_BASE_CURRENT_20260812.md`; ba file deep-read 27/08; hai file screening G2-G3 | Corpus giới hạn bởi `CLOSE_SEARCH`; một số DOI còn thiếu | Repair 16 mục thiếu DOI + 8 mục thiếu định danh trước khi nộp bản thảo trích dẫn |
| **Chuyên đề 1** | Kiến trúc phương pháp RQ1/G1 (run-aware/LORO, CEI đã khóa) có cơ sở khoa học vững | `CEI_SCIENTIFIC_BASIS_AND_THESIS_SPECIFICATION_v1.1_20260812.md` (chỉ phần cơ sở khoa học, không dùng định nghĩa "profile"); `EVIDENCE_GATES_v2.1.md` G1 | Toàn bộ 14 gate item G1 vẫn `OPEN` | Khoá G1_EXECUTION_PACK theo đúng 14 mục |
| **Paper 1A / Gate 1** | Bằng chứng lab phân biệt trạng thái liên kết có kiểm soát dưới đánh giá leakage-controlled; đã có bản thảo thực thi (24/08) báo cáo (chưa xác minh trực tiếp) macro-F1 trong-campaign tới 0,955 và sụp đổ liên-campaign còn 0,147 | Corpus RQ1 (§6.1); pipeline dữ liệu 216 recording đã audit; mô tả bản thảo 24/08 qua con trỏ 28/08 | Mọi kết luận định lượng là candidate pending Gate 1; con số 24/08 chưa xác minh trực tiếp; bản thảo tự nhận một-seed | Xác nhận và cấp quyền đọc trực tiếp `00_CURRENT_SOURCE_OF_TRUTH`; chạy lại cấu hình chủ đạo với đa hạt giống; hoàn tất G1_ACCEPTANCE_MATRIX có chữ ký |
| **Paper 1B / Supporting Scope (không Gate riêng)** | Cấu hình cảm biến có thể ảnh hưởng hiệu năng phân loại — mức độ ảnh hưởng đang xung đột giữa hai nguồn nội bộ | §2.4, §4.4–4.5; `CONFLICT_AND_GAP_REGISTER_20260828.md` M-02 | Claim "dominates architecture" chưa được phân xử; không có Gate riêng nên không có nghĩa vụ đóng | Thầy hướng dẫn phân xử M-02; không dùng claim ở dạng khẳng định trong bất kỳ bản thảo nào |

---

## 8. Bảng claim-to-source locator — **MỚI Ở V2 (Nhiệm vụ 6)**

> Quy tắc: claim văn liệu phải truy được đến paper gốc và locator cụ thể nếu có. Claim thực nghiệm phải truy được đến artefact/bảng kết quả/script/output tương ứng. Nếu chỉ truy được đến deep-read note (không phải PDF gốc do chính phiên này đối chiếu), ghi `SECONDARY LOCATOR — ORIGINAL SOURCE NOT YET VERIFIED`. Nếu chưa có locator, ghi `NOT VERIFIED` — không tạo locator giả.

| Claim_ID | Exact claim | Claim type | Source file/paper | Page/section/table/figure or artefact path | Verification status | Allowed use | Limitation |
|---|---|---|---|---|---|---|---|
| C01 | RQ1 nguyên văn: "How reliably can vibration data from the 1:10 steel frame model and different sensor configurations produce evidence distinguishing controlled connection states under a run-aware, leakage-controlled evaluation protocol?" | THESIS APPLICATION (governance, khóa) | `MASTER_RESEARCH_CHARTER_v1.1_LIMITED_FEM_20260717.md` | §7 (Research questions) | VERIFIED AT SOURCE (đọc trực tiếp toàn văn phiên này) | Dùng nguyên văn cho mọi bản thảo | Không được diễn giải thêm vào câu hỏi |
| C02 | RQ2 nguyên văn: "How can state evidence from sensor data be organized and linked to BIM components and inspection records to ensure component-level traceability?" | THESIS APPLICATION (khóa) | cùng file trên | §7 | VERIFIED AT SOURCE | Dùng nguyên văn | Không diễn giải thêm |
| C03 | RQ3 nguyên văn: "How can a data-informed Digital Twin framework support the selection and recording of inspection actions at a real building under limited field damage data?" | THESIS APPLICATION (khóa) | cùng file trên | §7 | VERIFIED AT SOURCE | Dùng nguyên văn | Không diễn giải thêm |
| C04 | "Sensor configuration influences classification more strongly than model architecture choice" (Allowed claim) | THESIS APPLICATION | cùng file trên | §13 (Allowed claims) | VERIFIED AT SOURCE | Chỉ dùng cho Paper 1B, dạng candidate | Hiện xung đột với M-02 (§2.4) — không dùng làm khẳng định |
| C05 | CEI = confidence/evidence indicator; không phải severity/DSI/Health Index/xác suất hư hỏng | SOURCE EVIDENCE (governance) | `MASTER_RESEARCH_CHARTER_v1.1_LIMITED_FEM_20260717.md` §13/§14; `RESEARCH_ARCHITECTURE.md` Lớp 2; `CURRENT_STATUS_AND_NEXT_DIRECTION.md` §2 | Các mục nêu trên | VERIFIED AT SOURCE | Định nghĩa khóa, dùng xuyên suốt | Không có công thức tính đã khóa |
| C06 | Qualifier FEM bắt buộc: "nominal, uncalibrated, reference-only, not used for damage diagnosis" | SOURCE EVIDENCE | `RESEARCH_ARCHITECTURE_DECISION_RECORD_20260717.md` | "What FEM may still do" / "What FEM must not do" | VERIFIED AT SOURCE | Bắt buộc kèm mọi lần nhắc FEM | Không áp dụng cho thảo luận ngoài phạm vi FEM |
| C07 | Điểm Hội đồng: A=28, B=40, C=38 trên 10 tiêu chí | SOURCE EVIDENCE | `THE_COUNCIL_REVIEW_FEM_OR_NO_FEM_17.07.2026.md` | Phần 3 (Ma trận so sánh) | VERIFIED AT SOURCE | Minh họa căn cứ quyết định kiến trúc | Không suy rộng sang các quyết định khác của luận án |
| C08 | Wheat et al. 2024: sai số thay đổi tới 0,47 khi chuyển tách theo run → tách theo part | SOURCE EVIDENCE (literature, `RG9FMT8Y`) | `GATE1_00_INBOX_NEW_FULLTEXT_PRIOR_ART_SCREENING_20260827.md` | §3 | SECONDARY LOCATOR — ORIGINAL SOURCE NOT YET VERIFIED | Minh họa mức độ ảnh hưởng của leakage; nền cho khung diễn giải LOCO §2.2 | Không dùng làm ngưỡng định lượng cho luận án |
| C09 | Beleites et al. 2013: độ nhạy 0,75→0,38 khi grouped CV theo bệnh nhân/lô | SOURCE EVIDENCE (literature, `L97BIAI3`) | `GATE1_BATCH_B_DEEP_READ_20260827.md` | §5 | SECONDARY LOCATOR — ORIGINAL SOURCE NOT YET VERIFIED | Minh họa pseudoreplication; nền cho gap §3.1 | Không dùng làm ngưỡng định lượng |
| C10 | Ramasso et al.: giải thích LORO cao/LOCO thấp qua reassembly giữa campaign | SOURCE EVIDENCE (literature) | `CITATION_AUDIT_GATE1_TO_GATE23_20260811.md` | P1 | SECONDARY LOCATOR — ORIGINAL SOURCE NOT YET VERIFIED | Nền lý thuyết cho khung diễn giải LOCO bốn cấp (§2.2) | Không suy ra số liệu cụ thể cho dataset luận án |
| C11 | Bản thảo 24/08: macro-F1 CP2_21 tới 0,955 (ResNet1D); liên-campaign rơi 0,955→0,147 | THESIS APPLICATION (empirical, dataset luận án) | `PAPER1_BUILDINGS_VIETNAMESE_DRAFT_v0.2.md` (mô tả qua `00_LATEST_EVIDENCE_POINTER_20260828.md`) | Đường dẫn khai báo: `00_CURRENT_SOURCE_OF_TRUTH/05_PAPERS/PAPER_1_RQ1_G1/02_MANUSCRIPT_CURRENT/...v0.2.md` | **NOT VERIFIED** — file gốc không truy cập được (§0.2) | Không trích dẫn như fact trong bản thảo chính thức | Cần xác minh trực tiếp trước khi dùng trong Paper 1A |
| C12 | M-02: chênh lệch pipeline (0,34–0,48) >> chênh lệch cấu hình cảm biến (0,070–0,166) | THESIS APPLICATION (empirical) | `CONFLICT_AND_GAP_REGISTER_20260828.md` | Mục M-02 | **NOT VERIFIED** | Chỉ dùng để cảnh báo xung đột (§2.4, §4.5); không dùng làm kết luận | Cần thầy hướng dẫn phân xử sau khi xác minh nguồn 24/08 |
| C13 | Pauwels & Terkaj 2016: EXPRESS `RULE`/`FUNCTION` không chuyển được sang OWL2 DL | SOURCE EVIDENCE (literature) | `ROUND4_VERIFIED_EVIDENCE_RECORD_v1.1.md` | §4.5 (P5) | SECONDARY LOCATOR — ORIGINAL SOURCE NOT YET VERIFIED (deep-read tự nhận page-verified nhưng phiên này chưa đối chiếu PDF gốc trực tiếp) | Căn cứ cho quyết định không thừa kế ifcOWL trong Constraint Catalogue G2 | Không mở rộng sang các phần khác của EXPRESS/IFC ngoài RULE/FUNCTION/WHERE |
| C14 | Lorvão Antunes et al. 2024: 13 competency questions, SPARQL trả kết quả kèm GlobalId, 3 pilot | SOURCE EVIDENCE (literature) | `LIVING_EVIDENCE_BASE_CURRENT_20260812.md` mục B | Mục B, mã `XUN8EX6X` | SECONDARY LOCATOR — ORIGINAL SOURCE NOT YET VERIFIED | Benchmark gần nhất cho Paper 2 | Không dùng để tuyên bố Paper 2 vượt trội tuyệt đối |
| C15 | "No Gate is PASS" | SOURCE EVIDENCE (governance) | `CURRENT_STATUS_AND_NEXT_DIRECTION.md` | §1 (Locked Status) | VERIFIED AT SOURCE | Dùng xuyên suốt tài liệu | Không áp dụng riêng cho từng Gate mà không đối chiếu bảng §5 |
| C16 | Gap G1 (ba trục) — không nguồn nào trong 13 bài kiểm soát đồng thời | SYNTHESIS/INTERPRETATION | `GATE1_BATCH_B_DEEP_READ_20260827.md` | §7 (ma trận 16 trường) | SECONDARY LOCATOR — ORIGINAL SOURCE NOT YET VERIFIED | Phát biểu gap rút gọn §3.1 | Không mở rộng thành "chưa ai từng làm" |
| C17 | `00_CURRENT_SOURCE_OF_TRUTH` không truy cập được dù đã Glob nhiều lần | SOURCE EVIDENCE (hành động của chính phiên này) | Kết quả `Glob` trong phiên tạo v1 + `00_LATEST_EVIDENCE_POINTER_20260828.md`/`CONFLICT_AND_GAP_REGISTER_20260828.md` | Toàn văn hai file | VERIFIED AT SOURCE (tự thực hiện, có thể lặp lại) | Giải thích hạn chế truy cập (§0.2) | Không suy ra file không tồn tại — chỉ suy ra "không truy cập được trong phiên này" |
| C18 | Định nghĩa CEI "Condition Evidence Information profile" — bị hạ cấp ở v2 | THESIS APPLICATION (working spec, chưa phê duyệt) | `CEI_SCIENTIFIC_BASIS_AND_THESIS_SPECIFICATION_v1.1_20260812.md` | Toàn văn (đọc ở phiên trước, không đọc lại trong vòng revision này) | SECONDARY LOCATOR — ORIGINAL SOURCE NOT YET VERIFIED (chỉ đọc qua ghi chú của phiên trước) | Chỉ dùng làm cơ sở khoa học phụ trợ cho 7 nguyên tắc (§2.3 bảng), **không dùng làm định nghĩa chính** | Không phục hồi định nghĩa "profile" trong bất kỳ bản thảo nào cho tới khi được phê duyệt qua đúng quy trình Stream B |

---

## 9. Báo cáo kết thúc nhiệm vụ (vòng revision v2)

**File đã đọc thêm trong vòng revision này (không sửa/xoá/di chuyển):** `00_README_START_HERE.md`, `MASTER_RESEARCH_CHARTER.md`, `MASTER_RESEARCH_CHARTER_v1.1_LIMITED_FEM_20260717.md`, `RESEARCH_DIRECTION_AND_SCOPE.md` (v2.3), `RESEARCH_ARCHITECTURE.md` (v2.3), `CURRENT_STATUS_AND_NEXT_DIRECTION.md` (v2.3), `RESEARCH_ARCHITECTURE_DECISION_RECORD_20260717.md`, `THE_COUNCIL_REVIEW_FEM_OR_NO_FEM_17.07.2026.md` — cả 8 file đọc toàn văn trực tiếp trong phiên này.

**File đã tạo:** `MASTER_LITERATURE_AND_EVIDENCE_SYNTHESIS_v2_20260828.md` (file này); `REVISION_LOG_MASTER_SYNTHESIS_v2_20260828.md`. **File v1 giữ nguyên, không bị ghi đè/sửa/xoá.**

**Evidence đã dùng:** liệt kê tại §6 (kế thừa v1) và §8 (bảng locator mới).

**Hạn chế chưa giải quyết (kế thừa từ v1, chưa đổi):**
1. `00_CURRENT_SOURCE_OF_TRUTH` vẫn không truy cập được — hạn chế quan trọng nhất, ảnh hưởng trực tiếp Paper 1A (§0.2, §4.3).
2. Claim "sensor configuration dominates architecture" (nay Paper 1B) vẫn xung đột, chưa phân xử.
3. 16 nguồn thiếu DOI, 8 mục thiếu định danh thư mục học trong Living Evidence Base.
4. Bellon et al. (2025) — full text vẫn `FULLTEXT_UNAVAILABLE`.
5. Saturation Gate 1 chưa đạt.
6. Phiên bản Paper 1 chưa gắn `Supersedes:`/`Superseded by:` đầy đủ.
7. `demsar06a.pdf` chưa được mã hoá vào register nào.

**Vấn đề mới phát sinh từ vòng revision này (cần quyết định):**
8. Operational validation cho CEI (§2.3) chưa có phương pháp — cần phê duyệt trước khi vận hành hóa.
9. Việc tách Paper 1A/1B (§4.3–4.5) là cấu trúc nội bộ đề xuất trong tài liệu tổng hợp này để giảm rủi ro Gate 1 bị trì hoãn bởi claim đang xung đột — **chưa phải quyết định chính thức về chiến lược công bố**; cần thầy hướng dẫn xác nhận có áp dụng cấu trúc này cho bản thảo Paper 1 thật hay không.

**Next action tổng thể:** (1) NCS xác nhận vị trí vật lý `00_CURRENT_SOURCE_OF_TRUTH`; (2) Stream A — khoá G1_EXECUTION_PACK (Paper 1A); (3) thầy hướng dẫn phân xử M-02 (Paper 1B); (4) phê duyệt operational validation method cho CEI trước khi vận hành hóa; (5) Stream B/C như v1 (G2, G4).

**Evidence Gate kế tiếp có gần hơn không:** Không. Vòng revision này là chỉnh sửa cấu trúc/diễn giải/truy xuất nguồn của một tài liệu tổng hợp — không tạo, không thực thi và không ký bất kỳ artifact bắt buộc nào của G1–G7. Gate 1 vẫn `OPEN — PARTIAL EVIDENCE`, vẫn là ưu tiên, nay rõ ràng thuộc trách nhiệm Paper 1A.

---

## 10. Tự kiểm tra sáu nhiệm vụ

| # | Nhiệm vụ | Kết quả | Ghi chú |
|---|---|---|---|
| 1 | Khôi phục nguyên văn RQ đã khóa | **PASS** | §1.2 dùng đúng nguyên văn Charter v1.1 §7; bốn ý mở rộng đã tách và gắn trạng thái đúng vị trí |
| 2 | Khóa một định nghĩa CEI duy nhất | **PASS** | §2.3 dùng đúng định nghĩa yêu cầu; loại bỏ "Condition Evidence Information profile" khỏi vị trí định nghĩa chính; không tạo công thức; ghi rõ evidence còn thiếu |
| 3 | Tách Paper 1A/1B + bảng phân định | **PASS** | §4.3–4.5; bảng Topic/claim → 1A → 1B → Shared evidence → Prohibited overlap đầy đủ; Paper 1B ghi rõ không có RQ/WP/Gate riêng |
| 4 | Thu gọn research gap Gate 1 | **PASS** | §3.1 viết lại theo khung ba trục khái niệm; multi-seed/permutation/uncertainty/run registry ghi rõ là cơ chế kiểm chứng; bảng SUPPORTED/PARTIALLY SUPPORTED/Evidence insufficient thay cho "No study has…" |
| 5 | Sửa diễn giải LOCO và tách cấp đóng góp | **PASS** | §2.2 dùng đúng bốn cấp: empirical evidence → interpretation → implication for information management → potential management contribution (có điều kiện); không gọi LOCO thấp là management contribution tự thân |
| 6 | Bổ sung claim-to-source locator | **PASS** | §8, 18 dòng, đủ cột yêu cầu; phân biệt VERIFIED AT SOURCE / SECONDARY LOCATOR — ORIGINAL SOURCE NOT YET VERIFIED / NOT VERIFIED; không tạo locator giả; phân biệt SOURCE EVIDENCE / SYNTHESIS-INTERPRETATION / THESIS APPLICATION |

**Giới hạn của việc tự kiểm tra:** đây là tự đánh giá trong cùng phiên tạo ra tài liệu — nên được xem là `SYNTHESIS/INTERPRETATION`, không phải xác nhận độc lập. Khuyến nghị thầy hướng dẫn hoặc một phiên rà soát riêng đối chiếu lại trước khi dùng v2 làm nguồn chính thức cho bản thảo Paper 1A/1B hoặc Chuyên đề 1.
