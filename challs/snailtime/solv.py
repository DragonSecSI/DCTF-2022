from pwn import *
from tqdm import trange
import time

N = 512

#io = process(["python3", "src/snailtime.py"])
io = remote("localhost", 1337)


def interact(op, n):
    io.sendlineafter(b">", op)
    io.sendlineafter(b">", str(n))
    return io.recvline()


n = int(io.recvline().decode().split()[-1])
g = int(io.recvline().decode().split()[-1])
ct = int(io.recvline().decode().split()[-1])

h = pow(ct, 2**N, n)

s = (pow(g, 2**(N//2) - 1, n) * h) % n

T1 = []
T2 = []
T3 = []

def find_num():
    min = 1
    max = N - 1

    while min != max:
        mid = (max+min) // 2
        T1.append(time.time())
        payload = (pow(ct, 2**mid, n) * s) % n
        T2.append(time.time())
        tmp = interact("2", payload).decode().strip()
        T3.append(time.time())
        if not "fat" in tmp:
            max = mid
        else:
            if min == max - 1:
                return max
            min = mid
    return min

for i in trange(10):
    m = N - find_num()
    out = interact("1", m)
    if i < 9: ct = int(io.recvline().decode().split()[-1])

print(out)

H1 = [t2 - t1 for t1,t2 in zip(T1,T2)]
H2 = [t2 - t1 for t1,t2 in zip(T2,T3)]

print(sum(H1)/len(H1))
print(sum(H2)/len(H2))
