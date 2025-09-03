def check(s):
    for i in s :
        if i not in {"1", "2", "0"}:  #chay i neu i khong nam trong pham vi
            return "NO"
    return "YES"
    
for case in range(int(input())):
    s = input()
    print(check(s))


