# CONFERENCE PAPER PLAN — v1.0

**Version:** v1.0
**Issued:** 2026-08-07
**Status:** WORKING PLAN — NOT GOVERNANCE
**Source-of-truth level:** 8 (planning; subordinate to Charter, ACCEPTED ADRs, Evidence Gates, Paper 1 / Paper 2 directions)
**Scope:** Ba bài hội thảo phục vụ mục tiêu *tập viết* và *thu phản biện chuyên gia*, thiết kế để không tiêu thụ đóng góp chính của Paper 1 và Paper 2.
**Không làm gì:** Không bài nào trong file này đóng, mở hay thay đổi trạng thái G1/G2/G3/G4/G5.

---

## 0. Nguyên tắc nền (đọc trước khi viết bất kỳ dòng nào)

### 0.1 Quy tắc chống trùng lặp

> **Tạp chí không kiểm tra trùng phương pháp. Tạp chí kiểm tra trùng kết luận.**

| Thành phần | Được trùng với Paper 1/2 | Bắt buộc phải khác |
|---|---|---|
| Dataset (lát cắt con) | ✅ | — |
| Pipeline, HPO, kiến trúc mô hình | ✅ | — |
| Câu hỏi nghiên cứu | ❌ | ✅ |
| Câu kết luận trong Abstract | ❌ | ✅ |

### 0.2 Câu bắt buộc trong mọi bài (Limitations section)

> *"Results reported here are preliminary and are produced under an internal evidence-gate process that has not been closed. They are presented as evaluation-protocol evidence, not as validated structural diagnosis, and are not transferable to field conditions."*

Bản tiếng Việt cho CP-3:
> *"Kết quả trình bày là kết quả sơ bộ, được tạo ra trong quy trình nghiệm thu bằng chứng nội bộ chưa hoàn tất. Đây là bằng chứng về giao thức đánh giá, không phải kết luận chẩn đoán kết cấu, và không được suy diễn sang điều kiện hiện trường."*

### 0.3 Cấm tuyệt đối trong cả ba bài

- ❌ **Không con số ResNet1D nào** — cho tới khi sensor-mode provenance được chốt (`PAPER1_DIRECTION_AND_GATE` §Immediate blocker).
- ❌ Không claim field diagnosis, lab-to-field transfer, field readiness, predictive maintenance, RUL.
- ❌ Không trình bày CEI hay softmax như scalar Health Index / severity / damage probability / priority.
- ❌ Không dùng từ "validated", "passed", "proven" cho bất kỳ gate nào.
- ❌ Không dùng FEM cho diễn giải hư hỏng (FEM = nominal, uncalibrated, reference-only).

### 0.4 Nghĩa vụ khai báo khi nộp bài tạp chí

Khi nộp Paper 1 cho *Sensors*, cover letter **phải** liệt kê CP-1 và CP-2 kèm mô tả phần mở rộng. Kiểm tra chính sách prior-conference-publication trên trang tạp chí trước khi nộp bài hội thảo đầu tiên.

---

## 1. Dữ liệu — trạng thái đã làm rõ và điểm còn mở

| Đợt (campaign) | Số cảm biến | Ghi chú |
|---|---|---|
| Đợt 1 | 2 | Cấu hình S1, S2, S1+S2 |
| Đợt 2 | 3 | Ghi đồng thời |
| Đợt 3 | 3 | Ghi đồng thời |

**Hệ quả thiết kế quan trọng:** số kênh không đồng nhất giữa đợt 1 và đợt 2–3. Mọi so sánh xuyên đợt phải chọn một trong hai chiến lược, và **phải khai báo rõ trong bài**:

- **Chiến lược A — common-channel subset:** chỉ dùng 2 kênh chung cho cả 3 đợt. Cho phép so sánh xuyên đợt sạch. *Khuyến nghị cho CP-1 và CP-2.*
- **Chiến lược B — full-channel, within-group:** dùng đủ 3 kênh nhưng chỉ trong đợt 2–3. Cho phép trả lời câu hỏi về mật độ cảm biến, nhưng không so sánh được với đợt 1.

