n = int(input())

#for n = 3,  2 * (2 * (2 * 2 - 1) -1) -1 = 9
#
# 0 -> 2
#
# 1 -> 3
# 2 -> 5
# 3 -> 9
# 4 -> 17
# 5 -> 33
# 6 -> 65

# general formula: (2^n + 1)^2
print((2**n + 1)**2)