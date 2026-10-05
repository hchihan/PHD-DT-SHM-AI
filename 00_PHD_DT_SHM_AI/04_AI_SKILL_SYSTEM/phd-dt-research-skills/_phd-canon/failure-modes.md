# Canon — Thesis-Specific Failure Modes

**v1.0 · 2026-08-10 ·** adapted from the ARS AI-research-failure-mode pattern (mechanism #21), retargeted onto this thesis's actual exposure. The generic seven ARS modes are replaced by the thirteen below.

Use this as the attack list for review, and as a self-check before emitting any analysis.

---

| # | Failure mode | What it looks like | Test |
|---|---|---|---|
| **F1** | **Novelty inflation** | A technique on the prior-art list is described as the contribution | Is it in `novelty-boundary.md`'s prior-art list? Is the claim corpus-bounded? Is the contribution the integrated chain or a single technique? |
| **F2** | **Design → result promotion** | A schema, ER model or ADR is described as demonstrating, ensuring or achieving something | Place the verb on `epistemic-ladder.md`. Does evidence exist at that rung? |
| **F3** | **Gate inflation** | "Main steps are done, mark it PASS"; a gate treated as closed because artifacts look complete | Is there a signed acceptance artifact? Has every acceptance criterion a named evidence path? |
| **F4** | **Citation fabrication** | Plausible-looking references, DOIs, Zotero keys, years or quartiles appear to support a claim | Can each reference be located in the corpus? Unverifiable → `UNVERIFIED`, never asserted |
| **F5** | **Claim–source drift** | The citation exists but does not say what it is cited for | Locate the supporting passage. No passage → the claim is unsupported |
| **F6** | **ML data leakage** | High accuracy from segments split randomly within the same run; scaler fitted before splitting; fold definition written after seeing results | Was the split at run level, before windowing? Was preprocessing train-only? Was LORO preregistered? |
| **F7** | **Single-number reporting** | One macro-F1 with no per-fold or per-run variability | Mean ± sd across folds/runs, per-class results, seeds recorded |
| **F8** | **Field overclaim** | Field feasibility evidence presented as field validation or damage diagnosis | Which firewall layer produced the evidence, and which layer does the claim sit in? |
| **F9** | **Identity-binding overclaim** | A `Condition_Evidence` bound to a BIM component described as verified when several candidates existed and no human confirmed | Is there a recorded human verification act? Otherwise `CANDIDATE` |
| **F10** | **Chain notation drift** | `Action_Status` used as an identifier or as history; `Status_Event` written as accepted; gratuitous `Component_ID`; `completed` treated as closure; recommendation treated as `Action_Record` | Check against `research-chain.md` |
| **F11** | **FEM scope creep** | Calibration, MAC, EMA, stiffness or preload inference appears; FEM mentioned without its qualifier; a FEM gate is implied | Check `scope-control.md`. No FEM gate exists |
| **F12** | **Candidate-label loss** | Paper 1 metrics appear in an abstract, caption or conclusion without `Candidate claim pending Gate 1 closure` | Search abstract, captions and conclusion specifically — this is where labels disappear |
| **F13** | **Evidence/action disconnect** | The manuscript asserts that traceability supports better inspection decisions without evidence linking evidence to action outcome | Is the decision-support claim supported by G5 review evidence, or is it asserted? |

---

## Two composite patterns worth naming

**The sympathetic agreement.** The researcher states a claim with confidence and the assistant agrees because disagreeing feels unhelpful. This is how F1, F2 and F3 enter. The corrective is in `output-discipline.md` §9: withdraw a finding only for new evidence, not for firmer restatement.

**The plausible gap-filler.** The outline demands a Methods or Results paragraph, the materials do not contain one, and fluent prose appears anyway from general knowledge of what such a paragraph usually says. This is how F4 and F2 enter a manuscript together. The corrective is the material-gap marker: `[MATERIAL GAP — Evidence is currently insufficient.]`
