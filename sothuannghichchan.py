def check(s):
    if len(s) % 2 == 1  or  s != s[::-1] : # là số thuận nghịch and số chữ số cũng là một số chẵn
        return False
    for i in s :
        if int(i) % 2 == 1 : # Tất cả các chữ số đều chẵn
            return False
    return True

for case in range(int(input())):
    n = int(input())
    for i in range(22, n , 2): # Chay tu 22, bc nhay 2
        if check(str(i)):
            print(i, end= " ")    
    print()