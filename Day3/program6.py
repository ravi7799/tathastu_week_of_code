def makesumlist(list1):
    list1.sort()
    print(list1)
    l=list(list1)
    sum=0
    sumlist=[]
    sumlist.extend(list1)
    print(sumlist)
    for i in l:
        l=list1
        l.remove(i)
        list2=list(l)
        for j in list2:
            sum=int(i)+int(j)
            sumlist.append(str(sum))
    return sumlist



def program6():
    n=int(input("enter the size of list:"))
    list1=[]
    for i in range(n):
        list1.extend(input("enter the value:"))
    j=1
    list1.sort()
    sumlist=list(makesumlist(list1))
    s1=set(sumlist)
    sumlist=list(s1)
    print(sumlist)
    while True:
        if str(j) not in sumlist:
            return j
        else:
            j=j+1

c=program6()
print(c)