### ⚠️ ĐIỂM CẦN LÀM RÕ TRƯỚC KHI CHẠY BẤT KỲ THÍ NGHIỆM NÀO

Cụm từ *"đợt 2 và đợt 3 cùng lúc"* có hai cách hiểu, và hai cách này dẫn tới hai thiết kế đánh giá khác nhau:

- **Cách hiểu 1:** đợt 2 và đợt 3 dùng 3 cảm biến ghi *đồng thời* (3 kênh song song), nhưng hai đợt là hai lần lắp đặt/tháo lắp độc lập.
  → Đợt 2 và đợt 3 **là** hai nhóm độc lập hợp lệ cho LORO.
- **Cách hiểu 2:** đợt 2 và đợt 3 được thu *trong cùng một phiên đo*.
  → Đợt 2 và đợt 3 **không** độc lập; gộp chung thành một nhóm, và số nhóm độc lập thực tế giảm xuống còn 2 chứ không phải 3.

**Bắt buộc:** ghi nhận cách hiểu đúng vào `canonical run registry` **trước** khi chạy LORO. Nếu chọn sai, toàn bộ kết quả LORO của cả Paper 1 lẫn hai bài hội thảo đều mất hiệu lực. Đây là quyết định 30 phút chặn nhiều tháng công việc.

---

## 2. Danh mục ba bài và ánh xạ hội thảo

| Mã | Hội thảo | Thời điểm | Ngôn ngữ | Phụ thuộc |
|---|---|---|---|---|
| **CP-1** | Quốc tế tổ chức trong nước — Miền Tây | Tháng 10/2026 | EN | Cần LORO chạy xong |
| **CP-2** | Quốc tế tổ chức trong nước — Hà Nội | Tháng 12/2026 | EN | Cần CP-1 pipeline + nested HPO |
| **CP-3** | Hội thảo trong nước | Cuối 2026 | VI | **Không phụ thuộc gate nào — viết được ngay** |

---

## 3. CP-1 — Bài mở đường (deadline gần nhất)

### Tiêu đề

**Chính:**
> *Run-Aware versus Random Splitting in Vibration-Based Damage Classification: A Reproducible Evaluation Protocol for a Bolted Steel Frame*

**Phương án thay thế (nhấn thông điệp mạnh hơn):**
> *Does the Split Decide the Result? Quantifying Evaluation Bias in Vibration-Based Damage Classification of a Bolted Steel Frame*

### Câu hỏi nghiên cứu
Trên cùng một bộ dữ liệu và cùng một mô hình, độ chính xác báo cáo thay đổi bao nhiêu khi chuyển từ random window split sang run-aware / leave-one-run-out (LORO)?

### Claim được phép
- Cách chia dữ liệu ảnh hưởng có hệ thống tới hiệu năng báo cáo trên bộ dữ liệu này.
- Random window split cho kết quả lạc quan hơn run-aware split, với biên độ đo được.
- Giao thức run-aware là điều kiện tối thiểu để báo cáo hiệu năng có thể tái lập.

### Claim bị cấm
- ❌ Không so sánh cấu hình cảm biến làm kết luận chính *(đó là headline của Paper 1)*.
- ❌ Không xếp hạng kiến trúc mô hình *(cũng là Paper 1)*.
- ❌ Không con số ResNet1D.

### Thiết kế
- **Dữ liệu:** một đợt duy nhất (khuyến nghị đợt 2 hoặc đợt 3 — 3 kênh, dữ liệu đầy đủ hơn). Nếu dùng nhiều đợt, áp dụng Chiến lược A.
- **Mô hình:** RF + 1D-CNN. Hai mô hình là đủ; mục tiêu là *giao thức*, không phải *xếp hạng mô hình*.
- **Điều kiện so sánh:** (i) random window split; (ii) split-before-windowing; (iii) run-aware/LORO đa seed.
- **Báo cáo:** macro-F1 theo từng fold, kèm min–max hoặc khoảng biến thiên. Không báo cáo một con số đơn lẻ.

