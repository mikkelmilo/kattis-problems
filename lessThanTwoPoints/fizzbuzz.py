x,y,n = [int(x) for x in input().split()]

for i in range(1,n+1):
    if i % x == 0:
        print('Fizz', end='')
    if i % y == 0:
        print('Buzz')
        continue
    elif i % x != 0 and i % y != 0: print(i, end='')
    print('')