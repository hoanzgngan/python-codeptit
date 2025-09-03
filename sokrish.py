kr = [1] * 10
for i in range(2,10):
    kr[i] = kr[i-1] * i #n! = (n-1)*n

for case in range(int(input())):
    n = input()
    s = sum(kr[int(i)] for i in n)
    print("YES" if s == int(n) else "NO")


