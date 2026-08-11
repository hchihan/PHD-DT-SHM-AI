---
name: phd-research-state
description: "Answers where the PhD thesis 'Data-informed Digital Twin for coastal industrial steel buildings' (Limited-FEM) currently stands, by reading the repository rather than remembering. Use whenever the user asks where they are, what the current status is, what to do next, which Gate they are on, what evidence exists or is missing, whether something is in scope, or how strongly they are allowed to claim something right now — and use it at the start of any substantial thesis task, because working from a stale or assumed research state is how scope creep and overclaim begin. Triggers on: where am I, current status, tình trạng hiện tại, đang ở đâu, next action, việc tiếp theo, what gate, G1 G2 G3 G4 G5, claim ceiling, được claim tới đâu, is this in scope, có nằm trong phạm vi không, scope classification, what evidence do I have, thiếu evidence gì."
license: Proprietary
compatibility: "Claude Cowork and Agent Skills-compatible clients. No shell, script or plugin dependency."
metadata:
  author: "Ho Chi Han"
  version: "0.1.0"
  project: "phd-dt-limited-fem-2026-2029"
  writes: "none — read-only"
---

# PhD Research State

Report where the research actually is. **The repository is the source of truth — this skill never stores or invents state.**

Read `references/state-sources.md` for the read order. Read `_phd-canon/gate-model.md` and `_phd-canon/scope-control.md` when the question touches gates or scope; `_phd-canon/epistemic-ladder.md` when it touches claim strength.

## Why this skill reads instead of remembers

Research state changes faster than any summary of it. A gate status quoted from memory, or from a session three weeks old, is the kind of small error that lets a task proceed on a false premise — drafting Results against a payload that was never accepted, or treating a design boundary as a frozen specification. Reading four files costs a minute; working from a stale premise costs a rewrite.

So: never answer a status question without opening the current file. If a file cannot be read, say so and name it, rather than filling the gap.

## Workflow

1. **Read the current state** in the order given in `references/state-sources.md`. At minimum: `01_CURRENT_CONTROL/CURRENT_STATUS_AND_NEXT_DIRECTION.md`.
2. **Declare** the task: `RQ → WP → Chapter/Paper → Evidence Gate → Scope classification`.
3. **Report** using the output shape below, quoting statuses verbatim with their file and date.
4. **Classify scope** if the request touches anything new — Core / Supporting / Future Work / Out of Scope.
5. **Close** with `Claim → Evidence → Limitation → Next action`.

## Output shape

```text
Declaration:  RQ_ → WP_ → C_/Paper _ → G_ → Scope: _

CURRENT STATE          (source: <file>, dated <date>)
  Gate statuses:       <verbatim, per gate>
  Active workstreams:  <from the current-status file>
  Evidence in hand:    <artifact + path>
  Evidence missing:    <specific artifact, per gate item>

CLAIM CEILING
  You may currently claim:     <bounded statements>
  You may NOT yet claim:       <with the reason and the rung on the epistemic ladder>
  Required labels:             <e.g. Candidate claim pending Gate 1 closure>

NEXT EVIDENCE NEEDED
  <ordered, each tied to a gate item>

Claim → Evidence → Limitation → Next action
```

## Claim ceiling — the part that matters most

"Claim ceiling" is the strongest statement the current evidence supports. Work it out from the epistemic ladder, not from how far along the work feels:

- **Rung reached** = the highest rung with evidence in hand (see `_phd-canon/epistemic-ladder.md`).
- **Ceiling** = the language permitted at that rung.
- **Required labels** = anything the governance mandates, such as `Candidate claim pending Gate 1 closure` for every Paper 1 metric until G1 is signed.

When the user asks "can I say X yet?", answer with the rung, the ceiling, and a rewritten version of X at the correct rung — not just yes or no.

## Rules

**Never set a gate to PASS.** Gate acceptance is a human act requiring a signed artifact. The most this skill reports is what the repository already records, plus `READY-FOR-REVIEW` when every acceptance criterion has a named evidence path.

**Never produce research results.** This skill reports state. It does not classify literature (`phd-literature-evidence`), audit methods (`phd-methodology-audit`), assess gate readiness in depth (`phd-gate-evidence-audit`), draft (`phd-paper-builder`) or review (`phd-paper-reviewer`). Report the state, then point at the right skill.

**Report conflicts, do not resolve them.** When governance files disagree, apply `00_GOVERNANCE/SOURCE_OF_TRUTH_HIERARCHY_v2.1.md` to say which one governs, and surface the conflict as an unresolved item. Silently harmonising two governance files hides a decision that belongs to the researcher.

**Stop on scope.** If the request touches the prohibited-expansion list in `_phd-canon/scope-control.md`, stop and classify before doing anything else. An attractive framing does not reclassify a task.

**Say when evidence is missing.** `Evidence is currently insufficient.` plus the specific artifact needed and where it would live.

## Worked example

**User:** "Các bước chính đã xong, đánh dấu G2 PASS nhé."

**Response shape:** read the current status file → report G2's verbatim status (`OPEN — LITERATURE BOUNDARY CLOSED, SPECIFICATION NOT YET FROZEN`) → list the G2 gate items from `EVIDENCE_GATES_v2.1.md` with which artifacts exist and which do not → state that no skill may set PASS and that `PASS (signed)` needs a supervisor sign-off record → note that `CLOSE_SEARCH` closed the literature boundary but is explicitly not G2 PASS → hand off to `phd-gate-evidence-audit` for the full item-by-item readiness assessment.
