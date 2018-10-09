i = input()
def swap(type, pos):
    if type == 'A':
        x,y = pos[0], pos[1]
        pos[0] = y
        pos[1] = x
        return pos
    if type == 'B':
        x,y = pos[1], pos[2]
        pos[1] = y
        pos[2] = x
        return pos
    if type == 'C':
        x,y = pos[0], pos[2]
        pos[0] = y
        pos[2] = x
        return pos
    return pos

pos = [1,2,3]
for i in list(i):
    pos = swap(i, pos)

if pos[0] == 1: print(1)
elif pos[1] == 1: print(2)
elif pos[2] == 1: print(3)
