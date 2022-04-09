import sys

pads = []
for i in range(50):
    if i <= 2:
        pads.append(1)
    else:
        pads.append(pads[i-2] + pads[i-3])

if len(sys.argv) < 2:
    print(pads)
else:
    print(pads[int(sys.argv[1])])