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
        self.tagged_messages = []
        self.iv = get_random_bytes(16)

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
                        if len(req_json['message']) <= 32:
                            self.tagged_messages.append(req_json['message'])
                            self.tagged = True
                            response_json = self.tag(bytes.fromhex(req_json['message']), self.iv)
                            # Add the IV to prevent a trivial attack.
                            self.tagged_messages.append(response_json['iv'])
                            response = json.dumps(response_json)
                        else:
                            response = 'Your message is more than one block long.'
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
    def tag(self, message, iv):
        cipher = AES.new(self.key, AES.MODE_ECB)
        message = bytes(self.pad(message))
        input = self.xor(iv, message)
        ciphertext = cipher.encrypt(input)

        return {'iv': iv.hex(), 'ct': ciphertext.hex()}
    
    # Verify a (message, tag) pair by calculating the tag and comparing the
    # values. Only do this if the message is fresh (was not tagged before).
    def verify(self, message, tag):
        if message in self.tagged_messages:
            return False
        generated_tag = self.tag(bytes.fromhex(message), bytes.fromhex(tag[0]))
        return tag[0] == generated_tag['iv'] and tag[1] == generated_tag['ct']
    
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
