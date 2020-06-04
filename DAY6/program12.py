N=int(input("Enter the number of Strings you want to enter:"))
#for example use this string
#arr=["geeksforgeeks", "geeks", "geek", "geezer"]
arr=[]
print(arr)
for i in range(N):
    arr.append(input("Enter your String:"))
size = len(arr)
if (size == 0):
    print("no string in a array")
elif (size == 1):
    print(arr[0])
arr.sort()
end = min(len(arr[0]), len(arr[size - 1]))
i=0
while i<end:
    if arr[0][i] == arr[size - 1][i]:
        i += 1
    else:
        break
print("longest prefix is:",arr[0][0: i] )
