# BÁO CÁO TỔNG HỢP BẰNG CHỨNG, KHOẢNG TRỐNG VÀ ĐỊNH HƯỚNG LUẬN ÁN G1–G2–G3

**Ngày rà soát:** 02/08/2026  
**Phạm vi:** toàn bộ repository cục bộ; không dùng web, Zotero MCP hoặc kiến thức ngoài repository làm bằng chứng.  
**Ngành:** Quản lý xây dựng / Quản lý tài sản công trình.  
**Kiểm soát chất lượng:** file quản trị, README, planning và demo chỉ được dùng làm bằng chứng dự án/governance; nhận định học thuật chỉ dựa trên văn liệu đã được repository ghi nhận và kiểm soát trạng thái đọc.

## Quy ước phân loại bằng chứng

| Nhãn | Ý nghĩa |
|---|---|
| **Established evidence** | Bằng chứng học thuật đã deep-read hoặc kết quả dự án có artifact đủ để kiểm tra trực tiếp. |
| **Partial evidence** | Có kết quả/tài liệu liên quan nhưng thiếu phạm vi, provenance, kiểm thử hoặc khả năng tái lập cần thiết. |
| **Project hypothesis** | Giả thuyết/thiết kế do luận án đề xuất; chưa phải phát hiện khoa học. |
| **Planned contribution** | Đóng góp dự kiến, chỉ được xác nhận sau validation. |
| **Evidence gap** | Thiếu full text, artifact, test log, metadata hoặc kiểm chứng. |

## Source of truth áp dụng

Thứ tự ưu tiên được dùng trong báo cáo:

1. Quyết định của hai thầy hướng dẫn và Council Review về Limited-FEM.
2. `MASTER_RESEARCH_CHARTER_v2.1_TRACEABILITY_CORE_20260719.md`.
3. `RQ_WP_CHAPTER_PAPER_GATE_MATRIX_v2.1.md` và các ADR hiện hành.
4. `EVIDENCE_GATES_v2.1.md`.
5. `LIVING_EVIDENCE_BASE_v2.1_TRACEABILITY_CORE.md`.
6. RQ1/RQ2 addenda, competitor matrix, deep-read matrix và Zotero audit.
7. Paper direction files.
8. README v2.2, demo handoff, planning, báo cáo chuyên đề và archive chỉ là nguồn hỗ trợ.

Nguồn xác lập thứ tự này: `00_PHD_DT_STEEL_INSPECTION_2026_2029_LIMITED_FEM/00_GOVERNANCE/SOURCE_OF_TRUTH_HIERARCHY_v2.1.md`, dòng 7–18. Archive, backup, prompt và tài liệu discovery không được dùng để ghi đè governance hiện hành.

---

# 1. Tóm tắt điều hành

Luận án đang ở trạng thái **G1 và G2 triển khai song song, G3 chưa được thực thi như một validation package**. G1 vẫn là nút chặn bằng chứng kỹ thuật vì repository chưa có gói hoàn chỉnh, tự chứa và được ký duyệt gồm run registry khóa, pipeline tái lập, đánh giá LORO/LOCO sau khi sửa sensor identity, multi-seed deep model, ResNet1D provenance và acceptance matrix. Tái phân tích ba campaign đã tạo các kết quả candidate quan trọng, đặc biệt là sự sụp đổ cross-campaign, nhưng chính báo cáo xác nhận không đóng G1 và gói code/registry lớn nằm ngoài repository (`THREE_CAMPAIGN_REANALYSIS/00_EXECUTIVE_REPORT.md`, dòng 157–167).

G2 nên tiếp tục song song vì việc xác định boundary, xây competency questions (CQ), định nghĩa metadata, cardinality, integrity constraints, Inspection_Record và protocol validation không cần chờ metric cuối của G1. Tuy nhiên, G2/G3 phải chờ G1 để điền **Condition_Evidence thật và đáng tin cậy**, hiệu chỉnh ý nghĩa CEI, chứng minh reverse provenance tới sensor/run/model và biện minh một inspection/action instance bằng dữ liệu thực.

Bằng chứng học thuật mạnh nhất của G1 là yêu cầu tách nhóm nguồn trước windowing, đánh giá theo run/group và kiểm soát leakage; các quan sát dẫn xuất không làm tăng số đơn vị thí nghiệm độc lập (Beleites et al., 2013; Tougui et al., 2021; Matania et al., 2024; Wheat et al., 2024). Bằng chứng mạnh nhất của G2 là CoDEC: sensor/observation, inspection result và IFC GlobalId đã được nối bằng 13 CQs và truy vấn pilot (Lorvão Antunes et al., 2024). Do đó sensor-to-BIM, IFC GlobalId traversal, BIM-linked inspection và CQ nói chung **không còn là nội dung mới**.

Khoảng trống đáng khai thác nhất là: trong phạm vi nguồn văn liệu đã rà soát, chưa có source đã deep-read nào đồng thời chứng minh một chuỗi cấp cấu kiện từ condition evidence có context/confidence tới BIM component, inspection record và action/status history, kèm forward/reverse parity, constraint validation, invalid fixtures và accountability. Đây là **candidate gap mạnh**, nhưng chưa phải novelty đã xác nhận.

Rủi ro lớn nhất của G1 là nhầm các kết quả candidate hoặc bảng aggregate hiện có với bằng chứng cuối, trong khi sensor identity từng không ổn định và code/registries/corrected arrays chưa có trong repository. Rủi ro lớn nhất của G2/Paper 2 là bị reviewer xem là “system integration/website integration” nếu CQ, formal constraints, failure tests và đơn vị phân tích `traceability instance` không được khóa trước khi IT tiếp tục.

Trước triển khai công trình thực, tối thiểu phải có: G1 evidence đủ tin cậy; G2 schema/CQ được phê duyệt; G3 chạy được trên lab case với valid/invalid test log; access/data-right basis; asset/component identity; sensor assignment; baseline/QC protocol; inspection/human-review workflow. Công trình thực chỉ chứng minh field feasibility, không chứng minh field damage diagnosis hoặc transfer classifier.

### Bảy hành động ưu tiên

1. Khôi phục/copy vào repository toàn bộ canonical dataset package, registries, fold manifests, pipeline code và raw Campaign 2–3; gắn version/hash.
2. Chạy lại LORO/LOCO trên sensor mapping đã sửa; hoàn tất multi-seed 1D-CNN và quyết định rõ include/exclude ResNet1D bằng provenance audit.
3. Khóa G1 claim-status table và acceptance matrix; loại mọi metric legacy không có final provenance.
4. Trước IT build, pre-register SCQ/VCQ/RCQ, expected answers, failure conditions và acceptance criteria của G2.
5. Quyết định governance về `Action_Record_ID`, `Action_Status`, `Action_Level`, workflow status và status-event history; không để hai chuỗi cùng điều khiển implementation.
6. Xây G2 specification package tối thiểu và một bộ fixture nhỏ; sau đó chạy G3 forward/reverse và failure tests trước khi làm thêm UI.
7. Chỉ chuẩn bị field access, asset/sensor register và protocol; chưa mở rộng lắp đặt/thu nhận mới cho tới khi stop/go checklist ở Mục 12 đạt.

**Claim ->** Luận án có đủ cơ sở để tiếp tục G2 song song với G1.  
**Evidence ->** Văn liệu đã hỗ trợ các building blocks G2; Charter/matrix cho phép C4/Paper 1 và C5/Paper 2 chạy song song; G2 design không cần metric cuối G1.  
**Limitation ->** G2 chưa có artifact được phê duyệt; G3 chưa có implementation/test log; G1 chưa đóng.  
**Next action ->** Khóa CQ và acceptance criteria trước; hoàn thiện G1 evidence package song song; chỉ dùng evidence thật trong G3 sau G1.

---

# 2. Định vị toàn bộ luận án

| Thành phần | Nội dung |
|---|---|
| Vấn đề nghiên cứu trung tâm | Condition/state-change evidence từ dữ liệu dao động thường tách rời component identity, hồ sơ kiểm tra, provenance và quyết định quản lý; vì vậy khó kiểm chứng bằng chứng nào đã dẫn tới hành động nào. |
| Central thesis statement | Một khung Digital Twin dựa trên dữ liệu tổ chức condition evidence cùng confidence/evidence metadata thành chuỗi truy vết cấp cấu kiện tới BIM, hồ sơ kiểm tra và hỗ trợ hành động kiểm tra–bảo trì có thể kiểm chứng và giải trình; FEM chỉ là tham chiếu danh nghĩa. |
| RQ1 | Dưới đánh giá run-aware, leakage-controlled, dữ liệu khung thép 1:10 và cấu hình cảm biến tạo evidence phân biệt controlled states đáng tin cậy đến mức nào? |
| RQ2 | Condition evidence và confidence được tổ chức, liên kết với BIM components và inspection records thế nào để hỗ trợ justification/accountability dưới limited field damage data? |
| RQ3 | Khung có thể triển khai ở công trình công nghiệp thép thực tới mức nào để hỗ trợ lựa chọn và ghi nhận hành động kiểm tra, không chẩn đoán hư hỏng hiện trường? |
| WP1–WP4 | WP1 lab evidence; WP2 traceability-to-decision; WP3 field feasibility; WP4 decision-support synthesis, gộp vào WP2/WP3. |
| Chương 4–7 | C4 laboratory evidence; C5 traceability framework; C6 field feasibility; C7 inspection-maintenance action support, có thể gộp C6. |
| Paper 1–4 | P1 run-aware sensor/model evidence; P2 formal traceability; P3 field feasibility; P4/section synthesis human-reviewed action logic. |
| Gate G1–G7 | G1 lab integrity/evaluation; G2 specification/CQ; G3 executable lab traceability; G4 field feasibility; G5 scenario/expert review; G6 Paper 2 submission; G7 thesis synthesis/Paper 3 khi đủ evidence. |
| Core contribution | Quản lý thông tin; component-level traceability; verifiability; accountability; inspection-oriented information management. |
| Supporting contribution | Leakage-safe lab evidence; sensor/data quality; DT maturity definition; field deployment/QC lessons. |
| Future work | Predictive maintenance, RUL, calibrated FEM, automated optimization, advanced ontology/blockchain khi có nhu cầu thực. |
| Out of scope | Calibrated FEM, damage diagnosis, stiffness/bolt-preload inference, weighted Health Index, autonomous maintenance, direct lab-to-field transfer và commercial software development. |

