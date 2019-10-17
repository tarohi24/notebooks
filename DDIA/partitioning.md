Partitioninig
=========


## What’s partitioning?
- Assigning data into mutiple nodes.


## how to partition data?

### key range
- need sorting 
- skew (non-uniform data distribution)
- clear location
- effective for range query
  - e.g. sensor data have frequent range query
- weak for hot spot (intense access to the certain spot) 

### hash
* uniform data distribution
* not sorted
* no support for range queries

### range + hash
e.g. Cassandra … column family (multiple primary keys) -> include mutiple partitioning

### Using secondary index
- not identify a record, but effective for data modeling
- local index: secondary index is created in each partition
- light write
- costly search
  - necessary to search all of the partitions
- scatter, gather: query spreaded to all

### Term based partitioning
global index: group same index -> next partitioning

### dynamic paritioning
if a partition is over the pre-determined size, it will be divided into two


## Rebalancing
- this is to migrate data into another node to recover from injury
- minimum migration is required
- read/write may happen while migration

### Automatic rebalancing
pros
- convenient
cons
- dead node 
- rebalance
- dead node 
- rebalance

### request routing
Which node should I access to?
**ZooKeeper** : having mapping and notify it to the router
**Gosip protocol** : inform status to each other (IP table)
