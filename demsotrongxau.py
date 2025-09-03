for case in range(int(input())):
    s = input()
    n = input()
    f = s.find(n)
    count = 0
    while f != -1: # s.find(n, start) : neu khong tim thay, tra ve -1, start : vi tri bat dau
        count += 1
        f = s.find(n, f + len(n)) # vd:aaaaa n = aa -> len(n) = 2 -> chay tiep tu phtu 3
    print(count)


    