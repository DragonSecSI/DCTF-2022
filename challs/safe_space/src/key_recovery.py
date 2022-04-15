from sys import modules
modules.clear()
del modules

trusted_builtins = "eval input open print".split()
risks = 'print input open eval str getattr hasattr Exception " \' '.split()

FILE = "flag.txt"

def clear_builtins():
    orig = __builtins__.__dict__.copy()
    __builtins__.__dict__.clear()
    for i in trusted_builtins:
        __builtins__.__dict__[i] = orig[i]
    del orig

def main():
    print("Can you find the flag?\n")
    while True:
        try:
            inp = input(">>>")
            t = inp.replace("__builtins__", "")
            if not "_" in t:
                if not ([ele for ele in risks if(ele in inp)]):
                    print(eval(inp, {"__builtins__": {"open":open, "print":print, "list":list, "FILE":FILE}}))
                else:
                    print("Yeah no.")
            else:
                print("Not gonna let you use that.")
        except Exception as e:
            print(e)

main()