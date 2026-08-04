## Scope and method

This report evaluates peer-reviewed studies against the locked PhD research chain: **condition/state-change evidence → BIM/IFC component → inspection record → maintenance or inspection action record**, in Construction Management / Asset Management. FEM is nominal, uncalibrated, reference-only and is excluded from diagnostic use. The analysis draws on the project's existing living evidence base (traceability addendum, condition-evidence review, IFC GlobalId governance report)  plus new backward/forward citation searches on the six seed studies (Lorvão Antunes et al. 2024; Kim et al. 2018; Heaton & Parlikad 2020; Lee et al. 2021; Çelik et al. 2022; Johannes et al. 2021).[^1][^2][^3]

**Transparency note on seed studies.** Within the searched sources and databases, "Heaton & Parlikad (2020)" and "Lee et al. (2021)" were positively located and verified. "Lorvão Antunes et al. (2024)" could not be located as a distinct standalone paper; the closest matching verified reference is **Antunes, César Júnior, Ribeiro & Franco de Carvalho (2024), "Analysis of IFC interoperability data schema for project representation," Automation in Construction, vol. 166**, DOI 10.1016/j.autcon.2024.105650  — metadata/abstract-level only, author-name match is probable but not confirmed at full-text level. "Kim et al. (2018)" most plausibly corresponds to **Kim, K., Kim, H., Kim, W., Kim, C., Kim, J., & Yu, J. (2018), "Integration of IFC objects and facility management work information using Semantic Web," Automation in Construction, 87, 173–187**  — metadata-only in this search; full text was not retrieved. "Çelik et al. (2022)" and "Johannes et al. (2021)" could not be verified in the searched sources and databases; no matching peer-reviewed record with these author names in the BIM/IFC/condition-monitoring/inspection space was found. These two are flagged as **unresolved** and must not be cited as established evidence until located.[^4][^5][^6][^7][^8]

## Comparison table

