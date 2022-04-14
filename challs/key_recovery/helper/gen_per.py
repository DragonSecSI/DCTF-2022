import random
from tqdm import trange



op = [[0,1],[1,0]]
ab = [0b11101011, 0b10111110]

def o(x):
    return [op[int(b)] for b in f"{x:016b}"]

def m(x):
    return bytes([ab[int(b[0])] for b in x])

def test(p, a):
    out = []
    out.append(m(a))
    for _ in range(4):
        tmp = []
        for i in range(16):
            lp = p[2*i]
            rp = p[2*i+1]
            l = a[lp//2][lp%2]
            r = a[rp//2][rp%2]
            if l == r: return False
            tmp.append([l,r])
        a = tmp
        out.append(m(a))
    return out

def perm(key):
    cnt = 0
    for i in range(2**16):
        arr = o(i)
        if test(key, arr):
            cnt += 1
            # print(m(o(i)))
            print(i)
    return key, cnt

# perm(pbox)
p1 = [i for  i in range(0,32,2)]
random.shuffle(p1)
p2 = [i for  i in range(1,32,2)]
random.shuffle(p2)
p=[p1,p2]
pbox = [p[i%2].pop() for i in range(32)]
pbox = [24, 19, 12, 25, 0, 9, 6, 31, 26, 11, 28, 5, 14, 13, 20, 15, 18, 21, 10, 27, 4, 1, 22, 3, 8, 17, 16, 29, 2, 23, 30, 7]
# perm(pbox)
print(test(pbox, o(65535)))

# options = []

# N = 3

# for _ in trange(100):
#     key = [i for i in range(32)]
#     for i in range(N):
#         x = random.randint(1,14)
#         y = random.randint(x+1,15)
#         key = key[y:] + key[x:y] + key[:x]
#     k,n = perm(key)
#     if n > 0:
#         options.append((k,n))

# print(len(options))
# for a in options:print(a)

