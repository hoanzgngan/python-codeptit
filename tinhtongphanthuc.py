for case in range(int(input())):
    n = int(input())
    s = 0 
    for i in range(2 -  n%2, n + 1 , 2): #bat dau tu 2 neu n chan va tu 1 neu n le
        s += 1/i 

    print("{:.6f}".format(s))   # in ra op 6 chu so phan thap phan

