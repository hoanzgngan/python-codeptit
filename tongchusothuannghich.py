for case in range(int(input())):
    n = input()
    s = str(sum(int(i) for i in n))
    print("YES" if len(s) > 1 and s == s[::-1] else "NO")



