import math

for case in range(int(input())):
    n = int(input())
    kq = "1"
    for i in range(2, int(math.sqrt(n) + 1)):
        count = 0 
        while n % i == 0: #Dùng vòng lặp while để chia n liên tục cho i nếu n chia hết cho i.
            count += 1 # Đếm số lần chia, tức là số mũ của thừa số nguyên tố.
            n /= i
        if count > 0 : #Nếu cnt > 0, tức là i là một thừa số nguyên tố, ta thêm vào kết quả
            kq += " * " + str(i) +"^" + str(count)
        if n == 1: #Nếu n đã về 1, dừng vòng lặp vì không còn gì để phân tích.
            break
    
    if n > 1 :    #Nếu n > 1, thì n là một số nguyên tố lớn cần thêm vào kết quả.
        kq += " * " + str(int(n)) + "^1 "
    
    print(kq)

