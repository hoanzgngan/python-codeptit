D = [0] * 42 
nd10, count = 10, 0
while nd10 != 0 :
    a = [int(i) for i in input().split()]
    nd10 -= len(a)
    for i in a :
        if D[i % 42 ] == 0:
            D[i % 42] = 1
            count += 1
print(count)