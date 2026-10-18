# Claim strength: neither defending nor overreaching

A claim can fail in two directions. Defending is the paper arguing against itself on the reviewer's behalf; overreach is a reading that goes further than its evidence. The fix is the same for both: state the strongest claim the evidence supports, with its condition, and give a concession one clause.

The idea of writing a paper around what it actually achieves, rather than as an even report of everything that was tried, comes from the press-release principle of [Adkid-Zephyr/anti-defensive-writing-Skill](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill) (MIT License). This file keeps that idea in general form and pairs it with an honesty line of its own.

## What the reader needs from the claims

- **To know what the paper wins.** After the abstract and the introduction the reader can say which problem the paper solves or which question it answers, under which condition, and why that matters. A paper that gives every result equal weight leaves the reader to dig the contribution out of the tables.
- **The logic that holds, not the history.** The reader needs the reasons the result stands. The order in which things were tried, and what failed on the way, belongs in a lab notebook.
- **A reason for each result to be there.** Every experiment or analysis in the main text answers a question the argument raises, such as whether the method works, where its advantage comes from, or whether a simpler explanation would do. If the reader cannot name the question, the result belongs in the appendix or nowhere.
- **Claims they can trust.** Each claim carries its condition (on these benchmarks, at this scale, in our setting). Correlation reads as correlation. An explanation that is not settled reads as a conjecture ("This suggests that", "is consistent with") and is worded the same way wherever it appears. A label supports what its definition says and no more. A mechanism from the literature is cited with cf. and not grafted onto your own result with an as- or since-clause.
- **Weak results as facts with their condition.** "On X the method matches the baseline within variance, at a third of the compute" tells the reader what holds. "Unfortunately, our method only matches the baseline on X" tells them how the authors feel. A small gain is a small positive gain, and a difference inside the noise is mostly variation. A single run is one sample, so the number of runs and the spread are reported.
- **Limits stated once.** A weakness every reviewer will ask about goes into the Limitations paragraph once, with the conclusion it affects and the one it leaves untouched. Repeated at the end of every paragraph, it reads as a paper that does not believe itself.

## Verbs by what the evidence is

The verb of a result sentence tells the reader how far the evidence goes, so it is chosen by the evidence, not by the strength the authors would like. Published papers in this field use these verbs often (show that in 199 of 307 award papers, demonstrate that in 121, suggest that in 89, indicate that in 75); drafts use them about a third less often and state the result bare.

- *is consistent with, suggests, may, appears to*: a pattern in the data that fits the reading, with other readings not ruled out. One hedge is enough; "may possibly suggest" stacks three.
- *indicates, points to*: the data favour this reading over the obvious alternatives, but nothing was controlled.
- *shows, we find that*: measured directly, under the stated condition.
- *demonstrates, establishes*: measured with the alternative explanations ruled out, by an ablation, a control or an intervention.
- *proves*: a theorem, nothing else.
- *confirms*: only a prediction stated before the result; *reveals*: only something that was not visible before; *significantly*: only with a test behind it, where it is the right word.
- *is designed to, is meant to, is intended to, we expect*: below the ladder. These say what a component is for, not what it did, and stay true whether or not the experiment bears them out. Intent and outcome are two sentences or two clauses with their own verbs ("The gate is designed to drop distractors; Table 3 shows that it does"), never one verb doing both ("the gate is designed to remove distractors, improving recall by 4 points").

A paper that writes "demonstrates" for a correlation and "suggests" for its main ablated result has the ladder upside down: a reviewer reads the first as overreach and the second as the authors not believing their own evidence. A pointer frame ("As shown in Table 2,") says where the evidence is; it does not say how far it goes, so it precedes a reporting verb rather than replacing one.

## When a result does not support the story

Rebuild the story around the strongest evidence instead of defending the original plan. Narrow the claim to what holds, choose the setting or comparison where the paper's value shows, or move a result that does not bear on the contribution out of the main line. Two things stay off the table: dropping a result that bears on the core claim, and hiding the condition under which the method fails.

## What the read-back looks for

Signs of defending:

- A concession that takes a full sentence ("However, it must be acknowledged that regressions also shrink.") where a clause would do ("Repairs shrink across rounds, as do regressions.").
- A boundary sentence closing every paragraph instead of one at the end of the subsection.
- A self-weakening word on your own result (unfortunately, merely, still lags behind) where the fact and its condition would do. These are flagged for a look, not banned; "only" is right when it restricts scope.
- A sentence that answers an objection no reader would raise, or turns one local result into a verdict on the whole method.
- A conclusion that ends on a new limitation.

Signs of overreach:

- A claim stripped of its condition, or a qualifier deleted in revision.
- Correlation written as cause, or a conjecture written as a finding ("We trace this to" where the evidence gives "This suggests").
- A label read beyond its definition ("our probe does not attribute a cause" turned into "there is no cause").
- A cause imported from a cited paper and attached to your own result.
- A reporting verb stronger than its evidence ("demonstrates" on a correlation) or weaker ("suggests" on an ablated result), or a result stated bare where the field would say what the evidence shows.
- A design intent standing where the result should be ("is designed to remove X" as the only sentence on whether X was removed), or intent and outcome fused in one verb.
