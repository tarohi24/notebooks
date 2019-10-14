OCaml
==========

## Grammer

### No nil
if we write `X = nil`, `nil` is considered as a variable name.


### Recursive Definition
Use `rec`.

```ocaml
let rec has n lst =
  match lst with
  [] -> false 
  | (h::t) -> if n = h then true
              else has n t;;    
val has : 'a -> 'a list -> bool = <fun>
```
