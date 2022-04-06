#!/usr/bin/python3

import os
import subprocess
from nclib import TCPServer

# Create a server listening on port 1337
server = TCPServer(('0.0.0.0', 1337))

# Run the host
with subprocess.Popen('./host') as host:

    # Receive a client connection
    for client in server:
        source_code = ""
        while True:
            code = client.recv(timeout=5).decode()
            if len(code) == 0:
                break
            source_code += code

        # Write the source code to an attacker file
        with open('attacker.c', 'w') as attacker_file:
            attacker_file.write(source_code)

        # Compile the source code in the attacker file
        subprocess.run(
            'gcc -L/ -o attacker attacker.c -lcrypto -lrt -lsodium',
            shell=True
        )

        # Run the source code and return it's output.
        # The maximum running time is 60 seconds.
        try:
            output = subprocess.check_output(
                './attacker',
                timeout=60
            )
            client.send(output)
        except Exception as e:
            client.send(str(e))

        # Delete the attacker files
        os.remove('./attacker.c')
        os.remove('./attacker.o')
        os.remove('./attacker')