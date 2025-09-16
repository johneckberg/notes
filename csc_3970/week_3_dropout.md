# Dropout 

Read the original dropout paper and the variational dropout paper


## About Reading the Papers

    From the title, abstract, and figures alone, what can you infer about each paper’s contribution?
    - Dropout:
        - In general, Geoffrey Hinton's life work has been turning neural networks from a nice idea to a practical tool
        - Of course Sutskever's on this paper...
        - some neurons get trained to be highly dependent on eachother for high performance (co-adaption) "in which a feature detector is only helpful in the context of several other specific feature detectors". This paper proposes to break this by simply...dropping out random hidden neurons (individual feature detectors). 
        - This paper really pushes the "we're making neural nets more robust" angle. see that in both figure 2 & 3. But the fact that they throw up fig 1 which doesnt provide a benchmark against a non dropout model suggests that they really wanted to emphasize "look doesnt it suck when your test error starts going up again? Over-fitting? we fixed that." You dont even need to compare to a non dropout nn to one without, you can get the story just by looking at the test curve with respect to epochs. 

    - Variational Dropout
        - Variational bayesian inference is interesting to me because intractable integrals (in general estimating normalizing constants of distributions) is something i find super cool.
            - On that, the goal is this paper from the abstract is to come up with a more stable way to do SGD for the posterior probability, (the distribution of the parameters given the data). Finding the posterior probability is really the classic application of variational bayesian methods. 
            - Bayesian methods for inferring  a posterior distribution over neural network weights have a lof of theoretical niceties and reduce over-fitting, but underperform much more simple techniques like basic dropout. 
        - This paper is interesting because 1. It has 1 figure & 1 table (only 1 color 1 table & both are at the end) and 2. from the abstract alone we see that the connection to dropout is very much after the fact. "oh yeah btw this is also like this one type of dropout" (gaussian dropout from Fast dropout training) A quote from the abstract is literally, ". Additionally, we explore a connection with dropout"
        - When doing SGD, it can be hard to minimize in a predictable and useful manner if the variance of the gradient estimate is high.
        - This seems to not be a paper suggesting a better alternative to dropout (although the only figure provides evidence that it works better when used compared to basic dropout), but rather a method for improving the speed of finding the posterior for a set of nn parameters given some data. This is attacking the same issue (regularization and overfitting), but from a very different angle than dropout. A bit clickbait imo. 
    

    Which figure or table is most central to each paper? How can you tell?

        - Dropout:
            - The first figure showing the stable training curve for sure. You don't need to compare it to another validation curve, you can clearly see that on average, the loss is monotonically decreasing per epoch.

        - Variational Dropout:
            - The first (and only) table comparing SGD gradient variance comparisons. They emphasize the impacts on SGDVB & the posterior first, not the "oh yeah this can also be a dropout technique yeah"

    Without focusing on every equation, what general strategy does each paper propose?

        - Dropout: They randomly "dropout" neurons via a uniform bernoulli distribution over all? neurons

        - Variational Dropout: The strategy in this paper is based on gaussian dropout from Fast dropout training, which states,"we achieve the benefit of dropout training without actually sampling, thereby using all the data efficiently..based on an examination of the implied objective function of dropout training, we show how to do fast dropout training by sampling from or integrating a Gaussian approximation, instead of sampling from a uniform bernoulli. Still a little shaky on this, but the idea is related to the CLT, "dropout indicator variables z1...z5. As z is repeatedly sampled, the resulting inputs to the top unit are close to being normally distributed"

        I give this pretext because the VD finds a method for making variational inference on model parameters actually efficient, which happens to be related to the fast dropout paper, with the authors noting that gaussian dropout from the FD paper is a special case of VD. "We re-interpret dropout with continuous noise as a variational method"

    Did you notice differences in style, clarity, or framing between the original and the follow-on?

        - Variational dropout was much more rigorous and formal which makes sense, this is a bit more of a purer stats paper than the dropout paper. In VD they slam you with the math first, its definitely a paper meant for theorists, less so for applied practitioners. 
        - This paper is not framed as a better type of dropout, its framed as a better way to do a method that tries to solve the same problem that dropout does.

## About the Research Story

    Despite being more polished, why didn’t follow-on methods like Adaptive Dropout displace Dropout?
     - good enough is often the enemy of great.
     - To Dr. Bukowvys point last week, a lot of these models were of the age where you had to do all the legwork yourself, and because of that id imagine more complex dropout methods weren't used as much because it was extra work, especially if they received marginal gains.
     - also this is a paper based on a paper based on dropout, and even fast dropout isn't implemented in pytorch
     [See this pytorch forums post from 21](https://discuss.pytorch.org/t/fast-dropout-training/115320)

    What role did simplicity, timing, and memorability play in shaping which paper had the biggest impact?

        - In my experience theoretical niceties matter a lot less than practical performance in real life scenarios. elegant matters in theory not really in practice. Cool, we figured out a better way to estimate the probability of the model parameters conditioned on the data. Does anyone actually want to do that? A lot of people just want to reduce overfitting and call it a day.
        - I would also include fame as a part of memorability; theres a lot of big names on the dropout paper, and even if some of those names are only big now; at first glance a hinton paper is always going to win over a more less known researcher
        - Simpler ideas are easier to remember. 
        - Makes me think of the first s-bert paper and how it kinda sucks but got so hot

    Do you think the research community should give more recognition to follow-on work, even if the original dominates? Why or why not?

        - I would like to say yes, but it depends on how much it improves the novel technique; with so much novel and important work coming out rn it can be hard to revisit stuff. especially as we see more and more convoluted techniques being used for marginal performance gains. Even if you try to pick one sub area of one sub area right now, it can still be hard to track everything thats coming out. Particular loss functions or architectural techniques get implemented in libraries iff they provide immediate and clear value. Maybe if at some point in the future ML slows down there will be more time to visit forgotten techniques. 

    What lessons does this story offer about how ideas spread in computer science research?
    - Ideas still need to get sold, and bang for your buck matters. 
    - The more technical or arcane a technique is, the more the results of it must speak for themselves. To rephrase that, if your idea doesn't sell itself, you need to sell it yourself. This wasn't true when these papers came out, but a lot of times that means you need to implement your ideas in the form of PRs on big libraries. In the case of VD, theres a million ways to make a model train faster, with a lot of them being more straightforward than VD, and in general, more general methods of speeding up training take precedent?
