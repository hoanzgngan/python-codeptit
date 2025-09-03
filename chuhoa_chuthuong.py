n = input()

lower = 0
for i in n:
    if i.islower():
        lower += 1

l = len(n)
if lower >= l - lower :
    print(n.lower())
else: print(n.upper())

