n = int(input())

d = dict()

for i in range(n):
    category = input()
    if category in d.keys():
        d[category] += 1
    else: d[category] = 1

min_nr = 999999
for k in d.keys():
    if d[k] <= min_nr:
        min_nr = d[k]

best_categories = [x for x in d.keys() if d[x] == min_nr]
best_categories.sort()
for x in best_categories:
    print(x)
