import math
test = 1
test = int(input())

for tc in range((test)):
    # Write your code....
    n=int(input())
    l=list(map(int,input().split()))
    s=sum(l)
    if s<n:
        print(1)
    else:
        print(s-n)