# Canon — Epistemic Status Ladder

**v1.0 · 2026-08-10 · new capability (N2); no upstream ARS equivalent.**
Derived from `AGENT_RULES.md` §9, `EVIDENCE_GATES_v2.1.md` header rule, `CURRENT_STATUS_AND_NEXT_DIRECTION.md` §6.

---

## Why this exists

The most damaging failure in this thesis is not a wrong number. It is a **silent promotion**: something that was proposed gets described as designed, something designed gets described as implemented, something implemented gets described as validated. Each step sounds like a small edit and each step is a different scientific claim.

Reviewers attack exactly here, because it is where a manuscript's language and its evidence come apart. So before writing or accepting any statement about a component of this thesis, place it on this ladder and check that the required evidence exists.

---

## The ladder

| Rung | Meaning | Evidence required to stand on this rung | Language to use |
|---|---|---|---|
| 1 **PROPOSED** | An idea or draft rule exists; nobody has approved it | A written proposal or draft ADR | "proposed", "candidate", "draft", "pending review" |
| 2 **DESIGN** | A structure has been worked out but not fixed | A design document with named components | "designed", "design boundary", "under specification" |
| 3 **SPECIFIED** | The design is complete, internally consistent, reviewed and baselined | Reviewed, approved, baselined specification package | "specified", "baselined", "frozen" |
| 4 **IMPLEMENTED** | Something runs | A working artifact plus provenance of how it was built | "implemented", "prototype executes" |
| 5 **VALIDATED** | It runs and produces preregistered expected results on controlled inputs | Preregistered expectations + test logs + exact expected-vs-actual comparison | "validated under the stated fixtures" |
| 6 **VERIFIED / ACCEPTED** | A human with authority has signed off against acceptance criteria | Signed acceptance record | "accepted", "signed off" |

**Promotion requires the evidence in the row you are moving into. Absence of contrary evidence is not promotion evidence.**

---

## Current placements (as of 2026-08-04 governance)

Re-read `01_CURRENT_CONTROL/CURRENT_STATUS_AND_NEXT_DIRECTION.md` before relying on these; they change.

| Item | Rung | Note |
|---|---|---|
| Action–Status–Event rules | **1 PROPOSED** | ADR is `PROPOSED — NOT YET ACCEPTED` |
| Paper 2 traceability chain (G2) | **2 DESIGN** | Literature boundary closed; specification not frozen |
| G2 package (Decision Register, ER model, CQ Registry, Constraint Catalogue, Fixture/Oracle Manifest) | **1–2** | Artifacts incomplete; review and baseline outstanding |
| G3 end-to-end demo | **below 4** | `NOT IMPLEMENTED, NOT VALIDATED`; execution `NOT OPEN` |
| Paper 1 metrics (RF ≈0.862, 1D-CNN S12 ≈0.841, ResNet1D ≈0.828) | **candidate** | Must carry `Candidate claim pending Gate 1 closure` |
| Field feasibility (G4) | **1–2** | Field-access basis unresolved; preparation permitted, deployment not |

---

## Applying the ladder to a sentence

Ask three questions in order:

1. **What rung does this sentence assert?** Verbs give it away: *proves*, *demonstrates*, *validates*, *shows that*, *ensures*, *achieves* usually assert rung 5 or 6.
2. **What rung does the evidence actually support?** Name the artifact and its path. If you cannot name one, the rung is at most 1.
3. **If they differ, rewrite down to the evidence.** Do not soften the verb while keeping the implication — a hedged overclaim is still an overclaim.

**Example.**
Input: "The Status_Event system ensures maintenance actions are properly closed."
Rung asserted: 5–6. Evidence available: a design boundary and a draft ADR — rung 1–2.
Output: "The proposed Status_Event model specifies guarded closure conditions under which an action may not be closed without accepted post-action verification. The rules are `PROPOSED — NOT YET ACCEPTED` pending ADR review, and no executed validation exists (G3 execution is not open). *Evidence is currently insufficient* to claim that closure behaviour has been demonstrated."

---

## Two distinctions worth naming separately

**Design vs implementation.** A schema, an ER model, a constraint catalogue and a CQ registry are rungs 2–3 no matter how detailed they are. Detail is not execution.

**Candidate vs verified binding.** When a `Condition_Evidence` record has more than one plausible BIM component and no human has confirmed which, the binding is **CANDIDATE**. It becomes VERIFIED only through a recorded human verification act. Automatic nearest-match, highest-score or single-remaining-option resolution does not promote it.