Chuỗi nghiên cứu giữ nguyên:

```text
Vibration data
→ condition/state-change evidence
→ BIM-linked component
→ inspection record
→ inspection-maintenance action support
```

Chuỗi định danh dùng làm baseline của báo cáo theo yêu cầu hiện hành:

```text
Sensor_ID
→ BIM_GUID
→ Condition_Evidence_ID
→ Inspection_Record_ID
→ Action_Status
```

Repository có ADR được chấp nhận ngày 19/07/2026 đề xuất sửa mắt xích cuối thành `Action_Record_ID` và coi `Action_Status` là thuộc tính (`RESEARCH_ARCHITECTURE_DECISION_RECORD_ACTION_ID_20260719.md`, dòng 5–26). Báo cáo **không tự thay đổi chuỗi đã khóa trong nhiệm vụ này**. Đây là conflict governance bắt buộc giải quyết trước khi freeze schema; xem Phụ lục C.

FEM chỉ được mô tả:

> nominal, uncalibrated, reference-only, not used for damage diagnosis.

FEM không có RQ, WP, chương, Paper hoặc Evidence Gate riêng. Đóng góp chính không phải AI accuracy, FEM hoặc website; chúng chỉ là phương tiện tạo, tổ chức hoặc trình diễn evidence.

---

# 3. Bản đồ bằng chứng G1–G2–G3

| Gate | RQ/WP/Paper | Claim cần chứng minh | Evidence hiện có | Evidence còn thiếu | Trạng thái |
|---|---|---|---|---|---|
| G1 | RQ1/WP1/Paper 1 | Controlled states phân biệt được trên held-out runs; so sánh sensor/model công bằng; uncertainty/provenance đủ. | 216-file documentation; corrected mapping report; 12 test-result rows; provisional LORO/LOCO; permutation ở ba cấu hình; literature về leakage/grouped CV. | Self-contained raw/registry/code package; rerun trên corrected mapping; full CNN/multi-seed; ResNet1D provenance; signed acceptance. | **OPEN; partial evidence.** |
| G2 | RQ2/WP2/Paper 2 | Mô hình thông tin, CQ, cardinality, provenance và accountability được khóa trước build. | Prior studies cho từng building block; ADR/Charter design seeds; local IFC identity anchor. | Approved identifier/CEI/Inspection/Action schemas; CQ registry; expected answers; constraints; version governance. | **OPEN; specification not produced.** |
| G3 | RQ2/WP2/Paper 2 | Golden/reverse paths chạy; invalid records bị phát hiện; evidence truy về source sensor/run/model. | Test families đã đề xuất; IFC snapshot; UI handoff cho static scenarios. | Database/fixtures; executable queries; orphan/duplicate/missing/provenance/cardinality/status tests; test logs; reproducible package. | **OPEN; not implemented.** |

### Firewall bốn lớp

| Lớp | Được chứng minh | Không được thay thế bằng |
|---|---|---|
| Laboratory evidence | Validity của evidence trên controlled 1:10 runs. | Field feasibility hoặc damage diagnosis. |
| Information traceability | Completeness, integrity, round-trip, provenance. | Classification accuracy hoặc UI screenshots. |
| Field feasibility | Access, deployment, data return, baseline, mapping và workflow. | Lab performance hoặc simulated demo. |
| Management decision support | Transparency, human review, action/status history. | CEI score, DT maturity level hoặc automated alarm. |

---

# 4. G1 – Laboratory condition evidence

## 4.1. Mục tiêu khoa học

G1 phải tạo **evidence có provenance và uncertainty**, không chỉ accuracy. Đơn vị độc lập là run/campaign phù hợp với claim; windows là observations dẫn xuất. Việc báo cáo hàng nghìn windows như hàng nghìn đơn vị độc lập sẽ thổi phồng precision (Beleites et al., 2013). Group-wise/LOGO phản ánh unseen-source performance tốt hơn record-wise split (Tougui et al., 2021), còn nghiên cứu vibration chỉ ra leakage và sensor position có thể làm thay đổi mạnh apparent performance (Matania et al., 2024; Wheat et al., 2024).

## 4.2. Run-aware/LORO và leakage risk

**Claim ->** Split phải thực hiện ở cấp run trước windowing; learned preprocessing chỉ fit trên training runs.  
**Academic evidence ->** Source-group separation trước segmentation và grouped validation là biện pháp trực tiếp chống leakage (Tougui et al., 2021; Matania et al., 2024; Wheat et al., 2024).  
**Project evidence ->** Reanalysis ghi group split trước windowing, non-overlapping 2 s windows và train-only scaler (`00_EXECUTIVE_REPORT.md`, dòng 36–44).  
**Limitation ->** `pipeline_lib.py`, fold manifests và master registry đầy đủ không có trong repository, nên claim implementation chưa tự tái lập được.  
**Next action ->** Đưa code/registries/raw inputs vào versioned package; chạy một command từ raw tới metrics; lưu environment và hashes.

LORO không tự động tạo đủ statistical power. Sáu folds có training overlap, không tương đương sáu datasets độc lập; Wilcoxon trên folds chỉ nên exploratory (Demšar, 2006). Small-sample claims cần run-level outputs, empirical chance/permutation và sensitivity analysis (Combrisson & Jerbi, 2015; Ojala & Garriga, 2010).

## 4.3. Kết quả đã thực hiện và ranh giới

Kết quả project hiện có, luôn phải gắn nhãn **candidate pending G1 closure**:

- Tái phân tích báo cáo 216 recordings và 234 feature-model LORO fits, 27 feature-model LOCO fits, cùng 9/9 cross-campaign CNN configurations (`00_EXECUTIVE_REPORT.md`, dòng 72–99).
- Random Forest median macro-F1 trong campaign được báo cáo 0.683, 0.878 và 0.609; cross-campaign medians của LogReg/SVM/RF/CNN là 0.186/0.195/0.166/0.152, đều không vượt chance 0.25 (`00_EXECUTIVE_REPORT.md`, dòng 78–99).
- Permutation controls ở ba cấu hình ủng hộ within-campaign discrimination nhưng không ủng hộ cross-campaign generalization (`00_EXECUTIVE_REPORT.md`, dòng 126–138).
- Sensor block positions của Campaign 1–2 từng không ổn định; canonical dataset report sau đó tuyên bố 576/576 mappings resolved high confidence (`09_DATASET_VALIDATION_REPORT.md`, dòng 14–23). Tuy nhiên registry/code/corrected arrays tương ứng vắng trong repository và report yêu cầu fresh modelling pass (`09_DATASET_VALIDATION_REPORT.md`, dòng 26–45).
- Legacy RF/CNN/ResNet1D metrics đã bị claim audit loại khỏi final results vì chưa theo final LORO protocol (`PAPER1_GATE1_CLAIM_EVIDENCE_AUDIT_v2.md`, dòng 32–44).

Không được dùng một accuracy hoặc một macro-F1 để kết luận G1 đạt. G1 cần per-class/per-run/fold distribution, uncertainty, empirical null, provenance và sign-off.

## 4.4. Sensor configuration, sensor mode và model comparison

Sensor configuration có thể ảnh hưởng apparent performance, nhưng bearing evidence không xác định cấu hình tốt nhất cho khung thép (Wheat et al., 2024). So sánh S1/S2/S1+S2 chỉ có giá trị nếu cùng physical sensor mapping, folds, preprocessing, seed set và budget. Bảng `09_SENSOR_CONFIGURATION_RESULTS.csv` hiện aggregate model coverage không đồng đều; chưa đủ cho claim “sensor configuration dominates architecture”.

ResNet1D là blocker riêng: literature không thể sửa project provenance. Cần xác nhận channels, sensor mode, fold assignments, preprocessing, seeds, code version và checkpoint hash. Nếu không khôi phục được, lựa chọn tối giản và có thể bảo vệ là loại ResNet1D khỏi Paper 1 thay vì giữ một con số không truy nguồn.

## 4.5. CEI và metadata G1 phải chuyển cho G2

CEI là cấu trúc confidence/evidence metadata, không phải severity, Health Index hoặc scalar phổ quát. Một `Condition_Evidence_ID` tối thiểu cần:

