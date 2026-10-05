# CLAUDE COWORK OPERATING PROTOCOL

## 1. Start every task with a task card

```text
Task:
RQ:
WP:
Chapter:
Paper:
Gate:
Scope:
Source files:
Output file:
Decision authority:
```

## 2. Read before acting

Claude must inspect:

- current source-of-truth files;
- task-specific evidence;
- related accepted ADRs;
- current status and next-action plan.

Do not work from a single report when a later evidence overlay exists.

## 3. Plan file operations before editing

Before modifying the repository, return:

| File | Action | Reason | Authority | Risk |
|---|---|---|---|---|
| path | UPDATE / CREATE / ARCHIVE / NO CHANGE | why | governing file | conflict/data-loss risk |

Do not proceed with destructive changes without user approval.

## 4. Scientific writing protocol

For every proposed claim:

| Claim | Evidence | Evidence type | Exact location | Limitation | Allowed wording |
|---|---|---|---|---|---|

Use:

- established prior art;
- corpus-bounded gap;
- candidate contribution;
- implemented result;
- validated result.

Do not collapse these categories.

## 5. Specification-development protocol

For every schema decision:

| Item | Literature support | Classification | G2 decision | Validation required |
|---|---|---|---|---|
| entity/field/relation | sources | LITERATURE_SUPPORTED / MULTI_SOURCE_INFERRED / THESIS_DEFINED / EVIDENCE_INSUFFICIENT | FREEZE / PROVISIONAL / REVIEW / WAIT / REMOVE | CQ, constraint, fixture, expert review |

## 6. Gate discipline

A Gate passes only when:

- required artifacts exist;
- acceptance criteria were set before evaluation;
- evidence is reproducible;
- limitations are recorded;
- approval/sign-off exists.

A roadmap, UI or narrative report cannot pass a Gate.

## 7. Output discipline

Preferred outputs:

- update current files;
- concise decision registers;
- reproducible matrices;
- explicit changelogs;
- archive manifests.

Avoid:

- parallel summaries with unclear authority;
- long prose without decisions;
- new technologies without a research need;
- code before specification.
