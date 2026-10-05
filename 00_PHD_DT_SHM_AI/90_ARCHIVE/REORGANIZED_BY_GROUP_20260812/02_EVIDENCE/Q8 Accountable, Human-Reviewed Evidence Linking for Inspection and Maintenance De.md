## Scope and Purpose

This synthesis addresses the evidence base for an accountable, human-reviewed workflow that links condition evidence (sensor data, inspection findings, defect reports) to inspection actions and maintenance decisions in BIM, Digital Twin, and asset-management contexts. It is anchored by three studies — Lee, Lee, Masoud, Krishnan and Li (2021), Çelik, Petri and Barati (2022, published in *Computers in Industry* vol. 144, 2023 issue), and Johannes, Voordijk, Adriaanse and Aranda-Mena (2021) — and extends outward to the broader accountability, provenance, and human-in-the-loop literature.[^1][^2][^3]

## Anchor Studies: Verification and Full-Text Status

**Lee et al. (2021)** — "Integrated digital twin and blockchain framework to support accountable information sharing in construction projects," *Automation in Construction*, 127, 103688. DOI: 10.1016/j.autcon.2021.103688. Open-access PDF available via University of Michigan repository. The paper defines accountability operationally as the traceability and immutability of data transactions across a digital twin, achieved by recording IoT-sourced updates with blockchain timestamps so "any information can be shared securely and transparently," making information sharing accountable. It was tested on a prefabricated-brick positioning case, not a full inspection-to-work-order pipeline.[^4][^1]

**Çelik, Petri and Barati** — "Blockchain supported BIM data provenance for construction projects," *Computers in Industry*, 144, 103768 (received 17 May 2022, accepted 15 August 2022; journal-dated 2023). DOI: 10.1016/j.compind.2022.103768. Full text on ScienceDirect and Cardiff University ORCA repository. This paper is explicitly framed around **provenance**, not accountability per se: it records BIM object metadata — issuing discipline, object version, and "responsibility/liability associated with the data" — on an Ethereum test network with a Window-of-Latching model to verify accuracy, integrity, and timeliness of records. It gives stakeholders confidence and recognizes "levels of competence," tested on a real-world bridge construction scenario, with a cost analysis of blockchain overhead.[^5][^2]

**Johannes et al. (2021)** — "Identifying Maturity Dimensions for Smart Maintenance Management of Constructed Assets: A Multiple Case Study," *Journal of Construction Engineering and Management*, 147(9), 05021007. DOI: 10.1061/(ASCE)CO.1943-7862.0002112. Full text via University of Twente repository (open access). This is a maturity-model study, not a technical accountability framework: it derives a smart-maintenance maturity framework with technological dimensions (tracking and tracing) and behavioral/organizational dimensions (culture, allocation of responsibilities for predictive maintenance and dispersed data sets), validated through cross-case coding and **expert consultation**.[^3]

## Comparative Evidence Table

