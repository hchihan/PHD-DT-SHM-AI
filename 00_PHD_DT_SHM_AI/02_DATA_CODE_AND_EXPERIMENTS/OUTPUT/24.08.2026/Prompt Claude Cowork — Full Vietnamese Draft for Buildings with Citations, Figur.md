Bạn là senior academic researcher, scientific writer và research-data analyst chuyên về:

- structural/building condition monitoring;
- vibration-based monitoring;
- machine-learning validation;
- leakage-safe evaluation;
- experimental steel structures;
- research methodology;
- building inspection and asset-management information.

Nhiệm vụ lần này là **tạo một bản thảo Paper 1 tiếng Việt gần mức submission-ready cho tạp chí Buildings (MDPI)**.

Không chỉ tạo outline.

Không chỉ mô tả “cần bảng/hình”.

Hãy **thực sự tạo và chèn các bảng, hình, trích dẫn và danh mục tài liệu tham khảo có thể tạo được từ toàn bộ thư viện và kết quả hiện có**.

Chỉ những nội dung thực sự chưa đủ evidence mới được để placeholder.

---

# 1. OUTPUT DUY NHẤT

Tạo một manuscript chính:

```text
PAPER1_BUILDINGS_VIETNAMESE_DRAFT_v0.2.md
```

Ngoài file `.md` này, được phép tạo một thư mục phụ chỉ để chứa các hình do chính bạn tổng hợp:

```text
PAPER1_BUILDINGS_FIGURES/
```

Ví dụ:

```text
PAPER1_BUILDINGS_FIGURES/
├── Fig01_Research_Design.png
├── Fig02_LORO_Protocol.png
├── Fig03_Within_Campaign_Performance.png
├── Fig04_Sensor_Configuration.png
├── Fig05_Cross_Campaign_Degradation.png
└── Fig06_Cross_Campaign_Confusion.png
```

Không tạo thêm các report `.md` phụ.

Mọi audit, notes và completion checklist phải nằm cuối manuscript chính.

---

# 2. TARGET JOURNAL — BUILDINGS

Target:

**Buildings — MDPI**

Article type:

**Article**

Trước khi viết, phải kiểm tra phiên bản hiện hành của:

- Buildings Aims & Scope;
- Instructions for Authors;
- manuscript structure;
- abstract requirement;
- keywords;
- citation/reference style;
- figure/table requirements;
- Data Availability Statement;
- Supplementary Materials;
- Author Contributions;
- Funding;
- Conflict of Interest;
- các back-matter khác của MDPI.

Không tự suy đoán journal requirement.

Đầu file tạo:

## Journal Compliance Note

ghi ngắn gọn:

| Item | Buildings requirement | Manuscript status |
|---|---|---|
| Article type | | |
| Abstract | | |
| Keywords | | |
| Main structure | | |
| Citation style | | |
| Figures | | |
| Tables | | |
| Data Availability | | |
| Supplementary Materials | | |

Nếu không xác minh được:

> **[CẦN XÁC MINH YÊU CẦU BUILDINGS]**

---

# 3. RESEARCH ALIGNMENT — KHÓA

Paper thuộc:

- **RQ1**
- **WP1 — Laboratory vibration evidence**
- **Chapter 4**
- **Paper 1**
- **Evidence Gate 1**

RQ1:

> How reliably can vibration data from the 1:10 steel frame model and different sensor configurations produce evidence distinguishing controlled connection states under a run-aware, leakage-controlled evaluation protocol?

Chuỗi luận án:

```text
Vibration data
→ condition/state-change evidence
→ BIM-linked component
→ inspection record
→ inspection-maintenance action support
```

Paper này chỉ nghiên cứu:

```text
Vibration data
→ trustworthy laboratory condition evidence
```

Không phát triển:

- BIM traceability;
- Inspection_Record;
- Action_Status;
- field damage diagnosis;
- predictive maintenance;
- RUL;
- calibrated FEM.

---

# 4. QUYẾT ĐỊNH CP2 ĐÃ KHÓA

Thông tin mới đã được tác giả xác nhận:

```text
CANONICAL CP2 = CP2_21
```

CP2_21:

- bốn trạng thái Healthy/B1/B2/B3;
- cùng measurement session ngày 21/07;
- không vay B3 từ ngày khác;
- được sử dụng làm nhánh CP2 chính trong Paper 1.

Do đó:

**KHÔNG còn để placeholder “cần xác nhận CP2 branch”.**

