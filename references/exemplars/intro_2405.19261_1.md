<!-- section: intro; orientation: design; source: arXiv 2405.19261, published text, style reference only -->

on quality~[cite]. One such line of work involves constructing a family of models of various sizes (e.g., a small and large model), and suitably orchestrating amongst them to make a prediction.

While similar in spirit, cascades and speculative decoding are fundamentally different in details. Cascades employ a \emph{deferral rule} to identify ``hard'' inputs, and only invoke larger models on such inputs. For example, in a two-model cascade, one first invokes the smaller model, and uses its associated probability of the generated output to decide whether to defer to the larger model. By contrast, speculative decoding uses a small model to \emph{draft} a block of tokens via standard auto-regressive decoding, which are then \emph{verified} in parallel by a large model. One then accepts all drafted tokens until the first ``implausible'' one, which is rolled back

Owing to their different mechanisms, both methods have complementary strengths. Cascades seek to output distributions that have the best quality for a given cost budget, and potentially provide \textit{blackbetter cost-quality trade-offs}, sometimes even
