# Gate 1 - Deep read về context, đơn vị độc lập và phạm vi chuyển giao

**Ngày:** 2026-09-01  
**Trạng thái:** `EVIDENCE RECORD - NEW`; không thay thế và không sửa hồ sơ cũ.  
**Phạm vi:** đúng sáu work do người dùng chỉ định; phục vụ RQ1 / WP1 / Paper 1 / Gate 1 và các claim tương ứng trong Chương 3 của Tiểu luận tổng quan.  
**Ranh giới bất biến:** record này không thay đổi RQ, WP, Paper, Evidence Gate hoặc Limited-FEM; không mở rộng sang field diagnosis, predictive maintenance, RUL, calibrated FEM hoặc automated maintenance. Các thuật ngữ `damage`, `diagnosis`, `maintenance` dưới đây chỉ được ghi khi mô tả đúng phạm vi của nguồn và không được chuyển thành claim của luận án.  
**Quy ước locator:** `PDF p.` là số trang của tệp PDF đã đọc. Với Brake et al. (2019), số trang in của journal được ghi thêm trong ngoặc vuông. Với Ramasso et al., locator là trang của preprint PDF 2024 đã được chấp nhận đăng journal; metadata journal 2025 được kiểm tra riêng.  
**Mã trạng thái:** `AUTHOR-STATED` = tác giả nêu rõ; `READER-INFERRED` = giới hạn rút ra từ thiết kế/báo cáo; `FULLTEXT_DEEP_READ` = đã đọc toàn văn PDF, không dùng abstract thay toàn văn.

## 1. Kiểm soát parent, PDF, version và năm

| Work được tính một lần | Zotero parent và attachment đã đọc | Metadata/version audit | Năm dùng khi trích dẫn | Trạng thái deep-read |
|---|---|---|---|---|
| Ramasso, Teloli & Marcel | Parent `RWHW6F9I`; PDF `DTCZSR4N`, 26 trang | Parent hiện là arXiv `2405.20887`, ngày 2024-05-29, DOI `10.48550/arXiv.2405.20887`. PDF ghi ngày 2024-06-03, arXiv v1 và dòng "accepted in SAGE/SHM journal". Crossref xác nhận cùng title/authors, DOI journal `10.1177/14759217241259668`, online 2024-07-27, print 2025-07, *Structural Health Monitoring* 24(4), 2536-2558. Parent có quan hệ `dc:replaces` tới key không còn truy cập được, nên Zotero relation graph không hoàn chỉnh, nhưng title/authors/nội dung và DOI journal đủ xác nhận đây là preprint-version của bài journal, không phải hai nguồn độc lập. | **2025** cho bài journal; mọi locator trong record ghi rõ **preprint PDF 2024**. | `FULLTEXT_DEEP_READ`; `VERSION_RELATION_VERIFIED`; `PARENT_METADATA_NEEDS_JOURNAL_CROSSWALK` |
| Brake, Schwingshackl & Reuss | Parent `VPFBB9SG`; PDF `67HJW3I7`, 26 trang | Parent và PDF cùng bài journal 2019, DOI `10.1016/j.ymssp.2019.04.020`, *MSSP* 129, 282-307. Không phát hiện preprint-journal conflict. | 2019 | `FULLTEXT_DEEP_READ`; `VERSION_VERIFIED` |
| Amin, Najeh & Ghoul | Parent `6IW2HEFJ`; PDF `SMZRWRG4`, 18 trang | Parent và PDF cùng bài *Scientific Reports* 16, 19546; online 2026-06-23; DOI `10.1038/s41598-026-58967-0`. | 2026 | `FULLTEXT_DEEP_READ`; `VERSION_VERIFIED` |
| Vieira, Bauler, Rosa & Silva | Parent `S2WXRDUS`; PDF `NLVRIAPP`, 33 trang | Parent/PDF là journal 2026, DOI `10.1016/j.ymssp.2026.114640`, *MSSP* 258, 114640; PDF ghi received 2026-03-03, accepted 2026-06-28, online 2026-07-08. arXiv API xác nhận cùng work là `arXiv:2509.22267`, v1 ngày 2025-09-26, v5 ngày 2026-07-06, có `journal_ref` và DOI journal nêu trên. Zotero parent chưa có related-item link, nhưng arXiv metadata xác nhận trực tiếp quan hệ preprint 2025 -> journal 2026. | **2026** cho version journal đã đọc; arXiv 2025 chỉ là version history, không tính nguồn thứ hai. | `FULLTEXT_DEEP_READ`; `VERSION_RELATION_VERIFIED`; `ZOTERO_RELATION_MISSING` |
| da Silva et al. | Parent `IW7JBB3E`; PDF `YZ6YYU2U`, 10 trang | Journal volume/issue tháng 03-2024; DOI `10.1115/1.4063794`. PDF ghi manuscript online 2023-11-23 nhưng issue/copyright là 2024. Đây là online-first 2023 / issue 2024, không phải hai work. | 2024 | `FULLTEXT_DEEP_READ`; `VERSION_VERIFIED` |
| Ozdagli & Koutsoukos | Parent `WMBQRXFF`; PDF `E6RJLBT4`, 9 trang | Proceedings *Annual Conference of the PHM Society* 12(1), 2020; DOI `10.36001/phmconf.2020.v12i1.1184`. Không phát hiện version conflict. | 2020 | `FULLTEXT_DEEP_READ`; `VERSION_VERIFIED` |

**Quyết định kiểm soát version:** corpus có đúng sáu work. Ramasso preprint/journal và Vieira arXiv/journal đều được đếm một lần. Không trộn năm preprint với năm citation journal và không gán locator journal cho trang preprint.

## 2. Ramasso, Teloli & Marcel (journal 2025; preprint PDF 2024) - `RWHW6F9I`

