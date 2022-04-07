#!/usr/bin/env python3

num_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

flag = [ord(x) for x in "dctf{Ch0Os3_7h3_r1gh7_m0m3nt_84vnb0}"]
encoded_flag = [0 for i in range(36)]

iv = [0x8b, 0x50, 0x28, 0x62, 0x5c, 0x5e, 0xe9, 0x8e, 0x2f, 0x39, 0x40, 0x14, 0x97, 0x7b, 0xa1, 0xa5, 0x3e, 0x5a, 0xee, 0xad, 0x8d, 0xe5, 0x93, 0x5f, 0x9c, 0xfe, 0x66, 0xf5, 0x9a, 0xa8, 0xf9, 0xfb, 0x36, 0x50, 0x6, 0xd]

print(f"Flag ({len(flag)}): {flag}")
print(f"IV ({len(iv)}): {iv}")
print(f"Encoded flag ({len(encoded_flag)}): {encoded_flag}")
#print(f"flag: {flag}")


def encode_flag():
    print("\nEncoding flag:")
    print(flag)

    num = num_array[5]

    # plus num
    for i in range(len(flag)):
        encoded_flag[i] = flag[i] + num
        encoded_flag[i] = encoded_flag[i] << 0x9
        encoded_flag[i] -= (num << 0x9)
        encoded_flag[i] = encoded_flag[i] ^ iv[i]
    print(encoded_flag)

def decode_flag():
    print("\nDecoding flag:")
    num = num_array[5]
    for i in range(len(flag)):
        flag[i] = encoded_flag[i] ^ iv[i]
        flag[i] += (num << 0x9)
        flag[i] = flag[i] >> 0x9
        flag[i] -= num
    print(flag)

encode_flag()
decode_flag()
