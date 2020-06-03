list1=[5,3,36,421,8,54,32,865,13,72,12]

def evenoddsort(lis):
    even=[]
    odd=[]
    for i in range(len(lis)):
        if lis[i]%2==0:
            even.append(lis[i])
        else:
            odd.append(lis[i])
    even.sort(reverse=True)
    odd.sort()
    lis.clear()
    lis.extend(odd)
    lis.extend(even)
    return lis
