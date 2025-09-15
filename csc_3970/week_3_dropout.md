# Dropout 

Read the original dropout paper and the variational dropout paper

In the assignment notes, he makes a note about how timing matters. This makes me think of the first s-bert paper and how it kinda sucks but got so hot

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
        - This paper is interesting because 1. It has 1 figure & 1 table (only 1 color 1 table & both are at the end) and 2. from the abstract alone we see that the connection to dropout is very much after the fact. "oh yeah btw this is also like this one type of dropout" (gaussian dropout from Fast dropout training) A quote from the abstract is literally, ". Additionally, we explore a connection with dropout"
        - When doing SGD, it can be hard to minimize in a predictable and useful manner if the variance of the gradient estimate is high.
        - This seems to not be a paper suggesting a better alternative to dropout (although the only figure provides evidence that it works better when used compared to basic dropout), but rather a method for improving the speed of finding the posterior for a set of nn parameters given some data. This is attacking the same issue (regularization and overfitting), but from a very different angle than dropout. A bit clickbait imo. 
    
    - Drop Connect
        - 

        TODO!!! Finish

    Which figure or table is most central to each paper? How can you tell?

        - Dropout:
            - The first figure showing the stable training curve for sure

        - Variational Dropout:
            - The first (and only) table comparing SGD gradient variance comparisons.

    Without focusing on every equation, what general strategy does each paper propose?

        - Dropout: 

        - Variational Dropout: Bayesian methods for inferring  a posterior distribution over neural network weights have a lof of theoretical niceties and reduce over-fitting, but underperform much more simple techniques like basic dropout. They find a method for making this variational inference actually efficient, which happens to be related to a fast approximation of dropout (gaussian dropout from Fast dropout training)

    Did you notice differences in style, clarity, or framing between the original and the follow-on?

        - Variational dropout was much more formal. 

## About the Research Story

    Despite being more polished, why didn’t follow-on methods like Adaptive Dropout displace Dropout?
     - good enough is often the enemy of great.
     - To Dr. Bukowvys point last week, a lot of these models were of the age where you had to do all the legwork yourself, and because of that id imagine more complex dropout methods weren't used as much because it was extra work, especially if they received marginal gains

    What role did simplicity, timing, and memorability play in shaping which paper had the biggest impact?

        - In my experience theoretical niceties matter a lot less than practical performance in real life scenarios 

    Do you think the research community should give more recognition to follow-on work, even if the original dominates? Why or why not?

        - I would like to say yes, but it depends on how much it improves the novel technique; with so much novel and important work coming out rn it can be hard to revisit stuff. especially as we see more and more convoluted techniques being used for marginal performance gains. Even if you try to pick one sub area of one sub area right now, it can still be hard to track everything thats coming out. Particular loss functions or architectural techniques get implemented in libraries iff they provide immediate and clear value. Maybe if at some point in the future ML slows down there will be more time to visit forgotten techniques. 

    What lessons does this story offer about how ideas spread in computer science research?
    - bang for your buck matters.
