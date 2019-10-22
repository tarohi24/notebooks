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
