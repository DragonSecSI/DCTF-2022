# Do you C++ the way?

This is part 2 of the "Do you see the way?" chall from FRICTF. Written by AlwaysGuilty.

It has 2 global vars, one with encoded flag and the other with an IV.\
The program asks for input, which is essentially useless, then decodes the flag
and encodes it back. 

## Source compilation

`gcc -o chall/app chall/app.c -s`

## Solution

Use a debugger, check flag array just after the program decodes the flag.

flag: `dctf{Ch0Os3_7h3_r1gh7_m0m3nt_84vnb0}`