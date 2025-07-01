Ramblings on few shot NER

So to be clear, this paper (Modelling Monotonic and Non-Monotonic Attribute
Dependencies with Embeddings)does not guarantee that the model will be able to represent these dependencies, just that there’s proof that certain pooling operators definitely can’t and certain pooling operators probably can represent these types of dependencies. (the paper specifically uses the phrases, capable and not capable)

I picked the hadamard operator in this situation because my goal is work with the feature vectors as they are coming out of the bert model. The hadamard operator in this context lets (forces) us choose our own vector for class attribute in the dependency relation. My intuition here is that if we can adjust the vector inside the logistic classifier(representing in our case the vector for the class attribute), the token level feature vectors are rich enough that we will be able to capture the correct dependencies without ever needing to change them. This is a weird idea, and this is a very weird (but very cool) paper. I would recommend taking a look at the openreview discussion if you are more curious.

a named entity is a real-world object, such as a person, location, organization, product, etc., that can be denoted with a proper name. here is also a general agreement in the Named Entity Recognition community to consider temporal and numerical expressions as named entities, such as amounts of money and other types of units, which may violate the rigid designator perspective. The classical definition of NER is pretty much as follows: Given a sequence of tokens, NER outputs the boundaries of the named entities along with their associated types, I.e. a tuple of start, stop, and type.

I found a review paper that I skimmed & will read later so these are just my raw thoughts for now:
https://arxiv.org/html/2401.10825v1

There are two types of NER algorithms: rule/regex based and statistically based.

Recall, the sneaky thing is in both BERT and word2vec we use the task of Syntagmatic (using linguistics terms) prediction to create Paradigmatic embeddings by just removing the last layer of the model. Pretty smart.

This means that words that appear in similar contexts have similar word vectors

One of the biggest learning signals I feel like we don’t take advantage of in Bert models is white spaces.

Let’s just say we’re gonna have use sum of the *contextualized* token vectors for a specific NER, so just haamard pooling the subword tokens. Our goal is to make sure this Specific NER falls within the right “paradigm” to steal a term from linguistics.

This is more secure than a pure cos sim version and far more scalable as the Bert model is just trained in the background on more and more data for those that opt in.
Otherwise the linear classifiers can be stored and trained on device and we will never have any idea of what their categories are and what the ners are. But we still have to process the sentences with Bert

The previous Bert based attempts at few shot seem to be knn based which is lame and dumb because it relies on a support set of examples to ya know do the whole knn thing, and also requires task specific supervised training beforehand. What if we could perform Bert based few shot NER in such a way that lets us use one generic backbone Bert model for every customer and then bespoke head models  instead of having to train a full custom encoder model or dare I say decoder model for every customer. Even better would be if that backbone model could be unsupervised.  This brings me back to the Set-Fit article by Hugging Face/UKP Lab. The main idea behind that is to train simple linear classifiers off of a Sentence Bert model because Sentence Bert does a good job clustering similar sentences. This provides a lower cost alternative to doing few shot modeling with a large pre-trained decoder model.

So originally I thought the reason the set-fit paper works is specifically because of how isotropic the sentence embeddings are. Rather, it’s probably that the embeddings are well clustered because they happen to be isotropic. If we have a model that’s well clustered but very anisotropic, can we still do the whole few shot linear classifier thing? I bet we can *as long as everything is well clustered enough*. Ironically, there’s evidence that anisotropy may actually help clustering (linear clustering methods perform better when the Bert embeddings are anisotropic). The point is that Isotropy indicates that the data is linearly separable, but if the space is not Isotropic that doesn’t imply that the data isn’t linearly separable. If we can figure out to deal with NERS that span multiple tokens (which is most of them), we have a simple and powerful few shot NER system.
On that, let’s consider what we would need to capture. We want to find the set of shortest, contiguous, non intersecting sequences in the string that satisfy the linear inequality given by the classifier. The other thing we need to worry abt is ensuring that this system doesn’t truncate the NERs, we want to make sure that the whole span of the NER is captured, and that subsequences of the Named entity don’t also end up in the category of the named entity when they aren’t supposed to. To do this we can turn to my favorite paper as of late! We use the Hadamard product (i.e. the component-wise product of vectors) to capture these non monotonic and monotonic rules between unions of tokens and entity classes.

We have an untokenized sentence with a set of words defining the Named entity, and the class of that named entity. From there we want to get a tokenized sentence with the list of tokens that span the named entity, and again the class of that named entity. So Data format is tokenized sentence, span of NE and NE category. For each NE category, we know we can use other words or sets of words from the rest of the sentences, or even other NERs from different categories. So we take in each sentence in a batch and pull out the ground truth pairs (the full span of the NER ) with the label for the NE category like discussed above. This last layer isn’t a softmax classifier, it’s a set of individual logistic classifiers. Keep in mind though that these are negatives for every other classifier. Then we have the negatives, which have the label number 0. These are the rest of the spans defined by the group of well ordered subsets of the sequence under or equal to a specific cardinality. This will be generated by a function that takes in a tokenized sentence and outputs a list of every totally ordered subset under or equal to a specific cardinality, excluding the subset that contains exactly and only a specific span given to the function. So for example for the input sentence (I, am, walk, ing, my, grey, hound) and the span 5-7, and the cardinality 2, generates the subsets (I), (am), (walk),(ing),(my),(grey),(hound),(I, am),( am, walk),(walk, ing),(my, grey), excluding (grey, hound) and not including subsets longer than 2 like (I, am, walk)

 An important note is the fact that we “pool” vectors is a blessing and a curse. It gives us a bunch of negatives, but we have to search through a bunch of potential answers. Author’s note: the number of possible answers we need to search through is big but not big. Specifically, it’s n+1 choose 2 minus n+1-k choose 2 where k is the max subset size.
Further, to deal with the class imbalance this brings, we will use both focal loss and generate positive samples via dropout masks

We could train the logistic classifiers with focal loss to deal with the class imbalance.

Then at inference time we brute force search through that subset (generated by the same function) until we get a score vector for every one of the subsets. Then we return the ones that have a true with the correct label(s?). Note that this isn’t actually that many if we set a very reasonable limit on the length of the subsets (possible length of the named entity).

So for example for the input sentence (I, am, walk, ing, my, grey, hound) and the span 5-7, and the cardinality 2, generates the subsets (I), (am), (walk),(ing),(my),(grey),(hound),(I, am),( am, walk),(walk, ing),(my, grey), excluding (grey, hound) and not including subsets longer than 2 like (I, am, walk)

The above would look like a triangle with its top cut off so n+1 choose 2 minus n+1-k choose 2 (where k is the max subset size) is the number of possible answers we have to search through each time.

If the algorithm chooses the wrong sub sequences its purely because the vector inside the linear classifier is incorrect and this problem can be fixed just using backpropogation.
