# Online Algorithms 1 Amoritized Analysis

## key ideas:

- Amortized analysis is an upper bound: it's the average performance of each operation in the worst case
- Amortized analysis can be understood to take advantage of the fact that some expensive
operations may “pay” for future operations by somehow limiting the number or cost of
expensive operations that can happen in the near future.
- The key to performing amortized analysis is picking a good “credit” or “potential” function that captures how operations with different actual costs affect a data structure and allows the desired bounds to be shown
- This will lead us into more of Tarjans work on **Competitive Analysis**

Let's first review the three different ways we know of measuring computational complexity, so I can explain why we care about new ones. 
 - Best-case complexity: This is the complexity of solving the problem for the best input of size n. 
 - Average-case complexity: This is the complexity of solving the problem on an average. This complexity is only defined with respect to a probability distribution over the inputs. For instance, if all inputs of the same size are assumed to be equally likely to appear, the average case complexity can be defined with respect to the uniform distribution over all inputs of size n. 
 - Worst-case complexity: This is the complexity of solving the problem for the worst input of size n. 
     
We can think of finding the big oh complexity of an algorithim as the process of finding a cost function for a best case, worst case, or average case input, then finding the limiting behavior of the function as n goes to infinity. So when *isnt* that helpful?

In practice, we are often interested in the total time of a sequence of operations, rather than in the times of the individual operations. A worst-case analysis, in which we sum the worst-case times of the individual operations, may be too pessimistic, because it would ignore correlated effects of the operations on the data structure. On the other hand, an average-case analysis may be inaccurate, since the probabilistic assumptions needed to carry out the analysis may be false. Also, it offers an upperbound on the worst case running time of a sequence of operations, and this bound will always hold. An average case bound, on the other hand, does not preclude the possibility that one will get “unlucky” and encounter an input that requires much more than the expected computation time, even if the assumptions on the distribution of inputs are valid. 

Do to this, we're gonna first think like Yann and do some EBM. Lets define a potential function d that maps any configuration D of the data structure into a real number Φ(D) called the potential of D. We define the *amortized time* of an operation to be t+Φ(D’)-Φ(D), where t is the actual time of the operation and D and D’ are the configurations of the data structure before and after the operation, respectively. With this definition we have the following equality for any sequence of m operations:

$\sum_{i=1}^{m} t_i = \sum_{i=1}^{m} (a_i - Φ_i +Φ_i-1) = Φ_0 - Φ_m + \sum_{i=1}^{m} a_i $

Thats a doozy so lets break it down. $t_i$ and $a_i$ are the actual and amortized times of the ith operation, respectively, $Φ_i$ is the potential after the ith operation, and $Φ_0$ is the potential before the first operation. The total time of the operations equals the sum of their amortized times plus the net decrease in potential from the initial to the final configuration. Note that this is me pulling from a paper (Robert Tarjan: Amortized Computational Complexity), we are free to choose the potential function in any way we wish and of course, the more realistic our potential function is the more useful our analysis is. In most cases of interest, the initial potential is zero and the potential is always nonnegative.

Think of it like this: you're running a business (your data structure), and each operation is a transaction. Instead of looking at the cost of each individual transaction, you want to understand the average cost per transaction over a long period of time. The running times (cost) of successive operations (transactions) can fluctuate considerably, but only in such a way that the average cost of a transaction in a sequence of transactions is still small. To analyze such a situation, we must be able to bound the fluctuations. For each operation, we assign a certain number of credits. This is our "budget" for that operation, our *amortized cost*. The fundamental aim of the banker's method is to show that we can always perform any sequence of operations using the allocated credits; that we've budgeted correctly. 

We start with zero credits saved. When an operation's actual cost is less than its allocated (amortized) cost, the leftover credits are "saved" (deposited). These saved credits can then be used to "pay for" later operations whose actual cost exceeds their allocated cost When an operation is cheap, we save the extra credits for potentially expensive operations in the future. We can also think about it in reverse. If an operation is expensive, we can imagine "borrowing" credits from future, cheaper operations. However, this debt must be paid back eventually by the credits allocated to those future operations.

If we can prove that we never need to borrow credits to complete the sequence of operations, then the **actual time** of any initial part of a sequence of operations is **bounded by the sum of the corresponding amortized times**. If we need to borrow but such borrowing can be paid off by saving enough credits by the end of the sequence, then the **total time** of the operations is **bounded by the sum of all the amortized times**, although in the middle of the sequence we may be running behind. That is, the current elapsed time may exceed the sum of the amortized times by the current amount of net borrowing.

To illustrate this we can use the example from the paper on the manipulation of a stack. We have a sequence of operations composed of two operations: push, which adds a new item to the top of the stack, and pop, which removes and returns the top item on the stack. We wish to analyze the running time of a sequence of operations, each composed of zero or more pops followed by a push. Assume we start with an empty stack and carry out m such operations. A single operation in the sequence can take up to m time units, as happens if each of the first m-1 operations performs no pops and the last operation performs m-1 pops. However, altogether the m operations can perform at most 2m pushes and pops, since there are only m pushes altogether and each pop must correspond to an earlier push.

We can cast our analysis of this stack in the banker’s framework by allocating two credits per operation. During an operation, each pop is paid for by a saved credit, the push is paid for by one of the allocated credits, and the other allocated credit is saved, corresponding to the item stacked by the push. The number of saved
credits equals the number of stacked items, as we can never pop before we push. To fit the stack manipulation example into the physicist’s framework, we define the potential of a stack to be the number of items it contains. Then a stack operation consisting of k pops and one push on a stack initially containing items has an amortized time of $(K+1)+(i-K+1)-i=2$. The initial potential is zero and the potential is always nonnegative, so m operations take at most 2m pushes and pops. A simple worst case analysis would consider m operations with a worst case per operation cost of O(m) to have an upper bound of O(m^2). It should be intuitively obvious that not every single operation can have a cost of m, since previous operations have to push items onto the stack before they can be popped! The amortized per operation cost is 2, so the amortized cost of any sequence of m operations is 2m, which is O(m). 


**ADD arraylist example**


 For any sequence of operations: $O=o_{1},o_{2},\dots ,o_{n}$

The total amortized time: $T_{\mathrm {amortized} }(O)=\sum _{i=1}^{n}T_{\mathrm {amortized} }(o_{i})$

The total actual time: $T_{\mathrm {actual} }(O)=\sum _{i=1}^{n}T_{\mathrm {actual} }(o_{i})$

Then: 

$$ T_{\mathrm {amortized} }(O)=\sum _{i=1}^{n}\left(T_{\mathrm {actual} }(o_{i})+C\cdot (\Phi (S_{i})-\Phi (S_{i-1}))\right)=T_{\mathrm {actual} }(O)+C\cdot (\Phi (S_{n})-\Phi (S_{0})) $$

where the sequence of potential function values forms a telescoping series in which all terms other than the initial and final potential function values cancel in pairs. Rearranging this, we obtain: $ T_{\mathrm {actual} }(O)=T_{\mathrm {amortized} }(O)-C\cdot (\Phi (S_{n})-\Phi (S_{0})). $

Since $\Phi (S_{0})=0 $ and $\Phi (S_{n})\geq 0 $, $ T_{\mathrm {actual} }(O)\leq T_{\mathrm {amortized} }(O) $ so the amortized time can be used to provide an accurate upper bound on the actual time of a sequence of operations, even though the amortized time for an individual operation may vary widely from its actual time.