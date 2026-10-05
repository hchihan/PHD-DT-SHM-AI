# sensor_position_permutation_synchronization_notion

## 1. Method / Algorithm

The problem is formulated as a **sensor permutation recovery problem**.

Each CSV file contains signals recorded from several physical sensor locations. However, in some files, the sensor channels may have been assigned to the wrong positions. For example:

$$[S_1, S_2, S_3] \rightarrow [S_2, S_1, S_3]$$

The proposed method consists of three main steps.

---

### Step 1 — Sensor Fingerprint Extraction

For each sensor channel, extract signal characteristics that are expected to depend on the physical sensor location.

Possible features include:
- Power Spectral Density (PSD)
- dominant frequencies
- normalized spectral shape
- cross-spectral features
- coherence
- Frequency Response Function (FRF), if the excitation force is available

Each sensor channel is represented by a feature vector $x_{i,s}$ where $i$ is the CSV file and $s$ is the sensor channel.

---

### Step 2 — Pairwise Sensor Matching

For every pair of CSV files, compare the sensor fingerprints and construct a distance matrix:

$$C_{ij} = \begin{bmatrix} d(S_{i1}, S_{j1}) & d(S_{i1}, S_{j2}) & d(S_{i1}, S_{j3}) \\ d(S_{i2}, S_{j1}) & d(S_{i2}, S_{j2}) & d(S_{i2}, S_{j3}) \\ d(S_{i3}, S_{j1}) & d(S_{i3}, S_{j2}) & d(S_{i3}, S_{j3}) \end{bmatrix}$$

The sensor permutation with the minimum total matching cost is selected:

$$\hat{P}_{ij} = \arg\min_{P \in S_3} \text{Cost}(P)$$

With three sensors, there are only $3! = 6$ possible permutations. Therefore, all possible sensor assignments can be evaluated exhaustively, and the pairwise matching problem can be solved exactly.

---

### Step 3 — Global Permutation Synchronization

Pairwise matches may contain errors due to noise or similar signal characteristics.

Therefore, instead of comparing every file with only one reference file, all pairwise sensor mappings are combined using **Permutation Synchronization**.

Let $P_i$ represent the unknown sensor ordering of file $i$. Ideally:

$$P_{ij} = P_j P_i^{-1}$$

Permutation Synchronization estimates $P_1, P_2, \ldots, P_N$ such that the recovered sensor assignments are globally consistent with the pairwise measurements.

The final output identifies:
- files with the correct sensor order,
- files with swapped sensor positions,
- the permutation required to correct each file,
- files with low confidence that require manual inspection.

---

## 2. What Has Already Been Proven, and What Must Be Proven by Us?

The complete method can be separated into two parts:

$$\text{Vibration signals} \xrightarrow{A} \text{Pairwise sensor permutations} \xrightarrow{B} \text{Global sensor permutations}$$

### Part B — Already Supported by Published Theory

The second part, **Permutation Synchronization**, is an established research problem. It is not necessary to develop or prove a new synchronization algorithm from scratch.

**Pachauri et al., NeurIPS 2013**
*"Solving the Multi-way Matching Problem by Permutation Synchronization"*
This paper introduced a permutation-synchronization framework for recovering globally consistent object correspondences from noisy pairwise permutation estimates. The formulation $P_{ij} \approx P_j P_i^{-1}$ is directly applicable to the sensor-ordering problem.

**Chen et al., ICML 2014**
*"Near-Optimal Joint Object Matching via Convex Relaxation"*
This work introduced the MatchLift method and provided theoretical recovery guarantees under the corruption model and assumptions defined in the paper. It demonstrates that globally consistent correspondences can still be recovered even when some pairwise matches are incorrect.

**Ling, 2020/2021**
*"Near-Optimal Performance Bounds for Orthogonal and Permutation Group Synchronization via Spectral Methods"*
This work provides theoretical performance bounds for spectral permutation synchronization. Under the noise and corruption assumptions considered in the paper, exact recovery of the hidden permutations is possible when the signal-to-noise ratio is sufficiently high.

**Nguyen and Zhang, 2023**
*"A Novel and Optimal Spectral Method for Permutation Synchronization"*
This paper provides further theoretical guarantees and statistical error bounds for permutation synchronization using spectral methods.

### Therefore, What Has Already Been Proven?

Previous research already provides theoretical support for:

$$\text{Noisy pairwise permutation estimates} \rightarrow \text{Recovery of globally consistent hidden permutations}$$

Therefore, the mathematical backend used to combine pairwise sensor mappings does not need to be proven again. The existing algorithms and their theoretical guarantees can be cited directly, provided that the assumptions of the selected method are clearly stated and checked against the experimental setting.

---

## 3. What Must Be Proven by Us?

The part that is specific to our dataset is:

$$\text{Vibration signals} \rightarrow \text{Correct sensor correspondence}$$

Existing permutation-synchronization papers do not prove that the vibration signals measured at our physical sensor locations are sufficiently different to identify:
- **S1** — Apex,
- **S2** — Beam–Column,
- **S3** — Brace.

Therefore, we must experimentally validate that the selected signal fingerprints, such as PSD, FRF, coherence, or spectral features, can reliably distinguish the physical sensor locations.

We must also validate the performance of the complete method on our dataset.

---

## 4. Experimental Validation Required

A controlled sensor-permutation experiment should be performed.

Starting from files with known or manually verified sensor assignments, artificial sensor swaps are introduced. For example:
- $123 \rightarrow 213$
- $123 \rightarrow 132$
- $123 \rightarrow 321$

The algorithm is then applied to recover the injected permutation. The recovered permutation $P_\text{recovered}$ is compared with the known ground-truth permutation $P_\text{ground truth}$.

The following metrics should be reported:
- Exact Permutation Recovery Rate
- Sensor-wise Accuracy
- Sensitivity
- Specificity
- False Positive Rate
- Confidence of the recovered permutation

Robustness should also be evaluated under different levels of artificial corruption, for example: $5\%, 10\%, 20\%, 30\%, 40\%$ of files containing intentionally swapped sensor positions.

---

## 5. Final Conclusion

The proposed approach does not require us to invent a completely new algorithm.

The Permutation Synchronization component already has published theoretical foundations and recovery guarantees.

However, we must demonstrate that the vibration-derived sensor fingerprints provide sufficiently reliable pairwise sensor correspondences for our dataset.

Therefore, the part already supported by previous research is:

$$\text{Pairwise permutations} \rightarrow \text{Globally consistent permutations}$$

The part that must be validated by us is:

$$\text{Vibration signals} \rightarrow \text{Reliable sensor permutations}$$

and, at the complete-system level:

$$\text{Complete method} \rightarrow \text{Reliable detection and correction of sensor-position mislabeling in the 72 CSV files}$$

---

## References

1. Pachauri, D., Kondor, R., and Singh, V. (2013). Solving the Multi-way Matching Problem by Permutation Synchronization. *NeurIPS 2013*.
2. Chen, Y., Guibas, L. J., and Huang, Q. (2014). Near-Optimal Joint Object Matching via Convex Relaxation. *ICML 2014*.
3. Ling, S. Near-Optimal Performance Bounds for Orthogonal and Permutation Group Synchronization via Spectral Methods.
4. Nguyen and Zhang (2023). A Novel and Optimal Spectral Method for Permutation Synchronization.