**Vai trò bằng chứng:** trực tiếp nhất trong sáu nguồn đối với bolted-joint condition monitoring qua nhiều campaign; không phải steel frame và dùng acoustic emission (AE), không phải acceleration-based frame vibration.

| Thành phần | Đọc sâu và đánh giá | Locator |
|---|---|---|
| Vấn đề | Hiệu năng rất cao khi train/test trong cùng campaign không trả lời khả năng khái quát sang campaign mới. Với liên kết bu lông, tháo-lắp lại làm thay đổi micro-contact, contact pressure và AE patterns dù hình học tổng thể không đổi. Tác giả tách rõ `NO-SHM` (cùng campaign) với `SHM` (unseen campaign). | Preprint PDF 2024 pp. 2-5, Introduction và Section 2.2; pp. 12-15, Sections 4-5.1, Tables 7-8. |
| Phương pháp/framework | ORION-AE: AE stream được phân đoạn theo vibration cycles từ laser vibrometer; Hanning window; CWT scalograms 224 x 224; transfer learning với GoogLeNet, ResNet18, MobileNetV2, EfficientNetB5; so sánh frozen/fine-tuned layers, denoising, single sensor/sensor fusion, ordinal losses và 1cycle scheduler. SHM evaluation giữ lại toàn bộ một campaign để test và train trên bốn campaign còn lại. | pp. 3-8, Sections 2-3, Figs. 1-7; pp. 13-19, Sections 5-6, Figs. 8-13, Tables 8-9. |
| Đơn vị phân tích | Đơn vị vật lý cao nhất có ý nghĩa cho claim transfer là **measurement campaign sau complete disassembly/reassembly**; có 5 campaign B-F. Cấp thấp là khoảng 1,200 vibration cycles mỗi torque level, tạo khoảng 8,400 images/campaign/sensor. Các cycle/image không phải 8,400 đơn vị vật lý độc lập. | p. 4, Section 2.1; pp. 5-8, Sections 2.2-3.2; p. 19, Table 9. |
| Thiết kế kiểm chứng | Hai tầng: cùng-campaign train/validation/test 80/10/10 (`NO-SHM`) và leave-one-campaign-as-test (`SHM`). Phần prior-information thêm dần nhãn của campaign đích; phần super-convergence lặp 5 lần cho mỗi cấu hình và báo cáo độ phân tán. Đây là campaign-holdout thực, nhưng không phải LORO trong campaign và không phải field/site holdout. | pp. 12-16, Sections 4-6.1, Tables 1-8, Fig. 8; pp. 18-22, Sections 6.2-6.3, Table 9, Appendix Table 10. |
| Kết quả chính | Cùng campaign đạt trên 99%, nhưng baseline unseen campaign B chỉ khoảng `ACC+/-1` 52.2-65.9% khi fine-tune và thấp hơn khi freeze. Cấu hình tốt tăng campaign B lên khoảng 79%; leave-one-campaign results với EfficientNetB5 + POM1b là `ACC+/-1` 78.8, 86.4, 86.3, 78.8 và 86.1% cho B-F. Single mu80 sensor đủ; sensor fusion không cải thiện; pre-denoising có thể giảm hiệu năng. | pp. 13-15, Tables 2-8; pp. 16-21, Figs. 9-13, Table 9; p. 21, Section 7. |
| Limitation | `AUTHOR-STATED`: torque ground truth không đủ tin cậy do vị trí analog torque wrench; coi sai một adjacent class là đúng có thể không phù hợp một số ứng dụng. `READER-INFERRED`: chỉ 5 campaign của một ORION-AE test bench; metric chính `ACC+/-1` nới lỏng ground truth; hàng nghìn cycles không tăng số campaign độc lập; lựa chọn cấu hình tập trung nhiều vào campaign B trước khi áp sang các campaign khác; không có external structure/site test. | p. 14, Section 5; p. 21, Section 7; pp. 19-22, Table 9 và Appendix Table 10. |
| Future work | Mã hóa uncertainty của labels vào deep networks; khảo sát cảm biến có dải tần cao hơn để tăng generalization. | p. 21, Section 7. |
| Claim boundary | Được phép nói: campaign/reassembly holdout làm giảm mạnh hiệu năng so với same-campaign split và chứng minh transfer scope phải được báo cáo. Không được nói: paper chứng minh transfer tới steel frame, công trình thực, site mới, field diagnosis, hoặc rằng 78.8-86.4% là exact torque accuracy; đây là `ACC+/-1` trên 5 campaign của aluminum bolted-beam AE benchmark. | pp. 4-5, Sections 2.1-2.2; pp. 19-21, Table 9 và Section 7. |

**Verdict:** `DIRECT / STRONGLY STRENGTHENS CONTEXT-AND-TRANSFER AXIS`. Nguồn này chặn mọi claim rộng rằng bolted-joint literature chưa có campaign/reassembly holdout. Nó chưa đóng Gap 1 vì khác asset class, sensing modality và không thực hiện đồng thời run-level leakage control trên steel bolted frame.

## 3. Brake, Schwingshackl & Reuss (2019) - `VPFBB9SG`

**Vai trò bằng chứng:** cơ học/thí nghiệm nền cho lý do campaign/reassembly là nguồn biến thiên thật, không phải quy ước chia dữ liệu tùy ý.

