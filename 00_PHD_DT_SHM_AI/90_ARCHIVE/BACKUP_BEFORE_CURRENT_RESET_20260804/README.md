# BACKUP BEFORE CURRENT RESET 20260804

**Created:** 2026-08-04  
**Status:** Protected pre-reset snapshot  
**Scope:** Files scheduled for update, move, or archive during the current-direction reset.

This is a scoped control-surface backup, not a duplicate of the complete repository. Empirical evidence, literature PDFs, model outputs, raw/result CSVs, prior archives, and deep-read reports are not copied because the reset does not modify them.

`BACKUP_MANIFEST_20260804.csv` records the original path, snapshot path, pre-reset SHA-256, size, planned action, and copy verification for all 12 backed-up files. Every source-to-snapshot hash comparison passed.

The repository-wide pre-reset classification and action records are:

- `01_CURRENT_CONTROL/REPOSITORY_FILE_CLASSIFICATION_20260804.csv`
- `01_CURRENT_CONTROL/CURRENT_RESET_FILE_MANIFEST_20260804.csv`
- `01_CURRENT_CONTROL/PRE_UPDATE_GIT_STATUS_20260804.txt`

No file in this snapshot is a current source of truth. It is retained only for rollback and historical traceability.
