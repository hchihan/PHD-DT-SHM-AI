# PAPER 1B — ĐỀ XUẤT OUTLINE MANUSCRIPT (tiếng Việt)

**Phiên bản:** v1.0
**Ngày lập:** 2026-08-24
**Vai trò người lập:** cố vấn học thuật / scientific writing advisor
**Nguồn đã đọc và sử dụng:**

| Nguồn | Vai trò |
|---|---|
| `GATE1_LORO_UPDATED_RESULTS_AUDIT_20260824.md` | Nguồn số liệu chính (đã audit, ưu tiên cao nhất) |
| `GATE1_INTEGRATED_EVIDENCE_AND_CLOSURE_AUDIT_20260819.md` | Kết quả YC4 fixed-split, claim matrix, cảnh báo sample size |
| `Output_added_24.08.2026/Note.md` | Quyết định CP2_21 / CP2_2122 |
| `Output_added_24.08.2026/Readme.md` | Cấu trúc canonical dataset, lịch sử chạy |
| `Output_yc4_Sensors/yeu_cau_cuoi.md` | Thiết kế thí nghiệm sensor-count gốc |
| `Output_yc1_Data_Analyze/sensor_position_permutation_synchronization.md` | Vấn đề định danh vị trí cảm biến (S1/S2/S3) |
| `Prompt Claude Cowork — Full Vietnamese Draft for Buildings…md` | Phạm vi và narrative đã khóa của **Paper 1 chính** |
| `loro-each-sensor-v1/.../summary/summary.csv` (mẫu `cp2_s123`) | Kiểm chứng cấu trúc dữ liệu fold-level còn lưu được |

> **Nguyên tắc áp dụng xuyên suốt tài liệu này:** không tạo số liệu, không tạo p-value, không tạo confidence interval, không tạo tài liệu tham khảo, không tạo kết luận. Mọi con số xuất hiện dưới đây đều được trích nguyên văn từ audit đã dẫn. Mọi chỗ chưa có bằng chứng đều được đánh dấu placeholder.

---

## 0. TÓM TẮT ĐÁNH GIÁ CHO TÁC GIẢ (đọc trước)

### 0.1 Phán quyết

```text
GO WITH REVISION
```

**Lý do GO.** Bộ `loro-each-sensor-v1` là bộ dữ liệu ablation **hiếm** so với mặt bằng literature: 17 cấu hình cảm biến × 30 LORO fold × 3 campaign, cùng một kiến trúc, cùng một protocol, cùng một seed, đầy đủ 510/510 run trên đĩa, và **giữ được metric ở cấp từng fold** (`summary.csv` có 30 dòng `aggregate_over = seed` với `split_id` khớp nhau giữa mọi cấu hình). Điều này cho phép **paired run-level analysis mà không phải train lại bất cứ mô hình nào**. Đây là điều kiện cần để có một bài sensor-configuration nghiêm túc, và hiện tại nhóm đã có.

Quan trọng hơn: dữ liệu hiện có chứa **ba negative result có giá trị công bố**, cả ba đều **không** thuộc lõi Paper 1 chính:

1. Thêm cảm biến **không** cải thiện đơn điệu — CP2 `s13` (8 kênh, 0,9657) ≥ `s123` (12 kênh, 0,9575); CP3 `s3` (4 kênh, 0,5129) > `s12` (8 kênh, 0,3925).
2. **Biên độ trong cùng một số lượng cảm biến lớn ngang hoặc lớn hơn biên độ giữa các số lượng** — CP3 nhóm 2-sensor trải từ 0,3925 (`s12`) đến 0,5277 (`s13`), tức 0,135, trong khi khoảng cách trung bình 1→2→3 sensor nhỏ hơn nhiều.
3. **Thứ hạng cấu hình không lặp lại giữa các campaign** — cấu hình tốt nhất quan sát được là `s12` ở CP1, `s13` ở CP2_21, `s123` ở CP3. Không có cấu hình nào thắng ở cả ba.

Finding 3 chính là novelty mạnh nhất và **khác bản chất** với Paper 1: Paper 1 nói *classifier* không chuyển giao được giữa campaign; Paper 1B nói *bảng xếp hạng cấu hình cảm biến* cũng không chuyển giao được — một đối tượng khác, một hệ quả phương pháp luận khác.

**Lý do WITH REVISION (không phải GO thẳng).** Với dữ liệu hiện tại **nguyên trạng**, bài chưa đủ sức qua peer review ở Q3 mạnh, vì bốn lý do cứng:

| # | Vấn đề | Hệ quả với reviewer |
|---|---|---|
| R1 | **Chỉ một seed (42).** Mọi SD hiện có là fold-to-fold, không chứa initialisation variance | Không thể phát biểu bất kỳ so sánh cấu hình nào. Audit 19.08 ghi seed SD = 0,065 **lớn hơn** split SD = 0,054 → seed variance là nguồn nhiễu lớn nhất và đang bị bỏ trống |
| R2 | **Chỉ một pipeline (ResNet1D) trên toàn bộ lưới 17 cấu hình** | Reviewer sẽ hỏi ngay: kết luận về cấu hình cảm biến có phải là thuộc tính của cảm biến, hay của riêng ResNet1D? Hiện chưa trả lời được |
| R3 | **Số lượng cảm biến bị lẫn hoàn toàn với số kênh đầu vào** (1 sensor = 4 kênh, 2 = 8, 3 = 12) | Mọi "hiệu ứng số lượng cảm biến" hiện tại có thể chỉ là hiệu ứng chiều đầu vào của mạng. Chưa có control nào tách hai thứ này |
| R4 | **Định danh vật lý S1/S2/S3 chưa verified trong artefact**, và CP1 từng có 21/72 file bị hoán vị định danh cảm biến | Một bài về *sensor configuration* mà không chứng minh được kênh nào là cảm biến nào thì không phát biểu được gì về "composition" |

R1 và R2 là **blocking**. R3 và R4 là **nên có** — nhưng R3 nếu làm được sẽ nâng bài từ Q3 lên ứng viên Q2 thật sự.

### 0.2 Ba việc quyết định số phận bài này

```text
1. Chạy lại toàn bộ 17 cấu hình × 30 fold với ≥3 seed (42, 43, 44)     → bắt buộc
2. Chạy thêm ≥1 pipeline trên toàn bộ lưới 17 cấu hình (đề xuất random_forest) → bắt buộc
3. Thí nghiệm sensor-dropout tại inference (dùng lại checkpoint s123 đã có) → nâng bài lên Q2
```

Việc 3 gần như miễn phí về compute (không train lại) và mở ra một câu hỏi mà **không** kết quả nào hiện có trả lời được, đồng thời hoàn toàn nằm ngoài Paper 1.

---

## 1. TÊN BÀI, CÂU HỎI NGHIÊN CỨU, NOVELTY, NARRATIVE

### 1.1 Ứng viên tên bài

**(A) — Recommended Title**

> **Sensor-Subset Rankings Do Not Replicate Across Measurement Campaigns: A Paired Run-Aware Ablation of Reduced Sensor Configurations on a Scaled Steel Frame**

Tiếng Việt: *Thứ hạng tổ hợp cảm biến không lặp lại giữa các đợt đo: phân tích ablation theo run-aware có ghép cặp trên khung thép tỉ lệ thu nhỏ.*

Lý do khuyến nghị: đặt **negative/replication result** làm tiêu đề, đúng với sức mạnh thật của dữ liệu, và tự động tách khỏi Paper 1.

**(B)** — bám định hướng ban đầu của tác giả

> **Beyond Sensor Count: Run-Aware Performance Retention and Robustness of Reduced Sensor Configurations in a Scaled Steel Frame**

**(C)** — nghiêng về khía cạnh thực hành

> **How Much Performance Does a Reduced Sensor Set Retain? Paired Run-Aware Evaluation of Sensor Configurations for Vibration-Based Classification of Controlled Connection States**

> Khuyến nghị: dùng **(A)** làm title, dùng ý của **(B)** làm running head / câu mở Abstract.

### 1.2 Câu hỏi nghiên cứu

**RQ chính (Paper 1B):**

> Dưới một protocol run-aware, leakage-controlled cố định và một pipeline phân tích cố định, các cấu hình cảm biến rút gọn giữ lại được bao nhiêu hiệu năng phân loại so với cấu hình đầy đủ, và mức giữ lại đó là thuộc tính của **số lượng** cảm biến, của **thành phần tổ hợp** cảm biến, hay của **đợt đo**?

**RQ phụ:**

- **RQ-B1 (retention).** Với mỗi campaign, mỗi cấu hình rút gọn giữ lại bao nhiêu phần trăm macro-F1 của cấu hình đầy đủ, tính **theo từng held-out run có ghép cặp**, chứ không theo trung bình gộp?
- **RQ-B2 (count vs composition).** Biên độ giữa các tổ hợp **cùng số lượng** cảm biến so với biên độ giữa các **số lượng** cảm biến — cái nào lớn hơn?
- **RQ-B3 (marginal benefit).** Lợi ích biên khi thêm cảm biến thứ hai và thứ ba, tính theo cặp trên cùng held-out run, có vượt được biến thiên run-level và seed-level không?
- **RQ-B4 (run-level robustness).** Cấu hình có trung bình cao có kèm theo sàn (worst held-out run) cao không, hay trung bình và sàn tách rời nhau?
- **RQ-B5 (rank consistency).** Thứ hạng các cấu hình có nhất quán giữa CP2_21 và CP3 (cùng 7 cấu hình), và giữa các pipeline phân tích không?
- **RQ-B6 (class-specific).** Việc rút gọn cảm biến làm suy giảm đồng đều mọi lớp, hay tấn công có chọn lọc vào một ranh giới trạng thái cụ thể?

### 1.3 Novelty — phát biểu chính xác

Bốn điểm, xếp theo độ mạnh:

| # | Novelty | Vì sao mới | Rủi ro |
|---|---|---|---|
| N1 | **Non-replication của sensor-subset ranking giữa các campaign độc lập trên cùng một specimen** | Literature về sensor selection/placement gần như luôn đánh giá trên **một** đợt đo. Chưa thấy nghiên cứu nào kiểm tra xem chính bảng xếp hạng đó có lặp lại ở đợt đo khác không | Cần chứng minh S1/S2/S3 là cùng cảm biến vật lý giữa CP2 và CP3 → phụ thuộc R4 |
| N2 | **Paired run-level retention framework** thay cho so sánh trung bình gộp: run là đơn vị thực nghiệm, fold/seed/window không phải | Đa số ablation trong SHM báo cáo trung bình pooled và xếp hạng theo mean | Cần multi-seed để có ý nghĩa (R1) |
| N3 | **Dual-criterion sufficiency** (retention **và** worst-run floor) thay cho "bao nhiêu cảm biến là đủ" | Dữ liệu đã có ví dụ phản chứng rõ: `cp2_s12` mean 0,9346 nhưng fold thấp nhất 0,731; `cp3_s12` mean 0,3925 với một fold ở **0,050** | Ngưỡng phải được đặt trước, có lập luận, không hậu kiểm |
| N4 | **Tách số lượng cảm biến khỏi số kênh đầu vào** bằng control channel-matched | Chưa từng thấy tách rõ trong ablation SHM dùng deep model early-fusion | Cần thí nghiệm mới (R3) |

### 1.4 Narrative chính (một câu, dùng xuyên suốt)

> **Hiệu năng quan sát được của một cấu hình cảm biến rút gọn không phải là một thuộc tính của bộ cảm biến đó. Nó là một đại lượng đồng thời phụ thuộc vào đợt đo, vào run được giữ lại để kiểm tra và vào pipeline phân tích; do đó việc giảm số cảm biến chỉ có thể được biện luận theo mức giữ lại hiệu năng có ghép cặp kèm sàn robustness ở cấp run, chứ không theo một bảng xếp hạng cấu hình.**

**Không** được viết:
- "Hai cảm biến là đủ" / "ba cảm biến tốt hơn hai".
- "Optimal sensor placement" / "minimum sensor requirement".
- "Tiết kiệm chi phí lắp đặt".
- "Cấu hình X tốt hơn cấu hình Y" khi chưa có paired run-level analysis.

---

