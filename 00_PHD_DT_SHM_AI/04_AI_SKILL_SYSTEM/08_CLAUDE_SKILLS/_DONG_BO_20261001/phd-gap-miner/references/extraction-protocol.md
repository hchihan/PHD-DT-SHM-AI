# Extraction protocol: finding limitations, classifying them, appending to audit

## Where limitations actually live

A section literally titled "Limitations" is often thin or absent. Search all of these before concluding a paper has none worth logging:

- Discussion (qualifying language: "however", "should be noted", "a caveat is", "this was not tested on", "future work should")
- Conclusion (often restates scope more honestly than the abstract)
- Threats to validity / boundary conditions (common in software-engineering-style papers)
- Method section's own stated assumptions (e.g. "we assume X remains constant")
- Case-study description (single building, single bridge, single lab rig — the scale of validation is itself a limitation even when the authors don't call it one)
- Author contributions / funding note occasionally reveals scope (e.g. "further validation on industrial assets is planned")

A paper reporting a proof-of-concept on one artifact (one residential building, one air-handling unit, one bridge) carries an implicit scale limitation even if the authors never write the word "limitation." Log this as `READER-INFERRED`, not `AUTHOR-STATED` — keep the two apart in the Evidence column.

## Limitation-type taxonomy

Tag each extracted statement with one of:

- `SCOPE` — single case study, single building type, single software tool, narrow dataset
- `VALIDATION-SCALE` — proof of concept, small sample, lab rig vs field
- `METHOD` — an assumption, simplification, or known failure mode of the technique itself
- `DATA` — missing data, data leakage, unlabeled ground truth, synthetic-only validation
- `GENERALIZABILITY` — authors themselves flag transfer to other domains/structures as untested
- `FUTURE-WORK` — explicit next step the authors propose but did not do

## Evidence label

Alongside the type tag, label the statement's status:

- `AUTHOR-STATED` — the paper says this itself
- `READER-INFERRED` — a defensible inference from the method/case-study description, not stated outright

Never convert a `READER-INFERRED` label into `AUTHOR-STATED` phrasing when reporting to the user or writing to the audit file.

## Single-paper discipline

One paper is one data point. Before writing `NARROWS` or `WIDENS` with a defense-level change, check the audit file for how many independent sources already support the same direction on that gap. If this is the first, write the finding as a candidate and say so plainly — do not silently promote it. Refer to the gap-evaluation history already logged in the audit file's Phần 7 sections before deciding a level actually changes.

## Audit append mechanics

**Literature-review project (đồng bộ 01/10/2026):** không ghi vào tệp kiểm toán bên ngoài. Ghi ứng viên vào `revision/GD2_nhat_ky_khoang_trong.md` (mã UV-NN; trường: phát biểu, căn cứ kèm trang, loại căn cứ, liên quan K, số căn cứ độc lập, năm, Phản chứng đã kiểm, Phát biểu đã thu hẹp; cập nhật bảng tóm tắt và dòng "Tình trạng phản chứng"); ghi bảng gap-impact và mức bảo vệ vào `revision/GD2_phan_tich_khoang_trong_*.md`; ghi tóm tắt vào `revision/changelog.md`. Các bước dưới đây áp cho tệp KHÔNG NỘP ngoài tiểu luận.

The audit file is `AUDIT_TIEU_LUAN_TONG_QUAN_KHONG_NOP.md` (or whatever the user's current KHÔNG NỘP audit file is named — ask if not obvious). Never delete or renumber an existing entry.

1. Locate the end of the running `## PHẦN 7` narrative and the start of `## PHẦN 8. VIỆC CẦN LÀM TRƯỚC KHI NỘP` (grep for `^## PHẦN 8` if the file is too large to hold in context at once).
2. Insert a new numbered subsection immediately before `## PHẦN 8`, following the existing numbering convention (e.g. if the last subsection is `7.9`, add `7.10`).
3. The new subsection must contain: which paper was read, its verification level, the full Claim → Evidence → Limitation → Gap-impact → Allowed-usage-location table, and an explicit "Kết luận về ba khoảng trống" line stating whether any gap's defense level actually changed and on what count of independent sources.
4. If the finding surfaces a genuinely new conflict (metadata mismatch, contradicting an existing claim, an author/year discrepancy), add one row to the running conflict table using the next unused `X-NN` number — check the existing table for the highest number in use first.
5. If the finding leaves unresolved work (a PDF still needed, a chapter edit still pending user approval), add or update one line in `## PHẦN 8` rather than leaving it only in the new subsection.
6. Do not edit the three submission chapters (`CHUONG_2...`, `CHUONG_3...`, `CHUONG_4...`) as part of this append step — that is a separate, explicit step per SKILL.md step 8.
7. This procedure covers gap-impact findings only (`PHẦN 7` additions). Future-development opportunity notes use a separate `PHẦN 9` section placed after `PHẦN 8` — see `opportunity-radar.md` for that append target. Never mix an opportunity note into a `PHẦN 7` gap-evidence table or vice versa.
