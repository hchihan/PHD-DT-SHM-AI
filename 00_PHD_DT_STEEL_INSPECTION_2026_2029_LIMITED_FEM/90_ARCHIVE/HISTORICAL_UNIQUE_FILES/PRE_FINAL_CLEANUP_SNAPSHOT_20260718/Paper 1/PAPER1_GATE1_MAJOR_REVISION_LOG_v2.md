# PAPER 1 / GATE 1 — MAJOR REVISION LOG (v2)
**Date:** 2026-07-18 | **From:** `Paper 1 (10.06).docx` (draft 2026-06-10) → **To:** `PAPER1_GATE1_Q2_VERIFIED_EVIDENCE_REVISED_v2.docx`
**Nature of revision:** viết lại toàn bộ (coherent rewrite), không chỉnh vá. Bản nháp cũ được giữ nguyên, không sửa.

## 1. Title
- **Removed:** "Sensor Configuration Evaluation for AI-Based Asset Management: Evidence from Vibration-Based Damage Classification of a Scaled Steel Frame".
- **Replaced by locked title:** "Run-Aware Evaluation of Low-Cost Sensor Configurations for Vibration-Based Condition Classification of a Scaled Bolted Steel Frame".
- **Reason:** loại "damage classification"; bám title khóa của prompt.

## 2. Sections removed entirely
| Draft section/content | Reason |
|---|---|
| §4.4 Ordinal DSI proxy + confidence score; §5.5 DSI results (R=0.953, RMSE 0.119, MAE 0.051); §6.4 DSI discussion | Severity/DSI prohibited (Charter §11); preliminary single-split numbers |
| "Softmax preserves severity" và mọi diễn giải severity | Prohibited terminology |
| §7.2 Future work: FEM model updating (RSAP), physics-informed DSI, optimal sensor placement, field validation ADXL345/CV, Digital Twin platform | Out of Scope theo Limited-FEM; lab-to-field transfer prohibited |
| Bảng "NẾU MUỐN TĂNG KHẢ NĂNG ACCEPT", đề xuất journal strategy, bảng overclaim control cũ | Working notes, không thuộc manuscript |
| Mọi kết quả số: Tables 6–9 (macro-F1 0.869/0.546/0.641/0.541...; per-class F1; 0.475 BCJ; confidence 0.45–0.99); §5.4 overfitting narrative | PRELIMINARY — NOT VERIFIED UNDER FINAL LORO PROTOCOL; thay bằng placeholders §5 |

## 3. Overclaims removed
- "Random Forest outperforms 1D-CNN under small-data conditions across all configurations" (highlight + kết luận).
- "Dual-sensor input narrows the RF–CNN gap from 23 to 2 percentage points" (định lượng sơ bộ trong highlights/abstract).
- "Adding a sensor can improve diagnostic performance more than switching to a more complex algorithm" (chỉ được phát biểu sau final LORO; §6.2 giữ dạng bounded + placeholder).
- "Sensor number and location govern the upper bound of diagnostic observability" theo OSP literature (nguồn OSP bị reclassify POST_PHD; ngôn ngữ "optimal sensor placement" cấm trong core).
- Mọi hàm ý field deployment/maintenance readiness.

