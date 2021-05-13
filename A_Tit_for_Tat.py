import math
test = 1
test = int(input())

for tc in range((test)):
    # Write your code....
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    
    pos=0
    while(k>0):
        if pos<n-1 and l[pos]>0 and k>0:
            l[pos]=l[pos]-1
            l[n-1]=l[n-1]+1
            k-=1
        elif k==0 or pos>n-1:
            break
        else:
            pos+=1
    for i in range(n):
        print(l[i],sep=' ',end=' ')
    print()