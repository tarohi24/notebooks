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

### dvipdfmx:fatal: Cannot proceed without .vf or "physical" font for PDF output...
Fonts are not embedded. When we use Hiragino and certain version of macOS, it occurs.

### LaTeX Error: Cannot determine size of graphic in xxx (no BoundingBox)
Do you set `divpdfmx` in `usepackage{graphicx}`?

### Troubles with minipages

- Not aligned horizontally -> More that two CRs may be inserated.
