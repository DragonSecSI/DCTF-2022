from sage.all import * 
from random import randint, choice, shuffle
import signal
from constants import subset_sigs

# parameters
hashlen=32
# base field for M-221
A=530438
p=2**511 - 187 
e=EllipticCurve(GF(p), [A,1])
keys=[]

def generate_sig_strings(no_sigs): 
    ''' provde some random challenge strings'''
    sigs=[] 
    with open('challenge_strings') as f: 
        lines=f.readlines()
        for _ in range(no_sigs): 
            sigs.append(random.choice(lines))

def sign(bitstring): 
    '''sign with Naor-Reingold'''
    result=0
    for i in range(hashlen): 
        if bitstring[i] == '1': 
            result += keys[i]
    return str(result.xy()).strip()

def sign_strings(strings): 
    sigs=[]
    for i in range(len(strings)): 
        sigs.append(sign(strings[i]))
    return sigs

def parse_keys(): 
    with open('keyfile') as f: 
        k=f.readlines()
        for key in k: 
            coords=key.split()
            keys.append(e(coords[0], coords[1]))

if __name__=="__main__": 
    #parse keys
    parse_keys()

    # generate that many possible signatures 
    no_sigs=21
    generated=generate_sig_strings(no_sigs)
    shuffle(generated)
    for string in generated: 
        print(string)

    # gen subset + rand strings
    print("sign one of these strings: ")

    # gen subset sigs
    gen_sigs=sign_strings(generated)
   
    try: 
        signal.alarm(19)
        sig=input("Signature: ")
        sig=sig.strip()

        if sig in gen_sigs: 
            print("Lucky")
            with open(flag.txt) as f: 
                print(f.read())
        else: 
            print("Unlucky")

    except: 
        print("too slow")


