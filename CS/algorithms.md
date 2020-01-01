Algorithms
=====

## Compute greatest common division using Euclidean algorithm

```python
def gcd(x,y):
     while y:
          x,y = y, x % y
     return x
```