- dataset/file hash và version;
- campaign, run, excitation, controlled state và `Evidence_Context`;
- physical `Sensor_ID`, assignment/location, channels, axes, units, sampling;
- held-out run/campaign và fold definition;
- windowing/preprocessing provenance;
- model/config/code/checkpoint/seed version;
- prediction, confidence/calibration status;
- per-run/fold variability và permutation result;
- data-quality warnings, validity status, timestamp và creator.

## 4.6. Quan hệ phụ thuộc G1–G2

1. **G1 phải tạo gì cho G2?** Các `Condition_Evidence_ID` thật, versioned, có CEI/provenance và bounded-use statement.
2. **G2 cần field nào từ G1?** Toàn bộ metadata nêu tại 4.5 để reverse trace tới source run/model.
3. **G2 làm gì trước khi G1 đóng?** Domain boundary; context rules; entity/relationship draft; identifiers; CEI dictionary; record schemas; CQ/expected answer/failure/acceptance; valid/invalid fixture design.
4. **Paper 2 claim nào phụ thuộc G1?** Claim rằng real sensor-derived evidence đã đi trọn chain; CEI có empirical meaning; inspection/action instance được biện minh bằng evidence đáng tin cậy. Formal schema, cardinality, CQ và invalid-data protocol không cần chờ metric cuối G1.

**Verdict G1:** bằng chứng phương pháp mạnh, project result đáng chú ý nhưng chưa tự tái lập và chưa signed. **Evidence is currently insufficient.**

---

# 5. G2 – Cơ sở học thuật cho information traceability

## 5.1. Sensor/observation data và BIM/IFC

**Claim ->** Sensor/observation có thể liên kết với BIM/IFC và phục vụ truy vấn quản lý.  
**Academic evidence ->** CoDEC mô hình hóa sensors, observations và inspection results, dùng IFC GlobalId để truy vấn qua 13 CQs và ba pilots (Lorvão Antunes et al., 2024).  
**Prior achievement ->** Sensor/observation-to-IFC traversal và query-based retrieval đã có.  
**Limitation ->** Mapping còn manual; raw time series lưu ngoài ontology; SHACL chưa chạy; không có full evidence-to-action history.  
**Thesis relevance ->** Dùng như benchmark bắt buộc, không dùng như novelty claim.  
**Remaining gap ->** Contract giữa source evidence, external store, BIM component và downstream records có validation/failure tests.

## 5.2. IFC GlobalId và component identity

**Claim ->** Stable component identity là anchor của component-level traceability.  
**Academic evidence ->** CoDEC dùng IFC GlobalId (Lorvão Antunes et al., 2024); AIM case liên kết asset classification, IFC models và database nhưng chưa có sensor/inspection chain (Heaton & Parlikad, 2020).  
**Prior achievement ->** IFC/object identity và asset-information federation đã có tiền lệ.  
**Limitation ->** Stable GlobalId qua model revisions chưa được chứng minh trong corpus; local IFC chỉ là một snapshot.  
**Thesis relevance ->** G2 phải có snapshot/version/hash và cross-version policy.  
**Remaining gap ->** GUID persistence/change handling và mapping review under version changes.

## 5.3. Inspection and maintenance records

**Claim ->** BIM objects có thể anchor work/maintenance records.  
**Academic evidence ->** Kim et al. liên kết IFC/COBie objects với 590 FM records và hỗ trợ SPARQL retrieval (Kim et al., 2018); CoDEC nối inspection result với IFC element (Lorvão Antunes et al., 2024).  
**Prior achievement ->** Object-linked record retrieval và BIM-linked inspection không mới.  
**Limitation ->** Kim et al. không có sensor-derived condition evidence, persistent GlobalId proof, CQs/constraints hay status history.  
**Thesis relevance ->** Inspection_Record cần source, component, inspector, time, finding, disposition, approval và version.  
**Remaining gap ->** Evidence-to-inspection-to-accountable action continuity.

## 5.4. Provenance and evidence context

**Claim ->** Evidence/action cần actor, operation, version, timestamp và identity.  
**Academic evidence ->** BIM transaction prototype có thể tái dựng change history từ actor/operation/version/time (Çelik et al., 2022; publication year requires reconciliation). Lee et al. chứng minh accountable information sharing và tamper handling trong một DT/blockchain proof of concept (Lee et al., 2021).  
**Prior achievement ->** Provenance và accountability mechanisms đã có.  
**Limitation ->** Design/construction hoặc hypothetical case; không phải inspection provenance; blockchain không được chứng minh là cần thiết.  
**Thesis relevance ->** Lấy minimum provenance fields, không lấy blockchain làm novelty.  
**Remaining gap ->** Context-preserving provenance từ controlled lab evidence tới inspection/action record.

## 5.5. Competency questions và ontology validation

**Claim ->** CQ cần phân loại và gắn expected answer/failure.  
**Academic evidence ->** Scoping, validation và relationship CQs có chức năng khác nhau (Keet & Khan, [Author/year metadata requires verification]); CoDEC cho thấy CQ có thể dẫn thiết kế ontology/query (Lorvão Antunes et al., 2024).  
**Prior achievement ->** CQ và ontology nói chung không mới.  
**Limitation ->** Danh sách câu hỏi không đồng nghĩa validation; metadata của nguồn CQ chưa hoàn chỉnh.  
**Thesis relevance ->** Pre-register CQ trước schema freeze/build.  
**Remaining gap ->** CQ suite có expected answer, executable query, failure condition và acceptance evidence cho chain đề tài.

## 5.6. Referential integrity và constraint validation

**Claim ->** Query success không đủ; invalid data phải bị từ chối.  
**Academic evidence ->** CoDEC dùng CQ/SPARQL/OOPS nhưng không thực thi SHACL (Lorvão Antunes et al., 2024). Nguồn trực tiếp về SHACL/ifcOWL trong repository chỉ có HTML/abstract, không đủ cho detailed claim.  
**Prior achievement ->** Semantic query validation có tiền lệ; executed failure suite cho chain này chưa thấy trong corpus.  
**Limitation ->** Ba full texts ưu tiên còn thiếu.  
**Thesis relevance ->** SHACL chỉ là một implementation option; relational constraints hoặc JSON Schema/custom validator đều hợp lệ nếu đáp ứng CQ.  
**Remaining gap ->** Reproducible invalid fixtures cho orphan, duplicate, cardinality và missing provenance.

## 5.7. Action records, status history và accountability

**Claim ->** Current status không đủ cho accountability; cần record/event có actor/time/reason.  
**Academic evidence ->** Smart maintenance maturity nhấn mạnh asset-condition-job tracking, governance và human interpretation (Johannes et al., 2021).  
**Prior achievement ->** Organizational accountability và job tracking đã được nghiên cứu.  
**Limitation ->** Không có proposed four-level workflow hay action-event schema.  
**Thesis relevance ->** Tách immutable action record, action level, workflow/approval status và transition events.  
**Remaining gap ->** Governance chưa thống nhất `Action_Record_ID`/`Action_Status`; workflow chưa scenario-validated.

## 5.8. External time-series storage và BIM-linked architecture

**Claim ->** Time-series có thể lưu ngoài BIM nhưng phải có referential contract.  
**Academic evidence ->** Review 93 studies ghi nhận IFC time-series và toolchain barriers (Du et al., 2024; complete author metadata requires verification); CoDEC lưu raw series ở external JSON (Lorvão Antunes et al., 2024).  
**Prior achievement ->** External storage là kiến trúc phổ biến.  
**Limitation ->** External storage tự nó không đảm bảo integrity, provenance hoặc version parity.  
**Thesis relevance ->** G2 định nghĩa URI/key/hash/version contract, không nhét raw arrays vào IFC.  
**Remaining gap ->** Validation khi source file đổi, mất, trùng hoặc bị thay thế.

## 5.9. Digital Twin maturity phù hợp luận án

**Claim ->** DT maturity cần tự định nghĩa minh bạch và không đồng nhất với autonomy.  
**Academic evidence ->** Gemini-principles maturity model dùng 27 rubrics, 40 experts và hai cases để đánh giá mục đích, roles, data quality, standards, integration và governance ([Author/year metadata requires verification], 2021).  
**Prior achievement ->** Maturity rubrics và governance đã có.  
**Limitation ->** Maturity level không phải condition/action level; top maturity có autonomy ngoài scope.  
**Thesis relevance ->** Luận án là data-connected, descriptive/diagnostic-at-management-level, human-reviewed; không predictive/autonomous.  
**Remaining gap ->** Viết definition/maturity claim chính thức và kiểm chứng nó bằng artifacts thực, không bằng marketing website.

## 5.10. Construction/asset information management context

**Claim ->** Đóng góp thuộc quản lý thông tin và asset decision accountability.  
**Academic evidence ->** AIM hỗ trợ federated asset information (Heaton & Parlikad, 2020); smart maintenance yêu cầu asset/condition/job tracking và organizational governance (Johannes et al., 2021).  
**Prior achievement ->** Asset registers, BIM-FM integration và maturity models đã có.  
**Limitation ->** Không nguồn nào thay thế project validation.  
**Thesis relevance ->** Đơn vị phân tích là `traceability instance`, không phải website feature.  
**Remaining gap ->** Formal, measurable evidence-to-inspection/action traceability cho industrial steel building.

---

# 6. Phân tích đối thủ gần nhất

