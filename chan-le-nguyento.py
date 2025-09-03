import math 

def check(s):
    
    for i in range(len(s)):
        if i % 2 != int(s[i]) % 2 :
            return "NO"
        
    n = sum(int(i) for i in s )
    if n < 2 :
        return "NO"
    for i in range (2, int(math.sqrt(n) + 1 )):
        if n % i == 0 :
            return "NO"
    return "YES"
        
for case in range (int(input())):
    s = input()
    print(check(s))