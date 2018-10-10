c = float(input())
l = int(input())

res = 0
for i in range(l):
    w,h = [float(x) for x in input().split()]
    res += w * h * c
print("%.7f" % res)
