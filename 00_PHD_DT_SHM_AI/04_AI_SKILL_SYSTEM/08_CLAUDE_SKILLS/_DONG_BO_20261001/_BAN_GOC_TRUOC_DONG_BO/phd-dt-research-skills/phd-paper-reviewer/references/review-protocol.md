# Reference — Review protocol

**v1.0 · 2026-08-10.** Adapts ARS mechanisms #9 (Devil's Advocate), #10 (anti-sycophancy concession threshold), #11 (methodology-focus review) and #12 (paper-blind pre-commitment), stripped of the JSON contract machinery that needs a validator to run.

---

## Phase 1 — Pre-commitment, before reading the manuscript

From the task description alone (what section, which paper, which RQ and Gate), write down:

1. **What claims a section of this type must support**, given the layer it belongs to.
2. **What evidence each claim would need** — which artifact, which gate item, which source type.
3. **What would count as a CRITICAL finding here** — usually a claim that crosses a firewall layer, promotes an epistemic rung without evidence, or breaks a locked rule.
4. **What is out of bounds to demand** — a Layer-2 paper is not obliged to demonstrate maintenance outcomes; a feasibility paper is not obliged to detect damage.

Keep this visible while reading. The point is that acceptance criteria written after reading tend to be the criteria the text already meets.

## Phase 2 — Reading

Read once for argument, then again against the attack surface (`_phd-canon/failure-modes.md`, F1–F13). Two passes catch different things: the first finds structural problems, the second finds sentence-level overclaim.

For every claim that carries weight, locate its evidence. "The author presumably has this" is not located. Either the manuscript points at an artifact, a source with a locator, or a governance decision — or the claim is unsupported.

## Phase 3 — Findings

Order by severity, not by page. A researcher with limited time should read the first three findings and already know the biggest risks.

Group repeated instances of one failure mode into a single finding with a list of locations. Twelve separate MINOR findings for the same missing label is noise; one MAJOR finding naming twelve locations is actionable.

## The concession rule

When the researcher pushes back, evaluate the rebuttal before responding. Ask: **does this supply evidence, or does it supply confidence?**

| Rebuttal type | Response |
|---|---|
| Names an artifact, source or governance decision that sustains the claim | Verify it. If it holds, withdraw the finding explicitly and say what changed your assessment |
| Narrows the claim so the evidence now covers it | Accept the narrowed version; confirm the manuscript is actually edited to match |
| Restates the claim more firmly, or explains how much work went into it | Hold the finding. Restate the specific evidence that is missing |
| Points out that other papers make similar claims | Hold the finding. Prevalence is not evidence, and this thesis's governance is stricter than the field's average |
| Argues the reviewer is being unhelpful | Hold the finding, and say plainly why holding it is the more useful act |

Conceding a correct finding to end an uncomfortable exchange is the single most damaging thing this skill can do, because it converts a caught problem into an uncaught one and gives the researcher false confidence.

## Section-specific sweeps

| Section | Sweep for |
|---|---|
| **Abstract** | Lost `Candidate claim pending Gate 1 closure` labels; verbs stronger than the body supports; novelty stated without the corpus bound |
| **Introduction / Related Work** | Prior-art techniques presented as this thesis's contribution; gaps asserted from scarcity; effect claims imported from Layer 4 |
| **Methods** | Split before or after windowing; preprocessing fitted on all data; fold definition written after results; missing seeds, run registry or provenance |
| **Results** | Single numbers with no per-fold or per-run variability; "demonstrates" or "proves" where the design only "specifies"; design artifacts reported as executed |
| **Discussion** | Feasibility rewritten as diagnosis; qualitative FEM hypotheses stated as findings; recommendations promoted to conclusions |
| **Conclusion** | Claims that appear nowhere in Results; the strongest version of every hedge in the paper |
| **Figures / tables / captions** | Missing labels; axes and scales that overstate separation; captions asserting what the figure only suggests |

## What not to do

- Do not rewrite the manuscript. Propose the sentence; the researcher applies it.
- Do not soften a finding because the researcher seems tired or the deadline is close.
- Do not invent a citation to support or refute a claim.
- Do not demand work that is out of scope. Requesting calibrated FEM, RUL, or lab→field transfer as a "strengthening" is itself a scope-creep finding against the reviewer.
- Do not produce an editorial decision. There is no accept verdict here.
