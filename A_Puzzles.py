n,m=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
res=1001
for i in range(n,m+1):
    res=min(res,abs(l[i-1]-l[i-n]))
print(res)
