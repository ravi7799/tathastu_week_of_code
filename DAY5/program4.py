def knapSack(W, wt, val, n):
    if n == 0 or W == 0 :
        return 0
    if (wt[n-1] > W):
        return knapSack(W, wt, val, n-1)
    else:
        return max(val[n-1] + knapSack(W-wt[n-1], wt, val, n-1),
                   knapSack(W, wt, val, n-1))

val1 = [10,30,80,100]
wt1 = [2,8,5,6]
wt1.sort()
W =8
n = len(val1)
print(knapSack(W, wt1, val1, n))
