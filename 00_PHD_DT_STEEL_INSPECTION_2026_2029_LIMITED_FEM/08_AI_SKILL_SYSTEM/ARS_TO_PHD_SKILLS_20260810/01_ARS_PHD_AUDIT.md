# 01 — ARS → PhD SKILL AUDIT

**Version:** v1.0 | **Created:** 2026-08-10
**Status:** WORKING DOCUMENT — Phase 1 of ARS → PhD Digital Twin Research Skills migration
**Scope classification:** Supporting (research infrastructure)
**RQ → WP → Chapter/Paper → Gate:** Cross-cutting; advances no Gate. Serves G1 (Stream A), G2 (Stream B), G4 readiness (Stream C) indirectly by improving audit and drafting instruments.
**Inputs read:** `00_ARS_INVENTORY.md`; ARS v3.9.4 source tree; `MASTER_RESEARCH_CHARTER.md` + `MASTER_RESEARCH_CHARTER_v2.1_TRACEABILITY_CORE_20260719` (concise entry); `RESEARCH_DIRECTION_AND_SCOPE.md`; `RESEARCH_ARCHITECTURE.md`; `EVIDENCE_GATES_v2.1.md`; `AGENT_RULES.md`; `CLAUDE.md`; `CURRENT_STATUS_AND_NEXT_DIRECTION.md` (v2.2, 2026-08-04); `01_CURRENT_RESEARCH_CONTEXT_20260804.md`; `05_DOMAIN_PROFILE_PHD.md`; `02_EVIDENCE_BASE/RQ2_GATES2_3/00_README_START_HERE.md`; `phd-prompt-router/SKILL.md`.
**Nothing in ARS was modified. Nothing in the thesis repository was modified.**

---

## 1. Audit method

Every component is judged against the thesis as it is currently governed, not against generic academic practice. The governing facts used as the test set:

| Governing fact | Source |
|---|---|
| G1 = `OPEN — PARTIAL EVIDENCE`; no accepted Condition_Evidence payload, no signed acceptance matrix | `CURRENT_STATUS_AND_NEXT_DIRECTION.md` §1 |
| G2 = `OPEN — LITERATURE BOUNDARY CLOSED, SPECIFICATION NOT YET FROZEN` | ibid. |
| G3 = `OPEN — NOT IMPLEMENTED, NOT VALIDATED`; execution `EXECUTION-NOT-OPEN` until G2 baselined | ibid.; `EVIDENCE_GATES_v2.1.md` §G3 |
| `CLOSE_SEARCH` is corpus-bounded, is not universal absence, does not authorise a "first" claim, does not close G2 | `CURRENT_STATUS_AND_NEXT_DIRECTION.md` §3 |
| Established prior art: sensor-to-BIM, IFC GlobalId, BIM-linked inspection records, BIM–CMMS, provenance, SHACL, competency questions, generic human review | `01_CURRENT_RESEARCH_CONTEXT_20260804.md`; `AGENT_RULES.md` §5 |
| Novelty is the *integrated chain*, not any individual technique | `01_CURRENT_RESEARCH_CONTEXT_20260804.md` |
| Paper 1 metrics are `Candidate claim pending Gate 1 closure` | Charter §10; `AGENT_RULES.md` §4.1 |
| Mandatory reasoning structure: `Claim → Evidence → Limitation → Next action`; insufficiency phrase: `Evidence is currently insufficient.` | `CLAUDE.md`; `AGENT_RULES.md` §7 |
| FEM: nominal, uncalibrated, reference-only, not used for damage diagnosis; no FEM gate exists | Charter §9; `EVIDENCE_GATES_v2.1.md` |
| Prohibited self-expansion: calibrated FEM, MAC, EMA, stiffness degradation, RUL, predictive maintenance, field damage diagnosis, CFD, Smart City, Edge AI, weighted Health Index, commercial software, autonomous maintenance, lab→field classifier transfer, optimal sensor placement, ontology-engineering-as-contribution | `AGENT_RULES.md` §5 |
| Task declaration required: `RQ → WP → Chapter/Paper → Evidence Gate → Scope classification` | `AGENT_RULES.md` §2 |

**Decision vocabulary:** KEEP (usable near-verbatim) · ADAPT (valuable, must be specialised) · SPLIT · MERGE · REMOVE · NEW.

**Risk column:** the specific failure this component could cause *in this thesis* if inherited unchanged.

---

## 2. Executive verdict

**Claim:** ARS should be treated as a parts bin, not a chassis. Roughly one quarter of its named mechanisms are worth inheriting; none of its four skill shells is.

