P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

while True: 
    string = input()
    if string == "0": #string co 0 = break
        break

    k, s = string.split()
    k = int(k)
    res = ""
    for i in s :
        j = P.find(i)
        res += P[(j+k)%28]
    print(res[::-1])

