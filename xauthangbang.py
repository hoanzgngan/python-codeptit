def thangbang(a,b):
    for i in range(1, len(a)):
        if (abs(ord(a[i]) - ord(a[i-1]))) !=  (abs(ord(b[i]) - ord(b[i-1]))): #abs :tri tuyet doi
            return "NO"                                                       #ord : chuyen thanh ma ASCII
    return "YES"

for case in range(int(input())):
    a = input()
    print(thangbang(a,a[::-1]))





