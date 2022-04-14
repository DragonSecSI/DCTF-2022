import random
from secret import text, mapping
from string import printable

alphabet = "abcdefghijklmnopqrstuvwxyz \n.,{}?_-'"

def gen_key(alphabet, mapping):
    pool = list(printable[:-6])
    random.shuffle(pool)
    
    key = dict()

    for c, n in zip(alphabet, mapping):
        tmp = []
        for i in range(n):
            tmp.append(pool.pop())
        key[c] = tmp
    return key


def encrypt(pt, key):
    ct = ""
    for c in pt:
        if c in key:
            ct += random.choice(key[c])
    return ct


key = gen_key(alphabet, mapping)

ct = encrypt(text.lower(), key)
print(ct)
