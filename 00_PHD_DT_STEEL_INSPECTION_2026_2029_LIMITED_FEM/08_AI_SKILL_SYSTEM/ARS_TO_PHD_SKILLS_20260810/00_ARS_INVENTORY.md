# 00 — ARS INVENTORY (UPSTREAM REFERENCE IMPLEMENTATION)

**Version:** v1.0 | **Created:** 2026-08-10
**Status:** WORKING DOCUMENT — Phase 0 of ARS → PhD Digital Twin Research Skills migration
**Scope classification:** Supporting (research infrastructure, not thesis evidence)
**RQ → WP → Chapter/Paper → Gate:** Cross-cutting infrastructure; no RQ ownership; no Gate is advanced by this document.
**Source inspected:** `D:\00_GITHUB_REPOS\academic-research-skills` (read-only; nothing modified)
**Upstream identity:** `academic-research-skills` v3.9.4, author Cheng-I Wu, CC-BY-NC-4.0, last updated 2026-05-18

---

## 1. Purpose of this document

Enumerate what actually exists in ARS, by direct file inspection, so that the Phase 1 audit classifies **observed components**, not remembered ones. No component is judged here.

---

## 2. Top-level structure

| Directory | Files | Role |
|---|---|---|
| `deep-research/` | 50 | Upstream research engine skill |
| `academic-paper/` | 55 | Paper writing skill |
| `academic-paper-reviewer/` | 25 | Multi-perspective review skill |
| `academic-pipeline/` | 30 | Orchestrator skill |
| `shared/` | 43 | Cross-skill protocols, schemas, contracts |
| `scripts/` | 162 | Python/bash lints, validators, API clients, adapters |
| `tests/` | 291 | Pytest suite + fixtures |
| `docs/` | 39 | Design specs, performance docs, changelogs |
| `commands/` | 10 | `/ars-*` slash commands (Claude Code plugin) |
| `agents/` | 3 | Plugin-level relative symlinks to `deep-research/agents/` |
| `hooks/` | 1 | `hooks.json` — SessionStart announce hook |
| `.claude-plugin/` | 2 | `plugin.json`, `marketplace.json` |
| `skills/` | 4 | Symlink dir to the four skill directories |
| Root docs | 11 | README (70 KB), README.zh-TW (66 KB), CHANGELOG (133 KB), MODE_REGISTRY, POSITIONING, QUICKSTART, CONTRIBUTING, LICENSE, NOTICE, SECURITY, requirements-dev |

**Total inspected files (excluding `.git`): 746.**

---

## 3. Skills and modes

Source of truth for modes: `MODE_REGISTRY.md` — declares **25 modes across 4 skills**.

### 3.1 `deep-research` (v2.9.4) — 7 modes

| Mode | Output | Oversight |
|---|---|---|
| `full` | APA 7.0 report, 3,000–8,000 words | High |
| `quick` | Research brief, 500–1,500 words | Medium |
| `review` | Reviewer report on provided text | High |
| `lit-review` | Annotated bibliography + synthesis | Medium |
| `fact-check` | Claim-by-claim verification report | Medium |
| `socratic` | Research Plan Summary + INSIGHT collection | Very High |
| `systematic-review` | PRISMA 2020 report, 5,000–15,000 words | Medium |

**Agents (14 files):** `bibliography`, `devils_advocate`, `editor_in_chief`, `ethics_review`, `meta_analysis`, `monitoring`, `report_compiler`, `research_architect`, `research_question`, `risk_of_bias`, `socratic_mentor`, `source_verification`, `synthesis`, `timeline_extraction`.

**References (22):** APA7 style, argumentation/reasoning framework, cross-agent quality definitions, Crossref API protocol, EQUATOR reporting guidelines, ethics checklist, failure paths, interdisciplinary bridges, IRB decision tree, literature monitoring strategies, logical fallacies, methodology patterns, mode selection guide, OpenAlex API protocol, preregistration guide, Semantic Scholar API protocol, Socratic mode protocol, Socratic questioning framework, source quality hierarchy, systematic review protocol, systematic review toolkit, changelog.

**Templates (6):** evidence assessment, literature matrix, preregistration, PRISMA protocol, PRISMA report, research brief.

### 3.2 `academic-paper` (v3.1.2) — 10 modes

`full`, `plan`, `outline-only`, `revision`, `revision-coach`, `abstract-only`, `lit-review`, `format-convert`, `citation-check`, `disclosure`.

**Agents (12):** `abstract_bilingual`, `argument_builder`, `citation_compliance`, `draft_writer`, `formatter`, `intake`, `literature_strategist`, `peer_reviewer`, `revision_coach`, `socratic_mentor`, `structure_architect`, `visualization`.

