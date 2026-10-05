# Bibliographic Verification — CORE-5 (Paper 2, Gate 2–3)

Verification performed against Zotero item metadata AND the attached PDF (Version of Record), per instruction: **PDF/Version of Record > Zotero metadata > old notes**. All 5 PDFs opened and fully read (page by page).

| ID | Zotero item_key | Title (as in PDF) | Authors (as in PDF) | Year | Journal | Vol/Issue/Pages | DOI | PDF attached | PDF read |
|---|---|---|---|---|---|---|---|---|---|
| CORE-01 | `VC5ELKN2` | System- and Data-integrated linking of digital 3D models of existing bridge structures with Knowledge Graphs of non-destructive diagnostic methods | **Jan-Iwo Jäkel**, Eva Heinlein, Hendrik Morgenstern, Hongjo Kim, Katharina Klemt-Albert | 2025 | Journal of Information Technology in Construction (ITcon) | Vol. 30, pg. 603–630 | 10.36680/j.itcon.2025.025 | YES | YES (32/32 pages) |
| CORE-02 | `4RKYF9RY` | BIM-Enabled Infrastructure Asset Management Using Information Containers and Semantic Web | Philipp Hagedorn, Liu Liu, Markus König, Rade Hajdin, Tim Blumenfeld, Markus Stöckner, Maximilian Billmaier, Karl Grossauer, Kenneth Gavin | 2023 | Journal of Computing in Civil Engineering (ASCE) | 37(1), 04022041 | 10.1061/(ASCE)CP.1943-5487.0001051 | YES | YES (17/17 pages) |
| CORE-03 | `FCY7N3S7` | A BIM-based framework for operation and maintenance of utility tunnels | Xianfei Yin, Hexu Liu, Yuan Chen, Yaowu Wang, Mohamed Al-Hussein | 2020 | Tunnelling and Underground Space Technology | Vol. 97, 103252 | 10.1016/j.tust.2019.103252 | YES | YES (12/12 pages) |
| CORE-04 | `ZW6XVNGN` | Automated and interconnected facility management system: An open IFC cloud-based BIM solution | Sandra Matarneh, Faris Elghaish, Farzad Pour Rahimian, Nashwan Dawood, David Edwards | 2022 | Automation in Construction | Vol. 143, 104569 | 10.1016/j.autcon.2022.104569 | YES | YES (20/20 pages) |
| CORE-05 | `JTF8EM7Y` | Ontology-based representation of quality assurance and inspection planning in construction | Sebastian Seiß, Yuan Zheng, Jürgen Melzner, Jan Wium, Olli Seppänen | 2025 | Automation in Construction | Vol. 177, 106268 | 10.1016/j.autcon.2025.106268 | YES | YES (19/19 pages) |

## Conflicts between Zotero metadata and PDF (Version of Record)

### CORE-01 — CRITICAL conflict, resolved in favour of the PDF

- **Zotero metadata (`VC5ELKN2` → data.creators)** lists exactly four authors: Eva Heinlein; Hendrik Morgenstern; Hongjo Kim; K. Klemt-Albert. It does **not** list Jan-Iwo Jäkel at all. Zotero's `creatorSummary` is `"Heinlein et al."`.
- **The PDF itself** (title page, running header on every page, and the REFERENCE line on p. 603) states: *"Jan-Iwo Jäkel, Eva Heinlein, Hendrik Morgenstern, Hongjo Kim & Katharina Klemt-Albert (2025)."* Jäkel is listed **first**, with his own affiliation and email (`jaekel@icom.rwth-aachen.de`), and every page's running header reads **"Jäkel et al."** In-text self-citations throughout the paper also cite prior work as "Jäkel et al., 2024" / "Jäkel and Klemt-Albert, 2023" / "Jäkel and Heinlein, 2025" (the ontology's own home page, `http://purl.org/sodia`, is attributed to "Jäkel J.-I. and Heinlein E.").
- **Resolution applied in this deep-read (per instruction hierarchy PDF > Zotero > old notes):** the paper is cited as **Jäkel, Heinlein, Morgenstern, Kim & Klemt-Albert (2025)**, first author Jan-Iwo Jäkel. This directly reverses the user's own steer ("Không dùng tên 'Jäkel et al.' từ ghi chú cũ") — flagged explicitly because the live PDF is unambiguous and internally consistent (title page + running header + reference line + in-text self-citations all agree on Jäkel as first author), whereas the current Zotero record appears to have simply dropped him. **Recommendation:** update the Zotero item to add Jan-Iwo Jäkel as first author before this record is used in any citation manager export for the manuscript.
- All other fields (title, DOI, journal abbreviation, volume, pages 603–630) match exactly between Zotero and the PDF — only the creator list conflicts.

### CORE-02 through CORE-05 — no conflicts

- Titles, DOIs, journal names, volumes/issues/pages, and author name lists in Zotero match the PDF Version-of-Record title pages exactly for CORE-02, CORE-03, CORE-04, and CORE-05. No corrections needed. (Zotero stores some CORE-02 creators as single-field `name` rather than split first/last, e.g. "Hagedorn", "Pauwels", "König" — cosmetic only, not a factual conflict.)

## Note on Zotero tags already present

All 5 items already carried tags such as `GATE2_GATE3`, `PAPER2`, `RQ2_WP2`, `PRIORITY_A1` before this session started, i.e. they were pre-selected by an earlier pass. This deep-read is the first to open and read the attached PDFs page-by-page; no prior note in the library recorded full-text findings for these 5 items.

No Zotero metadata was modified during this task, per instruction.
