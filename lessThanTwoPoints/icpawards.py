n = int(input())

seen = []

prizeWinners = []

for i in range(n):
    uni, name = [x for x in input().split()]
    if not uni in seen:
        prizeWinners.append((uni, name))
    seen.append(uni)
j = 0
for i in prizeWinners:
    if j < 12:
        print(i[0], i[1])
    j += 1
