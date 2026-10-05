# Selecting Run permutations worth training, with Support Points / SPlit

## 1. The problem

Each campaign holds six Runs. A split assigns four to training, one to validation and one to test, so a split is fully described by the ordered pair (validation Run, test Run):

```
6 × 5 = 30 splits per campaign
30 × 4 campaigns × 3 seeds = 360 training runs
```

360 runs to answer one question is not a budget problem alone — it is an information problem. Most of those 30 splits are near-duplicates, so the budget buys repetition rather than coverage. Two facts make this concrete:

- A test Run is 12 recordings, so recording-level balanced accuracy moves in steps of 1/12 ≈ 8.3%.
- Measured on this data, re-seeding one fixed split moves the test score with sd ≈ 0.065 — larger than the sd across different splits (0.054).

So ranking 30 splits by score is largely ranking noise. What is needed instead is a principled way to pick a handful of splits that reproduce what all 30 would have told us.

## 2. Background: energy distance and support points

Energy distance (Székely & Rizzo) between two point sets:

```
E(X, Y) = 2/(nm) Σ_ij ‖x_i − y_j‖
        − 1/n² Σ_ii' ‖x_i − x_i'‖
        − 1/m² Σ_jj' ‖y_j − y_j'‖
```

E(X, Y) ≥ 0, with equality iff the two distributions coincide. That "iff" is the reason to use it here: it compares whole distributions, not a few moments, so a subset cannot score well by matching the mean while missing the spread or the shape.

**Support points** (Mak & Joseph) use it to answer exactly the subset question: given a point set X, find a small subset that best represents the distribution of X, by minimising the energy distance between the subset and X. The paper proves the resulting points converge to the underlying distribution.

**SPlit** (Joseph & Vakayil, arXiv:2012.10945) applies support points directly to train/test selection: choose the testing set so that it mirrors the distribution of the full data. The paper reports improved worst-case testing performance against random splitting across several models.

## 3. Adapting it: the Run is the atom, not the window

SPlit as published selects individual points. That cannot be done here.

- Windows inside one recording overlap — window 400 samples, hop 200 — so two windows from the same recording share half their samples.
- Recordings inside one Run share a session, an instrumentation and a mounting.

Selecting at the point level would put overlapping windows on both sides of the train/test boundary. The test score would then measure memorisation, not generalisation. The split has to happen at Run granularity or it leaks.

The adaptation keeps energy distance measured on the window distribution — that is the distribution the model actually sees — while the selection operates one level up, over Runs. Concretely, for a split with test Run `t`, validation Run `v` and train Runs `T`:

| Criterion | Definition | What it says |
| --- | --- | --- |
| e_test | E(windows of t, all windows) | The SPlit criterion itself. Small ⇒ the test Run mirrors the campaign, so its score estimates real performance rather than performance on one unusual Run. |
| e_val | E(windows of v, all windows) | Same, for the model-selection Run. |
| e_train | E(windows of T, all windows) | Whether the training set still represents the campaign after two Runs are removed. |
| e_gap | E(windows of T, windows of t) | The distance the model must actually generalise across. This is what the paper's worst-case claim is about. |

## 4. Point representation

Energy distance needs a metric space, so a window must become a vector. Each window is:

- **z-scored per channel** — the same normalisation `train_ddp_npz.py::load_runs` applies, so the geometry matches what the model sees;
- **Hann-windowed, real-FFT'd**, and reduced to 20 log-power bands per channel (160 dims for CP1's 8 channels, 240 for the 12-channel campaigns);
- **standardised across its own dimensions**, so distance compares spectral shape rather than overall level — level is hammer strength, not a property of the campaign.

Two reasons the spectral reduction is not optional:

1. Euclidean distance between raw waveforms is dominated by phase alignment, which is an artefact of where the window happened to start. Band power is invariant to it.
2. At 400 × C dimensions with a few thousand windows, concentration of measure puts nearly every pair at the same distance, and an energy distance computed there cannot discriminate between subsets.

## 5. The algorithm

### Step 1 — cache the pairwise distances (`01_window_features.py`)

```
for each campaign:
    F ← band_power(all windows)          # (N, C·20)
    D ← pairwise Euclidean distances of F # (N, N)
    cache D, run_id, label
```

Every energy distance downstream is a mean over a submatrix of D, so the expensive part runs exactly once per campaign. N is 1,746–3,065, so D is at most ~9.4 M entries.

### Step 2 — score every split (`02_select_splits.py`)

```
for each ordered pair (v, t) of distinct Runs:
    T      ← the remaining four Runs
    e_test  ← energy(idx[t], all)
    e_val   ← energy(idx[v], all)
    e_train ← energy(idx[T], all)
    e_gap   ← energy(idx[T], idx[t])
```

where `energy(a, b) = 2·mean(D[a,b]) − mean(D[a,a]) − mean(D[b,b])`.

### Step 3 — select by role

