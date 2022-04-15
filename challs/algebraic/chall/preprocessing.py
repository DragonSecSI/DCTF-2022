from sage.all import * 
from random import randint
from constants import prev_sigs, subset_sigs

# parameters
hashlen=32
# base field for M-221
A=530438
p=2**511 - 187 
e=EllipticCurve(GF(p), [A,1])

curvekeys=[]

# keygen
def keygen(): 
    keys=[]
    for i in range(hashlen): 
        point=e.random_point()
        curvekeys.append(point)
        x,y=point.xy()
        keys.append(str(x) +" " + str(y) + "\n")
    with open("keyfile", "w") as f: 
        f.writelines(keys)

def sign(bitstring): 
    result=0
    for i in range(hashlen): 
        if int(bitstring[i]) == 1: 
            if result == 0: 
                result=curvekeys[i]
            else: 
                result += curvekeys[i]
    return result

if __name__=="__main__": 
    # generate keys
    keygen()

    # sign random strings
    with open("previous_signatures", "w") as f: 
        for i in prev_sigs: 
            sig=sign(i)
            x,y=sig.xy()
            line="input: {input} signature: ({x},{y}) \n".format(input=i,
                    x=str(x), y=str(y))
            f.write(line)    

    with open("subset_signatures", "w") as f: 
        for i in subset_sigs: 
            for i in subset_sigs: 
                sig=sign(i)
                x,y=sig.xy()
                line="input: {input} signature: ({x},{y}) \n".format(input=i,
                        x=str(x), y=str(y))
                f.write(line)    

