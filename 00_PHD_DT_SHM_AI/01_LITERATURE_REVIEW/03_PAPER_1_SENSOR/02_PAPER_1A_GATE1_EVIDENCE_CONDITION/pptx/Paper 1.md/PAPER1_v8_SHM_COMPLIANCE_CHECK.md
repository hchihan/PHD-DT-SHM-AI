# PAPER1 v8 (Structural Health Monitoring, SAGE): compliance check

**File checked:** `PAPER1_v8_SHM_SUBMISSION.docx` (12 September 2026)
**Package:** passes Office XSD validation against the v7 original, and opens and exports in Microsoft Word 16. Word reports 29 pages, 18 table objects (Table 2 is three sub-tables), 12 embedded images and 13,211 words in total.
**Automated consistency checks:** **146 PASS, 0 FAIL** (script `check_v8.py`; categories in section 3).

Status key: **PASS** = satisfied in the file. **AUTHOR** = the file carries compliant text, but only the author can confirm it or supply the missing detail before upload. **NOTE** = optional or informational.

---

## 1. SAGE / Structural Health Monitoring author-guideline requirements

| # | Requirement (SHM author instructions, 12 Sep 2026) | Status | Evidence in v8 |
|---|---|---|---|
| 1 | Original Research Article with introduction, methodology, results, discussion | PASS | §1–§6 unchanged in structure |
| 2 | Word file; heading levels clear; no template required | PASS | .docx; Heading 1 / Heading 2 numbered hierarchy; MDPI running header removed |
| 3 | Title concise and accurate | PASS | Title unchanged from v7 |
| 4 | Unstructured abstract | PASS | One paragraph, 199 words |
| 5 | At least 5 keywords after the abstract | PASS | 7 keywords |
| 6 | Sage Vancouver reference style; every citation listed and vice versa | PASS | 35 numbered references in order of first citation. Superscript citations after punctuation. 35/35 cited, 0 orphan citations, 0 author–year remnants |
| 7 | "Statements and Declarations" with all six sub-headings, "Not applicable" where relevant | PASS | Ethical considerations · Consent to participate · Consent for publication · Declaration of conflicting interest · Funding statement · Data availability, in that order, after Acknowledgements |
| 8 | Funding statement mandatory, even if nil | PASS / **AUTHOR** | SAGE nil wording is inserted. **Confirm that no scholarship, grant or institutional funding supported the work.** If it did, replace the statement with the funder name and grant number, which the submission form also asks for |
| 9 | Conflicting-interest declaration | PASS / **AUTHOR** | SAGE standard nil wording. Confirm for all three authors |
| 10 | Data availability statement (sharing encouraged; justify if not shared) | PASS / **AUTHOR** | "available from the corresponding author upon reasonable request". SAGE encourages a public repository. The IT audit shows versioned dataset files already exist on the execution platform. Decide whether to deposit and cite a DOI or URL, or state why sharing is not possible |
| 11 | AI disclosure per SAGE AI policy; AI not an author | PASS / **AUTHOR** | The disclosure is under Acknowledgements (policy: "within the methods or acknowledgements"). It names the uses listed in v7 and states author verification and responsibility. The v7 Methods §3.11 has been removed. **See F-8.** |
| 12 | Figures numbered consecutively in order of mention | PASS | Figures 1–6, first mentioned in order |
| 13 | Figure resolution 300 dpi | PASS (Figs 3–6) / **AUTHOR** (Figs 1–2) | Embedded effective resolution at printed size: Fig 3 379 dpi, Fig 4 426, Fig 5 426, Fig 6 453. Photographs: Fig 1a 292, Fig 1b–c 299, Fig 1d 398, Fig 2a 399, Fig 2b 410, Fig 2c 306, **Fig 2d upper 211**, Fig 2d lower 290. Upload the original camera files for Figures 1–2 as figure files; do not upsample |
| 14 | Supplemental material optional | NOTE | Appendix A kept in the article, after the References (SAGE convention) |
| 15 | Single-anonymised review; author identity retained | PASS | Author block kept |
| 16 | Author metadata must exactly match the submission system; ORCID for submitting author | **AUTHOR** | See F-6: name form and order, department, corresponding e-mail and ORCID |
| 17 | Cover letter; figure, table and word counts; funder; preprint DOI | **AUTHOR** (separate from manuscript) | Counts in section 5 |

## 2. Revision-brief requirements

