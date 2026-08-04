# Zotero Writeback Queue
**Date:** 2026-07-18  
**Status:** Pending. Zotero MCP is in local-only mode; writes require `ZOTERO_API_KEY` and `ZOTERO_LIBRARY_ID` (hybrid/web mode).  
**Safety:** Do not write directly to the Zotero SQLite database.

## Writeback Rule

- Apply `DEEP_READ`, `FULLTEXT`, and `VERIFIED` only to the 19 complete target full texts below.
- Do not apply `DEEP_READ` to HTML-only records, incomplete standards, or `43648CQ8`.
- Do not create `RQ4`.
- Apply metadata corrections only from `08_DUPLICATE_AND_METADATA_CORRECTION_LOG_20260718.csv`.

## RQ1 / WP1 / Paper 1 / Gate 1

### `L97BIAI3`

**Tags:** `RQ1 WP1 PAPER1 GATE1 METHODOLOGICAL LAB_EVIDENCE DEEP_READ FULLTEXT VERIFIED LEAKAGE`

**Child note title:** `DEEP READ - LIMITED-FEM`

- Date: 2026-07-18
- RQ/WP/Paper/Gate: RQ1/WP1/Paper 1/Gate 1
- Evidence role: METHODOLOGICAL
- Evidence type: LAB_EVIDENCE
- Claim ID: C1-12/C1-15
- Claim: Effective sample size is the number of independent runs/groups, not derived windows.
- Evidence: Hierarchical patient/batch analysis, learning curves, and uncertainty calculations; PDF pp. 1-10.
- Validation: Repeated five-fold and batch-wise validation plus simulations.
- Limitation: Raman spectroscopy; no exact steel-frame LORO design.
- Allowed use: Justify run-level effective sample size and restrained uncertainty claims.
- Prohibited inference: Approximately six runs/class prove precise performance or model superiority.
- Relevant pages: PDF 1-10; published 25-33.
- Duplicate status: Replaces trashed same-DOI item `ZZHLGT9A`.
- Metadata corrections: None required.

### `PZ937I73`

**Tags:** `RQ1 WP1 PAPER1 GATE1 METHODOLOGICAL LAB_EVIDENCE DEEP_READ FULLTEXT VERIFIED LEAKAGE`

**Note:** Date 2026-07-18; RQ1/WP1/Paper 1/Gate 1; METHODOLOGICAL; LAB_EVIDENCE; Claim C1-15: small samples can exceed theoretical chance. Evidence: Gaussian-noise and baseline MEG/iEEG classifications with binomial/permutation thresholds, PDF pp. 3-10. Validation: 5/10-fold, LOO, repeated CV, 10,000 permutations. Limitation: no correlated run-window hierarchy. Allowed use: justify run-level empirical null. Prohibited inference: nominal above-chance accuracy proves reliable condition evidence. Duplicate: NOT_DUPLICATE. Metadata correction: none.

### `9XNSNIPX`

**Tags:** `RQ1 WP1 PAPER1 GATE1 METHODOLOGICAL LAB_EVIDENCE DEEP_READ FULLTEXT VERIFIED LEAKAGE`

**Note:** Date 2026-07-18; RQ1/WP1/Paper 1/Gate 1; METHODOLOGICAL; LAB_EVIDENCE; Claim C1-16: paired classifier tests require independent paired units. Evidence: Wilcoxon/Friedman assumptions and examples, JMLR 7 (2006), pp. 1-15. Limitation: independent datasets are not overlapping LORO folds. Allowed use: fair comparison and multiplicity control. Prohibited inference: six fold scores prove general superiority. Duplicate: NOT_DUPLICATE. Metadata correction pending: one author Janez Demsar; 2006; JMLR 7:1-30.

### `ZLFATP2Z`

**Tags:** `RQ1 WP1 PAPER1 GATE1 METHODOLOGICAL LAB_EVIDENCE DEEP_READ FULLTEXT VERIFIED LEAKAGE`

**Note:** Date 2026-07-18; RQ1/WP1/Paper 1/Gate 1; METHODOLOGICAL; LAB_EVIDENCE; Claim C1-15: empirical p-values require the identical full pipeline under an exchangeable null. Evidence: JMLR expanded paper pp. 1836-1843. Limitation: row exchangeability is not run exchangeability. Allowed use: group-preserving permutation design. Prohibited inference: individual overlapping windows can be permuted independently. Relevant pages: JMLR 1836-1843. Duplicate/version status: CONFERENCE_TO_JOURNAL_EXTENSION conflict; parent is 2009 ICDM DOI, PDF is 2010 JMLR extension. Metadata correction: separate/relink versions before citation.

### `XE9XS6BQ`

