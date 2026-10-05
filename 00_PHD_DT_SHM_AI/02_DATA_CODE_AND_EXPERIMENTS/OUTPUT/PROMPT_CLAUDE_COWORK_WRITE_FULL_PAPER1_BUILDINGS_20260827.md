# PROMPT CHO CLAUDE COWORK — VIẾT FULL PAPER 1 CHO BUILDINGS

Bạn là giáo sư hướng dẫn PhD, chuyên gia Construction Management, Asset Management, vibration-based condition monitoring, machine learning validation, data provenance và viết bài quốc tế cho tạp chí *Buildings*.

Tôi đã bổ sung các báo cáo, kết quả chạy mới, audit Gate 1, outline mới và các tài liệu quản trị nghiên cứu vào toàn bộ thư mục **Paper 1**. Hãy đọc toàn bộ cây thư mục Paper 1 một cách đệ quy và viết lại **full manuscript bằng tiếng Anh**, có đầy đủ kết quả mới nhất, theo chuẩn Research Article của *Buildings*.

## 1. Việc phải làm trước khi viết

Không bắt đầu viết manuscript ngay. Trước tiên, hãy:

1. Quét toàn bộ file và thư mục con của Paper 1, gồm `.md`, `.docx`, `.csv`, `.json`, hình, bảng, code/log và supplementary artefacts nếu có.
2. Lập nội bộ một `SOURCE_AUTHORITY_LEDGER` gồm: tên file, ngày/phiên bản, nội dung kiểm soát, trạng thái `CURRENT / SUPPORTING / HISTORICAL / SUPERSEDED`, và file nào thay thế file nào.
3. Khi có xung đột, áp dụng thứ tự ưu tiên:
   - Các Charter/ADR Limited-FEM đã được chấp thuận: kiểm soát RQ, WP, phạm vi và prohibited claims.
   - Báo cáo xác minh kết quả IT mới nhất và artefact gốc: kiểm soát số liệu, coverage, provenance, split và metric.
   - `OUTLINE_PAPER1_BUILDINGS_VI_20260827.md`: kiểm soát câu chuyện khoa học, cấu trúc bài và claim boundary, trừ khi có artefact mới hơn chứng minh cần sửa.
   - `GATE1_INTEGRATED_EVIDENCE_AND_CLOSURE_AUDIT_20260819.md`: dùng để nhận diện limitation, blocker và kết quả lịch sử; không dùng số cũ nếu đã được báo cáo mới thay thế.
   - Manuscript/báo cáo cũ: chỉ dùng cho citation leads, mô tả setup và lịch sử; phải kiểm tra lại trước khi tái sử dụng.
4. Không coi tên file “CURRENT”, ngày mới hơn hoặc version cao hơn tự động là đúng. Phải kiểm tra nội dung, artefact và quan hệ supersession.
5. Nếu một số liệu không truy được đến báo cáo/artefact hiện hành, không dùng số đó. Ghi `[PENDING—EVIDENCE REQUIRED: ...]`.

Không dừng công việc chỉ vì còn thiếu vài trường. Hãy viết đầy đủ mọi phần có thể chứng minh; đánh dấu rõ phần thiếu để tôi/IT bổ sung sau.

## 2. Định vị nghiên cứu bắt buộc

Routing:

- RQ luận án: **RQ1**.
- WP: **WP1 — Laboratory vibration evidence**.
- Chương: **Chapter 4**.
- Paper: **Paper 1**.
- Evidence Gate: **Gate 1**.
- Evidence type: **laboratory evidence**.
- Core Scope: dataset integrity, provenance, recording-level prediction, nested outer LORO, leakage control, multi-seed, within-/cross-campaign validity, empirical null và validation scope.

Chuỗi luận án đã khóa:

`Vibration data → qualified condition evidence → BIM-linked component → inspection record → inspection–maintenance action support`.

Paper 1 chỉ sở hữu mắt xích đầu tiên. Không được biến bài này thành full Digital Twin framework hoặc bài chẩn đoán kết cấu.

