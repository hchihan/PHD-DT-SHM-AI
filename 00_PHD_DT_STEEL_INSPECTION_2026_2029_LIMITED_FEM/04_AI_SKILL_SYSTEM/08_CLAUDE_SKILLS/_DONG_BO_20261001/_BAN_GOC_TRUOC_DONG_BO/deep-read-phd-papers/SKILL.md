---
name: deep-read-phd-papers
description: Deep-read and teach papers for the Digital Twin Limited-FEM PhD; verify evidence, map RQ/WP/Gates, and provide professor-style teach-back and defense coaching.
---

# Deep-read and teach PhD papers

Turn one paper into both a source-grounded evidence record and a supervisor-style learning session for the Limited-FEM thesis. Treat document conversion as preprocessing, not evidence; every important claim must remain traceable to the original paper. Never let a teaching explanation become an author claim.

## Required references

Read all four references before analyzing or teaching a paper:

- [references/source-authority.md](references/source-authority.md) for source precedence, dynamic status and superseded-file control.
- [references/thesis-routing-map.md](references/thesis-routing-map.md) for the locked thesis mapping and scope firewall.
- [references/deep-read-protocol.md](references/deep-read-protocol.md) for extraction, verification, idea screening and the output contract.
- [references/supervisor-teaching-protocol.md](references/supervisor-teaching-protocol.md) for method reconstruction, results interpretation, thesis application and interactive teaching.

When current source-of-truth files are supplied, read them before making thesis judgments and prefer them over bundled snapshots according to `source-authority.md`. Never infer that a newer-looking filename has authority.

## Select the response mode

Infer the mode from the request; do not ask unless the choice materially changes the work.

- `AUDIT`: verify a paper and produce the evidence record. Use for “đọc sâu”, “đánh giá”, “research gap”, “limitations”, “phương pháp”, or Gate mapping.
- `PROFESSOR`: teach the verified paper in layers. Use for “giảng lại”, “dạy tôi”, “tôi chưa hiểu”, “giống giáo sư hướng dẫn”, equations, figures, or method mechanics.
- `INTERACTIVE`: teach one module and one question at a time. Use for “hỏi tôi”, “kiểm tra mức hiểu”, “học tương tác”, or defense rehearsal.
- `FULL`: produce the complete evidence record plus all teaching modules only when the user explicitly requests a full report or reusable file.

Default to `AUDIT + a five-minute lesson`, not the full A–N report. This keeps the result usable while preserving a path to deeper teaching.

## Workflow

### 1. Establish the source

Require the original PDF whenever available. Record title, authors, year, venue, DOI or stable URL only if visible in the paper or verified from a primary source. Compute or retain a file hash when a local PDF is used.

If only an abstract, screenshot or citation is supplied, narrow the task and state that full-paper limitations and future work cannot be verified.

### 2. Convert and quality-check

Prefer the open-source MinerU parser for a complex or multi-column PDF:

```bash
python3 scripts/convert_with_mineru.py PAPER.pdf --output-dir PAPER_EXTRACT
```

MinerU is an optional runtime dependency, not bundled in this skill. If its CLI is unavailable, use an already converted Markdown/JSON packet or the available PDF-reading tools. Do not install large dependencies without user authorization.

After conversion, run:

```bash
python3 scripts/index_paper.py PAPER_EXTRACT/path/to/paper.md --output PAPER_EXTRACT/paper_index.json
```

Inspect the original PDF for every page used in the final evidence record. Verify at minimum: title/abstract, method or framework, central results, limitations, future work, and any table/figure carrying a key result. Mark conversion defects explicitly; never silently repair numbers, equations or citations.

### 3. Read in passes

Use the protocol's five passes:

1. orientation and contribution;
2. method, data and validation;
3. limitations and future work;
4. thesis mapping and idea screening;
5. professor-style teaching, teach-back and application.

Do not rely only on sections literally titled “Limitations” or “Future work.” Search the Discussion, Conclusion, threats to validity, boundary conditions and qualifying language.

### 4. Separate author statements from analysis

Label each limitation or proposed direction as one of:

- `AUTHOR-STATED`: explicitly stated by the paper;
- `READER-INFERRED`: defensible inference from method/results;
- `THESIS-RELEVANCE`: relationship to this thesis;
- `NEW-IDEA`: candidate idea, not yet an established gap.

