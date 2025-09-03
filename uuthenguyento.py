import math
def prime(n):
    if n < 2 :
        return 0
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0 :
            return 0
    return 1

for case in range(int(input())):
    s = list(int(i) for i in input())
    nt = 0 
    for i in s:
        if prime(i):
            nt += 1
    if prime(len(s)) and nt > len(s) - nt :
        print("YES")
    else: print("NO")

