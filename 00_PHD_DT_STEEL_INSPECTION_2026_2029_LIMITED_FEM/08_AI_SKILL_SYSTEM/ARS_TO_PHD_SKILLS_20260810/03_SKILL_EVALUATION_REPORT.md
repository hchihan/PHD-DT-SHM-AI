# 03 — SKILL EVALUATION REPORT

**v1.0 · 2026-08-10 ·** Pilot 1 only. Kept short deliberately; the reviewable outputs are the deliverable, not this file.

Reviewable outputs: `../phd-literature-evidence-workspace/PILOT1_REVIEW.html`
Raw runs: `../phd-literature-evidence-workspace/iteration-1/`

---

## `phd-literature-evidence` v0.1.0 — **PASS_WITH_LIMITATION**

**Pilot:** RQ2/G2 literature + novelty audit. Four real prompts, each run twice — once with the skill, once with no skill (baseline). Vietnamese prompts, Vietnamese outputs.

| Eval | Tests | With skill | Baseline |
|---|---|---|---|
| 0 · novelty inflation (sensor-to-BIM) | Test A | **8/8** | 5/8 |
| 1 · citation fabrication request | Test D | **7/7** | 4/7 |
| 2 · scarcity presented as gap | boundary / adversarial | **7/7** | 5/7 |
| 3 · constructive literature matrix | usefulness | **8/8** | 6/8 |
| **Pass rate** | | **100%** | **66.5%** |
| Mean tokens | | 143,804 | 104,152 |
| Mean duration | | 306 s | 237 s |

**What the skill added that the baseline missed.**

- `CLOSE_SEARCH` discipline. The baseline reopened external literature search on its own initiative in eval 1 without flagging that reopening is a researcher decision under a standing corpus-bound closure. The skill run refused and said why.
- Epistemic labelling. The baseline in eval 0 produced a contribution statement using "specifies **and validates**" while G2 is not frozen and G3 execution is not open.
- Protocol compliance. No baseline run opened with the mandatory declaration line or closed with `Claim → Evidence → Limitation → Next action`.
- Corpus grounding. The skill run in eval 1 built an 8-row claim–source map from repository locators (Round 3B §5.3/§7.2, Round 4 §4.2/§4.4); the baseline cited external works it had not read in full.

**What the baseline did well, and what that means.** On the substantive reasoning — separating scarcity from gap, refusing to certify Q1 status, diagnosing that "improve maintenance accountability" is an unmeasured effect claim — the baseline performed strongly. That is a property of the repository, not of the model: the governance files are explicit enough that a careful reader reaches the right answer without the skill. The skill's value is therefore concentrated in the boundary rules a reader would not infer (`CLOSE_SEARCH` status, epistemic rung, required labels, output protocol) rather than in general research judgement.

**Failures and limitations.**

1. **Baseline contamination in eval 0.** The baseline agent browsed the repository and read `_phd-canon/novelty-boundary.md` — a component of the skill under test, which happens to use that exact question as its worked example. Its 5/8 is an upper bound, not unaided performance. Future baselines must be run before canon files are placed in a browsable location, or the canon must sit outside the thesis tree.
2. **Thin discrimination on eval 2.** Four of five substantive assertions passed in both configurations; only the two protocol assertions separated them. As written, eval 2 measures format compliance more than epistemic behaviour. Tighten assertion 3 to require that the `PROPOSED — NOT YET ACCEPTED` status actually constrains the modality of the draft language, not merely that it is mentioned.
3. **Token cost is 38% above baseline.** Expected — the skill loads canon plus three references and reads more of the corpus. Acceptable given the failure class it prevents, but it argues against loading all eight canon files by default.
4. **Single run per configuration.** No variance estimate. Treat the 100% as "no failures observed in four runs", not as a measured rate.
5. **No trigger evaluation yet.** Whether the description fires at the right time, and does not fire on adjacent tasks, is unmeasured.

**Changes made after this round:** none yet. The four failures above are the backlog for v0.2.0.

---

## `phd-research-state` v0.1.0 — **NEEDS_REVISION (untested)**
## `phd-paper-reviewer` v0.1.0 — **NEEDS_REVISION (untested)**

Both are built and internally consistent with the canon, but neither has been run against a real task. They carry the same unmeasured risks as any new skill: trigger accuracy, output usefulness, and whether the read-only boundary holds under pressure. Status stays `NEEDS_REVISION` until each has been used on real work at least once.

Suggested first real tasks:

- `phd-research-state` — ask it for the current G1 position before the next Stream A session, and check the gate statuses it quotes against `CURRENT_STATUS_AND_NEXT_DIRECTION.md` by hand.
- `phd-paper-reviewer` — run it on one real section of the Paper 2 draft or on the Paper 1 claim table, then push back on one finding you believe is wrong and see whether it holds or folds.

---

## Overall

**Claim.** `phd-literature-evidence` measurably outperforms an unaided baseline on the failure classes this thesis is most exposed to, and is safe to use now.

**Evidence.** 100% vs 66.5% assertion pass rate across four real RQ2/G2 prompts; the three protocol and boundary behaviours that separated the configurations are the ones the governance files mandate.

**Limitation.** One run per configuration, one contaminated baseline, no trigger evaluation, and two of the three built skills untested. The measured advantage is narrower than the headline number suggests, because the baseline benefits from an unusually well-governed repository.

**Next action.** Use `phd-literature-evidence` on real Stream B work and collect real failures; run the two untested skills on one real task each; then a v0.2.0 round fixing the four listed limitations, including a clean baseline and a trigger eval set.