| Study | Accountability definition | Evidence linkage | Human role | Approval process | Audit trail | Technology | Validation method | Limitation |
|---|---|---|---|---|---|---|---|---|
| Lee et al. (2021)[^1][^4] | Traceable, immutable, transparent information sharing across stakeholders in a digital twin | IoT sensor updates → BIM/digital twin state, timestamped on blockchain | Not the focus; stakeholders are data recipients, not decision approvers | Not modeled — blockchain records transactions, not human sign-off | Yes — blockchain ledger of timestamped data transactions | Digital twin + private blockchain + IoT | Single case project (prefab brick positioning tracking) | No inspection/maintenance decision loop; no reviewer/approver roles; small-scale demonstration, not organizational deployment |
| Çelik et al. (2022/2023)[^5][^2][^6] | Not directly defined; treated as adjunct to "provenance" — trust, transparency, and traceable responsibility/liability assignment | BIM object modification history (who created/modified, version, discipline) recorded per transaction | Stakeholders as data contributors; no explicit reviewer/approver workflow | Not modeled — smart contract records provenance, no described human approval gate | Yes — blockchain transaction log of BIM object provenance | Ethereum test network, smart contracts, Window-of-Latching model | Bridge-construction case study + cost/gas analysis | Provenance ≠ accountability for decisions; no linkage to inspection findings, work orders, or maintenance actions; cost/scalability concerns noted |
| Johannes et al. (2021)[^3] | Not a technical data-accountability definition; organizational construct — "allocate responsibilities" for maintenance programs and data ownership as a maturity dimension | Not a data-linkage model; addresses whether organizations track/trace condition data across lifecycle as maturity indicator | Central — behavioral/cultural dimensions capture human responsibility allocation, decision ownership, expertise | Implied via organizational governance maturity, not a documented digital approval workflow | Partial — "tracking and tracing" is one maturity dimension, not an implemented audit-trail mechanism | None specific — technology-agnostic maturity framework | Multiple case study + expert consultation for framework validation | Framework is diagnostic/maturity-oriented, not a working information system; no metadata schema or workflow specification |
| Li et al. (blockchain/BIM/IoT/DAO for maintenance)[^7] | Not stated as accountability; framed as improved traceability and record-keeping | Sensor/condition data → smart contract trigger for semi-automated maintenance | Explicit human confirmation step: "work has been done satisfactorily" before DAO releases payment | Human confirmation gates payment release/status update in CAFM | Yes — DLT-based record keeping of maintenance/repair activities | BIM + IoT + DLT + smart contracts + DAO + CAFM | Not detailed in available excerpt (conceptual/proposal-level) | Semi-automated, not autonomous; human check limited to task completion confirmation, not diagnostic judgment |
| Tavakoli & Yitmen (blockchain DT provenance for predictive asset management)[^8] | Not defined; framed as data reliability/trustworthiness via provenance (origin, ownership, lineage) | Structured asset data + AIM maintained via blockchain-based DT for PAM decision support | Specialists/stakeholders use provenance record to inform PAM decisions | Not an approval workflow; enables decentralized apps (DApps) to publish real-time O&M data | Yes — immutable record of data origin/ownership/lineage | Blockchain-based digital twin | Not detailed in excerpt; presented as proposed/developed model | Provenance improves trust in inputs to PAM, but does not itself constitute a human-review or accountability chain for actions taken |
| Zhong et al. review (2023–24) of BC-BIM accountability/provenance literature[^9] | Synthesizes accountability as transparency + fraud prevention + traceability of asset maintenance records via blockchain/smart contracts | Cites "automated maintenance operations" linked to condition/maintenance records (Lee et al. 2021; Ye et al. 2022) | Not detailed at synthesis level | Not detailed at synthesis level | Yes, per synthesized sources | Blockchain + smart contracts + BIM | Literature review — no primary validation | Review-level claims of "automated maintenance operations" risk overstating autonomy of underlying primary studies |
| Kamal et al. (2022) BIM-based hospital work-order management[^10] | Not an accountability study; optimization of repair/maintenance work orders | BIM + Genetic Algorithm + Discrete Event Simulation optimizes R&M schedules from condition/maintenance needs | Managers' preferences/constraints are direct optimization inputs; human sets constraints | Manager approval of schedule implied, not modeled formally | Not a focus | BIM, AR, GA, DES | Real case study application | No accountability metadata (creator/reviewer/approver fields); optimization-focused, not audit-trail focused |
| Effects of BIM/COBie on work-order processing (2019, ASCE JPCF)[^11] | Not an accountability study | COBie/BIM data linked to CMMS work orders empirically | FM staff process work orders; role unspecified in metadata terms | Not modeled | CMMS logs exist but standardization "lacking" | BIM, COBie, CMMS | Statistical two-sample t-test on real CMMS export data | Found no significant work-order time improvement from BIM/COBie; highlights lack of standardized recording rules across sites — a direct gap in auditable metadata |

## How Accountability Is Currently Defined Across the Literature

