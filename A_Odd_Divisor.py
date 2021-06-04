import math
test = 1
test = int(input())

for tc in range((test)):
    # Write your code....
    n=int(input())
    print("NO" if n&(n-1)==0 else "YES")