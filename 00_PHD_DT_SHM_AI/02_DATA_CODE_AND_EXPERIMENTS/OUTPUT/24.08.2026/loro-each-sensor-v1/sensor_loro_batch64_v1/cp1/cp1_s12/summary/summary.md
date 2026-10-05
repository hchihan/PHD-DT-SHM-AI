# Recording-level results

Metrics are computed per recording: the window probabilities of a recording
are averaged before the argmax. `sd` is the sample standard deviation.

## Per run

| dataset_name | model_name | version | split_id | seed | accuracy | balanced_accuracy | f1_macro | roc_auc_macro | test_loss |
|---|---|---|---|---|---|---|---|---|---|
| cp1_s12 | resnet1D | resnet1D-843fbf2 | train1-2-3-4_val5_test6 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.3519 |
| cp1_s12 | resnet1D | resnet1D-843fbf2 | train1-2-3-4_val6_test5 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.3324 |
| cp1_s12 | resnet1D | resnet1D-843fbf2 | train1-2-3-5_val4_test6 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.3773 |
| cp1_s12 | resnet1D | resnet1D-843fbf2 | train1-2-3-5_val6_test4 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2882 |
| cp1_s12 | resnet1D | resnet1D-843fbf2 | train1-2-3-6_val4_test5 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.3576 |
| cp1_s12 | resnet1D | resnet1D-843fbf2 | train1-2-3-6_val5_test4 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.3057 |
| cp1_s12 | resnet1D | resnet1D-843fbf2 | train1-2-4-5_val3_test6 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.3556 |
| cp1_s12 | resnet1D | resnet1D-843fbf2 | train1-2-4-5_val6_test3 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.3248 |
| cp1_s12 | resnet1D | resnet1D-843fbf2 | train1-2-4-6_val3_test5 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.3623 |
| cp1_s12 | resnet1D | resnet1D-843fbf2 | train1-2-4-6_val5_test3 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.3338 |
| cp1_s12 | resnet1D | resnet1D-843fbf2 | train1-2-5-6_val3_test4 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2966 |
| cp1_s12 | resnet1D | resnet1D-843fbf2 | train1-2-5-6_val4_test3 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2860 |
| cp1_s12 | resnet1D | resnet1D-843fbf2 | train1-3-4-5_val2_test6 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.3504 |
| cp1_s12 | resnet1D | resnet1D-843fbf2 | train1-3-4-5_val6_test2 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.3417 |
| cp1_s12 | resnet1D | resnet1D-843fbf2 | train1-3-4-6_val2_test5 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.3431 |
| cp1_s12 | resnet1D | resnet1D-843fbf2 | train1-3-4-6_val5_test2 | 42 | 0.9167 | 0.9167 | 0.9143 | 0.9815 | 0.3934 |
| cp1_s12 | resnet1D | resnet1D-843fbf2 | train1-3-5-6_val2_test4 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2904 |
| cp1_s12 | resnet1D | resnet1D-843fbf2 | train1-3-5-6_val4_test2 | 42 | 0.9167 | 0.9167 | 0.9143 | 0.9907 | 0.3392 |
| cp1_s12 | resnet1D | resnet1D-843fbf2 | train1-4-5-6_val2_test3 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.2873 |
| cp1_s12 | resnet1D | resnet1D-843fbf2 | train1-4-5-6_val3_test2 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.3304 |
| cp1_s12 | resnet1D | resnet1D-843fbf2 | train2-3-4-5_val1_test6 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.3637 |
| cp1_s12 | resnet1D | resnet1D-843fbf2 | train2-3-4-5_val6_test1 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.4049 |
| cp1_s12 | resnet1D | resnet1D-843fbf2 | train2-3-4-6_val1_test5 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.3707 |
| cp1_s12 | resnet1D | resnet1D-843fbf2 | train2-3-4-6_val5_test1 | 42 | 0.8333 | 0.8333 | 0.8286 | 1.0000 | 0.4200 |
| cp1_s12 | resnet1D | resnet1D-843fbf2 | train2-3-5-6_val1_test4 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.4119 |
| cp1_s12 | resnet1D | resnet1D-843fbf2 | train2-3-5-6_val4_test1 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.4459 |
| cp1_s12 | resnet1D | resnet1D-843fbf2 | train2-4-5-6_val1_test3 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.3568 |
| cp1_s12 | resnet1D | resnet1D-843fbf2 | train2-4-5-6_val3_test1 | 42 | 1.0000 | 1.0000 | 1.0000 | 0.9907 | 0.4082 |
| cp1_s12 | resnet1D | resnet1D-843fbf2 | train3-4-5-6_val1_test2 | 42 | 0.9167 | 0.9167 | 0.9143 | 0.9907 | 0.4043 |
| cp1_s12 | resnet1D | resnet1D-843fbf2 | train3-4-5-6_val2_test1 | 42 | 0.8333 | 0.8333 | 0.8286 | 1.0000 | 0.4386 |

## Mean ± SD across seeds (one row per split/fold)

