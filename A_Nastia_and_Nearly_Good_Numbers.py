import math
test = 1
test = int(input())

for tc in range((test)):
    # Write your code....
    a, b = map(int, input().split())
    if b == 1:
        print("NO")
    else:
        print("YES")
        print(a, a*b, a*(b+1))
