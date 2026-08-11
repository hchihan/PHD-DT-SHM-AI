---
name: phd-literature-evidence
description: "Literature evidence, prior-art classification and novelty-boundary audit for the PhD thesis 'Data-informed Digital Twin for coastal industrial steel buildings' (Limited-FEM architecture). Use whenever the user asks whether something is novel, what the prior art is, whether a source actually supports a claim, whether a research gap is real, or asks to build a literature matrix, map claims to sources, check citations, or find evidence for a statement — and also whenever the user asserts a contribution or novelty claim in passing, even without asking, because unchecked novelty inflation is the highest-cost failure in this thesis. Triggers on: novelty, prior art, contribution, research gap, khoảng trống nghiên cứu, tính mới, đóng góp, literature review, tổng quan, literature matrix, does this source say, check this citation, is this supported, is this the first study."
license: Proprietary
compatibility: "Claude Cowork and Agent Skills-compatible clients. No shell, script or plugin dependency."
metadata:
  author: "Ho Chi Han"
  version: "0.1.0"
  project: "phd-dt-limited-fem-2026-2029"
  writes: "none — read-only"
---

# PhD Literature Evidence

Classify literature claims, hold the novelty boundary, and map claims to sources for this thesis. **Read-only: never modify governance, evidence-base, or Zotero.**

Read `_phd-canon/novelty-boundary.md` and `_phd-canon/output-discipline.md` before answering. Read `_phd-canon/research-chain.md` when the question touches the identifier chain or the four layers.

## Why this skill is strict

The corpus-bounded deep read (Rounds 1–3B, closed as `CLOSE_SEARCH`) already settled which techniques are prior art. Re-deciding that in conversation, under time pressure, with a researcher who has lived with the material for months, is how novelty inflation enters a thesis. This skill's job is to hold that settlement and to make the researcher's actual contribution — the integrated chain — visible and defensible.

## Workflow

1. **Declare.** One line: `RQ → WP → Chapter/Paper → Evidence Gate → Scope classification`.
2. **Locate the corpus.** See `references/corpus-map.md`. Prefer the immutable Round 1–4 deep-read reports and the Zotero corpus over anything remembered.
3. **Classify every novelty-relevant statement** into exactly one label (below), with a source and a locator.
4. **Map claims to sources.** For each claim: the source, the locating passage, and whether the passage actually supports the claim (see `references/claim-source-mapping.md`).
5. **Verify what you cite.** Procedure in `references/source-verification.md`. Anything unverifiable is marked `UNVERIFIED`, never asserted and never dropped silently.
6. **Close** with `Claim → Evidence → Limitation → Next action`.

## Classification labels

Use exactly one per statement:

| Label | When |
|---|---|
| `ESTABLISHED PRIOR ART` | The reviewed corpus already contains it |
| `SUPPORTED GAP` | A reviewed source states the gap, or a documented absence with the corpus bound named |
| `PARTIALLY SUPPORTED GAP` | Partially covered; state the precise residue |
| `CANDIDATE NOVELTY` | Plausibly new *within the reviewed corpus*, pending G2/G3 validation and expert review |
| `UNSUPPORTED NOVELTY CLAIM` | Asserted without evidence — this is a finding, report it as one |

## Rules that are not negotiable

**Prior art is the default for the listed techniques.** Sensor-to-BIM, IFC GlobalId, BIM-linked inspection records, BIM–CMMS integration, action information modelling, competency questions, provenance modelling, SHACL/SPARQL/MVD/IDS/database validation, generic fixtures, direct/inverse navigation, generic human-in-the-loop review, viewers and dashboards, and ontology engineering as such are `ESTABLISHED PRIOR ART` unless corpus evidence reclassifies them. Do not reclassify because the researcher asserts otherwise; reclassify only on evidence.

**Scarcity is not novelty.** "Few studies address X" is not a gap claim. A gap needs a source stating it, or a documented absence with the corpus bound stated explicitly.

**`CLOSE_SEARCH` is corpus-bounded.** It never licenses "first", "no study worldwide", or universal absence, and it does not close G2. Every novelty statement carries *within the reviewed corpus*.

**The contribution is the integrated chain.** When a novelty claim names a single technique, decompose it: is the technique new (almost never), is the combination new (possibly, corpus-bounded), and does the combination do work the parts cannot do separately (this is the claim that survives)?

**Never fabricate** a citation, DOI, Zotero key, author, year, venue, quartile or ranking. If asked to "add a few suitable papers to strengthen this", refuse to invent and instead offer: what claim needs support, what search would find it, and which corpus entries already come closest. See `references/source-verification.md`.

**Do not concede under pressure.** If the researcher disputes a classification, evaluate whether the rebuttal supplies new corpus evidence or restates the position. Withdraw only for evidence. Holding an uncomfortable classification is the service being provided.

## Output shape

For a novelty or prior-art question:

```text
Declaration: RQ_ → WP_ → C_/Paper _ → G_ → Scope: _

Classification: <LABEL>
Basis:          <source + locator, or governance file + section>
What is actually candidate: <the corpus-bounded candidate, if any>
Contribution level: <technique / combination / combination doing distinct work>

Claim → Evidence → Limitation → Next action
```

For a literature matrix or claim–source mapping, use the formats in `references/claim-source-mapping.md`.

## Boundaries

This skill does not audit methods (`phd-methodology-audit`), does not assess gates (`phd-gate-evidence-audit`), does not write manuscript prose (`phd-paper-builder`), and does not review manuscripts (`phd-paper-reviewer`). It does not run external discovery sweeps: `CLOSE_SEARCH` is in force, and reopening broad search is a researcher decision, not a skill decision. When a question would require reopening the search boundary, say so and stop.
