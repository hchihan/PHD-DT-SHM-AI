# RÀ SOÁT KẾT QUẢ CẬP NHẬT — BƯỚC 1 (DAO ĐỘNG) & BƯỚC 2 (BIM/IFC)

**Ngày lập:** 2026-08-05 | **Người lập:** Cowork Research Coordination Agent
**Phạm vi:** rà soát toàn bộ workspace `01_PHD_DT_AI_AM`, ưu tiên bản mới nhất, loại bản đã bị thay thế.
**Trạng thái:** BÁO CÁO RÀ SOÁT — KHÔNG ĐÓNG BẤT KỲ GATE NÀO.

---

## 0. Khai báo đầu nhiệm vụ

| Mục | Bước 1 | Bước 2 |
|---|---|---|
| RQ | RQ1 | RQ2 |
| WP | WP1 | WP2 |
| Chương / Paper | Chương 4 / Paper 1 | Chương 5 / Paper 2 |
| Evidence Gate hiện tại | **G1 — `OPEN — PARTIAL EVIDENCE`** | **G2 — `OPEN — LITERATURE BOUNDARY CLOSED, SPECIFICATION NOT YET FROZEN`**; G3 `NOT OPEN` |
| Phân loại phạm vi | Core Scope | Core Scope (công cụ Revit/IFC/Dynamo = Supporting) |

Nguồn trạng thái: `01_CURRENT_CONTROL/CURRENT_STATUS_AND_NEXT_DIRECTION.md` (v2.2, 2026-08-04) và `02_EVIDENCE_BASE/CURRENT/01_MASTER_G1_G2_G3_EVIDENCE_SYNTHESIS_20260804.md` (v1.0, 2026-08-04).

FEM: **nominal, uncalibrated, reference-only, not used for damage diagnosis.**

---

# PHẦN A — BƯỚC 1: DỮ LIỆU DAO ĐỘNG VÀ BẰNG CHỨNG TRẠNG THÁI

## A.1. Bản đồ file kết quả (đường dẫn chính xác + ngày cập nhật)

