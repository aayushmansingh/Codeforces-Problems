import math
test = 1
test = int(input())

for tc in range((test)):
    # Write your code....
    l, r = map(int, input().split())
    if 2*l > r:
        print(-1, -1)
    else:
        print(l, 2*l)
