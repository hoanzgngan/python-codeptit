def check(s):
    if len(s) < 3 :
        return "NO"
    array = list(int(i) for i in s )
    up = True
    for i in range (1, len(array)):
        if up and array[i] <= array[i - 1]:
            up = False
        elif not up and array[i] >= array[i - 1]:
            return "NO"
    return "YES"

for case in range(int(input())):
    s = input()
    print(check(s))