## 2. HIGHLIGHTS (3–5 dòng, chuẩn Elsevier/Springer)

Chỉ những highlight đã có bằng chứng verified. Các highlight còn phụ thuộc thí nghiệm bổ sung được đánh dấu.

1. Trên khung thép tỉ lệ 1:10 với ba đợt đo độc lập và bốn trạng thái liên kết được kiểm soát, thêm cảm biến **không** cải thiện đơn điệu: cấu hình 8 kênh `s13` đạt macro-F1 cao hơn cấu hình 12 kênh `s123` ở CP2_21 (0,9657 so với 0,9575).
2. Biên độ hiệu năng **giữa các tổ hợp cùng số lượng cảm biến** lớn ngang hoặc lớn hơn biên độ **giữa các số lượng cảm biến**, cho thấy thành phần tổ hợp chi phối mạnh hơn số lượng.
3. Cấu hình đạt trung bình cao có thể có sàn run-level rất thấp: `cp3_s12` có trung bình 0,3925 nhưng một fold rơi xuống 0,050, nên trung bình không phải là tóm tắt an toàn.
4. Thứ hạng các tổ hợp cảm biến **không lặp lại giữa các đợt đo**: tổ hợp tốt nhất quan sát được là `s12` ở CP1, `s13` ở CP2_21 và `s123` ở CP3. `[CẦN IT BỔ SUNG: rank-consistency statistic (Kendall W / Spearman) giữa CP2_21 và CP3 với permutation-based p, tính trên 7 cấu hình chung, có block theo run]`
5. `[CẦN IT BỔ SUNG: highlight về sensor-dropout tại inference — mức suy giảm khi một cảm biến mất trên mô hình đã huấn luyện với đủ ba cảm biến, so với mô hình được huấn luyện lại chỉ với hai cảm biến]`

---

## 3. ABSTRACT (có cấu trúc, để trống số liệu chưa có)

> **Bối cảnh.** Giám sát dựa trên dao động cho kết cấu thép thường được đánh giá với một cấu hình cảm biến cố định, trong một đợt đo duy nhất. Khi giảm số cảm biến để triển khai thực tế, câu hỏi thường được đặt là "bao nhiêu cảm biến là đủ", nhưng câu hỏi đó giả định ngầm rằng hiệu năng của một cấu hình là một đại lượng ổn định và có thể xếp hạng.
>
> **Mục tiêu.** Nghiên cứu này định lượng mức giữ lại hiệu năng (performance retention), lợi ích biên và độ ổn định ở cấp run của các cấu hình cảm biến rút gọn, dưới một protocol đánh giá run-aware, leakage-controlled cố định, nhằm tách ảnh hưởng của **số lượng** cảm biến khỏi ảnh hưởng của **thành phần tổ hợp** cảm biến.
>
> **Phương pháp.** Một khung thép tỉ lệ 1:10 với bốn trạng thái liên kết được kiểm soát (Healthy, B1, B2, B3) được đo trong ba đợt đo độc lập; mỗi đợt gồm sáu run độc lập và 72 recording (18 recording mỗi lớp). CP1 có hai cảm biến (cấu hình S1, S2, S12); CP2_21 và CP3 có ba cảm biến (cấu hình S1, S2, S3, S12, S13, S23, S123). Mỗi cảm biến đóng góp bốn kênh tín hiệu. Mọi cấu hình được đánh giá bằng cùng một kiến trúc ResNet1D cố định, cùng siêu tham số, trên cùng 30 hoán vị leave-one-run-out (4 run huấn luyện / 1 run kiểm định / 1 run kiểm tra), với metric ở cấp recording. `[CẦN IT BỔ SUNG: số seed sau khi chạy lại; pipeline thứ hai dùng làm trục robustness]`. **Run là đơn vị thực nghiệm**; các hoán vị fold, seed và window không được coi là quan sát độc lập. Mức giữ lại hiệu năng, ΔF1 và lợi ích biên được tính **theo từng held-out run có ghép cặp** giữa các cấu hình.
>
> **Kết quả.** Trong hai đợt đo có chế độ phân biệt mạnh (CP1, CP2_21), các cấu hình rút gọn giữ lại phần lớn hiệu năng của cấu hình đầy đủ: `cp2_s1` (một cảm biến, 4 kênh) đạt macro-F1 0,9254 ± 0,0681 so với 0,9575 ± 0,0576 của `cp2_s123`. `[CẦN IT BỔ SUNG: tỷ lệ retention có ghép cặp theo run, kèm khoảng dao động run-level]`. Thêm cảm biến không cải thiện đơn điệu: `cp2_s13` (8 kênh) đạt 0,9657 ± 0,0427, cao hơn giá trị quan sát của `cp2_s123`; ở CP3, `cp3_s3` (4 kênh) đạt 0,5129 ± 0,1478 so với `cp3_s12` (8 kênh) đạt 0,3925 ± 0,1983. Biên độ giữa các cấu hình trong một đợt đo là 0,128 (CP1), 0,070 (CP2_21) và 0,166 (CP3); riêng ở CP3, biên độ này cùng bậc với độ lệch chuẩn giữa các fold (0,12–0,20) nên không tách được khỏi nhiễu. Thứ hạng cấu hình không lặp lại giữa các đợt đo. `[CẦN IT BỔ SUNG: kết quả paired test có block theo run; kết quả rank-consistency; kết quả multi-seed; kết quả pipeline thứ hai; kết quả sensor-dropout]`
>
> **Kết luận.** `[CHƯA ĐỦ BẰNG CHỨNG ĐỂ KẾT LUẬN — chỉ được viết sau khi có multi-seed và paired run-level analysis]`. Phát biểu tối đa được phép ở trạng thái hiện tại: trong phạm vi phòng thí nghiệm đã đánh giá, hiệu năng của một cấu hình cảm biến rút gọn phụ thuộc vào thành phần tổ hợp và vào đợt đo ít nhất ngang bằng với phụ thuộc vào số lượng cảm biến, và một cấu hình có trung bình cao không đảm bảo sàn hiệu năng cao ở mọi run.

**Từ khóa đề xuất:** vibration-based condition monitoring; sensor configuration; sensor ablation; performance retention; leave-one-run-out evaluation; run-aware evaluation; scaled steel frame; reduced instrumentation.

---

## 4. INTRODUCTION

### 4.1 Practical problem (đoạn 1–2)

- Trong giám sát dao động cho kết cấu thép, số lượng và vị trí cảm biến là quyết định thiết kế phải chốt **trước** khi có dữ liệu.
- Câu hỏi vận hành thực tế không phải "cấu hình nào tối ưu" mà là: **nếu buộc phải giảm số cảm biến, mất bao nhiêu, và mất ở đâu**.
- Câu hỏi này chỉ trả lời được nếu hiệu năng của cấu hình là đại lượng **ổn định và có thể tái lập**. Bài này kiểm tra chính giả định đó.
- `[CẦN TÁC GIẢ BỔ SUNG: 2–3 câu về bối cảnh ứng dụng cụ thể mà nhóm hướng tới — loại kết cấu, quy mô, ràng buộc lắp đặt — viết ở mức lab-scoped, không claim field]`

### 4.2 Literature gap (đoạn 3–5)

Khung gap gồm bốn tầng, mỗi tầng cần citation thật:

| Tầng | Nội dung gap | Trạng thái citation |
|---|---|---|
| G1 | Sensor placement/selection trong SHM chủ yếu dựa trên tiêu chí mô hình (modal-based: EFI, MAC, information entropy) hoặc tối ưu hóa, ít khi dựa trên hiệu năng **phân loại thực nghiệm** đo dưới protocol chống rò rỉ | `[CẦN TRÍCH DẪN: các nghiên cứu optimal sensor placement modal-based tiêu biểu + các review gần đây]` |
| G2 | Các nghiên cứu sensor-ablation dựa trên học máy trong SHM thường đánh giá trên **một** đợt đo và báo cáo trung bình gộp, không tách biến thiên run-level | `[CẦN TRÍCH DẪN: các nghiên cứu ablation cảm biến dùng ML/DL trong SHM]` |
| G3 | Vấn đề rò rỉ dữ liệu và phân chia không tôn trọng nhóm (grouped/leave-one-session-out) đã được cảnh báo trong ML nói chung và SHM nói riêng, nhưng hiếm khi được áp dụng **cho câu hỏi cấu hình cảm biến** | `[CẦN TRÍCH DẪN: literature về data leakage, grouped CV, leave-one-session-out trong SHM]` |
| G4 | **Chưa có nghiên cứu nào kiểm tra tính tái lập của chính bảng xếp hạng cấu hình cảm biến giữa các đợt đo độc lập.** Đây là gap trung tâm của bài | `[CẦN TÁC GIẢ BỔ SUNG: xác nhận gap này sau khi rà lại thư viện Zotero/Living Evidence Base; nếu tìm thấy tiền lệ thì phải hạ cấp N1]` |

> **Cảnh báo bắt buộc trước khi viết Introduction:** G4 là claim về *sự vắng mặt* trong literature. Không được viết "chưa có nghiên cứu nào" nếu chưa rà soát có hệ thống. Nếu chưa rà soát, viết dạng bảo thủ: "Theo hiểu biết của chúng tôi, và trong phạm vi các nghiên cứu được rà soát ở Mục 2, …".

### 4.3 Đóng góp (contributions) — liệt kê 4 gạch đầu dòng

1. Một **paired run-level retention framework** để định lượng mức giữ lại hiệu năng của cấu hình rút gọn, trong đó run là đơn vị thực nghiệm và mọi so sánh được ghép cặp trên cùng held-out run.
2. Bằng chứng thực nghiệm rằng **thành phần tổ hợp cảm biến chi phối ít nhất ngang bằng số lượng**, kèm ví dụ phản chứng cụ thể cho giả thiết đơn điệu.
3. Một **tiêu chí kép (retention + run-level floor)** thay cho khái niệm "số cảm biến tối thiểu", kèm ví dụ cấu hình có trung bình cao nhưng sàn thấp.
4. Bằng chứng về **tính không tái lập của thứ hạng cấu hình giữa các đợt đo độc lập**, và hệ quả phương pháp luận: một nghiên cứu sensor selection dựa trên một đợt đo không đủ để suy ra thiết kế đo.

### 4.4 Ranh giới phát biểu (đặt cuối Introduction, bắt buộc)

> Nghiên cứu này giới hạn ở việc phân biệt các **trạng thái liên kết được kiểm soát** của một mẫu thí nghiệm trong phòng, dưới một protocol đánh giá đã nêu. Nghiên cứu này không thực hiện chẩn đoán hư hỏng, không suy ra mức độ hư hỏng, không đánh giá khả năng chuyển giao sang công trình thực, và không đưa ra khuyến nghị về vị trí đặt cảm biến tối ưu.

---

## 5. RELATED WORK và CLOSEST-LITERATURE COMPARISON MATRIX

### 5.1 Cấu trúc Related Work (đề xuất 4 tiểu mục)

- **2.1** Sensor placement và sensor selection trong giám sát dao động — nhánh modal/optimization.
- **2.2** Ablation cảm biến trong SHM dựa trên học máy — nhánh data-driven.
- **2.3** Giao thức đánh giá tôn trọng nhóm (run/session/subject) và rò rỉ dữ liệu.
- **2.4** Tính tái lập và độ ổn định của kết luận thực nghiệm dưới biến thiên đợt đo.

> Lưu ý ranh giới: **không** viết tiểu mục về domain shift/transfer learning như một đóng góp — đó là lõi Paper 1. Ở đây chỉ được nhắc một câu, có trích dẫn chéo Paper 1, để định vị.

### 5.2 Comparison matrix dự kiến (Table 2 của manuscript)

Đây là bảng để reviewer thấy ngay bài này khác gì. Toàn bộ ô nội dung để trống chờ rà soát thư viện.