Across BIM and digital twin research, "accountability" is used loosely and inconsistently, most often operationalized as **traceability plus immutability plus transparency** of data transactions rather than as a formal responsibility-assignment or liability construct. Lee et al. (2021) is the most explicit: accountability is achieved when data transactions are securely and transparently shared and auditable end-to-end via blockchain-recorded, timestamped transfers between the physical asset (via IoT), the digital twin, and stakeholders. Related blockchain-BIM literature frames accountability similarly — as a byproduct of a "transparent record of all activities" that supports "task delegation and accountability" in multi-stakeholder projects, and as fraud prevention, authenticity, and increased trust in transaction data. Johannes et al. (2021), by contrast, treats accountability as an organizational-maturity construct: whether responsibilities for maintenance programs, predictive maintenance, and dispersed data ownership have been explicitly "identified" and "allocated," independent of any specific IT system.[^6][^9][^1][^3]

This split matters for the thesis: one stream of literature equates accountability with a technical audit trail (who touched what, when), while another stream equates it with organizational responsibility allocation (who is answerable for a decision). A defensible thesis position should state both are necessary but distinct — the technical trail supports the organizational accountability, but does not constitute it on its own.

## Required Metadata Fields and Their Evidentiary Support

The query asks which metadata are required to determine creator, reviewer, approver, status-changer, and timing/reason of change. The strongest formal grounding for this comes not from the three anchor construction papers directly, but from provenance standards literature that the BIM-blockchain papers implicitly draw on:

- **W3C PROV-O** formally defines Entity, Activity, and Agent classes with relations such as `wasGeneratedBy`, `wasAttributedTo`, and `wasAssociatedWith`, giving a rigorous vocabulary for "who created," "using what process," and "from which inputs".[^12][^13][^14]
- **PAV (Provenance, Authoring and Versioning) ontology** extends PROV-O to distinguish `pav:authoredBy` (original creator), `pav:createdBy` (digital record creator), `pav:curatedBy` (reviewer/validator), and `pav:contributedBy`, plus versioning fields (`pav:version`, `pav:previousVersion`) — this maps closely onto the thesis's need for "who created" vs. "who reviewed" as separate, non-conflated roles.[^15][^16]
- Çelik et al. record BIM object metadata including issuing discipline, object version, and responsibility/liability attribution per blockchain transaction — an applied, partial instance of provenance metadata in the construction domain, but without explicit reviewer or approver fields.[^2]
- Lee et al. record timestamped transaction data on the blockchain (who/when for data updates) but do not define a reviewer or approver metadata schema — their "accountability" is transactional traceability, not decision governance.[^1]
- Industry/practitioner literature on digital twin traceability explicitly calls for capturing "who/what/when" for every record and transformation, and distinguishes lineage (path of transformations) from traceability (lineage plus proof of approval and supporting documentation).[^17]

**Conclusion on metadata**: creator and timestamp fields are strongly evidenced (blockchain transaction logs, PROV-O `wasGeneratedBy`/`wasAttributedTo`). Reviewer/curator fields are evidenced at the ontology level (PAV `curatedBy`) but only weakly instantiated in the specific BIM-blockchain case studies. Formal "approver of inspection action" and "who changed action status, and why" fields are **not directly evidenced** in any of the three anchor studies or their closest relatives — this is a genuine gap the thesis would need to address as a proposed contribution rather than cite as established practice.

## Studies Linking Condition/Inspection Data to Work Orders or Decisions

Several works explicitly connect condition or inspection evidence to maintenance actions, though with varying rigor:

- Kamal, Taghaddos and Metvaei (2022) integrate BIM, a genetic algorithm, and discrete-event simulation to optimize hospital repair-and-maintenance work-order scheduling from condition/maintenance needs, validated on a real case study, though it emphasizes optimization over auditability.[^10]
- The 2019 ASCE JPCF study statistically tested whether BIM/COBie data affects work-order processing time using real CMMS export data across multiple hospital campuses, finding no significant improvement and explicitly attributing this to a lack of standardized recording rules for work-order data — itself indirect evidence that metadata standardization, not just data linkage, determines system-level value.[^11]
- Industry CMMS comparative reviews (UpKeep, Limble CMMS, Fiix) describe inspection-to-work-order pipelines with photo evidence and completion tracking as commercial best practice, though these are vendor/product descriptions rather than peer-reviewed validation.[^18]
- Tavakoli and Yitmen's blockchain-DT provenance model for predictive asset management (PAM) is presented as informing PAM decision-making by improving data reliability, but the excerpt available does not describe a formal work-order or job-tracking schema.[^8]
- Li et al.'s DAO-based framework is the clearest primary-source example of inspection/condition data triggering a maintenance action with an explicit human-confirmation gate before smart-contract-driven payment release and CAFM status update — this is the strongest evidence base for a human-reviewed, evidence-to-action linkage found in this search, and should be central to the thesis's methodological justification.[^7]