**Evidence:**
- ARS's central abstraction is the *manuscript*. This thesis's central abstraction is the *Evidence Gate*. ARS has no gate concept, no scope-classification concept, no distinction between design boundary and implemented result, and no notion of a locked identifier chain. `EVIDENCE_GATES_v2.1.md` defines seven gates with artifact-level acceptance criteria that ARS's `integrity_verification_agent` cannot express.
- ARS's four SKILL.md files total 1,999 lines and its agents 13,209 lines; 162 scripts and 291 tests are shell-bound and unreachable from Cowork (`00_ARS_INVENTORY.md` §4, §6).
- ARS's own routing discipline section documents issue #133, where auto-routing ambiguous cross-phase materials to a single-phase agent caused harm — direct evidence against building a PhD orchestrator first.
- Conversely, ARS's verification mechanisms (citation existence triangulation, claim–citation alignment with quote/page locators, anti-leakage, anti-sycophancy concession thresholds, paper-blind pre-commitment) target exactly the failure modes this thesis's `AGENT_RULES.md` §5–§6 prohibits.

**Limitation:** This audit is static. No ARS mode has been executed against thesis material, so all behavioural claims below are architectural inferences from file contents, not measured results. Trigger quality and hallucination resistance are asserted, not yet measured. Measurement is Phase 4.

**Next action:** Build the six-skill architecture in `02_PHD_SKILL_ARCHITECTURE.md`, then measure with skill-creator evals before adopting.

---

## 3. Part A — Skill-level verdicts

| Component | Current role | Decision | RQ relevance | Gate relevance | Risk if inherited unchanged | Recommendation |
|---|---|---|---|---|---|---|
| `deep-research` | 7-mode, 14-agent universal research engine | **SPLIT + REMOVE** | RQ2 (novelty boundary) high; RQ1/RQ3 low | G2 | Runs open-ended external discovery after `CLOSE_SEARCH` was declared; a `full` run would generate new "gaps" that reopen a bounded decision without governance | Extract `lit-review` + `fact-check` behaviour into `phd-literature-evidence`. Discard `full`, `quick`, `systematic-review`, `socratic`, `review` shells. |
| `academic-paper` | 10-mode, 12-agent writing pipeline | **SPLIT + ADAPT** | All three | G6 (Paper 2 submission), M1 | `full` mode writes a paper *from a topic*. Against a thesis where G1 has no accepted payload and G2 is not frozen, this is the single highest-risk component: it will manufacture Methods and Results prose to fill an outline | Keep only a narrowed builder that writes **from verified artifacts only**, with FACT/RESULT/INTERPRETATION/CLAIM/LIMITATION separation. Discard `full`-from-topic, `format-convert`, `disclosure`, `plan`, `lit-review`. |
| `academic-paper-reviewer` | 6-mode, 7-agent review panel | **ADAPT** | RQ1, RQ2, RQ3 | G1 sign-off, G2 baseline, G6 | 5 generic reviewers produce generic critique. None knows that "sensor-to-BIM" is prior art here, or that Status_Event is `PROPOSED — NOT YET ACCEPTED` | Highest-value inheritance. Rebuild as a 3-reviewer read-only panel with thesis-specific attack surface. |
| `academic-pipeline` | 10-stage orchestrator, 5 agents, 621-line SKILL.md | **REMOVE** | — | — | Runs research→write→review→revise as one authorised chain. This thesis forbids exactly that: G3 execution is `NOT OPEN`, evidence may not be borrowed across the four layers, and only the researcher may accept a Gate | Do not port. Its useful parts (`integrity_verification`, `claim_ref_alignment_audit`, state tracking) are extracted individually. |
| `shared/` | Contracts, schemas, protocols | **ADAPT (selective)** | All | All | Material Passport is a manuscript-lifecycle ledger; the thesis already has a superior domain state model in `00_GOVERNANCE` + `02_EVIDENCE_BASE` | Take the *pattern* (typed handoff + append-only ledger), not the schema. Governance files remain source of truth. |

---

## 4. Part B — Mode-level verdicts (25 modes)

### deep-research

