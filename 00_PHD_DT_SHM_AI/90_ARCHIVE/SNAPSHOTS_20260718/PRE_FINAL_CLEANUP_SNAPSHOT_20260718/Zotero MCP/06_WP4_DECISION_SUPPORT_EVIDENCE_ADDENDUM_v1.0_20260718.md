# WP4 / Decision Support / Gate 5 Evidence Addendum
**Version:** v1.0 | **Date:** 2026-07-18  
**Control:** There is no RQ4.

## Core Finding

No reviewed source implements `Normal -> Watch -> Inspect -> Priority Inspection` or a genuinely equivalent transparent escalation with an auditable inspection trigger, status history, and scenario validation.

## Claim Register

| Claim ID | Claim | Evidence | Limitation | Next action |
|---|---|---|---|---|
| C4-03 | Decision support should preserve traceability among assets, condition data, and maintenance jobs. | `YGZ32C8M`, pp. 8-10 | No explicit condition/action states. | Make every recommendation traceable to evidence, component, and inspection record. |
| C4-04 | Human governance, responsibilities, and professional interpretation are essential. | `YGZ32C8M`, four cases and expert consultation | University CFM context. | Assign reviewer/approver roles in each scenario. |
| C4-05 | Transparent assessment should expose purpose, roles, communication, data quality, provenance, security, and integration. | `ESTEYBHA`, 27 rubrics and 40 experts | Digital Twin maturity, not condition escalation. | Reuse only unweighted trust/governance criteria. |
| C4-06 | Digital Twin maturity levels must not be mapped to condition-action levels. | `ESTEYBHA`, `EWBTQFTP` | ISO/IEC 30186 file is only a sample. | Keep maturity assessment separate from the four-level action workflow. |
| C4-07 | Digital Twin terminology does not require autonomous maintenance. | ISO/IEC 30173 preview, Clause 3.1.1 and notes | Preview is incomplete and generic. | Use terminology only, not workflow evidence. |

## Integrity Exclusions

- `43648CQ8`: the attached PDF is Tunney et al. (2002), DOI `10.1149/1.1470661`, not the 2010 ASCE maintenance decision-support paper. The parent paper is `FULLTEXT_UNAVAILABLE` and must not support Gate 5 until the correct PDF is attached and read.
- `EWBTQFTP`: complete local file read, but it is an ISO/IEC 30186 sample ending at source p. 7. It cannot establish full-standard conformity.
- `V3IYM6UC`: complete local file read, but it is an ISO/IEC 30173 preview ending in Clause 3.4.2.
- `EN2SIFMC`: metadata-only counterpart of canonical `YGZ32C8M`.

## Proposed Scenario-Evaluation Criteria

| Criterion | Required record |
|---|---|
| Transparent trigger | Evidence value, baseline/context, threshold/rule version, and rationale |
| Human review | Reviewer, timestamp, disposition, and comments |
| Traceability | `Condition_Evidence_ID`, `BIM_GUID`, `Inspection_Record_ID` |
| Status history | Prior/new `Action_Status`, actor, time, reason |
| Explainability | Plain-language reason and supporting evidence links |
| Scenario reproducibility | Input fixture, expected status, actual status, and discrepancy log |

## Gate Position

**ALLOWED CLAIM:** Supporting evidence favors traceable, governed, explicit, and human-reviewed decision support.  
**PROHIBITED INFERENCE:** AHP, weighted condition index, Markov deterioration, maintenance optimization, predictive maintenance, autonomous action, or Digital Twin maturity levels constitute the thesis four-level logic.  
**EVIDENCE SUFFICIENCY:** Evidence is currently insufficient for direct Gate 5 closure. The four-level logic remains a thesis design that requires scenario-based facility-manager review.