| dataset_name | model_name | version | split_id | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp1_s12 | resnet1D | resnet1D-843fbf2 | train1-2-3-4_val5_test6 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.3519 |  |
| cp1_s12 | resnet1D | resnet1D-843fbf2 | train1-2-3-4_val6_test5 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.3324 |  |
| cp1_s12 | resnet1D | resnet1D-843fbf2 | train1-2-3-5_val4_test6 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.3773 |  |
| cp1_s12 | resnet1D | resnet1D-843fbf2 | train1-2-3-5_val6_test4 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2882 |  |
| cp1_s12 | resnet1D | resnet1D-843fbf2 | train1-2-3-6_val4_test5 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.3576 |  |
| cp1_s12 | resnet1D | resnet1D-843fbf2 | train1-2-3-6_val5_test4 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.3057 |  |
| cp1_s12 | resnet1D | resnet1D-843fbf2 | train1-2-4-5_val3_test6 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.3556 |  |
| cp1_s12 | resnet1D | resnet1D-843fbf2 | train1-2-4-5_val6_test3 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.3248 |  |
| cp1_s12 | resnet1D | resnet1D-843fbf2 | train1-2-4-6_val3_test5 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.3623 |  |
| cp1_s12 | resnet1D | resnet1D-843fbf2 | train1-2-4-6_val5_test3 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.3338 |  |
| cp1_s12 | resnet1D | resnet1D-843fbf2 | train1-2-5-6_val3_test4 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2966 |  |
| cp1_s12 | resnet1D | resnet1D-843fbf2 | train1-2-5-6_val4_test3 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2860 |  |
| cp1_s12 | resnet1D | resnet1D-843fbf2 | train1-3-4-5_val2_test6 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.3504 |  |
| cp1_s12 | resnet1D | resnet1D-843fbf2 | train1-3-4-5_val6_test2 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.3417 |  |
| cp1_s12 | resnet1D | resnet1D-843fbf2 | train1-3-4-6_val2_test5 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.3431 |  |
| cp1_s12 | resnet1D | resnet1D-843fbf2 | train1-3-4-6_val5_test2 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 0.9815 |  | 0.3934 |  |
| cp1_s12 | resnet1D | resnet1D-843fbf2 | train1-3-5-6_val2_test4 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2904 |  |
| cp1_s12 | resnet1D | resnet1D-843fbf2 | train1-3-5-6_val4_test2 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 0.9907 |  | 0.3392 |  |
| cp1_s12 | resnet1D | resnet1D-843fbf2 | train1-4-5-6_val2_test3 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.2873 |  |
| cp1_s12 | resnet1D | resnet1D-843fbf2 | train1-4-5-6_val3_test2 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.3304 |  |
| cp1_s12 | resnet1D | resnet1D-843fbf2 | train2-3-4-5_val1_test6 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.3637 |  |
| cp1_s12 | resnet1D | resnet1D-843fbf2 | train2-3-4-5_val6_test1 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.4049 |  |
| cp1_s12 | resnet1D | resnet1D-843fbf2 | train2-3-4-6_val1_test5 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.3707 |  |
| cp1_s12 | resnet1D | resnet1D-843fbf2 | train2-3-4-6_val5_test1 | 1 | 0.8333 |  | 0.8333 |  | 0.8286 |  | 1.0000 |  | 0.4200 |  |
| cp1_s12 | resnet1D | resnet1D-843fbf2 | train2-3-5-6_val1_test4 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.4119 |  |
| cp1_s12 | resnet1D | resnet1D-843fbf2 | train2-3-5-6_val4_test1 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.4459 |  |
| cp1_s12 | resnet1D | resnet1D-843fbf2 | train2-4-5-6_val1_test3 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.3568 |  |
| cp1_s12 | resnet1D | resnet1D-843fbf2 | train2-4-5-6_val3_test1 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.9907 |  | 0.4082 |  |
| cp1_s12 | resnet1D | resnet1D-843fbf2 | train3-4-5-6_val1_test2 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 0.9907 |  | 0.4043 |  |
| cp1_s12 | resnet1D | resnet1D-843fbf2 | train3-4-5-6_val2_test1 | 1 | 0.8333 |  | 0.8333 |  | 0.8286 |  | 1.0000 |  | 0.4386 |  |

## Mean ± SD across splits/folds (one row per seed)

| dataset_name | model_name | version | seed | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp1_s12 | resnet1D | resnet1D-843fbf2 | 42 | 30 | 0.9444 | 0.0505 | 0.9444 | 0.0505 | 0.9429 | 0.0520 | 0.9985 | 0.0043 | 0.3558 | 0.0454 |

## Mean ± SD across every run (seeds and folds pooled)

| dataset_name | model_name | version | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp1_s12 | resnet1D | resnet1D-843fbf2 | 30 | 0.9444 | 0.0505 | 0.9444 | 0.0505 | 0.9429 | 0.0520 | 0.9985 | 0.0043 | 0.3558 | 0.0454 |

### Pooled confusion matrix: cp1_s12 / resnet1D / resnet1D-843fbf2

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 87 | 3 | 0 | 0 |
| B1 | 1 | 89 | 0 | 0 |
| B2 | 0 | 0 | 84 | 6 |
| B3 | 0 | 0 | 10 | 80 |

Row-normalized:

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 96.67 | 3.33 | 0.00 | 0.00 |
| B1 | 1.11 | 98.89 | 0.00 | 0.00 |
| B2 | 0.00 | 0.00 | 93.33 | 6.67 |
| B3 | 0.00 | 0.00 | 11.11 | 88.89 |
