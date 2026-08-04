# TERMINOLOGY CONTROL
**Version:** v1.1 — LIMITED-FEM | **Date:** 2026-07-17
Applies to: all thesis chapters, papers, reports, slides, evidence files, and agent outputs from this date.

## 1. Allowed terms (use these)

| Term | Usage note |
|---|---|
| condition evidence | Output of the vibration→evidence layer; never "damage proof" |
| state-change evidence | Alternative when no condition label is claimed |
| component-level traceability | Core Paper 2 term |
| BIM-linked inspection record | Core Paper 2/3 term |
| field feasibility | Core Paper 3 term; never "field validation of diagnosis" |
| inspection-maintenance support | Thesis-level framing |
| nominal reference model | The only sanctioned FEM descriptor |
| reference-informed sensor placement | Replaces "optimal sensor placement" |
| practical sensor configuration | Alternative replacement |
| confidence/evidence indicator (CEI) | CEI definition; never physical severity |
| descriptive–diagnostic Digital Twin (management level) | DT maturity self-definition (C3) |

## 2. Controlled or removed terms

| Term | Rule | Replacement / condition |
|---|---|---|
| calibrated FEM | REMOVE from all core text | Only in Post-PhD/limitations as explicitly deferred work |
| calibration (of FEM) | REMOVE as an activity of this thesis | "the nominal model is deliberately uncalibrated" |
| physics-informed condition evidence | REMOVE — prohibited in core architecture | "condition evidence" |
| equivalent stiffness degradation | REMOVE from claims | Only inside SUPPORTING_REFERENCE literature descriptions of other authors' work |
| mechanical damage interpretation | REMOVE as thesis activity | "qualitative mechanical hypothesis (nominal model; not confirmed)" |
| optimal sensor placement / OSP | REMOVE from thesis language | "reference-informed sensor placement"; OSP may appear only when citing the OSP literature as such |
| FEM-based diagnosis | REMOVE | — |
| damage severity / DSI | REMOVE from claims | CEI (confidence/evidence indicator) |
| MAC (as thesis acceptance criterion) | REMOVE as criterion | MAC may appear only in literature descriptions |
| stiffness degradation (of the real structure) | REMOVE from claims | — |
| RUL / remaining useful life | REMOVE | Out of scope; Post-PhD |
| predictive maintenance | REMOVE as thesis claim | "condition-based inspection support"; PdM only as literature-context label |
| autonomous maintenance decision | REMOVE | "human-reviewed decision support" |
| FEM_Node_ID (as chain link) | CONTROL | Optional metadata attribute only; never in the identifier chain |
| RSAP/FEM (in RQ/WP/chapter/paper/gate names) | REMOVE from all structural names | FEM confined to C3 methods subsection + Limitations |

## 3. Mandatory FEM qualifier

Every remaining mention of FEM in any current document must carry (at first mention per document/section): **"nominal, uncalibrated, reference-only, not used for damage diagnosis."**

## 4. Enforcement

Before any submission or gate closure: run a keyword check for the §2 terms plus FEM, RSAP, MAC, modal, calibrat*, severity, RUL, optimal sensor, physics-informed; record results in the gate evidence pack. Legacy/archived files are exempt (historical record) but must not be quoted into new text without translation to v1.1 terminology.
