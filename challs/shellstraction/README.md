# Shellstraction

This is a simple interctive shell written by Red_Epicness and improved and worked upon by AlwaysGuilty. 

There are 2 intended vulnerabilities built in.\
If we take a look in the `touch` command, there is a local variable `signed char offset`. By overflowing it, we can control the `guard` global variable. That allows us to execute code inside `eton` function. ~~This is where a simple double free can be performed.~~ This is where the hell begins.

## Compiling From Source

`gcc -fstack-protector -o chall/app chall/app.c`

## Solution

A not so working solution in [sol.py](sol.py)

Flag: `dctf{D035_4nyb0dy_l1st3n_T0_Ur14h_He4p_1093875hv914387v}`