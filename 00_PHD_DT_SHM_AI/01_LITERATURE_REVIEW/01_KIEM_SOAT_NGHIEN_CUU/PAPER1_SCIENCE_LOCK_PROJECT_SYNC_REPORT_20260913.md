# PAPER 1 SCIENCE LOCK — PROJECT SYNCHRONIZATION REPORT

**Ngày:** 13/09/2026 | **Loại:** synchronization/closure pass sau khi Paper 1 khóa khoa học. Đây không phải hồ sơ nghiệm thu Gate và không có thẩm quyền đóng Gate.
**Phạm vi:** đồng bộ trạng thái giữa final Paper 1 và các file quản trị ACTIVE/CURRENT. Không mở hướng nghiên cứu mới, không chạy thêm model hay phân tích, không đổi kiến trúc Limited-FEM, không sửa Charter, không tạo metric, claim, citation hay kết quả mới.
**Vị trí:** `01_LITERATURE_REVIEW/01_CURRENT_CONTROL/`. Các bản trước khi sửa được sao lưu tại `01_LITERATURE_REVIEW/90_ARCHIVE/01_SUPERSEDED_VERSIONS/PRE_SYNC_20260913/`, kèm manifest SHA-256.

```text
RQ:             RQ1 (upstream) → RQ2 (handover)
WP:             WP1 → WP2
Chương:         C4 → C5
Paper:          Paper 1 → Paper 2
Evidence Gate:  G1 (mặc định), và giao diện G1 → G2
Scope:          Core — đồng bộ quản trị
Evidence type:  Laboratory evidence (Paper 1); Information traceability (handover)
```

FEM trong toàn bộ báo cáo: **nominal, uncalibrated, reference-only, not used for damage diagnosis.** Paper 1 không dùng FEM. Cụm "nominal 1:10" trong Paper 1 chỉ tỷ lệ hình học của mô hình, không phải FEM.

---

## 1. Source files inspected

### 1.1 Năm nguồn source-of-truth được yêu cầu đọc trước

| # | File | Vị trí thực tế (13/09/2026) | Version / Status | Ghi nhận chính |
|---|---|---|---|---|
| 1 | `MASTER_RESEARCH_CHARTER.md` (17/07) | `90_ARCHIVE/HISTORICAL_UNIQUE_FILES/BACKUP_BEFORE_WRITEBACK_20260718/`; bản sao ở `90_ARCHIVE/SNAPSHOTS_20260718/` | Charter ngắn, bộ khung Limited-FEM | §10 cho phép tuyên bố "Cấu hình cảm biến ảnh hưởng mạnh hơn lựa chọn kiến trúc mô hình AI". Không có bản CURRENT cùng tên trong cây hiện hành |
| 2 | `MASTER_RESEARCH_CHARTER_v1.1_LIMITED_FEM_20260717.md` | Như trên (chỉ có trong archive) | v1.1, "Source of truth"; SOURCE_OF_TRUTH xếp level 2 | RQ1 nguyên văn; Paper 1 "…of Low-Cost Sensor Configurations…", nội dung lõi gồm sensor configuration effects và CEI; G1–G7, trong đó G6 = Paper 2 submission, G7 = Paper 3 + thesis synthesis; Paper 4 optional; §13 Allowed claims gồm tuyên bố về cấu hình cảm biến |
| 3 | `RESEARCH_DIRECTION_AND_SCOPE.md` | `01_CURRENT_CONTROL/` | v2.3, 11/08/2026, CURRENT SUPPORTING (level 7) | Không Gate nào PASS. Paper 3 "optional/bonus", nhưng minimum field evidence bắt buộc |
| 4 | `RESEARCH_ARCHITECTURE.md` | `01_CURRENT_CONTROL/` | v2.3, 11/08/2026 (level 7) | Bốn lớp; Lớp 1 → RQ1/WP1. Trỏ tới `../01_CURRENT_CONTROL/MASTER_INDEX_CURRENT.md` và `../02_EVIDENCE_BASE/` (thư mục không tồn tại) |
| 5 | `CURRENT_STATUS_AND_NEXT_DIRECTION.md` | `01_CURRENT_CONTROL/` | v2.3, 11/08/2026 (level 5) | G1 `OPEN — PARTIAL EVIDENCE`; Stream A mô tả G1 như chưa chạy LORO, chưa xác nhận ResNet1D. Không có dòng trạng thái Paper 1 |

### 1.2 Bộ quản trị hiện hành khác (`01_LITERATURE_REVIEW/01_CURRENT_CONTROL/`)

| File | Version | Dùng để |
|---|---|---|
| `MASTER_RESEARCH_CHARTER_CURRENT_20260812.md` | v2.1.2 (level 3, phụ thuộc baseline 17/07) | Kiểm tra xung đột với final Paper 1 (không sửa) |
| `08-RESEARCH_ARCHITECTURE_DECISION_RECORD_20260717.md` | ADR-2026-001, ACCEPTED | Ranh giới FEM |
| `SOURCE_OF_TRUTH_HIERARCHY_v2.1.md` | v2.3 (level 1) | Thứ tự thẩm quyền |
| `CURRENT_DIRECTION_LOCK_20260804.md` | v1.2 (level 4) | Chuỗi khóa, CEI lock, "Do not run Graph 02" |
| `RQ_WP_CHAPTER_PAPER_GATE_MATRIX_v2.1.md` | v2.3 (level 4) | Ma trận; §5 trạng thái claim Paper 1 |
| `EVIDENCE_GATES_v2.1.md` | v2.3 (level 4) | Tiêu chí G1 và Milestone M1 |
| `TERMINOLOGY_CONTROL_CURRENT.md`, `AGENT_RULES.md` | v2.3 | Nhãn "Candidate claim pending Gate 1 closure"; quy tắc file |
| `MASTER_INDEX_CURRENT.md` | v2.3 | Điều hướng (phần lớn đường dẫn đã lỗi thời) |
| `G1_G2_INTERFACE_DECISION_REGISTER.csv` | 12/08 | D003–D010 là các quyết định G1 → G2 |
| `LIVING_EVIDENCE_BASE_CURRENT_20260812.md`, `MASTER_LITERATURE_AND_EVIDENCE_SYNTHESIS_v2_20260828.md`, `REVISION_LOG_MASTER_SYNTHESIS_v2_20260828.md` | CURRENT | Claim cũ, xung đột M-02, tách Paper 1A/1B |
| `README.md` (control) | 28/08 | Điều hướng |

### 1.3 Final Paper 1 và G1 evidence

