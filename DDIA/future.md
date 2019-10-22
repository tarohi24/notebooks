The feature of Data Systems
==========

Here authors describe feature directions.
The goal they set is

> to explore how to create applications and systems that are reliable, scalable and maintainable.


## Data Integration
This book introduces sets of approaches for any given problem, all of which have different pros, cons and trade-offs. And the most appropriate choice of software tool depends on the circumstance. Evne so-called "general-purpose" database, is designed forf a particular usage pattern.

Howeever, even if we perfectly understand the mapping between tools and circumstances for their use, there is another challenge: in complex applications, data is often used in several different ways. We inevitably end up having to cobble together several different piece of software in order to provide our application's style.


## Reasoning about dataflow
In data-integration cases, e.g. if two applications write both the search indesx and the database introduces the problem: a conflict. -> Using event log may help because it's deterministic and idemponent.


## Derived data vs distributed transcations
2PC (Two-Phase Commit) assert consistency with distributed transactions. However, derived data systems are often asynchronously -> by default they don't offer time guarantees. Now the best promising approach that author believes is trhe log-based derived data.

(*Derived data* is data that can be computed from other base data. (https://www.dataversity.net/careful-derived-data/))


## The limits of total ordering

- In order to keep consistent ordered log, all events should go throughta single leader. Alternatively we can partition such data. But the order of two different partition is not clear.
- When we adopt microservice, they are deployed independently. -> no defined order, too.A


## Ordering events to capture causality
(causality ... the relationship between cause and effect)
- Assume a SNS service where message-send event and unfriend event are located in different places. If A unfriend B and then A send a message complaininga about B, if ther *dependency* hasn't been captured by the system, the message may also be sent to B. there's not a simple solution for this problem becuase:

- Logical timestamps may not be coodinated.
- if the system can see the casual dependency before being executed, it's OK.


## Batch and Stream Processing
As discussed previously, batch and stream have same principals in common. In fact, Spark performs stream processing on top of a batch processing engine by breaking the stream into (micro) batches. However, it would be poor according to its hopping or sliding window.


## Schema Migrations on Railways

> Reprocessing” the existing tracks in this way, and allowing the old
> and new versions to exist side by side, makes it possible to change the
> gauge gradually over the course of years.

In many cases we don't need to migrate schemas as a sudden switch.


## The lambda architecture
The lambda architecture has gained lots of attention. The idea is that if batch processing is used to reprocess historical data and the stream is used to process recent updates, then how to combine them?

In the architecture batch and steram are running in parallel. The stream processor consumes the events and quickly produces and approximate updat to the view. Batch processor will consumes the *same* set. The underlying idea is that batch processing is less prone to fail.

However, having the same logic both in streaming and batch requires a huge amount of effort. e.g. Summingbird offers an abstraction for them. And now the problem is gradually descreasing because both processors are implemented in the same system.


## Unboundaling databases
At a most abstract level, databases, Hadoop and OSs performs the same function: they store, process and query the data. The main difference is whether it's based on file systems or not. They have different philosopy in terms of data management. The unbounded approach follows the Unix philosophy that small tools do one thing well. The opposite idea is federation.


## Unbundled vs integrated systems
The future of unboundling is different from their current form. Specialized query engines will continue to be important. However, each software has a learinng curve. We may not need to waste our time.

The goal of unbundling is to combine several different databases in order to achieve good performance for much wider range of wrokloads.


## Exactly-once execution of an operation
*exactly-once* semantics is not to allow processing twice. exactly-once means arranging the ocmputaiton such that the final effect is the same as if no faults had occurred. If we make the operation idemopnent, we don't take care of how many times the operation is executed.


## Duplicate suppression
Suppressing duplicate transactinos is needed in certain patterns (especially if the operation is not idemponent).

How to suppress duplicate? One implementation is using unique ID. In the case above, preparing for request ID prevents a request from being executed multiple times.

```SQL

BEGIN TRANSACTION;
INSERT INTO requests
  (request_id, from_account, to_account, amount)
  VALUES('...', 4321, 1234, 11.00)
UPDATE accounts SET balance = balance + 11.00 WHERE account_id = 1234;
UPDATE accounts SET balance = balance - 11.00 WHERE account_id = 4321;
COMMIT;
```


## Enforcing Constraints
We see a uniqueness constraints are guaranteed by introducing `request_id`. How about other constraints?

Other kinds of constraints are very similar: e.g. balance never goes negative, meeting room does not have overlapping bookings. So technique that enforce uniqueness can often be used for these kinds of constrains as well.


## Uniqueness constraints require consensus
If there're selevel concurrent requests with the same value, the system should decide which one is accepted (achieving consensus means to meet this requirement). The most simple case is single-node-single-leader, in which consensus is very easy to be implemented. In mlutiple transactions, uniqueness checking can be scaled out by partitioning (e.g. making same request id be rooted to the same partition). The hard situation is asynchronous multi-master replication.


## Uniqueness in log-based messaging
The log guarantees all consumers to see messages in the same order (see total order broadcast).

A stream processor consumes all the messages in a log partition sequentially on a single thread. Thus if the log is partitioned based on the value that needs to be unique, the processor can deterministically decide which one came first.


## Loosely interpreted constraints
As discusses previously, enforcing a uniqueness constrains requires consensus. An easy and popular implementation is on a single thread. Of course the limitations are unavoidable.

However, another thing to realize is that we actually weaken many uniqueness constrains::

- If two people cuncurrently register the same username, we can send them a message to apologize and ask them to change usernames (*compensating transaction*).
- If a customer order more itesm than we have, let's apologize to customers for delay and offer them a discount. Thus we don't need to require a linearizable constraint on the number of items in stock.
- airline overbooks, hotels overbook rooms, ...
- Withdraw: ask consumers to return money. by limiting the total withdrawals per day, the risk to the bank is bounded.

In many business contexts, it is actually acceptable to temporarily violate constraints. The cost of apology is often low. The key is that these applications do require integrity (such as not losing moeny or reservation) but don't require timeliness.


## Coordination-avoiding data systems

- dataflow systems can maintane integrity guarantees on derived data without atomic commit. linearizability, or synchronous cross-partition coodination.
- Many applications actually allow temporal violation

these observations mean that the dataflow systesm can proviude the data management services without requireing coodination (*coordination avoiding data systems*). They are more scalable (can operate distributed across multiple datacenters in mutli-leader configurations, asynchronoulsy replicating). Although it cannot ensure timeliness or linearizablility, it still guarangtees integrity.


## Trust, but Verify
All of the discussion of correctness we had has been under the assumption that certain things might go wrong but other things won't. This model is called a *system model*. These assumptions are quite reasonable as they are true most of the time. And it would be difficult to worry about such cases. But things happen under certain probabilities. e.g. memory access can fault. So they deserve some attention.


## Maintaining integrity in the face of sortware bugs
- software bugs are always a risk.
- we would not catch them by lower-level network, memory, or filesystem checksums.
- Even widely used database software has bugs.
- If we do careful designing, testing, and reviewing, bugs still exsit.
- consistency in the sense of ACID is based on the idea that the database starts off in a consistent state
- and it transfers from consistent state to another consistent state.
- some noise can be in the transition


## Don't just blindly trust what they promise
- data corruption is inevitable sooner or later in addition to hardware / software bugs
- at least we need ot prepare for finding out if data has been corrupted
- audit works while it's not a financial application.
- mature systems consider the possiblity of unlikely thinkgs going wrong and xmanage that risk
- for example, they consider the risk of data corruption in Amazon S3
- checking when reading is necessary. sooner is better.
- trying to restore data from our backup is also important
  - otherwise we may only find out that our backup is broken when it's too late


## A culture of verification
- **"trust, but verify"** : systems such as S3 or the feature of ACID is less likely to fail, but it can
- don't trust a system blindly
- auditability is necessary


## Designing for auditability
If a transaction matures
