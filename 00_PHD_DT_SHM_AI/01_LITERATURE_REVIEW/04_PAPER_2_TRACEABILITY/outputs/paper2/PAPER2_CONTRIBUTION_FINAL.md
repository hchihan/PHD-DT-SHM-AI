# PAPER2_CONTRIBUTION_FINAL

Paper 2 · RQ2 / WP2 · P002 25×80 m · 2026-10-07. Maximum three contributions. None relies only on E3 internal verification.

## Contribution 1 (core): a version-scoped component-identity rule grounded in observed source-data divergence

- **Contribution.** Component identity in the evidence chain is the ordered pair (Model_Version_ID, BIM_GUID), where BIM_GUID is the exported IFC GlobalId, not the stored Revit IfcGUID parameter. A lookup under an unregistered version fails closed. A stored-identifier duplicate is detected and reported and is never silently repaired or used as the key.
- **External literature basis.** GUIDs are not persistent across phase files or delete-recreate edits (Borkowski et al. 2026; Chatsuwan et al. 2025; Shafiq & Lockley 2020). Identifier quality is measured but repaired in the mapping layer (Fang et al. 2025). None of these reports a rule that scopes a GlobalId reference held in a downstream record to a registered model version.
- **Objective P002 evidence (E1).** One hash-identified live model (SHA-256 47748cbe…, Document_Modified FALSE); 759 scoped elements; 8 duplicate stored IfcGUID values shared by 16 elements (OE-01, OE-03, OE-05).
- **Cross-source evidence (E2).** Revit vs IFC: 739 match, 8 mismatch, 12 not exported; all 747 exported GlobalIds distinct, so the export separates the 16 duplicate-pair elements (OE-04, OE-06). Live vs legacy inventory: 232/232 identities reproduced (OE-07).
- **Internal verification (E3).** Unregistered version rejected 9/9 (IV-05); all 8 real duplicate pairs handled 8/8 (IV-06).
- **Limitation.** One model version and one export; GlobalId persistence across re-exports is not tested; the rule scopes identity but does not provide persistence across versions, which Borkowski et al. (2026) address.
- **Allowed wording.** "We define and apply a version-scoped identity rule … In the P002 model, the stored IfcGUID parameter and the exported GlobalId diverged for 16 elements; the rule kept these elements distinguishable and rejected the shared stored value as a key." Not allowed: "persistent identity", "solves GUID instability".

## Contribution 2 (core): a component-level traceability structure from sensor to action status with explicit rejection rules

- **Contribution.** Six entities and the locked identifier chain Sensor_ID → BIM_GUID → Condition_Evidence_ID → Inspection_Record_ID → Action_Status, with forward and reverse reconstruction, 14 integrity rules in a fixed evaluation order and 12 competency questions, designed so that missing, invalid and ambiguous links produce distinct failure classes.
- **External literature basis.** Sensor-to-inspection linkage without actions or rule validation (Lorvão Antunes et al. 2024); inspection-to-maintenance in IFC without sensors or identity governance (Bellon et al. 2025; Hagedorn et al. 2022; Kim et al. 2018); ledger-based monitoring-to-reaction trace without BIM component identity (Mariniello et al. 2025). The combination is not reported in the ten Tier-A studies.
- **Objective P002 evidence (E1).** The chain is instantiated on nine real component identities from the verified model (primary columns, rafters, gable elements, a placeholder brace, the RD-001 duplicate pair).
- **Cross-source evidence (E2).** Identities used in fixtures are those confirmed across Revit and IFC (OE-04).
- **Internal verification (E3).** 9/9 forward and 9/9 reverse reconstruction; 121/121 CQ checks; 145/145 negatives rejected with the intended class (IV-03, IV-04).
- **Limitation.** All sensor, evidence, inspection and action records are synthetic; nine components; no field data; component-to-sensor cardinality not constrained.
- **Allowed wording.** "The structure was implemented and verified internally on synthetic chain records anchored to real component identities." Not allowed: "validated", "demonstrated in operation", "supports maintenance decisions in practice".

## Contribution 3 (supporting): a disclosed internal-verification record that separates first-run failures from corrective re-runs

- **Contribution.** A verification protocol for the chain that reports the first frozen run (68/78 on a 78-case challenge set; 10 failures classified as 8 validator defects and 2 specification gaps) separately from the corrective run on the same set (78/78), and excludes a lost intermediate attempt from evidence.
- **External literature basis.** Pre/post designs and gate checks are reported (Fang et al. 2025; García et al. 2026), and CQ verification is standard (Monfardini et al. 2023). Tier-A studies report final pass states; none reports first-run failures of their own checker. This is a reporting-practice contribution, not a novelty claim.
- **Objective P002 evidence (E1).** All 8 real duplicate pairs were included in the challenge set (3 cases each).
- **Cross-source evidence (E2).** None.
- **Internal verification (E3).** IV-07, IV-08.
- **Limitation.** Level C independence (same author; blind to output, not to code); corrected run reuses the set; not independent validation.
- **Allowed wording.** "corrective verification on the same challenge set". Not allowed: "100 % accuracy", "independent validation", "robust".

## Removed or downgraded

| Candidate | Decision | Reason |
|---|---|---|
| A Model-version-qualified identity as persistence | Downgraded to scope rule (inside C1) | Borkowski et al. 2026; Fang et al. 2025 |
| C Integrity-rule framework as a contribution | Implementation detail inside C2 | Rule-based BIM validation established (Lee et al. 2020; Fang et al. 2025; García et al. 2026) |
| D CQ-based verification | Method, not contribution | Lorvão Antunes et al. 2024; Borkowski et al. 2026 |
| E Negative testing as a contribution | Folded into C2/C3 as E3 | Internal only |
| F Real anomaly as a contribution | Evidence for C1 | Anomalies known; this observation is evidence, not a method |
| Accountable inspection record fields (performer/reviewer/approver) | Not claimed | García et al. 2026 and Bellon et al. 2025 (IfcActor) cover role attribution; P002 records only Inspector/Action_Actor |
| Evidence validity window as a contribution | Not claimed | Only one rule (IR-08) and synthetic dates; insufficient evidence |
