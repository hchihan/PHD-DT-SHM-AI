# PhD KNOWLEDGE UNIVERSE — 2026-08-11

**Version:** v1.0 | **Issued:** 2026-08-11
**Status:** CURRENT SUPPORTING — STRATEGIC NAVIGATION ARTIFACT | **Source-of-truth level:** 7
**Supersedes:** None. | **Superseded by:** None.
**Change summary:** Creates a navigable strategic map of the research programme. It closes no gate, accepts no proposed decision, and changes no governance.

> This is a **supporting navigation artifact**. It is subordinate to the Charter, the ACCEPTED ADRs, the Matrix and the Evidence Gates. Where it disagrees with any of those, they win. See `SOURCE_OF_TRUTH_HIERARCHY_v2.1.md`.

## 1. What this package is

One self-contained interactive file, `PHD_KNOWLEDGE_UNIVERSE_20260811.html`, containing all six required deliverables as views:

| Tab | Deliverable |
|---|---|
| Universe | D1 — interactive zoomable knowledge map (132 nodes, 118 links) |
| Executive map | D2 — static 16:9 plate for a supervisor slide |
| Gap portfolio | D3 — 39 research gaps in 8 families, 16 columns |
| Roadmap | D4 — Now / Next / Field preparation / Synthesis / Parallel / Post-PhD / Transfer |
| Shortlist | D5 — 12 opportunities scored 1–5 on 8 criteria, with reasoning |
| Outputs | Ring 4 — publication and technology-transfer ecosystem |
| Critical audit | D6 — five judgements plus the self-check table |

The file is offline, theme-aware, keyboard-navigable and printable (Ctrl/Cmd+P renders the current view without the chrome, which is how to produce an A1/A0 plate).

## 2. Sources read to build it

Governance: `MASTER_RESEARCH_CHARTER_v2.1_TRACEABILITY_CORE_20260719.md`; `MASTER_RESEARCH_CHARTER.md`; `RESEARCH_ARCHITECTURE.md`; `RESEARCH_DIRECTION_AND_SCOPE.md`; `RQ_WP_CHAPTER_PAPER_GATE_MATRIX_v2.1.md`; `EVIDENCE_GATES_v2.1.md`; `TERMINOLOGY_CONTROL_CURRENT.md`; `CLAUDE.md`; `RESEARCH_ARCHITECTURE_DECISION_RECORD_20260719.md`; `RESEARCH_ARCHITECTURE_DECISION_RECORD_ACTION_ID_20260719.md`; `ADR_ACTION_STATUS_EVENT_20260804_DRAFT.md`.

Control: `CURRENT_DIRECTION_LOCK_20260804.md`; `CURRENT_STATUS_AND_NEXT_DIRECTION.md`.

Evidence: `02_EVIDENCE_BASE/CURRENT/00_MASTER_INDEX_CURRENT_20260804.md`; `01_MASTER_G1_G2_G3_EVIDENCE_SYNTHESIS_20260804.md`; RQ1/RQ2/RQ3/WP4 addenda; `G1_TO_G2_CONDITION_EVIDENCE_INTERFACE_v1.0.md`.

Papers: Paper 1, Paper 2 and Paper 3 direction files.

Data: `CANONICAL_THREE_CAMPAIGN_DATASET/00_README.md`; `THREE_CAMPAIGN_REANALYSIS/00_EXECUTIVE_REPORT.md`; `15_NEXT_ANALYSIS_RECOMMENDATION.md`.

The prompt named `MASTER_RESEARCH_CHARTER_v1.1_LIMITED_FEM_20260717.md`, `00_README_START_HERE.md`, `THE_COUNCIL_REVIEW_FEM_OR_NO_FEM_17.07.2026.md` and `RESEARCH_ARCHITECTURE_DECISION_RECORD_20260717.md`. The first two have been archived or deleted in the 2026-08-04 reset; the Council review and the 20260717 ADR are superseded by the 20260719 ADR and the v2.1 Charter, which is what the map follows. The Limited-FEM decision itself is unchanged and is enforced throughout.

## 3. How the universe is read

- **Colour = layer.** Blue Layer 1, oxide Layer 2, green Layer 3, violet Layer 4, grey FEM satellite, crimson quarantine.
- **Fill = scope.** Solid Core, tinted Supporting, hollow-dashed Future/Post-PhD, hatched red Out of scope.
- **Shape = node type.** Square Data, hexagon Method, circle Evidence, tag Standard, figure Actor, diamond Decision, rounded Output, triangle Risk.
- **Line = relation.** Solid current dependency, dashed extension hypothesis, red prohibited transfer or claim.
- **Size = strategic role, never certainty.**

Six lenses filter the map: core thesis only, research gaps, publication opportunities, technology-transfer pathways, Gate dependencies, prohibited claims. Six selectors filter by Layer, Scope, Readiness, Gate, Node type and RQ/WP. Search covers labels, IDs, definitions, evidence, limitations and keywords.

## 4. Evidence discipline applied

Every quantitative figure carried into the map comes from the repository's own three-campaign reanalysis and is labelled **"Candidate claim pending Gate 1 closure"**. No citation, DOI, metric, standard clause, journal ranking or result was invented. Where the repository is silent, the record says **"Evidence is currently insufficient."**

Three specific honesty flags are worth repeating here:

1. The repository evidences **PASCO** acquisition only. There is **no ADXL-class or other low-cost node data** in it, so no low-cost sensor claim is possible; this is recorded as gap SC-04 with the data that would be needed.
2. The Charter's earlier candidate figures (RF ≈ 0.862; 1D-CNN S12 ≈ 0.841; ResNet1D ≈ 0.828) come from a **different, earlier pipeline**. The 2026 reanalysis did not reproduce them and **did not run ResNet1D at all**. Gap RP-04 records the confirm-or-remove decision.
3. Campaign 1 and Campaign 2 **single- and paired-sensor results are statements about a CSV column position, not about a verified apex / beam-column / brace-column identity**, until the per-file fingerprint reassignment in gap RP-01 is executed.

## 5. Gate state carried by the map (2026-08-04, unchanged)

| Gate | State |
|---|---|
| G1 | `OPEN — PARTIAL EVIDENCE` |
| G2 | `OPEN — LITERATURE BOUNDARY CLOSED, SPECIFICATION NOT YET FROZEN` |
| G3 | `OPEN — NOT IMPLEMENTED, NOT VALIDATED, NOT OFFICIALLY PASSED`; execution `NOT OPEN` |
| G4 | Readiness only; field access unconfirmed |
| G5 | OPEN; expert-reviewed decision-support evidence missing |
| G6 / G7 | OPEN |

`CLOSE_SEARCH` remains corpus-bounded. It is not universal absence, it supports no "first" claim, and it is not a Gate 2 pass.

## 6. Claim → Evidence → Limitation → Next action

- **Claim:** The programme now has a single navigable map that shows the locked chains, the four evidence layers, the interfaces between them, 39 classified gaps, the output ecosystem and the prohibited region, with scope and readiness attached to every node.
- **Evidence:** The governance, control, evidence-base, paper-direction and data files listed in §2, all read in full for this pass.
- **Limitation:** This artifact is a navigation and planning instrument. It creates no new evidence, closes no gate, accepts no proposed ADR, and resolves none of the expert-dependent decisions that Gate 2 and Gate 5 require.
- **Next action:** Work the Now column of the roadmap — canonical run registry and physical sensor identity (RP-01), multi-seed leakage-safe LORO (RP-02), ResNet1D provenance (RP-04) — while Stream B puts the Action-Status-Event ADR and the Gate 2 package to review, and Stream C confirms the field-access basis.
