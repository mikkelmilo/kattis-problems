x = [int(x) for x in input().split()]

largest = max(x)
smallest = min(x)
x.remove(largest)
second_largest = max(x)
x.remove(smallest)

print(smallest * second_largest)
