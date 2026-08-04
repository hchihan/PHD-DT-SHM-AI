# LIVING EVIDENCE BASE — v2.1 TRACEABILITY-CORE
**Version:** v2.1 | **Date:** 2026-07-19 | **Status:** CURRENT source of truth cho evidence base.
**Kế thừa (không tạo lại):** `LIVING_EVIDENCE_BASE_v1.1_LIMITED_FEM.md` (33 canonical substantive/limited) + `01_LIVING_EVIDENCE_BASE_v1.2_LIMITED_FEM_20260718.md` (19 new deep reads) + `../ZOTERO_DEEP_READ/02_NEW_DEEP_READ_EVIDENCE_MATRIX_20260718.csv` (titles/DOIs). Không sửa citation/DOI/kết quả; không re-read PDF trong bản migration này.
**Under:** `../../00_GOVERNANCE/MASTER_RESEARCH_CHARTER_v2.1_TRACEABILITY_CORE_20260719.md`.

## Locked research chain (v2.1)
```text
Vibration data → condition/state-change evidence (+ CEI) → BIM-linked component → inspection record → justified, accountable inspection action
```
Identifier chain: `Sensor_ID → BIM_GUID → Condition_Evidence_ID → Inspection_Record_ID → Action_Record_ID` (CEI = attribute của Condition_Evidence_ID; Action_Status = attribute của Action_Record_ID).
FEM: **nominal, uncalibrated, reference-only, not used for damage diagnosis.** Bốn lớp bằng chứng tách biệt: laboratory evidence / information traceability / field feasibility / management decision support — không mượn chéo.

Định vị: RQ1/WP1/C4/Paper 1/G1 (lab, run-aware/LORO, sensor config, CEI) · RQ2/WP2/C5/Paper 2/G2–G3 (traceability-to-decision, CEI, BIM component, inspection record, justification & accountability — **QLXD core**) · RQ3/WP3/C6/G4–G5 (minimum field feasibility, Rapexco). **Current priority: G1.**

---

## Executive Summary

- **Evidence mạnh nhất cho RQ1:** direct leakage/run-aware vibration sources — `M8LMWFQH` (test-training leakage in CBM) và `RG9FMT8Y` (data leakage in vibration signals, run/day/part + sensor-location effects, up to 0.47 error change); củng cố bởi grouped/LOGO (`XE9XS6BQ`), leakage-inflation (`PEUHYBPS`), và steel-frame bolted precedent `YR2NQWE7` (SHMnet). **Vẫn chưa có nguồn nào chứng minh đúng thiết kế ~6-run-per-class + LORO 6-fold + ResNet1D sensor mode của đề tài** → NPE (new PhD evidence), mở tại G1.
- **Evidence mạnh nhất cho RQ2:** `XUN8EX6X` (ontology BIM-AMS, 13 CQ, IFC GlobalId ↔ inspection result — closest competitor); representation/linkage layer (`2ILY9YZ3, IM9UKGRV, KDRSBM9K, ULHLMFZ8, PHXJ2KJN`); provenance (`EMTIHHX4`); CQ taxonomy SCQ/VCQ/RCQ (`LSYSC59G`); component identity (`FZ3GFSF2, PHXJ2KJN, WYN2RKEH, L52SHNEH`).
- **Evidence còn thiếu cho RQ2:** SHACL/invalid-data validation đã thực thi; full identifier-chain đã kiểm chứng; action-status history; automated referential-integrity. Ba full text ưu tiên chưa có: `3II2WKLN`, `NUTL57KJ`, `Z4IBWW9Y`. CQ methodology cần pre-register. **"Evidence is currently insufficient"** để đóng G3.
- **Evidence field feasibility hiện có:** steel-frame building precedent `9823WXJZ` (UCLA Factor Building); baseline dài hạn `TRZY4P6X`; temperature-threshold `GE3XSAYV`; missing-data `D3TGCKXW`; low-cost node qualification `LZPF7ILT`. **Chưa có** nguồn nào cho coastal industrial steel building với Sensor_ID→BIM_GUID + auditable inspection record + action history → G4 mở.
- **Khoảng trống cần bổ sung tiếp:** (1) DT management-maturity source đã có `ESTEYBHA`/`YGZ32C8M` nhưng cần chốt; (2) SHACL/invalid-data method (`3II2WKLN` full text); (3) IFC inspection-maintenance framework (`NUTL57KJ` full text); (4) four-level decision-support validation (chưa nguồn nào implement Normal→Watch→Inspect→Priority).
- **Nguồn đã hạ khỏi Core Scope:** toàn bộ FEM-updating/OSP/calibrated-FEM (§G): `LYNPWX2Q, 3N5DY3NV, YTH389L4, U4HIGWJ4, BERUCUIC, 7MUMMAHR, GGFJCZ7A, SF58JFER, SI97C35H (FEM aspect), PRQL4Y8P, L56P7RAF`; Future Work: `DX2JCMQ9, BBMA5P33, 66GL7FBR`.

