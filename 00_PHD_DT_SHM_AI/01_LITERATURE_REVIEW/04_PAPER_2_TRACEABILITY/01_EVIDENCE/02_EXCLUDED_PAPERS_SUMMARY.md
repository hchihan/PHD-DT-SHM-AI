# Excluded / Background Papers -- Summary

**Scope note.** This file summarizes papers considered during Stage A screening but not carried into the Stage B deep-read corpus. It is a counts-and-representative-examples summary, not an exhaustive per-item listing, per the task instructions.

---

## 1. Precision-tagged pool (PAPER_2 / RQ2 / WP2 Zotero tags)

**Total items screened under this tag combination: 22** (see [01_ZOTERO_TARGETED_SCREENING.csv](01_ZOTERO_TARGETED_SCREENING.csv) for the full per-item classification).

- **Carried into Stage B deep-read corpus:** 8 of the 22 (GWP87WLC, Y44EIXWG, XUN8EX6X, VI5QMSAE, TXRF6GUC, F8RMUZ44, AQDJR2UE, 8HJN7D7E), plus 4 items found via the separate "Candidate Gate" tag scheme (8MCF7A8G, XWZYTUV6) and plain topical match (YKGTBESL, NQ3KGDWN) -- 12 total, see file 03.
- **BACKGROUND_REFERENCE (not deep-read, but topically adjacent):** 10 items.
- **EXCLUDE (no PDF attachment, confirmed via `zotero_get_attachment_path` + `zotero_get_item_fulltext`):** 3 items -- JZVZCHRI (Hüthwohl et al., RC bridge defect schema), B8QZMS77 (PROV-DM standard), FJJAV9T4 (PROV-O standard).

### Representative BACKGROUND_REFERENCE examples and why they were not selected

| Zotero key | Title (short) | Reason not selected |
|---|---|---|
| JGM5YHH8 | BAS-BIM linked-data point naming (Quinn et al.) | Sensor-to-BIM linkage is already established territory per the prior CORE-5 review; would not test a *remaining* gap. |
| 9TDVUE9Q | Bridge damage IFC semantic enrichment (Isailović et al.) | Condition-evidence generation/injection into IFC already covered by CORE-5 (CORE-02); corpus-size cap (8-12 papers) prioritized less-covered ground. |
| MSI2K38K | BIM O&M maintenance-sheet schema (Carvalho et al.) | Falls in Action_Status/maintenance-record territory, which the task explicitly instructs to treat as downstream/supporting, not core. |
| 2ILY9YZ3 / 3S858MKE | IFC Monitor SHM schema extension (Theiler & Smarsly; Theiler, Dragos & Smarsly) | Self-tagged ABSTRACT_ONLY / laboratory companion study; methodological foundation rather than an identity- or accountability-chain contribution. |
| YIJ57IV5 | ifcOWL EXPRESS-to-OWL conversion (Pauwels & Terkaj) | Foundational conversion methodology cited as background by several Stage-B papers; not itself a traceability contribution. |
| SEZBLZHH | Building Topology Ontology (BOT) (Rasmussen et al.) | Foundational spatial-topology ontology, background/related-work status in the Stage-B corpus rather than a direct identity/provenance claim. |
| WFVDNKSJ | GSA BIM Guide Series 08 (U.S. GSA) | Directly relevant (persistent Asset ID alongside GUID) but is owner/government guidance, not a peer-reviewed primary study -- ranked below the Stage-B cut per the stated prioritization order. |
| EY3GJVZV | IFC 4.3.2.0 IfcRoot/IfcGloballyUniqueId normative spec | Essential normative baseline for the GUID mechanism, but a standards document rather than an empirical study; used as a reference definition, not deep-read as a corpus paper. |
| 8PB7EN2E | ISO 55000 asset-management vocabulary | Generic cross-domain vocabulary; self-tagged METADATA_ONLY; no BIM/IFC-specific identity or traceability content. |
| Q4PJY4QN | Competency-questions-in-ontology-engineering survey (Monfardini et al.) | Cross-domain ontology-engineering methodology survey, not BIM/traceability-specific. |

---

## 2. Broader background pool (`GATE2_GATE3` Zotero tag)

This tag marks the general "Digital Twin / SHM / bridge-inspection / BIM interoperability" literature collected during earlier, broader literature-review passes for the thesis (not screened specifically for this targeted review's G1/G2/G3 groups).

**Items observed carrying this tag: over 100** (the listing query was capped at 100 results and returned no sign of ending; the true count is at least 100 and likely higher). None of these were individually re-screened against the G1/G2/G3 definitions for this task, consistent with the instruction to report counts and representative examples rather than an exhaustive re-classification of the whole background pool.

By inspection of titles/abstracts, this pool is dominated by three non-target topic clusters:

1. **Digital Twin / SHM survey and application papers** (bridge DTs, railway DTs, heritage-structure monitoring, sensor-fusion reviews) -- e.g. *Strategies for Maximising the Value of Digital Twins for Bridge Management and Structural Monitoring: A Systematic Review* (WHL9M4DH), *Sensor-Driven Digital Twins for Bridge Infrastructure* (RXKCP2AK), *Digital Twin Technology in Transportation Infrastructure* (MEJ8J63Q). These describe DT/SHM system architectures generally but do not address BIM-GUID identity persistence, SHACL/RDF validation, or inspection-record accountability specifically.
2. **BIM/SHM/IoT integration papers not focused on identity or record accountability** -- e.g. *Enhancing Facility Management with a BIM and IoT Integration Tool* (23G8SQK5), *Linking SHM and BrIM through IFC schema enrichment* (QG8A6JYD), *Hybrid monitoring methodology* (YRMWNSY2). These are sensor-to-BIM or condition-monitoring papers; per this task's explicit exclusion rule, they were **not** classified DIRECT merely for containing BIM/DT/inspection keywords.
3. **Adjacent-domain provenance/versioning papers outside construction** -- e.g. *Unified Lineage System: Tracking Data Provenance at Scale* (J77SGY5B, distributed-systems data lineage), *Managing Clinical Data Lineage in Distributed Healthcare Integration Environments* (NXR6VRFZ, healthcare), *Untangling the Timeline: [...] Version Control in Modern CAD* (IIZ3GCNM, mechanical CAD). Topically resonant with G2/G3 concepts but outside the AEC/BIM domain and not selected given the corpus-size cap and the availability of closer BIM-domain candidates.

A small number of items in this broader pool were already promoted into the precision-tagged pool or the Stage-B corpus by earlier curation passes (e.g. YKGTBESL, VC5ELKN2/"Heinlein et al." system-and-data-integrated linking of 3D bridge models with knowledge graphs -- covered in the prior CORE-5 review, not re-selected here to avoid duplication).

**Disposition of the broader pool for this task:** BACKGROUND_ONLY / EXCLUDE en masse, except for the items already promoted into the precision-tagged pool (Section 1) or the Stage-B corpus (file 03). No individual full-text screening was performed on this broader pool in this task, per the ~8-12 paper corpus-size instruction and the requirement not to search new literature beyond what Zotero metadata/tags already surface.
