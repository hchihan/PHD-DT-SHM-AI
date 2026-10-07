"""Compare two IFC exports of the same registered RVT (ADR-RQ2-008, re-export stability test E2).

Dependency-free STEP text parser (IfcOpenShell is not installed on this workstation).
Join key: element Tag (= Revit ElementId written by the Revit exporter).

Usage:
    python compare_ifc_exports.py <export_1.ifc> <export_2.ifc> [out_dir]
"""
import csv, hashlib, pathlib, re, sys
from collections import Counter, defaultdict

HERE = pathlib.Path(__file__).parent
LIVE_INV = HERE.parent / "08_TRACEABILITY" / "P002_LIVE_STRUCTURAL_INVENTORY.csv"
ENTITY = re.compile(r"^#(\d+)\s*=\s*([A-Z0-9_]+)\s*\((.*)\)\s*;\s*$", re.S)
GUID = re.compile(r"^'[0-9A-Za-z_$]{22}'$")
# IfcElement subtypes carry Tag as the 8th attribute (index 7).
NON_ELEMENT_PREFIXES = ("IFCREL", "IFCPROPERTYSET", "IFCELEMENTQUANTITY")
NON_ELEMENT_CLASSES = {"IFCPROJECT", "IFCSITE", "IFCBUILDING", "IFCBUILDINGSTOREY", "IFCGROUP", "IFCSYSTEM",
                       "IFCZONE", "IFCGRID", "IFCSPACE"}


def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def split_args(s):
    out, depth, cur, i, instr = [], 0, [], 0, False
    while i < len(s):
        c = s[i]
        if instr:
            cur.append(c)
            if c == "'":
                if i + 1 < len(s) and s[i + 1] == "'":
                    cur.append("'"); i += 1
                else:
                    instr = False
        elif c == "'":
            instr = True; cur.append(c)
        elif c == "(":
            depth += 1; cur.append(c)
        elif c == ")":
            depth -= 1; cur.append(c)
        elif c == "," and depth == 0:
            out.append("".join(cur).strip()); cur = []
        else:
            cur.append(c)
        i += 1
    out.append("".join(cur).strip())
    return out


def is_element(cls, args):
    if cls in NON_ELEMENT_CLASSES or cls.startswith(NON_ELEMENT_PREFIXES) or cls.endswith("TYPE"):
        return False
    return len(args) >= 8 and args[5] != "$"   # ObjectPlacement present


def read_ifc(path):
    header, roots, elements = [], {}, {}
    buf, in_data = "", False
    with open(path, encoding="latin-1") as f:
        for line in f:
            if not in_data:
                if line.startswith("DATA;"):
                    in_data = True
                elif line.startswith(("FILE_DESCRIPTION", "FILE_NAME", "FILE_SCHEMA")):
                    header.append(line.strip())
                continue
            buf += line
            if not buf.rstrip().endswith(";"):
                continue
            m = ENTITY.match(buf.strip()); buf = ""
            if not m:
                continue
            cls, body = m.group(2), m.group(3)
            if not body.startswith("'"):
                continue
            args = split_args(body)
            if not GUID.match(args[0]):
                continue
            gid = args[0][1:-1]
            roots[gid] = cls
            if is_element(cls, args):
                tag = args[7].strip("'")
                elements.setdefault(tag, []).append((gid, cls))
    return header, roots, elements


def stored_duplicates():
    if not LIVE_INV.exists():
        return {}
    rows = list(csv.DictReader(open(LIVE_INV, encoding="utf-8-sig")))
    cnt = Counter(r["IfcGUID_StoredParameter"] for r in rows if r["IfcGUID_StoredParameter"])
    return {r["Revit_Element_ID"]: r["IfcGUID_StoredParameter"] for r in rows if cnt[r["IfcGUID_StoredParameter"]] > 1}


def header_field(header, key):
    return next((h for h in header if h.startswith(key)), "")