---

## Classification (A–J) + evidence records

**Schema:** Evidence_ID (Zotero key) · Citation · Year · Source type · RQ/WP/Paper · Evidence layer · Claim supported · Evidence extracted · Limitation · Scope status · Reading status · Full-text status · Next action.

### A. RQ1 — Laboratory evidence (Paper 1 / G1)

| Evidence_ID | Citation | Year | Source type | RQ/WP/Paper | Layer | Claim supported | Evidence extracted | Limitation | Scope | Reading | Full-text | Next action |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| YR2NQWE7 | Zhang, Biswal & Wang (SHMnet) | 2020 | Direct precedent | RQ1/WP1/P1 | Lab | Steel-frame bolted-connection classification; repeated-data lesson (C1-01, C1-04) | Single-accelerometer classification precedent | NOT leakage-safe protocol proof | Core | Deep read | Available | Cite as precedent, not protocol proof |
| HWUA93NT (dup W7HQQESV) | Valdez-Yepez et al. | 2024 | Dataset | RQ1/WP1/P1 | Lab | Labelled bolt-loosening dataset organisation (C1-02) | Sensor metadata, repeated runs | Jacket structure, strong-adjacent domain | Core | Deep read | Available | Use for dataset-documentation design |
| VVBGM9EN | Eraliev, Lee & Lee | 2022 | Method | RQ1/WP1/P1 | Lab | Multi-bolt loosening classification (C1-01, C1-04) | Window-split leakage caveat | Not exact design | Core | Deep read | Available | Support split-design |
| PEUHYBPS | Goodarzi et al. | 2025 | Method | RQ1/WP1/P1 | Lab | LOGO vs K-fold leakage inflation (C1-04) | Leakage inflation evidence | Methodological only | Core | Deep read | Available | Cite for leakage control |
| RWHW6F9I | Ramasso et al. (preprint) | 2024 | Method (preprint) | RQ1/WP1/P1 | Lab | Campaign/reassembly holdout; sensor comparison (C1-04) | Holdout-by-campaign | Preprint boundary | Core | Deep read | Preprint | Confirm peer-review status |
| QUGY4928 | Avci et al. | 2021 | Review | RQ1/WP1/P1 | Lab | Validation-limitation framing (C1-05) | Review framing | Review, not primary | Core (framing) | Deep read | Available | Framing only |
| QIS5QS7V | Sajedi & Liang | 2022 | Method | RQ1/WP1/P1 | Lab | Split-by-vehicle-make design framing (C1-03) | Simulated bridge vibration AI | Simulated | Core (framing) | Deep read | Available | Design-analogue |
| XSKNR656 | Armijo & Zamora-Sanchez | 2024 | Field/bkg | RQ1+RQ3/P1+P3 | Lab+Field | Sensor metadata; field workflow (C1-03, C3-01) | Bridge monitoring, MEMS | Normal-condition pilot only | Core | Deep read | Available | Cross-ref field §D |
| L97BIAI3 | Sample size planning for classification models (Beleites et al.) | 2013 | Method | RQ1/WP1/P1 | Lab | Independent test size controls performance precision | Hierarchical sample-size, learning curves | Biomedical domain; no LORO steel design | Core | Deep read | Available (DOI 10.1016/j.aca.2012.11.007) | Run-level effective sample size |
| PZ937I73 | Exceeding chance level by chance (Combrisson & Jerbi) | 2015 | Method | RQ1/WP1/P1 | Lab | Small samples can exceed chance | Null simulations, empirical thresholds | No grouped-window model | Core | Deep read | Available (10.1016/j.jneumeth.2015.01.010) | Empirical chance analysis |
| 9XNSNIPX | Statistical Comparisons of Classifiers over Multiple Data Sets (Demšar) | 2006 | Method | RQ1/WP1/P1 | Lab | Defensible independent pairing units | Wilcoxon/Friedman/post-hoc | Datasets ≠ overlapping LORO folds | Core | Deep read | Available (JMLR 7) | Choose inference test carefully |
| ZLFATP2Z | Permutation Tests for Studying Classifier Performance (Ojala & Garriga) | 2009/2010 | Method | RQ1/WP1/P1 | Lab | Empirical p-values under null | Permutation framework | **Version/attachment conflict (conf 2009 vs journal 2010)** | Core | Deep read | Conflict | **REVIEW NEEDED** — relink parent/PDF |
| XE9XS6BQ | Impact of Choice of Cross-Validation Techniques (grouped/LOGO) | 2021 | Method | RQ1/WP1/P1 | Lab | Records from one source stay in one partition | Grouped CV, subject-wise holdout | Healthcare audio; larger groups | Core | Deep read | Available (10.4258/hir.2021.27.3.189) | Justify LORO/LOGO |
| M8LMWFQH | Test-Training Leakage in ML for Condition-Based Maintenance | 2024 | Direct | RQ1/WP1/P1 | Lab | Source grouping must precede segmentation | Performance collapse under proper holdout | Bearing domain; weak uncertainty | Core | Deep read | Available (10.36001/phme.2024.v8i1.4125) | Run-first splitting |
| RG9FMT8Y | Impact of Data Leakage in Vibration Signals for Bearing Fault Diagnosis | 2024 | Direct | RQ1/WP1/P1 | Lab | Source identity + sensor position alter apparent performance | Up to 0.47 error change across grouping scales | No ResNet1D or group CI | Core | Deep read | Available (10.1109/ACCESS.2024.3497716) | Fair sensor-mode + grouped comparison |
| SI97C35H | Svendsen et al. (classification aspect) | 2023 | Method | RQ1/WP1/P1 | Lab | Supervised-classification aspect (FEM aspect → §G) | Hybrid SHM classification | FEM aspect demoted | Core (class. only) | Deep read | Available | Use classification aspect only |
| DFAJFF8J | Abdeljaber et al. | 2018 | Benchmark bkg | RQ1/WP1/P1 | Lab | 1-D CNN benchmark background (C1-03) | Benchmark reference | Limited access | Supporting | Limited access | Limited | Background only |
| JQSY7XD4 | Teng et al. | 2022/2023 | Method bkg | RQ1/WP1/P1 | Lab | Transfer-learning method background (C1-03) | TL method | Background only | Supporting | Deep read (addendum) | Available | Background only |
| VDPRGI94 | Dang et al. (AI-classification aspect) | 2022 | Bkg | RQ1/WP1/P1 | Lab | DT-SHM workflow AI part (C1-03) | Workflow background | FEM aspect → §G | Supporting | Deep read | Available | AI aspect only |

