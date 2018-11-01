n = int(input())

ins = n * [None]
for i in range(n):
    input()
    ys = [int(x) for x in input().split()]
    ins[i] = (min(ys), max(ys))

for i in ins:
    print((i[1] - i[0])*2)
