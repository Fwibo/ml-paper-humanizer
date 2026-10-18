<!-- section: intro; orientation: design; source: arXiv 2506.12229, published text, style reference only -->

For answering queries, we extend \mathrm{SDSL} to work with on-disk index, reducing the RAM requirement to a negligible amount. Our inference engine supports counting the occurrences of a query string and retrieving documents that contain the query string, both within seconds when working on the above corpora.

We apply \mathrm{infini-gram mini} to \textbf{analyzing contamination of benchmarks} widely used in state-of-art LM evaluations (\SREF). \mathrm{Infini-gram mini} allows us to do the analysis on larger corpora than prior works and on new benchmarks uploaded. This would be much more expensive if using other indexing methods.

\mathrm{Infini-gram mini} detects exact overlap for question of contaminated entries in text corpora, among which a large majority of questions appear together with the correct answer. \textbf{This reveals a dire evaluation crisis:} as benchmarks get increasingly contaminated by Internet crawls and consequently LM training data, evaluation results may give inflated estimates of true model capabilities. As such, we host a benchmark contamination bulletin to continually monitor contamination of core and community-contributed benchmarks on new Internet snapshots, and we call for more community attention on this matter.
