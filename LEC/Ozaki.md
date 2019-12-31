Lecture by Dr. Ozaki
=====

## Image search

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
