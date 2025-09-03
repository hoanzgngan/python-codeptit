def check(s):
    if s[0] == s[1] :
        return "NO"
    for i in range (2, len(s)):
        if s[i] != s[i - 2]:
            return "NO"
    return "YES"

for case in range(int(input())):
    s = input()
    print(check(s))


#vi du so dep 121212