import math
for test in range(int(input())):  
    n, x, m = [float(i) for i in input().split()]

    r = math.log(m/n,  1 + x / 100)
    print(math.ceil(r))

    