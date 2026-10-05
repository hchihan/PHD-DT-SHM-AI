# LITERATURE GAPS FOR PAPER 1

**Date:** 12/08/2026
**Basis:** `PAPER1_EXPANDED_LITERATURE_MATRIX_20260812.csv`, `LIVING_EVIDENCE_BASE_CURRENT_20260812.md`, `CITATION_AUDIT_GATE1_TO_GATE23_20260811.md`.
**Purpose:** record what the current corpus cannot support, and the exact question each search must answer. No source is invented here.

## 1. Bibliographic defects that must be repaired before submission

### 1.1 Entries with no bibliographic identity

Eight register entries carry the literal placeholder text `verify` in the year field and a description rather than a title: `PHXJ2KJN`, `FZ3GFSF2`, `L52SHNEH`, `WYN2RKEH`, `2ILY9YZ3`, `IM9UKGRV`, `KDRSBM9K`, `ULHLMFZ8`. They have no author, no title and no year. They cannot be cited in any form. The register notes that their detail sits in an RQ2 addendum held under `90_ARCHIVE`, which is not a current source.

Action: resolve each Zotero key to a full record, or delete the row. A citation cannot rest on a Zotero key alone.

### 1.2 Entries cited in this programme with no DOI recorded

`YR2NQWE7`, `HWUA93NT`, `VVBGM9EN`, `PEUHYBPS`, `QUGY4928`, `QIS5QS7V`, `DFAJFF8J`, `JQSY7XD4`, `XSKNR656`, `L56P7RAF`, `PRQL4Y8P`, `LSYSC59G`, `GIIUUEW8`, `4LKDXFMK`, `8Y64JYBR`, `9XNSNIPX`.

Sixteen of the works this paper depends on carry no DOI, journal, volume or page range in the register. Four of them (`YR2NQWE7`, `DFAJFF8J`, `GIIUUEW8`, and the Abdeljaber pair) have PDFs sitting in `02_EVIDENCE_BASE/RQ1_GATE1/RQ1_UPDATED_DEEP_READ_10.07/`, so the metadata can be read straight off the files.

Action: complete author, title, outlet, year, volume, pages and DOI for all sixteen from the PDFs already held, then reconcile against the register.

### 1.3 Unresolved version conflict

`ZLFATP2Z`, Ojala and Garriga, permutation tests for studying classifier performance. The register records a conflict between a 2009 conference item and a 2010 journal item with a parent-to-PDF mismatch. The paper relies on this work for its permutation framework.

Action: separate the conference parent from the journal extension, attach the correct PDF, and cite one of them.

### 1.4 Partial standards

`V3IYM6UC` (ISO/IEC 30173:2023) and `EWBTQFTP` (ISO/IEC 30186:2025) are held as clause previews, not full standards.

Action: acquire the full texts or drop both. A preview cannot support a normative statement. The same test applies to ISO 19650-3 and TCVN 14177:2024, which are currently cited as standards without a verified clause reference.

## 2. Substantive gaps in cluster coverage

The matrix covers clusters 2, 3 and 4 adequately for a Q2 submission. Clusters 1 and 5 are thin, and cluster 1 is the one that carries the repositioning.

### 2.1 Cluster 1 — construction asset management and condition-based inspection decision support

Current holdings: `YGZ32C8M`, `8Y64JYBR`, `GIIUUEW8`, `4LKDXFMK`, `XSKNR656`, `DOC-0008`, `DOC-0028`, `DOC-0041`, plus ISO 19650-3 and TCVN 14177:2024. Of these, three are locator-screened only and two are normative rather than empirical. That leaves roughly four usable empirical sources for the disciplinary framing of the entire paper. It is not enough.

Questions a targeted search must answer:

1. How do asset owners and facility managers currently decide to commission a structural inspection, and what information do they require before doing so? Sought: empirical studies, interview or survey based, in construction asset management or facilities management. Needed for section 4 of the manuscript.
2. What is documented about the gap between the output of a monitoring system and its actual use in a maintenance or inspection decision? Sought: adoption studies, post-implementation reviews, barriers-to-use studies. Needed for section 4 and section 12.
3. Is there published work on acceptance criteria or assurance requirements that an owner applies to sensor-derived information before acting on it? Needed for section 12, and this is the closest external analogue to the contribution.
4. What does the asset-management literature say about industrial steel-framed buildings specifically, as opposed to bridges? The current corpus is heavily bridge-weighted. Needed for section 6 and section 11.5.

### 2.2 Cluster 3 — data quality, provenance and trustworthiness of monitoring evidence

Current holdings: `EMTIHHX4`, `CITAUD-P3`, `CITAUD-P5`, `TRZY4P6X`, `GE3XSAYV`, `D3TGCKXW`, `L56P7RAF`.

These cover environmental context and provenance mechanics. None of them addresses the question this paper actually asks, which is what makes a derived monitoring output trustworthy enough to act on.

Questions a targeted search must answer:

5. Are there established frameworks for data quality or trustworthiness applied to sensor-derived engineering evidence, as distinct from generic data-quality dimensions? Needed for section 12.
6. Is there published work on sensor identity or channel provenance errors in deployed monitoring systems? This is the gap the audit exposed within this project, and no held source addresses it. Needed for section 7.2 and section 11.2, where it currently stands unsupported by any external reference.
7. What conventions exist for reporting the scope of validity of a data-derived engineering result? Needed for section 12.

Item 6 is the highest-value search in this document. The paper's most original observation, that a partition-valid result can rest on an unstable column-to-sensor mapping, currently has no comparator in the corpus.

### 2.3 Cluster 5 — information continuity to inspection records

Current holdings are adequate for the downstream-motivation role Paper 1 gives them: `XUN8EX6X`, `VI5QMSAE`, `EMTIHHX4`, `GUEJBZBZ`, `LSYSC59G`, `ESTEYBHA`. No further search is needed for Paper 1. These belong to Paper 2 and must not expand inside Paper 1.

## 3. What must not be done

Do not reopen the broad structural search. `CURRENT_STATUS_AND_NEXT_DIRECTION.md` §3 records the literature decision as `CLOSE_SEARCH`, bounded to the screened corpus, and permits reopening only for a new question likely to change the structural novelty boundary. Questions 1 to 7 above are bounded additions to specific manuscript sections, not a reopening.

Do not cite ISO 19650, TCVN 14177 or any legal instrument as decoration. `MASTER_RESEARCH_CHARTER_CURRENT_20260812.md` §8 restricts legal and normative references to anchoring management obligations, forbids deriving technical thresholds from them, and requires the label `Legal reference pending official-source verification` on anything unverified.

Do not cite the six works listed in `CITATION_AUDIT_GATE1_TO_GATE23_20260811.md` beyond what that audit states their authors demonstrate. The audit verified DOI, title, outlet, volume and pages; it did not record a completed full-text deep read for all of them, and the Living Evidence register still carries several of them as metadata-only.

## 4. Claim → Evidence → Limitation → Next action

**Claim.** The corpus supports the methodological argument of Paper 1 and does not yet support its disciplinary framing.

**Evidence.** Clusters 2, 3 and 4 hold 22 deep-read sources with adequate locators. Cluster 1 holds approximately four usable empirical sources, and the paper's central provenance observation has no external comparator.

**Limitation.** Sixteen cited works lack a DOI, eight register entries have no bibliographic identity at all, one carries an unresolved version conflict, and two standards are held only as previews.

**Next action.** Repair section 1 first, since it costs no search and the PDFs are already held. Then run searches 1, 3 and 6, in that order. Search 6 is the one that determines whether the paper's most original observation stands alone or stands in a line.
