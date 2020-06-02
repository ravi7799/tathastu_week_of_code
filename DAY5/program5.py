list1=[5,3,36,421,8,54,32,865,13,72,12]
even=[]
odd=[]
print("list before:",list1)
for i in range(len(list1)):
    if list1[i]%2==0:
        even.append(list1[i])
    else:
        odd.append(list1[i])
even.sort(reverse=True)
odd.sort()
list1.clear()
list1.extend(odd)
list1.extend(even)
print("list after:",list1)
