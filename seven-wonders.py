s = input()

Ts = s.count('T')
Cs = s.count('C')
Gs = s.count('G')

# nr sets of different cards
x = min(Ts, Cs, Gs)

res = Ts**2 + Cs**2 + Gs**2 + x*7
print(res)
