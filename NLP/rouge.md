ROUGE
===========

ROUGE is an evaluation measurement of summarization methods.
ROUGE basically compares a document outputted my the method and ground truth.


## Variants

### ROUGE-N
The most common measurement.
It is the F1 score over the recall and the precision of bi-gram matching.


### ROUGE-S(U)
ROUGE-S(U) also considers uni-gram matching in addition to bi-gram.


### ROUGE-L, ROUGE-W
They evaluate the length of the longest common sequence over two documents.
