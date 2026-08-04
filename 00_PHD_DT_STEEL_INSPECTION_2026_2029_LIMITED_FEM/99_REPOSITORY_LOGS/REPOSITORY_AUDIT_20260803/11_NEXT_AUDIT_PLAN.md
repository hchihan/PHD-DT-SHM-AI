# 11 — NEXT AUDIT PLAN

**Audit ID:** REPOSITORY_AUDIT_20260803 · **Proposed only — none of the stages below has been performed**

This run was a read-only inventory. The stages below describe what a subsequent pass *could* do. **Stages 4–6 must not begin without explicit user approval.**

---

## Stage 0 — What has already been done (this run)

| Done | Not done |
|---|---|
| Full recursive enumeration: 301 files, 61 directories, 183.5 MiB | No file read of `.pdf` (52) or `.docx` (13) |
| SHA-256 for 301/301 files | No content-similarity comparison (only name/size/hash) |
| Cloud-only / lock / access check on every file — all clear | No scan outside the repository root |
| 61 exact-duplicate groups identified | No canonical file selected for any family |
| 119 dangling artifact references identified | No broken reference repaired |
| 12 governance roles mapped to 41 candidates | No role resolved where candidates conflict |
| Legacy-keyword scan across 232 text files | No file reclassified or marked superseded |
| 11 report files produced | **No file moved, renamed, merged, archived, or deleted** |

---

## Stage 1 — Confirm the source of truth

**Trigger:** can start immediately. Prerequisite for everything else.
**Input:** `06_GOVERNANCE_AND_SOURCE_OF_TRUTH_CANDIDATES.md`, `10_MANUAL_REVIEW_PRIORITY.md` P1.
**Who decides:** the user. An agent can gather evidence but must not choose.

Steps:
1. Read the three root READMEs side by side; the user names one as current and states the disposition of the other two.
2. Decide whether the repository is operating at **v2.1** or **v2.2**. If v2.2, record which governance files still need synchronising (README v2.2 itself lists this as an open condition).
3. Decide the status of `Skill.md`: current, superseded, or requiring a chain update from `Action_Status` to `Action_Record_ID`.
4. Decide the fate of the archive tier: create `99_ARCHIVE_PRE_V2_SYSTEM_20260719/` inside this repository, point the hierarchy at `90_BACKUP/` instead, or record that the archive lives outside this root.
5. Decide whether `MASTER_INDEX_CURRENT.md` stays inside `PROJECT_CLEANUP_20260718/`.
6. Check `CURRENT_STATUS_AND_NEXT_DIRECTION.md` §4 against the 2026-07-29 reanalysis outputs and decide whether the LORO/run-registry statements need updating.

**Output:** `SOURCE_OF_TRUTH_DECISION_20260xxx.md` — one canonical file per governance role, with the disposition of every non-canonical candidate. **No file is moved at this stage; the decision is recorded first.**

---

## Stage 2 — Verify campaigns and evidence packages

**Trigger:** after Stage 1 (needs to know which charter and gate definition govern).
**Nature:** primarily a **search outside this repository**, not a read.

Steps:
1. Search the sibling folders one level up — `01_KNOWLEDGE/`, `02_PROJECTS/`, `03_RESEARCH_ASSETS/`, `04_AI_SYSTEM/`, `05_MASTER_INDEX_CONTROL/`, `05_REPORTS_AND_PRESENTATIONS/`, `06. Tieu_luan_tong_quan/` — and any local drive, for: the three campaign folders (216 CSVs), `CANONICAL_THREE_CAMPAIGN_DATASET.zip`, `DATA_ALL_3_CAMPAIGN/`, `RUN_REGISTRY_LOCKED.csv`, `BAO_CAO_RESNET1D.docx`, and the 20 pipeline scripts.
2. For any script located, verify it against the SHA-256 values published in `01_ENVIRONMENT_PROVENANCE.md` and `10_REPRODUCIBILITY_MANIFEST.md`. This gives a hard yes/no on provenance.
3. Read the 13 `.docx` files — especially the three Vietnamese experiment protocols, `Checklist_Campaign_3_Gate1.docx`, and `Yêu cầu phân tích PASCO–ADXL cho Paper S1.docx` — and extract campaign metadata into the campaign map.
4. Determine the intended relationship between `CANONICAL_THREE_CAMPAIGN_DATASET` and `THREE_CAMPAIGN_REANALYSIS`.
5. Record, per Evidence-Gate-1 artifact, whether it exists, exists elsewhere, or was never created.

**Output:** `G1_ARTIFACT_LOCATION_REGISTER_20260xxx.csv` — one row per named artifact: name, cited-by, found/not found, location if found, hash match yes/no.

**Constraint:** read-only. Do not copy the campaign data into this repository at this stage — where it should live is a Stage 4 decision.

---

## Stage 3 — Distinguish current from superseded

**Trigger:** after Stages 1 and 2.
**Input:** `04_DOCUMENT_VERSION_MAP.csv` (139 rows across 25 document families), `05_DUPLICATE_AND_NEAR_DUPLICATE_REPORT.csv` (153 pairs).

