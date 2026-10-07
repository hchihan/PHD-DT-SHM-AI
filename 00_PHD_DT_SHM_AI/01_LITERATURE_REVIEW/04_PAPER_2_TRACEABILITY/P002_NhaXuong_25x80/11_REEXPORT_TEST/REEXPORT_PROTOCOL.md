# P002 · Second IFC export of the same registered RVT: protocol

2026-10-07 · ADR-RQ2-008 (PROPOSED) · Purpose: test whether the exported GlobalIds (BIM_GUID) of `MV-RVT-20261005-47748cbe` are reproduced by a second export of the unchanged model (evidence type E2). This answers reviewer objection 2 in part: it tests re-export stability. It does **not** create a second model version.

The protocol and the reading rules below are fixed **before** the export, so that the result cannot steer the interpretation.

## A. Workstation (the one with Revit 2027, build 27.3.0.28)

1. Copy `models/P002_KCNX_80m_v4_APPLY_TARGET.rvt` to the Revit workstation. Before opening it, check its SHA-256:
   `47748cbeb460229eabd9db01ca1e3f0119ed0b195200ff971703952b93ec9624`
   In PowerShell: `Get-FileHash .\P002_KCNX_80m_v4_APPLY_TARGET.rvt -Algorithm SHA256`.
   If the hash differs, stop.
2. Record the Revit build (Help → About). It must be 27.3.0.28; any other build is a confound and must be reported.
3. Open the RVT. Do **not** upgrade, edit, synchronise or save it. Close any "Save changes?" dialog with **No**.

## B. Export settings (must match export 1; values taken from the header of export 1)

| Setting | Value |
|---|---|
| IFC version | IFC 4.3 (header `IFC4X3_ADD2`) |
| Exchange requirement / view | the same setup as export 1. The header shows `CoordinationView, QuantityTakeOffAddOnView`, so **Export base quantities = ON** |
| Coordinate base | Shared Coordinates |
| Project origin / site | Internal |
| **Store the IFC GUID in an element parameter after export** | **OFF** (otherwise the RVT is changed) |
| Export only elements visible in view | same as export 1. If not known, use the same 3D view and record which |
| File name | `P002_KCNX_80m_v4_REEXPORT_2.ifc` |

If the export setup used for export 1 is still saved in the IFC exporter, use it unchanged and record its name.

## C. After the export

1. Close Revit **without saving**, then compute the RVT hash again. It must still equal the value in A1.
2. Copy the IFC into `P002_NhaXuong_25x80/models/`.
3. Run the comparison:
   ```
   python 11_REEXPORT_TEST/compare_ifc_exports.py models/P002_KCNX_80m_v4_APPLY_TARGET.ifc models/P002_KCNX_80m_v4_REEXPORT_2.ifc 11_REEXPORT_TEST
   ```
   The outputs are `P002_REEXPORT_SUMMARY.md` and `P002_REEXPORT_GLOBALID_COMPARISON.csv`.
4. Note the export date, time, Revit build, export setup name and the RVT hash before and after in `REEXPORT_RUN_RECORD.md`.

The script was self-tested on 2026-10-07 by comparing export 1 with itself. It found 760/760 elements with SAME_GLOBALID and matched all 760 rows of `08_TRACEABILITY/P002_IFC_STRUCTURAL_INVENTORY.csv` on Tag and GlobalId, including the 8 re-identified duplicates.

## D. Reading rules (fixed in advance)

| Outcome | What it means | What Paper 2 may say |
|---|---|---|
| R1: all 760 SAME_GLOBALID, including the 8 re-identified elements | The exporter reproduces GlobalIds for an unchanged model, including those it re-identifies | "A second export of the unchanged model reproduced all 760 GlobalIds, including the 8 that the exporter re-identified." Limitation (2) is narrowed to "edits between versions untested". |
| R2: all SAME except some of the 8 re-identified elements | Re-identification of duplicates is not deterministic | This is a stronger finding. The BIM_GUID of a duplicate-stored element is export-specific, which supports scoping identity to version and export. Report it as E2. |
| R3: CHANGED_GLOBALID for other elements as well | GlobalIds are not stable even without edits | Report it as observed. BIM_GUID must then be bound to the registered export (hash), not only to the RVT version. Contribution 1 still holds, but the definition in ADR-RQ2-002 must be revisited by a new ADR. |
| Header differs (build, view, coordinates) | Confound | Report the difference. Do not treat it as stability evidence until it is re-exported with matching settings. |

Relationship and property-set GlobalIds are reported as secondary; they are not component identities.

## E. What does not change

No change to the validator, the rules, the fixtures, the schema or the Gate 3 results. The test adds one E2 observation and one row in `P002_MODEL_VERSION_REGISTRY.csv`: a second DERIVED_EXCHANGE_MODEL of the same Model_Version_ID.