RQ1 boundary (unchanged): không nguồn nào cung cấp leakage-safe run-level protocol của đề tài; LORO + ResNet1D sensor-mode verification là mục G1 mở.

### B. RQ2 — Information traceability (Paper 2 / G2–G3)

| Evidence_ID | Citation | Year | Source type | RQ/WP/Paper | Layer | Claim supported | Evidence extracted | Limitation | Scope | Reading | Full-text | Next action |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| XUN8EX6X | Ontology-based BIM-AMS integration in European Highways | 2024 | Direct (closest competitor) | RQ2/WP2/P2 | Traceability | CQ-driven ontology links inspection results to IFC GlobalIds | 13 CQs, SPARQL, 3 pilots | SHACL not executed; mapping partly manual; no action history | Core | Deep read | Available (10.1016/j.iswa.2024.200366) | Benchmark Paper 2 against it |
| VI5QMSAE | Integration of IFC objects & FM work info (Semantic Web) | 2018 | Strong adjacent | RQ2/WP2/P2 | Traceability | Object-linked retrieval of work records | 590-record case, SPARQL | No sensors/CQs/SHACL/status history | Core | Deep read | Available (10.1016/j.autcon.2017.12.019) | Object↔work-record requirement |
| EMTIHHX4 | Blockchain-supported BIM data provenance | 2022 | Method | RQ2/WP2/P2 | Traceability | Object provenance reconstructs change history | Actor/operation/version/timestamp events | Design provenance; no inspection/CQ/SHACL | Core | Deep read | Available (10.1016/j.compind.2022.103768) | Minimum provenance fields |
| GUEJBZBZ | BIM and IFC Data Readiness for AI Integration | 2024 | Background review | RQ2/WP2/P2 | Traceability | IFC time-series + toolchain barriers | 93-study PRISMA synthesis | No RQ2 chain validation | Supporting | Deep read | Available (10.3390/buildings14103305) | Scope time-series architecture |
| PHXJ2KJN | IFC GlobalId as stable component identity (per RQ2 addendum) | verify | Standard-linked | RQ2/WP2/P2 | Traceability | Component identity anchor (C2-03/04) | IFC GlobalId stability | Detail in RQ2 addendum | Core | Deep read | Available | Cite via addendum |
| FZ3GFSF2 | Component identifier source (per RQ2 addendum) | verify | Traceability | RQ2/WP2/P2 | Traceability | Standardized component identifiers (C2-03) | Identity model | Detail in addendum | Core | Deep read | Available | Cite via addendum |
| L52SHNEH | AIM/O&M information structure (per RQ2 addendum) | verify | Traceability | RQ2/WP2/P2 | Traceability | AIM/O&M info structures (C2-04) | Asset info structure | Detail in addendum | Core | Deep read | Available | Cite via addendum |
| WYN2RKEH | ISO 23247-aligned data categories/component IDs | verify | Traceability | RQ2/WP2/P2 | Traceability | Data categories + component IDs (C2-04) | ISO 23247 alignment | Detail in addendum | Core | Deep read | Available | Cite via addendum |
| 2ILY9YZ3 | Representation/linkage layer source (RQ2 addendum) | verify | Traceability | RQ2/WP2/P2 | Traceability | Representation layer (C2-01) | Linkage representation | Detail in addendum | Core | Deep read | Available | Cite via addendum |
| IM9UKGRV | Linkage layer source (RQ2 addendum) | verify | Traceability | RQ2/WP2/P2 | Traceability | Linkage layer (C2-02) | Linkage mechanism | Detail in addendum | Core | Deep read | Available | Cite via addendum |
| KDRSBM9K | Representation/linkage source (RQ2 addendum) | verify | Traceability | RQ2/WP2/P2 | Traceability | Representation/linkage (C2-01/02) | Linkage | Detail in addendum | Core | Deep read | Available | Cite via addendum |
| ULHLMFZ8 | Representation/linkage source (RQ2 addendum) | verify | Traceability | RQ2/WP2/P2 | Traceability | Representation/linkage (C2-01/02) | Linkage | Detail in addendum | Core | Deep read | Available | Cite via addendum |

