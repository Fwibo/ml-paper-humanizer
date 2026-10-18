# Sentence bank

Sentences from published award papers (NeurIPS, ICML, ICLR, ACL and others, 2023–2026), chosen where a draft written with this skill still fell short of the authors. Part A pairs the draft's sentence with the authors' sentence for the same job and says what differs; Part B gives further sentences by move. Read the sections for the moves you are about to write. The bank teaches the shape and the placement of a sentence, not its words: its content is never yours, and no run of six or more words from it may appear in your text (standard phrases of the field are not its property).

Move labels: I1 opening, I2 gap, I3 stakes, I4 turn to this paper, I5 thesis, I6 purpose-before-definition, I7 contribution lead, I8 orientation phrase, I9 example after an abstract claim, I10 hand-off; R1 pointer + claim, R2 the comparison that matters, R3 mechanism, R4 hedged reading, R5 concession in a clause, R6 boundary, R7 transition, R8 surprise, R9 setup, R10 recap.

## Part A. Where drafts fall short of the authors, by type

### Signposts: tell the reader what the sentence or paragraph is for

The authors spend a few words, often a stock phrase, to say what comes next and why: an objection they are about to answer, the purpose of the test, the turn to a new case, a hand-off. The drafts drop these words as filler and open on the result or the instrument, so the reader meets the number before the question.

**A1** (R7, from the paper 2505.12741, results section)
- Draft: Notably, SFT on the same data lowers mean accuracy by 5.7% relative to Prompt.
- Authors: Second, one may argue that the improvement mainly relies on training data. SFT (implemented by very moderate training configurations) can hardly bring improvement over the pre-trained LLM (-5.7%). In fact, these public data are likely to be seen during the pre-training of the LLM.
- What differs: The authors state the objection the SFT row answers ('one may argue that the improvement mainly relies on training data') before the number, then add a one-line reason why SFT fails. The model's 'Notably' gives the number with no question attached until the next sentence.

**A2** (R7, from the paper 2407.10490, results section)
- Draft: Responses that are not language receive almost no lift.
- Authors: To verify the existence of this global "push-down" pressure, we observe two types of responses; both have the same number of words as their $\bm{\mathsf{y}}_u^+$.
- What differs: The authors open the paragraph by saying what the probe is for (isolating the push-down pressure), which tells the reader why non-language responses were picked. The model opens with a result stated as an absence ('receive almost no lift'), which hides that the point of the test is the push-down.

**A3** (I4, from the paper 2505.16932, intro section)
- Draft: Prior work analyzes and discusses in more depth REF. We take the update rule REF as given and focus on computing $polar(\mM_t)$, which needs for every weight matrix at every step.
- Authors: For analysis and further discussion on Muon, we refer the reader to [cite]. In this paper, we take the Muon update rule as given and focus on the problem of efficiently computing the polar decomposition $\mathrm{polar}({\bm{M}})$.
- What differs: The authors hand off the side topic with the stock "we refer the reader to" and mark the turn to their own scope with "In this paper". The model makes "Prior work" the subject of a near-empty sentence and drops the signpost, so the scope statement arrives unannounced.

**A4** (I8, from the paper 2407.10490, intro section)
- Draft: We find that, for a softmax output trained with cross-entropy, a negative gradient on one label lowers the predictions on almost all labels and moves the removed probability to the labels that were already most likely.
- Authors: In short, for each token's prediction, the negative gradient will push down the model's predictions on (almost) all possible output labels, moving this probability mass to the most-likely labels.
- What differs: The authors give the formal condition in the preceding sentence and then announce the plain version with 'In short', using concrete verbs ('push down', 'moving this probability mass'); the model merges condition and effect into one sentence and uses the stiffer 'moves the removed probability'.

**A5** (I8, from the paper 2504.15266, intro section)
- Draft: Our thesis also bears on where randomness enters. If the random choices of a plan must be fixed before the first token, randomness may be better supplied with the input than drawn at the output.
- Authors: Next, we turn to how we elicit randomness from a Transformer. While the de facto approach is to elicit randomness at the output -- temperature sampling -- we contrast this with injecting randomness into the model.
- What differs: The authors open with a plain turn ('Next, we turn to') and name the standard practice before the alternative: temperature sampling at the output versus injecting randomness into the model. The model opens with the abstract 'bears on where randomness enters' and argues from a conditional without naming the practice it departs from.

**A6** (R7, from the paper 2602.01338, results section)
- Draft: REF turns sampling from the Gaussian tilt REF into a choice of two objects.
- Authors: Now, we return to the problem of sampling from a general Gaussian tilt: [display]
- What differs: The authors open with 'Now, we return to the problem of ...' and restate the target density, so the reader knows the section resumes an earlier thread; the model opens on a theorem reference and an abstract metaphor ('turns ... into a choice of two objects').

**A7** (R6, from the paper 2505.16932, results section)
- Draft: Appendix REF repeats these comparisons with error measures looser than the spectral norm.
- Authors: Note that REF measures error in the spectral norm. For many applications, we may be satisfied with a looser measure of error; see REF.
- What differs: The authors flag the limit with "Note that", state it (the figure uses the spectral norm) and give the reason a looser measure is worth seeing. The model makes the appendix the subject and leaves the reader to infer both the limit and why it matters.

