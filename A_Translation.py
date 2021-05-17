n=input()
r=input()
rev=''
for i in n:
    rev=i+rev
if rev==r:
    print("YES")
else:
    print("NO")