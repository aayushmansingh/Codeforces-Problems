import math
test = 1
test = int(input())

for tc in range((test)):
    # Write your code....
    n=int(input())
    y=n%2020
    x=(n-y)//2020-y
    if x>=0:
        print("YES")
    else:
        print("NO")