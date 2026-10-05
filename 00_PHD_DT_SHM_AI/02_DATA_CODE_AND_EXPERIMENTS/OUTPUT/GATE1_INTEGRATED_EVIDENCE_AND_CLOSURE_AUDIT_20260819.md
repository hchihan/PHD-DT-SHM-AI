# GATE 1 — INTEGRATED EVIDENCE AND CLOSURE AUDIT

**Ngày:** 19/08/2026 | **Phiên bản:** v1.0
**Loại:** Kiểm toán read-only trên artefact IT đã chạy cho YC1–YC4. Không phải bản thảo bài báo, không phải hồ sơ nghiệm thu Gate.
**Chế độ:** Read-only. Không sửa dữ liệu, không chạy lại mô hình, không thay đổi code.
**Phạm vi đã đọc:** 81 lần chạy mô hình, 6 tài liệu yêu cầu, toàn bộ mã nguồn `sensor_signal_analyzer`.

**Phân loại bằng chứng dùng trong báo cáo này:**
`SOURCE-VERIFIED` đọc trực tiếp từ artefact · `TECHNICAL INTERPRETATION` suy luận kỹ thuật của người kiểm toán · `THESIS APPLICATION` hệ quả cho luận án · `EVIDENCE INSUFFICIENT` không có artefact.

---

## 1. Executive verdict

```
GATE 1 OPEN — PARTIAL EVIDENCE
```

Bộ YC1–YC4 là bước tiến lớn nhất của Paper 1 từ trước tới nay. Ba trong bảy tiêu chí Gate 1 nay đạt hoặc gần đạt, và pipeline huấn luyện được kiểm chứng là chống rò rỉ ở mức cấu trúc, không chỉ ở mức tuyên bố.

Gate 1 chưa đóng được vì **ba blocker**, và cả ba đều là blocker thật chứ không phải hình thức:

1. **True LORO chưa tồn tại.** Sáu split của YC2 là Support Points selection, không phải sáu fold LORO. Ở mọi dataset có ít nhất một run không bao giờ được dùng làm test, và ít nhất một run được dùng hai lần. Ở `cp2_21` chỉ 4 trên 6 run từng làm test.
2. **Chỉ có một seed.** Chính tài liệu thiết kế của IT ghi rằng độ lệch chuẩn khi đổi seed trên một split cố định là **0,065**, lớn hơn độ lệch chuẩn giữa các split (0,054). Kế hoạch 3 seed được nêu trong thiết kế nhưng chỉ `seed42` tồn tại trong artefact. Do đó gần như mọi chênh lệch hiệu năng được báo cáo đều nằm trong nhiễu seed.
3. **ResNet1D sensor mode chưa xác nhận đầy đủ.** Phần lớn trường truy được, nhưng danh tính chính xác của 8 và 12 kênh, việc có dùng resultant hay không, và cách xử lý dead channel đều không có artefact xác nhận.

Ngoài ba blocker, một kết luận đã được tuyên bố trước trong tài liệu yêu cầu YC4 bị chính dữ liệu bác bỏ (mục 11).

---

## 2. Routing block

```text
RQ:             RQ1
WP:             WP1 — Laboratory vibration evidence
Chapter:        Chapter 4
Paper:          Paper 1
Evidence Gate:  Gate 1
Scope:          Core Scope
Evidence type:  Laboratory evidence
```

Chuỗi nghiên cứu, Paper 1 chỉ sở hữu mắt xích đầu:

```text
Vibration data → qualified condition/state-change evidence → BIM-linked component → inspection record → inspection-maintenance action support
```

Không mở rộng sang field diagnosis, severity, RUL, predictive maintenance, calibrated FEM, stiffness inference, optimal sensor placement, hay chuyển classifier trực tiếp từ lab ra field. Mọi mô hình phần tử hữu hạn nhắc tới trong chương trình này là **nominal, uncalibrated, reference-only, and not used for damage diagnosis**, và không mô hình nào như vậy tham gia vào bất kỳ kết quả nào ở đây.

---

## 3. Source authority và evidence inventory

### 3.1 Ghi chú về nguồn quản trị

Bảy tài liệu quản trị được nêu trong yêu cầu đã được rà soát trong các phiên trước và giữ nguyên hiệu lực: hệ Gate 1 gồm bảy tiêu chí, chuỗi định danh đã khóa, và ranh giới FEM. Không phát hiện mâu thuẫn giữa artefact YC1–YC4 và bộ quản trị đó về mặt phạm vi.

Một mâu thuẫn về **trạng thái** cần ghi nhận: các tài liệu quản trị hiện hành vẫn ghi ResNet1D là chưa từng chạy và LORO là đã hoàn thành. Artefact YC1–YC4 cho thấy điều ngược lại ở cả hai vế: ResNet1D **đã chạy** đầy đủ, còn LORO đúng nghĩa **chưa từng chạy**. Trạng thái quản trị cần được cập nhật theo artefact, không phải ngược lại.

### 3.2 Inventory artefact — SOURCE-VERIFIED

Thư mục gốc: `04_DATA_CODE_AND_EXPERIMENTS/OUTPUT_18.08.2026/`

| Thư mục | Số run mô hình | Artefact khác | Tài liệu yêu cầu kèm theo |
|---|---:|---|---|
| `Output_yc1_Data_Analyze/` | 8 | báo cáo phân tích v1.0, 3 hình | `yeu_cau_1_lam_sach_du_lieu.md`, `sensor_position_permutation_synchronization.md` |
| `Output_yc2_Sensor_Configuration/` | 48 | – | `yeucau2daolaicacruntrongcungCP.md`, `selectingrunpermutationssupportpointssplit.md` |
| `Output_yc3_Cross-campaign/` | 8 | – | `yeucau3kiemtracheo.md` |
| `Output_yc4_Sensors/` | 17 | – | `yeu_cau_cuoi.md` |
| **Tổng** | **81** | | **6 tài liệu** |

Mỗi run có bốn artefact: `scores.json`, `predictions.json`, `history.json`, `confusion_matrix.png`, cùng checkpoint `best_*.pt`. Mã nguồn `sensor_signal_analyzer` được nhân bản trong cả bốn thư mục (80 file mỗi bản, nội dung giống nhau).

### 3.3 Artefact được nêu tên nhưng KHÔNG có trong bộ bàn giao — EVIDENCE INSUFFICIENT

| Artefact | Được nêu ở đâu | Vai trò |
|---|---|---|
| `model_npz/manifest.json` | `train_ddp_npz.py` dòng đọc `manifest.json` | chứa `class_map` và `windows_per_recording`; script bắt buộc phải có |
| `R{run}.npz` (24 file) | `train_ddp_npz.py::load_runs` | chính là dataset đầu vào |
| `selected_splits.json` | `selectingrunpermutationssupportpointssplit.md` §8 | điểm số energy distance và vai trò từng split |
| `cache/<campaign>.npz` | cùng trên | ma trận khoảng cách cặp |
| `01_window_features.py`, `02_select_splits.py` | cùng trên | mã chọn split |
| `preprocessing_scripts_3/07b_detect_sensor_swap.py` | `yeu_cau_1_lam_sach_du_lieu.md` | thuật toán sửa hoán vị cảm biến |
| Log huấn luyện đầy đủ | 4 link Kaggle trong các tài liệu yêu cầu | nguồn kết quả gốc |
| `THREE_CAMPAIGN_REANALYSIS/` | có mặt ngày 18/08, không còn ở lần kiểm tra này | kết quả RF/SVM/LogReg và permutation control |

Việc thư mục `THREE_CAMPAIGN_REANALYSIS` biến mất giữa hai lần kiểm tra là một vấn đề quản lý phiên bản cần xử lý. Toàn bộ kết quả họ mô hình đặc trưng, permutation control 300 dòng và ba confusion matrix cấp window nằm trong đó.

---

## 4. Traceability matrix YC1–YC4 → artefact → research use

| YC | Yêu cầu | Artefact thực tế | Đủ hay thiếu | Dùng được cho Paper 1 ở mức nào |
|---|---|---|---|---|
| YC1 | Làm sạch dữ liệu, provenance, sửa hoán vị cảm biến | 8 run (4 dataset × 2 kiến trúc), 2 tài liệu phương pháp | Tài liệu đầy đủ; **artefact validation của thuật toán sửa hoán vị không có** | Methods và Dataset section. Kết quả mô hình chỉ là baseline một split |
| YC2 | Chọn và chạy tổ hợp train–val–test trong từng campaign | 48 run = 4 dataset × 2 kiến trúc × 6 split | Đúng thiết kế đã công bố; **không phải LORO** | Sensitivity/coverage analysis, không phải kết quả chính |
| YC3 | Kiểm tra chéo giữa các campaign | 8 run, hai chiều CP2↔CP3, hai view của CP2 | Đầy đủ theo Phase 1; Phase 2 để trống | **Kết quả chính**, negative result có giá trị cao nhất |
| YC4 | Ảnh hưởng số lượng và cấu hình cảm biến | 17 run đúng 17 tổ hợp yêu cầu | Đúng số lượng; **một split cố định, một seed** | `EXPLORATORY` |

