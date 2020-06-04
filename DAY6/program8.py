def spiraldisplay(mat,r,c):
    k=0
    m=c-1
    l=0
    n=r-1
    while(k<r and m<c):
        for i in range(k,m+1):
            print(mat[k][i],end=" ")
        k+=1
        for i in range(k,n+1):
            print(mat[i][m],end=" ")
        m-=1
        for i in range(m,l-1,-1):
            print(mat[n][i],end=" ")
        n-=1
        for i in range(n,k-1,-1):
            print(mat[i][l],end=" ")
        l+=1



number=0
R=int(input("enter number of row in your 2D matrix:"))
C=int(input("enter number of column in your 2D matrix"))

matrix1=[]
a=[]
for i in range(R):
    a=[]
    for j in range(C):
        a.append(number)
        number+=1
    matrix1.append(a)

print(matrix1)
print("spiral display of 2D matrix")
spiraldisplay(matrix1,R,C)