One split cannot serve three purposes, so three are chosen by three different rules:

```
representative ← argmin over splits of e_test   # SPlit-optimal
worst_case     ← argmax over splits of e_gap    # largest domain shift
coverage       ← support points of the 30 splits themselves
```

For the coverage role, each split becomes a point in the four-dimensional space (e_test, e_val, e_train, e_gap), standardised per dimension — without that, the four criteria sit on different scales and the selection would be driven by e_gap alone.

Selection is greedy:

```
chosen ← [representative, worst_case]   # forced: each earns its place
while |chosen| < budget:
    chosen ← chosen + argmin over remaining i of E(P[chosen ∪ {i}], P)
```

Greedy rather than the paper's continuous optimisation because the candidate set is 30 discrete splits, not a region of Rᵈ — there is nowhere to move a point to. The forced members are kept because an extremum is not something a representativeness criterion will select on its own; that is precisely why they are reported separately.

### Complexity

Step 1 is O(N² · d) per campaign and dominates the runtime. Steps 2 and 3 are submatrix means over the cached D plus a 30 × 30 distance matrix, both negligible.

## 6. Results

Six chosen splits represent all 30 roughly 2.3–2.6× better than six drawn at random — energy distance between the selected subset and the full 30, lower is better:

| Campaign | Support points | 6 at random (mean of 200) | Improvement |
| --- | --- | --- | --- |
| cp1 | 0.1621 | 0.3650 | 2.25× |
| cp2_21 | 0.1551 | 0.3526 | 2.27× |
| cp2_2122 | 0.1397 | 0.3604 | 2.58× |
| cp3 | 0.1387 | 0.3475 | 2.50× |

Budget: 360 → 72 training runs at three seeds.

### Splits worth running

| Campaign | representative | worst_case | coverage |
| --- | --- | --- | --- |
| cp1 | val R1 / test R3 | val R2 / test R1 | R2/R4, R5/R6, R6/R1, R6/R2 |
| cp2_21 | val R7 / test R10 | val R12 / test R9 | R7/R9, R8/R7, R9/R8, R11/R10 |
| cp2_2122 | val R7 / test R11 | val R11 / test R9 | R7/R8, R8/R7, R8/R12, R9/R8 |
| cp3 | val R13 / test R16 | val R17 / test R18 | R14/R15, R17/R13, R17/R14, R18/R13 |

Report the **representative** score as the headline and the **worst_case** score beside it as the lower bound. The coverage splits exist so that the spread between those two is measured rather than assumed.

### What the numbers show

**CP3 is an order of magnitude more scattered than the others.** Its per-Run e_test is 0.071–0.122 against 0.011–0.041 for CP1 and CP2, and its worst-case e_gap is 0.2357 against CP1's 0.0365 — 6.5× larger. Its Runs simply do not agree with each other. This is an independent confirmation of what the fingerprint statistics said (Fisher ratio 0.005–0.010, negative class-geometry correlation between Runs), and it predicts near-chance test scores.

**The training side carries no selection signal.** e_train varies only over 0.0013–0.0026 in CP1: any four of six Runs represent the campaign about equally well. All the discriminating power is in which Run is held out for test. This matches what an actual training sweep showed earlier — a Run characteristic correlated with the score at r = 0.82 when that Run was the test Run, but |r| ≤ 0.44 when it was the validation Run. It also means the validation dimension of the split space can be collapsed if the budget needs cutting further.

The exception is CP3, where e_train jumps to 0.0185–0.0209 for two splits (test R18, test R15) against ~0.003 elsewhere: removing R15 or R18 measurably damages how well the training set represents the campaign. Another sign that CP3's Runs are not interchangeable.

## 7. Running it

```bash
python3 experiments/01_window_features.py            # → cache/<campaign>.npz
python3 experiments/02_select_splits.py --budget 6   # → selected_splits.json
```

`--budget` controls how many splits survive per campaign. Setting it to 30 selects everything and the coverage figure goes to 0, which is a useful sanity check on the implementation.

## 8. Files

| File | Role |
| --- | --- |
| `01_window_features.py` | Windows → log band power → cached pairwise distance matrix |
| `02_select_splits.py` | Energy distance for all 30 splits, support-point selection → selected_splits.json |
| `selected_splits.json` | Per-campaign scores, roles and coverage statistics |
| `cache/` | Distance matrices (regenerable, git-ignored) |

## References

- Mak & Joseph, *Support Points*, Annals of Statistics 46(6A), 2018.
- Joseph & Vakayil, *SPlit: An Optimal Method for Data Splitting*, arXiv:2012.10945.
- Székely & Rizzo, *Energy statistics: A class of statistics based on distances*, Journal of Statistical Planning and Inference 143(8), 2013.

---

*Nguồn: [Notion page](https://typhoon-storm-ff4.notion.site/Selecting-Run-permutations-worth-training-with-Support-Points-SPlit-3c04e1a58f8c8052b742d9b708690056)*
