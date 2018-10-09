
x = int(input())
n = int(input())

sum = 0
for i in range(n):
    s = int(input())
    sum += s

print(x * (n+1) - sum)
