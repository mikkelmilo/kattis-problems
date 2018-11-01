n = int(input())

for i in range(n):
    l = int(input())
    x = []
    for j in range(l):
        x.append(input())
    print(len(set(x)))
