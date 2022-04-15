# Phonebook

Solution is in `sol.py`. It is **not reliable** so run it many times (8 should be enough)

## Compile

`gcc phonebook.c -o chall/phonebook.c`

## Flag

`DCTF{C4n_1_g3t_y0ur_numb3r?}`

## Writeup

If we set relation to friends and edit phone number with string of length 8
we can jump back to main

This enables us to edit and print freed chunks (UAF)

You just have to leak libc (unsorted bins) and poison tcache to get shell
