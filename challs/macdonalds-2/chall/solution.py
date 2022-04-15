#!/usr/bin/python3

import socket
import json
from Crypto.Random import get_random_bytes

HOST = "pwn.dragonsec.si"
PORT = 13371

# Open a connection to the challenger
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Get a tag of the all zero 16 byte block, but it can be any plaintext
    message = bytes([0] * 16)
    tag_obj = {
        'action': 'tag',
        'message': message.hex()
    }
    s.sendall(bytes(json.dumps(tag_obj), encoding='utf-8'))
    zero_tag = s.recv(1024)
    zero_tag_json = json.loads(zero_tag.decode())

    # Since IV is part of the plaintext, we can set it to whatever we want. We
    # will use this to generate a new message that will encrypt to the same
    # ciphertext ct that we got in zero_tag_json.
    #
    # We generate some random value to be our new IV. It mustn't be equal to
    # the old iv, but the probability for this is so low, we don't bother
    # checking.
    #
    # We set our new message to be (message XOR IV XOR new_IV) and our new tag
    # is (new_IV, ct). When the challenger verifies this message and tag, it
    # first calculates
    #
    #     (message XOR IV XOR new_IV) XOR new_IV = message XOR IV
    #
    # We see that we encrypt exactly the same value as when we first got a tag
    # of the all zero message, so the ciphertext of this is ct and our new tag
    # is valid.
    iv = bytes().fromhex(zero_tag_json['iv'])
    new_iv = get_random_bytes(16)
    new_message = [0] * 16
    for i in range(16):
        new_message[i] = message[i] ^ iv[i] ^ new_iv[i]

    forgery_obj = {
        'action': 'verify',
        'message': bytes(new_message).hex(),
        'tag': (new_iv.hex(), zero_tag_json['ct'])
    }
    s.sendall(bytes(json.dumps(forgery_obj), encoding='utf-8'))
    flag = s.recv(1024)
    print(f"Received {flag}")
       

