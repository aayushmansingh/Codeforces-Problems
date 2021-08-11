l=list(map(int,input().split()))
s=input()
cal=0
for i in range(len(s)):
    if int(s[i]=='1'):
        cal+=l[0]
    elif int(s[i]=='2'):
        cal+=l[1]
    elif int(s[i]=='3'):
        cal+=l[2]
    else:
        cal+=l[3]
print(cal)
