<!-- section: results; orientation: design; source: arXiv 2310.16834, published text, style reference only -->

We now empirically validate that our score entropy discrete diffusion (SEDD) model on a variety of language modeling tasks. We measure both perplexity (i.e. likelihood estimation capabilities) as well as generation quality, finding that our method performs quite well in both aspects.

Our core model is based on the diffusion transformer architecture [cite], which incorporates time conditioning into a standard encoder-only transformer architecture [cite], although we make some minor modifications such as employing rotary positional encoding [cite].

We construct SEDD Absorb and SEDD Uniform, which correspond to the matrices $Q^{\rm uniform}$ and $Q^{\rm absorb}$ respectively. We tested a geometric noise schedule (that interpolates between $10^{-5}$ and $20$), as well as a log-linear noise schedule (the number of changed tokens for total noise $\overline{\sigma}(t)$ is approximately $td$ for both transitions), which helps SEDD Absorb for perplexities. Outside of this, we did not systemically explore noise schedules or alternative loss weightings, although these could likely improve generation quality.