Boundary: no reviewed source validates the whole locked identifier chain; that chain is the PhD contribution (Gap C2-06). Detail: `../../90_ARCHIVE/SNAPSHOTS_20260718/BACKUP_BEFORE_WRITEBACK_20260718/04_RQ2_TRACEABILITY_EVIDENCE_ADDENDUM_v1.2_20260718.md`.

### C. RQ2 — Justification / accountability & decision support (Paper 2 / G2–G3, WP4/G5 link)

| Evidence_ID | Citation | Year | Source type | RQ/WP/Paper | Layer | Claim supported | Evidence extracted | Limitation | Scope | Reading | Full-text | Next action |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LSYSC59G | Characterising Competency Questions for Ontologies | verify | Method | RQ2/WP2/P2 | Traceability | SCQ/VCQ/RCQ có mục đích khác nhau | QuO definitions, examples | Empirical effectiveness = future work | Core | Deep read | Available (no DOI) | Label & operationalize Paper 2 CQs |
| XUN8EX6X | (see §B) | 2024 | Direct | RQ2/WP2/P2 | Traceability | Inspection result ↔ GlobalId justification | 13 CQ pilots | No action history | Core | Deep read | Available | Justification backbone |
| GIIUUEW8 | Deng et al. (threshold warning + element-ID) | 2022 | Method | RQ2+RQ3/P2+P3 | Traceability→Decision | Element-ID localized warning → inspection trigger (C2-05, C3-03) | Threshold warning, element-ID | Medium/indirect record linkage | Core | Deep read | Available | Inspection-record schema input |
| 4LKDXFMK | Li et al. (defect/condition/repair records) | 2023 | Method | RQ2+RQ3/P2+P3 | Traceability→Decision | Record structures for inspection (C2-05, C3-04, C4-01) | Defect/condition/repair record structures | Bridge/SHM domain | Core | Deep read | Available | Inspection_Record + Action_Record template |
| 8Y64JYBR | Chen et al. (SHM management decision-support arch) | 2014 | Bkg | RQ2+RQ3/P2 | Decision | Management decision-support architecture (C2-05, C3-03) | Decision-support architecture | Indirect | Supporting | Deep read | Available | Background for decision layer |
| YGZ32C8M (dup EN2SIFMC) | Identifying Maturity Dimensions for Smart Maintenance Management | 2021 | Strong adjacent | WP4→RQ2/P2 | Decision | Asset-condition-job traceability + human governance | 48 interviews, 7-expert review | No four-level escalation; no steel-building case | Core (governance) | Deep read | Available (10.1061/(ASCE)CO.1943-7862.0002112) | Governance/accountability anchor |

