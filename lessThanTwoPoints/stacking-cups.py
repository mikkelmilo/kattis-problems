n = int(input())
l = []
for i in range(n):
    a,b = [x for x in input().split()]
    if a.isdigit():
        l.append((b, int(a)/2))
    else:
        l.append((a, int(b)))
l.sort(key=lambda x: x[1])
for (s,_) in l:
    print(s)
