<!-- section: intro; orientation: design; source: arXiv 2506.12229, published text, style reference only -->

To address this challenge, we index text corpora with \textbf{FM-index} [cite], a compact data structure frequently used in bioinformatics [cite], but not yet used for natural language data at scale. Prior work only applies this data structure to 13.4 GB dataset [cite]. We explain FM-index in detail in \SREF.

For natural text, the size of FM-index can be made as small as 0.26$\times$ of the corpus; practically, to ensure low query latency, we build FM-index with a storage multiplier of \textbf{0.44$\times$}, or 7\% compared to the canonical suffix array.

\textbf{\mathrm{Infini-gram mini}} is the system we developed for efficiently constructing the FM-index at scale and answering search queries. For indexing, we extend and combine components from [cite], [cite], and [cite] into a highly parallelized program, which achieves a \textbf{18$\times$} speedup and uses only \textbf{32\%} as much RAM compared to the best existing implementation by \mathrm{SDSL} [cite].

We use \mathrm{infini-gram mini} to construct FM-index for two LM pretraining datasets -- the Pile and DCLM-baseline -- and 7 recent Common Crawl dumps from January to July 2025. Altogether, we indexed \textbf{83TB} of text in 99 days with a single CPU node with 128 vCPUs, and this could have been done in 19 hours if embarrassingly parallelized across 137 such nodes.
