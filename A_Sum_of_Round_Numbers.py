import math
test = 1
test = int(input())

for tc in range((test)):
    # Write your code....
    n=int(input())
    pos=1
    l=[]
    while(n!=0):
        d=n%10
        if d>0:
            l.append(d*pos)
        n//=10
        pos*=10
    print(len(l))
    for i in sorted(l,reverse=True):
        print(i,end=' ')
    print()