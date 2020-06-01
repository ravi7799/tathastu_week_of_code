n=int(input("enter the number of votes:"))
list1=[]
for i in range(n):
    list1.append(input("enter the candidate name to vote for him"))
list1.sort()
lis=[]
max=0
dictvote={}
for i in list1:
    if i not in lis:
        count=0
        for j in list1:
            if i==j:
                count=count+1
        dictvote[i]=int(count)
    if i not in lis:
        lis.append(i)
print(dictvote)
for i,j in dictvote.items():
    if dictvote[i]>max:
        max=dictvote[i]
print(max)
for i in dictvote:
    if dictvote[i]==max:
        print("highest number of votes are in favour of:    ",i,"    with the count of:",dictvote[i])

