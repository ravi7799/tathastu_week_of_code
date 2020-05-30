#program number 3
#print the given pattern


n=int(input("enter the value in N:"))
for i in range(0,n):
    for j in range(0,n):
        if i==j or i+j==n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()

