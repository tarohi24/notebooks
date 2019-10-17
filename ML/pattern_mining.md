Pattern mining
=====

## Frequent pattern
A frequent pattern is a frequent subset of a set. The concept of frequent patten is the basic of affinity analysis (=market basket analysis).

### Support
An absolute support is the frequency of a subset in the whole set. A relative support is the probability of the absolute support. Basically a larger support means higher likehihood that it is a frequent pattern. A support tends to increase as the set gets smaller. So normalizations including lift value are usually used.

### Association Rule
Association rule is the degree how much patten A invokes patten B (thus it's expressed like $ A \to B $). The support of the rule is $P(A \cup B)$. The condidence, the indication of how likely to be true the rule is, is $P(B | A)$.


## Apriori Algorithm
Apriori is an efficient algorithm to find associatino rules. Apriori is based on downward closure. Downward closure is a feature of rules that a subsets of a frequent pattern is also a frequent pattern. Apriori cuts the association rule candidates based on the characteristics.


## FPGrowth
Frequent Patten (FP) Growth uses the more compact data structure, called suffix tree, than that of Apriori.
