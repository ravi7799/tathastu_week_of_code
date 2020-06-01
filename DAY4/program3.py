dict1={}
n=int(input("enter number of element in dictionary to be inserted:"))
for i in range(n):
        dict1[i]=int(input("enter its value:"))
len1=len(dict1)
max=0
for i in range(len1):
    if dict1.get(i)>max:
        max=dict1.get(i)
max2=0
for i in range(len1):
    if dict1.get(i)>max2 and dict1.get(i)<max:
        max2=dict1.get(i)
print(max2)
