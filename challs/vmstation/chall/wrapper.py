import base64
import string
import random
import subprocess
import os
import sys
def generate_random_name():
    _len = 50
    return"".join(random.choices(string.ascii_uppercase+string.digits+string.ascii_lowercase,k=_len))

fname = f"/tmp/{generate_random_name()}"
with open(fname,"wb+") as f:
    data = input("Enter b64 encoded bin file: ")
    if len(data) > 1000:
        print("File to big! (max 1000)")
        sys.exit(1)
    f.write(base64.b64decode(data))

fname_enc = f"/tmp/{generate_random_name()}"
print(f"file with your data to encrypt is at {fname_enc}")
with open(fname_enc,"wb+") as f:
    data = input("Enter b64 encoded file to encrypt: ")
    if len(data) > 1000:
        print("File to big! (max 1000)")
        sys.exit(1)
    f.write(base64.b64decode(data))


proc = subprocess.Popen(['./vmstation', fname],shell=False)
proc.communicate()

print(f"deleting: f{fname}")
print(f"deleting: f{fname_enc}")
os.system(f"rm  {fname}")
os.system(f"rm  {fname_enc}")