def main():
    a, b = map(pathlib.Path, sys.argv[1:3])
    out = pathlib.Path(sys.argv[3]) if len(sys.argv) > 3 else HERE
    out.mkdir(parents=True, exist_ok=True)
    ha, hb = sha256(a), sha256(b)
    hda, ra, ea = read_ifc(a)
    hdb, rb, eb = read_ifc(b)
    dups = stored_duplicates()

    rows, cls_count = [], Counter()
    for tag in sorted(set(ea) | set(eb), key=lambda t: (len(t), t)):
        ga, gb = ea.get(tag, []), eb.get(tag, [])
        if len(ga) > 1 or len(gb) > 1:
            status = "MULTIPLE_ENTITIES_PER_TAG"
        elif not ga:
            status = "ONLY_IN_EXPORT_2"
        elif not gb:
            status = "ONLY_IN_EXPORT_1"
        elif ga[0][0] == gb[0][0]:
            status = "SAME_GLOBALID"
        else:
            status = "CHANGED_GLOBALID"
        cls_count[status] += 1
        rows.append({
            "Revit_Element_ID": tag,
            "IFC_Class": (ga or gb)[0][1],
            "GlobalId_Export_1": ";".join(g for g, _ in ga),
            "GlobalId_Export_2": ";".join(g for g, _ in gb),
            "Status": status,
            "Stored_IfcGUID_Duplicate": "YES" if tag in dups else "NO",
            "Stored_IfcGUID": dups.get(tag, ""),
        })

    with open(out / "P002_REEXPORT_GLOBALID_COMPARISON.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)

    dup_rows = [r for r in rows if r["Stored_IfcGUID_Duplicate"] == "YES"]
    dup_status = Counter(r["Status"] for r in dup_rows)
    root_same = len(set(ra) & set(rb))
    elem_gids_a = [g for v in ea.values() for g, _ in v]
    elem_gids_b = [g for v in eb.values() for g, _ in v]

    hdr = [("FILE_SCHEMA", "FILE_SCHEMA"), ("FILE_DESCRIPTION (view, RevitIdentifiers, coordinates)", "FILE_DESCRIPTION"),
           ("FILE_NAME (time, exporter)", "FILE_NAME")]
    lines = [
        "# P002 re-export GlobalId stability: summary", "",
        f"Generated by `compare_ifc_exports.py`. Join key: element Tag (= Revit ElementId).", "",
        "| | Export 1 | Export 2 |", "|---|---|---|",
        f"| File | `{a.name}` | `{b.name}` |",
        f"| SHA-256 | `{ha}` | `{hb}` |",
        f"| Rooted entities with GlobalId | {len(ra)} | {len(rb)} |",
        f"| Elements (by Tag) | {len(ea)} | {len(eb)} |",
        f"| Distinct element GlobalIds | {len(set(elem_gids_a))} of {len(elem_gids_a)} | {len(set(elem_gids_b))} of {len(elem_gids_b)} |",
        "", "## Header comparison", "",
    ]
    for label, key in hdr:
        x, y = header_field(hda, key), header_field(hdb, key)
        lines += [f"- **{label}: {'IDENTICAL' if x == y else 'DIFFERENT'}**", f"  - 1: `{x}`", f"  - 2: `{y}`"]
    lines += ["", "## Element GlobalIds (joined on Tag)", "", "| Status | Count |", "|---|---|"]
    lines += [f"| {k} | {v} |" for k, v in sorted(cls_count.items())]
    lines += ["", f"## The {len(dup_rows)} elements with duplicated stored IfcGUID", "", "| Status | Count |", "|---|---|"]
    lines += [f"| {k} | {v} |" for k, v in sorted(dup_status.items())]
    lines += ["", "| Revit_Element_ID | Stored IfcGUID | Export 1 | Export 2 | Status |", "|---|---|---|---|---|"]
    lines += [f"| {r['Revit_Element_ID']} | {r['Stored_IfcGUID']} | {r['GlobalId_Export_1']} | {r['GlobalId_Export_2']} | {r['Status']} |" for r in dup_rows]
    lines += ["", "## All rooted entities (secondary)", "",
              f"GlobalIds present in both exports: {root_same}; only in 1: {len(set(ra) - set(rb))}; only in 2: {len(set(rb) - set(ra))}. "
              "Relationship and property-set GlobalIds may be regenerated by the exporter; they are not component identities."]
    (out / "P002_REEXPORT_SUMMARY.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines[:40]))


if __name__ == "__main__":
    main()