Ghi chú định vị: bốn dataset `cp1`, `cp2_21`, `cp2_2122`, `cp3` là **bốn analysis view trên ba campaign vật lý**. `cp2_21` và `cp2_2122` cùng dùng run R7–R12 của CP2 và **không phải hai campaign độc lập, không phải hai replication**. Tài liệu `yeu_cau_1_lam_sach_du_lieu.md` cộng gộp thành "288 recording, 24 run"; con số đúng ở cấp vật lý là **216 recording, 18 run**.

---

## 5. Dataset và provenance audit

### 5.1 Cấu trúc vật lý so với analysis view — SOURCE-VERIFIED

| Cấp | Số lượng | Định danh | Nguồn |
|---|---:|---|---|
| Physical campaign | 3 | CP1, CP2, CP3 | `yeu_cau_1_lam_sach_du_lieu.md` |
| Physical run | 18 | R1–R6, R7–R12, R13–R18 | `predictions.json` mọi run, tiền tố `R{n}:` |
| Physical recording | 216 | 12 recording mỗi run | 4 state × 3 excitation × 6 run × 3 campaign |
| Analysis view | 4 | `cp1`, `cp2_21`, `cp2_2122`, `cp3` | tên thư mục và `--dataset-name` |
| Window | 9.948 | – | `yeu_cau_1_lam_sach_du_lieu.md` bảng tổng quan |

Mỗi view chứa 72 recording và 18 recording mỗi lớp, cân bằng tuyệt đối ở cấp recording. Window lệch nhẹ dưới 1,6 % giữa các lớp.

### 5.2 Thành phần hai view của CP2 — SOURCE-VERIFIED

Kiểm chứng trực tiếp từ `recording_id` trong `Output_yc3_Cross-campaign/cross_cp3_to_cp2_*/predictions.json`, n = 72 mỗi view:

| View | Recording từ 21/07 | Recording từ 22/07 | Lớp trong nhóm 21/07 | Lớp trong nhóm 22/07 |
|---|---:|---:|---|---|
| `cp2_21` | 72 | 0 | B1, B2, B3, Healthy | – |
| `cp2_2122` | 18 | 54 | **chỉ B3** | B1, B2, Healthy |

`TECHNICAL INTERPRETATION.` `cp2_2122` có nhãn trạng thái trùng khít hoàn toàn với ngày đo cho lớp B3: toàn bộ 18 recording B3 đến từ 21/07 và không recording nào của ba lớp còn lại đến từ ngày đó. Đây là nhiễu loạn thu nhận hoàn toàn ở cấp một lớp.

`SOURCE-VERIFIED.` Buổi 21/07 **có** đo đủ bốn trạng thái, chứng minh bởi `cp2_21` với 72 recording đủ bốn lớp cùng một ngày. Do đó nhiễu loạn trong `cp2_2122` là **hệ quả của cách dựng dataset**, không phải giới hạn thu thập. `yeu_cau_1_lam_sach_du_lieu.md` mô tả đúng chủ ý này: "Bộ 2: 3 cái của ngày 22 (S0, B1, B2) + 1 cái của ngày 21".

`THESIS APPLICATION.` Cặp `cp2_21` và `cp2_2122` là một **control có thiết kế** cho nhiễu loạn buổi đo. Đây là artefact có giá trị phương pháp cao nhất trong YC1, và cần được trình bày như vậy trong manuscript.

### 5.3 Mapping B1/B2/B3 sang liên kết vật lý — EVIDENCE INSUFFICIENT

`SOURCE-VERIFIED.` `train_ddp_npz.py` khóa `class_map = {"B1": 0, "B2": 1, "B3": 2, "Healthy": 3}` và kiểm tra bắt buộc với `manifest.json`. Nhãn được giải mã tất định từ tên file.

`EVIDENCE INSUFFICIENT.` Không artefact nào trong YC1–YC4 xác nhận B1 = Apex, B2 = Beam–Column, B3 = Brace–Column. `sensor_position_permutation_synchronization.md` §3 có nêu "S1 — Apex, S2 — Beam–Column, S3 — Brace", nhưng đó là ánh xạ **cảm biến**, không phải ánh xạ **trạng thái hư hỏng**. Hai thứ này khác nhau và không được lẫn.

Hệ quả: mọi diễn giải theo lớp cụ thể trong báo cáo này và trong manuscript đều là có điều kiện. Không phát biểu nào nói một trạng thái gần Healthy hơn trạng thái khác.

### 5.4 File thiếu, bổ sung, loại và cảnh báo provenance — SOURCE-VERIFIED

| Sự việc | Chi tiết | Nguồn |
|---|---|---|
| Tổng file thô | 270 | `yeu_cau_1_lam_sach_du_lieu.md` §Bước 02 |
| Cắt null đuôi | 177 file bị cắt, 1.171 mẫu = **0,061 %** dữ liệu, nhiều nhất 92 mẫu một file | cùng trên |
| File phải review sau khi cắt | 0 | cùng trên |
| Thiếu B3 ngày 22/07 | ngày 2 chỉ đo S0, B1, B2 | `yeu_cau_1_lam_sach_du_lieu.md` §CP2 |
| Bù bằng recording ngày 21/07 | 18 recording B3 | mục 5.2 |
| File loại | 0 | không artefact nào ghi nhận loại bỏ |

`TECHNICAL INTERPRETATION.` Con số 270 file thô ăn khớp với 216 recording canonical nếu CP2 đóng góp 126 file thô cho 72 recording sau khi chọn view. Quan hệ chính xác giữa 270 và 216 vẫn chưa có một register duy nhất ghi lại.

### 5.5 Hoán vị vị trí cảm biến CP1 — SOURCE-VERIFIED, validation EVIDENCE INSUFFICIENT

`SOURCE-VERIFIED` từ `yeu_cau_1_lam_sach_du_lieu.md`:

| Chỉ số | Giá trị |
|---|---|
| File CP1 bị hoán vị | **21 / 72** |
| Phân bố theo run | R1: 6, R2: 6, R3: 1, R4: 2, R5: 4, R6: 2 |
| `pair_margin` nhỏ nhất | 1,167 |
| `sync_residual` lớn nhất | 0,0000 |
| `force_check` | agree 72/72 |

Phương pháp được đặc tả đầy đủ trong `sensor_position_permutation_synchronization.md`: trích vân tay cảm biến, ghép cặp vét cạn trên 3! = 6 hoán vị, rồi Permutation Synchronization toàn cục theo Pachauri et al. (NeurIPS 2013), Chen et al. (ICML 2014), Ling (2020/2021), Nguyen và Zhang (2023).

`EVIDENCE INSUFFICIENT.` Chính tài liệu đó, §4, yêu cầu một thí nghiệm validation có kiểm soát: tiêm hoán vị nhân tạo đã biết, rồi báo cáo **Exact Permutation Recovery Rate, Sensor-wise Accuracy, Sensitivity, Specificity, False Positive Rate** ở các mức nhiễu 5 %, 10 %, 20 %, 30 %, 40 %. **Không artefact nào của thí nghiệm này tồn tại trong bộ bàn giao.**

`TECHNICAL INTERPRETATION.` `sync_residual = 0,0000` cho biết nghiệm hoán vị toàn cục nhất quán hoàn hảo với các ghép cặp, và `pair_margin` nhỏ nhất 1,167 cho biết biên phân tách không sát ngưỡng. Cả hai đều là chỉ báo mạnh nhưng đều là **chỉ báo nội tại**: chúng đo sự nhất quán của lời giải, không đo tỉ lệ đúng so với ground truth. Chỉ thí nghiệm tiêm hoán vị mới đo được điều đó.

`THESIS APPLICATION.` Đây là mắt xích cần cho một đóng góp có thể công bố. Bài báo đang tuyên bố sửa được lỗi định danh cảm biến trên 21 file; nếu không có recovery rate, tuyên bố đó dựa trên chỉ báo nội tại chứ không dựa trên kiểm chứng. Chi phí thí nghiệm thấp vì dữ liệu và mã đã có.

### 5.6 Dead và flat channel — EVIDENCE INSUFFICIENT trong bộ YC

Không artefact nào trong YC1–YC4 ghi nhận dead channel hay cách xử lý. Thông tin này chỉ tồn tại trong bộ `THREE_CAMPAIGN_REANALYSIS` nay không còn trong thư mục.

### 5.7 Mất cân bằng window giữa các recording — SOURCE-VERIFIED, và là một defect

`yeu_cau_1_lam_sach_du_lieu.md` §"Hai điều bảng này lộ ra" ghi nhận thẳng:

| View | Window/recording nhỏ nhất | Lớn nhất | Tỉ lệ |
|---|---:|---:|---:|
| `cp1` | 19 | 31 | 1,63× |
| `cp2_21` | 33 | 62 | **1,88×** |
| `cp2_2122` | 33 | 60 | 1,82× |
| `cp3` | 29 | 29 | 1,00× |

Nguyên nhân: **bước cắt cửa sổ chung 40 s đã bị bỏ.** Một recording ở `cp2_21` có thể đóng góp gấp 1,88 lần recording khác cùng lớp trong tập huấn luyện.

`TECHNICAL INTERPRETATION.` Đây không phải leakage, vì tính độc lập giữa các run vẫn giữ. Nhưng nó tạo trọng số huấn luyện không đồng đều giữa các recording, và trọng số đó tương quan với độ dài bản ghi chứ không với nội dung trạng thái. Ở cấp báo cáo thì vô hại, vì tổng hợp là trung bình softmax trong từng recording. Ở cấp huấn luyện thì không.

