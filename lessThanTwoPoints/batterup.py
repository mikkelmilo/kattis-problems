n = int(input())
bats = [int(x) for x in input().split()]
nrWalks = sum([-x for x in bats if x == -1])
res = sum([x for x in bats if x != -1])/(n - nrWalks)
print(res)
