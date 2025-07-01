[Bert-flow:](https://arxiv.org/pdf/2011.05864.pdf)

1. Motivation:   
   1. Anisotropicity:  
      1. BERT word embeddings suffer from anisotropy, authors hypothesize that the sentence embeddings from BERT (average of context embeddings from the last layers) may suffer from similar issues.  
   2.  Low-Frequency Words Disperse Sparsely:  
      1. Due to the sparsity, many “holes” could be formed around the low-frequency word embeddings in the embedding space, where the semantic meaning can be poorly defined. Note that BERT sentence embeddings are produced by averaging the context embeddings, which is a convexity preserving operation. However, the holes violate the convexity of the embedding space.   
2. Method:  
   1. Transform embedding space via a [Normalizing flow Model](https://arxiv.org/abs/1908.09257)  
   2. Why is gaussian good?  
      1. First, standard Gaussian (mean of *the distribution is equal to zero and its covariance matrix is equal to the identity matrix*.) satisfies isotropy. The probabilistic density in standard Gaussian distribution does not vary in terms of angle. If the l2 norm of samples from standard Gaussian are normalized to 1, these samples can be regarded as uniformly distributed over a unit sphere. (In high dimensions, Gaussian distributions are practically indistinguishable from uniform distributions on the unit sphere)  
      2. The probabilistic density of Gaussian is well defined over the entire real space. This means there are no “hole” areas, which are poorly defined in terms of probability.  
   3. Trains unsupervised on NLI and also full target database, both denoted in paper. Bert parameters themselves **do not** change, only invertible mapping.  
   4. Also trains “supervised”, where they first fine-tune BERT on the SNLI+MNLI textual entailment classification task in a siamese fashion, then flow is trained unsupervised on either NLI or target database.

[Whitening:](https://arxiv.org/pdf/2103.15316.pdf)

1. Motivation:   
   1. Also anisotropicity  
   2. The authors note that cosine similarity via the dot product is only satisfied when the coordinate basis is the Standard Orthogonal Basis.  
   3. “If a set of vectors satisfies isotropy, we can assume it is derived from the Standard Orthogonal Basis in which it also indicates that we can calculate the cosine similarity via equation 1 (dot product form). Otherwise, if it is anisotropic, we need to transform the original sentence embedding in a way to enforce it being isotropic, and then use equation 1 to calculate the cosine similarity.”  
2. Method:   
   1. Adopts the same supervised/unsupervised training set up from bert-flow; without the unsupervised learning of the flow model obv. The whitening transformation is just performed on each set of sentence vectors.  
   2. Whitening Transformation  
      1. Authors apply a common pre-processing method as a post-processing step to transform the mean value of the sentence vectors to 0 and the covariance matrix to the identity matrix, given a matrix of sentence embeddings where the sentences are the columns. I.E. turn vector distribution into standard Gaussian  
         

[TSDAE:](https://arxiv.org/pdf/2104.06979.pdf)

3. Motivation:   
   1. [Denoising autoencoders](https://aclanthology.org/N16-1162.pdf)  
   2. Domain specific datasets/tasks  
      1. “A crucial shortcoming of previous unsupervised approaches is the evaluation. Often, approaches are mainly evaluated on the Semantic Textual Similarity (STS) task from SemEval (Li et al., 2020; Giorgi et al., 2021; Carlsson et al., 2021; Gao et al., 2021). As we argue in Section 4, we perceive this as an insufficient evaluation. The STS datasets do not include sentences with domain specific knowledge…Further, STS datasets have an artificial score distribution, and the performance on STS datasets does not correlate with downstream task performances (Reimers et al., 2016).”  
4. Method:  
   1. Sequential denoising autoencoder with transformers  
      1. Authors train sentence embeddings by adding a certain type of noise (e.g. deleting or swapping words) to input sentences, encoding the damaged sentences into fixed-sized vectors and then reconstructing the vectors into the original input.

      ![][image1]

      2. Connection with [Bert and family eat word salad](https://arxiv.org/pdf/2101.03453.pdf) & noise?  
         1. In Bert and Family eat word salad authors show that Bert models struggle even with the form of language by demonstrating that they force meaning onto token sequences devoid of any.  
   2. Cross Attention modification:  
      1.  Decoder decodes only from a fixed-size sentence representation produced by the encoder. It does not have access to all contextualized word embeddings from the encoder. This modification introduces a bottleneck, that should force the encoder to produce a meaningful sentence representation  
   3. Benchmarks in three ways  
      1. Completely Unsupervised:  
         1. Authors assume  they just have unlabeled sentences from the target task and tune our approaches based on these sentences.  
      2. Domain adaptation:  
         1. Authors assume they have unlabeled sentences from the target task and labeled sentences from NLI & STSb. Authors test 2 set ups:  
            1. Training on NLI+STS data, then unsupervised training to the target domain  
            2. Unsupervised training on the target domain, then supervised training on NLI \+ STS  
      3. Pre-training:  
         1. Authors assume they have a larger collection of unlabeled sentences from the target task and a smaller set of labeled sentences from the target task.

      

Simcse:

1. Motivation: CT  
2. Method:  
   1. samples different dropout masks for the same sentence to generate a embedding-level positive pair and uses in-batch negatives.This learning objective is equivalent to feeding each batch of sentences to the shared encoder twice and applying the MNRL-loss

