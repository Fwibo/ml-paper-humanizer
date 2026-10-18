<!-- section: results; orientation: proof; source: arXiv 2510.19315, published text, style reference only -->

Let $\varphi_n$ be an LTL formula that recognizes $L_n$. Because the smallest accepted word by any LTL formula has length at most exponential in the formula size, using an exponential conversion from LTL to finite automata similar to [cite], it follows that the size of $\varphi_n$ is at least exponential in $n$. \end{proof}

Conversely, the next result shows that UHATs have polynomially bounded expansion over LTL: every LTL formula has an at most polynomially larger UHAT for the same language. Combined with REF, this pins the gap between UHATs and LTL: at most polynomial universally, and at least exponential on a witness family. The proof can be found in REF.

Conversely, the best known translation from counter-free automata---the class of finite automata equivalent to LTL---to LTL incurs an exponential blow-up [cite]. Composing this with REF yields an at-most exponential-time translation from counter-free automata to UHATs, which shows that UHATs have exponentially bounded expansion over finite automata when restricted to the star-free languages. The translation in [cite] also incurs an exponential blow-up via [cite].
