k=int(input("enter the value of k equal to number of sorted array:"))
list=[]
for i in range(k):
    a=[]
    size=int(input("enter the size of array:"))
    for j in range(size):
        a.append(int(input("enter elements in your array")))
    a.sort()
    list.append(a)
print(list)

a=[]
for i in range(k):
    print(list[i])
    a.extend(list[i])
a.sort()
print(a)
