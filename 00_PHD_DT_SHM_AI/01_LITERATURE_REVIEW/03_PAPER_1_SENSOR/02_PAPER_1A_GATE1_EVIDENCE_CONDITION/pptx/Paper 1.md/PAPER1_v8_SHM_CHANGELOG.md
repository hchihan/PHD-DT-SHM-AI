# PAPER1 v8 (Structural Health Monitoring, SAGE): changelog

**Date:** 12 September 2026
**Output:** `PAPER1_v8_SHM_SUBMISSION.docx`
**Source manuscript:** `PAPER1_v7_Buildings_Drafting.docx`. No file named `PAPER1_v7_Buildings_Drafting(2).docx` exists in the project or in Downloads. The only other v7 copy, `Downloads\PAPER1_v7_CITATION_COMPLETED.docx`, is byte-identical to the source.
**Overriding technical evidence:** `BAO_CAO_IT01_IT06.md` (IT-01 to IT-06).
**Locked decisions applied without re-asking:** `PAPER1_v8_EDITING_DECISIONS_LOCKED.md` (Decisions 1 and 2).
**Journal requirements:** `SHM_AUTHOR_GUIDELINES_CHECKLIST_2026-09-12.md`, SAGE AI policy (fetched 12 Sep 2026), and the SAGE Vancouver CSL definition. The SAGE Vancouver PDF now returns 404 on both SAGE domains.

## Scope guard

The following were not done in this revision:

- No new analysis, model rerun, re-selection of candidates or checkpoints, or change of scope.
- No calibrated FEM, field diagnosis, severity or RUL content.

Other constraints held:

- **Numbers:** result values are unchanged except the three IT-06 cells.
- **Framing:** the locked framing (generalisation limits plus provenance-aware condition evidence) is unchanged.
- **Table 3:** execution counts are unchanged (540 / 180 / 72).
- **972:** it is not used as an execution count anywhere.

The edits were applied to the v7 XML in place (49 logged edits), so v7 styles, tables and figures are preserved. The package passes the Office XSD validation.

---

## A. IT-01 to IT-06 corrections