| Study | Sensor/data | BIM/IFC identity | Condition evidence | Inspection record | Action record/status | CQ validation | Integrity tests | Main limitation |
|---|---|---|---|---|---|---|---|---|
| Lorvão Antunes et al. (2024) | Có sensor/observation; raw external JSON | IFC GlobalId | Có condition/inspection result | Có | Partial next-inspection info | 13 CQ, SPARQL, OOPS | Không executed SHACL/failure suite | Mapping partly manual; không full action history. |
| Lee et al. (2021) | Hypothetical positioning sensors | BIM object, không GlobalId proof | Compliance statements | Không | Ledger/block status, không inspection action | Partial compliance rules | Ledger/tamper, không ID constraints | Virtual/mock construction case. |
| Kim et al. (2018) | Không | IFC entity/object IDs | Không | 590 maintenance records | Không | Không | Không | Không sensor-derived evidence, GlobalId stability hoặc status history. |
| Çelik et al. (2022) | Không | BIM object IDs | Không | Không | Operation/transaction status | Transaction verification | Không referential suite | Design-stage provenance, không inspection chain. |
| Heaton & Parlikad (2020) | Không | IFC/AIM asset identity | Không | Không | Không | Không | Không | Architecture/asset foundation, không chain. |

Competitor gần nhất là Lorvão Antunes et al. (2024). Paper 2 phải benchmark trực tiếp feature coverage, CQ answers, reverse query và invalid fixtures với CoDEC. Không được tuyên bố mới ở:

- sensor-to-BIM integration;
- BIM-linked inspection records;
- IFC GlobalId traversal;
- competency questions nói chung;
- ontology, graph database hoặc blockchain nói chung.

**Claim ->** Paper 2 chỉ khác biệt nếu chứng minh complete constrained traceability, không phải vì kết nối BIM với sensor.  
**Evidence ->** CoDEC đã bao phủ phần lớn sensor/inspection/GlobalId/CQ; Kim/Çelik/Lee đã bao phủ records/provenance/accountability từng phần.  
**Limitation ->** Missing full texts có thể thu hẹp gap.  
**Next action ->** Hoàn tất acquisition, pre-register comparison matrix và validation trước implementation.

---

# 7. Khoảng trống nghiên cứu và ranh giới tính mới

## 7.1. Khoảng trống có bằng chứng tương đối mạnh

- Chưa có reviewed full-text source nào kết hợp semantic integrity với accountability trong một evidence-to-inspection/action chain; hai năng lực này còn tách giữa CoDEC và các provenance/accountability studies (Lorvão Antunes et al., 2024; Lee et al., 2021; Çelik et al., 2022).
- Không reviewed implementation nào báo cáo deliberate orphan, duplicate, missing mandatory links và illegal status changes rồi chứng minh tất cả bị bắt (Lorvão Antunes et al., 2024).
- Không source nào báo cáo forward/reverse parity trên cùng linked set, dù đã có object-to-record và inspection-to-element queries từng phần (Kim et al., 2018; Lorvão Antunes et al., 2024).
- Không source nào có action status-event history đầy đủ gắn trực tiếp với inspection evidence (Johannes et al., 2021; Lorvão Antunes et al., 2024).

## 7.2. Candidate gaps

- Context-preserving condition evidence model có CEI, provenance và bounded-use rules.
- Stable IFC GlobalId qua revisions/tool round-trips.
- Explicit cardinalities và mapping confidence/human verification.
- Laboratory evidence -> inspection-oriented information management mà không suy transfer vật lý.
- Four-level human-reviewed action workflow.

## 7.3. Cần thêm full text hoặc systematic search

- `3II2WKLN`: ifcOWL/SHACL.
- `NUTL57KJ`: IFC inspection-maintenance representation.
- `Z4IBWW9Y`: IFC bridge defects/actions.
- Parent metadata của CQ paper.
- Systematic search ngoài corpus hiện tại trước final novelty statement.

## 7.4. Không còn được xem là mới

- Sensor/observation-to-BIM/IFC.
- IFC/object-linked work records.
- BIM-linked inspection results.
- IFC GlobalId traversal.
- CQ-driven ontology/query.
- Provenance ledger/blockchain nói chung.
- DT maturity model nói chung.

| Candidate contribution | Prior evidence | Remaining gap | Strength of evidence | Required validation | Publication potential |
|---|---|---|---|---|---|
| Context-preserving evidence model | Provenance, external storage, CEI ingredients từng phần | Formal context/non-transfer constraints | Medium | Schema + valid/invalid fixtures + G1 payload | High nếu generalizable. |
| Constrained component chain | GlobalId/records/CQs đã có | Full chain + cardinality + accountability | Medium-high, corpus-bounded | Formal model, queries, integrity suite | Cao nhất cho Paper 2. |
| Pre-registered CQ protocol | CQ taxonomy/CoDEC | Expected answers/failure criteria cho chain đề tài | Medium | Timestamped pre-registration; executable report | Supporting-to-strong. |
| Referential failure validation | SHACL candidate, chưa full text | Deliberate failure suite | Medium | Tool-independent tests and logs | Strong differentiator. |
| Bidirectional parity | Partial object/record retrieval | Same-set round trip proof | Medium | Automated golden/reverse comparison | Strong supporting. |
| Action/status history | Governance/job tracking từng phần | Event-level accountable transitions | Medium-low | Scenario + expert review | Promising, may merge Paper 2/4. |
| Lab-to-inspection information link | Lab evidence và traceability riêng rẽ | Bounded-use, non-transfer linkage | Low-medium | G1 evidence + context validation | Candidate, high reviewer risk. |

Mọi novelty statement phải viết:

> Trong phạm vi nguồn văn liệu đã rà soát, các tiền lệ từng phần đã tồn tại, nhưng chuỗi evidence-to-action có ràng buộc, kiểm thử lỗi và accountability chưa được chứng minh đầy đủ.

---

# 8. Đề xuất đóng góp khoa học có thể bảo vệ

| Claim | Evidence | Limitation | Validation needed | Verdict |
|---|---|---|---|---|
| Context-preserving Condition Evidence model | G1 metadata needs; provenance/external-store literature | CEI chưa operationalized; chưa có G1 final payload | Schema, context/non-transfer rules, invalid cases | **Strong candidate** |
| Chuỗi truy vết cấp cấu kiện có ràng buộc | GlobalId, records và CQ precedents | Complete chain chưa implemented | Cardinality, uniqueness, FK/constraints, benchmark | **Strong candidate** |
| Competency questions được pre-register | CQ taxonomy và CoDEC | Parent metadata/CQ effectiveness chưa hoàn chỉnh | Registry trước schema freeze; expected/actual answers | **Supporting contribution** |
| Referential-integrity và failure-case validation | Gap rõ trong closest competitor | Direct SHACL source thiếu full text | Tool-independent invalid fixture suite | **Strong candidate** |
| Bidirectional round-trip traceability | Partial prior queries | Parity chưa chứng minh | Golden/reverse automated tests | **Promising but not yet demonstrated** |
| Inspection_Record và Action_Record/status history | FM records, provenance, governance | Governance chain xung đột; workflow vocabulary chưa khóa | Schema decision + event tests | **Promising but not yet demonstrated** |
| Accountable action workflow | Smart maintenance governance/human interpretation | Four-level logic chưa literature-validated | Facility-manager scenarios; reviewer records | **Supporting contribution** |
| Laboratory evidence với inspection-oriented management | G1 + G2 conceptual bridge | Không được suy lab-to-field transfer; G1 chưa final | Bounded-use contexts + real G1 payload | **Promising but not yet demonstrated** |

Không candidate nào được gọi là contribution đã hoàn thành trước G2/G3 validation.

---

# 9. G2 Specification Package đề xuất

| Artifact | Mục tiêu | Trường/quan hệ chính | Tiêu chí hoàn thành | Dependency |
|---|---|---|---|---|
| 1. Identifier schema | Khóa namespace và lifecycle ID | Sensor_ID, BIM_GUID, Condition_Evidence_ID, Inspection_Record_ID, current end-state; immutable/mutable rules | Unique, format, owner, creation/retirement rules được duyệt | G2; governance decision về action. |
| 2. Condition_Evidence/CEI schema | Chứa evidence + confidence/context | source hash, run, sensor, model, prediction, validity, variability, quality, context, timestamp/version | Mọi required field có type/source/null rule; fixture G1-like hợp lệ | Draft độc lập; final semantic meaning chờ G1. |
| 3. Inspection_Record schema | Ghi inspection có trách nhiệm | component, trigger evidence, inspector, method, finding, disposition, attachments, approval, version | Reverse query tới evidence/component; không orphan | G2. |
| 4. Action_Record/status-event schema | Tách action identity và trạng thái | action ID proposal, level, workflow/approval status, prior/new event, actor, time, reason | Governance quyết định; legal transitions; event immutable | G2; scenario validation G3/G5. |
| 5. Provenance requirements | Tái dựng lineage | creator, source, operation, transform, version/hash, time, approver | Reverse tới raw source/model; tamper/change logged | G1 metadata + G2. |
| 6. Cardinality/integrity constraints | Ngăn chain sai | 1:n/m:n rules, mandatory links, uniqueness, effective dates | Machine-checkable; invalid fixtures fail | G2; implemented G3. |
| 7. SCQ/VCQ/RCQ registry | Khóa câu hỏi trước build | ID, type, actor, question, query target | Supervisor approval + timestamp before schema freeze | G2 independent of final G1. |
| 8. Expected answers | Chống post-hoc validation | fixture, expected rows/fields/count | Mỗi CQ có deterministic expected result | G2. |
| 9. Failure conditions | Định nghĩa fail | missing, duplicate, orphan, mismatch, stale status | Mỗi CQ có explicit fail state | G2. |
| 10. Acceptance criteria | Điều kiện PASS | completeness, parity, detection, reproducibility | Numeric/binary criteria và reviewer/sign-off | G2. |
| 11. Validation protocol | Quy trình chạy G3 | environment, data fixtures, test order, logs | Một command; retained outputs; rerunnable | G3. |
| 12. Governance/version control | Kiểm soát thay đổi | schema version, migration, model snapshot/hash, CDE state, owner/approver | Không silent change; change log và compatibility policy | G2/G3; field. |