FEM chỉ là `nominal, uncalibrated, reference-only, not used for damage diagnosis`. Không đưa FEM vào trục Methods/Results, không tạo FEM claim và không dùng FEM để giải thích định lượng.

## 3. Câu chuyện khoa học phải giữ

Câu chuyện trung tâm:

> High within-campaign performance is insufficient to qualify a model output as reusable condition evidence. Such evidence must carry recording/run/campaign provenance, a leakage-controlled validation protocol, uncertainty information, and an explicit validation scope. In the present multi-campaign experiment, within-campaign discrimination was high for CP1 and CP2 but limited for CP3, while CP2↔CP3 transfer was not shown to exceed the fixed-prediction empirical random-label association at the 0.05 level.

Bài không nhằm chứng minh ResNet tốt nhất. Hai kiến trúc chỉ là instruments để kiểm tra độ nhạy theo model capacity.

Đóng góp chính theo thứ tự:

1. Run-aware evidence-qualification protocol có thể tái lập.
2. Provenance audit từ raw/canonical/run registry/model input đến recording-level prediction.
3. Bằng chứng thực nghiệm về khoảng cách giữa within-campaign validity và cross-campaign transportability.
4. Minimum condition-evidence record bắt buộc mang provenance và `Validation_scope`, làm payload chuyển sang Paper 2.

Không biến CEI thành điểm scalar hoặc physical severity. Nếu tên mở rộng của CEI chưa nhất quán giữa các file, dùng thuật ngữ trung tính `condition-evidence record/package` và ghi vấn đề vào completion log.

## 4. Tên bài và Paper RQs

Tên ưu tiên:

**Run-Aware Qualification of Vibration-Derived Condition Evidence for Steel-Building Inspection: A Multi-Campaign Study on a Scaled Frame**

Paper RQs:

1. To what extent can controlled connection states be distinguished within each acquisition campaign under recording-level, leakage-controlled nested LORO evaluation?
2. Does within-campaign evidence remain valid when the trained pipeline is transferred to another campaign with the same four-state problem and aligned sensor view?
3. Which provenance and validation-scope fields must accompany a prediction before it can be treated as traceable condition evidence rather than a generalizable diagnosis?

Nếu literature audit cho thấy cần điều chỉnh câu chữ, chỉ sửa hẹp; không thay đổi trục khoa học.

## 5. Dataset và kết quả headline phải kiểm tra

Hãy xác minh các giá trị dưới đây từ báo cáo mới nhất trước khi đưa vào bài. Nếu artefact mới hơn khác, dùng artefact mới hơn và ghi rõ trong completion log.

### Dataset

- 3 physical campaigns: CP1, CP2, CP3.
- 6 runs/campaign; 12 recordings/run; tổng 72 recordings/campaign và 216 recordings.
- 4 controlled states, cân bằng 18 recordings/class/campaign.
- Mỗi state/run gồm BEAT-L1, BEAT-L2 và white noise.
- CP1 dùng `s12`; CP2 và CP3 dùng `s123`.
- Cross-campaign core chỉ dùng CP2↔CP3 vì cùng sensor view và cùng bài toán bốn lớp.
- CP2 canonical có nguồn từ CP2-21: 71 recordings giữ nguyên + 1 recording `BS1B1L1R12` được thay bằng file bổ sung có truy vết. Không dùng dữ liệu 22/07.
- Không dùng CP2-2122 trong manuscript chính.

### Within-campaign results

| Model | CP1 Accuracy | CP1 Macro-F1 | CP2 Accuracy | CP2 Macro-F1 | CP3 Accuracy | CP3 Macro-F1 |
|---|---:|---:|---:|---:|---:|---:|
| 1D-CNN | 0.694 ± 0.048 | 0.688 ± 0.056 | 0.745 ± 0.099 | 0.740 ± 0.107 | 0.440 ± 0.076 | 0.404 ± 0.081 |
| ResNet-1D | 0.935 ± 0.008 | 0.935 ± 0.008 | 0.958 ± 0.014 | 0.959 ± 0.014 | 0.569 ± 0.037 | 0.568 ± 0.030 |

Chỉ viết ResNet có observed scores cao hơn; không tuyên bố statistically/general universally superior nếu chưa có kiểm định trực tiếp hợp lệ.