| IT | Location in v8 | v7 text / value | v8 text / value | Basis in IT report |
|---|---|---|---|---|
| IT-01 | §3.5, dataset paragraph | Substitute recording stated only as "one B1 recording is a substitute acquired on 29 Jul 2026" | Adds the identity: RUN012/REC0004, B1, BEAT_L1. It **replaces** a recording within the 72 of CP2 and is not a 73rd. Compared with all 72 CP3 recordings: no whole-file or full-array duplicate, no identical contiguous 400-sample segment, longest identical segment 22 samples | IT-01 details |
| IT-01 | §3.5, QC paragraph | none | "Rebuilding the windows from the canonical files reproduces these counts and the stored window tensors (Section 4.1)." | IT-01: 6,899 windows and 951 samples in 149 recordings reproduced |
| IT-01 | §4.1, paragraph 2 (new text) | "Agreement between the registry and the files actually loaded during training is therefore specified and not verified [IT-01]" | Reconciliation stated: 216 unique IDs, 216 distinct source paths and SHA-256 hashes, and recomputed source/canonical hashes match the registry. The window rebuild reproduces the tensors of all 216 recordings (6,899 windows). The 102 stored files, which cover sensor configurations and are not recordings, match the registry locally and as downloaded from the training platform | IT-01 conclusion "Đã được" |
| IT-01 | §4.1, paragraph 3 (new); §5.5; §5.6 | none | **Residual limit kept:** there is no per-file hash at load time, so byte identity with the files loaded at training time is not established | IT-01 "Chưa được" |
| IT-02 | §3.3, sensing paragraph | "a fourth channel holding the resultant magnitude was derived during the dataset build" | The resultant is in the PASCO-exported CSV and was copied unchanged, **not computed** by the build. Channel order per block is x, y, z, resultant. The force column is not used. Block order can vary per recording, and the build code assigns position labels from the gravity orientation of each block, with the map kept per recording | IT-02 details and "Cần xử lý" |
| IT-02 | §3.3, configuration paragraph | none | "With four channels per sensor, the model inputs have eight channels in CP1 and twelve in CP2 and CP3." | IT-02 table |
| IT-02 | Table 1, accelerometer row | "…acc_z and derived acc_resultant" | "…acc_z and acc_resultant, as exported in the source CSV files" | IT-02 |
| IT-02 | §4.1, paragraph 3; §5.5; §5.6 | "[IT-02]" placeholder | **Residual limit kept:** no device record links a CSV block to the serial number and mounting position of a unit, so the physical mapping is not independently confirmed | IT-02 "Chưa được" |
| IT-03 | §3.6, feature paragraph | "The dimension actually used for the twelve-channel case … is not asserted [IT-03]" | Full executed definition: 10 time-domain statistics (named), 12 relative FFT band powers (Hanning window, DC zeroed) and 3 spectral descriptors (centroid and dominant frequency as fractions of Nyquist) give 25 per channel. One mean-product feature per channel pair. **228** for 8 channels (200+28) and **366** for 12 channels (300+66). Confirmed against all 360 executed feature-based fits (180 in Table 3 plus 180 in Table A4) | IT-03 |
| IT-03 | Appendix A, note below Table A2 | 228 only | 228 (CP1) and 366 (CP2, CP3), with the 25-per-channel composition | IT-03 "Còn cần làm" |
| IT-04 | §3.6, channel-combination paragraph | "concatenated along the channel axis of a shared window index … [IT-04]" | Combined **by CSV row / sample index**: columns reordered without changing row membership, the common valid row prefix kept, and windows cut at identical offsets. No timestamp join, interpolation, resampling or delay correction. The window start timestamp is metadata only. Explicitly *not* described as time synchronisation | IT-04 "Cần xử lý" |
| IT-04 | §3.4, RUN012 paragraph | "measured timestamps … retained separately in the source files" | Source timestamps are retained in `timestamp_original`, and the synthetic sequence was not used to realign the signals | IT-04 details |
| IT-04 | §4.1, paragraph 3; §5.5; §5.6 | "[IT-04]" | **Residual limit kept:** how the PASCO software synchronised the wireless units before export is undocumented | IT-04 "Chưa xác nhận" |
| IT-05 | §3.7, feature-based parameters | "…probability or score construction and any calibration random state require confirmation [IT-05]" | RF and SVM both use `random_state = 42` and `predict_proba`. SVM probabilities come from built-in SVC estimation (`probability = True`). No further calibration | IT-05 table |
| IT-05 | §3.7, deep-model paragraph | "early stopping with patience 10 on validation loss" | Seeds 42/43/44 and softmax output. **The checkpoint is saved only when window-level validation loss decreases AND recording-level validation BA > 0.25.** Patience 10 applies once a valid checkpoint exists; 80 epochs maximum | IT-05 "Chưa đúng trong Methods" |
| IT-05 | §3.8, fitting paragraph | "The test partition is read once, after the best checkpoint has been restored." [IT-05] | Test data are **loaded before training**, but test **inference** happens only after the checkpoint is restored. No test quantity enters checkpointing, early stopping or candidate selection. All four models average window probabilities; none averages decision scores or votes | IT-05 "Chưa đúng trong Methods" |
| IT-05 | §3.8, selection paragraph | "…then split identifier." | "…then ascending split identifier as the final tie-break." | IT-05 "ghi đúng split_id làm tie-break cuối" |
| IT-05 | §4.1, paragraph 1 | none | The checkpoint metadata of all 612 deep-model fits were reproduced (= 540 + 72 in Table 3) | IT-05 |
| IT-05 | Table A2 (RF, SVM, 1D-CNN, ResNet1D rows) | "fixed random state"; "…to be verified [IT-05]"; "patience 10" | `random_state = 42` with `predict_proba`, and no further calibration. SVM `probability = True`. Deep rows: "checkpoint rule and patience 10 as in Section 3.7 … seeds 42, 43, 44; softmax outputs" | IT-05 |
| IT-05 | §4.2, second paragraph; §5.6 | "SVM calibration and output route require code confirmation [IT-05]" | Removed. The single-seed and RF seed-sensitivity limitation is retained | IT-05 |
| IT-06 | **Table 5**, CP1 / RUN006 / 1D-CNN mean | 0.640 | **0.639** | IT-06 (exact 0.6394841) |
| IT-06 | Table 5 caption | none | "Means are computed from unrounded per-seed values." The mean of the *displayed* seeds, 0.6397, would round to 0.640, so the caption prevents an apparent inconsistency | Follows from the IT-06 exact-fraction check |
| IT-06 | **Table A3**, CP1 / ResNet1D / B3 F1 | 0.871 | **0.870** | IT-06 (exact 0.8704984) |
| IT-06 | **§4.5** (restatement of the same F1) | "0.866 and 0.871" | "0.866 and **0.870**" | IT-06 "Cần xử lý" |
| IT-06 | **Table A3**, CP3 / ResNet1D / B3 SD_seed | 0.754 ± 0.115 | 0.754 ± **0.114** | IT-06 (exact 0.1144831) |
| IT-06 | §3.10 | "SD_fold … [IT-06: confirm the SD denominator from the reporting script]" | SD_seed and SD_fold are both defined as sample SD with denominator n − 1 | IT-06: ddof = 1 confirmed for SD_seed and reproduces all SD_fold values |
| IT-06 | §4.1, paragraph 2 | none | Of the 472 reported values in Tables 4–7, A3, A4 and A7, all agree with recomputation from stored recording-level predictions within rounding. Permutation p-values were not recomputed | IT-06 (469/472 matched v7; the 3 mismatches are now replaced by recomputed values) |
| IT-06 | §4.1, paragraph 3 | none | **Residual limit kept:** window-to-recording averaging is confirmed in code, but per-window probabilities were not archived, so that step cannot be recomputed arithmetically | IT-06 "Chưa thể tính lại" |

