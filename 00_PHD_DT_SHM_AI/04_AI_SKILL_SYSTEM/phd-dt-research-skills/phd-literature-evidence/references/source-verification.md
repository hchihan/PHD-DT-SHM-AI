# Reference — Source verification procedure

**v1.0 · 2026-08-10.** Adapted from ARS mechanisms #4 (citation existence verification) and #6 (locators), expressed as a procedure rather than a script — the upstream Python clients require a shell this environment does not provide for the thesis drive.

---

## The three states a reference can be in

| State | Meaning | How it may be used |
|---|---|---|
| `VERIFIED` | Located in the project corpus, or confirmed to exist through a check recorded in this session | Cite normally, with locator |
| `UNVERIFIED` | Referenced by the researcher or found in a secondary summary, existence not confirmed here | Cite **with the `UNVERIFIED` marker attached**, and state what check is outstanding |
| `NOT FOUND` | Searched for and not located | Do not cite. Report the failure and what was searched |

There is no fourth state. A reference is never quietly upgraded because it looks plausible, and never quietly dropped because it was inconvenient — a dropped reference loses information the researcher may need.

## Verification order

1. **Project corpus first.** Search `02_EVIDENCE_BASE/RQ2_GATES2_3/` Round reports, `06_LITERATURE_AND_ZOTERO/`, and the evidence addenda. A reference already deep-read in this project is the strongest verification available, because the researcher has read it.
2. **Existing bibliographic records second.** Zotero-derived material in the repository.
3. **External check third, only if needed.** Confirm existence via title + first author + year. Record what was checked and how.
4. **If none of these resolve it → `UNVERIFIED`.** Say so plainly.

## Locators

Every supporting citation carries a locator so the claim can be checked without re-reading the whole source:

```text
[Author Year, p. 14]        [Author Year, §3.2]        [Author Year, Table 4]
```

For repository artifacts, the locator is the path plus section:

```text
[G2_G3_ROUND3B_HISTORY_ACCOUNTABILITY_AND_SEARCH_CLOSURE.md, §Search closure]
```

A citation without a locator supports nothing checkable. When a locator cannot be given, say which part of the source is being relied on and mark the claim as needing locator confirmation.

## What to do when asked to "add some suitable papers"

This request is common, reasonable-sounding, and the direct route to a fabricated bibliography. `AGENT_RULES.md` §6 forbids inventing references, and the failure survives into the published record.

Respond with the four things that are actually useful:

1. **State plainly that references cannot be invented**, and why it matters here.
2. **Name the claim that needs support**, precisely. Often the claim is doing more work than it should, and narrowing it removes the need for new sources.
3. **Point at the closest existing corpus entries** — with paths — that already bear on it.
4. **Describe the search that would find real support**: the concepts, the venue types, the year window. Note that reopening broad search is a researcher decision because `CLOSE_SEARCH` is in force.

Never produce a formatted reference list of works whose existence has not been confirmed, even labelled as suggestions — formatted references get copied.

## Claim–citation alignment

Existence is not support. After confirming a source exists, confirm it says what it is cited for:

1. Locate the specific passage.
2. Compare the passage's scope with the claim's scope. Watch for the common drifts: the source studied a different structure type, a different scale, a controlled setting cited as field evidence, a proposal cited as a validated result, or a single case cited as a general finding.
3. If the passage is narrower than the claim, either narrow the claim or find a source that covers it. Do not bridge the gap with a hedge.

Report misalignment as a finding, with the claim, the source, the passage, and the specific mismatch.
