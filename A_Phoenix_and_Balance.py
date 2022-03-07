import math
test = 1
test = int(input())

for tc in range((test)):
    # Write your code....
    n=int(input())
    s1=pow(2,n)
    for i in range(1,n//2):
        s1+=pow(2,i)
    s2=0
    for i in range(n//2,n):
        s2+=pow(2,i)
    print(abs(s2-s1))