### Cấu trúc bài (6 trang)
1. Introduction — vì sao hiệu năng SHM báo cáo trong y văn khó tái lập
2. Related work — leakage trong dữ liệu rung (`M8LMWFQH`, `RG9FMT8Y`, `XE9XS6BQ`, `PEUHYBPS`); tiền lệ khung thép bulông (`YR2NQWE7`)
3. Experimental setup — khung thép 1:10, trạng thái hư hỏng, bố trí cảm biến
4. Evaluation protocols compared — ba điều kiện
5. Results — bảng so sánh + biểu đồ phân tán theo fold
6. Discussion — hàm ý cho việc báo cáo kết quả SHM
7. Limitations — câu bắt buộc §0.2

### Sản phẩm phụ cho luận án
✅ **Pipeline LORO đa seed chạy được** — đây là blocker số 1 của G1. Viết bài này đồng nghĩa với việc bị ép hoàn thành Stream A bước 3.

---

## 4. CP-2 — Bài HPO/AI (bài bạn yêu cầu)

### Tiêu đề

**Chính:**
> *Evidence of Learnability before Deployment: Nested Hyperparameter Optimization and Leakage-Safe Evaluation of 1D-CNN for Vibration-Based Damage Classification*

**Phương án thay thế (thông điệp CEM rõ hơn):**
> *How Much of the Learned Signal Survives Leakage Control? Nested HPO for 1D-CNN on a Multi-Campaign Bolted Steel Frame Dataset*

### Khung lập luận — đây là điểm then chốt

Bạn muốn chứng minh *"AI có thể học được dữ liệu rung động, tạo bằng chứng trước khi áp dụng thực tế"*. Cách đóng khung **an toàn và mạnh hơn** là:

> Chứng minh khả năng học **sau khi đã loại bỏ mọi con đường rò rỉ**, và đo phần hiệu năng còn lại.

Lý do: một kết quả 0.95 chưa kiểm soát leakage không thuyết phục ai. Một kết quả thấp hơn nhưng **sống sót qua LORO** là bằng chứng thật, và chính là loại bằng chứng cần có *trước* khi triển khai hiện trường. Đây cũng là câu chuyện hay hơn để trình bày trước hội trường.

### Câu hỏi nghiên cứu
Sau khi kiểm soát rò rỉ ở cấp run và campaign, mô hình 1D-CNN được tối ưu siêu tham số còn giữ được bao nhiêu khả năng phân biệt trạng thái? Và HPO đóng góp bao nhiêu so với cấu hình mặc định?

### Claim được phép
- Dưới đánh giá leakage-safe, khả năng phân biệt trạng thái vẫn cao hơn mức ngẫu nhiên một cách nhất quán trên các fold.
- HPO cải thiện (hoặc không cải thiện) hiệu năng một lượng đo được, khi được lồng đúng cách bên trong vòng đánh giá.
- Mức hiệu năng leakage-safe này là ngưỡng tham chiếu tối thiểu cần đạt trước khi cân nhắc thử nghiệm hiện trường.

### Claim bị cấm
- ❌ Không claim sẵn sàng triển khai hiện trường (*field readiness*).
- ❌ Không claim kết quả phòng thí nghiệm chuyển giao được sang công trình thật.
- ❌ Không so sánh cấu hình cảm biến làm kết luận chính.
- ❌ Không con số ResNet1D.

### 🔴 Yêu cầu kỹ thuật bắt buộc — HPO lồng (nested)

Đây là chỗ bài này có thể **tự phá hỏng** nếu làm sai:

```
SAI:  HPO trên toàn bộ dữ liệu  →  chọn cấu hình tốt nhất  →  báo cáo LORO
      (selection leakage: cấu hình đã "nhìn thấy" fold test)

ĐÚNG: for mỗi outer fold (LORO):
          tách outer test = 1 run/campaign giữ lại
          HPO chỉ trên inner folds của phần còn lại
          huấn luyện lại với cấu hình thắng
          đánh giá 1 lần trên outer test
      báo cáo phân bố kết quả outer, không phải kết quả tốt nhất
```

Nếu chi phí tính toán quá lớn, giảm không gian tìm kiếm (ví dụ random search 20–30 lượt) chứ **không** giảm tính lồng.

