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


### asyncio
A basic code will be like this. Note that just calling `main()` does *not* iinvoke the method to run.

```python
>>> import asyncio

>>> async def main():
...     print('hello')
...     await asyncio.sleep(1)
...     print('world')

>>> asyncio.run(main())
hello
world
```

The best description is on https://realpython.com/async-io-python/. The following is my code:

```python
>>> import asyncio
>>> async def count():
...     print('one')
...     await asyncio.sleep(1)
...     print('two')
...
>>> async def main():
...     await asyncio.gather(count(), count(), count())
...
>>> asyncio.run(main())
one
one
one
two
two
two
```
