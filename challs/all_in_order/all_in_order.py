from random import randint
from secret import flag

p = 16966551860569544237729154265643150311060024379767290139464547310194588106043648199013753498233018130107168404586872929807946275550211247832739070960401619
g = 2

ct = []
# print(flag)
bin_flag = "".join([f"{ord(c):08b}" for c in flag])

# print(bin_flag[:8])

for b in bin_flag:
    x = randint(1, p-1) * 2 + int(b)
    ct.append(pow(g, x, p))

print(f"{p = }")
print(f"{g = }")
print(f"{ct = }")