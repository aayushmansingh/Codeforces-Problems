import math

for _ in range(int(input())):
    # Write your code....
    s=int(input())
    count=0
    ans=[2050]
    for i in range(14):
        ans.append(ans[-1]*10)
    n=len(ans)
    for i in range(n-1,-1,-1):
        while s>=ans[i]:
            s-=ans[i]
            count+=1
    if count==0 or s>0:
        print(-1)
    else:
        print(count)