### One relation per sentence, said in order

The drafts fit purpose, method and outcome into one sentence with appositives and which-clauses. The authors give each its own sentence, in the order the reader needs them, and let a familiar frame carry the join.

**A8** (R9, from the paper 2505.16932, results section)
- Draft: We first measure how fast Polar Express approaches the polar factor, comparing the spectral-norm error $\|\operatorname{polar}(M) - X_t\|_2$ of its iterate $X_t$ after $t$ iterations with that of degree-5 Newton-Schulz, Jordan's method REF and You's method REF.
- Authors: We compare Polar Express against degree-5 Newton-Schulz and the methods of [cite] and [cite].
- What differs: The authors open the section with one short sentence that names only the comparison. The model's first sentence carries the aim, the error formula, the definition of the iterate and the three baselines at once.

**A9** (I5, from the paper 2505.10465, intro section)
- Draft: As the degree of superposition and the structure of the data change, when does the loss follow a power law in width, and, when it does, what is its exponent?
- Authors: Varying the degree of superposition and data structure, when is the loss a power law? And if the loss is a power law, what will the exponent be?
- What differs: The authors ask the two questions as two sentences, so each reads on its own. The model nests the second question inside the first with ', and, when it does,'.

**A10** (R9, from the paper 2505.12741, results section)
- Draft: Compute limits lead us to the smallest current LLMs, so we build every vertex from Qwen2.5-0.5B and tie all vertices to one set of weights.
- Authors: Due to the computation budget, we consider modern LLMs with minimum size. We use Qwen2.5-0.5B as the vertex module to be shared among all vertexes.
- What differs: The authors give the reason and the model choice in two short sentences with a familiar opener ('Due to the computation budget'). The model chains reason, model choice and weight tying with 'so' and 'and' under an unusual subject ('Compute limits lead us to').

**A11** (I6, from the paper 2505.16932, intro section)
- Draft: REF speed up this early phase with a Newton-Schulz variant that changes the polynomial at every iteration while keeping super-exponential convergence in the later iterations.
- Authors: Due to the slow initial convergence of Newton-Schulz, [cite] developed a version of the Newton-Schulz iteration, which adapts the polynomial at each iteration. The resulting method achieves a faster initial convergence, while retaining super-exponential convergence in later iterations.
- What differs: The authors open with the reason, restating the named problem ("Due to the slow initial convergence") instead of pointing back with "this early phase", then give what was built and what it achieves one sentence each. The model fits motive, method and both convergence properties into one sentence.

**A12** (I7, from the paper 2505.16932, intro section)
- Draft: We introduce Polar Express (REF), an iteration whose polynomial shifts from favoring speed in the early steps to favoring accuracy in the late ones.
- Authors: We present Polar Express (REF), an iterative method for approximating $\mathrm{polar}(\bm{M})$. Our method dynamically adapts the polynomial update rule at each iteration, prioritizing rapid progress in the initial stage and high accuracy in the later stage.
- What differs: The authors' contribution lead says what the method is for (approximating polar(M)) and gives the mechanism its own second sentence. The model packs the mechanism into the appositive and never says what the method computes.

**A13** (I7, from the paper 2602.01338, intro section)
- Draft: We answer this question in the affirmative with a new meta-algorithm, first-order rejection sampling (FORS, Algorithm REF), which simulates rejection sampling using gradient queries alone.
- Authors: We answer this question affirmatively via a new meta-algorithm, which we call first-order rejection sampling (\textsf{FORS}); see REF. This algorithm aims at simulating rejection sampling using only first-order (gradient) queries.
- What differs: The authors name the method in one sentence and say what it does in the next. The model loads the name, abbreviation, algorithm pointer and a which-clause on the mechanism into the one sentence that answers the question.

### Familiar phrasing over precise-but-strange phrasing

A stock academic phrase is read without being noticed; a fresh image has to be decoded. The authors write "This would not be a fair comparison, because", "Numerical analysts have spent decades developing", "We also test"; the drafts write "That yardstick measures a different goal", "Numerical analysis offers an alternative", "The right panel turns to". Prefer the sentence a reviewer has read a hundred times.

**A14** (R6, from the paper 2505.12741, results section)
- Draft: That yardstick, however, measures a different goal. A monolithic LLM of that size is trained from scratch, whereas upgrades a model that already exists.
- Authors: This would not be a fair comparison, because LMNet is a general method to improve the intelligence of a given LLM, with additional training cost only less than $1%$ of the pre-training.
- What differs: 'This would not be a fair comparison, because ...' is the familiar move and gives verdict and reason in one sentence. The model's metaphor ('That yardstick ... measures a different goal') needs the next sentence to be decoded.