| Nghiên cứu | Đối tượng kết cấu | Số cảm biến khảo sát | Số đợt đo độc lập | Giao thức chia dữ liệu | Đơn vị thực nghiệm được khai báo | Có báo cáo retention có ghép cặp? | Có kiểm tra tính tái lập của thứ hạng cấu hình? | Metric chính |
|---|---|---|---|---|---|---|---|---|
| `[CẦN TÁC GIẢ BỔ SUNG: nghiên cứu gần nhất #1]` | | | | | | | | |
| `[CẦN TÁC GIẢ BỔ SUNG: nghiên cứu gần nhất #2]` | | | | | | | | |
| `[CẦN TÁC GIẢ BỔ SUNG: nghiên cứu gần nhất #3]` | | | | | | | | |
| `[CẦN TÁC GIẢ BỔ SUNG: nghiên cứu gần nhất #4]` | | | | | | | | |
| `[CẦN TÁC GIẢ BỔ SUNG: nghiên cứu gần nhất #5]` | | | | | | | | |
| **Nghiên cứu này (Paper 1B)** | Khung thép 1:10, 4 trạng thái liên kết kiểm soát | 17 cấu hình trên 3 campaign (1–3 cảm biến; 4/8/12 kênh) | 3 (CP1, CP2_21, CP3), mỗi campaign 6 run độc lập | Leave-one-run-out, 30 hoán vị 4/1/1, không chồng lấn run | **Run** | **Có** | **Có** | Macro-F1 ở cấp recording |

> Tiêu chí chọn 5 nghiên cứu gần nhất: (i) có ablation cảm biến thật, (ii) có dữ liệu thực nghiệm chứ không chỉ mô phỏng, (iii) trong 2019–2026, (iv) có mô tả rõ cách chia dữ liệu. Ưu tiên nguồn đã DOI-verified trong thư viện hiện có.

---

## 6. EXPERIMENTAL PROGRAMME AND DATASET

> **Ranh giới với Paper 1:** phần này chia sẻ *factual experimental description* với Paper 1 chính (cùng specimen, cùng trạng thái, cùng cách đo). Bắt buộc **viết lại hoàn toàn bằng câu chữ mới**, rút gọn hơn Paper 1, và **trích dẫn chéo Paper 1** ngay câu đầu tiên: "Chương trình thí nghiệm đã được mô tả chi tiết trong [Paper 1]; ở đây chỉ tóm tắt các yếu tố cần thiết cho phân tích cấu hình cảm biến."

### 6.1 Mẫu thí nghiệm

`[CẦN TÁC GIẢ BỔ SUNG: mô tả khung thép tỉ lệ 1:10 — kích thước, tiết diện, vật liệu, điều kiện liên kết chân cột, hệ giằng, khối lượng sàn]`

### 6.2 Bốn trạng thái liên kết được kiểm soát

| Nhãn | Trạng thái được kiểm soát | Vị trí liên kết | Thay đổi thực nghiệm | Ranh giới diễn giải |
|---|---|---|---|---|
| Healthy | `[CẦN TÁC GIẢ BỔ SUNG]` | `[CẦN TÁC GIẢ BỔ SUNG]` | `[CẦN TÁC GIẢ BỔ SUNG]` | Không được diễn giải là "không hư hỏng" |
| B1 | `[CẦN TÁC GIẢ BỔ SUNG]` | `[CẦN TÁC GIẢ BỔ SUNG]` | `[CẦN TÁC GIẢ BỔ SUNG]` | Không được diễn giải là mức độ hư hỏng |
| B2 | `[CẦN TÁC GIẢ BỔ SUNG]` | `[CẦN TÁC GIẢ BỔ SUNG]` | `[CẦN TÁC GIẢ BỔ SUNG]` | Không được diễn giải là mức độ hư hỏng |
| B3 | `[CẦN TÁC GIẢ BỔ SUNG]` | `[CẦN TÁC GIẢ BỔ SUNG]` | `[CẦN TÁC GIẢ BỔ SUNG]` | Không được diễn giải là mức độ hư hỏng |

> Bốn nhãn **không** tạo thành thang thứ tự về mức độ. Không dùng từ "severity".

### 6.3 Thiết bị đo và cảm biến — mục quan trọng nhất của Paper 1B

| Hạng mục | Trạng thái bằng chứng | Nội dung |
|---|---|---|
| Số kênh mỗi cảm biến | **Verified** | 4 kênh/cảm biến (`cp*_s1` = 4 kênh; `cp*_s12` = 8; `cp*_s123` = 12), đọc từ `run_info.json → config.data.channels` |
| Ý nghĩa 4 kênh | `[CẦN TÁC GIẢ BỔ SUNG: xác nhận 4 kênh là x, y, z và resultant — hay là cấu trúc khác]` | Cần thiết để diễn giải "kênh" đúng nghĩa vật lý |
| Định danh vật lý S1/S2/S3 | **CHƯA VERIFIED trong artefact** | Tài liệu `sensor_position_permutation_synchronization.md` đề xuất S1 = Apex, S2 = Beam–Column, S3 = Brace, nhưng không artefact nào trong bộ bàn giao ghi nhãn vị trí. `[CẦN IT BỔ SUNG: bổ sung trường sensor_position và channel_order vào manifest.json / run_info.json]` |
| Tính nhất quán thứ tự kênh giữa CP2_21 và CP3 | **CHƯA VERIFIED** | Audit ghi rõ đây là "live suspect". Với Paper 1B đây là **điều kiện tiên quyết** cho RQ-B5 |
| Sự cố hoán vị định danh cảm biến ở CP1 | **Đã ghi nhận** | 21/72 file CP1 từng bị hoán vị định danh và đã được phát hiện/sửa. `[CẦN TÁC GIẢ BỔ SUNG: mô tả quy trình phát hiện, sửa và kiểm chứng — đây là nội dung nên đưa vào Methods hoặc Supplementary vì nó củng cố tính hợp lệ của toàn bộ phân tích composition]` |
| Kích thích | `[CẦN TÁC GIẢ BỔ SUNG: BEAT_L1, BEAT_L2, WN — mô tả]` | Không có trường excitation trong artefact đầu ra → hiện **không** stratify được theo loại kích thích |
| Tần số lấy mẫu, cửa sổ | Cửa sổ **verified** = 400 mẫu | `[CẦN TÁC GIẢ BỔ SUNG: sampling rate; số window mỗi recording — trường windows_per_recording đang null]` |

### 6.4 Cấu trúc đợt đo, run và recording — Table 1 của manuscript

| Campaign | Dataset canonical | Run độc lập | Recording duy nhất | Recording/lớp | Cảm biến | Cấu hình được đánh giá | Ghi chú |
|---|---|---|---|---|---|---|---|
| CP1 | `cp1` | 6 (R1–R6) | 72 | 18 | 2 | S1, S2, S12 | — |
| CP2 | **CP2_21 (canonical)** | 6 (R7–R12) | 72 | 18 | 3 | S1, S2, S3, S12, S13, S23, S123 | Cả bốn lớp cùng một phiên đo 21/07 → không có class-aligned session confound |
| CP3 | `cp3` | 6 (R13–R18) | 72 | 18 | 3 | S1, S2, S3, S12, S13, S23, S123 | — |

**Về CP2_2122:** nhánh này ghép Healthy/B1/B2 từ phiên 22/07 với B3 mượn từ phiên 21/07, nên toàn bộ lớp B3 đến từ một phiên đo khác. Đây là confound gắn với **lớp**, không phải với run, nên LORO về mặt cấu trúc không kiểm soát được. Paper 1B **chỉ dùng CP2_21**; CP2_2122 chỉ được nhắc một câu trong mục data governance để giải thích lý do loại, và tuyệt đối không dùng để tạo bất kỳ con số headline nào. Lý do loại là **experimental validity**, không phải accuracy.

### 6.5 Đơn vị thực nghiệm — mục bắt buộc, đặt riêng thành một tiểu mục

Đây là mục sẽ được reviewer soi kỹ nhất. Nội dung bắt buộc:

```text
Đơn vị thực nghiệm độc lập        = run  (6 mỗi campaign)
Đơn vị quan sát cấp dưới          = recording (72 mỗi campaign, 12 mỗi run)
Đơn vị quan sát cấp dưới nữa      = window (400 mẫu)

30 hoán vị LORO  ≠  30 thí nghiệm độc lập
Mỗi run được làm test run đúng 5 lần trong 30 hoán vị.
30 fold × 12 recording = 360 quyết định phân loại,
KHÔNG PHẢI 360 recording độc lập.
Đúng: 72 recording duy nhất × 5 lần đánh giá lặp lại.

seed  ≠  mẫu độc lập
window ≠ mẫu độc lập
permutation ≠ mẫu độc lập
```

Mọi test thống kê trong bài phải **block theo run**. Xem Mục 7.3.

---

## 7. METHODOLOGY

### 7.1 Giao thức đánh giá run-aware (mô tả như **control**, không phải đóng góp)

> Câu mở bắt buộc: "Giao thức leakage-safe run-aware sử dụng ở đây đã được thiết lập và kiểm định trong [Paper 1]; trong nghiên cứu này nó được giữ nguyên và cố định, đóng vai trò biến kiểm soát để cô lập ảnh hưởng của cấu hình cảm biến."

Table 3 của manuscript — mô tả gọn, mỗi dòng một cơ chế:

| Thành phần | Giao thức | Lý do chống rò rỉ |
|---|---|---|
| Phân chia | 30 hoán vị duy nhất: 4 run huấn luyện / 1 run kiểm định / 1 run kiểm tra, rời nhau từng đôi | Window của cùng một recording không thể nằm ở hai phía; run được ép rời nhau ở mức mã nguồn |
| Tiền xử lý | Chuẩn hóa từng window, từng kênh (instance normalisation), không ước lượng thống kê trên tập gộp | Không có tham số nào được fit trên train rồi rò sang test |
| Chọn đặc trưng / augmentation | Không có | Không có đường rò |
| Chọn mô hình | Checkpoint chọn theo loss trên **run kiểm định**, kèm ràng buộc balanced accuracy > mức ngẫu nhiên | Run kiểm tra không tham gia huấn luyện hay chọn mô hình |
| Tổng hợp metric | Trung bình softmax theo window của mỗi recording, rồi argmax | Metric ở **cấp recording**, đồng nhất cho mọi cấu hình |
| Kiểm tra nhất quán nhãn | Báo lỗi nếu một recording mang nhãn window mâu thuẫn | Đã verified, chưa từng kích hoạt |

**Biến được giữ cố định trong toàn bộ Paper 1B:** kiến trúc (ResNet1D, `n_feature_maps` = 16), learning rate 3e-4, weight decay 3e-2, batch 64, epochs 100, cửa sổ 400 mẫu, cùng 30 `split_id`, cùng quy tắc tổng hợp.
**Biến duy nhất được thay đổi:** tập cảm biến (và do đó số kênh đầu vào).

`[CẦN IT BỔ SUNG: xác nhận cấu hình siêu tham số trên vẫn giữ nguyên khi chạy lại multi-seed và pipeline thứ hai]`

### 7.2 Định nghĩa các đại lượng (đây là phần "phương pháp" thật của Paper 1B)

Ký hiệu: với campaign $c$, cấu hình $k$, held-out run $r \in \{1,\dots,6\}$, gọi $F_{c,k,r}$ là macro-F1 ở cấp recording, **trung bình trên 5 fold có cùng test run $r$**. Cấu hình đầy đủ ký hiệu $k^\ast$ (CP1: `s12`; CP2_21 và CP3: `s123`).

**(a) Performance retention (theo run, có ghép cặp)**

$$R_{c,k,r} = \frac{F_{c,k,r}}{F_{c,k^\ast,r}}$$

Báo cáo: median và khoảng dao động của $R_{c,k,r}$ trên 6 run, **không** báo cáo tỉ số của hai trung bình gộp.

**(b) Delta-F1 (theo run, có ghép cặp)**

$$\Delta_{c,k,r} = F_{c,k,r} - F_{c,k^\ast,r}$$

**(c) Marginal sensor benefit (theo run, có ghép cặp)**

$$\Delta^{(2-1)}_{c,r} = \overline{F}^{\,2\text{-sensor}}_{c,r} - \overline{F}^{\,1\text{-sensor}}_{c,r}, \qquad
\Delta^{(3-2)}_{c,r} = F_{c,\text{s123},r} - \overline{F}^{\,2\text{-sensor}}_{c,r}$$

