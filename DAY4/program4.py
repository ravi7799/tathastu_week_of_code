dict2={}
n=int(input("enter number of element in dictionary to be inserted:"))
for i in range(n):
        dict2[i]=int(input("enter its value:"))
lis=[]
dict1=dict(dict2)
print(dict2)
for i,j in dict2.items():
    if j in lis:
        dict1.pop(i)
    lis.append(j)
print(dict1)
