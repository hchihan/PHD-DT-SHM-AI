# Reference — Re-review and revision traceability

**v1.0 · 2026-08-10.** Adapts ARS mechanisms #13 (R&R traceability matrix) and the `re-review` mode, aligned to the existing thesis practice in `03_PAPERS/PAPER_1/REVISION_HISTORY/PAPER1_GATE1_MAJOR_REVISION_LOG_v2.md`.

---

## When to use this instead of a fresh review

Use re-review when a previous round of findings exists — from this skill, from a supervisor, or from a journal. The question is no longer "what is wrong" but "did the revision actually fix what was raised, and did it break anything else".

## The traceability matrix

| # | Original finding | Severity | Author response | Manuscript change (verbatim, with location) | Verdict |
|---|---|---|---|---|---|

**Verdict values:**

- `RESOLVED` — the change addresses the finding, and the text now says something the evidence supports
- `PARTIALLY RESOLVED` — moved in the right direction; name precisely what remains
- `NOT RESOLVED` — the finding stands; say whether the response engaged with it
- `RESPONSE WITHOUT CHANGE` — the author argued rather than edited. Evaluate the argument on the concession rule in `review-protocol.md`; this is a legitimate outcome when the argument supplies evidence
- `NEW ISSUE INTRODUCED` — the revision created a problem that was not there before

Quote the actual manuscript text in the change column. An author's description of what they changed and what the text now says are different objects, and the second is what a reviewer sees.

## Regression sweep

Revisions leak. After checking the matrix, sweep specifically for:

1. **Label loss.** Did `Candidate claim pending Gate 1 closure` survive in every place a Paper 1 metric appears — including new text, the abstract and captions?
2. **Hedge drift.** A sentence softened in round 1 often hardens again in round 2 when the paragraph around it is rewritten.
3. **Epistemic promotion.** Did a design element quietly acquire a stronger verb while the paragraph was being restructured?
4. **Orphaned references.** Did a source removed from one section leave a claim behind that still depends on it?
5. **Cross-section contradiction.** Does the revised Discussion still match the Results, and does the Conclusion still match both?
6. **Scope drift.** Did anything from the prohibited-expansion list enter as a "strengthening" — calibrated FEM, RUL, predictive maintenance, lab→field transfer?

## Response letter check

When a response letter exists, verify each response against the manuscript rather than against itself. Three patterns to watch:

- **"We have clarified this"** — check whether the text changed at all, or only the surrounding text.
- **"We have added a limitation"** — check that the limitation actually constrains the claim rather than sitting in a separate paragraph while the claim stands unchanged.
- **"As suggested, we have removed this claim"** — check that it was removed everywhere, not only where the reviewer quoted it.

## Output

Matrix first, regression sweep second, then `Claim → Evidence → Limitation → Next action`. Terminal states are the same as a fresh review: `CRITICAL ISSUES`, `MAJOR ISSUES`, `MINOR ISSUES`, `NO BLOCKING ISSUES FOUND`. There is no accept verdict, and a clean re-review does not close a gate.
