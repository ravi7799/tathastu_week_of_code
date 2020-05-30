"""
program for checking a number is odd or not
"""
num=int(input("enter a number to check if a number is even or odd :"))
if num%2==0:
    print("even number")
else:
    print("odd number")

#program to check if the number is prime or not


num2=int(input("enter a number to check if a number is prime or not :"))
if num2==1 or num2==2:
    print("prime number")

x=int(num2/2)

for i in range(2,x+2):
    if num2%i!=0 and i==x+1:
        print("prime number ")
    elif num2%i==0:
        print("not a prime number")
        break;



#program to check if number is palindrome or not

num3=int(input("enter a number to check if it is a palindrome:"))
x=int(num3)
rev=0
i=0
while x!=0:
    x=x//10
    i=i+1

x=num3
while x!=0:
    rev=int(rev+(x%10)*(10**(i-1)))
    x=x//10
    i=i-1

if rev==num3:
    print("number is palindrome  ")
else :
    print("number is not a palindrome   ")


#to check if a number is armstrong or not

num4=int(input("enter a number to check if it is a armstrong number or not"))
sum=0

x=num4
while x!=0:
    sum=sum+(x%10)**3
    x=x//10

if sum==num4:
    print("armstrong number")
else:
    print("not a armstrong number")





