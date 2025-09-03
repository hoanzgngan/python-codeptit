for case in range(int(input())):
    n = input()
    a = list(int(i) for i in n)
    tong, tich = 0, 0
    for i in range (len(a)):
        if i % 2 == 1:  # vi tri le 
            tong += a[i]
        else: 
            if a[i] != 0: # cac so con lai 
                if tich == 0:
                    tich = a[i]
                else : tich *= a[i]

    print(str(tich) + " " + str(tong))    