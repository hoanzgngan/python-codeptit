def check(n):
    if  len(n) % 2 == 1 or n != n[::-1] :
        return 0
    for i in n :
        if int(i) % 2 == 1 :
            return 0
    return 1

for case in range(int(input())) :
    n = int(input())
    for i in range(22,n):
        if check(str(i)):
            print(i, end=" ")
    print()


