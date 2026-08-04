# LIVING EVIDENCE BASE
**Version:** v1.1 — LIMITED-FEM | **Date:** 2026-07-17
**Supersedes as source of truth:** `Literature_Evidence_Living.md` (v1.0). The v1.0 file is preserved unchanged in this folder as the historical extraction record; detailed per-paper extraction tables live there and are referenced, not duplicated, here. Duplicate control remains governed by `../05_MASTER_INDEX_CONTROL/Literature_Review_Master_Index_Current.md`.
**Migration rule applied:** all RQ1 evidence retained; former RQ2-FEM evidence reclassified (SUPPORTING_REFERENCE / POST_PHD / ARCHIVE); former RQ3 traceability evidence retagged to new RQ2/Paper 2; former RQ4 evidence retagged to WP4. No evidence was re-read, added, or fabricated in this migration.

## Locked research chain (v1.1)

```text
Vibration data → condition/state-change evidence → BIM-linked component → inspection record → inspection-maintenance action support
```

Identifier chain: Sensor_ID → BIM_GUID → Condition_Evidence_ID → Inspection_Record_ID → Action_Status. FEM_Node_ID = optional metadata only.

## Section 1 — RQ1 / Paper 1: laboratory vibration evidence (retained unchanged)

All v1.0 RQ1 records remain valid. Claim IDs: C1-xx (Paper 1).

| Zotero key | Shorthand | Status | Role (bounded) | Claim ID | Paper |
|---|---|---|---|---|---|
| YR2NQWE7 (counterpart of DJACN6MG) | Zhang, Biswal & Wang 2020 (SHMnet) | Deep read (addendum) | Direct lab steel-frame bolted-connection precedent; single-accelerometer classification; repeated-data lesson; NOT leakage-safe protocol proof | C1-01 precedent; C1-04 split-design justification | Paper 1 |
| HWUA93NT (dup: W7HQQESV) | Valdez-Yepez et al. 2024 | Deep read | Labelled bolt-loosening dataset organisation, sensor metadata, repeated runs (jacket structure, strong adjacent) | C1-02 dataset documentation | Paper 1 |
| VVBGM9EN | Eraliev, Lee & Lee 2022 | Deep read | Multi-bolt loosening classification; window-split leakage caveat | C1-01, C1-04 | Paper 1 |
| PEUHYBPS | Goodarzi et al. 2025 | Deep read | LOGO vs K-fold; leakage inflation evidence (methodological) | C1-04 | Paper 1 |
| RWHW6F9I | Ramasso et al. 2024 (preprint) | Deep read — preprint boundary | Campaign/reassembly holdout; sensor comparison | C1-04 | Paper 1 |
| QUGY4928 | Avci et al. 2021 | Deep read | Review framing; validation limitations | C1-05 framing | Paper 1 |
| QIS5QS7V | Sajedi & Liang 2022 | Deep read | Simulated bridge vibration AI; split-by-vehicle-make design framing | C1-03 | Paper 1 |
| XSKNR656 | Armijo & Zamora-Sanchez 2024 | Deep read | Field bridge monitoring, sensor metadata → also field-feasibility background (see §5) | C1-03; C3-01 | Paper 1; Paper 3 bkg |
| VDPRGI94 | Dang et al. 2022 | Deep read | DT-SHM workflow background (AI classification part) — FEM part reclassified, see §6 | C1-03 | Paper 1 bkg |
| DFAJFF8J | Abdeljaber et al. 2018 | Limited access | 1-D CNN benchmark background only | C1-03 | Paper 1 bkg |
| JQSY7XD4 | Teng et al. 2022/2023 | Deep read (addendum) | Transfer-learning method background only | C1-03 | Paper 1 bkg |

RQ1 boundary (unchanged): no reviewed source provides the PhD's leakage-safe run-level protocol — it remains NPE (new PhD evidence). LORO and ResNet1D sensor-mode verification are open Gate 1 items.

## Section 2 — RQ2 / Paper 2 (new): evidence-to-action traceability

Claim register with full source table: `../04_RQ_EVIDENCE_ADDENDA/RQ2_TRACEABILITY_EVIDENCE_ADDENDUM_v1.0.md` (claims C2-01…C2-11). Summary: representation and linkage layers strongly supported (2ILY9YZ3, IM9UKGRV, KDRSBM9K, ULHLMFZ8, PHXJ2KJN); component identifiers standardized (FZ3GFSF2, L52SHNEH, WYN2RKEH); inspection-record linkage medium/indirect (GIIUUEW8, 4LKDXFMK, 8Y64JYBR); missing: CQ methodology, schema-validation criteria, provenance, DT maturity source (NEW_DEEP_READ_REQUIRED via OpenCode).

## Section 3 — BIM-linked inspection records

Cross-reference: addendum claims C2-05 and C2-11. Sources GIIUUEW8, 4LKDXFMK, 8Y64JYBR provide record structures (defect records, condition scores, repair records, element-ID-localized warnings) from bridge/SHM-management domains. Boundary: no reviewed source links records to leakage-controlled condition evidence in one chain — that chain is the PhD contribution (Gap statement C2-06).

## Section 4 — Component-level identifiers

Cross-reference: addendum claims C2-03, C2-04. IFC GlobalId as stable component identity (PHXJ2KJN, FZ3GFSF2); AIM/O&M information structures (L52SHNEH); ISO 23247-aligned data categories and component IDs (WYN2RKEH). Normative anchors for the thesis: TCVN 14177:2024; ISO 19650-3 (standards, cited as standards, not as research findings).

## Section 5 — Field feasibility (RQ3 / Paper 3)

