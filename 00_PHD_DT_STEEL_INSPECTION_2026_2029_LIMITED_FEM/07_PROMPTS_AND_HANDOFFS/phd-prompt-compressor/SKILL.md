---
name: phd-prompt-compressor
description: "Rút gọn prompt nghiên cứu quá dài thành câu lệnh thực thi ngắn, giữ nguyên mục tiêu, nguồn, ràng buộc học thuật và đầu ra. Dùng khi prompt có nhiều chú thích, lặp bối cảnh, trộn nhiều nhiệm vụ hoặc không nêu rõ sản phẩm cuối."
license: Proprietary
compatibility: "ChatGPT Skills and Agent Skills-compatible clients."
metadata:
  author: "Ho Chi Han"
  version: "1.0.0"
  project: "phd-dt-limited-fem-2026-2029"
---

# PhD Prompt Compressor

Use this skill to compress an existing draft prompt without changing its research intent.

Read [the PhD scope reference](references/phd-scope.md) only when the prompt belongs to the thesis.

## Compression procedure

1. Extract:
   - target model;
   - primary objective;
   - input sources;
   - indispensable tasks;
   - non-negotiable constraints;
   - one main output.

2. Delete:
   - repeated thesis background;
   - explanations already implied by the task;
   - optional suggestions;
   - duplicated prohibitions;
   - motivational language;
   - requests that belong to another Gate;
   - secondary artifacts not necessary to complete the objective.

3. Resolve conflicts by prioritizing:
   - the user's latest explicit instruction;
   - the relevant Evidence Gate;
   - the locked thesis scope;
   - the simplest executable workflow.

4. Return only the compressed prompt.

## Required structure

```text
MỤC TIÊU
NGUỒN
NHIỆM VỤ
RÀNG BUỘC
ĐẦU RA
```

## Limits

- Normal length: 100–220 words.
- Complex code or deep-read prompt: maximum 350 words.
- Maximum five numbered tasks.
- Keep exact paths, filenames, labels, sample rates, states, run IDs, and requested metrics.
- Do not add new research aims.
- Do not remove safeguards against leakage, unsupported claims, or scope expansion.
- Where relevant retain `Claim → Evidence → Limitation → Next action`.
- Return no commentary before or after the prompt.
