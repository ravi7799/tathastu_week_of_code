#assuming value of house cannot be negative
def max_stole(list1,len1):
    if len1==0:
        return 0
    elif len1==1:
        return list1[0]
    elif len1==2:
        return max(list1[0],list1[1])
    max_val=None
    val1=list1[0]
    val2=max(list1[0],list1[1])
    for i in range(2,n):
        max_val=max(val1+list1[i],val2)
        val1 = val2
        val2 = max_val
    return max_val

n=int(input("enter the number of houses in a line:"))
lis=[]
for i in range(n):
    lis.append(int(input("enter the value of house")))
print(max_stole(lis,n))
