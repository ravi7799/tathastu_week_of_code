def check(str):
    global arr
    l1=list(str)
    l1.sort()
    str1="".join(l1)
    bool1=False
    s=""
    for i in str:
        if i in arr:
            s=s+i
    l2=list(s)
    l2.sort()
    str2="".join(l2)
    if str1==str2:
        return True
    else:
        return False

dict2=["add","go","bat","me","eat","goal","boy","run"]
arr=['e','o','b','a','m','g','l']

for i in dict2:
    Bool1=check(i)
    if Bool1==True:
        print(i)


