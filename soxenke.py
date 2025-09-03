def check(s):
    if len(s) % 2 == 0: #len(s) phai le
        return "NO"
    if s[0] == s[1] :
        return "NO"
    for i in range(2, len(s), 2):  #chay tu phan tu thu 3 vs bc nhay 2, stop la phan tu cuoi cung
        if s[i] != s[0]:  
            return "NO"    
             
    return "YES"  

for case in range(int(input())):
    s = input()
    print(check(s))

     # so xen ke :  2324272  