| Study | Sensor/condition evidence | BIM/IFC identity | Inspection record | Action/status record | Competency questions | Constraint validation | Failure tests | Main limitation | Access/Classification |
|---|---|---|---|---|---|---|---|---|---|
| Hüthwohl, Brilakis, Borrmann & Sacks (2018), *J. Comput. Civ. Eng.* 32(3), DOI 10.1061/(ASCE)CP.1943-5487.0000744 [^9] | No sensor data; defect imagery from manual inspection manuals | IFC4-based entities `IfcMeasuredRegion`, `IfcDegradation`, `IfcDegradationElements` bound to bridge elements | Yes — core contribution: standardized defect/inspection information model | No explicit maintenance/work-order record | Not pre-registered; three-step derivation (manual→entity→IFC mapping) | Prototype implementation as proof of concept | Not reported | No sensor/condition-monitoring linkage at all; inspection-to-IFC only | Full text reviewed. METHODOLOGICAL EVIDENCE (inspection-BIM layer only) |
| Xu, Wang, Wang, Wu, Shou & Liu (2022), *J. Comput. Civ. Eng.* 36(4), DOI 10.1061/(ASCE)CP.1943-5487.0001026 [^10] | No live sensor; parametric defect geometry from inspection data | IFC-based parametric defect entities linked to bridge elements, root causes | Yes — defect/inspection representation | Yes — explicit "maintenance actions" entity linked to defects | Not stated | Motorway bridge case demonstration | Not reported | No condition-monitoring/sensor evidence; static inspection-to-repair chain only | Abstract/metadata reviewed. STRONG ADJACENT |
| Lee, Eastman & Solihin (2021), *J. Comput. Des. Eng.* 8(1), 97–114, DOI 10.1093/jcde/qwaa064 [^11][^8] | No sensor/condition evidence | Rule-based GUID/GlobalId validation for IFC/COBie exchange | Not an inspection-record model; validation rules for data exchange | Not addressed | Not stated | Rule-based validation logic; file-level GUID uniqueness checks | Formal rule-conformance testing, not field trial | Strong on identity validation, weak on inspection/maintenance linkage | Full text reviewed (via citing document). METHODOLOGICAL EVIDENCE (identity-validation layer) |
| Heaton, Parlikad & Schooling / Heaton & Parlikad (2020), *IFAC-PapersOnLine* 53(3), 366–371, DOI 10.1016/j.ifacol.2020.11.059 [^4][^12] | No raw sensor stream modeled; conceptual real-time performance/condition data category | Asset Information Model (AIM) structured per BIM/ISO 19650 classification (UNIClass) | Implicit — AIM intended to support O&M records | Implicit — supports Digital Twin/predictive-maintenance direction, not an explicit action-status schema | Not stated | West Cambridge case-study demonstrator | Not reported | Conceptual AIM structuring; no explicit sensor→component→inspection→action data model or validation | Full text reviewed. STRONG ADJACENT (AIM/DT framing, not the locked chain) |
| Lu, Xie, Parlikad, Schooling et al. (2020), *Automation in Construction* 118, 103277 [^13][^14] | Yes — real sensor/condition monitoring feed (cooling pumps, West Cambridge DT pilot) with Bayesian change-point anomaly detection | IFC-based data structure extracting monitoring data tied to asset/BIM objects | Implicit — anomaly flags intended to prompt inspection | Not an explicit maintenance action/work-order record | Not stated | Demonstrator on real cooling-pump assets | Not reported | Strong on sensor-to-BIM anomaly detection; does not close the loop to a formal inspection-record/action-status schema | Abstract/partial full text reviewed. STRONG ADJACENT |
| Antunes, César Júnior, Ribeiro & Franco de Carvalho (2024), *Automation in Construction* 166, DOI 10.1016/j.autcon.2024.105650 [^7] | Not sensor-focused; concerns IFC schema representation for project data | IFC interoperability data-schema analysis for project representation | Not the paper's focus (per available metadata) | Not addressed (per available metadata) | Not stated | Not stated | Not stated | Metadata-only access; cannot confirm inspection/maintenance content — do not use for detailed methodological claims | Metadata only. Classification pending full-text confirmation |
| Kim, K., Kim, H., Kim, W., Kim, C., Kim, J. & Yu, J. (2018), *Automation in Construction* 87, 173–187 [^8] | Not confirmed — title indicates FM work-information integration via Semantic Web, not sensor/condition evidence | IFC object integration with facility-management work information (Semantic Web) | Plausible — FM "work information" likely includes inspection/work-order records, but not confirmed at full-text level | Plausible — same caveat | Not stated | Not stated | Not stated | Metadata-only; full text not retrieved in this session — cannot confirm sensor-evidence linkage | Metadata only. Access insufficient for methodological claims |
| Deng et al. (2022) — threshold-warning/element-ID localization (per project evidence base) [^2] | Yes — sensor-triggered threshold warnings | Element-ID-localized (BIM-linked) warning | Inspection trigger, not full inspection record | Not explicit action/work-order record | Not stated | Not stated in available extraction | Not stated | Inspection trigger only; incomplete action-status closure | Per project's prior full-text review. DIRECT EVIDENCE (partial chain) |
| Li et al. (2023) — defect/condition/repair record structures (per project evidence base) [^2] | Not sensor-native; condition scores as input | Not the paper's core focus per extraction | Yes — defect/condition record structures | Yes — repair-record structures | Not stated | Not stated | Not stated | Record-structure precedent without confirmed sensor-to-BIM linkage in one paper | Per project's prior full-text review. STRONG ADJACENT (record layer) |
| Chen et al. (2014) — SHM management decision-support architecture (per project evidence base) [^2] | Yes — SHM data feeding decision support | Not confirmed as IFC/BIM-native | Implicit decision/inspection triggers | Decision-support architecture, not granular action-status field | Not stated | Not stated | Not stated | Architecture-level, not a component-level traceability schema | Per project's prior full-text review. BACKGROUND REVIEW |

## Which studies connect sensor/condition-monitoring results with BIM/IFC components AND inspection records?

Within the searched sources and databases, no single peer-reviewed study **simultaneously and formally** links (a) sensor-derived condition/state-change evidence, (b) a BIM/IFC component identity, and (c) a structured inspection record in one validated data model. The closest partial matches split across two clusters:

- **Sensor-to-BIM anomaly detection without formal inspection-record schema**: Lu, Xie, Parlikad, Schooling et al. (2020) demonstrate an IFC-based data structure carrying diagnostic monitoring data from a real asset (cooling pumps, West Cambridge Digital Twin pilot) with Bayesian anomaly detection. This is the strongest verified sensor+BIM pairing found, but the paper's own account stops at anomaly flagging — it does not formalize a downstream inspection record or maintenance-action-status field.[^13][^14]
- **Inspection-to-BIM/IFC defect models without sensor/condition-monitoring input**: Hüthwohl et al. (2018) and Xu et al. (2022) formalize inspection/defect information as IFC entities bound to bridge elements, and Xu et al. add an explicit maintenance-action entity. Neither paper ingests sensor or condition-monitoring evidence — their "evidence" originates from manual inspection manuals, not vibration or condition-monitoring data streams.[^9][^10]

