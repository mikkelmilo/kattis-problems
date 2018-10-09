n = int(input())
res = 0
for i in range(n):
    s = input()
    res += int(s[:len(s)-1])**int(s[len(s)-1])

print(res)
