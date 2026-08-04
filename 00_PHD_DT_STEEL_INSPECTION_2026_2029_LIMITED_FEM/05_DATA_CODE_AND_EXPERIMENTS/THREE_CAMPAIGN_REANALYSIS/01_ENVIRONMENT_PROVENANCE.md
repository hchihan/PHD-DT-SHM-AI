# 01_ENVIRONMENT_PROVENANCE

**Scope:** RQ1 → WP1 → Chapter 4 → Paper 1 → Evidence Gate 1 (candidate, laboratory evidence only). Not a field-diagnosis result. Not a Gate 1 closure.

## Framework audit (Section 5 of the task spec)

Two standard deep-learning frameworks were checked, per protocol, before any 1D-CNN result was produced.

| Framework | Result |
|---|---|
| PyTorch | Not installed at session start. A prior session in this same project (`PIPELINE_REPLICATION_BLOCKER_REPORT.md`, `POSITIVE_CONTROL_BLOCKER_REPORT.md`, both in `DATA_ALL_3_CAMPAIGN/`) documented that the standard Linux PyPI wheel for any current `torch` version unconditionally attempts to preload ~15 CUDA runtime shared libraries at `import torch` time regardless of GPU presence, and that `download.pytorch.org/whl/cpu` (the CPU-only index that avoids this) is proxy-blocked from this sandbox. Not re-attempted in this session since TensorFlow (below) resolved the framework requirement. |
| TensorFlow / Keras | **Working.** `tensorflow-cpu==2.21.0` (Keras 3.12.3) was downloaded directly from `files.pythonhosted.org` (273.6 MB wheel, resumable `curl -C -`, SHA256-verified via `zipfile.testzip()`), installed with `pip install --break-system-packages`, and verified with a real forward pass + one `model.fit` training step on CPU before use. `tf.config.list_physical_devices('GPU')` = `[]` (CPU-only, consistent with this sandbox). |

**Conclusion:** a standard framework (TensorFlow/Keras) imports and trains stably in this environment. `DEEP_LEARNING_ENVIRONMENT_BLOCKER.md` was therefore **not** created; the compact 1D-CNN baseline was run with `tf.keras`, not a hand-written NumPy engine.

## Software versions

| Component | Version |
|---|---|
| Python | 3.10.12 |
| OS | Linux 6.8.0-124-generic x86_64 (Ubuntu-based sandbox) |
| CPU / GPU | 2 vCPUs, 3.8 GiB RAM, no GPU |
| numpy | 2.2.6 |
| pandas | 2.3.3 |
| scipy | 1.15.3 |
| scikit-learn | 1.7.2 |
| tensorflow-cpu | 2.21.0 |
| keras | 3.12.3 |

## Seeds

`seed=42` was used for every result reported as the **main** fixed-baseline result (feature models: `random_state=42`; CNN: `tf.keras.utils.set_random_seed(42)`). Seeds `123` and `2026` (the task's minimum 3-seed requirement) were **not** run for the CNN family in this session — see `15_NEXT_ANALYSIS_RECOMMENDATION.md`. RF's own internal bootstrap randomness under a fixed `random_state` is deterministic given the seed; SVM/LogReg are deterministic given the seed and solver.

## Code hashes (reproducibility)

| Script | SHA256 |
|---|---|
| build_registry.py | `8c8e335b2163d20dbac92a1e395bb7a9cb835313efad22105acaa1ffe2540a6d` |
| build_data_cache.py | `46f879bcf4e803987cedf23828980425c7add16049d9682a183113c4cb610832` |
| pipeline_lib.py | `7efbf379b845d0d54cda1023df9aaa7464f7c90b97c1ef644f3bd79663791713` |
| run_feature_baselines.py | `dac220690d48ed7dad22789715d372347055b16a74d3566c4c9bfa91ab6213d0` |
| run_cnn.py | `d0afcb5b60202f96f86af6758fae71e347ec0321aae30cfe8022a7204c855fec` |
| run_permutation_control.py | `383b00709a6e9fe5f503afd570469b736aaffb030ec79bfcf548dd7403f849d8` |
| run_sensitivity.py | `ae77cb3ca2b681b23e299a2efe64a1830f4ec1163d0c65829356eb41192be5b0` |
| assemble_outputs.py | `dc10612ca36e265d1cdfc9d4cc3a551d67edef9a7f639f59ca0011ee1d820827` |

(SHA256 values as printed by `sha256sum` in this session; truncate/verify against the copies shipped alongside this report if re-running.)

## Rerun conditions

All source CSVs are opened **read-only**; none were modified, renamed, or moved. Re-running `build_registry.py` → `build_data_cache.py` → `run_feature_baselines.py` → `run_cnn.py` → `run_permutation_control.py` → `run_sensitivity.py` → `assemble_outputs.py`, in that order, against the same three raw campaign folders should reproduce every CSV in this package bit-for-bit for the feature-baseline and permutation results (fully deterministic given `seed=42`), and closely (not bit-for-bit, CPU floating-point/thread-scheduling dependent) for the TensorFlow CNN results.