| Thành phần | Đọc sâu và đánh giá | Locator |
|---|---|---|
| Vấn đề | Trong jointed structures, uncertainty do part-to-part variability và measurement/assembly repeatability có thể lớn hơn nonlinear effect cần đo. Nếu setup, interface và assembly không được kiểm soát, biến thiên đo được trộn experimental error với joint behavior. | PDF pp. 1-5 [journal pp. 282-286], Sections 1-3.2, Figs. 1-4. |
| Phương pháp/framework | Chương trình thí nghiệm bốn năm trên Brake-Reuss beam, tích hợp tribology, contact mechanics và nonlinear dynamics. So sánh ba assembly/testing procedures; thay đổi roughness, settling/wear, meso- và macro-interface geometry, cùng far-field structure; shaker hoặc impact hammer; FRF, Hilbert-transform ringdown, amplitude-dependent frequency và damping. | pp. 2-3 [283-284], Section 2; pp. 3-13 [284-294], Sections 3-5; pp. 14-24 [295-305], Sections 6-9. |
| Đơn vị phân tích | Tùy thí nghiệm: một specimen/beam pair; một complete assembly; một impact measurement. Ví dụ thiết kế chuẩn có 3 assemblies x 3 impact levels x 5 repetitions = 45 measurements. `Variability` là khác biệt giữa nominally identical parts; `repeatability` là khác biệt giữa phép đo/assembly của cùng parts. | p. 1 [282], Section 1; p. 10 [291], Section 3.4, Fig. 10; p. 17 [298], Section 6.4, Fig. 17. |
| Thiết kế kiểm chứng | So sánh Procedure 1-3 dưới torque/roughness/fixturing kiểm soát; đo maximum difference của natural frequencies; kiểm tra wear bằng visual inspection và permanent frequency shift; so sánh interface geometries và contact-pressure measurements. Không có ML split/CV. | pp. 6-12 [287-293], Sections 3.2-4, Figs. 6-12, Table 1; pp. 17-20 [298-301], Figs. 17-22, Table 2. |
| Kết quả chính | Chuẩn hóa alignment/tightening giảm first-mode frequency variation từ 5.6% xuống 0.063% với shaker, gần hai orders of magnitude. Rough interface kém repeatable hơn smooth interface. Variation khoảng 0.06% qua 3 assemblies ở setup tốt, trong khi excitation-induced shift 1.25%; ở setup kém, variability có thể lớn hơn effect cần đo. Wear gây permanent frequency shifts. Interface contact pressure và far-field modal loading thay đổi apparent joint dynamics. | pp. 7-13 [288-294], Figs. 7-13, Table 1; pp. 22-24 [303-305], Sections 8-9. |
| Limitation | `AUTHOR-STATED`: nhiều specimen đầu kỳ không còn để follow-up và lấp data gaps; một số nhận định đầu kỳ chỉ là general observations. Cách cố ý đưa uncertainty vào stochastic model mới chỉ được chứng minh trên một class of joints. `READER-INFERRED`: nhiều thí nghiệm con ghép trong bốn năm với specimen/setup thay đổi; đây không phải prevalence study và không cho một variance component model thống nhất cho mọi source. | p. 2 [283], cuối Section 1; p. 8 [289], Section 3.2.3; p. 24 [305], Section 9. |
| Future work | Tác giả yêu cầu further testing cho Repeatability Hypothesis; đề xuất nghiên cứu polymer/elastomer gaskets trong ứng dụng cần sealing. | p. 11 [292], Section 3.4; p. 24 [305], Section 8. |
| Claim boundary | Được phép nói: assembly, alignment, roughness, wear và contact state có thể làm response thay đổi giữa lần lắp/đợt đo và phải được coi là context/provenance. Không được dùng paper như bằng chứng về ML generalization, data leakage, steel-frame classification hoặc định lượng trực tiếp expected LOCO drop của luận án. | pp. 22-24 [303-305], Sections 8-9. |

**Verdict:** `DIRECT-MECHANISTIC / SUPPORTS CAMPAIGN AS PHYSICAL UNIT`. Nguồn củng cố mạnh Chương 3 Sections 3.3.1 và 3.3.3, nhưng không tự xác lập giao thức grouped evaluation.

## 4. Amin, Najeh & Ghoul (2026) - `6IW2HEFJ`

**Vai trò bằng chứng:** methodological implementation gần nhất cho pipeline order và event-level grouping trên vibration data; asset là railway switch/crossing, không phải steel bolted frame.

| Thành phần | Đọc sâu và đánh giá | Locator |
|---|---|---|
| Vấn đề | Accuracy của vibration-event classifier có thể bị thổi phồng nếu feature selection, augmentation hoặc normalization dùng toàn dataset, hoặc ba correlated measurements của cùng physical event bị chia sang train/test. | PDF pp. 1-2, Introduction và contributions. |
| Phương pháp/framework | Full-scale outdoor S&C test facility nhưng controlled-laboratory; 3 accelerometers theo x/y/z; tín hiệu chia thành 1 s; 16 time/frequency features; pipeline `split -> select -> augment -> standardize -> train -> evaluate`; autoencoder augmentation; benchmark 21 classifiers/8 families. | pp. 2-8, Experimental set-up and methods, Figs. 1-6, Tables 1-3. |
| Đơn vị phân tích | Cấp mẫu mô hình là một segment 1 s từ một axis. Cấp grouping là **physical event 1 s**, đồng thời được ba accelerometer axes ghi lại. Tổng 801 axis-segments = 267 grouped events. Bài không group toàn bộ bogie traversal/session; vì vậy event ở đây thấp hơn run/campaign của luận án. | pp. 5-6, Feature engineering và Evaluation pipeline; p. 8, Dataset characteristics, Table 3. |
| Thiết kế kiểm chứng | Event-level 80/20 held-out split trước data-dependent transformations; MI, autoencoder và augmentation chỉ fit trên training; scaler fit trên augmented training; top models dùng stratified group-aware 5-fold CV và standardization trong từng fold. | p. 6, Evaluation pipeline Steps 1-8; pp. 8-13, Results và Table 7/Fig. 12. |
| Kết quả chính | Top held-out accuracy 81.5%, ROC-AUC khoảng 0.94. Group-aware CV: Bagging 80.4% +/- 2.1%, XGBoost và Gradient Boosting 80.2% +/- 2.4%. Crossing chỉ 6 held-out samples, recall CI rất rộng. Augmentation effect nhỏ và model-dependent; standardization quyết định convergence của scale-sensitive models. | pp. 8-13, Tables 3-7, Figs. 7-13. |
| Limitation | `AUTHOR-STATED`: một controlled facility, artificial defects, 267 events, crossing under-represented; chưa có operational infrastructure validation; joint/squat confusion còn cao. `READER-INFERRED`: grouping không lên tới full traversal, day, campaign hoặc physical S&C specimen; bài chỉ nói standardization fold-local trong CV, không mô tả rõ autoencoder/augmentation có được refit hoàn toàn trong từng fold hay không. | pp. 15-16, Discussion, Limitations và Conclusions; p. 6, Step 8. |
| Future work | Mở rộng dataset/classes; operational railway validation; transfer learning cho cross-site generalization; temporal sequence modelling. | p. 16, Conclusions/Future work. |
| Claim boundary | Được phép kế thừa thứ tự pipeline và nguyên tắc group correlated multi-axis measurements. Không được gọi event-level grouping này là run-/campaign-independent evaluation; không chuyển accuracy railway sang steel frame; không dùng deployment discussion để mở rộng luận án sang automated maintenance hoặc field diagnosis. | pp. 6, 15-16. |

