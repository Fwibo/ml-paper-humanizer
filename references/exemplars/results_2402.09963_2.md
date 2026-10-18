<!-- section: results; orientation: proof; source: arXiv 2402.09963, published text, style reference only -->

In this experiment, we train transformers to fit $f \in \{PARITY, MAJORITY, FIRST, MEAN\}$ on sequence lengths from 4 to 30. For each function and sequence length, we retrain the model 10 times from different random initializations.

For PARITY, sharpness stably increases with the input length (Figure~REF). For the other functions, whose sensitivity grows more slowly with $n$, (a) the absolute value of sharpness is orders of magnitude lower than for PARITY; (b) there is little increase with $n$. More results are shown in Appendix REF.

At any fixed input length $n$, high sensitivity can be achieved by a combination of large weights and a large LayerNorm blowup. By Theorem REF, the product of $C$ and squared blowup is bounded from below with some value $B_n(f)$. Hence, the product of $\sqrt{C}$ and blowup is bounded with $\sqrt{B_n(f)}$, and the sum of $\frac{1}{2} \log C$ and $\log \mathrm{Blowup}$ is bounded with $\frac{1}{2} \log {B_n(f)}$. However, $C$ depends exponentially on parameters, and thus we expect the parameter norm to trade off with the logarithm of the layer norm blowup. Moreover, for PARITY the value of $B_n(f)$ increases with $n$, and therefore sum of parameter norms and the logarithm of the blowup should also increase with $n$.