| Zotero key | Shorthand | Role (bounded) | Claim ID | Paper |
|---|---|---|---|---|
| XSKNR656 | Armijo & Zamora-Sanchez 2024 | In-service monitoring workflow, low-cost MEMS sensors, warning dashboard; normal-condition pilot only | C3-01 field workflow | Paper 3 |
| VDPRGI94 | Dang et al. 2022 | Conceptual DT data-interaction workflow (non-FEM aspects) | C3-02 | Paper 3 bkg |
| GIIUUEW8 | Deng et al. 2022 | Threshold warning + element-ID localization | C3-03 inspection trigger | Paper 3 |
| 8Y64JYBR | Chen et al. 2014 | SHM management decision-support architecture | C3-03 | Paper 3 bkg |
| 4LKDXFMK | Li et al. 2023 | Defect/condition/repair record structures | C3-04 record workflow; C4-01 | Paper 3; WP4 |
| 3CJAB5LG | Zhang et al. 2024 | Optional decision-analysis vocabulary (WP4 only) | C4-02 | Optional |

Boundary: field feasibility means deployment + baseline + traceability scenarios. No field damage diagnosis; no classifier transfer; any anomaly triggers inspection, not a damage claim.

## Section 6 — Digital Twin maturity and scope

The thesis DT is **descriptive–diagnostic (management level), data-informed, without mandatory physics model**. Current support is background-level only (BZKLQK4H BIM→DT evolution; M72SVKKB conceptual framework; EK8QXFGD, FRJYYGCZ, M94HVWCY review metadata — screened only). A dedicated maturity-model source is NEW_DEEP_READ_REQUIRED (addendum C2-10). The C3 subsection "DT definition and maturity" must be written from a verified source, not from these background records alone.

## Section 7 — SUPPORTING_REFERENCE: former RQ2-FEM evidence (reclassified)

These records are no longer core evidence. Permitted use: qualitative mechanical hypotheses in Discussion/Limitation sections (labelled "hypothesis, not confirmed"), and historical context. Prohibited use: supporting any calibrated-FEM, stiffness-degradation, severity, or diagnosis claim in the thesis core.

| Zotero key | Shorthand | v1.0 role | v1.1 classification |
|---|---|---|---|
| LYNPWX2Q | Yang, Xia & Loh 2014 | Direct FEM loosening interpretation | SUPPORTING_REFERENCE |
| 3N5DY3NV | Weng, Loh & Yang 2009 | Direct FE updating | SUPPORTING_REFERENCE |
| YTH389L4 | Biswal et al. 2022 (NV: possible DOI overlap with BERUCUIC — unresolved) | Direct FE updating / virtual damper | SUPPORTING_REFERENCE |
| U4HIGWJ4 | Pal et al. 2022 | Direct fixity-factor updating | SUPPORTING_REFERENCE |
| BERUCUIC | Biswal et al. 2021 | Direct OpenSEES spring updating | SUPPORTING_REFERENCE |
| 7MUMMAHR | Yaoyama et al. 2024 | Strong adjacent probabilistic updating | SUPPORTING_REFERENCE |
| GGFJCZ7A (dup: UCIYTI8C) | Musil et al. 2025 | Strong adjacent MAC/frequency matching | SUPPORTING_REFERENCE |
| DX2JCMQ9 | Tian et al. 2021 | Methodological contact parameterisation | POST_PHD (calibrated-FEM expansion) |
| SF58JFER | Jiang, Zhu & Zhuo 2024 | Strong adjacent acoustic classification | SUPPORTING_REFERENCE (adjacent context) |
| SI97C35H | Svendsen et al. 2023 | Calibrated-FEM hybrid SHM | SUPPORTING_REFERENCE for the FEM aspect; retains Paper 1 supporting role for supervised-classification aspect (§1) |
| BBMA5P33 | Yi et al. 2011 | FEM-based OSP | POST_PHD — "optimal sensor placement" language prohibited in core; usable only as background for reference-informed placement discussion |
| 66GL7FBR | Sun et al. 2025 | OSP review | Same handling as BBMA5P33 |
| PRQL4Y8P | Guerrero Bobadilla et al. 2016 | Lab steel-frame dynamic response | SUPPORTING_REFERENCE (lab dynamics background) |
| L56P7RAF | Weil et al. 2025 | Modal tracking + uncertainty | SUPPORTING_REFERENCE (uncertainty framing may support CEI discussion) |
| VDPRGI94 (FEM aspect) | Dang et al. 2022 | Synthetic stiffness-loss FEM data | SUPPORTING_REFERENCE (FEM aspect only; see §1, §5 for retained aspects) |

## Section 8 — ARCHIVE / non-substantive records

Unchanged from v1.0: all screened-only, ranked-only, background-only, full-text-unavailable, source-not-located, manual-check, and duplicate records keep their v1.0 status and future rules in `Literature_Review_Master_Index_Current.md`. None were promoted or demoted in this migration.

## Cross-reference rule

Each evidence record appears in exactly one primary section; other sections cite it by key. Full extraction detail (research problem, sensor configuration, validation approach, boundaries) remains in v1.0 (`Literature_Evidence_Living.md`) and the PX addenda — not duplicated here.

## Claim / Evidence / Limitation / Next action

Claim: the evidence base migrates to the Limited-FEM architecture without loss — 33 substantive/limited canonical records retained, 15 reclassified, 0 deleted. Evidence: sections 1–8 above; counts per Master Index Current. Limitation: reclassification was performed from existing extraction records without re-reading PDFs; YTH389L4/BERUCUIC duplicate suspicion unresolved; DT-maturity and CQ-methodology evidence missing. Next action: OpenCode Zotero session for the five missing groups (addendum §Missing); resolve YTH389L4/BERUCUIC in the duplicate log.
