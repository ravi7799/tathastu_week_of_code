n1=int(input("number of element in list 1:" ))
n2=int(input("number of element in list 2:" ))

list1=[]
list2=[]
for i in range(n1):
    list1.extend(input("enter the value in list 1:"))

for i in range(n2):
    list2.extend(input("enter the value in list 2:"))

inter=[]
for i in list1:
    for j in list2:
        if j==i:
            inter.extend(j)
        else:
            continue
listunion=list(list1)
listunion.extend(list2)
s=set(listunion)
print("intersection is the given two list is:",inter)
print("union of the list will be:",s)
