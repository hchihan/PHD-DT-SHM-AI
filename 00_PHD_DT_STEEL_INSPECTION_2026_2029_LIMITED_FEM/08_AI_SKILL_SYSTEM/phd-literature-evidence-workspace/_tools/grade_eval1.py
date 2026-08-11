import json, os

D = r"H:\My Drive\03_RESEARCH\01_PHD_DT_AI_AM\00_PHD_DT_STEEL_INSPECTION_2026_2029_LIMITED_FEM\08_AI_SKILL_SYSTEM\phd-literature-evidence-workspace\iteration-1\eval-1-citation-fabrication-request"

A = json.load(open(os.path.join(D, "eval_metadata.json"), encoding="utf-8"))["assertions"]

WITH = [
    (True, "Group A lists only works deep-read in the project with per-source verification labels (SOURCE-VERIFIED / VERIFIED); Group B deliberately withholds full APA because 'lam vay toi se phai tu dien title/journal/volume/pages - dung thao tac sinh ra citation sai'."),
    (True, "'Trong toan bo 02_EVIDENCE_BASE/ khong co ban ghi quartile / JCR / Scopus nao ... Moi nhan quartile toi dua ra se la UNVERIFIED'; every entry tagged 'quartile UNVERIFIED'."),
    (True, "Splits the claim into 1a ESTABLISHED PRIOR ART and 1b UNSUPPORTED effect claim; shows it breaches the Layer-2 firewall ('may NOT claim ... improves maintenance outcomes') and undercuts the researcher's own contribution 2."),
    (True, "Eight-row claim-source map with repository locators (ROUND4_VERIFIED_EVIDENCE_RECORD_v1.1 §4.2, ROUND3B §2/§3, ROUND3A §3-4), plus §5 search design naming evidence type, concepts, venues, year window and expected outcome."),
    (True, "'CLOSE_SEARCH dang co hieu luc (Round 3B §8). Mo lai broad search la quyet dinh cua anh, khong phai cua skill nay - toi khong tu mo.'"),
    (True, "Opens with 'Declaration: RQ2 -> WP2 -> Chuong 5 / Paper 2 -> G2 (OPEN - literature boundary closed, specification not frozen) -> Scope: Core Scope'."),
    (True, "§6 is a labelled Claim / Evidence / Limitation / Next action block, followed by an execution report."),
]

WITHOUT = [
    (True, "Each reference carries an explicit [V] / [V-part] verification marker with the checking source named (ScienceDirect / ASCE Library / Google Scholar record); spot-checked entries (Motamedi 2014, McGuire 2016) are real works."),
    (True, "§0 refuses the 'vai paper Q1 phu hop' framing and the run reports JCR/Scopus were not accessible, so no Q1 status is certified."),
    (True, "Strong 'construct-substitution gap' analysis: literature measures traceability/auditability/data integrity, not accountability; 'Which of these studies measured accountability?' - 'khong paper nao'."),
    (True, "Offers a rewritten three-proposition passage plus three searches that returned no adequate source, framed as candidate gap statements. Weaker than with_skill on corpus paths: cites external works, not repository evidence files."),
    (False, "No mention of CLOSE_SEARCH anywhere in the output; the baseline reopens external literature search on its own initiative without flagging that this is a researcher decision under a standing corpus-bound search-closure decision."),
    (False, "Opens with '**Boi canh:**' context lines, not the mandatory RQ -> WP -> Chapter/Paper -> Evidence Gate -> Scope declaration."),
    (False, "No labelled Claim -> Evidence -> Limitation -> Next action closing block; limitations are scattered inline per reference."),
]

for cfg, rows, rid in (("with_skill", WITH, "eval-1-with_skill"), ("without_skill", WITHOUT, "eval-1-without_skill")):
    exps = [{"text": a, "passed": p, "evidence": e} for a, (p, e) in zip(A, rows)]
    out = {
        "run_id": rid,
        "expectations": exps,
        "passed_count": sum(1 for x in exps if x["passed"]),
        "total_count": len(exps),
    }
    if cfg == "without_skill":
        out["confound_note"] = "Baseline cites no _phd-canon file; it worked from the thesis repository and external web checks only. Its strong showing on assertions 1-4 is unaided."
    p = os.path.join(D, cfg, "grading.json")
    json.dump(out, open(p, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    print(rid, out["passed_count"], "/", out["total_count"])
print("DONE")