Trong manuscript phải ghi rõ:

> CP2_21 was retained as the canonical CP2 dataset because all four controlled connection states were acquired within the same measurement session, thereby avoiding the class-aligned session confounding inherent in the alternative CP2_2122 construction.

Bản tiếng Việt diễn đạt tự nhiên tương ứng.

CP2_2122:

- không phải main dataset;
- chỉ được nhắc nếu cần trong phần data governance / sensitivity rationale;
- không dùng để tạo headline performance.

Không lựa chọn CP2_21 vì accuracy cao.

Lý do là **experimental validity / confounding control**.

---

# 5. SOURCE OF TRUTH

Đọc toàn bộ các nguồn hiện có trong workspace trước khi viết.

Ưu tiên theo thứ tự:

## A. Research governance

```text
MASTER_RESEARCH_CHARTER.md
MASTER_RESEARCH_CHARTER_v1.1_LIMITED_FEM_20260717.md
RESEARCH_DIRECTION_AND_SCOPE.md
RESEARCH_ARCHITECTURE.md
CURRENT_STATUS_AND_NEXT_DIRECTION.md
```

## B. Gate 1 evidence

```text
GATE1_LORO_UPDATED_RESULTS_AUDIT_20260824.md
Note.md
Readme.md / Readme(3).md
```

và toàn bộ:

```text
signal_loro_v1/
loro-each-sensor-v1/
ml_loro_v1/
loro-cross-campaign-v1/
```

## C. Literature libraries

Hãy sử dụng **TẤT CẢ thư viện tài liệu học thuật hiện có và truy cập được trong Project/workspace**, gồm nếu tồn tại:

- Zotero library;
- Zotero exports;
- Living Evidence Base;
- canonical evidence records;
- deep-read records;
- DOI-verified lists;
- literature gap files;
- citation audit files;
- Paper 1 literature folders;
- `.bib`;
- `.ris`;
- `.enw`;
- `.csv`;
- `.json`;
- `.md`;
- PDF papers;
- previous manuscripts;
- literature matrices;
- NotebookLM-exported notes nếu có trong workspace;
- reference lists của các bài cốt lõi.

Không giới hạn ở tài liệu đã từng xuất hiện trong manuscript cũ.

---

# 6. QUY TẮC TRÍCH DẪN — BẮT BUỘC

Mục tiêu lần này là **chèn citation thật vào manuscript**, không chỉ để:

```text
[CẦN TRÍCH DẪN]
```

nếu thư viện hiện có đã có nguồn phù hợp.

## Evidence hierarchy

Ưu tiên:

1. DOI verified;
2. full-text/deep-read;
3. canonical evidence;
4. metadata verified;
5. nguồn chính thức của journal/standard.

Không sử dụng citation chỉ vì title có vẻ phù hợp.

Phải kiểm tra source thực sự hỗ trợ claim.

## Không được bịa

Không được invent:

- author;
- year;
- title;
- DOI;
- journal;
- volume;
- pages;
- standards;
- metrics.

Nếu nguồn chưa đủ:

> **[CẦN TRÍCH DẪN: mô tả chính xác claim cần evidence]**

## Citation format

Vì target là Buildings/MDPI:

- sử dụng citation numbering `[1]`, `[2]`, `[3–5]` trong body;
- cuối manuscript tạo **References** theo format gần nhất với Buildings/MDPI;
- numbering phải theo thứ tự xuất hiện.

Không dùng `(Author, Year)` trong bản v0.2 nếu metadata đủ.

---

# 7. LITERATURE SEARCH STRATEGY

Không cần nhồi nhiều citation.

Ưu tiên literature phục vụ trực tiếp 6 nhóm claim:

### L1 — vibration-based structural condition monitoring

### L2 — machine learning/deep learning in SHM

### L3 — leakage / non-independent segmentation / grouped validation

### L4 — leave-one-run/group/session-out evaluation

### L5 — domain shift / distribution shift / cross-domain generalization in SHM

### L6 — provenance / trustworthy condition evidence / uncertainty and scope of validity

Đặc biệt tìm các paper trong:

- Buildings;
- Structural Control and Health Monitoring;
- Journal of Civil Structural Health Monitoring;
- Mechanical Systems and Signal Processing;
- Measurement;
- Engineering Structures;
- Automation in Construction;
- Sensors;
- Smart Structures and Systems;

nhưng chỉ sử dụng nếu thực sự liên quan.