**IT-06 items deliberately not added.**

- **SD values computed but not reported.** The IT deliverable `METRIC_AGGREGATION_CHECK.csv`, which holds the `COMPUTED_NOT_REPORTED` values, is not present anywhere in the project folders, so no new SD cells were added. The Table A3 caption already states that a missing SD does not mean zero variation.
- **SD_fold export script.** The original script was not located. The manuscript states the ddof = 1 definition, which reproduces every reported SD_fold. That the historical script itself used ddof = 1 is recorded here as an internal residual rather than in the manuscript.

## B. Locked decisions

| Decision | Where applied | Result |
|---|---|---|
| 1. Remove the 294-candidate claim | §3.8 (v7: "…reproduced all 294 selected candidates across the wider evaluated archive…") and §4.1 (v7: "all 294 candidate selections were reproduced…") | Both removed. The verbatim locked sentence "Within the audited scope, 192 stored candidate selections were reproduced from validation quantities alone." appears in §3.8 and §4.1. §3.8 adds "Evaluations of sensor subsets, which lie outside this paper, were not part of that audit." so 192 is not presented as the whole archive. The token "294" no longer occurs anywhere |
| 2. No 972 as an execution count | §4.1 only | 972 appears once: "The training, validation and test run sets are disjoint in every one of the 972 fits examined in the source audit…" Table 3 is untouched (540 / 180 / 72) |

**Consistency note for the author, not written into the manuscript.** The audit scopes reconcile with the design:

- 612 deep-model fits = 540 + 72 (Table 3).
- 360 feature-based fits = 4 models × 3 campaigns × 30 splits.
- 972 fits = 612 + 360.
- 192 selections = 6 test runs × (18 deep + 12 feature-based model–campaign–seed cells) + 12 cross-campaign.

This supports the §4.1 statement that the 972-fit scope includes the Table A4 models.

## C. Placeholders and draft markup removed

