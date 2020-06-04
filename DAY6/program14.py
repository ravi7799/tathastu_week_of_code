def rotate90(lis,n):
    for i in range(n//2):
        for j in range(i,n-1-i):
            temp = lis[i][j]
            lis[i][j] = lis[N - 1 - j][i]
            lis[N - 1 - j][i] = lis[N - 1 - i][N - 1 - j]
            lis[N - 1 - i][N - 1 - j] = lis[j][N - 1 - i]
            lis[j][N - 1 - i] = temp


    print("\n--------------------------------------------------------------------------\n")
    for i in range(n):
        for j in range(n):
            print("{0:<4d}".format(lis[i][j]),end=" ")
        print()

list=[]
N=int(input("enter dimension of matrix,N="))
num=1
for i in range(N):
    a=[]
    for i in range(N):
        a.append(num)
        num+=1
    list.append(a)
print("normal matrix representation:")
for i in range(N):
    for j in range(N):
        print("{0:<4d}".format(list[i][j]),end=" ")
    print()
rotate90(list,N)
