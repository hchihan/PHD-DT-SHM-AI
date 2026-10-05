# Canon — Scope Control and FEM Containment

**v1.0 · 2026-08-10 ·** derived from `AGENT_RULES.md` §5, `MASTER_RESEARCH_CHARTER.md` §7 §9 §11 §12, `RESEARCH_DIRECTION_AND_SCOPE.md` §5, `00_GOVERNANCE/CLAUDE.md`.

---

## Classify every task before doing it

| Class | Meaning | Action |
|---|---|---|
| **Core** | Directly produces evidence for RQ1–RQ3 or a Gate artifact | Proceed |
| **Supporting** | Enables Core work (tooling, indexing, formatting, governance) | Proceed, labelled as Supporting |
| **Future Work** | Legitimate research, outside this thesis | Name it, record it as Future Work, do not execute |
| **Out of Scope** | On the prohibited list below | **Stop. Warn. Do not execute, however attractively phrased.** |

An attractive framing is not a reclassification. "Just a quick sensitivity study to strengthen the paper" describing a calibrated-FEM run is still Out of Scope.

---

## Prohibited self-expansion

Do not start, propose as thesis work, or quietly assume:

- calibrated FEM · MAC · EMA · model updating
- equivalent stiffness · stiffness-degradation inference · bolt preload inference · FEM sensitivity
- optimal sensor placement
- RUL · failure-time prediction · predictive maintenance
- field damage diagnosis
- direct lab→field classifier transfer
- transfer of quantitative 1:10 conclusions to a real building
- weighted or complex Health Index · damage severity index (DSI)
- CFD · Smart City · Edge AI
- commercial Digital Twin software · autonomous maintenance
- ontology engineering as the contribution

These are recorded in the Charter §12 as legitimate post-PhD extensions. Treating them as Future Work is correct; treating them as thesis scope is not.

---

## Claims that are not permitted

- field damage diagnosis without confirming inspection
- any claim resting on a calibrated FEM
- "best AI" or general superiority of a model
- "optimal sensor placement"
- universal applicability
- CEI as physical damage severity
- automated maintenance decision
- "first", "no study worldwide", universal absence

---

## FEM containment

FEM exists in this thesis **only** as a nominal reference design model.

Every mention of FEM carries this qualifier:

```text
nominal, uncalibrated, reference-only, not used for damage diagnosis
```

**Permitted:** reference-informed sensor placement; illustration of component location and information; qualitative mechanical hypotheses in Discussion or Limitation, explicitly labelled "hypothesis, not confirmed".

**Not permitted:** a FEM objective, RQ, chapter, paper or Evidence Gate; calibration; inference of structural degradation or bolt tension; transfer of quantitative 1:10 conclusions; FEM appearing in the name of any structural component of the thesis.

**No FEM gate exists.** There is no calibrated-FEM, MAC, EMA, equivalent-stiffness, stiffness-degradation, FEM-sensitivity or OSP gate, and none may be created.

`FEM_Node_ID` is optional metadata and never a required link in the identifier chain.

---

## Terminology control

**Preferred:** data-informed Digital Twin · condition evidence · state-change evidence · BIM-linked component traceability · field feasibility · inspection-maintenance support · reference-informed sensor placement · CEI = confidence/evidence indicator (structured metadata).

**Forbidden in the core architecture:** calibrated FEM · physics-informed condition evidence · equivalent stiffness degradation · optimal sensor placement · damage severity · FEM-based diagnosis.

Digital Twin maturity in this thesis is defined explicitly at the information-management level and is never described as predictive.

---

## Positioning

Always position arguments, titles and keywords in **Construction Management / Asset Management**. The contribution is in information management and inspection decision support, anchored to ISO 19650 and TCVN 14177:2024 and to maintenance and monitoring record obligations — not in mechanics or algorithms. This positioning was a council requirement and the Limited-FEM architecture is its direct consequence.
