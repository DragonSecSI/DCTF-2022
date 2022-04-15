import re
import sys
import string
from sys import stdout
sys.stderr = stdout

from sys import modules
modules.clear()
del modules

trusted_builtins = """
    True False type int print exec
    """.split()

sanitize = re.compile(
    r'(?:globals|__|import|locals|exec|eval|join|format|replace|translate|try|except|with|content|frame|back)'
    ).sub

alphabet = ' \n\r0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ(),.:;<=>[]_{}'

t1 = ''.join(chr(code) for code in range(256))
t2 = []
for i in t1:
    if i in alphabet:
        t2.append(i)
    else:
        t2.append(' ')
trans_table = str.maketrans(t1, ''.join(t2))

DRAGON_IQ = 200
PERCEPTION_CHECK = 0

del alphabet, t1, t2, i, sys, string, re


def clear_builtins():
    orig = __builtins__.__dict__.copy()
    __builtins__.__dict__.clear()
    for i in trusted_builtins:
        __builtins__.__dict__[i] = orig[i]

found_the_lair = "dctf{y0ur_dr4g0n_r4ce_rep"
lured_the_dragon = '_d3cre4s3d_but_Dr4gonSecSI'
stole_the_loot = '_r3p_1ncr34sed}'

def main():
    print("""
  ____     ____   _____   _____   ____     ___    ____    ____  
 |  _ \   / ___| |_   _| |  ___| |___ \   / _ \  |___ \  |___ \ 
 | | | | | |       | |   | |_      __) | | | | |   __) |   __) |
 | |_| | | |___    | |   |  _|    / __/  | |_| |  / __/   / __/ 
 |____/   \____|   |_|   |_|     |_____|  \___/  |_____| |_____|
                                                                
    """)

    print ("Welcome to The Dragon's Lair!\n\n"
           'Can you steal the treasure?\n'
           'Submit your code with Ctrl+D or ///\n')

    stdout.flush()
    
    code = []
    total_chars = 0
    while True:
        try:
            value = input(">>>")
            total_chars += len(value)
            assert total_chars < 1337
            if value == '///':
                break
            code.append(value)
        except EOFError:
            break
    
    code = sanitize("/NO/", '\n'.join(code).translate(trans_table))
    code = code.replace("/NO/closure/NO/", "__closure__")
    code = code.replace("/NO/code/NO/", "__code__")
    code = code.replace("/NO/defaults/NO/", "__defaults__")
    code = code.replace("/NO/doc/NO/", "__doc__")
    clear_builtins()

    def jail():

        def exec_code(inp, ctx):
            exec(inp, ctx)
            print("\nLet's see if you got anyhing...\n"
                  "Your loot from the lair is:"
            )
            try:
                assert FLAG != lured_the_dragon 
                print(FLAG)
            except:
                print('Nothing ¯\_(ツ)_/¯')

        def have_you_found_the_lair():
            global FLAG
            FLAG = found_the_lair

        def is_the_dragon_really_gone():
            global FLAG
            FLAG += lured_the_dragon

        def did_you_remember_to_take_all_the_loot():
            global FLAG
            FLAG += stole_the_loot

        def explore():
            
            a = "Commendable!"
            b = "Smart!"
            c = "Try again!"

            def explore():

                def explore():
                    if 21 < PERCEPTION_CHECK:
                        print(a)
                        have_you_found_the_lair()
                    else:
                        print(c)

                if 22 > DRAGON_IQ:
                    print(b)
                    is_the_dragon_really_gone()
                else:
                    print(c)
                
                return explore

            did_you_remember_to_take_all_the_loot()
            return explore

        exec_code(code, {"explore":explore})

    jail()

if __name__ == "__main__":
    main()