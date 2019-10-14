GloVe
======

GloVe ([#37](https://github.com/tarohi24/literature/issues/37)) is a word embedding technique which incooporates features from word2vec ([#36](https://github.com/tarohi24/literature/issues/36)) and SVD.
Word2vec takes only context words in the windows. On the other hand, a co-occurence matrix considers all the co-occurence between words, although its dimension is same as its vocabulary size (too large to handle!). GloVe mixes those two methods, achieving low-dimension expresssion generated from a co-occurence matrix.

## Objective function
The objective function of GloVe is as the following:

$$
{J(\theta) = \frac{1}{2}\sum^{W}_{i,j=1}f(P_{ij})(u^{T}_{i}v_j - \log{P_{ij}})^2 }
$$

Where $P$ is the co-occurence matrix and f is a weighting function (this is an arbitrary function).
