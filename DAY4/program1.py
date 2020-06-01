n=int(input("enter the number of values you want to add in your tuple:"))
list1=[]
for i in range(n):
    list1.append(int(input("enter your values:")))
tup=tuple(list1)
len1=len(tup)
print("length of tuple:",len1)
count=0
tup2=list(tup)
lis=[]
for i in tup2:
    if i not in lis:
        count=0
        for j in tup2:
            if i==j:
                count=count+1
        print("number of ",i,"in tuple are:",count)
    lis.append(i)
