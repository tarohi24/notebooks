Coping with large vocabulary size
=========

## References
- [#35](https://github.com/tarohi24/literature/issues/35) (Hierarchical Softmax)


## About
In NLP, typical generative networks requires output nodes as many as its vocabulary.
When we apply softmax for the output layer, it can be a computational bottleneck (we need to compute all the outputs to normalize them).

The followings are techniques to reduce computation costs:

- Hierarchical softmax
- Noise constructive estimation
- Negative sampling
- Self-normalization


## Hierarchical softmax
This construct output layers hierarchically, assuming the outputs are in a tree from many binary classifiers.


## Self normalization
This is to force outputs so that the sum over them to be 1.
