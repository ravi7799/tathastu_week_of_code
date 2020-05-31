n=int(input("enter the number of values you want to put in your list:"))
list1=[]
for i in range(n):
    list1.extend(input("enter the value:"))

print("Before :\n",list1)

for k in list1:
    for m in list1[list1.index(k)+1:]:
        if m==k:
            list1.remove(m)
        else:
            continue


print("After removing duplicacy:\n",list1)
