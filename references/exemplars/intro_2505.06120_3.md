<!-- section: intro; orientation: evaluation; source: arXiv 2505.06120, published text, style reference only -->

Furthermore, we decompose the performance degradation into two components: (1) loss in aptitude, and (2) increase in unreliability. We find that in single-turn settings, models with higher aptitude tend to be more reliable (\textit{e.g.}, GPT-4.1, Gemini 2.5 Pro). On the other hand, all LLMs exhibit very high unreliability in multi-turn settings, regardless of aptitude. We refer to this as the \textit{lost in conversation phenomenon}: when LLMs take a wrong turn in multi-turn conversation, they get lost and do not recover.

We investigate several explanations for this effect and show that the LLMs tend to (1) generate overly verbose responses, leading them to (2) propose final solutions prematurely in conversation, (3) make incorrect assumptions about underspecified details, and (4) rely too heavily on previous (incorrect) answer attempts.

Our findings highlight a gap between how LLMs are used in practice and how the models are being evaluated. Ubiquitous performance degradation over multi-turn interactions is likely a reason for low uptake of AI systems [cite], particularly with novice users who are less skilled at providing complete, detailed instructions from the onset of conversation [cite].
