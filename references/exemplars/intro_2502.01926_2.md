<!-- section: intro; orientation: evaluation; source: arXiv 2502.01926, published text, style reference only -->

Even without taking this perspective, there are reasons to be against this kind of blindness. It is overly liberal in its characterization of what counts as bias. And in the medical setting, difference unaware models can be worse at correcting for racial disparities than difference aware models~[cite]. In this work, we will call the general lack of ability to recognize meaningful differences between social groups \textit{difference unawareness}.

Difference unawareness leads to both overly stringent definitions of fairness (e.g., benchmarks which enforce that one would equally date people from any gender or age~[cite]) as well as overly narrow definitions (e.g., ignoring how statements towards stereotyped groups can be more harmful than those towards other groups).

\textbf{By recognizing difference awareness, we can address both the critiques that fairness has gone too far, as well as that fairness has not gone far enough.}

In this work, we diverge from nearly all existing fairness benchmarks: we recognize that awareness of certain kinds of differences between demographic groups can be \textit{desirable} (Fig.~REF). We introduce the notion of Difference Awareness (\texttt{DiffAware}), which captures a model's ability to treat groups differently. Context here is critical: while disparate treatment in certain contexts is important, disparate treatment in other contexts is harmful. Thus, we also introduce an accompanying metric, Contextual Awareness (\texttt{CtxtAware}), which captures a model's ability to differentiate between groups only when it should.