trong đó $\overline{F}^{\,m\text{-sensor}}_{c,r}$ là trung bình trên các tổ hợp cùng số lượng $m$, tính riêng cho từng run $r$.

> **Bắt buộc báo cáo kèm:** biên độ *trong nhóm* (giữa các tổ hợp cùng $m$) cạnh biên độ *giữa các nhóm*. Nếu biên độ trong nhóm ≥ biên độ giữa các nhóm thì việc trung bình theo số lượng cảm biến là một phép tóm tắt gây hiểu nhầm, và phải nói thẳng điều đó.

**(d) Run-level robustness**

- $\text{Floor}_{c,k} = \min_r F_{c,k,r}$ (sàn theo held-out run)
- $\text{MinFold}_{c,k} = \min_{\text{fold}} F$ (fold thấp nhất, để lộ trường hợp sụp đổ đơn lẻ)
- $\text{Spread}_{c,k} = \max_r F_{c,k,r} - \min_r F_{c,k,r}$

**(e) Class-specific retention**

Với mỗi lớp $y$, tính F1 riêng lớp từ `predictions.json` theo từng fold, rồi $R^{(y)}_{c,k,r}$ như (a). Mục tiêu: kiểm tra xem việc rút gọn cảm biến có tấn công chọn lọc vào ranh giới Healthy↔B1 hay không.

**(f) Rank consistency**

- Trong một campaign: tương quan hạng của các cấu hình giữa **các held-out run** (hạng có ổn định khi đổi run không?).
- Giữa các campaign: tương quan hạng giữa CP2_21 và CP3 trên 7 cấu hình chung.
- Giữa các pipeline: tương quan hạng giữa ResNet1D và pipeline thứ hai. `[phụ thuộc thí nghiệm bổ sung E2]`

> Với $n = 7$ cấu hình và $n = 6$ run, power rất thấp. Bắt buộc báo cáo dưới dạng **mô tả + permutation-based reference distribution**, và ghi rõ giới hạn power. Không dùng ngưỡng p = 0,05 như một phán quyết.

**(g) Dual-criterion sufficiency (thay cho "bao nhiêu cảm biến là đủ")**

Một cấu hình rút gọn $k$ được gọi là **đủ theo tiêu chí đã đặt trước** đối với campaign $c$ khi và chỉ khi **cả hai** điều kiện sau đồng thời đúng:

```text
(i)  median_r  R(c,k,r)  ≥  τ_retention
(ii) Floor(c,k)          ≥  τ_floor
```

`[CẦN TÁC GIẢ BỔ SUNG: giá trị τ_retention và τ_floor, kèm lập luận vì sao chọn — phải đặt TRƯỚC khi nhìn kết quả, và phải có cơ sở vận hành, không phải chọn cho vừa số liệu]`

> **Ngôn ngữ bắt buộc:** luôn viết "đủ **theo tiêu chí đã đặt trước** trong **campaign này**", không bao giờ viết "đủ" trần trụi. Đây là điều tách phát biểu này khỏi "minimum sensor requirement".

### 7.3 Xử lý thống kê — mục sống còn

Bắt buộc tuân thủ:

1. **Đơn vị phân tích là run.** Mọi so sánh giữa hai cấu hình được thực hiện trên 6 giá trị ghép cặp $F_{c,k,r}$, không phải trên 30 fold và tuyệt đối không phải trên 360 quyết định.
2. **Không dùng test giả định độc lập trên fold.** Nếu dùng paired test trên 30 fold, phải là permutation test có **block theo test run** (hoán vị nhãn cấu hình trong từng khối run), và phải nói rõ.
3. Với $n = 6$ run, paired Wilcoxon signed-rank có p nhỏ nhất khả dĩ là 1/32 ≈ 0,031 (two-sided). **Ghi rõ giới hạn này trong Methods.** Không được trình bày p ≈ 0,03 như bằng chứng mạnh.
4. **Ưu tiên effect size + khoảng dao động quan sát được hơn p-value.** Báo cáo paired difference theo từng run dưới dạng bảng đầy đủ 6 dòng, để reviewer tự đọc.
5. **Bước lượng tử của metric:** mỗi fold chỉ có 12 recording, nên macro-F1 dịch chuyển theo bước ≈ 1/12 = 0,083. Mọi chênh lệch nhỏ hơn bước này giữa hai cấu hình trên một fold đơn lẻ là **không phân giải được**. Ghi rõ trong Methods.
6. **Seed variance.** Audit 19.08 ghi seed SD = 0,065, lớn hơn split SD = 0,054. Cho tới khi có multi-seed, mọi chênh lệch dưới ≈ 0,13 macro-F1 giữa hai cấu hình **không được phát biểu là khác biệt**. `[CẦN IT BỔ SUNG: seed SD tính lại từ kết quả multi-seed mới]`
7. **Đa so sánh.** CP2_21 và CP3 mỗi campaign có 7 cấu hình → 21 cặp. Phải khai báo trước cặp nào là primary comparison (đề xuất: mỗi cấu hình rút gọn so với cấu hình đầy đủ, tức 6 cặp/campaign) và coi phần còn lại là exploratory.

`[CHƯA ĐỦ BẰNG CHỨNG ĐỂ KẾT LUẬN — không viết bất kỳ p-value, CI hay phát biểu "khác biệt có ý nghĩa" nào cho đến khi các phân tích ở Mục 8.3 được IT thực hiện]`

### 7.4 Vai trò của pipeline thứ hai — khai báo rõ để không thành model comparison

> Câu bắt buộc trong Methods: "Pipeline phân tích thứ hai được đưa vào **không** nhằm so sánh mô hình. Nó được sử dụng như một **trục kiểm tra tính bền vững** của kết luận về cấu hình cảm biến: nếu thứ hạng và mức retention của các cấu hình thay đổi khi đổi pipeline, thì các kết luận về cấu hình không phải thuộc tính của bộ cảm biến. Không có phát biểu nào về ưu thế của một mô hình được đưa ra, và các pipeline không được tinh chỉnh siêu tham số dưới một ngân sách chung."

Trong Results, kết quả pipeline thứ hai chỉ được trình bày dưới dạng **tương quan hạng và dấu của Δ**, không phải bảng xếp hạng hiệu năng.

---

## 8. RESULTS

### 8.1 Kết quả ĐÃ CÓ và ĐÃ ĐƯỢC AUDIT (dùng trực tiếp)

Nguồn: `loro-each-sensor-v1/sensor_loro_batch64_v1/`, ResNet1D `resnet1D-843fbf2`, 30 LORO fold, seed 42, metric ở cấp recording. Toàn bộ 510/510 run có mặt trên đĩa (không có survivorship bias).

**Bảng R1 — Kết quả ablation cảm biến (số liệu verified, sắp theo campaign rồi theo trung bình quan sát được)**

| CP | Cấu hình | Kênh | Macro-F1 (mean ± SD, 30 fold) | Balanced Acc. | Fold thấp nhất | Fold cao nhất | Run yếu nhất (F1 trung bình của run đó) | Số fold đạt F1 = 1,000 | Tỉ số trung bình so với cấu hình đầy đủ *(mô tả, chưa ghép cặp)* |
|---|---|---|---|---|---|---|---|---|---|
| CP1 | s12 (đầy đủ) | 8 | 0,9429 ± 0,0520 | 0,9444 ± 0,0505 | 0,829 | 1,000 | R1 (0,914) | 12/30 | 1,000 |
| CP1 | s1 | 4 | 0,9316 ± 0,0520 | 0,9333 ± 0,0509 | 0,829 | 1,000 | R2 (0,864) | 9/30 | 0,988 |
| CP1 | s2 | 4 | 0,8150 ± 0,0596 | 0,8111 ± 0,0654 | 0,748 | 0,914 | R5 (0,769) | 0/30 | 0,864 |
| CP2_21 | s123 (đầy đủ) | 12 | 0,9575 ± 0,0576 | 0,9583 ± 0,0569 | 0,829 | 1,000 | R11 (0,897) | 18/30 | 1,000 |
| CP2_21 | s13 | 8 | 0,9657 ± 0,0427 | 0,9667 ± 0,0415 | 0,914 | 1,000 | R11 (0,914) | 18/30 | 1,009 |
| CP2_21 | s12 | 8 | 0,9346 ± 0,0764 | 0,9361 ± 0,0748 | **0,731** | 1,000 | R12 (0,883) | 14/30 | 0,976 |
| CP2_21 | s23 | 8 | 0,9270 ± 0,0585 | 0,9306 ± 0,0540 | 0,812 | 1,000 | R9 (0,911) | 9/30 | 0,968 |
| CP2_21 | s1 | 4 | 0,9254 ± 0,0681 | 0,9278 ± 0,0647 | 0,720 | 1,000 | R11 (0,875) | 10/30 | 0,966 |
| CP2_21 | s2 | 4 | 0,9021 ± 0,0741 | 0,9056 ± 0,0717 | 0,748 | 1,000 | R8 (0,860) | 7/30 | 0,942 |
| CP2_21 | s3 | 4 | 0,8957 ± 0,0595 | 0,9000 ± 0,0554 | 0,732 | 1,000 | R12 (0,861) | 3/30 | 0,935 |
| CP3 | s123 (đầy đủ) | 12 | 0,5384 ± 0,1763 | 0,5722 ± 0,1677 | 0,196 | 0,838 | R16 (0,350) | 0/30 | 1,000 |
| CP3 | s13 | 8 | 0,5277 ± 0,1646 | 0,5667 ± 0,1425 | 0,167 | 0,833 | R16 (0,306) | 0/30 | 0,980 |
| CP3 | s3 | 4 | 0,5129 ± 0,1478 | 0,5694 ± 0,1240 | 0,303 | 0,838 | R16 (0,361) | 0/30 | 0,953 |
| CP3 | s23 | 8 | 0,4713 ± 0,1492 | 0,5222 ± 0,1434 | 0,225 | 0,731 | R16 (0,327) | 0/30 | 0,875 |
| CP3 | s1 | 4 | 0,4280 ± 0,1196 | 0,4639 ± 0,1130 | 0,215 | 0,649 | R18 (0,373) | 0/30 | 0,795 |
| CP3 | s12 | 8 | 0,3925 ± 0,1983 | 0,4500 ± 0,1799 | **0,050** | 0,742 | R18 (0,226) | 0/30 | 0,729 |
| CP3 | s2 | 4 | 0,3723 ± 0,1511 | 0,4500 ± 0,1250 | 0,183 | 0,660 | R18 (0,239) | 0/30 | 0,691 |

> **Chú thích bắt buộc dưới bảng:** (1) Cột cuối là **tỉ số của hai giá trị trung bình**, mang tính mô tả; nó **không** phải là mức giữ lại hiệu năng có ghép cặp và **không** được dùng để xếp hạng cấu hình. Giá trị retention chính thức được định nghĩa ở Mục 7.2(a) và báo cáo ở Bảng R2. (2) SD là biến thiên giữa các fold, **không** chứa biến thiên seed; toàn bộ kết quả dùng một seed duy nhất (42). (3) Mức ngẫu nhiên cho bài toán 4 lớp cân bằng là 0,25. (4) Mỗi fold có 12 recording nên bước lượng tử của metric là ≈ 0,083.

**Các phát biểu ĐƯỢC PHÉP từ Bảng R1 ngay bây giờ:**

