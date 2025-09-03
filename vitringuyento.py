
import math
def prime(n):
    if n < 2 :
        return False # = return 0
    for i in range(2 , int(math.sqrt(n) + 1)):
        if n % i == 0 : 
            return False
    return True # = return 1

def check(s):
    for i in range(len(s)):
        if (prime(i) and not prime(int(s[i]))) or (not prime(i) and prime(int(s[i]))):
            return "NO"
    return "YES"

for case in range(int(input())):
    s = input()
    print(check(s))  