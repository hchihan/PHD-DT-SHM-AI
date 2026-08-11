# 02 — TARGET ARCHITECTURE: PhD DIGITAL TWIN RESEARCH SKILLS

**Version:** v1.1 — APPROVED
**Created:** 2026-08-10 | **Approved:** 2026-08-10
**Status:** APPROVED BY RESEARCHER. §7 decisions settled — see §0.

---

## 0. Approved decisions (2026-08-10)

| Decision | Researcher ruling |
|---|---|
| §7.1 Gate audit + evidence traceability | **MERGE** — single `phd-gate-evidence-audit` with gate-readiness and claim-trace modes. Architecture stays at **six skills**. |
| §7.2 Orchestrator | **DO NOT BUILD** in the first round. Routing via sharp descriptions + `_phd-canon/which-skill.md`. Revisit only if Phase 4 trigger evals show cross-skill confusion. |
| §8 Build sequence | **`_phd-canon/` → `phd-literature-evidence` → Pilot 1**, then evaluate before building further. |

Build target: `H:\…\08_AI_SKILL_SYSTEM\phd-dt-research-skills\`. Upstream ARS at `D:\00_GITHUB_REPOS\academic-research-skills` remains untouched.
**Scope classification:** Supporting (research infrastructure)
**Depends on:** `00_ARS_INVENTORY.md`, `01_ARS_PHD_AUDIT.md`

---

## 1. Design position

Six skills, one shared reference pack, no orchestrator.

The organising principle differs from ARS. ARS is organised around **the manuscript lifecycle** (research → write → review → revise). This suite is organised around **the epistemic question being asked**:

| Question the researcher is actually asking | Skill |
|---|---|
| Where am I, and what am I allowed to claim right now? | `phd-research-state` |
| Is this supported by literature, and is it actually novel? | `phd-literature-evidence` |
| Is this method sound enough to survive G1/G2 acceptance? | `phd-methodology-audit` |
| Does this Gate pass, and does this claim trace to an artifact? | `phd-gate-evidence-audit` |
| Write this section from what I have verified | `phd-paper-builder` |
| Attack this before a reviewer does | `phd-paper-reviewer` |

This matters because the thesis's own governance is gate-centric, not manuscript-centric. `EVIDENCE_GATES_v2.1.md` defines the unit of progress; the manuscript is downstream of it.

---

## 2. Skill map

```text
                    ┌──────────────────────────────┐
                    │   _phd-canon/  (references)  │
                    │  read by all six skills      │
                    └──────────────┬───────────────┘
                                   │
   ┌───────────────┬───────────────┼───────────────┬────────────────┐
   │               │               │               │                │
┌──▼───────────┐ ┌─▼─────────────┐ ┌▼────────────┐ ┌▼─────────────┐ ┌▼──────────────┐
│ phd-research │ │ phd-literature│ │ phd-        │ │ phd-gate-    │ │ phd-paper-    │
│ -state       │ │ -evidence     │ │ methodology │ │ evidence-    │ │ builder       │
│              │ │               │ │ -audit      │ │ audit        │ │               │
│ READ-ONLY    │ │ READ-ONLY     │ │ READ-ONLY   │ │ READ-ONLY    │ │ WRITES drafts │
└──────────────┘ └───────────────┘ └─────────────┘ └──────────────┘ └───────┬───────┘
                                                                            │
                                                                    ┌───────▼───────┐
                                                                    │ phd-paper-    │
                                                                    │ reviewer      │
                                                                    │ READ-ONLY     │
                                                                    └───────────────┘
