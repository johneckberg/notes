**Does word order matter?**

Key Points:

- Early research on models like BERT suggested they learn linguistic structures, including phrase-level information and syntax. I think this is dumb and bad.
- Subsequent studies challenged the necessity of word order for model performance, showing that models pre-trained on shuffled text can still achieve high accuracy on many tasks.
- Some researchers argue for a more a nuanced reality: models trained on shuffled text can still implicitly learn or retain some original word order information due to correlations between tokens. 
- All in all, theres strong evidence (imo) to suggest that sequential language models never actually learn semi-arbitrary linguistic structures and instead learn complicated co-occurence statistics. Understanding seems to be anchored in things like "key tokens" which checks out given the learning process. regardless of positional encoding, models have been observed retaining some semblance of word order information due to dependencies between sentence length and unigram probabilities
- This gets at the heart of a larger issue; language models don't learn a casual model of the generating process, just associations.

**Does BERT have any Grasp of Linguistic Structures?**
What does BERT learn about the structure of language?

- Suggests that BERT's internal representations capture information in a compositional manner that echoes classical, tree-like linguistic structures. Experiments demonstrated that BERT's representations capture phrase-level information, particularly in its lower layers. 

**Does Word Order Really Matter? The Case for Distributional Hypothesis**
BERT & Family Eat Word Salad: Experiments with Text Understanding
Masked Language Modeling and the Distributional Hypothesis:Order Word Matters Pre-training for Little

- Showed that MLMs pre-trained on sentences with randomly shuffled word order could still achieve surprisingly high accuracy on many downstream natural language understanding tasks after fine-tuning
- Primary driver of performance seemed to be the learned distributional information. 
- Models trained on sentences with randomly permuted word order perform close to state-of-the-art models that were trained on correctly ordered text, especially if the fine-tuning data itself was also shuffled, suggesting that for many tasks, the necessary word order information (if any) could be picked up during fine-tuning, or that the tasks themselves didn't heavily rely on it.  

**Word Order still sends a signal**
Word Order Does Matter (And Shuffled Language Models Know It)

- Word order does matter because language models trained on shuffled text retain information about the original, naturalistic word order.
    - One key reason for this is a subtlety in how shuffling was often implemented: performing the shuffling before subword segmentation (like BPE tokenization) rather than after. 
    - Shuffling words before breaking them into subword units means that sequences of subwords forming actual words remain contiguous. These intact multi-subword units can provide a consistent signal, allowing models to learn local word order within these smaller windows, especially when combined with positional embeddings.
- Even when text is shuffled after subword segmentation, models can retain some semblance of word order information due to dependencies between sentence length and unigram probabilities (i.e., certain words are more common in shorter or longer sentences, or in specific genres). 


Next: (2021) Do Prompt-Based Models Really Understand the Meaning of their Prompts?