Accountability = truy vết role/evidence/creator/approver/timestamp/version/approval status (Charter §2.4) — **không phải trách nhiệm pháp lý.** Legal mapping (§F) chỉ neo nghĩa vụ, không tạo ngưỡng kỹ thuật.

### D. RQ3 — Field feasibility (Paper 3 / G4–G5)

| Evidence_ID | Citation | Year | Source type | RQ/WP/Paper | Layer | Claim supported | Evidence extracted | Limitation | Scope | Reading | Full-text | Next action |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 9823WXJZ | Earthquake & Ambient Vibration Monitoring of Steel-Frame UCLA Factor Building | 2006 | Direct | RQ3/WP3/P3 | Field | Steel-building deployment precedent; operational/wind effects alter baselines | Continuous 72-channel building data | No component/BIM/inspection chain; no confirmed damage | Core | Deep read | Available (10.1193/1.1946707) | Steel-building precedent |
| TRZY4P6X | Temperature-based SHM baseline for long-span bridges | 2015 | Strong adjacent | RQ3/WP3/P3 | Field | Location-specific environmental baselines feasible | 3-year field surfaces, installation | Bridge; no BIM chain | Core | Deep read | Available (10.1016/j.engstruct.2014.12.042) | Baseline QC design |
| GE3XSAYV (dup 2RB2YRBW) | Dynamic Threshold Cable-Stayed Bridge HM (Temperature Correction) | 2023 | Strong adjacent | RQ3/WP3/P3 | Field | Temperature affects operational thresholds | 1-year hourly GNSS | Missingness/inspection provenance incomplete | Core | Deep read | Available (10.3390/s23218826) | Environmental-baseline requirement |
| D3TGCKXW | Long-term HM of concrete & steel bridges under large/missing data | 2023 | Strong adjacent | RQ3/WP3/P3 | Field | Environmental variation + missingness dominate field features | Freezing/missing-data analyses | Secondary data; no sensor/component provenance | Core | Deep read | Available (10.1016/j.engstruct.2023.115616) | Missing-data controls |
| LZPF7ILT | Low-Cost Wireless Multinode Vibration Monitoring System | 2023 | Method | RQ3/WP3/P3 | Field/Lab | Low-cost nodes need application-specific qualification | Impulse success, ambient failure | Lab only; no long-term field | Core | Deep read | Available (10.1155/2023/5240059) | Sensor qualification protocol |
| XSKNR656 | Armijo & Zamora-Sanchez | 2024 | Field | RQ3/WP3/P3 | Field | In-service low-cost MEMS workflow (C3-01) | Warning dashboard, normal-condition pilot | Normal-condition only | Core | Deep read | Available | Field workflow analogue |
| GIIUUEW8 | Deng et al. | 2022 | Method | RQ3/P3 | Field→Decision | Threshold warning + element-ID localization (C3-03) | Inspection trigger | Indirect | Core | Deep read | Available | Cross-ref §C |
| 4LKDXFMK | Li et al. | 2023 | Method | RQ3/P3+WP4 | Field→Decision | Record workflow (C3-04, C4-01) | Record structures | Bridge domain | Core | Deep read | Available | Cross-ref §C |
| VDPRGI94 | Dang et al. (workflow aspect) | 2022 | Bkg | RQ3/P3 | Field | Conceptual DT data-interaction workflow (C3-02) | Non-FEM workflow | FEM aspect → §G | Supporting | Deep read | Available | Background |

