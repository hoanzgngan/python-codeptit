import math 
def check(n):
    if n < 2 :
        return "NO"
    for i in range(2, int(math.sqrt(n)) + 1 ):
        if n % i == 0 :
            return "NO"
    return "YES"

for case in range(int(input())):
    s = input()
    n = int(s[-4:]) # 4 so hang cuoi cua s
    print(check(n))