`SOURCE-VERIFIED.` Tài liệu cũng nêu một recording CP2 dài bất thường, 12.635 mẫu so với median 7.190, và tự đặt câu hỏi đó là đo dài thật hay lỗi ghi. Câu hỏi này chưa được trả lời.

### 5.8 Dataset version, hash, manifest — EVIDENCE INSUFFICIENT

Không có dataset version tag, không có hash, và `manifest.json` mà script bắt buộc phải đọc không nằm trong bộ bàn giao. Đây là tiêu chí Gate 1 số 1 và nó chưa đạt.

---

## 6. Split, LORO và leakage audit

### 6.1 Ba thiết kế split hiện diện trong bộ YC — SOURCE-VERIFIED

| Thiết kế | Nơi xuất hiện | Bản chất |
|---|---|---|
| Một split cố định | YC1 (8 run), YC4 (17 run) | 4 train / 1 val / 1 test, cố định theo dataset |
| Sáu Support-Point split | YC2 (48 run) | 6 trên 30 cặp (val, test) được chọn bằng energy distance |
| Cross-campaign holdout | YC3 (8 run) | 5 run train / 1 run val của campaign nguồn, toàn bộ campaign đích làm test |
| **True outer LORO** | **không nơi nào** | **chưa tồn tại** |

### 6.2 Bảng LORO coverage — SOURCE-VERIFIED

Định danh run làm test được đọc trực tiếp từ trường `recording_id` trong `predictions.json` của 48 run YC2. Vai trò split lấy từ `yeucau2daolaicacruntrongcungCP.md`.

**cp1** (run R1–R6)

| Split | Vai trò | Val | Test | Test run giữ lại đúng một lần? | Artefact |
|---|---|---|---|---|---|
| 1 | representative | R1 | R3 | có | `cp1_*_v5_split1/ddp_seed42/` |
| 2 | worst_case | R2 | **R1** | **không, lần 1/2** | `..._split2/` |
| 3 | coverage | R2 | R4 | có | `..._split3/` |
| 4 | coverage | R5 | R6 | có | `..._split4/` |
| 5 | coverage | R6 | **R1** | **không, lần 2/2** | `..._split5/` |
| 6 | coverage | R6 | R2 | có | `..._split6/` |
| – | – | – | **R5** | **không bao giờ làm test** | – |

**cp2_21** (run R7–R12)

| Split | Vai trò | Val | Test | Test run giữ lại đúng một lần? |
|---|---|---|---|---|
| 1 | coverage | R7 | **R9** | không, lần 1/2 |
| 2 | representative | R7 | **R10** | không, lần 1/2 |
| 3 | coverage | R8 | R7 | có |
| 4 | coverage | R9 | R8 | có |
| 5 | coverage | R11 | **R10** | không, lần 2/2 |
| 6 | worst_case | R12 | **R9** | không, lần 2/2 |
| – | – | – | **R11, R12** | **không bao giờ làm test** |

**cp2_2122** (run R7–R12): test = R8, R11, R7, R12, R8, R9. R8 hai lần; **R10 không bao giờ làm test**.

**cp3** (run R13–R18): test = R16, R15, R13, R14, R18, R13. R13 hai lần; **R17 không bao giờ làm test**.

Tổng hợp:

| Dataset | Run riêng biệt từng làm test | Run bị lặp | Run chưa từng làm test |
|---|---:|---|---|
| `cp1` | 5 / 6 | R1 (×2) | R5 |
| `cp2_21` | **4 / 6** | R9 (×2), R10 (×2) | R11, R12 |
| `cp2_2122` | 5 / 6 | R8 (×2) | R10 |
| `cp3` | 5 / 6 | R13 (×2) | R17 |

`TECHNICAL INTERPRETATION.` Sáu split của YC2 **không phải 6-fold LORO** và không được gọi như vậy. Đây là thiết kế có chủ ý, được đặc tả và biện minh đầy đủ trong `selectingrunpermutationssupportpointssplit.md`, dựa trên Support Points của Mak và Joseph (Annals of Statistics 2018), SPlit của Joseph và Vakayil (arXiv:2012.10945) và energy distance của Székely và Rizzo (2013). Nó trả lời câu hỏi "sáu split nào đại diện tốt nhất cho cả 30 split", và nó trả lời tốt: energy distance giữa tập chọn và toàn bộ 30 split thấp hơn 2,25–2,58 lần so với chọn ngẫu nhiên.

Nhưng nó **không** trả lời câu hỏi mà LORO trả lời: "hiệu năng ngoài mẫu, trung bình trên mọi run độc lập, là bao nhiêu". Với `cp2_21`, một phần ba số run chưa từng được kiểm tra.

`THESIS APPLICATION.` Support-Point splits được báo cáo trong Paper 1 như **sensitivity và coverage analysis**, kèm điểm representative làm headline và worst_case làm cận dưới, đúng như thiết kế của IT khuyến nghị. Chúng không thay thế outer LORO trong phần Results chính.

### 6.3 Phương án LORO tối thiểu đề xuất

`THESIS APPLICATION.` Để mở khóa tiêu chí Gate 1 số 3, cần và chỉ cần:

- **Sáu outer fold cho mỗi dataset**, mỗi run làm test đúng một lần;
- **Run validation chọn bằng một quy tắc cố định** trong năm run còn lại, ví dụ giữ nguyên tiêu chí `argmin e_val` của Support Points trong tập năm run đó, hoặc đơn giản là run kế tiếp theo vòng. Quy tắc phải được công bố trước và áp dụng như nhau cho mọi fold;
- **Giữ nguyên run granularity**, không chia window ngẫu nhiên qua train/val/test;
- **Ba seed** cho mỗi fold, vì độ lệch chuẩn seed 0,065 lớn hơn độ lệch chuẩn split 0,054.

Khối lượng: 4 dataset × 6 fold × 2 kiến trúc × 3 seed = **144 lần chạy**. Thiết kế Support Points ban đầu định cắt từ 360 xuống 72; phương án này nằm giữa hai con số đó và giữ được tính đầy đủ của LORO.

Support Points vẫn giữ nguyên giá trị: nó trả lời câu hỏi khác và trả lời tốt, và nên được giữ trong bài như một mục riêng.

### 6.4 Leakage control — SOURCE-VERIFIED từ mã nguồn

Kiểm chứng trực tiếp trong `sensor_signal_analyzer/scripts/train_ddp_npz.py`:

| Cơ chế | Bằng chứng trong mã | Đánh giá |
|---|---|---|
| Dữ liệu lưu theo run | `load_runs` đọc `R{run}.npz`, mỗi file một run | Cấu trúc chống lẫn run ngay từ lưu trữ |
| Không lẫn run trong file | `if set(item["run_id"].tolist()) != {run}: raise ValueError` | Kiểm tra chủ động, không phải giả định |
| Train/val/test rời nhau | `if set(train_runs) & set(val_runs + test_runs) or set(val_runs) & set(test_runs): parser.error(...)` | Bắt buộc ở cấp tham số |
| Chia trước khi windowing | Window đã nằm sẵn trong NPZ theo run; không thao tác nào trộn run | Thỏa mãn ở cấp cấu trúc |
| Chuẩn hóa | `X = (X - X.mean(2)) / (X.std(2) + 1e-8)` | **Chuẩn hóa từng window, từng kênh, theo trục thời gian của chính nó** |
| Không có thống kê học từ tập nào | không tồn tại đối tượng scaler được fit | Xem diễn giải bên dưới |
| Val dùng cho early stopping | `improved = val_loss < best_loss and val_acc > chance`, `stale >= patience` | Đúng vai trò |
| Test không tham gia chọn model | checkpoint chọn theo val, test chỉ chạy sau khi nạp checkpoint tốt nhất | Không có model selection trên test |
| Tổng hợp cấp recording | `score = probabilities[mask].mean(0)`, rồi `argmax` | Cấp báo cáo là recording |
| Nhãn nhất quán trong recording | `if len(np.unique(labels[mask])) != 1: raise` | Kiểm tra chủ động |
| Xác định | `torch.manual_seed`, `np.random.seed`, `torch.use_deterministic_algorithms(True, warn_only=True)` | Có |

`TECHNICAL INTERPRETATION.` Điểm chuẩn hóa cần được phát biểu chính xác, vì nó khác với yêu cầu thông thường. Pipeline **không** fit scaler trên tập train rồi áp lên test. Nó chuẩn hóa **từng window một cách độc lập** theo trung bình và độ lệch chuẩn của chính window đó trên trục thời gian. Do đó không tồn tại đường rò rỉ thống kê giữa các tập, không phải vì được kiểm soát tốt, mà vì **không có thống kê toàn cục nào được ước lượng**. Đây là thiết kế mạnh hơn yêu cầu "train-only fitting", và cần được mô tả đúng như vậy trong Methods, không nên viết là "scaler fit trên train".

Hệ quả phụ cần ghi nhận: chuẩn hóa từng window loại bỏ thông tin biên độ tuyệt đối giữa các window. Đây là lựa chọn thiết kế có hệ quả, và nó ngược với kết luận của phép kiểm độ nhạy trong bộ `THREE_CAMPAIGN_REANALYSIS`, nơi giữ biên độ cho kết quả cao hơn chuẩn hóa RMS 0,130. Hai pipeline dùng hai quy ước biên độ khác nhau; điều này phải được nêu khi so sánh chúng.

