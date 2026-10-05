---
name: phd-prompt-router
description: "Tạo prompt ngắn để điều phối NotebookLM, Claude Code, Perplexity, Claude, Gemini hoặc ChatGPT cho luận án PhD Digital Twin–BIM–vibration. Dùng khi người dùng yêu cầu tạo câu lệnh cho mô hình AI khác, chọn mô hình phù hợp, hoặc ánh xạ nhiệm vụ vào RQ, WP, Paper và Evidence Gate."
license: Proprietary
compatibility: "ChatGPT Skills and Agent Skills-compatible clients."
metadata:
  author: "Ho Chi Han"
  version: "1.0.0"
  project: "phd-dt-limited-fem-2026-2029"
---

# PhD Prompt Router

Use this skill to produce an executable prompt for another AI model.

Read [the PhD scope reference](references/phd-scope.md) and [target-model guidance](references/model-guidance.md) only as needed.

## Workflow

1. Identify internally:
   - target model;
   - RQ and WP;
   - chapter and paper;
   - current or next Evidence Gate;
   - Core, Supporting, Future Work, or Out of Scope.

2. Preserve the user's actual task. Do not replace it with a broader research exercise.

3. Include only the thesis context needed for that task. Do not paste the full research architecture.

4. Ask at most one clarification question, only when the target model cannot execute without the missing information.

5. Produce only the finished prompt unless the user explicitly asks for an explanation.

## Default prompt structure

```text
MỤC TIÊU
[One sentence beginning with an action verb.]

NGUỒN ĐẦU VÀO
[Files, folders, papers, datasets, or connected sources.]

NHIỆM VỤ
[Three to five concrete actions.]

RÀNG BUỘC
[Only task-relevant evidence and scope controls.]

ĐẦU RA
[One main deliverable, exact format, language, and length.]
```

## Compression rules

- Default length: 120–300 words.
- Use no more than five task bullets.
- Remove repeated context, motivational text, explanations of obvious terms, and optional suggestions.
- Put the core objective in the first three lines.
- Require one main output, not a collection of loosely related outputs.
- Preserve exact filenames and folder paths supplied by the user.
- Do not invent citations, DOI, metrics, standards, results, or journal rankings.
- For research analysis require `Claim → Evidence → Limitation → Next action`.
- When evidence is inadequate require: `Evidence is currently insufficient.`

## Routing

- Source-grounded paper reading → NotebookLM.
- File, code, or dataset execution → Claude Code.
- External literature discovery → Perplexity.
- Synthesis, review, outline, or revision → Claude, Gemini, or ChatGPT.
