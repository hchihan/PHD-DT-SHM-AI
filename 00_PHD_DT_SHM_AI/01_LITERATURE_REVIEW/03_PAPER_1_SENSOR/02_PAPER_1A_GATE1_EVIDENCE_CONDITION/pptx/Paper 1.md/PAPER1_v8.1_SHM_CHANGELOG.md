# PAPER1 v8.1 (Structural Health Monitoring, SAGE): changelog

**Date:** 13 September 2026
**Output:** `PAPER1_v8.1_SHM_RISK_REDUCED.docx`

**Source.** The source is `PAPER1_v8_SHM_SUBMISSION.docx` as it exists on H:, last saved 12 Sep 2026 at 22:49. That is **after** the v8 delivery, and it contains one author edit: the corresponding author is now "Tri – Ngo Ngoc". This edit is preserved.

**Inputs read in full:** v8 manuscript, `PAPER1_v8_SHM_CHANGELOG.md`, `PAPER1_v8_SHM_COMPLIANCE_CHECK.md`, and `PAPER1_OPENALEX_CROSSCHECK.md` (located at `D:\08_NGHIEN_CUU_MCP\`, not in the paper folder).

## Scope guard

The following were not done:

- No model was rerun.
- No result value, table cell or execution count was changed.
- No FEM, field diagnosis, severity, RUL, predictive-maintenance or new-architecture content was added.

`check_v81.py` confirms the following against v8:

- All 17 data tables are identical in text to v8; the only changed table is the Figure 2 photo-layout grid.
- No three-decimal value was lost or added anywhere in the text.
- The IT-01 to IT-06 corrections are untouched: 972 appears once with its audit framing, the locked 192 sentence is present, and "294" is absent.
- The six protected limitations are all still present: HPO dependence, run independence, state order, sensor mapping, synchronisation and the cross-campaign caveats.

**Package:** passes Office XSD validation against v8 (1024 → 1028 paragraphs). **Checks:** 50/50 PASS.
**Length:** main text (Introduction–Conclusions, excluding tables and captions) 9,405 → 9,518 words (+1.2%). Abstract 199 → 219 words.

---

## Step 1: Figure 3 contradiction

| Item | v8 | v8.1 |
|---|---|---|
| Figure 3 image | Raster whose "Model development and evaluation" box read "Window-wise standardisation / Training data only", contradicting §3.6 | **Redrawn schematic.** No editable source was found anywhere in D:\01_RESEARCH, the H: PhD tree, D:\08_NGHIEN_CUU_MCP or the code archive; the only hit for the box texts is a mention in `PAPER1_FULL_MANUSCRIPT_v3.md`. The raster was therefore **not edited**. A new diagram was drawn from Sections 3.5–3.9 with matplotlib (`make_fig3.py`, 3200 × 2080 px), and it contains no data. The fitting box now reads "**Per-window channel standardisation (applied independently to all partitions)**" and, separately, "**SVM StandardScaler (fitted on training data only)**". It also shows the checkpoint and early-stopping rule on the validation run, candidate selection on validation quantities, the prior hyperparameter-development pool (5 of 6 runs; RUN006/012/018 withheld; test run in the pool for 15 of 18 folds and all transfer cases) and the cross-campaign transfer design. An automated check confirmed that no text overflows its box |
| Figure 3 display size | 5.18 × 3.24 in (image 1965 × 1230 px, 380 dpi at that size) | 6.30 × 4.10 in, 508 dpi effective |
| Figure 3 caption | ended "…do not remove development-stage dependence." | adds "Per-window channel standardisation is applied independently to every window in all partitions; only the SVM StandardScaler is fitted on training data." |
| AI disclosure | none for figures | states that Figure 3 was redrawn with plotting code written with Claude and contains no data |

**[AUTHOR ACTION]:** approve the redrawn Figure 3, or replace it with a corrected diagram from your own source file.

## Step 2: state-order confounding (§5.6)

After "…the CP2 timestamp irregularities are unexplained." this sentence was added:

> "Because state acquisition was not fully randomised and the reference state occupied a consistent sequence position within each campaign, the present design cannot fully separate the effect of the manipulated connection state from other measurement-history factors that may have co-varied with acquisition order."

It does not assert that confounding occurred, and names no drift, heating, mounting or excitation-history mechanism. The facts behind it are in Table 2: S0 comes first in every CP1 and CP2 run and last in every CP3 run.

## Step 3: Figure 2 and photo resolution

| Item | v8 | v8.1 | Basis |
|---|---|---|---|
| Search for a true B1 photograph | none | **None found.** `IMAGES_EXP/` holds only the same eight files already embedded (identical byte sizes) plus the procurement invoice (`6.jpg`). The fabrication DOCX holds the same five photos. No other project photo exists | inspection |
| Panel (b) label | "(b) B1 apex manipulation" | "(b) B1 apex location (view repeated from Figure 1d)" | option C of the brief: repeated view stated explicitly |
| Second photograph under (d) | unlabelled | labelled "**(e) hand-tool adjustment of a bolted end-plate connection**", which describes only what the photo shows | option D (d)/(e); the connection it shows is not asserted |
| Figure 2 caption | "(b) B1 apex manipulation; … (d) B3 brace-connection manipulation." | "(b) B1 apex connection location, shown with the same photograph as Figure 1(d); (c) …; (d) …; (e) hand-tool adjustment of a bolted end-plate connection." | — |
| Figure 1(a) | `image1.jpeg`, 926 × 695 px (292 dpi at print width) | replaced by `IMAGES_EXP/1.jpg`, **the same photograph** (pixel correlation 0.999) at native 1280 × 960 px, same Word crop, **404 dpi**. Not upsampled | "use original image files where available" |
| Figure 1(b–c) 299 dpi; Figure 2(c) 306; 2(d) 211; 2(e) 290 | — | unchanged; no higher-resolution originals exist in the project | **[AUTHOR ACTION]:** upload camera originals |

**[AUTHOR TO CONFIRM]:** the uncropped `image7.jpg` carries a camera overlay dated "21 Th7, 2026 10:20:18", the CP2 date. If this photo shows the B1 apex manipulation, it should become panel (b) instead of the repeated Figure 1(d) view.

## Step 4: metadata and AI disclosure

| Item | Change |
|---|---|
| Title block | Unchanged: the author's v8 edit (corresponding author Tri – Ngo Ngoc) is kept. No e-mail, ORCID or department was invented. The items are listed in the pre-submission audit §4 |
| AI disclosure (Acknowledgements) | Now names the tools supported by project records: **Claude (Anthropic)**, for drafting, methodological review of text, literature screening, consistency checking and editing (records: `PAPER1_EXPERIMENTAL_MODEL_AND_INSTRUMENTATION_SOURCE_NOTE.md` "Working source note for Claude Cowork"; `PAPER1_FINAL_COMPLETION_REQUIREMENTS_v5A.md`). **Consensus** (AI-assisted academic search), used to locate and verify candidate references. It also discloses the Figure 3 redraw. No claim is made about analysis code or the provenance of the original Figure 3, because there is no record; both are **[AUTHOR TO CONFIRM]** |
| Document properties | The title "Paper 1 — Buildings editorial manuscript" and subject "internal completion and Gate assessment" were internal metadata that would travel with the file. They are replaced by the manuscript short title and an empty subject and description |

## Step 5: data and code availability

The Data availability statement is **unchanged** ("available from the corresponding author upon reasonable request"): no public repository or DOI exists. The inventory and the repository recommendation are in the pre-submission audit §5.

## Step 6: new references (details in `PAPER1_v8.1_NEW_REFERENCE_AUDIT.md`)

| Ref. | Added text | Location |
|---|---|---|
| **26** Teloli RO et al., *Mech Syst Signal Process* 2022; 163: 108172 (Orion beam) | "Teloli et al. treated repeatability as an explicit design and test-practice objective for a bolted lap-joint benchmark and examined how tightening torque and excitation amplitude affect the identified stiffness and damping." | §2.3, after Brake et al. |
| 26 (second use) | "…repeatable measurement of bolted joints depends on joint design and test practice,²⁶ and holding out a campaign…" | §5.3 |
| **36** Zorzi S et al., *Struct Health Monit* 2025; 24(5): 3028–3045 | "Reliability-based metrics for SHM information quality judge monitoring output by how it changes the structural reliability assessment it informs,³⁶ which requires the characteristics of the measurement to be known." | §5.5 |
| **38** Wernitz S et al., *Struct Control Health Monit* 2022; 29(11): e3077 | "Robustness to environmental and operational variability, which cannot be fully evaluated under laboratory conditions,³⁸ was not examined." | §5.6, final paragraph |

KW51 (Maes et al.), Deng et al. 2023, Makhoul 2024 and Smith et al. 2017 were verified but **not added** (reasons in the reference audit).

**Renumbering.** All 38 references are renumbered by first citation:

- 1–25 are unchanged.
- v8 26–34 became 27–35.
- v8 35 (Johannes) became 37.

The text of all 35 existing entries is unchanged, and every citation resolves (38 cited = 38 listed).

## Step 7: knowledge advancement

| Location | v8 | v8.1 |
|---|---|---|
| Abstract | "The empirical contribution is a bounded account of connection-state separability and evaluation variability for this laboratory frame." | "Strong within-campaign separability thus did not establish transferable condition evidence; the contribution is an experimentally documented, bounded account of how the interpretation of such evidence changes once the acquisition hierarchy, held-out-run variability and acquisition context are retained." |
| §1, last paragraph but one | "For structural-inspection readers, the study shows why the reported classification evidence must retain its acquisition and evaluation context." | "The principle that strong within-campaign separability does not by itself establish transferable condition evidence is not new; the advancement reported here is its experimentally documented consequence for a bolted steel-frame vibration dataset, in which near-perfect feature-based separation within two campaigns coexists with weaker, run-dependent separation in a third and with exploratory transfer scores close to the chance level, so that the interpretation changes materially once the physical acquisition hierarchy, held-out-run variability and acquisition context are retained." |

The principle is explicitly **not** claimed as new. The Conclusions were not changed.

## Step 8: optional analysis

The manuscript contains **no** cross-campaign RF/SVM results (Table 7 covers deep models only), and the code archive holds none either: `signal-loro-cross-campaign-v1` contains only 1D-CNN and ResNet1D runs. **Nothing was run.** The recommendation is in the pre-submission audit §6.

## Step 9: targeted tightening (no limitation removed)

| Location | v8 | v8.1 | Where the content is retained |
|---|---|---|---|
| §2.4 | "The controls are not novel, and no claim is made that no previous study has combined them." | "Neither the controls nor their combination is claimed as novel." | — |
| §3.4 | two sentences on the RUN012 span and overlap | merged into one | same paragraph |
| §5.2 | three sentences restating the HPO dependence and the single seed | "The comparison carries the two asymmetries set out in Sections 3.9 and 4.2: only the deep models depend on prior hyperparameter development, and only the feature-based models were run at a single seed." | §3.9, §4.2, §5.4, §5.6 |
| §5.3 | two sentences restating the CP3 order-group caveat | one sentence with a cross-reference to §4.4 | §4.4 (full caveat), §5.6 |
| §5.4 | restatement of per-window standardisation | shortened, with a cross-reference to §3.6 | §3.6 |
| §5.5 | third paragraph repeating the three unverified provenance items | "…the provenance items that remain unverified (Section 4.1; Section 5.6) bound what the reported evidence can be used for." | §4.1 (four limits), §5.6 |

## Reproducibility detail added (reviewer risk: FFT-band reproducibility)

The executed extractor, `src/lib/ml/features.py` in the archived Kaggle code bundle (consistent with IT-03), defines the band groups as `np.linspace(0, 201, 13)` over the 201 `rfft` bins. §3.6 now states:

- the twelve bands are "the fraction of the total spectral power, after a Hanning window and with the DC component set to zero, falling in each of twelve contiguous groups of 16 or 17 FFT bins, about 4.2 Hz wide, spanning 0 Hz to the 50 Hz Nyquist frequency";
- the pair feature "equals their zero-lag Pearson correlation coefficient". The extractor z-scores with the population SD, so the mean product is exactly Pearson's r.

No computation was rerun.

## Not changed

- Tables 1–7 and A1–A7.
- Figures 1 (apart from the higher-resolution 1(a) file), 4, 5 and 6.
- §3.9.
- Results (§4) apart from nothing.
- The Conclusions.
- Statements and Declarations.
- The data-availability wording.
- Table 3 counts.
- The locked framing.