### Thứ tự thực hiện tối thiểu

1. Boundary và controlled vocabulary.
2. SCQ/VCQ/RCQ + expected/failure/acceptance.
3. Governance decision về action identity/status.
4. Freeze ER/cardinality và metadata schemas.
5. Tạo valid/invalid fixtures.
6. Chọn implementation đơn giản nhất đáp ứng CQ.
7. Chạy G3; UI chỉ đọc từ validated records.

**Claim ->** IT không nên tiếp tục API/UI khoa học trước CQ và schema freeze.  
**Evidence ->** Repository hiện không có G2 package, data model implementation hoặc G3 tests; demo handoff cho phép static data nhưng không định nghĩa integrity.  
**Limitation ->** Viewer engine có thể tái sử dụng sau.  
**Next action ->** Dừng feature build; giao IT specification/test fixtures sau khi G2 được duyệt.

---

# 10. G3 – Thiết kế kiểm chứng end-to-end

## 10.1. Golden path

```text
Condition evidence
→ source Sensor_ID
→ BIM_GUID
→ Inspection_Record_ID
→ action record / Action_Status
```

## 10.2. Reverse path

```text
Action/inspection record
→ BIM_GUID
→ Condition_Evidence_ID
→ Sensor_ID
→ source run/file/model/version
```

## 10.3. Protocol test tối thiểu

| Test ID | Input | Expected result | Failure condition | Acceptance criterion | Evidence artifact |
|---|---|---|---|---|---|
| G3-T01 | Một valid traceability instance | Golden path trả đủ links | Bất kỳ mandatory link thiếu | 100% expected IDs/fields đúng | `G3_GOLDEN_PATH_LOG` |
| G3-T02 | Action/inspection ID hợp lệ | Reverse path về đúng evidence/sensor/run/model | Linked set khác golden path | Set equality = true | `G3_REVERSE_PATH_LOG` |
| G3-T03 | Orphan Sensor_ID | Record bị reject/flag | Record được chấp nhận | Detection = PASS | invalid fixture + validator log |
| G3-T04 | Orphan BIM_GUID | Reject/flag | Silent acceptance | Detection = PASS | fixture/log |
| G3-T05 | Duplicate ID | Uniqueness failure | Hai records cùng ID tồn tại | Detection = PASS | fixture/log |
| G3-T06 | Missing Condition_Evidence | Chain incomplete | Inspection/action vẫn hợp lệ | Detection = PASS | fixture/log |
| G3-T07 | Missing CEI/provenance | Reject hoặc explicit invalid status | Evidence được coi valid | Detection = PASS | fixture/log |
| G3-T08 | Invalid cardinality | Constraint failure | Nhiều quan hệ trái policy được nhận | Detection = PASS | fixture/log |
| G3-T09 | Invalid relationship/type | Domain/range failure | Link sai entity được nhận | Detection = PASS | fixture/log |
| G3-T10 | Stale/conflicting Action_Status | Conflict/version failure | Current status không xác định | Single current state + conflict logged | event fixture/log |
| G3-T11 | Broken reverse traceability | Reverse parity fail | Golden pass nhưng reverse thiếu | Equality assertion fails correctly | query comparison report |
| G3-T12 | Unaccountable status change | Reject event thiếu actor/time/reason | Event được chấp nhận | Mandatory event fields enforced | accountability log |

SHACL phù hợp nếu dùng RDF/ontology; relational FK/check/unique constraints hoặc JSON Schema + application validator có thể phù hợp hơn với architecture tối giản. Công cụ không phải đóng góp; machine-checkable behavior mới là evidence.

G3 chỉ đóng khi test package, fixtures, expected/actual outputs, environment, version và reviewer/sign-off đều nằm trong repository. Website chạy không thay thế các artifact này.

---

# 11. Đánh giá demo hiện tại

| Thành phần | Trạng thái thực tế | Phân loại | Quyết định |
|---|---|---|---|
| IFC viewer/3D engine | Handoff nói engine hiện có; source repo không hiện diện | UI capability claim, unauditable | Chỉ tái sử dụng khi lấy được source/version. |
| Traceability module | Tài liệu ghi “hoàn toàn chưa có” | Planned artifact | Xây sau G2; không hard-code logic trong UI. |
| Static 2–3 scenarios | Được planning cho phép | UI/demo fixture seed | Externalize thành validated fixture; UI chỉ hiển thị. |
| Data model | Chỉ có conceptual chain/ADR | Design seed | Phải xây/freeze theo G2. |
| API/database | Không tìm thấy implementation/OpenAPI/migration | Absent | Không phát triển trước schema. |
| Integrity tests | Không có G3 executable tests | Absent | Bắt buộc xây mới. |
| IFC identity | Một IFC4X3 snapshot có GlobalIds/version metadata; Asset_ID chưa đầy đủ và có duplicate business ID | Partial project evidence | Audit, repair, tạo second controlled version. |
| Rapexco dashboard | Screenshots/claims trong report; không có source/API/data provenance | Communication artifact | Không dùng làm G3/G4 closure. |
| Commercial SaaS features | Pricing/auth/team collaboration | Out of thesis scope | Dừng/ẩn; không đầu tư thêm. |
| CDE/version UI | Chưa có verified version lineage | Planned UI | Chỉ làm sau model-version register. |

### Có thể chuyển thành artifact

- ADR/Charter fields -> G2 schema seed.
- README context/non-transfer block -> context-mapping rules seed.
- IFC GlobalIds/Asset_ID -> valid identity seed sau repair.
- Duplicate `Asset_ID` -> deliberate G3 negative fixture sau khi baseline sạch.
- Asset register -> assignment schema seed, không phải mapping evidence.
- Static scenarios -> G3 fixtures nếu nằm ngoài UI và có expected results.

### Phải xây lại

- Traceability data layer; sensor assignment; asset–IFC crosswalk.
- ConditionEvidence/Inspection/Action records và status-event history.
- G3 test pack, model-version register, provenance package.
- Field raw-data/processing package và Git/release provenance.

### Không cần đầu tư lúc này

- Pricing/auth/multi-tenant collaboration.
- Live streaming trước static fixtures pass.
- Ontology/SPARQL/blockchain/graph database trước khi relational/JSON solution không đáp ứng CQ.
- Dashboard decoration, gauge, nhiều biểu đồ, automated alerts.
- Rebuild viewer engine khi source hiện tại chưa được audit.

**Verdict demo:** hiện là handoff/UI concept và một số visual claims, không phải data-model implementation hoặc G3 evidence. **Evidence is currently insufficient.**

---

# 12. Điều kiện trước khi triển khai công trình thực tế

| Điều kiện | Gate liên quan | Bắt buộc trước field? | Trạng thái hiện tại | Evidence cần có |
|---|---|---|---|---|
| G1 evidence đủ tin cậy | G1 | Có cho scientific field integration | OPEN | Signed G1 matrix; reproducible corrected evaluation. |
| G2 schema đã khóa | G2 | Có | Chưa có package | Approved schema/CQ/version. |
| G3 lab demo đã chạy | G3 | Có trước claim field traceability | Chưa implemented | Test logs và fixtures. |
| Field access/data rights | G4 | Có | Report có contract reference nhưng signed artifact chưa thấy | Signed/confirmed agreement + data-use terms. |
| BIM_GUID/asset identity | G2/G4 | Có | Cam Ranh IFC partial; Rapexco identity chưa xác nhận | Field asset register/crosswalk/version. |
| Sensor-to-component mapping | G4 | Có | Không có governed mapping | Sensor assignment ID, location, effective dates, reviewer/confidence. |
| Baseline acquisition protocol | G4 | Có | Chưa khóa | Sampling, environment, duration rationale, completeness/drift rules. |
| Inspection workflow | G4/G5 | Có | Conceptual | Template, actors, trigger/disposition/approval. |
| Human review | G5 | Có trước action validation | Chưa có review record | Reviewer, time, comments, disposition. |
| Ethics/data governance | G4 | Khi áp dụng | Chưa xác nhận | Ownership, privacy, retention, access, incident handling. |
| Raw-data return/provenance | G4 | Có | Field data package thiếu | Manifest, hashes, clocks/timezone, configs, QC. |
| Không direct classifier transfer | G4 | Luôn | Governance đã cấm | Protocol statement và audit. |

**Stop/go:** field preparation được làm song song ngay; physical deployment/data acquisition mới là **NO-GO** cho tới khi access, identities, assignment, QC, provenance và human workflow được duyệt. Không cần chờ nộp Paper 1–2 để soạn protocol, nhưng deployment chỉ bắt đầu sau một authorization point rõ trong G4.

---

# 13. Chiến lược bài báo

