# 05 — ITEMS REQUIRING YOUR DECISION

**Plan ID:** REORGANIZATION_PLAN_20260803 · Plan only, nothing moved.

Seven decisions. Items **R1–R3** change what the plan does and are worth answering before approval. **R4–R7** can be deferred; the plan parks those files safely in `91_REVIEW_REQUIRED/` either way.

You can reply `APPROVE REORGANIZATION` to accept every default below, or `APPROVE REORGANIZATION` plus any override (e.g. *"R1: archive all six"*).

---

## R1 — Paper 1: six files with competing same-date versions ⚠️ *affects the plan*

**Plan default:** `MOVE_TO_REVIEW` → `91_REVIEW_REQUIRED/PAPER1_VERSION_REVIEW/`

| File | Size | Modified |
|---|---:|---|
| `PAPER1_OUTLINE_20260719.md` | 37 KB | 2026-07-19 |
| `PAPER1_Q2_INTEGRATED_OUTLINE_WITH_PRELIMINARY_RESULTS_v4_20260719.md` | 48 KB | 2026-07-19 |
| `PAPER1_JOURNAL_OUTLINE_EMPTY_RESULTS_SOURCE_v2_20260719.md` | 7 KB | 2026-07-19 |
| `KICH_BAN_THI_NGHIEM_PAPER1_VA_TIEN_KIEM_CHUNG_CAM_BIEN_CO_DAY_20260721.docx` | 53 KB | 2026-07-21 |
| `KICH_BAN_THI_NGHIEM_RUT_GON_20260721.docx` | 43 KB | 2026-07-21 |
| `Kich_ban_thi_nghiem_21.07.2026.docx` | 20 KB | 2026-07-21 |

**Why this is a judgement call.** Your instruction says outlines with multiple versions and undetermined currency go to `90_ARCHIVE/PAPER_VERSION_HISTORY`; it also says files whose role is undetermined go to the review folder. Both apply here. I chose **review**, because archiving all six would leave Paper 1 with no active outline and no active experiment protocol — and none of these files declares itself old. The three files that *do* declare themselves old (`Paper 1_Old_version (10.06).docx`, and the v3/v4/v6 `.docx` outlines already in `ARCHIVE_MINIMAL/`) go to archive as instructed.

`Evidence is currently insufficient` to name the current version: the three `.docx` protocols were not read, and the three `.md` outlines share a date with no supersede header.

**Options:** (a) keep as planned — review; (b) archive all six; (c) name the current file for each pair and archive the rest; (d) leave all six in `03_PAPERS/PAPER_1/` untouched.

---

## R2 — `MASTER_RESEARCH_CHARTER.md`: keep as navigation pointer? ⚠️ *affects the plan*

**Plan default:** `KEEP` in `00_GOVERNANCE/`

Your active-governance list does not name it, but `SOURCE_OF_TRUTH_HIERARCHY_v2.1.md` §2 assigns it a **distinct role** — "CURRENT NAVIGATION", a concise entry that redirects to v2.1 — separate from the Charter role itself. `00_README_START_HERE.md` reading-order item 5 also points to it.

Under "one active file per governance role", it does not conflict with v2.1: they hold different roles. But if you consider Charter-navigation redundant now that the README exists, it should be archived.

**Options:** (a) keep as planned; (b) archive to `90_ARCHIVE/GOVERNANCE_HISTORY/CHARTERS/`.

---

## R3 — `MASTER_RESEARCH_CHARTER_v2_20260719.docx` (v2.0) ⚠️ *affects the plan*

**Plan default:** `ARCHIVE` → `90_ARCHIVE/GOVERNANCE_HISTORY/CHARTERS/`

The hierarchy ranks it **#4 — "HISTORICAL DECISION SOURCE"**, above several active files, and describes it as the record of the v2.0 reframe to be consulted for context. Your instruction says old charters go to archive. Archiving it is consistent with that, but it means a file the hierarchy lists as a live lookup source moves out of ACTIVE, and two governance files that name it will need a path update.

**Note:** this `.docx` was not read.

**Options:** (a) archive as planned; (b) keep in `00_GOVERNANCE/` as a historical decision source.

---

## R4 — `Skill.md` — confirmed stale, but what next?

**Plan default:** `MOVE_TO_REVIEW` → `91_REVIEW_REQUIRED/STALE_AGENT_RULES/Skill.md`. **Content not edited.**

Modified 2026-07-28 — nine days after the `Action_Record_ID` ADR — yet §2 still states the chain as `… → Inspection_Record_ID → Action_Status` and `FEM_Node_ID chỉ là metadata tùy chọn`. Because it generates prompts for other models, the stale chain propagates downstream.

