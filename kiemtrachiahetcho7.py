def check(s):
    for i in range (1000):
        if s % 7 == 0 :
            return s 
        r = int(str(s)[::-1])  
        s += r 
    return -1

for case in range(int(input())):
    s = int(input())
    print(check(s))  