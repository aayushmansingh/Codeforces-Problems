import math
test = 1
test = int(input())

for tc in range((test)):
    # Write your code....
    l=list(map(int,input().split()))
    l.sort()
    flag=1
    for i in range(0,len(l)-1):
        if abs(l[i]-l[i+1])<=1:
            flag=1
        else:
            print("NO")
            exit()
    if flag:
        print("YES")