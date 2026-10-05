# Backup Manifest Before Zotero Writeback
**Created:** 2026-07-18  
**Purpose:** Non-destructive Phase 0 snapshot before any Zotero write attempt.

## Included

- Supervisor-approved Charter and ADR files.
- Current research direction, architecture, and status files.
- Living Evidence Base v1.1 and transitional v1.2.
- RQ1, RQ2, RQ3, and WP4 addenda dated 2026-07-18.
- New deep-read evidence matrix and Paper 2 competitor matrix.
- Duplicate/metadata correction log.
- Deep-read completion report and Zotero writeback queue.
- `MASTER_INDEX_CURRENT_v1.1.md`.
- `Literature_Review_Master_Index_Current.md`.
- `TERMINOLOGY_CONTROL_v1.1.md`.
- `ZOTERO_ITEM_KEY_INVENTORY_20260718.csv`.
- `ZOTERO_METADATA_EXPORT_CURRENT_20260718.csv`.

## Environment Status

- Zotero library read: available.
- Zotero API key: not present in environment.
- Zotero library ID: not present in environment.
- Zotero write mode: unavailable/local-only.
- Direct SQLite write: not attempted and prohibited.
- Web-API BibTeX export: unavailable because the local API does not support Atom output.

## Integrity Note

The metadata CSV is a read-only snapshot assembled from current Zotero collection metadata and the verified deep-read matrix. It is a fallback because the Zotero bibliography export endpoint requires web API credentials.