**A15** (I1, from the paper 2505.16932, intro section)
- Draft: Numerical analysis offers an alternative in the iterative methods it has developed over several decades REF.
- Authors: Numerical analysts have spent decades developing iterative methods for computing $\mathrm{polar}(\bm{M})$.
- What differs: The authors use people as the subject and a plain verb ("have spent decades developing ... for computing"). The model personifies the field ("offers an alternative in the iterative methods it has developed"), an odd collocation that also hides what the methods compute.

**A16** (R7, from the paper 2505.16932, results section)
- Draft: The right panel of Figure REF turns to a non-synthetic matrix, the gradient of a weight matrix in the fourth transformer block of a randomly initialized GPT-2 model.
- Authors: We also test convergence on a non-synthetic matrix: the gradient of a weight matrix from the fourth transformer block of a GPT-2 model (REF, right).
- What differs: The authors mark the second test with "We also test" and put the figure reference in a parenthesis. The model makes the figure panel the agent that "turns to" a matrix, which reads oddly and hides that a new test begins.

**A17** (I2, from the paper 2505.12741, intro section)
- Draft: This round trip is required when a model talks to people, but between two models it is needless. De-embedding discards part of what the output vectors hold and emits discrete tokens, which gradients cannot pass through.
- Authors: Though this embedding/de-embedding cycle is necessary for communication between model and human, it is redundant for communication among models, loses information, and breaks gradient flow.
- What differs: The authors put the concession in a 'Though' clause and list the three costs with standard phrases (redundant, loses information, breaks gradient flow). The model spends two sentences and swaps the standard phrases for descriptions ('discards part of what the output vectors hold', 'which gradients cannot pass through').

**A18** (I2, from the paper 2505.10465, intro section)
- Draft: Several of the explanations above implicitly place models in the weak regime REF, which sits uneasily with the number of tokens an LLM must fit into its hidden space.
- Authors: Although models can represent more features than their dimensionality would suggest through a mechanism known as superposition [cite], prior works on neural scaling laws seem to fall in the weak superposition regime implicitly [cite], which may be less relevant to the regime where LLMs operate.
- What differs: The authors fit the superposition background into one concessive clause and end on a plain, hedged gap ('may be less relevant to the regime where LLMs operate'). The model spends six sentences on background before the gap, then states it with the odd collocation 'sits uneasily with'.

**A19** (I8, from the paper 2505.16932, intro section)
- Draft: The choice of the polar factor reflects a choice of norm. The direction $-polar(\mM)$ is the steepest-descent direction under the spectral norm, whereas plain SGD steps along $-\mM$, the steepest-descent direction under the Frobenius norm.
- Authors: The motivation for Muon is that $-\mathrm{polar}({\bm{M}})$ gives the steepest-descent direction with respect to the spectral norm (instead of the Frobenius norm, as in standard SGD).
- What differs: The authors label the sentence with a familiar frame ("The motivation for Muon is that") and put the SGD comparison in a parenthesis. The model opens with an abstract aphorism ("reflects a choice of norm") and spends a second full clause on the side comparison.

### Purpose before definition

The drafts define a term as soon as it appears, in an appositive, before the reader knows why it is needed. The authors first say what the thing is for or what is at stake, then name it, and often give the plain meaning before the formal one.

**A20** (I1, from the paper 2407.10490, intro section)
- Draft: Learning dynamics describe how a gradient-descent update on one training example changes a model's predictions on other examples, linking each change in prediction to the gradients of specific examples.
- Authors: Deep neural networks usually acquire new knowledge by updating their parameters via gradient descent (GD). This procedure can be described by learning dynamics, which links changes in the model's predictions to the gradients generated by learning specific examples.
- What differs: The authors open with a fact every reader accepts (networks learn by gradient descent) and introduce learning dynamics as a way to describe that procedure; the model opens on the term itself and packs its definition plus a participial gloss into one sentence before the reader knows why it is needed.

**A21** (I6, from the paper 2505.10465, intro section)
- Draft: We focus here on how a model represents the features of its data within a hidden space of limited width. A feature is an atomic, irreducible unit of the data; for an LLM it is, naively, a token or a more abstract concept.
- Authors: When considering LLMs specifically, it becomes clear that representation or embedding can be a limiting factor, which is closely related to a phenomenon called superposition [cite], yet this aspect has not been thoroughly studied.
- What differs: Before defining anything, the authors say why representation matters (it can be a limiting factor), connect it to the term the paper needs, and name the gap. The model announces a focus and defines 'feature' before the reader knows why representation deserves study; the reason comes four sentences later.

**A22** (I6, from the paper 2602.01338, intro section)
- Draft: Samplers built on these corrections come with high-accuracy guarantees: their iteration count grows as $\polylog(1/\delta)$ rather than $\poly(1/\delta)$, so they converge exponentially fast in the accuracy.
- Authors: Complexity bounds which scale as $\mathrm{polylog}(1/\delta)$, indicating that algorithms converge exponentially fast, are known as "high-accuracy" guarantees, as they ensure that one can draw an extremely accurate sample without too many iterations.
- What differs: The authors tie the term to what it buys ("as they ensure that one can draw an extremely accurate sample without too many iterations"). The model gives only the formal definition after the colon and never says why a reader should want the property.

