# Transaction

## What’s transaction?
Put multiple read/write into a logical unit.
* success … commit
* fail … abort, role back to the status before execution
* in order to achieve transaction, ACID is necessary

## ACID
atomic … transaction is a unit, not devided
* commit or abort
consistency … meet constraints (e.g. no money is lost)
* this is a feature of an application, not of a database
isolation … a transaction will not be affected by another transactio
durability … commit will have been permanentaly
* logging, replication
* no perfect durability exists

Weak isolation level
* single-threaded is considered as the highest level of isolation


## Detail view in atomic and isolatinos
if a database crash while executing a transaction, the transaction will be aborted


## isolation level
* read committed … can read only committed object
    * enabled by locking
    * response time will be huge
    * MVCC

## snapshot isolation
- non repeatable reads don't happen!
