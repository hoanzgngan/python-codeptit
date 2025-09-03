""" Hãy viết chương trình thao tác trên mảng một chiều, với các phần tử là số nguyên
Yêu cầu: Nhập, Xuất, Tính tổng, trung bình cộng các phần tử nguyên dương, trung bình cộng các phần
tử nguyên âm """


def mang():
    n = int(input())
    arr = []
    for i in range(n) :
        a = int(input())
        arr.append(a)
    return arr 

def xuatmang(arr):
    print(arr)

def tongmang(arr):
    return sum(arr)

def tbduong(arr):
    duong = [i for i in arr if i > 0]
    return sum(duong) / len(duong) if duong else False

def tbam(arr):
    am = [i for i in arr if i < 0]
    return sum(am) / len(am) if am else False

if 1 :
    arr = mang()
    xuatmang(arr)
    print(tongmang(arr))
    print(tbduong(arr))
    print(tbam(arr))


    






