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
print(f"created: f{fname}")
with open(fname,"wb+") as f:
	f.write(base64.b64decode(input("Enter b64 encoded bin file: ")))

proc = subprocess.Popen(['./vmstation', fname],shell=False)
proc.communicate()

print(f"deleting: f{fname}")
os.system(f"rm  {fname}")
