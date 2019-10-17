Neuralnet for IR
=========


## Document Autoencoder ([#50](https://github.com/tarohi24/literature/issues/50))
- Unsupervised
- Loss function only leads to compress dimension --> not so effective in IR


## Siamese network ([#27](https://github.com/tarohi24/literature/issues/27))
- a popular metric learning framework
- by using RankLoss, NN can learn IR tasks.
- this can be used if a document is expressed as an embedding, which in most case doesn't work


## Next query prediction
- If a NN is trained to output suffix of prefix given by the user, the network can do completion.


## Lexical and semantic matching ([#69](https://github.com/tarohi24/literature/issues/69))
- NN is not robust for lees frequent words
- If such a word emerges in the document, we want to weight perfect matching result instead of semantic matching.
- this method combines two complementary methods


## Duet Architecture ([#70](https://github.com/tarohi24/literature/issues/70))
- outputs linear average between outputs of lexical matching model and semantic matching model
- they propose more complecated model including URL matching, texts of pages the page links to, header tag contents, etc..
- web documents are more than just body text
