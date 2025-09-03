def check(a,b):
    for i in range(len(a)):
        if a[i] > b[i]:
            return "NO"
    return "YES"

for case in range(int(input())):
    n = int(input())
    a = sorted([int(i) for i in input().split()]) #sorted : tang dan day so trong danh sach
    b = sorted([int(i) for i in input().split()])
    print(check(a,b))

# nếu chỉ có 1 cách sắp xếp lại, chỉ cần xếp tăng dần dãy a và b, kiểm tra a[i] có <= b[i] hay không.

