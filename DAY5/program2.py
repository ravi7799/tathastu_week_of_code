lis=[16, 17, 4, 3, 5, 2]
def findgreatest(list1):
    max=list1[0]
    for i in list1[1:]:
        if i>max:
            max=int(i)
    return max
len1=len(lis)
print(len1)

for i in range(len1):
    if i<len1-1:
        lis[i]=findgreatest(lis[i+1:])
    else:
        lis[i]=-1
print(lis)
