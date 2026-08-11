# TASK TEMPLATES

## Template A — G1 evidence closure

```text
Audit G1 for RQ1/WP1/C4/Paper 1.

Check run registry, sensor identity, split-before-windowing, LORO folds, preprocessing provenance, model seeds and ResNet1D sensor mode.

Return:
1. claim-evidence matrix;
2. reproducibility blockers;
3. metrics allowed/prohibited;
4. Gate 1 acceptance checklist;
5. exact next execution task.

Do not use window-level sample count as independent experimental N.
```

## Template B — G2 ADR

```text
Draft the Action–Status–Event ADR for RQ2/WP2/C5/Paper 2/G2.

Use Round 1–3B only.

Resolve:
- Action_Record_ID versus Action_Status;
- current-state projection versus append-only event history;
- recommendation, authorization, execution and verification boundaries;
- closure/reopen guards;
- Verification_Record entity versus Inspection_Record subtype.

For every decision provide:
Claim → Evidence → Limitation → Decision → Validation.
Do not mark the ADR accepted.
```

## Template C — G2 ER model

```text
Create ER model v0.1 only after the ADR is approved.

Classify every entity, field and relation as:
LITERATURE_SUPPORTED / MULTI_SOURCE_INFERRED / THESIS_DEFINED / EVIDENCE_INSUFFICIENT.

Use:
FREEZE / FREEZE_PROVISIONALLY / EXPERT_REVIEW_REQUIRED / WAIT_FOR_G1_PAYLOAD / REMOVE.

Do not choose SHACL, graph database or blockchain as mandatory.
```

## Template D — CQ and validation contract

```text
Create the CQ Registry, Constraint Catalogue and Fixture/Oracle Manifest for G2.

Separate:
- business competency questions;
- structural constraints;
- lifecycle-transition rules;
- authorization rules;
- exact expected query answers;
- isolated invalid mutations.

Do not equate reverse query with transformation round-trip.
```

## Template E — Repository update

```text
Update current repository files to the approved 2026-08-04 position.

Preserve immutable deep-read reports.
Archive only files with an explicit successor.
Create a changelog and archive manifest.
Do not commit or push.
```
