# RQ2 Traceability Evidence Addendum
**Version:** v1.2 | **Date:** 2026-07-18

## Scope

Paper 2 is positioned in Construction Management / Asset Management as a verifiable component-level traceability framework. Novelty must be phrased as "within the reviewed evidence base" and must not be claimed for sensor-to-BIM integration generally.

## New Claim Register

| Claim ID | Claim | Evidence | Limitation | Next action |
|---|---|---|---|---|
| C2-12 | IFC objects can anchor retrieval of historical FM work records. | `VI5QMSAE`, PDF pp. 9-13 | No persistent GlobalId demonstration or condition evidence. | Require `BIM_GUID` and reverse component-to-record queries. |
| C2-13 | Operational time-series commonly require external storage linked to BIM/IFC. | `GUEJBZBZ`, PDF pp. 11-22 | External storage alone does not ensure integrity. | Specify the external-store-to-`BIM_GUID` contract and provenance. |
| C2-14 | Provenance should retain actor/source, operation, version, timestamp, and event identity. | `EMTIHHX4`, PDF pp. 5-14 | Design transactions, not inspection evidence. | Add minimal provenance fields without requiring blockchain. |
| C2-15 | A CQ-driven ontology can connect inspection results to IFC GlobalIds. | `XUN8EX6X`, PDF pp. 4-10 | SHACL not executed; mappings partly manual; action history absent. | Benchmark Paper 2 against CoDEC with invalid-data and reverse-query tests. |
| C2-16 | Scoping, validation, and relationship CQs should be distinguished. | `LSYSC59G`, PDF pp. 3-12 | Conceptual taxonomy with limited user evaluation. | Label each CQ and attach query, expected answer, and failure condition. |
| C2-17 | Complete traceability requires an explicit status-event history, not only current status. | Gap across all five sources | No direct source validates the complete chain. | Define `Action_Status_Event_ID`, prior/new status, actor, timestamp, reason, and linked record. |

## Competitor Boundary

The closest competitor is `XUN8EX6X`: it includes sensors/observations, IFC GlobalId traversal, inspection procedures/results, and CQs. It does **not** validate the full chain from raw sensor data to derived condition evidence, inspection record, action-status history, and executed constraint tests.

`VI5QMSAE` supports object/work-record retrieval; `EMTIHHX4` supports provenance requirements; `GUEJBZBZ` supports the external time-series architecture boundary; `LSYSC59G` supplies CQ methodology. None alone or together proves the thesis implementation.

## Proposed Gate 2-3 Test Families

| Test family | Required evidence |
|---|---|
| SCQ | Domain entities, actors, records, and boundaries are explicit. |
| VCQ | Executable query, expected result, actual result, and reproducible dataset. |
| RCQ | Direction, arity, domain/range, and cardinality are explicit. |
| Referential integrity | Orphan and duplicate IDs fail validation. |
| Bidirectional traceability | Forward and reverse paths return the same linked set. |
| Provenance | Source, actor, time, version/transformation, and evidence lineage are retained. |
| Status history | Every status transition has actor, time, reason, and linked inspection record. |

## Missing Full Text

- `3II2WKLN`: direct SHACL/ifcOWL candidate; HTML only.
- `NUTL57KJ`: direct IFC inspection-maintenance candidate; HTML only.
- `Z4IBWW9Y`: IFC defect/action candidate; no attachment.

For all three: **Evidence is currently insufficient.** Do not assign detailed claims before full-text review.

## Gate Position

**ALLOWED CLAIM:** Within the reviewed evidence base, partial precedents exist for sensor/IFC linkage, inspection records, provenance, and CQ evaluation, but the complete locked chain has not been validated.  
**PROHIBITED INFERENCE:** No study exists; sensor-to-BIM integration itself is novel; CoDEC provides complete referential integrity or action-status validation.  
**EVIDENCE SUFFICIENCY:** Gate 2 is materially strengthened. Gate 3 remains open pending approved CQs, formal schema/constraints, invalid-data tests, and end-to-end laboratory demonstration.
