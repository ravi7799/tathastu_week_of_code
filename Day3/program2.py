str1=input("enter a string:")
len=len(str1)

result = []

def permute(data, i, length):
    if i == length:
        result.append(''.join(data) )
    else:
        for j in range(i, length):

            data[i], data[j] = data[j], data[i]
            permute(data, i + 1, length)
            data[i], data[j] = data[j], data[i]
permute(list(str1), 0, len)
s1=set(result)
len2=0
for i in s1:
    len2=len2+1

print("Resultant permutations", s1,"\nNumber of permutations possible are:",len2)

