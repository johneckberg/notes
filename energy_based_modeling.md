# EBM

Yan LeCun: "probabilistic modeling comes with a high price, and should be avoided when the application does not require it"

[For more on this topic click here for lecuns website](https://cs.nyu.edu/~yann/research/ebm/)

## Energy-Based Models: A High-Level View

Energy based modeling is fundamentally about going back to the most basic problem: we have good answers we want to give a good score and bad answers we want to give a bad score. But there are too many damn bad answers.

A great example of this is **CLIP** by OpenAI. Imagine a classification problem where you want to classify an image. Now, imagine wanting to add more and more classes, until you have an infinite number. This is the kind of problem EBMs are great at. They don't need to categorize every possible output; they just need to learn what "good" looks like versus what "bad" looks like.

---

## The Boltzmann Distribution and Its Properties

The core of EBM is the **Boltzmann distribution**, which defines a probability distribution over possible outputs based on their energy. The probability of an output $y$ given an input $x$ is defined as:

$$P(y|x) = \frac{e^{-E(x,y)/T}}{Z(x)}$$

Here, $E(x,y)$ is the energy function, and $T$ is a temperature parameter. The term $Z(x)$ is the **partition function** or **normalizing constant**, which is the sum (or integral) of $e^{-E(x,y)/T}$ over all possible outputs $y$. This ensures the probabilities sum to one:

$$Z(x) = \sum_{y} e^{-E(x,y)/T}$$

$$Z(x) = \int_{ y\in Y} e^{-E(x,y)/T} $$


A conjecture that often comes up is that any **density function** can be represented using the Boltzmann energy distribution with a suitable energy function. While this is a nice idea, it's important to note that LeCun's 2006 tutorial is a much weaker statement of basically "you can mess with the energy function to model a good number of distributions; if they are PDFs then the integral defining the normalizing constant must converge."

[See the 2020 paper, "Your Classifier is Secretly an Energy Based Model and You Should Treat it Like One"](https://arxiv.org/abs/1912.03263)

I'm comfortable saying that you can model any **mass function** from an **exponential family** using the Boltzmann distribution and a smart choice of energy function, although I haven't (and don't have the skills) to prove it. 

## Contrastive Learning and Intractable Normalization

The normalizing constant $Z(x)$ is often **intractable**, especially in high-dimensional spaces, which makes **Maximum Likelihood Estimation (MLE)** difficult. If we were to treat $Z(x)$ as a parameter to be learned, we could make the likelihood arbitrarily large by simply making $Z(x)$ go to zero, which is a problem.

This is where **contrastive learning** comes into play. Contrastive learning doesn't require us to compute the exact value of $Z(x)$. Instead we acknowledge that if we estimate it, our loss will still "push down" the energy of "good" examples and "push up" the energy of "bad" or "negative" examples (or vice versa if your doing negative log likelihood). This allows us to estimate the model's parameters even when the likelihood function is intractable. While this approach is not perfectly rigorous, it works!

OpenAI's CLIP model provides a good example for the sort of problems this can solve. During pre-training, CLIP is optimized to align corresponding image-text pairs in a shared vector space. It does this by moving the output vectors of similar pairs closer together while simultaneously pushing the vectors of non-paired images and texts further apart.

Another example I think is important to note is self-supervised text and image embedding models. They create a positive pair by duplicating a datapoint and applying a handful of augmentations to the copy.

Note that this process in general is not without its problems, as it requires good negative samples. 

## Quick Note on Connection to Generalized Linear Models

Energy-based loss functions connect to **Generalized Linear Models (GLMs)** through the Boltzmann distribution. When the temperature $T=1$ and the energy function is just the dot product, the Boltzmann distribution becomes the **softmax function**
$$P(y|x) = \frac{e^{-E(x,y)}}{\sum_{y'} e^{-E(x,y')}}$$

## Two Examples of Energy Based Loss Functions I Think are Cool

### COSent Loss

###