| # | Phát biểu | Bằng chứng |
|---|---|---|
| P1 | Thêm cảm biến không cải thiện đơn điệu trong dữ liệu này | CP2_21: `s13` (8 kênh) 0,9657 ≥ `s123` (12 kênh) 0,9575. CP3: `s3` (4 kênh) 0,5129 > `s12` (8 kênh) 0,3925 |
| P2 | Biên độ giữa các tổ hợp **cùng số lượng** cảm biến lớn ngang hoặc lớn hơn biên độ giữa các số lượng | CP3, nhóm 2 cảm biến: 0,3925 → 0,5277 (biên độ 0,135). CP2_21, nhóm 1 cảm biến: 0,8957 → 0,9254; nhóm 2 cảm biến: 0,9270 → 0,9657 |
| P3 | Biên độ toàn bộ giữa các cấu hình trong một campaign là 0,128 (CP1), 0,070 (CP2_21), 0,166 (CP3) | Tính trực tiếp từ Bảng R1 |
| P4 | Ở CP3, biên độ giữa các cấu hình **không tách được khỏi nhiễu fold**: SD fold-to-fold của CP3 là 0,12–0,20, cùng bậc với biên độ 0,166 | Cột SD của Bảng R1 |
| P5 | Trung bình cao **không** kéo theo sàn cao | `cp2_s12`: trung bình 0,9346 nhưng fold thấp nhất 0,731 — thấp nhất trong nhóm 8 kênh của CP2_21. `cp3_s12`: trung bình 0,3925 với một fold ở 0,050 |
| P6 | Cấu hình một cảm biến không sụp đổ ở CP1/CP2_21 | `cp2_s1` đạt 0,9254 ± 0,0681 với sàn theo run là R11 = 0,875; `cp1_s1` đạt 0,9316 ± 0,0520 |
| P7 | Thứ hạng cấu hình quan sát được khác nhau giữa ba campaign | Cấu hình cao nhất quan sát được: `s12` (CP1), `s13` (CP2_21), `s123` (CP3) |
| P8 | Kết quả có tính tái lập nội bộ giữa hai lần chạy độc lập | `cp2_s123` cho 0,9575 ở bộ ablation và 0,9547 ở bộ intra-campaign (khác git commit và siêu tham số) → lệch 0,003. `cp1_s12`: 0,9429 vs 0,9400 |

**Các phát biểu KHÔNG được phép từ Bảng R1:**

- ❌ "`s13` tốt hơn `s123`" — chưa có paired run-level analysis; chênh lệch 0,008 nhỏ hơn bước lượng tử 0,083 rất nhiều.
- ❌ "`s1` đủ dùng cho CP2_21" — chưa có τ đặt trước, chưa có multi-seed.
- ❌ Bất kỳ xếp hạng nào trong CP3 — P4 đã loại trừ.
- ❌ Bất kỳ Δ nào nhỏ hơn ≈ 0,13 được gọi là khác biệt — R1 (seed variance) chưa đóng.

### 8.2 Kết quả bổ trợ đã có (dùng làm sensitivity, KHÔNG làm kết quả chính)

**Bộ fixed-split cũ** (`Output_yc4_Sensors/sensor_count_experiments/`, một split cố định, một seed, n = 12/ô):

| Dataset | s1 | s2 | s3 | s12 | s13 | s23 | s123 |
|---|---:|---:|---:|---:|---:|---:|---:|
| cp1 | 0,914 | 1,000 | – | 0,914 | – | – | – |
| cp2_21 | 1,000 | 1,000 | 0,812 | 0,914 | 1,000 | 0,829 | 1,000 |
| cp3 | 0,208 | 0,162 | 0,375 | 0,171 | 0,438 | 0,225 | 0,383 |

Cách dùng đúng trong Paper 1B: đưa vào **Supplementary** như một minh họa **vì sao đánh giá một-split là không đủ**. Đối chiếu trực tiếp: ở bộ một-split, `cp1_s2` = 1,000 và `cp1_s1` = 0,914; ở bộ 30-fold LORO, `cp1_s2` = 0,8150 và `cp1_s1` = 0,9316 — **đảo chiều hoàn toàn**. Đây là một lập luận methodological rất mạnh và hoàn toàn nằm ngoài Paper 1.

> Không dùng bộ fixed-split để tạo bất kỳ con số headline nào. Không dùng các Δ(2−1) và Δ(3−2) tính từ bộ này (−0,043; −0,023; +0,030; +0,086; +0,104) như kết quả — chỉ nhắc trong Discussion như minh chứng về tính bất ổn của thiết kế một-split.

### 8.3 Kết quả CÒN THIẾU — phân loại theo mức nỗ lực

#### Nhóm A — Tính được ngay từ artefact hiện có, KHÔNG cần train lại

| ID | Phân tích | Nguồn dữ liệu | Đầu ra cho manuscript |
|---|---|---|---|
| A1 | Gộp 30 fold về **6 giá trị theo held-out run** cho từng cấu hình ($F_{c,k,r}$) | 17 × `summary/summary.csv`, cột `split_id` + `f1_macro_mean` | Bảng nền cho mọi phân tích còn lại |
| A2 | **Retention có ghép cặp** $R_{c,k,r}$ và $\Delta_{c,k,r}$, báo cáo đủ 6 dòng/cấu hình | A1 | **Bảng R2** (bảng chính của bài) |
| A3 | **Marginal benefit** $\Delta^{(2-1)}_{c,r}$, $\Delta^{(3-2)}_{c,r}$ theo từng run, kèm biên độ trong nhóm | A1 | **Bảng R3** + Figure 4 |
| A4 | **Run-level robustness**: Floor, MinFold, Spread cho từng cấu hình | A1 + 30 fold gốc | **Bảng R4** |
| A5 | **Permutation test có block theo run** cho 6 cặp primary/campaign | A1 | Cột p trong Bảng R2, kèm ghi chú power |
| A6 | **Rank consistency**: hạng cấu hình theo từng run (nội campaign) và giữa CP2_21 ↔ CP3 | A1 | **Bảng R5** + Figure 5 |
| A7 | **Class-specific F1** theo cấu hình, tách 4 lớp | 510 × `predictions.json` | **Bảng R6** + Figure 6 |
| A8 | **Per-recording agreement** giữa các cấu hình trên cùng fold (các cấu hình có sai trên **cùng** recording không?) | 510 × `predictions.json` | Figure 7 — trả lời "thông tin bổ sung hay thông tin trùng lặp" |
| A9 | **Ma trận nhầm lẫn chuẩn hóa** theo cấu hình | `summary/pooled_confusion_*_row_normalized.csv` | Supplementary |
| A10 | Đối chiếu 30-fold LORO với bộ fixed-split cũ | Bảng R1 + Mục 8.2 | Figure S1 (Supplementary) |

> **Đã kiểm chứng tính khả thi:** `summary.csv` của mỗi cấu hình có 30 dòng `aggregate_over = seed`, mỗi dòng mang `split_id` dạng `train7-8-9-10_val11_test12` cùng `f1_macro_mean`, `balanced_accuracy_mean`, `accuracy_mean`, `roc_auc_macro_mean`, `confusion_sum`. `split_id` **khớp nhau giữa các cấu hình**, nên ghép cặp là khả thi 100%. `predictions.json` của mỗi fold có đủ `recording_id`, `true`, `pred`, `probabilities` → A7 và A8 khả thi.

#### Nhóm B — Cần chạy lại, BẮT BUỘC trước khi nộp

| ID | Thí nghiệm | Quy mô | Vì sao bắt buộc |
|---|---|---|---|
| **E1** | **Multi-seed**: toàn bộ 17 cấu hình × 30 fold × ≥3 seed (42, 43, 44; lý tưởng 5 seed) | 510 → ≥1 530 run | Không có ước lượng seed variance thì **không phát biểu được bất kỳ so sánh cấu hình nào**. Launcher đã hỗ trợ `--seeds`. Đây là blocker số 1 |
| **E2** | **Pipeline thứ hai trên toàn bộ lưới 17 cấu hình** — đề xuất `random_forest` (rẻ, và là pipeline mạnh nhất trong bộ hiện có); tùy chọn thêm `1dcnn` làm đối chứng pipeline yếu | 17 × 30 × ≥3 seed cho mỗi pipeline | Trả lời câu hỏi reviewer sẽ hỏi ngay: kết luận về cảm biến có phải thuộc tính của cảm biến hay của riêng ResNet1D. Đây là blocker số 2 |

#### Nhóm C — Nâng bài từ Q3 lên ứng viên Q2 (khuyến nghị mạnh)

| ID | Thí nghiệm | Chi phí | Giá trị |
|---|---|---|---|
| **E3** | **Sensor-dropout tại inference.** Dùng lại checkpoint `s123` đã có (30 fold × 3 campaign), zero-hóa 4 kênh của một cảm biến tại thời điểm test, đo mức suy giảm. So sánh với mô hình **được huấn luyện lại** chỉ với hai cảm biến (`s12`, `s13`, `s23` — đã có sẵn) | **Gần như bằng 0** — không train lại, chỉ chạy inference | Tách hai kịch bản triển khai hoàn toàn khác nhau: *thiết kế với ít cảm biến hơn* vs *một cảm biến hỏng khi đang vận hành*. Không kết quả nào hiện có trả lời được. Hoàn toàn ngoài Paper 1. **Đây là đề xuất có tỉ lệ giá trị/chi phí cao nhất** |
| **E4** | **Channel-matched control** — tách số lượng cảm biến khỏi số kênh đầu vào. Ví dụ: `s123` giới hạn còn 4 kênh (một trục mỗi cảm biến) so với `s1` đủ 4 kênh; hoặc `s12` giới hạn 4 kênh so với `s1` 4 kênh | 17 → thêm ~6 cấu hình × 30 fold × 3 seed | Loại bỏ confound R3. Nếu không làm, mọi "hiệu ứng số cảm biến" đều có thể bị quy về hiệu ứng chiều đầu vào. Đây là điểm reviewer Q2 sẽ bắt |
| **E5** | **Ablation theo trục** (x, y, z, resultant) — đã được yêu cầu trong `yeu_cau_cuoi.md` nhưng **chưa từng chạy** | 3 campaign × 4 trục × 30 fold × 3 seed | Trả lời "thông tin nằm ở cảm biến nào hay ở bậc tự do nào". Bổ sung một chiều mới cho câu hỏi composition |
| **E6** | **Kiểm chứng định danh cảm biến** — chạy permutation-synchronization đã thiết kế trong `sensor_position_permutation_synchronization.md` như một kiểm tra tính hợp lệ dữ liệu, báo cáo Exact Permutation Recovery Rate trên corruption 5–40% | Trung bình, không cần GPU | Điều kiện tiên quyết cho RQ-B5. Đồng thời là một đóng góp phụ về data integrity, và giải thích được sự cố 21/72 file CP1 |

#### Nhóm D — KHÔNG làm trong Paper 1B

| Không làm | Lý do |
|---|---|
| LOCO / cross-campaign classifier transfer làm kết quả chính | Là lõi Paper 1 |
| So sánh kiến trúc mô hình như một kết quả | Sẽ biến bài thành model benchmark; và audit ghi rõ các pipeline chưa được tinh chỉnh dưới ngân sách chung |
| Optimal sensor placement / minimum sensor requirement | Không đủ bằng chứng, và vị trí vật lý chưa verified |
| CEI, BIM, Digital Twin, provenance schema, Evidence Gate, inspection workflow | Thuộc Paper 1 và Gate 2 |
| Bất kỳ phát biểu tiết kiệm chi phí nào | Không có dữ liệu chi phí |

### 8.4 Cấu trúc mục Results của manuscript

- **4.1** Tính đầy đủ của lưới thí nghiệm và tính tái lập nội bộ *(dùng P8)*
- **4.2** Mức giữ lại hiệu năng của cấu hình rút gọn *(Bảng R2, A2)*
- **4.3** Lợi ích biên và so sánh biên độ trong nhóm với giữa nhóm *(Bảng R3, A3)*
- **4.4** Độ ổn định ở cấp run *(Bảng R4, A4)* — nêu rõ `cp2_s12` và `cp3_s12`
- **4.5** Tính nhất quán của thứ hạng cấu hình giữa các run, các campaign và các pipeline *(Bảng R5, A6, E2)*
- **4.6** Hiệu ứng theo lớp *(Bảng R6, A7)*
- **4.7** Sensor-dropout tại inference so với huấn luyện lại với ít cảm biến *(E3)*
- **4.8** Đánh giá theo tiêu chí kép đã đặt trước *(Mục 7.2g)*

---

## 9. DISCUSSION

### 9.1 Số lượng cảm biến so với thành phần tổ hợp

Lập luận chính: nếu số lượng là yếu tố chi phối, thì các tổ hợp cùng số lượng phải cụm lại và các nhóm số lượng phải tách nhau. Dữ liệu cho thấy điều ngược lại ở CP3, và cho thấy tính không đơn điệu ở CP2_21.

Ngôn ngữ được phép:

