nlist=[]


def sum(l,s=0):
    for i in l:
        nlist.append(s+i)
        l1=list(l)
        l1.remove(i)
        sum(l1,s+i)

n=int(input("enter the size of list:"))
list1=[]
for i in range(n):
    list1.append(int(input("enter the value:")))
j=1
list1.sort()
sum(list1)


while True:
    if j not in nlist:
        print(j)
        print()
        break
    else:
        j=j+1

