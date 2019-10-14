Transformer
===============

## Encoder-Decoder and Attention
Encoder-Decoder is a fundamental idea on NN architectures that both encoder and decoder have their RNN. Decoding in the architecture sometimes fails because decoder gets compressed information about the input.

One solution for the problem is **attention** mechanism ([#39](https://github.com/tarohi24/literature/issues/39)), where decoder also consider the raw input in addition to the encoded input. Attention usually hands out the raw input in the form of weighted average (weights are parameters trained during the training), but the way to pass the raw input is arbitrary. Another advantage of attention is that the input propagate without decaying, which is a major problem in RNN and CNN. Easy parallelization is an advantage, too.

Attention needs a mechanism to encode sequence ID for each token. **Positional Encoding** is a unique way to embed positional information in tokens.
