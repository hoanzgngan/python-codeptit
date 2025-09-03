for case in range(int(input())):
    s = input() + "."
    count,now = 0, s[0]
    for i in s:
        if i == now :
            count += 1
        else: 
            print(str(count) + now , end="")
            count, now = 1, i
    print()