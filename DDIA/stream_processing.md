Stream Processing
============


## Batch and stream processing
Data has no separation among them (or very short unit).

## Terms
- event file is an sequence of record (=event)
- event has usually timestamps
- producer/consumer is those of events

events are aggregated into topics (streams).

producer writes data and consumer pull
the medium is datastore

event-oriented notification to consumer is required
--> however, this kind of functions are not supported by typical databases
--> so unique tools have been developed


## Messaging system
### if producer produce more data than 
- delete messages
- buffering
- flow adjustment 
pipe, UNIX TCP --> flow adjustment

### if a node clashes, are messages lost?
disk write costs
if we allow message lost, (this requirement depends on task), we can efficientky deal with the task.


### re-doing
how about re-doing seen in batch processing


## Direct messaging
(without system)
this needs a mechanism to detect lost packet
both sides need to be online (otherwise messages can be lost)


## message broker
the medium exists
robustness is depending on that of message broker

## Compared to database
Essentially message brokers are similar to database
however, it deletes messages after sending it to the receiver
--> so working set (queue) is pretty small. many data storing lowens the performance.


database supports various ways to search data, while message brokers partially supports

message broker can detect modification of data, while database is not aware of them (because they are based on transactionus)


## Multiple consumers
load balancing matters

### acknowledgement and redelivery
a consumer can crash. if a node doesn't return acc, unless timeout is set, infinity loops occur.

### isolate message of consumers from each other
to avoid conflicts


## Partitioned log
a new consumer canont read previosu messages, while database supports

one approach is append-only log
Kafka nad twitter's distributed log work like this


## Compared to traditional messaging
fan-out is not supported (log-based approach forces consumer to read logs independently)

broker is not required to receive all acks, but check offsets in a certain pediod.

## Log on disks
Append-only logs requires a huge disk
- old segments are pushed to archive disk or deleted

- however, a message for a slow consumer could be missed
- but e,g, 6TB 150MB/s -> 11hours endurance the disk has (actually more times: not all time we need the full throughput)
- if a consumer cannot receive a message, other consumers are not violated
- Traditionbal approach, broker deletes messages

--> Thus by setting offset, log-based approach is equivalent to batch processing (we can redo from an arbitrary point).


## Database and stream
stream processings incorporates idea from database
integration among different database systems may be helped by stream processing
- we need today.

data warehouse is an option. but it requires full-copy

dual write ... if a data is modified, the system notices all the systems

### Keepnig system in sync
- unless the system has a cheanism to detect modifications in the same time, conclicts happen
- if we can decide a leader, it's OK
  - CDC (a leader tells the other followers to modify the data)  can be used if a leader is defined
- log consumer remembers sequence of messages --> can be used!
  - we can implement CDC using log consumer!


### CDC
Note : CDC is async. record database doesn't wait for consumer modification finishing  


### Initial snapshot
a adatabase can be reconstruct using full logs
Alternatively, a snapshot is OK


## Log compaction
storage engine detect duplicated record (same keys).
but key exists unless a key is overwritten or delketed,
- this approach doesn't need to have snapshot because the log reflects the latest version


## Event sourcing
- liek CDC, it saves all modification of applications

event log is immutable, append only, updating is not recommended

e.g. 
if a student remove a class, CDC considers it as a log,  while Event sourcing takes it as an event


User want to know current state (not the log)
--> CDC event, primary key is from the latest event (log compression deletes old event) --> not re-constructive


## Commandas and events
- Events and commands should strictly be distinguished
- command is just a command
- event is checked command

event consumers cannot deny a event
--> so before accepting it, we need to verify it


## QA

- multiple consumers don't read the same pertition
- consumer is responsible for remembering offsets



### State, Streams Immutability
- if data is immutable, batch processing can start not only from the starting point
- database has a state (conflicting with immutability)


$$
state(now) = \int_0^{now} stream(t) dt
$$

mutable states and immutable logs don't conflict!


### Immutable events
- auditability: easy recovering if a buggy write is done
- logging inner state: if a customer put and delete an item, the log is on the log


### Deriving several views from the same event log
- e.g. kafka ... Druid can put data from kafka, and pistachiio can store kafka, ...
  - it allows various ways of expressions

It's good if we want to add a new feature to an application by generating veiw without log modification

- schema design is too complex --> separate write design and view desing work! (this ideais called CQRS)


- in event sourcing, a write is not always reflected in some logs
  - refresh view and event append in the same time
    - not good, not supporting async
  - current state is derived from event log  --> Good
    - user is not required to refresh veiw


### Limitation of immutability
- is it possible to store all the aimmutable logs?
  - it depends on how many updates happen
- history should be re-written under some laws (in terms of privacy)


## Processing streams

1. make data readable from another data
1. push event
1. generate stream from a stream
  - the main difference is not having the process end (consequenly, infinity)


### Use fo stream processing
stream is used for monitoring
- anomaly detection
- e.g. credit card

among them patten macchigs mattered, but now complex event processing is required


### Complex event processing
- process multiple events
- mainly for patten detection (need pattern inputted)
- e.g. SQLstream


### Stream Analysis
- not interested in detecting pattern, but in aggregating data
- e.g. trend detection
- e.g. kafka stream, apache spark streaming


### Search on streams
- need for searching for streams by complex queries
- queries are saved, documents are tested (reverse to existing IR)


## Reasoging about time
- stream processor is required to manage times
  - queries usually contain time period
- local time is not effective if there's a large delay
  - e.g. if a stream system reboot, this can happen

### Knowing whe you're ready
approaches
- late event is abnormal, so abondant it
- correct time of delayed data

### Whose clock are you using?
- mobile can be onffline
  - buffered data is exposed after the device connected next time
  - so less reliability of user-defined time


## Types of window
1. tumling window
  - fixed length. one event belongs to one window
1. hopping window
  - fixed length. windows partly overlap.
1. sliding window
  - fixed length. slide window
1. session window
  - not fixed. if no response for a time, window ends.

## Stream joins
stream-stream, strem-table, table-table

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
If two events occur in the same time in different streams, how to manage sequence?
- this problem is called slowly changing dimension
  - this makes join undicidable


## Fault tolerance
- batch processing adopts exatyle-once-semantics
- stream doesn't see task done.
  - by dividing and blocking a stream, this can be considered as mini batch problem. (this is the way of Spark Streaming)


## Idempotence
- goal of fault torelance: minimize the effect of tasks that failed.
- idempotence ... can be executed multi times, but no matter how many times it's executed, the final result is identical
