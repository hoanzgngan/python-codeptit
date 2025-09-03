import math

def prime(n):
    if n < 2 :
        return 0
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0 :
            return 0
    return 1

list = [0,2] # Danh sách bắt đầu với 0 (giá trị đệm) và số nguyên tố đầu tiên là 2
k = 3
while (len(list) <= 1001) : # Lặp đến khi có ít nhất 1001 số nguyên tố
    if (prime(k)):
        list += [k]  # Thêm số nguyên tố vào danh sách
    k += 2    # Chỉ kiểm tra số lẻ vì số chẵn (trừ 2) không thể là số nguyên tố   

n, x = [int(i) for i in input().split()]
#n : số lần thực hiện phép cộng.
#x : giá trị ban đầu.
for i in range(n + 1):
    x += list[i]
    print(x, end=" ")

    


