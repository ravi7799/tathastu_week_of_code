list1=[2, 3, -7, 6, 8, 1, -10, 15]
list1.sort()
j = 0
len1=len(list1)
for i in list1:
    if (i<=0):
        j += 1
print(list1,j)
missing_num=1
for i in list1[j:]:
    if missing_num not in list1:
        print("missing smallest number is:",missing_num)
        break
    missing_num+=1

