# PAPER2_SELF_REFERENCE_AUDIT

Audited object: `PAPER2_MANUSCRIPT_v1.md` (all sections), `PAPER2_CLAIM_SOURCE_MATRIX.csv`, `PAPER2_RESEARCH_GAP_FINAL.md`, `PAPER2_CONTRIBUTION_FINAL.md`. Date 2026-10-07.

## 1 Reference-list check

- Reference list: 19 external items, all with DOI verified against OpenAlex or the publisher PDF.
- Internal markdown, CSV, ADR, manifest, Gate report or evidence log in the reference list: **none**.
- Authors' own Paper 1 (unpublished): **not cited**. Claim CL-25 ("Paper 1 provides the condition evidence") was removed; condition evidence is treated as an abstract record type (Section 3.1).
- Future data repository: not cited (does not yet exist).

## 2 Section-by-section findings

| Section | Flag found | Problem | Why problematic | Correction | Status |
|---|---|---|---|---|---|
| Abstract | INTERNAL_RESULT_USED_TO_PROVE_NOVELTY (draft risk) | Pass rates appear next to the gap sentence | A reader may read 145/145 or 78/78 as proof of contribution | Gap sentence cites "the ten closest studies"; pass rates follow and are labelled internal verification; closing sentence states what is not shown | FIXED in v1 |
| 1.1–1.5 | none | External references only | — | — | PASS |
| 1.7 Contributions | CIRCULAR_VALIDATION (risk) | Contribution 2 lists verification outcomes | Using own tests to prove own design | Wording: "verified internally"; novelty argued in 1.5 from external literature | PASS |
| 2.1–2.8 | none | No repository document cited | — | — | PASS |
| 2.8 Table 1, row "This study" | INTERNAL_RESULT_USED_TO_PROVE_NOVELTY (risk) | Own row in a positioning table | Self-assessment beside external studies | Row labels show "(synthetic)" and "identities and anomaly real; chain records synthetic" | PASS (keep labels) |
| 3 Method | none | Repository used as study documentation, not as literature | — | — | PASS |
| 3.10 | CIRCULAR_VALIDATION | Challenge set by same author as validator | Not independent | Stated as Level C internal; never called validation | PASS |
| 6.4–6.9 | CIRCULAR_VALIDATION | E3 results | Same author for fixtures and validator | Tagged [E3]; Section 6.10 Table 8 separates classes | PASS |
| 6.8 | CIRCULAR_VALIDATION | 78/78 on the same set after correction | Not fresh evidence | Explicit sentence: "not fresh evidence of robustness" | PASS |
| 7.3 | UNSUPPORTED_EXTERNAL_CLAIM (checked) | Statements about each Tier-A paper | Must match full text | Each statement checked against extracted full text 2026-10-07 | PASS |
| 7.4 | INTERNAL_RESULT_USED_TO_PROVE_NOVELTY (risk) | Contribution discussion | — | States novelty argued from literature, function shown by E3 | PASS |
| 7.6 | UNSUPPORTED_EXTERNAL_CLAIM (minor) | Practice recommendations | Derived from one case | Phrased as practices that "follow from the case" | PASS (reviewer may still ask for external support) |
| 8, 9 | none | — | — | — | PASS |
| References | SELF_CITATION_NOT_NEEDED | none present | — | — | PASS |

## 3 Remaining flags to watch in later versions

1. Do not add the authors' Paper 1 or Gate reports to motivate the gap.
2. Do not replace "internal verification" with "validation" in any edit.
3. If Table 1 is shortened, keep the synthetic labels in the "This study" row.

## 4 Audit result

**PASS.** No HIGH self-reference risk remains in the manuscript. MEDIUM risk (CL-21) is controlled by wording.
