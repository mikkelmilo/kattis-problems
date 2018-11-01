
while True:
    n = int(input())
    if n == -1: break
    t = 0
    d = 0
    for i in range(n):
        speed, time = [int(x) for x in input().split()]
        d += speed * (time - t)
        t = time
    print(d, "miles")
