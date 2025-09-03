s = [1] * 93 # tao chuoi 1 * 93
for i in range(3 , 93): #chay tu phan tu thu 3
    s[i] = s[i - 1] + s[i - 2] # cong thuc

for case in range(int(input())):
    a , b = [int(i) for i in input().split()] #tao a , b
    for i in range(a , b+1):
        print(s[i], end=" ")  
    print()# sau vòng lặp để xuống dòng cho test case tiếp theo