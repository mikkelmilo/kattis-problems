n = int(input())
inputs = n *[None]
for i in range(n):
    inputs[i] = input()

for i in inputs:
    print(len(i))
