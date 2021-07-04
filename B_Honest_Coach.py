# Similar to Minimise Heights II GFG problem
import math
test = 1
test = int(input())

for tc in range((test)):
    # Write your code....
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    res = l[n-1]-l[0]
    for i in range(n):
        for j in range(i+1, n):
            res = min(res, l[j]-l[i])
    print(res)
