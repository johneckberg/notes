IR is a distinct task from STS. IR focuses on semantic relevancy, or *relevance matching*, while STS focuses on semantic similarity/ *semantic matching.* In general I think it’s important to emphasize the difference between similar tasks in embeddings. Our problem formulation is as follows:  Given two datasets X^ and X\* of x, where X^ is a larger unlabeled set of text data, and X^ is a significantly smaller dataset of pairs of word sequences, where pairs have been collected iff the sequences in the pair are semantically relevant to each other. Our goal is to train a classifier function such that the function maps input patterns into a target space in such a way that the l1 distance in the target space approximates the “semantic” distance with respect to relevancy in the input space. 

I guess the main idea here is that it makes sense to both 1\. Preserve the quality of the original training objective to preserve the quality of the features (which can be done by continued pre-training), and 2\. Treat the downstream tasks as independent from the embedding model and freeze the base model. We hypothesize that the activations of the neurons in the last hidden layer might serve as very strong features for a variety of downstream language tasks, and this is because of the MLM objective. It seems that preserving the MLM task is an important aspect of model performance and that preventing catastrophic forgetting is important to the quality of downstream classification tasks. This seems to contradict some previous research done with CNNs as people have been experimenting with both freezing and full fine tuning (some authors conclude that full fine tuning is better). I need to dig deeper and see if these choices correlate with dataset size.

We can talk alot more here about MLM and PLM and how we go from skipgram to Bert to XLnet to MPnet and friends like RoBERTA but that would be long for my current purposes. I will probably link a collection of papers up here categorized via topic.

- How have we been learning word representations?:  
- What are we actually learning?:  
- Current issues with the BERT and fam embedding space:

**Main points are:**

- Removing the NSP task improves performance:   
  - RoBERTa: A Robustly Optimized BERT Pretraining Approach  
  - MPnet  
- PLM improves performance  
  - MPNET  
  - XLnet  
- Fine Tuning remains the paradigm of choice for transfer learning with Bert models, and with DNNs in general (noted by progressive learning paper)  
  - While fine tuning may allow us to recover expert performance in the target domain, it is a destructive process which discards the previously learned function.  
  - Introduced in G. E. Hinton and R. R. Salakhutdinov. Reducing the dimensionality of data with neural networks.  