**A23** (I1, from the paper 2505.16932, intro section)
- Draft: Several optimizers for deep learning evaluate a matrix function, a scalar function applied to a matrix through its eigenvalues or singular values, as part of their update.
- Authors: Advanced linear algebra is making its way into deep learning. Efficient algorithms for computing matrix functions have found exciting new applications in training neural networks.
- What differs: The authors open with a short trend sentence that is read at once, then name matrix functions through their new use in training. The model halts its first sentence to define the term in an appositive before the reader knows why it matters.

**A24** (R3, from the paper 2505.10465, results section)
- Draft: The Welch bound limits how small the overlaps of many unit vectors can be made, however carefully they are arranged.
- Authors: We want to understand how such a structure will change the scaling of overlaps. It turns out that for better error correction (using bias to cancel interference), the model needs to minimize the maximum overlap rather than the sum of squared overlaps.
- What differs: The authors first state the question and why the maximum overlap is the quantity the model cares about, so the bound arrives with a purpose. The model introduces the Welch bound cold, and the reader has to guess why a max-overlap bound matters here.

**A25** (I6, from the paper 2602.02908, intro section)
- Draft: When sampling follows the deterministic probability-flow ODE, each trained model defines a sampling map: the noise seed fully determines the generated sample. For diffusion models this map is strikingly stable across training runs, a property known as consistency.
- Authors: A distinctive feature of diffusion models is their striking consistency across training runs (Figure REF).
- What differs: The authors name the phenomenon in one sentence as 'a distinctive feature' and fold the deterministic flow into the evidence sentence; the model first defines a 'sampling map' the reader has no reason to want yet, then labels consistency with 'a property known as'.

### Say what the result means, and mark the surprise

The drafts report a curve or a number and stop. The authors add the reading ("showing generalization", "is borne out", "prohibitively expensive") and flag what is expected and what is not ("As expected", "However, ... is non-trivial", "Remarkably"). One evaluative word on a concrete claim is not hype; a number without a reading is not modesty.

**A26** (R1, from the paper 2407.10490, results section)
- Draft: The first panel of REF shows that responses close to $\vy_u^+$ first rise and then sink, while $\vy_u^+$ itself keeps climbing.
- Authors: As demonstrated in the first panel of REF, the model's confidence on $\bm{\mathsf{y}}_u^+$ keeps increasing throughout the whole learning process, which is straightforward because the main "pull-up" pressure is imposed directly on $\bm{\mathsf{y}}_u^+$. However, the behavior of some responses similar to $\bm{\mathsf{y}}_u^+$ is non-trivial.
- What differs: The authors handle the expected curve first and label it ('straightforward because ...'), then turn with 'However, ... is non-trivial', so the reader knows which curve to look at. The model puts both curves in one sentence, leads with the surprising one, drops in the expected one as a 'while' clause, and gives no label for either.

**A27** (I2, from the paper 2505.16932, intro section)
- Draft: The most direct way to obtain $polar(\mM)$ is through an SVD, which costs $O(mn\min(m,n))$ time and is hard to parallelize on GPUs.
- Authors: Although $\mathrm{polar}({\bm{M}})$ can be computed directly via an SVD in $O(mn\min(m,n))$ time, doing so is prohibitively expensive in deep learning applications, especially as standard SVD algorithms fail to take full advantage of the parallelism available on GPUs.
- What differs: The authors concede the direct route in an "Although" clause and then give the verdict ("prohibitively expensive in deep learning applications"). The model lists the cost and the parallelism problem as neutral facts and never says the route is ruled out.

**A28** (R1, from the paper 2602.02908, results section)
- Draft: For UNets on FFHQ64 at $n = 3\!\cdot\!10^4$, it correlates with the observed cross-split MSE over 1000 seeds, with Spearman correlation 0.33 ($p = 2.5\times10^{-26}$; Figure REFF).
- Authors: Spatially, the inhomogeneity effect is borne out: RMT predictions correlate with observed cross-split deviations for each initial noise; e.g., UNets trained on FFHQ64 with $n=30000$ achieve a Spearman correlation of $0.33$ ($p=2.5\times10^{-26}$) over 1000 seeds (Fig. REFF).
- What differs: The authors give the verdict and the general claim first ('Spatially, the inhomogeneity effect is borne out: RMT predictions correlate ...') and the number as 'e.g.'; the model opens on the specific configuration with 'it' as subject and reports the correlation without saying the prediction is confirmed.

**A29** (I7, from the paper 2407.10490, intro section)
- Draft: This analysis points to a simple method that improves alignment by weakening the squeezing effect.
- Authors: Inspired by this, we propose a simple but very effective method to further improve alignment performance.
- What differs: The authors own the contribution ('we propose') and evaluate it ('simple but very effective'), right after a one-line stakes sentence ('This can be detrimental to the alignment we are trying to achieve'); the model hands agency to 'this analysis points to', drops the stance, and never says plainly that the effect harms alignment.