## 4. Sections rewritten
| Section | Change |
|---|---|
| Highlights | 5 dòng methodological, không số liệu |
| Abstract | Cấu trúc Problem → Gap → Method → [DATA REQUIRED] → Contribution → Scope limitation; không từ cấm |
| Introduction | 7 luận điểm bắt buộc (trustworthy evidence = sensing + valid evaluation; windows ≠ independent experiments; random split inflation; sensor config thường bị cố định; gap; bounded contribution; không thuật toán mới/không field diagnosis) + RQ + 4 contributions |
| Related Work | Tái cấu trúc 2.1–2.4 + literature-gap table; chỉ nguồn deep-read; "Within the reviewed evidence base..." thay cho "no study exists" |
| §3 Experimental Program | Chuyển thành data-governance structure: specimen (chỉ facts đã xác minh, không similitude claim), states categorical (không ordinal), excitation placeholder, sensor metadata placeholder, run registry bắt buộc, exclusion rules |
| §4 Methods | Thành "Run-Aware Evaluation Protocol": independent unit, split-before-windowing, train-only preprocessing, common LORO folds, model provenance (ResNet1D conditional), fairness locks, metrics, run-level uncertainty + group-preserving permutation, leakage-audit checklist |
| §5 Results | Toàn bộ placeholders có đặc tả input/output/section/claim |
| §6 Discussion | Bounded; leakage contrast chỉ khi được chạy chủ đích; asset-management relevance giới hạn 4 điểm cho phép |
| §7 Limitations | Đủ 10 mục bắt buộc theo prompt |
| §8 Conclusions | Trả lời RQ1 (framework); tuyên bố "Gate 1 is not yet closed; the manuscript specifies the remaining experimental controls." |

## 5. Terminology replacements applied
| Old | New |
|---|---|
| damage classification / damage state | controlled connection-state classification / controlled connection state |
| damage diagnosis | condition evidence / state classification |
| diagnostic accuracy/performance | classification performance |
| damage severity / DSI / health index | (removed; CEI chỉ như future analysis request §5.8) |
| optimal sensor | sensor configuration evaluated under the study protocol |

## 6. Citations replaced
- **Removed (unverified draft citations):** Azhar 2024; Svendsen 2023; Yang 2024; Abdeljaber 2018 (limited access); Almutairi 2021; Guerrero 2016; Sabnis 1983; Ozbek 2022; Ostachowicz 2019; Yi 2011; Sun 2025; Mardanshahi 2025; Simoncelli 2024; Pham 2020; Chou 2014; Chou 2019; Bao 2023; Kiranyaz 2021; Dang 2022; Jia & Li 2023; Plevris & Papazafeiropoulos 2024; Wang 2024; Guo 2017; Bergstra & Bengio 2012.
- **Added (7 verified new RQ1 sources):** Beleites et al. 2013; Combrisson & Jerbi 2015; Demšar 2006 (metadata corrected: one author, JMLR 7:1–30); Ojala & Garriga 2010 (cited as 2010 JMLR version, không gắn DOI hội nghị 2009); Tougui et al. 2021; Matania et al. 2024 (conference paper); Wheat et al. 2024.
- **Retained (canonical RQ1 v1.1, có cờ metadata check):** Zhang et al. 2020 (SHMnet); Eraliev et al. 2022; Valdez-Yepez et al. 2024; Goodarzi et al. 2025; Ramasso et al. 2024 (preprint boundary); Avci et al. 2021 (framing).

## 7. Placeholders added (theo format chuẩn)
16 placeholders: DATA REQUIRED ×7; ANALYSIS REQUIRED ×6 (audit, leakage audit, sensor contrast, model contrast, permutation, sensitivity, CEI); TABLE REQUIRED ×4; FIGURE REQUIRED ×1; METHOD DECISION REQUIRED ×3; AUTHOR CONFIRMATION REQUIRED ×4; REFERENCE METADATA CHECK REQUIRED ×9 (trong References + audit CSV). Mỗi placeholder ghi rõ input, output, section, claim.

## 8. Reference conflicts handled
- `ZLFATP2Z` (Ojala–Garriga): PDF là bản JMLR 2010 mở rộng, parent Zotero là ICDM 2009. Manuscript trích JMLR 2010 pp.1836–1843, không gắn DOI 2009, không bịa DOI JMLR; đã ghi vào reference audit; relink chờ Zotero writeback.
- `9XNSNIPX` (Demšar): sửa metadata — một tác giả, 2006, JMLR 7, 1–30; không bịa DOI.
- `M8LMWFQH` (Matania): trích như conference paper.

## 9. Files
- Bản nháp cũ `Paper 1 (10.06).docx`: giữ nguyên, không sửa/ghi đè (đóng vai trò archive).
- File mới: 6 file v2 liệt kê trong `PAPER1_GATE1_READINESS_REPORT_v2.md`.
