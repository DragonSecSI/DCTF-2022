import re
import string

regex = re.compile("dctf{.*}")

def decipher(file):
    with open(file, "r") as f:
        ciphertext = "".join(f.readlines())

    alphabet = string.ascii_uppercase + string.ascii_lowercase + string.digits
    key = "eompX1GDv0RIy8KYLqSt7FhrZ2B5OzfECkV6QnwdMsj9TPNbAacUig3ulxHW4J"
    rev_mapping = dict(zip(key, alphabet))
    plaintext = "".join([rev_mapping[c] if c in rev_mapping.keys() else c for c in ciphertext])

    flag = regex.findall(plaintext)[0]
    print(flag)

if __name__ == '__main__':
    decipher("chall/ciphertext.txt")
