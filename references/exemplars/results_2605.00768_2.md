<!-- section: results; orientation: proof; source: arXiv 2605.00768, published text, style reference only -->

We summarize performance using a heatmap of the longest perfect length in REF. Full numerical results, including accuracies and longest perfect lengths, are provided in REF.

As predicted, local-only transformers succeed precisely on the $\ytl$-definable languages: they achieve perfect generalization up to length $500$ on the two $\ytl$ tasks in REF, while failing to generalize on the remaining languages.

Hybrid models, especially with $k=1$, succeed on all languages definable in $\yptl$, which subsumes both ${LTLColor \textup{\textbf{LTL}}}\left[{OperatorColor \mathrel{\textup{\textbf{P}}}}\right]$ and $\ytl$. As visualized in REF, they generalize perfectly up to length $500$ on the bottom six languages.

Among the tested window sizes, $k=1$ is consistently the strongest performer. Both $k=2$ and $k=4$ fail even on definite languages, and increasing the window can hurt: for example, hybrid models with $k=2$ learn ${{{{StringColor \Sigma}}^*}}{StringColor \texttt{a}}{StringColor \texttt{b}}{{{{StringColor \Sigma}}^*}}$, whereas those with $k=4$ do not.

As expected, none of the models perfectly generalizes on the two languages in ${LTLColor \textup{\textbf{LTL}}}[{OperatorColor \mathrel{\textup{\textbf{S}}}}] \setminus \yptl$, namely the right-deterministic polynomial and bounded Dyck. Nevertheless, hybrid attention yields the strongest partial generalization on these tasks.
