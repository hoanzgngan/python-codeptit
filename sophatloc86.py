def check(n):
    l = len(n)
    if n[l - 2] == "8" and n[l-1] == "6" :
        return "YES"
    else: return"NO"

for t in range(int(input())):
    n = input()
    print(check(n)) 


    