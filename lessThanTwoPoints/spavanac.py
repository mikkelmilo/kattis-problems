h,m = [int(x) for x in input().split()]

if m >= 45:
    print(h, m-45)
else:
    rest = 45 - m
    print((h-1) % 24, 60-rest)
