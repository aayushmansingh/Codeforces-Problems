import math
test = 1
test = int(input())

for tc in range((test)):
    # Write your code....
    n=int(input())
    l=list(map(int,input().split()))
    rs=[l[-1]]*len(l)
    ls=[l[0]]*len(l)
    for i in range(1,n):
        ls[i]=ls[i-1]^l[i]
        rs[n-i-1]=rs[n-i]^l[n-i-1]
    c=0
    for j in range(1,n):
        if ls[i-1]==rs[i]:
            c=1
    for i in range(n):
        for j in range(i+2,n):
            if ls[i]==rs[j] and ls[i]==ls[j-1]^ls[i]:
                c=1
    if c==1:
        print("YES")
    else:
        print("NO")