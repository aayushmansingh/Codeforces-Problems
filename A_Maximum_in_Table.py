n=int(input())
r,c=n,n
def sum(r,c):
    if r==1 or c==1:
        return 1
    return sum(r-1,c)+sum(r,c-1)
print(sum(n,n))