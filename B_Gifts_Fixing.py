import math
test = 1
test = int(input())

for tc in range((test)):
    # Write your code....
    n = int(input())
    l = list(map(int, input().split()))
    l2 = list(map(int, input().split()))
    mini = min(l)
    mini2 = min(l2)
    res = 0
    for i in range(n):
        res += max(abs(mini-l[i]), abs(mini2-l2[i]))
    print(res)