**A30** (I7, from the paper 2505.10465, intro section)
- Draft: Actual LLMs, shown as gray points in the same panel, follow a similar exponent near 1.
- Authors: Remarkably, we find that actual LLMs follow a similar scaling.
- What differs: The authors flag the LLM agreement as striking ('Remarkably') and keep the sentence short. The model gives it the flat tone of a figure note and puts plotting detail between subject and verb.

### Restate the point in plain words

The authors say the technical thing and then the plain thing ("i.e.", "This means", "That explains why", "Thus", "Overall"), or end a paragraph on its point rather than on its last detail. The drafts keep only one of the two and end on the detail or the caveat. Redundancy that helps a skimming reader is not padding.

**A31** (I5, from the paper 2406.05946, intro section)
- Draft: In current LLMs, safety alignment adapts the output distribution mainly over the first few tokens of a response.
- Authors: In this paper, we examine one underlying problem in current safety alignment that may make models particularly vulnerable to relatively simple exploits: safety alignment is largely only a few tokens deep, i.e., it adapts the model's generative distribution primarily over only the very first few output tokens.
- What differs: The authors state the thesis twice in one sentence: first as a memorable plain phrase ('only a few tokens deep'), then the technical gloss after 'i.e.'; the model keeps only the gloss, so the reader gets no short handle that the title and later sections can echo.

**A32** (I5, from the paper 2505.12741, intro section)
- Draft: From outside, looks like any other LLM system, since text enters at the bottom and leaves at the top.
- Authors: Thus, LMNet keeps the external interface of ordinary LLM systems while making internal communication learnable.
- What differs: The authors close the paragraph with a 'Thus' recap that pairs what stays (the interface) with what changes (learnable internal communication). The model keeps only the first half, so the paragraph ends on a detail instead of the point.

**A33** (R10, from the paper 2505.10465, results section)
- Draft: Negative biases cancel part of this signal through the ReLU. The rest adds to the loss of the sample, which therefore grows with the squared overlaps $(W_i\cdot W_j)^2$ summed over $i\neq j$.
- Authors: The loss arises from the non-zero overlaps between representation vectors.
- What differs: After the formula, the authors restate the point in plain words (the loss comes from non-zero overlaps between vectors). The model ends on the formula after a 'therefore' and never gives the one-line takeaway.

**A34** (I3, from the paper 2505.16932, intro section)
- Draft: As a result, the method is fast in its first iterations and converges super-exponentially in the later ones (REF), whereas the recent heuristic proposals REF do not converge at all. In practice it reaches a good approximation within five to ten iterations.
- Authors: Our method converges to $\mathrm{polar}(\bm{M})$ super-exponentially (REF), and it quickly reaches a good approximation within just five to ten iterations. This early-stage acceleration is especially valuable in deep learning applications, where runtime efficiency takes precedence over high accuracy.
- What differs: After the speed claim the authors add one sentence on why it matters, tying back to the opening requirement (runtime over accuracy). The model leaves the five-to-ten-iterations figure as a bare fact and never reconnects it to the deep-learning stakes set up at the start.

**A35** (R10, from the paper 2502.00640, results section)
- Draft: Proactive Base improves steadily but remains below CollabLLM at every checkpoint, although individual ratings vary widely at each one.
- Authors: This suggests that CollabLLM maintains sustained engagement more effectively.
- What differs: The authors end the paragraph with a plain, hedged one-line summary of what the curves mean. The model ends on a caveat about variance, so the paragraph's last word is a concession, not the finding.

### Read the table by the comparison that matters

The drafts walk through cells, rows and panels; the authors state the one contrast the argument needs, with the rest as a concession clause or an example.

**A36** (R2, from the paper 2406.05946, results section)
- Draft: Without a prefix, the base models answer harmfully on 68.6% (Llama-2-7B) and 85.4% (Gemma-7B) of the instructions. Every prefix lowers both rates. The longest one, "I apologize, but I cannot", brings them down to 2.1% and 1.0%. Notably, the gap between base and aligned models narrows sharply once both start from the same refusal prefix, even though the base models have received no safety training of any kind.
- Authors: Although the unaligned base models generally have higher ASR than their aligned counterparts in standard decoding, the gap considerably decreases when both models are forced to start with refusal prefixes.
- What differs: The authors read the table by the one contrast the argument needs (the base-vs-aligned gap closes under a refusal prefix), with the no-prefix baseline as a concession clause; the model walks through cells for three sentences and reaches the gap only in the fourth, behind 'Notably'.

**A37** (R2, from the paper 2505.16932, results section)
- Draft: Figure REF shows that on GPT-2-Small, muon-PolarExp achieves a lower final validation loss than the other two variants at every learning rate. At each method's best rate it ends at 3.588 (lr $= 0.005$), against 3.629 for muon-You and 3.639 for muon-Jordan (both lr $= 0.01$). The AdamW-only baseline adamw trails considerably, at 4.197 with lr $= 0.0005$. On GPT-2-Large, muon-PolarExp is again lowest at every learning rate (Figure REF), reaching 3.340 at the shared best rate of 0.02, against 3.398 for muon-Jordan and 3.399 for muon-You.
- Authors: REF show the results in terms of validation loss for the GPT-Large and GPT-Small models, respectively. In both cases, muon-PolarExp achieves a better validation loss than muon-Jordan or muon-You. The advantage is remarkably consistent across all learning rates and epochs.
- What differs: The authors read both models at once ("In both cases") and add the one evaluative sentence the figures support ("remarkably consistent across all learning rates and epochs"). The model walks model by model through best-rate cell values and never states the cross-model pattern.

