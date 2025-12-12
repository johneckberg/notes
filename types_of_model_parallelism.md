# training parallelism 

## Data Parallelism

* Replicates the full model on each device and splits the dataset across them. Each device computes gradients on its local batch and then synchronizes parameters with others (e.g., via all-reduce, i.e., model communication). 

## Model Parallelism

* Splitting up the model onto multiple GPUS; Two main types: 

### Tensor Parallelism

* Splits individual layers (e.g., large matrix multiplications) across multiple devices. Instead of a single device performing a full matrix multiplication, each device handles a different chunk of the tensor, and partial results must be gathered to construct the complete output (i.e. activation communication). Taking a general matrix multiplication as an example, let's say we have C = AB. We can split B along the column dimension into [B0 B1 B2 ... Bn] and each device holds a column. We then multiply A with each column in B on each device, we will get [AB0 AB1 AB2 ... ABn]. At this moment, each device still holds partial results, e.g. device rank 0 holds AB0.

### Pipeline Parallelism

* Divides the model layers into distinct segments, each assigned to a different device. During training, microbatches are staged through this pipeline, with each device processing its assigned layers in turn.


I guess now reflecting I realize that I don't know exactly how grad accumulation works. I know it averages the loss over the mini batches but how does that work with backprop & the autograd graph? Is the loss disconnected from the loss until the loss is accumulated then its backproped? No, Linearity of the derivative; The derivative of a sum is the sum of the derivatives. In general, the final mini-batch gradient is the average of the individual gradients of all examples within that mini-batch. In grad accumulation, we add up each gradient after the backward pass, then once we have the whole batch we actually do the weight update. Multiple backward passes, only one weight updates based on the average of the gradients for those backward passes.
Using gradient accumulation loops over your forward and backward pass (the number of steps in the loop being the number of gradient accumulation steps). Instead of taking the sum & dividing by the number of training examples in the minibatch, you take a larger sum that you keep adding to, then divide the number of examples set by the accumulation size/ whole effective batch. The reason this doesn't work for contrastive learning is that, because of the design of the loss function, the gradient for each sample is dependent on each other sample in the batch. There's no way to do a forward and backward pass for each sample independently, both rely on every item in the batch for calculation
Could we train part of a model at a time with grad caching? The link/perspective shift in my mind is by treating each negative sample in grad caching as a neuron in a layer without bias. Could we avoid storing even a full layer at once using this technique?
It aligns well with tensor parallelism because it separates out the calculation of each neuron? Or are they split on different dimensions? Grad caching separates the math out by row, while I think tensor parallelism separates out the math by column? Because then you do an accumulate to do the dot product across all returned rows by just adding the vectors. One dimension value of the input vector times one weight for each neuron, repeated for each neuron (tensor parallel) vs one neuron each with the full weights? Which has less parameters? Depends on which is bigger, the input or output layers, that determines the dimensions of the weight matrix. Would there be any benefits to splitting up the tensor differently? Maybe training LoRa adapters? This is different than gradient checkpointing because thats a just in time sort of thing right? Yes, we don't drop intermediate activations (as we do with grad checkpointing) with grad caching, we separate out the backprop into nice chunks. 
Could we use grad caching to do tensor parallelism for attention with the softmax? Is there ever a time where attention is the memory bottleneck?
https://huggingface.co/blog/huseinzol05/tensor-parallelism Im reading you can split the layer row or column wise