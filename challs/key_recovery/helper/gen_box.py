import random
from tqdm import trange

def df_table(s):
    results = []
    for a in range(256):
        for b in range(256):
            matches = 0
            for x in range(256):
                z = s[x]
                if s[x ^ a] == z ^ b:
                    matches += 1
            results.append((a, b, matches))

    results = sorted(results, key=lambda tup: tup[2], reverse=True)
    results = list(map(lambda t: (t[0], t[1], t[2]/256), results))
    return results

def gen(d):
    s = [i for i in range(256)]
    random.shuffle(s)
    for i in range(256):
        c = random.choice(d)
        s[i^c[0]] = s[i]^c[1]
    return s

def box(d):
    tmp = [gen(d) for _ in range(1000)]
    tmp.sort(key=lambda x: len(set(x)), reverse=True)
    kek = tmp[1]
    for i in range(256):
         if not i in kek:
             for j in range(256):
                 if kek.count(j) > 1:
                     kek[kek.index(j)] = i
    return kek

def get(d):
    B = [box(d) for _ in trange(1000)]
    B.sort(key=lambda x: sum(a[2] for a in df_table(x)[1:2]))
    return B[-1]

d = [(190, 235)]

s = get(d)
print(s)
print(df_table(s)[1:2])
# for a in df_table(s)[1:2]:
#     print(a[2]**4)
# print("-"*20)