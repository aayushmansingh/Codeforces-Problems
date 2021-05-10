n,q=map(int,input().split())
lc=list(map(int,input().split()))
queryno=list(map(int,input().split()))
 
 
s=[0]*55
for i in range(len(lc)):
     if s[lc[i]]==0:
          s[lc[i]]=i+1
 
for i in range(q):
    curr=queryno[i]
    print(s[curr],end=' ')
    for j in range(1,55):
        if s[j]!=0 and s[curr]>s[j]:
            s[j]+=1
    s[curr]=1        