import base64
import tempfile
import hashlib
import shutil
from time import time
import os
import subprocess

import sys
from string import ascii_lowercase
from math import ceil, floor
from random import choice
from time import strftime, localtime, time

#ERR = sys.stderr            # Destination for error messages
DAYS = 60 * 60 * 24         # Seconds in a day
tries = [0]                 # Count hashes performed for benchmark


def check(stamp, resource=None, bits=None,
                 check_expiration=None, ds_callback=None):
    """Check whether a stamp is valid

    Optionally, the stamp may be checked for a specific resource, and/or
    it may require a minimum bit value, and/or it may be checked for
    expiration, and/or it may be checked for double spending.

    If 'check_expiration' is specified, it should contain the number of
    seconds old a date field may be.  Indicating days might be easier in
    many cases, e.g.

      >>> from hashcash import DAYS
      >>> check(stamp, check_expiration=28*DAYS)

    NOTE: Every valid (version 1) stamp must meet its claimed bit value
    NOTE: Check floor of 4-bit multiples (overly permissive in acceptance)
    """
    if stamp.startswith('0:'):          # Version 0
        try:
            date, res, suffix = stamp[2:].split(':')
        except ValueError:
            #ERR.write("Malformed version 0 hashcash stamp!\n")
            return False
        if resource is not None and resource != res:
            return False
        elif check_expiration is not None:
            good_until = strftime("%y%m%d%H%M%S", localtime(time()-check_expiration))
            if date < good_until:
                return False
        elif callable(ds_callback) and ds_callback(stamp):
            return False
        elif type(bits) is not int:
            return True
        else:
            hex_digits = int(floor(bits/4))
            return hashlib.sha1(stamp.encode("ascii")).hexdigest().startswith('0'*hex_digits)
    elif stamp.startswith('1:'):        # Version 1
        try:
            claim, date, res, ext, rand, counter = stamp[2:].split(':')
        except ValueError:
            print("Malformed version 1 hashcash stamp!\n")
            return False
        if resource is not None and resource != res:
            return False
        elif type(bits) is int and bits > int(claim):
            return False
        elif check_expiration is not None:
            good_until = strftime("%y%m%d%H%M%S", localtime(time()-check_expiration))
            if date < good_until:
                return False
        elif callable(ds_callback) and ds_callback(stamp):
            return False
        else:
            hex_digits = int(floor(int(claim)/4))
            return hashlib.sha1(stamp.encode("ascii")).hexdigest().startswith('0'*hex_digits)
    else:                               # Unknown ver or generalized hashcash
        #ERR.write("Unknown hashcash version: Minimal authentication!\n")
        if type(bits) is not int:
            return True
        elif resource is not None and stamp.find(resource) < 0:
            return False
        else:
            hex_digits = int(floor(bits/4))
            return hashlib.sha1(stamp.encode("ascii")).hexdigest().startswith('0'*hex_digits)

POW_BITS = 30


if __name__ == '__main__':
    
    resource = ''.join(choice(ascii_lowercase) for _ in range(12))
    print("Proof of work:")
    print("hashcash -mb{} -r {}".format(POW_BITS, resource))
    proof = input("stamp: ")

    if not check(proof, resource=resource, bits=POW_BITS):
        print("failed.")
        sys.exit(0)
    


    code = input("Please give me the base64encoded exploit.c: ")


    try:
        decoded = base64.b64decode(code).decode("ascii")
        print("your code was:")
        print(decoded)
    except:
        print("input must be base64 decoding to valid ascii")
        sys.exit(0)

    with tempfile.TemporaryDirectory() as tempdirname:
        shutil.copytree("/serverside", tempdirname, dirs_exist_ok=True)
        os.chdir(tempdirname)
        with open("userspace/tests/exploit.c", "w") as f:
            f.write(decoded)
        print("Building...")
        subprocess.run("./setup_cmake.sh", stdout=subprocess.DEVNULL)
        os.chdir("build")
        try:
            subprocess.run(["qemu-system-x86_64", "-m", "8M", "-nographic", "-monitor", "null", "-serial", "null", "-drive", "file=SWEB.qcow2,index=0,media=disk", "-debugcon", "stdio", "-no-reboot", "-cpu", "qemu64"], timeout=20)
        except subprocess.TimeoutExpired:
            print("Timeout")

        

        



        
