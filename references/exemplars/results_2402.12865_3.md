<!-- section: results; orientation: design; source: arXiv 2402.12865, published text, style reference only -->

We observe that while all the prompt's tokens contribute to the gradient construction (REF), the majority of these contributions are done by VJPs, $\delta_i$, with a close-to-zero norm. Furthermore, upon examining the LL of every individual neuron from the gradient matrix (Appendix REF), we found that all the projected tokens are correlated with only 1-2 vectors we can identify from the spanning sets presented in REF.

To discern the relative importance of tokens and layers in the gradient reconstruction, we divide each prompt's tokens into segments and plot their $\delta_i$ mean norm. This experiment is done with GPT2-xl, due to its extensive use in prior work on interpretability research.

Results are depicted for $FF_2$ in REF, see Appendix~REF for $FF_1$. Evidently, predominant updates occur in two main areas: (1) by the subject's tokens in the initial layers, and (2) by the last prompt's token around the second quarter of the layers. The majority of other tokens exhibit a norm close to zero throughout the layers, indicating that they have almost no effect on the updating.
