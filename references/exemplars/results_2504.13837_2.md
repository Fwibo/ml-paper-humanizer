<!-- section: results; orientation: evaluation; source: arXiv 2504.13837, published text, style reference only -->

However, as $k$ increases, with steeper curves, base models consistently catch up to and eventually surpass RL-trained models across all benchmarks, indicating their broader coverage of solvable problems. For example, on the Minerva benchmark with a 32B-sized model, the base model outperforms the RL-trained model by approximately 9\% at $k = 128$, implying that it can solve around 9\% more problems in the validation set.

We further examine RL models trained with Oat-Zero and DAPO. As shown in~REF, although the RL model initially demonstrates a strong performance, nearly 30\% higher than the base model, it is eventually surpassed by the base model. Based on these results, we conclude that RLVR increases the likelihood of sampling correct responses at low $k$, but narrows the model's overall coverage. We further analyze the root cause of this phenomenon in~REF.

\textbf{CoT Case Analysis.} We present the correct CoTs sampled from the base model in~REF and~REF, manually selected from 2048 samplings for the hardest questions in AIME24. The responses from the base model tend to be long CoTs and exhibit reflective behavior, highlighting the strong reasoning ability inherent in the base model.
