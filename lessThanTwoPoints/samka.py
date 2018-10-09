l = int(input())
d = int(input())
x = int(input())

def sumDigits(n):
	return sum([int(x) for x in list(str(n))])

n = d
m = l
	
for i in range(l,d+1):
	if sumDigits(i) == x and i < n: n = i 
	if sumDigits(i) == x and i > m: m = i
	
print(n)
print(m)