Steps:
1. For each of the 25 families with more than one member, read the members and assign exactly one of: `CURRENT`, `HISTORICAL_REFERENCE`, `SUPERSEDED`, `BACKUP_COPY`, `UNKNOWN`.
2. Give priority to the families flagged `Conflict_Risk = HIGH` in `04_DOCUMENT_VERSION_MAP.csv`.
3. Confirm the header convention the governance already mandates — `Status: SUPERSEDED` / `Superseded by:` / `Preserved for: historical traceability only` — and list which files lack it.
4. For the 61 exact-duplicate groups, decide per group which path is the keeper. Note the two groups that duplicate **within active locations** (`kim2018.pdf` ×3, `phd-scope.md` ×2).
5. Identify which of the 63 unique-content files in `90_BACKUP/` must be preserved as history.

**Output:** `CURRENT_VS_SUPERSEDED_REGISTER_20260xxx.csv`. **Still no file moved** — this stage adds status headers at most, and only with approval.

---

## Stage 4 — Define the target structure ⚠️ *requires user approval*

**Trigger:** only after Stages 1–3 are complete and signed off.

Steps:
1. Decide whether the current `00_`–`90_` scheme is kept or revised.
2. Decide where the archive tier lives and what goes in it.
3. Decide the home for: the G1 data and code (if located), the prompt-tooling cluster, the currently-loose root files, and the six empty directories.
4. Decide the retention rule for `90_BACKUP/` — keep whole, keep only unique content, or supersede with a fresh snapshot.
5. Write a naming convention covering the deviations recorded in `08_LOOSE_ROOT_ITEMS_REPORT.md` §5.

**Output:** `TARGET_REPOSITORY_STRUCTURE_20260xxx.md`, approved by the user before Stage 5.

---

## Stage 5 — Produce a move / archive plan ⚠️ *requires user approval*

**Trigger:** after Stage 4 is approved.

Steps:
1. Write a per-file plan: `File_ID`, current path, proposed path, action (`KEEP` / `MOVE` / `ARCHIVE` / `MERGE_CANDIDATE`), justification, reversibility note.
2. Take a fresh checksum snapshot before any change, following the pattern of the existing `SNAPSHOT_CHECKSUM_MANIFEST_20260718.csv`.
3. Dry-run the plan: verify every proposed target path is free and every affected inbound reference is listed.
4. List the documents whose internal links would break, and the exact edits needed. **The 119 dangling references already present should be repaired in the same pass, not left.**
5. Have the user approve the plan file itself.

**Output:** `MOVE_AND_ARCHIVE_PLAN_20260xxx.csv` + `PRE_MOVE_CHECKSUM_MANIFEST_20260xxx.csv`.

**Rule:** deletion is not part of this plan. Governance already states — `SOURCE_OF_TRUTH_HIERARCHY_v2.1.md` §3 — *"Không xóa khi chưa chắc chắn — đưa vào archive thay vì xóa"* (do not delete when unsure; archive instead). This audit endorses that rule.

---

## Stage 6 — Execute ⚠️ *requires explicit user approval; not part of any audit*

Only after Stage 5 is approved, and only as written. Post-execution: re-run the inventory, diff against `01_FULL_REPOSITORY_INVENTORY.csv`, verify every SHA-256 survived the move unchanged, and confirm no reference was left broken.

---

## Dependency diagram

```
Stage 1  Source of truth ──────┐
                               ├──> Stage 3  Current vs superseded ──> Stage 4  Target structure ⚠
Stage 2  Artifact location ────┘                                              │
                                                                              v
                                                                       Stage 5  Move plan ⚠
                                                                              │
                                                                              v
                                                                       Stage 6  Execute ⚠
```

Stages 1 and 2 can run in parallel. Stages 4–6 are gated on user approval.

---

## Standing constraints for every future stage

1. **Zotero must not be modified** until the user approves the writeback queue — `UNRESOLVED_ITEMS_TRACKER_v2.1.md` item #14.
2. **No research result, metric, or citation may be altered** without evidence — `SOURCE_OF_TRUTH_HIERARCHY_v2.1.md` §3.
3. **Archive rather than delete** when uncertain — same source.
4. **No superseded file may be removed** without the `Status: SUPERSEDED` / `Superseded by:` header being applied first.
5. **Evidence files are never deleted** — only reclassified or relinked — same source.
6. Every stage produces its output in `99_REPOSITORY_LOGS/` and touches nothing else without approval.

---

## Claim → Evidence → Limitation → Next action

**Claim.** A six-stage plan follows from this inventory. Stages 1–3 are read-and-decide and can proceed on the evidence already gathered. Stages 4–6 change the repository and are gated on explicit user approval. **None of the six stages has been performed.**

**Evidence.** Stage ordering follows the dependency structure recorded in `10_MANUAL_REVIEW_PRIORITY.md` and the blocking items in `UNRESOLVED_ITEMS_TRACKER_v2.1.md`. The standing constraints are quoted from `SOURCE_OF_TRUTH_HIERARCHY_v2.1.md` §3 and the tracker, not invented by this audit. Stage 5's checksum-snapshot step follows the precedent already set by `SNAPSHOT_CHECKSUM_MANIFEST_20260718.csv` in `90_BACKUP/`.

**Limitation.** The plan assumes the missing G1 artifacts can be located in Stage 2. If they cannot, Stage 4 must additionally decide how to represent an unreproducible evidence package — a question this audit does not attempt to answer. Stage timings are not estimated because Stage 2 is a search whose duration depends on where the data turns out to be. `Evidence is currently insufficient` to plan beyond Stage 2 in detail.

**Next action.** User reads `00_EXECUTIVE_SUMMARY.md` and `10_MANUAL_REVIEW_PRIORITY.md`, then authorises Stage 1 and Stage 2. No repository change occurs until Stage 4 is reached and approved.
