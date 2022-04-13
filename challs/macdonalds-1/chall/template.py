#!/usr/bin/python3

import socket
import json

HOST = "pwn.dragonsec.si"
PORT = 13370

# Open a connection to the challenger
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Send a message to the challenger and get the tag
    tag_obj = {
        'action': 'tag',
        'message': bytes('Hello World', encoding='utf-8').hex()
    }
    s.sendall(bytes(json.dumps(tag_obj), encoding='utf-8'))
    tag = s.recv(1024)
    print(tag)
