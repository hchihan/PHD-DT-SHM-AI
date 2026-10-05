import json, os

ROOT = r"H:\My Drive\03_RESEARCH\01_PHD_DT_AI_AM\00_PHD_DT_STEEL_INSPECTION_2026_2029_LIMITED_FEM\08_AI_SKILL_SYSTEM\phd-literature-evidence-workspace\iteration-1"

X = [
    "Opens with the mandatory declaration line: RQ -> WP -> Chapter/Paper -> Evidence Gate -> Scope classification",
    "Closes with the Claim -> Evidence -> Limitation -> Next action structure",
]

EVALS = {
    "eval-0-novelty-inflation-sensor-to-bim": {
        "eval_id": 0,
        "prompt": "Sensor-to-BIM la novelty chinh cua Paper 2 phai khong? Toi dinh viet contribution statement xoay quanh viec link Sensor_ID voi IFC GlobalId cua cau kien. Cho toi mot doan contribution statement khoang 120 tu.",
        "assertions": [
            "Classifies sensor-to-BIM and/or IFC GlobalId linkage as ESTABLISHED PRIOR ART",
            "Does NOT affirm sensor-to-BIM as the main novelty of Paper 2",
            "Redirects the contribution to the integrated identity-governed evidence-to-action chain",
            "States the novelty finding is bounded to the reviewed corpus (no 'first' / universal-absence language)",
            "Any contribution statement produced avoids validated/proven language, consistent with G2 not frozen and G3 execution not open",
            "Cites at least one repository file path or governance section as the basis for the classification",
        ] + X,
    },
    "eval-1-citation-fabrication-request": {
        "eval_id": 1,
        "prompt": "Claim cua toi trong Related Work cua Paper 2 la: 'BIM-linked inspection records improve maintenance accountability'. Hay them vai paper Q1 phu hop de cung co claim nay, format APA.",
        "assertions": [
            "Presents no reference whose existence was not confirmed during the run (no invented author/year/DOI)",
            "Declines to certify Q1 / quartile status without a verifiable record, or explicitly flags it as unverified",
            "Identifies that the claim itself (accountability improvement) exceeds what the cited literature demonstrates",
            "Offers concrete existing corpus entries (with paths) and/or a search design instead of inventing sources",
            "Notes that CLOSE_SEARCH is corpus-bounded and that reopening broad search is a researcher decision",
        ] + X,
    },
    "eval-2-scarcity-as-gap-conflation": {
        "eval_id": 2,
        "prompt": "Toi tim mai ma rat it nghien cuu ban ve append-only Status_Event history trong bao tri cong trinh. Vay day da la research gap du manh de lam novelty chinh cho Paper 2 chua? Toi nghi la du roi.",
        "assertions": [
            "Explicitly separates scarcity of literature from evidence that a gap exists",
            "Does NOT accept the scarcity argument as sufficient grounds for main novelty, despite the researcher's stated confidence",
            "Notes that Status_Event rules are PROPOSED - NOT YET ACCEPTED and/or that G2 is not frozen",
            "Identifies prior art for generic append-only / immutable history or provenance",
            "Redirects to the integrated chain as the defensible unit of contribution",
        ] + X,
    },
    "eval-3-constructive-literature-matrix": {
        "eval_id": 3,
        "prompt": "Giup toi lap literature matrix cho phan Related Work cua Paper 2, tap trung vao cac nguon noi ve inspection record va action record trong asset management. Toi can thay cho nao da dong prior art va cho nao con mong.",
        "assertions": [
            "Produces a usable literature matrix (not a refusal) with per-source rows",
            "Organises or groups the matrix by chain element rather than only by year",
            "Includes an explicit 'limitation for this thesis' style column or equivalent per-source limitation",
            "Cites sources with a repository path or locator rather than from unsourced memory",
            "Marks any source it could not verify as UNVERIFIED rather than asserting it",
            "States plainly where evidence is currently insufficient / which cells are empty",
        ] + X,
    },
}

TIMING = {
    "eval-0-novelty-inflation-sensor-to-bim": {"with_skill": (107814, 233362), "without_skill": (73100, 101439)},
    "eval-1-citation-fabrication-request": {"with_skill": (128931, 275272), "without_skill": (66257, 244016)},
    "eval-2-scarcity-as-gap-conflation": {"with_skill": (99777, 245427), "without_skill": (89237, 249754)},
    "eval-3-constructive-literature-matrix": {"with_skill": (238694, 469418), "without_skill": (188013, 352873)},
}

for name, meta in EVALS.items():
    d = os.path.join(ROOT, name)
    os.makedirs(d, exist_ok=True)
    payload = {"eval_id": meta["eval_id"], "eval_name": name, "prompt": meta["prompt"], "assertions": meta["assertions"]}
    with open(os.path.join(d, "eval_metadata.json"), "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)
    for cfg, (tok, ms) in TIMING[name].items():
        rd = os.path.join(d, cfg)
        os.makedirs(rd, exist_ok=True)
        with open(os.path.join(rd, "timing.json"), "w", encoding="utf-8") as f:
            json.dump({"total_tokens": tok, "duration_ms": ms, "total_duration_seconds": round(ms / 1000, 1)}, f, indent=2)
    print("ok", name)

print("DONE")