**A38** (R2, from the paper 2504.15266, results section)
- Draft: For the smaller and the diffusion model , Figure REF shows that diffusion training improves algorithmic creativity over next-token training on three of the four tasks. We report each model at its best sampling setting, searched over temperatures in $\{0, 0.5, 1, 2\}$ with and without top-$K$ sampling ($K = 50$). The diffusion gains are clearest on the two exploratory tasks, Circle and Line Construction; on , the one exception, both diffusion variants (Absorb and Uniform) score mildly below next-token training.
- Authors: For the smaller models, in Fig REF, we find that the diffusion model improves over next-token training of similar-sized Transformers on all tasks, except on Sibling Discovery where it is mildly worse.
- What differs: The authors read the figure as one rule with one exception in a single sentence ('on all tasks, except on Sibling Discovery where it is mildly worse'). The model gives a count ('three of the four tasks'), breaks off for a protocol sentence, and names the exception two sentences later.

**A39** (R2, from the paper 2502.00640, results section)
- Draft: The two models start from about the same rating at turn 3. CollabLLM's rating then rises by turn 6 and holds at turn 9, whereas the rating of Base falls back between turns 6 and 9.
- Authors: In contrast, both CollabLLM and Proactive Base exhibit increasing ratings over time, with CollabLLM consistently achieving higher average ratings every three turns compared to Proactive Base.
- What differs: The authors read the plot by grouping (Base declines, while both proactive models rise) and then make the one comparison that matters (CollabLLM above Proactive Base at every checkpoint). The model goes through the checkpoints one by one for two models.

**A40** (R2, from the paper 2505.12741, results section)
- Draft: Self-Consistency also cannot cover every task: it is marked N.a.\ on HumanEval and MBPP, because a vote over programs needs a notion of agreement that is undefined without outside feedback. requires no agreement between answers and applies unchanged to all eleven benchmarks.
- Authors: Another advantage of LMNet over TTS methods is that it is generally applicable. For example, we could not apply Self-Consistency to coding tasks without external feedback as the consistency of code is not defined, let alone other TTS methods requiring an additional verifier or step-wise decomposition.
- What differs: The authors state the point first (LMNet is generally applicable) and use Self-Consistency on code as the example. The model starts from table cells (N.a. on HumanEval and MBPP) and reaches LMNet's advantage only in its last sentence.

## Part B. Further sentences by move, from the same papers and others

### Openings (I1)

**B1** (I1, 2503.14858) While scaling model size has been an effective recipe in many areas of machine learning, its role and impact in reinforcement learning (RL) remain unclear.
- Why it works: Sets the field with a fact nobody disputes and opens the question in the main clause, so the first sentence already carries the paper's topic.

**B2** (I1, 2406.02507) Denoising diffusion models [cite] generate synthetic images by reversing a stochastic corruption process. Essentially, an image is revealed from pure noise by denoising it little by little in successive steps.
- Why it works: Pair: a one-line technical definition, then 'Essentially' restates it in everyday words, so readers of either level are on board after two sentences.

### Stakes (I3)

**B3** (I3, 2402.06782) As these systems continue to advance, they will surpass expert knowledge. Consequently, there will be no ground truth to rely on, rendering most alignment approaches unusable.
- Why it works: Pair: a two-step consequence chain in plain words; the stakes follow by logic, not adjectives.

**B4** (I3, 2407.05872) This mismatch may persist silently until the model is scaled past a threshold where the difference in exponents dominates over other factors: a risky situation in the current "train once" era of very large models.
- Why it works: Says when the failure shows up, then a short tail after the colon names the practical cost ('train once'), so the stakes come from the mechanism and need no hype.

### The turn to this paper (I4)

**B5** (I4, 2304.15004) In this paper, we call into question the claim that LLMs possess emergent abilities, by which we specifically mean sharp and unpredictable changes in model outputs as a function of model scale on specific tasks.
- Why it works: 'In this paper' marks the turn, and the 'by which we specifically mean' clause pins the disputed term down, so the reader knows exactly what is being doubted.

**B6** (I4, 2502.06768) Therefore, we ask: Are the benefits of inference flexibility for MDMs enough to outweigh the drawbacks of training complexity?
- Why it works: Turns the two factors just listed into one yes/no question that the rest of the introduction answers.

### Orientation phrases (I8)

**B7** (I8, 2404.07965) To explore how language models learn at the token level, we initially examined training dynamics, particularly how the token-level loss evolves during usual pretraining.
- Why it works: Purpose-first opener ('To explore ...') tells the reader why the analysis is coming before what it is.