**Tags:** `RQ1 WP1 PAPER1 GATE1 METHODOLOGICAL LAB_EVIDENCE DEEP_READ FULLTEXT VERIFIED LEAKAGE LORO`

**Note:** Date 2026-07-18; RQ1/WP1/Paper 1/Gate 1; METHODOLOGICAL; LAB_EVIDENCE; Claim C1-12/C1-14: source-wise grouping and fold-contained preprocessing better estimate unseen-source performance. Evidence: subject-wise holdout, grouped CV and LOGO, pp. 190-198. Limitation: healthcare audio with much larger group count. Allowed use: LORO/LOGO and train-only pipeline design. Prohibited inference: random-window CV estimates unseen-run performance. Duplicate: NOT_DUPLICATE. Metadata correction: none.

### `M8LMWFQH`

**Tags:** `RQ1 WP1 PAPER1 GATE1 DIRECT LAB_EVIDENCE DEEP_READ FULLTEXT VERIFIED LEAKAGE LORO`

**Note:** Date 2026-07-18; RQ1/WP1/Paper 1/Gate 1; DIRECT; LAB_EVIDENCE; Claim C1-12/C1-13: source-group separation must precede segmentation. Evidence: segment/record/fault-shape split comparison on two vibration datasets, PDF pp. 1-5. Limitation: bearing diagnosis and weak uncertainty reporting. Allowed use: direct split-design justification. Prohibited inference: bearing results prove steel-frame field diagnosis, RUL, or severity. Duplicate: NOT_DUPLICATE. Metadata correction pending: item type conferencePaper.

### `RG9FMT8Y`

**Tags:** `RQ1 WP1 PAPER1 GATE1 DIRECT LAB_EVIDENCE DEEP_READ FULLTEXT VERIFIED LEAKAGE LORO`

**Note:** Date 2026-07-18; RQ1/WP1/Paper 1/Gate 1; DIRECT; LAB_EVIDENCE; Claim C1-12/C1-17: grouping scale and sensor position materially alter apparent vibration-classification performance. Evidence: leave-one-run/day/part-out and A1/A2 comparison, IEEE pp. 169883-169892. Limitation: bearing rigs; no ResNet1D or group-level CI. Allowed use: fair sensor-mode comparison on common LORO folds. Prohibited inference: closer sensor is universally optimal or validates project ResNet1D. Duplicate: NOT_DUPLICATE. Metadata correction: none.

## RQ2 / WP2 / Paper 2 / Gates 2-3

### `VI5QMSAE`

**Tags:** `RQ2 WP2 PAPER2 GATE2 GATE3 STRONG_ADJACENT TRACEABILITY DEEP_READ FULLTEXT VERIFIED INSPECTION_RECORD`

**Note:** Date 2026-07-18; RQ2/WP2/Paper 2/Gates 2-3; STRONG_ADJACENT; TRACEABILITY; Claim C2-12: IFC objects can anchor retrieval of historical FM work records. Evidence: ontology and 590-record SPARQL case, PDF pp. 9-13. Validation: sample office model and queries. Limitation: no sensors, demonstrated GlobalId, SHACL, cardinality, or status history. Allowed use: object/work-record linkage requirement. Prohibited inference: validated end-to-end sensor traceability. Duplicate: replaces `IQW2IJJE`. Metadata correction: none.

### `GUEJBZBZ`

**Tags:** `RQ2 WP2 PAPER2 GATE2 BACKGROUND TRACEABILITY DEEP_READ FULLTEXT VERIFIED`

**Note:** Date 2026-07-18; RQ2/WP2/Paper 2/Gate 2; BACKGROUND; TRACEABILITY; Claim C2-13: IFC time-series support and extraction toolchains remain barriers. Evidence: PRISMA-guided review of 93 studies, PDF pp. 11-22. Limitation: no identifier-chain validation. Allowed use: justify external time-series storage linked to BIM. Prohibited inference: external storage ensures referential integrity. Duplicate: NOT_DUPLICATE. Metadata correction pending: DOI URL.

### `EMTIHHX4`

**Tags:** `RQ2 WP2 PAPER2 GATE3 METHODOLOGICAL TRACEABILITY DEEP_READ FULLTEXT VERIFIED PROVENANCE`

**Note:** Date 2026-07-18; RQ2/WP2/Paper 2/Gate 3; METHODOLOGICAL; TRACEABILITY; Claim C2-14: provenance events should retain actor, operation, version, timestamp, and identity. Evidence: bridge scenario and blockchain prototype, PDF pp. 5-14. Limitation: design-stage transactions, not inspection evidence. Allowed use: minimum provenance fields. Prohibited inference: blockchain is required or inspection traceability is validated. Duplicate: NOT_DUPLICATE. Metadata correction pending: DOI URL.

