num=int(input("enter a integer input:"))
#program is to replace all 0 of a integer number with 5
def replace(num2):
    num2=str(num2)
    num2=list(num2)
    for i in num2:
        if int(i)==0:
            num2[num2.index(i)]=str(5)
    num2="".join(num2)
    return num2

k=replace(num)
print("new number is :",k)