### Cross-campaign results

| Direction | Model | Balanced Accuracy | Campaign Macro-F1 |
|---|---|---:|---:|
| CP2→CP3 | 1D-CNN | 0.259 ± 0.029 | 0.190 ± 0.023 |
| CP2→CP3 | ResNet-1D | 0.227 ± 0.029 | 0.105 ± 0.014 |
| CP3→CP2 | 1D-CNN | 0.296 ± 0.029 | 0.289 ± 0.039 |
| CP3→CP2 | ResNet-1D | 0.282 ± 0.021 | 0.248 ± 0.045 |

### Fixed-prediction permutation tests

| Direction | Model | BA one-sided p | Macro-F1 one-sided p |
|---|---|---:|---:|
| CP2→CP3 | 1D-CNN | 0.395 | 0.511 |
| CP2→CP3 | ResNet-1D | 0.980 | 0.709 |
| CP3→CP2 | 1D-CNN | 0.131 | 0.088 |
| CP3→CP2 | ResNet-1D | 0.151 | 0.096 |

Kết luận đúng:

> None of the tested cross-campaign configurations showed evidence of stronger prediction–label association than the fixed-prediction empirical null at α = 0.05.

Không viết “the models were statistically below chance”. Phải nói rõ permutation giữ prediction cố định và không retrain toàn pipeline.

### Coverage và aggregation

- Mỗi model/campaign in-campaign có 30 variants/seed × 3 seeds = 90/90 usable evaluations.
- Mỗi direction/model cross-campaign có 6 source-validation variants × 3 seeds = 18/18.
- Outer LORO: mỗi run làm outer test đúng một lần; trong năm run còn lại có bốn train và một validation.
- Prediction được gộp từ windows thành đúng một prediction/recording.
- Macro-F1 chính thức được tính trên 72 recording-level predictions của toàn campaign trong từng seed, sau đó báo mean ± SD qua ba seed.
- Ba seed là stochastic sensitivity, không phải ba independent data samples.
- Run-level results chỉ là diagnostic.
- Validation rule là `standardized post-hoc aggregation rule`, không phải predefined/preregistered.

## 6. Các số liệu/kết luận cũ tuyệt đối không tái sử dụng

- Không dùng `71/90 ResNet–CP3`; coverage mới là 90/90.
- Không dùng các Macro-F1 cũ 0.173, 0.164 hoặc 0.203 cho CP2→CP3–1D-CNN; số chính thức là 0.190 ± 0.023.
- Không dùng one-seed hoặc Support-Point split cũ làm headline khi nested LORO 3 seed đã có.
- Không coi CP2-21 và CP2-2122 là hai campaign độc lập.
- Không dùng CP2-2122 để chứng minh robustness.
- Không viết “cross-campaign below chance” như kết luận thống kê.
- Không viết ResNet vượt trội có ý nghĩa nếu không có direct test.
- Không viết “two sensors are sufficient”, “S13 is optimal” hoặc bất kỳ kết luận số lượng/vị trí cảm biến nào.

## 7. Ranh giới với Paper 1B

Paper 1B xử lý riêng sensor subset/configuration. Vì vậy trong Paper 1:

- chỉ ghi `s12` và `s123` như acquisition/model-input conditions;
- không phân tích S1/S2/S3/S12/S13/S23/S123;
- không kết luận minimum sensor count, best subset hoặc marginal benefit;
- không dùng bảng/hình lõi của Paper 1B;
- nếu phải nhắc, ghi rằng sensor-configuration analysis is outside the scope of the present paper.

## 8. Cấu trúc full manuscript

Viết bằng tiếng Anh học thuật tự nhiên, theo Research Article của *Buildings*:

1. **Title**
2. **Abstract** — một đoạn khoảng 200 từ, có background, gap, methods, exact headline results, narrow conclusion.
3. **Keywords** — 6–9 từ.
4. **Introduction**
   - management problem: trustworthy evidence before inspection/action;
   - leakage/grouping/cross-campaign problem in vibration ML;
   - verified literature gap;
   - objectives, Paper RQs và contributions.