| Mode | Decision | Reason |
|---|---|---|
| `full` | **REMOVE** | Produces a 3–8k word research report on a topic. Duplicates work already frozen in Round 1–3B immutable evidence. Risk: generates parallel, ungoverned findings. |
| `quick` | **REMOVE** | Same failure at smaller scale; no Gate consumes it. |
| `lit-review` | **ADAPT** | Becomes the literature-matrix + prior-art classification core of `phd-literature-evidence`. Must gain the five-level novelty vocabulary. |
| `fact-check` | **ADAPT** | Claim-by-claim verification is directly reusable; retarget from "is this claim true in the world" to "is this claim supported by an artifact in this repository". |
| `review` | **MERGE** | Overlaps `academic-paper-reviewer`. Collapse into the single PhD reviewer skill. |
| `socratic` | **ADAPT (reduced)** | Useful for G2 specification thinking (CQ Registry, Constraint Catalogue design). But `01_CURRENT_RESEARCH_CONTEXT` records `CLOSE_SEARCH` and a locked chain — Socratic RQ *exploration* is closed. Keep only as an optional dialogue posture inside `phd-research-state`, not a mode that can reopen RQ scope. |
| `systematic-review` | **REMOVE** | PRISMA machinery is disproportionate. `CLOSE_SEARCH` is corpus-bounded and explicitly not a systematic-review claim; running PRISMA would invite exactly the "universal absence" language `AGENT_RULES.md` §5 forbids. |

### academic-paper

| Mode | Decision | Reason |
|---|---|---|
| `full` | **ADAPT (heavily narrowed)** | Only survives as write-from-verified-artifacts. Must refuse to write Results sections when no accepted payload exists. |
| `plan` | **MERGE** | Fold into `phd-research-state` (which already must know RQ/WP/Gate) rather than a separate Socratic planning mode. |
| `outline-only` | **KEEP (as sub-behaviour)** | Cheap, low-risk, useful for Paper 2 structure. Becomes a mode of `phd-paper-builder`. |
| `revision` | **ADAPT** | Valuable for Paper 1 revision history (`PAPER1_GATE1_MAJOR_REVISION_LOG_v2.md` already exists). Must preserve the candidate-claim labelling on every touched metric. |
| `revision-coach` | **MERGE** | Roadmap-from-reviewer-comments folds into `phd-paper-builder` revision behaviour. |
| `abstract-only` | **ADAPT** | Needed (VI/EN bilingual is a real thesis requirement). Must inherit the candidate-claim label rule; an abstract is where overclaim concentrates. |
| `lit-review` | **MERGE** | Duplicate of deep-research `lit-review`. One owner only: `phd-literature-evidence`. |
| `format-convert` | **REMOVE** | Pandoc/LaTeX conversion is shell-bound and not a Cowork capability. Handle outside the skill system. |
| `citation-check` | **ADAPT** | Keep as a behaviour inside `phd-literature-evidence`, not a standalone mode. |
| `disclosure` | **REMOVE** | Venue-specific AI-disclosure generators for ICLR/NeurIPS/Nature/ACL are irrelevant to a Construction Management thesis. Write one short disclosure paragraph manually when needed. |

### academic-paper-reviewer

