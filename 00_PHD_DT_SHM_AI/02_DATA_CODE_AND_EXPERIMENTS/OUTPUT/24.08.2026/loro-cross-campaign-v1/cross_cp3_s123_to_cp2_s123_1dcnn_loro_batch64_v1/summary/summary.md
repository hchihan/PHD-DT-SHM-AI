# Recording-level results

Metrics are computed per recording: the window probabilities of a recording
are averaged before the argmax. `sd` is the sample standard deviation.

## Per run

| dataset_name | model_name | version | split_id | seed | accuracy | balanced_accuracy | f1_macro | roc_auc_macro | test_loss |
|---|---|---|---|---|---|---|---|---|---|
| cross_cp3_s123_to_cp2_s123_1dcnn | 1dcnn | 1dcnn-06dfe3b | train13-14-15-16-17_val18_test7-8-9-10-11-12 | 42 | 0.3056 | 0.3056 | 0.2288 | 0.6469 | 1.3674 |
| cross_cp3_s123_to_cp2_s123_1dcnn | 1dcnn | 1dcnn-06dfe3b | train13-14-15-16-18_val17_test7-8-9-10-11-12 | 42 | 0.3056 | 0.3056 | 0.2360 | 0.5795 | 1.4198 |
| cross_cp3_s123_to_cp2_s123_1dcnn | 1dcnn | 1dcnn-06dfe3b | train13-14-15-17-18_val16_test7-8-9-10-11-12 | 42 | 0.2778 | 0.2778 | 0.1702 | 0.5774 | 1.4044 |
| cross_cp3_s123_to_cp2_s123_1dcnn | 1dcnn | 1dcnn-06dfe3b | train13-14-16-17-18_val15_test7-8-9-10-11-12 | 42 | 0.2500 | 0.2500 | 0.1370 | 0.5802 | 1.4322 |
| cross_cp3_s123_to_cp2_s123_1dcnn | 1dcnn | 1dcnn-06dfe3b | train13-15-16-17-18_val14_test7-8-9-10-11-12 | 42 | 0.3611 | 0.3611 | 0.2804 | 0.6168 | 1.3744 |
| cross_cp3_s123_to_cp2_s123_1dcnn | 1dcnn | 1dcnn-06dfe3b | train14-15-16-17-18_val13_test7-8-9-10-11-12 | 42 | 0.3056 | 0.3056 | 0.3120 | 0.5224 | 1.4850 |

## Mean ± SD across seeds (one row per split/fold)

| dataset_name | model_name | version | split_id | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cross_cp3_s123_to_cp2_s123_1dcnn | 1dcnn | 1dcnn-06dfe3b | train13-14-15-16-17_val18_test7-8-9-10-11-12 | 1 | 0.3056 |  | 0.3056 |  | 0.2288 |  | 0.6469 |  | 1.3674 |  |
| cross_cp3_s123_to_cp2_s123_1dcnn | 1dcnn | 1dcnn-06dfe3b | train13-14-15-16-18_val17_test7-8-9-10-11-12 | 1 | 0.3056 |  | 0.3056 |  | 0.2360 |  | 0.5795 |  | 1.4198 |  |
| cross_cp3_s123_to_cp2_s123_1dcnn | 1dcnn | 1dcnn-06dfe3b | train13-14-15-17-18_val16_test7-8-9-10-11-12 | 1 | 0.2778 |  | 0.2778 |  | 0.1702 |  | 0.5774 |  | 1.4044 |  |
| cross_cp3_s123_to_cp2_s123_1dcnn | 1dcnn | 1dcnn-06dfe3b | train13-14-16-17-18_val15_test7-8-9-10-11-12 | 1 | 0.2500 |  | 0.2500 |  | 0.1370 |  | 0.5802 |  | 1.4322 |  |
| cross_cp3_s123_to_cp2_s123_1dcnn | 1dcnn | 1dcnn-06dfe3b | train13-15-16-17-18_val14_test7-8-9-10-11-12 | 1 | 0.3611 |  | 0.3611 |  | 0.2804 |  | 0.6168 |  | 1.3744 |  |
| cross_cp3_s123_to_cp2_s123_1dcnn | 1dcnn | 1dcnn-06dfe3b | train14-15-16-17-18_val13_test7-8-9-10-11-12 | 1 | 0.3056 |  | 0.3056 |  | 0.3120 |  | 0.5224 |  | 1.4850 |  |

## Mean ± SD across splits/folds (one row per seed)

| dataset_name | model_name | version | seed | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cross_cp3_s123_to_cp2_s123_1dcnn | 1dcnn | 1dcnn-06dfe3b | 42 | 6 | 0.3009 | 0.0369 | 0.3009 | 0.0369 | 0.2274 | 0.0656 | 0.5872 | 0.0420 | 1.4139 | 0.0430 |

## Mean ± SD across every run (seeds and folds pooled)

| dataset_name | model_name | version | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cross_cp3_s123_to_cp2_s123_1dcnn | 1dcnn | 1dcnn-06dfe3b | 6 | 0.3009 | 0.0369 | 0.3009 | 0.0369 | 0.2274 | 0.0656 | 0.5872 | 0.0420 | 1.4139 | 0.0430 |

### Pooled confusion matrix: cross_cp3_s123_to_cp2_s123_1dcnn / 1dcnn / 1dcnn-06dfe3b

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 26 | 16 | 6 | 60 |
| B1 | 28 | 15 | 5 | 60 |
| B2 | 17 | 27 | 6 | 58 |
| B3 | 10 | 13 | 2 | 83 |

Row-normalized:

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 24.07 | 14.81 | 5.56 | 55.56 |
| B1 | 25.93 | 13.89 | 4.63 | 55.56 |
| B2 | 15.74 | 25.00 | 5.56 | 53.70 |
| B3 | 9.26 | 12.04 | 1.85 | 76.85 |
