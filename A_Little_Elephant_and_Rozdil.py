import math
test = 1
# test = int(input())

# for tc in range((test)):
    # Write your code....
n=int(input())
l=list(map(int,input().split()))
if n==1:
    print(1)
    exit(0)
mini=-1
flag=True
mini=min(l)
i=l.index(mini)
j=l.pop(i)
k=min(l)
if mini==k:
    print("Still Rozdil")
    exit(0)
else:
    print(i+1)
    flag==False 