The move itself is not in question. The open item is the follow-up: **update it to `Action_Record_ID`, or retire it in favour of `00_GOVERNANCE/AGENT_RULES.md`?** That is a separate task and is not attempted here.

---

## R5 — The prompt-tooling cluster: four locations, three copies of the scope statement

The plan consolidates the two root items into `07_PROMPTS_AND_HANDOFFS/PROMPT_CONTROL_CENTER/`, but does **not** resolve which is authoritative:

| Item | Size | Note |
|---|---:|---|
| `PROMPT_CONTROL_CENTER_PROJECT_INSTRUCTIONS.md` (root) | 10.4 KB | "HƯỚNG DẪN DỰ ÁN" |
| `PROMPT_CONTROL_CENTER_PROJECT/00_PROJECT_INSTRUCTIONS.md` | 4.1 KB | "PROJECT INSTRUCTIONS" |

Not byte-identical — different structure, 2.5× size difference. After the move both land in the same folder, which makes the overlap visible but does not resolve it.

Separately, `07_PROMPTS_AND_HANDOFFS/phd-prompt-compressor/references/phd-scope.md` and `phd-prompt-router/references/phd-scope.md` are **byte-identical** (1,811 B). The plan **keeps both** — each is a self-contained skill package and deduplicating them would break skill portability. Confirm if you disagree.

---

## R6 — `BIM-AEC-CLAUDE.jpg`: role unknown

**Plan default:** `MOVE` → `07_PROMPTS_AND_HANDOFFS/ASSETS/`

228 KB, modified 2026-07-31, the only image in the repository, referenced by no document. Placement in `ASSETS/` is a guess based on the "CLAUDE" in its filename. If it is a paper figure or a demo screenshot it belongs elsewhere.

**Options:** (a) as planned; (b) `91_REVIEW_REQUIRED/`; (c) name its correct home.

---

## R7 — Empty folders

| Folder | Plan default | Why |
|---|---|---|
| `New folder/` | → `91_REVIEW_REQUIRED/EMPTY_FOLDERS/` | Default Windows name, created 2026-07-28, purpose unknown |
| `02_EVIDENCE_BASE/02.08.2026 Q2-Q3/` | → `91_REVIEW_REQUIRED/EMPTY_FOLDERS/` | Created 2026-08-02 — one day before the audit. Looks like a work phase you opened but had not populated. **If this is live, say so and it stays** |
| `03_PAPERS/PAPER_4_OPTIONAL/` | KEEP | Placeholder in the target structure |
| `04_PHD_SPECIAL_TOPICS/CHUYEN_DE_1/`, `CHUYEN_DE_2/` | KEEP | Placeholders |
| `06_LITERATURE_AND_ZOTERO/REFERENCE_EXPORTS/` | KEEP | Placeholder for future RIS exports |

Nothing is deleted in any case.

---

## Also recorded, no decision needed now

- **`90_BACKUP/` shell.** After its 127 files move to `90_ARCHIVE/`, the empty folder tree remains. The plan leaves it in place rather than removing it. Say the word and it goes to `91_REVIEW_REQUIRED/EMPTY_FOLDERS/`.
- **`CURRENT_STATUS_AND_NEXT_DIRECTION.md` is flagged, not edited.** Its §4 states *"LORO chưa chạy … run registry chưa khóa"* (dated 19/07), while `THREE_CAMPAIGN_REANALYSIS/` (files modified 29/07) contains a completed LORO matrix. **No research claim was altered by this plan.** Rewriting the status file is a separate, explicit task.
- **119 pre-existing dangling references** recorded in the 2026-08-03 audit are not caused by, and not repaired by, this plan.
- **Two G1 packages** remain separate with no supersession claim, as instructed.
- **No Gate is claimed closed, open, or passed.**

---

## Claim → Evidence → Limitation → Next action

**Claim.** Seven items cannot be decided from file metadata and governance documents alone. Three (R1–R3) change what the plan does; four (R4–R7) affect only where a file rests inside the review folder. In every case the file is preserved and the decision is left to you.

**Evidence.** Competing-version detection by identical modification date with no supersede marker; role conflicts read directly from `SOURCE_OF_TRUTH_HIERARCHY_v2.1.md` §1–§2 and `V2.1_CORE_EVIDENCE_INDEX.md`; SHA-256 comparison establishing that the two prompt-control-centre instruction files differ while the two `phd-scope.md` files are identical; folder creation timestamps.

**Limitation.** `Evidence is currently insufficient` to resolve R1 and R6 without reading the `.docx` files and opening the image — neither was done, since reading is not required to plan a reversible move and the instruction was explicit about not deciding unilaterally.

**Next action.** Answer R1–R3 (or accept the defaults), then reply `APPROVE REORGANIZATION`.