5. **Materials and Methods**
   - research design and claim boundary;
   - scaled frame and controlled states;
   - campaigns, runs, excitations and sensors;
   - dataset provenance/canonicalization;
   - preprocessing/windowing;
   - 1D-CNN và ResNet-1D;
   - nested outer LORO;
   - validation-variant selection;
   - recording-level aggregation/metrics;
   - cross-campaign evaluation;
   - fixed-prediction permutation test;
   - minimum condition-evidence record.
6. **Results**
   - dataset/provenance/coverage;
   - within-campaign results;
   - per-run/per-class diagnostics;
   - cross-campaign results;
   - empirical null;
   - seed/validation-choice sensitivity;
   - evidence-scope summary.
7. **Discussion**
   - within-campaign accuracy versus transportability;
   - CP3 as a different evidence regime;
   - model capacity versus evidence stability;
   - provenance and Validation_scope;
   - Construction Management/Digital Twin implication;
   - comparison with closest studies;
   - limitations.
8. **Conclusions** — ngắn, không lặp Results, không overclaim.
9. **Back Matter** theo MDPI: Supplementary Materials, Author Contributions, Funding, IRB, Informed Consent, Data Availability, Acknowledgments, Conflicts of Interest, References.

## 9. Quy tắc viết Results và Discussion

- Results tổ chức theo Paper RQs/evidence objectives, không theo thứ tự phần mềm xuất output.
- Báo descriptive results trước, inferential/statistical result sau.
- Không lặp toàn bộ bảng trong prose; chỉ nêu pattern và số quyết định.
- Confusion matrices phải giải thích theo error pattern từng lớp, không chỉ accuracy.
- Phân biệt statistical significance với practical/evidence significance.
- Không che giấu CP3 yếu hoặc kết quả cross-campaign âm.
- Mọi giả thuyết về amplitude/frequency distribution, excitation, mounting, coupling, environment hoặc model overfitting phải gắn nhãn hypothesis, not confirmed.
- Không suy rộng từ lab sang field.

## 10. Literature và citation control

1. Chỉ dùng tài liệu tham khảo có thể xác minh từ file gốc, Zotero/library record hoặc nguồn chính thức có metadata đầy đủ.
2. Không bịa citation, DOI, volume, issue, page hoặc journal ranking.
3. Không dùng citation trong manuscript chỉ vì nó xuất hiện trong một báo cáo AI cũ; phải kiểm tra nguồn gốc.
4. Lập ma trận 8–12 closest studies theo các chiều: split unit, leakage control, run/session holdout, cross-campaign validation, provenance, empirical null và management output.
5. Chỉ khóa novelty/gap sau ma trận này. Không viết “no previous study” nếu chưa chứng minh.
6. Dùng citation style số của MDPI. Nếu thiếu nguồn, chèn `[CITATION NEEDED: mô tả nguồn cần tìm]` thay vì bịa.
7. Không trích dẫn các file quản trị nội bộ trong bibliography; chúng chỉ kiểm soát nghiên cứu.

## 11. Figures và tables

- Tìm và sử dụng đúng hình/bảng thuộc báo cáo mới nhất.
- Không chèn hình từ output cũ nếu metric/caption đã bị thay thế.
- Mỗi figure/table phải tự hiểu được, có caption đầy đủ, nêu unit of analysis, seed, aggregation và sample size khi cần.
- Nếu file hình chưa có, đặt placeholder cụ thể: `[FIGURE X TO INSERT: ...; source file required: ...]`.
- Ưu tiên 6–8 bảng và 6–7 hình chính; phần đầy đủ đưa Supplementary.

Các hình/bảng cốt lõi cần có:

- specimen/states/sensor positions;
- provenance pipeline;
- nested LORO and cross-campaign design;
- within-campaign Macro-F1;
- cross-campaign metrics;
- empirical null;
- cross-run heatmap/campaign confusion matrices;
- minimum evidence record/validation-scope table.

## 12. Missing evidence handling

Rà toàn bộ thư mục để điền các mục sau. Nếu chưa có bằng chứng, để placeholder rõ ràng và ghi vào completion log:

- B1/B2/B3 ↔ physical connection/state mapping;
- specimen geometry/material/connection details;
- acquisition dates và replacement recording date;
- Sensor_ID/channel order/axes/resultant;
- sampling rate cho mọi campaign;
- dead/flat channel handling;
- current model architecture/hyperparameters;
- window-count imbalance/sampling control;
- campaign-level confusion matrices và per-class metrics;
- prediction/sensitivity của `BS1B1L1R12`;
- sensitivity theo validation choices;
- CP1 sensor-permutation injection/recovery validation nếu CP1 correction được dùng như claim;
- cross-campaign fixed-hyperparameter control;
- probability calibration status;
- Data Availability và reproducibility package.

Không tự điền các thông số này bằng suy đoán.

## 13. Claim firewall

### Được phép

- Controlled states were distinguishable within CP1/CP2 under the tested nested run-aware protocol.
- CP3 showed lower within-campaign discrimination.
- Cross-campaign transfer was not supported under the tested source-trained pipeline.
- Evidence validity depended on recording/run/campaign provenance.
- Validation_scope should accompany condition evidence.
- The findings are laboratory-bound.

### Không được phép

- Physical damage was diagnosed.
- CP3 labels/data were faulty nếu không có bằng chứng.
- ResNet was universally/statistically superior.
- Cross-campaign performance was statistically below chance trong mọi trường hợp.
- A specific environmental/mechanical factor caused domain shift.
- CEI represents physical severity hoặc calibrated confidence.
- The classifier transfers to the real building.
- The study demonstrates predictive maintenance, RUL hoặc autonomous maintenance.
- FEM validates damage hoặc stiffness degradation.
- Any sensor configuration is optimal/minimal.

## 14. Văn phong và chất lượng

- Viết như một bài nghiên cứu quốc tế, không như báo cáo tiến độ hoặc thesis chapter.
- Không nhắc “IT”, “Claude”, “the user”, “our previous chat” hoặc tên file nội bộ trong manuscript.
- Tránh câu sáo rỗng, tuyên bố novelty chung chung và lặp lại.
- Giữ thuật ngữ nhất quán: `campaign`, `run`, `recording`, `window`, `controlled state`, `condition evidence`, `validation scope`.
- Phân biệt rõ `run` với `recording`: một run gồm 12 recordings.
- Dùng dấu thập phân tiếng Anh.
- Không sao chép nguyên văn manuscript cũ; tái cấu trúc để tránh self-plagiarism, nhưng giữ citation hợp lệ.
- Không viết Discussion vượt quá bằng chứng.

## 15. Deliverables

Tạo hai file:

1. **`PAPER1_BUILDINGS_FULL_MANUSCRIPT_v3.0.docx`**
   - full English manuscript;
   - có title, abstract, keywords, toàn bộ sections, bảng/hình hoặc placeholders, back matter và references đã kiểm chứng;
   - định dạng sạch, có heading hierarchy, caption và cross-reference nhất quán.

2. **`PAPER1_SOURCE_AND_COMPLETION_LOG_v3.0.md`**
   - source-authority ledger;
   - danh sách số liệu cũ bị loại và số liệu mới thay thế;
   - claim-to-source matrix;
   - bảng/hình đã dùng và nguồn file;
   - citation verification log;
   - danh sách `[PENDING]` theo mức `BLOCKER / REQUIRED / OPTIONAL`;
   - đánh giá cuối: phần nào đã submission-ready, phần nào còn phải bổ sung.

Trước khi kết thúc, tự kiểm tra:

- tất cả số headline khớp báo cáo mới nhất;
- không có CP2-2122 trong kết quả chính;
- không có sensor-configuration claim;
- không có field-diagnosis/FEM/predictive-maintenance overclaim;
- Results và Discussion tách đúng vai trò;
- mọi citation và DOI đều có nguồn xác minh;
- mọi thông tin chưa đủ bằng chứng được đánh dấu rõ, không bị lấp bằng suy đoán.

Hãy thực hiện toàn bộ công việc, không chỉ tạo outline hoặc đề xuất cách viết.