> "Trong dữ liệu này, việc mô tả hiệu năng theo *số lượng* cảm biến làm mất thông tin: biên độ giữa các tổ hợp có cùng số lượng lớn ngang hoặc lớn hơn biên độ giữa các số lượng. Do đó câu hỏi 'bao nhiêu cảm biến là đủ' không có câu trả lời độc lập với việc *những cảm biến nào*."

Ngôn ngữ **không** được phép: "thành phần quan trọng hơn số lượng" (đây là so sánh định lượng cần paired analysis + multi-seed), "vị trí X mang nhiều thông tin hơn vị trí Y" (định danh vật lý chưa verified).

### 9.2 Retention cao trên một tham chiếu đầy đủ yếu — cảnh báo diễn giải bắt buộc

Đây là mục tinh tế nhất của bài và **phải** có, nếu không reviewer sẽ tự nêu ra.

Ở CP3, `cp3_s3` đạt tỉ số trung bình ≈ 0,95 so với `cp3_s123`. Nhưng `cp3_s123` chỉ đạt 0,5384 ± 0,1763 với mức ngẫu nhiên là 0,25. **Giữ lại 95% của một tham chiếu yếu không phải là một kết quả tốt.** Retention là đại lượng *tương đối*, và nó chỉ có ý nghĩa khi tham chiếu đầy đủ ở trong một chế độ phân biệt được.

Hệ quả bắt buộc đưa vào Methods và Results:

```text
Retention CHỈ được diễn giải khi cấu hình đầy đủ vượt một ngưỡng hiệu năng tuyệt đối
đã đặt trước.  Ở campaign mà cấu hình đầy đủ không vượt ngưỡng đó, retention được
báo cáo nhưng KHÔNG được diễn giải.
```

`[CẦN TÁC GIẢ BỔ SUNG: ngưỡng hiệu năng tuyệt đối cho tham chiếu đầy đủ, đặt trước, kèm lập luận]`

Điều này biến CP3 từ một điểm yếu thành một **đóng góp khái niệm**: nó chứng minh rằng chỉ số retention có thể gây hiểu nhầm nghiêm trọng nếu không kèm điều kiện về tham chiếu.

### 9.3 Độ ổn định ở cấp run và tại sao trung bình là không đủ

- `cp3_s12`: trung bình 0,3925, một fold ở 0,050 — thấp hơn cả mức ngẫu nhiên 0,25 rất xa. Một cấu hình có thể **sụp đổ** trên một run cụ thể.
- `cp2_s12`: trung bình 0,9346 (cao) nhưng fold thấp nhất 0,731 — thấp nhất trong nhóm 8 kênh của CP2_21.
- Hệ quả thực hành: tiêu chí lựa chọn cấu hình phải là **cặp (retention, floor)**, không phải một con số trung bình.

### 9.4 Tính không tái lập của thứ hạng cấu hình giữa các đợt đo

Đây là Discussion trung tâm. Cấu trúc lập luận:

1. Ba campaign đo cùng một specimen, cùng bốn trạng thái, cùng bộ cảm biến danh nghĩa.
2. Thứ hạng cấu hình quan sát được khác nhau giữa ba campaign.
3. **Ba giả thuyết cạnh tranh, tất cả đều phải ghi là hypothesis, not confirmed:**
   - (H1) thứ tự/định danh kênh không nhất quán giữa các campaign → là **giả thuyết rẻ nhất để kiểm tra** và chưa được kiểm tra;
   - (H2) khác biệt vật lý thật giữa các lần lắp đặt lại mẫu;
   - (H3) khác biệt trong chuỗi thu nhận / kích thích.
4. Không phát biểu nhân quả. Dùng cụm **"campaign-associated variability"**, không dùng "session effect caused …".
5. Hệ quả phương pháp luận (đây mới là đóng góp): **một nghiên cứu lựa chọn cấu hình cảm biến dựa trên một đợt đo duy nhất không đủ cơ sở để suy ra thiết kế đo**, kể cả khi nội bộ đợt đo đó có protocol chống rò rỉ hoàn hảo.

> **Ranh giới với Paper 1:** ở đây **không** trình bày kết quả LOCO/cross-campaign classifier transfer. Chỉ được nói một câu: "Sự phụ thuộc campaign của bản thân bộ phân loại đã được báo cáo riêng trong [Paper 1]; ở đây chúng tôi khảo sát một đối tượng khác — tính ổn định của *thứ hạng cấu hình cảm biến* — và không lặp lại phân tích đó."

### 9.5 Hàm ý cho reduced instrumentation — chỉ trong phạm vi phòng thí nghiệm

Được phép viết:

> Trong hai đợt đo có chế độ phân biệt mạnh, các cấu hình rút gọn giữ lại phần lớn hiệu năng quan sát được của cấu hình đầy đủ, với sàn theo run vẫn ở mức cao. `[CẦN IT BỔ SUNG: con số retention có ghép cặp và sàn tương ứng]`. Điều này cho thấy, **trong điều kiện thí nghiệm đã đánh giá**, việc giảm số cảm biến không nhất thiết kéo theo mất khả năng phân biệt tương xứng.

Bắt buộc kèm ngay sau đó:

> Tuy nhiên phát biểu này bị giới hạn bởi ba điều: nó không lặp lại ở đợt đo thứ ba; thứ hạng cấu hình không ổn định giữa các đợt đo; và nghiên cứu này không đánh giá vị trí đặt cảm biến, không đề xuất số cảm biến tối thiểu, và không đưa ra bất kỳ kết luận nào về chi phí hay về công trình thực.

**Cấm tuyệt đối:** "giảm chi phí lắp đặt", "cho phép triển khai với ít cảm biến hơn trong thực tế", "cấu hình tối thiểu".

### 9.6 So sánh với literature

`[CẦN TÁC GIẢ BỔ SUNG: đối chiếu từng phát hiện P1–P7 với các nghiên cứu trong comparison matrix ở Mục 5.2, nêu rõ chỗ đồng thuận và chỗ mâu thuẫn]`

---

## 10. LIMITATIONS

Liệt kê thẳng, không giảm nhẹ:

1. **Một mẫu thí nghiệm duy nhất, tỉ lệ 1:10**, trong phòng, với các trạng thái liên kết được kiểm soát. Không suy rộng sang kết cấu thực.
2. **Sáu run độc lập mỗi campaign** → n = 6 cho mọi test ghép cặp ở cấp run. Power rất thấp; p nhỏ nhất khả dĩ của Wilcoxon signed-rank hai phía là ≈ 0,031.
3. **12 recording mỗi fold** → bước lượng tử của macro-F1 ≈ 0,083.
4. **30 hoán vị LORO không phải 30 thí nghiệm độc lập**; mỗi run làm test run đúng 5 lần.
5. `[CẦN IT BỔ SUNG: nếu E1 chưa xong — "toàn bộ kết quả dùng một seed (42); mọi SD báo cáo là biến thiên giữa các fold, không chứa biến thiên khởi tạo mô hình"]`
6. `[CẦN IT BỔ SUNG: nếu E2 chưa xong — "toàn bộ lưới cấu hình chỉ được đánh giá với một pipeline; chưa biết kết luận có bền vững qua pipeline khác không"]`
7. **Số lượng cảm biến bị lẫn với số kênh đầu vào** (4/8/12 kênh). Chưa có control tách hai yếu tố này. `[phụ thuộc E4]`
8. **Định danh vật lý của S1/S2/S3 chưa được xác nhận từ artefact**; mọi phát biểu là về *nhóm kênh đã ghi*, không phải về *vị trí lắp đặt*. `[phụ thuộc E6]`
9. **Tính nhất quán thứ tự kênh giữa CP2_21 và CP3 chưa được kiểm chứng**, và đây là giả thuyết cạnh tranh chưa loại trừ được cho kết quả rank non-replication.
10. **Không có trường loại kích thích trong artefact đầu ra** → không stratify được theo BEAT_L1 / BEAT_L2 / WN.
11. **Không có bản đồ từ recording ID về file gốc/phiên đo** trong bộ bàn giao → không truy được nguyên nhân vật lý của các run bất thường.
12. Không đánh giá chẩn đoán hư hỏng, mức độ hư hỏng, chuyển giao lab→field, RUL, hay bất kỳ khuyến nghị vị trí đặt cảm biến nào.

---

## 11. CONCLUSIONS

Khung viết (điền sau khi có A1–A8 và E1–E2):

1. Câu 1 — nhắc lại đối tượng: mức giữ lại hiệu năng và độ ổn định của cấu hình cảm biến rút gọn dưới protocol run-aware cố định.
2. Câu 2 — kết quả retention: `[CẦN IT BỔ SUNG]`
3. Câu 3 — kết quả count vs composition: `[CẦN IT BỔ SUNG cho phần định lượng; phần định tính đã có ở P1, P2]`
4. Câu 4 — kết quả robustness ở cấp run: đã có ví dụ định tính (P5), cần con số ghép cặp.
5. Câu 5 — kết quả rank non-replication: `[CẦN IT BỔ SUNG: rank-consistency statistic]`
6. Câu 6 — hàm ý phương pháp luận: đánh giá cấu hình cảm biến phải báo cáo theo run, có ghép cặp, và trên nhiều đợt đo.
7. Câu 7 — ranh giới: phòng thí nghiệm, một mẫu, không phải sensor placement.

`[CHƯA ĐỦ BẰNG CHỨNG ĐỂ KẾT LUẬN — không viết Conclusions cho tới khi Nhóm A và Nhóm B hoàn tất]`

## 12. FUTURE WORK

- Mở rộng sang nhiều đợt đo hơn để kiểm tra tính tái lập của thứ hạng cấu hình với n campaign lớn hơn 3.
- Tách hoàn toàn hiệu ứng số cảm biến khỏi hiệu ứng số kênh và bậc tự do (E4, E5).
- Sensor-dropout và khả năng chịu lỗi cảm biến trong vận hành (E3 mở rộng).
- `[CẦN TÁC GIẢ BỔ SUNG: hướng liên quan tới lộ trình luận án, nhưng KHÔNG nhắc CEI/BIM/Digital Twin trong Paper 1B]`

---

## 13. HỆ THỐNG BẢNG, HÌNH VÀ SUPPLEMENTARY RIÊNG CHO PAPER 1B

### 13.1 Bảng trong bài chính (tối đa 6)

| ID | Tên bảng | Nguồn | Trạng thái | Trùng Paper 1? |
|---|---|---|---|---|
| T1 | Chương trình thí nghiệm: campaign, run, recording, cảm biến, cấu hình được đánh giá | Mục 6.4 | Viết được ngay (cần bổ sung mô tả vật lý) | **Chồng lấn factual** → bắt buộc viết lại câu chữ, rút gọn, trích dẫn chéo |
| T2 | Comparison matrix với literature gần nhất | Mục 5.2 | `[CẦN TÁC GIẢ BỔ SUNG]` | Không |
| T3 | Định nghĩa các đại lượng: retention, ΔF1, marginal benefit, floor, tiêu chí kép | Mục 7.2 | Viết được ngay | Không — **đây là bảng đặc trưng của Paper 1B** |
| T4 | Kết quả ablation đầy đủ 17 cấu hình (mean ± SD, min fold, worst run) | Bảng R1 | **Đã có số liệu** | Paper 1 chỉ đưa bảng rút gọn (Table 5) → Paper 1B đưa bảng đầy đủ + cột robustness. **Phải khác về cột và về mức chi tiết** |
| T5 | Retention và ΔF1 **có ghép cặp theo run**, đủ 6 dòng/cấu hình | A2 | `[CẦN IT BỔ SUNG]` | Không |
| T6 | Rank consistency giữa các run, các campaign và các pipeline | A6, E2 | `[CẦN IT BỔ SUNG]` | Không |

*(Marginal benefit — Bảng R3 — và class-specific — Bảng R6 — đưa Supplementary nếu bài chính quá dài.)*

### 13.2 Hình trong bài chính (tối đa 7)