| # | Brief item | Status | Evidence |
|---|---|---|---|
| 1 | Apply all verified IT-01 to IT-06 corrections | PASS | Changelog §A: 27 IT-linked edits. The three IT-06 cells and the §4.5 restatement are corrected: Table 5 0.639; Table A3 0.870 and ±0.114; §4.5 0.870 |
| 2 | Remove obsolete IT placeholders; keep genuine residual limitations | PASS | 0 occurrences of `IT-0`, `[IT`, `AUTHOR-EXP`, highlight or placeholder colour. The residual limitations are stated in §4.1 (four limits), §5.5 and §5.6: training-time byte identity, physical sensor-to-position mapping, pre-export synchronisation, and window-mean arithmetic. The AUTHOR-EXP limitation sentences are kept verbatim |
| 3 | Keep the locked framing (generalisation limits + provenance-aware condition evidence) | PASS | The abstract closing sentence states the condition-evidence condition. Conclusions and Discussion are unchanged in substance. No new claim or result was introduced |
| 4 | No new analyses, reruns, scope expansion, calibrated FEM, field diagnosis, severity or RUL | PASS | All result values unchanged except the three IT-06 corrections. "Severity", "field damage" and "remaining service life" appear only as explicit exclusions |
| 5 | Convert to current SHM requirements | PASS | Section 1 |
| 6 | Table 3 execution counts unchanged | PASS | 540 / 180 / 72; cases × splits × seeds = fits for every row |
| 7 | 972 not used as an execution count | PASS | 972 appears once (§4.1), only as the disjointness-audit scope |
| 8 | Remove the 294 claim; use the approved 192 sentence | PASS | "294" appears 0 times. The locked sentence appears verbatim in §3.8 and §4.1, with the sensor-subset exclusion stated so 192 is not read as the whole archive |
| 9 | Final numerical, citation, cross-reference and figure/table checks | PASS | Section 3 |

## 3. Automated check results (146 / 146 PASS)

| Category | What was verified |
|---|---|
| Residual tokens (13) | No `IT-0`, `[IT`, `AUTHOR-EXP`, `294`, `[Bản nháp]`, Vietnamese IT table, MDPI header, highlight, placeholder colour or square-bracket placeholders. Header cleared. Locked 192 sentence present. 972 appears once, with audit framing |
| Citations (7) | First appearances run 1→35 in order. Reference list numbered 1–35. Cited set equals listed set. No author–year remnants. Superscripts contain only citation numbers. No uncited reference |
| Cross-references (7) | Every "Section x.y" target exists. Every cited Table or Figure has a caption. Figure captions run 1–6 and table captions 1–7 then A1–A7. Figures and main tables are first mentioned in numerical order |
| Table 4 ↔ Table 6 (12) | The mean of each Table 6 row equals the Table 4 balanced accuracy (±0.001) |
| §4.4 text ↔ Table 6 (5) | CP3 order-group means (0.944/0.806, 0.778/0.611, 0.583/0.491, 0.444/0.417). RUN012 is the lowest CP2 fold for all four models |
| Table 5 (18) | Mean of seeds consistent with the Mean column; pooled column equals Table 4 Macro-F1; each fold value is below pooled, as §4.3 states |
| Table 7 ↔ Table A5 (15) | Seed means, seed SD (n − 1) and smallest p per row. Null-mean range 0.2495–0.2506. Smallest p 0.167, none below 0.05. Abstract range 0.227–0.278 |
| Table A7 ↔ Tables A3 / 4 (32) | Row sums 18 or 54. Trace/total equals Table 4 accuracy for all 12 model–campaign cells. For single-seed RF and SVM, per-class F1 from the counts equals Table A3 and Macro-F1 equals Table 4. CP3 RF precision and recall (0.714 / 0.722). §4.5 CP2 1D-CNN counts (17 / 16) |
| Counts and arithmetic (8) | Windows 1,746 + 3,065 + 2,088 = 6,899. QC 149 recordings and 951 samples. Table 3 arithmetic. Audit scopes reconcile with the design (612 = 540 + 72; 360 = 4 × 3 × 30; 972 = 612 + 360; 192 = 6 × 30 + 12). Feature dimensions 228 / 366. §5.2 differences 0.185 / 0.124 / 0.203 |
| IT-06 values (6) | 0.639, 0.870 (Table A3 and §4.5) and ±0.114 present; 0.640 (Table 5), 0.871 and ±0.115 absent |
| SAGE structure (15) | Required sections present. Back-matter order Conclusions → Acknowledgements → S&D → References → Appendix. S&D sub-headings in SAGE order. At least 5 keywords. Line numbering on |

## 4. Items flagged but not changed (need the author or source files)

