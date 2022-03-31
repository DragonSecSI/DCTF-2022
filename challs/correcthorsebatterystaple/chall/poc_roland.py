#!/usr/bin/env python3
import sys
import string

def decrypt(init_value, encr_values):
    alphabet = string.ascii_lowercase
    res = ""
    current_idx = init_value
    print("start value: ", current_idx)
    for i in range(len(encr_values)):
        current_idx = (current_idx + encr_values[i]) % 26
        res += alphabet[current_idx]
    print(res) 

def main():
    encr_pw = sys.argv[1]
    encr_chars = encr_pw.split(" ")

    encr_bytes = list(map(int, encr_chars))
    print(encr_bytes)

    for i in range(26):
        decrypt(i, encr_bytes)

if __name__ == "__main__":
    main()
