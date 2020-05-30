#program number 3
#print the given pattern

for i in range(0,8):
    for j in range(0,8):
        if i==j or i+j==7:
            print("*",end="")
        else:
            print(" ",end="")
    print()
