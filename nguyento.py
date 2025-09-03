import math
def prime(n):
    if n < 2 :
        return 0
    for i in range(2,int(math.sqrt(n) + 1)):
        return 0
    return 1


for case in range(int(input())):
    k = 0
    n = int(input())
    for i in range(1,n):
        if int(math.gcd(i,n)) == 1:
            k += 1
    print("YES" if prime(k) else "NO")
