import math
def check(a,b):
    a, b = int(a), int(b)
    if math.gcd(a,b) == 1 : #uoc chung lon nhat cua a va b = 1
        return "YES"
    else: return "NO"

for case in range(int(input())):
    n = input() #su dung n dang chuoi nen k dc dung int
    print(check(n,n[::-1])) #so n va so dao nguoc cua n


