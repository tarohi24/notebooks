Stream Processing
============

## Batch and stream processing
Unlike batch data, stream data has no separation among them. This means there is no end of task.


## Necessary for the medium
Consider the case where data producers pass message (data) to data consumers. Direct passing has some problems (both parts should be always online). Existence of the medium (datastore system) between them is usually helpful.

Such systems are required to notify consumers if an event arrives. However, this kind of functions are not supported by typical databases. So unique tools have been developed.


## Messaging system and database

There are some faults.

If the producer produce data in higher speed than consumer accepts them, the buffer floods. There are two ways to do deal with flooding:
- delete messages
- adjust flow 
(e.g. UNIX pipe, TCP adopts flow adjustment)

If a node clashes, are messages lost? ... Unless it doesn't write data on a disk. Persistence of data on disks and efficiency is a trade-off. If we allow message to lost, (this requirement depends on task), we can efficientky process messages.


The medium between producers and consumers are called **message broker**. The robustness of systems depends on message broker (not producer or consumer).


### Compared to database
Essentially message brokers are similar to databases.
However, the difference is in data persistence. A message broker deletes messages after sending it to the receiver.
Thus working set (queue) is pretty small. Arriving many data lowers the performance.

Another difference is in detecting modification. Message brokers are aware of modification of data, while database is not (because they are based on transactionus).


### The case of multiple consumers
Load balancing matters.  Acknowledgement and redelivery is not guaranteed because  a consumer can crash anytime. If a node doesn't return acc, unless timeout is set, infinity loops occur. To avoid such conflicts, each consumers are isolated from each other.


### Log on disks
A new-arriving consumer canont read the previosu messages, while in database users can. This is because message brokers delete data once a messanger accepts it. Previous message can be stored in log. e.g. Kafka and Twitter's distributed log adopts append-only log.

Append-only logs requires a huge disk. Of course disks don't have infinite storage. So old data should be deteled or moved to another archive storage. However, throughputs of each customers differs. Data deletion may results in losting data that is to slow consumers.

However, it doesn't matter. e.g. 6TB 150MB/s -> 11-hours-long endurance the disk has (actually more times: not all time we need the full throughput).

- however, a message for a slow consumer could be missed
- if a consumer cannot receive a message, other consumers are not violated
- Traditionbal approach, broker deletes messages

--> Thus by setting offset, log-based approach is equivalent to batch processing (we can redo from an arbitrary point).

### Compared to traditional messaging
(traditional) fan-out is not supported (log-based approach forces consumer to read logs independently)
(broker) broker is not necessary to receive all acks, but check offsets in a certain pediod.



## Database and stream

**CDC** change data capture. Usually CDC is async. This means that record database doesn't wait for consumer modification to finish.

### Keepnig system in sync
- Unless the system has a mechanism to detect modifications of the same file in the same time, conclicts happen.
- if we can decide a leader, it's OK.
  - CDC (a leader tells the other followers to modify the data)  can be used if a leader is defined
- log consumer remembers sequence of messages --> can be used!
  - we can implement CDC using log consumer!


### Log compaction
Storage engine detect duplicated record (same keys).
But key exists unless a key is overwritten or deleted. -> so huge!
After key deletion, restorability is lost. however, users are interested in the current state, not logs.


## Event sourcing
- like CDC, event sourcing saves all the modification of the applications.
- Event logs are immutable, append only.:w
- multiple consumers don't read the same pertition
- consumer is responsible for remembering offsets

e.g. if a student remove a class, CDC considers it as a log,  while Event sourcing takes it as an event.



### Commandas and events
- command is just a command
- event is checked (validated) command --> it should be done


### State, Streams Immutability
- if data is immutable, batch processing can start not only from the starting point
- database has a state (conflicting with immutability)

$$
state(now) = \int_0^{now} stream(t) dt
$$

mutable states and immutable logs don't conflict!


### Immutable events
- auditability: easy recovering if a buggy write is done
- logging inner state: if a customer put and delete an item, the log do not desappear.


### Deriving several views from the same event log
- e.g. kafka ... Druid can put data from kafka, and pistachiio can store kafka, ...  -->  it allows various ways of expressions

It's good if we want to add a new feature to an application by generating veiw without log modification.
e.g. schema design is too complex --> separate write design and view desing work! (this ideais called CQRS)


In event sourcing, a write is not always reflected in some logs. This is because states are mutable whereas events are immutable. If we are sure to reflect the latest change, there are two approaches.
1. refresh view and event append in the same time 
  - syncronized way is not good
2. Decide current states are from **event log**. Users are not required to refresh veiw. It is a better idea.


### Limitation of immutability
- is it possible to store all the immutable logs?
- history should be re-written under some laws (in terms of privacy). deleting includes a huge cost.


## Processing streams

Stream processing is executed in the following manner:

1. Make data readable from another data
1. push event
1. generate stream from a stream
  - the main difference is not having the process end (consequenly, infinity)

Stream processing aims mainly to monitoring such as anomaly detection. If so, pattern matching matters.


### Usecase of stream processing

**Complex event processing**
- process multiple events
- mainly for patten detection (need pattern inputted)
- e.g. SQLstream


**Stream Analysis**
- not interested in detecting pattern, but in aggregating data
- e.g. trend detection
- e.g. kafka stream, apache spark streaming


**Search on streams**
- need for searching for streams by complex queries
- queries are saved, documents are tested (reverse to existing IR)


## Reasoging about time
Stream processor is required to manage times because queries usually contain time period.
Local time in the system is not helpful if there's a large delay. e.g. if a stream system reboot, system time means nothing.

### Window processing - types of window
1. tumling window
  - fixed length. one event belongs to one window
1. hopping window
  - fixed length. windows partly overlap.
1. sliding window
  - fixed length. slide window
1. session window
  - not fixed. if no response for a time, window ends.

## Stream joins

### Stream-stream join
e.g. to analyze click through rate for each url, we need to aggregate events with the same session ID
--> Indexing


### stream-table join
e.g. check events against user information
--> coping database in local is good
- stream need to launch in the long term

### table-table join
this can be considered as managemnt for a join materialized view

### Time-dependence of joins
If two events occur in the same time in different streams, how to manage sequence? This problem is called slowly changing dimension. This makes join undicidable --> this leads to not exact restoring.


## Fault tolerance
- batch processing adopts exatyle-once-semantics
- stream doesn't see task done.
  - by dividing and blocking a stream, this can be considered as mini batch problem. (this is the way of Spark Streaming)


## Idempotence
- goal of fault torelance: minimize the effect of tasks that failed.
- idempotence ... can be executed multi times, but no matter how many times it's executed, the final result is identical
