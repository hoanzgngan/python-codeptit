import math
def prime(n):
    if n < 2 :
        return 0
    for i in range(2 , int(math.sqrt(n) + 1)):
        if n % i == 0 :
            return 0
    return 1

for case in range( int(input())):
    s = input()
    if prime(int(s[-3:])) and prime(int(s[:3])):
        print("YES")
    else: print("NO")


    

