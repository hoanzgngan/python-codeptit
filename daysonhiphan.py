n = int(input())
l = [int(i) for i in input().split()]

count = 0
for i in range(1, len(l)):
    if l[i] != l[i - 1]:
        count += 1
print(count)




