<!-- section: results; orientation: design; source: arXiv 2310.16834, published text, style reference only -->

Our results are reported in Table REF. Our SEDD Absorb beats GPT-2 on a majority of the zero-shot tasks across both sizes. To the best of our knowledge, this is the first time where a non-autoregressive language model has matched a modern, reasonably sized, and well-known autoregressive model for perplexities. We also compare against the most competitive continuous [cite] and discrete [cite] diffusion baselines, seeing a large improvement over both.

With our trained models, we compare against prior work in terms of generation quality. In particular, we compare GPT-2 with our SEDD Absorb on a variety of scales. Results for SEDD Uniform are given in Appendix REF.

We first compare the quality of unconditional samples between GPT-2 and SEDD. As most language metrics are meant for comparing conditional generations [cite], we instead measure the generative perplexity of sampled sequences (using a GPT-2 large model for evaluation). This is a simple and common metric [cite] but can easily be ``hacked" by simple distribution annealing methods. So, we compare analytically sampled generations (i.e. no temperature scaling).