**B8** (I8, 2503.14858) At first glance, it makes sense why training very large RL networks should be difficult: the RL problem provides very few bits of feedback (e.g., only a sparse reward after a long sequence of observations), so the ratio of feedback to parameters is very small.
- Why it works: 'At first glance' warns the reader this is the common view the paper will revise, and the colon delivers the reason with a parenthetical example.

**B9** (I8, 2410.02355) Broadly, model editing approaches fall into two categories: (1) parameter-modifying methods, which directly adjust a small subset of parameters [cite], and (2) parameter-preserving methods that integrate additional modules without altering the original parameters [cite].
- Why it works: 'Broadly' and 'two categories' set up the map before the items, each defined by one relative clause.

### An example after an abstract claim (I9)

**B10** (I9, 2310.16834) Although modern autoregressive transformers have produced stunning results [cite], there are limits. For example, the sequential sampling of tokens is slow, hard to control, and often degrades without distribution annealing techniques like nucleus sampling [cite].
- Why it works: Pair: concedes success in a clause, makes the abstract claim in three words ('there are limits'), then makes it concrete with three named problems.

**B11** (I9, 2412.09871) Central to our architecture is the idea that models should dynamically allocate compute where it is needed. For example, a large transformer is not needed to predict the ending of most words, since these are comparably easy, low-entropy decisions compared to choosing the first word of a new sentence.
- Why it works: States the design principle, then grounds it in a case every reader knows (word endings versus sentence starts).

### Hand-offs that keep the introduction moving (I10)

**B12** (I10, 2410.02355) A detailed theoretical proof is provided in Section REF.
- Why it works: A one-line hand-off placed right after the claim it supports, then the paragraph moves on; no roadmap paragraph needed.

**B13** (I10, 2502.06768) While the above might appear to be bad news for MDMs, in the second part of this paper, we answer our guiding question in the affirmative by building upon the observation [cite] that MDMs which can perfectly solve all masking subproblems can be used to decode in any order.
- Why it works: Concedes the first part in one clause, then tells the reader where the paper turns and which answer to expect.

### Concessions in a clause (R5)

**B14** (R5, 2405.19261) Methods that use speculative execution are considerably faster than sequential token-level cascades (TokenCascade [Chow]), although sequential cascades do have an advantage in the low-latency regimes.
- Why it works: Main comparison first, then the regime where the loser wins, conceded in one clause before the next sentence explains it.

**B15** (R5, 2406.02507) While conditional ImageNet generation may be getting close to saturation, the unconditional results remain surprisingly poor.
- Why it works: Concedes the saturated setting in the subordinate clause and moves the reader to the setting where the method has room to show.

### Boundaries stated once (R6)

**B16** (R6, 2405.19261) We also do not claim to develop a new state-of-the-art method for fast LM inference.
- Why it works: Draws the scope line once, in the evaluation setup, so readers do not judge the results against the wrong baseline family.

**B17** (R6, 2406.11011) Due to computational resource constraints, most of our experiments focus on the GPT-2 and Pythia-410M models, but this is not a limitation of the algorithm itself.
- Why it works: Separates the experiment's scale limit from the method's scope in one clause each.

### Surprises earned by the setup (R8)

**B18** (R8, 2403.06634) Generally, attacks that operate under stronger threat models have higher precision. But theoretical improvements are not always practical: the theoretically stronger attack from §REF that learns 5 logprobs per query in practice requires more queries and recovers logits with lower fidelity.
- Why it works: (pair) States the expected pattern first, then the exception it breaks, so the surprise is earned by the setup rather than by an adjective.

**B19** (R8, 2605.00768) One might hope that positional encodings would allow global attention to approximate locality. In our experiments, however, neither SiPE nor RoPE compensates for the absence of local attention: Positional encodings do not erase the qualitative separation between global-only and hybrid models; on the contrary, they often reduce performance on the tested languages.
- Why it works: [pair] States the reasonable expectation first, then refutes it with the specific encodings tested and scopes it to 'the tested languages'.

### Setup sentences that read easily (R9)

**B20** (R9, 2401.06416) To produce confidence intervals for our experiments, we train 5 sets of models for each language using different random seeds, which affect the model parameter initialization and dataset shuffling during training.
- Why it works: Says why before what (confidence intervals), gives the count (5 seeds per language), and says what a seed varies.

**B21** (R9, 2407.05872) We investigate the role of alignment, per-layer learning rate exponents and constant factors, and the epsilon hyperparameter by running tens of thousands of experiments in a Transformer language model across all combinations of the three optimizers, four parameterizations, learning rate sweeps with a granularity of 2^0.25 or 2^0.5, and fourteen model widths ranging up to 26.8 billion parameters.
- Why it works: Questions first, then the grid as counted axes (three, four, fourteen) joined by 'across all combinations of', so a large sweep reads as one design.

### Recaps in plain words (R10)

**B22** (R10, 2504.13837) Based on these results, we conclude that RLVR increases the likelihood of sampling correct responses at low k, but narrows the model's overall coverage.
- Why it works: Both halves of the pass@k crossover in one balanced sentence with 'but' as the hinge.

