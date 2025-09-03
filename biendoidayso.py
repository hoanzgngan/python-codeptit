while True:
    list = [int(i) for i in input().split()]
    if list.count(0) == 4 :
        break
    dem = 0 
    while list.count(list[0]) != 4:
        cp = list.copy()
        for i in range(4):
            list[i] = abs(cp[i] - cp[(i+1) % 4])  #(i + 1) % 4 giúp lấy phần tử kế tiếp trong danh sách (xoay vòng).
        dem += 1
    print(dem)




