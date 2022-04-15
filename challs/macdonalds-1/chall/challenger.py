#!/usr/bin/python3

import socket
import json
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Read the flag from a file
FLAG = ""
with open('flag.txt') as f:
    FLAG = f.readline()[:-1]

class Signatory():

    def __init__(self, conn):
        self.conn = conn
        self.forgeries = 0
        self.tagged = False
        self.key = get_random_bytes(16)
        self.tagged_message = ''

    def handle(self):
        response = 'Empty'
        while True:
            # Receive a message from the client. It is expected to be a string
            # encoded JSON.
            data = self.conn.recv(1024)
            if not data:
                break
            
            try:
                # Parse the message into a JSON object
                req_json = json.loads(data)

                # Perform a task based on the value of the action field
                if req_json['action'] == 'tag':

                    # Tag a message that the user has provided, but only do
                    # this once. Remember what message we tagged to prevent a
                    # trivial forgery.
                    if not self.tagged:
                        self.tagged_message = req_json['message']
                        self.tagged = True
                        response = self.tag(bytes.fromhex(req_json['message']))
                    else:
                        response = 'Already tagged one message for you, pal.'
                
                elif req_json['action'] == 'verify':

                    # Verify a (message, tag) pair from the client. If the
                    # verification is successfull, send the flag.
                    if self.verify(req_json['message'], req_json['tag']):
                        response = FLAG
                    else:
                        response = 'NOT OK'
                else:
                    response = 'Unknown action'
                    break

                self.conn.sendall(bytes(response, encoding='utf-8'))
            except Exception as e:
                response = str(e)
                break

        self.conn.sendall(bytes(response, encoding='utf-8'))

    # Pad a message to a multiple of 16 bytes. We use the non invertible all 0
    # padding scheme.
    def pad(self, message):
        temp = bytearray(message)
        if len(message) % 16:
            num_missing = 16 - (len(message) % 16)
            for _ in range(num_missing):
                temp.append(0)
        return temp

    # Calculate a tag of the message using CBC-MAC with the AES cipher.
    def tag(self, message):
        cipher = AES.new(self.key, AES.MODE_ECB)
        mask = bytes([0] * 16)
        
        message = bytes(self.pad(message))
        block_count = len(message) // 16
        for i in range(block_count):
            input = self.xor(mask, message[i * 16 : (i+1) * 16])
            mask = cipher.encrypt(input)

        return mask.hex()
    
    # Verify a (message, tag) pair by calculating the tag and comparing the
    # values. Only do this if the message is fresh (was not tagged before).
    def verify(self, message, tag):
        if message == self.tagged_message:
            return False
        return self.tag(bytes.fromhex(message)) == tag
    
    # Bytewise XOR of two bytes objects with 16 elements.
    def xor(self, b1, b2):
        result = [0] * 16
        for i in range(len(b1)):
            result[i] = int(b1[i]) ^ int(b2[i])
        return bytes(result)

PORT = 1337
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Start listening for client connections
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('0.0.0.0', PORT))
    sock.listen()

    while True:
        conn, addr = sock.accept()
        with conn:
            srv = Signatory(conn)
            srv.handle()