**B23** (R10, 2505.06120) In short, no matter how strong an LLM's single-turn performance is, we observe large performance degradations in the multi-turn setting.
- Why it works: Closes the paragraph by stating the finding without model names or numbers, after those were given.

## Sources

The authors' sentences above are quoted from the papers below, with citations and cross-references replaced by [cite] and REF. Copyright stays with the authors; licenses as listed on arXiv (checked 2026-10-10 and 2026-10-17).

| arXiv | Title | License | Part A pairs | Part B sentences |
|---|---|---|---|---|
| [2304.15004](https://arxiv.org/abs/2304.15004) | Are Emergent Abilities of Large Language Models a Mirage? | CC BY-NC-ND 4.0 | 0 | 1 |
| [2310.16834](https://arxiv.org/abs/2310.16834) | Discrete Diffusion Modeling by Estimating the Ratios of the Data Distribution | CC BY 4.0 | 0 | 1 |
| [2401.06416](https://arxiv.org/abs/2401.06416) | Mission: Impossible Language Models | CC BY 4.0 | 0 | 1 |
| [2402.06782](https://arxiv.org/abs/2402.06782) | Debating with More Persuasive LLMs Leads to More Truthful Answers | arXiv non-exclusive license | 0 | 1 |
| [2403.06634](https://arxiv.org/abs/2403.06634) | Stealing Part of a Production Language Model | arXiv non-exclusive license | 0 | 1 |
| [2404.07965](https://arxiv.org/abs/2404.07965) | Rho-1: Not All Tokens Are What You Need | arXiv non-exclusive license | 0 | 1 |
| [2405.19261](https://arxiv.org/abs/2405.19261) | Faster Cascades via Speculative Decoding | CC BY 4.0 | 0 | 2 |
| [2406.02507](https://arxiv.org/abs/2406.02507) | Guiding a Diffusion Model with a Bad Version of Itself | arXiv non-exclusive license | 0 | 2 |
| [2406.05946](https://arxiv.org/abs/2406.05946) | Safety Alignment Should Be Made More Than Just a Few Tokens Deep | arXiv non-exclusive license | 2 | 0 |
| [2406.11011](https://arxiv.org/abs/2406.11011) | Data Shapley in One Training Run | CC BY 4.0 | 0 | 1 |
| [2407.05872](https://arxiv.org/abs/2407.05872) | Scaling Exponents Across Parameterizations and Optimizers | CC BY 4.0 | 0 | 2 |
| [2407.10490](https://arxiv.org/abs/2407.10490) | Learning Dynamics of LLM Finetuning | CC BY-NC-SA 4.0 | 5 | 0 |
| [2410.02355](https://arxiv.org/abs/2410.02355) | AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models | CC BY 4.0 | 0 | 2 |
| [2412.09871](https://arxiv.org/abs/2412.09871) | Byte Latent Transformer: Patches Scale Better Than Tokens | CC BY 4.0 | 0 | 1 |
| [2502.00640](https://arxiv.org/abs/2502.00640) | CollabLLM: From Passive Responders to Active Collaborators | arXiv non-exclusive license | 2 | 0 |
| [2502.06768](https://arxiv.org/abs/2502.06768) | Train for the Worst, Plan for the Best: Understanding Token Ordering in Masked Diffusions | CC BY 4.0 | 0 | 2 |
| [2503.14858](https://arxiv.org/abs/2503.14858) | 1000 Layer Networks for Self-Supervised RL: Scaling Depth Can Enable New Goal-Reaching Capabilities | CC BY 4.0 | 0 | 2 |
| [2504.13837](https://arxiv.org/abs/2504.13837) | Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model? | CC BY 4.0 | 0 | 1 |
| [2504.15266](https://arxiv.org/abs/2504.15266) | Roll the dice & look before you leap: Going beyond the creative limits of next-token prediction | CC BY 4.0 | 2 | 0 |
| [2505.06120](https://arxiv.org/abs/2505.06120) | LLMs Get Lost In Multi-Turn Conversation | CC BY 4.0 | 0 | 1 |
| [2505.10465](https://arxiv.org/abs/2505.10465) | Superposition Yields Robust Neural Scaling | CC BY 4.0 | 6 | 0 |
| [2505.12741](https://arxiv.org/abs/2505.12741) | Language Model Networks: Supervision-Efficient Learning through Dense Communication | CC BY 4.0 | 6 | 0 |
| [2505.16932](https://arxiv.org/abs/2505.16932) | The Polar Express: Optimal Matrix Sign Methods and Their Application to the Muon Algorithm | arXiv non-exclusive license | 12 | 0 |
| [2602.01338](https://arxiv.org/abs/2602.01338) | High-accuracy sampling for diffusion models and log-concave distributions | arXiv non-exclusive license | 3 | 0 |
| [2602.02908](https://arxiv.org/abs/2602.02908) | A Random Matrix Theory Perspective on the Consistency of Diffusion Models | CC BY 4.0 | 2 | 0 |
| [2605.00768](https://arxiv.org/abs/2605.00768) | Characterizing the Expressivity of Local Attention in Transformers | CC BY 4.0 | 0 | 1 |
