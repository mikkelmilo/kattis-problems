import math

n = int(input())
g = 9.82
for i in range(n):
    v0, theta, x1, h1, h2 = [float(x) for x in input().split()]
    theta = theta * math.pi/180
    t = lambda x : x/(v0 * math.cos(theta))
    yt = lambda t : v0 * t * math.sin(theta) - 1/2 * g * t**2
    y = yt(t(x1))
    if h1+1 <= y <= h2-1:
        print('Safe')
    else: print('Not Safe')
