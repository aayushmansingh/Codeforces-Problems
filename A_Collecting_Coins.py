import math
test = 1
test = int(input())

for tc in range((test)):
    # Write your code....
    l = [0]*3
    l[0], l[1], l[2], n = map(int, input().split())
    l.sort()
    n -= 2*l[2]-l[1]-l[0]
    if n < 0 or n % 3 != 0:
        print("NO")
    else:
        print("YES")
