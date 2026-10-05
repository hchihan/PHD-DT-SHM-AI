# Recording-level results

Metrics are computed per recording: the window probabilities of a recording
are averaged before the argmax. `sd` is the sample standard deviation.

## Per run

| dataset_name | model_name | version | split_id | seed | accuracy | balanced_accuracy | f1_macro | roc_auc_macro | test_loss |
|---|---|---|---|---|---|---|---|---|---|
| cross_cp3_s123_to_cp2_s123 | resnet1D | resnet1D-06dfe3b | train13-14-15-16-17_val18_test7-8-9-10-11-12 | 42 | 0.1944 | 0.1944 | 0.1105 | 0.3971 | 1.7596 |
| cross_cp3_s123_to_cp2_s123 | resnet1D | resnet1D-06dfe3b | train13-14-15-16-18_val17_test7-8-9-10-11-12 | 42 | 0.1806 | 0.1806 | 0.1284 | 0.4375 | 2.3096 |
| cross_cp3_s123_to_cp2_s123 | resnet1D | resnet1D-06dfe3b | train13-14-15-17-18_val16_test7-8-9-10-11-12 | 42 | 0.2361 | 0.2361 | 0.1596 | 0.5095 | 1.4057 |
| cross_cp3_s123_to_cp2_s123 | resnet1D | resnet1D-06dfe3b | train13-14-16-17-18_val15_test7-8-9-10-11-12 | 42 | 0.2639 | 0.2639 | 0.2166 | 0.5638 | 1.6428 |
| cross_cp3_s123_to_cp2_s123 | resnet1D | resnet1D-06dfe3b | train13-15-16-17-18_val14_test7-8-9-10-11-12 | 42 | 0.2361 | 0.2361 | 0.1620 | 0.5700 | 1.8050 |
| cross_cp3_s123_to_cp2_s123 | resnet1D | resnet1D-06dfe3b | train14-15-16-17-18_val13_test7-8-9-10-11-12 | 42 | 0.1806 | 0.1806 | 0.1066 | 0.4807 | 2.0553 |

## Mean ± SD across seeds (one row per split/fold)

| dataset_name | model_name | version | split_id | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cross_cp3_s123_to_cp2_s123 | resnet1D | resnet1D-06dfe3b | train13-14-15-16-17_val18_test7-8-9-10-11-12 | 1 | 0.1944 |  | 0.1944 |  | 0.1105 |  | 0.3971 |  | 1.7596 |  |
| cross_cp3_s123_to_cp2_s123 | resnet1D | resnet1D-06dfe3b | train13-14-15-16-18_val17_test7-8-9-10-11-12 | 1 | 0.1806 |  | 0.1806 |  | 0.1284 |  | 0.4375 |  | 2.3096 |  |
| cross_cp3_s123_to_cp2_s123 | resnet1D | resnet1D-06dfe3b | train13-14-15-17-18_val16_test7-8-9-10-11-12 | 1 | 0.2361 |  | 0.2361 |  | 0.1596 |  | 0.5095 |  | 1.4057 |  |
| cross_cp3_s123_to_cp2_s123 | resnet1D | resnet1D-06dfe3b | train13-14-16-17-18_val15_test7-8-9-10-11-12 | 1 | 0.2639 |  | 0.2639 |  | 0.2166 |  | 0.5638 |  | 1.6428 |  |
| cross_cp3_s123_to_cp2_s123 | resnet1D | resnet1D-06dfe3b | train13-15-16-17-18_val14_test7-8-9-10-11-12 | 1 | 0.2361 |  | 0.2361 |  | 0.1620 |  | 0.5700 |  | 1.8050 |  |
| cross_cp3_s123_to_cp2_s123 | resnet1D | resnet1D-06dfe3b | train14-15-16-17-18_val13_test7-8-9-10-11-12 | 1 | 0.1806 |  | 0.1806 |  | 0.1066 |  | 0.4807 |  | 2.0553 |  |

## Mean ± SD across splits/folds (one row per seed)

| dataset_name | model_name | version | seed | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cross_cp3_s123_to_cp2_s123 | resnet1D | resnet1D-06dfe3b | 42 | 6 | 0.2153 | 0.0349 | 0.2153 | 0.0349 | 0.1473 | 0.0413 | 0.4931 | 0.0687 | 1.8297 | 0.3167 |

## Mean ± SD across every run (seeds and folds pooled)

| dataset_name | model_name | version | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cross_cp3_s123_to_cp2_s123 | resnet1D | resnet1D-06dfe3b | 6 | 0.2153 | 0.0349 | 0.2153 | 0.0349 | 0.1473 | 0.0413 | 0.4931 | 0.0687 | 1.8297 | 0.3167 |

### Pooled confusion matrix: cross_cp3_s123_to_cp2_s123 / resnet1D / resnet1D-06dfe3b

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 0 | 32 | 48 | 28 |
| B1 | 1 | 28 | 51 | 28 |
| B2 | 1 | 44 | 47 | 16 |
| B3 | 4 | 52 | 34 | 18 |

Row-normalized:

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 0.00 | 29.63 | 44.44 | 25.93 |
| B1 | 0.93 | 25.93 | 47.22 | 25.93 |
| B2 | 0.93 | 40.74 | 43.52 | 14.81 |
| B3 | 3.70 | 48.15 | 31.48 | 16.67 |
