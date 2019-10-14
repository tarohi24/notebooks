Write Skew and Phantoms
=========

Dirty writes and lost updates -> need to be prevented in order to avoid data corruption.
But there are not the only cases where two writes conflict.
This section is to show the remaining potential of conflicts.

## Dirty write
One client overwrites data that another client has written, but not yet committed. Almost all transactions' implementations prevent from dirty writes.


## lost update
Two clients concurrently perform a read-modify-write cycle. One overwrites the other’s write without incorporating its changes, so data is lost. Some implementations of snapshot isolation prevent this anomaly automatically, while others require a manual lock (SELECT FOR UPDATE).


## write skew
Is neither a dirty write nor a lost update (because they update two different objects)
You can think of write skew as a generalization of lost update, and the special case where different objects update the  same object, then lost update


### How to prevent from write skew?
Most database doesn't have built-in support for constraints which is related to multiple objects (unless you don't use Serializable isolation)
When Snapshot isolation, the best choice would be lock (SQL are here)

```SQL
BEGIN TRANSACTION;
SELECT * FROM doctors
WHERE on_call = true
AND shift_id = 1234 FOR UPDATE;

UPDATE doctors
SET on_call = false
WHERE name = 'Alice'
AND shift_id = 1234;

COMMIT;
```

How about allowing only one commit per time ?
-> modern system such as airline reservation doesn't allow
Stored procedure

