i = [int(x) for x in input().split()]

i.sort()

diffs = [i[1]-i[0], i[2]-i[1]]
if diffs[0] == diffs[1]:
    print(i[2]+diffs[0])
elif diffs[0] > diffs[1]:
    print(diffs[0]//2 + i[0])
else:
    print(diffs[1]//2 + i[1])
