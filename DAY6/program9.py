list=[]
size=int(input("enter size of the array:"))
k=int(input("enter the value of k, to find the kth smallest element of the array"))
print("plz enter distinct element in the array")
for i in range(size):
    list.append(int(input("enter an element to array:")))
list.sort()

print("kth smallest element is:",list[k-1])
