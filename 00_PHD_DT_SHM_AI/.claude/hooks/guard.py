#!/usr/bin/env python3
"""Hàng rào cho repo luận án 00_PHD_DT_SHM_AI. Hai chế độ:

  python guard.py            đọc JSON của hook PreToolUse (Claude Code) từ stdin
  python guard.py --staged   kiểm tra những gì đã git add (dùng trong .githooks/pre-commit)

Chặn: commit tệp lớn, đuôi nhị phân/mô hình, khóa API, notebook còn output;
ghi đè kết quả đã khóa (90_ARCHIVE, CANONICAL_THREE_CAMPAIGN_DATASET, ddp_seed*).
Mã thoát 2 = chặn. Chỉ dùng thư viện chuẩn.
"""
import fnmatch, json, os, re, subprocess, sys, tempfile

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

PROJ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MAX_BYTES = 5_000_000
BLOCK_EXT = {".pt", ".pth", ".joblib", ".npz", ".pkl", ".h5", ".onnx", ".pdf", ".rvt", ".rfa",
             ".dwg", ".ifc", ".sdb", ".zip", ".m4a", ".mp3", ".mp4", ".key", ".pem"}
SECRET_RES = [re.compile(p) for p in (
    r"sk-[A-Za-z0-9_-]{20,}", r"AKIA[0-9A-Z]{16}", r"gh[pousr]_[A-Za-z0-9]{30,}",
    r"xox[baprs]-[A-Za-z0-9-]{10,}", r"AIza[0-9A-Za-z_-]{35}",
    r"(?i)(api[_-]?key|secret|token|password)[\"']?\s*[:=]\s*[\"'][A-Za-z0-9_\-/+=]{16,}[\"']",
    r"(?i)bearer\s+[A-Za-z0-9._-]{30,}",
)]
# Kết quả đã chốt: chỉ chặn ghi đè tệp ĐÃ CÓ; tạo tệp mới (thư mục chạy mới) vẫn được.
LOCKED = ["*/90_ARCHIVE/*", "*/CANONICAL_THREE_CAMPAIGN_DATASET/*", "*/ddp_seed*/*"]
REMIND = ("Tài liệu luận án: định tuyến RQ -> WP -> Chương/Bài -> Evidence Gate -> Phạm vi; trình bày "
          "Claim -> Evidence -> Limitation -> Next action (skill govern-phd-evidence). Số liệu chưa có "
          "run_manifest.json chỉ là khám phá, không dùng làm bằng chứng trong bản thảo.")


def block(msg):
    print("CHẶN: " + msg, file=sys.stderr)
    sys.exit(2)


def git(*args, check=False, cwd=None):
    r = subprocess.run(["git", "-c", "core.quotepath=off", *args], cwd=cwd or PROJ, capture_output=True)
    if check and r.returncode:
        block("git " + " ".join(args) + " lỗi: " + r.stderr.decode("utf-8", "replace"))
    return r.stdout


def staged():
    top = git("rev-parse", "--show-toplevel").decode().strip()
    prefix = os.path.relpath(PROJ, top).replace("\\", "/") + "/"
    git_top = lambda *a: git(*a, cwd=top)  # đường dẫn trong Git tính từ gốc repo
    def names(filt):
        out = git_top("diff", "--cached", "--name-only", "-z", "--diff-filter=" + filt, "--", prefix)
        return [n for n in out.decode("utf-8", "replace").split("\0") if n]
    added, changed = names("A"), names("ACM")
    allow = set()
    p = os.path.join(PROJ, ".githooks", "allow_large.txt")
    if os.path.exists(p):
        allow = {l.strip() for l in open(p, encoding="utf-8") if l.strip() and not l.startswith("#")}
    errs, warns = [], []
    for n in added:
        ext = os.path.splitext(n)[1].lower()
        base = os.path.basename(n)
        if ext in BLOCK_EXT or base == ".env" or base.startswith(".env."):
            errs.append(f"{n}: loại tệp không đưa vào Git (mô hình, nhị phân, khóa); để trên Drive")
    for n in changed:
        if n in allow:
            continue
        r = subprocess.run(["git", "cat-file", "-s", ":" + n], cwd=top, capture_output=True)
        size = int(r.stdout or 0)
        if size > MAX_BYTES:
            errs.append(f"{n}: {size/1e6:.1f} MB > {MAX_BYTES/1e6:.0f} MB (thêm vào .githooks/allow_large.txt nếu hợp lệ)")
        if n.lower().endswith(".ipynb"):
            try:
                nb = json.loads(git_top("show", ":" + n).decode("utf-8", "replace"))
            except ValueError:
                errs.append(f"{n}: không đọc được notebook")
                continue
            code = [c for c in nb.get("cells", []) if c.get("cell_type") == "code"]
            if any(c.get("outputs") or c.get("execution_count") for c in code):
                errs.append(f"{n}: notebook còn output/execution_count (xóa bằng Clear All Outputs)")
            if not re.search(r"seed|random_state", "".join("".join(c.get("source", [])) for c in code[:3]).lower()):
                warns.append(f"{n}: không thấy seed ở 3 ô code đầu")
    diff = git_top("diff", "--cached", "-U0", "--no-color", "--", prefix).decode("utf-8", "replace")
    cur = None
    for line in diff.splitlines():
        if line.startswith("+++ b/"):
            cur = line[6:]
        elif line.startswith("+") and not line.startswith("+++") and len(line) < 2000:
            for rx in SECRET_RES:
                if rx.search(line):
                    errs.append(f"{cur}: giống khóa/mật khẩu ({rx.pattern[:24]}…)")
                    break
    for w in warns:
        print("CẢNH BÁO: " + w, file=sys.stderr)
    if errs:
        block("không commit được:\n  - " + "\n  - ".join(errs[:30]))


def claude_hook():
    try:
        d = json.load(sys.stdin)
    except ValueError:
        return
    tool, inp = d.get("tool_name", ""), d.get("tool_input", {}) or {}
    if tool == "Bash":
        cmd = inp.get("command", "")
        if re.search(r"(?:^|[;&|(]\s*)git\s+(?:-\S+\s+)*commit\b", cmd):
            if re.search(r"--no-verify|\s-n\b|--no-gpg-sign", cmd):
                block("không bỏ qua hook commit (--no-verify).")
            staged()
        return
    path = (inp.get("file_path") or inp.get("notebook_path") or "").replace("\\", "/")
    if not path:
        return
    if os.path.exists(path) and any(fnmatch.fnmatch(path, g) for g in LOCKED):
        block(f"{path} thuộc kết quả đã khóa. Tạo thư mục chạy mới thay vì ghi đè (hoặc tự sửa tay nếu cố ý).")
    if "/01_LITERATURE_REVIEW/" in path and path.endswith(".md"):
        mark = os.path.join(tempfile.gettempdir(), f"phd_guard_{d.get('session_id', 'x')}")
        if not os.path.exists(mark):
            open(mark, "w").close()
            print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse", "additionalContext": REMIND}},
                             ensure_ascii=False))


if __name__ == "__main__":
    staged() if "--staged" in sys.argv else claude_hook()
