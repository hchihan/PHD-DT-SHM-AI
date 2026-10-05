# Deep-read protocol

## Contents

1. Evidence hierarchy
2. Five reading passes
3. Limitation and future-work extraction
4. Thesis mapping
5. Research-idea screening
6. Output by response mode
7. Required output sections

## 1. Evidence hierarchy

Use evidence in this order:

1. Original PDF page, table, figure or appendix.
2. Publisher/JATS/HTML full text when it is the same version.
3. MinerU JSON/Markdown checked against the PDF.
4. Abstract-only metadata, used only for screening.

Distinguish printed page number from PDF viewer index. Use `PDF p. n` when the paper has no printed page number. A converted-text locator is provisional until checked against the PDF.

## 2. Five reading passes

### Pass A — Orientation

Extract: research problem, unit of analysis, context, stated gap, research question/objective, claimed contribution and paper structure.

### Pass B — Method and evidence

Extract: design, data source, sample/case size, sensors or information objects, preprocessing, train/validation/test separation, baselines, evaluation metrics, uncertainty, external validation, reproducibility artifacts and actual result boundaries.

For ML papers, explicitly check data leakage, grouping unit, split logic and whether results are run-aware or specimen/site-aware. For BIM/DT papers, check whether the contribution is a formal model with measurable validation or only system integration/demo. For field papers, separate deployment feasibility from damage diagnosis.

### Pass C — Limitations and future work

Read the full Discussion and Conclusion, then search these families:

- limitations: `limitation`, `limited`, `constraint`, `weakness`, `shortcoming`, `threat to validity`, `caution`, `cannot`, `does not`, `not considered`;
- generalizability: `generaliz`, `transfer`, `external valid`, `single case`, `small sample`, `laboratory`, `field`, `scale`;
- data/method: `dataset`, `label`, `sensor`, `noise`, `uncertainty`, `baseline`, `validation`, `leakage`, `imbalance`;
- future work: `future work`, `further research`, `should investigate`, `remains`, `next step`, `extend`, `need to`, `could be explored`.

Record each item with: exact meaning in paraphrase, short compliant excerpt only when necessary, locator, limitation category, affected claim, author remedy, and whether the paper actually tested that remedy.

### Pass D — Thesis relationship

For each candidate gap touched, also list the counter-evidence to check (standards and systems such as BCF 3.0, IFC4 IfcActionRequest/IfcApproval, SSN Deployment, ISO 19650, CMMS, and the mandatory precedents in `project-canon-tltq.md` §4). Record "Phản chứng đã kiểm" and "Phát biểu đã thu hẹp"; a candidate with any "chưa kiểm" item cannot go to Gap stage (ĐD3).

Determine whether the paper:

- directly supports a locked thesis claim;
- supplies a method or evaluation criterion;
- challenges an assumption;
- defines a boundary or limitation;
- offers only background;
- falls outside the locked scope.

Map one primary and at most two secondary destinations. Explain why a paper does **not** belong to tempting but incorrect destinations.

### Pass E — Supervisor-style teaching

After the evidence extraction is complete, explain the paper using `references/supervisor-teaching-protocol.md`. Keep the verified record and teaching layer separate. The teaching layer may clarify implicit logic but must not add unverified author claims.

## 3. Limitation and future-work extraction

Classify limitations as:

| Code | Category | Typical question |
|---|---|---|
| L-DATA | Data | Is the sample narrow, imbalanced, synthetic or unrepresentative? |
| L-DESIGN | Research design | Does the design support the claimed causal or comparative conclusion? |
| L-VALID | Validation | Is there independent, grouped, external or field validation? |
| L-METHOD | Method/model | Are assumptions, baselines, sensitivity or uncertainty incomplete? |
| L-SCALE | Scale/transfer | Can lab, case or scale results transfer beyond the tested setting? |
| L-TRACE | Traceability/information | Can evidence be traced to assets, records and actions? |
| L-DECISION | Decision/management | Was human review, workflow fit or action usefulness evaluated? |
| L-REPORT | Reporting/reproducibility | Are data, code, parameters or definitions missing? |

Do not equate “future work” with “limitation.” Some future directions are optional extensions and do not weaken current claims.