| Paper | Central claim | Required evidence | Novelty risk | Dependency | Gate to close | Recommended timing |
|---|---|---|---|---|---|---|
| Paper 1 | Run-aware evidence phân biệt controlled states và giới hạn cross-campaign; fair sensor/model comparison | Corrected package, LORO/LOCO, permutation, multi-seed, ResNet decision, uncertainty | Nếu chỉ báo accuracy hoặc overclaim sensor superiority | Raw/package restoration | G1 | Ưu tiên gần nhất sau rerun/sign-off. |
| Paper 2 | Formal, verifiable component-level traceability từ evidence tới inspection/action | G2 package; benchmark; G3 valid/invalid tests; G1 payload | Reviewer xem là system integration | CQ before build; G1 real evidence for final case | G2, G3, G6 | Draft concept/method song song G1; submit sau G3. |
| Paper 3 | Field feasibility: deployment, baseline, mapping, data return, scenarios, inspection workflow | Access, sensor/asset registers, baseline/QC, 2–3 scenarios | Field case mỏng; thiếu baseline/provenance | G1–G3 stable + G4 authorization | G4/G5 | Sau lab validation và field window. |
| Paper 4/synthesis | Human-reviewed evidence-to-inspection action logic | Scenario protocol, facility-manager review, status history | Subjective/small sample; overlap P2/P3 | G5 evidence | G5/G7 | Merge Paper 3 nếu evidence độc lập không đủ. |

Paper 2 tránh “website integration” bằng năm điều:

1. Đơn vị phân tích là `traceability instance`.
2. CQ/expected/failure/acceptance được pre-register.
3. Formal schema/cardinality/constraints là contribution object.
4. Valid/invalid fixture và round-trip test là evaluation.
5. UI chỉ là instrument; bài báo phải đứng vững nếu bỏ toàn bộ screenshots.

Không khẳng định Q1/Q2 hoặc journal ranking. **Journal quartile is unverified.**

---

# 14. Định hướng chương luận án

| Chương | Vai trò | Evidence sử dụng | Paper liên quan | Nội dung chưa đủ bằng chứng |
|---|---|---|---|---|
| Chương 1 | Vấn đề quản lý và mục tiêu | Governance + context | — | Formal programme requirements. |
| Chương 2 | Literature/gap | Peer-reviewed G1/G2/G3 corpus | P1–P3 | Missing competitor full texts/systematic search. |
| Chương 3 | Research design, firewall, DT definition, nominal FEM | Charter + methodology | Tất cả | DT maturity wording và governance conflicts. |
| Chương 4 | Laboratory evidence | Corrected G1 package/results | Paper 1 | Final rerun, ResNet, acceptance. |
| Chương 5 | Traceability framework | G2 schemas/CQ/G3 tests | Paper 2 | Toàn bộ specification/implementation. |
| Chương 6 | Field feasibility | Access, mapping, baseline, QC, scenarios | Paper 3 | Field package chưa đủ. |
| Chương 7 | Inspection-maintenance support | Action/status events + human review | Paper 4/synthesis | Four-level validation chưa có. |
| Chương 8 | Synthesis/conclusion | Cross-layer evidence, không mượn chéo | — | Chỉ viết final claims sau gate sign-off. |

Không có chương FEM riêng. Lab validity không được dùng thay field feasibility; field feasibility không được dùng thay decision validity.

---

# 15. Roadmap nghiên cứu 2026–2029

| Giai đoạn | Mục tiêu | Deliverable | Dependency | Stop/go criterion | Rủi ro |
|---|---|---|---|---|---|
| 1. G1 closure | Tạo evidence tái lập | Full package, rerun, claim table, sign-off | Recover files/code/raw data | GO Paper 1 khi mọi G1 PASS | Leakage, unstable generalization, missing ResNet. |
| 2. G2 specification/literature | Khóa gap và model | Full texts, competitor matrix, 12 artifacts | Có thể song song G1 | GO build sau CQ/schema approval | Post-hoc schema, overclaim. |
| 3. G3 executable lab validation | Chứng minh chain/integrity | DB/fixtures, queries, 12 tests, logs | G2 freeze; G1 payload cho final case | GO khi valid pass/invalid fail/reverse parity | Demo-only implementation. |
| 4. Paper 1 submission | Công bố G1 | Manuscript + reproducibility package | G1 PASS | Submission readiness signed | Metric drift. |
| 5. Paper 2 development/submission | Công bố formal traceability | Benchmark + G3 case | G2/G3 | G6 submission record | “System integration” rejection. |
| 6. Field access/deployment | Chuẩn bị và thu baseline | Agreement, registers, raw/QC package | G4 authorization | GO only if checklist Mục 12 passes | Access/data loss. |
| 7. G4–G5 validation | Field feasibility và human review | Scenarios, inspection/action records | Field data/actors | No field diagnosis; reviewer sign-off | Sparse data, subjective review. |
| 8. Paper 3/4 | Công bố khi evidence đủ | Field paper; optional decision paper | G4/G5 | Merge/defer nếu evidence yếu | Scope overload. |
| 9. Thesis synthesis | Hợp nhất bốn lớp | Chapters, claim matrix, limitations | Gate evidence | Every thesis claim linked to artifact | Cross-layer overclaim. |

Ưu tiên gate-closing artifacts; không ưu tiên thêm giao diện.

---

# 16. Risk register

| Risk | Consequence | Probability | Severity | Early warning | Mitigation |
|---|---|---|---|---|---|
| G1 leakage/unstable generalization | Paper 1 claim sụp | Medium | High | Random split cao, LOCO sub-chance | Group-first pipeline, permutation, external rerun. |
| Sensor mapping không đáng tin | Sensor-config claim sai | Medium | High | Fingerprint multimodal/duplicate assignment | Immutable sensor ID + versioned assignment registry. |
| ResNet1D provenance thiếu | Model comparison không audit được | High | High | Không có channels/checkpoint/code | Audit deadline; nếu fail thì loại model. |
| Paper 2 bị xem là system integration | Rejection | High | High | Manuscript tập trung UI/API | Formal CQ/schema/constraints/failure tests. |
| Novelty overclaim | Mất credibility | Medium | High | Dùng “first/no study” | Corpus-bounded wording và signed competitor matrix. |
| Thiếu full text competitor | Gap bị thu hẹp muộn | High | Medium-high | Claims dựa title/abstract | Acquire three priority full texts trước novelty freeze. |
| Governance conflict | Dev build sai chain | High | High | Action_Status/Action_Record_ID cùng tồn tại | One signed decision + migration map. |
| Demo không có failure tests | Không đóng G3 | High | High | UI đẹp nhưng không validator/log | Test-first fixtures; UI last. |
| Field access delay | Paper 3 trễ | Medium-high | Medium | Không có signed artifact | Parallel preparation; Paper 3 optional. |
| DT terminology challenge | Reviewer coi là database/dashboard | Medium | Medium-high | Không self-define maturity/twinning | C3 definition + evidence of update/provenance/feedback. |
| Zombie FEM | Scope quay lại structural modelling | Medium | High | MAC/calibration/stiffness claims xuất hiện | Mandatory qualifier và keyword audit. |
| Quá tải phạm vi | Không đóng gate nào | High | High | Graph/blockchain/live stream trước schema | Minimal relational/JSON implementation; defer extras. |
| Action_Record/Action_Status chưa thống nhất | Integrity/accountability không xác định | High | High | UI dùng status như identifier | Governance decision trước schema freeze. |
| Repository không tự chứa | Không reproducible | High | High | Chat cards/temporary paths | Copy, hash, commit/tag versioned packages. |
| Field classifier transfer | Scientific overclaim | Medium | High | Lab labels dùng làm field diagnosis | Field feasibility firewall; anomaly -> inspection only. |

---

# 17. Kết luận và hướng ưu tiên

## 17.1. Trả lời trực tiếp

1. **Có đủ cơ sở tiếp tục G2 song song G1 không?** Có. G2 specification, CQ, constraints và literature consolidation độc lập với final G1 metrics; real G3 instance và empirical CEI phải chờ G1 đáng tin cậy.
2. **Khoảng trống đáng khai thác nhất?** Complete constrained component-level evidence-to-inspection/action traceability với pre-registered CQ, invalid-data tests, bidirectional parity và accountability.
3. **Khoảng trống còn yếu?** Cross-scale lab/prototype mapping, mapping confidence, stable GUID qua versions, four-level action logic và universal novelty. **Evidence is currently insufficient.**
4. **Paper 2 định vị thế nào?** Là design-science/formal information model + reproducible evaluation; website chỉ là optional viewer.
5. **G2 khóa gì trước IT?** Vocabulary; action identity/status decision; SCQ/VCQ/RCQ; expected/failure/acceptance; ER/cardinality; metadata schemas; valid/invalid fixtures; version governance.
6. **Khi nào chuyển field?** Khi G1 evidence đủ tin cậy, G2 freeze, G3 lab tests chạy, và field access/identity/assignment/QC/inspection/human-review checklist được duyệt.
7. **Năm việc trong 3–6 tháng:** recover/reproduce G1; rerun corrected multi-seed models và ResNet decision; acquire competitor full texts; freeze G2 CQ/schema; run minimal G3 test pack.

## 17.2. Kết luận theo Claim → Evidence → Limitation → Next action

