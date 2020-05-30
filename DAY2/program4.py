#program number 4
#To print a pattern

n=int(input("enter the value in N:"))
for i in range(0,n):
    for j in range(0,n):
        if i+j<=n/2-1 or j-i>=n/2:
            print("*",end=" ")
        elif i-j>=n/2 or i+j>=n+n/2-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
