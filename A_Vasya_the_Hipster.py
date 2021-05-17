a,b=map(int,input().split())
c1=min(a,b)
c2=0
res=abs(a-b)
while(res>0):
    if res%2==0:
        c2+=1
    else:
        if (res-1)%2==0 and res>1:
            c2+=1
    res-=2
        
print(c1,c2)


