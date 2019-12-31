Lecture by Dr. Ozaki
=====

## Traditional Image search

- This task is related to *specific object recognition*, which is a task to identify an "identical objects".
  - e,g, Google image search, face recognition

### What's challenging in object recognition
- Different scale
- Different viewpoints
- Occlusion
  - The phenomenon that a object in front hides another objcet in back.
- Effects of lights
- Time variation


### Traditional approach

Extract local descripters (features) mainly to gain the border between two objects and embed images by them (local ≃ in part).

Such descripters should be invariant by the following effects:

- scale
- rotation
- lights


**invariants to scale** is achieved by laplacian of gaussian. Laplacian operator stresses the border (2nd derivation).  `maximum_filter` in scipy is helpful.  

**Invariants to rotation** is achieved by **SIFT**.

**Invariants to affine transformation** asserts a descripter is consistent no matter what linear transformations (scaling, move, rotation) are conducted. SIFT is not an affine-invatiant descripter. Instead, Root SIFT is an affine-invariant descripter. Root SIFT transforms an vector in a euclidean space so that euclidean distance between the transformed vector would be equivalent to hellinger distance between the original vectors.


### Indexing images

Bag of Visual Words is a popular way to index images. Visual words are features (descripters).


### Product Quantization

Product Quantiaztion is a way to achieve fast approximate search in a distant space.


### Other techniques

For a method to be robust for outlier, RANSAN is a good choice. It estimates values of parameters of a mathematical model with their inliers (degrees of confidence).



## Modern Image Search

Deep learning. CNN is a successful architecture, which succeedes to reduce parameters. CNN obtains kernel functions in LoG automatically by train data. Typicall an image is embedded by NN.


### How to generate embeddings?
**SPoC** uses sum pooling of the last convolution layer as the embedding. This is an approach to extract a *global descripter* from an image.

Another approach, including DELF, is to extract local descripters. DELF uses Attention mechanism. For example, in lanbmark dataset, few attentions focus on the human faces.
