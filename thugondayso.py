n = int(input())
array = list(int(i) for i in input().split())

stack = []
for i in array:
    if stack and (stack[-1] + i) % 2 == 0 :
        stack.pop()
    else:
        stack.append(i)
print(len(stack))




