x,y = [int(x[::-1]) for x in input().split()]

print(x if x > y else y)
