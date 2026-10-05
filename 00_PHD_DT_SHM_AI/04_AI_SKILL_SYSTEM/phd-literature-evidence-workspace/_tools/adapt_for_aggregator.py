"""Adapt the flat run layout to what skill-creator's aggregate_benchmark.py expects.

It wants  eval-*/<config>/run-N/grading.json  with a `summary` block.
We wrote   eval-*/<config>/grading.json       with passed_count/total_count.
This script mirrors each config dir into run-1/ and adds the summary block.
Original files are left in place so the eval viewer still finds outputs/.
"""
import json, os, shutil

ROOT = r"H:\My Drive\03_RESEARCH\01_PHD_DT_AI_AM\00_PHD_DT_STEEL_INSPECTION_2026_2029_LIMITED_FEM\08_AI_SKILL_SYSTEM\phd-literature-evidence-workspace\iteration-1"

for eval_name in sorted(os.listdir(ROOT)):
    eval_dir = os.path.join(ROOT, eval_name)
    if not os.path.isdir(eval_dir) or not eval_name.startswith("eval-"):
        continue
    for cfg in ("with_skill", "without_skill"):
        cfg_dir = os.path.join(eval_dir, cfg)
        gpath = os.path.join(cfg_dir, "grading.json")
        if not os.path.exists(gpath):
            print("skip (no grading):", eval_name, cfg)
            continue
        g = json.load(open(gpath, encoding="utf-8"))
        exps = g.get("expectations", [])
        passed = g.get("passed_count", sum(1 for e in exps if e.get("passed")))
        total = g.get("total_count", len(exps))
        g["summary"] = {
            "passed": passed,
            "failed": total - passed,
            "total": total,
            "pass_rate": round(passed / total, 4) if total else 0.0,
        }
        json.dump(g, open(gpath, "w", encoding="utf-8"), indent=2, ensure_ascii=False)

        run_dir = os.path.join(cfg_dir, "run-1")
        os.makedirs(run_dir, exist_ok=True)
        json.dump(g, open(os.path.join(run_dir, "grading.json"), "w", encoding="utf-8"), indent=2, ensure_ascii=False)
        tpath = os.path.join(cfg_dir, "timing.json")
        if os.path.exists(tpath):
            shutil.copyfile(tpath, os.path.join(run_dir, "timing.json"))
        print(f"{eval_name:45s} {cfg:15s} {passed}/{total}")

print("DONE")
