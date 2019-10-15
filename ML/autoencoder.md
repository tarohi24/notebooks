Autoencoder
========

Autoencoder is a framework to learn efficient representation of the input data. It can be used for dimensional reduction.

## What is efficient representation?
e.g. A professional chess player can remember a board face in 5 seconds. Note that such a board face is not generated randomly. The player doesn't remember, but grasp the abstract (vague) idea about the board. To say mathematically, they don't grasp `8*8=64` features but realize features in lower dimentions.

### Undercomplete
Undercomplete means a frame (in linear algebra **frame** means an ordered set of bases) which has less functions than the original bases. An autoencoder is usually undercomplete.

Linear undercomplete autoencoder is equivalent to PCA. The objective function of AE is

$$
|| (x_n - x) - W^t ( WX - Wa ) (=W(X-a) ) ||.
$$

This is same as that of PCA.

## Variants

### Stacked Autoencoder

Stacked Autoencoder is an AE which consists of multiple (and usually symmetrical) hidden layers. Note that it is easier to over-fit than normal AE.


### Denoising Autoencoder

Denoising Autoencoder ([#57](https://github.com/tarohi24/literature/issues/57)) is a robsut AE, which accepts the input violated by noises. By trying to recover the actual (non-noised) input, it acquires the mechanism to remove noise from the data.

Noises usually follow normal distribution. Inserting Dropout layers also works.


### Sparse Autoencoder

Making Autoencoder sparse (forcing less nodes to activate). The philosophy behind it that "ff you could speak only a few words per month, you would prorably try to make them worth listening to".


### Variational Autoencoder

Variational Autoencoder ([#58](https://github.com/tarohi24/literature/issues/58)) is a generative Autoencoder which encodes input into the parameters of a distribution instead of an embedding. The coding space is called latent space. Variational Autoencoder is generative becasue we can generate dummy outputs from noises.

### Constructive Autoencoder

Adding loss for derivatives $|| \frac{\partial f}{\partial x} || $ (force AE to train parameters gradually).
