import math
test = 1
test = int(input())

for tc in range((test)):
    # Write your code....
    x, y = map(int, input().split())
    mini = min(x, y)
    maxi = max(x, y)
    res = max(mini+mini, maxi)
    print(res*res)
