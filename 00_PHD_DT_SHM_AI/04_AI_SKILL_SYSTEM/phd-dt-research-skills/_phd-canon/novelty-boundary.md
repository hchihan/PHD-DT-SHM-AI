# Canon — Novelty Boundary and Prior-Art Classification

> **Đồng bộ 01/10/2026 — Tiểu luận tổng quan.** Với mọi việc thuộc Tiểu luận tổng quan (`01_LITERATURE_REVIEW/03_OUTPUTS/01_TIEU_LUAN_TONG_QUAN/`), `CLAUDE.md` của tiểu luận và `_phd-canon/project-canon-tltq.md` thắng tệp này. Khác biệt chính: mô hình dữ liệu là schema đồ thị (CLAUDE.md mục 8), `STATUS_EVENT` và `AGENT` là thực thể bắt buộc, chuỗi định danh tuyến tính chỉ để trình bày (Phụ lục A); hai trục `priority_level` / `Action_Status` tách riêng; K1–K3 là giả thuyết làm việc, chốt ở ĐD3; ứng viên khoảng trống phải qua quy tắc phản chứng (CLAUDE.md mục 7.4). Ngoài tiểu luận, tệp này giữ nguyên hiệu lực.


**v1.0 · 2026-08-10 · new capability (N3).**
Derived from `01_CURRENT_RESEARCH_CONTEXT_20260804.md`, `AGENT_RULES.md` §5, `CURRENT_STATUS_AND_NEXT_DIRECTION.md` §3, `02_EVIDENCE_BASE/RQ2_GATES2_3/` Rounds 1–4.

---

## Why this exists

Novelty inflation is the failure that ends vivas. It happens gently: a technique the corpus already contains gets described as "novel", usually because the researcher has been working on it for months and the literature memory has faded. The corpus-bounded deep read (Rounds 1–3B, closed as `CLOSE_SEARCH`) already settled most of these questions. This file holds that settlement so it does not have to be relitigated, and so an assistant cannot cheerfully agree that something is novel because the researcher sounded confident.

---

## Classification vocabulary

Every novelty-relevant statement gets exactly one label:

| Label | Meaning | Evidence needed |
|---|---|---|
| **ESTABLISHED PRIOR ART** | The corpus already contains this | ≥1 source in the reviewed corpus, cited with locator |
| **SUPPORTED GAP** | The corpus shows this is missing or unresolved, and the absence is documented | Explicit statement in ≥1 reviewed source, or a documented systematic absence across the screened corpus with the corpus bound stated |
| **PARTIALLY SUPPORTED GAP** | Partially addressed; the remaining part is narrow | Sources showing partial coverage + a precise statement of the residue |
| **CANDIDATE NOVELTY** | Plausibly new *within the reviewed corpus*, pending G2/G3 validation and expert review | Corpus-bounded argument + explicit statement that it is corpus-bounded and unvalidated |
| **UNSUPPORTED NOVELTY CLAIM** | Asserted as new without evidence | — (this is the finding) |

**Scarcity is not novelty.** "Few studies address X" is not evidence that X is a contribution. It may mean X is uninteresting, X is solved elsewhere under another name, or the search was too narrow. A gap claim needs a source that says the gap exists, or a documented absence with the corpus bound named.

---

## Established prior art — classify as PRIOR ART by default

These require positive evidence to be reclassified as anything else:

- sensor-to-BIM linking
- IFC GlobalId as a persistent component identifier
- BIM-linked inspection records
- BIM–CMMS integration
- action information modelling
- competency questions as a validation device
- provenance modelling
- SHACL / SPARQL / MVD / IDS / database constraint validation
- generic valid/invalid fixtures
- direct and inverse navigation
- generic human-in-the-loop review
- viewers, dashboards, websites
- ontology engineering as such

## Narrowed or supporting gaps

Real but not sufficient alone to carry the contribution:

- stable `Inspection_Record`–`Action_Record` relation
- evidence-basis preservation
- chain-specific integrity mutations
- paired forward/reverse queries
- query-answer parity
- declared transformation equivalence and permitted loss

## Strong core candidates

- immutable, queryable maintenance `Status_Event` history
- accountable approval / rejection / rework
- actor-bound authorization
- formal post-action verification
- guarded closure and reopen
- **the complete identity-governed evidence-to-action record–event chain**

---

## The decomposition rule

**The defensible unit of contribution is the integrated chain. Individual techniques are not.**

When a novelty claim is made, decompose it and ask which level it lives at:

1. *Is the technique new?* Almost always no — see the prior-art list.
2. *Is the combination new?* Possibly, within the reviewed corpus.
3. *Is the combination new **and** does it do work that the parts cannot do separately?* This is what has to be argued, and it is the only claim that survives a competent reviewer.

A contribution statement that survives looks like: "Within the reviewed corpus, no single model carries identity governance, append-only event history, actor-bound authorization, post-action verification and guarded closure as one validated chain; each element individually is established prior art."

---

## `CLOSE_SEARCH` — what it does and does not license

`CLOSE_SEARCH` was declared on the basis of the screened and deep-read corpus (Rounds 1–3B).

**It does license:** stopping broad external discovery; transferring remaining uncertainty to governance decisions, expert review, the G1 payload, and later executable validation.

**It does not license:**

- "first", "no study worldwide", "novel for the first time", or any universal-absence claim
- treating the corpus bound as a systematic review
- closing G2 — `CLOSE_SEARCH` is not a gate decision
- refusing to reopen search if a new question would plausibly move the structural novelty boundary

Every novelty statement must carry the corpus bound explicitly: *within the reviewed corpus*.

---

## Worked example

**Prompt:** "Sensor-to-BIM is the main novelty of Paper 2, right?"

**Correct response shape:**

- **Classification:** ESTABLISHED PRIOR ART. Sensor-to-BIM linking and IFC GlobalId anchoring appear in the reviewed corpus and are listed as prior art in `01_CURRENT_RESEARCH_CONTEXT_20260804.md`; `AGENT_RULES.md` §5 explicitly forbids an independent novelty claim for it.
- **What is actually candidate:** the integrated identity-governed evidence-to-action record–event chain, and specifically the event-history / authorization / verification / guarded-closure cluster — all corpus-bounded and pending G2 baseline and G3 validation.
- **Limitation:** even the candidate cluster is unvalidated; G2 is not frozen and G3 execution is not open.
- **Next action:** if Paper 2 currently frames sensor-to-BIM as the contribution, rewrite the contribution statement around the chain and move sensor-to-BIM into the background/prior-art section.

Do not concede this classification because the researcher restates the question more forcefully. Concede only if shown corpus evidence that reclassifies it.