No verified source in this search combines both halves of the chain end-to-end with an explicit identifier schema (e.g., Sensor_ID → BIM_GUID → Inspection_Record_ID).

## Which studies also include maintenance actions, work orders, recommended inspections, or status history?

Xu et al. (2022) is the only study in this batch with an explicit "maintenance action" entity formally connected to defect/inspection entities inside the IFC schema. Lee, Eastman & Solihin (2021) contribute rule-based validation for BIM/COBie data exchange, which is a prerequisite governance layer for reliable work-order data but is not itself a maintenance-action or status-history model. Within the project's own prior full-text extraction, Li et al. (2023) is recorded as providing "defect/condition/repair record structures," which is the nearest maintenance-record precedent identified to date, though not independently re-verified in this session.[^2][^8][^10][^11]

## Closest competitor to a formal component-level evidence-to-action traceability framework

Within the searched sources and databases, **no single study is a full competitor** to a formal, identifier-based, component-level evidence-to-action traceability framework spanning sensor evidence → BIM/IFC component → inspection record → maintenance action. The **closest partial competitor**, when the chain is assessed as a whole, is **Lu, Xie, Parlikad, Schooling et al. (2020)**, because it is the only verified source pairing a real sensor/condition-monitoring feed with an IFC-based data structure at the component level inside an operating Digital Twin pilot. It falls short of full competitor status because it does not formalize an inspection-record entity or a maintenance-action/status-history schema — the anomaly output is not shown closing the loop into a governed inspection or action record.[^14][^13]

On the inspection-and-maintenance side of the chain, **Xu et al. (2022)** is the closest competitor for the downstream half (IFC-formalized defect → inspection → maintenance-action linkage), but it lacks any sensor or condition-monitoring input, relying instead on manually reported inspection data.[^10]

No reviewed source combines both strengths in one validated framework — this is consistent with, but does not by itself prove, a literature gap; it reflects only what was found within the searched sources and databases in this session.

## What has already been established (cannot be claimed as novel)

- IFC-based formalization of inspection/defect information bound to bridge/BIM components, including dedicated entities for measured regions and degradation, is established (Hüthwohl et al. 2018; Xu et al. 2022).[^9][^10]
- An explicit maintenance-action entity linked to IFC-modeled defects is established (Xu et al. 2022).[^10]
- Rule-based validation of IFC/COBie GUID and data-exchange integrity is established (Lee, Eastman & Solihin 2021).[^8][^11]
- Real-time sensor/condition-monitoring data structured through an IFC-based schema and used for anomaly detection at the component level in an operating Digital Twin pilot is established (Lu, Xie, Parlikad, Schooling et al. 2020).[^13][^14]
- BIM object GUID plus a separate human-readable Asset Identification Number as the governance pattern for linking BIM, COBie, and CMMS/FM systems is established in normative FM guidance, per the project's own IFC GlobalId governance report.[^3]
- Conceptual Asset Information Model (AIM) structures intended to support Digital Twin-enabled O&M are established (Heaton & Parlikad 2020).[^12][^4]

## Candidate gap remaining

Within the searched sources and databases, the candidate gap is the **absence of a single validated, identifier-based data model that traces condition/state-change evidence (sensor-derived) through a BIM/IFC component to a structured inspection record and then to an explicit maintenance/inspection-action status record**, with pre-registered competency questions and constraint-validation testing. Existing work either formalizes the inspection→action half (without sensor input) or the sensor→BIM half (without a formal inspection-record and action-status schema). This candidate gap is stated as an observation from the current search, not as proof that no such study exists anywhere in the literature.

## Strength of evidence

**Weak to Medium.** The sensor-to-BIM anomaly-detection evidence (Lu et al. 2020) is Medium strength — it is a real case-study demonstrator on live assets but was reviewed only via abstract/secondary citation in this session, not full text. The inspection-to-BIM/maintenance-action evidence (Xu et al. 2022; Hüthwohl et al. 2018) is Medium strength — case-study/prototype validated but reviewed at abstract/metadata level in this session. The two unresolved seed studies (Çelik et al. 2022; Johannes et al. 2021) and the uncertain matches for "Lorvão Antunes et al. 2024" and "Kim et al. 2018" are **Weak** — metadata-only or unverified, and must not be used to support detailed methodological claims until full text is obtained.[^14][^9][^10][^13]

