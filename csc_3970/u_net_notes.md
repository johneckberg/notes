# U-Net: Convolutional Networks for Biomedical Image Segmentation


Form your opinion on your initial impressions:

- What problem are the authors trying to solve?
  - There's not a lot of data for this specific problem. CNNs are effective, but need lots of data. Not only is lots of data out of reach, "biomedical image processing, the desired output should include localization, i.e., a class label is supposed to be assigned to each pixel."
  - There was previous approach for this, in [Deep Neural Networks Segment Neuronal Membranes in Electron Microscopy Images](https://papers.nips.cc/paper_files/paper/2012/hash/459a4ddcb586f24efd9395aa7662bc7c-Abstract.html). They use the labeled patches, instead of labeled images, to provide more granularity and give each pixel a label. This means that 1. we get some form of localization, and 2., we get more data because theres more labeled data than with just images with a single label. "We modify and extend this architecture such that it works with very few training images and yields more precise segmentations"
    - was this their work?

- they show with the channels the fact that we get a score for each pixel. Again, I wish they had a comparison with the previous architecture. 
- the upsampling operator is still confusing to me im not an image guy.
- recall (for me) that information is not typically shared between channels 
- I've come around on the architecture diagram. Been asking myself, how would I present this differently. I dont think the cart came before the horse; the data augmentation is featured heavily in another figure. The model architecture is novel & the specific novel architecture components are well highlighted because of the u shape. 
- open question for class; can you think of a better way to represent the up-conv? Because the more I think about the u shape

- What approach do they take?
  - The main difference between this and a more traditional CNN is the addition of upsampling. Do they still use pooling operators? Yes, this is what gives it the "U" shape. "The network does not have any fully connected layers"

- Why might this matter?
  - This provides a better, but also easier to train biomed image segmentation model

- Focus especially on the figures. We will go over them in class and take opinions.
  - copy and crop used kinda like residual connections to maintain spatial features that are lost when down sampling
  - the architecture diagram is great. I think visualizing novel architectures is hard and they did a great job
  - Looks like it functions as some form of a feature encoder then feature decoder? "n order to localize, high resolution features from the contracting path are combined with the upsampled output."
  - Didn't see why those chose 32x32 as the smallest conv. I know these things can be slightly arbitrary (we did it bc it worked) but more justification would be nice.
  - They say its fast, but provide a relative measurement not say TeraFlops needed for one forward pass or even the number of parameters 
  - They benchmark on two? benchmarks the EM segmentation challenge, SBI cell tracking challenge.
    - What metrics are we measuring?
      - Warping Error Rand Error Pixel Error for EM segmentation challenge
        - they sort by warping error so I'm assuming this is the most important
      - SBI cell tracking challenge uses intersection over union
  - I'm not that familiar with image segmentation models so I wish this paper did a better job justifying the metrics.
  - Table 1: low warping error but high pixel error?
  - I'm not super familiar with image segmentation models so I don't think I can comment on anything besides how easy they were for someones who's not in the domain to understand. Fig 2 looked nice but didn't help me clarify how the tiling strategy works. 
  

1. Category: What type of paper is this? A measurement paper? An analysis of an existing system? A description of a research prototype?

- A description of a research prototype. "We modify and extend this architecture such that it works with very few training images and yields more precise segmentations"

2. Context: Which other papers is it related to? Which theoretical bases were used to analyze the problem?

- Related to both other deep image processing architectures and .

3. Correctness: Do the assumptions appear to be valid?

- Assumptions:
  - They make assumptions on what sort of data augmentations are valid for the domain
  - "As for our tasks there is very little training data available, we use excessive data augmentation by applying elastic deformations to the available training images. This allows the network to learn invariance to such deformations, without the need to see these transformations in the annotated image corpus. This is particularly important in biomedical segmentation, since deformation used to be the most common variation in tissue and realistic deformations can be simulated efficiently."
- I saw energy function which to me indicates non MLE objective

4. Contributions: What are the paper’s main contributions?

- A novel model architecture that solves a lack of data issue.

5. Clarity: Is the paper well written?

- Seems so. I'm looking at it in retrospect so I'm not sure this is a fair assessment. 
