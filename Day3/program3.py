str1=input("enter  string to remove dupliacte character:")
l1=list(str1)

for i in l1:

    for j in l1[l1.index(i)+1:]:
        if j==i:
            l1.remove(j)
        else:
            continue


strn="".join(l1)
print(strn)

