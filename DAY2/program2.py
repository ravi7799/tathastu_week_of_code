#program for fibonacci series


a=0
b=1
third=0
n=int(input("enter the number of terms you want in your fibonacci series"))
print(a," , ",b,end="")
for i in range(0,n-2):
    third=b+a
    a=b
    b=third
    print(" , ",third,end="")

