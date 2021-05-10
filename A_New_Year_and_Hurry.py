n,k=map(int,input().split())
total=240
time_problemo=0
pc=0
for i in range(1,n+1):
    time_problemo=5*i
    if time_problemo+k<=240:
        pc+=1
        k+=time_problemo
print(pc)