Leader
===========

## Multi leader candidates
In most distribution algorithm, especially in master-worker schema, deciding a leader is required. However, how can we decide leaders without leaders? This chapter introduces ways to tackle such a difficult problem.

### Need for multiple leaders
A single leader is usually not sufficient because of
- low performance if a node and a leader are located far from each other
- low robustness
Thus locating multiple leaders is reasonable.

### Conflicts
Conflicts may happne because fo multi leader (eg: update for same data). To avoid them, there's an approch to force nodes except for a single data center not to accept udpate. This approach is called *half-single-leader*.

## Keywords
- Quoram
