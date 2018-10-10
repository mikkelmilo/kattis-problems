x = input()
res = 0

for i in range(len(x)):
    #print('offset', i%3, i, x[i])
    offset = i % 3
    if offset == 0 and x[i] != 'P':
        res += 1
    elif offset == 1 and x[i] != 'E':
        res += 1
    elif offset == 2 and x[i] != 'R':
        res += 1
print(res)
