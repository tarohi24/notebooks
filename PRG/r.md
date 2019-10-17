R TIPS
================

## Functions

### mod
To separate values with the modulo of their keys, `split(vec, 1:4)`.

### find indices
`which(vec == x)` returns a list of indices in `vec` which value is equal to `x`.

### apply

**sapply**
```R
> c = sapply(vec, function(x) {return (x %/% 5)})
> c
  [1]  0  0  0  0  1  1  1  1  1  2  2  2  2  2  3  3  3  3  3  4  4  4  4  4  5
 [26]  5  5  5  5  6  6  6  6  6  7  7  7  7  7  8  8  8  8  8  9  9  9  9  9 10
 [51] 10 10 10 10 11 11 11 11 11 12 12 12 12 12 13 13 13 13 13 14 14 14 14 14 15
 [76] 15 15 15 15 16 16 16 16 16 17 17 17 17 17 18 18 18 18 18 19 19 19 19 19 20
```

## Data structures

### matrix <-> dgTMatrix (sparse matrix)
```R
> sparse_mat <- as(data, "dgTMatrix”)
```


## Trouble shooting

### Cannot find ... when using parallel
This is because the master couldn't pass the arguments to the workers.