| Item | Action |
|---|---|
| "[Bản nháp]" draft marker (first line) | Removed |
| `[IT-01]`, `[IT-02]`, `[IT-03]`, `[IT-04]`, `[IT-05]` (×5), `[IT-06]`, `[IT-01–IT-05]` (×2) | All removed. The text was replaced with verified content (section A) or with the named residual limitation |
| `[AUTHOR-EXP]` tags in §3.2 and §3.3 (×3) | Tag removed. The **limitation sentences are kept verbatim**: L1/L2 definition, drive amplitude, signal-source model, sensor-axis orientation, wave-driver attachment point, and the absence of a torque or assembly log |
| Yellow highlighting (37 runs) and dark-orange placeholder colour (all runs) | Removed |
| Internal Vietnamese IT checklist table after the references | Removed |
| Running header "Paper 1 \| Editorial working manuscript \| 9 September 2026" | Cleared. The footer page number is kept |
| §3.11 "Use of generative AI tools" (Methods) | Removed from Methods and rewritten as the AI disclosure under Acknowledgements (see D) |

## D. SHM / SAGE conversion

| Area | Change |
|---|---|
| References | 35 MDPI author–year entries became 35 **SAGE Vancouver** entries, numbered in order of first citation. Author format is "Surname Initials", with the first three authors then "et al." when there are four or more. NLM journal abbreviations are italic, in the form `Year; Vol(Issue): pages.` Proceedings use `In: … , city, dates, pp.x–y. Publisher.` DOIs are omitted where volume and pages exist, per SAGE Vancouver; they are kept in section F for the editorial office |
| In-text citations | 60 author–year citations became superscript numbers, placed after punctuation (STM variant), sorted and collapsed (e.g. ³⁻⁷). Narrative citations keep the name ("Zhang et al.³ trained…"). All 35 references are cited, and every citation resolves |
| Keywords | 7 (minimum 5): vibration-based structural health monitoring; bolted steel frame; connection-state classification; leave-one-run-out evaluation; grouped cross-validation; experimental provenance; condition evidence |
| Abstract | Stays unstructured (199 words). Only the closing sentence was rewritten to carry the locked framing: "Such output can serve as condition evidence for inspection only when its acquisition provenance, evaluation scope and observed variability are reported with it; the results do not validate field diagnosis or maintenance decisions." |
| Acknowledgements (new) | Holds the AI disclosure, since SAGE policy puts it "within the methods or acknowledgements". It lists the v7 uses (drafting assistance, methodological review, literature screening, consistency checking, editing), author review and responsibility, reference verification, and that no AI is listed as an author |
| Statements and Declarations (new) | All six SAGE sub-headings, in order: Ethical considerations (Not applicable, with reason); Consent to participate (Not applicable); Consent for publication (Not applicable); Declaration of conflicting interest (SAGE standard nil wording); Funding statement (SAGE standard nil wording); Data availability (on reasonable request). **Author confirmation is needed for the COI, funding and data wording** (see the compliance file) |
| Section order | Conclusions → Acknowledgements → Statements and Declarations → References → Appendix A. In v7, Appendix A came before the References |
| Title block | Affiliation gains "Da Nang, Vietnam". The author separator is made consistent ("Tri – Ngo Ngoc"). Placeholder colouring is removed. Names are otherwise unchanged |
| Layout | Continuous line numbering added for review. The Reference style's hanging indent is widened for the numbers. Heading hierarchy (Heading 1 / Heading 2) is unchanged and unambiguous |

## E. Reference corrections found in the Crossref check (all 34 DOIs queried)

| v8 no. | Reference | v7 | v8 (Crossref) |
|---|---|---|---|
| 8 | Wheat et al., *IEEE Access* 2024 | pages 169883–169892 | **169879–169895** |
| 6 | Parziale et al., *Structures* 2024 | second author "Lomazzi, L." | **Silva PH** (confirmed by Crossref and the SSRN preprint record) |
| 3, 5, 13, 15, 20, 22, 2, 26, 27 | Zhang 2020; Biswal 2022; Vabalas 2019; Ramasso 2025; Tougui 2021; Eraliev 2022; Jia 2023; da Silva 2024; Ozdagli 2020 | issue number missing | issue added: 19(4); 21(2); 14(11); 24(4); 27(3); 22(3); 23(21); 10(1); 12(1) |
| 15, 26 | Ramasso 2025; da Silva 2024 | "de Oliveira Teloli, R." | "Teloli RO" (Crossref family name Teloli) |
| 3, 4, 26, 29 | Zhang (online 2019), Pal (online 2021), da Silva (online 2023), Sohn (online 2006) | issue year | Issue year kept (2020, 2022, 2024, 2007), as in v7 |

