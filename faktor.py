x, y = [ x for x in input().split(" ")]
articles = int(x)
impactFactor = int(y)

citation = articles * impactFactor
goal = int(citation/articles) - 1
while citation/articles > goal:
	citation -= 1
print(citation+1) 
