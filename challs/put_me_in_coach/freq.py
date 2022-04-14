from string import printable

f = open("ct.txt").readline()

alphabet = printable[:-6]

d = {c:0 for c in alphabet}

for c in f:
    if c in alphabet:
        d[c] += 1

a = sum(d.values())

# print({k:100*v/a for k,v in d.items()})

for k,v in d.items():
    if v > 0:
        print(f"{k}: {100*v/a}")


# key = dict()

# for k,v in zip( "^!J;>o&b}ysPUcxv8z:t?pf%0Q+guHNEe4", 
#                 "dctf{}\n._        o?ananrdistatiere"):
#     key[k] = v

# out=""

# for c in f:
#     if c in key:
#         out += key[c]
#     else:
#         # out += c
#         out += "_"

# print(out)

# je solvable na roke, not doing it again tho