#Problem Link: https://codeforces.com/problemset/problem/260/A

a,b,n=map(int,input().split())
for i in range(10):
    if (a*10+i)%b==0:
        print(str(a*10+i)+('0'*(n-1)))
        exit(0)
print(-1)
