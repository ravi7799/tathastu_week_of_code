
n=int(input("enter the size array:"))
arr=[]
print("enter a array in sorted manner or rotated manner:")
for i in range(n):
    arr.append(int(input("enter element in your array")))

min=99999999
for i in arr:
    if i<min:
        min=i
if min==arr[0]:
    print("Its a sorted array:",arr)
else:
    print("it is a rotated array:",arr,"by ",arr.index(min),"steps")
    arr.sort()
    print("its sorted version is:",arr)