Boundary: field feasibility = deployment + baseline + traceability scenarios. **No field damage diagnosis; no classifier transfer;** anomaly → inspection, not damage claim. **Evidence is currently insufficient** để đóng G4 (chưa có coastal industrial steel building với Sensor_ID→BIM_GUID + auditable records + action history).

### E. Digital Twin / BIM / asset-management foundation

| Evidence_ID | Citation | Year | Source type | RQ/WP/Paper | Layer | Claim supported | Evidence extracted | Limitation | Scope | Reading | Full-text | Next action |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ESTEYBHA | Gemini Principles-Based Digital Twin Maturity Model for Asset Management | 2021 | Method | WP4→C3 | Foundation | Explicit rubrics support transparent DT-maturity self-definition | 27 rubrics; 40-expert + 2 cases | Maturity ≠ condition escalation; top level includes autonomy | Supporting (C3 def) | Deep read | Available (10.3390/su13158224) | Write C3 DT-maturity self-definition |
| YGZ32C8M | Identifying Maturity Dimensions (see §C) | 2021 | Strong adjacent | WP4→C3 | Foundation | Maturity dimensions for smart maintenance | Case + expert | No four-level logic | Supporting | Deep read | Available | C3 support |
| BZKLQK4H | BIM→DT evolution (background) | verify | Bkg | E/C3 | Foundation | BIM→DT evolution context | Background | Screened/background only | Supporting | Screened | Available | Deep-read only if needed |
| M72SVKKB | Conceptual DT framework (background) | verify | Bkg | E/C3 | Foundation | Conceptual framework context | Background | Background only | Supporting | Screened | Available | Deep-read only if needed |
| EK8QXFGD / FRJYYGCZ / M94HVWCY | DT/SHM review metadata (screened only) | verify | Review meta | E | Foundation | Field framing | Metadata only | Screened only | Supporting | Screened | Metadata | Not citable as findings |

### F. Legal & management context (neo nghĩa vụ — không tạo ngưỡng kỹ thuật)

| Evidence_ID | Citation | Year | Source type | RQ/WP/Paper | Layer | Claim supported | Evidence extracted | Limitation | Scope | Reading | Full-text | Next action |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ISO19650-3 | ISO 19650-3 Information management (operational phase) | 2020 | Standard | RQ2/P2 | Mgmt context | Information-management obligation anchor | Normative (cited as standard) | Normative, not empirical | Core context | Standard | Standard | Cite as standard |
| TCVN14177 | TCVN 14177:2024 (asset identification) | 2024 | Standard | RQ2/P2 | Mgmt context | Component/asset identity obligation | Normative | Normative | Core context | Standard | Standard | Cite as standard |
| WYN2RKEH/ISO23247 | ISO 23247 DT framework alignment | verify | Standard | RQ2/P2 | Mgmt context | Data categories/component IDs | Normative alignment | Normative | Supporting | Deep read | Available | Cite alignment |
| V3IYM6UC | ISO/IEC 30173:2023 Digital twin — Concepts & terminology | 2023 | Normative (partial) | WP4/C3 | Mgmt context | DT requires data-connected physical/digital convergence | Clause 3.1.1 (preview) | Local file incomplete preview | Supporting | Partial | **Partial** | Acquire full standard |
| EWBTQFTP | ISO/IEC 30186:2025 DT — Maturity model & assessment | 2025 | Normative (partial) | WP4/C3 | Mgmt context | Five generic maturity aspects | Clauses 1,3,5.1 (preview) | Incomplete sample | Supporting | Partial | **Partial** | Acquire full standard |
| VN-LEGAL | Luật XD 135/2025; NĐ 207/2026/NĐ-CP; TT 32/2026/TT-BXD; QĐ 46/2026/QĐ-UBND Khánh Hòa; Công văn 3839 | 2025–2026 | Legal | RQ2/P2 | Mgmt context | Management/inspection/maintenance-record obligation (justification & accountability) | — | **Legal reference pending official-source verification** | Core context | — | **Unverified** | **REVIEW NEEDED** — verify official source; không suy ngưỡng kỹ thuật |

