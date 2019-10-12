Graph Database
==========

Relational Model is good to express many-to-many, while document database isn't.

## Graph Data model

**Various object** can be a node.
(e.g.) a node in Facebook can be a person or a place or an event or ...
--> They are different in attribute types


## Cypher
A property graph model.
Altough relational schema can express data structure,
SQL is not suitable for descriving it (require too long tokens).

features:
- Each node can have an edge.
- We can easily find edges derived from a specific node.

Optimizer decide the most efficient plans.


## RDF
Resource Description Framework (RDF) is an attempt to express metadata of various website.
- model: triple-store model (tuple or xml can express the model)
- SPARQL is a processing language.
  - SPARCL consists of a subject, a predicate and an object.


## datalog
An old language for graph database
not simple declare .. datalog requires rule
