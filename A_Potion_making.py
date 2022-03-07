import math
test = 1
test = int(input())

for tc in range((test)):
    # Write your code....
    k = int(input())
    print(100//math.gcd(k, 100-k))