| Mode | Decision | Reason |
|---|---|---|
| `full` | **ADAPT** | Core of `phd-paper-reviewer`; reduce 5 reviewers → 3 (methodology, domain/asset-management, devil's advocate). |
| `methodology-focus` | **KEEP** | Directly serves G1 Stream A (leakage, LORO, provenance) and G2 Stream B (schema, CQ, constraint). |
| `re-review` | **ADAPT** | Needed for the Paper 1 revision loop; must check that prior candidate-claim labels survived revision. |
| `quick` | **KEEP** | Low-cost triage of a single section or claim set. Directly matches Pilot 3. |
| `guided` | **REMOVE** | Socratic review dialogue duplicates `methodology-focus` findings at higher token cost with no Gate output. |
| `calibration` | **REMOVE** | FNR/FPR measurement of a simulated reviewer requires a labelled ground-truth set that does not exist here. Would produce a precision figure with no evidential basis — the exact overclaim pattern `AGENT_RULES.md` §6 forbids. |

### academic-pipeline

| Mode | Decision | Reason |
|---|---|---|
| pipeline (10-stage) | **REMOVE** | See Part A. |
| `resume_from_passport` | **REMOVE** | Solves a context-window problem that the thesis repository already solves better: any session resumes by reading `01_CURRENT_CONTROL/CURRENT_STATUS_AND_NEXT_DIRECTION.md`. Adding a second state ledger creates two sources of truth. |

**Net:** 25 modes → 0 inherited as modes; ~9 inherited as behaviours inside 6 new skills.

---

## 5. Part C — Agent-level verdicts (39 agents)

Grouped; individual justification only where the verdict is non-obvious.

| Agents | Decision | Note |
|---|---|---|
| `integrity_verification_agent` (Phases A–E), `claim_ref_alignment_audit_agent`, `source_verification_agent`, `bibliography_agent` | **ADAPT — highest value** | These four carry the anti-hallucination substance. Retarget Phase A/B (reference existence, citation context) at the Zotero corpus and at `02_EVIDENCE_BASE`; retarget Phase E (claim verification) at Gate acceptance criteria. |
| `methodology_reviewer_agent`, `devils_advocate_reviewer_agent`, `domain_reviewer_agent` | **ADAPT** | Become the 3-reviewer PhD panel. DA's 8 challenges (cherry-picking, confirmation bias, logic chain, overgeneralisation, "so what?") map cleanly onto novelty-inflation attack. |
| `draft_writer_agent` (604 lines), `literature_strategist_agent` (526), `structure_architect_agent`, `argument_builder_agent`, `intake_agent` | **ADAPT (compress heavily)** | Useful writing scaffolding buried in mode-branching for six paper types and five citation formats the thesis will never use. Extract ~15% of the content. |
| `abstract_bilingual_agent` | **ADAPT** | Retarget zh-TW/EN → VI/EN. |
| `revision_coach_agent`, `peer_reviewer_agent`, `editorial_synthesizer_agent`, `eic_agent`, `perspective_reviewer_agent`, `field_analyst_agent` | **MERGE / REMOVE** | `field_analyst` auto-detects a domain — the domain is fixed and locked here. `eic` + `editorial_synthesizer` + `perspective_reviewer` add editorial theatre without new findings. Fold synthesis into a single decision section. |
| `socratic_mentor_agent` ×2 (549 + 497 lines) | **MERGE → reduced** | Two near-duplicate 500-line agents. At most one compressed dialogue protocol survives, inside `phd-research-state`. |
| `formatter_agent` (811 lines) | **REMOVE** | LaTeX/DOCX/Pandoc output. Shell-bound; not a Cowork capability. |
| `pipeline_orchestrator_agent` (804 lines), `state_tracker_agent` (518) | **REMOVE / ADAPT-pattern** | The orchestrator goes. From `state_tracker`, keep only the *idea* of a declared current state — implemented by reading governance files, not by maintaining a parallel ledger. |
| `meta_analysis_agent`, `risk_of_bias_agent`, `timeline_extraction_agent`, `monitoring_agent`, `ethics_review_agent`, `research_question_agent`, `research_architect_agent`, `report_compiler_agent`, `synthesis_agent`, `editor_in_chief_agent`, `devils_advocate_agent` (research-side) | **REMOVE** | Meta-analysis and risk-of-bias serve clinical/quantitative synthesis designs absent here. `research_question_agent` and `research_architect_agent` would propose RQs — RQ1–RQ3 are locked. `monitoring_agent` would reopen a `CLOSE_SEARCH` decision. Research-side DA duplicates review-side DA. |
| `visualization_agent`, `citation_compliance_agent` | **ADAPT (partial)** | Citation compliance survives as a checking behaviour. Visualization: keep the *anti-pattern list* (misleading axes, unsupported trend lines); drop the plotting machinery. |
| `collaboration_depth_agent`, `compliance_agent` (PRISMA-trAIce + RAISE + 8-role matrix) | **REMOVE** | Advisory scoring of human–AI collaboration depth, and PRISMA-trAIce compliance for systematic reviews. Neither maps to any of G1–G7. Pure context cost. |

**Net:** 39 agents → 0 ported as agents. Cowork has no agent-file loader in the ARS sense; their content becomes `references/` under six skills.

---

## 6. Part D — Mechanism inheritance ruling

The five questions required for each mechanism.

| # | Mechanism | Keep? | PhD problem it solves | Required change | Owner skill | Duplication risk |
|---|---|---|---|---|---|---|
| 1 | Human-in-the-loop mandatory checkpoints | **KEEP** | Only the researcher may accept a Gate (`AGENT_RULES.md` §9) | Reframe from "pipeline stage 2.5/4.5" to "no skill emits PASS; skills emit READY-FOR-REVIEW at most" | `phd-gate-evidence-audit` (enforces); all skills (respect) | None — it is a global rule, stated once in the shared canon |
| 2 | Material Passport (Schemas 1–13) | **DROP the schema, KEEP the pattern** | Typed handoff between skills; append-only history | Replace with the existing repository: `00_GOVERNANCE` + `01_CURRENT_CONTROL` + `02_EVIDENCE_BASE` are already the passport. Skills read it; skills do not maintain a second copy | `phd-research-state` (reads only) | **HIGH if ported** — would create a second source of truth against `SOURCE_OF_TRUTH_HIERARCHY_v2.1.md` |
| 3 | Integrity gates + Phase A–E verification | **KEEP** | Catches fabricated refs, mis-cited context, unsupported claims before a Gate submission | Add Phase F: *epistemic-status check* (proposal / design / implemented / validated / verified). ARS has no such phase and it is the thesis's dominant failure mode | `phd-gate-evidence-audit` | Overlaps #5; resolve by giving #3 the artifact scope and #5 the sentence scope |
| 4 | Citation existence verification (S2 / OpenAlex / Crossref) | **KEEP as protocol, DROP the scripts** | `AGENT_RULES.md` §6 forbids invented DOI/Zotero key | Scripts are shell-bound. In Cowork, express as a verification *procedure* using available web tools, with an explicit "unverified" state rather than a silent pass | `phd-literature-evidence` | None |
| 5 | Claim–citation alignment audit | **KEEP** | The thesis-critical question: does this source actually say this? | Retarget to include repository artifacts, not only published sources | `phd-literature-evidence` (source claims); `phd-gate-evidence-audit` (artifact claims) | Managed by the scope split above |
| 6 | Three-layer citation emission (`ref` + quote/page `anchor`) | **KEEP — strongly** | Makes every claim locatable; directly implements the thesis's own traceability ethic | Simplify the HTML-comment encoding to plain `[Source, p.X / §Y]` — the machine-readable form exists to feed ARS lint scripts that will not run in Cowork | `phd-literature-evidence`, `phd-paper-builder` | None |
| 7 | Contaminated-source advisory signals (4-tier) | **DROP** | Would flag post-2024 preprints as possible LLM-hallucinated citations | The corpus is Zotero-curated and deep-read by the researcher (Round 1–3B). The signal adds noise, not evidence | — | — |
| 8 | Anti-leakage protocol (knowledge isolation) | **KEEP — strongly** | The single most important inheritance for `phd-paper-builder`. Prevents writing a Methods section from parametric memory when no accepted payload exists | Strengthen: ARS's `[MATERIAL GAP]` flag becomes the mandatory `Evidence is currently insufficient.` phrase from `CLAUDE.md`. Extend activation to *all* modes, not just `full`/`revision` | `phd-paper-builder` (primary); shared canon (rule) | None |
| 9 | Devil's Advocate | **KEEP** | Test A (novelty inflation) and Test B (design-vs-result) require an agent willing to disagree | Load the thesis's own prior-art list as the DA's ammunition, so "sensor-to-BIM is novel" is refuted from `01_CURRENT_RESEARCH_CONTEXT` rather than from generic scepticism | `phd-paper-reviewer` | Drop the research-side duplicate |
| 10 | Anti-sycophancy / concession threshold (1–5, no concession below 4/5) | **KEEP — strongly** | Directly implements the required behaviour in Tests A–C: do not agree because the user pushed | Keep the scoring discipline; state the *why* rather than the numeric ritual | `phd-paper-reviewer` (primary); shared canon (rule for all skills) | None |
| 11 | Methodology-focus review | **KEEP** | G1's entire acceptance matrix is methodological (split-before-windowing, train-only preprocessing, LORO fold definition, seeds, uncertainty) | Replace generic checklists with the G1 and G2 gate-item tables verbatim from `EVIDENCE_GATES_v2.1.md` | `phd-methodology-audit` | Overlaps `phd-paper-reviewer`; resolve: audit skill checks the *method*, reviewer skill checks the *manuscript* |
| 12 | Sprint Contract / paper-blind pre-commitment | **KEEP the idea, DROP the schema** | Stops the reviewer from rationalising whatever the manuscript happens to say | Express as: state your acceptance criteria before reading the artifact. Schema 13.1 + 12 `allOf` branches + validator are unusable without `pytest` | `phd-paper-reviewer`, `phd-gate-evidence-audit` | None |
| 13 | R&R traceability matrix | **KEEP** | Paper 1 already has `PAPER1_GATE1_MAJOR_REVISION_LOG_v2.md`; matches existing practice | Align columns to the existing log format rather than importing ARS's | `phd-paper-builder` | None |
| 14 | Score trajectory (per-dimension deltas) | **DROP** | Tracks rubric improvement across review rounds | Invites a quantified quality claim with no evidential basis. The Gate acceptance matrix is the real trajectory | — | Would duplicate Gate status |
| 15 | Reviewer calibration (FNR/FPR) | **DROP** | See Part B | No labelled ground truth exists; output would be an unfounded precision figure | — | — |
| 16 | Reproducibility metadata / audit | **KEEP** | G1 requires dataset hash, run registry, commit hash, seeds, config register | Map ARS's fields onto the exact G1 artifact list (`DATASET_MANIFEST.csv`, `RUN_REGISTRY_LOCKED.csv`, `FILE_PROVENANCE_REGISTER.csv`, `SENSOR_METADATA_REGISTER.csv`, `MODEL_CONFIGURATION_REGISTER.csv`, `LORO_PROTOCOL_PREREGISTERED.md`, `RESNET1D_PROVENANCE_AUDIT.md`, `G1_ACCEPTANCE_MATRIX.md`) | `phd-methodology-audit` | None |
| 17 | `data_access_level` frontmatter (raw / redacted / verified_only) | **ADAPT** | Cleanly expresses "the reviewer must not see unverified material" | Reuse the concept as a per-skill declaration of which repository zones the skill may read and whether it may write | All skills (declared in frontmatter metadata) | None |
| 18 | Socratic mode + reading-check probe | **ADAPT (reduced)** | Useful for designing CQ Registry and Constraint Catalogue (G2 Stream B) | Must not reopen RQ scope; the chain is locked and `CLOSE_SEARCH` is declared | `phd-research-state` | Drop the second 500-line copy |
| 19 | Progressive disclosure (3-level loading) | **KEEP — structural** | Cowork context budget; six skills must coexist | Short SKILL.md (target ≤150 lines), everything else in `references/` | All skills | None |
| 20 | Context-rot protection / passport reset | **DROP mechanism, KEEP intent** | Long sessions lose state | Achieved by re-reading `CURRENT_STATUS_AND_NEXT_DIRECTION.md`, which is already the mandated session-start read | `phd-research-state` | Would duplicate #2 |
| 21 | AI research failure-mode checklist (7 modes) | **ADAPT** | ARS's "methodology fabrication" mode is exactly Test B's risk | Replace the 7 generic modes with ~8 thesis-specific ones (novelty inflation, design→result promotion, gate inflation, citation fabrication, ML leakage, field overclaim, identity-binding overclaim, FEM scope creep) | Shared canon; enforced by `phd-paper-reviewer` | None — becomes the reviewer's attack list |
| 22 | Collaboration depth observer | **DROP** | Scores delegation intensity and cognitive vigilance | No Gate consumes it; pure context cost | — | — |
| 23 | Routing discipline / intent clarification (#133) | **KEEP the lesson, DROP the layer** | Evidence *against* building an orchestrator | Instead of a routing skill, write sharp non-overlapping descriptions and one shared "which skill do I need" reference table | Shared canon | Building an orchestrator would itself be the duplication |
| 24 | PATTERN PROTECTION downstream hardening | **ADAPT (pattern only)** | Demonstrates that agents drift and need explicit anti-drift blocks | Adopt the technique (an explicit anti-drift block per skill), not ARS's 18 patterns (IRB anonymity, psychometric reverse-coding — irrelevant here) | All skills | None |

**Tally: 12 KEEP/KEEP-strongly · 5 ADAPT · 7 DROP.**

---

## 7. Part E — Infrastructure verdicts

| Component | Decision | Reason |
|---|---|---|
| 162 `scripts/` (lints, validators, API clients, migrations) | **REMOVE** | All require a shell + Python + filesystem. Cowork sessions in this project cannot reach `D:\` or the project drive through the sandbox shell — verified this session: the thesis folder is readable via file tools but not mounted in the bash sandbox. A skill that depends on them fails silently. |
| 291 `tests/` | **REMOVE from the shipped skill**; **ADAPT the discipline** | Keep the *practice* of eval cases (Phase 4 skill-creator evals), not the pytest suite. |
| `hooks/hooks.json` (SessionStart) | **REMOVE** | Claude Code plugin loader only. |
| 10 `/ars-*` slash commands | **ADAPT (optional, Claude Code only)** | May be added later as an optional Claude Code extension. Must not be a dependency of the Cowork build. |
| `.claude-plugin/` marketplace + plugin manifest | **NEW (later)** | If the six skills are ever packaged as a plugin, write a fresh manifest. Do not copy ARS's. |
| Frontmatter convention | **ADAPT from local precedent, not from ARS** | `phd-prompt-router/SKILL.md` already runs in this environment using `name`, `description`, `license`, `compatibility`, `metadata{author, version, project}`. That is a validated pattern for this user; adopt it rather than ARS's `data_access_level`/`task_type` fields, which exist to feed lint scripts. |

---

## 8. Part F — NEW: capabilities the thesis needs that ARS has no equivalent for

| # | Capability | Why ARS cannot supply it | Owner |
|---|---|---|---|
| N1 | **Evidence Gate model** — entry conditions, required artifact, acceptance criterion, evidence path, owner, sign-off, status ∈ {OPEN, PARTIAL EVIDENCE, IN-PROGRESS, READY-FOR-REVIEW, EXECUTION-NOT-OPEN, PASS(signed), N/A} | ARS's integrity verdict vocabulary is PASS/FAIL on a manuscript. It cannot express `EXECUTION-NOT-OPEN` or a Gate with 15 artifact rows | `phd-gate-evidence-audit` |
| N2 | **Epistemic status ladder** — proposal → design → specified → implemented → validated → verified, with promotion forbidden without evidence | Nothing in ARS distinguishes a design boundary from a result. This is the direct cause of Test B failure | Shared canon; enforced everywhere |
| N3 | **Five-level novelty vocabulary** — ESTABLISHED PRIOR ART / SUPPORTED GAP / PARTIALLY SUPPORTED GAP / CANDIDATE NOVELTY / UNSUPPORTED NOVELTY CLAIM, seeded with the thesis's own prior-art list | ARS produces "research gaps" as a free-text section with no epistemic grading and no memory of what was already ruled prior art | `phd-literature-evidence` |
| N4 | **Identifier-chain conformance check** — `Sensor_ID → BIM_GUID / Asset_ID @ Model_Version_ID → Condition_Evidence_ID → Inspection_Record_ID → Action_Record_ID`; `Action_Status`/`Workflow_Status` is a projection, never an identifier; `Status_Event_ID` is `PROPOSED`; no gratuitous `Component_ID` | Entirely thesis-specific | `phd-methodology-audit` (RQ2 branch) |
| N5 | **Run-aware leakage detector** — split-before-windowing, train-only preprocessing, LORO fold definition, seed logging, per-fold uncertainty | ARS's methodology reviewer has generic statistical checklists, no notion of run-level grouping | `phd-methodology-audit` (RQ1 branch) |
| N6 | **Scope-creep classifier** — Core / Supporting / Future Work / Out of Scope, with the prohibited-expansion list as a hard stop | ARS has no scope model; it treats scope expansion as intellectual ambition | Shared canon; enforced by every skill's opening declaration |
| N7 | **Candidate-claim labelling** — every Paper 1 metric carries `Candidate claim pending Gate 1 closure` until G1 is signed | Charter §10 requirement with no ARS analogue | `phd-paper-builder`, `phd-paper-reviewer` |
| N8 | **Field feasibility vs field diagnosis firewall** | ARS has no layered-evidence firewall; it would let Layer 3 evidence support a Layer 1 claim | Shared canon; `phd-paper-reviewer` |
| N9 | **FEM containment** — every FEM mention carries "nominal, uncalibrated, reference-only, not used for damage diagnosis"; no FEM gate exists | Thesis-specific | Shared canon |
| N10 | **Bilingual VI/EN operation** | ARS is EN + zh-TW | All skills |

---

## 9. Part G — Risk register for the new suite

| Risk | Mechanism that mitigates it | Residual |
|---|---|---|
| A skill writes a Results section that does not exist | Anti-leakage (#8) + N2 epistemic ladder + `phd-paper-builder` refusing to draft Results without an accepted payload | Requires eval coverage (Test B) |
| A skill agrees that sensor-to-BIM is novel | Anti-sycophancy (#10) + N3 seeded prior-art list + DA (#9) | Requires eval coverage (Test A) |
| A skill marks G2 PASS | #1 human-in-the-loop + N1 Gate model; no skill may emit PASS | Low if the rule is stated in every SKILL.md, not only in a reference |
| A skill invents a supporting citation | #4 existence verification + #5 alignment + #6 locators + `AGENT_RULES.md` §6 | Verification in Cowork is procedural, not scripted — weaker than ARS's CI. Must be stated as a limitation, not hidden |
| Six skills overlap and trigger wrongly | Sharp descriptions + one routing reference (#23); no orchestrator | Requires trigger evals (skill-creator description optimisation) |
| Context overhead exceeds ARS's | Progressive disclosure (#19); target ≤150-line SKILL.md vs ARS's ~500 | Measurable in Phase 4 |
| The skill suite becomes a second source of truth | #2 — governance files remain authoritative; skills read, never mirror | Must be enforced by a written prohibition on skill-side state files |

---

## 10. Summary of counts

| Level | Inspected | KEEP | ADAPT | SPLIT | MERGE | REMOVE | NEW |
|---|---|---|---|---|---|---|---|
| Skills | 5 (incl. `shared`) | 0 | 2 | 2 | 0 | 1 | 6 proposed |
| Modes | 25 | 3 | 9 | — | 5 | 8 | — |
| Agents | 39 | 0 | ~14 | — | ~6 | ~19 | — |
| Mechanisms | 24 | 12 | 5 | — | — | 7 | 10 new (N1–N10) |
| Infrastructure | 5 classes | 0 | 2 | — | — | 3 | 1 |

---

## 11. Closing statement

**Claim:** The PhD suite should be six skills, built from twelve inherited ARS mechanisms plus ten new thesis-specific capabilities, with no orchestrator, no Material Passport, and no ported agent files.

**Evidence:** Part A–G above, derived from direct inspection of 746 ARS files and eleven governing thesis documents dated 2026-07-17 to 2026-08-04.

**Limitation:** Nothing here has been executed. Trigger accuracy, hallucination resistance, scope discipline and context cost are all *predicted*. Two judgments in particular are contestable and are flagged for the researcher rather than settled here: (i) merging gate audit with evidence traceability into one skill; (ii) not building an orchestrator at all. Both are argued in `02_PHD_SKILL_ARCHITECTURE.md` §7.

**Next action:** Researcher review of `02_PHD_SKILL_ARCHITECTURE.md`. No skill is built until that architecture is approved.

---

## 12. Verification pass (2026-08-10)

Checks run against this document and `02_PHD_SKILL_ARCHITECTURE.md` after drafting.

| Check | Result |
|---|---|
| Upstream ARS content unmodified | **Confirmed.** `git status` in the ARS checkout reports 723 files as modified, but `git diff` shows 127,081 insertions against 127,081 deletions — a whole-file CRLF/LF line-ending artifact of reading a Windows checkout through a Linux mount, not content change. `git diff MODE_REGISTRY.md` shows identical text on both sides. This dirty state predates this session; no write operation was issued against `D:\00_GITHUB_REPOS\academic-research-skills`. |
| Thesis repository unmodified | **Confirmed.** Only three new files created, all under a new directory `08_AI_SKILL_SYSTEM/ARS_TO_PHD_SKILLS_20260810/`. No governance, evidence-base or paper file was read-modified. |
| Gate statuses quoted correctly | **Confirmed** against `CURRENT_STATUS_AND_NEXT_DIRECTION.md` v2.2 §1 and `EVIDENCE_GATES_v2.1.md` §G1–G3. |
| Prior-art list quoted correctly | **Confirmed** against `01_CURRENT_RESEARCH_CONTEXT_20260804.md` §"Established prior art" and `AGENT_RULES.md` §5. |
| Referenced repository paths exist | **Confirmed** for `00_GOVERNANCE/SOURCE_OF_TRUTH_HIERARCHY_v2.1.md`, `01_CURRENT_CONTROL/CURRENT_DIRECTION_LOCK_20260804.md`, `02_EVIDENCE_BASE/CURRENT/00_MASTER_INDEX_CURRENT_20260804.md`, `02_EVIDENCE_BASE/RQ2_GATES2_3/` Rounds 1–4, `06_LITERATURE_AND_ZOTERO/`, `05_DATA_CODE_AND_EXPERIMENTS/`. |
| ARS file counts | **Confirmed** by direct `find` counts, recorded in `00_ARS_INVENTORY.md` §2–§5. |
| ARS behavioural claims | **Not verified.** No ARS mode was executed. All statements about how ARS *behaves* are inferences from file contents. Stated as a limitation in §2 and §11. |

**One correction arising from verification.** `05_DATA_CODE_AND_EXPERIMENTS/` is not an empty placeholder. It already contains `CANONICAL_THREE_CAMPAIGN_DATASET/` (README, channel quality rules, data dictionary, dataset variants, validation report, reproducibility manifest, automated validation results) and `THREE_CAMPAIGN_REANALYSIS/` (executive report, environment provenance, data-quality and provenance log, within-campaign LORO results, cross-campaign results, baseline model comparison, permutation results, sensor configuration results, sensitivity results, confusion matrices, training curves).

This does not change any verdict, and it does not change G1's status — `CURRENT_STATUS_AND_NEXT_DIRECTION.md` §1 already records that "supporting dataset/reanalysis documentation exists, but no accepted Condition_Evidence payload or signed G1 acceptance matrix exists." It does mean `phd-methodology-audit` (RQ1 branch) has substantial real input available for Pilot 2 from the first day, and that its reference list must include these paths.
