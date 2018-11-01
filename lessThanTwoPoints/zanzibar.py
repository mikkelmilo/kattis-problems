n = int(input())

for i in range(n):
    turtles = [int(x) for x in input().split()]
    turtles = turtles[:len(turtles)-1]
    prev = -1
    sum = 0
    for j in turtles:
        if prev == -1:
            prev = j
            continue
        if j > 2 * prev:
            sum += j - (2*prev)
        prev = j
    print(sum)
