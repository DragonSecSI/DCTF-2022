#!/usr/bin/python3

import subprocess
import sys
import nclib

# Launch the host process
with subprocess.Popen('/host') as host:

    # Receive a program and write it to a file
    with open('attacker', 'w') as attacker:
        attacker.write(sys.stdin.read())

        # Execute the attacker
        attack = subprocess.run(
            ['chmod +x ./attacker; ./attacker']
        )

        print(attack.stdout.decode())