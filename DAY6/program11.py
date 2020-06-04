N=int(input("enter size of array:"))
list=[]
for i in range(N):
    list.append(int(input("enter element in your array:")))
list.sort()
mulmax=1
for i in range(N-1,N-4,-1):
    mulmax*=list[i]
print("maximum product of three numbers in this array can be:",mulmax)