**References (25):** abstract writing guide, academic writing style, **anti-leakage protocol**, APA7 Chinese citation guide, APA7 extended guide, citation format switcher, CRediT authorship guide, disclosure mode protocol, failure paths, funding statement guide, HEI domain glossary, journal submission guide, LaTeX template reference, mode selection guide, paper structure patterns, plan mode protocol, policy anchor disclosure protocol, policy anchor table, statistical visualization standards, venue disclosure policies, VLM figure verification, workflow phase details, writing judgment framework, writing quality check, changelog.

**Templates (11):** bilingual abstract, case study, conference paper, CRediT statement, funding statement, IMRaD, LaTeX article (`.tex`), literature review, policy brief, revision tracking, theoretical paper.

### 3.3 `academic-paper-reviewer` (v1.9.1) — 6 modes

`full`, `re-review`, `quick`, `methodology-focus`, `guided`, `calibration`.

**Agents (7):** `devils_advocate_reviewer`, `domain_reviewer`, `editorial_synthesizer`, `eic`, `field_analyst`, `methodology_reviewer`, `perspective_reviewer`.

**References (12):** calibration mode protocol, editorial decision standards, guided mode protocol, integration guide, quality rubrics, re-review mode protocol, review criteria framework, review quality thinking, **sprint contract protocol**, statistical reporting standards, top journals by field, changelog.

**Templates (3):** editorial decision, peer review report, revision response.

### 3.4 `academic-pipeline` (v3.9.4) — orchestrator + `resume_from_passport=<hash>`

**Agents (5):** `claim_ref_alignment_audit`, `collaboration_depth`, `integrity_verification`, `pipeline_orchestrator`, `state_tracker`.

**References (20):** adapters overview, AI research failure modes, claim audit calibration protocol, claim verification protocol, external review protocol, integrity review protocol, literature corpus consumers, mode advisor, **passport as reset boundary**, pipeline state machine, plagiarism detection protocol, process summary protocol, progress dashboard template, reinforcement content, reproducibility audit, score trajectory protocol, team collaboration protocol, two-stage review protocol, changelog.

**Templates (1):** pipeline status.

### 3.5 `shared/` (43 files)

**Agent (1):** `compliance_agent` (PRISMA-trAIce 17 items + RAISE 4 principles + 8-role matrix).

**Protocol / pattern docs (14 at top level):** artifact reproducibility pattern, benchmark report pattern + schema, collaboration depth rubric, compliance checkpoint protocol + schema, cross-model verification, ground truth isolation pattern, **handoff schemas** (Material Passport, Schemas 1–13), mode spectrum, PRISMA-trAIce protocol, RAISE framework, sprint contract schema, style calibration protocol.

**Contracts (21 JSON/MD):**
- `contracts/passport/` — `literature_corpus_entry`, `citation_provenance`, `claim_audit_result`, `claim_drift`, `claim_intent_manifest`, `constraint_violation`, `audit_artifact_entry`, `rejection_log`, `reset_ledger_entry`, `temporal_audit_results`, `timeline`, `uncited_assertion`, `uncited_audit_failure`
- `contracts/audit/` — `audit_jsonl`, `audit_sidecar`, `audit_verdict`
- `contracts/reviewer/` — `full.json`, `methodology_focus.json`
- `contracts/writer/full.json`, `contracts/evaluator/full.json`

**References (5):** intent clarification protocol, IRB terminology glossary, protected hedging phrases, psychometric terminology glossary, word count conventions.

**Templates (1):** codex audit multifile template.

---

## 4. Scripts, hooks, tests (Claude Code-only infrastructure)

- **162 files in `scripts/`** — version lints (`check_v3_6_7_*`, `check_v3_7_3_*`, `check_v3_9_0_*`, `check_v3_9_2_*`, `check_v3_9_4_*`), schema validators, `semantic_scholar_client.py`, `crossref_client.py`, `openalex_client.py`, `contamination_signals.py`, claim-audit pipeline/finalizer/calibration, migration scripts, three reference corpus adapters (`folder_scan`, `zotero`, `obsidian`), `run_codex_audit.sh`, `announce-ars-loaded.sh`.
- **291 files in `tests/`** — pytest suite; upstream reports 967 pass / 3 skipped at v3.7.3 convergence.
- **`hooks/hooks.json`** — one `SessionStart` hook running `announce-ars-loaded.sh`.
- **`commands/`** — 10 `/ars-*` slash commands with model routing pinned in frontmatter (`opus` for `full` and `revision-coach`, `sonnet` for the other eight).
- **CI:** `.github/workflows/spec-consistency.yml` + `pytest.yml`.

**Every item in this section depends on a filesystem, a shell, `pytest`, and the Claude Code plugin loader. None of it is reachable from a Claude Cowork session as-is.**

---

## 5. Agent census and observed count drift

| Skill | Agent files observed |
|---|---|
| deep-research | 14 |
| academic-paper | 12 |
| academic-paper-reviewer | 7 |
| academic-pipeline | 5 |
| shared | 1 |
| **Total** | **39** |

Discrepancies observed between declarations and files:

| Declaration | Location | Observed |
|---|---|---|
| "13-agent pipeline" | `deep-research/SKILL.md` description | 14 agent files |
| "12-agent" | `academic-paper` description | 12 agent files (consistent) |
| "38-agent ensemble" | `.claude-plugin/plugin.json` | 39 agent files |
| "35+ modes" | `.claude-plugin/plugin.json` | 25 modes in `MODE_REGISTRY.md` |

**Claim → Evidence → Limitation → Next action**
- **Claim:** ARS's own component counts drift between its manifest, its skill descriptions, and its files.
- **Evidence:** file counts above vs. `plugin.json` and SKILL.md frontmatter, inspected 2026-08-10.
- **Limitation:** drift of ±1 agent and a mode-counting convention difference is cosmetic and does not by itself indicate defective behaviour; "35+ modes" may count sub-modes not registered in `MODE_REGISTRY.md`.
- **Next action:** treat this as a reason to inherit ARS *mechanisms by inspection*, not ARS *claims by citation*. Do not carry any ARS self-description into PhD skill documentation without re-verifying it against files.

---

## 6. Context cost (why this matters for Cowork)

| Artifact | Lines | Words |
|---|---|---|
| `deep-research/SKILL.md` | 506 | 3,483 |
| `academic-paper/SKILL.md` | 449 | 4,517 |
| `academic-paper-reviewer/SKILL.md` | 423 | 3,131 |
| `academic-pipeline/SKILL.md` | 621 | 5,028 |
| All 39 agent files | 13,209 | — |

Largest single agents: `formatter_agent` (811 lines), `pipeline_orchestrator_agent` (804), `draft_writer_agent` (604), `peer_reviewer_agent` (596), `socratic_mentor_agent` (549).

Skill-creator guidance targets **SKILL.md under ~500 lines**. Three of four ARS SKILL.md files are at or over that line; the orchestrator exceeds it by 25%. A single `academic-pipeline` invocation that loads the orchestrator agent alone puts ~1,400 lines of instruction into context before any thesis material is read.

---

## 7. Upstream mechanisms catalogued for Phase 1 evaluation

Named here so Phase 1 can rule on each one individually rather than on "ARS" as a block:

1. Human-in-the-loop checkpoints (Stage 2.5 / 4.5 MANDATORY integrity gates)
2. Material Passport (`shared/handoff_schemas.md`, Schemas 1–13)
3. Integrity gates + `integrity_verification_agent` (Phases A–E)
4. Citation existence verification (Semantic Scholar / OpenAlex / Crossref triangulation, v3.9.0)
5. Claim–citation alignment (`claim_ref_alignment_audit_agent`)
6. Three-layer citation emission — `<!--ref:slug-->` + `<!--anchor:kind:value-->` locators (v3.7.3)
7. Contaminated-source advisory signals (v3.9.0 4-tier matrix)
8. Anti-leakage protocol (knowledge isolation, v3.3)
9. Devil's Advocate agents (research-side and review-side)
10. Anti-sycophancy / concession threshold (rebuttals scored 1–5; no concession below 4/5)
11. Methodology-focus review mode + `methodology_reviewer_agent`
12. Sprint Contract hard gate (Schema 13.1; paper-blind Phase 1 → paper-visible Phase 2)
13. R&R traceability matrix / revision tracking template
14. Score trajectory protocol (per-dimension rubric deltas across rounds)
15. Reviewer calibration mode (FNR/FPR/balanced accuracy)
16. Reproducibility metadata + `reproducibility_audit.md`
17. Data access metadata (`data_access_level` frontmatter: raw / redacted / verified_only)
18. Socratic research mode + reading-check probe (v3.5.1)
19. Progressive disclosure (three-level loading)
20. Context-rot protection (passport reset boundary, `ARS_PASSPORT_RESET=1`)
21. AI research failure modes checklist (7 modes, Lu 2026)
22. Collaboration depth observer (advisory, never blocks)
23. Routing discipline / intent clarification protocol (v3.9.2, issue #133)
24. PATTERN PROTECTION downstream-agent hardening (v3.6.7, 18 documented patterns)

---

## 8. Closing statement

**Claim:** ARS is a large, actively-maintained, Claude-Code-oriented research suite whose value is concentrated in ~24 named verification mechanisms rather than in its four skill shells.

**Evidence:** 746 files inspected; 25 registered modes; 39 agents; 162 scripts and 291 tests that are all shell/filesystem-bound; four SKILL.md files averaging 500 lines.

**Limitation:** This inventory records structure and size. It does not measure whether any mechanism actually works, and it has not been executed. Behavioural quality is unmeasured at this point.

**Next action:** Phase 1 audit — classify each component KEEP / ADAPT / SPLIT / MERGE / REMOVE / NEW against RQ1–RQ3, G1–G5 and Cowork constraints. See `01_ARS_PHD_AUDIT.md`.