- Catastrophic forgetting occurs only in the later layers during fine tuning: [https://www.lsv.uni-saarland.de/wp-content/publications/2020/On\_the\_Stability\_of\_Fine-tuning\_BERT\_preprint.pdf](https://www.lsv.uni-saarland.de/wp-content/publications/2020/On_the_Stability_of_Fine-tuning_BERT_preprint.pdf)  
- A similar issue result presents itself when looking at layers during fine tuning; a paper abt freezing layers for classification and how out of distribution embeddings dont change when fine tuning occurs: [freezing during fine tuning](https://aclanthology.org/2020.blackboxnlp-1.4.pdf)   
  - These problems both source from changing the later layers and are both connected to generalization  
  - We “don't know” why MLM is important for downstream tasks but it seems to be important  
- Note the results from TSDAE about MLM performing good  
  - TSDAE notes that out of distribution performance is bad for a lot of fine tuning methods (This generalization issue could be related to catastrophic forgetting).

This all may be due to the nature of the fine tuning tasks being in opposition to the pre training task. There is much debate about what bert learns, and although we don't know why MLM matters for downstream tasks, I posit that MLM just creates very strong features/ representations and it's in our best interest to keep those intact for downstream tasks. We can do lots of the ad-hoc optimization fixes for these issues as discussed in papers about fine tuning bert, but what about a different solution

- “progressive learning”/freezing as a solution  
- The TSDAE paper also notes that ideally you want a system that can take advantage of both supervised and unsupervised data. Include image with notation

**How to preserve MLM learned representations? We address this issue, and another two on the way (Freezing, Pooling, Objective choice/distance metric)**

- We hope to experiment with treating a bert model as a backbone model like as done with a more classical CNN transfer learning pipeline, and also inspired by the newly introduced progressive learning paradigm: The concept of progressive learning mimics human skill learning, which is adding a new skill on top of previously learned skills as a foundation to learn a new one. E.g, a child learns how to run after learning to crawl and walk and using all the skills obtained in the process.  
- In progressive learning, catastrophic forgetting is prevented by instantiating a new neural network (a column) for each task being solved, while transfer is enabled via lateral connections to features of previously learned columns. The old network(s) stay frozen.  
  -  [https://arxiv.org/pdf/1606.04671.pdf](https://arxiv.org/pdf/1606.04671.pdf) This paper has implications for further steps if this works.  
- This is related to an idea that's been around in CNN’s for a long time: just freeze the pre-trained cnn, train the “head” model  
  - This is noted in [https://www.mdpi.com/2227-7080/11/2/40](https://www.mdpi.com/2227-7080/11/2/40) which points to this: [https://arxiv.org/pdf/1704.06040.pdf](https://arxiv.org/pdf/1704.06040.pdf) study from 2017\. They specifically use the language, “feature extractor” This has shown to be particularly efficient in image based domains.  
  - Learning without forgetting: https://arxiv.org/pdf/1606.09282.pdf  
- We treat the base bert model just as a “feature extractor” The big difference is: we’re treating the mean pooled encoder outputs as the features for the sequence, rather than the token values as is usually done. In this sense, we are treating the task of IR as a multistage process. First, word features must be learned robustly, then, based on these features, we can learn which sequences are semantically relevant to eachother.  
- Add a DNN based EBM and loss from:  
  - [https://cs.nyu.edu/\~sumit/publications/assets/cvpr05.pdf](https://cs.nyu.edu/~sumit/publications/assets/cvpr05.pdf)  
  - The advantage of EBMs over traditional probabilistic models, particularly generative models, is that there is no need for estimating normalized probability distributions over the input space. The absence of normalization saves us from computing partition functions that may be intractable. This is compared to MNR loss, which can be considered the standard loss function for IR and STS tasks. The key difference here is that instead of (poorly) approximating the normalizing component of the loss via in batch negatives, we skip it entirely with a better configured loss function  
  - Quick image regarding gradients of L1, cosine, and euclidean norm here  
  - Potential benefits of this:  
    - Hope to improve out of distribution performance by avoiding catastrophic forgetting of MLM learned features  
    - Potential dimensionality reduction  
    - Ignore the current isotropy issue completely by disregarding the direct distance between embeddings. This is not to say we expect our new embedding output to be isotropic    
- When using RoBERTa/MPnet, the \[CLS\] token still exists without the NSP objective. The idea is that simply having the same token present at the start of all sentences will enable it, through self attention, to learn some representation of the sentence as a whole. The CLS token is then actually tuned for something in the downstream classification task. In general this thought process encourages fine tuning.  
  - https://discuss.huggingface.co/t/on-using-the-final-cls-hidden-state-of-roberta/15024  
  - [https://github.com/huggingface/transformers/blob/f9a2a9e32bf4f6dc128decd0c124fa1f5507532e/src/transformers/modeling\_utils.py\#L1535-L1538](https://github.com/huggingface/transformers/blob/f9a2a9e32bf4f6dc128decd0c124fa1f5507532e/src/transformers/modeling_utils.py#L1535-L1538) for class SequenceSummary(nn.Module): as an alternative  
- Mean pooling is beneficial for cases where query phrase(s) are matched to multiple relevant terms in the context.  
  -  [Bridging the Gap Between Relevance Matching and Semantic Matching for Short Text Similarity Modeling | Facebook AI Research](https://ai.meta.com/research/publications/bridging-the-gap-between-relevance-matching-and-semantic-matching-for-short-text-similarity-modeling/)   
  - Bert with mean pooling seems to do a good job on IR but not really on STS (in TSDAE paper). This is backed up by the proof that models that perform the best on STS tasks on MTEB typically perform worse on IR, and vice versa  
  - It also has the added benefits of not corrupting the MLM objective by not messing with the hidden state representations during training?


  


**Setups:**

- MLM tune bert on all data, mean pool and train just dnn head using CE loss via L1 norm.  
  - Just do mean pool and train just dnn head using CE loss via L1 norm.  
  - MLM tune bert on all data, mean pool and train just dnn head using CE loss via L1 norm, then unfreeze and fine tune for another epoch

