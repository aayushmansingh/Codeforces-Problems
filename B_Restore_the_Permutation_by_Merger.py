import math
test = 1
test = int(input())

for tc in range((test)):
    # Write your code....
    n=int(input())
    l=list(map(int,input().split()))
    freq=[0]*(len(l))
    j=0
    for i in l:
        if i not in freq:
            freq[j]=i
            j+=1
    for i in freq:
        if i!=0:
            print(i,sep=' ', end=' ')
    print()