Gốc: `H:\My Drive\03_RESEARCH\01_PHD_DT_AI_AM\00_PHD_DT_STEEL_INSPECTION_2026_2029_LIMITED_FEM\`

| # | File | Đường dẫn tương đối | Cập nhật | Vai trò |
|---|---|---|---|---|
| A1 | `00_README.md` | `05_DATA_CODE_AND_EXPERIMENTS\CANONICAL_THREE_CAMPAIGN_DATASET\` | **2026-07-29 21:35** | **BẢN MỚI NHẤT** — bộ dữ liệu chuẩn tắc, đã sửa định danh sensor |
| A2 | `09_DATASET_VALIDATION_REPORT.md` | nt | **2026-07-29 21:36** | Kết luận `READY_FOR_IT_TRAINING`, 12/12 PASS |
| A3 | `08_AUTOMATED_VALIDATION_RESULTS.csv` | nt | 2026-07-29 21:36 | Bảng 12 test T01–T12, toàn bộ PASS |
| A4 | `03_CHANNEL_QUALITY_RULES.md` | nt | 2026-07-29 21:35 | Quy tắc phân loại kênh chết / low-dynamic |
| A5 | `07_DATA_DICTIONARY.md`, `08_DATASET_VARIANTS.md`, `10_REPRODUCIBILITY_MANIFEST.md`, `11_DATASET_HANDOFF_FOR_IT.md` | nt | 2026-07-29 21:35–21:36 | Từ điển trường, biến thể Set A/B/C, manifest tái lập, handoff IT |
| A6 | `00_EXECUTIVE_REPORT.md` | `05_DATA_CODE_AND_EXPERIMENTS\THREE_CAMPAIGN_REANALYSIS\` | **2026-07-29 17:50** | Báo cáo mô hình hóa gần nhất (**trước** A1 khoảng 4 giờ) |
| A7 | `05_WITHIN_CAMPAIGN_LORO_RESULTS.csv` (238 dòng) | nt | 2026-07-29 18:00 | LORO trong từng campaign |
| A8 | `06_CROSS_CAMPAIGN_RESULTS.csv` (36 dòng) | nt | 2026-07-29 17:56 | LOCO chéo campaign |
| A9 | `07_BASELINE_MODEL_COMPARISON.csv` | nt | 2026-07-29 17:56 | So sánh LogReg/SVM/RF/CNN |
| A10 | `08_PERMUTATION_RESULTS.csv` (300 dòng) | nt | 2026-07-29 18:02 | Negative control hoán vị nhãn |
| A11 | `09_SENSOR_CONFIGURATION_RESULTS.csv` | nt | 2026-07-29 17:56 | Tổng hợp theo cấu hình sensor |
| A12 | `11_SENSITIVITY_RESULTS.csv` | nt | 2026-07-29 17:56 | 4 phân tích độ nhạy A–D |
| A13 | `12_CONFUSION_MATRICES\` (3 file) | nt | 2026-07-29 18:02 | 3 fold đại diện |
| A14 | `03_DATA_QUALITY_AND_PROVENANCE_LOG.csv` (66 dòng) | nt | 2026-07-29 17:55 | Nhật ký chất lượng/xuất xứ |
| A15 | `15_NEXT_ANALYSIS_RECOMMENDATION.md` | nt | 2026-07-29 17:55 | 8 việc tồn đọng ưu tiên |
| A16 | `01_ENVIRONMENT_PROVENANCE.md` | nt | 2026-07-29 17:54 | TensorFlow/Keras 2.21.0, CPU |
| A17 | `Checklist_Campaign_3_Gate1.docx` | `05_DATA_CODE_AND_EXPERIMENTS\CAMPAIGN_DOCUMENTATION\` | 2026-07-27 17:53 | Checklist Campaign 3 |
| A18 | `PAPER1_GATE1_READINESS_REPORT_v2.md` | `03_PAPERS\PAPER_1\GATE1_EVIDENCE\` | file 2026-08-03 11:36 / **nội dung ghi ngày 2026-07-18** | **Đã lạc hậu một phần** — nêu "chưa có run registry/LORO"; A6/A1 (29/07) đã làm. Kết luận `NOT READY` vẫn đúng |

> **Cảnh báo ưu tiên bản mới:** A1 (21:35) **mới hơn** A6 (17:50) trong cùng ngày và **đã sửa lỗi định danh sensor mà A6 phát hiện**. Vì vậy **mọi con số macro-F1 trong A6 là kết quả trên định danh sensor cũ (theo vị trí cột CSV)**, chưa chạy lại trên bộ dữ liệu A1. Không trích A6 như kết quả cuối cùng.

## A.2. Dữ liệu / campaign đã dùng

**Claim.** Ba campaign PASCO, 216 bản ghi CSV thô, đầy đủ 100%.

**Evidence.**
- `Campaign1_25.04.2026/`, `Campaign2_22.07.2026/`, `Campaign3_29.07.2026/` — mỗi campaign 72 CSV = **216 file**.
- Thiết kế: 4 trạng thái (`Healthy`, `B1`, `B2`, `B3`) × 3 kích thích (`Beat L1`, `Beat L2`, `White_Noise`) × 6 run × 3 campaign.
- Tần số lấy mẫu 100.000 Hz, không jitter; thời lượng hữu hiệu 41,55–122,30 s → mọi file phủ đủ cửa sổ chung 40 s.
- Kiểm tra: 216/216 file có mặt, **0 trùng SHA-256**, 0 NaN giữa file, 0 spike, 0 clipping thật (nguồn A1/A2/A3, A6 §1).

**Limitation.** 1 file `BS1B1L1R12.csv` (Campaign 2) thiếu tiền tố ngày `20260721__/20260722__` → gắn cờ `PROVENANCE_WARNING`, **không tự loại**.

**Next action.** Giữ nguyên; đã có test độ nhạy có/không file này (§A.6).

## A.3. Run registry

**Claim.** Registry 216 dòng đã được dựng lại từ dữ liệu thô, có hash — nhưng **file registry gốc không nằm trong workspace này**.

**Evidence.**
- A6 §1 khai báo `02_MASTER_RUN_REGISTRY.csv` (216 dòng); A2 khai báo `06_MASTER_RUN_REGISTRY.csv` mang SHA-256 + thời lượng thô/hữu hiệu cho toàn bộ 216 bản ghi.
- Mọi ô hoàn chỉnh (Campaign × Run × State × Excitation) khớp đúng 1 file; 0 thiếu, 0 trùng hash.

**Limitation — quan trọng.** A6 §11 và A1 nêu rõ: các file lớn (`02_MASTER_RUN_REGISTRY.csv`, `04_ANALYSIS_SET_MANIFEST.csv`, `10_PER_CLASS_RESULTS.csv`, `14_PREDICTIONS_WITH_PROVENANCE.csv`, `sensor_fingerprint_check.csv`, toàn bộ NPZ, fold manifest, mã pipeline) **được giao qua file card của phiên chat, không copy vào Drive**. Tôi đã quét toàn bộ `05_DATA_CODE_AND_EXPERIMENTS\` — **các file này không tồn tại trên Drive**. `G1_TO_G2_CONDITION_EVIDENCE_INTERFACE_v1.0.md` §3.4 xác nhận: thư mục `G1_EXECUTION_PACK/` và `RUN_REGISTRY_LOCKED.csv` **không tồn tại**.

**Next action.** Yêu cầu copy `CANONICAL_THREE_CAMPAIGN_DATASET.zip` + các CSV registry gốc vào `05_DATA_CODE_AND_EXPERIMENTS\G1_EXECUTION_PACK\` trước khi bất kỳ số liệu nào được dùng cho Paper 1. Đây là **nút chặn số 1** của G1.

## A.4. Cách chia dữ liệu theo run / LORO

**Claim.** Hai sơ đồ chia, tách hoàn toàn theo nhóm run/campaign.

**Evidence.**
- **Within-campaign LORO** (Leave-One-Run-Out): 6 fold/campaign, giữ 1 run làm test.
- **Cross-campaign LOCO** (Leave-One-Campaign-Out): 3 fold, giữ 1 campaign làm test.
- Hai tập phân tích **không trộn nhau**:
  - `CORE_THREE_CAMPAIGN_SET` — Campaign 1+2+3, kênh `S1_Ax/S2_Ax`, **18 run độc lập**, shape `[4000, 2]`;
  - `SUPPORTING_THREE_SENSOR_SET` — Campaign 2+3, `S1/S2/S3 × Ax/Ay/Az`, **12 run độc lập**, shape `[4000, 9]`.
- Fold manifest (bản A1): `06_WITHIN_CAMPAIGN_LORO_MANIFEST.csv` (**42 dòng**) và `07_CROSS_CAMPAIGN_LOCO_MANIFEST.csv` (**3 dòng**).

**Limitation.** `D003`/`D004` trong decision register vẫn để mở: **đơn vị độc lập chính thức (run / recording / replicate group) chưa khóa**.

**Next action.** Chốt D003–D004 trước khi hình thành Condition_Evidence chính thức.

## A.5. Kiểm soát data leakage

**Claim.** Ba lớp kiểm soát; cả ba đều báo đạt.

**Evidence.**

| Lớp | Cơ chế | Kết quả |
|---|---|---|
| Thiết kế | Chia nhóm (run) **trước khi cắt cửa sổ**; cửa sổ 2 s / 200 mẫu, **không chồng lấn**; scaler chỉ fit trên fold train | `pipeline_lib.py::build_dataset` (A6 §2) |
| Tự động | Test **T10** (không run nào vừa ở train vừa ở test) + **T11** (smoke test sinh cửa sổ, overlap = 0) | **PASS** (A3) |
| Thực nghiệm | Hoán vị nhãn ở mức bản ghi, 100 lần/cấu hình, chỉ xáo phía train, giữ nguyên cấu trúc nhóm | **300 dòng** trong A10 |

Kết quả negative control (A6 §7, RF):

| Cấu hình | macro-F1 thật | Trung vị null | Dải null | p(null ≥ real) |
|---|---|---|---|---|
| Within-C2, S1+S2+S3_xyz, held-out R7 | 0,962 | 0,222 | 0,000–0,489 | **0,000** |
| Within-C1, S1+S2_Ax, held-out R1 | 0,647 | 0,229 | 0,077–0,399 | **0,000** |
| Cross-campaign LOCO, S1+S2_Ax, held-out C1 | 0,129 | 0,224 | 0,134–0,324 | **1,000** |

Null tập trung quanh mức ngẫu nhiên (~0,22–0,23) ở cả ba → **pipeline không rò rỉ**.

**Limitation.** Chỉ 3 cấu hình đại diện được hoán vị, không phải toàn ma trận. Toàn bộ 12 test T01–T12 là **proxy output**: không có source rows, timestamp thực thi, hay hash đầu ra (theo `G1_TO_G2...INTERFACE_v1.0.md` §3.3).

**Next action.** Lưu log thực thi + hash đầu ra cho bộ test; mở rộng hoán vị nếu Paper 1 cần.

## A.6. Mô hình đã kiểm tra

| Họ mô hình | Cấu hình | Độ phủ |
|---|---|---|
| Logistic Regression | Đặc trưng cố định, seed 42, **không tuning** | LORO **đầy đủ** + LOCO **đầy đủ** |
| SVM | nt | nt |
| Random Forest | nt | nt |
| 1D-CNN nhỏ gọn | Adam 1e-3, batch 32, dropout 0,3, ≤100 epoch, patience 10, seed 42 | LOCO **9/9 đầy đủ**; LORO **chỉ 4/6 fold của Campaign 1 / S1_Ax** |
| ResNet1D | — | **Không chạy** (chưa quyết định include/exclude) |

Bộ đặc trưng cố định/kênh: RMS, std, peak-to-peak, tần số trội, spectral centroid, 3 band-energy, PSD-peak.

Khối lượng: **234 fit** feature-baseline LORO (13 cấu hình × 6 fold × 3 mô hình) + **27 fit** LOCO + CNN.

## A.7. Kết quả sơ bộ gần nhất

> Toàn bộ số dưới đây là **candidate claim pending Gate 1 closure** (Charter v2.1 §10) và dựa trên **định danh sensor theo vị trí cột** (chưa phải bản A1 đã sửa).

**Within-campaign LORO — Random Forest (mạnh nhất), trung vị macro-F1:**

| Campaign | Trung vị | Dải | Cấu hình tốt nhất |
|---|---|---|---|
| Campaign 1 (Ax) | **0,683** | 0,573–0,788 | S1+S2_Ax: 0,760 |
| Campaign 2 (xyz) | **0,878** | 0,630–0,975 | S3_xyz: 0,911 |
| Campaign 3 (xyz) | **0,609** | 0,218–0,954 | S1+S2+S3_xyz: 0,678 |

**Cross-campaign LOCO — trung vị trên 9 fold-config (mức ngẫu nhiên = 0,25):**

| Mô hình | Trung vị | TB | Std | Min | Max |
|---|---|---|---|---|---|
| LogReg | 0,186 | 0,189 | 0,032 | 0,153 | 0,259 |
| SVM | 0,195 | 0,193 | 0,039 | 0,120 | 0,230 |
| RF | 0,166 | 0,160 | 0,024 | 0,129 | 0,202 |
| CNN (seed 42) | 0,152 | 0,157 | 0,050 | 0,100 | 0,250 |

**Phát hiện quan trọng nhất (chịu tải nặng nhất cho luận án):**

1. **Trong cùng campaign, 4 trạng thái phân biệt được rõ ràng** (0,61–0,88 so với 0,25), đã loại trừ artefact bằng hoán vị (p = 0,000).
2. **Chéo campaign thì sụp đổ hoàn toàn**: mọi cấu hình × mọi họ mô hình đều **ở hoặc dưới mức ngẫu nhiên**; hơn nữa cấu hình LOCO được kiểm chứng có `p(null ≥ real) = 1,000` — mô hình huấn luyện trên **nhãn thật** của 2 campaign lại **tệ hơn** khi huấn luyện trên nhãn bị xáo. Đây là bằng chứng trực tiếp mô hình đang học **nhiễu đặc thù campaign**, không phải trạng thái kết cấu.

**Độ nhạy (một fold đại diện — Campaign 2, held-out R7, RF), nguồn A12:**

| Phân tích | Biến thể | macro-F1 |
|---|---|---|
| A — file `BS1B1L1R12` | có / không | 0,9708 / 0,9750 |
| B — độ dài cửa sổ | giữa 40 s / toàn thời lượng | 0,9708 / 0,8589 |
| C — chuẩn hóa | giữ biên độ / RMS-normalised | 0,9708 / 0,8412 |
| D — chọn trục | C2 Ax-only 0,7698 · C2 xyz 0,9192 · C3 Ax-only 0,6599 · C3 xyz 0,6903 | |

Đọc: giữ biên độ tốt hơn chuẩn hóa RMS (−0,13); cửa sổ 40 s tốt hơn toàn thời lượng (−0,11); ép về Ax-only (cần cho tập CORE chéo campaign) làm mất 0,149 macro-F1 trong Campaign 2 — **mà vẫn không mua được khả năng tổng quát chéo campaign**.

## A.8. Các nội dung CHƯA KHÓA (Bước 1)

| # | Nội dung | Trạng thái | Nguồn |
|---|---|---|---|
| 1 | **Định danh vật lý sensor Campaign 1 & 2** | A6 §1 phát hiện vị trí cột CSV **không ổn định** (C1 lưỡng mode ~−2,08 / +1,50 m/s²; C2 tam mode ~−1,97 / −0,3 / +1,71). A1 tuyên bố đã sửa bằng fingerprint trọng trường + gán Hungarian (576/576 block `RESOLVED_HIGH_CONFIDENCE`) — **nhưng chưa chạy lại mô hình trên bản sửa** | A6 §1, A2 điều 2–3, D005 `BLOCKING_OPEN` |
| 2 | Seed sweep CNN | Chỉ seed 42; thiếu 123 và 2026 (tối thiểu 3 seed) | A15 mục 2 |
| 3 | Ma trận LORO cho CNN | Chỉ 4/6 fold của 1 cấu hình / 1 campaign | A15 mục 3 |
| 4 | Early-stopping epoch ~11 | Vài fold sụp về gần đơn lớp (macro-F1 ≈ 0,10); cần ablation patience=20 | A15 mục 4 |
| 5 | Confusion matrix & prediction theo cửa sổ | Chỉ 3/≈70 fold | A15 mục 5 |
| 6 | Training curves | **Không lưu** per-epoch history | A15 mục 6 |
| 7 | Biến động Campaign 3 | Std 0,184 (so với 0,091 của C2), min 0,218 | A15 mục 7 |
| 8 | ResNet1D | Chưa xác minh provenance → chưa quyết định | Stream A mục 4 |
| 9 | Hyperparameter tuning | **Ngoài phạm vi pass này**; chỉ mở sau khi G1 sanity + permutation + reproducibility được chấp nhận | A15 mục 8 |
| 10 | Ma trận chấp nhận & ký duyệt G1 | **Chưa tồn tại** | `01_MASTER_G1_G2_G3_EVIDENCE_SYNTHESIS` §D |
| 11 | 6 quyết định `BLOCKING_OPEN` | D004 đơn vị độc lập, D005 định danh sensor, D007 quy tắc tổng hợp, D013 Inspection_Record, D014 Action_Record, D016 competency questions | `G1_G2_INTERFACE_DECISION_REGISTER.csv` |

---

# PHẦN B — BƯỚC 2: TRUY VẾT BIM/IFC VÀ KIỂM TRA ĐỊNH DANH

## B.1. Bản đồ file kết quả

| # | File | Đường dẫn | Cập nhật | Vai trò |
|---|---|---|---|---|
| B1 | `G2_G3_REVIT_IFC_AIM_EXECUTION_ROADMAP.md` | `...LIMITED_FEM\02_EVIDENCE_BASE\RQ2_GATES2_3\` | **2026-08-03 18:00** | **BẢN MỚI NHẤT** — chứa toàn bộ số liệu kiểm tra Revit–IFC (§4.1–4.6) và roadmap R0–R20 |
| B2 | `G2_G3_PAPER2_CURRENT_ROADMAP_v2.1_20260804.md` (nội dung v2.2) | nt | **2026-08-04 14:57** | Roadmap G2→G3 hiện hành, thay thế B4 |
| B3 | `G1_TO_G2_CONDITION_EVIDENCE_INTERFACE_v1.0.md` (74 KB) | nt | 2026-08-04 14:57 | **Hợp đồng G1→G2**; định nghĩa Condition_Evidence, 37 negative test |
| B4 | `G2_G3_PAPER2_REVISED_ROADMAP_v1.1.03.08.2026.md` | nt | 2026-08-03 18:44 | **Đã bị B2 thay thế** — không dùng |
| B5 | `PHD_BIM_AIM_IMPLEMENTATION_ROADMAP.md` | nt | 2026-08-03 17:43 | Bản sớm hơn B1 — không dùng |
| B6 | `G1_G2_INTERFACE_DECISION_REGISTER.csv` (26 quyết định) | `...LIMITED_FEM\01_CURRENT_CONTROL\` | 2026-08-04 15:00 | Sổ quyết định mở, có owner/reviewer |
| B7 | `01_MASTER_G1_G2_G3_EVIDENCE_SYNTHESIS_20260804.md` | `...LIMITED_FEM\02_EVIDENCE_BASE\CURRENT\` | 2026-08-04 14:55 | Tổng hợp chính thức + G2 Final Decision Register |
| B8 | `PAPER2_CURRENT_DIRECTION_v2.1_20260804.md` | `...LIMITED_FEM\03_PAPERS\PAPER_2\` | 2026-08-04 14:59 | Ranh giới claim Paper 2 |
| B9 | `DT10_MODEL 13.03.26.ifc` (95,8 MB) | `01_PHD_DT_AI_AM\03_RESEARCH_ASSETS\BIM_MODELS\` | **2026-03-13 21:22** | **Mô hình IFC baseline duy nhất có mặt trên Drive** |
| B10 | `IFC_mapping.txt` | nt | 2026-03-13 21:21 | Mapping `Asset_ID → IfcColumn/IfcBeam/IfcMember`, Pset `Identity Data`, property `Tag` |
| B11 | `KET CAU NHA XUONG.rvt` (26,5 MB), `KHUNG THEP.rvt` (8,4 MB) | nt | 2025-11-17 / 2025-11-05 | Mô hình Revit nguồn |
| B12 | `26.02.09_DT10_K25L80 Asset Register.xlsx` | nt | 2026-02-09 | Asset register |

## B.2. Mô hình / file IFC–Revit đã dùng

**Claim.** Có hai phiên bản mô hình được khai báo; chỉ **một** hiện diện trên Drive.

**Evidence — baseline (đã kiểm chứng độc lập trong phiên này):**

| Trường | Giá trị khai báo (B1 §4.1) | Kiểm chứng của tôi trên `DT10_MODEL 13.03.26.ifc` |
|---|---|---|
| Schema | `IFC4X3_ADD2` | ✅ `FILE_SCHEMA(('IFC4X3_ADD2'))` |
| SHA-256 | `814baf3ac26432d2b689c1013406cbea57678e9cb602290f40cf239b302bb7f7` | ✅ **khớp tuyệt đối** |
| `Model_Version_ID` | `MV-20260313-814baf3a` | ✅ nhất quán (ngày file 2026-03-13, 8 ký tự đầu hash) |
| Revit nguồn | 25.4.0.32 | ✅ `Autodesk Revit 25.4.0.32 (ENU) - IFC 25.4.0.32` |
| ODA SDAI | 24.12 | ✅ `ODA SDAI 24.12` |
| Tổng `IfcElement` | 4.013 | (khai báo — chưa parse lại) |
| Cấu kiện kết cấu | 1.813 | (khai báo — chưa parse lại) |

**Evidence — bản đồng bộ Revit 2027 (B1 §4.4):** `model_revit2027_sync_v1.ifc`, `Model_Version_ID` = `MV-20260803-fc94ef3c`, parent = `MV-20260313-814baf3a`. Môi trường: Revit 2027.1 + Dynamo 4.0.2.3852 + PythonNet3, graph `01_export_revit_crosswalk_structural_Dynamo4.dyn`, `INCLUDE_STEEL_CONNECTIONS = False`.

**Limitation — quan trọng.** Tôi đã quét toàn bộ workspace: **`model_revit2027_sync_v1.ifc`, các file `.dyn`, mapping `DT_UserDefinedPropertySets_ACCEPTED_V1.txt`, và mọi CSV crosswalk/binding/Pset audit KHÔNG có mặt trên Drive.** Thư mục `05_GATE2/` và `revit_integration/ifc_export/accepted/` (theo R0/R1 của B1) **chưa được tạo**. Toàn bộ số liệu §B.3–B.4 dưới đây hiện chỉ tồn tại dưới dạng **trần thuật trong B1**, chưa có artefact tái lập kèm hash.

**Next action.** Thực thi **R0** (tạo `05_GATE2/`, copy artefact, tính SHA-256, lập `G2_CURRENT_INPUT_MANIFEST.csv`) trước mọi bước tiếp theo. Stop condition của R0: dừng nếu không xác định được file Revit nào tạo ra file IFC nào.

## B.3. Chuỗi định danh đã kiểm tra

**Chuỗi khóa hiện hành** (`CURRENT_STATUS_AND_NEXT_DIRECTION.md` §2, `G1_G2_INTERFACE_DECISION_REGISTER.csv` D002 — `LOCKED`):

```
Sensor_ID
→ BIM_GUID / Asset_ID @ Model_Version_ID
→ Condition_Evidence_ID
→ Inspection_Record_ID
→ Action_Record_ID
```

- `Action_Status` / `Workflow_Status` = **hình chiếu trạng thái hiện tại**, KHÔNG phải định danh.
- `Status_Event_ID` = **PROPOSED — NOT ACCEPTED** (`ADR_ACTION_STATUS_EVENT_20260804_DRAFT.md`).
- `FEM_Node_ID` = metadata tùy chọn, không bao giờ là mắt xích bắt buộc.
- Định danh hỗ trợ: `Asset_ID`, `Model_Version_ID`, `Revit_UniqueId`, `Revit_ElementId`, `Run_ID`.

**Lưu ý phiên bản:** B1 (03/08) vẫn ghi chuỗi kết thúc ở `Action_Status`; **B7 và decision register (04/08) đã sửa** kết thúc ở `Action_Record_ID`. Dùng bản 04/08.

Property set đã kiểm tra: **`Pset_DT_AssetIdentity`** với **7 property** — `Asset_ID`, `Asset_Name`, `Asset_Type`, `Location_Mark`, `Asset_ID_Source`, `Verification_Status`, `Traceability_Scope`.

## B.4. Kết quả đối chiếu Revit–IFC (số phép kiểm tra đạt / chưa đạt)

### (a) Phase 1 — BIM Information Readiness (trên baseline `MV-20260313-814baf3a`)

| Chỉ số | Giá trị | Đọc |
|---|---:|---|
| Asset_ID duy nhất dùng được | **24** | Chỉ 24 cấu kiện hiện có định danh dùng được |
| Asset_ID bị chặn do trùng | **2** | Xung đột trùng lặp |
| Không có nguồn Asset_ID | **1.787** | **98,6 % cấu kiện kết cấu chưa có Asset_ID** |
| Geometry usable | **1.812 / 1.813** | 99,94 % |
| Placement suy biến được geometry khôi phục | **607 / 607** | 100 % |
| Link audit | **8 / 8 PASS** | 100 % |

### (b) Crosswalk Revit 2027 (cấu kiện kết cấu, loại trừ steel connections)

| Category | Số lượng |
|---|---:|
| Structural Framing | 596 |
| Structural Columns | 56 |
| Generic Models | 41 |
| Structural Foundations | 24 |
| Floors | 1 |
| **Tổng** | **718** |

### (c) IFC sync `MV-20260803-fc94ef3c` và round-trip Revit ↔ IFC

| Chỉ số | Giá trị | Tỷ lệ |
|---|---:|---|
| `IfcElement` | 3.468 | — |
| Structural | 1.703 | — |
| **GUID unique** | **3.468 / 3.468** | **100 %** |
| Geometry usable | 1.703 / 1.703 | 100 % |
| IFC Tag | 714 | — |
| **`MATCH_TAG_AND_GUID`** | **685 / 718** | **95,4 %** |
| Có IFC counterpart duy nhất | 701 / 718 | 97,6 % |
| Conflict | **0** | — |
| Duplicate Tag | **0** | — |
| `REVIT_ONLY` (không sang IFC) | **17** | 2,4 % **CHƯA ĐẠT** |
| **GUID persistence trên tập chung** | **90 / 90** | **100 %** |

### (d) Pset export validation v2 — phép kiểm tra chính

```
41 / 41 PASS
 0   PASS_WITH_LIMITATION
 0   FAIL