Không cố trích dẫn Buildings một cách nhân tạo.

---

# 8. NARRATIVE KHOA HỌC CHÍNH

Không viết:

> AI đạt độ chính xác rất cao.

Không lấy sensor configuration làm hero contribution.

Không viết paper như model benchmark.

Narrative chính:

> **High within-campaign classification performance does not necessarily establish transportability across independent measurement campaigns. Reliable vibration-based laboratory condition evidence therefore requires run-aware leakage-controlled evaluation, explicit characterization of run/campaign dependence, and preservation of provenance and the evaluated scope of validity.**

Trong tiếng Việt cần diễn đạt học thuật, gọn và không overclaim.

---

# 9. QUY TẮC VỀ “CAMPAIGN EFFECT”

Không causal claim:

> session effect caused the failure.

Nếu metadata chưa đủ.

Dùng:

> **campaign-associated distribution shift**

hoặc:

> sự dịch chuyển phân bố gắn với campaign đo.

Có thể thảo luận các hypothesis:

- sensor remounting;
- acquisition-chain differences;
- excitation differences;
- experimental reassembly;
- channel alignment;
- environmental variation;

nhưng bắt buộc ghi:

> **hypothesis, not confirmed**

nếu chưa có evidence trực tiếp.

---

# 10. QUY TẮC VỀ SAMPLE SIZE — BẮT BUỘC

Đây là yêu cầu rất quan trọng.

Mỗi campaign có:

```text
6 independent experimental runs
72 unique recordings
```

30 LORO permutations không phải 30 independent experiments.

Mỗi held-out run xuất hiện dưới nhiều train/validation configurations.

Do đó:

- independent experimental unit = run;
- recording = lower-level observational unit;
- repeated model evaluations ≠ independent new recordings.

Không được viết:

> 360 independent recordings.

Nếu:

```text
72 unique recordings × 5 repeated model evaluations
```

thì phải diễn giải đúng.

Tương tự cross-campaign:

```text
72 unique target recordings
× 6 source-model variants
= 432 prediction decisions
```

Không gọi 432 independent observations.

---

# 11. MAIN RESULTS — SỬ DỤNG TRỰC TIẾP

Khai thác toàn bộ số liệu đã audit.

Không nhập lại bằng tay nếu có thể đọc trực tiếp từ CSV/JSON.

## Deep learning

Ví dụ:

### CP1

ResNet1D:

```text
Macro-F1 ≈ 0.940
```

### CP2_21

ResNet1D:

```text
Macro-F1 ≈ 0.955
```

### CP3

ResNet1D:

```text
Macro-F1 ≈ 0.533
```

với variability lớn.

## Classical ML

Khai thác:

- Random Forest;
- Extra Trees;
- Histogram Gradient Boosting;
- RBF-SVM.

CP3 Random Forest:

```text
Macro-F1 ≈ 0.846
```

nếu audit/source xác nhận.

## Cross-campaign

CP2_21 → CP3 ResNet1D:

```text
Macro-F1 ≈ 0.114
```

CP3 → CP2_21:

```text
Macro-F1 ≈ 0.147
```

1D-CNN:

```text
≈ 0.19–0.23
```

Báo explicit class collapse.

Không dùng con số từ summary audit nếu raw artefact mâu thuẫn.

Raw outputs + run_info + predictions ưu tiên hơn narrative text.

---

# 12. TẠO BẢNG THẬT — KHÔNG CHỈ ĐỀ XUẤT

Tạo và chèn trực tiếp các bảng Markdown hoàn chỉnh trong manuscript.

## Table 1 — Experimental Campaigns and Dataset Structure

Các cột dự kiến:

| Campaign | Canonical dataset | Independent runs | Unique recordings | States | Sensor configuration | Remarks |

CP2 phải ghi rõ:

```text
CP2_21 — canonical
```

Không ghi CP2_2122 như main dataset.

---

## Table 2 — Controlled Connection States

| Label | Controlled state | Connection location | Experimental modification | Interpretation boundary |

Không gọi severity.

Thiếu physical detail thì placeholder cụ thể.

---

## Table 3 — Leakage-Safe Run-Aware Evaluation Protocol

Ví dụ:

| Evaluation element | Protocol | Leakage-control rationale |

Bao gồm:

- run-level partition;
- preprocessing;
- recording-level aggregation;
- model selection;
- test isolation.

---

## Table 4 — Main Within-Campaign Results

