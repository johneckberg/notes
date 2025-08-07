# EBM

This markdown document outlines the core concepts of energy-based machine learning models, reflecting a practical, less formal perspective on the topic.

## Energy-Based Models: A High-Level View

The fundamental idea behind **energy-based models (EBMs)** is to shift the problem from a traditional classification or regression task to a scoring problem. Instead of predicting a specific output, we learn an **energy function** that assigns a low energy score to correct or "good" answers and a high energy score to incorrect or "bad" answers. The challenge is that there are infinitely many "bad" answers, which makes this task non-trivial.

A great example of this is **CLIP** by OpenAI. Imagine a classification problem where you want to classify an image. Now, imagine wanting to add more and more classes, until you have an infinite number. This is the kind of problem EBMs are great at. They don't need to categorize every possible output; they just need to learn what "good" looks like versus what "bad" looks like.

---

## The Boltzmann Distribution and Its Properties

The core of many EBMs is the **Boltzmann distribution**, which defines a probability distribution over possible outputs based on their energy. The probability of an output $y$ given an input $x$ is defined as:

$$P(y|x) = \frac{e^{-E(x,y)/T}}{Z(x)}$$

Here, $E(x,y)$ is the energy function, and $T$ is a temperature parameter. The term $Z(x)$ is the **partition function** or **normalizing constant**, which is the sum (or integral) of $e^{-E(x,y)/T}$ over all possible outputs $y$. This ensures the probabilities sum to one:

$$Z(x) = \sum_{y} e^{-E(x,y)/T}$$

A conjecture that often comes up is that any **discrete distribution** can be represented using the Boltzmann energy distribution with a suitable energy function. While this is a widely cited idea, it's important to note the original caveats from LeCun's 2006 work on the topic.

You can also model any probability mass function (**pmf**) from the **exponential family** using the Boltzmann distribution.

---

## Contrastive Learning and Intractable Normalization

The normalizing constant $Z(x)$ is often **intractable** to compute, especially in high-dimensional spaces, which makes **Maximum Likelihood Estimation (MLE)** difficult. If we were to treat $Z(x)$ as a parameter to be learned, we could make the likelihood arbitrarily large by simply making $Z(x)$ go to zero, which is a problem for MLE.

This is where **contrastive learning** becomes incredibly powerful. Contrastive learning doesn't require us to compute the exact value of $Z(x)$. Instead, it focuses on pushing down the energy of "good" examples and pushing up the energy of "bad" or "negative" examples. This allows us to estimate the model's parameters even when the likelihood function is intractable. While this approach is not perfectly rigorous, it works remarkably well in practice.

---

## Quick Note on Connection to Generalized Linear Models

Energy-based loss functions connect to **Generalized Linear Models (GLMs)** through the Boltzmann distribution. When the temperature $T=1$, the Boltzmann distribution becomes the **softmax function**
$$P(y|x) = \frac{e^{-E(x,y)}}{\sum_{y'} e^{-E(x,y')}}$$
This is the same functional form used in softmax regression, which is a type of GLM. Specifically, softmax regression is a GLM with a categorical likelihood function and a logit link function. Thus, energy-based models can be seen as a generalization of softmax regression where the "energy" function $E(x,y)$ is learned and can be arbitrarily complex, rather than a simple linear combination of features. Adjusting the temperature parameter $T$ allows for control over the "sharpness" of the probability distribution; a lower temperature increases confidence, while a higher temperature makes the distribution more uniform.