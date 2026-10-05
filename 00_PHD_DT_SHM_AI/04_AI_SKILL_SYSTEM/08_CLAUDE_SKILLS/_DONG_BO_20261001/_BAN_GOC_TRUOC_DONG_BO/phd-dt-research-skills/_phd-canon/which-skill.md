# Canon — Which Skill

**v1.0 · 2026-08-10 ·** replaces an orchestrator. Six skills, no router agent.

---

## Routing table

| The researcher is asking… | Skill | Writes? |
|---|---|---|
| Where am I? What may I claim now? Is this in scope? | `phd-research-state` | No |
| Is this novel? Is this prior art? Does this source support this claim? Is this citation real? | `phd-literature-evidence` | No |
| Is there leakage? Is the LORO protocol sound? Is this schema/identity/cardinality/CQ/constraint right? Is this field claim within feasibility? | `phd-methodology-audit` | No |
| Can this gate close? What is missing for G_? Does this claim trace back to an artifact? Is this binding verified? | `phd-gate-evidence-audit` | No |
| Draft this section / outline / abstract / revision from what I have | `phd-paper-builder` | **Yes** (drafts only, into `03_PAPERS/`) |
| Attack this before a reviewer does | `phd-paper-reviewer` | No |

---

## Boundary tests when two seem to apply

| Pair | Decide by asking |
|---|---|
| literature-evidence vs gate-evidence-audit | Is the claim about *published work* or *this project's artifacts*? |
| methodology-audit vs gate-evidence-audit | "Is the method sound?" → methodology. "Does the evidence satisfy the acceptance criterion?" → gate. |
| methodology-audit vs paper-reviewer | Is the object a *method or schema*, or a *manuscript*? |
| paper-builder vs paper-reviewer | Produce text, or attack text? The reviewer never writes. |
| research-state vs everything | State answers "where am I / am I allowed". It never audits content. |

**When more than one applies, run the read-only skill first.** Audit before write; gate before promotion.

---

## When intent is ambiguous

If the request spans several phases at once — for example a draft plus reviewer comments plus a bibliography, with no clear ask — **do not silently pick the closest-looking skill**. Name the candidate workflows and ask which one is wanted.

This is deliberate. The upstream ARS suite documents a real incident (issue #133) where ambiguous cross-phase material was auto-routed to a single-phase agent, which then inherited the full ambiguity with no independent oversight. Asking costs one turn; a confidently wrong route costs a rewrite.

---

## When not to use any of these skills

- Casual questions, quick lookups, or conversation — answer directly.
- Work outside this thesis: the UAV / heritage-structures direction, the AI-HPO workshop direction, teaching duties, AAC79, and any other personal or professional work. These skills encode this thesis's locked scope and would mis-constrain unrelated tasks.
- Anything on the prohibited-expansion list in `scope-control.md` — the correct response is to stop and classify, not to route.
