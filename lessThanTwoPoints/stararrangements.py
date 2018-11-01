n = int(input())

print(str(n)+':')
for i in range(2,n):
    for j in range(i-1,i+1):
        mod = n % (i+j)
        if mod == 0 or mod == i:
            print(str(i) + ","+str(j))