### `XUN8EX6X`

**Tags:** `RQ2 WP2 PAPER2 GATE2 GATE3 DIRECT TRACEABILITY DEEP_READ FULLTEXT VERIFIED CQ PROVENANCE INSPECTION_RECORD`

**Note:** Date 2026-07-18; RQ2/WP2/Paper 2/Gates 2-3; DIRECT; TRACEABILITY; Claim C2-15: CQ-driven ontology can link inspection results to IFC GlobalIds. Evidence: 13 CQs, SPARQL, OOPS and three pilots, PDF pp. 4-10. Limitation: SHACL not executed, mapping partly manual, no complete sensor-evidence-action chain or status history. Allowed use: closest competitor and CQ/GlobalId benchmark. Prohibited inference: novelty in sensor-to-BIM generally or complete integrity validation. Duplicate: NOT_DUPLICATE. Metadata correction pending: online date and DOI URL.

### `LSYSC59G`

**Tags:** `RQ2 WP2 PAPER2 GATE2 METHODOLOGICAL TRACEABILITY DEEP_READ FULLTEXT VERIFIED CQ`

**Note:** Date 2026-07-18; RQ2/WP2/Paper 2/Gate 2; METHODOLOGICAL; TRACEABILITY; Claim C2-16: scoping, validation, and relationship CQs have different purposes. Evidence: formal QuO definitions, SewerNet and ROCQS, PDF pp. 3-12. Limitation: first conceptual categorization with limited user evaluation. Allowed use: classify CQs and require executable VCQs. Prohibited inference: an informal question list equals ontology validation. Duplicate: NOT_DUPLICATE. Metadata correction pending: standalone attachment needs title/authors/proceedings/year/URL if converted to a parent item.

## RQ3 / WP3 / Paper 3 / Gate 4

### `TRZY4P6X`

**Tags:** `RQ3 WP3 PAPER3 GATE4 STRONG_ADJACENT FIELD_FEASIBILITY DEEP_READ FULLTEXT VERIFIED PROVENANCE`

**Note:** Date 2026-07-18; RQ3/WP3/Paper 3/Gate 4; STRONG_ADJACENT; FIELD_FEASIBILITY; Claim C3-05: location-specific environmental baselines are feasible in long-term field monitoring. Evidence: three-year steel-bridge network, installation and three-minute sampling, pp. 161-167. Limitation: no BIM chain; sensitivity scenarios are numerical, not field-confirmed damage. Allowed use: placement, sampling and environmental-QC precedent. Prohibited inference: universal baseline duration or field diagnosis. Duplicate: no in-collection duplicate. Metadata correction pending: pages and DOI URL.

### `GE3XSAYV`

**Tags:** `RQ3 WP3 PAPER3 GATE4 STRONG_ADJACENT FIELD_FEASIBILITY DEEP_READ FULLTEXT VERIFIED`

**Note:** Date 2026-07-18; RQ3/WP3/Paper 3/Gate 4; STRONG_ADJACENT; FIELD_FEASIBILITY; Claim C3-05/C3-07: temperature adjustment materially changes operational threshold behavior. Evidence: one year hourly GNSS and July comparison, PDF pp. 10-21. Limitation: missingness and manual-inspection provenance incomplete; alerts lack ground truth. Allowed use: environmental-baseline and missing-data requirements. Prohibited inference: threshold exceedance equals damage or validated safety improvement. Duplicate: canonical exact counterpart of `2RB2YRBW`. Metadata correction: none.

### `LZPF7ILT`

**Tags:** `RQ3 WP3 PAPER3 GATE4 METHODOLOGICAL LAB_EVIDENCE DEEP_READ FULLTEXT VERIFIED`

**Note:** Date 2026-07-18; RQ3/WP3/Paper 3/Gate 4; METHODOLOGICAL; LAB_EVIDENCE; Claim C3-06: low-cost nodes require application-specific qualification. Evidence: side-by-side low/high-grade tests, sampling drops and ambient-vibration failure, PDF pp. 2-15. Limitation: laboratory slab and short sessions only. Allowed use: noise/timing/sampling/storage qualification. Prohibited inference: field suitability or field damage detection. Duplicate: NOT_DUPLICATE. Metadata correction pending: DOI URL.

### `D3TGCKXW`

**Tags:** `RQ3 WP3 PAPER3 GATE4 STRONG_ADJACENT FIELD_FEASIBILITY DEEP_READ FULLTEXT VERIFIED`

**Note:** Date 2026-07-18; RQ3/WP3/Paper 3/Gate 4; STRONG_ADJACENT; FIELD_FEASIBILITY; Claim C3-07: freezing and mode-dependent missingness can dominate field-derived features. Evidence: Z24/KW51 analyses, PDF pp. 6-13. Limitation: secondary datasets omit sensor/component provenance and use intervention labels. Allowed use: environmental-coverage and missing-data controls. Prohibited inference: transfer classifier or label anomalies as damage. Duplicate: NOT_DUPLICATE. Metadata correction pending: DOI, URL, date, volume and article number.

