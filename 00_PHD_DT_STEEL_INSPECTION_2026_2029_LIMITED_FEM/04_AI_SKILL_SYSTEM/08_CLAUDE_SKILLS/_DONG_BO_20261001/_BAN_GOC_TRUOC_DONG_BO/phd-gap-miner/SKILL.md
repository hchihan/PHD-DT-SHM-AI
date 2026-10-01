---
name: phd-gap-miner
description: Deep-read the Limitations, Discussion, Conclusion and future-work content of a full PDF and score its impact against the three locked research gaps of the Data-informed Digital Twin — Limited-FEM PhD thesis (condition-evidence qualification, component-level traceability, evidence-to-action), using a Claim → Evidence → Limitation → Gap-impact → Allowed-usage-location table, then append the finding to the thesis audit file (KHÔNG NỘP). Use when the user supplies a new PDF and asks to đọc sâu limitation, tìm research gap từ tài liệu này, soi phần limitation, or whether a paper narrows/widens one of the three locked gaps. Complements deep-read-phd-papers (full audit + teach-back) and govern-phd-evidence (scope/RQ/WP/Gate routing) — this skill only does limitation-mining and gap-impact scoring, then writes the result into the audit trail.
---

# PhD gap miner

Take one full PDF, extract every limitation-bearing statement, and decide whether it narrows, widens, or leaves untouched one of the thesis's three locked research gaps. Output is a table plus a direct append to the audit file. Never touch the three submission chapters in this skill — that stays a separate, deliberate step the user asks for by name.

## Required reading before scoring any paper

Read both reference files in full before extracting or scoring:

- [references/locked-gaps.md](references/locked-gaps.md) — the three gaps' exact Claim wording, the defense-level scale, the four evidence layers, and the prohibited-claims list. Every score in this skill is relative to this file; never improvise a fourth gap or a different wording of an existing one.
- [references/extraction-protocol.md](references/extraction-protocol.md) — where to look for limitations beyond a section literally titled "Limitations", the limitation-type taxonomy, the verification-level scale, and the exact audit-append mechanics.
- [references/opportunity-radar.md](references/opportunity-radar.md) — a separate pass for spotting future-development angles (cross-domain transfer, reusable tooling, methodological combinations, recurring unresolved threads) that the user has not yet noticed. Kept strictly apart from gap-impact scoring; never edits the current thesis scope on its own.

If a current source-of-truth architecture file is supplied by the user (e.g. `RESEARCH_ARCHITECTURE.md`), read it and prefer it over the restated summary in `locked-gaps.md` if the two conflict — the restatement is a convenience copy, not the source of truth.

## Workflow

### 1. Establish the source

Require the original PDF. Ask for it if only a citation, abstract, or Consensus snippet is supplied — this skill's scoring assumes full-text access; state explicitly which parts of the analysis (if any) had to run on partial text, and downgrade verification level accordingly per `extraction-protocol.md`.

### 2. Read for limitations, not for the whole paper

Do not summarize the paper end to end. Read title/abstract/method only enough to know what the paper claims and what it validated. Then apply the search strategy in `extraction-protocol.md` to pull every limitation-bearing statement, whether or not it sits under a heading called "Limitations."

### 3. Classify each statement

For each limitation-bearing statement, capture: the claim it qualifies, the exact evidence for the limitation (quote or precise paraphrase with a page/section locator), the limitation type (see taxonomy), and which of the three gaps it could plausibly touch — often none.

### 4. Score gap-impact

For each statement that touches a gap, decide `NARROWS`, `WIDENS`, or `NO_CHANGE`, and state a resulting defense-level for that gap (`STRONG` / `NARROW_BUT_DEFENSIBLE` / `WEAK` / `NOT_DEFENSIBLE`) using the rubric in `locked-gaps.md`. Never move a gap's defense level on the strength of one paper alone — a single paper can only be logged as one data point; state explicitly how many independent sources now support the same conclusion before changing a defense level, and if this is the first, log it as a candidate only.

### 5. Determine allowed-usage-location

State which thesis location (chapter + section number, e.g. "C4 §4.4.2 giới hạn của gap") this finding is *allowed* to update, per the existing routing already established in that chapter. If no location fits, write "không có vị trí phù hợp trong ba chương hiện tại — chỉ ghi vào audit." Do not invent a new section to house an orphan finding.

### 6. Produce the table

One row per limitation-bearing statement, in this exact column order:

`Nguồn | Claim | Evidence | Loại limitation | Gap bị ảnh hưởng | Gap-impact | Mức bảo vệ sau khi xét | Allowed-usage-location`

### 7. Append to the audit file

Follow the exact mechanics in `extraction-protocol.md` §Audit append. Always append (never delete or renumber existing entries), always add a fresh conflict number (`X-NN`) only for genuine new conflicts, and always leave a follow-up line in Part 8 ("VIỆC CẦN LÀM TRƯỚC KHI NỘP") if the finding creates unresolved work.

### 8. Propose, do not silently apply, chapter edits

Report the table and the audit append to the user first. Only edit Chapter 2/3/4 body text in the same turn if the user's original request already authorized it (e.g. they asked to "cập nhật luôn" or this mirrors a pattern of standing approval already established in the conversation); otherwise offer the edit and wait.

### 9. Scan the same reading for future-development opportunities

After gap-impact scoring is done, re-read the same limitation/future-work/discussion passages with a different question in mind: not "does this affect the three locked gaps" but "does this paper contain a signal — a technique, dataset, recurring unresolved thread, or cross-domain angle — that could become a future paper or capability the user has not yet noticed." Follow `references/opportunity-radar.md` for the search patterns, the classification taxonomy, and the output table. This pass is additive and separate: it never edits Chapter 2/3/4, never changes an RQ/WP/Gate, and never feeds the gap-impact table. Log it in its own audit section (`PHẦN 9`), distinct from the gap-evidence sections in `PHẦN 7`. If a signal recurs across multiple already-reviewed papers and keeps not fitting any of the three locked gaps, flag this explicitly to the user as `TAXONOMY_PRESSURE` — worth their attention, not a decision this skill makes.

## Non-negotiable controls

- Do not fabricate a quotation, page number, DOI, sample size, or limitation the paper does not state or defensibly imply.
- Do not treat the abstract as proof of a limitation; a limitation claim needs the full-text passage.
- Do not create a fourth gap, rename a gap, or restate a gap's Claim in looser language than `locked-gaps.md`.
- Do not change a gap's defense level from one paper. Log single-paper findings as candidates.
- Do not let FEM become a diagnostic axis, RQ, WP, chapter, paper or Gate regardless of what the new paper argues.
- Do not introduce field damage diagnosis, predictive maintenance, RUL, calibrated-FEM diagnosis, weighted Health Index, or autonomous maintenance decisions as an allowed-usage-location, even if the source paper does these things.
- Do not claim a standard's clause content from a secondary academic source; if the paper cites ISO/TCVN/IFC clause text, mark it `SECONDARY_ONLY` and leave a `[CẦN ĐỐI CHIẾU BẢN GỐC: ...]` placeholder rather than asserting the clause.
- Write "Bằng chứng hiện chưa đủ" whenever a gap-impact call cannot be made confidently from the available text.
- Do not let a future-development opportunity silently become a current RQ, WP, chapter, or Gate. Log it in `PHẦN 9` and let the user decide; do not act on it unprompted.
- Do not present a single-source opportunity note with the same confidence as a multi-source one. Always state the count of independent sources behind it.