### Thiết kế
- **Dữ liệu:** cả ba đợt theo Chiến lược A (2 kênh chung). Nếu chọn Chiến lược B, giới hạn ở đợt 2–3 và nói rõ.
- **Mô hình:** 1D-CNN (chính) + RF làm baseline.
- **HPO:** random search hoặc Bayesian; ghi rõ không gian tìm kiếm và ngân sách. **Không** dùng metaheuristic (GWO/SAFCA) — thêm lớp công nghệ không cần thiết, không có nguồn nào trong Living Evidence Base hỗ trợ, và làm loãng thông điệp.
- **Baseline đối chiếu:** chance level thực nghiệm qua permutation test (`ZLFATP2Z`, `PZ937I73`). Đây là thứ biến "AI học được" từ khẳng định thành bằng chứng.

### Mục cầu nối QLXD (bắt buộc có — đây là căn cước luận án của bạn)

Một mục ngắn: *"Reporting confidence as inspection metadata"*.
- Chỉ ra softmax **chưa hiệu chuẩn** thì overconfident; minh họa bằng reliability diagram và ECE.
- Kết luận: đầu ra mô hình phải được đóng gói thành **metadata có cấu trúc** — evidence-validity status, confidence basis & scale, run/fold variability, sensor configuration, data-quality status, provenance, timestamp, version — chứ không phải một con số xác suất đưa thẳng cho người quản lý.
- **Nói rõ:** đây *không* phải damage probability, *không* phải Health Index, *không* prescribe hành động.

> Ghi chú an toàn: CEI **không** nằm trong candidate novelty boundary của Paper 2 (`PAPER2_CURRENT_DIRECTION` §3 liệt kê: identities, Status_Event, authorization, verification, closure, mutation/oracle, CQ parity). Trình bày CEI ở mức metadata reporting không tiêu thụ đóng góp của Paper 2.

### Cấu trúc bài (6–8 trang)
1. Introduction — vì sao cần bằng chứng learnability trước khi triển khai
2. Related work — 1D-CNN cho SHM; leakage; HPO
3. Dataset và thiết kế thí nghiệm ba đợt
4. Nested HPO + leakage-safe evaluation protocol
5. Results — hiệu năng theo fold; HPO có / không; permutation baseline
6. Reporting confidence as inspection metadata *(mục cầu nối QLXD)*
7. Discussion — ngưỡng tối thiểu trước khi cân nhắc hiện trường
8. Limitations — câu bắt buộc §0.2

### Ranh giới với CP-1 (phải giữ nghiêm)
| | CP-1 | CP-2 |
|---|---|---|
| Đối tượng nghiên cứu | **Giao thức đánh giá** | **Khả năng học của mô hình** |
| Câu kết luận | "Cách chia dữ liệu quyết định con số báo cáo" | "Tín hiệu học được sống sót qua kiểm soát rò rỉ ở mức X" |
| Vai trò của LORO | Là *biến được so sánh* | Là *điều kiện cố định* |

CP-2 **trích dẫn** CP-1 cho phần giao thức, không lặp lại phân tích đó.

### Sản phẩm phụ cho luận án
✅ Gói bất định run/fold (Stream A bước 5) + không gian HPO đã ghi nhận, dùng lại trực tiếp cho Paper 1.

---

## 5. CP-3 — Bài position tiếng Việt (viết được ngay hôm nay)

### Tiêu đề

**Chính:**
> *Từ bằng chứng tình trạng đến hành động bảo trì: đề xuất khung truy vết có trách nhiệm giải trình cho công trình thép công nghiệp ven biển — báo cáo tiến độ và các vấn đề còn mở*

**Phương án ngắn gọn hơn:**
> *Truy vết bằng chứng — hồ sơ kiểm tra — hành động bảo trì trong quản lý công trình thép công nghiệp: khung đề xuất và năm câu hỏi cần ý kiến chuyên gia*

### Thể loại
**Position / work-in-progress paper.** Đây là thể loại chính danh của hội thảo. Bạn công bố *câu hỏi*, không công bố *đặc tả đã chốt* — nên không có claim nào để vi phạm, và không chẻ Paper 2.

