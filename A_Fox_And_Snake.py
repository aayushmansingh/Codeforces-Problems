r,c=map(int,input().split())
for i in range(1,r+1):
    if i%2==1:
        print("#"*c)
    else:
        if i%4==0:
            print("#",end='')
            print("."*(c-1))
        if i%4==2:
            print("."*(c-1),end='')
            print("#")
