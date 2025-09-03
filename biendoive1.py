while 1:
    n = int(input())
    if n == 0 :
        break    #neu n = 0 dung chuong trinh
    count = 1    #neu n = 1 thi count luon = 1
    while n > 1 :
        if n % 2 == 0 :
            n = n/2
            count += 1
        else:
            n = n*3 + 1
            count += 1
    print(count)

