# EBM

This markdown document outlines the core concepts of energy-based machine learning models, reflecting a practical, less formal perspective on the topic.

## Energy-Based Models: A High-Level View

The fundamental idea behind **energy-based models (EBMs)** is to shift the problem from a traditional classification or regression task to a scoring problem. Instead of predicting a specific output, we learn an **energy function** that assigns a low energy score to correct or "good" answers and a high energy score to incorrect or "bad" answers. The challenge is that there are infinitely many "bad" answers, which makes this task non-trivial.

A great example of this is **CLIP** by OpenAI. When training Clip, you run into the issue of having an unkown (potentially infinite) number of classes to categorize images into. When doing this sort of embedding based zero shot classification, the loss is often just the softmax but instead of there being a fixed matrix representing a fixed number of output classes, with energy based embeddings we have a non fixed number of output classes, meaning our coefficient matrix is determined by the other vectors in the batch. This is why EBM is so powerful, you don't need to categorize every possible output; you just need to learn what "good" looks like versus what "bad" looks like.

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

Energy-based loss functions connect to **Generalized Linear Models (GLMs)** through the Boltzmann distribution. When the temperature $T=1$ and the energy function is just the dot product, the Boltzmann distribution becomes the **softmax function**
$$P(y|x) = \frac{e^{-E(x,y)}}{\sum_{y'} e^{-E(x,y')}}$$