### Nội dung
1. Bối cảnh: công trình thép công nghiệp ven biển, nghĩa vụ hồ sơ kiểm tra – bảo trì
2. Vấn đề: bằng chứng tình trạng và quyết định kiểm tra thường không nối được với nhau để giải trình
3. Chuỗi đề xuất:
   `Condition_Evidence → BIM-linked component → Inspection_Record → Action_Record`
4. **Năm câu hỏi mở gửi hội trường** *(phần quan trọng nhất của bài)*
5. Hướng tiếp theo

### Năm câu hỏi mở — ánh xạ trực tiếp tới `EXPERT_REVIEW_REQUIRED`

| # | Câu hỏi gửi chuyên gia | Mục Decision Register tương ứng |
|---|---|---|
| 1 | Một hồ sơ kiểm tra nên sinh ra bao nhiêu hồ sơ hành động? Có trường hợp 1 kiểm tra → nhiều hành động, hoặc nhiều kiểm tra → 1 hành động không? | Exact Inspection-Action cardinality |
| 2 | Từ vựng vòng đời hành động nào phản ánh đúng thực tế vận hành ở Việt Nam? | Action lifecycle vocabulary |
| 3 | Ai có thẩm quyền phê duyệt, từ chối, yêu cầu làm lại? Có cần tách bạch người thực hiện và người xác nhận không? | Role and permission matrix |
| 4 | Tiêu chí nào xác nhận một hành động bảo trì đã hoàn tất *thật sự*, khác với việc chỉ được đánh dấu "đã xong"? | Exact verification criteria |
| 5 | Khi nào được phép mở lại một hồ sơ đã đóng? Ai quyết định? | Closure/reopen policy |

### Ghi chú bắt buộc trong bài
Nếu đề cập `Status_Event`, phải ghi rõ: *"đang ở trạng thái đề xuất, chưa được chấp thuận (ADR PROPOSED — NOT ACCEPTED)"*.

### Sản phẩm phụ cho luận án
✅ **Biên bản phản hồi chuyên gia** — nộp làm evidence cho G2 expert review. Đây là bài có tỷ lệ giá trị/công sức cao nhất trong cả ba.

**Cách khai thác tối đa:** chuẩn bị sẵn một phiếu ghi ý kiến 5 câu (in ra hoặc QR form), phát tại phiên trình bày. Ghi lại tên, đơn vị, chức danh người trả lời — đó là dữ liệu expert review có thể trích dẫn.

---

## 6. Bài tùy chọn — CP-4 (chỉ sau khi Paper 1 đã nộp)

> *Sensing Cost per Unit of Diagnostic Confidence: An Asset-Management View on Sensor Configuration for Steel-Frame Monitoring*

Khai thác đúng sự bất đối xứng 2 kênh (đợt 1) vs 3 kênh (đợt 2–3). Góc **chi phí** không nằm trong `PAPER1_DIRECTION` §Scope, nên là claim mới thật. **Không viết trước khi Paper 1 nộp** — sẽ trùng headline.

---

## 7. Ma trận chống trùng lặp — kiểm tra trước mỗi lần nộp

| Claim | Paper 1 | Paper 2 | CP-1 | CP-2 | CP-3 |
|---|:---:|:---:|:---:|:---:|:---:|
| Cấu hình cảm biến > kiến trúc mô hình | ✅ độc quyền | — | ❌ | ❌ | — |
| Xếp hạng mô hình (RF/CNN) | ✅ độc quyền | — | ❌ | ❌ | — |
| Split protocol thay đổi kết quả báo cáo | phụ | — | ✅ **chính** | trích dẫn | — |
| Learnability sống sót qua leakage control | phụ | — | — | ✅ **chính** | — |
| Đóng góp của HPO | — | — | — | ✅ **chính** | — |
| Confidence dưới dạng metadata (CEI) | phụ | phụ | — | ✅ mục phụ | — |
| Identity/event/verification/closure chain | — | ✅ độc quyền | — | — | ❌ chỉ đặt câu hỏi |
| Nghĩa vụ quản lý theo pháp luật VN | — | bối cảnh | — | — | ✅ **chính** |

