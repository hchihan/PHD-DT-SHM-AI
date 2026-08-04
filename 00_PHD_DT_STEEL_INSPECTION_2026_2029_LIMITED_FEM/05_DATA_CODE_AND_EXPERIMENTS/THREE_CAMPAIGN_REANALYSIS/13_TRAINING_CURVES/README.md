# 13_TRAINING_CURVES

Per-epoch training curves were not retained during the CNN sweep in this pass — only the final epoch count at which `EarlyStopping` triggered was logged (see the `epochs_run` column in `05_WITHIN_CAMPAIGN_LORO_RESULTS.csv` and `06_CROSS_CAMPAIGN_RESULTS.csv`), not the per-epoch loss/accuracy history.

This is disclosed, not silently omitted: see `15_NEXT_ANALYSIS_RECOMMENDATION.md` item 6. If curve plots are required for Paper 1, the specific folds needed should be re-run with Keras `History` capture enabled (`model.fit(..., ).history`), which was not wired into `run_cnn.py` in this pass.