**Verdict:** `METHODOLOGICAL / CLOSES EVENT-LEVEL PIPELINE PRECEDENT, NOT RUN-LEVEL TRANSFER`. Nguồn thu hẹp novelty của split-first/train-only processing, nhưng đồng thời cho thấy cần khai báo rõ hierarchy `axis-segment -> event -> traversal/run -> session/campaign`.

## 5. Vieira et al. (journal 2026; arXiv 2025) - `S2WXRDUS`

**Vai trò bằng chứng:** bằng chứng phương pháp mạnh nhất trong sáu nguồn về leakage cấp physical component và tác động nhân quả của split, nhưng ngoài asset/application của luận án.

| Thành phần | Đọc sâu và đánh giá | Locator |
|---|---|---|
| Vấn đề | Segment-wise, repetition-wise và condition-wise splits vẫn có thể đưa dữ liệu của cùng physical bearing vào train/test, để model ghi nhớ identity artifacts. So sánh naive và bearing-wise splits thường bị confound vì đồng thời giảm số training bearings; paper thiết kế thí nghiệm cố định trained model và chỉ đổi test set. | Journal PDF pp. 1-3, Introduction; pp. 5-8, Sections 3.1-3.4. |
| Phương pháp/framework | Strict bearing-wise split; multi-label binary classification + ROC/Macro AUROC; double CV cho model selection/performance estimation; WDCNN và shallow RF/SVM; four datasets CWRU, PU, UORED-VAFCLS, HUST; augmentation chỉ training; controlled leakage experiments trên synthetic và real data. | pp. 8-16, Section 4, Figs. 2-8, Tables 2-6; pp. 20-24, Section 6, Tables 11-13. |
| Đơn vị phân tích | Đơn vị suy luận là **unique physical bearing/component**, không phải 1 s segment, recording repetition hoặc operating condition. Paper còn phân biệt số signals với số `[bearing, health-state]` instances. | pp. 8-15, Sections 4.1.1-4.2.4, Figs. 2-7, Table 4. |
| Thiết kế kiểm chứng | Bearing-disjoint train/test; hyperparameter-tuning splits tách khỏi evaluation split configurations; 100 evaluation splits. Quan trọng nhất, Section 6 giữ training set/model cố định, thay test composition thành no-leakage, bearing-level leakage, repetition-level leakage hoặc segmentation leakage; dùng paired one-tailed tests. | pp. 10-14, Sections 4.1.3-4.2.3; pp. 20-24, Section 6, Tables 11-13. |
| Kết quả chính | UORED: segmentation leakage đẩy Macro AUROC khoảng 87-90% lên gần 100%; bearing leakage tăng 3.0-6.4 points. PU: no-leakage 54.25/61.25/76.98%, condition leakage 86.88/92.27/87.79%, repetition và segmentation gần 99-100%. CWRU: no-leakage khoảng 63-64%, condition/segmentation leakage gần 100%. Tăng số distinct training bearings cải thiện generalization dù total sample exposure được giữ gần bằng nhau. Leakage có thể đảo model/input ranking, không chỉ thổi phồng metric. | pp. 17-20, Figs. 9-14, Tables 8-10; pp. 21-25, Tables 11-13, Figs. 15-16. |
| Limitation | `AUTHOR-STATED/ADMITTED`: computational budget giới hạn model space; CWRU có cấu trúc khó tạo clean split; trong generic CV description, một số data dùng ở performance stage có thể đã xuất hiện trong hyperparameter tuning và tác giả cho rằng nhiều splits làm loãng ảnh hưởng, nên đây không phải final untouched external test. `READER-INFERRED`: nhiều repeated split estimates không tạo thêm physical bearings; t-test trên repeated splits có thể không hoàn toàn độc lập; claim về bearing diagnosis không chuyển trực tiếp sang steel-frame dynamics. | p. 10, Section 4.1.3; pp. 24-26, Sections 7-9. |
| Future work | Không có mục future-work riêng; recommendations yêu cầu datasets hỗ trợ physical-component split, rõ model selection, chia sẻ code/splits/pipeline và thử nhiều dataset/diversity configurations. Deployment section đề xuất sensor-group/machine-wise split khi bearing ID không có. Với luận án, đây chỉ là hướng phương pháp, không phải mở rộng sang diagnosis/deployment. | pp. 26-27, Sections 8-9. |
| Claim boundary | Được phép chuyển nguyên tắc: group ở cấp vật thể vật lý cao nhất liên quan deployment và kiểm soát training diversity khi so splits. Không được chuyển numerical AUROC drops sang steel frames; không được coi bearing-wise là luôn tương đương run-wise; không dùng multi-label diagnosis làm hướng của luận án. | pp. 5-8, Sections 3.1-3.4; pp. 24-26, Sections 7-9. |