**Claim ->** Trục luận án evidence -> component -> inspection -> action support phù hợp Quản lý xây dựng và có thể bảo vệ hơn trục AI/FEM.  
**Evidence ->** Literature đã hỗ trợ grouped lab evaluation (Tougui et al., 2021; Matania et al., 2024), BIM-linked records (Kim et al., 2018), GlobalId/CQ (Lorvão Antunes et al., 2024), provenance (Çelik et al., 2022; Lee et al., 2021) và human governance (Johannes et al., 2021); Council/Charter khóa Limited-FEM.  
**Limitation ->** Các building blocks mới chỉ rời rạc; G1 chưa signed; G2 package và G3 tests chưa tồn tại.  
**Next action ->** Đóng G1 reproducibility và G2 specification song song; kiểm chứng G3 trước field.

**Claim ->** Paper 2 có publication potential nếu tránh system-integration framing.  
**Evidence ->** Closest competitor chưa kết hợp complete chain, deliberate failures, reverse parity và accountability (Lorvão Antunes et al., 2024), trong khi các nguồn bổ sung chỉ bao phủ record linkage hoặc provenance từng phần (Kim et al., 2018; Çelik et al., 2022; Lee et al., 2021).  
**Limitation ->** Gap chỉ được xác nhận trong corpus; ba full texts còn thiếu; ontology/GlobalId/CQ không mới.  
**Next action ->** Acquire full texts; benchmark CoDEC; pre-register tests; viết contribution ở mức formal constraints và validation.

**Claim ->** Công trình thực nên là field-feasibility case.  
**Evidence ->** Field literature cho thấy monitoring thực cần kiểm soát environmental/operational variability và không được đồng nhất warning với confirmed damage (Armijo & Zamora-Sánchez, 2024); repository governance cấm diagnosis/transfer.  
**Limitation ->** Access artifact, Rapexco identity, raw field provenance và workflow chưa đủ.  
**Next action ->** Chỉ preparation; deployment khi checklist Mục 12 được phê duyệt.

---

# TÀI LIỆU THAM KHẢO

Chỉ DOI đã được repository kiểm chứng mới được ghi. Quartile/ranking không được xác nhận.

1. Beleites, C., Neugebauer, U., Bocklitz, T., Krafft, C., & Popp, J. (2013). Sample size planning for classification models. *Analytica Chimica Acta, 760*, 25–33. DOI: `10.1016/j.aca.2012.11.007`.
2. Combrisson, E., & Jerbi, K. (2015). Exceeding chance level by chance: The caveat of theoretical chance levels in brain signal classification and statistical assessment of decoding accuracy. *Journal of Neuroscience Methods*. DOI: `10.1016/j.jneumeth.2015.01.010`. [Volume/pages metadata requires verification]
3. Demšar, J. (2006). Statistical comparisons of classifiers over multiple data sets. *Journal of Machine Learning Research, 7*, 1–30. Không ghi DOI vì repository không xác nhận.
4. Ojala, T., & Garriga, G. C. (2010). Permutation tests for studying classifier performance. *Journal of Machine Learning Research, 11*, 1833–1863. Không gắn DOI conference 2009 vào bản journal 2010.
5. Tougui, I., Jilbab, A., & El Mhamdi, J. (2021). Impact of the choice of cross-validation techniques on the results of machine- and deep-learning-based diagnostic applications. *Healthcare Informatics Research, 27*(3), 189–199. DOI: `10.4258/hir.2021.27.3.189`.
6. Matania et al. (2024). Test-training leakage in evaluation of machine learning algorithms for condition-based maintenance. *PHM Society European Conference, 8*(1). DOI: `10.36001/phme.2024.v8i1.4125`. [Author/year metadata requires verification]
7. Wheat et al. (2024). Impact of data leakage in vibration signals used for bearing fault diagnosis. *IEEE Access, 12*, 169883–169892. DOI: `10.1109/ACCESS.2024.3497716`. [Author/year metadata requires verification]
8. Lorvão Antunes, A., Barateiro, J., Marecos, V., Petrović, J., & Cardoso, E. (2024). Ontology-based BIM-AMS integration in European Highways. *Intelligent Systems with Applications, 22*, 200366. DOI: `10.1016/j.iswa.2024.200366`.
9. Kim, K., Kim, H., Kim, W., Kim, C., Kim, J., & Yu, J. (2018). Integration of IFC objects and facility management work information using Semantic Web. *Automation in Construction, 87*, 173–187. DOI: `10.1016/j.autcon.2017.12.019`.
10. Çelik, Y., Petri, I., & Barati, M. (2022). Blockchain supported BIM data provenance for construction projects. *Computers in Industry*. DOI: `10.1016/j.compind.2022.103768`. Repository có xung đột năm 2022/2023; cần reconcile trước submission.
11. Heaton, J., & Parlikad, A. K. (2020). Asset Information Model to support the adoption of a Digital Twin: West Cambridge case study. *IFAC-PapersOnLine, 53*(3), 366–371. DOI: `10.1016/j.ifacol.2020.11.059`.
12. Johannes, K., Voordijk, J. T., Adriaanse, A. M., & Aranda-Mena, G. (2021). Identifying maturity dimensions for smart maintenance management of constructed assets: A multiple case study. *Journal of Construction Engineering and Management, 147*(9), 05021007. DOI: `10.1061/(ASCE)CO.1943-7862.0002112`.
13. Lee, D., Lee, S. H., Masoud, N., Krishnan, M. S., & Li, V. C. (2021). Integrated digital twin and blockchain framework to support accountable information sharing in construction projects. *Automation in Construction, 127*, 103688. DOI: `10.1016/j.autcon.2021.103688`.
14. Du et al. (2024). BIM and IFC Data Readiness for AI Integration in the Construction Industry. *Buildings, 14*(10), 3305. DOI: `10.3390/buildings14103305`. [Author/year metadata requires verification]
15. Keet & Khan. Characterising Competency Questions for Ontologies. [Author/year metadata requires verification]. Không có DOI được repository xác nhận.
16. Armijo, A., & Zamora-Sánchez, D. (2024). Integration of Railway Bridge Structural Health Monitoring into the Internet of Things with a Digital Twin: A Case Study. *Sensors, 24*(7), 2115. DOI: `10.3390/s24072115`.
17. *Earthquake and Ambient Vibration Monitoring of the Steel-Frame UCLA Factor Building* (2006). *Earthquake Spectra*. DOI: `10.1193/1.1946707`. [Author/year metadata requires verification]
18. *Temperature-based structural health monitoring baseline for long-span bridges* (2015). *Engineering Structures*. DOI: `10.1016/j.engstruct.2014.12.042`. [Author/year metadata requires verification]
19. *Dynamic Threshold Cable-Stayed Bridge Health Monitoring System Based on Temperature Effect Correction* (2023). *Sensors*. DOI: `10.3390/s23218826`. [Author/year metadata requires verification]
20. *Long-term health monitoring of concrete and steel bridges under large and missing data by unsupervised meta learning* (2023). *Engineering Structures, 279*, 115616. DOI: `10.1016/j.engstruct.2023.115616`. [Author/year metadata requires verification]
21. *A Low-Cost Wireless Multinode Vibration Monitoring System for Civil Structures* (2023). DOI: `10.1155/2023/5240059`. [Author/year metadata requires verification]

---

# Phụ lục A – Literature evidence matrix

| Citation key | Author, year | Main contribution | Evidence type | Relevance to RQ/Gate | Limitation | Full-text status |
|---|---|---|---|---|---|---|
| L97BIAI3 | Beleites et al., 2013 | Independent units/sample precision | Method | RQ1/G1 | Biomedical/Raman | Complete deep read |
| PZ937I73 | Combrisson & Jerbi, 2015 | Empirical chance in small samples | Method | RQ1/G1 | Không grouped windows | Complete deep read |
| 9XNSNIPX | Demšar, 2006 | Classifier comparison assumptions | Method | RQ1/G1 | Datasets ≠ overlapping folds | Complete deep read |
| ZLFATP2Z | Ojala & Garriga, 2010 | Permutation framework | Method | RQ1/G1 | Parent/PDF version conflict | Complete deep read |
| XE9XS6BQ | Tougui et al., 2021 | Grouped/LOGO CV | Method | RQ1/G1 | Healthcare audio | Complete deep read |
| M8LMWFQH | Matania et al., 2024 | Direct vibration leakage | Direct method | RQ1/G1 | Bearing domain; authors verify | Complete deep read |
| RG9FMT8Y | Wheat et al., 2024 | Group/sensor-position effect | Direct method | RQ1/G1 | Bearing domain; authors verify | Complete deep read |
| XUN8EX6X | Lorvão Antunes et al., 2024 | Sensor/inspection/GlobalId/CQ | Direct competitor | RQ2/G2–G3 | No executed SHACL/action history | Complete deep read |
| VI5QMSAE | Kim et al., 2018 | IFC object–FM record retrieval | Strong adjacent | RQ2/G2 | No sensor/evidence/status chain | Complete deep read |
| EMTIHHX4 | Çelik et al., 2022 | BIM provenance events | Method | RQ2/G2–G3 | Design-stage; year conflict | Complete deep read |
| Lee local PDF | Lee et al., 2021 | Accountable DT information sharing | Strong adjacent | RQ2/G2–G3 | Hypothetical/mock case | Complete local PDF |
| L52SHNEH | Heaton & Parlikad, 2020 | AIM/IFC federation | Strong adjacent | RQ2/G2 | No sensor/inspection chain | Complete deep read |
| YGZ32C8M | Johannes et al., 2021 | Asset-condition-job governance | Strong adjacent | RQ2/WP4/G5 | No four-level workflow | Complete deep read |
| GUEJBZBZ | Du et al., 2024 | IFC/AI readiness review | Background review | RQ2/G2 | No chain validation; authors verify | Complete deep read |
| LSYSC59G | Keet & Khan, verify | CQ taxonomy | Method | RQ2/G2 | Parent metadata incomplete | PDF read; metadata incomplete |
| 3II2WKLN | Wang et al., 2024 | Potential SHACL/ifcOWL method | Metadata/abstract | G3 | No full text | Full text unavailable |
| NUTL57KJ | Bellon et al., 2025 | Potential IFC inspection/maintenance | Metadata/abstract | G2–G3 | No full text | Full text unavailable |
| Z4IBWW9Y | Xu et al., verify | Potential IFC defect/action model | Abstract | G2–G3 | No full text | Full text unavailable |
| XSKNR656 | Armijo & Zamora-Sánchez, 2024 | Field low-cost DT workflow | Field | RQ3/G4 | Normal-condition pilot; no GUID chain | Complete deep read |
| 9823WXJZ | [Author/year metadata requires verification] | Steel-building monitoring precedent | Field | RQ3/G4 | No BIM/inspection/damage confirmation | Complete deep read |
| TRZY4P6X | [Author/year metadata requires verification] | Location-specific baseline | Field | RQ3/G4 | Bridge; no BIM chain | Complete deep read |
| GE3XSAYV | [Author/year metadata requires verification] | Temperature-adjusted thresholds | Field | RQ3/G4 | Missing inspection provenance | Complete deep read |
| D3TGCKXW | [Author/year metadata requires verification] | Missing/environment effects | Field | RQ3/G4 | Secondary data; no provenance | Complete deep read |
| LZPF7ILT | [Author/year metadata requires verification] | Low-cost sensor qualification | Method/lab | RQ3/G4 | No long-term field | Complete deep read |