### G. Supporting reference — nominal FEM only (demoted from Core)
> Toàn bộ nhóm này: **nominal, uncalibrated, reference-only, not used for damage diagnosis.** Permitted: qualitative mechanical hypotheses (Discussion/Limitation, "hypothesis, not confirmed"), historical context. Prohibited: supporting calibrated-FEM/stiffness-degradation/severity/diagnosis claim in thesis core. Không nguồn nào là bằng chứng lõi cho RQ/WP/Paper/Gate.

| Evidence_ID | Citation | Year | Prior role | Scope (v2.1) | Reading | Full-text | Next action |
|---|---|---|---|---|---|---|---|
| LYNPWX2Q | Yang, Xia & Loh | 2014 | Direct FEM loosening interpretation | Supporting (FEM) | Deep read | Available | Hypothesis/context only |
| 3N5DY3NV | Weng, Loh & Yang | 2009 | Direct FE updating | Supporting (FEM) | Deep read | Available | Hypothesis/context only |
| YTH389L4 | Biswal et al. | 2022 | FE updating / virtual damper | Supporting (FEM) | Deep read | Available | **REVIEW** dup DOI vs BERUCUIC |
| U4HIGWJ4 | Pal et al. | 2022 | Fixity-factor updating | Supporting (FEM) | Deep read | Available | Context only |
| BERUCUIC | Biswal et al. | 2021 | OpenSEES spring updating | Supporting (FEM) | Deep read | Available | **REVIEW** dup DOI vs YTH389L4 |
| 7MUMMAHR | Yaoyama et al. | 2024 | Probabilistic updating (strong adjacent) | Supporting (FEM) | Deep read | Available | Context only |
| GGFJCZ7A (dup UCIYTI8C) | Musil et al. | 2025 | MAC/frequency matching (strong adjacent) | Supporting (FEM) | Deep read | Available | Context only; MAC only as lit-description |
| SF58JFER | Jiang, Zhu & Zhuo | 2024 | Acoustic classification (strong adjacent) | Supporting (adjacent) | Deep read | Available | Adjacent context |
| SI97C35H | Svendsen et al. (FEM aspect) | 2023 | Calibrated-FEM hybrid SHM | Supporting (FEM aspect) | Deep read | Available | FEM aspect context; class. aspect → §A |
| PRQL4Y8P | Guerrero Bobadilla et al. | 2016 | Lab steel-frame dynamic response | Supporting (lab dynamics) | Deep read | Available | Background dynamics |
| L56P7RAF | Weil et al. | 2025 | Modal tracking + uncertainty | Supporting (uncertainty→CEI framing) | Deep read | Available | May inform CEI confidence discussion |

### H. Future Work (deferred, out of PhD core)

| Evidence_ID | Citation | Year | Prior role | Scope | Reading | Next action |
|---|---|---|---|---|---|---|
| DX2JCMQ9 | Tian et al. | 2021 | Contact parameterisation | Future Work (calibrated-FEM expansion) | Deep read | Post-PhD |
| BBMA5P33 | Yi et al. | 2011 | FEM-based OSP | Future Work | Deep read | Post-PhD; "optimal sensor placement" prohibited in core |
| 66GL7FBR | Sun et al. | 2025 | OSP review | Future Work | Deep read | Post-PhD |
| 3CJAB5LG | Zhang et al. | 2024 | Decision-analysis vocabulary (optional WP4) | Future Work / optional | Deep read | Optional Paper 4 only |

### I. Out of Scope

| Evidence_ID | Citation | Year | Reason | Next action |
|---|---|---|---|---|
| 43648CQ8 | (target: DSS integrating CM/PM/CBM) — **attached PDF is Tunney et al. 2002, wrong paper** | — | PDF mismatch; target unavailable | Out of scope until correct PDF attached & read |

### J. Evidence insufficient / full text needed