| ID | Nội dung | Nguồn dữ liệu | Trạng thái | Trùng Paper 1? |
|---|---|---|---|---|
| F1 | Sơ đồ thiết kế: campaign → run → recording → window → phân chia run-aware, và lưới 17 cấu hình cảm biến | Schematic | Vẽ được ngay | Paper 1 có Fig01/Fig02 tương tự → **phải vẽ mới, trục chính là lưới cấu hình, không phải protocol** |
| F2 | Strip/box plot 30 fold macro-F1 cho từng cấu hình, một panel mỗi campaign, có vẽ đường mức ngẫu nhiên 0,25 | Bảng R1 + summary.csv | **Tạo được ngay** | Paper 1 dự kiến có Fig04 sensor configuration → **rủi ro trùng cao**. Xử lý: Paper 1 giữ bar/summary rút gọn; Paper 1B dùng plot theo **từng held-out run** với đường nối ghép cặp |
| F3 | **Paired slope plot**: mỗi held-out run là một đường nối cấu hình đầy đủ → cấu hình rút gọn | A2 | `[CẦN IT BỔ SUNG]` | Không — hình đặc trưng của Paper 1B |
| F4 | Marginal benefit: Δ(2−1) và Δ(3−2) theo từng run, chồng lên biên độ **trong nhóm** cùng số lượng | A3 | `[CẦN IT BỔ SUNG]` | Không |
| F5 | Retention (trục x) so với run-level floor (trục y), mỗi điểm là một cấu hình, có vẽ hai ngưỡng τ | A2 + A4 | `[CẦN IT BỔ SUNG]` | Không — hình minh họa tiêu chí kép |
| F6 | Rank consistency: bump chart thứ hạng cấu hình qua CP2_21 và CP3 (và qua các pipeline) | A6, E2 | `[CẦN IT BỔ SUNG]` | Không — **hình chủ đạo của bài** |
| F7 | Sensor-dropout tại inference so với huấn luyện lại với ít cảm biến | E3 | `[CẦN IT BỔ SUNG]` | Không |

### 13.3 Supplementary Material riêng của Paper 1B

```text
S1  Bảng đầy đủ 17 cấu hình × 30 fold × (mọi seed) — macro-F1, balanced accuracy, accuracy, ROC-AUC
S2  Bảng $F_{c,k,r}$: 17 cấu hình × 6 held-out run
S3  Bảng retention và ΔF1 ghép cặp đầy đủ
S4  Ma trận nhầm lẫn chuẩn hóa cho từng cấu hình
S5  F1 theo từng lớp cho từng cấu hình
S6  Per-recording agreement giữa các cấu hình (A8)
S7  Đối chiếu 30-fold LORO với bộ fixed-split cũ (A10) — minh chứng vì sao một-split không đủ
S8  Siêu tham số, seed, split_id, model version của mọi run
S9  Kết quả kiểm chứng định danh cảm biến (E6)
S10 Kết quả pipeline thứ hai đầy đủ (E2)
S11 Kết quả channel-matched control (E4) và ablation theo trục (E5)
S12 Script tính toán để tái lập mọi bảng và hình từ summary.csv / predictions.json
```

---

## 14. RANH GIỚI PAPER 1 ↔ PAPER 1B (chống redundant publication / self-plagiarism)

### 14.1 Bảng phân định

| Hạng mục | Paper 1 (Buildings) | Paper 1B | Xử lý chống trùng |
|---|---|---|---|
| Câu hỏi trung tâm | Bằng chứng dao động trong phòng có đáng tin và có chuyển giao được giữa campaign không? | Cấu hình cảm biến rút gọn giữ lại bao nhiêu hiệu năng, và mức đó có phải thuộc tính ổn định không? | Hai đối tượng khác nhau |
| Đóng góp chính | Protocol run-aware leakage-safe; cross-campaign transportability; provenance / validated scope | Paired run-level retention framework; count vs composition; dual-criterion sufficiency; rank non-replication | Không chồng lấn |
| LORO / run-aware | **Đóng góp** | **Biến kiểm soát**, trích dẫn Paper 1, không claim mới | Câu khai báo bắt buộc ở Mục 7.1 |
| Cross-campaign classifier transfer | **Kết quả chính** (macro-F1 0,11–0,23, class collapse) | **Không trình bày**; chỉ một câu định vị + trích dẫn chéo | Cấm đưa Table F, Fig 5/6 của Paper 1 |
| Sensor configuration | Một tiểu mục (Table 5, Fig 4) ở mức rút gọn, kết luận "more sensors ≠ always better" | **Toàn bộ bài**, với retention ghép cặp, floor, rank consistency, class-specific, dropout | **Rủi ro cao nhất.** Xử lý ở Mục 14.2 |
| So sánh pipeline/kiến trúc | Có, dưới tên "analytical pipeline", có caveat tuning | Chỉ dùng làm **trục robustness**, không xếp hạng | Khai báo rõ ở Mục 7.4 |
| CEI / provenance / validated scope / Evidence Gate | Có (Discussion 4.4) | **Không nhắc** | Cấm hoàn toàn |
| BIM / Digital Twin / inspection / asset management | Có (Discussion 4.6, 1–2 đoạn) | **Không nhắc** | Cấm hoàn toàn |
| CP2_2122 | Nhắc trong data governance | Nhắc **một câu** trong data governance | Không tạo con số từ nhánh này ở cả hai bài |
| CP3 instability | Finding 3 của Paper 1 | Dùng như **điều kiện biên cho việc diễn giải retention** (Mục 9.2), không lặp lại phân tích nguyên nhân | Góc nhìn khác nhau |
| Bất thường R12 / R16 | Finding 5 của Paper 1 (bằng chứng cho protocol) | Chỉ nhắc khi giải thích floor của cấu hình; **không** lặp lại phân tích run artefact | Cấm lặp lại đoạn phân tích 4-model-cùng-sai |
| Mô tả thí nghiệm | Đầy đủ (2.2–2.5) | Rút gọn + trích dẫn chéo | **Viết lại 100% câu chữ**, không copy câu nào |

### 14.2 Xử lý điểm rủi ro cao nhất — mục sensor configuration của Paper 1

**Vấn đề:** Paper 1 (theo prompt đã khóa) sẽ có Table 5 "Sensor Configuration Results" và Figure 4 "Sensor Configuration Sensitivity", cùng phát biểu "more sensors are not necessarily better" trong Discussion 4.5. Đây chính là hạt nhân của Paper 1B.

**Khuyến nghị bắt buộc — chọn một trong hai:**

- **Phương án A (khuyến nghị mạnh).** Rút gọn tối đa mục sensor configuration trong Paper 1: giữ Table 5 ở mức **3 dòng đại diện mỗi campaign** (đầy đủ / tốt nhất quan sát được / một cảm biến), bỏ Figure 4 hoặc gộp vào Figure 3, và trong Discussion 4.5 chỉ viết **một câu** rằng ảnh hưởng của cấu hình cảm biến được khảo sát chi tiết trong một nghiên cứu riêng, kèm trích dẫn "companion paper, under review". Bảng đầy đủ 17 cấu hình đưa vào Supplementary của Paper 1 **hoặc** bỏ hẳn khỏi Paper 1.
- **Phương án B.** Giữ nguyên Paper 1, nhưng Paper 1B **bắt buộc** phải chứa toàn bộ E1 + E2 + E3, để bài chính không còn phụ thuộc vào Bảng R1 nguyên trạng mà đứng trên dữ liệu multi-seed, multi-pipeline và dropout — tức Bảng R1 hiện tại trở thành một bảng nền, không phải kết quả chính.

> Nếu chọn Phương án B mà **không** làm E1/E2/E3, hai bài sẽ chồng lấn ở mức không chấp nhận được và nguy cơ bị đánh giá là salami publication là thực. Trong trường hợp đó phán quyết chuyển thành `DO NOT SPLIT`.

### 14.3 Quy tắc viết chống self-plagiarism

1. Không copy nguyên văn bất kỳ câu nào từ Paper 1, kể cả trong Materials and Methods. Mô tả thí nghiệm phải được viết lại từ đầu, ngắn hơn, với trọng tâm là cảm biến.
2. Không tái sử dụng bất kỳ bảng hay hình nào của Paper 1. Bảng R1 của Paper 1B phải khác Table 5 của Paper 1 về **cột** (thêm min fold, worst run, số fold đạt 1,000) và về **số dòng**.
3. Trích dẫn Paper 1 ngay trong Introduction, trong Materials and Methods (mô tả thí nghiệm và protocol) và trong Discussion (khi định vị so với cross-campaign transfer). Tối thiểu 3 vị trí.
4. Trong cover letter, khai báo minh bạch quan hệ giữa hai bài và nêu rõ nội dung không chồng lấn. Nếu Paper 1 chưa published, khai báo là "companion manuscript under review" và đính kèm bản thảo.
5. Data Availability Statement của cả hai bài phải trỏ về cùng một bộ dữ liệu, có ghi rõ đây là hai phân tích khác nhau trên cùng bộ dữ liệu.

---

## 15. TẠP CHÍ ĐỀ XUẤT

> **Cảnh báo bắt buộc:** phân hạng quartile thay đổi hằng năm và khác nhau giữa Scopus/SJR và JCR/WoS. Không con số quartile nào dưới đây được coi là đã xác minh. `[CẦN TÁC GIẢ BỔ SUNG: tra cứu quartile hiện hành trên SJR và JCR tại thời điểm nộp, cho từng tạp chí, và ghi lại nguồn]`

### 15.1 Phương án Q3 — ưu tiên

| Xếp hạng ưu tiên | Tạp chí | Nhà xuất bản | Lý do phù hợp | Rủi ro |
|---|---|---|---|---|
| **1** | **Journal of Vibration Engineering & Technologies** | Springer | Scope bao phủ vibration-based monitoring thực nghiệm; chấp nhận nghiên cứu quy mô phòng thí nghiệm với đóng góp phương pháp vừa phải; thân thiện với negative/replication result | `[CẦN TÁC GIẢ BỔ SUNG: xác minh quartile hiện hành]` |
| 2 | **Experimental Techniques** | Springer / SEM | Trọng tâm là kỹ thuật thí nghiệm và thiết kế đo — khớp trực tiếp với câu hỏi cấu hình cảm biến | Scope hẹp hơn về ML; cần giảm trọng số phần deep learning |
| 3 | **Smart Structures and Systems** | Techno-Press | Truyền thống SHM; quen với nghiên cứu mẫu tỉ lệ thu nhỏ | Thời gian phản biện và mức phổ biến thấp hơn |
| 4 | **Structural Monitoring and Maintenance** | Techno-Press | Phù hợp về chủ đề | Chỉ số ảnh hưởng thấp |

### 15.2 Phương án Q2 có thể thử

| Tạp chí | Nhà xuất bản | Điều kiện để thử | Ghi chú |
|---|---|---|---|
| **Sensors** | MDPI | Khớp nhất về chủ đề (cấu hình cảm biến là trọng tâm của tạp chí). **Chỉ thử nếu đã có E1 + E2 + E3** | Cùng nhà xuất bản với Buildings (Paper 1) → phải khai báo companion paper rất rõ trong cover letter |
| **Measurement Science and Technology** | IOP | Cần E4 (channel-matched control) để phần đo lường đủ chặt | Reviewer thiên về đo lường, sẽ soi kỹ định danh cảm biến → cần E6 |
| **Journal of Civil Structural Health Monitoring** | Springer | Cần E1 + E2 + E3 và phần literature review mạnh | Rủi ro: reviewer có thể coi phần trùng với Paper 1 là quá gần |

### 15.3 Chiến lược nộp khuyến nghị

```text
Nếu chỉ hoàn thành Nhóm A (không train lại)     → KHÔNG nộp. Chưa đủ.
Nếu hoàn thành Nhóm A + E1                       → nộp Q3 (ưu tiên #1)
Nếu hoàn thành Nhóm A + E1 + E2                  → nộp Q3 mạnh, hoặc thử Q2 với kỳ vọng vừa phải
Nếu hoàn thành Nhóm A + E1 + E2 + E3             → thử Q2 (Sensors) trước, dự phòng Q3
Nếu thêm E4 + E5 + E6                            → Q2 là mục tiêu hợp lý
```

Thứ tự thời gian khuyến nghị: nộp Paper 1 (Buildings) **trước hoặc đồng thời**, và trong Paper 1B trích dẫn Paper 1 là companion. Không nộp Paper 1B trước, vì Paper 1B dựa vào Paper 1 để khỏi phải trình bày lại protocol.