**Verdict:** `METHODOLOGICAL / STRONGLY STRENGTHENS PHYSICAL-UNIT AND LEAKAGE CLAIMS`. Nguồn này làm rõ rằng split theo condition/run thấp hơn physical object vẫn có thể rò rỉ; đối với WP1, group level phải được chọn theo claim transfer cụ thể, không mặc định window hoặc event là đủ.

## 6. da Silva et al. (2024) - `IW7JBB3E`

**Vai trò bằng chứng:** trực tiếp cho transfer giữa nominally similar bolted-joint specimens; đồng thời cho thấy source choice và target context chi phối kết quả.

| Thành phần | Đọc sâu và đánh giá | Locator |
|---|---|---|
| Vấn đề | GMM học trên một bolted beam hoạt động tốt trong source nhưng thất bại trên beam tương tự khác do feature distributions khác nhau; retraining target tốn dữ liệu. | PDF pp. 1-2, Introduction; p. 4, Section 4, Figs. 5-8. |
| Phương pháp/framework | Bốn Orion beams: ba flat-patch nominally same, Beam 4 flat-flat contact; white-noise shaker; base accelerometer + laser vibrometer; modal frequencies khoảng 700/1900 Hz; healthy GMM + Mahalanobis/chi-square threshold; z-score; Transfer Component Analysis (TCA) map source-target từ 3D xuống 2D latent space; thử các source-target combinations. | pp. 2-5, Sections 2-4, Figs. 1-5; pp. 7-10, Figs. 8-13. |
| Đơn vị phân tích | Asset/domain unit là một physical beam/specimen. Dữ liệu mỗi beam gồm 8 sets x 16 measurements sau complete assembly/disassembly, trên các ngày khác nhau, tổng 128 realizations mỗi torque level. Tuy nhiên paper báo cáo chủ yếu ở observation level và không đưa fold/campaign registry. | p. 3, Section 3.1; pp. 4-5, Section 4 và Table 1. |
| Thiết kế kiểm chứng | Source GMM dùng 70% healthy (448), validation healthy 30% (192), damaged validation 128 tại 25 cN m. Classifier source được áp thẳng target để cho thấy failure, sau đó TCA kết hợp source với unlabeled target data và đánh giá bằng target labels; Figure 13 đối chiếu mọi source-target ở torque 25/20/15 cN m. Đây là **transductive domain adaptation**, không phải untouched-target holdout. | pp. 4-5, Section 4, Figs. 5-8; pp. 7-10, Figs. 9-13, Table 1. |
| Kết quả chính | Source-only Beam 2 có FPR 1.9%, FNR 0 nhưng thất bại trên Beam 1 original space. Sau TCA, Beam 2 -> Beam 1 ở 25 cN m cho target FPR 0.3%, FNR 0; tuy nhiên source choice quyết định mạnh: Beam 2 tốt nhất, Beam 1/4 làm source có false alarms cao; Beam 1 có wear marks và Beam 4 khác contact interface. | pp. 4-5, Figs. 6-12; pp. 9-10, Fig. 13 và Final Remarks. |
| Limitation | `AUTHOR-STATED`: performance phụ thuộc source database; TCA one-to-one, source kết hợp với target ở chỉ một tightening torque mỗi case; compression có thể làm mất thông tin; data dispersion/contact interface ảnh hưởng classifier. `READER-INFERRED`: không có run-/campaign-grouped holdout, không có train-only normalization audit (chỉ nói z-score trên "all data sets"), không có untouched external target, không báo uncertainty across 8 assembly sets; safe/unsafe threshold và damage language là study-specific. | pp. 5, 9-10, Section 4 và Final Remarks. |
| Future work | Không nêu chương trình future work tường minh. Tác giả chỉ gợi ý classifier phù hợp hơn cho từng data core có thể cải thiện performance; data chỉ cung cấp on request. | pp. 9-10, Section 4/Final Remarks/Data availability. |
| Claim boundary | Được phép nói source-trained classifier không mặc nhiên hợp lệ cho specimen khác và adaptation success phụ thuộc source/target context. Không được nói TCA chứng minh out-of-sample transfer tới unseen asset/campaign, vì target distribution được dùng để fit adaptation; không chuyển safe/damaged labels thành condition evidence của luận án. | pp. 5, 9-10. |

**Verdict:** `DIRECT / SUPPORTS CROSS-SPECIMEN SHIFT, PARTIAL VALIDATION`. Nguồn tăng sức nặng cho requirement báo cáo source/target provenance nhưng không đóng leakage-controlled transfer scope.

## 7. Ozdagli & Koutsoukos (2020) - `WMBQRXFF`

**Vai trò bằng chứng:** tiền lệ domain-adversarial adaptation và source-target distribution shift; chất lượng evaluation cho claim independent generalization bị giới hạn bởi windowing/split design.

