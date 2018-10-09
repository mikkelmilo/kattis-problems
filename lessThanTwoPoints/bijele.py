board = [1,1,2,2,2,8]
x = [int(x) for x in input().split()]
for (x,y) in (zip(x,board)):
	print(y-x, end=' ')
	
print()
