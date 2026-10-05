# Recording-level results

Metrics are computed per recording: the window probabilities of a recording
are averaged before the argmax. `sd` is the sample standard deviation.

## Per run

| dataset_name | model_name | version | split_id | seed | accuracy | balanced_accuracy | f1_macro | roc_auc_macro | test_loss |
|---|---|---|---|---|---|---|---|---|---|
| cross_cp2_s123_to_cp3_s123_1dcnn | 1dcnn | 1dcnn-06dfe3b | train7-8-10-11-12_val9_test13-14-15-16-17-18 | 42 | 0.2222 | 0.2222 | 0.1479 | 0.6245 | 2.2456 |
| cross_cp2_s123_to_cp3_s123_1dcnn | 1dcnn | 1dcnn-06dfe3b | train7-8-9-10-11_val12_test13-14-15-16-17-18 | 42 | 0.3056 | 0.3056 | 0.1990 | 0.5463 | 2.6973 |
| cross_cp2_s123_to_cp3_s123_1dcnn | 1dcnn | 1dcnn-06dfe3b | train7-8-9-10-12_val11_test13-14-15-16-17-18 | 42 | 0.2361 | 0.2361 | 0.1168 | 0.6613 | 2.1492 |
| cross_cp2_s123_to_cp3_s123_1dcnn | 1dcnn | 1dcnn-06dfe3b | train7-8-9-11-12_val10_test13-14-15-16-17-18 | 42 | 0.3333 | 0.3333 | 0.2427 | 0.6319 | 2.3714 |
| cross_cp2_s123_to_cp3_s123_1dcnn | 1dcnn | 1dcnn-06dfe3b | train7-9-10-11-12_val8_test13-14-15-16-17-18 | 42 | 0.3333 | 0.3333 | 0.2439 | 0.5983 | 2.4718 |
| cross_cp2_s123_to_cp3_s123_1dcnn | 1dcnn | 1dcnn-06dfe3b | train8-9-10-11-12_val7_test13-14-15-16-17-18 | 42 | 0.2917 | 0.2917 | 0.2155 | 0.5972 | 2.9364 |

## Mean ± SD across seeds (one row per split/fold)

| dataset_name | model_name | version | split_id | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cross_cp2_s123_to_cp3_s123_1dcnn | 1dcnn | 1dcnn-06dfe3b | train7-8-10-11-12_val9_test13-14-15-16-17-18 | 1 | 0.2222 |  | 0.2222 |  | 0.1479 |  | 0.6245 |  | 2.2456 |  |
| cross_cp2_s123_to_cp3_s123_1dcnn | 1dcnn | 1dcnn-06dfe3b | train7-8-9-10-11_val12_test13-14-15-16-17-18 | 1 | 0.3056 |  | 0.3056 |  | 0.1990 |  | 0.5463 |  | 2.6973 |  |
| cross_cp2_s123_to_cp3_s123_1dcnn | 1dcnn | 1dcnn-06dfe3b | train7-8-9-10-12_val11_test13-14-15-16-17-18 | 1 | 0.2361 |  | 0.2361 |  | 0.1168 |  | 0.6613 |  | 2.1492 |  |
| cross_cp2_s123_to_cp3_s123_1dcnn | 1dcnn | 1dcnn-06dfe3b | train7-8-9-11-12_val10_test13-14-15-16-17-18 | 1 | 0.3333 |  | 0.3333 |  | 0.2427 |  | 0.6319 |  | 2.3714 |  |
| cross_cp2_s123_to_cp3_s123_1dcnn | 1dcnn | 1dcnn-06dfe3b | train7-9-10-11-12_val8_test13-14-15-16-17-18 | 1 | 0.3333 |  | 0.3333 |  | 0.2439 |  | 0.5983 |  | 2.4718 |  |
| cross_cp2_s123_to_cp3_s123_1dcnn | 1dcnn | 1dcnn-06dfe3b | train8-9-10-11-12_val7_test13-14-15-16-17-18 | 1 | 0.2917 |  | 0.2917 |  | 0.2155 |  | 0.5972 |  | 2.9364 |  |

## Mean ± SD across splits/folds (one row per seed)

| dataset_name | model_name | version | seed | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cross_cp2_s123_to_cp3_s123_1dcnn | 1dcnn | 1dcnn-06dfe3b | 42 | 6 | 0.2870 | 0.0478 | 0.2870 | 0.0478 | 0.1943 | 0.0518 | 0.6099 | 0.0392 | 2.4786 | 0.2938 |

## Mean ± SD across every run (seeds and folds pooled)

| dataset_name | model_name | version | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cross_cp2_s123_to_cp3_s123_1dcnn | 1dcnn | 1dcnn-06dfe3b | 6 | 0.2870 | 0.0478 | 0.2870 | 0.0478 | 0.1943 | 0.0518 | 0.6099 | 0.0392 | 2.4786 | 0.2938 |

### Pooled confusion matrix: cross_cp2_s123_to_cp3_s123_1dcnn / 1dcnn / 1dcnn-06dfe3b

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 3 | 55 | 46 | 4 |
| B1 | 1 | 43 | 62 | 2 |
| B2 | 2 | 32 | 72 | 2 |
| B3 | 3 | 32 | 67 | 6 |

Row-normalized:

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 2.78 | 50.93 | 42.59 | 3.70 |
| B1 | 0.93 | 39.81 | 57.41 | 1.85 |
| B2 | 1.85 | 29.63 | 66.67 | 1.85 |
| B3 | 2.78 | 29.63 | 62.04 | 5.56 |
