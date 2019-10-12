---
title: "the trouble with distributed system.md"
---

## Problems in distributed system

### Network is not reliable
(delay, lost, etc..). Even Network Time Protocol (NTP) has a problem with syncing. So it's hard to use last-write-wins approach.

### Process pause
This is a problem, too. This may be because of GC, virtual machine pause/restart, I/O or closing laptop.

When thinking about pausing, we have to be aware of the following matters:
- We cannot predict thread pauses.
- Distributed machines: no shared-memory. Therefore we cannot use approaches for one machine.
- Threads can possibly stop for an arbitrary period

### Lease
Due to the unreliability in distributed systems, leasing approach (The keader has the lease) doesn't work if both two clocks are incaccurate.

### Realtime
- Systems in such as an airplane, a rocket or a car need to guarantee a quick response. They are called hard real-time systems.
- Systesm such as a web application (realtime streaming) don't always need realtime response.  If you want the system to support real-time response, all levels of stacks in the system should support it. It will take a huge cost.

### Locking
- e.g. if a process runs GC after getting lock, (and the lock expires without it knowing the fact), conflict will occur.
    - how about sending lock with its ID?
- Most systems are not tolerant with **Byzantine faults** (a node can lie). They usually assume all the nodes are honest.
- hardware-level support is possible but tough
    - not practical


## Approaches

The philosophy is not relying on a single node.

### Predicting disorder of system
Three classes:
* synchronized model … frequently used!
    * suppose upper bound of delay
* partly syncrhronized model
    * some delay can be over the upper bound
* asynchronized model
    * clock should not exist
    * no concept about “timing"

### Node failture
Three classes
* Crash-stop
    * no recovery
* chash-recovery
    * assume that a node has a non-volatime memory and apply it the recovery program
* byzantine
    * a node can lie

### correctness of an algorithm
* need for describing the “"correct” state of the algorithm output
* e.g. fencing tokens
    * uniqueness: not return identity values
    * if a node doesn’t crash, it should return response

