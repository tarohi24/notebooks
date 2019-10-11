## About

Authors categorized systems in the following manner.

- **Online system**, which is sensitive to response time and errors outputted.
- **Batch processing system**, which requires high throughput
- **Stream processing** (described in later parts)

This chapter is mainly for discussion of batch processing.

It starts by describing trade-off between chain of UNIX commands and custom programming languages.
If data is too large to be on memory, UNIX commands works well.
Algorithms such as sorting are better in custom languages.

A common way of communication between processes is stdin and stdout.
They are easy to debug, but cannot connect to the network.
MapReduce, which is a main technique in this chapter, solves this problem.


## MapReduce
MapReduce offers connections to other hosts, which stdio doesn't offer.
MapReduce consists of mapper (generate keys) and reducer (aggregate keys).

### Join of MapReduce
Where to aggregate keys? Beforehand (map-side joins)? In advance (reduce-side joins)?

- map-side joins … join in mapper
    * :good: good response time
    * :bad: constraints of input
- reduce-side joins … join in reducer
    * :good: no constraints in input
    * :bad: response time

(e.g.) Assume we have the user histories and analyze tendency of users' behaviors in each page.
—> Where join takes place?


### Output of batch workflows

Outputs are done not only for reporting but also telling information to another task.
(e.g.) Machine learning application —> output format is something insertable to the database

Output unit matters. Where huge data flows, including web application, 1 output / query is not efficient.
Instead, having a database in batch job is recommended.
Constructing index is almost equivalent to mapper process, so there's few overhead.

 
### Beyond MapReduce Models

MapReduce is a simple model.
Simple menas it is whitebox, and we cannot say simple is easy.
—> leads to more high level models such as pig, hive, cascading. crunch
They are more easy to use, less robust than MapReduce.

Hadoop: mapreduce + distributed file system
difficulty: Diversity of strage

- Data outputted by MapReduce is just byte sequences
  - can be saved as an arbitrary model


### Dataflow engine
Jobs are independent of each other.
Communication between jobs are done by passing Intermediate file is called Intermediate State.
SO it should wait for previous job.
(c.f. Pipe in UNIX can start job in parallel)

**dataflow engines** consider the whole workflow as a job (not divide).
- No need to have operator, just need to mapper/reducer
    * sorting is not always necesssary
- Data dependency is obvious
    * easy optimization
    * not have Inner state as 
- cons: not having intermediate state leads to the less robustness


### Fault tolerance
* Operator in workflow should start at first when fails
* Operator should be deterministic
    * e.g. cannot use random value


## Graph and Iterative Processing
Many graph algorithm process an edge exatyle one time
MapReduce is not suitable for such algorithms (`while` loop).

Pregel processing model
* apply a function which accepts an edge and send a message to other edges
* at every time an iteration stops, record the output in device
    * falut tolerant
* Graph node allocation is responsible for the algorithm
    * Ideally minimal network communication
* Network delay is a big matter