Ưu tiên bảng không quá rộng.

Các hàng:

```text
CP1
CP2_21
CP3
```

và các representative pipelines cần thiết.

Cột:

- Macro-F1;
- Balanced Accuracy;
- Accuracy;
- fold/run dispersion;
- worst held-out run.

Không dump toàn bộ model nếu không cần.

---

## Table 5 — Sensor Configuration Results

Chỉ giữ các kết quả có giá trị diễn giải.

Có thể full table đưa Supplementary.

Main paper ưu tiên:

- best representative;
- single sensor;
- multi-sensor;
- evidence rằng more sensors ≠ always better.

Không gọi optimal.

---

## Table 6 — Cross-Campaign Evaluation

| Source campaign | Target campaign | Pipeline | Macro-F1 | Balanced Accuracy | Main failure pattern |

Đánh dấu 4-class chance reference nếu phù hợp.

---

## Table 7 — Claim–Evidence–Limitation Matrix

Nếu quá management-oriented để đưa paper thì giữ trong:

```text
INTERNAL COMPLETION CHECKLIST
```

không đưa final publication.

---

# 13. TẠO FIGURE THẬT TỪ RESULT FILES

Không chỉ viết:

> [CẦN HÌNH]

nếu dữ liệu đã đủ để tạo hình.

Dùng Python/R hoặc plotting tools hiện có trong workspace để tạo publication-quality figures.

Không thay đổi số liệu.

---

## Figure 1 — Research and Evaluation Design

Tạo schematic:

```text
Controlled steel-frame experiment
        ↓
Campaign
        ↓
Run
        ↓
Recording
        ↓
Window
        ↓
Run-aware train/validation/test
        ↓
Recording-level evidence
```

Đồng thời thể hiện:

```text
Within-campaign LORO
vs.
Cross-campaign evaluation
```

Hình phải rõ và đơn giản.

---

## Figure 2 — LORO Protocol

Minh họa 6 runs:

```text
R1 R2 R3 R4 | R5 | R6
 Train      | Val| Test
```

và các permutation.

Phải có chú thích:

> multiple permutations do not represent independent test populations.

---

## Figure 3 — Within-Campaign Performance

Tạo từ raw `summary.csv`.

Ưu tiên:

- x-axis = campaign;
- y-axis = macro-F1;
- individual held-out run results;
- mean/dispersion.

Không chỉ bar chart mean.

Cần cho reviewer nhìn thấy:

```text
CP1 stable
CP2_21 stable
CP3 variable
```

---

## Figure 4 — Sensor Configuration Sensitivity

Tạo từ:

```text
loro-each-sensor-v1/
```

Ưu tiên plot thể hiện:

- CP1;
- CP2_21;
- CP3;

và các:

```text
s1
s2
s3
s12
s13
s23
s123
```

Nếu physical identity của S1/S2/S3 chưa verified:

chỉ ghi `S1/S2/S3`, không tự gọi AP/BCJ/BR.

---

## Figure 5 — Intra- vs Cross-Campaign Degradation

Đây là một trong hai figures quan trọng nhất.

Hiển thị rõ:

```text
within CP2_21 → ~0.95
CP2_21 → CP3 → ~0.11–0.19
```

và chiều ngược lại.

Đánh dấu chance-level phù hợp nếu metric cho phép.

---

## Figure 6 — Cross-Campaign Class Collapse

Tạo normalized confusion matrices.

Ưu tiên:

- CP2_21 → CP3 ResNet1D;
- CP3 → CP2_21 ResNet1D hoặc representative pipeline khác.

Không lấy 432 decisions để mô tả như 432 unique recordings.

Caption phải ghi rõ:

> aggregated predictions from six source-model variants applied repeatedly to the same 72 unique target recordings.

---

# 14. FIGURE CAPTIONS

Mỗi hình phải có caption hoàn chỉnh như submission.

Ví dụ:

> **Figure 5.** Comparison between within-campaign and cross-campaign recording-level classification performance. Cross-campaign results represent repeated evaluations of the same 72 unique target recordings using models trained under six source-campaign train/validation configurations; these evaluations are not independent target samples.

Viết bản tiếng Việt tương ứng.

---

# 15. RESULTS STRUCTURE

## 3.1 Dataset and Evaluation Completeness

## 3.2 Within-Campaign Run-Aware Reliability

## 3.3 Run-to-Run Variability

Đặc biệt R12 / R16 nếu raw evidence xác nhận.

