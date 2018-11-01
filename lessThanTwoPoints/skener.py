R,C,ZR,ZC = [int(x) for x in input().split()]

inputs = R * [None]
for i in range(R):
    inputs[i] = input()

for l in inputs:
    lp = ''.join([x * ZC for x in l])
    for i in range(ZR):
        print(lp)
