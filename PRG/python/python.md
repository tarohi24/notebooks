Python
=============

## Specifications

### Multiple types of equality
`is` checks if two objects are same, while `==` checks by `eq()` method.

## TIPS

### memo
```python
@lru_cache(maxsize=1000)
def func(arg):
  pass
```

It works when the function has reference transparency.



