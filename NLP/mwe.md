Multiword Expressions
=====

## References
- [ACL Wiki](https://aclweb.org/aclwiki/Multiword_Expressions)
- [Tokenization - Stanford NLP](https://nlp.stanford.edu/IR-book/html/htmledition/tokenization-1.html)


## About the task

> Multiword expressions (MWEs) are expressions which are made up of at least 2 words and which can be syntactically and/or semantically idiosyncratic in nature.
(ACL Wiki)

Examples:
- San Fransisco (proper names)
- kick the bucket (idioms)
- telephone box (compounded nouns)

In IR context, there's also a simialr problem:

> Conceptually, splitting on white space can also split what should be regarded as a single token
(Stanford NLP)


## Studies

(the following categories are from ACL Wiki)

### Lexical phrases
Methods which have in part syntax or pragmatics. This category is further classified into three classes in terms of types of expressions a method assumes.

- fixed expressions: e.g. while we can say *in short*, we cannot say *in very short*.
- semi-fixed expresssions: while word orders are invariable, minor variances such as determiner selection is possible. e.g. the rule of *kick the backet* also accepts *kicks the bucket*.
- syntactically-flexible expresssions


### Intuitionalized phrases
More compositional than lexical phrases. These methods capture MWEs which are statistically idiosyncratic, but syntactically compositional.
