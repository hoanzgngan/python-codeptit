import math

def check(s):
    if s < 2 :
        return "NO"
    for i in range(2 , int(math.sqrt(s) + 1)): 
        if s % i == 0 :
            return "NO"
    return "YES"

for case in range(int(input())): 
    n = input()
    s = sum(int(i) for i in n)
    print(check(s))