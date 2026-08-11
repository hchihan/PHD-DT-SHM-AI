# CROSS-FILE CONSISTENCY AUDIT 20260804

**Audit date:** 2026-08-04
**Status:** PASS WITH DECLARED HISTORICAL EXCEPTIONS
**Scope:** Current governance, navigation, G2-G3 roadmap, Paper 2 direction, G1-to-G2 interface, decision registers, archive moves, and protected-file integrity.

## 1. Checks And Results

| Check | Evidence | Result |
|---|---|---|
| Required current paths | 10 required entry, governance, control, roadmap, Paper 2, and interface files tested; 10 present | PASS |
| Single authority stack | Charter remains highest academic source; current-direction set is explicitly subordinate; Master Index is the sole complete current-file list | PASS |
| Locked research chain | Current entry, hierarchy, status, lock, roadmap, Paper 2, and interface use evidence -> BIM component -> inspection -> action -> status-event progression | PASS |
| Identifier chain | Current files use `Sensor_ID -> BIM_GUID -> Condition_Evidence_ID -> Inspection_Record_ID -> Action_Record_ID` | PASS |
| `Action_Status` semantics | Current files treat it as an `Action_Record` attribute/projection; status changes use `Status_Event` | PASS |
| CEI semantics | Current files define structured metadata and prohibit scalar, Health Index, severity, damage-probability, and priority meanings | PASS |
| FEM boundary | Current files retain `nominal, uncalibrated, reference-only, not used for damage diagnosis` | PASS |
| Gate states | G1 `OPEN / NOT READY`; G2 `OPEN / SPECIFICATION DEVELOPMENT`; G3 `NOT OPEN`; Paper 2 `DESIGN AND EVIDENCE DEVELOPMENT` | PASS |
| Single Paper 2 | One current Paper 2 spans G2 specification and later G3 executed validation; split/dual-paper commitments are explicitly superseded | PASS |
| G2-before-G3 order | G3 requires an explicit G2 readiness decision; no tool execution is accepted as a substitute | PASS |
| Instrument boundary | Revit, IFC, Dynamo, Pset, IDS, SQLite, viewers, and validation languages are supporting instruments; Graph 02 is prohibited at the current state | PASS |
| Decision register syntax | CSV parsed as 20 decisions: 4 `LOCKED`, 6 `BLOCKING_OPEN`, 9 `OPEN`, 1 `DEFERRED` | PASS |
| Archive integrity | 9 moved documents: 9 source paths absent, 9 destination SHA-256 values equal pre-reset hashes | PASS |
| Protected-file integrity | 214 protected evidence/history files scheduled to remain in place were re-hashed; 214 unchanged, 0 failures | PASS |
| Pre-reset path coverage | All 342 pre-reset classification rows resolve to a final retained or archived path | PASS |
| Final reset manifest | 367 managed rows; 366 post-reset hashes rechecked with 0 failures; self-hash intentionally omitted | PASS |
| Hard deletion rule | No hard deletion performed | PASS |

## 2. Historical Exceptions

The following are expected historical references, not current conflicts:

- `00_GOVERNANCE/THE_COUNCIL_REVIEW_FEM_OR_NO_FEM_17.07.2026.md` contains the 2026-07-17 identifier notation ending in `Action_Status`. The hierarchy now limits this file's authority to Verdict B scope and states that the 2026-07-19 Action-ID ADR supersedes its data-model notation.
- Protected evidence, discovery outputs, repository audits, backups, and archives may contain old paths, old status labels, or superseded terminology. Current governance explicitly prevents these files from overriding the current set.
- The two referenced roadmap names `G2_G3_PAPER2_REVISED_ROADMAP_v1.1.md` and `G2_G3_DUAL_PAPER_ROADMAP_v1.2.md` were not present. Their attributed commitments are recorded as logically superseded, not represented as physically archived files.

## 3. QA-Driven Fixes

The audit found and corrected:

1. live Charter and Action-ID ADR references to the archived unresolved-items tracker;
2. ambiguity about whether historical Council data-model notation could override the later ADR; and
3. missing current-status disclosure for pending official legal-source verification, unresolved G4 field access, and retained historical notation.

## 4. Untracked Concurrent Files

Three PDFs appeared at the project root after the pre-reset inventory:

- `applsci-16-04642.pdf`
- `buildings-15-01312.pdf`
- `buildings-15-02633.pdf`

They were not read, classified, modified, moved, staged, or committed by this reset. Their status remains outside the managed reset baseline and requires separate user classification.

## 5. Limitations

- This audit checks governance consistency, path existence, CSV syntax, Git state, and cryptographic integrity. It does not validate the scientific conclusions of protected evidence or extract and review every PDF/DOCX.
- Passing this audit does not close G1, G2, or G3 and does not establish Paper 2 submission readiness.
- Open decisions in `G1_G2_INTERFACE_DECISION_REGISTER.csv` remain substantive research work.

## 6. Conclusion

**Claim:** The current control surface now presents one research chain, one identifier chain, one G2-before-G3 roadmap, and one current Paper 2 direction.

**Evidence:** Current-path checks, status and terminology scans, 9 archive hash matches, 214 protected-file hash matches, 342/342 pre-reset path resolution, 366 verified final-manifest hashes, and parsed decision-register counts.

**Limitation:** Gate execution evidence remains incomplete and three concurrent untracked PDFs are outside this reset.

**Next action:** Resolve the six `BLOCKING_OPEN` interface decisions and preregister competency questions and acceptance criteria before any G3 implementation.