| Thành phần | Đọc sâu và đánh giá | Locator |
|---|---|---|
| Vấn đề | Supervised classifier giả định source/test cùng phân phối, trong khi operating load hoặc representation-to-experiment tạo domain shift; source-only model có thể thất bại trên target. | PDF pp. 1-3, Introduction và Section 2. |
| Phương pháp/framework | Domain-Adversarial Neural Network (DANN) gồm feature extractor, label predictor và domain classifier qua gradient reversal, tối thiểu H-divergence. Case 1: gearbox low-load source/high-load target; Case 2: small three-story numerical source/experimental target. So sánh source-only, DANN và TCA ở Case 1. | pp. 2-5, Sections 1-3.1.2, Figs. 1-3; pp. 6-7, Sections 3.1.3-4, Tables 1-3. |
| Đơn vị phân tích | Cấp mô hình là STFT window: 1,000 samples, 80% overlap, khoảng 2,700 windows/condition từ hai recordings khoảng 4 s ở gearbox; structural case cũng tạo 2,100 windows/condition. Physical recording/specimen không được dùng làm grouping unit trong split. | p. 5, Section 3.1.1; p. 6, Section 3.2.1. |
| Thiết kế kiểm chứng | Source và target đều split 4:1 sau khi tạo overlapping windows; DANN dùng unlabeled target-training windows; target test accuracy so với source-only. Paper không báo recording-wise grouping, seeds, interval hoặc external target. Structural case nằm ngoài Limited-FEM scope của record và chỉ được ghi như một case của paper, không được route vào luận án. | pp. 5-7, Sections 3.1-3.3, Tables 1-3. |
| Kết quả chính | Gearbox target accuracy tăng 64.29% -> 71.79% với DANN; TCA target 42.55%. Structural target tăng 36.11% -> 63.08%. Các kết quả chứng minh adaptation có thể cải thiện target-window accuracy trong hai datasets đã thấy, không chứng minh unseen-run/campaign transfer. | pp. 6-7, Tables 1 và 3, Section 3.3. |
| Limitation | `AUTHOR-STATED`: TCA chỉ dùng 1/4 training samples vì memory; classifier SVM có thể không phù hợp; chỉ dense networks. `READER-INFERRED`: 80%-overlap windows và random 4:1 split có nguy cơ near-duplicate/recording leakage; target data tham gia adaptation; không có run-aware split; không có uncertainty; nên accuracy không đủ làm bằng chứng independent transfer. | pp. 5-7, Sections 3.1.1-3.3. |
| Future work | Khai thác limited labeled normal target data; thử convolutional architectures và các GAN-based adaptation strategies. | p. 7, Conclusion. |
| Claim boundary | Chỉ được dùng cho khái niệm domain shift và tiền lệ DANN. Không được dùng làm bằng chứng rằng domain adaptation đã giải quyết transfer scope, không dùng structural numerical case để mở rộng sang calibrated FEM/damage diagnosis, và không dùng target accuracy như run-independent validation. | pp. 3-7. |

**Verdict:** `METHODOLOGICAL BACKGROUND / VALIDATION-CAUTION`. Nguồn củng cố sự tồn tại của distribution shift nhưng, khi đọc toàn văn, không đủ mạnh để hỗ trợ claim về independent transfer evaluation.

## 8. Tổng hợp chéo sáu nguồn

### 8.1 Chuỗi logic đã được xác minh

1. **Context thay đổi response thật:** Brake cho thấy assembly/alignment/roughness/wear/contact pressure có thể tạo variation lớn hơn effect cần đo; Ramasso quan sát campaign sau reassembly như một heterogeneous system; da Silva cho thấy nominally similar beams có distributions khác và source choice quyết định performance.
2. **Đơn vị chia phải theo claim:** Amin group ba axes theo physical event, nhưng chỉ ở cấp 1 s; Vieira chứng minh cần nâng grouping lên physical component nếu claim là unseen-component generalization; Ramasso nâng lên campaign nếu claim là unseen-reassembly generalization.
3. **Pipeline order là prior art:** Amin triển khai split trước select/augment/standardize; Vieira fit augmentation trên training và tách physical components; đây không còn là novelty method.
4. **Transfer không đồng nghĩa adaptation success:** da Silva và Ozdagli dùng target data trong adaptation, nên kết quả là transductive target adaptation; Ramasso có campaign holdout thật nhưng chỉ 5 campaigns và metric chấp nhận adjacent class do label uncertainty.
5. **Cỡ mẫu biểu kiến không phải cỡ mẫu độc lập:** Ramasso có khoảng 42,000 images/sensor nhưng 5 campaigns; Amin có 801 segments nhưng 267 events; Vieira cho thấy hàng trăm/hàng nghìn segments không thay thế distinct bearings; Brake phân biệt measurement repeatability với part-to-part variability.

### 8.2 Ma trận mức gần Gap 1

| Source | Đúng bolted joint | Đúng steel frame | Physical-unit grouping | Train-only/leakage control | Run/session/campaign transfer | Effect lên Gap 1 |
|---|---:|---:|---|---|---|---|
| Ramasso 2025 / PDF 2024 | YES | NO - aluminum two-beam ORION | YES ở campaign; cycles không độc lập | PARTIAL - campaign test độc lập, nhưng within-training hierarchy không audit đầy đủ | **YES - leave-one-campaign test** | Closest transfer/context competitor; buộc thu hẹp gap về đúng asset/modality và conjunction |
| Brake 2019 | YES | NO - stainless lap-joint beam | YES - part/assembly/measurement được phân biệt | n/a | Mechanistic evidence, không ML holdout | Củng cố lý do cần campaign provenance, không đóng protocol gap |
| Amin 2026 | NO | NO | YES ở event 1 s; NO ở traversal/session | **YES ở held-out pipeline; CV augmentation nesting chưa đủ rõ** | NO | Đóng novelty của event grouping + train-only pipeline, không đóng run/campaign gap |
| Vieira 2026 | NO | NO | **YES ở physical component** | **YES, có controlled leakage experiments** | Component/dataset transfer only, không bolted campaign | Đóng novelty phương pháp và cho evidence định lượng mạnh ngoài lĩnh vực |
| da Silva 2024 | YES | NO - aluminum beams | PARTIAL - specimen/campaign có nhưng split registry không báo | NOT REPORTED; normalization wording không đủ | PARTIAL - cross-specimen transductive adaptation | Chứng minh source-target shift trực tiếp, không đóng independent transfer |
| Ozdagli 2020 | NO cho case chính; structural case ngoài route | NO | NO - overlapping windows | NO/NOT REPORTED ở recording level | PARTIAL - transductive domain adaptation | Background only; không đủ làm validation precedent |