## 3.4 Sensor-Configuration Sensitivity

## 3.5 Sensitivity to Analytical Pipeline

Dùng:

> analytical pipeline

không phải pure architecture.

## 3.6 Cross-Campaign Transportability

Đây là main finding.

## 3.7 Class-Level Failure Patterns

Healthy↔B1 nếu supported.

Không viết:

> physically expected

nếu chưa có evidence.

---

# 16. DISCUSSION STRUCTURE

## 4.1 What High Within-Campaign Performance Establishes

Chỉ chứng minh:

> discrimination within the tested laboratory evaluation envelope.

---

## 4.2 Why Run-Aware Evaluation Is Necessary

Dùng R12/R16 như evidence về hidden run dependence.

---

## 4.3 Within-Campaign Reliability Does Not Establish Cross-Campaign Transportability

Đây là central Discussion.

Kết nối với literature về domain/distribution shift.

---

## 4.4 Implications for Trustworthy Condition Evidence

Thảo luận:

```text
Predicted state
+ uncertainty/confidence
+ provenance
+ evaluated scope
→ interpretable laboratory condition evidence
```

Không xây schema BIM.

---

## 4.5 Sensor Configuration

Nhấn mạnh:

- sensor choice matters;
- more sensors are not necessarily better;
- effect depends on campaign/pipeline.

Không nói optimal.

---

## 4.6 Implications for Building Inspection and Asset Management

Chỉ 1–2 đoạn.

Ý chính:

> evidence used for inspection support must carry information about where, when and under what validated conditions it was produced.

Không chuyển thành Paper 2.

---

## 4.7 Limitations

Bao gồm:

- one scaled specimen;
- controlled laboratory states;
- six independent runs/campaign;
- limited campaigns;
- repeated split evaluations not independent experiments;
- single seed nếu chưa rerun;
- channel mapping nếu chưa verified;
- acquisition-order confounding nếu chưa checked;
- no field diagnosis;
- no quantitative lab→field transfer;
- no severity;
- no universal model superiority.

---

# 17. MULTI-SEED

Nếu multi-seed chưa chạy:

không bỏ toàn bộ current results.

Sử dụng current single-seed results và ghi rõ:

> **[BLOCKING BEFORE SUBMISSION: cập nhật kết quả multi-seed cho các headline configurations; các SD hiện tại phản ánh variability giữa LORO splits/runs, không phải random-seed variability.]**

Đừng để placeholder ở mọi bảng.

Chỉ đặt một note rõ trong Methods/Results/Table footnote và completion checklist.

---

# 18. SENSOR MAPPING

ResNet1D sensor mode đã được verified.

Được phép viết:

> multi-sensor early fusion at raw-channel level.

Nhưng nếu physical mapping chưa verified:

không tự gán:

```text
S1 = AP
S2 = BCJ
S3 = BR
```

Đặt:

> **[CẦN XÁC MINH METADATA: physical mapping của S1/S2/S3 và channel order giữa CP2_21 và CP3.]**

---

# 19. MANUSCRIPT STRUCTURE — BUILDINGS

Tạo manuscript hoàn chỉnh:

# Title

3 candidates.

Đánh dấu:

**Recommended Title**

# Abstract

Khoảng yêu cầu Buildings hiện hành.

Viết hoàn chỉnh bằng tiếng Việt.

Chỉ dùng số liệu đã đủ evidence.

# Keywords

# 1. Introduction

# 2. Materials and Methods

## 2.1 Research Design
## 2.2 Scaled Steel-Frame Specimen
## 2.3 Controlled Connection States
## 2.4 Instrumentation and Excitation
## 2.5 Experimental Campaigns and Runs
## 2.6 Data Preparation
## 2.7 Run-Aware Leakage-Safe Evaluation
## 2.8 Recording-Level Aggregation
## 2.9 Analytical Pipelines
## 2.10 Sensor Configuration Analysis
## 2.11 Cross-Campaign Evaluation
## 2.12 Performance Measures

# 3. Results

theo cấu trúc §15.

# 4. Discussion

theo cấu trúc §16.

# 5. Conclusions

# Supplementary Materials

# Author Contributions

# Funding

# Institutional Review Board Statement

# Informed Consent Statement

# Data Availability Statement

# Acknowledgments

# Conflicts of Interest

# References

---

# 20. SUPPLEMENTARY MATERIAL

Đề xuất Supplementary giữ:

