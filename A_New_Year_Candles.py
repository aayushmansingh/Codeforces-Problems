a,b=map(int,input().split())
count=0
count+=a
while(a>=b):
    d=a//b
    count+=d
    a=d+(a%b)
print(count)