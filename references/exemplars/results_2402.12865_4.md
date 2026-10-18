<!-- section: results; orientation: design; source: arXiv 2402.12865, published text, style reference only -->

We hypothesize that the changes to the last subject token may involve editing the information transferred by the subject's token through attention, as demonstrated by [cite].

A complementary view is provided by considering, for the LL rank of each VJP $\delta_i$ (labeled by the segment of token $i$ of the input) the rank of the target token.

REF illustrates that the VJP of the last token from the edited prompts, $\delta_n$, consistently ranks the target token among the least probable ones. The VJPs of other tokens from the edited prompt, $\delta_i$, exhibit comparable behavior, generally ranking the target token as improbable.

The result reveals that along the first and last layers, some of the $\delta_i$ show degradation in their ranking of the target token, which we attribute to their low norms as reflected by REF. We demonstrate in REF that normalizing $\delta_i$ before LL magnifies the presence of the target token. Specifically, the drop at the model's last layer is due to the fact that apart from the last prompt's token, all the others have a zero vector $\delta_i$ at that layer (REF).