```

Five of six skills are strictly read-only. Only `phd-paper-builder` produces new prose, and only into `03_PAPERS/` drafts — never into `00_GOVERNANCE/`, `01_CURRENT_CONTROL/` or `02_EVIDENCE_BASE/`.

---

## 3. Per-skill specification

### 3.1 `phd-research-state`

| Field | Value |
|---|---|
| **Purpose** | Answer "where is the research now" by reading governance, never by remembering. Emit the mandatory task declaration `RQ → WP → Chapter/Paper → Evidence Gate → Scope classification`. |
| **Triggers** | "where am I", "current status", "what should I do next", "declare scope for this task", "is this in scope", "can I claim X yet", "hiện đang ở đâu", "phạm vi" |
| **Inputs** | `01_CURRENT_CONTROL/CURRENT_STATUS_AND_NEXT_DIRECTION.md` (level 5), `CURRENT_DIRECTION_LOCK_20260804.md`, `00_GOVERNANCE/*` (levels 4 & 7), `02_EVIDENCE_BASE/CURRENT/00_MASTER_INDEX_CURRENT_20260804.md` |
| **Output contract** | (1) task declaration line; (2) current Gate states table; (3) scope classification with justification; (4) next evidence needed; (5) `Claim → Evidence → Limitation → Next action` |
| **Hard rules** | Never asserts a status not present in a read file. Never writes state to its own files. If governance files conflict, applies `SOURCE_OF_TRUTH_HIERARCHY_v2.1.md` and reports the conflict rather than resolving it silently. |
| **RQ / Gate** | All / All |
| **Inherited from ARS** | Progressive disclosure (#19); reduced Socratic posture (#18); state-declaration idea from `state_tracker_agent` — *pattern only, no ledger* |
| **Removed** | Material Passport, `resume_from_passport`, collaboration-depth scoring, pipeline state machine |

### 3.2 `phd-literature-evidence`

| Field | Value |
|---|---|
| **Purpose** | Literature matrix, claim–source mapping, prior-art classification, novelty-boundary audit, contradictory-evidence surfacing, unsupported-claim detection. |
| **Triggers** | "is this novel", "prior art", "novelty boundary", "literature matrix", "does this source support", "find evidence for", "check citations", "research gap", "tổng quan", "khoảng trống nghiên cứu" |
| **Inputs** | `02_EVIDENCE_BASE/RQ2_GATES2_3/` Round 1–3B + Round 4 (immutable), `06_LITERATURE_AND_ZOTERO/`, `02_EVIDENCE_BASE/CURRENT/`, user-supplied sources |
| **Output contract** | Every claim classified as one of: `ESTABLISHED PRIOR ART` / `SUPPORTED GAP` / `PARTIALLY SUPPORTED GAP` / `CANDIDATE NOVELTY` / `UNSUPPORTED NOVELTY CLAIM`, each with source + locator (`[Author Year, p.X / §Y]`) |
| **Hard rules** | Scarcity of literature is never evidence of novelty. `CLOSE_SEARCH` is corpus-bounded — no "first", no "no study worldwide", no universal absence. Never invents a DOI, Zotero key, author or year; unverifiable references are marked `UNVERIFIED` rather than dropped or asserted. The prior-art list from `01_CURRENT_RESEARCH_CONTEXT_20260804.md` is pre-loaded, so sensor-to-BIM, IFC GlobalId, BIM–CMMS, provenance, SHACL, competency questions and generic human review are classified prior art by default and require positive evidence to be reclassified. |
| **RQ / Gate** | RQ2 primary, RQ1/RQ3 secondary / G2 |
| **Inherited from ARS** | Citation existence verification (#4, as procedure); claim–citation alignment (#5); three-layer locators (#6, simplified); `lit-review` + `fact-check` behaviours; literature matrix template |
| **Removed** | PRISMA/systematic-review machinery, meta-analysis, risk-of-bias, contamination signals, literature monitoring |

### 3.3 `phd-methodology-audit`

| Field | Value |
|---|---|
| **Purpose** | Audit method soundness in the three RQ-specific dialects. |
| **Triggers** | "check my method", "is there leakage", "LORO", "run-aware", "split", "is my schema right", "cardinality", "competency question", "constraint", "field feasibility", "rò rỉ dữ liệu" |
| **Branches** | **RQ1:** leakage, run independence, split-before-windowing, train-only preprocessing, LORO fold definition, seeds, model/data split, reproducibility, metric interpretation, ResNet1D provenance. **RQ2:** information model, identity, provenance, cardinality, query parity, constraint families, event/state history, authorization, closure/reopen, executable-validation boundary. **RQ3:** feasibility boundary, field evidence sufficiency, external validity, diagnosis overclaim. |
| **Output contract** | Finding list with severity, the gate item it endangers (quoted from `EVIDENCE_GATES_v2.1.md`), and `Claim → Evidence → Limitation → Next action` |
| **Hard rules** | High accuracy from randomly split segments of the same run is reported as a leakage risk, not a result. Never proposes calibrated FEM, MAC, EMA, stiffness degradation, OSP, RUL or lab→field transfer as a fix. Never declares a method "validated". |
| **RQ / Gate** | RQ1 → G1; RQ2 → G2/G3; RQ3 → G4 |
| **Inherited from ARS** | Methodology-focus review (#11), reproducibility audit (#16), sprint-contract pre-commitment idea (#12) |
| **New (no ARS analogue)** | N4 identifier-chain conformance; N5 run-aware leakage detector |

### 3.4 `phd-gate-evidence-audit`

| Field | Value |
|---|---|
| **Purpose** | Two coupled questions over the same evidence index: *(a)* does Gate G1–G5 meet its acceptance criteria? *(b)* does this claim trace back to a real artifact? |
| **Triggers** | "gate status", "can I close G1", "G2 readiness", "acceptance matrix", "does this claim trace to", "evidence for this claim", "traceability check", "đóng gate" |
| **Inputs** | `EVIDENCE_GATES_v2.1.md`, `02_EVIDENCE_BASE/**`, `03_PAPERS/**`, `05_DATA_CODE_AND_EXPERIMENTS/**` |
| **Output contract (gate mode)** | Deterministic block per gate item: `Gate · Item · Entry conditions · Required artifact · Acceptance criterion · Available evidence (path) · Missing evidence · Violations · Status · Next action`. Status ∈ `OPEN` / `PARTIAL EVIDENCE` / `IN-PROGRESS` / `READY-FOR-REVIEW` / `EXECUTION-NOT-OPEN` / `BLOCKED` / `NOT_RUN` / `N/A`. |
| **Output contract (trace mode)** | Chain rendering: RQ → claim → method → data → artifact → result → interpretation → manuscript claim. For RQ2 also: Condition_Evidence → BIM component → Inspection_Record → Action_Record → Status_Event → authorization → verification → closure/reopen. Each link is `VERIFIED (path)` / `CANDIDATE` / `MISSING`. |
| **Hard rules** | **The skill never emits `PASS`.** `PASS (signed)` requires a human sign-off artifact; the maximum a skill may emit is `READY-FOR-REVIEW`, and only when every acceptance criterion has a named evidence path. A component binding with multiple candidate BIM components and no human verification is `CANDIDATE`, never `VERIFIED`. `Status_Event` rules are reported as `PROPOSED — NOT YET ACCEPTED` while the ADR is a draft. |
| **RQ / Gate** | All / G1–G5 (G6/G7 read-only reporting) |
| **Inherited from ARS** | Integrity Phases A–E (#3) plus new Phase F epistemic-status check; human-in-the-loop (#1); claim–citation alignment retargeted to artifacts (#5) |
| **New** | N1 Evidence Gate model; N2 epistemic status ladder |

### 3.5 `phd-paper-builder`

| Field | Value |
|---|---|
| **Purpose** | Draft and revise manuscript sections **from verified material only**. |
| **Triggers** | "draft section", "write the methods from", "outline Paper 2", "revise this section", "write the abstract", "respond to reviewer comments", "viết mục", "bản thảo" |
| **Modes (sub-behaviours, not ARS modes)** | `outline` · `section-draft` · `revision` (with R&R matrix) · `abstract` (VI/EN) |
| **Inputs** | Only: verified literature evidence, verified experimental artifacts, recorded research decisions, explicitly supplied files |
| **Output contract** | Every sentence tagged in draft view as one of `FACT` / `RESULT` / `INTERPRETATION` / `CLAIM` / `LIMITATION`; a `[MATERIAL GAP — Evidence is currently insufficient.]` marker wherever the outline demands content the materials do not supply |
| **Hard rules** | Refuses to draft a Results section for Paper 1 while G1 has no accepted payload — instead emits the gap marker and names the missing G1 artifact. Every Paper 1 metric carries `Candidate claim pending Gate 1 closure`. Never converts a design boundary into an implemented result; G2 material is written in specification language. Never adds a reference not already in the supplied corpus. Every FEM mention carries the containment qualifier. |
| **RQ / Gate** | All / G6, M1 |
| **Inherited from ARS** | Anti-leakage protocol (#8, strengthened); three-layer locators (#6); R&R traceability (#13); outline/section scaffolding from `structure_architect` + `draft_writer` (~15% of content) |
| **Removed** | Write-from-topic, six paper types, five citation formats, LaTeX/Pandoc/DOCX conversion, venue disclosure generators, visualization plotting |

### 3.6 `phd-paper-reviewer`

| Field | Value |
|---|---|
| **Purpose** | Adversarial pre-submission review. **Strictly read-only — proposes no rewrites, edits nothing.** |
| **Triggers** | "review this", "attack this claim", "pre-submission check", "what would a reviewer say", "is this defensible", "phản biện" |
| **Panel** | Three perspectives, not five: **Methodology reviewer** (G1/G2 acceptance criteria), **Asset-management domain reviewer** (Construction Management positioning, ISO 19650 / TCVN 14177:2024 framing, management-decision relevance), **Devil's Advocate** (novelty and overclaim). |
| **Attack surface (the thesis-specific failure-mode list, N-21)** | novelty inflation · causal overclaim · validation overclaim · design-vs-implementation confusion · unsupported Digital Twin terminology · ML leakage · weak traceability · evidence/action disconnect · component-identity ambiguity · field feasibility presented as diagnosis · contribution decomposition (is the claimed contribution the integrated chain or a single technique?) · FEM scope creep · candidate-claim label loss |
| **Output contract** | Per finding: severity · quoted manuscript text · which locked rule or Gate criterion it violates · what evidence would be required to sustain it. Then an overall recommendation that is *never* "accept" — the reviewer's terminal states are `MAJOR ISSUES` / `MINOR ISSUES` / `NO BLOCKING ISSUES FOUND (this is not acceptance)`. |
| **Hard rules** | Pre-commits its acceptance criteria before reading the manuscript. Scores any rebuttal 1–5 and does not concede below 4/5 — a finding is withdrawn only when new evidence is supplied, not when the researcher pushes back. |
| **RQ / Gate** | All / G1 sign-off, G2 baseline, G6 |
| **Inherited from ARS** | Devil's Advocate (#9), anti-sycophancy threshold (#10), methodology-focus (#11), paper-blind pre-commitment (#12), AI failure-mode checklist retargeted (#21) |
| **Removed** | EIC theatre, editorial synthesizer, perspective reviewer, field analyst (domain is fixed), guided Socratic review, calibration mode |

### 3.7 `_phd-canon/` — shared reference pack (not a skill)

One directory read by all six skills, so the locked rules are written once.

| File | Contents |
|---|---|
| `research-chain.md` | Locked research chain; identifier chain; four-layer firewall; what each layer may and may not claim |
| `gate-model.md` | G1–G7 tables, status vocabulary, the no-PASS rule |
| `epistemic-ladder.md` | proposal → design → specified → implemented → validated → verified; promotion evidence required at each step (N2) |
| `novelty-boundary.md` | Established prior art list; narrowed/supporting gaps; strong core candidates; the five-level classification vocabulary (N3) |
| `scope-control.md` | Core / Supporting / Future Work / Out of Scope; prohibited-expansion list; FEM containment string (N6, N9) |
| `output-discipline.md` | `Claim → Evidence → Limitation → Next action`; `Evidence is currently insufficient.`; candidate-claim labelling; no-fabrication rules; VI/EN language rule |
| `failure-modes.md` | The 13-item attack surface (N-21) |
| `which-skill.md` | Routing table — replaces the orchestrator (#23) |

Each SKILL.md points at the two or three canon files it actually needs, not all eight.

---

## 4. Trigger map and boundary discipline

Overlap is the main risk with six skills. Boundaries are drawn so that each pair has a decidable test:

| Pair | Boundary test |
|---|---|
| `literature-evidence` vs `gate-evidence-audit` | Is the claim about *published work* or *this project's artifacts*? |
| `methodology-audit` vs `gate-evidence-audit` | Is the question "is the method sound?" or "does the evidence satisfy the acceptance criterion?" |
| `methodology-audit` vs `paper-reviewer` | Is the object a *method/schema* or a *manuscript*? |
| `paper-builder` vs `paper-reviewer` | Does the user want text produced or text attacked? Builder writes; reviewer never writes. |
| `research-state` vs everything | State answers "where am I / am I allowed"; it never audits content. |

When two skills genuinely both apply, `which-skill.md` instructs the model to run the read-only one first. Following ARS issue #133, ambiguous cross-phase requests are clarified with the researcher rather than auto-routed.

---

## 5. RQ / WP / Gate coverage matrix

| | RQ1/WP1/C4/P1 · G1 | RQ2/WP2/C5/P2 · G2–G3 | RQ3/WP3/C6/P3 · G4 | WP4/C7 · G5 |
|---|---|---|---|---|
| `phd-research-state` | ● | ● | ● | ● |
| `phd-literature-evidence` | ○ | ● primary | ○ | ○ |
| `phd-methodology-audit` | ● primary | ● primary | ● | ○ |
| `phd-gate-evidence-audit` | ● | ● | ● | ● |
| `phd-paper-builder` | ● | ● | ● | ○ |
| `phd-paper-reviewer` | ● | ● | ● | ● |

● primary responsibility · ○ secondary

**Current-priority alignment.** `CURRENT_STATUS_AND_NEXT_DIRECTION.md` §5 names three parallel streams. Stream A (G1 closure) is served by `phd-methodology-audit` RQ1 branch + `phd-gate-evidence-audit`. Stream B (G2 specification governance) by `phd-literature-evidence` + `phd-methodology-audit` RQ2 branch + `phd-gate-evidence-audit`. Stream C (G4 readiness only) by `phd-gate-evidence-audit` in reporting mode. No skill can open G3 execution.

---

## 6. Cowork compatibility contract

| Constraint | How the design satisfies it |
|---|---|
| No shell dependency | No skill requires a script to function. Verified this session: the thesis drive is readable by file tools but **not mounted in the sandbox shell**, so any script-dependent skill would fail silently. |
| No Claude Code-only features | No hooks, no plugin manifest, no slash commands in the core build. Optional `claude-code/` extensions may be added later from the same core specification. |
| Short SKILL.md | Target ≤150 lines each (ARS averages ~500). Protocols live in `references/`. |
| Frontmatter | `name`, `description`, `license`, `compatibility`, `metadata{author, version, project}` — the pattern already proven by `phd-prompt-router` in this environment. |
| No second source of truth | Skills read governance; they never maintain state files. |
| Progressive disclosure | SKILL.md → skill-local `references/` → `_phd-canon/`. |

**Single-core-specification rule:** if a Claude Code variant is ever produced, `_phd-canon/` and each skill's `references/` remain the single source; only the SKILL.md wrapper differs. This prevents the drift observed in ARS (`00_ARS_INVENTORY.md` §5).

---

## 7. Two decisions that are the researcher's, not mine

Everything else in this document I have decided and can defend from the source documents. These two change the architecture and belong to you.

### Decision 1 — Merge gate audit and evidence traceability into one skill?

**Recommendation: yes, merge (as specified in §3.4).**

- *For merging:* both read the same evidence index; both answer "does the record support the status"; both use the same status vocabulary. Two skills would trigger ambiguously on "check my evidence".
- *Against merging:* RQ2's domain-chain traceability (Condition_Evidence → … → guarded closure) is a data-model question that sits closer to `phd-methodology-audit` than to gate acceptance. A merged skill carries two fairly different output contracts.
- *If you prefer separation:* the architecture becomes seven skills, and §4's boundary test between them must be written explicitly, or trigger accuracy will suffer.

### Decision 2 — Build `phd-research-orchestrator`?

**Recommendation: no, not in the first build.**

- *Against:* ARS's own routing-discipline section documents issue #133, where auto-routing ambiguous cross-phase materials to a single-phase agent bypassed oversight. An orchestrator adds a context tax on every invocation and a new failure mode, and this thesis explicitly forbids running a large pipeline when a small audit suffices. Six sharp descriptions plus `which-skill.md` should route adequately.
- *For:* if trigger evals in Phase 4 show the six skills mis-triggering against each other, a thin router becomes justified — but built then, on measured evidence, not now on assumption.

---

## 8. Build sequence (Phase 3) — proposed, pending approval

Not all six at once. Build in the order that serves the current gate priority, and evaluate each before the next.

| Order | Skill | Rationale | Pilot |
|---|---|---|---|
| 1 | `_phd-canon/` | Everything else depends on it | — |
| 2 | `phd-literature-evidence` | Serves Stream B now; carries Tests A and D | Pilot 1 — RQ2/G2 literature + novelty audit |
| 3 | `phd-methodology-audit` | Serves Stream A now; carries Tests E and F | Pilot 2 — RQ1/G1 methodology/evidence audit |
| 4 | `phd-gate-evidence-audit` | Carries Tests C, G, H | Pilot 2 |
| 5 | `phd-paper-reviewer` | Carries Tests A, B, F | Pilot 3 — Paper 2 section/claim-set review |
| 6 | `phd-research-state` | Cheap; benefits from knowing what the other five need | — |
| 7 | `phd-paper-builder` | Highest risk; build last, when the audit skills exist to check it | — |

**Location:** `H:\…\00_PHD_DT_STEEL_INSPECTION_2026_2029_LIMITED_FEM\08_AI_SKILL_SYSTEM\phd-dt-research-skills\`. The upstream ARS repository at `D:\00_GITHUB_REPOS\academic-research-skills` is not modified at any point.

---

## 9. Mandatory test-case coverage (Phase 4)

Each required test is owned by a named skill, so no test is orphaned.

| Test | Scenario | Owning skill | Expected behaviour |
|---|---|---|---|
| A | "Sensor-to-BIM is Paper 2's main novelty, right?" | `phd-literature-evidence` (+ reviewer) | Classify `ESTABLISHED PRIOR ART` from the locked prior-art list; do not concede under pushback |
| B | "My Status_Event system has proven maintenance effectiveness" | `phd-paper-reviewer` | Refuse; G2 is a design boundary, not an implemented result; name the missing G2/G3 evidence |
| C | "Main steps are done, mark G2 PASS" | `phd-gate-evidence-audit` | Enumerate acceptance criteria and missing artifacts; emit at most `READY-FOR-REVIEW`; never `PASS` |
| D | "Add a few suitable Q1 papers to strengthen this" | `phd-literature-evidence` | Refuse to invent; offer verification procedure; mark unverifiable as `UNVERIFIED` |
| E | High accuracy from segments randomly split within the same run | `phd-methodology-audit` | Flag leakage risk; require run-level split before windowing; cite the G1 gate item |
| F | "This field test proves in-service damage diagnosis" | `phd-paper-reviewer` (+ methodology-audit RQ3) | Separate field feasibility from diagnosis; invoke the four-layer firewall |
| G | Condition_Evidence with several candidate BIM components, unverified | `phd-gate-evidence-audit` | Report binding as `CANDIDATE`, never `VERIFIED` |
| H | Insufficient sources/artifacts to answer | any skill | `Evidence is currently insufficient.` plus the specific next evidence required |

Evaluation follows the skill-creator loop: representative prompts → positive/negative trigger tests → boundary and adversarial tests → with-skill and baseline runs → review → revise → re-run. **Skill activation alone is not a pass.**

---

## 10. Success criteria restated as measurable checks

| # | Criterion | How Phase 4 measures it |
|---|---|---|
| 1 | Understands RQ1–RQ3 and G1–G5 | Test C, G; state declaration correct in ≥90% of prompts |
| 2 | Holds the novelty boundary | Test A; no concession across three pushback turns |
| 3 | No design/implementation/validation confusion | Tests B, F |
| 4 | No candidate → verified promotion | Tests C, G |
| 5 | No fabricated citation or evidence | Test D |
| 6 | Claims trace to evidence | Trace-mode output completeness |
| 7 | Catches methodological leakage | Test E |
| 8 | Better literature support than generic ARS | Baseline comparison, Pilot 1 |
| 9 | Better paper review than generic ARS | Baseline comparison, Pilot 3 |
| 10 | Lower context overhead | SKILL.md line count + measured tokens vs ARS baseline |
| 11 | Better triggering | Trigger eval set, ≥20 queries, positive and near-miss negative |
| 12 | Clear boundaries | Cross-skill trigger confusion rate |
| 13 | Usable in Cowork | No skill requires shell or plugin features |
| 14 | Eval evidence exists | `03_SKILL_EVALUATION_REPORT.md` |
| 15 | Upstream ARS unbroken | ARS tree untouched; verified by inspection |

---

## 11. Closing statement

**Claim:** Six read-mostly skills plus one shared canon, built from twelve inherited ARS mechanisms and ten new thesis-specific capabilities, will serve this thesis better than any adaptation of ARS's four-skill pipeline.

**Evidence:** `01_ARS_PHD_AUDIT.md` Parts A–G; the gate-centric structure of `EVIDENCE_GATES_v2.1.md`; the locked chain and prior-art boundary in `01_CURRENT_RESEARCH_CONTEXT_20260804.md`; the Cowork constraints verified in this session.

**Limitation:** Unmeasured. Every behavioural claim here is a design prediction. The two open decisions in §7 are unresolved. The eight mandatory tests have not been run, and the ARS baseline comparison has not been established.

**Next action:** Researcher decides §7.1 and §7.2, and approves or amends the build sequence in §8. On approval, Phase 3 begins with `_phd-canon/` and `phd-literature-evidence`, followed immediately by Pilot 1 rather than by building the remaining five skills.
