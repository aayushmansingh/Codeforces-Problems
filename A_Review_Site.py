import math
test = 1
test = int(input())

for tc in range((test)):
    # Write your code....
    n=int(input())
    l=[]
    l=list(map(int,input().split()))
    c=0
    for i in l:
        if i==1 or i==3:
            c+=1
    print(c)