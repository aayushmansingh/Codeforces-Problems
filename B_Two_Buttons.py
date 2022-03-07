n,m=map(int,input().split())
count=0
if m<n:
    print(n-m)
    exit(0)
while(m>n):
    if m%2==0:
        m//=2
        count+=1
    else:
        m+=1
        count+=1
print(abs(count+n-m))