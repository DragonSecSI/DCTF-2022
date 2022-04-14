f = open("box.txt").readlines()

arr = []

for i in range(0,len(f),4):
    arr.append((f[i], float(f[i+1]), float(f[i+2])))

arr.sort(key=lambda x: x[1]*x[2])

for a in arr[-10:]:
    print(a[1]* a[2])