key={'N': 'a', 'w': 'a', 'm': 'a', 'O': 'a', '0': 'a', 'B': 'b', '@': 'c', 'S': 'c', '[': 'd', 'X': 'd', '-': 'd', 'z': 'e', 'K': 'e', '2': 'e', 'L': 'e', 'U': 'e', '=': 'e', '_': 'e', '6': 'e', 'r': 'f', 'T': 'f', 'R': 'g', '/': 'g', 'y': 'h', 'l': 'h', '5': 'h', 'I': 'h', 'i': 'i', 'd': 'i', '|': 'i', 'G': 'i', 'g': 'i', ',': 'j', ':': 'k', 'D': 'l', 'A': 'l', 'Y': 'l', '\\': 'm', 'b': 'm', '4': 'n', ']': 'n', 'F': 'n', 'j': 'n', 'u': 'o', 'J': 'o', 't': 'o', 'f': 'o', '8': 'o', '$': 'p', '+': 'p', 'M': 'q', 'a': 'r', 'Z': 'r', 'x': 'r', 'v': 'r', '1': 's', '%': 's', '?': 's', '*': 's', "'": 't', '>': 't', 's': 't', '^': 't', 'H': 't', '{': 't', '"': 'u', 'c': 'u', 'Q': 'v', '`': 'w', '3': 'w', 'p': 'x', 'e': 'y', 'o': 'y', '!': 'z', ')': ' ', '7': ' ', 'q': ' ', 'E': ' ', 'h': ' ', ';': ' ', 'P': ' ', 'n': ' ', '}': ' ', 'W': '\n', '(': '.', 'k': ',', '~': '{', '9': '}', '.': '?', '&': '_', 'C': '-', '#': "'"}

# def gen_dec_key(key):
#     dec_key = dict()
#     for k,v in key.items():
#         for i in v:
#             dec_key[i] = k
#     return dec_key

def decrypt(ct, key):
    pt = ""
    for c in ct:
        pt += key[c]
    return pt

# dec_key = gen_dec_key(key)
# print(dec_key)

ct = open("ct.txt").read().strip()

print(decrypt(ct,key))