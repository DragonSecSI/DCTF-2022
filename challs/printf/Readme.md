# String format exploit

You have control over printf's format. Leak flag from stack.

## Source compilation

`gcc -o chall/printf printf.c`

## Solution

Run `python3 sol.py`. If you get flag it works. More detailed description is in
`sol.py`.

## Flag

`dctf{jus7_a_pr1ntf_wo_f0rm4t}`
