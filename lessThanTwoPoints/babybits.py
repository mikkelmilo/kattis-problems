bites = int(input())
mumbles = [x for x in input().split()]

f = [x for (i,x) in enumerate(mumbles) if x == str(i+1) or x == "mumble"]
if len(f) == len(mumbles):
    print('makes sense')
else:
    print('something is fishy')
