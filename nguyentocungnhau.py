import math

n, k = [int(i) for i in input().split()]
min = 10**(k-1)   # so nho nhat co k chu so [  10^(2-1) = 10^1 = 10 -> Số nhỏ nhất có 2 chữ số là 10  ]
max = 10**k - 1   # so lon nhat co k chu so [  10^2 - 1 = 99] 
count = 0
for i in range(min, max + 1):
    if math.gcd(n,i) == 1:
        print(i, end=" ")
        count += 1
        if count % 10 == 0: #1 dong co 10 so -> xuong dong
            print()


