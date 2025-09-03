import math

a,b = [int(i) for i in input().split()]
for x in range(a, b+1):
    for y in range(x + 1, b + 1):
        for z in range(y + 1, b + 1):
            if math.gcd(x,y) == 1 and math.gcd(x,z) == 1 and math.gcd(y,z) == 1 :
                print("("+ str(x) + ", " + str(y)+ ", " + str(z)+")")


