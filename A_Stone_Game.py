import math
test = 1
test = int(input())

for tc in range((test)):
    # Write your code....
    n = int(input())
    l = list(map(int, input().split()))
    maxi = l.index(max(l))
    mini = l.index(min(l))
    if(mini > maxi):
        maxi, mini = mini, maxi
    print(min(maxi+1, n-mini, mini+1+n-maxi))