---

# Phụ lục B – Claim register

| Claim ID | Claim | Supporting studies | Project evidence | Allowed wording | Prohibited wording |
|---|---|---|---|---|---|
| G1-C01 | Run/group là split/inference unit | Beleites; Tougui; Matania; Wheat | G1 addendum/reanalysis | “Đánh giá run-aware là cần thiết” | “Windows là independent samples” |
| G1-C02 | Within-campaign evidence có tín hiệu | Permutation methods | Candidate reanalysis | “Candidate pending G1 closure” | “G1 passed” |
| G1-C03 | Cross-campaign collapse | Methodological support | Candidate LOCO tables | “Observed in provisional pass” | “Universal non-transferability” |
| G1-C04 | Sensor config ảnh hưởng performance | Wheat et al. | Incomplete/affected comparisons | “May materially affect” | “S1/S2 optimal/dominates” |
| G2-C01 | IFC object anchors records | Kim et al. | Local IFC/asset register | “Prior precedent exists” | “Novel sensor-BIM” |
| G2-C02 | CQ links inspection/GlobalId | Antunes et al. | Planned CQ | “Benchmark against CoDEC” | “CQ is novel” |
| G2-C03 | Provenance fields required | Çelik; Lee | ADR/CEI plan | “Minimum provenance fields” | “Blockchain required” |
| G2-C04 | Complete constrained chain gap | Antunes; Kim; Çelik; Lee | No implementation | “Trong phạm vi corpus...” | “No study exists worldwide” |
| G2-C05 | Action/status history needed | Johannes et al.; gap synthesis | ADR conflict | “Project hypothesis/requirement” | “Literature-validated workflow” |
| G3-C01 | Integrity failure testing differentiates contribution | Competitor limitations | Planned tests | “Planned contribution” | “Validated” trước test log |
| G3-C02 | Bidirectional parity | Partial prior queries | No project test | “Candidate validation criterion” | “Round-trip achieved” |
| G4-C01 | Field baseline must account context | Field deep reads | Partial field clues | “Field feasibility requirement” | “Anomaly equals damage” |
| G5-C01 | Human review/accountability needed | Johannes et al. | Proposed scenarios | “Supporting evidence favors...” | “Autonomous maintenance” |

---

# Phụ lục C – Governance conflict list

| Conflict | Files involved | Current authority | Consequence | Required decision |
|---|---|---|---|---|
| Council chain kết thúc `Action_Status`; Charter/ADR dùng `Action_Record_ID` | Council dòng 16/154; ADR Action_ID dòng 5–26; Charter/matrix current | Nhiệm vụ này yêu cầu giữ chain `Action_Status`; repo hierarchy lại xếp Council trên Charter | Dev/schema có thể dùng hai models | Hai thầy ký quyết định cuối; publish one canonical chain + migration map. |
| `Action_Status` vừa là action level vừa có thể là workflow status | ADR dòng 6; demo dòng 74; WP4 addendum dòng 28–35 | Chưa có G2 schema | Trộn recommendation, approval và lifecycle | Quyết định tách `Action_Level`, `Workflow_Status`, status-event hay một vocabulary duy nhất. |
| README v2.2 là operational current nhưng Charter vẫn v2.1 | README v2.2 dòng 5–10, 359–385 | Charter v2.1 | Quy tắc Cam Ranh/cross-scale/fallback ID chưa ratify | Ratify governance v2.2 hoặc relabel README là proposed addendum. |
| Council claim sensor dominance; Charter coi candidate | Council dòng 42; Charter/matrix candidate rules | Charter v2.1 claim control | Overclaim Paper 1 | Ghi Council là preliminary; final claim table sau G1. |
| G1 gate table stale so với reanalysis/canonical reports | Evidence Gates dòng 15–29; later reports | Evidence Gates quyết định closure | Duplicate work hoặc nhầm PASS | Owner cập nhật OPEN/IN-PROGRESS/READY/PASS từng item. |
| Run registry/canonical package được report nhưng file lớn/code vắng | Reanalysis dòng 165–167; canonical README | Gate acceptance requires repository evidence | Không reproducible | Copy package, hash, version, rerun. |
| G2 order khác nhau | Paper 2 yêu cầu CQ trước build; README sequence draft model trước CQ | Charter/Paper 2 | CQ bị post-hoc | Định nghĩa draft vs freeze; CQ/criteria trước formal build. |
| Paper 3/G5 ownership và timing | Charter/matrix/Paper 3/README | Charter/matrix v2.1 | Scope/timing không rõ | Quyết định G5 thuộc P3 hay P4/synthesis; preparation now vs deployment approval. |
| Claim-register lineage đứt | Living Evidence Base dùng C1-01..., addenda bắt đầu C1-12/C2-12 | LEB current | Không audit old claims | Recover old registers hoặc canonical renumber/map. |
| Active old FEM-core guidance ngoài archive | Planning, AI skills, old master index | Charter v2.1 | Agent mở lại zombie FEM | Mark superseded/disable trong một governance task riêng. |
| Supervisor approval vừa “approved” vừa pending written confirmation | Charter/status/Council | Hierarchy không có signed artifact rõ | Decision basis khó audit | Attach written approval hoặc downgrade status. |
| Demo DoD hiển thị Action_Status nhưng bỏ action identity | Demo dòng 65–76, 116–121 | Chưa quyết governance | UI có thể pass nhưng G3 fail | Update handoff sau decision; UI phải phản ánh canonical model. |

---

# Phụ lục D – Missing evidence acquisition list

| Priority | Missing source/evidence | Why needed | Gate/Paper affected | Recommended action |
|---|---|---|---|---|
| 1 | Full canonical G1 package + raw Campaign 2/3 + code | Reproducibility và corrected rerun | G1/P1 | Recover, hash, version, rerun. |
| 2 | ResNet1D provenance | Include/exclude model | G1/P1 | Audit channels/folds/seeds/code/checkpoint; exclude if fail. |
| 3 | Full text `3II2WKLN` | Constraint/SHACL benchmark | G3/P2 | Acquire and deep-read. |
| 4 | Full text `NUTL57KJ` | Inspection/maintenance representation | G2–G3/P2 | Acquire and deep-read. |
| 5 | Full text `Z4IBWW9Y` | Defect/action IFC model | G2–G3/P2 | Acquire and deep-read. |
| 6 | CQ parent metadata | Citation integrity/method | G2/P2 | Create verified parent record. |
| 7 | Signed action/status governance decision | Prevent incompatible schema | G2/G3/P2 | Supervisor decision before freeze. |
| 8 | Second controlled IFC export + diff/GUID test | Version/GUID stability | G2/G3 | Export after controlled edits; hash/diff/review. |
| 9 | Approved G2 package | Prerequisite to IT implementation | G2/P2 | Produce 12 artifacts in Mục 9. |
| 10 | G3 executable fixtures/test logs | Core validation | G3/P2 | Minimal local implementation; one-command tests. |
| 11 | Signed field access/data-use artifact | Field authorization | G4/P3 | Reconcile report contract references with signed file. |
| 12 | Rapexco asset/sensor assignment and raw-data provenance | Field traceability/QC | G4/P3 | Build registers; recover raw data/configs/hashes. |
| 13 | Facility-manager review records | Validate action workflow | G5/P3/P4 | Pre-specify scenarios and review protocol. |
| 14 | Verified journal quartiles | Publication planning only | P1–P3 | Check later using approved ranking source; do not claim now. |
