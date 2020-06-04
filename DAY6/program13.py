n=int(input("size of array:"))
arr=[]
print("plz enter real numbers in this array:\n example- 0.3")
for i in range(n):
    arr.append(input("enter real numbers greater than  zero:"))
#use this for example
#arr=['0.6', '0.2', '1', '0.5', '0.999', '0.88']

print(arr)
arr2=list(arr)
for a in arr2:
    print("a=",a)
    arr2.remove(a)
    for b in arr2:
        arr2.remove(b)
        print("b=",b)
        for c in arr2:
            print("a+b+c",a+b+c)
            if float(float(a)+float(b)+float(c))<2 and float(float(a)+float(b)+float(c))>1:
                print("triplet found a=",a,"b=",b,"c=",c,"\na+b+c=",float(a)+float(b)+float(c),"\n")
        arr2.append(b)
    arr2.append(a)
