import math
test = 1
test = int(input())

for tc in range((test)):
    # Write your code....
    x, y, n = map(int, input().split())
    print((n-y)//x*x+y)
