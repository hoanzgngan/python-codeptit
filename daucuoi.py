def check(s):
    for i in range(len(s)):
        if s[len(s) - 2] == s[0] and s[len(s) - 1] == s[1]:
            return "YES"
    return "NO"

for i in range(int(input())):
    s = input()
    print(check(s))


      
