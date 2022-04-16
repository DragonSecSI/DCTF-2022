import os
import random
import shutil

rand_hash = random.getrandbits(128)
dirname = str(rand_hash)
path = os.path.join("tmp/", dirname)

os.mkdir(path)
os.chdir(path)
#os.system("stdbuf -i0 -o0 -e0 ../../app")
os.system("../../app")

shutil.rmtree(os.getcwd())
