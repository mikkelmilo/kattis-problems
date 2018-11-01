s = input()

res = [x for (i,x) in enumerate(s) if i == 0 or s[i-1] != x]
print(''.join(res))
