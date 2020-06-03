def knapSack(W, wt, val, n):
    if n == 0 or W == 0 :
        return 0
    if (wt[n-1] > W):
        return knapSack(W, wt, val, n-1)
    else:
        return max(val[n-1] + knapSack(W-wt[n-1], wt, val, n-1),
                   knapSack(W, wt, val, n-1))

n=int(input("enter the number of weight and value pair you want to add")
val1 = []
for i in range(n):
      val1[i].append(int(input("enter value:")))
      

wt1 = []
for i in range(n):
      wt11[i].append(int(input("enter value:")))    
      

wt1.sort()
W =int(input("enter the maximum weight"))
print(knapSack(W, wt1, val1, n))
