# Opportunity radar: spotting future-development angles the user hasn't seen yet

This is a separate pass from gap-impact scoring. Gap-impact asks "does this narrow or widen one of the three locked gaps." The opportunity radar asks a different question: "does this paper contain a signal — a technique, a dataset, a recurring unaddressed thread, a cross-domain angle — that could become a future paper, a post-PhD extension, or a capability worth building later, even though it has no place in the current locked architecture."

**This pass never changes the current thesis.** Nothing found here edits Chapter 2/3/4, changes an RQ/WP/Gate, or feeds the gap-impact table in `locked-gaps.md`. It is a separate, clearly-labeled log the user reads when they choose to, not a silent expansion of scope. If a finding here looks strong enough to belong in the current thesis, say so explicitly and let the user decide — do not fold it in yourself.

## Where the signal usually hides

- The paper's own "future work" that goes *beyond* what the three locked gaps ask for (not "we should test more units" — that's a gap-impact limitation — but "this could be extended to X domain" or "a natural next step is Y capability").
- A technique or dataset the paper used for an unrelated purpose that happens to transfer well to this thesis's problem (e.g. a leakage-detection method built for a different sensor type; a provenance ontology built for a different industry).
- A recurring thread across multiple papers read so far that none of them resolved and that sits *outside* the three gaps as currently worded — this can be a signal that the gap taxonomy itself may need a fourth entry someday, which is a decision for the user and the thesis committee, never something this skill decides on its own.
- Tooling, a public dataset, an open-source library, or a benchmark the paper introduces that could be reused as infrastructure for a future paper.
- A collaboration or venue angle: the paper is from a group/lab whose stated interests overlap with a direction the user might want to pursue after this thesis.
- A methodological combination nobody in the reviewed corpus has tried yet (e.g. pairing technique A from one reviewed paper with technique B from another), noticed only because both papers were read carefully in the same session.

## Classification

Tag each opportunity note with one type:

- `FUTURE_PAPER_CANDIDATE` — a plausible standalone paper beyond the current three, for after this PhD or as an explicit scope-expansion decision
- `CROSS_DOMAIN_TRANSFER` — a technique proven elsewhere that could transfer to this problem
- `TOOLING_OR_DATASET_REUSE` — a reusable artifact (code, dataset, benchmark) worth tracking
- `METHODOLOGICAL_COMBINATION` — a pairing of ideas from two or more already-reviewed sources
- `TAXONOMY_PRESSURE` — a recurring thread that keeps not fitting any of the three locked gaps, worth flagging to the user as a possible sign the gap set itself deserves review (never resolved by this skill alone)
- `COLLABORATION_OR_VENUE` — a lab, dataset owner, or venue worth knowing about for later

## Confidence

State how many independent sources support the same opportunity signal. One paper mentioning something in passing is a note to watch, not a recommendation to act on. Say so plainly: "một nguồn, chưa có nguồn thứ hai xác nhận" versus "nguồn thứ ba lặp lại cùng một hướng."

## Output format

One row per opportunity, appended to the audit under its own section (never mixed into the gap-impact table):

`Nguồn | Loại cơ hội | Mô tả | Vì sao nằm ngoài phạm vi luận án hiện tại | Số nguồn độc lập ủng hộ | Điều kiện để trở thành khả thi`

## Audit placement

Append to a dedicated `## PHẦN 9. CƠ HỘI MỞ RỘNG VÀ HƯỚNG PHÁT TRIỂN TƯƠNG LAI (KHÔNG THUỘC PHẠM VI LUẬN ÁN HIỆN TẠI)` section, created once at the end of the audit file if it does not yet exist, appended to (never rewritten or reordered) on every later run. Keep this section strictly after `PHẦN 8` so the checklist for submission stays the last actionable thing a reader sees before this speculative log. Never merge a row from this section into `PHẦN 7`'s gap-evidence tables.
