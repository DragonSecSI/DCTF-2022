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

#prev_sigs=['11110011001101000001011010110001', '10001110101010011100111001111000', '11111111100001011111000100000000', '10100100010110000011000101110100', '01010100101111000100100010000000', '11100110011001000011001010010111', '01101011001011000000110011111010', '00001111101011001011111000010111', '00100100111110011001000110101110', '01010010101010110111111010110001', '11011011011110000110001010100010', '11011110011000011011110101111001', '11011111001100011011010100110011', '11010100000010110110000100100000', '00011011101001010001000101000101', '10011011110110001100001111000111', '11010010110010001010010011001010', '10101010111110011100010010001000', '01101110111111011110011110100011', '00001111100110111001101101011110']

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

