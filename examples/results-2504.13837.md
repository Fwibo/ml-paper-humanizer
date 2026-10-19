# Example: a results section written three ways

Paper: *Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?* ([arXiv 2504.13837](https://arxiv.org/abs/2504.13837), NeurIPS 2025 runner-up, CC BY 4.0). Section: "RLVR for Mathematical Reasoning".

Setup. The model (Claude Opus) was given the section's content outline and facts, but not the authors' wording, and asked to write the section. The run with the skill also built the paper's term ledger and read three exemplar passages, as its steps require. Each draft is one generation.

- **Without the skill**: the model was told to write as a careful author. Written 2026-10-10.
- **With the skill** (seven steps including the frames pass): written 2026-10-16.
- **The authors**: the published passage, with citations and cross-references replaced by `[cite]` and `REF`.

| | Words | Mean sentence length | Field verbs per 1k words | Sentences opening on a frame of the field |
|---|---|---|---|---|
| Without the skill | 342 | 19.0 | 5.8 | not measured |
| With the skill | 342 | 19.0 | 5.8 | 39% |
| The authors | 506 | 22.0 | 13.8 | 65% |

The counts say what is still missing (the authors write longer and with more of the field's verbs). What the skill changes is visible in the text: each paragraph says what it is for before the number, the paper's own names stay (*reasoning ability boundary*, *coverage*), results are read with the field's frames (*REF shows that*, *These curves indicate that*, *We analyze ... in REF*) rather than with the writer's images (*The crossover persists*, *the ordering does not survive*), and the inference carries its reporting verb.

---

## Without the skill

**Models and benchmarks.** In math, a model writes a chain of thought (CoT) followed by a final answer, and only the answer is checked. Our main model family is Qwen2.5 [cite], with the 7B, 14B and 32B base models; LLaMA-3.1-8B [cite] serves as a second family. The RL models are the zero-RL checkpoints of SimpleRLZoo [cite], trained with GRPO directly on these pretrained models on GSM8K and the MATH training set, with a correctness reward and no format reward, so each is compared with the exact checkpoint it started from. The test sets range from grade-school word problems to competition mathematics: GSM8K [cite], MATH500 [cite], Minerva [cite], Olympiad [cite], AIME24 and AMC23. We also evaluate two RLVR models known for strong AIME24 results, Oat-Zero-7B [cite], trained from Qwen2.5-Math-7B, and DAPO-32B [cite], trained from the Qwen2.5-32B base model.

**Base models solve more problems once $k$ is large.** fig:math plots pass@$k$ for each base model and its RL-trained version (GSM8K and AMC23 are in REF). At $k=1$, the average-case accuracy that is usually reported, the RL model leads in every panel. The ordering does not survive larger sampling budgets. The base curves rise more steeply with $k$, catch up with the RL curves after tens or hundreds of samples, and in most panels end clearly above them; the same shape appears across sizes, families and benchmarks. On Minerva, for example, the 32B base model outperforms its RL-trained counterpart by approximately 9% at $k=128$, that is, it solves about 9% more of the problems in the benchmark. Higher accuracy per sample thus coexists with fewer problems solved: RL makes answers the base model can already produce more probable, while some problems within its reach drop out. sec:pattern_analysis examines why.

**RL models with strong AIME24 results.** The crossover persists for models selected for their AIME24 strength (REF). Oat-Zero-7B and DAPO-32B start nearly 30% above their base models on AIME24, yet their curves flatten while the base curves keep climbing, and at the largest $k$ the base models are ahead. Strong RL training makes a correct answer far more likely within a few attempts, but it narrows rather than enlarges the set of problems the model ever solves.

**Are rare successes genuine?** Since math is graded on the final answer alone, a flawed CoT can still land on the right number, and such hits become more frequent as $k$ grows. If guessing drove the base models' coverage, the comparison above would say little about reasoning. The base samples suggest otherwise: correct CoTs we picked by hand from 2048 samples on the hardest AIME24 questions are long, reflective solutions that build the argument step by step (REF). For a systematic check we follow [cite] and read every CoT that ends in a correct answer on the most challenging solvable GSM8K problems, those with an average accuracy below 5% but above 0%; a question counts as genuinely solved if at least one of these CoTs is correct. The base model answers 25 such questions and 24 of them contain at least one correct CoT; the RL-trained model also answers 25, of which 23 do. On AIME24 we apply the same check to questions with average accuracy below 5% (REF). The base model answers 7; we set aside one whose correctness is ambiguous because the CoT skips reasoning steps, and 5 of the remaining 6 contain a correct CoT. The RL-trained model answers 6, and 4 of them do. For both models, most successes on rarely solved problems rest on valid reasoning, so the base models' wider coverage at large $k$ is not explained by lucky guesses.

---

## With the skill

**Models and Benchmarks.** In mathematics, the first domain we examine, each model must output a CoT followed by a final answer, and correctness is judged on the final answer alone. Our main models are the Qwen2.5 base models at 7B, 14B and 32B [cite], and LLaMA-3.1-8B [cite] adds a second model family. For each base model, the RL-trained model is the zero-RL checkpoint released by SimpleRLZoo [cite]. These checkpoints are trained with GRPO on the GSM8K and MATH training sets, with a correctness reward and no format reward. We evaluate on benchmarks of varying difficulty: GSM8K [cite], MATH500 [cite], Minerva [cite], Olympiad [cite], AIME24 and AMC23. We also evaluate Oat-Zero-7B and DAPO-32B [cite], two RLVR models known for strong AIME24 performance.

**The Effect of RLVR: Increased Likelihood of Correct Samples, Decreased Coverage of Solvable Problems.** REF shows that the pass@$k$ curves follow one pattern for every model family and benchmark: RL-trained models lead at small $k$, and base models catch up with and then surpass them as $k$ grows. In other words, measured by average-case accuracy, which equals pass@$k$ at $k = 1$, RLVR improves the models. The base curves, however, rise more steeply with $k$ than those of the RL-trained models. On Minerva at $k = 128$, for example, the 32B base model outperforms its RL-trained model by approximately 9%, i.e., it solves about 9% more of the problems in the set.

We next check whether RLVR models with strong AIME24 results escape this pattern. REF shows that on AIME24, Oat-Zero-7B and DAPO-32B start nearly 30% above their base models, yet the base models overtake both as $k$ grows. These curves indicate that RLVR makes a correct sample more likely at small $k$ but narrows the reasoning ability boundary. With many samples, the RL-trained model solves fewer problems than its base model. We analyze the cause of this narrowing in REF.

**CoT Case Analysis.** REF show two correct CoTs of the 7B base model on the hardest AIME24 questions, selected by hand from 2048 samples. We observe that each works through the problem step by step and reaches the correct final answer. These cases show that the base model can already write long CoTs with reflective behavior on questions this hard.

**Validity of Chain-of-Thought.** Since only final answers are checked in mathematics, a correct answer can also come from an incorrect CoT through hacking or lucky guesses, a risk that grows with $k$. To test whether the coverage of base models at large $k$ rests on lucky guesses, we follow [cite] and read by hand the CoTs behind correct answers on the most challenging solvable problems. These are the problems whose average accuracy is below 5% but above 0%. On GSM8K, we find that 24 of the 25 such questions answered by the base model have at least one correct CoT, as do 23 of the 25 answered by the RL-trained model. On AIME24 (details in REF), the base model answers 7 such questions. We exclude one whose correctness is ambiguous because reasoning steps are skipped. Of the remaining 6, 5 have at least one correct CoT, as do 4 of the 6 answered by the RL-trained model. Overall, for both models, most of these questions have a correct CoT. This indicates that the larger coverage of base models at large $k$ comes from valid reasoning rather than lucky guesses.

---

## The authors

**Models and Benchmarks.** In math problems, models are required to generate a reasoning process (i.e., CoT) along with the final answer. To ensure the robustness of conclusions, we experiment with multiple LLM families, primarily Qwen2.5 (7B/14B/32B base variants) [cite] and additionally LLaMA-3.1-8B [cite]. We adopt RLVR models released by SimpleRLZoo [cite], which train zero-RL models using GRPO on GSM8K and the MATH training set, with correctness reward only, excluding any format-based reward. We compare the pass@$k$ curves of base and zero-RL models on benchmarks of varying difficulty: GSM8K [cite], MATH500 [cite], Minerva [cite], Olympiad [cite], AIME24, and AMC23. Additionally, we include the RLVR model Oat-Zero-7B and DAPO-32B [cite]. These two models are characterized by strong performance on the challenging AIME24 benchmark.

**The Effect of RLVR: Increased Likelihood of Correct Samples, Decreased Coverage of Solvable Problems.** As shown in REF, we consistently observe a contrasting trend between small and large $k$ values. When $k$ is small (e.g., $k = 1$, equivalent to average-case accuracy), RL-trained models outperform their base counterparts. This aligns with the common observation that RL improves performance, suggesting that RLVR makes models significantly more likely to sample correct responses.

However, as $k$ increases, with steeper curves, base models consistently catch up to and eventually surpass RL-trained models across all benchmarks, indicating their broader coverage of solvable problems. For example, on the Minerva benchmark with a 32B-sized model, the base model outperforms the RL-trained model by approximately 9% at $k = 128$, implying that it can solve around 9% more problems in the validation set.

We further examine RL models trained with Oat-Zero and DAPO. As shown in REF, although the RL model initially demonstrates a strong performance, nearly 30% higher than the base model, it is eventually surpassed by the base model. Based on these results, we conclude that RLVR increases the likelihood of sampling correct responses at low $k$, but narrows the model's overall coverage. We further analyze the root cause of this phenomenon in REF.

**CoT Case Analysis.** We present the correct CoTs sampled from the base model in REF and REF, manually selected from 2048 samplings for the hardest questions in AIME24. The responses from the base model tend to be long CoTs and exhibit reflective behavior, highlighting the strong reasoning ability inherent in the base model.

**Validity of Chain-of-Thought.** For mathematical problems, the common evaluation is based solely on the correctness of the final answer, with the risk of "hacking". To accurately reflect the reasoning ability boundary using pass@$k$, it is important to assess how many solved problems result from sampling genuinely correct CoTs, rather than from lucky guesses. Following [cite], we manually inspect all CoTs that led to correct answers to the most challenging solvable problems in the GSM8k dataset -- those with an average accuracy below 5% but above 0%. The base model answered 25 such questions, with 24 containing at least one correct CoT. Similarly, the RL-trained model answered 25 questions, 23 of which included at least one correct CoT.

We also manually check the CoTs for problems in the challenging AIME24 benchmark with an average accuracy below 5%. Details can be found in REF. The base model answered 7 such questions, with 5 out of 6 containing at least one correct CoT (excluding one ambiguous case of correctness due to skipped reasoning steps). Similarly, the RL-trained model answered 6 questions, 4 of which included at least one correct CoT. These results suggest that the base model can sample valid reasoning paths to solve the problems.

---

The authors' passage is quoted from a CC BY 4.0 paper; copyright stays with its authors. The two drafts are model output and carry no claim of authorship.
