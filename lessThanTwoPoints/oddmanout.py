n = int(input())

for i in range(n):
    m = int(input())
    s = [int(x) for x in input().split()]
    sp = list(s)
    k = set(s)
    for j in k:
        s.remove(j)
    r = k - set(s)
    print('Case #' + str(i+1) + ":", r.pop())
