# issue

So, I've been taking a look again at the implementations and the source paper. I believe I've figured out what the issue is and would like to get everyone's take on it.

## The CoSENT loss function from the original blog

$$\mathcal{L}_{\cos} =  \log \left( 1 + \sum_{\text{sim(i,j)} > \text{sim(k,l)}} e^{\lambda(\cos(u_k, u_l) - \cos(u_i, u_j))} \right)$$

$$\mathcal{L}_{\cos} =  \log(1 + \sum _{\text{sim(i,j)} > \text{sim(k,l)}} e^{i-j})$$

## The CoSENT loss function from the AnglE paper (pre-print only)

$$\mathcal{L}_{cos} = \log \left[ 1 + \sum_{s(X_i, X_j) > s(X_m, X_n)} e^{\frac{\cos(X_m, X_n) - \cos(X_i, X_j)}{\tau}} \right]$$

## The AnglE loss function from the AnglE paper (pre-print & ACL)

$$\mathcal{L}_{angle} = \log \left[ 1 + \sum_{s(X_i, X_j) > s(X_m, X_n)} e^{\frac{\Delta\theta_{ij} - \Delta\theta_{mn}}{r}} \right]$$

Notice that from CoSENT loss to AnglE loss, the order of $s(m,n) - s(i,j)$ is changed to $s(i,j) - s(m,n)$. However, the actual code does not reflect this change.

## The Sentence Transformers [CoSENT loss](https://github.com/UKPLab/sentence-transformers/blob/master/sentence_transformers/losses/CoSENTLoss.py#L86) implementation

 ```
scores = scores[:, None] - scores[None, :]
```

## The Sean Lee [cosine_loss](https://github.com/SeanLee97/AnglE/blob/main/angle_emb/angle.py#L90) (CoSENT loss) Implementation

 ```
y_pred = y_pred[:, None] - y_pred[None, :]
```

## The Sean Lee [AnglE loss](https://github.com/SeanLee97/AnglE/blob/main/angle_emb/angle.py#L114) Implementation

 ```
y_pred = y_pred[:, None] - y_pred[None, :]
```

For a list of ground truth scores for a set of sentence pairs $$ {[i,j], [m,n],…} $$

This line of code performs subtraction element-wise between two broadcasted $(N, N)$ tensors. This leaves us with an $N\times N$ tensor where the $([m,n], [i,j])-th$ element will be $s(m,n) - s(i,j)$, **not**  $s(i,j) - s(m,n)$.

In the previous issue discussing this, I simply assumed that I had made a mistake, so I changed the documentation to reflect the screenshot of the paper included in the issue. This was a mistake on my part. Instead, it appears that there is a slight difference between the equation given in the AnglE paper and the code in the corresponding AnglE repository. I think it would make sense to make note of this error in the documentation.

The angle distance as described in the paper is not inversely proportional to cosine similarity. It is designed to provide a better learning signal than normal cosine similarity, as there is very small gradient when cosine similarity is close to the top or the bottom of the waveform. 