- full 30 LORO permutations;
- all sensor configurations;
- all four ML pipelines;
- complete confusion matrices;
- model hyperparameters;
- seed/split/model version;
- provenance fields;
- detailed CP3 results;
- detailed cross-campaign prediction tables.

Main article không được biến thành result dump.

---

# 21. REFERENCES

Cuối manuscript phải có **reference list thật**.

Mục tiêu sơ bộ:

```text
~35–60 references
```

nhưng chất lượng quan trọng hơn số lượng.

Ưu tiên:

- recent 2020–2026 literature cho current state;
- seminal older references khi thực sự cần;
- closest-method studies;
- Buildings articles liên quan;
- run-aware/leakage/domain-shift literature.

Mỗi reference phải có nguồn kiểm chứng.

Nếu DOI có:

đưa DOI.

Nếu không có DOI nhưng metadata verified:

giữ reference và không bịa DOI.

---

# 22. CITATION AUDIT CUỐI CÙNG

Cuối manuscript, sau References, thêm:

# INTERNAL CITATION AUDIT — REMOVE BEFORE SUBMISSION

Bảng:

| Ref. | Claim supported | Source location | Full text read? | DOI verified? | Keep? |
|---|---|---|---|---|---|

Mục này để nội bộ, không thuộc manuscript submission.

---

# 23. FIGURE/TABLE AUDIT

Tiếp theo:

# INTERNAL FIGURE AND TABLE AUDIT — REMOVE BEFORE SUBMISSION

| ID | Source data | Generated? | Final? | Remaining issue |
|---|---|---|---|---|

---

# 24. COMPLETION CHECKLIST

Cuối cùng:

# INTERNAL COMPLETION CHECKLIST — REMOVE BEFORE SUBMISSION

Tổng hợp tất cả:

```text
[CẦN BỔ SUNG...]
[CẦN XÁC MINH...]
[CẦN TRÍCH DẪN...]
[BLOCKING BEFORE SUBMISSION...]
```

Nhưng phải cố gắng giải quyết tối đa bằng thư viện hiện có trước khi để placeholder.

---

# 25. CLAIM CONTROL

Bắt buộc REMOVE khỏi manuscript nếu còn từ bản cũ:

> sensor configuration influences classification more strongly than model architecture.

Evidence mới không hỗ trợ claim này.

Không thay bằng:

> model architecture matters more.

Vì comparison hiện tại còn confounded bởi representation/pipeline differences.

Wording đúng:

> substantial differences were observed across the evaluated analytical pipelines.

---

# 26. KHÔNG CHẠY THÊM MODEL TÙY TIỆN

Được phép:

- đọc CSV/JSON;
- recompute aggregate metrics;
- reshape tables;
- generate figures;
- validate arithmetic;
- generate normalized confusion matrices.

Không được tự:

- tune model;
- add new algorithm;
- rerun experiments lớn;
- remove outliers;
- change preprocessing;

chỉ để manuscript đẹp hơn.

Nếu phát hiện cần experiment mới:

ghi:

> **[PROPOSED ADDITIONAL ANALYSIS — AUTHOR APPROVAL REQUIRED]**

---

# 27. TIÊU CHUẨN CHẤT LƯỢNG CUỐI

Bản thảo phải đạt mức mà tác giả có thể đọc từ đầu đến cuối như **một paper thật**, không phải report kỹ thuật.

Mỗi main claim phải theo logic nội bộ:

```text
Claim
→ Evidence
→ Limitation
→ defensible interpretation
```

Results nói:

> what was found.

Discussion nói:

> what it means and what it does not mean.

Không che giấu:

- CP3 instability;
- cross-campaign failure;
- class collapse;
- single-seed limitation;
- contradictory model results.

Những negative results này phải được sử dụng để làm rõ scientific contribution, không được coi là lỗi cần giấu.

---

# 28. FINAL RESEARCH MESSAGE

Paper phải kết thúc nhất quán với thông điệp:

> **A vibration-based classifier can provide strong laboratory condition discrimination within a controlled measurement campaign, but high within-campaign performance alone does not establish transportability. Run-aware evaluation, campaign-level robustness testing, provenance and an explicit evaluated validity scope are therefore necessary for condition evidence intended to support subsequent building inspection and asset-management workflows.**

Không vượt quá evidence hiện có.

Nếu evidence không đủ cho bất kỳ câu nào:

> **Evidence is currently insufficient.**