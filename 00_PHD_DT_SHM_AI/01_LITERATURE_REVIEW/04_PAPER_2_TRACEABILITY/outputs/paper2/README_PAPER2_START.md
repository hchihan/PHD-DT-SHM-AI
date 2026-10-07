# Paper 2 start package · 2026-10-07

Location note: the brief named `E:\Researchgate23-bim-traceability\outputs\paper2`. That drive path does not exist on this workstation, so the package was written here. The P002 case folder used is `../../P002_NhaXuong_25x80`.

## Evidence authority

- Authoritative status: `P002_WP2_FINAL_TECHNICAL_STATUS_v3.md` (supersedes v2, v1); Gate 2 closure v3; Gate 3 closure v1; robustness assessment; `00_PROJECT_CONTROL/P002_RQ2_RESEARCH_EVIDENCE_LOG.md` (append-only, EV-RQ2-001…043); `RQ2_REPRODUCIBILITY_INCIDENTS.md`.
- Not available on this workstation: `outputs/wp2_final/*` (manifest, claim matrix, method freeze, claim discipline, earlier positioning files), `outputs/gate3/*` result CSVs, `VALIDATOR_VERSION_HISTORY.md` (only `_history/VALIDATOR_VERSION_HISTORY_v1.md` present).
- Re-verified directly from frozen CSVs in this session: 759 elements; 739/8/12 match classes; 731/16/12 integrity classes; 8 duplicate stored values (16 elements); 747/747 distinct exported GlobalIds; 14 rules; 17 mutation classes; 13 failure classes; 9 positives; 145 negatives; 78 challenge cases (19 accept / 59 reject, 8 multi-fault); all downstream records SYNTHETIC_CHAIN_RECORD.
- Verified only against the evidence log and closure reports (result CSVs absent): 154/154, 18/18 trace, 121/121 CQ checks, 68/78, 78/78, v2.1 0 differences.

## Files

PAPER2_OBJECTIVE_EVIDENCE_MATRIX.csv · PAPER2_LITERATURE_POSITIONING_FINAL.csv · PAPER2_COUNTER_EVIDENCE.md · PAPER2_RESEARCH_GAP_FINAL.md · PAPER2_CONTRIBUTION_FINAL.md · PAPER2_CLAIM_SOURCE_MATRIX.csv · PAPER2_OUTLINE_FINAL.md · PAPER2_SELF_REFERENCE_AUDIT.md · PAPER2_MANUSCRIPT_v1.md

## Final quality questions

| Q | Answer |
|---|---|
| Q1 Contribution without internal pass rates? | Yes, reduced: C1 rests on E1/E2 (stored vs exported divergence, 16 elements) plus the literature gap; C2 remains a design argued from literature. C3 disappears. |
| Q2 Gap from independent literature? | Yes; 10 Tier-A full texts; targeted search. |
| Q3 Objective vs synthetic separated? | Yes; E1/E2/E3 tags, Section 5.6, Table 8. |
| Q4 Empirical vs implementation verification distinguishable? | Yes; Sections 6.1–6.3 vs 6.4–6.9. |
| Q5 Repository used to prove novelty? | No (audit PASS). |
| Q6 P002 25×80 consistent? | Yes; only P002 used. |
| Q7 25×70 / P001 / FEM excluded? | Yes; not mentioned in the manuscript. |
| Q8 First-run failures reported? | Yes; 68/78 with classification; lost 76/78 excluded. |
| Q9 Limitations visible? | Yes; 11 items. |
| Q10 Construction-management relevance? | Yes; Sections 1.1, 6 of gap file, 7.5. |
