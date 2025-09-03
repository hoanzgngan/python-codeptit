for case in range(int(input())):
    n = input()
    r = "" # chuoi rong
    for i in range(0, len(n), 2 ):
        r += n[i] * int(n[i+1]) 
    print(r)