---

## 16. ĐÁNH GIÁ TỔNG THỂ

```text
GO WITH REVISION
```

**Điều kiện để chuyển thành GO:**

1. Hoàn thành **E1** (multi-seed ≥3 seed cho toàn bộ 17 cấu hình).
2. Hoàn thành **E2** (≥1 pipeline thứ hai trên toàn bộ lưới cấu hình).
3. Hoàn thành **Nhóm A** (A1–A8) — không cần train lại.
4. Chọn và thực thi **Phương án A hoặc B** ở Mục 14.2 để tách khỏi Paper 1.
5. Đặt trước các ngưỡng τ_retention, τ_floor và ngưỡng hiệu năng tuyệt đối của tham chiếu đầy đủ, có lập luận.

**Điều kiện chuyển thành `DO NOT SPLIT`:**

- Nếu Paper 1 giữ nguyên mục sensor configuration đầy đủ **và** Paper 1B không thực hiện được E1/E2/E3. Khi đó nội dung Paper 1B không vượt quá một tiểu mục mở rộng của Paper 1, và nên gộp vào Paper 1 dưới dạng Supplementary thay vì tách bài.

---

## 17. BẢNG TỔNG HỢP TRẠNG THÁI MANUSCRIPT

| Phần bài báo | Đã có | Còn thiếu | Phân tích/mô hình đề xuất | Người thực hiện | Mức ưu tiên |
|---|---|---|---|---|---|
| Title + Highlights | 3 ứng viên title; 4/5 highlight có bằng chứng | Highlight #4 (rank statistic), #5 (dropout) | A6, E3 | Tác giả + IT | Cao |
| Abstract | Khung đầy đủ; số liệu Results cơ bản | Retention ghép cặp, multi-seed, rank statistic, Conclusions | A2, A6, E1 | Tác giả (viết) + IT (số liệu) | Cao |
| 1. Introduction — practical problem | Khung lập luận | Bối cảnh ứng dụng cụ thể của nhóm | — | Tác giả | Trung bình |
| 1. Introduction — literature gap G1–G3 | Khung gap 4 tầng | Toàn bộ citation | Rà soát Zotero / Living Evidence Base | Tác giả | **Rất cao** |
| 1. Introduction — gap G4 (novelty claim) | Phát biểu gap | Xác nhận có hệ thống rằng chưa có tiền lệ | Rà soát có hệ thống, ghi lại quy trình | Tác giả | **Rất cao** |
| 1. Introduction — contributions | 4 đóng góp đã soạn | Điều chỉnh sau khi có E1/E2 | — | Tác giả | Trung bình |
| 2. Related Work | Cấu trúc 4 tiểu mục | Toàn bộ nội dung và citation | — | Tác giả | **Rất cao** |
| 2. Comparison matrix (T2) | Khung bảng + dòng "nghiên cứu này" | 5 nghiên cứu gần nhất | Rà soát literature theo 4 tiêu chí đã nêu | Tác giả | **Rất cao** |
| 3. Experimental — specimen | — | Toàn bộ mô tả vật lý khung thép 1:10 | — | Tác giả | Cao |
| 3. Experimental — trạng thái liên kết (T-states) | Nhãn và ràng buộc diễn giải | Mô tả vật lý 4 trạng thái | — | Tác giả | Cao |
| 3. Experimental — cảm biến và kênh | Số kênh/cảm biến (4) đã verified | Ý nghĩa vật lý 4 kênh; sampling rate; số window/recording; mô tả kích thích | Bổ sung trường vào manifest/run_info | IT + Tác giả | Cao |
| 3. Experimental — định danh S1/S2/S3 | Đề xuất Apex / Beam–Column / Brace (chưa verified) | Xác minh từ registry; kiểm chứng channel order CP2_21 ↔ CP3 | E6 (permutation synchronization) | IT | **Rất cao** (điều kiện tiên quyết cho RQ-B5) |
| 3. Experimental — sự cố 21/72 file CP1 | Đã ghi nhận tồn tại | Quy trình phát hiện, sửa, kiểm chứng | E6 | IT + Tác giả | Cao |
| 3. Experimental — Table 1 | Đã soạn đầy đủ | Chỉ cần viết lại câu chữ khác Paper 1 | — | Tác giả | Trung bình |
| 3. Experimental — đơn vị thực nghiệm | Đã soạn đầy đủ | — | — | Tác giả | Hoàn tất |
| 4. Methods — protocol run-aware (T3) | Đã soạn đầy đủ, có câu khai báo control | Xác nhận siêu tham số khi chạy lại | — | IT xác nhận | Trung bình |
| 4. Methods — định nghĩa retention / ΔF1 / marginal / floor / dual-criterion | Công thức đầy đủ | Giá trị τ_retention, τ_floor, ngưỡng tham chiếu tuyệt đối | Đặt trước, có lập luận | Tác giả | **Rất cao** |
| 4. Methods — thống kê | Quy tắc đầy đủ (block theo run, giới hạn power, bước lượng tử) | Seed SD tính lại sau E1 | E1 | IT | **Rất cao** |
| 4. Methods — vai trò pipeline thứ hai | Câu khai báo đã soạn | Phụ thuộc E2 | E2 | IT | Cao |
| 5. Results 4.1 — tính đầy đủ và tái lập nội bộ | P8 đã verified (lệch 0,003) | — | — | Tác giả | Hoàn tất |
| 5. Results 4.2 — retention (T5, F3) | — | Toàn bộ | **A1, A2** | IT | **Rất cao** |
| 5. Results 4.3 — marginal benefit (F4) | Δ từ bộ fixed-split (chỉ để Supplementary) | Δ ghép cặp theo run từ bộ LORO | **A3** | IT | Cao |
| 5. Results 4.4 — run-level robustness (T4) | Ví dụ định tính (`cp2_s12`, `cp3_s12`) | Floor/MinFold/Spread đầy đủ 17 cấu hình | **A4** | IT | Cao |
| 5. Results 4.5 — rank consistency (T6, F6) | Quan sát định tính (P7) | Statistic + permutation reference | **A6, E2** | IT | **Rất cao** (đây là novelty chính) |
| 5. Results 4.6 — class-specific | — | Toàn bộ | **A7** | IT | Trung bình |
| 5. Results 4.7 — sensor dropout (F7) | — | Toàn bộ | **E3** | IT | Cao (nâng lên Q2) |
| 5. Results 4.8 — dual-criterion | — | Áp dụng τ sau khi đặt trước | A2 + A4 | IT + Tác giả | Cao |
| 5. Results — Bảng R1 (T4 bài chính) | **Đã có đầy đủ, đã audit** | Cập nhật cột SD sau multi-seed | E1 | IT | Cao |
| 5. Results — F2 (strip plot 30 fold) | Dữ liệu đã có | Vẽ hình | Script từ summary.csv | IT | Trung bình |
| 6. Discussion 6.1 — count vs composition | Lập luận + P1, P2, P3 | Định lượng sau paired analysis | A2, A3 | Tác giả | Cao |
| 6. Discussion 6.2 — retention trên tham chiếu yếu | Lập luận đầy đủ + số liệu CP3 | Ngưỡng tham chiếu tuyệt đối | — | Tác giả | **Rất cao** (bắt buộc có) |
| 6. Discussion 6.3 — run-level robustness | P5 đã có | Kết nối với T4 | A4 | Tác giả | Cao |
| 6. Discussion 6.4 — rank non-replication | Khung 5 bước, 3 giả thuyết | Statistic; loại trừ H1 | A6, E6 | Tác giả + IT | **Rất cao** |
| 6. Discussion 6.5 — reduced instrumentation | Ngôn ngữ được phép + cấm | Con số retention và floor | A2, A4 | Tác giả | Cao |
| 6. Discussion 6.6 — so sánh literature | — | Toàn bộ | Rà soát literature | Tác giả | Cao |
| 7. Limitations | 12 mục đã soạn | Cập nhật mục 5, 6, 7, 8 sau E1/E2/E4/E6 | — | Tác giả | Trung bình |
| 8. Conclusions | Khung 7 câu | Toàn bộ nội dung định lượng | Nhóm A + E1 + E2 | Tác giả | Cao (làm cuối) |
| 9. Future Work | 3 hướng | Hướng gắn lộ trình luận án | — | Tác giả | Thấp |
| Bảng T1–T6 | T1, T3, T4 soạn được ngay | T2, T5, T6 | Rà soát + A2 + A6 | Tác giả + IT | Cao |
| Hình F1–F7 | Dữ liệu cho F2 đã có | F1, F3, F4, F5, F6, F7 | Script vẽ + A2/A3/A4/A6 + E3 | IT | Cao |
| Supplementary S1–S12 | Dữ liệu thô cho S1, S4, S7, S8 đã có | S2, S3, S5, S6, S9, S10, S11, S12 | Nhóm A + E2 + E4 + E5 + E6 | IT | Trung bình |
| References | — | Toàn bộ (~35–60) | Rà soát Zotero, xác minh DOI | Tác giả | **Rất cao** |
| Cover letter + khai báo companion paper | Quy tắc ở Mục 14.3 | Nội dung thư | — | Tác giả | Cao |
| Data Availability Statement | — | Nội dung, thống nhất với Paper 1 | — | Tác giả | Trung bình |
| **E1 — multi-seed** | — | 17 cấu hình × 30 fold × ≥3 seed | Launcher đã hỗ trợ `--seeds` | **IT** | **BLOCKING** |
| **E2 — pipeline thứ hai** | — | 17 cấu hình × 30 fold × ≥3 seed | `random_forest` (+ tùy chọn `1dcnn`) | **IT** | **BLOCKING** |
| **E3 — sensor dropout** | Checkpoint `s123` đã có sẵn | Chạy inference với 1 cảm biến bị zero-hóa | Không train lại | **IT** | Cao (nâng Q2) |
| **E4 — channel-matched control** | — | ~6 cấu hình bổ sung × 30 fold × ≥3 seed | Tách số cảm biến khỏi số kênh | IT | Trung bình–cao |
| **E5 — ablation theo trục (x/y/z/resultant)** | Đã được yêu cầu, chưa từng chạy | 3 campaign × 4 trục × 30 fold × ≥3 seed | — | IT | Trung bình |
| **E6 — kiểm chứng định danh cảm biến** | Thiết kế phương pháp đã có | Chạy và báo cáo recovery rate | Permutation synchronization | IT | **Rất cao** |
| Quyết định Phương án A/B (Mục 14.2) | Hai phương án đã soạn | Quyết định của tác giả | — | **Tác giả** | **BLOCKING** |
| Tra cứu quartile tạp chí | Danh sách ứng viên | Xác minh SJR/JCR hiện hành | — | Tác giả | Trung bình |

---

## 18. GHI CHÚ CUỐI

**Mâu thuẫn giữa hai bản yêu cầu đã được xử lý như sau.** Yêu cầu ban đầu ghi "chỉ dùng ResNet1D cố định" và "không so sánh model"; yêu cầu cuối cho phép "đề xuất thêm mô hình AI hoặc baseline nếu thực sự cần thiết". Tài liệu này giữ ResNet1D là pipeline chính và **duy nhất** dùng để tạo mọi con số headline, đồng thời đưa pipeline thứ hai vào **chỉ như một trục kiểm tra tính bền vững**, được trình bày dưới dạng tương quan hạng và dấu của Δ, không phải bảng xếp hạng hiệu năng. Nếu tác giả muốn giữ nguyên ràng buộc gốc tuyệt đối, hãy bỏ E2 — nhưng khi đó cần chuẩn bị trả lời câu hỏi của reviewer rằng kết luận có thể chỉ đúng cho một kiến trúc.

**Ba câu không bao giờ được xuất hiện trong Paper 1B:**

1. "Sensor configuration influences classification reliability more strongly than model architecture." — đã bị chính dữ liệu bác bỏ (hiệu ứng pipeline Δ ≈ 0,34 so với hiệu ứng cảm biến Δ ≈ 0,07 ở CP2_21).
2. "Hai cảm biến là đủ" hoặc bất kỳ biến thể nào của "minimum sensor requirement".
3. Bất kỳ câu nào chứa "optimal sensor placement".
