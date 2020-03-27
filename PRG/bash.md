bash
=====

## Load `.bash_profile` when bash launches

You need to specify login mode.

```sh
$ bash -l
```


## GNU parallel

### Quick template
```bash
parallel --halt soon,fail=1 script.rb -i $var -o {#}_{} ::: ${array[@]}
```

### Examples

```bash 
rate=(0.05 0.1 0.25 0.5 0.75 1) 
lang=(en de fr)
run() { 
    export GPUID=
{1} - 1 )) 
    echo $GPUID 
    python laser/train_l2.py “laser/params/lr-
{3}.param” 
}
export -f run 
parallel –halt soon,fail=1 –lb –jobs 16 run {%} {} ::: 
{rate[@]}
```
