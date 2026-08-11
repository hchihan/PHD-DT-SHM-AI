# PhD DT Research Skills

**v0.1.0 · 2026-08-10 ·** for the thesis *Data-informed Digital Twin Framework for Condition Monitoring and Inspection–Maintenance Support of Coastal Industrial Steel Buildings* (Limited-FEM architecture).

Derived from `academic-research-skills` v3.9.4 (upstream reference, unmodified at `D:\00_GITHUB_REPOS\academic-research-skills`). Twelve upstream mechanisms inherited, ten thesis-specific capabilities added, four upstream skill shells discarded. See `../ARS_TO_PHD_SKILLS_20260810/01_ARS_PHD_AUDIT.md`.

---

## Built so far

| Skill | Status | Replaces upstream | Writes? |
|---|---|---|---|
| `_phd-canon/` | shipped v1.0 | `shared/` | — |
| `phd-literature-evidence` | shipped v0.1.0, evaluated | `deep-research` | no |
| `phd-research-state` | shipped v0.1.0, untested | `academic-pipeline` | no |
| `phd-paper-reviewer` | shipped v0.1.0, untested | `academic-paper-reviewer` | no |
| `phd-methodology-audit` | not built | — | no |
| `phd-gate-evidence-audit` | not built | — | no |
| `phd-paper-builder` | not built | `academic-paper` | drafts only |

No orchestrator. Routing is by skill description plus `_phd-canon/which-skill.md`.

## Installing in Cowork

Each skill directory is self-contained apart from `_phd-canon/`, which all of them read. Keep the whole `phd-dt-research-skills/` tree together so the relative canon references resolve.

## The two rules that govern everything here

1. **The repository is the source of truth.** No skill stores research state. Statuses are read from `01_CURRENT_CONTROL/` and `00_GOVERNANCE/` and quoted verbatim with their file date.
2. **No skill closes a gate.** `PASS (signed)` is a human act requiring a sign-off artifact. The strongest verdict a skill emits is `READY-FOR-REVIEW`.

## Shared canon

| File | Purpose |
|---|---|
| `research-chain.md` | Locked evidence and identifier chains; four-layer firewall; instrument boundary |
| `gate-model.md` | G1–G7 items, status vocabulary, the no-PASS rule |
| `epistemic-ladder.md` | proposal → design → specified → implemented → validated → verified |
| `novelty-boundary.md` | Prior-art list, five-level classification, `CLOSE_SEARCH` limits |
| `scope-control.md` | Core/Supporting/Future Work/Out of Scope; prohibited expansions; FEM containment |
| `output-discipline.md` | Declaration line; Claim → Evidence → Limitation → Next action; no-fabrication rules |
| `failure-modes.md` | F1–F13, the reviewer's attack surface |
| `which-skill.md` | Routing table and boundary tests |

## Evaluation

Pilot 1 (`phd-literature-evidence`, 4 evals × with-skill and baseline) is recorded in `../ARS_TO_PHD_SKILLS_20260810/03_SKILL_EVALUATION_REPORT.md`, with the reviewable outputs at `../phd-literature-evidence-workspace/PILOT1_REVIEW.html`.
