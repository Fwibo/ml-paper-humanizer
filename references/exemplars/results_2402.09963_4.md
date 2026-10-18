<!-- section: results; orientation: proof; source: arXiv 2402.09963, published text, style reference only -->

By Theorem REF, sensitivity of each autoregressive step when computing PARITY with scratchpad is $O(1)$. Hence, Theorem $REF$ provides no nontrivial lower bound for $L_{\rho,n}(T)$. We trained an Encoder-Decoder Transformer, predicting PARITY of $i$-th substring on $i$-th autoregressive step: ${t}_i = \mathrm{PARITY}(x_{1:i}) = x_i \oplus {t}_{i - 1}$ (${t}_0 = 0$). The visual dependency between sharpness and length of input for PARITY with a scratchpad is shown in Figure REF. Even for length around 300, sharpness is low and there is little increase with input length. Thus, decrease in sensitivity due to the scratchpad can explain why prior work [cite] found that PARITY is easy for Transformers with scratchpad.

Figure REF represents the evolution of loss and sharpness of Transformer models trained for PARITY with input length 25. The results are averaged across 39 converged runs. Similar curves for parameter norm and LayerNorm blowup are presented in Appendix REF.

A dramatic increase in sharpness occurs at exactly the time when loss falls to 0. This suggests the presence of a steep minimum in the loss landscape, and fitting PARITY requires the optimization procedure to find this minimum.