| File | Vị trí | Vai trò |
|---|---|---|
| `PAPER1_v8.1_SHM_RISK_REDUCED.docx` (13/09) | `03_OUTPUTS/03_PAPER_1A_GATE1/Paper 1.md/` | **Final manuscript.** Tên bài: "Run-Aware Evaluation of Vibration-Based Connection-State Classification: Within-Campaign Performance and Cross-Campaign Limits on a Scaled Bolted Steel Frame". Tạp chí đích: Structural Health Monitoring (SAGE) |
| `PAPER1_v8.1_SHM_PRE_SUBMISSION_AUDIT.md`, `_CHANGELOG.md`, `PAPER1_v8.1_NEW_REFERENCE_AUDIT.md` | như trên | 50/50 check PASS; kết luận "READY AFTER AUTHOR METADATA / FIGURE FIXES" |
| `PAPER1_v8_SHM_SUBMISSION.docx`, `_CHANGELOG`, `_COMPLIANCE_CHECK` | như trên | Bản IT-verified trước v8.1 (superseded) |
| `BAO_CAO_IT01_IT06.md` (12/09) | `03_PAPER_1A_GATE1/` | Kiểm tra IT-01 đến IT-06. Là overriding evidence cho số liệu |
| `PAPER1_Figure3_A4_Editable.pptx`, `PAPER1_v8.1_Figure3_redrawn_400dpi.png` | `03_PAPER_1A_GATE1/`, `Paper 1.md/` | Figure 3, chờ tác giả duyệt |
| `PAPER1_SUPERVISOR_REPORT_DUT_TEMPLATE_v2.pptx`, `PAPER1_GIAI_THICH_NGHIEN_CUU_DE_HIEU_v2.md`, `PAPER1_SUPERVISOR_REPORT_v2_CHANGELOG.md` | `02_CHUYEN_DE_1/` (và bản sao ở `03_PAPER_1A_GATE1/`) | Câu chữ trạng thái Gate 1 thống nhất |
| `Paper 1.md/README.md` (28/08) | `03_PAPER_1A_GATE1/Paper 1.md/` | Paper 1A status record (đã lỗi thời) |
| `GATE1_INTEGRATED_EVIDENCE_AND_CLOSURE_AUDIT_20260819.md` | `02_DATA_CODE_AND_EXPERIMENTS/OUTPUT/` | 19/08: "GATE 1 OPEN — PARTIAL EVIDENCE"; khi đó chưa có LORO thật và chỉ có một seed |
| `GATE1_LORO_UPDATED_RESULTS_AUDIT_20260824.md` | `…/OUTPUT/24.08.2026/` | 24/08: "PARTIALLY CLOSED" (7/11 hạng mục); ResNet1D sensor mode "CLOSED — VERIFIED" |
| `bao_cao_xac_minh_tinh_hop_le_va_ket_qua_ml.md` | `…/OUTPUT/27.08.2026/` | Quan hệ CP2 và CP2-21; permutation dùng prediction cố định; quy tắc gộp validation chuẩn hóa sau khi đã có test artefact, tức không preregistered |
| `THREE_CAMPAIGN_REANALYSIS/*.csv`, `CANONICAL_THREE_CAMPAIGN_DATASET/08_AUTOMATED_VALIDATION_RESULTS.csv` | `02_DATA_CODE_AND_EXPERIMENTS/` | Reanalysis sơ bộ 29/07, dùng định danh cảm biến S1/S2/S3 kiểu cũ theo vị trí khối. Đã superseded đối với claim |
| `06_GATE1_TECHNICAL_VERDICT.md` và bộ `00`–`07` (07/09) | `D:\01_RESEARCH\08_Output_07.09\` (**ngoài repository**) | Kết luận kỹ thuật: "Gate 1 vẫn OPEN". Con số "294/294 candidate" trong bộ này đã được thay bằng câu 192 đã khóa |
| `v1/manifest.json`, `v1/index.csv`, bốn Kaggle bundle, `_AUDIT_WORKSPACE/` | `D:\01_RESEARCH\08_Output_07.09\` (**ngoài repository**) | 216 recording, 6.899 window, 102 NPZ có SHA-256; `canonical_manifest_sha256 = f400e943…` |

### 1.4 Giao diện, Literature Review và dashboard

| File | Vị trí | Ghi nhận |
|---|---|---|
| `G1_TO_G2_CONDITION_EVIDENCE_INTERFACE_v1.0.md` (nội dung v1.1, 04/08) | `02_DEEP_READ_CURRENT_PDF/03_RQ2_GATE2_3/` | CURRENT WORKING SPECIFICATION. §2 và §17 dùng chuỗi kết thúc bằng `Action_Record_ID`/`Status_Event` |
| `TIEU_LUAN_TONG_QUAN_HOAN_CHINH_v2_13092026.docx` | `03_OUTPUTS/01_TIEU_LUAN_TONG_QUAN/` | Bản Literature Review mới nhất, là đầu vào của P1 |
| `CURRENT_PRIORITY.md`, `GATE_STATUS_DASHBOARD.md`, `CLAIM_EVIDENCE_LIMITATION_NEXT_ACTION.md` (09/08) | `01_LITERATURE_REVIEW/90_ARCHIVE/04_HISTORICAL_DECISIONS/CURRENT_LIMITED_FEM_BY_GATE_20260809/08_CURRENT_STATUS_DASHBOARD/` | **Chỉ còn trong archive**, không có bản ACTIVE nào |
| `README.md` (Literature Review), `99_INDEX_AND_LOG/MASTER_FILE_INDEX_CURRENT.md`, README của Paper 1B, Paper 2, Paper 3, Chuyên đề 1 | `01_LITERATURE_REVIEW/…` | Điều hướng, dùng tên thư mục đã đổi |

### 1.5 File được viện dẫn nhưng không tìm thấy trong cây hiện hành

- `00_README_START_HERE.md` ở project root (chỉ còn trong archive).
- `06-MASTER_RESEARCH_CHARTER_v1.1_LIMITED_FEM_20260717.md` dưới `02_EVIDENCE_BASE/` (chỉ còn trong archive, không có tiền tố `06-`).
- `EVIDENCE_GATES_v1.1_LIMITED_FEM.md`.
- `PAPER1_DIRECTION_AND_GATE_v2.1_20260719.md`, `00_EXECUTIVE_REPORT.md`, `SUPERSEDED_DOCUMENT_REGISTER_20260804.csv`, `LIVING_EVIDENCE_BASE_v2.1_TRACEABILITY_CORE.md`, `PAPER1_SUPERVISOR_PRELIMINARY_SYNTHESIS_20260812.md`.
- `05_DATA_CODE_AND_EXPERIMENTS/G1_EXECUTION_PACK/`: cả thư mục gốc `05_…` lẫn pack đều không tồn tại.
- Toàn bộ file bàn giao IT-01 đến IT-06 và thư mục `evidence/`: `DATASET_REGISTRY_FINAL.csv`, `SENSOR_CHANNEL_MAP.csv`, `FEATURE_DEFINITION.csv`, `CHANNEL_SYNCHRONISATION_NOTE.md`, `MODEL_OUTPUT_AND_SELECTION.md`, `METRIC_AGGREGATION_CHECK.csv`.
- `PAPER1_CLAIM_STATUS_TABLE.md` (hạng mục của M1) và `G1_ACCEPTANCE_MATRIX.md`.

---

## 2. Final scientific state of Paper 1

### 2.1 A. Trạng thái Paper 1

**`SCIENCE LOCKED` — chưa SUBMISSION READY — chưa SUBMITTED.**

- **Claim:** nội dung khoa học của Paper 1 đã khóa ở bản `PAPER1_v8.1_SHM_RISK_REDUCED.docx` (13/09/2026).
- **Evidence:** IT-01 đến IT-06 (12/09) đối chiếu 472 ô số: 469 khớp, 3 ô đã sửa ở v8. Pre-submission audit v8.1 báo 50/50 check PASS và kết luận "The manuscript is scientifically ready". Không còn scientific blocker.
- **Limitation:** chưa đạt "SUBMISSION READY" vì ba lý do.
  1. Còn bảy hạng mục phía tác giả: tên, affiliation, e-mail, ORCID; funding và COI; bốn điểm AI disclosure; duyệt Figure 3; ảnh B1 và ảnh gốc Figure 1–2; quyết định data DOI.
  2. `EVIDENCE_GATES_v2.1.md` M1 đòi hỏi "G1 closed" trước "Submission-ready", mà G1 chưa ký.
  3. Không có hồ sơ thầy xác nhận việc khóa khoa học. Việc khóa do NCS công bố ngày 13/09/2026; bằng chứng phê duyệt cấp thầy: `Evidence is currently insufficient.`
- **Next action:** hoàn tất các mục tác giả, xin thầy ký G1 hoặc phê duyệt ngoại lệ M1 (C-04), rồi mới nộp.

### 2.2 B. RQ1/WP1 đã tạo ra gì (chỉ Laboratory evidence)

1. **Dataset và provenance đã đối chiếu.**
   - Quy mô: 3 campaign (CP1 25/04/2026, CP2 21/07/2026, CP3 29/07/2026), 18 run (6 mỗi campaign), 216 recording (72 mỗi campaign, 18 mỗi lớp) và 6.899 window (1.746 / 3.065 / 2.088).
   - Window: 400 mẫu, bước 200, tần số 100 Hz. QC cắt 951 mẫu cuối không hợp lệ ở 149 recording; không loại recording nào.
   - Hash: 216 source SHA-256 là duy nhất và khớp registry; 102 NPZ khớp hash cả bản local lẫn bản tải từ Kaggle (IT-01).
   - CP2/RUN012/REC0004 là recording thay thế đo ngày 29/07. Nó không trùng dữ liệu CP3: đoạn giống hệt dài nhất là 22 mẫu.
2. **Đánh giá run-aware, chống rò rỉ, chấm điểm ở cấp recording.**
   - Mỗi split gồm 4 train run, 1 validation run và 1 test run. Mỗi case chạy đủ 30 tổ hợp validation–test có thứ tự.
   - Window được cắt trong từng recording, rồi gán nguyên run vào một phía của phép chia, nên không window nào vượt qua ranh giới split.
   - Candidate được chọn chỉ bằng đại lượng validation. "Within the audited scope, 192 stored candidate selections were reproduced from validation quantities alone." 612 checkpoint DL được tái hiện.
   - Metric là pooled confusion matrix trên 72 recording mỗi seed.
   - Số fit thực chạy: 540 / 180 / 72 (Table 3). Con số 972 chỉ là phạm vi kiểm toán, không phải số lần chạy.
3. **Mô hình.** Bốn mô hình trong thân bài:
   - RF và SVM-RBF không tuning, dùng 25 feature mỗi kênh, tổng 228 chiều (CP1) hoặc 366 chiều (CP2/CP3).
   - 1D-CNN và ResNet1D chạy seed 42/43/44; siêu tham số lấy từ một pool phát triển trước.
   - Extra trees và HistGB chỉ nằm ở Table A4.
4. **Kết quả chính (Table 4, pooled Macro-F1).**

   | Campaign | RF | SVM-RBF | ResNet1D | 1D-CNN |
   |---|---|---|---|---|
   | CP1 | 1.000 | 1.000 | 0.930 ± 0.001 | 0.727 ± 0.043 |
   | CP2 | 0.986 | 0.986 | 0.959 ± 0.014 | 0.777 ± 0.039 |
   | CP3 | 0.875 | 0.690 | 0.523 ± 0.123 | 0.399 ± 0.077 |

   SD_fold ở CP3 nằm trong khoảng 0.096–0.139.
5. **Giới hạn chuyển giao.** Chuyển giao exploratory CP2 ↔ CP3, chỉ với mô hình deep:
   - Balanced accuracy trung bình 0.227–0.278; Macro-F1 0.124–0.210.
   - p một phía nhỏ nhất trên 12 candidate là 0.167, và chỉ có giá trị khi chấp nhận giả định exchangeability chưa được biện minh.
   - CP1 không được đánh giá chuyển giao.
   - Kết luận của bài: kết quả "does not establish a valid independent test of transfer beyond the acquisition context."
6. **Đóng góp theo đúng lời văn đã khóa.** Bài báo không tuyên bố các biện pháp kiểm soát hay tổ hợp của chúng là mới. Đóng góp là hệ quả được ghi nhận bằng thực nghiệm: tách trạng thái gần như hoàn hảo trong CP1/CP2 tồn tại song song với tách yếu hơn, phụ thuộc run ở CP3, và với chuyển giao gần mức ngẫu nhiên. Vì vậy một classification output chỉ dùng được như condition evidence khi đi kèm provenance, giao thức đánh giá và độ biến thiên quan sát được.

### 2.3 C. Hạn chế (theo v8.1 §4.1 và §5.6)

1. Chỉ 18 run trên một mẫu vật. Fold quantisation là 1/12. Run là acquisition grouping unit, **không phải** independent experimental unit đã được kiểm chứng, vì không có hồ sơ tháo lắp giữa các run.
2. Mô hình deep phụ thuộc HPO: 15/18 fold within-campaign và cả 4 case transfer đã dùng pool phát triển có chứa test run. Điều này được khai báo, không được hiệu chỉnh, và không ước lượng độ lớn.
3. RF và SVM chỉ chạy một seed; độ nhạy seed của RF chưa đo. Permutation chỉ có cho cross-campaign; within-campaign so với mức ngẫu nhiên lý thuyết 0.25. Không có kiểm định ý nghĩa và không có CI.
4. Không chạy phép so sánh với random split, nên không đo được mức thổi phồng do rò rỉ trên dữ liệu này.
5. Các campaign không phải replicate. Thứ tự đo trạng thái không ngẫu nhiên hóa: ở CP3 trạng thái S0 luôn đo cuối, và CP3 có hai nhóm thứ tự ngược nhau. Timestamp của CP2 bất thường; RUN012 có timestamp tổng hợp.
6. Provenance còn mở ở ba điểm: byte identity lúc training, ánh xạ cảm biến vật lý tới vị trí (gán bằng gravity fingerprint, không có serial thiết bị), và đồng bộ PASCO trước khi xuất file. Các kênh ghép theo sample index. Xác suất từng window không được lưu trữ.
7. Không có dữ liệu torque, preload, độ cứng hay modal. Không chuyển giao 1:10 sang công trình thực, không chẩn đoán hiện trường, không severity. Chưa xét độ bền với biến thiên môi trường và vận hành (EOV).

### 2.4 CURRENT STATE AUDIT

Bảng này lập trước khi sửa bất kỳ file quản trị nào.

| # | Item | Repository currently says | Final Paper 1 evidence says | Conflict? | Required update |
|---|---|---|---|---|---|
| 1 | Paper 1 status | CURRENT_STATUS v2.3 không có dòng Paper 1. Paper 1A README (28/08) nói metric là candidate và còn thiếu registry, split-before-windowing, multi-seed, ResNet1D provenance. MASTER_INDEX §5 trỏ tới `PAPER1_DIRECTION_AND_GATE_v2.1` (không tồn tại) | v8.1 đã khóa khoa học; audit 50/50 PASS; "READY AFTER AUTHOR METADATA / FIGURE FIXES"; chưa nộp | **Có** (thiếu và lỗi thời) | Thêm dòng Paper 1 vào CURRENT_STATUS; viết lại Paper 1A README; thêm mục Paper 1 vào MASTER_INDEX |
| 2 | Gate 1 status | `OPEN — PARTIAL EVIDENCE` ở mọi nơi (11/08). Blocker ghi là LORO, ResNet1D, uncertainty chưa có | Bằng chứng khoa học đã đầy đủ và được kiểm toán. Chưa có `G1_EXECUTION_PACK` trong repo, chưa có `G1_ACCEPTANCE_MATRIX` đã ký. Kết luận kỹ thuật 07/09: "Gate 1 vẫn OPEN" | Nhãn: **không**. Mô tả blocker: **có** | Giữ nguyên nhãn; viết lại blocker (§3) |
| 3 | Số dataset/campaign/run | EVIDENCE_GATES: "count khóa (xác nhận '6' hay khác)". Charter §12: "corrected 216-record canonical dataset" | 3 / 18 / 216 / 6.899; fit 540 / 180 / 72 (+180 ở A4); 972 chỉ là phạm vi kiểm toán | Có (số chưa được khóa trong quản trị) | Ghi vào CURRENT_STATUS §3 và bản sync của EVIDENCE_GATES |
| 4 | Run registry / manifest | `RUN_REGISTRY_LOCKED.csv` OPEN; pack không tồn tại; audit 24/08 nói "registry absent" | Registry canonical (recordings.csv có source/canonical SHA-256) nằm trong Kaggle bundle trên D:. `v1/manifest.json` và `index.csv` có trên D:. `DATASET_REGISTRY_FINAL.csv` đã bàn giao nhưng không có trong project. Manifest ghi `selected_split_count: 18`, trong khi thực chạy 30 tổ hợp | **Có** (có ngoài repo nhưng chưa khóa) | Ghi khoảng trống; đề xuất materialize pack. Pass này không tạo pack |
| 5 | Leakage-safe evaluation | Stream A: "Audit split-before-windowing and train-only preprocessing" vẫn đang chờ | 0/1.482 vi phạm. Gán nguyên run; không window nào vượt ranh giới. Per-window standardisation không fit trên train. StandardScaler của SVM chỉ fit trên train. Test không tham gia checkpoint, early stopping hay lựa chọn candidate. Riêng phụ thuộc HPO của mô hình deep được khai báo | **Có**, và câu chữ tiêu chí lệch với cách triển khai (C-05) | Ghi vào CURRENT_STATUS và EVIDENCE_GATES; cần thầy quyết định |
| 6 | LORO | "Execute leakage-safe run-aware/LORO … with multiple seeds" (đang chờ). Audit 19/08: "True LORO chưa tồn tại" | Đã chạy: 4/1/1, 30 tổ hợp có thứ tự mỗi case, 6 outer fold gộp thành 72 recording mỗi seed. DL 3 seed, RF/SVM 1 seed. Không preregistered | Có (lỗi thời) | Cập nhật trạng thái; ghi rõ "not preregistered" |
| 7 | LOCO / cross-campaign | Literature Review §3.3.3: "Luận án sử dụng hai giao thức … LORO … LOCO". Master synthesis §2.2 diễn giải "LOCO thấp". `06_CROSS_CAMPAIGN_RESULTS.csv` (29/07) dùng định danh cảm biến kiểu cũ | **Không có giao thức LOCO.** Chỉ có chuyển giao exploratory CP2 ↔ CP3, mô hình deep, balanced accuracy 0.227–0.278, p nhỏ nhất 0.167 (có điều kiện), CP1 không đánh giá, campaign đích nằm trong pool HPO | **Có** | Sửa thuật ngữ trong Literature Review (LR-05); đánh dấu CSV 29/07 là superseded đối với claim |
| 8 | Sensor-configuration claims | Charter v1.1 §13 cho phép "Sensor configuration influences classification more strongly than model architecture choice". Charter v2.1 §3 và §10 có candidate "dominates". Ma trận §1 và §5 cũng vậy. Master synthesis M-02: xung đột, chuyển sang Paper 1B | v8.1 chỉ phân tích cấu hình đầy đủ nhất (S12 / S123); các tập con "outside the scope of this paper"; không có claim về cấu hình cảm biến. Khối sensor-subset (07/09) chỉ một seed: chênh lệch CP2 là 0.0018 so với SD_fold 0.06–0.09; biên độ CP3 là 0.157, nhỏ hơn SD giữa fold. Trong cùng một cấu hình, chênh lệch giữa mô hình lại lớn (CP3: 0.875 so với 0.399) | **Có** (ở cấp Charter) | Không sửa Charter. Ghi trạng thái ở ma trận §5A; đề xuất quyết định C-02 |
| 9 | Mô hình trong final manuscript | EVIDENCE_GATES: model register gồm "RF, 1D-CNN, ResNet1D". Charter: RF / 1D-CNN / ResNet1D | RF, SVM-RBF, 1D-CNN, ResNet1D; thêm Extra trees và HistGB ở Table A4 | Có (nhỏ) | Ghi vào bản sync của EVIDENCE_GATES |
| 10 | Trạng thái ResNet1D | "Confirm or remove ResNet1D based on provenance". Charter §9: provenance đang chờ. Candidate "ResNet1D corroborates" | **Giữ lại.** Sensor mode được xác minh (audit 24/08 "CLOSED — VERIFIED", đầu vào 4/8/12 kênh; kết luận 07/09 "đạt về mặt kỹ thuật"). 3 seed; 612 checkpoint được tái hiện. Claim "corroborates" không xuất hiện trong bài. File `RESNET1D_PROVENANCE_AUDIT.md` riêng không tồn tại | Có (lỗi thời) | Cập nhật CURRENT_STATUS, EVIDENCE_GATES, ma trận §5A |
| 11 | Uncertainty evidence | "Report run/fold uncertainty" (đang chờ); bảng uncertainty OPEN | SD_fold và SD_seed (ddof = 1); balanced accuracy từng fold (Table 6); quantisation 1/12, 1/36, 1/72. Không CI, không kiểm định ý nghĩa. Script xuất SD_fold không tìm thấy (ddof = 1 tái tạo được bảng). Không có permutation within-campaign | Có (lỗi thời) | Cập nhật EVIDENCE_GATES |
| 12 | Condition_Evidence interface | Interface v1.1 (04/08): G1 OPEN; handoff cần G1 đã ký hoặc quyết định provisional; chuỗi kết thúc bằng `Action_Record_ID`/`Status_Event`. Register D003–D010 OPEN hoặc BLOCKING_OPEN | Paper 1 cung cấp prediction cấp recording kèm campaign, run, recording, cấu hình, phiên bản mô hình, seed, split, commit; độ biến thiên; phạm vi hiệu lực. Quy tắc gộp là trung bình xác suất window rồi argmax (xác minh trong code, không preregistered). Không có Condition_Evidence register. Sensor_ID vật lý chưa xác minh | **Có** (chuỗi định danh và trạng thái) | Chỉ thêm header sync vào interface; thêm ghi chú vào register; không đổi chuỗi |
| 13 | Allowed claims | Charter v2.1 §10: allowed, candidate và prohibited, kèm số liệu cũ | Claim được phép theo v8.1: xem §2.2 mục 4–6. Cấm: chẩn đoán hiện trường, severity, độ cứng, preload, chuyển giao lab → field, AI hay họ mô hình vượt trội, cấu hình cảm biến chi phối, độ lớn thổi phồng do rò rỉ | **Có** | Ma trận §5A; bảng cuối báo cáo |
| 14 | Limitations | Chỉ có câu chung chung ("Evidence is currently insufficient") | Bảy nhóm hạn chế cụ thể (§2.3) | Có (thiếu) | CURRENT_STATUS §3; Paper 1A README |
| 15 | Paper 1 → Paper 2 handover | Interface §15: điều kiện handoff. Paper 2 README: "không dùng Paper 1 metrics làm evidence traceability" | v8.1 §1: "This study addresses that evidence layer alone". §5.5: danh sách thuộc tính provenance | Không mâu thuẫn, nhưng chưa nghiệm thu | Thêm handover statement vào CURRENT_STATUS, Paper 2 README, header interface |
| 16 | Metric cũ | Charter v2.1 §10, ma trận §5, master synthesis §2.4: RF ~0.862, 1D-CNN S12 ~0.841, ResNet1D ~0.828 | Đã superseded bởi Table 4 của v8.1 | **Có** | Ma trận §5A đánh dấu SUPERSEDED; câu chữ Charter chờ quyết định (C-03) |
| 17 | Nhãn candidate claim | AGENT_RULES §4.1, Charter §1(2), EVIDENCE_GATES: mọi claim Paper 1 là "Candidate claim pending Gate 1 closure" cho tới G1 PASS; M1 cần G1 đóng | v8.1 đã khóa khoa học để nộp | **Có** (C-04) | Giữ nhãn trong file quản trị; cần quyết định |
| 18 | Tên và phạm vi Paper 1 so với Charter v1.1 §10 | "Run-Aware Evaluation of Low-Cost Sensor Configurations…", nội dung gồm sensor configuration effects và CEI | Tên mới, không có hiệu ứng cấu hình cảm biến, không dùng thuật ngữ CEI (chỉ "condition evidence" và provenance) | **Có** (C-07) | Ghi nhận; tách Paper 1A/1B đang chờ thầy xác nhận |
| 19 | Điều hướng repository | MASTER_INDEX, SOURCE_OF_TRUTH, AGENT_RULES, EVIDENCE_GATES trỏ tới `00_GOVERNANCE/`, `02_EVIDENCE_BASE/`, `03_PAPERS/`, `05_DATA_CODE_AND_EXPERIMENTS/`, không thư mục nào tồn tại. Các README dùng `00_CURRENT_CONTROL`, `01_MASTER_SYNTHESIS`, `02_DEEP_READ_CURRENT` | Không áp dụng | **Có** (C-09, C-11) | Sửa MASTER_INDEX, Literature Review README, MASTER_FILE_INDEX. SOURCE_OF_TRUTH và AGENT_RULES để lại cho quyết định |
| 20 | Dashboard (CURRENT_PRIORITY, GATE_STATUS_DASHBOARD, CLAIM_EVIDENCE…) | Chỉ có trong archive (09/08), ưu tiên ghi G1 | Không áp dụng | Có (không có bản ACTIVE) | Chỉ thêm pointer; ưu tiên hiện hành do CURRENT_STATUS v2.4 mang. Không tạo dashboard mới để tránh nhân bản |

### 2.5 D. Bàn giao WP1 → WP2

```text
Vibration data
→ Condition Evidence
→ provenance + validity scope
→ BIM-linked component traceability
```

**Paper 1 bàn giao:**
- Prediction cấp recording (không phải cấp window), kèm campaign, run, recording, trạng thái, kích thích, cấu hình cảm biến (theo thành phần cảm biến), phiên bản mô hình, seed, split và code commit.
- SD_fold và SD_seed.
- Phạm vi hiệu lực: chỉ within-campaign; chuyển giao chưa được xác lập; CP1 chưa đánh giá chuyển giao.
- Danh sách provenance còn mở.

**Quy tắc cho Paper 2:**
1. Paper 2 **không** coi raw AI prediction là ground truth vô điều kiện. Một prediction chỉ thành `Condition_Evidence` khi mang theo provenance, phạm vi hiệu lực và độ bất định (Charter §7 CEI lock).
2. Cho tới khi G1 được ký, dữ liệu gốc từ Paper 1 chỉ được dùng làm bản ghi `CANDIDATE`/`DRAFT` để thiết kế đặc tả và fixture G2. Cả hai eligibility flag giữ `false` (interface §15). Không có handoff được nghiệm thu.
3. Softmax hay `predict_proba` không phải xác suất hư hỏng. Nhãn trạng thái chỉ vị trí bị thao tác, không phải severity.
4. Chuỗi định danh giữ nguyên: `Sensor_ID → BIM_GUID → Condition_Evidence_ID → Inspection_Record_ID → Action_Status`. `Sensor_ID` vật lý của Paper 1 chưa xác minh (D005), nên mắt xích Sensor → BIM ở phòng thí nghiệm chỉ ở mức candidate.

---

## 3. Gate 1 status and supporting artefacts

### 3.1 Kết luận

**Gate 1 = OPEN. Nhãn chính thức giữ nguyên `OPEN — PARTIAL EVIDENCE`.**
**Evidence is currently insufficient** để ghi Gate 1 = CLOSED.

Theo quy tắc, đóng Gate cần đủ ba thứ:
1. **Evidence:** đủ cho khoa học của Paper 1, nhưng phần lớn chưa được materialize vào repository.
2. **Tiêu chí nghiệm thu:** có trong bảng G1 của `EVIDENCE_GATES_v2.1.md`. File `EVIDENCE_GATES_v1.1_LIMITED_FEM.md` mà Charter v1.1 viện dẫn không tồn tại.
3. **Acceptance record đã ký:** **không có.**

Câu chữ thống nhất với deck v2 và explainer v2: "Gói bằng chứng Gate 1: sẵn sàng về mặt khoa học; chờ thầy rà soát và ký nghiệm thu chính thức." Câu này mô tả bằng chứng, không phải trạng thái Gate.

### 3.2 Đối chiếu từng hạng mục G1 (EVIDENCE_GATES v2.1)

| Hạng mục G1 | Artefact bắt buộc | Bằng chứng hiện có | Vị trí | Trong repo pack? | Khoảng trống |
|---|---|---|---|---|---|
| Dataset version | `DATASET_MANIFEST.csv` | `manifest.json` (216 recording, 6.899 window, `canonical_manifest_sha256 = f400e943…`) và `index.csv` (102 NPZ SHA-256); NPZ trên Kaggle khớp (IT-01) | `D:\…\v1\` | Không | Materialize; ghi chú lệch `selected_split_count = 18` |
| Run registry | `RUN_REGISTRY_LOCKED.csv` + data dictionary | `campaigns.csv`, `runs.csv`, `recordings.csv` canonical (trong bundle); `DATASET_REGISTRY_FINAL.csv` do IT bàn giao | Kaggle bundle trên D:; file IT không có trong project | Không | Chưa khóa; không có data dictionary |
| Input manifest | `FILE_PROVENANCE_REGISTER.csv` | 216 đường dẫn nguồn và 216 SHA-256; hash tính lại khớp | IT `evidence/DATASET_AUDIT.json` (không có trong project) | Không | **Byte identity lúc training không kiểm chứng được**, vì không có hash lúc load. Đây là hạn chế vĩnh viễn |
| Sensor metadata | `SENSOR_METADATA_REGISTER.csv` | `SENSOR_CHANNEL_MAP.csv`: kênh x, y, z, resultant; 8 hoặc 12 kênh | File IT không có trong project | Không | Serial thiết bị, vị trí lắp và đồng bộ PASCO chưa rõ (IT-02, IT-04) |
| Script/repo/version | commit hash / repo tag | commit `360c79f`, `git_dirty = false` trên 1.482 run; bốn bản mã giống hệt | Bundle / `_AUDIT_WORKSPACE` | Không | Không có tag; repo private |
| Fold definition | `LORO_PROTOCOL_PREREGISTERED.md` | Giao thức mô tả trong code và v8.1 §3.8 | Manuscript | Không | **Không preregistered.** Không đáp ứng hồi tố được (C-05) |
| Split-before-windowing | evidence log | Window cắt trong recording **trước** khi chia; gán nguyên run; 0 vi phạm | v8.1 §3.5 và §3.8; `01_PROTOCOL_AND_LEAKAGE_AUDIT.md` (D:) | Không | Câu chữ tiêu chí không khớp nghĩa đen; tương đương về chức năng (C-05) |
| Train-only preprocessing | evidence log | Per-window standardisation (thống kê của chính window, mọi partition); StandardScaler của SVM chỉ fit trên train | v8.1 §3.6; IT-05 | Không | Câu chữ tiêu chí (C-05) |
| Common seeds | config | DL 42/43/44; RF và SVM `random_state = 42` | Table A2; `EXECUTED_CONFIGS.json` (IT, không có trong project) | Không | RF và SVM một seed |
| Model configuration | `MODEL_CONFIGURATION_REGISTER.csv` | Table A2; `bao_cao_lua_chon_hyperparameter.pdf` | Manuscript; `03_PAPER_1A_GATE1/` | Không (chưa có file) | Chưa có register |
| Output metrics | metrics table | Tables 4–7, A3–A7; 469/472 khớp, 3 đã sửa | v8.1; `METRIC_AGGREGATION_CHECK.csv` (IT, không có trong project) | Không | Xác suất từng window không được lưu trữ |
| Run/fold uncertainty | uncertainty table | SD_fold, SD_seed (ddof = 1); Table 6 | v8.1 | Không | Không có permutation within-campaign |
| ResNet1D provenance | `RESNET1D_PROVENANCE_AUDIT.md` | Sensor mode được xác minh; 612 checkpoint được tái hiện | `02_DATA_CODE_AND_EXPERIMENTS/OUTPUT/24.08.2026/GATE1_LORO_UPDATED_RESULTS_AUDIT_20260824.md`; IT-05 | Không (chưa có file riêng) | Thiếu file audit riêng |
| Rerun conditions | rerun note | Notebook, config, bundle | D: | Không | Không có rerun note; CSV raw và canonical không có ở local |
| **Gate sign-off** | **`G1_ACCEPTANCE_MATRIX.md`** | **Không có** | — | **Không** | **CHẶN** |

### 3.3 Danh sách artefact còn thiếu để có thể xét đóng Gate 1

1. Thư mục `G1_EXECUTION_PACK/`. Đường dẫn chỉ định nằm dưới gốc `05_DATA_CODE_AND_EXPERIMENTS`, là thư mục không tồn tại (C-11).
2. `DATASET_MANIFEST.csv`, `RUN_REGISTRY_LOCKED.csv` kèm data dictionary, `FILE_PROVENANCE_REGISTER.csv` và `SENSOR_METADATA_REGISTER.csv`. Có thể materialize từ file bàn giao IT-01/IT-02 và bundle Kaggle mà không cần phân tích mới.
3. File bàn giao IT-01 đến IT-06 và thư mục `evidence/` phải được lưu vào project.
4. `LORO_PROTOCOL_PREREGISTERED.md`, hoặc quyết định của thầy chấp nhận giao thức đã ghi nhận nhưng không preregistered (C-05).
5. Evidence log cho split-before-windowing và train-only preprocessing, viết theo cách triển khai thực tế, hoặc quyết định sửa câu chữ tiêu chí (C-05).
6. `MODEL_CONFIGURATION_REGISTER.csv`, file seed/config và rerun note.
7. `RESNET1D_PROVENANCE_AUDIT.md`, tổng hợp từ audit 24/08 và IT-05.
8. `PAPER1_CLAIM_STATUS_TABLE.md` (M1). Bảng cuối báo cáo này có thể làm bản nháp.
9. Kết quả keyword check thuật ngữ trước khi đóng Gate (TERMINOLOGY §4).
10. **`G1_ACCEPTANCE_MATRIX.md` do thầy ký.**

Các phân tích mà kết luận kỹ thuật 07/09 từng đề xuất nhưng **không** thực hiện trong pass này, vì không được phép chạy phân tích mới:
- permutation within-campaign;
- seed 43 và 44 cho RF/SVM và cho khối sensor-subset;
- đối chiếu hash ngay trên Kaggle.

Việc G1 có bắt buộc các phân tích này hay không là quyết định của thầy (C-06).

---

## 4. Files updated + lý do

Mọi file dưới đây đã được sao lưu trước khi sửa vào `01_LITERATURE_REVIEW/90_ARCHIVE/01_SUPERSEDED_VERSIONS/PRE_SYNC_20260913/`, kèm `PRE_SYNC_BACKUP_MANIFEST_20260913.csv` (SHA-256).

| # | File | Thay đổi | Lý do |
|---|---|---|---|
| 1 | `01_CURRENT_CONTROL/CURRENT_STATUS_AND_NEXT_DIRECTION.md` (v2.3 → v2.4) | Thêm dòng Paper 1 (`SCIENCE LOCKED`) và G5. Mô tả lại blocker G1 (nhãn không đổi). Thêm §3 (RQ1/WP1 đã tạo ra gì và hạn chế) và §4 (handover WP1 → WP2). Thay ba workstream bằng ưu tiên P1/P2/P3. Cập nhật §8 | Nguồn trạng thái thực thi (level 5) đang lỗi thời so với final Paper 1 |
| 2 | `01_CURRENT_CONTROL/MASTER_INDEX_CURRENT.md` (v2.3 → v2.4) | Sửa đường dẫn theo cây thực tế; thêm mục Paper 1 và G1 evidence; liệt kê file được viện dẫn nhưng không tìm thấy; cập nhật state summary | Điều hướng trỏ tới năm thư mục không tồn tại |
| 3 | `01_CURRENT_CONTROL/RQ_WP_CHAPTER_PAPER_GATE_MATRIX_v2.1.md` (v2.3 → v2.4) | Thêm §5A (trạng thái claim Paper 1 sau khi khóa khoa học); thêm ghi chú xung đột kiến trúc dưới §1; thêm ghi chú sync ở §7. **Các dòng kiến trúc giữ nguyên** | Đồng bộ trạng thái claim mà không sửa kiến trúc hay Charter |
| 4 | `01_CURRENT_CONTROL/EVIDENCE_GATES_v2.1.md` (v2.3 → v2.4) | Thêm mục "G1 / M1 evidence sync (13/09/2026)"; cập nhật dòng "Current priority". **Cột Status của từng hạng mục giữ nguyên** | Hiện trạng bằng chứng G1 thay đổi nhưng không có sign-off |
| 5 | `01_CURRENT_CONTROL/G1_G2_INTERFACE_DECISION_REGISTER.csv` | Thêm ghi chú `[Sync 13/09/2026]` vào cột Notes của D003–D010. **Status giữ nguyên** | Paper 1 cung cấp dữ kiện cho các quyết định mở; việc quyết định vẫn thuộc thầy |
| 6 | `02_DEEP_READ_CURRENT_PDF/03_RQ2_GATE2_3/G1_TO_G2_CONDITION_EVIDENCE_INTERFACE_v1.0.md` | Chỉ thêm khối "Sync note 13/09/2026" (metadata trạng thái). Nội dung spec giữ nguyên | Ghi rõ G1 chưa ký, chuỗi canonical kết thúc bằng `Action_Status`, và quy tắc handover |
| 7 | `01_CURRENT_CONTROL/README.md` | Thêm pointer tới trạng thái hiện hành và báo cáo này | Điều hướng |
| 8 | `01_LITERATURE_REVIEW/README.md` | Sửa tên thư mục thực tế; thêm dòng trạng thái | Tên thư mục cũ không tồn tại |
| 9 | `99_INDEX_AND_LOG/MASTER_FILE_INDEX_CURRENT.md` | Sửa tên thư mục; thêm dòng trạng thái Paper 1, G1 và ưu tiên | Điều hướng |
| 10 | `03_OUTPUTS/03_PAPER_1A_GATE1/Paper 1.md/README.md` | Viết lại thành Paper 1 status record | Status record lỗi thời |
| 11 | `03_OUTPUTS/04_PAPER_1B_SENSOR_CONFIGURATION/README.md` | Thêm ghi chú trạng thái claim cấu hình cảm biến | Claim đã tách khỏi Paper 1 và chưa được bằng chứng hỗ trợ |
| 12 | `03_OUTPUTS/05_PAPER_2_TRACEABILITY/README.md` | Thêm quy tắc handover | WP1 → WP2 |
| 13–15 | `90_ARCHIVE/…/08_CURRENT_STATUS_DASHBOARD/CURRENT_PRIORITY.md`, `GATE_STATUS_DASHBOARD.md`, `CLAIM_EVIDENCE_LIMITATION_NEXT_ACTION.md` | **Chỉ thêm một dòng pointer** "ARCHIVED — superseded" | Tránh dùng nhầm dashboard ngày 09/08 |
| 16 | `01_CURRENT_CONTROL/PAPER1_SCIENCE_LOCK_PROJECT_SYNC_REPORT_20260913.md` | **Tạo mới** (báo cáo này) | Hồ sơ đồng bộ |

**Đã rà soát nhưng cố ý KHÔNG sửa:**
- Nhóm file có thẩm quyền cao hoặc đang có quyết định treo: `MASTER_RESEARCH_CHARTER_CURRENT_20260812.md`, Charter 17/07 (archive), ADR-2026-001, `SOURCE_OF_TRUTH_HIERARCHY_v2.1.md`, `AGENT_RULES.md`, `TERMINOLOGY_CONTROL_CURRENT.md`, `CURRENT_DIRECTION_LOCK_20260804.md`.
- Nhóm file vẫn đúng: `RESEARCH_DIRECTION_AND_SCOPE.md` và `RESEARCH_ARCHITECTURE.md` vẫn ghi đúng "No Gate is PASS".
- Nhóm file thuộc P1 hoặc cần một vòng sync riêng: `LIVING_EVIDENCE_BASE_CURRENT_20260812.md`, `MASTER_LITERATURE_AND_EVIDENCE_SYNTHESIS_v2_20260828.md`.
- Toàn bộ file manuscript, deck và Literature Review docx.
- README của Paper 3 và Chuyên đề 1: không có trạng thái Paper 1 cần đồng bộ.

---

## 5. Conflicts / unresolved items

Không xung đột nào dưới đây được tự giải quyết. Charter không bị sửa. Mỗi mục kèm quyết định đề xuất cần phê duyệt.

| ID | Xung đột | Nguồn (cao hơn ↔ thấp hơn / thực tế) | Xử lý trong pass này | Quyết định đề xuất (người phê duyệt) |
|---|---|---|---|---|
| C-01 | **Kiến trúc Gate và Paper** | Charter v1.1 §10–11 và v2.1 §4, §5, §9: Paper 2 → G2, G3, G6; Paper 3 (bonus) → G4, G5; Paper 4 optional; C7 optional; G6 là Paper 2 submission; G7 là thesis synthesis. Ngược lại, kiến trúc khóa dùng cho deck v2 và Literature Review README: Paper 2 → G2–G3; Paper 3 → G4–G5; WP4 là decision-support synthesis, không có bài báo bắt buộc; không có G6 | Giữ nguyên các dòng ma trận; thêm ghi chú xung đột | Thầy chọn: (a) giữ G6/G7 như submission/synthesis milestone (giống M1, không phải evidence gate), hoặc (b) bỏ G6/G7 và Paper 4. Cần một ADR mới và đồng bộ Charter v2.1, ma trận, EVIDENCE_GATES, Literature Review Bảng 5.2 |
| C-02 | **Claim cấu hình cảm biến** | Charter v1.1 §13 và Charter 17/07 §10 (level 2) cho phép "Sensor configuration influences classification more strongly than model architecture choice"; Charter v2.1 có candidate "dominates". Final Paper 1 không đưa ra claim này, và bằng chứng hiện có không ủng hộ nó (khối sensor-subset một seed; chênh lệch giữa mô hình trong cùng cấu hình lớn; M-02) | Ma trận §5A ghi "NOT CLAIMED; NOT SUPPORTED at current evidence" | Thầy quyết định bỏ claim khỏi Allowed claims, hoặc chuyển thành giả thuyết Paper 1B cần bằng chứng multi-seed. Cần ADR hoặc Charter amendment |
| C-03 | **Metric cũ trong Charter** | Charter v2.1 §10 và ma trận §5: RF ~0.862, 1D-CNN ~0.841, ResNet1D ~0.828. v8.1 Table 4 cho số mới | Ma trận §5A đánh dấu SUPERSEDED | Thay bằng pointer tới v8.1 Table 4 trong lần sửa Charter kế tiếp |
| C-04 | **Nhãn candidate và M1 so với việc khóa khoa học** | Charter v2.1 §1(2), AGENT_RULES §4.1, EVIDENCE_GATES M1: claim là candidate và chưa được nộp cho tới khi G1 đóng. v8.1 đã khóa khoa học | Giữ nhãn trong file quản trị; Paper 1 = SCIENCE LOCKED, không phải SUBMISSION READY | Thầy ký G1 sau khi pack được materialize, **hoặc** phê duyệt bằng văn bản ngoại lệ M1 cho phép nộp SHM trong khi G1 chờ ký |
| C-05 | **Câu chữ tiêu chí G1 so với cách triển khai** | EVIDENCE_GATES đòi "Split ở cấp run TRƯỚC khi windowing", "Scaler/normalisation fit chỉ trên train fold", `LORO_PROTOCOL_PREREGISTERED.md`. Thực tế: window cắt trong recording trước khi chia rồi gán nguyên run; per-window standardisation; SVM scaler chỉ fit trên train; giao thức và quy tắc gộp validation không preregistered (báo cáo 27/08) | Ghi nhận; không đổi tiêu chí | Thầy quyết định chấp nhận tương đương chức năng kèm khai báo không preregistered, hoặc sửa câu chữ tiêu chí qua change control |
| C-06 | **Phạm vi bằng chứng tối thiểu để đóng G1** | Kết luận 07/09 đề xuất permutation within-campaign, thêm seed 43/44 cho RF/SVM và sensor-subset, đối chiếu hash trên Kaggle. Pass này cấm phân tích mới | Không chạy | Thầy xác định các phân tích này có bắt buộc cho G1 hay không. Nếu có, cần ủy quyền riêng |
| C-07 | **Phạm vi Paper 1 so với Charter v1.1 §10** | Charter: tên "…Low-Cost Sensor Configurations…", nội dung lõi gồm sensor configuration effects và CEI. Final: tên mới, không có hiệu ứng cấu hình, CEI chuyển sang giai đoạn tích hợp của Paper 2 | Ghi nhận | Thầy xác nhận chính thức việc tách Paper 1A/1B (revision log 28/08, mục 3, còn treo) và việc CEI chuyển sang Paper 2 |
| C-08 | **Câu chữ RQ1** | Charter v1.1 §7 (nguyên văn, không có vế "chi phối") khác Charter v2.1 §3 (thêm "cấu hình cảm biến có chi phối mạnh hơn…") | Theo v1.1 (nguồn cao hơn) | Sửa Charter v2.1 §3 về nguyên văn v1.1 |
| C-09 | **Vị trí baseline 17/07 và drift điều hướng** | SOURCE_OF_TRUTH level 2 trỏ tới `../02_EVIDENCE_BASE/06-MASTER_RESEARCH_CHARTER_v1.1…`, nhưng file chỉ còn trong `90_ARCHIVE`; Council Review cũng vậy. SOURCE_OF_TRUTH, AGENT_RULES, EVIDENCE_GATES, RESEARCH_ARCHITECTURE còn trỏ tới `00_GOVERNANCE/`, `02_EVIDENCE_BASE/`, `03_PAPERS/` | MASTER_INDEX và README đã sửa; file level 1/4 để nguyên | Phê duyệt đặt một bản sao read-only của Charter v1.1 và Council Review vào `01_CURRENT_CONTROL/` (như ADR-2026-001), rồi sửa đường dẫn trong SOURCE_OF_TRUTH, AGENT_RULES, EVIDENCE_GATES |
| C-10 | **Chuỗi định danh trong interface** | Interface v1.1 §2 và §17 dùng `Action_Record_ID`/`Status_Event`. Chuỗi khóa kết thúc bằng `Action_Status` (baseline 17/07, khôi phục 11/08) | Chỉ thêm header sync; không đổi chuỗi | Xử lý qua ADR Action-Status-Event (G2); sửa interface thành v1.2 sau quyết định |
| C-11 | **Đường dẫn G1_EXECUTION_PACK** | EVIDENCE_GATES: `05_DATA_CODE_AND_EXPERIMENTS/G1_EXECUTION_PACK/`. Thực tế: gốc là `02_DATA_CODE_AND_EXPERIMENTS/` | Ghi nhận | Chỉ định đường dẫn chính thức, ví dụ `02_DATA_CODE_AND_EXPERIMENTS/G1_EXECUTION_PACK/` |
| C-12 | **Bằng chứng G1 nằm ngoài repository** | Bundle Kaggle, NPZ `v1`, bộ audit 07/09 ở `D:\01_RESEARCH\08_Output_07.09\`; file bàn giao IT không có ở đâu trong project | Ghi nhận | NCS và IT đưa vào repository (chỉ sao chép, không phân tích lại) |
| C-13 | **Thứ tự P2 so với quy tắc CQ trước schema** | Ưu tiên P2 mở đầu bằng "formal traceability model", trong khi EVIDENCE_GATES G2 và Direction Lock cấm build hoặc freeze schema trước khi CQ và verification criteria được duyệt | Diễn giải "formal traceability model" là mô hình khái niệm, chưa phải schema build hay freeze (§6) | Thầy xác nhận cách diễn giải |
| C-14 | **P3 baseline so với field deployment** | "Operational baseline" trong P3; Charter §6.1 xếp việc thu baseline dài hạn vào field deployment, chỉ được làm sau khi G4 mở và có field access | Diễn giải P3 chỉ là chuẩn bị protocol | Xác nhận field-access basis trước khi thu baseline |
| C-15 | **Data availability** | M1 đòi hỏi reproducibility package. Không có DOI công khai; repo code private; CSV raw và canonical không có ở local | Ghi nhận | Tác giả quyết định có lưu Zenodo/DOI hay không (pre-submission audit §5) |
| C-16 | **Con số "294" trong bộ audit 07/09** | `06_GATE1_TECHNICAL_VERDICT.md` (D:) ghi 294/294 candidate; quyết định đã khóa thay bằng câu 192 | Không dùng 294 trong file quản trị | Không cần; ghi để tránh trích dẫn lại |
| C-17 | **Câu chữ "bonus / Paper 4"** | Charter v2.1, ma trận, RESEARCH_DIRECTION dùng "bonus/optional"; deck v2 đã bỏ | Không sửa | Gộp vào quyết định C-01 |

---

## 6. New current priorities

### 6.1 P1 — Hoàn thiện Báo cáo tiểu luận tổng quan

- **Đầu vào:** `03_OUTPUTS/01_TIEU_LUAN_TONG_QUAN/TIEU_LUAN_TONG_QUAN_HOAN_CHINH_v2_13092026.docx`.
- **Việc cần làm:** áp dụng danh sách §6.4. Không viết lại toàn bộ và không thêm kết quả Paper 1 như kết luận luận án khi chưa quyết định (LR-01).
- **Tiêu chí xong:** có bản v3 kèm changelog, keyword check thuật ngữ và thầy rà soát.

### 6.2 P2 — Gate 2–3

Thứ tự thực hiện, giữ quy tắc CQ trước schema:

1. **Formal traceability model:** mô hình khái niệm gồm thực thể, quan hệ và định danh trên chuỗi khóa `Sensor_ID → BIM_GUID → Condition_Evidence_ID → Inspection_Record_ID → Action_Status`, kèm CEI metadata. Chưa build hay freeze schema (C-13).
2. **Competency questions:** SCQ/VCQ/RCQ và verification criteria, preregistered và được thầy duyệt.
3. **Quy tắc định danh và toàn vẹn:** constraint catalogue; giải quyết D003–D017 trong register.
4. **Fixture hợp lệ và không hợp lệ:** fixture/oracle manifest, chỉ sau khi CQ được duyệt. Có thể dùng bản ghi candidate có nguồn từ Paper 1, luôn giữ eligibility = false.
5. **Kiểm chứng hai chiều và end-to-end:** thuộc G3; thực thi vẫn `NOT OPEN` cho tới khi G2 được baseline. **Do not run Graph 02.**

### 6.3 P3 — Chuẩn bị G4 tại hiện trường (preparation only)

1. `Sensor_ID`: field sensor register.
2. `BIM_GUID`: mapping protocol và audit độ ổn định GUID.
3. Metadata lắp đặt và provenance: serial thiết bị, vị trí lắp, hướng trục, đồng bộ, hash lúc load. Đây chính là các khoảng trống Paper 1 không đóng được.
4. Protocol baseline vận hành. Việc thu thật là field deployment, chỉ làm khi G4 mở (C-14).
5. Kịch bản đánh giá khả thi truy vết tại hiện trường (2–3 kịch bản).

Không triển khai và không claim ở bước này. Field access vẫn chưa được xác nhận.

**Việc hành chính mang theo, chạy song song, không chen trước P1–P3:**
- (a) Materialize `G1_EXECUTION_PACK` từ artefact đã có, xin quyết định C-04, C-05, C-06, rồi xin ký `G1_ACCEPTANCE_MATRIX.md`.
- (b) Các mục tác giả của Paper 1 (§2.1); nộp SHM sau khi G1 được ký hoặc có ngoại lệ đã phê duyệt.

**Không phải ưu tiên hiện tại:**
- **Gate 5** (logic bốn mức, expert review): giữ OPEN.
- Không mở phân tích Paper 1 mới (RF/SVM transfer, multi-seed, permutation within-campaign) nếu thầy chưa ủy quyền.

### 6.4 UPDATES REQUIRED IN LITERATURE REVIEW AFTER PAPER 1 SCIENCE LOCK

Đối tượng: `TIEU_LUAN_TONG_QUAN_HOAN_CHINH_v2_13092026.docx`. Pass này **không** viết lại Literature Review.

| # | Vị trí (Literature Review v2) | Hiện đang viết | Cần cập nhật | Nhóm | Cần quyết định trước? |
|---|---|---|---|---|---|
| LR-01 | Ch.1, đoạn phương pháp tổng quan ("Tiểu luận không nhằm trình bày kết quả cuối cùng…") | Không dùng kết quả sơ bộ | Giữ nguyên tắc. Thêm ghi chú trạng thái có ngày: Paper 1 khóa khoa học 13/09/2026 (v8.1), G1 chờ ký. Chỉ trỏ tới Paper 1, không chép số | Kết quả trước tạm thời, nay đã chốt | Có: tác giả chọn có đưa số liệu hay không (khuyến nghị: không) |
| LR-02 | §3.2.1 Cấu hình cảm biến | Cấu hình cảm biến hỗ trợ RQ1; không tìm vị trí tối ưu | Thêm: Paper 1 chỉ phân tích cấu hình đầy đủ nhất; so sánh tập con thuộc Paper 1B; không viết "cấu hình cảm biến chi phối kiến trúc" | Claim Paper 1 | Có (C-02) |
| LR-03 | §3.2.2 Tiền xử lý | Nguyên tắc "chia theo đơn vị vật lý trước các phép biến đổi học được" | Giữ như nguyên tắc từ tài liệu. Khi nói về dữ liệu của luận án thì mô tả đúng cách làm: cắt window trong recording, gán nguyên run, không window nào vượt ranh giới split, per-window standardisation không fit trên train, SVM scaler chỉ fit trên train | Thuật ngữ / claim | Không |
| LR-04 | §3.3.1, §5.5.2 (G1), §5.6.1 "đơn vị độc lập" | Dùng "đơn vị độc lập" chung | Với dữ liệu luận án, dùng "đơn vị nhóm thu nhận (acquisition grouping unit) = lần chạy". Không gọi run là independent experimental unit đã kiểm chứng | Thuật ngữ | Không |
| LR-05 | §3.3.3 LORO/LOCO | "Luận án sử dụng hai giao thức … LORO … LOCO" | Ghi đúng: LORO đã chạy (4/1/1, 30 tổ hợp). Liên campaign chỉ có **chuyển giao exploratory CP2 ↔ CP3** với mô hình deep; không phải giao thức LOCO; CP1 không đánh giá; chuyển giao chưa được xác lập. Giữ LOCO như khái niệm lấy từ tài liệu | Tạm thời → đã chốt; claim | Không |
| LR-06 | §3.3.4 Cơ chế bổ trợ | Permutation phải bảo toàn cấu trúc nhóm; nhiều seed | Thêm: Paper 1 dùng permutation nhãn recording không giới hạn (exchangeability chưa biện minh; chỉ mô tả), chỉ cho cross-campaign; within-campaign so với mức 0.25 lý thuyết; DL 3 seed, RF/SVM 1 seed | Hạn chế | Không |
| LR-07 | §3.4.1 Thuộc tính tối thiểu của bản ghi | Sáu thuộc tính | Đồng bộ với v8.1 §5.5: cấu hình theo thành phần cảm biến (không theo số lượng); campaign và run; thứ tự đo trạng thái; giao thức và grouping unit; độ biến thiên; chuyển giao có được đánh giá không và kết quả | Chuyển RQ1 → RQ2 | Không |
| LR-08 | §3.4.2 Phạm vi hiệu lực | "Kết quả chuyển giao kém giữa các đợt là thông tin về giới hạn…" (giả định) | Chuyển sang dạng đã ghi nhận: CP3 yếu hơn và phụ thuộc fold; chuyển giao chưa được xác lập. Không nói "tương đương mức ngẫu nhiên", không nói "không thể chuyển giao" | Tạm thời → đã chốt | Không |
| LR-09 | §5.5.1 Bảng 5.2 | RQ3 → G4; WP4 → "Chương 7 nếu tách riêng / Bài báo 4 tùy chọn hoặc gộp Bài báo 3" | Theo kiến trúc khóa: RQ3 → G4–G5; WP4 là decision-support synthesis, không có bài báo bắt buộc | Kiến trúc | **Có (C-01)** |
| LR-10 | §5.5.3 Cổng hiện tại ("vẫn là G1, với bảy yêu cầu…") | Bảy yêu cầu như chưa làm | Ghi trạng thái từng yêu cầu theo §3.2 báo cáo này; G1 chính thức vẫn OPEN, chờ ký; ưu tiên nghiên cứu chuyển sang G2–G3 | Tạm thời → đã chốt | Không |
| LR-11 | §5.7.1 Đóng góp 1 | "đóng góp dự kiến nằm ở việc kết hợp chúng thành một quy trình tái lập được" | **Mâu thuẫn với v8.1** ("Neither the controls nor their combination is claimed as novel"). Đổi thành: hệ quả được ghi nhận bằng thực nghiệm trên dữ liệu khung thép bắt bu lông, cộng với cách báo cáo có provenance. "Dự kiến" → "đã hình thành ở mức bằng chứng phòng thí nghiệm (Paper 1; chờ nghiệm thu G1)" | Claim Paper 1 | Không |
| LR-12 | §5.7.1 đoạn 2 ("Nếu kết quả suy giảm giữa các đợt…") | Câu điều kiện | Thay bằng kết quả đã ghi nhận, kèm biên | Tạm thời → đã chốt | Không |
| LR-13 | §5.8.1 Bảng 5.4 "Phạm vi hỗ trợ" | "mô hình phần tử hữu hạn danh nghĩa để tham chiếu" | Viết đủ qualifier: "danh nghĩa, chưa hiệu chuẩn, chỉ tham chiếu, không dùng cho chẩn đoán hư hỏng". Không tìm thấy đoạn FEM-core cũ nào khác | FEM / kiến trúc cũ | Không |
| LR-14 | §5.8 Giới hạn | Chưa có giới hạn cụ thể của bằng chứng lab | Thêm tóm tắt các hạn chế ở §2.3 (18 run, một mẫu vật; campaign không phải replicate; thứ tự đo; ánh xạ và đồng bộ cảm biến; byte identity; HPO; một seed; không đo độ thổi phồng do rò rỉ) | Hạn chế | Không |
| LR-15 | §5.9.1–5.9.2 và §5.10 đoạn cuối | "Ưu tiên 1 – Đóng G1"; "Trước hết phải đóng G1…" | Cập nhật: bằng chứng khoa học G1 đã xong; ký nghiệm thu là việc hành chính song song; tiếp theo là G2–G3, rồi chuẩn bị G4; G5 sau cùng | Tạm thời → đã chốt; RQ1 → RQ2 | Không |
| LR-16 | Chuyển tiếp cuối Ch.3 sang Ch.4; §5.6.1 mũi tên 1 | Có mô tả nghĩa vụ của mũi tên thứ nhất | Thêm handover: "Vibration data → Condition Evidence → provenance + validity scope → BIM-linked component traceability". Paper 2 không coi raw AI prediction là ground truth vô điều kiện. Evidence từ G1 là candidate cho tới khi G1 ký | Chuyển RQ1 → RQ2 | Không |
| LR-17 | RQ1 (Ch.1 và §5.4) | Nguyên văn RQ1 bản dịch tiếng Việt | Giữ nguyên văn Charter v1.1. Thêm ghi chú: Paper 1 trả lời phần độ tin cậy của bằng chứng cho cấu hình đầy đủ nhất; phần cấu hình cảm biến thuộc Paper 1B (chưa xong) | Claim Paper 1 | Không |
| LR-18 | Toàn văn: câu về rò rỉ | Nguyên tắc từ tài liệu ("sẽ bị đánh giá lạc quan") | Kiểm tra: không câu nào nói dữ liệu luận án đã cho thấy thổi phồng do random split, vì Paper 1 không chạy so sánh này | Claim | Không |
| LR-19 | Tài liệu tham khảo Ch.3 | Tập tham khảo hiện tại | Tùy chọn: bổ sung các tài liệu đã xác minh trong Paper 1 nếu dùng (Teloli 2022; Zorzi 2025; Wernitz 2022; Goodarzi 2025; Varma & Simon 2006; Vabalas 2019) | Hỗ trợ claim | Không |
| LR-20 | Tài liệu nguồn của Literature Review: `MASTER_LITERATURE_AND_EVIDENCE_SYNTHESIS_v2`, `LIVING_EVIDENCE_BASE_CURRENT` | Số cũ (0.862…); M-02 "ĐANG XUNG ĐỘT"; "LORO + ResNet1D sensor-mode verification là mục G1 mở" | Cần một vòng sync riêng cho hai file này (không làm trong pass này) | Tạm thời → đã chốt | Không |

### 6.5 Bảng tổng hợp cuối

| Claim / Status | Evidence artefact | Repository file updated | Final state |
|---|---|---|---|
| Paper 1 status | `PAPER1_v8.1_SHM_RISK_REDUCED.docx`; `PAPER1_v8.1_SHM_PRE_SUBMISSION_AUDIT.md` (50/50 PASS) | CURRENT_STATUS v2.4; Paper 1A README; MASTER_INDEX v2.4 | **SCIENCE LOCKED**; chưa submission-ready; chưa nộp |
| Gate 1 | EVIDENCE_GATES G1 table; `06_GATE1_TECHNICAL_VERDICT.md` (D:); `BAO_CAO_IT01_IT06.md` | CURRENT_STATUS v2.4; bản sync EVIDENCE_GATES; ma trận §7 | **`OPEN — PARTIAL EVIDENCE`**. Evidence is currently insufficient để ghi CLOSED; không có acceptance đã ký |
| Dataset 3 / 18 / 216 / 6.899 | `v1/manifest.json`; IT-01; v8.1 §3.5 | CURRENT_STATUS §3; bản sync EVIDENCE_GATES | Đã đối chiếu trên bản lưu trữ; byte identity lúc training chưa kiểm chứng |
| Run registry khóa | recordings.csv trong bundle; `DATASET_REGISTRY_FINAL.csv` (IT, không có trong project) | Bản sync EVIDENCE_GATES | Có ngoài repo; **chưa khóa** trong G1_EXECUTION_PACK |
| Leakage-safe run-aware evaluation | `01_PROTOCOL_AND_LEAKAGE_AUDIT.md` (D:); IT-05; v8.1 §3.5–3.9 | Bản sync EVIDENCE_GATES; ma trận §5A | Được hỗ trợ trong từng fit; phụ thuộc HPO của mô hình deep đã khai báo; câu chữ tiêu chí chờ quyết định (C-05) |
| LORO | v8.1 Table 3; audit 24/08 | CURRENT_STATUS §3 | Đã chạy (30 tổ hợp mỗi case); không preregistered |
| Chuyển giao cross-campaign | v8.1 §4.7, Table 7, Table A5 | Ma trận §5A | Exploratory; chuyển giao chưa được xác lập; CP1 không đánh giá |
| Kết quả chính RF/SVM | v8.1 Table 4 | Ma trận §5A | Đã khóa trong manuscript; Candidate claim pending Gate 1 closure |
| "Sensor configuration dominates / influences more than architecture" | Kết luận 07/09 §4; M-02; v8.1 §3.3 | Ma trận §5A; Paper 1B README | **Không claim; không được bằng chứng hiện có hỗ trợ**; xung đột Charter (C-02) |
| Metric cũ RF ~0.862 / 1D-CNN ~0.841 / ResNet1D ~0.828 | Superseded bởi v8.1 Table 4 | Ma trận §5A | SUPERSEDED (câu chữ Charter chờ C-03) |
| ResNet1D | Audit 24/08; kết luận 07/09; IT-05 | CURRENT_STATUS §3; bản sync EVIDENCE_GATES | **Giữ lại**; sensor mode xác minh về kỹ thuật; thiếu file audit riêng |
| Uncertainty | v8.1 §3.10, Tables 4–6; IT-06 | Bản sync EVIDENCE_GATES | Đã báo cáo SD_fold và SD_seed; không có permutation within-campaign; không CI |
| Condition_Evidence handover | Interface v1.1; decision register | Header interface; ghi chú register; Paper 2 README; CURRENT_STATUS §4 | **Chưa nghiệm thu**; chỉ là candidate cho thiết kế G2 |
| Chuỗi định danh | Charter v1.1; Direction Lock | Không (giữ nguyên) | **LOCKED:** `Sensor_ID → BIM_GUID → Condition_Evidence_ID → Inspection_Record_ID → Action_Status` |
| FEM | Charter v1.1 §15; ADR-2026-001 | Không (giữ nguyên) | nominal, uncalibrated, reference-only, not used for damage diagnosis; không dùng trong Paper 1 |
| Ưu tiên hiện hành | Báo cáo này §6 | CURRENT_STATUS v2.4 §7; MASTER_FILE_INDEX | P1 Literature Review; P2 G2–G3; P3 chuẩn bị G4; G5 không phải ưu tiên hiện tại |
| Điều hướng | Kiểm tra cây thư mục ngày 13/09 | MASTER_INDEX v2.4; Literature Review README; MASTER_FILE_INDEX | Đã sửa những chỗ xác minh được; đường dẫn trong SOURCE_OF_TRUTH và AGENT_RULES chờ quyết định (C-09) |
| Dashboard lưu trữ | `90_ARCHIVE/…/08_CURRENT_STATUS_DASHBOARD/` | Pointer trong 3 file | ARCHIVED — đã thêm pointer |