### 6.5 Selection bias từ việc chọn split bằng phân bố toàn dataset

`TECHNICAL INTERPRETATION.` Support Points chọn split bằng energy distance tính trên **toàn bộ window của campaign, bao gồm cả window của run sẽ làm test**. Tiêu chí `e_test = E(windows of t, all windows)` theo định nghĩa phải nhìn vào phân bố của run test.

Đây không phải leakage theo nghĩa nhãn hay đặc trưng đi vào huấn luyện. Nhưng nó là **selection bias có hướng**: split "representative" được chọn chính vì run test của nó giống phân bố chung nhất, tức là split dễ nhất theo tiêu chí phân bố. Báo cáo điểm representative làm headline vì thế là báo cáo một ước lượng có thiên lệch lên trên so với trung bình LORO.

Thiết kế của IT đã lường trước điều này và yêu cầu báo cáo worst_case bên cạnh làm cận dưới. Đó là cách xử lý đúng, và Paper 1 phải giữ nguyên cặp đó, không được tách rời.

---

## 7. ResNet1D sensor-mode verification

| Trường | Giá trị | Nguồn | Trạng thái |
|---|---|---|---|
| Sensor source | `R{run}.npz`, khóa `X`, `y`, `recording_id`, `run_id` | `train_ddp_npz.py::load_runs` | `SOURCE-VERIFIED` cấu trúc; **file NPZ không có trong bộ bàn giao** |
| Physical sensors | cp1: 2 cụm (Apex, BeamColumn); cp2_*, cp3: 3 cụm (+ BraceColumn) | `yeu_cau_1_lam_sach_du_lieu.md` bảng Sensor | `SOURCE-VERIFIED` từ tài liệu |
| Axes/channels | cp1 = **8 kênh**, cp2_*/cp3 = **12 kênh** | cùng trên; và `--expected-channels` được kiểm tra bởi `X.shape[1] != channels` | `SOURCE-VERIFIED` số lượng |
| Danh tính từng kênh | 8 = 2 cụm × 4; 12 = 3 cụm × 4 | suy ra từ số học | `EVIDENCE INSUFFICIENT` — thứ tự và ý nghĩa từng kênh không có artefact |
| Có dùng resultant không | `yeu_cau_cuoi.md` nêu "chạy theo từng dữ liệu (x, y, z, resultant)" | | `EVIDENCE INSUFFICIENT` — bốn kênh mỗi cụm phù hợp với x, y, z, resultant nhưng **không được xác nhận ở bất kỳ artefact nào** |
| Sampling rate | 100 Hz | tài liệu canonical trước đó, không có trong bộ YC | `EVIDENCE INSUFFICIENT` trong phạm vi bộ YC |
| Window length / hop | **400 mẫu / hop 200**, tức chồng lấn 50 % | `selectingrunpermutationssupportpointssplit.md` §3 và chú thích trong `cnn1d/model.py` ("a 400-sample window") | `SOURCE-VERIFIED` |
| Input shape | `(N, C, 400)` với C = 8 hoặc 12 | `load_runs` kiểm tra `X.ndim == 3 and X.shape[1] == channels` | `SOURCE-VERIFIED` |
| Dead-channel handling | – | – | `EVIDENCE INSUFFICIENT` |
| Normalization | z-score từng window từng kênh trên trục thời gian, `eps = 1e-8` | `train_ddp_npz.py::load_runs` | `SOURCE-VERIFIED` |
| Model version | `v5` cho YC1–YC3, `v6` cho YC4 | hậu tố thư mục và link Kaggle | `SOURCE-VERIFIED` |
| Kiến trúc | 3 residual block, kernel 8/5/3, GAP, linear; `n_feature_maps` 16 (cp1, cp3) hoặc 32 (cp2) | `src/resnet1d/model.py`; `yeu_cau_1_lam_sach_du_lieu.md` bảng siêu tham số | `SOURCE-VERIFIED` |
| Split protocol | 4 train run / 1 val run / 1 test run, rời nhau, kiểm tra bắt buộc | `train_ddp_npz.py` | `SOURCE-VERIFIED` |
| Seeds | **chỉ 42** | mọi thư mục là `ddp_seed42` | `SOURCE-VERIFIED` |
| Optimizer | AdamW; lr 3e-4 (cp1, cp2) hoặc 2e-4 (cp3); weight decay 1e-2 (cp1, cp2) hoặc 3e-2 (cp3) | `yeu_cau_1_lam_sach_du_lieu.md` | `SOURCE-VERIFIED` |
| Early stopping | patience 10, chọn theo `val_loss` với ràng buộc `val_acc > 0.25` | `train_ddp_npz.py` | `SOURCE-VERIFIED` |

**Kết luận điều kiện "ResNet1D mode confirmed": `PARTIAL`.**

Bốn trường quan trọng chưa truy được về artefact: danh tính từng kênh trong 8 và 12 kênh, việc có dùng resultant hay không, sampling rate trong phạm vi bộ YC, và cách xử lý dead channel. Ba trong bốn có thể đóng bằng cách bàn giao `manifest.json` và một file NPZ mẫu. Đây là công việc bàn giao, không phải công việc thí nghiệm.

`THESIS APPLICATION.` Số kênh là 8 và 12, không phải 6 và 9. Mọi mô tả trước đây trong tài liệu Paper 1 nói "6 kênh cho CP1, 9 kênh cho CP2 và CP3" là **sai** và phải sửa. Nếu kênh thứ tư mỗi cụm là resultant thì nó là một đặc trưng phái sinh từ ba kênh kia, và điều đó cần được nêu rõ trong Methods vì nó ảnh hưởng tới cách diễn giải "số kênh".

---

## 8. Results theo từng nhiệm vụ

Mọi số liệu dưới đây ở **cấp recording**, n = 12 recording mỗi test run trừ YC3 (n = 72). Toàn bộ là `seed42`. Mức ngẫu nhiên bốn lớp cân bằng: macro-F1 = 0,25.

### 8.1 YC1 — baseline một split cố định

Locator: `Output_yc1_Data_Analyze/{dataset}_{arch}_v5/ddp_seed42/scores.json`

| Dataset | Test run | 1D-CNN macro-F1 | ResNet1D macro-F1 | 1D-CNN val_loss | ResNet1D val_loss |
|---|---|---:|---:|---:|---:|
| `cp1` | R6 | 0,727 | **0,914** | 1,626 | 0,396 |
| `cp2_21` | R12 | 0,581 | **0,914** | 2,077 | 0,322 |
| `cp2_2122` | R12 | 0,586 | **0,914** | 1,464 | 0,442 |
| `cp3` | R18 | 0,250 | **0,345** | 3,325 | 1,506 |

`TECHNICAL INTERPRETATION.` Ba nhận định.

ResNet1D cao hơn 1D-CNN ở cả bốn dataset. Kiểm định McNemar chính xác ghép cặp trên cùng recording cho p = 0,500 / 0,219 / 0,125 / 1,000; **không so sánh nào đạt ý nghĩa** ở n = 12.

Chênh lệch nằm ở khả năng khái quát, không ở khả năng khớp: train accuracy cuối của cả hai kiến trúc là 0,983–1,000 ở cp1 và cp2, còn val_loss của 1D-CNN cao hơn ResNet1D từ 3 đến 6 lần.

`cp3` khó ở phía dữ liệu: train accuracy chỉ 0,874 và 0,881, tức cả hai kiến trúc **không khớp nổi tập huấn luyện**. Tăng độ sâu chỉ đưa macro-F1 từ 0,250 lên 0,345.

`SOURCE-VERIFIED` giải thích định lượng cho `cp3`: `yeu_cau_1_lam_sach_du_lieu.md` báo cáo tỉ số Fisher tách lớp **cp1 0,245–0,276; cp2 0,022–0,054; cp3 0,005–0,010**. Độ tách lớp của cp3 thấp hơn cp1 khoảng 25–50 lần. `selectingrunpermutationssupportpointssplit.md` §6 độc lập xác nhận: e_gap worst-case của cp3 là 0,2357 so với 0,0365 của cp1, gấp 6,5 lần, và tài liệu tự dự báo "near-chance test scores" cho cp3 trước khi chạy.

`THESIS APPLICATION.` Hai chỉ số này (Fisher ratio và energy distance giữa các run) là **bằng chứng độc lập với mô hình** cho biết độ khó nằm ở dữ liệu. Chúng nên vào manuscript như một bảng đặc trưng dataset, vì chúng biến "mô hình thất bại ở cp3" thành "cp3 có cấu trúc lớp yếu và các run không đồng nhất".

### 8.2 YC2 — Support-Point splits

Locator: `Output_yc2_Sensor_Configuration/{dataset}_{arch}_v5_split{n}/ddp_seed42/scores.json`

Macro-F1 theo vai trò split đã công bố:

| Dataset | Kiến trúc | s1 | s2 | s3 | s4 | s5 | s6 | representative | worst_case | Biên độ |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `cp1` | 1D-CNN | 0,554 | 0,655 | 0,564 | 0,727 | 0,512 | 0,661 | 0,554 | 0,655 | 0,214 |
| `cp1` | ResNet1D | 0,914 | 0,914 | 1,000 | 0,914 | 0,914 | 0,914 | 0,914 | 0,914 | 0,086 |
| `cp2_21` | 1D-CNN | 0,607 | 0,676 | 0,914 | 0,731 | 0,676 | 0,576 | 0,676 | 0,576 | 0,338 |
| `cp2_21` | ResNet1D | 1,000 | 1,000 | 1,000 | 1,000 | 1,000 | 1,000 | **1,000** | **1,000** | **0,000** |
| `cp2_2122` | 1D-CNN | 0,914 | 0,760 | 0,760 | 0,731 | 0,731 | 0,731 | 0,760 | 0,731 | 0,183 |
| `cp2_2122` | ResNet1D | 0,914 | 0,914 | 1,000 | 0,914 | 0,914 | 0,833 | 0,914 | 0,833 | 0,167 |
| `cp3` | 1D-CNN | 0,334 | 0,368 | 0,361 | 0,198 | 0,250 | 0,575 | 0,334 | 0,250 | 0,377 |
| `cp3` | ResNet1D | 0,438 | 0,658 | 0,727 | 0,576 | 0,345 | 0,731 | 0,438 | 0,345 | 0,386 |

`TECHNICAL INTERPRETATION.` Bốn nhận định.

**ResNet1D trên `cp2_21` đạt 1,000 ở toàn bộ sáu split.** Sáu lần, mỗi lần 12/12 recording đúng, trên bốn run test khác nhau. Đây là kết quả nội-view mạnh nhất của cả bộ. Nó cũng là kết quả cần dè dặt nhất: `cp2_21` là một buổi đo duy nhất, một lần lắp đặt, sáu run liên tiếp. Nó đo khả năng phân biệt trạng thái **trong một lần thiết lập**, không đo khả năng lặp lại qua thiết lập.

**View trộn hai buổi khó hơn view một buổi.** ResNet1D: `cp2_21` 1,000 ở mọi split, `cp2_2122` 0,833–1,000. Nếu nhiễu loạn buổi đo thổi phồng kết quả thì chiều phải ngược lại. Kết hợp với YC1, nơi hai view cho cùng 0,914, bằng chứng nghiêng về kết luận **nhiễu loạn buổi đo trong `cp2_2122` không tạo lợi thế hiệu năng**.

**Biên độ giữa các split lớn hơn nhiễu seed ở `cp3` và `cp2_21`/1D-CNN.** Biên độ 0,377 và 0,386 ở `cp3`, và 0,338 ở `cp2_21`/1D-CNN, đều vượt xa độ lệch chuẩn seed 0,065. Ở những dataset đó, việc chọn run nào làm test quan trọng hơn nhiều so với seed. Ngược lại, biên độ 0,086 và 0,000 của ResNet1D trên `cp1` và `cp2_21` nằm trong hoặc dưới nhiễu seed.

**Ở `cp3`, representative thấp hơn cả trung vị coverage.** ResNet1D: representative 0,438, trung vị coverage 0,693, worst_case 0,345. Split được chọn vì run test giống phân bố chung nhất lại không cho điểm cao nhất. `TECHNICAL INTERPRETATION`: ở một campaign mà các run không đồng nhất, khái niệm "run đại diện" mất đi phần lớn ý nghĩa, đúng như tài liệu Support Points đã cảnh báo với e_train của cp3 nhảy lên 0,0185–0,0209.

### 8.3 YC3 — kiểm tra chéo giữa campaign

Locator: `Output_yc3_Cross-campaign/cross_{source}_to_{target}_{arch}/ddp_seed42/`

Thiết kế theo `yeucau3kiemtracheo.md`: train 5 run của campaign nguồn, val 1 run của campaign nguồn, test **toàn bộ 6 run** của campaign đích, n = 72 recording.

| Nguồn | Đích | Kiến trúc | macro-F1 | balanced acc | ROC-AUC | Lớp bị dự đoán nhiều nhất | Tỉ lệ | e_shift |
|---|---|---|---:|---:|---:|---|---:|---:|
| `cp2_21` | `cp3` | 1D-CNN | **0,101** | 0,250 | **0,427** | B2 | **98,6 %** | 1,4988 |
| `cp2_21` | `cp3` | ResNet1D | 0,147 | 0,222 | 0,622 | B1 | 65,3 % | 1,4988 |
| `cp2_2122` | `cp3` | 1D-CNN | 0,160 | 0,236 | 0,548 | Healthy | 76,4 % | 1,0848 |
| `cp2_2122` | `cp3` | ResNet1D | 0,189 | 0,236 | 0,507 | Healthy | 58,3 % | 1,0848 |
| `cp3` | `cp2_21` | 1D-CNN | **0,280** | 0,347 | 0,515 | B1 | 69,4 % | 1,5399 |
| `cp3` | `cp2_21` | ResNet1D | 0,161 | 0,208 | 0,545 | B1 | 62,5 % | 1,5399 |
| `cp3` | `cp2_2122` | 1D-CNN | 0,202 | 0,292 | 0,441 | B1 | 63,9 % | 1,0902 |
| `cp3` | `cp2_2122` | ResNet1D | **0,082** | **0,097** | 0,400 | B3 | 54,2 % | 1,0902 |

Recall từng lớp, hai ca cực trị:

| Ca | B1 | B2 | B3 | Healthy |
|---|---:|---:|---:|---:|
| `cp2_21` → `cp3`, 1D-CNN | 0,000 | **1,000** | 0,000 | 0,000 |
| `cp3` → `cp2_2122`, ResNet1D | 0,222 | 0,000 | 0,167 | 0,000 |

`TECHNICAL INTERPRETATION.` Năm nhận định, và đây là phần có giá trị khoa học cao nhất của cả bộ.

**Bảy trên tám cấu hình dưới mức ngẫu nhiên 0,25.** Ngoại lệ duy nhất là `cp3 → cp2_21` với 1D-CNN ở 0,280, vượt ngẫu nhiên 0,030, tức nửa độ lệch chuẩn seed.

**Sụp đổ về một lớp, không phải suy giảm hiệu năng.** Tỉ lệ lớp được dự đoán nhiều nhất dao động 54,2 % đến **98,6 %**, so với sự thật cân bằng 25 %. Trường hợp `cp2_21 → cp3` với 1D-CNN là một bộ dự đoán suy biến gần như hoàn toàn: 98,6 % gán vào B2, recall B2 = 1,000, ba lớp còn lại recall 0,000.

**Lớp B3 gần như biến mất khi chuyển giao.** Recall B3 bằng 0,000 ở năm trên tám cấu hình, và không vượt 0,556 ở bất kỳ cấu hình nào. Lớp Healthy cũng bằng 0,000 ở năm trên tám.

**Ba trên tám cấu hình có ROC-AUC dưới 0,5** (0,427, 0,441, 0,400). Xếp hạng xác suất tệ hơn ngẫu nhiên, tức mô hình học được một cấu trúc **phản tương quan** với nhãn của campaign đích, không phải học được ít thông tin.

**Không có hướng nào an toàn.** Trung bình theo chiều: CP2 → CP3 cho 0,101–0,189; CP3 → CP2 cho 0,082–0,280. Cả hai chiều đều hỏng, và view `cp2_2122` không hỏng nhiều hơn `cp2_21` một cách hệ thống.

`SOURCE-VERIFIED` bổ trợ: `yeucau3kiemtracheo.md` ghi e_shift 1,0848–1,5399 cho bốn cặp, so với e_gap worst-case nội campaign lớn nhất là 0,2357 ở cp3. Khoảng cách phân bố liên campaign lớn hơn khoảng cách nội campaign khắc nghiệt nhất **từ 4,6 đến 6,5 lần**. Thất bại chuyển giao vì thế là hệ quả có thể dự báo được từ chính đo lường phân bố, không phải một bất ngờ.

`THESIS APPLICATION.` Đây là kết quả chính của Paper 1. Nó chuyển "mô hình không khái quát được" thành một phát biểu kiểm chứng được về **ranh giới hiệu lực của bằng chứng**, kèm ba mức định lượng: tỉ lệ sụp lớp, recall từng lớp, và khoảng cách phân bố đo trước khi chạy. Phạm vi kết luận: giới hạn chuyển giao **giữa các campaign trong phòng thí nghiệm**. Không suy rộng sang công trình thực.

### 8.4 YC4 — cấu hình cảm biến

Locator: `Output_yc4_Sensors/sensor_count_experiments/{dataset}/{config}/ddp_seed42/scores.json`

Đủ 17 tổ hợp yêu cầu. Split cố định: cp1 train R1–R4 / val R5 / test R6; cp2_21 train R7–R10 / val R11 / test R12; cp3 train R13–R16 / val R17 / test R18.

| Dataset | s1 | s2 | s3 | s12 | s13 | s23 | s123 |
|---|---:|---:|---:|---:|---:|---:|---:|
| `cp1` | 0,914 | 1,000 | – | 0,914 | – | – | – |
| `cp2_21` | 1,000 | 1,000 | 0,812 | 0,914 | 1,000 | 0,829 | 1,000 |
| `cp3` | 0,208 | 0,162 | 0,375 | 0,171 | 0,438 | 0,225 | 0,383 |

Tổng hợp theo đúng quy tắc đã công bố trong `yeu_cau_cuoi.md`:

| Dataset | 1 sensor (TB) | 2 sensors (TB) | 3 sensors | Δ(2−1) | Δ(3−2) |
|---|---:|---:|---:|---:|---:|
| `cp1` | 0,957 | 0,914 | – | **−0,043** | – |
| `cp2_21` | 0,938 | 0,914 | 1,000 | **−0,023** | **+0,086** |
| `cp3` | 0,249 | 0,278 | 0,383 | +0,030 | **+0,104** |

Ngưỡng thực tế đã công bố trước: +0,020. Độ lệch chuẩn seed đã công bố: 0,065.

---

## 9. Integrated recording-level results

Toàn bộ 81 run đều báo cáo ở cấp recording, không có metric cấp window nào trong bộ YC. Điều này khắc phục hoàn toàn vấn đề bất đối xứng cấp báo cáo từng nêu trong kiểm toán trước.

| Nhóm | Số run | n mỗi run | Khoảng macro-F1 | Ghi chú |
|---|---:|---:|---|---|
| YC1 baseline | 8 | 12 | 0,250 – 0,914 | một split cố định |
| YC2 Support-Point | 48 | 12 | 0,198 – 1,000 | sáu split, không phải LORO |
| YC3 cross-campaign | 8 | 72 | 0,082 – 0,280 | bảy trên tám dưới ngẫu nhiên |
| YC4 sensor config | 17 | 12 | 0,162 – 1,000 | một split cố định |

**Cảnh báo về độ chính xác ước lượng.** Với n = 12, macro-F1 dịch chuyển theo bước 1/12 ≈ 0,083. Khoảng tin cậy Wilson 95 % cho 11/12 là [0,646; 0,985]; cho 12/12 là [0,739; 1,000]; cho 4/12 là [0,138; 0,609]. Chính tài liệu thiết kế của IT nêu con số này và nêu rằng độ lệch chuẩn seed 0,065 lớn hơn độ lệch chuẩn split 0,054.

`TECHNICAL INTERPRETATION.` Hệ quả trực tiếp: **không chênh lệch nào dưới khoảng 0,13 macro-F1 giữa hai cấu hình đơn lẻ trên cùng một split một seed là phân biệt được với nhiễu.** Điều này áp cho toàn bộ so sánh trong YC4, toàn bộ so sánh kiến trúc trong YC1, và phần lớn so sánh giữa các split trong YC2.

Những chênh lệch **vượt** ngưỡng đó và do đó có thể phát biểu: khoảng cách nội campaign so với liên campaign (0,9 xuống 0,1, tức gấp gần chín lần); khoảng cách cp1/cp2 so với cp3; và biên độ giữa các split ở cp3 (0,377 và 0,386).

---

## 10. Cross-campaign boundary

`THESIS APPLICATION.` Phát biểu được phép, và chỉ phát biểu này:

> Trong phạm vi phòng thí nghiệm, bằng chứng trạng thái sinh ra trong một campaign không chuyển giao được sang campaign khác trên cùng khung thép. Trên tám cấu hình được kiểm tra theo hai chiều và hai kiến trúc, bảy cấu hình cho macro-F1 cấp recording dưới mức ngẫu nhiên bốn lớp, mô hình sụp về một lớp chiếm 54 % đến 99 % số dự đoán, và ba cấu hình có ROC-AUC dưới 0,5. Khoảng cách phân bố liên campaign đo bằng energy distance lớn hơn khoảng cách nội campaign khắc nghiệt nhất từ 4,6 đến 6,5 lần.

Phát biểu **không** được phép:

- Không suy rộng sang công trình thực. Ba campaign đều trong phòng thí nghiệm, trên cùng một khung, cách nhau vài tuần.
- Không quy nguyên nhân cho một yếu tố cụ thể. Ba campaign khác nhau về số cụm cảm biến, độ dài bản ghi, siêu tham số huấn luyện và, với CP1 và CP2, về tính ổn định định danh cột. Không thí nghiệm ablation nào tách được các yếu tố này. **Evidence is currently insufficient.**
- Không gọi đây là "mô hình không hoạt động". Nội campaign đạt 0,914–1,000 trên cùng kiến trúc và cùng pipeline.
- Không dùng kết quả này để biện minh cho domain adaptation như một hướng của Paper 1. Đó là hướng khác và nằm ngoài phạm vi đã khóa.

Một điểm cần thầy quyết. Siêu tham số **khác nhau giữa các campaign** (cp1 fc-dim 64 / n-feature-maps 16 / wd 1e-2 / lr 3e-4; cp2 fc-dim 128 / 32 / 1e-2 / 3e-4; cp3 64 / 16 / 3e-2 / 2e-4). Trong thí nghiệm cross-campaign, mô hình được huấn luyện bằng siêu tham số của campaign nguồn rồi áp lên campaign đích. Đây là một confound thật: một phần của thất bại chuyển giao có thể do siêu tham số không phù hợp với đích, chứ không chỉ do domain shift. Cần một lần chạy đối chứng với siêu tham số thống nhất để tách hai nguyên nhân, hoặc cần nêu rõ giới hạn này trong manuscript.

---

## 11. Sensor-configuration findings

`TECHNICAL INTERPRETATION.` Kết quả YC4 **bác bỏ kết luận đã được tuyên bố trước** trong chính tài liệu yêu cầu.

`yeu_cau_cuoi.md` §"Kết quả hướng tới" viết trước khi chạy:

> Dự kiến chứng minh: Hai sensor cải thiện rõ rệt so với một sensor. Ba sensor không cải thiện đáng kể so với hai sensor. Mức tăng từ hai lên ba sensor nhỏ hơn ngưỡng thực tế, ví dụ 2 percentage points Macro-F1. Từ đó đưa ra kết luận: Hai sensor là số lượng đủ cho bài toán.

Dữ liệu, chấm theo đúng quy tắc tổng hợp và đúng metric mà tài liệu đó tự quy định:

- **Hai sensor không cải thiện so với một sensor.** Δ(2−1) = **−0,043** ở `cp1` và **−0,023** ở `cp2_21`, tức âm ở hai trên ba dataset. Chỉ `cp3` dương ở +0,030.
- **Ba sensor cải thiện so với hai sensor, vượt xa ngưỡng đã đặt.** Δ(3−2) = **+0,086** ở `cp2_21` và **+0,104** ở `cp3`, gấp 4 đến 5 lần ngưỡng +0,020.

Chiều của cả hai kết luận dự kiến đều bị đảo.

`TECHNICAL INTERPRETATION` về mức tin cậy. Không kết luận nào theo chiều nào đứng vững, vì cả ba lý do sau đồng thời đúng: mỗi ô là **một split cố định**, **một seed**, và **n = 12**. Mọi Δ trong bảng nằm trong khoảng ±1 độ lệch chuẩn seed (0,065) ngoại trừ Δ(3−2) của `cp3` (0,104), vốn cũng chỉ bằng 1,6 lần độ lệch chuẩn đó.

Trung bình theo số lượng cảm biến cũng che giấu biến thiên lớn giữa các tổ hợp cụ thể. Ở `cp2_21`, hai sensor cho 0,829 đến 1,000 tùy tổ hợp; ở `cp3`, 0,171 đến 0,438. Biên độ trong nhóm lớn hơn chênh lệch giữa các nhóm.

`THESIS APPLICATION.` Toàn bộ YC4 được gắn nhãn **`EXPLORATORY`**. Trong manuscript:

- Báo cáo **từng tổ hợp cụ thể**, không chỉ trung bình theo số lượng.
- Không phát biểu "hai sensor là đủ" và cũng không phát biểu "ba sensor tốt hơn".
- Không dùng cụm "optimal sensor placement" ở bất kỳ đâu.
- Phát biểu được phép: cấu hình cảm biến ảnh hưởng tới kết quả, biên độ giữa các tổ hợp cùng số lượng lớn ngang hoặc lớn hơn biên độ giữa các số lượng, và thiết kế hiện tại chưa đủ để xác định số lượng tối thiểu.

Điều kiện để mở khóa kết luận về số lượng cảm biến tối thiểu, theo đúng yêu cầu đã đặt: cùng model và siêu tham số, lặp qua true LORO fold, nhiều seed, ngưỡng cải thiện xác định trước có cơ sở, và báo cáo cả tổ hợp cụ thể. Hiện đạt một trên năm.

---

## 12. Gate 1 closure matrix

