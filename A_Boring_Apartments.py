import math
test = 1
test = int(input())
def count(num):
    c=0
    while(num>0):
        c+=1
        num//=10
    return c    
for tc in range((test)):
    # Write your code....
    n=int(input())
    dig=count(n)
    print(10*(n%10-1)+((dig*(dig+1))//2))    