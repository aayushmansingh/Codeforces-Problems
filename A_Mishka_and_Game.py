n=int(input())
mcount,ccount=0,0
for i in range(n):
    m,c=map(int,input().split())
    if m>c:
        mcount+=1
    elif c>m:
        ccount+=1
if mcount>ccount:
    print("Mishka")
elif ccount>mcount:
    print("Chris")
else:
    print("Friendship is magic!^^")