## F. Citation map and DOIs (v8 number → source)

| No. | Reference | DOI |
|---|---|---|
| 1 | Avci et al. 2021 | 10.1016/j.ymssp.2020.107077 |
| 2 | Jia and Li 2023 | 10.3390/s23218824 |
| 3 | Zhang et al. 2020 | 10.1177/1475921719881237 |
| 4 | Pal et al. 2022 | 10.1002/stc.2873 |
| 5 | Biswal et al. 2022 | 10.1177/14759217211009217 |
| 6 | Parziale et al. 2024 | 10.1016/j.istruc.2024.107583 |
| 7 | Yang et al. 2014 | 10.1061/(ASCE)ST.1943-541X.0000831 |
| 8 | Wheat et al. 2024 | 10.1109/ACCESS.2024.3497716 |
| 9 | Vieira et al. 2026 | 10.1016/j.ymssp.2026.114640 |
| 10 | Matania et al. 2024 | 10.36001/phme.2024.v8i1.4125 |
| 11 | Beleites et al. 2013 | 10.1016/j.aca.2012.11.007 |
| 12 | Varma and Simon 2006 | 10.1186/1471-2105-7-91 |
| 13 | Vabalas et al. 2019 | 10.1371/journal.pone.0224365 |
| 14 | Brake et al. 2019 | 10.1016/j.ymssp.2019.04.020 |
| 15 | Ramasso et al. 2025 | 10.1177/14759217241259668 |
| 16 | Limongelli 2020 | 10.1007/s13349-020-00439-8 |
| 17 | Makhoul 2022 | 10.1186/s43251-022-00068-9 |
| 18 | Kamariotis et al. 2024 | 10.1017/dce.2024.24 |
| 19 | Naresh et al. 2023 | 10.1111/str.12439 |
| 20 | Tougui et al. 2021 | 10.4258/hir.2021.27.3.189 |
| 21 | Amin et al. 2026 | 10.1038/s41598-026-58967-0 |
| 22 | Eraliev et al. 2022 | 10.3390/s22031210 |
| 23 | Combrisson and Jerbi 2015 | 10.1016/j.jneumeth.2015.01.010 |
| 24 | Ojala and Garriga 2009 | 10.1109/ICDM.2009.108 |
| 25 | Demšar 2006 | none (JMLR 7: 1–30) |
| 26 | da Silva et al. 2024 | 10.1115/1.4063794 |
| 27 | Ozdagli and Koutsoukos 2020 | 10.36001/phmconf.2020.v12i1.1184 |
| 28 | Goodarzi et al. 2025 | 10.5194/jsss-14-119-2025 |
| 29 | Sohn 2007 | 10.1098/rsta.2006.1935 |
| 30 | Keshmiry et al. 2023 | 10.3390/buildings13040918 |
| 31 | Breiman 2001 | 10.1023/A:1010933404324 |
| 32 | Cortes and Vapnik 1995 | 10.1007/BF00994018 |
| 33 | Kiranyaz et al. 2021 | 10.1016/j.ymssp.2020.107398 |
| 34 | He et al. 2016 | 10.1109/CVPR.2016.90 |
| 35 | Johannes et al. 2021 | 10.1061/(ASCE)CO.1943-7862.0002112 |

## G. Deliberately unchanged

- **Tables:** Tables 1–4, 6, 7 and A1, A4–A7 keep their values, apart from the Table 1 channel-label wording. Table 3 is identical.
- **Figures:** Figures 1–6 are unchanged; the embedded images were not edited (see compliance items F-2 to F-4).
- **§3.9:** the hyperparameter-development dependence and all its disclosures are unchanged. IT-05 explicitly does not remove this dependence.
- **Discussion and Conclusions:** unchanged in substance; only the placeholder paragraphs in §5.5 and §5.6 were rewritten.
- **Retained v7 limitation statements:** RF single seed; hyperparameter reuse in 15/18 folds and all cross-campaign cases; unmeasured window-split inflation; CP1 transfer not evaluated; campaign confounding; the CP3 order groups; no torque, preload or modal data; amplitude invariance; no quantitative transfer to full scale.