## How Human Review Is Evaluated in This Literature

Evaluation methods vary widely and rarely target the specific "human review of an inspection decision" step the thesis is concerned with:

- **Expert consultation / expert validation**: Johannes et al. (2021) validate their maturity framework through expert consultation following multi-case coding — the clearest "expert review" methodology among the anchor studies.[^3]
- **Case-study demonstration with practitioner feedback**: Several BIM-CMMS integration papers (e.g., BIM3R for facilities maintenance) report "positive comments" from industrial partners in pilot studies, which is a lighter-weight form of qualitative validation than structured expert review.[^19][^20]
- **Interviews and semi-structured qualitative methods**: studies on digital twin adoption in facility management (e.g., NTNU thesis on DT in FM) use semi-structured interviews with experts to surface organizational challenges, a pattern relevant to evaluating human-review protocols but not focused on inspection/maintenance decisions specifically.[^21]
- **Formal usability testing or scenario-based evaluation of a human reviewer's workflow for condition-evidence-to-action decisions was not found** in the anchor studies or their close derivatives. This is a genuine gap: Lee et al. and Çelik et al. validate the *technical* framework (traceability, cost, correctness of blockchain transactions), not the *human review process* around it.[^2][^1]
- A published human-in-the-loop survey for infrastructure visual inspection systematically reviews automation-enabled HITL inspection approaches, providing the closest topical match for how such review might be formally evaluated in future work, though it is a review paper rather than new empirical validation.[^22]

This indicates that "human review" of inspection/maintenance decisions in this domain is currently evaluated indirectly — via organizational maturity assessment, practitioner feedback in pilots, or qualitative interviews — rather than via controlled usability studies of the review interface or decision protocol itself.

## Accountability vs. Provenance vs. Auditability vs. Legal Liability

These four terms are frequently conflated in the literature but are conceptually distinct:

