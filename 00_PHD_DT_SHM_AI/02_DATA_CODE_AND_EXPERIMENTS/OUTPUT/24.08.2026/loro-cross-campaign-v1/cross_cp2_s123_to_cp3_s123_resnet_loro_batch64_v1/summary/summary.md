# Recording-level results

Metrics are computed per recording: the window probabilities of a recording
are averaged before the argmax. `sd` is the sample standard deviation.

## Per run

| dataset_name | model_name | version | split_id | seed | accuracy | balanced_accuracy | f1_macro | roc_auc_macro | test_loss |
|---|---|---|---|---|---|---|---|---|---|
| cross_cp2_s123_to_cp3_s123 | resnet1D | resnet1D-06dfe3b | train7-8-10-11-12_val9_test13-14-15-16-17-18 | 42 | 0.2500 | 0.2500 | 0.1492 | 0.5553 | 4.3460 |
| cross_cp2_s123_to_cp3_s123 | resnet1D | resnet1D-06dfe3b | train7-8-9-10-11_val12_test13-14-15-16-17-18 | 42 | 0.1944 | 0.1944 | 0.1296 | 0.4851 | 2.7640 |
| cross_cp2_s123_to_cp3_s123 | resnet1D | resnet1D-06dfe3b | train7-8-9-10-12_val11_test13-14-15-16-17-18 | 42 | 0.2361 | 0.2361 | 0.1161 | 0.4817 | 4.0516 |
| cross_cp2_s123_to_cp3_s123 | resnet1D | resnet1D-06dfe3b | train7-8-9-11-12_val10_test13-14-15-16-17-18 | 42 | 0.2361 | 0.2361 | 0.0955 | 0.5136 | 5.4807 |
| cross_cp2_s123_to_cp3_s123 | resnet1D | resnet1D-06dfe3b | train7-9-10-11-12_val8_test13-14-15-16-17-18 | 42 | 0.2361 | 0.2361 | 0.0966 | 0.4897 | 5.8828 |
| cross_cp2_s123_to_cp3_s123 | resnet1D | resnet1D-06dfe3b | train8-9-10-11-12_val7_test13-14-15-16-17-18 | 42 | 0.2361 | 0.2361 | 0.0966 | 0.5049 | 5.8269 |

## Mean ± SD across seeds (one row per split/fold)

| dataset_name | model_name | version | split_id | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cross_cp2_s123_to_cp3_s123 | resnet1D | resnet1D-06dfe3b | train7-8-10-11-12_val9_test13-14-15-16-17-18 | 1 | 0.2500 |  | 0.2500 |  | 0.1492 |  | 0.5553 |  | 4.3460 |  |
| cross_cp2_s123_to_cp3_s123 | resnet1D | resnet1D-06dfe3b | train7-8-9-10-11_val12_test13-14-15-16-17-18 | 1 | 0.1944 |  | 0.1944 |  | 0.1296 |  | 0.4851 |  | 2.7640 |  |
| cross_cp2_s123_to_cp3_s123 | resnet1D | resnet1D-06dfe3b | train7-8-9-10-12_val11_test13-14-15-16-17-18 | 1 | 0.2361 |  | 0.2361 |  | 0.1161 |  | 0.4817 |  | 4.0516 |  |
| cross_cp2_s123_to_cp3_s123 | resnet1D | resnet1D-06dfe3b | train7-8-9-11-12_val10_test13-14-15-16-17-18 | 1 | 0.2361 |  | 0.2361 |  | 0.0955 |  | 0.5136 |  | 5.4807 |  |
| cross_cp2_s123_to_cp3_s123 | resnet1D | resnet1D-06dfe3b | train7-9-10-11-12_val8_test13-14-15-16-17-18 | 1 | 0.2361 |  | 0.2361 |  | 0.0966 |  | 0.4897 |  | 5.8828 |  |
| cross_cp2_s123_to_cp3_s123 | resnet1D | resnet1D-06dfe3b | train8-9-10-11-12_val7_test13-14-15-16-17-18 | 1 | 0.2361 |  | 0.2361 |  | 0.0966 |  | 0.5049 |  | 5.8269 |  |

## Mean ± SD across splits/folds (one row per seed)

| dataset_name | model_name | version | seed | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cross_cp2_s123_to_cp3_s123 | resnet1D | resnet1D-06dfe3b | 42 | 6 | 0.2315 | 0.0190 | 0.2315 | 0.0190 | 0.1139 | 0.0221 | 0.5051 | 0.0275 | 4.7253 | 1.2303 |

## Mean ± SD across every run (seeds and folds pooled)

| dataset_name | model_name | version | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cross_cp2_s123_to_cp3_s123 | resnet1D | resnet1D-06dfe3b | 6 | 0.2315 | 0.0190 | 0.2315 | 0.0190 | 0.1139 | 0.0221 | 0.5051 | 0.0275 | 4.7253 | 1.2303 |

### Pooled confusion matrix: cross_cp2_s123_to_cp3_s123 / resnet1D / resnet1D-06dfe3b

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 0 | 100 | 8 | 0 |
| B1 | 0 | 88 | 20 | 0 |
| B2 | 0 | 96 | 12 | 0 |
| B3 | 0 | 93 | 15 | 0 |

Row-normalized:

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 0.00 | 92.59 | 7.41 | 0.00 |
| B1 | 0.00 | 81.48 | 18.52 | 0.00 |
| B2 | 0.00 | 88.89 | 11.11 | 0.00 |
| B3 | 0.00 | 86.11 | 13.89 | 0.00 |
