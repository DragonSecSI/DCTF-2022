#!/usr/bin/python3

import socket
import json

HOST = "pwn.dragonsec.si"
PORT = 13370

# Read up on CBC-MAC here:
# https://en.wikipedia.org/wiki/CBC-MAC

# Open a connection to the challenger
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Get a tag of the all zero 16 byte block
    tag_obj = {
        'action': 'tag',
        'message': '00000000000000000000000000000000'
    }
    s.sendall(bytes(json.dumps(tag_obj), encoding='utf-8'))
    zero_tag = s.recv(1024)
    # Because we are using CBC-MAC with an all zero IV, the tag we received is
    # actually just the encryption of the all zero block.

    # For the forgery, we send a message with two 16 byte blocks. The first one
    # is again the all zero block, and the second is the tag (encryption) of
    # this block.
    
    # Since the Signatory is using CBC-MAC, it XORes each plaintext block of the
    # message with the previous ciphertext block before encrypting it. When we
    # send it this message, the following happens:
    # 
    #     1. The signatory XORes the first all zero block with the all zero IV
    #        and gets an all zero block.
    #     2. The signatory encrypts this block and gets the first ciphertext
    #        block which is equal to 'zero_tag'.
    #     3. The signatory takes the second block of our message and XORes it
    #        with the previous ciphertext block, but:
    #            zero_tag XOR zero_tag = 0 !!!
    #     4. The signatory encrypts this all zero block and gets zero_tag again,
    #        which it uses as the tag.

    # CBC-MAC is not secure for variable length messages!
    forgery_obj = {
        'action': 'verify',
        'message': '00000000000000000000000000000000' +
            zero_tag.decode(encoding='utf-8'),
        'tag': zero_tag.decode(encoding='utf-8')
    }
    s.sendall(bytes(json.dumps(forgery_obj), encoding='utf-8'))
    flag = s.recv(1024)
    print(f"Received {flag}")
       

