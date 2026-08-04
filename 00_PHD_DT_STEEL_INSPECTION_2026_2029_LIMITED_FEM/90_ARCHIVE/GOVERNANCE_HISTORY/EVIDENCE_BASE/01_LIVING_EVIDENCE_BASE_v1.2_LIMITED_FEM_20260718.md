# LIVING EVIDENCE BASE
**Version:** v1.2 - LIMITED-FEM  
**Date:** 2026-07-18  
**Status:** New evidence update; does not overwrite `LIVING_EVIDENCE_BASE_v1.1_LIMITED_FEM.md`.

## 1. Locked Scope

Core chain: vibration data -> condition/state-change evidence -> BIM-linked component -> inspection record -> inspection-maintenance action support.

Identifier chain: `Sensor_ID -> BIM_GUID -> Condition_Evidence_ID -> Inspection_Record_ID -> Action_Status`.

FEM, where mentioned, is **nominal, uncalibrated, reference-only, not used for damage diagnosis**. Laboratory evidence, field feasibility, and decision support remain separate evidence classes.

## 2. Corpus Audit

| Audit measure | Count | Interpretation |
|---|---:|---|
| Zotero items inspected | 28 | All items in the four requested current collections |
| PDF attachments opened and read | 22 | Includes one wrong-paper attachment and two partial standards previews |
| New complete target full texts | 19 | Eligible for `DEEP_READ` and canonical evidence |
| No target full text | 6 | HTML/webpage/no-PDF records; `FULLTEXT_UNAVAILABLE` |
| Partial standards | 2 | Complete local preview/sample read, but complete standard unavailable |
| PDF mismatch | 1 | Parent `43648CQ8` has an unrelated PDF |
| Active duplicate/counterpart pairs | 3 | `P674U5V2/Z4IBWW9Y`, `2RB2YRBW/GE3XSAYV`, `EN2SIFMC/YGZ32C8M` |
| Material version/attachment conflicts | 1 | `ZLFATP2Z`: 2009 conference parent with 2010 journal-extension PDF |
| Verified metadata records requiring correction | 16 | 14 article/item records plus 2 partial-standard attachment controls; writeback is pending; see `../ZOTERO_AUDIT/08_DUPLICATE_AND_METADATA_CORRECTION_LOG_20260718.csv` |

The 19 new complete full texts are additional to the 33 substantive/limited records retained in v1.1. They are not automatically equivalent in evidential strength: two are direct Gate 1 vibration-method sources, one is the closest RQ2 ontology competitor, one is a direct steel-building field deployment, and the remainder are methodological, strong-adjacent, background, or supporting evidence.

## 3. Evidence Map

### RQ1 / WP1 / Paper 1 / Gate 1

Complete new sources: `L97BIAI3`, `PZ937I73`, `9XNSNIPX`, `ZLFATP2Z`, `XE9XS6BQ`, `M8LMWFQH`, `RG9FMT8Y`.

**Claim ->** Independent runs/groups, not derived windows, are the defensible split and inference unit.  
**Evidence ->** Hierarchical sample-size analysis (`L97BIAI3`), small-sample chance analysis (`PZ937I73`), dependence-aware tests (`9XNSNIPX`), permutation methods (`ZLFATP2Z`), grouped/LOGO validation (`XE9XS6BQ`), direct vibration segment leakage (`M8LMWFQH`), and run/day/part plus sensor-location effects (`RG9FMT8Y`).  
**Limitation ->** No paper validates the project's exact approximately six-runs-per-class design, confirms the ResNet1D sensor mode, or supplies a definitive inferential procedure for six overlapping LORO folds.  
**Next action ->** Lock the run registry, split runs before windowing, fit all transforms on training runs only, run common LORO folds and seeds, verify ResNet1D provenance, and report run-level uncertainty.

Gate effect: **materially strengthened, not closed**.

### RQ2 / WP2 / Paper 2 / Gates 2-3

Complete new sources: `VI5QMSAE`, `GUEJBZBZ`, `EMTIHHX4`, `XUN8EX6X`, `LSYSC59G`.

**Claim ->** Paper 2 can be evaluated as a formal and reproducible evidence-to-inspection traceability framework rather than claiming novelty for sensor-to-BIM integration generally.  
**Evidence ->** IFC-object/work-history retrieval (`VI5QMSAE`), IFC/time-series architecture constraints (`GUEJBZBZ`), provenance events (`EMTIHHX4`), CQ-driven IFC GlobalId/inspection linkage (`XUN8EX6X`), and the distinction among scoping, validation, and relationship CQs (`LSYSC59G`).  
**Limitation ->** No complete source validates the whole locked identifier chain. Executed SHACL validation, invalid-data tests, action-status history, and automated referential-integrity mapping remain absent. Three highly relevant sources lack PDFs.  
**Next action ->** Pre-register SCQ/VCQ/RCQ sets, define forward/reverse queries and invalid-data cases, formalize cardinality and provenance, and obtain `3II2WKLN`, `NUTL57KJ`, and `Z4IBWW9Y` full text.

