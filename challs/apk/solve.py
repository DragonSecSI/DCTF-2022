import os
import subprocess
import time

FLAG_LEN = 23

pid = subprocess.check_output("adb shell ps -A | grep dctf",shell=True).decode().split(" ")
while "" in pid:
    pid.remove("")
pid = pid[1]

print(pid)

lttrs = list("abcdefghijklmnopqstuvwxyz{}0123456789_-ABCDEFGHIJKLMNOPQRSTUVWXYZ")

flag = [" " for i in range(FLAG_LEN)]

os.system("adb shell input tap 510 310")

for ch in lttrs:
    os.system(f"adb shell input text \"{ch * FLAG_LEN}\" && adb shell input tap 560 900")
    
    time.sleep(0.6)

    #out = subprocess.check_output((f"adb logcat *:E --pid {pid} -s Tag -s END -d -t 30"),shell=True).decode().splitlines()[1:]
    out = subprocess.check_output((f"adb logcat *:E --pid {pid} -s Tag -s END -d -t 50"),shell=True).decode().splitlines()[1:]

    #get last 23 lines 
    out = out[-FLAG_LEN:]
    #print(out)
    print(len(out))
    
   
    os.system("adb shell input tap 510 310")

    res=""

    for i in range(FLAG_LEN):

        res += out[i].split(" ")[-1]
        
        if out[i].split(" ")[-1] == '1':
            flag[i] = ch
    print(res)
    print("{}: {}".format(ch, "".join(flag)))

print("""-------------------------
Flag found:""","".join(flag))