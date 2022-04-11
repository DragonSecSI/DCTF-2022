from sage.all import * 
from random import randint
import signal

# parameters
hashlen=32
# base field for M-221
A=530438
p=2**511 - 187 
e=EllipticCurve(GF(p), [A,1])

# for i in range(hashlen): 
#     keys.append(e.random_point())
# print(keys)

prev_sigs=['11110011001101000001011010110001', '10001110101010011100111001111000', '11111111100001011111000100000000', '10100100010110000011000101110100', '01010100101111000100100010000000', '11100110011001000011001010010111', '01101011001011000000110011111010', '00001111101011001011111000010111', '00100100111110011001000110101110', '01010010101010110111111010110001', '11011011011110000110001010100010', '11011110011000011011110101111001', '11011111001100011011010100110011', '11010100000010110110000100100000', '00011011101001010001000101000101', '10011011110110001100001111000111', '11010010110010001010010011001010', '10101010111110011100010010001000', '01101110111111011110011110100011', '00001111100110111001101101011110']

def generate_sig_strings(nr): 
    for i in range(nr-1): 
        s=''
        for i in range(hashlen): 
            s+="randint(0, 1)" 
    return ret

def sign(bitstring): 
    result=0
    for i in range(len(hashlen)): 
        if bitstring[i] == 1: 
            result += keys[i]
    return result

def sign_strings(strings): 
    sigs=[]
    for i in range(len(strings)): 
        sigs+=sign(strings[i])
    return sigs

if __name__=="__main__": 
    # generate that many possible signatures 
    no_sigs=20
    generated=generate_sig_strings(no_sigs)

    # gen subset + rand strings
    print("sign one of these strings")

    # gen subset sigs
    gen_sigs=sign_strings(generated)
    #gen_sigs.append(gen_subset())
    #gen_sigs.shuffle()
   
    # get 5s to sign TODO may be changed
    try: 
        signal.alarm(19)
        sig=input("Signature: ").strip()
    except: 
        print("too slow")
    # defuse alarm
    signal.alarm(0)

    if sig in gen_sigs: 
        with open(flag.txt) as f: 
            print(f.read())
    else: 
        print("Unlucky")


