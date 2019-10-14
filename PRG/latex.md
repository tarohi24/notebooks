LaTeX
=========

## TIPS

### Change prefix of lstlisting
Renew command `\lstlistingname`.

### Refer a footnote in multiple positions
Add this to the preamble
```tex
\makeatletter
\newcommand\footnoteref[1]{\protected@xdef\@thefnmark{\ref{#1}}\@footnotemark}
\makeatother
```

And refer like this:
```tex
\footnote{\label{fn_label1} this is a footnote}
```


## Trouble shooting

### Spacing is ignored in verbatim
`* ` works (in some styles spacing mark appears).

### Minipage doesn't place two itesm horizontally
This may be because more than two CRs are inserted between two items in the source code.