| Evidence_ID | Citation | Year | RQ/Gate | Status | Next action |
|---|---|---|---|---|---|
| 3II2WKLN | Enhancement & validation of ifcOWL based on SHACL | 2024 | RQ2/G3 | **FULLTEXT_UNAVAILABLE** (HTML only) | Acquire full text — Gate 3 priority (SHACL/invalid-data) |
| NUTL57KJ | IFC framework for inspection & maintenance representation in FM | 2025 | RQ2/G2–3 | **FULLTEXT_UNAVAILABLE** (HTML only) | Acquire full text — inspection/maintenance schema |
| Z4IBWW9Y (dup P674U5V2) | A Parameter-Driven Method for Modeling Bridge Defects through IFC | verify | RQ2/G2–3 | **FULLTEXT_UNAVAILABLE** (abstract only) | Acquire full text — IFC defect/action model |
| ZLFATP2Z | Permutation Tests... (version conflict) | 2009/2010 | RQ1/G1 | **REVIEW NEEDED** (parent/PDF mismatch) | Separate conference parent vs journal extension |
| DT-MATURITY | Dedicated DT management-maturity source | — | C3 | Partially met by ESTEYBHA/YGZ32C8M | Confirm sufficiency or deep-read one more |

---

## Canonical handling (duplicates — không đếm là bằng chứng độc lập)
`W7HQQESV`=dup `HWUA93NT`; `UCIYTI8C`=dup `GGFJCZ7A`; `P674U5V2`=dup `Z4IBWW9Y`; `2RB2YRBW`=dup `GE3XSAYV`; `EN2SIFMC`=dup `YGZ32C8M`. Canonical: đếm `GE3XSAYV`, `Z4IBWW9Y`, `YGZ32C8M`. `43648CQ8` loại tới khi đúng PDF. ISO preview (`EWBTQFTP`,`V3IYM6UC`) không tag là full standard.

## CEI — quy tắc
CEI = **confidence/evidence metadata** (evidence validity status, model confidence, run/fold variability, sensor configuration, data-quality status, provenance, timestamp/version). Nguồn hỗ trợ CEI như metadata độ tin cậy: run-level uncertainty & grouping (`RG9FMT8Y`, `L97BIAI3`, `PZ937I73`, `XE9XS6BQ`), modal-tracking uncertainty framing (`L56P7RAF`). **CEI KHÔNG phải** severity, Health Index, hay chỉ số hư hỏng. **Evidence is currently insufficient** để định nghĩa CEI như một scalar index phổ quát → giữ CEI ở dạng cấu trúc metadata.

## FEM — quy tắc
Mọi nguồn FEM (§G, §H) là Supporting Scope hoặc Future Work; citation được giữ nguyên (không xóa); không dùng làm bằng chứng lõi cho RQ/WP/Paper/Gate; luôn ghi "nominal, uncalibrated, reference-only, not used for damage diagnosis".

## Firewall bốn lớp
Không dùng lab evidence để tuyên bố field diagnosis. Không dùng traceability để tuyên bố damage detection. Không dùng legal mapping để tạo ngưỡng kỹ thuật.

## Claim → Evidence → Limitation → Next action
- **Claim:** Evidence base migrate sang Traceability-Core v2.1 không mất mát — kế thừa 33 (v1.1) + 19 (v1.2) canonical; phân loại A–J; FEM demote sang §G/§H; 0 xóa.
- **Evidence:** v1.1 §1–8; v1.2 §3; CSV deep-read matrix (titles/DOIs); RQ addenda.
- **Limitation:** reclass thực hiện từ record đã trích, không re-read PDF; RQ2 keys (2ILY9YZ3/IM9UKGRV/KDRSBM9K/ULHLMFZ8/PHXJ2KJN/FZ3GFSF2/L52SHNEH/WYN2RKEH) chưa có author-year xác minh trong bản này (verify từ Zotero/RQ2 addendum); YTH389L4/BERUCUIC dup chưa giải quyết; ZLFATP2Z version conflict; 3 RQ2 full text thiếu; legal refs chưa xác minh; CEI chưa đủ để thành scalar.
- **Next action:** (G1) khóa run registry → LORO → ResNet1D provenance → run-level uncertainty; (G2) pre-register SCQ/VCQ/RCQ + CEI/Action_Record schema; acquire `3II2WKLN`,`NUTL57KJ`,`Z4IBWW9Y`; resolve YTH389L4/BERUCUIC + ZLFATP2Z; verify legal refs + RQ2-key metadata.