| # | Gate criterion | Required evidence | Artefact/file locator | Finding | Limitation | Status |
|---|---|---|---|---|---|---|
| 1 | Dataset metadata và canonical run registry đã khóa | manifest có version tag và hash; registry ký nghiệm thu | `manifest.json` được `train_ddp_npz.py` đọc nhưng **không có trong bộ bàn giao**; không có `selected_splits.json` | Cấu trúc run/recording nhất quán và kiểm chứng được từ `predictions.json` của 81 run | Không version tag, không hash, không acceptance record; quan hệ 270 file thô ↔ 216 recording chưa có register | **PARTIAL** |
| 2 | Run-aware/leakage-controlled evaluation đã hoàn thành | mã và log chứng minh chia theo run, train-only preprocessing, test không tham gia chọn model | `sensor_signal_analyzer/scripts/train_ddp_npz.py`; 81 `predictions.json` mang tiền tố run | Chống rò rỉ ở cấp cấu trúc: NPZ theo run, kiểm tra run_id chủ động, ép rời nhau train/val/test, chuẩn hóa từng window không dùng thống kê toàn cục, checkpoint chọn theo val | Selection bias có hướng từ Support Points dùng phân bố toàn dataset (mục 6.5); mất cân bằng window 1,88× giữa các recording | **PASS WITH LIMITATION** |
| 3 | True LORO đã hoàn thành | mỗi run làm test đúng một lần, mọi dataset | không tồn tại | Sáu Support-Point split cho mỗi dataset; `cp2_21` chỉ 4/6 run từng làm test, các dataset khác 5/6 | Đây là thiết kế có chủ ý và được biện minh, nhưng không phải LORO | **FAIL** |
| 4 | ResNet1D sensor mode đã xác nhận | manifest đầy đủ 12 trường | mục 7 | 8/12 trường truy được về artefact | Danh tính từng kênh, resultant, sampling rate trong bộ YC, dead-channel handling đều thiếu | **PARTIAL** |
| 5 | Kết quả có thể truy ngược về artefact | prediction, split, config, code, hash | 81 × `{scores,predictions,history}.json` + checkpoint + mã nguồn có test suite | Mọi con số trong báo cáo này truy được về một file cụ thể | Dataset NPZ và `manifest.json` không có; log Kaggle chỉ ở dạng link ngoài; `THREE_CAMPAIGN_REANALYSIS` đã biến mất | **PASS WITH LIMITATION** |
| 6 | Metric chính báo cáo nhất quán ở cấp recording | mọi metric ở cấp recording | `train_ddp_npz.py::evaluate` tổng hợp softmax theo recording rồi argmax | Toàn bộ 81 run ở cấp recording; không metric cấp window nào | n = 12 mỗi run làm bước metric 8,3 %; không có khoảng tin cậy trong artefact | **PASS WITH LIMITATION** |
| 7 | Claim boundary phù hợp laboratory evidence | không claim field, severity, RUL, optimal placement | 6 tài liệu yêu cầu | Không tài liệu nào vượt ranh giới lab | `yeu_cau_cuoi.md` tuyên bố trước kết luận "hai sensor là đủ", bị chính dữ liệu bác bỏ (mục 11) | **PARTIAL** |

### Phán quyết

```
GATE 1 OPEN — PARTIAL EVIDENCE
```

Một tiêu chí `FAIL`, ba `PARTIAL`, ba `PASS WITH LIMITATION`. Tiêu chí 3 tự nó đủ để giữ Gate mở, và theo quy tắc đã đặt, không được tuyên bố Gate đóng khi true LORO hoặc ResNet1D sensor mode chưa được chứng minh từ artefact. Cả hai đều chưa.

---

## 13. Paper 1 claim matrix

| # | Claim | Mức hỗ trợ | Bằng chứng | Giới hạn | Trạng thái |
|---|---|---|---|---|---|
| 1 | Controlled states are distinguishable within campaigns | **Mạnh** | YC2: ResNet1D đạt 1,000 trên 6/6 split của `cp2_21`, 0,833–1,000 trên `cp2_2122`, 0,914–1,000 trên `cp1`. YC1 xác nhận trên split độc lập | Không đúng cho `cp3`, nơi ResNet1D chỉ 0,345–0,731 và 1D-CNN 0,198–0,575. Chưa qua LORO. n = 12 mỗi fold | **Khóa được cho cp1 và cp2, có điều kiện LORO. Chưa khóa cho cp3** |
| 2 | Evidence validity depends on run/campaign provenance | **Mạnh** | Biên độ giữa các split 0,377–0,386 ở `cp3`; e_gap nội campaign 0,0365 (cp1) so với 0,2357 (cp3); e_shift liên campaign 1,08–1,54; 21/72 file CP1 bị hoán vị cảm biến | Thí nghiệm validation hoán vị chưa chạy | **Khóa được** |
| 3 | Cross-campaign transfer is limited | **Rất mạnh** | YC3: 7/8 cấu hình dưới ngẫu nhiên; sụp lớp 54–98,6 %; recall B3 = 0,000 ở 5/8; ROC-AUC < 0,5 ở 3/8 | Chỉ CP2↔CP3, chưa có CP1. Siêu tham số khác nhau giữa campaign là confound | **Khóa được, trong phạm vi CP2↔CP3** |
| 4 | Sensor configuration affects performance | **Trung bình** | YC4: biên độ giữa các tổ hợp cùng số lượng 0,171–0,438 ở `cp3`, 0,829–1,000 ở `cp2_21` | Một split, một seed, n = 12. Mọi Δ trong nhiễu seed | **`EXPLORATORY`, chưa khóa** |
| 5 | Sensor configuration influences performance more strongly than architecture choice | **Không đủ** | – | Không thí nghiệm nào bắt chéo cấu hình cảm biến với kiến trúc. YC4 chỉ chạy một kiến trúc; YC1 và YC2 chỉ chạy một cấu hình cảm biến | **Không phát biểu được. Evidence is currently insufficient.** |

### Phân loại kết quả cho manuscript

**Kết quả chính:** thất bại chuyển giao liên campaign kèm cơ chế sụp lớp (YC3); phân biệt trạng thái nội campaign dưới đánh giá run-aware (YC1, YC2); phát hiện và sửa hoán vị định danh cảm biến trên 21/72 file CP1 (YC1).

**Kết quả bổ trợ:** so sánh ResNet1D với 1D-CNN; đặc trưng dataset bằng Fisher ratio và energy distance; control buổi đo qua cặp `cp2_21` / `cp2_2122`.

**Negative result có giá trị:** YC3 toàn bộ; và việc `cp3` không khớp nổi tập huấn luyện, cho thấy độ khó nằm ở dữ liệu chứ không ở dung lượng mô hình.

**Chỉ exploratory:** toàn bộ YC4.

**Claim phải bỏ:** "hai sensor là đủ"; mọi xếp hạng kiến trúc có ý nghĩa thống kê; mọi phát biểu về sensor placement.

**Bảng và hình cần đưa vào manuscript:** bảng đặc trưng dataset (Fisher ratio, e_gap, window/recording); bảng LORO coverage (mục 6.2, để minh bạch thiết kế); bảng YC3 đầy đủ kèm tỉ lệ sụp lớp và recall từng lớp; bảng YC2 theo vai trò split; bảng YC4 từng tổ hợp; hình phân bố lớp dự đoán của ca `cp2_21 → cp3` với 98,6 % dồn một lớp.

---

## 14. CEI-Lab / Gate 2 handoff

`THESIS APPLICATION.` Đề xuất bản ghi tối thiểu, dựng **hoàn toàn từ trường đã kiểm chứng trong artefact**. Ví dụ dưới đây lấy từ một recording thật trong `Output_yc2_Sensor_Configuration/cp2_21_resnet1d_v5_split3/ddp_seed42/predictions.json`.

| Trường | Giá trị ví dụ | Nguồn trong artefact | Trạng thái |
|---|---|---|---|
| `Condition_Evidence_ID` | `CE-LAB-cp2_21-R7-d21_BS0L1R7-resnet1d_v5-s42` | dựng từ các trường bên dưới | đề xuất |
| `Dataset_View_ID` | `cp2_21` | tên thư mục, `--dataset-name` | `SOURCE-VERIFIED` |
| `Campaign_ID` | `CP2` | ánh xạ view → campaign vật lý | `SOURCE-VERIFIED` |
| `Session_ID` | `d21` | tiền tố trong `recording_id` | `SOURCE-VERIFIED` |
| `Run_ID` | `R7` | tiền tố `R{n}:` trong `recording_id` | `SOURCE-VERIFIED` |
| `Recording_ID` | `d21_BS0L1R7` | `predictions.json.recording_id` | `SOURCE-VERIFIED` |
| `Sensor_configuration` | 3 cụm, 12 kênh | `--expected-channels`, tài liệu YC1 | `PARTIAL`, danh tính kênh chưa xác nhận |
| `Sensor_ID` | – | – | **`EVIDENCE INSUFFICIENT`** |
| `Controlled_state_label` | `Healthy` | `predictions.json.true` + `class_map` | `SOURCE-VERIFIED` |
| `Model_version` | `resnet1d_v5`, `n_feature_maps=32` | tên thư mục, `yeu_cau_1` | `SOURCE-VERIFIED` |
| `Split_protocol` | Support Points, split 3, role coverage, train R9–R12 / val R8 / test R7 | `yeucau2daolaicacruntrongcungCP.md` + `predictions.json` | `SOURCE-VERIFIED` |
| `Seed` | 42 | tên thư mục `ddp_seed42` | `SOURCE-VERIFIED` |
| `Predicted_state` | `Healthy` | `predictions.json.pred` | `SOURCE-VERIFIED` |
| `Model_score` | vector 4 phần tử từ `probabilities` | `predictions.json.probabilities` | `SOURCE-VERIFIED` |
| `Calibration_status` | `NOT_ASSESSED` | không có artefact hiệu chuẩn | `SOURCE-VERIFIED` |
| `Quality_provenance_flag` | `SENSOR_PERMUTATION_CORRECTED` với CP1; `SESSION_MIXED` với `cp2_2122` | YC1 | `PARTIAL` |
| `Validation_scope` | `WITHIN_VIEW_SUPPORT_POINT_SPLIT_ONLY`; `CROSS_CAMPAIGN_TRANSFER_NOT_SUPPORTED` | YC2 và YC3 | `SOURCE-VERIFIED` |
| `Timestamp_hash` | – | không có artefact | **`EVIDENCE INSUFFICIENT`** |