---

## 8. Lộ trình thực thi

### Chặn tất cả: hai việc phải xong trước

| # | Việc | Thời lượng ước tính | Chặn cái gì |
|---|---|---|---|
| **B0** | Chốt cách hiểu "đợt 2 và đợt 3 cùng lúc" → ghi vào canonical run registry | 30 phút | **Tất cả** |
| **B1** | Khóa canonical run registry + sensor identity/provenance | 1–2 ngày | CP-1, CP-2, G1 |

### Trình tự

```
Tuần 1     B0 → B1 → khởi động CP-3 (không phụ thuộc gì)
Tuần 2–3   Chạy LORO đa seed → draft CP-1
Tuần 4     Hoàn thiện CP-1, nộp hội thảo tháng 10
Tuần 4–6   Nested HPO + permutation baseline + calibration
Tuần 7–9   Draft CP-2, nộp hội thảo tháng 12
Song song  Hoàn thiện CP-3, nộp hội thảo trong nước
```

### ⚠️ Kiểm tra deadline trước khi khóa lịch
Chưa xác định được deadline nộp bài của cả ba hội thảo. **Hội thảo tháng 10 nhiều khả năng có deadline trong tháng 8–9**, tức là gấp. Việc đầu tiên trong tuần này: tra deadline chính thức của cả ba hội thảo và điều chỉnh lộ trình trên. Nếu deadline tháng 10 quá gấp so với tiến độ LORO, **đổi CP-3 lên nộp hội thảo tháng 10** (vì CP-3 không phụ thuộc gate nào) và đẩy CP-1 sang tháng 12.

---

## 9. Checklist trước mỗi lần nộp

- [ ] Câu kết luận trong Abstract khác với Paper 1 và Paper 2
- [ ] Không có bất kỳ con số ResNet1D nào
- [ ] Câu bắt buộc §0.2 có trong mục Limitations
- [ ] Không dùng từ "validated" / "passed" / "field-ready" / "proven"
- [ ] Không trình bày CEI hay softmax như một con số đơn lẻ để ra quyết định
- [ ] Chiến lược kênh (A hay B) được khai báo rõ trong mục Dataset
- [ ] Kết quả báo cáo theo fold kèm biến thiên, không phải một con số đơn
- [ ] HPO được lồng trong vòng đánh giá *(chỉ CP-2)*
- [ ] `Status_Event` được ghi rõ là PROPOSED *(chỉ CP-3)*
- [ ] Đã hỏi ý kiến người hướng dẫn trước khi nộp

---

## 10. Các mục còn chưa xác định — cần xác minh, không suy đoán

| # | Mục | Cách xác minh |
|---|---|---|
| 1 | Cách hiểu đúng của "đợt 2 và đợt 3 cùng lúc" | Sổ ghi chép thí nghiệm / hồ sơ thu số liệu |
| 2 | Deadline nộp bài của cả ba hội thảo | Trang web hội thảo |
| 3 | Chính sách prior-conference-publication của *Sensors* | Trang Instructions for Authors của tạp chí |
| 4 | Hội thảo trong nước cụ thể cho CP-3 | Chưa xác định |
| 5 | Ý kiến người hướng dẫn về việc công bố hội thảo trước khi G1 đóng | Quyết định của người hướng dẫn, không phải của kế hoạch này |
| 6 | Trạng thái xác minh các văn bản pháp luật VN (§F Living Evidence Base vẫn ghi `Unverified`) | Cổng thông tin văn bản pháp luật chính thức — cần cho CP-3 |

---

**Ghi nhớ một câu:**
> *Bài hội thảo tốt là bài mà nếu không viết, bạn vẫn phải làm phần việc đó cho luận án.*

Cả ba bài trong file này đều thỏa điều kiện đó: CP-1 sinh ra pipeline LORO, CP-2 sinh ra gói bất định và phân tích hiệu chuẩn, CP-3 sinh ra biên bản expert review cho G2.
