import os
import sys

# Find each repo
os.chdir("challs")
dirs = [d for d in os.listdir(".") if os.path.isdir(d)]
for d in dirs:
    files = [f for f in os.listdir(d) if os.path.isfile(os.path.join(d, f))]
    if "challenge.yml" in files:
        print(f"[=] Syncing and installing challenge {d}")
        os.chdir(d)
        os.system(f"ctf challenge sync ./challenge.yml ;ctf challenge install ./challenge.yml ")
        os.chdir('..')
