def check(n):
    for i in range(len(n)):
        if n[i] != "4" and n[i] != "7" :
            return "NO" 
    return "YES"

for case in range(int(input())):
    n = input()
    print(check(n))
