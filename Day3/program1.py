"""
1st method
"""
str=input("enter a string which you want to be reversed: ")
len1=len(str)
i=0
rev=""
while(i<=(len1-1)):
    rev=rev+str[-1-i]
    i=i+1
print(rev)

#another method

rev2=[]
l=list(str)
for i in range(len1):
    rev2.append(l.pop())
m="".join(rev2)
print(m)

#3rd method

rev3=""
for i in str:
    rev3=i+rev3
print(rev3)

#4th method
print(str[::-1])
