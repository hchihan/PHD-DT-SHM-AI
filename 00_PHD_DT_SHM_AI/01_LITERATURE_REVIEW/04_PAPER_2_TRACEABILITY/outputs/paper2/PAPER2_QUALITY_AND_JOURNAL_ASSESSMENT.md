# Paper 2: quality, novelty and journal assessment

Manuscript assessed: `PAPER2_MANUSCRIPT_v2_FULL.md` (2026-10-07). Assessor stance: critical journal reviewer. Scores are on a 1–5 scale (3 = acceptable for a Q2 journal after minor/major revision).

## 1 Scientific contribution and novelty

| Criterion | Score | Basis |
|---|---|---|
| Novelty of the problem | 3 | The question (is a component reference in an inspection/maintenance record still valid for the model state that issued it?) is not posed in this form by the 10 Tier-A studies. It is a narrow question. |
| Novelty of the solution | 2.5 | Each element is precedented: GlobalId as key (Fang 2025, Chatsuwan 2025), persistent identity (Borkowski 2026), inspection→maintenance in IFC (Bellon 2025), CQs and rule checks. The new part is the combination and the version-scoped fail-closed rule. A reviewer can call the rule "obvious once stated". |
| Strength of objective evidence | 3 | 759 live elements, hash-identified file, 16 elements with diverging stored/exported identifiers. Real and reproducible, but from one model and one export. Revit-to-IFC re-identification of copied elements may be seen as known exporter behaviour. |
| Strength of evaluation | 2 | Downstream chain records are synthetic; all tests are internal (Level C); the version rule is tested only against a fabricated unregistered version, never against a second real version. |
| Methodological transparency | 4.5 | First-run failures (68/78), lost intermediate run, E1/E2/E3 separation and 12 explicit limitations. This is above the norm in the Tier-A set. |
| Construction-management relevance | 3.5 | Framed as accountability of evidence used in maintenance actions; asset-information governance. No practitioner input or organisational evaluation. |
| Writing and structure | 4 | Clear, bounded claims; consistent terminology. |
| Overall | 3.0 | Publishable in a Q2 applied journal as a case-based method paper; not competitive for top-tier journals (Automation in Construction, Advanced Engineering Informatics) at the current evidence level. |

### Main reviewer objections to expect

1. "The downstream chain is synthetic, so traceability is shown only for data the authors invented." Mitigation: keep the E1/E2/E3 framing and say plainly that the contribution is the identity rule plus the verified logic, not field performance.
2. "Version scoping is never tested on a second real version." This is the weakest point of Contribution 1. Cheapest fix within the frozen scope: a second IFC export of the same registered RVT, which tests GlobalId stability (E2) without new design work. It would need a scope decision from the researcher, because WP2 is frozen.
3. "Rico Thirion et al. (2026) already have persistent component identifiers with IoT and inspection records." The full text has not been read. Read it before submission.
4. "Duplicate stored IfcGUIDs are a known Revit copy/paste artefact." Answer: the cause is not claimed; the finding is that a key taken from the stored parameter would merge 8 pairs, and the rule prevents that.
5. "100 % pass rates on self-written tests." Already handled by reporting 68/78 first.

### Novelty statement that survives review

"A version-scoped identity rule and a sensor-to-action traceability structure with explicit rejection rules, exercised on a real model in which stored and exported IFC identifiers diverge." Do not claim persistence, field validation or decision support.

## 2 Journal selection

Data: OpenAlex source records (2-year mean citedness, h-index, APC), publisher pages and indexer sites retrieved 2026-10-07. Third-party metric sites disagree slightly; treat quartiles as approximate.

| Journal | Fit to topic | Metrics found | APC | Speed | Where competitors published | Verdict |
|---|---|---|---|---|---|---|
| Buildings (MDPI) | High (BIM, FM, digital twins, construction management) | JCR IF 3.1, Q2 (Construction & Building Technology; Civil Eng.); CiteScore 4.4; OpenAlex 2yr citedness 4.22 | CHF 2600 | Median ~15 days to first decision (H1 2025) | Fang 2025, Chatsuwan 2025 | **Primary choice** |
| Journal of Information Technology in Construction (ITcon) | Very high | JCR ~3.8 (Q1, third-party), SJR 0.761 (Q2 Building & Construction, third-party); OpenAlex 2yr citedness 3.72 | None (diamond OA) | Not published; 2–4 reviewers | Jäkel 2025, Otranto 2025, Rogage 2020, Godager 2024 | **Alternative if no APC budget** |
| Construction Innovation (Emerald) | Medium–high | SJR 0.778, Q1 (third-party) | Hybrid, no APC required | Slower | — | Possible; stronger CM framing needed |
| Smart and Sustainable Built Environment | Medium | IF 5.7, Q1 (third-party) | Hybrid | Slower | Tavakoli 2024 | Higher bar; synthetic data a risk |
| Applied Sciences / Infrastructures (MDPI) | Medium | Q2 | CHF ~2400–2900 | Fast | García 2026 | Weaker fit than Buildings |
| Automation in Construction / Adv. Eng. Informatics | High | Q1, 2yr citedness 13.3 / 10.7 | Hybrid | Slow | Bellon, Mariniello, Kim, Ramonell, Kochovski | Not recommended at current evidence level |

Decision: **Buildings (MDPI)**. Reasons: Q2 target agreed for the thesis; two direct competitors were published there in 2025, so the editors and reviewers know the topic; fast first decision. Fallback: ITcon (free, scope fit), then Construction Innovation.

## 3 Formatting applied (MDPI Buildings research article)

Derived from the layout of Buildings 2025 papers read in full (Fang et al. 2025, 15:4096; Chatsuwan et al. 2025, 15:1928), because MDPI's instruction pages blocked automated access (HTTP 403):

- Title in Title Case; authors, affiliations, correspondence.
- Single-paragraph abstract of about 200 words without headings; 3–10 keywords separated by semicolons.
- Sections numbered "1. Introduction", "2. ...", subsections "2.1.", "2.1.1."; IMRaD order: Introduction, Related Work, Materials and Methods, Results, Discussion, Conclusions.
- Generative-AI use declared in a Materials and Methods subsection and in Acknowledgments.
- Back matter in MDPI order: Author Contributions (CRediT), Funding, Institutional Review Board Statement, Informed Consent Statement, Data Availability Statement, Acknowledgments, Conflicts of Interest, Abbreviations, Appendix.
- References numbered in order of first citation, cited as [1] or [1,2] or [3–5]; format "Surname, I.; Surname, I. Title. Abbrev. Journal Year, Volume, Pages." with DOI.
- Before upload, paste the text into the official MDPI Buildings Word template from the journal website (not retrievable automatically).

Sources: [ITcon about](https://itcon.org/about); [ITcon for authors](https://www.itcon.org/for-authors); [Buildings about](https://www.mdpi.com/journal/Buildings/about); [Buildings journal page](https://www.mdpi.com/journal/Buildings); [journalmetrics ITcon](https://www.journalmetrics.org/journal/journal-of-information-technology-in-construction); [Construction Innovation metrics](https://www.resurchify.com/impact/details/19900191719); [SASBE metrics](https://www.journalmetrics.org/journal/smart-and-sustainable-built-environment).
