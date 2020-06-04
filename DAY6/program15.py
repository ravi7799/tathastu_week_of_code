"""n=int(input("size of array:"))
list=[]
for i in range(n):
    list.append(int(input("enter element in your array:")))
"""
def checksm(lis,k):
    print(lis,k)
    list2=lis[:k+1]
    list2.remove(lis[k])

    list3=lis[k:]
    list3.remove(lis[k])

    list2.sort()
    print("list2   :",list2)
    list3.sort()
    print("list3    :",list3)
    print("\n")
    if k==0:
        if list3[0]>lis[k]:
            return True
    elif k==len(lis):
        if list2[len(list2)-1]<lis[k]:
            return True
    elif list2[len(list2)-1]<lis[k] and list3[0]>lis[k]:
        return True
    else:
        return False

list=[5, 1, 4, 3, 6, 8, 10, 7, 9]
a=[]
count=0
for i in range(len(list)):
    if checksm(list,i)==True:
        a.append(list[i])
        count+=1

a.sort()
if count>=1:
    print("element at index",list.index(a[0])," is the smallest number after which all number are greater\n and before which all number are smaller")
