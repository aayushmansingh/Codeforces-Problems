import math
test = 1
test = int(input())

for tc in range((test)):
    # Write your code....
    s0, s1, s2, s3 = map(int, input().split())
    l = []
    max1 = max(s0, s1)
    max2 = max(s2, s3)
    min1 = min(s0, s1)
    min2 = min(s2, s3)
    if max1 < min2:
        print("NO")
    elif min1 > max2:
        print("NO")
    else:
        print("YES")