## 4. Thesis mapping

For each relevant finding, fill:

| Paper evidence | Primary/secondary | RQ | WP | Chapter | Paper | Gate | Scope | Use in thesis |
|---|---|---|---|---|---|---|---|---|

Valid uses: definition, gap evidence, method choice, metric/criterion, design warning, comparison baseline, limitation, discussion, or future work.

## 5. Research-idea screening

Treat every idea as a candidate until it passes all checks:

1. `Source`: anchored in an author-stated or defensibly inferred limitation.
2. `Fit`: advances the locked chain and Construction Management contribution.
3. `Evidence`: more than one paper supports the candidate gap, or a verification search is planned.
4. `Data`: available or realistically collectible within the PhD.
5. `Method`: testable with a defined unit of analysis and evaluation criterion.
6. `Novelty`: not already answered by the focal paper or known thesis work.
7. `Boundary`: does not create prohibited proof obligations.
8. `Priority`: helps close the current or next Evidence Gate.

Score each check `PASS`, `PARTIAL`, `FAIL` or `UNKNOWN`. Recommend only ideas with no `FAIL`; label all `UNKNOWN` items.

Use one of four decisions:

- `ADOPT NOW`: directly strengthens the current Gate with available data.
- `ADD TO REVIEW`: useful candidate gap requiring cross-paper confirmation.
- `DEFER`: valid post-PhD or low-priority extension.
- `REJECT`: out of scope, duplicative, infeasible or claim-inflating.

## 6. Output by response mode

| Mode | Required delivery |
|---|---|
| `AUDIT` | A–G, compressed to decision-relevant evidence, plus Section I |
| `PROFESSOR` | Verified one-paragraph verdict, I, then the most relevant of J–M |
| `INTERACTIVE` | Verified boundary, one teaching module, then one question; wait for the answer |
| `FULL` | A–N without omission; normally save as a reusable Markdown record |

Do not produce a full-length report merely because the paper is long. Scale depth to the user's decision and learning need.

## 7. Required output sections

**Literature-review project mapping:** sections A–G map onto `notes/<ZoteroKey>.md` (CLAUDE.md §7.4 table + items 1–8); section H goes to `revision/GD2_phan_tich_khoang_trong_*.md`; candidates go to `revision/GD2_nhat_ky_khoang_trong.md`.

### A. Paper identity and conversion QA

Title; authors; year; venue; DOI/URL status; source file/hash; PDF quality; conversion method; conversion defects; sections verified against PDF.

### B. One-paragraph verdict

State what the paper contributes, the strength of its evidence, and its primary thesis destination.

### C. Deep-read evidence table

| Element | Author's claim or evidence | Locator | Critical assessment | Thesis use |
|---|---|---|---|---|

Include at minimum: gap, objective, data, method, validation, key results, contribution and claim boundary.

### D. Limitations and future work

| ID | Status | Limitation/direction | Locator | Affected claim | Relevance to thesis |
|---|---|---|---|---|---|

`Status` must be `AUTHOR-STATED` or `READER-INFERRED`.

### E. Thesis routing

Show the complete route and the mapping table from Section 4. State the primary destination, secondary destinations and non-destinations.

### F. Candidate research ideas

| Idea | Source limitation | Fit | Evidence | Data | Method | Novelty | Boundary | Priority | Decision |
|---|---|---|---|---|---|---|---|---|---|

Give at most three ideas, ranked. Prefer one well-supported idea over several speculative ones.

### G. Claim–Evidence–Limitation–Next action

Close with the most decision-relevant thesis judgment. If verification is missing, write exactly: `Evidence is currently insufficient.`

### H. Cross-paper synthesis, when applicable

| Candidate gap or idea | Supporting papers | Contradicting papers | Thesis destination | Evidence strength | Verification needed | Decision |
|---|---|---|---|---|---|---|

Require locators back to each individual paper record. Report both convergence and disagreement. Never use absence from the reviewed subset as proof of absence from the literature.

### I–N. Professor-style tutorial

After Sections A–H, produce the six teaching sections specified in `references/supervisor-teaching-protocol.md`: five-minute lesson, logical walkthrough, method reconstruction, results interpretation, thesis application and three-question comprehension check.
