# Data and Concept Drift: Measuring Model Quality in Production

Monitoring ML models is harder than classical software because models often fail silently. Relying on customer feedback is "professional negligence"; you need proactive ways to detect when the model is no longer performing as expected.

## 1. Distribution Shift (Data Drift)

This occurs when the input data changes, making the input distribution non-stationary.

* **Covariate Shift**: Detecting this in complex domains like text is difficult.
* **Explanation Shift**: A method for detecting shifts in tabular data by analyzing the "explanation space."
* **Impact**: Data drift does not always degrade performance; it is important to distinguish between benign and harmful shifts.
* **Resources**:
* [When data drift does not affect performance (NannyML)](https://www.nannyml.com/blog/when-data-drift-does-not-affect-performance-machine-learning-models).
* [Explanation Shift: Detecting distribution shifts on tabular data via the explanation space (Arxiv)](https://arxiv.org/abs/2210.12369).



## 2. Concept Drift & Performance Estimation

Concept drift occurs when the relationship between inputs and outputs changes. Since labels are often delayed, we use estimation:

* **CBPE (Confidence-Based Performance Estimation)**: Estimates metrics like the confusion matrix using model confidence scores. Assumes the model is well-calibrated.
* **DLE (Direct Loss Estimation)**: Trains a "Nanny model" to predict the loss of the primary model. Essential for regression where metrics cannot be calculated on a single observation.

## 3. Domain-Specific Confidence & Calibration

Different architectures require specialized calibration to ensure confidence scores are trustworthy.

* **ASR (Speech)**: Uses entropy-based methods for word-level confidence.
* **Resource**: [Entropy-Based Methods for Word-Level ASR Confidence Estimation (NVIDIA)](https://developer.nvidia.com/blog/entropy-based-methods-for-word-level-asr-confidence-estimation/).
* **Key Idea**: Moving beyond raw probabilities to Tsallis and Rényi entropy to better detect incorrect words.


* **Zero-Shot (Vision-Language)**: Large models like CLIP are often miscalibrated in zero-shot settings.
* **Resource**: [Enabling Calibration In The Zero-Shot Inference of Large Vision-Language Models (Arxiv)](https://arxiv.org/abs/2303.12748).
* **Key Idea**: Proposes "Zero-Shot-Enabled Temperature Scaling" to preserve the ability to generalize to unseen classes while maintaining reliable confidence.



## 4. Temperature Scaling

A post-processing technique used to **calibrate** model probabilities.

* **The Method**: Divide the "logits" by a scalar  before the Softmax layer.
* **Source**: [On Calibration of Modern Neural Networks (Guo et al., 2017)](https://arxiv.org/abs/1706.04599).
* **Note**: For methods like **CBPE** to work, the model must be calibrated. If the model is overconfident, performance estimates will be wrong.