## 9. Chapter update implications

Phần này chỉ nêu implication đối với **Chương 3 của Tiểu luận tổng quan** hiện hành; không tự sửa Chương 3.

### 9.1 Claim được củng cố

| Claim hiện hành | Trạng thái sau deep-read | Bằng chứng và cách dùng chính xác |
|---|---|---|
| Section 3.3.1: dữ liệu có hierarchy và unit cao hơn window/segment mới phù hợp cho inference | **CỦNG CỐ MẠNH** | Amin: 3 axis-segments phải ở cùng physical event (pp. 5-8). Vieira: condition/repetition split vẫn leak nếu cùng bearing (pp. 5-8, 20-24). Ramasso: campaign sau reassembly là unit transfer (pp. 4-5, 13-21). |
| Section 3.3.2: data-dependent transformations phải học từ training only | **CỦNG CỐ TRỰC TIẾP** | Amin triển khai split -> select -> augment -> standardize và fit scaler/training augmentation đúng phía (p. 6). Vieira áp augmentation riêng training và controlled leakage comparisons (pp. 15, 20-24). |
| Section 3.3.3: assembly/reassembly làm phạm vi transfer giữa campaign khắt khe hơn within-campaign | **CỦNG CỐ TRỰC TIẾP, KHÔNG CHỈ SUY LUẬN** | Brake định lượng setup/assembly effect (pp. 6-13, Table 1); Ramasso giữ lại campaign đã tháo-lắp lại và thấy same-campaign >99% nhưng unseen-campaign chỉ 78.8-86.4% theo `ACC+/-1` ở cấu hình tốt (pp. 13-21, Tables 8-9). |
| Section 3.4: condition evidence phải mang source context và validated scope | **CỦNG CỐ** | Source identity/campaign/specimen làm thay đổi kết quả trong Ramasso, Brake và da Silva; physical-component identity làm thay đổi leakage/generalization trong Vieira. Đây là rationale cho provenance/scope, không phải evidence rằng schema của luận án đã được validation. |
| Section 3.2.3: model ranking không đáng tin nếu protocol sai | **CỦNG CỐ ĐỊNH LƯỢNG NGOÀI ASSET** | Vieira cho thấy leakage không chỉ tăng AUROC mà làm các input representations hội tụ gần 100% và có thể đảo kết luận model/input (pp. 21-25, Tables 11-13). Amin cho thấy single split và grouped CV đổi ranking/stability (pp. 10-16, Table 7). |

### 9.2 Claim phải thu hẹp hoặc sửa câu

| Claim/cách viết hiện hành | Điều chỉnh bắt buộc |
|---|---|
| Section 3.3.3/3.5: "phép giữ lại theo đợt thí nghiệm gần như vắng mặt" | Chỉ được giữ nếu viết rõ: **trong subset steel-frame vibration studies đã rà soát**. Không được áp cho bolted-joint condition-monitoring literature nói chung, vì Ramasso thực hiện unseen-campaign holdout sau complete disassembly/reassembly. |
| Section 3.3.2: grouped evaluation có thể được mô tả như một giải pháp đơn tầng | Phải bổ sung hierarchy: Amin giải quyết correlation giữa axes cùng event nhưng không giữ toàn traversal/session; Vieira cho thấy condition/run thấp hơn physical component vẫn leak. Group level phải khớp với claim, không chỉ dùng `GroupKFold` là đủ. |
| Section 3.3.3: domain adaptation "cải thiện nhưng không xóa hết khoảng cách" | Giữ ở mức dataset-specific. da Silva và Ozdagli là transductive adaptation vì target distribution tham gia training; chúng không chứng minh generalization tới unseen target. Ramasso mới là independent campaign test, nhưng chỉ 5 campaigns và dùng `ACC+/-1`. |
| Section 3.5: gap có thể dựa trên thiếu transfer evaluation trong bolted joints | Phải bỏ nền này. Transfer/campaign evaluation đã có ở bolted-beam AE và cross-specimen adaptation đã có ở bolted beams. Gap chỉ còn ở **simultaneous qualification trên steel bolted frame vibration data** với physical run unit, leakage control và explicit run/session/campaign transfer scope. |
| Section 3.4: mọi context field đều đã được nguồn chứng minh là đủ | Không được. Sáu nguồn chỉ chứng minh các field như campaign, assembly, source specimen, sensor/event identity là cần để diễn giải; chúng không validation danh mục năm nhóm metadata của luận án là đầy đủ. |

### 9.3 Claim không được phép

- **Không được phép:** "Chưa có nghiên cứu bolted-joint nào đánh giá unseen campaign/reassembly." Ramasso chặn claim này.
- **Không được phép:** "Event-wise split đồng nghĩa run-wise hoặc campaign-wise independence." Amin chỉ group ba axes của event 1 s; higher-level traversal/session vẫn chưa được giữ lại.
- **Không được phép:** "Domain adaptation chứng minh model chuyển được sang asset/site mới." da Silva và Ozdagli dùng target data để fit adaptation; đó là transductive adaptation trên target đã thấy.
- **Không được phép:** "Same-campaign accuracy trên 99% là SHM generalization." Ramasso gọi rõ đây là `NO-SHM` case.
- **Không được phép:** dùng `ACC+/-1` 78.8-86.4% của Ramasso như exact seven-level torque accuracy hoặc chuyển sang expected WP1 performance.
- **Không được phép:** chuyển AUROC inflation của Vieira, event accuracy của Amin hoặc setup variation của Brake thành effect size dự kiến cho steel frame của luận án.
- **Không được phép:** dùng six-source record để tuyên bố novelty cho grouped CV, split-before-windowing, train-only preprocessing, domain adaptation hoặc cross-campaign holdout; các phương pháp/tiền lệ này đã tồn tại.
- **Không được phép:** route Ozdagli structural case hoặc ngôn ngữ `damage/diagnosis` của các nguồn thành calibrated FEM, field diagnosis, predictive maintenance, RUL hay automated maintenance trong luận án.

