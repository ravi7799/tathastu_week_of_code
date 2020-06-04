def ackerman(m,n):
    if m==0:
        return n+1
    elif m!=0 and n==0:
        return ackerman(m-1,1)
    else:
        return ackerman(m-1,ackerman(m,n-1))

m=int(input("enter value of m:"))
n=int(input("enter value of n:"))
print("By using ackerman function, the result we got is for m=",m,"n=",n,"is:",ackerman(m,n))
