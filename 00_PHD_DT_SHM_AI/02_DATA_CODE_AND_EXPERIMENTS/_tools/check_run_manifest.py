#!/usr/bin/env python3
"""Kiểm tra tái lập cho một thư mục chạy: python check_run_manifest.py <thư_mục_chạy> [--root <gốc_tìm_dữ_liệu>]

Đọc <thư_mục_chạy>/run_manifest.json, kiểm tra trường bắt buộc, tính lại SHA-256 của dữ liệu và
checkpoint, đối chiếu tệp kết quả. Chỉ đọc. Mã thoát 0 = đạt, 1 = thiếu/lệch.
"""
import hashlib, json, os, re, sys

sys.stdout.reconfigure(encoding="utf-8")


def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    run = sys.argv[1]
    roots = [run] + ([sys.argv[sys.argv.index("--root") + 1]] if "--root" in sys.argv else [])
    mp = os.path.join(run, "run_manifest.json")
    if not os.path.exists(mp):
        print("THIẾU run_manifest.json -> chỉ là kết quả khám phá, chưa dùng làm bằng chứng")
        return 1
    m = json.load(open(mp, encoding="utf-8"))
    bad, warn = [], []

    def need(path, cond=lambda v: v not in (None, "", [], {})):
        v = m
        for k in path.split("."):
            v = v.get(k) if isinstance(v, dict) else None
        if not cond(v):
            bad.append(f"thiếu hoặc rỗng: {path}")
        return v

    need("seed", lambda v: isinstance(v, (int, list)) and v != [])
    need("command")
    c = need("code.commit", lambda v: isinstance(v, str) and re.fullmatch(r"[0-9a-f]{7,40}", v) is not None)
    if m.get("code", {}).get("dirty"):
        warn.append("code.dirty = true: mã chạy chưa commit, không truy ngược được")
    need("data.dataset_version")
    need("split.scheme", lambda v: v in ("LORO", "LOCO"))
    need("split.folds")
    need("model.arch")
    need("env.python")
    need("env.packages")
    for item in (m.get("data", {}).get("files") or []):
        p = next((os.path.join(r, item["path"]) for r in roots if os.path.exists(os.path.join(r, item["path"]))), None)
        if not p:
            bad.append(f"không thấy tệp dữ liệu: {item['path']}")
        elif sha(p) != item.get("sha256"):
            bad.append(f"SHA-256 lệch: {item['path']}")
    if not m.get("data", {}).get("files"):
        bad.append("data.files rỗng")
    ck = m.get("model", {}).get("checkpoint_sha256")
    if ck is None:
        warn.append("model.checkpoint_sha256 = null: không có mô hình để đối chiếu")
    for r in m.get("results") or []:
        if not os.path.exists(os.path.join(run, r)):
            bad.append(f"thiếu tệp kết quả: {r}")
    for w in warn:
        print("CẢNH BÁO:", w)
    for b in bad:
        print("LỖI:", b)
    print("ĐẠT" if not bad else f"KHÔNG ĐẠT ({len(bad)} lỗi)")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
