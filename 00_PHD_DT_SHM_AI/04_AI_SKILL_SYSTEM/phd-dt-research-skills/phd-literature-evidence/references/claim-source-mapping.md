# Reference — Literature matrix and claim–source mapping formats

**v1.0 · 2026-08-10.**

---

## 1. Claim–source map

Use when the researcher asks whether a set of claims is supported, or before a section is drafted.

| # | Claim (as written) | Label | Source + locator | Passage supports? | Residual gap |
|---|---|---|---|---|---|
| 1 | *verbatim claim* | PRIOR ART / SUPPORTED GAP / PARTIALLY SUPPORTED GAP / CANDIDATE NOVELTY / UNSUPPORTED NOVELTY CLAIM | `[Author Year, §3.2]` or repository path | Yes / Narrower than claim / No | what would close it |

Quote claims verbatim. Paraphrasing a claim during audit is how an overclaim gets audited as if it were the milder version.

**"Passage supports?" values:**

- **Yes** — the passage's scope covers the claim's scope
- **Narrower than claim** — state the mismatch dimension: scale, setting, structure type, epistemic rung, generality
- **No** — the source does not bear on this claim

## 2. Literature matrix

Use when building or extending a review section.

| Source | Year | Venue type | What it establishes | Chain element | Layer | Relevance to RQ | Limitation for this thesis |
|---|---|---|---|---|---|---|---|

- **Chain element** — which part of the locked chain it speaks to: condition evidence · component identity · inspection record · action record · status/event history · authorization · verification · closure/reopen · none
- **Layer** — 1 laboratory · 2 traceability · 3 field feasibility · 4 decision support (see `_phd-canon/research-chain.md`)
- **Limitation for this thesis** — the honest reason it does not settle the question: different scale, different structure type, proposal not validated, no identity governance, no event history, no authorization model, etc. This column is what makes the matrix argue rather than list.

Sort by chain element, not by year. The contribution argument is structural, so a matrix organised by chain element shows immediately which elements are crowded with prior art and which are thin.

## 3. Prior-art decomposition table

Use when a novelty claim is on the table.

| Level | Question | Finding |
|---|---|---|
| Technique | Is this individual technique new? | usually `ESTABLISHED PRIOR ART` — name the corpus sources |
| Combination | Is this combination new within the reviewed corpus? | corpus-bounded finding |
| Distinct work | Does the combination do something the parts cannot do separately? | the claim that has to be argued |

Only the third row can carry a contribution. State it as: *within the reviewed corpus, no single model carries [elements] as one validated chain; each element individually is established prior art.*

## 4. Gap audit

For each asserted gap:

```text
Gap as asserted:  <verbatim>
Evidence type:    stated-in-source / documented-absence / scarcity-only / none
Corpus bound:     <which screening/deep-read rounds this rests on>
Verdict:          SUPPORTED GAP / PARTIALLY SUPPORTED GAP / UNSUPPORTED NOVELTY CLAIM
Residue:          <the precise part that remains open, if partial>
```

`scarcity-only` and `none` both resolve to `UNSUPPORTED NOVELTY CLAIM`. This is not a harsh reading — it is the reading a reviewer will apply, and it is better to meet it here.

## 5. Contradictory evidence

Contradictions are reported, never smoothed. For each:

- both positions, with sources and locators
- the evidence quality on each side — study type, scale, setting, whether validated or proposed
- what would resolve it
- how the thesis currently proceeds despite it

Suppressing a contradiction that a reviewer will find is more damaging than reporting one the thesis cannot yet resolve.
