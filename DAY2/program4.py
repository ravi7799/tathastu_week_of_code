#program number 4
#To print a pattern

for i in range(0,10):
    for j in range(0,10):
        if i+j<=4 or j-i>=5:
            print("*",end=" ")
        elif i-j>=5 or i+j>=14:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