Gate effect: **Gate 2 materially strengthened; Gate 3 closer but not closed**.

### RQ3 / WP3 / Paper 3 / Gate 4

Complete new sources: `TRZY4P6X`, `GE3XSAYV`, `LZPF7ILT`, `D3TGCKXW`, `9823WXJZ`.

**Claim ->** Real deployment requires explicit sensor qualification, environmental/operational baselines, missing-data controls, stable channel identity, and human inspection confirmation.  
**Evidence ->** Three-year steel-bridge baseline and practical installation (`TRZY4P6X`), temperature-adjusted thresholding with disclosed missingness (`GE3XSAYV`), low-cost-node sampling/noise limitations (`LZPF7ILT`), freezing and missing modal data (`D3TGCKXW`), and continuous monitoring in an occupied steel-frame building (`9823WXJZ`).  
**Limitation ->** None demonstrates a coastal industrial steel building with `Sensor_ID -> BIM_GUID`, auditable inspection records, and action-status history. Anomalies and transient frequency changes are not field damage diagnoses.  
**Next action ->** Define the field sensor register and BIM mapping before deployment; predefine completeness, drift/fault, environmental-coverage, baseline, and alert-to-inspection protocols; do not impose a universal baseline duration.

Gate effect: **supporting field-feasibility evidence strengthened; Gate 4 remains open**.

### WP4 / Decision Support / Gate 5

Complete new sources: `YGZ32C8M`, `ESTEYBHA`. Normative previews: `EWBTQFTP`, `V3IYM6UC`. Excluded for PDF mismatch: `43648CQ8`.

**Claim ->** Transparent decision support should expose asset-condition-job traceability, responsibilities, data quality, provenance, communication, and human review.  
**Evidence ->** Four facility-management cases and expert consultation (`YGZ32C8M`); 27 explicit Digital Twin maturity rubrics and 40-expert review (`ESTEYBHA`); included terminology in ISO/IEC 30173 and maturity aspects in ISO/IEC 30186 previews.  
**Limitation ->** No source implements or validates `Normal -> Watch -> Inspect -> Priority Inspection`, an equivalent escalation, an inspection trigger, an action-status state machine, or scenario-based audit trail. Standards previews are incomplete and are normative, not empirical evidence.  
**Next action ->** Design the thesis-specific four-level logic as a transparent, unweighted, human-reviewed workflow and validate it through pre-specified scenarios with facility managers.

Gate effect: **supporting transparency evidence improved; direct Gate 5 evidence remains insufficient**.

## 4. Evidence Sufficiency Controls

- **Allowed:** run-aware leakage control; group-preserving inference; component-level traceability; IFC GlobalId/BIM_GUID; provenance events; field feasibility; transparent human-reviewed inspection support.
- **Prohibited:** field damage diagnosis; direct lab-to-field classifier transfer; weighted Health Index; severity/DSI; RUL; predictive maintenance; automated maintenance; general AI superiority.
- **Insufficient:** exact six-run performance precision, ResNet1D sensor mode, complete SHACL protocol, full inspection-record schema, field identifier-chain demonstration, and four-level scenario validation.

**Evidence is currently insufficient** to close Gates 1, 3, 4, or 5. Gate 2 has stronger methodological support but still requires approved and pre-registered CQs and criteria.

## 5. Canonical Handling

- Count `GE3XSAYV`, `Z4IBWW9Y`, and `YGZ32C8M` as canonical for their counterpart pairs.
- Do not count `2RB2YRBW`, `P674U5V2`, or `EN2SIFMC` as independent evidence.
- Treat `ZLFATP2Z` as a metadata/version conflict until the conference parent and journal-extension PDF are separated or relinked.
- Exclude `43648CQ8` from substantive evidence until the correct paper PDF is attached and read.
- Do not tag ISO/IEC preview/sample attachments as complete full-text standards.

## 6. Priority Actions

1. Close the experimental parts of Gate 1: run registry, split-before-windowing, LORO, train-only preprocessing, common folds/seeds, ResNet1D provenance, and run-level uncertainty.
2. Approve and pre-register Gate 2 competency questions, cardinality rules, provenance fields, forward/reverse queries, and invalid-data tests before schema implementation.
3. Acquire the missing RQ2 PDFs and design the Gate 4/5 field-to-inspection scenario protocol with explicit human review.
