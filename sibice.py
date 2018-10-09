import math

N,W,H = [int(x) for x in input().split()]
for i in range(N):
    x = int(input())
    if x <= math.sqrt(W**2 + H**2): print('DA')
    else: print('NE')
