# Hypothesis Testing

## Notes and Questions from "The insignificance of Null Hypothesis Testing

* [Misunderstanding a P-value?](https://stats.stackexchange.com/questions/166323/misunderstanding-a-p-value/166327#166327)
  * "The p – value represents the apriori probability of making a type I error, that is, of rejecting the null hypothesis under the assumption that it is true."
  * This **IS NOT** the same as saying that its, "the probability of making a type I error, or rejecting the null hypothesis when it is true."
  * 
* [Interpretation of p-value in hypothesis testing](https://stats.stackexchange.com/questions/46856/interpretation-of-p-value-in-hypothesis-testing)
  * "The combination of Fisherian P-values with Neyman-Pearsonian error rates has been called an incoherent mishmash, and it is unfortunately very widespread."
  * "A decision to reject the null hypothesis on the basis of a small P-value typically depends on 'Fisher's disjunction': Either a rare event has happened or the null hypothesis is false. In effect, it is rarity of the event is what the P-value tells you rather than the probability that the null is false."

[utexas: Type I and II Errors and Significance Levels](https://web.ma.utexas.edu/users/mks/statmistakes/errortypes.html)


**Under any null hypothesis, the p-values are uniformly distributed: all p-values between 0 and 1 are equally likely.**

In leu of a formal proof, here’s some intuition. For any significance level $\alpha$, how often will a statistical test under the null hypothesis give a significant result that we falsely reject? Of course $\alpha$, by the definition of the significance level. But for a test to be significant at $\alpha$, it must be true that the p-value $p < \alpha$. So we’re saying that $p < \alpha$ with probability $\alpha$. Or $Pr(p < \alpha) = \alpha$, which is the definition of a uniform distribution.

More formally, when we perform a statistical test, we calculate some statistic $\hat{S}$ from the data. Under the null, this statistic follows some distribution $S$. The statistic $\hat{S}$ is associated with a p-value $\hat{p}$, which by definition is the probability that the test statistic is at least as extreme as $\hat{S}$: $\hat{p} = Pr(S > \hat{S})$. But note also that for the p-value to be smaller than $\hat{p}$ would require that the test statistic be larger than $\hat{S}$, so $Pr(p < \hat{p}) = Pr(S > \hat{S})$, which we just said is equal to $\hat{p}$. So $Pr(p < \hat{p}) = \hat{p}$, which is again the definition of a uniform distribution.

If you decide to reject the null whenever p<0.05, you are essentially "trapping" the bottom 5% of that uniform distribution. If you start claiming your error rate is 1% just because you got a 0.01, you are "cherry-picking" your significance level after seeing the data. To have a long-run error rate of 1%, you would have had to commit to α=0.01 before you ran the test.

Every single value in that 0 to 0.05 range is a "false alarm."

Notice that nowhere did I have to assume anything about $S$, the distribution of the test statistic. This result holds no matter what test statistic we do.

* So let's present a case of this contradiction:
  * Consider the following situation:
    * The null hypothesis is true.
    * α has been set conventionally at 0.05.
    * The computed p-value is 0.01.
  * Now, the probability of getting data as extreme or more extreme than your data is 1% (that's what the p-value   means). You have rejected the null hypothesis, making a type I error. Is it true that the long run type I error rate in this situation is also 1%?
  * Type I error isn't a property of a single result, its a property of the significance level you set. alpha is the probability of making a type 1 error, not p. You would reject the null hypothesis anytime the p value is below alpha. The long run probability of this is then alpha, not p. If you had gotten a p-value of 0.02, you would still have rejected the null. In fact, you would have rejected the null even if p had been 0.0499 repeating.

## General Notes

* The real problem with conventional hypothesis testing is that it answers a question that you are not really interested in having answered, i.e. "is there significant evidence of a difference?", rather than "is there evidence of a significant difference?"
  * This is what effect size helps you quantify!

* A statistical test is associated with a specific probability distribution such as normal or students t, by using it to define the expected range of test statistic values under the null hypothesis

* A hypothesis is a claim or statement about a characteristic of a population of interest to us. A hypothesis test is a way for us to use our sample statistics to test a specific claim.

* The test statistic is a value computed from the sample data that is used in making a decision about the rejection of the null hypothesis.

* My brain is used to thinking in regards to paired model evaluations on the same data
  * paired t test, Mcnemar's test, etc
  * **I was having an issue because I was 1. tired and just coming out of a busy day, and 2. I was confused on the jump from research question to hypothesis because I'm just to (in my mind) more straightforward questions 
  * It is interesting how many ML papers...just dont give a shit about statistical significance.
    * Machine learning papers tend not to report this unless they use cross-fold validation. The issue is that, typically, the training set and test set are well-defined and identical for all choices of different methods. They are also sufficiently diverse that that variation of the data (which again, does not actually vary between methods) drives the volatility of methods. Confidence intervals are the wrong trick for this problem, and far too conservative for it. Consider what happens if you have two classifiers A,B and a multi-modal test set, with one large mode that A and B work equally well on at about 70% accuracy, and a second smaller mode that only B works on. Now by all objective measures B is better than A, but if the second mode is substantially smaller than the first, this might not be apparent under a confidence interval based test. The standard stats answer is to "just gather more data", but in the ML community, changing the test set is seen as actively misleading and cheating, as it means that the raw accuracy and precision of earlier papers can no longer be directly compared.
    * Usually, the performance is measured on some unseen data set. So how well the algorithm generalizes to new data can be deterministically measured, and there is no need for any confidence interval.
    * You might say,  "John, For any practical usecase, a test set is a sample!" However, there are some standard benchmark datasets, and tbh the field isn’t concerned with how these datasets generalize. The datasets are used only for ranking algorithms. So CI aren’t useful in this case. And honestly, I think this is reasonable; because we're not making any claim about the population. As long as the training/test/validation sets represent a reasonable problem, we can say something about how well an algorithm does on this specific type of problem. 

* Backing up,a test statistic is a single value derived from sample data used in hypothesis testing to determine if the observed performance difference is statistically significant.

