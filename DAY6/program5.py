n=int(input("enter the number of element in your fibonacci series:"))
fib=[]
a=0
b=1
fib.append(a)
fib.append(b)
for i in range(n-2):
    c=a+b
    fib.append(c)
    a=b
    b=c
print(fib)
i=int(input("enter a number from fibonacci series:"))
j=int(input("enter another number from fibonacci series:"))
if i in fib and j in fib:
     if i+j in fib:
            print("fibonacci elements :",i,"and",j,"there exist a fibonacci number equal to their sum",i+j)
     else:
         print("fibonacci number equal to sum of element is not present")
