x = [x for x in input().split()]
vowels = "aeiou"

res = []
for word in x:
    i = 0
    r = ''
    while i < len(word):
        r += word[i]
        if word[i] in vowels:
            i += 3
        else:
            i += 1
    res.append(r)

print(' '.join(res))