Never convert an author recommendation directly into the user's novelty claim. A viable idea must pass scope, evidence, data, method, contribution and non-duplication checks in the protocol.

### 5. Route into the thesis

Always report:

`RQ → WP → thesis chapter → target paper → Evidence Gate → scope → evidence type`

Allow one primary mapping and up to two secondary mappings. Give the primary mapping only when a specific result, method or limitation directly serves it. Otherwise map the paper to Chapter 2 background/gap evidence or mark it out of scope.

Apply the Limited-FEM firewall. FEM may be nominal, uncalibrated and reference-only; it cannot become a diagnostic axis, RQ, WP, chapter, paper or Gate.

### 6. Produce the evidence record

Follow the report structure in [references/deep-read-protocol.md](references/deep-read-protocol.md), scaled to the selected response mode. Use concise Vietnamese unless another language is requested.

For a reusable or batch review, save one Markdown record named `<year>_<first-author>_<short-title>_deep-read.md`; keep conversion files separate from the analytical record.

For all thesis judgments, use:

`Claim → Evidence → Limitation → Next action`

Give locators as printed PDF page plus section/table/figure when available. If only converted text is available, use the Markdown heading and line range and label it provisional.

### 7. Teach the paper after verifying it

Follow [references/supervisor-teaching-protocol.md](references/supervisor-teaching-protocol.md). Reconstruct the paper as:

`Problem → research design → data/input → processing/model → validation → results → defensible conclusion`

Explain in layers: short overview, section-by-section logic, method mechanics, results interpretation, then thesis application. Define technical terms on first use. For equations, define variables, intuition, assumptions and what the equation cannot prove. For tables and figures, explain the comparison, the signal, uncertainty and claim boundary.

Label teaching content as:

- `SOURCE-VERIFIED`: explicitly supported by the paper;
- `TUTOR-EXPLANATION`: a faithful explanation or analogy;
- `THESIS-APPLICATION`: proposed use or adaptation for this thesis;
- `UNKNOWN`: requires further evidence.

Teach at three depths: intuition, research mechanics and defense-level critique. Explain why the authors made each design choice, what alternative choices existed and what proof obligation each choice creates. Never substitute polished explanation for missing evidence.

For `PROFESSOR`, deliver the five-minute lesson and the most relevant module first, then offer the next module. For `INTERACTIVE`, ask exactly one question, wait, diagnose the misconception and continue from basic to advanced. For `FULL`, deliver all tutorial sections and the three-question comprehension check.

### 8. Synthesize a paper set

For multiple papers, finish and save each independent evidence record before comparing them. Then build a cross-paper matrix of convergent limitations, conflicting findings, method differences, thesis destinations and candidate ideas. Do not let one paper's interpretation contaminate another paper's extraction.

Save the synthesis as `<topic>_cross-paper-synthesis.md`. Treat a gap as a candidate until supported by at least two independent papers or a targeted verification search. Distinguish “the literature has not done this” from “the reviewed papers did not report this.”

## Non-negotiable controls

- Do not fabricate quotations, citations, DOI, metrics, sample sizes, datasets, limitations or future-work statements.
- Do not treat the abstract as proof of method or results.
- Do not treat citation frequency, journal rank or author reputation as methodological quality.
- Do not claim a research gap from one paper. Use “candidate gap” until cross-paper evidence exists.
- Do not transfer laboratory classifiers directly to field diagnosis.
- Do not introduce predictive maintenance, RUL, calibrated FEM, stiffness-degradation inference, weighted Health Index, autonomous maintenance or AI-superiority claims.
- Do not call a paper “core” merely because it contains Digital Twin, BIM, sensors or AI keywords.
- Do not present a tutor analogy, reconstructed example or thesis adaptation as if it came from the paper.
- Do not copy a paper's method into the thesis without checking construct fit, data compatibility, validation obligations and novelty.
- Do not equate statistical significance, classification accuracy or a visual trend with practical maintenance usefulness.
- Do not hard-code the current Gate, dataset count, model result or field-access status. Read the current status source each time; otherwise write `Evidence is currently insufficient.`
- Do not let a professor-style explanation imply that the paper, the thesis or the user has proved more than the cited evidence supports.
- Write `Evidence is currently insufficient.` whenever the paper or thesis evidence does not support a conclusion.