Ba quy tắc bắt buộc kèm bản ghi:

`Model_score` là điểm số mô hình, **không phải** physical severity và **không phải** calibrated confidence, vì `Calibration_status = NOT_ASSESSED`. Guo et al. (ICML 2017) và Ovadia et al. (NeurIPS 2019) là cơ sở để phân biệt hai khái niệm này.

`Validation_scope` là **trường bắt buộc**, không phải chú thích. Kết quả YC3 làm nó bắt buộc: một bản ghi không mang phạm vi hiệu lực sẽ bị diễn giải sai khi đọc lại.

`Sensor_ID` chưa gán được. Đây là mắt xích đầu tiên của chuỗi định danh đã khóa, và nó cần `manifest.json` cùng ánh xạ kênh để đóng.

**Artefact sẵn sàng chuyển sang Gate 2:** 81 bộ `predictions.json` với `recording_id` mang cấu trúc `Run:Session_Recording`, đủ để sinh `Condition_Evidence_ID` và `Model_score` cho **972 recording-level evidence object** (81 × 12, trong đó YC3 đóng góp 72 mỗi run). Đây là payload thực, không phải mẫu.

---

## 15. Remaining actions

### BLOCKER — chặn Gate 1

| # | Việc | Vì sao chặn | Khối lượng |
|---|---|---|---|
| B1 | **Chạy true outer LORO**: 4 dataset × 6 fold × 2 kiến trúc × 3 seed = 144 run, mỗi run làm test đúng một lần, quy tắc chọn val công bố trước | Tiêu chí Gate 1 số 3 đang `FAIL` | Lớn, nhưng là việc duy nhất tốn tính toán |
| B2 | **Khóa canonical run registry**: dataset version tag, hash, `manifest.json`, ánh xạ 270 file thô → 216 recording, acceptance record ký | Tiêu chí 1 đang `PARTIAL` | Nhỏ, chủ yếu là tài liệu |
| B3 | **Hoàn tất ResNet1D sensor-mode manifest**: bàn giao `manifest.json` và một NPZ mẫu; ghi rõ danh tính 8 và 12 kênh, có resultant hay không, sampling rate, xử lý dead channel | Tiêu chí 4 đang `PARTIAL` | Nhỏ, là việc bàn giao |

### REQUIRED — chặn manuscript, không chặn Gate

| # | Việc | Vì sao |
|---|---|---|
| R1 | Chạy thí nghiệm validation hoán vị cảm biến theo đúng §4 của `sensor_position_permutation_synchronization.md`: tiêm hoán vị đã biết, báo cáo Exact Recovery Rate và Sensor-wise Accuracy ở 5–40 % nhiễu | Đóng góp "sửa được 21/72 file" hiện dựa trên chỉ báo nội tại, chưa có kiểm chứng ngoài |
| R2 | Chốt ánh xạ B1/B2/B3 sang liên kết vật lý từ nhật ký thí nghiệm | Không viết được Methods; mọi diễn giải theo lớp đang có điều kiện |
| R3 | Thu hồi `THREE_CAMPAIGN_REANALYSIS` vào một vị trí có kiểm soát phiên bản | Toàn bộ kết quả RF/SVM/LogReg và permutation control 300 dòng đang không truy được |
| R4 | Chạy một lần đối chứng cross-campaign với siêu tham số thống nhất giữa các campaign | Tách confound siêu tham số khỏi domain shift trong YC3 |
| R5 | Sửa mọi tài liệu Paper 1 đang ghi "6 kênh / 9 kênh" thành 8 và 12 | Sai số kênh trong tài liệu hiện hành |
| R6 | Cập nhật tài liệu quản trị: ResNet1D đã chạy; LORO chưa chạy | Trạng thái quản trị đang ngược với artefact ở cả hai vế |

### OPTIONAL

| # | Việc | Giá trị |
|---|---|---|
| O1 | Khôi phục bước cắt cửa sổ chung 40 s, hoặc cân bằng ở tầng sampler | Triệt tiêu mất cân bằng window 1,88× |
| O2 | Kiểm tra recording CP2 dài 12.635 mẫu: đo dài thật hay lỗi ghi | Câu hỏi do chính IT nêu và chưa trả lời |
| O3 | Chạy Phase 2 của YC3 | Mục để trống trong `yeucau3kiemtracheo.md` |
| O4 | Permutation control cho các fold LORO dùng làm bằng chứng chính, ≥ 1.000 hoán vị | Nâng độ mạnh phát biểu |
| O5 | Bắt chéo cấu hình cảm biến × kiến trúc | Điều kiện duy nhất để claim 5 có thể được xét |

---

## 16. Claim → Evidence → Limitation → Next action

**Claim.** Bộ YC1–YC4 đưa Paper 1 từ trạng thái không có artefact kiểm chứng được sang trạng thái có 81 lần chạy truy vết đầy đủ, pipeline chống rò rỉ được xác minh ở cấp mã nguồn, và một kết quả chuyển giao âm tính đủ mạnh để làm kết quả chính. Gate 1 vẫn mở vì true LORO chưa tồn tại.

**Evidence.** 81 bộ `{scores, predictions, history}.json` cấp recording; `train_ddp_npz.py` với sáu cơ chế chống rò rỉ kiểm chứng được ở cấp mã; 6 tài liệu yêu cầu đặc tả đầy đủ thiết kế; YC3 với 7/8 cấu hình dưới ngẫu nhiên và sụp lớp tới 98,6 %; YC1 với Fisher ratio và e_gap giải thích độ khó của `cp3` độc lập với mô hình.

**Limitation.** True LORO chưa chạy ở bất kỳ dataset nào; `cp2_21` chỉ 4/6 run từng làm test. Chỉ một seed, trong khi độ lệch chuẩn seed 0,065 do chính IT đo được lớn hơn độ lệch chuẩn giữa các split. n = 12 mỗi fold khiến metric dịch theo bước 8,3 %. Dataset NPZ và `manifest.json` không có trong bộ bàn giao. Thí nghiệm validation thuật toán sửa hoán vị cảm biến chưa chạy. Ánh xạ nhãn sang liên kết vật lý vẫn chưa có. Siêu tham số khác nhau giữa campaign là confound chưa tách trong YC3.

**Next action.** B3 và B2 trước, vì chúng là việc bàn giao và tài liệu, chi phí thấp, và mở khóa hai tiêu chí `PARTIAL`. Sau đó R2 (một lần tra nhật ký). Rồi B1, việc duy nhất tốn tính toán. R1 chạy song song vì độc lập với B1.

---

## Trả lời năm câu hỏi

**1. Gate 1 đã khóa được chưa?**
Chưa. `GATE 1 OPEN — PARTIAL EVIDENCE`. Một tiêu chí `FAIL` (true LORO), ba `PARTIAL`, ba `PASS WITH LIMITATION`.

**2. Còn chính xác bao nhiêu blocker?**
**Ba.** True outer LORO chưa chạy; canonical run registry chưa khóa và `manifest.json` chưa bàn giao; ResNet1D sensor-mode manifest thiếu bốn trường. Hai trong ba là việc bàn giao và tài liệu; chỉ blocker thứ nhất cần tài nguyên tính toán.

**3. Công việc IT tối thiểu cần bổ sung là gì?**
Bàn giao `manifest.json`, một `R{run}.npz` mẫu và bảng danh tính kênh, kèm dataset version tag và hash. Sau đó chạy 144 run true LORO (4 dataset × 6 fold × 2 kiến trúc × 3 seed) với quy tắc chọn validation run công bố trước. Song song, chạy thí nghiệm tiêm hoán vị cảm biến để có Exact Recovery Rate. Không yêu cầu thu thập dữ liệu mới.

**4. Paper 1 hiện có thể viết đến mức nào?**
Viết được **toàn bộ trừ phần Results chính**. Introduction, Literature Background, Materials and Methods, Dataset và provenance, phần cross-campaign của Results, Discussion, Conclusions và phần bàn giao CEI đều đã đủ bằng chứng. Ba claim khóa được: phân biệt trạng thái nội campaign cho `cp1` và `cp2` (có điều kiện LORO), phụ thuộc của độ tin cậy vào provenance, và giới hạn chuyển giao liên campaign. Hai claim chưa khóa: ảnh hưởng cấu hình cảm biến (`EXPLORATORY`) và so sánh cấu hình với kiến trúc (`EVIDENCE INSUFFICIENT`). Bảng hiệu năng nội campaign phải chờ LORO trước khi thành kết quả chính; hiện chúng vào bài như Support-Point sensitivity analysis.

**5. Artefact nào đã sẵn sàng chuyển sang Gate 2?**
Sẵn sàng: 81 bộ `predictions.json` với `recording_id` cấu trúc `Run:Session_Recording`, đủ sinh `Condition_Evidence_ID`, `Model_score`, `Predicted_state`, `Controlled_state_label`, `Run_ID`, `Session_ID`, `Recording_ID`, `Split_protocol`, `Seed`, `Model_version` và `Validation_scope` cho từng recording. `Calibration_status = NOT_ASSESSED` đi kèm bắt buộc.
Chưa sẵn sàng: `Sensor_ID` (cần `manifest.json` và ánh xạ kênh) và `Timestamp_hash` (chưa có artefact). Hai trường này chặn mắt xích đầu của chuỗi định danh đã khóa và phải đóng trước khi Gate 2 nhận payload.
