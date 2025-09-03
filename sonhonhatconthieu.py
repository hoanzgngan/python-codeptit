n = int(input())
a = [int(i) for i in input().split()]

for i in range(1, n+2): #nho nhat = 1
    if i not in a:
        print(i)  #neu i khong co trong danh sach, in i ra va break luon -> ta dc so nho nhat con thieu
        
        break


