n = int(input())
xs = [int(x) for x in input().split()]
xs = xs[:n]
res = 0
for x in xs:
    if x < 0:
        res += 1
print(res)
