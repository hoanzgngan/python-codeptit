s = input()
for i in range(len(s)-3, 0 , -3): #chay tu cuoi len, buoc nhay -3, stop 0
    s = s[:i] + "," + s[i:]  # truoc i va cuoi i chen dau ","
print(s) 