### 9.4 Trạng thái deep-read per source

| Parent | Work | Deep-read status | Evidence use status |
|---|---|---|---|
| `RWHW6F9I` | Ramasso et al. | `FULLTEXT_DEEP_READ`; preprint-journal relation verified | `CITE AS JOURNAL 2025`; locators ghi preprint PDF 2024; direct context/transfer evidence |
| `VPFBB9SG` | Brake et al. | `FULLTEXT_DEEP_READ`; journal version verified | Direct mechanistic context/repeatability evidence |
| `6IW2HEFJ` | Amin et al. | `FULLTEXT_DEEP_READ`; journal version verified | Method precedent; event-level only |
| `S2WXRDUS` | Vieira et al. | `FULLTEXT_DEEP_READ`; arXiv 2025 -> journal 2026 verified | Method precedent; physical-component/leakage evidence only |
| `IW7JBB3E` | da Silva et al. | `FULLTEXT_DEEP_READ`; online-first/issue year resolved | Direct cross-specimen shift; transductive adaptation boundary |
| `WMBQRXFF` | Ozdagli & Koutsoukos | `FULLTEXT_DEEP_READ`; proceedings version verified | Background/method precedent; independent-validation claim blocked |

## 10. Tác động lên Gap 1

**Phát hiện có khả năng làm thay đổi cách viết Gap 1:** Gap 1 không còn được bảo vệ bằng sự thiếu vắng campaign/reassembly evaluation trong bolted-joint monitoring nói chung. Ramasso là counterexample trực tiếp; da Silva còn là counterexample cho cross-specimen source-target adaptation. Amin và Vieira đồng thời đóng phần novelty phương pháp của split-first, train-only và physical-unit grouping.

**Gap còn bảo vệ được, nhưng hẹp hơn:** trong corpus đã kiểm chứng, chưa nguồn nào thực hiện và báo cáo **đồng thời** trên **steel frame with bolted connections using vibration condition evidence** ba trục: (1) physical independent unit ở cấp run và hierarchy cao hơn được khai báo; (2) leakage control toàn pipeline, gồm split trước segmentation/augmentation và train-only fitting; (3) transfer scope được kiểm chứng riêng qua run/session/campaign. Ramasso đạt trục (3) trên aluminum bolted beam AE nhưng không đạt đúng asset/modality và không audit trục (1)-(2) ở run hierarchy; Amin đạt phần lớn trục (2) ở railway event level nhưng không trục (3); Vieira cung cấp authority cho (1)-(2) ngoài structural asset; da Silva/Ozdagli là transductive adaptation.

**Đánh giá Gap 1 sau sáu nguồn:** `NARROW_BUT_DEFENSIBLE`, nhưng yếu hơn nếu được viết như một absence claim. Dạng đúng là **application-and-conjunction gap**, không phải method gap. Closest competitor cho transfer axis phải chuyển thành Ramasso et al. (2025), với caveat preprint locators/AE/aluminum/five campaigns/`ACC+/-1`. Nếu tìm thấy một steel bolted-frame study kết hợp run-aware leakage control với independent campaign holdout, Gap 1 phải hạ xuống `WEAK` hoặc đóng.

## 11. Claim - Evidence - Limitation - Next action

**Claim:** Qualification của condition evidence cần group level tương ứng với phạm vi suy luận: axes/windows trong event, events trong run, runs trong session/campaign, và campaigns gắn với assembly/context.

**Evidence:** Amin chứng minh event-level grouping và train-only pipeline (PDF pp. 5-8); Vieira chứng minh condition/repetition splits vẫn leak ở physical-component level bằng controlled fixed-model experiments (pp. 20-24, Tables 11-13); Ramasso thực hiện unseen-campaign test sau reassembly (preprint PDF pp. 4-5, 13-21, Table 9); Brake định lượng assembly/setup variation (PDF pp. 6-13, Table 1); da Silva chứng minh source specimen choice quyết định target performance (PDF pp. 4-10, Fig. 13).

**Limitation:** Bằng chứng hội tụ nhưng không paper nào đúng toàn bộ asset + modality + protocol conjunction của WP1. Hai domain-adaptation papers dùng target data trong training; Amin dừng ở event; Ramasso chỉ có 5 campaigns và uncertain ordinal labels; Vieira là bearing diagnosis ngoài asset.

**Next action cho Chương 3/Paper 1 khi được phép cập nhật:** (1) thêm Ramasso vào closest-competitor table với campaign là independent transfer unit; (2) tách `event-aware`, `run-aware`, `campaign-aware` thay vì dùng grouped evaluation chung chung; (3) mô tả da Silva/Ozdagli là transductive adaptation, không phải independent transfer; (4) giữ Gap 1 ở conjunction/application form; (5) không thay đổi bất kỳ RQ/WP/Paper/Gate/Limited-FEM status từ record này.

**Gate statement:** record này là literature evidence only. Gate 1 vẫn theo source-of-truth hiện hành; không có Gate nào được pass hoặc đổi trạng thái bởi deep-read này.