### `9823WXJZ`

**Tags:** `RQ3 WP3 PAPER3 GATE4 DIRECT FIELD_FEASIBILITY DEEP_READ FULLTEXT VERIFIED PROVENANCE`

**Note:** Date 2026-07-18; RQ3/WP3/Paper 3/Gate 4; DIRECT; FIELD_FEASIBILITY; Claim C3-08: continuous vibration monitoring is feasible in an occupied steel-frame building and reveals wind/operational baseline variation. Evidence: 72-channel network and ambient/wind/earthquake records, pp. 715-735. Limitation: no industrial/coastal context, BIM mapping, inspection confirmation, or field damage. Allowed use: steel-building deployment precedent. Prohibited inference: transient frequency change equals damage. Duplicate: NOT_DUPLICATE. Metadata correction pending: complete bibliographic fields.

## WP4 / Decision Support / Gate 5

### `YGZ32C8M`

**Tags:** `WP4 GATE5 STRONG_ADJACENT DECISION_SUPPORT DEEP_READ FULLTEXT VERIFIED INSPECTION_RECORD ACTION_STATUS PROVENANCE`

**Note:** Date 2026-07-18; WP4/Decision Support/Gate 5; STRONG_ADJACENT; DECISION_SUPPORT; Claim C4-03/C4-04: transparent maintenance support benefits from asset-condition-job traceability, governance, and expert interpretation. Evidence: four embedded cases, 48 interviews and seven-expert consultation, PDF pp. 3-12. Limitation: no four-level escalation or condition-action vocabulary. Allowed use: traceability, stewardship, roles and human review. Prohibited inference: predictive/autonomous maintenance or validation of the thesis four-level logic. Duplicate: canonical counterpart of `EN2SIFMC`. Metadata correction pending: full journal fields and fourth author.

### `ESTEYBHA`

**Tags:** `WP4 GATE5 METHODOLOGICAL DECISION_SUPPORT DEEP_READ FULLTEXT VERIFIED PROVENANCE`

**Note:** Date 2026-07-18; WP4/Decision Support/Gate 5; METHODOLOGICAL; DECISION_SUPPORT; Claim C4-05/C4-06: transparent assessment should expose purpose, roles, communication, provenance, data quality, security, and integration. Evidence: 27 rubrics, 40 expert responses and two cases, PDF pp. 4-13. Limitation: Digital Twin implementation maturity is not condition escalation; highest maturity includes autonomy outside scope. Allowed use: unweighted trust/governance criteria. Prohibited inference: map maturity levels to Normal/Watch/Inspect/Priority or create a weighted condition index. Duplicate: NOT_DUPLICATE. Metadata correction pending: date 2021-07-23.

## Non-DEEP_READ Status Queue

| Key | Tags/status to add | Reason |
|---|---|---|
| `NUTL57KJ` | `RQ2 WP2 PAPER2 GATE2 GATE3 TRACEABILITY FULLTEXT_UNAVAILABLE` | HTML only |
| `P674U5V2` | `RQ2 WP2 PAPER2 GATE2 GATE3 TRACEABILITY FULLTEXT_UNAVAILABLE` | Duplicate webpage of `Z4IBWW9Y` |
| `Z4IBWW9Y` | `RQ2 WP2 PAPER2 GATE2 GATE3 TRACEABILITY FULLTEXT_UNAVAILABLE` | No PDF |
| `3II2WKLN` | `RQ2 WP2 PAPER2 GATE3 TRACEABILITY SHACL FULLTEXT_UNAVAILABLE` | HTML only |
| `2RB2YRBW` | `RQ3 WP3 PAPER3 GATE4 FIELD_FEASIBILITY FULLTEXT_UNAVAILABLE` | Duplicate webpage of `GE3XSAYV` |
| `43648CQ8` | `WP4 GATE5 DECISION_SUPPORT FULLTEXT_UNAVAILABLE` | Wrong-paper PDF |
| `EN2SIFMC` | `WP4 GATE5 DECISION_SUPPORT FULLTEXT_UNAVAILABLE` | Duplicate webpage of `YGZ32C8M` |
| `EWBTQFTP` | `WP4 GATE5 NORMATIVE DECISION_SUPPORT FULLTEXT_UNAVAILABLE` | Partial standard sample |
| `V3IYM6UC` | `WP4 GATE5 NORMATIVE DECISION_SUPPORT FULLTEXT_UNAVAILABLE` | Partial standard preview |
