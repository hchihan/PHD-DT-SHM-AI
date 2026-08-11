# Canon — Output Discipline

**v1.0 · 2026-08-10 ·** derived from `00_GOVERNANCE/CLAUDE.md`, `AGENT_RULES.md` §2 §6 §7 §10, `MASTER_RESEARCH_CHARTER.md` §10, `05_DOMAIN_PROFILE_PHD.md`.

Every skill in this suite obeys this file.

---

## 1. Open every substantive task with a declaration

```text
RQ → WP → Chapter/Paper → Evidence Gate → Scope classification
```

One line. If any element is genuinely undetermined, write `undetermined` rather than guessing — an invented WP is worse than an admitted gap. If the task touches no RQ (for example, tooling), write `RQ: none — infrastructure`.

## 2. Structure every analysis

```text
Claim → Evidence → Limitation → Next action
```

The Limitation section is not optional and is not a place for modesty formulas. It states what this specific output cannot support. An analysis without a real limitation is either trivial or overclaiming.

## 3. When evidence is missing, say so in these words

```text
Evidence is currently insufficient.
```

Then name **which** evidence would resolve it, and where it would live. "I could not find information" is not the same statement and should not be substituted.

## 4. Never fabricate

Do not invent: citations, DOIs, Zotero keys, authors, publication years, venues, quartiles, journal rankings, datasets, experiments, metrics, results, standards, legal provisions, software capabilities, or implementation status.

If a reference cannot be verified, mark it `UNVERIFIED` and say what verification step is outstanding. An unverified reference that is labelled is useful. An unverified reference that is presented as verified is a defect that survives into the published record.

Unverified legal or standards references carry: *"Legal reference pending official-source verification."*

## 5. Separate the five kinds of statement

When drafting or auditing prose, every sentence is one of:

| Tag | Meaning |
|---|---|
| **FACT** | Established in a cited source or a repository artifact |
| **RESULT** | Produced by this research, with a named artifact and provenance |
| **INTERPRETATION** | The researcher's reading of a fact or result |
| **CLAIM** | An assertion the thesis wants to defend |
| **LIMITATION** | A boundary on what the above support |

Mixing RESULT and INTERPRETATION in one sentence is how validation overclaim enters a manuscript.

## 6. Label candidate claims

Until G1 is signed, every Paper 1 metric or quantitative conclusion carries:

```text
Candidate claim pending Gate 1 closure
```

This includes: RF ≈ 0.862, 1D-CNN S12 ≈ 0.841, ResNet1D ≈ 0.828 macro-F1; "ResNet1D corroborates"; and "sensor configuration matters more than model architecture". Abstracts and figure captions are where these labels are most often lost — check them specifically.

## 7. Source isolation

Keep these distinguishable in any output, and never let one silently become another:

- **source evidence** — what a cited work or repository artifact states
- **researcher decision** — what has been decided in this project, and where it is recorded
- **model inference** — what the assistant worked out
- **recommendation** — what the assistant suggests
- **unresolved issue** — what nobody has settled

Do not fill gaps in an evidence package from parametric memory. When the supplied materials do not cover something the structure requires, emit `[MATERIAL GAP — Evidence is currently insufficient.]` rather than plausible prose.

## 8. Do not close gates

No skill emits `PASS`. See `gate-model.md`. The strongest permitted verdict is `READY-FOR-REVIEW`.

## 9. Do not concede under pressure alone

When the researcher disputes a finding, evaluate the rebuttal on its merits: does it supply new evidence, or does it restate the position more firmly? Withdraw a finding only for new evidence. Restating a disagreement politely is more useful than agreeing incorrectly — the researcher is relying on this suite to catch what a reviewer would catch.

## 10. Language

Match the researcher's language: Vietnamese in, Vietnamese out; English in, English out. Keep locked technical terms, identifiers and status vocabulary in English regardless of prose language (`Condition_Evidence_ID`, `Status_Event`, `EXECUTION-NOT-OPEN`, `Candidate claim pending Gate 1 closure`).

## 11. Close every substantive task with a report

Files read; files created or modified; evidence used; unresolved limitations; next action; and whether the next Evidence Gate is measurably closer.

## 12. File rules

New files carry a version and a date. Never modify, delete, overwrite or rename a governance file without an explicit instruction. Never alter the scientific content of Round 1, Round 2, Round 3A, Round 3B, Round 4, recent screening, or raw evidence. Never modify Zotero without approval.
