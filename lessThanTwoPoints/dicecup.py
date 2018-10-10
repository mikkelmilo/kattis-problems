x,y = [int(x) for x in input().split()]

if x == y:
    print(x+1)
else:
    for i in range(abs(x-y)+1):
        print(i+1+min(x,y))