## Full texts that must be read next

- Lu, Q., Xie, X., Parlikad, A.K., Schooling, J.M. (2020). "Digital twin-enabled anomaly detection for built asset monitoring in operation and maintenance." *Automation in Construction*, 118, 103277 — full text required to confirm whether any inspection-record or maintenance-action schema follows the anomaly-detection step.[^13]
- Xu, S., Wang, J., Wang, X., Wu, P., Shou, W., Liu, C. (2022). "A Parameter-Driven Method for Modeling Bridge Defects through IFC." *J. Comput. Civ. Eng.*, 36(4), DOI 10.1061/(ASCE)CP.1943-5487.0001026 — full text required to verify the maintenance-action entity's structure and any status-history mechanism.[^10]
- Kim, K., Kim, H., Kim, W., Kim, C., Kim, J., Yu, J. (2018). "Integration of IFC objects and facility management work information using Semantic Web." *Automation in Construction*, 87, 173–187 — full text required to confirm/deny this is the intended seed study and whether it contains sensor/condition evidence.[^8]
- Antunes, M.L.R., César Júnior, K.M.L., Ribeiro, J.C.L., Franco de Carvalho, J.M. (2024). "Analysis of IFC interoperability data schema for project representation." *Automation in Construction*, 166, DOI 10.1016/j.autcon.2024.105650 — full text required to confirm author-name match to "Lorvão Antunes et al." and to assess inspection/condition-evidence content.[^7]
- Lee, Y.C., Eastman, C.M., Solihin, W. (2021). "Rules and validation processes for interoperable BIM data exchange." *J. Comput. Des. Eng.*, 8(1), 97–114, DOI 10.1093/jcde/qwaa064 — full text required beyond the secondary-citation excerpt already reviewed.[^11]
- Targeted database search (Scopus/Web of Science by exact author string) for "Çelik et al. 2022" and "Johannes et al. 2021" in BIM/IFC/SHM/asset-management venues — neither could be located in this session and both require direct resolution before further use.

---

## References

1. [reports/condition_evidence_literature_review.md](reports/condition_evidence_literature_review.md)

2. [LIVING_EVIDENCE_BASE_v1.1_LIMITED_FEM.md](LIVING_EVIDENCE_BASE_v1.1_LIMITED_FEM.md)

3. [RESEARCH_ARCHITECTURE.md](RESEARCH_ARCHITECTURE.md)

4. [ifc_globalid_traceability_report.md](ifc_globalid_traceability_report.md)

5. [MASTER_RESEARCH_CHARTER_v1.1_LIMITED_FEM_20260717.md](MASTER_RESEARCH_CHARTER_v1.1_LIMITED_FEM_20260717.md)

6. [From BIM towards digital twin: Strategy and future development for smart asset management](https://discovery.ucl.ac.uk/id/eprint/10082757/) - UCL Discovery is UCL's open access repository, showcasing and providing access to UCL research outpu...

7. [Asset Information Model to support the adoption of a Digital Twin: West Cambridge case study](https://www.sciencedirect.com/science/article/abs/pii/S2405896320302093)

8. [Digital Twin and BIM synergy for predictive maintenance in ...](https://wjarr.com/sites/default/files/fulltext_pdf/WJARR-2020-0409.pdf)

9. [parametrização e modelagem de - Portal Gov.br](https://www.gov.br/dnit/pt-br/assuntos/planejamento-e-pesquisa/ipr/relatorios-de-pesquisa-1/ipr_rp_024_parametrizacao_e_modelagem_de_danos_em_sge_parte_3.pdf)

10. [Digital Twins implementation in Operations and Maintenance ...](https://projekter.aau.dk/projekter/files/413238078/Final_Thesis_000.pdf)

11. [BIM-based design and setup of structural health monitoring systems](https://www.sciencedirect.com/science/article/pii/S0926580523005058)

12. [Application of Building Information Modelling (BIM) in the Health Monitoring and Maintenance Process: A Systematic Review](https://www.mdpi.com/1424-8220/21/3/837?type=check_update&version=2) - Improvements in the science of health monitoring and maintenance have facilitated the observation of...

13. [Condition Information Models in the context of Structural ...](https://onlinelibrary.wiley.com/doi/abs/10.1002/cepa.2069)

14. [4.1. 4. Using Bim For...](https://pmc.ncbi.nlm.nih.gov/articles/PMC7866213/) - Improvements in the science of health monitoring and maintenance have facilitated the observation of...