| ID | Item | Why it was not changed | Suggested action |
|---|---|---|---|
| F-1 | Appendix tables are first cited in the order A1, A4, A2, A3, A7, A5, A6. v7 already had this order | Renumbering touches text, captions and the Figure 6 caption. SAGE's consecutive-numbering rule is stated for figures | Optional: renumber A2–A7 by first mention |
| F-2 | **Figure 2(b) (B1 apex manipulation) is the same embedded photograph as Figure 1(d) (apex sensor mounting)**: identical file `image2.jpg` | Only the author knows whether a distinct B1 photograph exists | Replace 2(b) with the B1-state photograph, or state in the caption that the same view is shown |
| F-3 | Figure 2(d) holds two photographs under one label | Figure layout decision | Label them (d) and (e), or add "two views" to the caption |
| F-4 | **The Figure 3 image text** "Window-wise standardisation / Training data only" can be read as a training-fitted standardisation. That contradicts §3.6: per-window standardisation is applied to all partitions, and only the SVM scaler is fitted on training data | The figure is a raster image; editing it needs the source file. The caption is consistent | Edit the source diagram, e.g. "Per-window standardisation (all partitions) · SVM scaler fitted on training data only". This also makes it consistent with the §3.7 checkpoint rule |
| F-5 | Photo resolution below 300 dpi at printed size (Fig 2d upper 211 dpi; Figs 1a and 1b–c just under 300) | Upsampling is not acceptable | Upload the original camera images as separate figure files |
| F-6 | **Title page.** Author names are in the v7 form "Han – Ho Chi; Tri – Ngo Ngoc; Duc – Pham Anh" (only the hyphen in the second name was normalised). The affiliation has no department or faculty. **No corresponding-author e-mail. No ORCID** | Identity data must match the submission system exactly | Confirm the final name form and order as it should appear in print, add the department, and add the corresponding e-mail and ORCID iD(s) |
| F-7 | Funding, conflict-of-interest and data-availability wording are SAGE defaults | Only the authors can attest to them | See section 1, items 8–10 |
| F-8 | The AI disclosure lists the uses from v7 but does not name the tools | Tool names and versions are not recorded in the project. SAGE requires disclosure when generative AI produces content that affects methodology, analysis or results, and prohibits AI-generated images presented as novel research images | Add the tool names and versions. **Confirm whether any figure (e.g. the Figure 3 schematic) or the analysis code was produced with generative AI.** If so, extend the disclosure |
| F-9 | IT-06 computed SDs "COMPUTED_NOT_REPORTED" were not added to Table A3 | `METRIC_AGGREGATION_CHECK.csv` and the other IT deliverables linked from `BAO_CAO_IT01_IT06.md` (e.g. `DATASET_REGISTRY_FINAL.csv`, the `evidence/` folder) were not found in any project folder searched (D:\01_RESEARCH, the H: PhD tree, Downloads) | Optional. If you add them, take the values from the IT deliverable CSV |
| F-10 | IT evidence files are referenced but not archived with the paper | As F-9 | Archive the IT deliverables with the paper. They back several §4.1 statements and would support a data-availability deposit |
| F-11 | DOIs omitted from references with volume and pages (SAGE Vancouver) | Style rule | If the editorial office asks for DOIs, all 34 are listed in the changelog, section F |
| F-12 | The official SAGE Vancouver PDF returns 404 | Rules were taken from the SAGE–NLM/Vancouver CSL (superscript, 3 authors then et al., abbreviated italic journal, `Year; Vol(Issue): pages`) plus SAGE guidance (superscript after punctuation for STM) | SAGE copy-editing normalises remaining details. No action needed |
| F-13 | Continuous line numbering was added | Not required by SHM; added for reviewers | Remove in Layout → Line Numbers if you don't want it |
| F-14 | Internal residual, not in the manuscript: the historical SD_fold export script was not located | IT-06 shows that ddof = 1 reproduces every reported SD_fold | None for submission; keep on file |

## 5. Submission-form data

| Field | Value |
|---|---|
| Article type | Original Research Article |
| Title | Run-Aware Evaluation of Vibration-Based Connection-State Classification: Within-Campaign Performance and Cross-Campaign Limits on a Scaled Bolted Steel Frame |
| Abstract | 199 words, unstructured |
| Keywords | 7 |
| Main text (Introduction–Conclusions) | 9,405 words, excluding tables and captions (515 caption words) |
| Figures | 6 |
| Tables | 7 in the main text plus 7 in Appendix A (A1–A7) |
| References | 35 |
| Pages (Word, A4) | 29 |
| Supplementary files | None (Appendix A in-article) |
| Still to prepare outside the manuscript | Cover letter; funder and grant number (if any); ORCID; high-resolution figure files for Figures 1–2 (and a corrected Figure 3 source, F-4) |