```

Đã chứng minh: 14/14 giá trị đúng · đúng một `IfcColumn` và một `IfcBeam` · toàn bộ kiểu `IfcText` · tiếng Việt không lỗi font · **không lan sang phần tử thứ ba** · `Tag`, `GlobalId`, class và geometry **không đổi** · không tồn tại giá trị `verified` · input khóa bằng SHA-256.

### (e) Tổng hợp đạt / chưa đạt

| Nhóm phép kiểm tra | Đạt | Chưa đạt | Ghi chú |
|---|---:|---:|---|
| Pset export v2 | **41** | 0 | Điều kiện để freeze setup xuất |
| Link audit | **8** | 0 | |
| GUID uniqueness | 3.468 | 0 | |
| GUID persistence | 90 | 0 | |
| Round-trip Tag+GUID | 685 | **33** | 17 `REVIT_ONLY` + 16 khác |
| Geometry usable (baseline) | 1.812 | **1** | |
| Asset_ID có nguồn | 24 | **1.789** | 1.787 thiếu + 2 trùng |
| Negative test `CE-NEG-001…037` | **0** | — | **37 test mới chỉ ĐỊNH NGHĨA, chưa chạy** (B3 §14) |

## B.5. Cấu kiện / trường thông tin đã thử nghiệm

- **Cấu kiện thử nghiệm:** đúng **1 `IfcColumn` + 1 `IfcBeam`** (2 cấu kiện) trong test model tách riêng khỏi working model.
- **Trường thử nghiệm:** 7 property của `Pset_DT_AssetIdentity` × 2 cấu kiện = 14 giá trị → 14/14 đúng.
- **Mapping cơ sở** (`IFC_mapping.txt`, đã đọc trực tiếp): `Asset_ID` → `IfcColumn` / `IfcBeam` / `IfcMember`, Pset `Identity Data`, property `Tag`.
- **Trạng thái hiện tại của B1:** `READY TO FREEZE PSET EXPORT SETUP` — nhưng **Gate 2 chưa đóng, Gate 3 chưa bắt đầu**.
- **Lệnh cấm còn hiệu lực:** `Do not run Graph 02` (D019 `LOCKED`).

## B.6. Nội dung tiếp theo cần tích hợp với `Condition_Evidence_ID`

Nguồn: `G1_TO_G2_CONDITION_EVIDENCE_INTERFACE_v1.0.md` §7–§8, §17, §20.

**Cấu trúc bản ghi Condition_Evidence chuẩn tắc (8 khối):** Identity · Source provenance · Sensor provenance · Processing provenance · Evidence content · **BIM/component context** · Accountability · Downstream governance.

**Thực thể liên kết cần dựng:** `Condition_Evidence_Sensor_Link` · `Condition_Evidence_Window_Link` · **`BIM_Binding`** · `Condition_Evidence_Fold_Link` · các liên kết provenance chuẩn hóa.

**Việc phải làm để nối Bước 1 ↔ Bước 2:**

| # | Việc | Chặn bởi |
|---|---|---|
| 1 | Chuẩn hóa & khóa registry G1 (Dataset, Run, Recording, Source Hash, Sensor/Channel, Fold, Model Config, Environment, Exclusion) dưới một quy ước đặt tên duy nhất | Registry gốc chưa có trên Drive (§A.3) |
| 2 | Tạo **schema Condition Evidence Register** + template rỗng theo §7–§8; **không** nạp evidence thật trước khi G1 cho phép | D003, D007 |
| 3 | Khóa đơn vị bằng chứng chính thức + `Aggregation_Rule_ID` + tiêu chí valid-window/sensor-completeness + chính sách abstention | D004, D007, D008, D009 `OPEN` |
| 4 | **Đối chiếu `Physical Sensor_ID` với kết quả legacy S1/S2/S3** và định nghĩa governance liên kết Sensor → Asset/BIM (model version, ambiguity, thẩm quyền reviewer) | D005 `BLOCKING_OPEN` — `CE-NEG-025` cấm gán vị trí cột thành sensor vật lý |
| 5 | Tạo positive fixtures: single-sensor, multi-sensor, multi-recording, **candidate BIM**, **verified BIM**, superseded evidence, reproducibility-pass | §20 mục 5 |
| 6 | Tạo 37 negative fixtures §14 + manifest kỳ vọng thất bại — **không** chạy, **không** claim thành công | §20 mục 6 |
| 7 | Pre-register SCQ/VCQ/RCQ + acceptance criteria, rồi họp duyệt schema chung G1–G2 | D016 `BLOCKING_OPEN`; `CE-GOV-012` chặn mọi phê duyệt G2 khi thiếu |

**Ràng buộc BIM binding cốt lõi:** phân biệt tuyệt đối `UNBOUND` / **`CANDIDATE`** / **`VERIFIED`**. `CE-NEG-010` (coi candidate là verified), `CE-NEG-011` (verified thiếu reviewer/thời gian/bằng chứng), `CE-NEG-012` (trùng binding đang hoạt động), `CE-NEG-028` (GUID không tồn tại trong model version), `CE-NEG-034` (binding trỏ model đã bị thay thế) đều là **BLOCKER**.

**Cấm diễn giải xuôi dòng:** Condition_Evidence **không phải** hư hỏng đã xác nhận, chẩn đoán khuyết tật, suy giảm độ cứng, mức ưu tiên bảo trì, Health Index, RUL, khuyến nghị sửa chữa, lệnh kiểm tra hay lệnh bảo trì. Softmax **không phải** xác suất hư hỏng vật lý. CEI **phải** là cấu trúc metadata đa chiều, **không được** rút về scalar (`CE-NEG-027`, BLOCKER).

---

# PHẦN C — GIỚI HẠN HIỆN TẠI (TỔNG HỢP)

| # | Giới hạn | Mức độ | Ảnh hưởng |
|---|---|---|---|
| L1 | **Registry & dataset gốc của Bước 1 không có trên Drive** (chỉ có tài liệu + CSV tổng hợp) | 🔴 Chặn | Không thể tái lập, không thể ký duyệt G1 |
| L2 | **Kết quả mô hình (A6) chạy trên định danh sensor cũ**; bản sửa (A1) chưa được mô hình hóa lại | 🔴 Chặn | Mọi số single/paired-sensor của C1, C2 phải đọc là "vị trí cột 1/2", không phải Apex/BeamColumn |
| L3 | **Artefact Revit 2027 / Pset không có trên Drive**; số 41/41, 685/718 chỉ là trần thuật trong B1 | 🔴 Chặn | Chưa có bằng chứng tái lập cho G2 |
| L4 | CNN chỉ 1 seed, LORO chỉ 4/6 fold của 1 cấu hình | 🟠 Cao | Không đủ để so sánh họ mô hình trong campaign |
| L5 | **1.787/1.813 cấu kiện không có nguồn Asset_ID** | 🟠 Cao | Phạm vi truy vết thực tế rất hẹp |
| L6 | 37 negative test mới chỉ định nghĩa; 0 test đã chạy | 🟠 Cao | G3 chưa có bằng chứng nào |
| L7 | 6 quyết định `BLOCKING_OPEN` (D004, D005, D007, D013, D014, D016) | 🟠 Cao | Chặn cả G1 payload lẫn G2 freeze |
| L8 | 17 phần tử `REVIT_ONLY` chưa sang IFC | 🟡 Trung bình | Cần giải trình trước khi freeze scope |
| L9 | Training curves không lưu; confusion matrix chỉ 3/≈70 fold | 🟡 Trung bình | Thiếu hình cho Paper 1 |
| L10 | `ADR_ACTION_STATUS_EVENT_20260804_DRAFT.md` là **PROPOSED**, chưa chấp nhận | 🟡 Trung bình | `Status_Event_ID` chưa được dùng như định danh |
| L11 | `Checklist_Campaign_3_Gate1.docx` chưa được đọc/ trích xuất vào evidence | 🟡 Trung bình | Bằng chứng hiện chưa đủ |

**Không gate nào được đóng.** G1 `OPEN — PARTIAL EVIDENCE`; G2 `OPEN — SPECIFICATION NOT YET FROZEN`; G3 `NOT OPEN`.

---

# PHẦN D — HÌNH / BẢNG DÙNG ĐƯỢC NGAY CHO SLIDE

## D.1. Dùng ngay, không cần chỉnh (đã có số, đã có kiểm chứng phản chứng)

| Slide | Nội dung | Nguồn | Ghi chú bắt buộc trên slide |
|---|---|---|---|
| **S1** | Bảng **within-campaign LORO — RF trung vị 3 campaign** (0,683 / 0,878 / 0,609 vs chance 0,25) | A6 §5 bảng 1 | "Candidate claim pending Gate 1 closure" |
| **S2** | Bảng **cross-campaign LOCO 4 họ mô hình** (0,152–0,195 vs chance 0,25) | A6 §5 bảng 2 | nt |
| **S3** | **Bảng negative control 3 dòng** (real vs null median vs p) — **slide mạnh nhất**: chứng minh không rò rỉ + chứng minh sụp đổ chéo campaign là thật | A6 §7 / A10 | nt |
| **S4** | **Bảng độ nhạy A–D** (4 dòng) | A12 (10 dòng, đã đọc trực tiếp) | Ghi rõ "một fold đại diện" |
| **S5** | **Bảng 12 test tự động T01–T12, 12/12 PASS** | A3 | Ghi "kiểm soát rò rỉ dữ liệu" |
| **S6** | **Bảng Pset export validation: 41/41 PASS / 0 / 0** | B1 §4.5 | Ghi "test model, 1 IfcColumn + 1 IfcBeam" |
| **S7** | **Bảng round-trip Revit↔IFC** (685/718, GUID 3468/3468, conflict 0, duplicate 0, REVIT_ONLY 17) | B1 §4.4 | Ghi rõ 17 REVIT_ONLY |
| **S8** | **Sơ đồ chuỗi định danh** `Sensor_ID → BIM_GUID/Asset_ID @ Model_Version_ID → Condition_Evidence_ID → Inspection_Record_ID → Action_Record_ID` | B7 §C | Kèm chú thích `Status_Event_ID = PROPOSED` |
| **S9** | **Bảng trạng thái Gate** G1/G2/G3/Paper 2 | `CURRENT_STATUS_AND_NEXT_DIRECTION.md` §1 | Dùng nguyên văn |
| **S10** | **Bảng Phase 1 readiness** (Asset_ID 24 / 2 / 1.787; geometry 1.812/1.813; link audit 8/8) | B1 §4.2 | Nêu 1.787 là khoảng trống chính |

## D.2. Cần dựng thêm (chưa có sẵn hình)

| Hình | Cần gì | Dữ liệu đã có? |
|---|---|---|
| Boxplot macro-F1 theo cấu hình sensor (11 cấu hình) | Vẽ từ A11 (`09_SENSOR_CONFIGURATION_RESULTS.csv`) | ✅ Có đủ median/mean/std/worst |
| Biểu đồ within vs cross campaign (2 nhóm cột + đường chance 0,25) | Vẽ từ A7 + A8 | ✅ |
| Histogram phân phối null vs vạch real (3 panel) | Vẽ từ A10 (300 dòng) | ✅ |
| Confusion matrix heatmap 3 fold | A13 | ✅ (chỉ 3 fold) |
| Training curve | — | ❌ **Không lưu** — phải chạy lại fold |
| Sơ đồ kiến trúc Revit→IFC→Pset→DB | — | ❌ Chưa có; dựng từ B1 §4 + roadmap R0–R20 |

## D.3. KHÔNG được đưa lên slide

- Bất kỳ con số nào gán nhãn "Apex / BeamColumn / BraceColumn" cho Campaign 1 hoặc Campaign 2 (chỉ được ghi "vị trí cột 1/2/3") — `CE-NEG-025`.
- Con số ~0,91 macro-F1 của pipeline `cc_*.py` cũ (đã bị loại khỏi mục tiêu).
- Bất kỳ phát biểu nào hàm ý G1/G2/G3 đã đóng, hoặc "first"/"no study worldwide" (`CLOSE_SEARCH` chỉ giới hạn trong corpus).
- Bất kỳ diễn giải nào biến Condition_Evidence thành mức độ hư hỏng, ưu tiên bảo trì hay Health Index.

---

# PHẦN E — HÀNH ĐỘNG KHUYẾN NGHỊ (THEO THỨ TỰ)

| Ưu tiên | Hành động | Kết quả mong đợi | Gate hưởng lợi |
|---|---|---|---|
| **1** | Copy `CANONICAL_THREE_CAMPAIGN_DATASET.zip` + toàn bộ registry gốc vào `05_DATA_CODE_AND_EXPERIMENTS\G1_EXECUTION_PACK\`, tính SHA-256 | Gỡ L1 | G1 |
| **2** | Chạy lại LORO/LOCO (baseline + 1D-CNN, ≥3 seed, permutation control) **trên bộ A1 đã sửa định danh sensor** | Gỡ L2, L4; trả lời được "sụp đổ chéo campaign có đổi không" | G1 |
| **3** | Thực thi **R0** của B1: tạo `05_GATE2/`, đóng băng artefact Revit/IFC + hash, lập `G2_CURRENT_INPUT_MANIFEST.csv` | Gỡ L3 | G2 |
| **4** | Chốt 6 quyết định `BLOCKING_OPEN` với người hướng dẫn (D004, D005, D007, D013, D014, D016) | Gỡ L7 | G1 + G2 |
| **5** | Dựng schema Condition Evidence Register (rỗng) + 37 negative fixtures (định nghĩa, không chạy) | Chuẩn bị G3 | G2 |
| **6** | Pre-register SCQ/VCQ/RCQ + acceptance criteria | Điều kiện `CE-GOV-012` | G2 |
| **7** | Lập ma trận chấp nhận G1 và trình ký | Đóng G1 | G1 |

---

# PHẦN F — HOÀN THÀNH NHIỆM VỤ

**Files đã đọc (chính):**
`00_GOVERNANCE\AGENT_RULES.md` · `01_CURRENT_CONTROL\MASTER_INDEX_CURRENT.md` · `01_CURRENT_CONTROL\CURRENT_STATUS_AND_NEXT_DIRECTION.md` · `01_CURRENT_CONTROL\G1_G2_INTERFACE_DECISION_REGISTER.csv` · `02_EVIDENCE_BASE\CURRENT\01_MASTER_G1_G2_G3_EVIDENCE_SYNTHESIS_20260804.md` · `02_EVIDENCE_BASE\RQ2_GATES2_3\G2_G3_REVIT_IFC_AIM_EXECUTION_ROADMAP.md` · `...\G2_G3_PAPER2_CURRENT_ROADMAP_v2.1_20260804.md` · `...\G1_TO_G2_CONDITION_EVIDENCE_INTERFACE_v1.0.md` · `03_PAPERS\PAPER_1\GATE1_EVIDENCE\PAPER1_GATE1_READINESS_REPORT_v2.md` · `05_DATA_CODE_AND_EXPERIMENTS\THREE_CAMPAIGN_REANALYSIS\{00,15}` + 5 CSV kết quả · `05_DATA_CODE_AND_EXPERIMENTS\CANONICAL_THREE_CAMPAIGN_DATASET\{00,09}` + `08_AUTOMATED_VALIDATION_RESULTS.csv` · `03_RESEARCH_ASSETS\BIM_MODELS\IFC_mapping.txt` · header + SHA-256 của `DT10_MODEL 13.03.26.ifc`.

**Files đã tạo:** file này (`11_Output\Cowork\RA_SOAT_KET_QUA_BUOC1_BUOC2_20260805.md`). Không sửa, xóa, đổi tên hay ghi đè bất kỳ file nào khác. Không chạm Zotero.

**Bằng chứng đã dùng:** chỉ file trong workspace + một kiểm chứng độc lập (SHA-256 của IFC baseline khớp giá trị khai báo trong B1 §4.1).

**Giới hạn chưa giải quyết:** L1–L11 ở Phần C.

**Evidence Gate kế tiếp có tiến gần hơn không:** **Chưa.** Rà soát này không sinh bằng chứng gate mới; nó xác định chính xác hai nút chặn vật lý (dataset gốc và artefact Revit/IFC đều không có trên Drive) và 6 quyết định `BLOCKING_OPEN`. Khoảng cách còn lại là **artefact + quyết định quản trị**, không phải văn liệu.
