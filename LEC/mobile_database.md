Mobile database lecture by Prof. Hara
=====

## How to manage mobile databases?

Due to narrow band width of mobile networking, simple syncing is not effective.
 On the other hand, the strategy that every node has the whole database is also not effective. So there's a trade-off issue.


## Escrow
Escrow is (generally) a third-party organization that mediates a supplier and a consumer. In database are, if a data can be splitted, an escrow allocates each partition of the data to a mobile node. The node can be access the data allocated without permissions (Krishnakumar 97).


## Quoram system

Suppose there're eights nodes in a network, If a node write an update to at least five nodes, a node will read the update if the node read four or mode nodes.
