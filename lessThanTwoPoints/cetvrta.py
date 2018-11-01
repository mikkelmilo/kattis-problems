a,b = [int(x) for x in input().split()]
c,d = [int(x) for x in input().split()]
e,f = [int(x) for x in input().split()]

x = 0
if a == c:
    x = e
elif a == e:
    x = c
else:
    x = a

y = 0
if b == d:
    y = f
elif b == f:
    y = d
else:
    y = b

print(x,y)
