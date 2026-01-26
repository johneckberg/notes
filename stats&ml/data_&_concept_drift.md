# Data and Concept Drift: Measuring Model Quality in Production

Monitoring ML models is harder than classical software because models often fail silently. Relying on customer feedback is "professional negligence"; you need proactive ways to detect when the model is no longer performing as expected.

* **(2023) Catching silent failures: a machine learning model monitoring and explainability survey**

## 1. Distribution Shift/Covariate Shift (Data Drift)

This occurs when the input data changes, making the input distribution non-stationary.

* **Impact**: Data drift does not always degrade performance; it is important to distinguish between benign and harmful shifts.
* **Resources**:
* Look at nannyml for a practical review of pca based methods
* [When data drift does not affect performance (NannyML)](https://www.nannyml.com/blog/when-data-drift-does-not-affect-performance-machine-learning-models).
* **Explanation Shift**: A method for detecting shifts in tabular data by analyzing the "explanation space."
  * [Explanation Shift: Detecting distribution shifts on tabular data via the explanation space (Arxiv)](https://arxiv.org/abs/2210.12369).

* [Improving predictive inference under covariate shift by weighting the log-likelihood function](https://www.sciencedirect.com/science/article/abs/pii/S0378375800001154)
  * apparently covariate shift is less serious when models are correctly specified? Model misspecification in parametric models happens when the chosen model's assumptions (like linearity, normality, independence) don't match the true data-generating process, leading to biased parameter estimates, incorrect standard errors, unreliable hypothesis tests, and flawed predictions. Unclear if thats a reasonable assumption to make in industry (doesn’t seem like it is). 
  * Probably not worth getting too sucked into because the number of resources on covariate shift in production indicate it’s an issue.
  * for more, see the google paper: How Underspecification Presents Challenges for Machine Learning

* **This is closely related to OOD detection**
  * Outlier vs anomaly are sometimes used as distinct terms but are very often interchangeable. Better to focus specifically on the term out of distribution.
  * [Maximum Likelihood Estimation is All You Need for Well-Specified Covariate Shift](https://openreview.net/forum?id=eoTCKKOgIs)
  * In practice I think likelihood ratio methods are the best it’s just that they’re usually very expensive
  * Still trying to clarify the relationship between density ratios and likelihood ratios
    * [Likelihood ratios for OOD detection](https://arxiv.org/abs/1906.02845)
    * (2009) Direct importance estimation for covariate shift adaptation (first paper on density ratio estimation)
    * (2012) [A Kernel Two-Sample Test](https://jmlr.csail.mit.edu/papers/v13/gretton12a.html)
    * (2010) Statistical Outlier Detection for using Direct density ratio estimation

## 2. Concept Drift & Performance Estimation

Concept drift occurs when the relationship between inputs and outputs changes. Since labels are often delayed, we use estimation:

* **CBPE (Confidence-Based Performance Estimation)**: Estimates metrics like the confusion matrix using model confidence scores. Assumes the model is well-calibrated.
* **DLE (Direct Loss Estimation)**: Trains a "Nanny model" to predict the loss of the primary model. Essential for regression where metrics cannot be calculated on a single observation. [see NannyML for more info](https://nannyml.readthedocs.io/en/stable/)

## 3. Domain-Specific Confidence & Calibration

Different architectures require specialized calibration to ensure confidence scores are trustworthy.

* **ASR (Speech)**: Uses entropy-based methods for word-level confidence.
* **Resource**: [Entropy-Based Methods for Word-Level ASR Confidence Estimation (NVIDIA)](https://developer.nvidia.com/blog/entropy-based-methods-for-word-level-asr-confidence-estimation/).
* **Key Idea**: Moving beyond raw probabilities to Tsallis and Rényi entropy to better detect incorrect words.


* **Zero-Shot (Vision-Language)**: embedding based zero shot models like CLIP are often miscalibrated because of the energy based/contrastive training.
* **Resource**: [Enabling Calibration In The Zero-Shot Inference of Large Vision-Language Models (Arxiv)](https://arxiv.org/abs/2303.12748).
* **Key Idea**: Proposes "Zero-Shot-Enabled Temperature Scaling" to preserve the ability to generalize to unseen classes while maintaining reliable confidence.

* **Detecting covariate shift in text for LLM applications**

  * This is for classification purposes I think? but interesting none the less
    * [Measuring Distributional Shifts in Text: The Advantage of Language Model-Based Embeddings](https://arxiv.org/abs/2312.02337)



## 4. Temperature Scaling

A post-processing technique used to **calibrate** model probabilities.

* **The Method**: Divide the "logits" by a scalar  before the Softmax layer.
* **Source**: [On Calibration of Modern Neural Networks (Guo et al., 2017)](https://arxiv.org/abs/1706.04599).
* **Note**: For methods like **CBPE** to work, the model must be calibrated. If the model is overconfident, performance estimates will be wrong.

## Unorganized thoughts:

* Could we do energy based likelihood ratios to cancel out the normalizing constant while retaining the implicit knowledge?
  * the perturbed data would need to still originate from the original data generating distribution

* I have a gut feeling arf/forde could help with this but I need to do more research.
Arf is stupid fast bc it turns multivariate density estimators into a set of univariate estimators and can capture non linearities in a way that pca methods can’t. Also works with categorical variables in a way that pca methods can’t. Might also be more interpretable. 
  * There’s a note in the arf conclusion on how future work could be on anomaly detection 
  * We can use the knowledge that a certain feature was used for splitting more heavily across one forest vs another to indicate what feature has changed the most?
  * In general there seems to be a lot of Deep neural net based methods for tabular anomaly/ OOD detection. Why don’t we try to switch out the expensive neural network for a cheap ARF? 
  * Can we effectively perturb tabular data to estimate the density of just the background data? 
    * [Withdrawn but maybe interesting paper on likelihood tests for tabular data](https://openreview.net/forum?id=CX0Z5c0LbN)
    * Look at (2024) Unsupervised Anomaly Detection for Tabular Data Using Noise Evaluation