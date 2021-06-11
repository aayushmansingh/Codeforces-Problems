n=int(input())
boys=list(map(int,input().split()))
m=int(input())
girls=list(map(int,input().split()))
boys.sort()
girls.sort()
ans=0
for i in range(n):
    for j in range(m):
        if abs(boys[i]-girls[j])<=1:
            girls[j]=-1
            ans+=1
            break
print(ans)