for case in range(int(input())):
    s = input()
    t = 1
    for i in s :
        if int(i) != 0 :
            t *= int(i) 
    print(t)  