- **Provenance** is the documented history of an entity's origin and transformations — "the surveillance chronology of an object," per Çelik et al., encompassing who created/modified data, when, and through what process. The W3C PROV framework formalizes this as records of "people, institutions, entities, and activities involved in producing, influencing, or delivering a piece of data".[^14][^23][^5]
- **Auditability** is the practical capacity to inspect that provenance record after the fact to verify what happened — it depends on provenance existing but adds the requirement of retrievability and completeness for review (e.g., blockchain ledgers enabling "seamless" inspections and audits).[^24]
- **Accountability**, in this literature, is generally used to mean that responsibility for an action or data change can be traced to a specific agent — a combination of provenance and organizational responsibility allocation (Johannes et al.'s "allocate responsibilities"). It does not, in these papers, imply legal consequence.[^1][^3]
- **Legal liability** is a distinct, narrower concept involving formal legal responsibility and consequence, and is only occasionally invoked — Çelik et al. mention recording "responsibility/liability associated with the data" as blockchain metadata, but this is a data-attribution field, not a demonstrated legal mechanism or contractual liability framework. None of the three anchor studies provide legal evidence, case law, or regulatory analysis; a 2025 paper on digital twins under EU law is the only source found that directly engages legal compliance obligations for audit trails and provenance, and it addresses regulatory requirements rather than construction-project liability specifically.[^25][^5][^2]

**Recommendation for the thesis**: state explicitly that "accountability" as used should mean traceable responsibility and information history — who did what, when, and reviewable by whom — and that this is analytically distinct from legal liability, which would require contract law, tort, or regulatory evidence not present in this technical literature.

## Is Blockchain Necessary, or One Implementation Option?

The literature treats blockchain as one implementation mechanism for achieving traceability/provenance, not as a necessary condition for accountability. Lee et al. and Çelik et al. both use blockchain specifically to add immutability and decentralized trust to data that could, in principle, be tracked by other means (e.g., versioned databases, digital signatures, centralized audit logs). Reviews of blockchain-BIM integration explicitly frame blockchain's value as improving traceability, security, and trust relative to file-based or centralized systems, implying it is a chosen solution among alternatives, motivated by multi-stakeholder trust problems rather than a technical requirement for provenance itself. The PROV-O/PAV provenance ontologies are blockchain-agnostic and can be implemented in conventional databases. Cost-analysis sections in Çelik et al. (Ethereum gas cost accounting) further indicate blockchain introduces real overhead, reinforcing that it is a design choice with trade-offs rather than an inherent necessity.[^26][^27][^13][^15][^2][^1]

**Conclusion**: blockchain is a plausible, evidenced implementation option for immutable audit trails, but the thesis should not claim it is required — conventional access-controlled, versioned, digitally-signed databases can satisfy the same accountability requirements, and this should be stated as a design decision justified by trust/decentralization needs, not as a technical mandate.

## Studies Supporting Asset–Condition–Inspection–Job Tracking

The most directly relevant chain-of-evidence studies are: Li et al.'s DAO/CAFM framework for semi-automated maintenance triggered by condition data with human confirmation; the BIM-based hospital work-order optimization framework linking condition/maintenance needs to scheduled jobs; the COBie/CMMS work-order processing study using real asset-linked work-order data; commercial CMMS platforms (UpKeep, Limble, Fiix) explicitly designed around inspection-to-work-order closure loops with photo evidence and audit trails, cited here as descriptive industry practice rather than peer-reviewed research; and Tavakoli & Yitmen's blockchain-DT provenance model oriented toward predictive asset management decisions. None of these fully implement the specific four-stage "asset–condition–inspection–job" pipeline with formal accountability metadata (creator/reviewer/approver/status-change-reason) in a single system — each covers a subset of the chain, meaning the thesis's integrated framework would be a genuine synthesis contribution rather than a replication of prior work.[^8][^7][^10][^11][^18]

## Claims That Would Incorrectly Imply Autonomous Maintenance

Based on the language actually used in primary sources versus secondary syntheses, the thesis must avoid the following overstatements:

- Describing blockchain/smart-contract systems as performing "automated maintenance operations" without qualification — this phrase appears in a review synthesis but the underlying primary source (Lee et al. 2021) demonstrates only data traceability, not automated decision-making or execution of maintenance work.[^9][^1]
- Implying that Li et al.'s DAO framework executes maintenance autonomously — the source explicitly requires human confirmation that "work has been done satisfactorily" before any smart-contract payment release or status update occurs; it is semi-automated with a human gate, not autonomous.[^7]
- Claiming that any of the three anchor studies validate an end-to-end automated pipeline from condition sensing to maintenance action without human judgment — none of them test or claim this; Lee et al. validate data traceability on a single tracked component, Çelik et al. validate BIM data provenance recording, and Johannes et al. validate an organizational maturity model, not a technical automation system.[^2][^3][^1]
- Using "human-in-the-loop" AI framing that implies AI handles "routine maintenance decisions autonomously" with humans only intervening on exceptions — this operating model is described in current industry/vendor material (2026) as an aspirational or product framing, not as a peer-reviewed, validated finding applicable to the thesis's inspection-decision context.[^28]
- Presenting provenance metadata (who touched data, when) as equivalent to "the system decided" — provenance records what happened to data; it says nothing about the correctness or automation of a maintenance decision itself.

## Assessment of Evidence Strength

**Strong evidence** (directly demonstrated in peer-reviewed primary sources): data traceability and timestamped transaction logging via blockchain in a digital twin context; BIM object-level provenance metadata (creator, discipline, version) recorded via blockchain in a real case study; organizational maturity dimensions for allocating maintenance responsibilities, validated by expert consultation; formal provenance ontology definitions (PROV-O, PAV) for creator/curator/version metadata, though not domain-specific to construction.[^13][^15][^3][^1][^2]

**Indirectly supported** (inferred from adjacent or partial studies, not directly tested together): linkage of condition/inspection evidence to work orders (evidenced separately in hospital BIM-CMMS optimization and COBie/CMMS studies, but not combined with accountability metadata); human-confirmation gating of maintenance actions (evidenced in Li et al.'s DAO proposal, but at a conceptual/proposal level without reported empirical validation); the specific claim that blockchain-based provenance improves stakeholder trust and reduces risk contingencies (asserted across multiple review papers, but based on case demonstrations and cost analyses rather than controlled comparative studies).[^26][^10][^11][^7][^2]

**Remaining thesis hypotheses** (not evidenced in the literature reviewed and requiring the thesis's own contribution or validation): a unified metadata schema explicitly capturing "who reviewed," "who approved an inspection action," "who changed action status," and "why," integrated across asset–condition–inspection–job stages; a validated human-review protocol (with usability testing or scenario evaluation) specifically for inspection/maintenance decision approval, as distinct from organizational maturity assessment or general practitioner feedback; and any formal linkage between the technical accountability trail and legal liability in a construction/FM context.

## A Human-Review Protocol Framework Relevant to Thesis Gate "G5"

Drawing on the maturity-framework, provenance-ontology, and HITL-survey evidence gathered, a defensible human-review protocol for a gate such as "G5" (condition evidence → approved inspection/maintenance action) would combine: (1) a PAV/PROV-O-style metadata schema recording `createdBy` (evidence record originator), `curatedBy` (reviewer who validated the evidence), an explicit `approvedBy` field for the inspection/maintenance action distinct from the reviewer, a `statusChangedBy` and `statusChangeReason`/timestamp field for any subsequent action-status update; (2) routing logic that escalates only uncertain or high-consequence findings to human reviewers rather than requiring blanket manual review of every record, consistent with confidence-threshold-based human-in-the-loop practice described in visual-inspection HITL research; and (3) validation of the review protocol itself through expert consultation or facility-manager interviews, following the precedent set by Johannes et al.'s maturity-framework validation approach, supplemented by scenario-based or usability testing of the reviewer interface, since no anchor study directly validated a human-review interface for this exact decision point.[^22][^15][^13][^3]

## What Must Not Be Claimed

The thesis should explicitly state it does **not** claim: that maintenance decisions are made autonomously by the system; that blockchain is a required (versus chosen) technology for achieving accountability; that provenance metadata alone constitutes proof of correct decision-making; or that the accountability framework establishes legal liability, contractual responsibility, or regulatory compliance in any jurisdiction, absent direct legal evidence such as contract clauses, statutes, or case law specific to the asset-management context. Accountability, as supported by this literature, should be presented strictly as traceable responsibility and information history — a record of who created, reviewed, approved, or changed a given piece of evidence or action, and when — not as a legal or automated-decision-making claim.[^25][^2]

---

## References

1. [Integrated digital twin and blockchain framework ... - ACE-MRL](http://acemrl.engin.umich.edu/wp-content/uploads/sites/412/2021/04/Lee-digital-construction.pdf) - viết bởi D Lee · 2021 · Trích dẫn 559 bài viết — Integrated digital twin and blockchain framework. D...

2. [Blockchain supported BIM data provenance for construction projects](https://www.sciencedirect.com/science/article/pii/S0166361522001646) - The management of construction projects requires adequate techniques to support the continual exchan...

3. [Identifying Maturity Dimensions for Smart Maintenance Management of Constructed Assets: A Multiple Case Study](https://ris.utwente.nl/ws/portalfiles/portal/264321856/Johannes_2021_Identifying_maturity_dimensions_for.pdf)

4. [2021 European Conference on Computing in Construction](https://arxiv.org/ftp/arxiv/papers/2106/2106.11030.pdf)

5. [[PDF] Blockchain supported BIM data provenance for construction projects](https://orca.cardiff.ac.uk/id/eprint/152310/7/1-s2.0-S0166361522001646-main.pdf)

6. [A Novel Framework for Integrating](https://orca.cardiff.ac.uk/id/eprint/174651/1/Thesis_YasinCelik.pdf)

7. [Blockchain and BIM (Building Information Modeling)](https://arxiv.org/pdf/2104.00547.pdf)

8. [Blockchain-based digital twin data provenance for predictive asset management in building facilities](http://hj.diva-portal.org/smash/record.jsf?pid=diva2:1816800) - Purpose: The purpose of this study is to focus on structured data provision and asset information mo...

9. [Construction Innovation: Information, Process, Management](https://irep.ntu.ac.uk/id/eprint/49512/1/1789554_Zhong.pdf)

10. [BIM-based repair and maintenance for hospital work order management](https://www.sciencedirect.com/science/article/abs/pii/S0926580522004174) - Work order management in hospitals that are dynamic and high-pressured environments is a significant...

11. [Effects of BIM and COBie Database Facility Management on Work Order Processing Times: Case Study | Journal of Performance of Constructed Facilities | Vol 33, No 6](https://ascelibrary.org/doi/abs/10.1061/(ASCE)CF.1943-5509.0001333) - AbstractThis study investigates the effects of using building information modeling (BIM) and constru...

12. [PROV-O - Open Neuroscience Graph](https://openneuroscience.org/Standards/PROV-O) - PROV-O — W3C Provenance Ontology Overview PROV-O is a standard ontology (a shared, formally defined ...

13. [PROV-O: The PROV Ontology](https://www.w3.org/TR/prov-o/) - It provides a set of classes, properties, and restrictions that can be used to represent and interch...

14. [The lifecycle of provenance metadata and its](https://arxiv.org/pdf/1605.01229.pdf)

15. [Provenance, Authoring and Versioning Ontology (PAV ...](https://msi.dublincore.org/standards/pav/) - Tracks provenance, authorship, curation, and version history of resources using lightweight RDF prop...

16. [PAV ontology: provenance, authoring and versioning - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4177195/) - viết bởi P Ciccarese · 2013 · Trích dẫn 145 bài viết — PROV-O provides terms that can be used to tra...

17. [Digital Twin Traceability](https://www.adlibsoftware.com/glossary/digital-twin-traceability) - Learn what digital twin traceability is, why it breaks in handovers, and how to build auditable line...

18. [Best Building Condition Assessment Software (2026)](https://gitnux.org/best/building-condition-assessment-software/) - Compare the top 10 Building Condition Assessment Software tools, including Pareto Facilities, UpKeep...

19. [Collaborative BIM-Based Markerless Mixed Reality Framework for Facilities Maintenance](https://www.academia.edu/85498246/Collaborative_BIM_Based_Markerless_Mixed_Reality_Framework_for_Facilities_Maintenance) - Facilities maintenance tasks require gathering and sharing large amount of information related to fa...

20. [[PDF] The Development of a BIM-enabled Inspection Management System ...](http://www.iaarc.org/publications/fulltext/ISARC2016-Paper206.pdf)

21. [Digital transformation in facility management: An analysis of the challenges and benefits of implementing digital twins in the use phase of a building](https://ntnuopen.ntnu.no/ntnu-xmlui/handle/11250/3068140) - Digital transformation and the adoption of technologies in the AEC-sector can lead to efficiency gai...

22. [A survey of automation-enabled human-in-the-loop ...](https://www.sciencedirect.com/science/article/abs/pii/S0926580518303248)

23. [PROV-O: The PROV Ontology Tutorial - Archivo Digital UPM](https://oa.upm.es/21511/1/DC2013.pdf)

24. [LEVERAGING BLOCKCHAIN TECHNOLOGY IN A BIM ...](https://pdfs.semanticscholar.org/23f1/1d874278d9b52ba9fcd60b6a6eda0793eae6.pdf)

25. [Digital Twins Under EU Law: A Unified Compliance ...](https://www.mdpi.com/2079-9292/14/24/4881) - viết bởi BN Jørgensen · 2025 · Trích dẫn 10 bài viết — Digital Twin operators must ensure audit trai...

26. [Integrating BIM and Blockchain across construction lifecycle and supply chains](https://core.ac.uk/download/558907966.pdf)

27. [When BIM meets blockchain: a mixed-methods literature review](https://pure.bond.edu.au/ws/portalfiles/portal/264300168/When_BIM_meets_blockchain_a_mixed-methods_literature_review.pdf)

28. [What Is Human-in-the-Loop in Facility Management AI?](https://www.xempla.ai/resources/what-is-human-in-the-loop-in-facility-management-ai) - AI handles the routine. Humans handle what matters. See how Xempla keeps FM governance intact withou...

