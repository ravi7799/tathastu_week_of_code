#assuming value of house cannot be negative
def maxvalue(list1,k):
    sum=0
    cursum=0
    if k%2==0:
        for i in range(k,len(list1),2):
            if cursum+list1[i]>sum:
                sum=cursum+list1[i]
                cursum=cursum+list1[i]
            else:
                continue
        return sum
    else:
        for i in range(k,len(list1),2):
            if cursum+list1[i]>sum:
                sum=cursum+list1[i]
                cursum=cursum+list1[i]
            else:
                continue
        return sum


n=int(input("enter the number of houses in a line:"))
lis=[]
for i in range(n):
    lis.append(int(input("enter the value of house")))
sum1=maxvalue(lis,0)
sum2=maxvalue(lis,1)
if sum1>sum2:
    print(sum1)
else:
    print(sum2)
