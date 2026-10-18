<!-- section: results; orientation: design; source: arXiv 2405.19261, published text, style reference only -->

\textbf{Fine-tuned T5 cascades.} Our experiments on T5 models are based on the setup in [cite]; see \SREF for details. We use T5-small (77M) as the small model, and either T5-large (800M) or T5-XL (3B) as the large model. In each case, we supervised fine-tune these models on three tasks: WMT EN$\rightarrow$DE translation [cite], CNN/DM summarization [cite], and XSum abstractive summarization [cite].

We use temperatures $T=0, 0.1, 0.5, 1.0$, and block sizes $\gamma = 3, 5, 7$ (full results in \SREF). Following the protocol in [cite], to measure latency, we evaluate the wall-clock decoding time with batch size 1.

\if 0 We evaluate all methods under both greedy decoding ($T=0$), and temperature sampling with temperature $T=1$. As noted in \SREF, with greedy decoding, the {\tt OPT} deferral rule coincides with the {\tt Diff} deferral rule. \fi

In Figure REF, we present plots of quality vs.\ latency for the different methods. In each case, we vary the lenience parameter $\alpha$, and plot either the BLEU or ROUGE-2 metric as a function of the relative latency to the larger model. For brevity, we include the three main baselines; in \SREF--REF,
