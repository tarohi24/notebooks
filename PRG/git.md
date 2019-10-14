Git
============


## diff

### --check
Check whitespaces.


## log
`git log A..B` shows commits that are in branch `B` but not in branch `A`. `..` is called as double dot notation. Triple dot annotation means commits that not neither `A` or `B`.

e.g.
```
$ git log origin/master..HEAD
```

## shortlog
Commit logs for each author.

## apply
Atomically apply a patch. On the other hand, `git patch` applies a patch not atomically.


## cherry-pick
A commit-wise rebase.

## show
e.g.
```
$ git show master@{yesterday}
```
shows the HEAD in yesterday.

## reset
Equivalent to `checkout --soft` and re-`commit`.


## checkout
Move current HEAD. (cf. `reset` moves a commit instead of HEAD).

## `~n`
n-th parents of the commit.
