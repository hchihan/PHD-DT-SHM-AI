# MULTI_01 -- Lee, Eastman & Solihin (2021)

**Rules and validation processes for interoperable BIM data exchange.** Journal of Computational Design and Engineering, 8(1), 97-114. DOI: 10.1093/jcde/qwaa064. Zotero key: GWP87WLC. Touches Group 1 (identity) and Group 2 (integrity/validation).

**Source read:** Full text, complete (`G1_GWP87WLC_LeeEastmanSolihin.txt`, 18 pages).

---

**Q1 -- Research problem.** How to validate that IFC/COBie data exchanges (specifically Coordination View 2.0 and COBie MVDs) are correct and interoperable, by developing formal, rule-based validation processes -- including GUID-level rules -- rather than relying on ad-hoc manual QA.

**Q2 -- Information architecture.** PARTIAL. Chain is: IFC export/exchange file -> rule-based validation engine -> validation report (pass/fail per rule, including GUID rules). No sensor or condition-evidence layer; the "record" here is the validation report itself, not an inspection record.

**Q3 -- Identity representation.** YES. IFC GUID (GlobalId) is explicitly one of the objects of validation: uniqueness, format, and correct propagation/round-tripping of GUIDs through the exchange process are directly tested.

**Q4 -- Identity persistence across model revisions.** PARTIAL. CLAIM: the paper develops rules to check GUID uniqueness and round-trip correctness within an exchange/re-export cycle. EVIDENCE: rule-based validation processes described for CV2.0/COBie exchange, including GUID-focused rules. LIMITATION: the persistence tested is round-trip correctness through one export-import cycle of a specific exchange format, not longitudinal persistence across independently authored successive project-phase models. IMPLICATION: this is a strong precedent for "GUID integrity checking as part of a formal validation process," directly informing Paper 2's Gate 2/3 claim about GUID/identity validation, but does not itself demonstrate multi-phase, multi-revision persistence.

**Q5a-d -- Four provenance types.** NOT_REPORTED. The paper's scope is rule-based structural/semantic validation, not provenance recording of source, measurement, processing, or human actors.

**Q5e -- Review/approval provenance.** NOT_REPORTED.

**Q6 -- Model/version context.** PARTIAL. Validation is scoped to a given exchange instance (one CV2.0 or COBie export); no explicit multi-version/multi-revision model context is modeled.

**Q7 -- Validity/applicability scope.** YES. Explicitly scoped to CV2.0 and COBie MVDs for IFC/COBie interoperability validation -- a clearly bounded applicability statement.

**Q8 -- Forward and reverse traceability.** NOT_REPORTED explicitly in traceability terms, though rule validation reports implicitly support tracing a failed rule back to the offending IFC/COBie entity.

**Q9 -- Validation method.** YES. Rule-based validation processes are the paper's central contribution; rules are applied to real exchange data and validation outcomes reported.

**Q10 -- Deliberate invalid-case testing.** YES (tagged NEGATIVE_TESTING in prior curation, corroborated by content). CLAIM: the paper explicitly develops rules to catch malformed/duplicate GUID and other exchange-integrity violations as part of its rule set. EVIDENCE: GUID uniqueness and format-validation rules are a named part of the rule catalogue for CV2.0/COBie validation. LIMITATION: the specific taxonomy of invalid cases tested (duplicate vs. missing vs. stale vs. wrong-revision GUID) was not itemized in full in the extracted text at the granularity Paper 2's Gate 2/3 evidence table requires; treat the presence of negative testing as YES but its exact sub-case coverage as PARTIAL/EVIDENCE_INSUFFICIENT pending closer line-level reading. IMPLICATION: this is the strongest direct precedent in the corpus for "rule-based negative testing of GUID integrity," and materially narrows any claim that negative/invalid-case GUID testing is itself a novel contribution of Paper 2.

**Q11 -- G3 record fields.** NOT_APPLICABLE -- no inspection-record accountability content; the "record" is a machine validation report, not a human inspection record with performer/reviewer/approver roles.

**Q12 -- ALREADY_ESTABLISHED vs REMAINING_GAP.** ALREADY_ESTABLISHED: rule-based GUID/exchange validation, including negative-case rules, for standard IFC/COBie MVDs. REMAINING_GAP: this paper validates a *single exchange event*, not a chain from Sensor_ID through BIM_GUID through Condition_Evidence_ID through Inspection_Record_ID with human-accountability metadata -- so Paper 2's broader, record-accountability-integrated traceability framework remains distinct and not subsumed by this paper, but its GUID-validation-rules component specifically should be described as building on, not originating, GUID rule-based validation.
