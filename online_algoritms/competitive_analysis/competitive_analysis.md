# Online Algorithms 2 Competitive analysis

## key ideas:
-  Robert E Tarjan, Allan Borodin, Daniel Sleator, Ran El-Yaniv
- Better than worst case, not perfect; will expand on this in later documents
- Useful for comparing an online algorithm to the optimal offline algorithm for a problem
- Theres the slight issue that the optimal offline algorithm might not be known. So you can set strong bounds relative to a very weak object.
- key paper this document will be covering:
    - Sleator, D.; Tarjan, R. (1985), "Amortized efficiency of list update and paging rules"

This paper starts with a study of the list update problem which will help us understand the paging problem better. The dictionary problem is as follows: Maintain a set of items under an intermixed sequence of the following three kinds of operations: 
- access(i): Locate item i in the set. 
- insert(i): Insert item i in the set. 
- delete(i): Delete item i from the set.

In discussing the list update problem, we shall use n to denote the maximum number of items ever in the set at one time and m to denote the total number of operations. We shall generally assume that the initial set is empty. We will define the cost of the various operations as follows.

Accessing or deleting the ith item in the list costs i. Inserting a new item costs i + 1, where i is the size of the list before the insertion. Immediately after an ac- cess or insertion of an item i, we allow i to be moved at no cost to any position closer to the front of the list; we call the exchanges used for this purpose free. Any other exchange, called a paid exchange, costs 1. 

**Free vs Paid exchanges**

**So lets get into it. Recall that amortized complexity helps us by**
- telescoping series bounds

Why do we care about this at all? Because, we can estimate the total running time by choosing a potential function and bounding Φ, Φ', and a, for each i. In the list update example, the initial configuration has zero potential since the initial lists are empty, and the final configuration has a *non*-negative potential. Thus the actual cost to the online algorithm of a sequence of operations is bounded by the sum of the operations’ amortized times. 

**The practical motivation for this is that there was historically theoretical support for one algorithm(transpose), while another performed better in practice(move to the front).** This brings us to the main point of this paper and in general this series of notes: We would like to use theory to inform how an algorithm will perform in practice. 


*An online algorithm is c competitive if its cumulative cost on any sequence (plus a constant) is within a factor c to the optimal offline cost. This brings us to Theorem 1:
For any Algorithm A and any sequence of operations s, let CA(s) be the total cost of all the operations, not counting paid exchanges, let $X_A(S)$ be the number of paid exchanges, and let $F_A(s)$ be the number of free exchanges. Note that $X_MF(S) = X_T(S) = X_FC(S) = 0$ and that $F_A(s)$ for any algorithm A is at most $C_A(S) - m$ (After an access or insertion of the ith item there are at most i - 1 free exchanges.) 

Now, for any Algorithm A and any sequence of operations s starting with the empty set,

$$ C_mf(s) \leq 2C_A(s) + X_A(s) - F_A(s) - m$$

Theorem 1 is a very strong result, which implies the average-case optimality result for move-to-front mentioned at the beginning of the section. Theorem 1 states that on any sequence of operations, move-to-front is to within a constant factor as efficient as any algorithm, including algorithms that base their behavior on advance knowledge of the entire sequence of operations. Very powerful stuff that we will come back to later.

We will quick to theorem 3 as it will come back to bite us when paging. 

Let A be an algorithm for a sequence s of insertions and accesses. Then, there is another algorithm for s that is no more expensive than A and does no paid exchanges. (THIS HAS BEEN DISPROVEN)


So lets formalize the paging problem.
Consider a two-level memory divided into pages of fixed uniform size. Let n be the number of pages of fast memory. Each operation is an access that specifies a page of information. If the page is in fast memory, the access costs nothing. If the page is in slow memory, we must swap it for a page in fast memory, at a cost of one page fault. The goal is to minimize the number of page faults for a given sequence of accesses.

Paging Rules

- Least recently used (LRU). When swapping is necessary, replace the page whose most recent access was earliest.
- First-in, first-out (FIFO). Replace the page that has been in fast memory longest. 
- Last-in, first-out (LIFO). Replace the page most recently moved to fast memory. 
- Least frequently used (LFU). Replace the page that has been accessed the least.
- Longest forward distance (MIN). Replace the page whose next access is latest. 

All these rules use demand paging: They never move a page out of fast memory unless room is needed for a newly accessed page. It is "well known" that premature paging cannot reduce the number of page faults (what does this mean? Come back to this after paging with lookahead THIS HAS BEEN DISPROVEN). Theorem 3 can be regarded as a generalization of this observation. Least recently used paging is equivalent to move-to-front: least frequently used paging corresponds to frequency count. 


Theorem 6: For any sequence s,

$$F_{LRU}(s) \le \left(\frac{n_{LRU}}{n_{LRU} - n_{MIN} + 1}\right) F_{MIN}(s) + n_{MIN}$$




