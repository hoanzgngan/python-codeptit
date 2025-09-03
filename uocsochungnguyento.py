import math
def prime(n):
    if n < 2 :
        return 0
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return 0
    return 1

for case in range(int(input())):
    a,b = [int(i) for i in input().split()]
    s = sum(int(i) for i in str(math.gcd(a,b)))
    if prime(s):
        print("YES")
    else: print("NO")  

