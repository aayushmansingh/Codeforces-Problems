import math
test = 1
test = int(input())

for tc in range((test)):
    # Write your code....
    n = int(input())
    l = list(map(int, input().split()))
    res = [0]*n
    left = 0
    right = n-1
    for i in range(len(l)):
        if i % 2 == 0:
            res[i] = l[left]
            left += 1
        else:
            res[i] = l[right]
            right -= 1
    print(*res)
